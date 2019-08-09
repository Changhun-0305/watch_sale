import threading, time
import requests
from bs4 import BeautifulSoup
import re
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

proxies = {
  'http': 'http://142.93.80.120:3128',
  'https': 'http://20.41.41.145:3128',
}

def foo():
    print(time.ctime())

def get_html(url):
    _html = ""
    # resp = requests.get(url, proxies=proxies)
    # if resp.status_code == 200:
    #     _html = resp.text
    # else:
    #     print(resp.status_code)
    return _html

WAIT_TIME_SECONDS = 2
CON_URL = "https://www.cosstores.com/kr_krw/coe/changeCountry.html"
US_URL = "http://www.cosstores.com/content/cos/page.countryselector.en_US.en_usd.USD.jsp?goeorguri=%2Fen_eur%2Findex.html"
GER_URL = "https://www.cosstores.com/en_eur/sale.html"
KOR_URL = "https://www.cosstores.com/kr_krw/men/sale.html"
ORGANIC_URL = "https://www.cosstores.com/en_usd/men/trousers/product.elasticated-organic-cotton-trousers-oatmeal.0742719002.html"
if __name__ == "__main__":
    #html = get_html(CON_URL)
    #soup = BeautifulSoup(html, 'html.parser')
    #for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
    #    print(link.get('href'))
    html2 = get_html(ORGANIC_URL)
    soup = BeautifulSoup(html2, 'lxml')
    #print(soup.prettify())
    div = soup.find("button", id="size_0742719002002")
    # print(dir(div))
    # print(div)
    # print(div.text)
    # print(div['class_'])
    # print(div.text)
    # print(div.keys)
    # print(soup.find_all(class_="tooltip-text"))

    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome()
    driver.get(CON_URL)
    html = driver.page_source
    print("1")
    country_element = driver.find_element_by_class_name('countries')
    print('2')
    print(dir(country_element))
    clocked = driver.find_element_by_xpath('//a[@href="'+US_URL+'"]').click()
    print(driver.page_source)
    driver.find_element_by_xpath('//a[@href="'+'/en_usd/men.html'+'"]').click()
    

    driver.close()
    


    
    #ticker = threading.Event()
    #while not ticker.wait(WAIT_TIME_SECONDS):
    #    foo()#