from django.urls import path

from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('recipes/', views.recipes, name='recipes'),
	path('tips/', views.tips, name='tips'),
	path('whoWeAre/', views.whoWeAre, name='whoWeAre'),
	path('communication/', views.communication, name='communication'),
	path('setLanguage/<str:language>/', views.setLanguage, name='setLanguage'),
]
