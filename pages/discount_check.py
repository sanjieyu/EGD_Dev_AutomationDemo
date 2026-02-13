# Author:Yi Sun(Tim) 2025-04-09

'''Verify the door price discount function'''

import selenium
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from pages.login_admin import Admin_Portal
from pages.add_quote import Add_Quote
from pages.add_standar_door import Add_Standard_Door
from pages.add_quote_with_door import Add_Quote_With_Door
from pages.quotation_panel_door import Quotation_Panel
from pages.standard_door import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException

class Discount():

    for_automation_test_loc = (By.CSS_SELECTOR, "[aria-label='testautomation']")

    def __init__(self,driver):
        self.driver = driver
        self.add_quote1 = Add_Quote(self.driver)
        self.add_door = Add_Standard_Door(self.driver)
        self.standard_door = Standard_Door(self.driver)
        self.add_quote_panellift = Add_Quote_With_Door(self.driver)
        self.quotation_panellift = Quotation_Panel(self.driver)
        self.proposal_number = None

    def add_panellift_door(self):
        self.add_quote1.go_addquote()
        self.add_door.go_addstandarddoor()
        self.add_door.add_door()

    @property
    def discount_panellift(self):
        sleep(1)
        account_type = Select(self.driver.find_element(*self.add_quote1.account_type_select))
        account_type.select_by_visible_text('Account')
        account_customer_input = self.driver.find_element(*self.add_quote1.account_customer_select1)
        account_customer_input.clear()
        account_customer_input.send_keys('For Automation Testing')
        self.driver.find_element(*self.for_automation_test_loc).click()
        self.driver.find_element(*self.add_quote1.supply_type_select).click()
        self.driver.find_element(*self.add_quote1.supply_type_select).click()
        sleep(1)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element(*self.add_quote1.save_quote_btn).click()
        sleep(2)
        self.add_quote_panellift.get_proposal_number
        self.quotation_panellift.goto_quotation_discount()
        return self.quotation_panellift.check_discount()


if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("http:// ")
    driver.implicitly_wait(10)

    login = Admin_Portal(driver)
    login.typeUserName('aa@ecogaragedoors.com')
    login.typePassword('aabb')
    login.clickLogin()
    login1 = Discount(driver)
    login1.add_panellift_door()
    login1.discount_panellift



