from django.contrib import admin
from django.urls import path, re_path, include

from general.views import custom_404

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include(('general.urls', 'general'), namespace='general')),
	path('login/', include(('login.urls', 'login'), namespace='login')),
]
urlpatterns += [
	re_path(r'(?P<path>.*)', custom_404, name='custom404')
]
