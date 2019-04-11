from django.http import HttpResponse
from django.shortcuts import render
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from vegitnow.settings import BASE_DIR, CRAWLER_AGENTS


def isCrawler(userAgent=''):
	userAgent = userAgent.lower()
	return any(crawlerAgent in userAgent for crawlerAgent in CRAWLER_AGENTS)


def prerenderSelenium(request):
	url = 'http://' + request.META['HTTP_HOST'] + request.META['PATH_INFO']
	options = Options()
	options.headless = True
	driverExecutablePath = BASE_DIR + '/frontend/node_modules/chromedriver/bin/chromedriver'
	driver = webdriver.Chrome(options=options, executable_path=driverExecutablePath)
	driver.get(url)
	return driver.page_source


def indexView(request):
	if not isCrawler(request.META['HTTP_USER_AGENT']):
		return render(request=request, template_name="index.html")
	html = prerenderSelenium(request)
	return HttpResponse(html)
