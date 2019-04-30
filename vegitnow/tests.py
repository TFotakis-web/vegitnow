import asyncio

from django.http import HttpResponse
from django.shortcuts import render
from requests_html import AsyncHTMLSession, HTMLSession


async def aprerenderPage(url):
	# resp = HTMLSession().get(url)
	resp = await AsyncHTMLSession().get(url)
	# await resp.html.arender()
	await resp.html.render()
	html = resp.html.html
	return html


def prerenderPage(url):
	resp = HTMLSession().get(url)
	resp.html.render()
	html = resp.html.html
	return html


def prerenderPyppeteer(url):
	from pyppeteer import launch
	loop = asyncio.new_event_loop()
	asyncio.set_event_loop(loop)
	loop.set_debug(True)
	browser = loop.run_until_complete(launch(args=['no-sandbox']))
	pg = browser.newPage()
	loop.run_until_complete(pg.goto(url))


def prerenderSelenium(url):
	from selenium import webdriver
	from selenium.webdriver.chrome.options import Options
	options = Options()
	options.headless = True
	driver = webdriver.Chrome(options=options)
	driver.get(url)
	return driver.page_source


def main():
	url = "http://localhost:8000/recipes/1"
	# html = asyncio.run(prerenderPage(url))

	# resp = HTMLSession().get(url)
	# resp.html.render()
	# html = resp.html.html

	# html = prerenderPage(url)
	# html = prerenderPyppeteer(url)
	html = prerenderSelenium(url)
	print(html)


main()
