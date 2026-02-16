# Author:Yi Sun(Tim) 2024-5-21

'''SMS Notification Page'''

import selenium
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from pages.admin_portal import *

class SMS_Notification(Admin_Page):
    """
        Note: For security and confidentiality, specific XPath/CSS selectors
        have been replaced with 'test_sample', and additional private locators
        have been omitted from this public sample.
    """
    sms_title_loc = (By.CSS_SELECTOR,"label[for='test_sample']")
    apikey_box_loc =(By.ID,'test_sample')
    pwd_box_loc = (By.ID,'test_sample')
    from_box_loc = (By.ID,'test_sample')
    # [Remaining 10+ locators redacted for confidentiality]
    '''mlb install tab'''


    def go_sms_notification(self):
        '''Switch to SMS Notification Page from Account Menu'''
        self.driver.find_element(*self.account_loc).click()
        self.driver.find_element(*self.sms_loc).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.sms_title_loc))
        # sleep(2)

    @property
    def check_sms_url(self):
        '''Check the URL'''
        sms_url = self.driver.current_url
        return  sms_url

    @property
    def check_sms_title(self):
        '''Check the Title'''
        sms_title = self.driver.find_element(*self.sms_title_loc).text
        return  sms_title

    @property
    def check_default_value(self):
        '''Check the default value'''
        apikey_value = self.driver.find_element(*self.apikey_box_loc).get_attribute('value')
        pwd_value = self.driver.find_element(*self.pwd_box_loc).get_attribute('value')
        from_value = self.driver.find_element(*self.from_box_loc).get_attribute('value')
        return apikey_value,pwd_value,from_value

    @property
    def check_apikey_disable(self):
        '''Check the apikey box status'''
        apikey_status = self.driver.find_element(*self.apikey_box_loc)
        if apikey_status.is_enabled():
            return True
        else:
            return False


if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("http://test_sample")
    driver.implicitly_wait(10)
    login = SMS_Notification(driver)
    login.typeUserName('test_sample')
    login.typePassword('test_sample')
    login.clickLogin()
    login.go_sms_notification()