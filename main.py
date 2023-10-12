from bs4 import BeautifulSoup as bs
import requests
import pages.data

down = ['https://keyfob.ru/brelki/pulti-apollo/', 'https://keyfob.ru/brelki/brelok-apollo-mf-novij.html']

# url = "https://keyfob.ru"

# if url in down:
#     print(1)
# else:
#     print(0)
# page = pages.data.getPage(url)
# print(pages.data.isPageMatched(page, 'product-info'))

# url = "https://keyfob.ru/brelki/brelki--pulti-distancionnogo-upravlenija-apollo/"
# page = pages.data.getPage(url)
# links = pages.data.getChildUrls(page)
# linksCategories = []
# for link in links:
#     if link.find('keyfob.ru') >= 0 and link.find('?') < 0 and link != 'https://keyfob.ru/':
#         childPage = pages.data.getPage(link)
#         if pages.data.isPageMatched(childPage, 'category-info'):
#             linksCategories.append(link)
#             print(link)

# for link in linksCategories:
#     print(link)
# print(soup.prettify())

# page = pages.data.getPage('https://keyfob.ru/brelki/brelok-apollo-mf-novij.html')

with open("good.html") as fp:
    page = bs(fp, 'html5lib')

    description = pages.data.getDescription(page, 'product-info')
    print(description)
    print(pages.data.getParameters(description))