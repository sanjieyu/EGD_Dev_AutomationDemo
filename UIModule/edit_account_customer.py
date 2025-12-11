# Author:Yi Sun(Tim) 2024-08-06

'''Edit Account Customer Page'''

import selenium
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from UIModule.account_customer import *
from selenium.webdriver.support import expected_conditions as EC

class Edit_Account_Customer(Account_Customer):

    '''loc for general elements'''
    edit_customer_title_loc = (By.CSS_SELECTOR, "[aria-label='edit']")
    active_loc = (By.ID,'IsActiveText')
    active_switch_loc = (By.CSS_SELECTOR,"label[for='ActiveSwitch']")
    access_loc = (By.ID,'accessToDealerPortalText')
    access_switch_loc = (By.CSS_SELECTOR,"label[for='AccessSwitch']")
    customer_name_des_loc = (By.CSS_SELECTOR,"label[for='CustomerName']")
    first_name_des_loc = (By.CSS_SELECTOR,"label[for='FirstName']")
    customer_name_box_loc = (By.ID,'CustomerName')
    first_name_box_loc = (By.ID,'FirstName')
    back_btn_loc = (By.ID, "btnBack")
    save_btn_loc = (By.ID,'btnSaveCustomer')

    '''loc for Address Details section'''


    def __init__(self,driver):
        self.driver = driver
        self.active_status = None

    def goto_edit_account(self):
        '''Go to the Edit Account screen'''
        self.driver.find_element(*self.account_searchbox_loc).send_keys('tim2')
        sleep(3)
        self.driver.find_element(*self.account_searchbtn_loc).click()
        sleep(3)
        self.driver.find_element(*self.search_result_name_loc).click()


    @property
    def check_edit_url(self):
        '''Check the edit account customer URL'''
        edit_url = self.driver.current_url
        # print(edit_url)
        return edit_url

    @property
    def check_general_elements(self):
        '''Check general elements'''
        edit_title = self.driver.find_element(*self.edit_customer_title_loc).text
        active_des  = self.driver.find_element(*self.active_loc).text
        access_des = self.driver.find_element(*self.access_loc).text
        customername_des = self.driver.find_element(*self.customer_name_des_loc).text
        firstname_des = self.driver.find_element(*self.first_name_des_loc).text
        back_btn_des = self.driver.find_element(*self.back_btn_loc).text
        save_btn_des = self.driver.find_element(*self.save_btn_loc).text
        print(edit_title,active_des,access_des,customername_des,firstname_des,back_btn_des,save_btn_des)
        return  edit_title,active_des,access_des,customername_des,firstname_des,back_btn_des,save_btn_des

    @property
    def check_active_status(self):
        '''Check the Active Status'''
        self.active_status = self.driver.find_element(*self.active_switch_loc)
        if self.active_status.is_enabled:
            # print('enabled')
            return True
        else:
            # print('disable')
            return False

    @property
    def check_active_off(self):
        '''Check the active off status'''
        self.active_status.click()
        active_off_des = self.driver.find_element(*self.active_loc).text
        print(active_off_des)
        return active_off_des



if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("http:// ")
    driver.implicitly_wait(10)

    login = Edit_Account_Customer(driver)
    login.typeUserName('aa@ecogaragedoors.com')
    login.typePassword('aabb')
    login.clickLogin()
    login.goto_account_customer()
    login.goto_edit_account()
    # login.check_edit_url
    login.check_general_elements
    # login.check_active_status
    # login.check_active_off
