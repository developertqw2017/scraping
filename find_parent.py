from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bs0 = BeautifulSoup(html,"html5lib")

print(bs0.find("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())
