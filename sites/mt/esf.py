import re
from urllib.error import HTTPError
from urllib.parse import urlparse
from urllib.request import urlopen

from bs4 import BeautifulSoup

import services.store as store
import utils.extention as ext
from core.models.pageContent import pageContent
from utils.extention import splitAddress

allContentLinks = set()

def crawler(config):
	
	print('抓取麦田二手房信息-开始')

    #抓取页数
	size = 1 
	i = 1

	while i < size + 1:
		url = 'http://fz.maitian.cn/esfall/PG' + str(i)
		getAllContentLinks(url)
		i = i + 1

	for url in allContentLinks:
		page = getPageContent(url)
		if page is not None:
			print(page.title)
			store.save(config, page)
			
	print('抓取麦田二手房信息-结束')

def getAllContentLinks(siteUrl):
	html = urlopen(siteUrl)
	bsObj = BeautifulSoup(html.read(), 'html5lib')
	content = bsObj.find('div', {'class': 'list_wrap'})

	if content is not None:
		internalLinks = ext.getInternalLinks(content, splitAddress(siteUrl)[0])
		for link in internalLinks:
			link = str(link).strip()
			link = link.replace('://', 'http://fz.maitian.cn')
			if (link not in allContentLinks and link != ''):
				print(link)
				allContentLinks.add(link)

def getPageContent(url):

	html = None

	try:
		html = urlopen(url)
	except HTTPError as e:
		print('http vistor error')
	except Exception as e:
		print('load fail')

	return parseHtml(url, html)

def parseHtml(url, html):

	if html is None:
		print('链接:' + url + ' 内容页为空')
		return
	if html.msg != 'OK':
		print('链接:' + url + ' 访问错误:' + html.msg)
		return

	bsObj = BeautifulSoup(html, 'html5lib')
	
	title = '无标题'
	
	try:
		title = bsObj.find('h3', {'class': 'xq_name'}).get_text()
	except:
		print('链接: ' + url + ' 获取标题失败')
		
	content = bsObj.find('article', {'class': 'whiteBg pr'})
	author = bsObj.find('p', {'class': 'xq_muster_info'})
	
	if author is not None:
		author = author.find('a')
	
	cover = ''

	if content is None:
		print('链接:' + url + ' 内容为空')
		return
	else:
		
		images = content.findAll('img')
		
		try:
			
			for image in images:
				image['src'] = image['src']
				
			cover = content.findAll('img')[1]['src']
			
		except:
			print('链接:' + url + ' 格式有误')
			
		content = str(content)

	if author is not None:
		author = '麦田-' + author.get_text()

	page = pageContent(title, content, author, '房产', cover)

	return page
