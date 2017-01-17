from lxml import html
import urllib.request
import sys
import os
import requests

page = input("Enter the webpage address: ")
page = requests.get(page)
tree = html.fromstring(page.content)

# gets the required information from the webpage
# gets the folder name from title
folderName = tree.xpath("//head/title")
# get the image paths
imgPath = tree.xpath("//*[@class='zoom']/@href")
# clears out the de-clutters the folder name
folderName = folderName[0].text_content().rstrip(
    'Imgur').rstrip('Album on').rstrip('-').strip()

# creates the folder if not existing
if not os.path.exists(folderName):
    os.makedirs(folderName)

print("Will be saved to the folder {0: s}".format(folderName))

for i in range(len(imgPath)):

    downloadSrc = imgPath[i].strip('//')
    print(downloadSrc)

    urllib.request.urlretrieve(
        "https://{0:s}".format(downloadSrc),
        "{0:s}/{1:d}".format(folderName, (i + 1)))
    print('Downloaded Image', (i + 1))
