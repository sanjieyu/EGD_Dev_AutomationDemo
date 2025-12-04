# Author:Yi Sun(Tim) 2024-5-21

'''SMS Notification Page'''

import selenium
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from UIModule.admin_portal import *

class SMS_Notification(Admin_Page):

    sms_title_loc = (By.XPATH,'/html/body/div[3]/div[2]/div/h1')
    apikey_box_loc =(By.ID,'APIKEYInput')
    pwd_box_loc = (By.ID,'PasswordInput')
    from_box_loc = (By.ID,'FromNumberinput')

    mlb_tab_loc = (By.XPATH,'/html/body/div[3]/div[2]/div/div/form/ul/li[1]/a')
    syd_tab_loc = (By.XPATH,'/html/body/div[3]/div[2]/div/div/form/ul/li[2]/a')

    '''mlb install tab'''
    production_enter_loc = (By.CSS_SELECTOR,'#MLBInstallTab > div:nth-child(1) > div:nth-child(2) > label:nth-child(1)')
    production_rollforming_loc = (By.CSS_SELECTOR,'#MLBInstallTab > div:nth-child(4) > div:nth-child(2) > label:nth-child(1)')
    production_qc_loc = (By.CSS_SELECTOR,'#MLBInstallTab > div:nth-child(7) > div:nth-child(2) > label:nth-child(1)')

    def go_sms_notification(self):
        '''Switch to SMS Notification Page from Account Menu'''
        self.driver.find_element(*self.account_loc).click()
        self.driver.find_element(*self.sms_loc).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.sms_title_loc))  # new added
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

    @property
    def check_pwd_disable(self):
        '''Check the pwd box status'''
        pwd_status = self.driver.find_element(*self.pwd_box_loc)
        if pwd_status.is_enabled():
            return True
        else:
            return False

    @property
    def check_from_disable(self):
        '''Check the from box status'''
        from_status = self.driver.find_element(*self.from_box_loc)
        if from_status.is_enabled():
            return True
        else:
            return False

    @property
    def check_tab(self):
        '''Check the tab screen'''
        mlb_tab = self.driver.find_element(*self.mlb_tab_loc).text
        syd_tab = self.driver.find_element(*self.syd_tab_loc).text
        print(mlb_tab,syd_tab)
        return mlb_tab,syd_tab

    @property
    def check_mlb_enter(self):
        '''Check the Production Enter in MLB-Install tab screen'''
        production_enter = self.driver.find_element(*self.production_enter_loc).text
        print(production_enter)
        return production_enter

    @property
    def check_mlb_rollforming(self):
        '''Check the Production Rollforming in MLB-Install tab screen'''
        production_rollforming = self.driver.find_element(*self.production_rollforming_loc).text
        print(production_rollforming)
        return production_rollforming

    @property
    def check_mlb_qcpass(self):
        '''Check the Production QC Pass in MLB-Install tab screen'''
        production_qcpass = self.driver.find_element(*self.production_qc_loc).text
        print(production_qcpass)
        return production_qcpass

if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("http:// ")
    driver.implicitly_wait(10)

    login = SMS_Notification(driver)
    login.typeUserName('aa@ecogaragedoors.com')
    login.typePassword('aabb')
    login.clickLogin()
    login.go_sms_notification()
    # login.check_sms_url
    # login.check_sms_title
    # login.check_default_value
    # login.check_apikey_disable
    # login.check_pwd_disable
    # login.check_from_disable
    # login.check_tab
    login.check_mlb_install