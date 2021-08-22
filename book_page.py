#!/env/bin/python
# coding:utf-8

from base import base
from selenium.webdriver.common.by import By
import time

class BookPage(base):
    def book(self):
        if "2203" in self.driver.page:
            return self.findele(By.XPATH, "/html/body/div[8]/div[8]/table/tbody[1]/tr[27]/td[13]/a")