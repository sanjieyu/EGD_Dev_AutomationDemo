# Author:Yi Sun(Tim) 2023-11-16

'''Production Page'''

import selenium
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from UIModule.admin_portal import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class Production(Admin_Page):

    production_title_loc = (By.CSS_SELECTOR, "[aria-label='title']")

    '''loc for each section in this page'''
    roller_doors_loc = (By.XPATH, '//*[@id="roller"]/div/span')
    panel_lift_loc = (By.XPATH, '//*[@id="panelift"]/div/span')
    insulated_doors_loc = (By.XPATH, '//*[@id="insulated"]/div/span')
    custom_doors_loc = (By.XPATH, '//*[@id="custom"]/div/span')
    roller_shutters_loc = (By.XPATH, '//*[@id="shutter"]/div/span')
    all_doors_loc = (By.XPATH, '//*[@id="alldoors"]/div/span')

    def go_production(self):
        '''Switch to Production from LIST Menu'''
        self.driver.find_element(*self.list_loc).click()
        self.driver.find_element(*self.production_list_loc).click()
        # sleep(2)
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.roller_doors_loc))  #new added

    @property
    def check_production_url(self):
        '''check the url for Production page'''
        production_url = self.driver.current_url
        print(production_url)
        return production_url

    @property
    def check_production_title(self):
        '''check the title for Production page'''
        production_title = self.driver.find_element(*self.production_title_loc).text
        print(production_title)
        return production_title
    @property
    def check_production_section(self):
        '''check each section in Production page'''
        roller_doors = self.driver.find_element(*self.roller_doors_loc).text
        panel_lift_safe = self.driver.find_element(*self.panel_lift_loc).text
        insulated_doors = self.driver.find_element(*self.insulated_doors_loc).text
        custom_doors = self.driver.find_element(*self.custom_doors_loc).text
        roller_shutters = self.driver.find_element(*self.roller_shutters_loc).text
        all_doors = self.driver.find_element(*self.all_doors_loc).text
        print (roller_doors,panel_lift_safe,insulated_doors,custom_doors,roller_shutters,all_doors)
        return roller_doors,panel_lift_safe,insulated_doors,custom_doors,roller_shutters,all_doors

if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("http:// ")
    driver.implicitly_wait(10)

    login = Production(driver)
    login.typeUserName('aa@ecogaragedoors.com')
    login.typePassword('aabb')
    login.clickLogin()
    login.go_production()
    login.check_production_url
    # login.check_production_section
    # login.check_production_title