from django.urls import path

from . import views

urlpatterns = [
	path('', views.homeView, name='home'),
	path('base_layout/', views.base_layout, name='base_layout'),
	path('base_layout', views.base_layout, name='base_layout'),
	path('whoWeAre/', views.whoWeAreView, name='whoWeAre'),
	path('communication/', views.communicationView, name='communication'),
	path('setLanguage/<str:language>/', views.setLanguage, name='setLanguage'),
	path('test/', views.test, name='test'),
]
