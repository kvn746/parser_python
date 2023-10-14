import requests

def saveImage(imageUrl, filename):
    try:
        session = requests.session()
        headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0",
                   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"}
        p = session.get(imageUrl, headers = headers)
        saveFile(p.content, filename, "wb")

    except:
        print('not loaded image')
        return

def saveFile(content, filename, format):
    try:
        out = open(filename, format)
        out.write(content)
        out.close()
    except:

        return