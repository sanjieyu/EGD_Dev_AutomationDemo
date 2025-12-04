
# Author:Yi Sun(Tim) 2023-08-29

'''Login Page'''

from selenium.webdriver.common.by import By
from UIModule.basePage import *
from selenium import webdriver
from time import sleep

class Admin_Portal(WebDriver):
    '''input username, password'''
    username_loc = (By.XPATH,'//*[@id="Email"]')
    password_loc = (By.XPATH,'//*[@id="Password"]')
    login_loc = (By.XPATH,'//*[@id="loginForm"]/form/div[4]/div/input')
    '''forget password,submit username page'''
    # forgetpwd_loc = (By.XPATH,'/html/body/div/div/div[2]/div[2]/div[1]/button')
    # forgetusername_loc = (By.XPATH,'/html/body/div/div/div[2]/div/p')
    # forgetsubmit_loc = (By.XPATH,'/html/body/div/div/div[2]/button')
    # forgetdescription_loc = (By.XPATH,'/html/body/div/div/div[2]/div/p')
    # wrongemailwaring_loc = (By.XPATH,'/html/body/div/div/div[2]/div[1]')
    # inputemail_loc = (By.XPATH,'/html/body/div/div/div[2]/div/input')
    '''forget password,submit code page'''
    # forgetusernamesubmit_loc = (By.XPATH,'/html/body/div/div/div[2]/div[2]/input[1]')
    # forgetentercode_loc = (By.XPATH,'/html/body/div/div/div[2]/div[2]/input[2]')
    # forgetenternew_loc = (By.XPATH,'/html/body/div/div/div[2]/div[2]/input[3]')
    # passwordrequire_loc = (By.XPATH,'/html/body/div/div/div[2]/div[2]/p')
    # forgetsubmitbutton_loc = (By.XPATH,'/html/body/div/div/div[2]/button')


    def typeUserName(self,username):
        # self.driver.find_element(By.NAME,'email').send_keys(username)
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
        # print('login_error:',login_error)
        return login_error


    def clickForget(self):
        self.driver.find_element(*self.forgetpwd_loc).click()

    @property
    def getForget(self):
        '''Forget password description'''
        print('forgot username:',self.driver.find_element(*self.forgetdescription_loc).text)
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

    def submitusername(self):
        '''Forget password, submit username page'''
        self.driver.find_element(*self.inputemail_loc).send_keys('tim@itrazotracetech.com')
        self.driver.find_element(*self.forgetsubmit_loc).click()

    @property
    def submitcode_pwdrequire(self):
        '''Forget password, submit code page, pwd require check'''
        pwdrequire_string = self.driver.find_element(*self.passwordrequire_loc).text
        # print('pwdrequire is:',pwdrequire_string)
        return pwdrequire_string



if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("http:// ")
    driver.implicitly_wait(10)

    login = Admin_Portal(driver)
    login.typeUserName('aa@ecogaragedoors.com')
    login.typePassword('aabb')
    # login.typeUserName('sanjieyu')
    # login.typePassword('124')
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


