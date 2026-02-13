# Author:Yi Sun(Tim) 2025-2-11

'''Add a Dealer Quote with a insulated door function'''

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.login_admin import Admin_Portal
from pages.add_dealer_quote import Add_Dealer_Quote
from pages.add_dealer_insulated_door import Add_DP_Insulated
from pages.dealer_insulated_door import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException

class Add_Dealer_Quote_With_Insulated_Door():
    proposal_number_loc = (By.ID,'ProposalNo')   #get the proposal number for the edit box
    find_quote_input = (By.ID,'search-quote')
    find_quote_btn = (By.ID,'search-btn')

    searched_proposal_no_loc = (By.NAME,'proposalnum')
    searched_door_no_loc = (By.NAME,'doorid')
    searched_door_status_loc = (By.NAME,'')

    setting_btn_loc = (By.CSS_SELECTOR,"th.grid-header:nth-child(2) > div:nth-child(1) > span:nth-child(1)")
    quotation_loc = (By.CSS_SELECTOR,'th.grid-header:nth-child(10) > div:nth-child(1) > span:nth-child(1)')
    submit_quote_btn_loc = (By.ID,'btnSubmitQuoteFinal')
    submit_msg_btn_loc = (By.XPATH,"//button[text()='SubmitMsg']")

    def __init__(self,driver):
        self.driver = driver
        self.add_dealer_quote = Add_Dealer_Quote(self.driver)
        self.add_dealer_insulated_door = Add_DP_Insulated(self.driver)

    def add_dealer_insulateddoor_fun(self):
        self.add_dealer_quote.creat_quote()
        self.add_dealer_insulated_door.go_insulated_door()
        self.add_dealer_insulated_door.add_dealer_insulated_door()
        sleep(2)
        self.add_dealer_quote.check_add_dealer_quote_success

    @property
    def get_proposal_number(self):
        global proposal_number
        proposal_number = self.driver.find_element(*self.proposal_number_loc).get_attribute('value')    #取对话框里面的job nubmer的值
        print('number is:',proposal_number)
        return proposal_number

    def search_new_quote(self):
        self.driver.refresh()
        sleep(1)
        self.driver.find_element(*self.find_quote_input).send_keys(proposal_number)
        sleep(2)
        self.driver.find_element(*self.find_quote_btn).click()
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.searched_door_no_loc))      #new add

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
        sleep(1)
        self.driver.find_element(*self.submit_msg_btn_loc).click()
        sleep(2)
        self.driver.refresh()
        sleep(1)
        self.driver.find_element(*self.find_quote_input).send_keys(proposal_number)
        sleep(2)
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
    driver.get("http:// ")
    driver.implicitly_wait(10)

    login = Admin_Portal(driver)
    login.typeUserName('aa@ecogaragedoors.com')
    login.typePassword('aabb')
    login.clickLogin()
    login1 = Add_Dealer_Quote_With_Insulated_Door(driver)
    login1.add_dealer_insulateddoor_fun()
    login1.get_proposal_number
    login1.search_new_quote()
    login1.verify_new_quote
    login1.go_quotation()
    login1.verify_new_quote_submitted