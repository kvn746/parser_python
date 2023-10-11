from bs4 import BeautifulSoup as bs
import requests

url = "https://keyfob.ru/brelki/brelki--pulti-distancionnogo-upravlenija-apollo/"
html = requests.get(url)

soup = bs(html.content, 'html5lib')

links = []
for tag in soup.find_all('a'):
    link = str(tag.attrs.get('href'))
    if link.find('keyfob.ru') >= 0 and link.find('?') < 0 and link != 'https://keyfob.ru/':
        links.append(link)

for link in links:
    print(link)
# print(soup.prettify())
