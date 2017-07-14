from urllib import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bs0bj = BeautifulSoup(html,"html5lib")

nameList = bs0bj.findAll("span",{"class":"green"})
for name in nameList:
    print(name.get_text())
