# Author:Yi Sun(Tim) 2025-10-14

'''Add a OptiRoll Door'''

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from UIModule.standard_door import *
from selenium.webdriver.common.keys import Keys

class Add_OptiRoll_Door(Standard_Door):

    new_door_page_loc = (By.ID, 'quickDoorAddModalBody')
    new_door_title = (By.NAME, 'DoorTitle')
    new_door_duplicate = (By.CSS_SELECTOR, "[aria-label='duplicate']")
    new_door_delete = (By.ID, 'deletedoor')

    '''Input the necesary details for a OptiLift door'''
    def add_optiroll_door(self):
        # self.driver.find_element(*self.install_type_select).click()
        wait = WebDriverWait(self.driver,5)
        install_type_select = Select(self.driver.find_element(*self.install_type_select))
        install_type_select.select_by_visible_text('Commercial Cat 1')
        door_type_select = Select(self.driver.find_element(*self.door_type_select))
        door_type_select.select_by_visible_text('OptiRoll')
        design_select = Select(wait.until(EC.presence_of_element_located(self.design_select)))
        design_select.select_by_visible_text('OptiRoll eS')
        colour_category_select = Select(self.driver.find_element(*self.colour_category_select))
        colour_category_select.select_by_visible_text('ColorBond')
        door_colour_select = Select(wait.until(EC.presence_of_element_located(self.door_colour_select)))
        door_colour_select.select_by_visible_text('Monument')
        door_finish_select = Select(self.driver.find_element(*self.door_finish_select))
        door_finish_select.select_by_visible_text('Smooth Texture')
        self.driver.find_element(*self.opensize_lh_select).clear()
        self.driver.find_element(*self.opensize_lh_select).send_keys('2100')
        self.driver.find_element(*self.opensize_rh_select).clear()
        self.driver.find_element(*self.opensize_rh_select).send_keys('2100')
        self.driver.find_element(*self.opensize_width_select).clear()
        self.driver.find_element(*self.opensize_width_select).send_keys('2950')
        self.driver.find_element(*self.sr_left_select).clear()
        self.driver.find_element(*self.sr_left_select).send_keys('200')
        self.driver.find_element(*self.hr_select).clear()
        self.driver.find_element(*self.hr_select).send_keys('400')
        self.driver.find_element(*self.sr_right_select).clear()
        self.driver.find_element(*self.sr_right_select).send_keys('200')
        opener_select = Select(self.driver.find_element(*self.opener_select))
        opener_select.select_by_visible_text('Use Existing')
        new_door_page = self.driver.find_element(*self.new_door_page_loc)
        self.driver.execute_script("arguments[0].scrollIntoView(false);", new_door_page)  # 滚动条拉到Form最下面
        self.driver.find_element(*self.add_standarddoor_btn).click()


    @property
    def new_added_door(self):
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
    driver.get("http://egd2.sighte.com/")
    driver.implicitly_wait(10)

    login = Add_OptiRoll_Door(driver)
    login.typeUserName('ysun@ecogaragedoors.com.au')
    login.typePassword('Tims@123')
    login.clickLogin()
    login.go_addquote()
    login.go_addstandarddoor()
    login.add_optiroll_door()
    login.new_added_door
    login.duplicate_btn