# Author:Yi Sun(Tim) 2023-2-11

'''Add a Dealer Roller Door'''

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from pages.dealer_roller_door import *

class Add_DP_Roller(Dealer_Roller_Door):
    new_door_page_loc = (By.ID,'quickDoorAddModalBody')
    new_door_title= (By.XPATH,'//*[@id="btnShowDoor"]')
    new_door_duplicate = (By.CSS_SELECTOR, "[aria-label='duplicate']")
    new_door_delete = (By.ID,'deletedoor')

    '''loc for validation'''
    validation_msgbox_loc = (By.ID,'doorerrormsgs_body')

    '''Check the input validateiong'''
    @property
    def validation_input(self):
        new_door_page = self.driver.find_element(*self.new_door_page_loc)
        self.driver.execute_script("arguments[0].scrollIntoView(false);", new_door_page)  # 滚动条拉到Form最下面
        self.driver.find_element(*self.add_rollerdoor_btn_loc).click()
        msg_error = self.driver.find_element(*self.validation_msgbox_loc).text
        print(msg_error)
        return msg_error

    '''Input the necesary details for a door'''
    def add_dealer_roller_door(self):
        wait = WebDriverWait(self.driver, 5)
        design_select = Select(wait.until(EC.presence_of_element_located(self.design_select_loc)))
        design_select.select_by_visible_text('ExoRoll eS')
        colour_category_select = Select(self.driver.find_element(*self.colour_category_select_loc))
        colour_category_select.select_by_visible_text('ColorBond')
        door_colour_select = Select(wait.until(EC.presence_of_element_located(self.door_colour_select_loc)))
        door_colour_select.select_by_visible_text('Monument')
        door_finish_select = Select(self.driver.find_element(*self.door_finish_select_loc))
        door_finish_select.select_by_visible_text('Smooth Texture')
        self.driver.find_element(*self.size_lh_box_loc).clear()
        self.driver.find_element(*self.size_lh_box_loc).send_keys('2200')
        self.driver.find_element(*self.size_rh_box_loc).clear()
        self.driver.find_element(*self.size_rh_box_loc).send_keys('2200')
        self.driver.find_element(*self.size_width_box_loc).clear()
        self.driver.find_element(*self.size_width_box_loc).send_keys('3000')
        self.driver.find_element(*self.seals_quantity_2500_loc).clear()
        self.driver.find_element(*self.seals_quantity_2500_loc).send_keys('2')
        opener_select = Select(self.driver.find_element(*self.open_box_loc))
        opener_select.select_by_visible_text('Manual/No Opener or Lock')
        new_door_page = self.driver.find_element(*self.new_door_page_loc)
        self.driver.execute_script("arguments[0].scrollIntoView(false);", new_door_page)  # 滚动条拉到Form最下面
        self.driver.find_element(*self.add_rollerdoor_btn_loc).click()

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
        driver.get("http://xxxxx/")
        driver.implicitly_wait(10)

        login = Add_DP_Roller(driver)
        login.typeUserName('xxx@xxx.com')
        login.typePassword('xxxx!')
        login.clickLogin()
        login.creat_quote()
        login.go_roller_door()
        login.validation_input
        # login.add_dealer_roller_door()
        # login.new_added_door
        # login.duplicate_btn

