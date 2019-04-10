console.log("Running");

const staticCacheName = 'vegitnow-static-v2';
const precacheUrls = [
	'/'
];

self.addEventListener('install', event => {
	self.skipWaiting();
	event.waitUntil(
		caches.open(staticCacheName).then(cache => {
			return cache.addAll(precacheUrls);
		})
	);
});

self.addEventListener('activate', event => {
	event.waitUntil(
		caches
			.keys()
			.then(cacheNames => {
				return Promise.all(
					cacheNames
						.filter(cacheName => {
							return cacheName.startsWith('vegitnow-') && cacheName !== staticCacheName;
						})
						.map(cacheName => {
							caches.delete(cacheName);
							console.log('Deleted cache: ', cacheName)
						})
				);
			})
	);
});

self.addEventListener('fetch', event => {
	// console.log('Service worker: ', event.request);
	event.respondWith(
		caches.open(staticCacheName)
			.then(cache => {
				return fetch(event.request)
					.then(function (response) {
						cache.put(event.request, response.clone());
						return response;
					}) || cache.match(event.request);
			})
	)
});
