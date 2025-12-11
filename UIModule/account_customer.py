# Author:Yi Sun(Tim) 2024-08-05

'''Account Customer Page'''

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from UIModule.admin_portal import *
from selenium.webdriver.support import expected_conditions as EC

class Account_Customer(Admin_Page):
    '''loc for the Account Customer page'''
    account_title_loc = (By.CSS_SELECTOR, "[data-test='login-submit']")
    account_searchbtn_loc = (By.CSS_SELECTOR, ".btn.btn-search")
    account_searchbox_loc = (By.ID,'searchCustomerName')

    customer_name_loc = (By.ID,'customername')
    contact_name_loc = (By.XPATH,"//div[contains(@class,'cname')]")
    address_loc = (By.NAME,"address")
    email_loc = (By.NAME,"email")
    suburb_loc = (By.NAME,"suburb")
    search_result_name_loc = (By.ID,"searchCustomerResult")

    def goto_account_customer(self):
        '''Go to account customer screen'''
        self.driver.find_element(*self.list_loc).click()
        self.driver.find_element(*self.account_list_loc).click()
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((self.account_title_loc)))
        # sleep(2)

    @property
    def check_accountcustomer_url(self):
        '''Check the url'''
        account_customer_url = self.driver.current_url
        print(account_customer_url)
        return account_customer_url

    @property
    def check_accountcustomer_title(self):
        '''Check the title'''
        account_customer_title = self.driver.find_element(*self.account_title_loc).text
        print(account_customer_title)
        return  account_customer_title

    @property
    def check_search_btn(self):
        '''Check the search button'''
        account_btn = self.driver.find_element(*self.account_searchbtn_loc)
        if account_btn.is_displayed:
            print('is there')
            return True
        else:
            print('not there')
            return False

    @property
    def check_searchbox(self):
        '''Check the search box'''
        search_box = self.driver.find_element(*self.account_searchbox_loc)
        if search_box.is_displayed:
            return True
        else:
            return False

    @property
    def check_columns(self):
        '''Check each column on the screen'''
        customer_name = self.driver.find_element(*self.customer_name_loc).text
        contact_name = self.driver.find_element(*self.contact_name_loc).text
        address = self.driver.find_element(*self.address_loc).text
        email = self.driver.find_element(*self.email_loc).text
        suburb = self.driver.find_element(*self.suburb_loc).text
        print(customer_name,contact_name,address,email,suburb)
        return customer_name,contact_name,address,email,suburb

    @property
    def check_search_result(self):
        '''Check the Search function'''
        self.driver.find_element(*self.account_searchbox_loc).send_keys('tim2')
        sleep(3)
        self.driver.find_element(*self.account_searchbtn_loc).click()
        sleep(3)
        # search_result_name = WebDriverWait(self.driver,4).until(EC.visibility_of_element_located(self.search_result_name_loc)).text
        search_result_name = self.driver.find_element(*self.search_result_name_loc).text
        print(search_result_name)
        return search_result_name




if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("http://aa")
    driver.implicitly_wait(10)

    login = Account_Customer(driver)
    login.typeUserName('aa@ecogaragedoors.com')
    login.typePassword('aabb')
    login.clickLogin()
    login.goto_account_customer
    # login.check_accountcustomer_url
    # login.check_accountcustomer_title
    # login.check_columns
    # login.check_search_result
