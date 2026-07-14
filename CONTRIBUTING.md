# Adding a region pack

You do not need to know how to code. You need an eBird account and about
ten minutes.

## 1. Download the data

For each state in your region:

1. Log in to eBird.
2. Go to `https://ebird.org/barchart?r=US-OH` (swap `US-OH` for your state).
3. Click **Change Date**. Set **Entire Year**, and years **2015 to now**.

   Don't use 1900. Bird ranges have shifted — cardinals moved north, ravens
   returned to the Northeast, collared-doves arrived in the 90s. A century-wide
   window blends today's distribution with a century of obsolete ones.

4. Scroll to the very bottom. Click **Download Histogram Data**.
5. It saves as a `.txt` file. Leave it alone — don't open it in Excel, don't
   rename it. The script reads it as-is.

State codes for each region are in [regions.md](regions.md).

## 2. Build the pack

    python3 build-pack-from-ebird.py \
        --input ~/Downloads/ebird_US-OH_*.txt \
        --id ohio \
        --name "Ohio" \
        --subtitle "269 species — from eBird checklists" \
        --min-freq 0.005 \
        --out pack-ohio.json

Multiple states in one region? Pass them all:

    python3 build-pack-from-ebird.py \
        --input ~/Downloads/ebird_US-OH*.txt ~/Downloads/ebird_US-MI*.txt \
        --id midwest --name "Midwest" --out pack-midwest.json

Each state is weighted by how many checklists it contributes. A species on
30% of Kansas lists but absent from heavily-birded Ohio comes out *uncommon*
region-wide, not common — which is correct.

## 3. Register it

Add an entry to `packs.json`:

    {
      "id": "ohio",
      "name": "Ohio",
      "subtitle": "269 species — from eBird checklists",
      "speciesCount": 269,
      "file": "pack-ohio.json",
      "status": "available"
    }

## 4. Bump the version

Two places, and they **must match**, or installed phones never see the update:

- the version badge in `index.html`
- `const VERSION` in `sw.js`

## 5. Open a PR

---

## How status is decided

eBird frequency is the share of complete checklists reporting the species.
Peak weekly value maps to:

| Frequency | Status |
|---|---|
| ≥ 20% | common |
| ≥ 2%  | uncommon |
| < 2%  | rare |

`--min-freq` (default 0.005, i.e. 1 checklist in 200) drops true vagrants so
a pack doesn't fill up with birds nobody will see.

## Writing species accounts

`species-*.py` holds the hand-written accounts — plumage, diet,
habitat, behavior. A species with no account still ships; it just gets a
name, a status and a frequency. Adding one is a single `S(...)` call.

**Do not add measurements.** Length, weight, wingspan and lifespan were
deliberately removed from this project because they could not be verified at
scale. If you want them back, bring a citable source.
