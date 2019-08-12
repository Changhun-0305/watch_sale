import threading, time
import requests
from bs4 import BeautifulSoup
import re
import json
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

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
    options = webdriver.ChromeOptions()
    options.add_argument('headless')

    driver = webdriver.Chrome()
    driver.get(CON_URL)
    html = driver.page_source
    print("1")
    country_element = driver.find_element_by_class_name('countries')
    print('2')
    print(dir(country_element))

    clocked = driver.find_element_by_xpath('//a[@href="'+US_URL+'"]').click()
    print("3")
    #print(driver.page_source)
    driver.get(ORGANIC_URL)
    #print(driver.page_source)
    sizes = driver.find_element_by_id("sizes")
    xs = sizes.find_element_by_id("size_0742719002001")
    att = xs.get_attribute('class')
    print(att)
    # print(sizes)
    # print(xs)
    # print(sizes.text)
    # print(xs.text)
    # spanned = driver.find_element_by_xpath("//span[@class='show-tooltip']")
    # print(spanned)
    # print(spanned.text)
    # print(dir(spanned))
    #print(spanned.text)


    # driver.find_element_by_xpath('//a[@href="'+'/en_usd/men.html'+'"]').click()
    # print("4")
    # driver.find_element_by_xpath('//a[@href="'+'/en_usd/men/trousers.html'+'"]').click()
    # print("5")
    
    # driver.find_element_by_xpath('//a[@href="'+'/en_usd/men/trousers/product.elasticated-organic-cotton-trousers-oatmeal.0742719002.html'+'"]').click()
    # print(driver.page_source)


    driver.close()
    


    
    #ticker = threading.Event()
    #while not ticker.wait(WAIT_TIME_SECONDS):
    #    foo()#