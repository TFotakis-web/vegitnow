from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include
# from django.views.decorators.cache import cache_control
from django.views.generic import TemplateView

from vegitnow import settings
from .routers import router

urlpatterns = [
	path('s6AptmegHaGM3Ry5vdlr/database/', admin.site.urls),
	path('api/', include(router.urls)),
	path('summernote/', include('django_summernote.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [re_path(r'(?P<path>.*)', TemplateView.as_view(template_name='index.html'))]
