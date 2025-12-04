# Author:Yi Sun(Tim) 2023-11-27

'''Add Service Item window'''

import selenium
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from UIModule.add_service import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class Add_Service_Item(Add_Service):
    '''loc for each section in this page'''
    item_title_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/div[2]/div/div/div/div[1]/h1')
    item_search_box = (By.ID,'searchTextInputServiceItem')
    view_more_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/div[2]/div/div/div/div[2]/div[2]/table/thead/tr/th[1]')
    item_type_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/div[2]/div/div/div/div[2]/div[2]/table/thead/tr/th[2]')
    item_select_btn = (By.ID,'btnSelectServiceItem')
    item_close_btn = (By.ID,'btnCloseServiceItem')

    service_charges_radiobox = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/div[2]/div/div/div/div[2]/div[2]/table/tbody/'
                                         'tr[1]/td[1]/button/span')
    res_rt_checkbox = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/div[2]/div/div/div/div[2]/div[2]/table/tbody/tr[2]/td/'
                                'div/table/tbody/tr[1]/td[1]/input')

    '''after service "S-Res-ST" added'''
    added_item_name = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/div[1]/div/div[4]/div/div/div[1]/table/tbody/tr/td[4]')
    discount_loc = (By.NAME,'discount')

    def go_service_item(self):
        '''Switch to Add Service Item from Add Service page'''
        self.driver.find_element(*self.add_service_item_btn).click()
        sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[-1])   # switch to the add door details page


    @property
    def check_add_item_title(self):
        '''check the title for Add Service Item page'''
        service_item_title = self.driver.find_element(*self.item_title_loc).text
        print(service_item_title)
        return service_item_title

    @property
    def check_item_sections(self):
        '''check each section in Add Service Item page'''
        view_more = self.driver.find_element(*self.view_more_loc).text
        item_type = self.driver.find_element(*self.item_type_loc).text
        print(view_more,item_type)
        return view_more,item_type


    @property
    def check_item_select_btn(self):
        '''check Item Select button in this page'''
        item_select_btn = self.driver.find_element(*self.item_select_btn)
        if item_select_btn.is_displayed() and item_select_btn.is_enabled():
            print("Button is present and visible")
            return True
        else:
            print('Button is not present or visible')
            return False

    @property
    def check_item_close_btn(self):
        '''check Close button in this page'''
        item_close_btn = self.driver.find_element(*self.item_close_btn)
        if item_close_btn.is_displayed() and item_close_btn.is_enabled():
            print("Button is present and visible")
            return True
        else:
            print('Button is not present or visible')
            return False

    @property
    def check_search_item_box(self):
        '''check the Search box in this page'''
        search_item_box = self.driver.find_element(*self.item_search_box)
        if search_item_box.is_displayed:
            print('yes')
            return  True
        else:
            print('no')
            return  False

    @property
    def add_item_success(self):
        '''Select servie items then add'''
        self.driver.find_element(*self.service_charges_radiobox).click()
        self.driver.find_element(*self.res_rt_checkbox).click()
        self.driver.find_element(*self.discount_loc).clear()
        self.driver.find_element(*self.discount_loc).send_keys('90')
        sleep(1)
        self.driver.find_element(*self.item_select_btn).click()
        added_success = self.driver.find_element(*self.added_item_name).text
        print(added_success)
        return added_success


if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("http:// ")
    driver.implicitly_wait(10)

    login = Add_Service_Item(driver)
    login.typeUserName('aa@ecogaragedoors.com')
    login.typePassword('aabb')
    login.clickLogin()
    login.go_addservice()
    login.go_service_item()
    # login.check_add_item_title
    # login.check_item_sections
    # login.check_item_select_btn
    # login.check_item_close_btn
    # login.check_search_item_box
    # login.add_service_item
    login.add_item_success