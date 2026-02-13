# Author:Yi Sun(Tim) 2023-2-11

'''Add a Dealer Quote with a roller door function'''

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.login_admin import Admin_Portal
from pages.add_dealer_quote import Add_Dealer_Quote
from pages.add_dealer_roller_door import Add_DP_Roller
from pages.dealer_roller_door import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException

class Add_Dealer_Quote_With_Roller_Door():
    proposal_number_loc = (By.ID,'ProposalNo')
    find_quote_input = (By.ID,'search-quote')
    find_quote_btn = (By.ID,'search-btn')

    searched_proposal_no_loc = (By.NAME, 'proposalid')
    searched_door_no_loc = (By.NAME, 'doorid')
    searched_door_status_loc = (By.NAME, 'doorstatus')

    setting_btn_loc = (By.ID,'Settings')
    quotation_loc = (By.CSS_SELECTOR,'div.col-md-4:nth-child(2) > div:nth-child(6) > label:nth-child(1)')
    submit_quote_btn_loc = (By.ID,'btnSubmitQuoteFinal')
    submit_msg_btn_loc = (By.ID,'SubmitMsg')

    def __init__(self,driver):
        self.driver = driver
        self.add_dealer_quote = Add_Dealer_Quote(self.driver)
        self.add_dealer_roller_door = Add_DP_Roller(self.driver)

    def add_dealer_rollerdoor_fun(self):
        self.add_dealer_quote.creat_quote()
        self.add_dealer_roller_door.go_roller_door()
        self.add_dealer_roller_door.add_dealer_roller_door()
        self.add_dealer_quote.check_add_dealer_quote_success

    @property
    def get_proposal_number(self):
        global proposal_number
        proposal_number = self.driver.find_element(*self.proposal_number_loc).get_attribute('value')
        print('number is:',proposal_number)
        return proposal_number

    def search_new_quote(self):
        self.driver.refresh()
        self.driver.find_element(*self.find_quote_input).send_keys(proposal_number)
        self.driver.find_element(*self.find_quote_btn).click()
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.searched_door_no_loc))

    @property
    def verify_new_quote(self):
        searched_proposal_no = self.driver.find_element(*self.searched_proposal_no_loc).text
        searched_door_no = self.driver.find_element(*self.searched_door_no_loc).text
        searched_door_status = self.driver.find_element(*self.searched_door_status_loc).text
        print(searched_door_no,searched_door_status)
        return searched_door_no,searched_door_status

    def go_quotation(self):
        self.driver.find_element(*self.setting_btn_loc).click()
        self.driver.find_element(*self.quotation_loc).click()
        self.driver.find_element(*self.submit_quote_btn_loc).click()
        self.driver.find_element(*self.submit_msg_btn_loc).click()
        self.driver.refresh()
        self.driver.find_element(*self.find_quote_input).send_keys(proposal_number)
        self.driver.find_element(*self.find_quote_btn).click()
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.searched_door_no_loc))

    @property
    def verify_new_quote_submitted(self):
        searched_door_status = self.driver.find_element(*self.searched_door_status_loc).text
        print(searched_door_status)
        return searched_door_status


if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("http://xxxxx/")
    driver.implicitly_wait(10)

    login = Admin_Portal(driver)
    login.typeUserName('xx@xxx.com')
    login.typePassword('xxxx')
    login.clickLogin()
    login1 = Add_Dealer_Quote_With_Roller_Door(driver)
    login1.add_dealer_rollerdoor_fun()
    login1.get_proposal_number
    login1.search_new_quote()
    login1.verify_new_quote
    # login1.go_quotation
    # login1.verify_new_quote_submitted

