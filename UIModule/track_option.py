# Author:Yi Sun(Tim) 2025-5-23

'''Verify the track option for Roller Doors'''

import selenium
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from UIModule.login_admin import Admin_Portal
from UIModule.add_quote import Add_Quote
from UIModule.add_roller_door import Add_Roller_Door
from UIModule.standard_door import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException

class Track_Option():

    def __init__(self,driver):
        self.driver = driver
        self.add_quote = Add_Quote(self.driver)
        self.add_door = Add_Roller_Door(self.driver)

    @property
    def check_track_t35(self):
        self.add_quote.go_addquote()
        self.add_door.go_addstandarddoor()
        return self.add_door.track_t35

    @property
    def check_track_t50(self):
        # self.add_quote.go_addquote
        # self.add_door.go_addstandarddoor
        return self.add_door.track_t50

if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("http:// ")
    driver.implicitly_wait(10)

    login = Admin_Portal(driver)
    login.typeUserName('aa@ecogaragedoors.com')
    login.typePassword('aabb')
    login.clickLogin()
    login1 = Track_Option(driver)
    login1.check_track_t35
    login1.check_track_t50