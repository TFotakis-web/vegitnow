from django.urls import path

from . import views

urlpatterns = [
	path('recipes/', views.recipesListView, name='recipesList'),
	path('recipes/<int:id>/<str:title>', views.recipeView, name='recipeView'),
	path('tips/', views.tipsListView, name='tipsList'),
	path('tips/<int:id>/<str:title>', views.tipView, name='tipView'),
]
