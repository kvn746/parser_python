from bs4 import BeautifulSoup as bs
import requests

def getPage(url):
    html = requests.get(url)

    return bs(html.content, 'html5lib')

def getChildUrls(page):

    links = []
    for tag in page.find_all('a'):
        links.append(str(tag.attrs.get('href')))

    return links

def isPageMatched(page, css_class):
    result = 0
    for tag in page.find_all('dev'):
        if str(tag.attrs.get('class')) == css_class:
            result = 1

    return result