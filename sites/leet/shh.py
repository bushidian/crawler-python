from urllib.request import urlopen
from urllib.parse import urlparse
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re

import utils.extention as ext
import services.store as store
from utils.extention import splitAddress
from core.models.pageContent import pageContent

allContentLinks = set()

def crawler(config):
	
	print('抓取骊特二手房信息-开始')
	
	#抓取页数
	size = 1 
	i = 1
	
	while i < size + 1:
		url = 'http://fuzhou.leet.com.cn/esf/page' + str(i)
		getAllContentLinks(url)
		i = i + 1
	
	for url in allContentLinks:
		page = getPageContent(url)
		if page is not None:
			print(page.title)
			store.save(config, page)
	
	
	print('抓取骊特二手房信息-结束')
	
def getAllContentLinks(siteUrl):
	html = urlopen(siteUrl)
	bsObj = BeautifulSoup(html.read(), 'html5lib')
	content = bsObj.find('div', {'class': 'container'})

	if content is not None:
		internalLinks = ext.getInternalLinks(content, splitAddress(siteUrl)[0])
		for link in internalLinks:
			link = str(link).strip()
			link = link.replace('://', 'http://fuzhou.leet.com.cn')
			if (link not in allContentLinks and link != '' and 'html' in link):
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
		title = bsObj.find('div', {'class': 'wsrter'}).find('h3').get_text()
	except:
		print('链接: ' + url + ' 获取标题失败')
		
	content = bsObj.find('div', {'class': 'container'})
	author = bsObj.find('div', {'class': 'nul_jinjr'})
	
	if author is not None:
		author = author.find('strong')
	
	cover = ''

	if content is None:
		print('链接:' + url + ' 内容为空')
		return
	else:
		
		images = content.findAll('img')
		
		try:
			
			for image in images:
				image['src'] = 'http://fuzhou.leet.com.cn' + image['src']
				
			img = content.find('img')
			if img is not None:
				cover = img['src']
		except:
			print('链接:' + url + ' 格式有误')
			
		content = str(content)

	if author is not None:
		author = '骊特-' + author.get_text()

	page = pageContent(title, content, author, '房产', cover)

	return page
