from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import translation
from django.utils.translation import gettext

from articles.models import recommendedArticles, recommendedRecipes, homePageArticles


def homeView(request):
	context = {
		'title': 'VegItNow',
		'carouselArticles': homePageArticles(),
		'recommendedRecipes': recommendedRecipes(),
		'recommendedArticles': recommendedArticles(),
	}
	return render(request=request, template_name='general/home.html', context=context)


def whoWeAreView(request):
	context = {
		'title': gettext('Who we are') + ' - VegItNow',
		'activeTab': 'whoWeAre',
	}
	return render(request=request, template_name='general/whoWeAre.html', context=context)


def communicationView(request):
	context = {
		'title': gettext('Communication') + ' - VegItNow',
		'activeTab': 'communication',
	}
	return render(request=request, template_name='general/communication.html', context=context)


def custom404View(request, path):
	context = {
		'title': 'Oops! Error 404. - VegItNow'
	}
	return render(request=request, template_name='Shared/404.html', context=context)


def custom500View(request):
	context = {
		'title': 'Oops! Error 500. - VegItNow'
	}
	return render(request=request, template_name='Shared/500.html', context=context)


def setLanguage(request, language):
	translation.activate(language)
	referer = request.META.get('HTTP_REFERER')
	response = HttpResponseRedirect(referer)
	response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
	return response


def base_layout(request):
	return render(request=request, template_name='Base/base.html')


def test(request):
	return render(request=request, template_name='general/test.html')
