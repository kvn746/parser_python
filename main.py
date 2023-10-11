from bs4 import BeautifulSoup as bs
import requests
import pages.getUrls

url = "https://keyfob.ru/brelki/brelki--pulti-distancionnogo-upravlenija-apollo/"
page = pages.getUrls.getPage(url)
links = pages.getUrls.getChildUrls(page)
linksCondition = []
for link in links:
    if link.find('keyfob.ru') >= 0 and link.find('?') < 0 and link != 'https://keyfob.ru/':
        linksCondition.append(link)
        if link.find('.html') >= 0:
            print(link)
            print(pages.getUrls.isPageMatched(pages.getUrls.getPage(link), 'product_info'))
# for link in linksCondition:
#     print(link)
# print(soup.prettify())

