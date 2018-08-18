from django.urls import path

from . import views

urlpatterns = [
	path('', views.LoginFormView.as_view(), name='login'),
	path('register/', views.RegisterFormView.as_view(), name='register'),
	path('logout/', views.logoutView, name='logout'),
]
