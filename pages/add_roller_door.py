# Author:Yi Sun(Tim) 2024-8-29

'''Add a Roller Door'''

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from pages.standard_door import *
from selenium.webdriver.common.keys import Keys

class Add_Roller_Door(Standard_Door):

    new_door_page_loc = (By.ID, 'quickDoorAddModalBody')
    new_door_title = (By.NAME, 'DoorTitle')
    new_door_duplicate = (By.CSS_SELECTOR, "[aria-label='duplicate']")
    new_door_delete = (By.ID, 'deletedoor')
    default_track_box_loc = (By.ID,'DefaultTrack')

    '''Input the necesary details for a roller door'''
    def add_roller_door(self):
        # self.driver.find_element(*self.install_type_select).click()
        wait = WebDriverWait(self.driver,5)
        install_type_select = Select(self.driver.find_element(*self.install_type_select))
        install_type_select.select_by_visible_text('Commercial Cat 1')
        door_type_select = Select(self.driver.find_element(*self.door_type_select))
        door_type_select.select_by_visible_text('ExoRoll')
        design_select = Select(wait.until(EC.presence_of_element_located(self.design_select)))
        design_select.select_by_visible_text('ExoRoll eC')
        colour_category_select = Select(self.driver.find_element(*self.colour_category_select))
        colour_category_select.select_by_visible_text('ColorBond')
        door_colour_select = Select(wait.until(EC.presence_of_element_located(self.door_colour_select)))
        door_colour_select.select_by_visible_text('Monument')
        door_finish_select = Select(self.driver.find_element(*self.door_finish_select))
        door_finish_select.select_by_visible_text('Smooth Texture')
        self.driver.find_element(*self.opensize_lh_select).clear()
        self.driver.find_element(*self.opensize_lh_select).send_keys('3100')
        self.driver.find_element(*self.opensize_rh_select).clear()
        self.driver.find_element(*self.opensize_rh_select).send_keys('3100')
        self.driver.find_element(*self.opensize_width_select).clear()
        self.driver.find_element(*self.opensize_width_select).send_keys('2500')
        self.driver.find_element(*self.sr_left_select).clear()
        self.driver.find_element(*self.sr_left_select).send_keys('200')
        self.driver.find_element(*self.hr_select).clear()
        self.driver.find_element(*self.hr_select).send_keys('200')
        self.driver.find_element(*self.sr_right_select).clear()
        self.driver.find_element(*self.sr_right_select).send_keys('200')
        opener_select = Select(self.driver.find_element(*self.opener_select))
        opener_select.select_by_visible_text('Use Existing')
        new_door_page = self.driver.find_element(*self.new_door_page_loc)
        self.driver.execute_script("arguments[0].scrollIntoView(false);", new_door_page)  # 滚动条拉到Form最下面
        self.driver.find_element(*self.add_standarddoor_btn).click()
        # self.driver.switch_to.window(self.driver.window_handles[0])     #回到之前的quote页面

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

    @property
    def track_t35(self):
        # self.driver.find_element(*self.install_type_select).click()
        wait = WebDriverWait(self.driver,5)
        door_type_select = Select(self.driver.find_element(*self.door_type_select))
        door_type_select.select_by_visible_text('ExoRoll')
        design_select = Select(wait.until(EC.presence_of_element_located(self.design_select)))
        design_select.select_by_visible_text('ExoRoll eC')
        colour_category_select = Select(self.driver.find_element(*self.colour_category_select))
        colour_category_select.select_by_visible_text('ColorBond')
        door_colour_select = Select(wait.until(EC.presence_of_element_located(self.door_colour_select)))
        door_colour_select.select_by_visible_text('Monument')
        door_finish_select = Select(self.driver.find_element(*self.door_finish_select))
        door_finish_select.select_by_visible_text('Smooth Texture')
        self.driver.find_element(*self.opensize_lh_select).clear()
        self.driver.find_element(*self.opensize_lh_select).send_keys('2000')
        self.driver.find_element(*self.opensize_rh_select).clear()
        self.driver.find_element(*self.opensize_rh_select).send_keys('2000')
        self.driver.find_element(*self.opensize_width_select).clear()
        self.driver.find_element(*self.opensize_width_select).send_keys('2500')
        self.driver.find_element(*self.sr_left_select).clear()
        self.driver.find_element(*self.sr_left_select).send_keys('200')
        self.driver.find_element(*self.hr_select).clear()
        self.driver.find_element(*self.hr_select).send_keys('200')
        self.driver.find_element(*self.sr_right_select).clear()
        self.driver.find_element(*self.sr_right_select).send_keys('200')
        default_track_box = self.driver.find_element(*self.default_track_box_loc)
        default_track_value = default_track_box.get_attribute('value')
        print(default_track_value)
        return default_track_value

    @property
    def track_t50(self):
        sleep(1)
        self.driver.find_element(*self.opensize_lh_select).clear()
        self.driver.find_element(*self.opensize_lh_select).send_keys('3000')
        self.driver.find_element(*self.opensize_rh_select).clear()
        self.driver.find_element(*self.opensize_rh_select).send_keys('3000')
        self.driver.find_element(*self.opensize_width_select).clear()
        self.driver.find_element(*self.opensize_width_select).send_keys('4101')
        self.driver.find_element(*self.hr_select).send_keys(Keys.RETURN)     #需要在页面某一个地方click或者回车一下，不然不会更新
        default_track_box = self.driver.find_element(*self.default_track_box_loc)
        default_track_value = default_track_box.get_attribute('value')
        print(default_track_value)
        return default_track_value


    @property
    def track_t60(self):
        sleep(1)
        self.driver.find_element(*self.opensize_lh_select).clear()
        self.driver.find_element(*self.opensize_lh_select).send_keys('3500')
        self.driver.find_element(*self.opensize_rh_select).clear()
        self.driver.find_element(*self.opensize_rh_select).send_keys('3500')
        self.driver.find_element(*self.opensize_width_select).clear()
        self.driver.find_element(*self.opensize_width_select).send_keys('4101')
        self.driver.find_element(*self.hr_select).send_keys(Keys.RETURN)     #需要在页面某一个地方click或者回车一下，不然不会更新
        default_track_box = self.driver.find_element(*self.default_track_box_loc)
        default_track_value = default_track_box.get_attribute('value')
        print(default_track_value)
        return default_track_value


if __name__ == '__main__':
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get("http:// ")
        driver.implicitly_wait(10)

        login = Add_Roller_Door(driver)
        login.typeUserName('aa@ecogaragedoors.com')
        login.typePassword('aabb')
        login.clickLogin()
        login.go_addquote()
        login.go_addstandarddoor()
        # login.add_roller_door()
        # login.validation_input
        # login.add_door
        # login.new_added_door
        # login.duplicate_btn
        login.track_t35
        login.track_t50
        login.track_t60



