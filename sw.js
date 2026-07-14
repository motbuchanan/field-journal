/* Field Journal — service worker
 *
 * CACHE VERSION MUST MATCH THE VERSION BADGE IN index.html.
 * Bump it on every deploy or installed devices never see the update.
 */
const VERSION = 'v3.1';
const SHELL   = `field-journal-shell-${VERSION}`;
const PACKS   = `field-journal-packs-${VERSION}`;

// The app itself — safe to cache hard, it's versioned.
const SHELL_FILES = [
  './',
  './index.html',
  './manifest.json',
  './icon.svg',
];

self.addEventListener('install', e => {
  e.waitUntil(
    caches.open(SHELL)
      .then(c => c.addAll(SHELL_FILES))
      .then(() => self.skipWaiting())
  );
});

// Drop every cache that isn't this version.
self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys()
      .then(keys => Promise.all(
        keys.filter(k => k !== SHELL && k !== PACKS)
            .map(k => caches.delete(k))
      ))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', e => {
  const req = e.request;
  if (req.method !== 'GET') return;

  const url = new URL(req.url);
  if (url.origin !== self.location.origin) return;

  // ── Packs: NETWORK FIRST ──────────────────────────────────────
  // New region packs get added to this repo over time. If packs were
  // cache-first, an installed user would be frozen on whatever pack
  // list existed the day they installed. Try the network, fall back
  // to cache so the app still works on a trail with no signal.
  const isPackData = /(^|\/)(packs\.json|pack-[^/]+\.json)$/.test(url.pathname);
  if (isPackData) {
    e.respondWith(
      fetch(req)
        .then(res => {
          if (res && res.ok) {
            const copy = res.clone();
            caches.open(PACKS).then(c => c.put(req, copy));
          }
          return res;
        })
        .catch(() => caches.match(req))
    );
    return;
  }

  // ── App shell: CACHE FIRST, revalidate in background ───────────
  e.respondWith(
    caches.match(req).then(hit => {
      const net = fetch(req).then(res => {
        if (res && res.ok) {
          const copy = res.clone();
          caches.open(SHELL).then(c => c.put(req, copy));
        }
        return res;
      }).catch(() => hit);
      return hit || net;
    })
  );
});
