# Author:Yi Sun(Tim) 2025-10-14

'''Production WA Page'''

import selenium
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from UIModule.admin_portal import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class Production_WA(Admin_Page):

    production_wa_title_loc = (By.XPATH, '/html/body/div[3]/div[2]/div[1]/h1')

    '''loc for each section in this page'''
    optiroll_doors_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/div[3]/ul/li[1]/a')
    optilift_doors_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/div[3]/ul/li[2]/a')

    def go_production_wa(self):
        '''Switch to Production WA from LIST Menu'''
        self.driver.find_element(*self.list_loc).click()
        self.driver.find_element(*self.productionWA_list_loc).click()
        # sleep(2)
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.optiroll_doors_loc))  #new added

    @property
    def check_production_wa_url(self):
        '''check the url for Production WA page'''
        production_wa_url = self.driver.current_url
        print(production_wa_url)
        return production_wa_url

    @property
    def check_production_wa_title(self):
        '''check the title for Production WA page'''
        production_wa_title = self.driver.find_element(*self.production_wa_title_loc).text
        print(production_wa_title)
        return production_wa_title
    @property
    def check_production_wa_section(self):
        '''check each section in Production WA page'''
        optiroll_doors = self.driver.find_element(*self.optiroll_doors_loc).text
        optilift_doors = self.driver.find_element(*self.optilift_doors_loc).text
        print (optiroll_doors,optilift_doors)
        return optiroll_doors,optilift_doors

if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("http:// ")
    driver.implicitly_wait(10)

    login = Production_WA(driver)
    login.typeUserName('aa@ecogaragedoors.com')
    login.typePassword('aabb')
    login.clickLogin()
    login.go_production_wa()
    login.check_production_wa_url
    login.check_production_wa_section
    login.check_production_wa_title