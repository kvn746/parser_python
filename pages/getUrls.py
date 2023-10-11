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
    for tag in page.find_all('div'):
        if str(tag.attrs.get('class')).find(css_class) >= 0:
            result = 1

    return result

def getContent(page, css_class):
    content = []
    for tag in page.find_all('div'):
    #     if str(tag.attrs.get('class')).find(css_class) >= 0:
    #         container = tag
    # for tag in container.find-all('div'):
        if str(tag.attrs.get('class')).find('image') >= 0:
            image = tag
        if str(tag.attrs.get('class')).find('description') >= 0:
            description = tag
        if str(tag.attrs.get('class')).find('price') >= 0:
            price = tag

    content.append(image)
    content.append(description)
    content.append(price)

    return content
