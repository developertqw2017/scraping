from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bs0bj = BeautifulSoup(html,"html5lib")
nameList = bs0bj.findAll("span",{"class":"green"})
for name in nameList:
    print(name.get_text())

print("---------------------------")

nameList1 = bs0bj.findAll(id = "text")
for name in nameList1:
    print(name.get_text())

nameList2 = bs0bj.findAll({"h1","h2","h3","h4"})
for name in nameList2:
    print(name.get_text())
