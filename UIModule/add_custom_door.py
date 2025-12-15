# Author:Yi Sun(Tim) 2025-4-16

'''Add a Custom Door'''

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from UIModule.custom_door import *

class Add_Custom_Door(Custom_Door):

    new_door_page_loc = (By.ID,'customDoorForm')
    new_door_title= (By.ID,'btnShowDoor')
    new_door_duplicate = (By.CSS_SELECTOR, 'a.glyphicon.glyphicon-duplicate')
    new_door_delete = (By.CSS_SELECTOR, 'a.glyphicon.glyphicon-remove.aware-btn.left-padding')

    '''loc for validation'''
    validation_msgbox_loc = (By.ID,'customErrorsBody')

    '''Check the input validateiong'''
    @property
    def validation_input(self):
        new_door_page = self.driver.find_element(*self.new_door_page_loc)
        self.driver.execute_script("arguments[0].scrollIntoView(false);", new_door_page)  # 滚动条拉到Form最下面
        self.driver.find_element(*self.add_btn_loc).click()
        msg_error = self.driver.find_element(*self.validation_msgbox_loc).text
        print(msg_error)
        return msg_error


    '''Input the necesary details for a door'''

    def add_custom_detail(self):
        wait = WebDriverWait(self.driver,5)
        install_type_select = Select(self.driver.find_element(*self.install_type_select))
        install_type_select.select_by_visible_text('Residential')
        design_select = Select(self.driver.find_element(*self.design_select))
        design_select.select_by_visible_text('Aliwood')
        colour_category_select = Select(self.driver.find_element(*self.colour_category_select))
        colour_category_select.select_by_visible_text('OilColour')
        self.driver.find_element(*self.opensize_lh_select).clear()
        self.driver.find_element(*self.opensize_lh_select).send_keys('2800')
        self.driver.find_element(*self.opensize_rh_select).clear()
        self.driver.find_element(*self.opensize_rh_select).send_keys('2800')
        self.driver.find_element(*self.opensize_width_select).clear()
        self.driver.find_element(*self.opensize_width_select).send_keys('5510')
        self.driver.find_element(*self.sr_left_select).clear()
        self.driver.find_element(*self.sr_left_select).send_keys('200')
        self.driver.find_element(*self.hr_select).clear()
        self.driver.find_element(*self.hr_select).send_keys('400')
        self.driver.find_element(*self.sr_right_select).clear()
        self.driver.find_element(*self.sr_right_select).send_keys('200')
        self.driver.find_element(*self.panel_wide_btn_loc).click()
        panels_wide = self.driver.find_element(*self.panel_wide_input_loc)
        panels_wide.send_keys('1 Panel Wide')
        opener = Select(self.driver.find_element(*self.opener_select))
        opener.select_by_visible_text('Lock Only')
        new_door_page = self.driver.find_element(*self.new_door_page_loc)
        self.driver.execute_script("arguments[0].scrollIntoView(false);", new_door_page)  # 滚动条拉到Form最下面
        self.driver.find_element(*self.add_btn_loc).click()

    @property
    def new_added_custom_door(self):
        door_title = self.driver.find_element(*self.new_door_title).text
        print(door_title)
        return door_title

    @property
    def duplicate_btn(self):
        door_duplicate = self.driver.find_element(*self.new_door_duplicate)
        if door_duplicate.is_displayed():
            print('true')
            return True
        else:
            print('false')
            return False
    @property
    def delete_btn(self):
        door_delete = self.driver.find_element(*self.new_door_delete)
        if door_delete.is_displayed():
            print('true')
            return True
        else:
            print('false')
            return False




if __name__ == '__main__':
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get("http://aa")
        driver.implicitly_wait(10)

        login = Add_Custom_Door(driver)
        login.typeUserName('aa@ecogaragedoors.com')
        login.typePassword('aabb')
        login.clickLogin()
        login.go_addquote()
        login.go_addcustomdoor()
        login.validation_input
        # login.add_custom_detail()
        # login.new_added_custom_door
        # login.duplicate_btn
        # login.delete_btn
