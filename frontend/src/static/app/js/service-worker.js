/**
 * Service Worker version 20190713
 */

let today = new Date();
let timestamp = today.getFullYear().toString();
timestamp += (today.getMonth() < 8 ? '0' : '') + (today.getMonth() + 1).toString();
timestamp += today.getDate().toString();

const staticCacheName = 'static-' + timestamp;
const mediaCacheName = 'media-20190813';
const apiCacheName = 'api-' + timestamp;
const cacheWhitelist = [staticCacheName, mediaCacheName, apiCacheName];

const precacheUrls = [
	'/'
];

if (typeof self.skipWaiting === 'function') {
	self.addEventListener('install', function (e) {
		e.waitUntil(self.skipWaiting());
	});
}

self.addEventListener('activate', function (e) {
	if (self.clients && (typeof self.clients.claim === 'function')) {
		// self.clients.claim();
		e.waitUntil(self.clients.claim());
	}
	e.waitUntil(
		caches.keys().then(function (cacheNames) {
			return Promise.all(
				cacheNames.map(function (cacheName) {
					if (cacheWhitelist.indexOf(cacheName) === -1) {
						caches.delete(cacheName);
						// console.log('Deleted cache: ', cacheName);
					}
				})
			);
		})
	);
	e.waitUntil(
		caches.open(staticCacheName).then(cache => {
			return cache.addAll(precacheUrls);
		})
	);
});

let networkFirst = function (event, cacheToUse) {
	event.respondWith(
		fetch(event.request)
			.then(function (response) {
				if (!response || response.status !== 200 || response.type !== 'basic') return response;

				let responseClone = response.clone();
				caches.open(cacheToUse)
					.then(function (cache) {
						cache.put(event.request, responseClone);
					});
				return response;
			})
			.catch(function () {
				return caches.open(cacheToUse)
					.then(function (cache) {
						return cache.match(event.request);
					});
			})
	);
};

let cacheFirst = function (event, cacheToUse) {
	event.respondWith(
		caches.open(cacheToUse)
			.then(function (cache) {
				return cache.match(event.request)
					.then(function (response) {
						return response ||
							fetch(event.request)
								.then(function (response) {
										if (!response || response.status !== 200 || response.type !== 'basic') return response;

										cache.put(event.request, response.clone());
										return response;
									}
								);
					});
			})
	);
};

self.addEventListener('fetch', event => {
	const requestURL = new URL(event.request.url);
	if (self.location.origin !== requestURL.origin) return;
	else if (/^\/__webpack_hmr/.test(requestURL.pathname)) return;
	else if (/^\/s6AptmegHaGM3Ry5vdlr\/database\//.test(requestURL.pathname)) return;
	else if (/^\/summernote\//.test(requestURL.pathname)) return;
	else if (/^\/static\//.test(requestURL.pathname)) cacheFirst(event, staticCacheName);
	else if (/^\/media\//.test(requestURL.pathname)) cacheFirst(event, mediaCacheName);
	else if (/^\/api\//.test(requestURL.pathname)) networkFirst(event, apiCacheName);
	else {
		let requestRoot = new Request('/');
		let cacheToUse = staticCacheName;
		event.respondWith(
			fetch(requestRoot)
				.then(function (response) {
					if (!response || response.status !== 200 || response.type !== 'basic') return response;

					let responseClone = response.clone();
					caches.open(cacheToUse)
						.then(function (cache) {
							cache.put(requestRoot, responseClone);
						});
					return response;
				})
				.catch(function () {
					return caches.open(cacheToUse)
						.then(function (cache) {
							return cache.match(requestRoot);
						});
				})
		);
	}
});
