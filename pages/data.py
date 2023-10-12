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
    try:
        page.find('div', css_class)
        return 1
    except:
        return 0
    result = 0
    for tag in page.find_all('div'):
        if str(tag.attrs.get('class')).find(css_class) >= 0:
            result = 1

    return result

def getImageUrl(page, css_class):
    try:
        info = page.find('div', css_class)
        return info.find('a', 'colorbox').attrs.get('href')
    except:
        return ''

def getDescription(page, css_class):
    try:
        info = page.find('div', css_class)
        description = info.find('div', 'description')
        return description
    except:
        return ''

def getParameters(description):
    try:
        parameters = description.text

        return parameters
    except:
        return ''