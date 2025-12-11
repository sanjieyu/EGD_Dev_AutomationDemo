# Author:Yi Sun(Tim) 2025-10-07

'''Add a Quote with a OptiLift door function'''

import selenium
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from UIModule.login_admin import Admin_Portal
from UIModule.add_quote import Add_Quote
from UIModule.add_optilift_door import Add_OptiLift_Door
# from UIModule.standard_door import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException

class Add_Quote_With_OptiLift_Door():

    proposal_number_loc = (By.ID,'ProposalNo')   #get the proposal number for the edit box
    find_quote_input = (By.ID,'search-quote')
    find_quote_btn = (By.ID,'search-btn')

    searched_proposal_no_loc = (By.NAME, 'searchedid')
    searched_door_no_loc = (By.NAME, 'doorid')
    searched_door_status_loc = (By.NAME, 'doorstatus')

    def __init__(self,driver):
        self.driver = driver
        self.add_quote= Add_Quote(self.driver)
        self.add_optilift_door = Add_OptiLift_Door(self.driver)

    def add_door_func(self):
        self.add_quote.go_addquote()
        self.add_optilift_door.go_addstandarddoor()
        self.add_optilift_door.add_optilift_door()
        sleep(2)
        self.add_quote.check_add_quote_success

    @property
    def get_proposal_number(self):
        global proposal_number
        proposal_number = self.driver.find_element(*self.proposal_number_loc).get_attribute('value')    #取对话框里面的job nubmer的值
        print('number is:',proposal_number)
        return proposal_number

    @property
    def search_new_quote(self):
        self.driver.refresh()
        sleep(1)
        self.driver.find_element(*self.find_quote_input).send_keys(proposal_number)
        sleep(2)
        self.driver.find_element(*self.find_quote_btn).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.searched_door_no_loc))  # new add

    @property
    def verify_new_quote(self):
        searched_proposal_no = self.driver.find_element(*self.searched_proposal_no_loc).text
        searched_door_no = self.driver.find_element(*self.searched_door_no_loc).text
        searched_door_status = self.driver.find_element(*self.searched_door_status_loc).text
        print(searched_door_no, searched_door_status)
        return searched_door_no, searched_door_status

if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("http:// ")
    driver.implicitly_wait(10)

    login = Admin_Portal(driver)
    login.typeUserName('aa@ecogaragedoors.com')
    login.typePassword('aabb')
    login.clickLogin()
    login1 = Add_Quote_With_OptiLift_Door(driver)
    # login1.get_proposal_number
    # login1.search_new_quote
    # login1.verify_new_quote
    login1.add_door_func()
    login1.get_proposal_number
    login1.search_new_quote
    login1.verify_new_quote



