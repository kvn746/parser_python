from bs4 import BeautifulSoup as bs
import requests

def getPage(url):
    try:
        html = requests.get(url)

        return bs(html.content, 'html5lib')
    except:
        return None

def getChildUrls(page):
    try:
        links = []
        for tag in page.find_all('a'):
            links.append(str(tag.attrs.get('href')))

        return links
    except:

        return None

def isPageMatched(page, css_class):
    try:
        page.find('div', css_class)

        return 1
    except:

        return 0

def getTag(page, tag, css_class):
    try:

        return page.find(tag, css_class)
    except:

        return None
