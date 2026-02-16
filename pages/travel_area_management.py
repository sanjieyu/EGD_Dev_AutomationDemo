# Author:Yi Sun(Tim) 2024-5-20

'''Travel Area Management Page'''

import selenium
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from pages.admin_portal import *

class Travel_Area_Management(Admin_Page):
    """
        Note: For security and confidentiality, specific XPath/CSS selectors
        have been replaced with 'test_sample', and additional private locators
        have been omitted from this public sample.
    """
    travel_area_title_loc = (By.NAME,'test_sample')
    new_btn_loc = (By.ID,'test_sample')
    search_result_suburb_loc = (By.CSS_SELECTOR, "[aria-label='test_sample']")
    # [Remaining 10+ locators redacted for confidentiality]
    '''new page'''

    def go_travel_area_management(self):
        '''Switch to Travel Area Management Page from Account Menu'''
        self.driver.find_element(*self.account_loc).click()
        self.driver.find_element(*self.travel_area_loc).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.travel_area_title_loc))

    @property
    def check_travel_area_url(self):
        '''Check the URL'''
        travel_area_url = self.driver.current_url
        return  travel_area_url

    @property
    def check_travel_area_title(self):
        '''Check the Title'''
        travel_area_title = self.driver.find_element(*self.travel_area_title_loc).text
        return  travel_area_title

    @property
    def check_new_button(self):
        '''Check the New button'''
        new_button = self.driver.find_element(*self.new_btn_loc)
        if new_button.is_displayed:
            return True
        else:
            return False


    @property
    def check_search_result(self):
        '''Check the search result for postcode 7879'''
        self.driver.find_element(*self.search_box_loc).send_keys("test_sample")
        suburb_name = self.driver.find_element(*self.search_result_suburb_loc).text
        return  suburb_name

    @property
    def check_new_screen(self):
        ''''Check the Add New Area screen'''
        self.driver.find_element(*self.new_btn_loc).click()
        self.driver.switch_to.window(self.driver.window_handles[-1])  # switch to new page
        new_title = self.driver.find_element(*self.new_title_loc).text
        return new_title

    @property
    def check_new_save_btn(self):
        ''''Check Save in the Add New Area screen'''
        self.driver.find_element(*self.new_btn_loc).click()
        self.driver.switch_to.window(self.driver.window_handles[-1])  # switch to new page
        new_save_btn = self.driver.find_element(*self.new_save_btn_loc)
        if new_save_btn.is_displayed:
            return True
        else:
            return False

    @property
    def check_new_close_btn(self):
        ''''Check Close in the Add New Area screen'''
        # self.driver.find_element(*self.new_btn_loc).click()
        # self.driver.switch_to.window(self.driver.window_handles[-1])  # switch to new page
        new_close_btn = self.driver.find_element(*self.new_close_btn_loc)
        if new_close_btn.is_displayed:
            return True
        else:
            return False

if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("http://test_sample ")
    driver.implicitly_wait(10)
    login = Travel_Area_Management(driver)
    login.typeUserName('test_sample')
    login.typePassword('test_sample')
    login.clickLogin()
    login.go_travel_area_management()