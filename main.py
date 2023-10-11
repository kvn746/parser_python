from bs4 import BeautifulSoup as bs
import requests
import pages.getUrls

# down = ['https://keyfob.ru/brelki/pulti-apollo/', 'https://keyfob.ru/brelki/brelok-apollo-mf-novij.html']

url = "https://keyfob.ru/brelki/pulti-apollo/"
page = pages.getUrls.getPage(url)
print(pages.getUrls.isPageMatched(page, 'product-info'))

# url = "https://keyfob.ru/brelki/brelki--pulti-distancionnogo-upravlenija-apollo/"
# page = pages.getUrls.getPage(url)
# links = pages.getUrls.getChildUrls(page)
# linksCondition = []
# for link in links:
#     if link.find('keyfob.ru') >= 0 and link.find('?') < 0 and link != 'https://keyfob.ru/':
#         linksCondition.append(link)
#
# for link in linksCondition:
#     print(link)
# print(soup.prettify())

