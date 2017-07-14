from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
html = urlopen("http://pythonscraping.com/pages/page1.html")
bs0bj = BeautifulSoup(html.read(),'html5lib')
print(bs0bj.h1)
print(bs0bj.html.body.h1)
print(bs0bj.body.h1)
print(bs0bj.html)

try:
    html1 = urlopen("http://pythonscraping.com/pages/page88888.html")
    #bs0bj1 = BeautifulSoup(html1.read(),'html5lib')
    #print(bs0bj1.h1)
    print(bs0bj.html.div)
except HTTPError as e:
    print(e)
    print(bs0bj.div)
