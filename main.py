from bs4 import BeautifulSoup as bs
import pages.data
import pages.image
import os

URL = "https://keyfob.ru"

down = []
csv = "artikul;model;manufacturer;image;price;link" + '\n'

def getImageUrl(page, css_class):
    try:
        info = pages.data.getTag(page, 'div', css_class)

        return info.find('a', 'cloud-zoom').attrs.get('href')
    except:

        return None

def getDescription(page, css_class):
    try:

        return pages.data.getTag(page, 'div', css_class)
    except:

        return None

def getParameters(description):
    try:
        parameters = description.text
        parameters = parameters.replace(' ', '')
        parameters = parameters.replace('\t', '')
        parameters = parameters.split('\n')
        parameters = list(filter(None, parameters))

        return parameters
    except:

        return None

def getPrice(page, css_class):
    try:
        price = pages.data.getTag(page, 'div', css_class).text
        price = price.replace(' ', '')
        price = price.replace('\t', '')
        price = price.split('\n')
        price = list(filter(None, price))

        return float(price[1].replace('р.',''))
    except:

        return None

def parsePage(page):
    try:
        description = getDescription(page, 'description')
        imageUrl = getImageUrl(page, 'product-info')
        filename = imageUrl[imageUrl.rfind('/') + 1:]
        imageFilename = 'images/' + imageUrl[imageUrl.rfind('/') + 1:]
        filename = filename[:filename.rfind('.')]
        pages.image.saveImage(imageUrl, imageFilename)

        parameters = getParameters(description)
        manufacturer = ''
        artikul = ''
        model = ''
        for parameter in parameters:
            if parameter.find('Производитель') >= 0:
                manufacturer = parameter[parameter.find(':') + 1:]
            if parameter.find('Артикул') >= 0:
                artikul = parameter[parameter.find(':') + 1:]
            if parameter.find('Модель') >= 0:
                model = parameter[parameter.find(':') + 1:]
        if artikul == '':
            artikul = model
        price = getPrice(page, 'price')
        json = ('[{"artikul":"' + artikul +
                '", "model":"' + model +
                '", "manufacturer":"' + manufacturer +
                '", "image":"' + imageFilename +
                '", "price":"' + str(price) +
                '", "link":"' + imageUrl + '"}]')

        pages.image.saveFile(json, 'json/' + filename + '.json', "w")

        return (json)
    except:

        return None

if not os.path.exists('images'):
    os.makedirs('images')
if not os.path.exists('json'):
    os.makedirs('json')



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

# with open("good.html") as fp:
#     page = bs(fp, 'html5lib')
#     print(parsePage(page))


with open("main.html") as fp:
    page = bs(fp, 'html5lib')

    links = pages.data.getChildUrls(page)
    linksCategories = []
    for link in links:
        if link.find('novotechnic.ru') >= 0 and link.find('?') < 0 and link != 'http://novotechnic.ru/':
            childPage = pages.data.getPage(link)
            if pages.data.isPageMatched(childPage, 'div', 'category-info'):
                linksCategories.append(link)

    print(linksCategories)

# page = pages.data.getPage("http://novotechnic.ru/login/")
#
# print(pages.data.isPageMatched(page, 'div', 'category-info'))

