import threading, time
import requests
from bs4 import BeautifulSoup
import re

proxies = {
  'http': 'http://208.72.119.2:60099',
  'https': 'http://165.22.164.22:8080',
}

def foo():
    print(time.ctime())

def get_html(url):
    _html = ""
    resp = requests.get(url, proxies=proxies)
    if resp.status_code == 200:
        _html = resp.text
    return _html

WAIT_TIME_SECONDS = 2
CON_URL = "https://www.cosstores.com/kr_krw/coe/changeCountry.html"
US_URL = "https://www.cosstores.com/en_usd/sale.html"
GER_URL = "https://www.cosstores.com/en_eur/sale.html"
KOR_URL = "https://www.cosstores.com/kr_krw/men/sale.html"


if __name__ == "__main__":
    #html = get_html(CON_URL)
    #soup = BeautifulSoup(html, 'html.parser')
    #for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
    #    print(link.get('href'))
    html2 = get_html(US_URL)
    print(len(html2))
    print(type(html2))
    soup = BeautifulSoup(html2, 'lxml')
    print(soup.text)


    
    #ticker = threading.Event()
    #while not ticker.wait(WAIT_TIME_SECONDS):
    #    foo()#