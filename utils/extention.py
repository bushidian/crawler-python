from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re

#获取html内所有内链的列表
def getInternalLinks(html, includeUrl):
	includeUrl = urlparse(includeUrl).scheme + '://' + urlparse(includeUrl).netloc
	internalLinks = []
	
	allLinks = []
	
	try: 
		allLinks = html.findAll('a', { 'href': re.compile('^(/|.*' + includeUrl + ')') })
	except Exception as e:
		print('NotFound:' + str(e))
	
	if allLinks is None:
		return internalLinks
	
	#找出所有以“／”开头的链接
	for link in allLinks:
		if link['href'] is not None:
			if link.attrs['href'] not in internalLinks:
				if link.attrs['href'].startswith('/'):
					internalLinks.append(includeUrl + link.attrs['href'])
				else:
					internalLinks.append(link.attrs['href'])				
	
	return internalLinks
	
def splitAddress(address):
	addressParts = address.replace('http://', '').split('/')
	return addressParts
	
def hello():
	print('hello')