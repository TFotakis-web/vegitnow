from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.decorators.cache import cache_control
from django.views.generic import TemplateView

from vegitnow import settings
from .routers import router
from .views import indexView

urlpatterns = [
	path('s6AptmegHaGM3Ry5vdlr/database/', admin.site.urls),
	path('api/', include(router.urls)),
	path('summernote/', include('django_summernote.urls')),
	url(r'^froala_editor/', include('froala_editor.urls')),
	path('service-worker.js', cache_control(max_age=2592000)(TemplateView.as_view(template_name="static/app/js/service-worker.js", content_type='application/javascript', )), name='service-worker.js'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += [re_path(r'(?P<path>.*)', TemplateView.as_view(template_name='index.html'))]
urlpatterns += [re_path(r'^.*', indexView, name='index')]
