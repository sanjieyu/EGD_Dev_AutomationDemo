# Author:Yi Sun(Tim) 2024-09-04

'''Add Service Document function'''

import selenium
from selenium import webdriver
from time import sleep
from UIModule.add_service import *
import os

class Add_Service_Doc(Add_Service):

    def upload_attachement(self):
        '''Upload a attachement'''
        os.chdir(os.path.dirname(__file__))
        file_path = os.path.abspath("../Config/api_EGD_Dev.xlsx")
        self.driver.find_element(*self.add_attachement_btn_loc).send_keys(file_path)

if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(" ")
    driver.implicitly_wait(10)

    login = Add_Service_Doc(driver)
    login.typeUserName('aa@ecogaragedoors.com')
    login.typePassword('aabb')
    login.clickLogin()
    login.go_addservice()
    login.upload_attachement()