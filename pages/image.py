import requests

def saveImage(imageUrl, filename):
    p = requests.get(imageUrl)
    out = open(filename, "wb")
    out.write(p.content)
    out.close()