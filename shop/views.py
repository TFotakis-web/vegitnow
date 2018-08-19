from django.shortcuts import render
from django.utils.translation import gettext


def homeView(request):
	context = {
		'title': gettext('Shop') + ' - VegItNow',
	}
	return render(request=request, template_name='shop/home.html', context=context)
