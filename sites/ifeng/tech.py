from urllib.request import urlopen
from urllib.parse import urlparse
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re
import datetime
import random

import utils.extention as ext
from utils.extention import splitAddress
from core.models.pageContent import pageContent

random.seed(datetime.datetime.now)
allContentLinks = set()

# 爬取入口
def crawler(config):
    print('凤凰科技频道抓取-开始')

    getAllContentLinks('http://tech.ifeng.com')

    for url in allContentLinks:
        page = getPageContent(url)
        if page is not None:
            print(page.title)

    print('凤凰科技频道抓取-结束')
    
    print(config.storeApi)

# 获取所有内容链接
def getAllContentLinks(siteUrl):
    html = urlopen(siteUrl)
    bsObj = BeautifulSoup(html.read(), 'html5lib')
    content = bsObj.find('div', {'class': 'box01_hots'})

    if content is not None:
        internalLinks = ext.getInternalLinks(content, splitAddress(siteUrl)[0])
        for link in internalLinks:
            link = str(link).strip()
            if (link not in allContentLinks and link != ''):
                print(link)
                allContentLinks.add(link)

# 获取抓取内容信息
def getPageContent(url):

    html = None

    try:
        html = urlopen(url)
    except HTTPError as e:
        print('http vistor error')
    except Exception as e:
        print('load fail')

    return parseHtml(url, html)

# 解析内容页面Html
def parseHtml(url, html):

    if html is None:
        print('链接:' + url + ' 内容页为空')
        return
    if html.msg != 'OK':
        print('链接:' + url + ' 访问错误:' + html.msg)
        return
        
    bsObj = BeautifulSoup(html, 'html5lib')
    
    title = bsObj.title.get_text()
    content = bsObj.find('div', { 'id': 'main_content' })
    author = bsObj.find('span', { 'itemprop': 'publisher' })
    
    if content is None:
        print('链接:' + url + ' 内容为空')
        return
    else:
       content = str(content)
    
    if author is not None:
        author = author.get_text()
    
    page = pageContent(title, content, author)
    
    return page
            
