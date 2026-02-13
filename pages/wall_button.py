# Author:Yi Sun(Tim) 2025-04-09

'''Verify the wall button logic function'''

import selenium
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from pages.login_admin import Admin_Portal
from pages.add_quote import Add_Quote
from pages.add_standar_door import Add_Standard_Door
from pages.standard_door import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException

class Wall_Button():

    def __init__(self,driver):
        self.driver = driver
        self.add_quote1 = Add_Quote(self.driver)
        self.add_door = Add_Standard_Door(self.driver)
        self.standard_door = Standard_Door(self.driver)


    @property
    def default_wallbutton_amount(self):
        self.add_quote1.go_addquote()
        self.add_door.go_addstandarddoor()
        self.add_door.add_door_opener()
        wallbutton = self.driver.find_element(*self.standard_door.wall_btn_select)
        wallbutton_value = wallbutton.get_attribute('value')
        self.driver.find_element(*self.standard_door.close_standarddoor_btn).click()
        print(wallbutton_value)
        return wallbutton_value

    '''Change to a Customer which got the 1st wall button free on customer card'''

    @property
    def customer_wallbutton_amount(self):
        sleep(1)
        account_type = Select(self.driver.find_element(*self.add_quote1.account_type_select))
        account_type.select_by_visible_text('Account')
        account_customer_input = self.driver.find_element(*self.add_quote1.account_customer_select1)
        account_customer_input.clear()
        account_customer_input.send_keys('For Automation Testing')
        self.driver.find_element(*self.add_quote1.account_customer_btn).click()
        sleep(1)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.add_door.go_addstandarddoor()
        self.add_door.add_door_opener()
        wallbutton_account = self.driver.find_element(*self.standard_door.wall_btn_select)
        wallbutton_account_value = wallbutton_account.get_attribute('value')
        self.driver.find_element(*self.standard_door.close_standarddoor_btn).click()
        print(wallbutton_account_value)
        return wallbutton_account_value


if __name__ == '__main__':
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get("http:// ")
        driver.implicitly_wait(10)
        login = Admin_Portal(driver)
        login.typeUserName('aa@ecogaragedoors.com')
        login.typePassword('aabb')
        login.clickLogin()
        login = Wall_Button(driver)
        login.default_wallbutton_amount
        login.customer_wallbutton_amount