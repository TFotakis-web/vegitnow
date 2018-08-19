from django.urls import path

from . import views

urlpatterns = [
	path('', views.homeView, name='home'),
	path('whoWeAre/', views.whoWeAreView, name='whoWeAre'),
	path('communication/', views.communicationView, name='communication'),
	path('setLanguage/<str:language>/', views.setLanguage, name='setLanguage'),
]
