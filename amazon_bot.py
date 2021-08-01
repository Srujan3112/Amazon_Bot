from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

import re
import time
class AmazonBot(object):
    def __init__(self,items):
        self.amazon_url='https://www.amazon.in/'
        self.items=items
        self.options = Options()
        self.driver=webdriver.Chrome(options=self.options)
        self.driver.get(self.amazon_url)
    def search_items(self):
        urls=[]
        prices=[]
        names=[]
        for item in self.items:
            print(f"Searching for {item}.")
            self.driver.get(self.amazon_url)
            search_input=self.driver.find_element_by_id("twotabsearchtextbox")
            search_input.send_keys(item)
            self.driver.implicitly_wait(2)
            search_button=self.driver.find_element_by_xpath('//*[@id="nav-search"]/form/div[2]/div/input')
            search_button.click()
            self.driver.implicitly_wait(2)
            first_result=self.driver.find_element_by_xpath('//*[@id="search"]/div[1]/div/div[1]/div/span[3]/div[2]/div[3]')
            asin=first_result.get_attribute("data-asin")
            url="https://amazon.in/dp/"+asin
            price=self.get_product_price(url)
            name=self.get_product_name(url)
            prices.append(price)
            names.append(name)
            urls.append(url)
            print(price)
            print(name)
            print(url)
            self.driver.implicitly_wait(2)
        return  urls,prices,names
    def get_product_name(self,url):
        self.driver.get(url)
        product_name=None
        try:
            product_name = self.driver.find_element_by_id("productTitle").text
        except:
            pass
        if product_name is None:
            product_name='Not available'
        return  product_name



    def get_product_price(self,url):
        self.driver.get(url)
        price=None
        try:
            price=self.driver.find_element_by_id("priceblock_ourprice").text
        except:
            pass
        try:
            price = self.driver.find_element_by_id("priceblock_saleprice").text
        except:
            pass
        if price is None:
            price="Not available"
        else:
            non_decimal=re.compile(r'[^\d.]+')
            price=non_decimal.sub('',price)
        return price



