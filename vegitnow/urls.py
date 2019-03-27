from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.decorators.cache import cache_control
from django.views.generic import TemplateView

from vegitnow import settings
from .routers import router


urlpatterns = [
	path('s6AptmegHaGM3Ry5vdlr/database/', admin.site.urls),
	path('api/', include(router.urls)),
	path('summernote/', include('django_summernote.urls')),
	path('service-worker.js', cache_control(max_age=2592000)(TemplateView.as_view(template_name="service-worker.js", content_type='application/javascript', )), name='service-worker.js'),
	# re_path(r'(?P<path>.*)', TemplateView.as_view(template_name='index.html')),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns.append(re_path(r'(?P<path>.*)', TemplateView.as_view(template_name='index.html')))
