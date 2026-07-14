#!/usr/bin/env python3
"""
build_pack_from_ebird.py — generate an authoritative region pack.

WHY THIS EXISTS
---------------
An earlier version of these packs had the species lists and regional
status written from memory. That approach put birds in regions they
don't live in. This script replaces guesswork with eBird's own data:
the species list and the frequency come from real checklists submitted
by real birders, which is the same source Merlin's packs use.

WHAT YOU NEED
-------------
An eBird bar chart export for the region. To get one:

  1. Go to  https://ebird.org/barchart?r=US-OH        (swap in your region)
     Multiple states:  https://ebird.org/barchart?r=US-OH,US-MI,US-IN
  2. Set the date range (use all years for a full picture).
  3. Click "Download Histogram Data" — you get a .txt/.tsv file.

USAGE
-----
  python3 build_pack_from_ebird.py \
      --input   ebird_US-OH__1900_2026_1_12_barchart.txt \
      --id      midwest \
      --name    "Midwest" \
      --subtitle "Ohio Valley, Great Plains & prairie states" \
      --min-freq 0.005 \
      --out     ../packs/midwest.json

FREQUENCY -> STATUS
-------------------
eBird frequency = the fraction of checklists in that region reporting
the species. We map peak weekly frequency to the app's three statuses:

    >= 0.20   common       (on 1 in 5 checklists or better)
    >= 0.02   uncommon
    <  0.02   rare

--min-freq drops true vagrants so a pack doesn't balloon with birds
nobody will see. 0.005 (one checklist in 200) is a sane default.
"""
import argparse, csv, json, os, re, sys

# ── Qualitative species notes (plumage, diet, habitat, behavior) ──
# These are descriptive, not numeric, and are merged in where available.
# A species with no entry here still ships — it just gets no prose.
def load_descriptions():
    here = os.path.dirname(os.path.abspath(__file__))
    ns = {}
    for f in sorted(os.listdir(here)):
        if re.match(r'species-\d+-.*\.py$', f):
            exec(open(os.path.join(here, f)).read(), ns)
    out = {}
    for sp in ns.get('SPECIES', []):
        out[sp['name'].lower()] = {
            'emoji':   sp['emoji'],
            'tags':    sp['tags'],
            'about':   sp['about'],
            'male':    sp['male'],
            'female':  sp['female'],
            'diet':    sp['diet'],
            'habitat': sp['habitat'],
        }
    return out

# ── Grouping ─────────────────────────────────────────────────────
# The bar chart export carries no taxonomic order, so we key off the
# family word in the common name. North American bird names are highly
# regular this way ("...Duck", "...Hawk", "...Woodpecker"), which beats
# dumping every unwritten species into "songbird".
WATER_WORDS = (
    'duck','goose','geese','swan','teal','merganser','scaup','wigeon','pintail',
    'shoveler','gadwall','redhead','canvasback','bufflehead','goldeneye','scoter',
    'eider','mallard','brant','loon','grebe','cormorant','pelican','anhinga',
    'heron','egret','bittern','ibis','spoonbill','stork','rail','coot','gallinule',
    'moorhen','crane','limpkin','plover','killdeer','sandpiper','yellowlegs',
    'dowitcher','snipe','phalarope','godwit','curlew','whimbrel','turnstone',
    'dunlin','sanderling','knot','ruff','willet','avocet','stilt','oystercatcher',
    'gull','tern','skimmer','jaeger','kittiwake','woodcock',
)
RAPTOR_WORDS = (
    'hawk','eagle','falcon','kestrel','merlin','harrier','osprey','vulture',
    'owl','kite','goshawk','caracara','condor',
)
WOODPECKER_WORDS = ('woodpecker','sapsucker','flicker')

# ── Emoji by family ───────────────────────────────────────────────
# Without this, every species the eBird export brings in that has no
# written account renders as the same generic bird, and a list of 269
# identical icons is useless to scan.
EMOJI_RULES = [
    (('goose','geese','brant'),                                          '🪿'),
    (('swan',),                                                          '🦢'),
    (('duck','teal','merganser','scaup','wigeon','pintail','shoveler',
      'gadwall','redhead','canvasback','bufflehead','goldeneye','scoter',
      'eider','mallard','bufflehead'),                                   '🦆'),
    (('grebe','loon','cormorant','pelican','anhinga','coot'),            '🦆'),
    (('heron','egret','bittern','crane','ibis','spoonbill','stork'),     '🦩'),
    (('gull','tern','skimmer','kittiwake','jaeger'),                     '🕊️'),
    (('dove','pigeon'),                                                  '🕊️'),
    (('owl',),                                                           '🦉'),
    (('hawk','eagle','falcon','kestrel','merlin','harrier','osprey',
      'vulture','kite','goshawk','caracara','condor'),                   '🦅'),
    (('turkey',),                                                        '🦃'),
    (('quail','pheasant','grouse','bobwhite','prairie-chicken',
      'ptarmigan'),                                                      '🐓'),
]

def emoji_for(name):
    toks = set(re.split(r"[\s\-]+", name.lower()))
    for words, glyph in EMOJI_RULES:
        if toks & set(words):
            return glyph
    return '🐦'

def group_for(name):
    # Tokenize on spaces AND hyphens, then match whole words only.
    # Substring matching is a trap here: "Yellowlegs" contains "owl",
    # and "Nighthawk" contains "hawk" but is not a raptor.
    toks = set(re.split(r"[\s\-]+", name.lower()))
    if toks & set(WOODPECKER_WORDS): return 'woodpecker'
    if toks & set(RAPTOR_WORDS):     return 'raptor'
    if toks & set(WATER_WORDS):      return 'waterfowl'
    return 'songbird'

def status_for(freq):
    if freq >= 0.20: return 'common'
    if freq >= 0.02: return 'uncommon'
    return 'rare'

def parse_barchart(path):
    """
    eBird histogram export is tab-separated: a preamble, a "Sample Size:"
    row giving the number of complete checklists per week, then one row
    per taxon with 48 frequency values (4 bins per month).

    Frequency = share of complete checklists reporting that species.
    We take each species' PEAK weekly value — how findable it is at its
    best time of year — and also return the mean sample size so several
    states can be merged with correct weighting.
    """
    rows, sample = [], 0.0
    with open(path, encoding='utf-8', errors='replace') as fh:
        for line in fh:
            parts = line.rstrip('\n').split('\t')
            if len(parts) < 10:
                continue
            name = parts[0].strip()
            vals = []
            for p in parts[1:]:
                try:
                    vals.append(float(p))
                except ValueError:
                    pass
            if name.lower().startswith('sample size'):
                if vals:
                    sample = sum(vals) / len(vals)
                continue
            if not name:
                continue
            if len(vals) >= 40:
                rows.append((name, max(vals)))
    return rows, (sample or 1.0)


def merge_regions(paths):
    """
    Combine several state exports into one regional frequency.

    A species on 40% of Ohio lists and 2% of Kansas lists is not 21%
    region-wide — it depends how many checklists each state contributes.
    So we weight each state's frequency by its checklist sample size.
    A species absent from a state contributes a real zero for that state,
    which is what stops a locally-common bird from looking region-wide.
    """
    per_state, weights = [], []
    for p in paths:
        rows, sample = parse_barchart(p)
        per_state.append(dict(rows))
        weights.append(sample)

    total_w = sum(weights) or 1.0
    all_names = set()
    for d in per_state:
        all_names |= set(d)

    merged = {}
    for name in all_names:
        acc = 0.0
        for d, w in zip(per_state, weights):
            acc += d.get(name, 0.0) * w      # absent -> 0, and that counts
        merged[name] = acc / total_w
    return sorted(merged.items())

QUALIFIERS = ('northern','southern','eastern','western','american','common')

def match_key(name):
    """
    Normalize for looking up a written account.
    eBird taxonomy adds directional qualifiers when it splits a species;
    'Northern House Wren' should still find the 'House Wren' account.
    """
    words = name.lower().replace("'s", '').split()
    while len(words) > 1 and words[0] in QUALIFIERS:
        words = words[1:]
    return ' '.join(words)


def clean_name(raw):
    """
    Drop eBird's non-species taxa. Slashes ('Greater/Lesser Scaup'),
    'sp.' entries, hybrids, and subspecies groups in parentheses are
    not things a life list should track as species.
    """
    if '/' in raw or ' sp.' in raw or ' x ' in raw.lower():
        return None
    return re.sub(r'\s*\([^)]*\)', '', raw).strip()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--input', required=True, nargs='+',
                    help='One or more eBird bar chart exports (one per state)')
    ap.add_argument('--id', required=True)
    ap.add_argument('--name', required=True)
    ap.add_argument('--subtitle', default='')
    ap.add_argument('--min-freq', type=float, default=0.005)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()

    for p in a.input:
        if not os.path.exists(p):
            sys.exit(f'No such file: {p}')

    desc = load_descriptions()
    # index the written accounts under BOTH their literal and normalized keys
    desc_by_key = {}
    for k, v in desc.items():
        desc_by_key.setdefault(k, v)
        desc_by_key.setdefault(match_key(k), v)
    seen, species = set(), []
    dropped_vagrant = dropped_taxon = 0

    for raw, freq in merge_regions(a.input):
        name = clean_name(raw)
        if not name:
            dropped_taxon += 1
            continue
        if freq < a.min_freq:
            dropped_vagrant += 1
            continue
        if name.lower() in seen:
            continue
        seen.add(name.lower())

        d = desc_by_key.get(name.lower()) or desc_by_key.get(match_key(name)) or {}
        acct_emoji = d.get('emoji')
        entry = {
            'name':   name,
            'emoji':  acct_emoji if (acct_emoji and acct_emoji != '🐦') else emoji_for(name),
            'status': status_for(freq),
            'freq':   round(freq * 100),          # 0-100 for the app's bar
            'tags':   d.get('tags') or [group_for(name)],
            'region': f'Reported on {freq*100:.1f}% of {a.name} checklists at peak season (eBird).',
        }
        for k in ('about', 'male', 'female', 'diet', 'habitat'):
            if d.get(k):
                entry[k] = d[k]
        species.append(entry)

    order = {'waterfowl': 0, 'raptor': 1, 'woodpecker': 2, 'songbird': 3}
    species.sort(key=lambda s: (order.get(s['tags'][0], 9), -s['freq'], s['name']))

    pack = {
        'id': a.id, 'name': a.name, 'subtitle': a.subtitle,
        'schema': 1, 'speciesCount': len(species),
        'source': 'Species list and frequency from eBird bar chart data.',
        'species': species,
    }
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    with open(a.out, 'w') as fh:
        json.dump(pack, fh, indent=1)

    withprose = sum(1 for s in species if 'about' in s)
    print(f'{a.out}')
    print(f'  merged {len(a.input)} state export(s), weighted by checklist volume')
    print(f'  {len(species)} species  ({withprose} with written accounts)')
    print(f'  dropped {dropped_vagrant} below min-freq, {dropped_taxon} non-species taxa')

if __name__ == '__main__':
    main()
