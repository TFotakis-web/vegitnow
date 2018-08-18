from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import translation
from django.utils.translation import gettext


def home(request):
	context = {
		'title': 'VegItNow',
	}
	return render(request=request, template_name='general/home.html', context=context)


def recipes(request):
	context = {
		'title': gettext('Recipes') + ' - VegItNow',
		'activeTab': 'recipes',
	}
	return render(request=request, template_name='general/recipes.html', context=context)


def tips(request):
	context = {
		'title': gettext('Tips') + ' - VegItNow',
		'activeTab': 'tips',
	}
	return render(request=request, template_name='general/tips.html', context=context)


def whoWeAre(request):
	context = {
		'title': gettext('Who we are') + ' - VegItNow',
		'activeTab': 'whoWeAre',
	}
	return render(request=request, template_name='general/whoWeAre.html', context=context)


def communication(request):
	context = {
		'title': gettext('Communication') + ' - VegItNow',
		'activeTab': 'communication',
	}
	return render(request=request, template_name='general/communication.html', context=context)


def custom_404(request, path):
	context = {
		'title': 'Oops! Error 404. - VegItNow'
	}
	return render(request=request, template_name='Shared/404.html', context=context)


def custom_500(request):
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
