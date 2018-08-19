from django.shortcuts import render, redirect
from django.utils.translation import gettext

from .models import Article, ArticleTypeAssociation


def recipesListView(request):
	articleTypeAssociationList = ArticleTypeAssociation.objects.filter(Type__Name='Recipe').all()
	articleList = []
	for obj in articleTypeAssociationList:
		data = obj.Article.LocalData
		if data and data.Released:
			articleList.append(data)
	context = {
		'title': gettext('Recipes') + ' - VegItNow',
		'activeTab': 'recipes',
		'articleList': articleList,
	}
	return render(request=request, template_name='articles/recipes.html', context=context)


def recipeView(request, id, title):
	article = Article.objects.get(id=id).LocalData
	if article is None or not article.Released:
		return redirect('articles:recipesList')
	context = {
		'title': article.Title + ' - VegItNow',
		'article': article,
	}
	return render(request=request, template_name='articles/recipeView.html', context=context)


def tipsListView(request):
	articleTypeAssociationList = ArticleTypeAssociation.objects.filter(Type__Name='Tip').all()
	articleList = []
	for obj in articleTypeAssociationList:
		data = obj.Article.LocalData
		if data and data.Released:
			articleList.append(data)
	context = {
		'title': gettext('Tips') + ' - VegItNow',
		'activeTab': 'tips',
		'articleList': articleList,
	}
	return render(request=request, template_name='articles/tips.html', context=context)


def tipView(request, id, title):
	article = Article.objects.get(id=id).LocalData
	if article is None or not article.Released:
		return redirect('articles:tipsList')
	context = {
		'title': article.Title + ' - VegItNow',
		'article': article,
	}
	return render(request=request, template_name='articles/tipView.html', context=context)
