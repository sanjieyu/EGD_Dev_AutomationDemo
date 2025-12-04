# Author:Yi Sun(Tim) 2025-3-26

'''Add a Shutter Door'''

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from UIModule.shutter_door import *

class Add_Shutter_Door(Shutter_Door):

    new_door_page_loc = (By.ID,'shutterDoorForm')
    new_door_title= (By.ID,'btnShowDoor')
    new_door_duplicate = (By.XPATH, '/html/body/div[3]/div[2]/div[1]/div/fieldset/div/div/div[1]/div/div/div/div[3]/a[1]')
    new_door_delete = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/div/fieldset/div/div/div[1]/div/div/div/div[3]/a[2]')

    '''loc for validation'''
    validation_msgbox_loc = (By.ID,'shutterErrorsBody')

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

    def add_shutter_detail(self):
        wait = WebDriverWait(self.driver,5)
        install_type_select = Select(self.driver.find_element(*self.install_type_select_loc))
        install_type_select.select_by_visible_text('Residential')
        slat_type_select = Select(self.driver.find_element(*self.slat_type_select_loc))
        slat_type_select.select_by_visible_text('100 x 0.8mm')
        self.driver.find_element(*self.opensize_lh_select_loc).clear()
        self.driver.find_element(*self.opensize_lh_select_loc).send_keys('4000')
        self.driver.find_element(*self.opensize_rh_select_loc).clear()
        self.driver.find_element(*self.opensize_rh_select_loc).send_keys('4000')
        self.driver.find_element(*self.opensize_width_select_loc).clear()
        self.driver.find_element(*self.opensize_width_select_loc).send_keys('5000')
        self.driver.find_element(*self.sr_left_select_loc).clear()
        self.driver.find_element(*self.sr_left_select_loc).send_keys('200')
        self.driver.find_element(*self.hr_select_loc).clear()
        self.driver.find_element(*self.hr_select_loc).send_keys('300')
        self.driver.find_element(*self.sr_right_select_loc).clear()
        self.driver.find_element(*self.sr_right_select_loc).send_keys('200')
        opener_select = Select(self.driver.find_element(*self.opener_select_loc))
        opener_select.select_by_visible_text('Reuse Existing Motor Only')
        track_select = Select(self.driver.find_element(*self.track_select_loc))
        track_select.select_by_visible_text('100mm Upgrade')
        new_door_page = self.driver.find_element(*self.new_door_page_loc)
        self.driver.execute_script("arguments[0].scrollIntoView(false);", new_door_page)  # 滚动条拉到Form最下面
        self.driver.find_element(*self.add_btn_loc).click()

    @property
    def new_added_shutterdoor(self):
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
        driver.get("http:// ")
        driver.implicitly_wait(10)

        login = Add_Shutter_Door(driver)
        login.typeUserName('aa@ecogaragedoors.com')
        login.typePassword('aabb')
        login.clickLogin()
        login.go_addquote()
        login.go_add_shutter_door()
        # login.validation_input
        login.add_shutter_detail()
        login.new_added_shutterdoor
        # login.duplicate_btn
        # login.delete_btn
