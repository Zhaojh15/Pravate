#!/env/bin/python
# coding:utf-8

from base import base
from selenium.webdriver.common.by import By
import time

class SearchPage(base):
    def search_depart(self):
        return self.findele(By.ID, "fromStationText")

    def search_arrive(self):
        return self.findele(By.ID, "toStationText")

    def search_date(self,day):
        self.findele(By.ID, "train_date").click()
        day = "/html/body/div[11]/div[1]/div[2]/div["+day+"]/div"
        return self.findele(By.Xpath, day)

    def seach_btn(self):
        return self.findele(By.ID, "search_one")

    def search_train(self, depart, arrive, day):
        self.search_depart().send_keys(depart)
        time.sleep(2)
        self.search_arrive().send_keys(arrive)
        time.sleep(2)
        self.search_date(day).click()
        self.seach_btn().click()
        time.sleep(5)



