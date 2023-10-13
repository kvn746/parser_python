import requests

def saveImage(imageUrl, filename):
    try:
        p = requests.get(imageUrl)
        saveFile(p.content, filename, "wb")

    except:

        return

def saveFile(content, filename, format):
    try:
        out = open(filename, format)
        out.write(content)
        out.close()
    except:

        return