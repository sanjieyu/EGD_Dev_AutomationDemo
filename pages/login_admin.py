
# Author:Yi Sun(Tim) 2023-08-29

'''Login Page'''

from selenium.webdriver.common.by import By
from pages.basePage import *
from selenium import webdriver
from time import sleep

class Admin_Portal(WebDriver):
    """
        Note: For security and confidentiality, specific XPath/CSS selectors
        have been replaced with 'test_sample', and additional private locators
        have been omitted from this public sample.
    """
    '''input username, password'''
    username_loc = (By.ID,'test_sample')
    password_loc = (By.NAME,'test_sample')
    login_loc = (By.CSS_SELECTOR, "[aria-label='test_sample']")

    def typeUserName(self,username):
        self.driver.find_element(*self.username_loc).send_keys(username)

    def typePassword(self,password):
        self.driver.find_element(*self.password_loc).send_keys(password)


    def clickLogin(self):
        self.driver.find_element(*self.login_loc).click()

    def login(self,username,password):
        self.typeUserName(username)
        self.typePassword(password)
        self.clickLogin()

    def getUsername(self):
        print('username is:',self.driver.find_element(*self.username_loc).text)
        return self.driver.find_element(*self.username_loc).text


    def getLoginError(self):
        '''Catch wrong info'''
        login_error = self.driver.find_element(*self.loginError_loc).text
        return login_error

    def clickForget(self):
        self.driver.find_element(*self.forgetpwd_loc).click()

    @property
    def getForget(self):
        '''Forget password description'''
        return self.driver.find_element(*self.forgetdescription_loc).text


    def submitwrongemail(self):
        '''Forget password, submit wrong emain in username page'''
        self.driver.find_element(*self.inputemail_loc).send_keys('ddd')
        self.driver.find_element(*self.forgetsubmit_loc).click()

    @property
    def submitwrongemail_description(self):
        '''Forget password, submit wrong emain in username page, description require check'''
        error_string = self.driver.find_element(*self.wrongemailwaring_loc).text
        print('pwdrequire is:',error_string)
        return error_string

if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("http://test_sample ")
    driver.implicitly_wait(10)

    login = Admin_Portal(driver)
    login.typeUserName('test_sample')
    login.typePassword('test_sample')
    login.clickLogin()
    # login.getUsername
    # login.getLoginError
    # login.getURL
    # login.clickForget()
    # login.getForget
    # login.submitusername()
    # login.submitcode_pwdrequire
    # login.crm_portal
    # login.submitusername()
    # login.submitcode_username
    # login.admin_portal


