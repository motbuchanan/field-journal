# Field Journal — Bird Tracker

A free, offline birding life list and sighting tracker. Installs to your phone,
works with no signal, and keeps every sighting on your own device.

No account. No cloud. No tracking. No ads.

**Live:** https://motbuchanan.github.io/field-journal/

---

## What it does

- Pick your region and get a checklist of the birds that actually occur there
- Mark a species seen, and write field notes on it
- Add any species yourself — vagrants, birds outside the region, anything
- Export your whole list to a file, and restore it later
- Everything saves on-device. Close the browser, it's still there.

## Regions

Region data lives in `packs/`, separate from the app, and loads at runtime.
Sightings are stored under the species *name*, in their own bucket — so
switching regions, or a new pack landing, never touches your list.

| Pack | Species | Source |
|---|---|---|
| Ohio | 269 | eBird checklists, 2015–2026 |
| Start From Scratch | 0 | — |

More regions are in progress. See [`tools/`](tools/) to build one yourself.

---

## Where the data comes from

The species list and the common / uncommon / rare status for each pack are
generated from **eBird bar chart data** — the frequency with which real birders
report each species on real checklists in that region.

This matters. An earlier build of these packs was written from memory and it
was wrong: it listed Common Raven for the Midwest, where the species does not
occur. That's exactly the error a birder spots on sight. The data-driven
pipeline drops the raven automatically, because eBird's Ohio frequency for it
is effectively zero. No memory involved.

For the same reason, body measurements (length, weight, wingspan, lifespan)
are **not** in these packs. They could not be verified at scale, so they were
removed rather than published unverified. Descriptions of plumage, diet,
habitat, and behavior remain — those are qualitative and hand-written.

If you spot an error, open an issue. Birders will find things I didn't.

---

## Install it on your phone

Open the live link in Chrome or Safari, then "Add to Home Screen." It runs
fullscreen and works offline from then on.

## Run it yourself

It's a static site — no build step, no dependencies.

    git clone https://github.com/motbuchanan/field-journal
    cd field-journal
    python3 -m http.server 8000
    # open http://localhost:8000

**Note:** packs load over `fetch()`, which browsers block on `file://` URLs.
Opening `index.html` straight from your file manager will show the
"Start From Scratch" option and a manual pack loader, but not the region
picker. Serve it over HTTP (as above, or via GitHub Pages) for the full app.

---

## Repo layout

    index.html                  the whole app — HTML, CSS and JS in one file
    sw.js                       service worker (cache key must match version badge)
    manifest.json               PWA manifest
    icon.svg

    packs.json                  the pack list the app reads at startup
    pack-ohio.json              269 species, from eBird
    pack-blank.json             empty starter

    build-pack-from-ebird.py    generates a pack from eBird data
    regions.md                  eBird region codes per pack
    species-*.py                hand-written species accounts

Everything sits at the repo root — no subfolders. That's deliberate: GitHub's
web uploader can't take a folder from a phone, only files.

## Contributing a region pack

See [CONTRIBUTING.md](CONTRIBUTING.md). Short version: download an eBird bar
chart for your states, run one script, open a PR.

## License

MIT. Take it, fork it, ship your own.

Bird data derives from [eBird](https://ebird.org), Cornell Lab of Ornithology.
If this tool is useful to you, go contribute checklists — that's what makes the
packs possible.
