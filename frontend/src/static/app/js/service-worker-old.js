var staticCacheName = 'djangopwa-v1';

self.addEventListener('install', function (event) {
	event.waitUntil(
		caches.open(staticCacheName).then(function (cache) {
			return cache.addAll([
				// '/static/css/bootstrap.min.css',
				// '/static/css/fontello.css',
				// '/static/css/animate.css',
				// '/static/css/style.css',
				// '/static/css/colorPalette.css',
				// '/static/font/AC-ScriptCondenced_unicode.ttf',
				// '/static/font/AlegreyaSans/AlegreyaSans-Regular.ttf',
				// '/static/font/fontello.woff',
				// '/static/font/fontello.woff2',
				// '/static/font/fontello.ttf',
				// '/static/js/bootstrap.min.js',
				// '/static/js/jquery-3.3.1.slim.min.js',
				// '/static/js/popper.min.js',
				// '/static/img/logo.png',
				// '/static/img/v.png',
				// '/static/img/karota.png',
				// '/static/img/carouselFava.png',
				// '/manifest.json',
				// '/base_layout',
				'/',
			]);
		})
	);
});

// self.addEventListener('fetch', function (event) {
// 	var requestUrl = new URL(event.request.url);
// 	if (requestUrl.origin === location.origin) {
// 		if ((requestUrl.pathname === '/')) {
// 			event.respondWith(caches.match('/'));
// 			return;
// 		}
// 	}
// 	event.respondWith(
// 		caches.match(event.request).then(function (response) {
// 			return response || fetch(event.request);
// 		})
// 	);
// });

self.addEventListener('fetch', function (event) {
	event.respondWith(
		caches.open(staticCacheName)
			.then(function (cache) {
				return cache.match(event.request)
					.then(function (response) {
						return response || fetch(event.request)
							.then(function (response) {
								cache.put(event.request, response.clone());
								return response;
							});
					});
			})
	);
});

self.addEventListener('fetch', function (event) {
	event.respondWith(
		caches.open(staticCacheName)
			.then(function (cache) {
				return fetch(event.request)
					.then(function (response) {
						cache.put(event.request, response.clone());
						return response;
					});
			})
	);
});
