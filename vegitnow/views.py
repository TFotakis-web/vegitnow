import json
import time

import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse
from django.shortcuts import render

from vegitnow.settings import BASE_DIR, CRAWLER_AGENTS


# def prerenderSelenium(request):
# 	from selenium import webdriver
# 	from selenium.webdriver.chrome.options import Options
# 	from selenium.webdriver.firefox.options import Options
# 	url = request.scheme + '://' + request.META['HTTP_HOST'] + request.META['PATH_INFO']
# 	options = Options()
# 	options.headless = True
# 	driverExecutablePath = BASE_DIR + '/frontend/node_modules/geckodriver/geckodriver'
# 	# driverExecutablePath = BASE_DIR + '/frontend/node_modules/chromedriver/lib/chromedriver/chromedriver'
# 	# driverExecutablePath = '/lib/chromium/chromedriver'
# 	# driverExecutablePath = '/home/tzanis/Downloads/chromium/chromedriver'
# 	# driverExecutablePath = '/home/tzanis/Workspace/PyCharm/vegitnow/frontend/node_modules/chrome-driver-standalone/binaries/chromedriver_linux64'
#
# 	# driverBinary = BASE_DIR + '/frontend/node_modules/chromium-binary/lib/chromium/chrome-linux/chromium'
# 	# driverBinary = '/lib/chromium/chromium'
# 	# driverBinary = '/home/tzanis/Downloads/chromium/chromium'
# 	# driverBinary = '/home/tzanis/Workspace/PyCharm/vegitnow/frontend/node_modules/chromium/lib/chromium/chrome-linux/chrome'
# 	# driverBinary = '/home/vegitno1/vegitnowPublic/vegitnow/frontend/node_modules/chromium/lib/chromium/chrome-linux/chrome'
# 	driverBinary = '/home/tzanis/Workspace/PyCharm/vegitnow/frontend/node_modules/get-firefox/bin/firefox/firefox'
#
# 	options.binary_location = driverBinary
#
# 	options.add_argument('--no-sandbox')
#
# 	# options.experimental_options["prefs"] = {
# 	# 	"profile.default_content_settings": {"images": 2},
# 	# 	"profile.managed_default_content_settings": {"images": 2}
# 	# }
# 	#
# 	options.preferences["browser.tabs.remote.autostart"] = False
#
# 	driver = webdriver.Firefox(options=options, executable_path=driverExecutablePath)
# 	# driver = webdriver.Chrome(options=options, executable_path=driverExecutablePath)
# 	driver.get(url)
# 	print('Got it')
# 	count = 0
# 	time.sleep(0.5)
# 	while count < 200 and (driver.find_element_by_id('metaDescription').get_attribute('content') == 'undefined' or driver.find_element_by_id('metaTitle').text == 'VegItNow'):
# 		print('Sleeping')
# 		time.sleep(0.1)
# 		count += 1
# 	html = driver.page_source
#
# 	driver.close()
# 	return html


def patchHTML(request, elementAttributes):
	# url = request.scheme + '://' + request.META['HTTP_HOST'] + request.META['PATH_INFO']
	# src = requests.get(url)
	# soup = BeautifulSoup(src.text, features='html.parser')
	src = render(request=request, template_name="index.html").content
	soup = BeautifulSoup(src, features='html.parser')
	head = soup.head

	for elementId in elementAttributes.keys():
		if elementId == 'metaTitle':
			element = head.select_one('#' + elementId)
			if element:
				element.string = elementAttributes[elementId]['content'] + ' | ' + element.string
			continue
		for attribute in elementAttributes[elementId].keys():
			value = elementAttributes[elementId][attribute]
			element = head.select_one('#' + elementId)
			if element:
				element.attrs[attribute] = value
	html = str(soup)
	return html


def prerenderDjango(request):
	elementAttributes = {}
	url = request.path.split('/')[1:]
	if url[0] == '':
		elementAttributes = {
			'metaTitle': {'content': 'Αρχική'},
			# 'metaDescription': {'content': ''},
			# 'metaKeywords': {'content': ''},
			'metaGooglePlusName': {'content': 'Αρχική'},
			# 'metaGooglePlusDescription': {'content': ''},
			# 'metaGooglePlusImage': {'content': ''},
			# 'metaTwitterCard': {'content': ''},
			# 'metaTwitterSite': {'content': ''},
			'metaTwitterTitle': {'content': 'Αρχική'},
			# 'metaTwitterDescription': {'content': ''},
			# 'metaTwitterCreator': {'content': ''},
			# 'metaTwitterImage': {'content': ''},
			'metaOpenGraphTitle': {'content': 'Αρχική'},
			# 'metaOpenGraphType': {'content': 'article'},
			# 'metaOpenGraphUrl': {'content': ''},
			# 'metaOpenGraphImage': {'content': ''},
			# 'metaOpenGraphDescription': {'content': ''},
			# 'metaOpenGraphSiteName': {'content': ''},
			# 'metaOpenGraphPublishedTime': {'content': ''},
			# 'metaOpenGraphModifiedTime': {'content': ''},
			# 'metaOpenGraphSection': {'content': ''},
			# 'metaOpenGraphTag': {'content': ''},
			# 'metaOpenGraphAdmins': {'content': ''}
		}
	elif url[0] == 'staticPage':
		uri = request.scheme + '://' + request.get_host() + '/api' + request.path + '/?locale=2'
		response = json.loads(requests.get(uri).text)
		preview = BeautifulSoup(response['Content'], 'html.parser').text
		preview = (preview[:150] if len(preview) > 150 else preview) + '...'
		elementAttributes = {
			'metaTitle': {'content': response['Name']},
			'metaDescription': {'content': preview},
			# 'metaKeywords': {'content': ''},
			'metaGooglePlusName': {'content': response['Name']},
			'metaGooglePlusDescription': {'content': preview},
			# 'metaGooglePlusImage': {'content': ''},
			# 'metaTwitterCard': {'content': ''},
			# 'metaTwitterSite': {'content': ''},
			'metaTwitterTitle': {'content': response['Name']},
			'metaTwitterDescription': {'content': preview},
			# 'metaTwitterCreator': {'content': ''},
			# 'metaTwitterImage': {'content': ''},
			'metaOpenGraphTitle': {'content': response['Name']},
			# 'metaOpenGraphType': {'content': 'article'},
			'metaOpenGraphUrl': {'content': request.get_raw_uri()},
			# 'metaOpenGraphImage': {'content': ''},
			'metaOpenGraphDescription': {'content': preview},
			# 'metaOpenGraphSiteName': {'content': ''},
			# 'metaOpenGraphPublishedTime': {'content': ''},
			# 'metaOpenGraphModifiedTime': {'content': ''},
			# 'metaOpenGraphSection': {'content': ''},
			# 'metaOpenGraphTag': {'content': ''},
			# 'metaOpenGraphAdmins': {'content': ''}
		}
	elif url[0] == 'articles' and len(url) == 1:
		elementAttributes = {
			'metaTitle': {'content': 'Άρθρα'},
			# 'metaDescription': {'content': ''},
			# 'metaKeywords': {'content': ''},
			'metaGooglePlusName': {'content': 'Άρθρα'},
			# 'metaGooglePlusDescription': {'content': ''},
			# 'metaGooglePlusImage': {'content': ''},
			# 'metaTwitterCard': {'content': ''},
			# 'metaTwitterSite': {'content': ''},
			'metaTwitterTitle': {'content': 'Άρθρα'},
			# 'metaTwitterDescription': {'content': ''},
			# 'metaTwitterCreator': {'content': ''},
			# 'metaTwitterImage': {'content': ''},
			'metaOpenGraphTitle': {'content': 'Άρθρα'},
			# 'metaOpenGraphType': {'content': 'article'},
			# 'metaOpenGraphUrl': {'content': ''},
			# 'metaOpenGraphImage': {'content': ''},
			# 'metaOpenGraphDescription': {'content': ''},
			# 'metaOpenGraphSiteName': {'content': ''},
			# 'metaOpenGraphPublishedTime': {'content': ''},
			# 'metaOpenGraphModifiedTime': {'content': ''},
			# 'metaOpenGraphSection': {'content': ''},
			# 'metaOpenGraphTag': {'content': ''},
			# 'metaOpenGraphAdmins': {'content': ''}
		}
	elif url[0] == 'recipes' and len(url) == 1:
		elementAttributes = {
			'metaTitle': {'content': 'Συνταγές'},
			# 'metaDescription': {'content': ''},
			# 'metaKeywords': {'content': ''},
			'metaGooglePlusName': {'content': 'Συνταγές'},
			# 'metaGooglePlusDescription': {'content': ''},
			# 'metaGooglePlusImage': {'content': ''},
			# 'metaTwitterCard': {'content': ''},
			# 'metaTwitterSite': {'content': ''},
			'metaTwitterTitle': {'content': 'Συνταγές'},
			# 'metaTwitterDescription': {'content': ''},
			# 'metaTwitterCreator': {'content': ''},
			# 'metaTwitterImage': {'content': ''},
			'metaOpenGraphTitle': {'content': 'Συνταγές'},
			# 'metaOpenGraphType': {'content': 'article'},
			# 'metaOpenGraphUrl': {'content': ''},
			# 'metaOpenGraphImage': {'content': ''},
			# 'metaOpenGraphDescription': {'content': ''},
			# 'metaOpenGraphSiteName': {'content': ''},
			# 'metaOpenGraphPublishedTime': {'content': ''},
			# 'metaOpenGraphModifiedTime': {'content': ''},
			# 'metaOpenGraphSection': {'content': ''},
			# 'metaOpenGraphTag': {'content': ''},
			# 'metaOpenGraphAdmins': {'content': ''}
		}
	elif (url[0] == 'articles' or url[0] == 'recipes') and len(url) == 2:
		uri = request.scheme + '://' + request.get_host() + '/api/article/' + url[1] + '/?locale=2'
		response = json.loads(requests.get(uri).text)
		imageUrl = request.scheme + '://' + request.get_host() + response['Thumbnail']
		elementAttributes = {
			'metaTitle': {'content': response['Title']},
			'metaDescription': {'content': response['Preview']},
			# 'metaKeywords': {'content': ''},
			'metaGooglePlusName': {'content': response['Title']},
			'metaGooglePlusDescription': {'content': response['Preview']},
			'metaGooglePlusImage': {'content': imageUrl},
			# 'metaTwitterCard': {'content': ''},
			# 'metaTwitterSite': {'content': ''},
			'metaTwitterTitle': {'content': response['Title']},
			'metaTwitterDescription': {'content': response['Preview']},
			# 'metaTwitterCreator': {'content': ''},
			'metaTwitterImage': {'content': imageUrl},
			'metaOpenGraphTitle': {'content': response['Title']},
			# 'metaOpenGraphType': {'content': 'article'},
			'metaOpenGraphUrl': {'content': request.get_raw_uri()},
			'metaOpenGraphImage': {'content': imageUrl},
			'metaOpenGraphDescription': {'content': response['Preview']},
			# 'metaOpenGraphSiteName': {'content': ''},
			# 'metaOpenGraphPublishedTime': {'content': ''},
			# 'metaOpenGraphModifiedTime': {'content': ''},
			# 'metaOpenGraphSection': {'content': ''},
			# 'metaOpenGraphTag': {'content': ''},
			# 'metaOpenGraphAdmins': {'content': ''}
		}
	return patchHTML(request, elementAttributes)


def isCrawler(userAgent=''):
	userAgent = userAgent.lower()
	return any(crawlerAgent in userAgent for crawlerAgent in CRAWLER_AGENTS)


def indexView(request):
	if not isCrawler(request.META['HTTP_USER_AGENT']):
		return render(request=request, template_name="index.html")
	# html = prerenderSelenium(request)
	html = prerenderDjango(request)
	return HttpResponse(html)
