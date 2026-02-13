# Author:Yi Sun(Tim) 2024-03-13

'''Dealer Portal Page'''

import selenium
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from pages.admin_portal import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class Deal_Portal(Admin_Page):

    '''loc for the dealer portal page'''
    find_quote_box = (By.XPATH,'//*[@id="search-quote"]')
    find_quote_btn = (By.XPATH,'//*[@id="search-btn"]/span')
    account_dealer_loc = (By.XPATH,'//*[@id="logoutForm"]/ul/li/a')

    '''loc for Add btn'''
    add_dealer_quote_loc = (By.CSS_SELECTOR,"label[for='AddDealer']")

    '''loc for Search btn'''
    list_dealer_quote_loc = (By.CSS_SELECTOR,"label[for='ListDealer']")


    '''loc for Account menu'''
    account_name_loc  = (By.CSS_SELECTOR,"label[for='AccountName']")
    log_off_loc = (By.CSS_SELECTOR,"label[for='LogOff']")


    @property
    def check_dealer_url(self):
        # sleep(2)
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.add_dealer_quote_loc)) #new added
        dealer_url = self.driver.current_url
        print(dealer_url)
        return dealer_url

    @property
    def check_default_values(self):
        add_quote = self.driver.find_element(*self.add_dealer_quote_loc).text
        search_quote = self.driver.find_element(*self.list_dealer_quote_loc).text
        account_menu = self.driver.find_element(*self.account_loc).text
        print(add_quote,search_quote,account_menu)
        return  add_quote,search_quote,account_menu

    @property
    def check_find_dealer_quote(self):
        find_dealer_quote = self.driver.find_element(*self.find_quote_box)
        if find_dealer_quote.is_displayed():
            print('true')
            return  True
        else:
            print('false')
            return False

    @property
    def check_account_menu(self):
        self.driver.find_element(*self.account_loc).click()
        account_name = self.driver.find_element(*self.account_name_loc).text
        logoff = self.driver.find_element(*self.log_off_loc).text
        print(account_name,logoff)
        return  account_name,logoff


if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("http:// ")
    driver.implicitly_wait(10)

    login = Deal_Portal(driver)
    login.typeUserName('aa@ecogaragedoors.com')
    login.typePassword('aabb')
    login.clickLogin()
    login.check_dealer_url
    login.check_default_values
    login.check_find_dealer_quote
    login.check_account_menu
