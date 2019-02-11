from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.decorators.cache import cache_control
from django.views.generic import TemplateView

from general.views import custom404View
from .routers import router

urlpatterns = [
	path('s6AptmegHaGM3Ry5vdlr/database/', admin.site.urls),
	path('api/', include(router.urls)),
	path('summernote/', include('django_summernote.urls')),
	path('service-worker.js', cache_control(max_age=2592000)(TemplateView.as_view(template_name="service-worker.js", content_type='application/javascript', )), name='service-worker.js'),
]

# if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [re_path(r'(?P<path>.*)', TemplateView.as_view(template_name='index.html'))]

urlpatterns += [
	# path('', include(('general.urls', 'general'), namespace='general')),
	# path('login/', include(('login.urls', 'login'), namespace='login')),
	# path('articles/', include(('articles.urls', 'articles'), namespace='articles')),
	# path('shop/', include(('shop.urls', 'shop'), namespace='shop')),
	# path('', include('pwa.urls')),
]


urlpatterns += [
	re_path(r'(?P<path>.*)', custom404View, name='custom404')
]
