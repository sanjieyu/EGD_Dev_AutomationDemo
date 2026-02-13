# Author:Yi Sun(Tim) 2023-09-01

'''Search Doors Page'''

import selenium
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from pages.admin_portal import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert


class Search_Door(Admin_Page):

    '''loc for default values in this page'''
    door_btn_loc = (By.ID,'btnDoor')
    searchdoor_title_loc = (By.NAME,'searchdoors')
    door_status_loc = (By.CSS_SELECTOR, "[aria-label='door_status']")
    other_para_loc = (By.CSS_SELECTOR, "[aria-label='other_para']")
    filter_date_loc = (By.CSS_SELECTOR, "[aria-label='filter_date']")
    door_status_loc = (By.CSS_SELECTOR, "[aria-label='door_status']")
    user_loc = (By.CSS_SELECTOR, "[aria-label='user']")
    search_door_btn_loc = (By.ID,'btnSearch')

    '''Input box for each filter'''
    door_status_select_loc = (By.CSS_SELECTOR, "[aria-label='status']")
    user_select_loc =(By.ID,'DoorSearchModel_UserAssignedId')

    def go_searchquotes(self):
        '''Switch to Search Quotes from LIST Menu'''
        self.driver.find_element(*self.list_loc).click()
        self.driver.find_element(*self.quote_list_loc).click()

    def go_searchdoors(self):
        '''Switch to Search Doors'''
        self.driver.find_element(*self.door_btn_loc).click()

    @property
    def check_title(self):
        '''check the title for Search Doors page'''
        searchdoors_title = self.driver.find_element(*self.searchdoor_title_loc).text
        print(searchdoors_title)
        return searchdoors_title

    @property
    def check_searchurl(self):
        '''check the url for Search Doors page'''
        searchdoors_url = self.driver.current_url
        print(searchdoors_url)
        return searchdoors_url

    @property
    def check_section_doors(self):
        '''check each section of Doors filter table in Search Doors page'''
        door_status = self.driver.find_element(*self.door_status_loc).text
        other_para = self.driver.find_element(*self.other_para_loc).text
        print(door_status,other_para)
        return door_status,other_para

    @property
    def check_door_status(self):
        '''check each filter in "Door Status changed between" in Doors filter table'''
        filter_date = self.driver.find_element(*self.filter_date_loc).text
        print(filter_date)
        return filter_date

    @property
    def check_other_para(self):
        '''check each filter in "Other Parameters" in Doors filter table'''
        door_status = self.driver.find_element(*self.door_status_loc).text
        user = self.driver.find_element(*self.user_loc).text
        print(door_status,user)
        return door_status,user

    @property
    def check_default_user(self):
        '''check the default user name in "User" filter in Doors filter table'''
        user_select = Select(self.driver.find_element(*self.user_select_loc))
        default_user = user_select.first_selected_option
        user_name = default_user.text
        print(user_name)
        return user_name


if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("http:// ")
    driver.implicitly_wait(10)

    login = Search_Door(driver)
    login.typeUserName('aa@ecogaragedoors.com')
    login.typePassword('aabb')
    login.clickLogin()
    login.go_searchquotes()
    login.go_searchdoors()
    login.check_searchurl
    # login.check_title
    # login.check_section_doors
    # login.check_door_status
    # login.check_other_para
    # login.check_default_user







