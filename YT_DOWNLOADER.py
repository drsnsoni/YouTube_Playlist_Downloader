from pytube import YouTube
import os
from bs4 import BeautifulSoup as bs
import requests

data = []
r = requests.get('https://www.youtube.com/playlist?list=PLe30vg_FG4OSaqSz3oEIXen8grekDAtBn')
page = r.text
soup = bs(page, 'html.parser')
b = open("a.html", "w", encoding="utf_8")
b.write(str(soup))
c = open("a.html", "r", encoding="utf_8")

d = c.readlines()
lin = 0
while True:
    try:
        a = d[lin]
    except:
        print("Finished")
        break
    if '"url":"/watch?v=' in a:
        a = a.split('"url":"')
        te = 0

        while True:
            try:
                if "/watch?v=" in a[te]:
                    aa = a[te].split('",')
                    e = 0
                    while True:
                        try:
                            if "/watch?v=" in aa[e]:
                                url = "https://www.youtube.com"+aa[e]
                                data.append(url)
                        except:

                            break
                        e += 1

            except:

                break
            te += 1

    lin += 1

c.close()
b.close()
os.remove("a.html")
# print("Given data is in list so you can print url by use this code print(data[0])\n\n")

print(data[0])

for i in data:
    youtubeObject = YouTube(i)
    youtubeObject = youtubeObject.streams.get_highest_resolution()

    try:
        youtubeObject.download()
        print(i +  "         Downloading.........")
    except:
        print("An error has occurred")
    print("Download is completed" + i + "successfully")
