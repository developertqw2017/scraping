from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bs0 = BeautifulSoup(html,"html5lib")

imageList = bs0.find("table",{"id":"giftList"}).children
for child in imageList:
    print(child)
