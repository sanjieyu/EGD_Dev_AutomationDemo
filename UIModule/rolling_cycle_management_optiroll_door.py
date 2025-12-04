# Author:Yi Sun(Tim) 2025-11-11

'''Rolling Cycle Management Page for OptiRoll Doors'''

import selenium
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from UIModule.admin_portal import *

class Rolling_Cycle_Management_Optiroll_Door(Admin_Page):

    rolling_title_optiroll_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/div[1]/h1')

    '''default section'''
    general_settings_optiroll_loc  = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/div[1]/div/ul/li[1]/a')
    colour_cycle_optiroll_settings_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/div[1]/div/ul/li[2]/a')
    temp_closed_optiroll_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/div[1]/div/ul/li[3]/a')
    history_optiroll_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/div[1]/div/ul/li[4]/a')

    '''General Settings tab'''
    split_doors_optiroll_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/div[1]/div/div/div[1]/form/h3[1]/span')
    lockout_settings_optiroll_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/div[1]/div/div/div[1]/form/h3[2]/span')
    default_shift_settings_optiroll_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/div[1]/div/div/div[1]/form/h3[4]/'
                                                    'span')

    '''Colour Cycles Settings screen'''
    coil_settings_optiroll_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/div[1]/div/div/div[2]/h3/span')
    save_coil_btn_optiroll_loc = (By.ID,'submitColourSettings')

    '''Temp closed screen'''
    temp_closed_cycles_optiroll_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/div[1]/div/div/div[3]/h3/span')
    update_cycles_btn_optiroll_loc = (By.ID,'submitClosedCycles')

    def go_optiroll(self):
        '''Switch to Rolling Cycle Management from Account Menu'''
        self.driver.find_element(*self.account_loc).click()
        self.driver.find_element(*self.rollcycle_loc).click()
        self.driver.find_element(*self.rollcycle_optirolldoors_loc).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.rolling_title_optiroll_loc))  #new added
        # sleep(2)


    @property
    def check_rolling_url(self):
        '''Check the URL'''
        rolling_url = self.driver.current_url
        print(rolling_url)
        return  rolling_url

    @property
    def check_rolling_title(self):
        '''Check the Title'''
        rolling_title = self.driver.find_element(*self.rolling_title_optiroll_loc).text
        print(rolling_title)
        return  rolling_title

    @property
    def check_tab(self):
        '''Check each tab'''
        general_settings_title = self.driver.find_element(*self.general_settings_optiroll_loc).text
        colour_cycles_settings_title = self.driver.find_element(*self.colour_cycle_optiroll_settings_loc).text
        temp_closed_title = self.driver.find_element(*self.temp_closed_optiroll_loc).text
        history_title = self.driver.find_element(*self.history_optiroll_loc).text
        print(general_settings_title,colour_cycles_settings_title,temp_closed_title,history_title)
        return general_settings_title,colour_cycles_settings_title,temp_closed_title,history_title

    @property
    def check_general_settings(self):
        '''Check the General Settings screen'''
        split_doors = self.driver.find_element(*self.split_doors_optiroll_loc).text
        lockout_settings = self.driver.find_element(*self.lockout_settings_optiroll_loc).text
        default_shift_settings = self.driver.find_element(*self.default_shift_settings_optiroll_loc).text
        print(split_doors,lockout_settings,default_shift_settings)
        return split_doors,lockout_settings,default_shift_settings

    @property
    def check_colour_cycle_settings(self):
        '''Check the Colour Cycle Settings screen'''
        self.driver.find_element(*self.colour_cycle_optiroll_settings_loc).click()
        coil_settings = self.driver.find_element(*self.coil_settings_optiroll_loc).text
        save_btn = self.driver.find_element(*self.save_coil_btn_optiroll_loc).text
        print(coil_settings,save_btn)
        return coil_settings,save_btn

    @property
    def check_temp_closed(self):
        '''Check the Temp Closed  screen'''
        self.driver.find_element(*self.temp_closed_optiroll_loc).click()
        temp_closed_cycles = self.driver.find_element(*self.temp_closed_cycles_optiroll_loc).text
        update_cycles_btn  = self.driver.find_element(*self.update_cycles_btn_optiroll_loc).text
        print(temp_closed_cycles,update_cycles_btn)
        return temp_closed_cycles,update_cycles_btn




if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("http:// ")
    driver.implicitly_wait(10)

    login = Rolling_Cycle_Management_OptiLift_Door(driver)
    login.typeUserName('aa@ecogaragedoors.com')
    login.typePassword('aabb')
    login.clickLogin()
    login.go_optiroll()
    login.check_rolling_url
    login.check_rolling_title
    login.check_tab
    # login.check_general_settings
    # login.check_colour_cycle_settings
    # login.check_temp_closed
#