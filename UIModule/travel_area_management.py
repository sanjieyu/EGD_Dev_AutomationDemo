# Author:Yi Sun(Tim) 2024-5-20

'''Travel Area Management Page'''

import selenium
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from UIModule.admin_portal import *

class Travel_Area_Management(Admin_Page):

    travel_area_title_loc = (By.NAME,'travel')
    new_btn_loc = (By.ID,'btnAddArea')
    search_box_loc = (By.ID,'travelAreaSearchInput')
    search_result_suburb_loc = (By.CSS_SELECTOR, "[aria-label='suburbs']")

    '''new page'''
    new_title_loc = (By.CSS_SELECTOR, "label[for='Title']")
    new_postcode_loc = (By.CSS_SELECTOR, "label[for='Postcode']")
    new_suburb_loc = (By.CSS_SELECTOR, "label[for='Suburb']")
    new_state_loc = (By.CSS_SELECTOR, "label[for='State']")
    new_comments_loc = (By.CSS_SELECTOR, "label[for='Comments']")
    new_category_loc = (By.CSS_SELECTOR, "label[for='Category']")
    new_delivery_loc = (By.CSS_SELECTOR, "label[for='Delivery']")

    new_save_btn_loc = (By.ID,'btnAreaSave')
    new_close_btn_loc = (By.ID, 'btnClose')

    def go_travel_area_management(self):
        '''Switch to Travel Area Management Page from Account Menu'''
        self.driver.find_element(*self.account_loc).click()
        self.driver.find_element(*self.travel_area_loc).click()
        # sleep(2)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.travel_area_title_loc))  # new added

    @property
    def check_travel_area_url(self):
        '''Check the URL'''
        travel_area_url = self.driver.current_url
        return  travel_area_url

    @property
    def check_travel_area_title(self):
        '''Check the Title'''
        travel_area_title = self.driver.find_element(*self.travel_area_title_loc).text
        return  travel_area_title

    @property
    def check_new_button(self):
        '''Check the New button'''
        new_button = self.driver.find_element(*self.new_btn_loc)
        if new_button.is_displayed:
            return True
        else:
            return False

    @property
    def check_search_box(self):
        '''Check the Search Box'''
        search_box = self.driver.find_element(*self.search_box_loc)
        if search_box.is_displayed:
            return True
        else:
            return False

    @property
    def check_search_result(self):
        '''Check the search result for postcode 7879'''
        self.driver.find_element(*self.search_box_loc).send_keys("7879")
        suburb_name = self.driver.find_element(*self.search_result_suburb_loc).text
        print(suburb_name)
        return  suburb_name

    @property
    def check_new_screen(self):
        ''''Check the Add New Area screen'''
        self.driver.find_element(*self.new_btn_loc).click()
        self.driver.switch_to.window(self.driver.window_handles[-1])  # switch to new page
        new_title = self.driver.find_element(*self.new_title_loc).text
        return new_title

    @property
    def check_new_screen_input(self):
        ''''Check each input in the Add New Area screen'''
        # self.driver.find_element(*self.new_btn_loc).click()
        # self.driver.switch_to.window(self.driver.window_handles[-1])  # switch to new page
        new_postcode = self.driver.find_element(*self.new_postcode_loc).text
        new_suburb = self.driver.find_element(*self.new_suburb_loc).text
        new_state = self.driver.find_element(*self.new_state_loc).text
        new_comment = self.driver.find_element(*self.new_comments_loc).text
        new_category = self.driver.find_element(*self.new_category_loc).text
        new_delivery = self.driver.find_element(*self.new_delivery_loc).text
        print(new_postcode,new_suburb,new_state,new_comment,new_category,new_delivery)
        return new_postcode,new_suburb,new_state,new_comment,new_category,new_delivery

    @property
    def check_new_save_btn(self):
        ''''Check Save in the Add New Area screen'''
        # self.driver.find_element(*self.new_btn_loc).click()
        # self.driver.switch_to.window(self.driver.window_handles[-1])  # switch to new page
        new_save_btn = self.driver.find_element(*self.new_save_btn_loc)
        if new_save_btn.is_displayed:
            print("exist")
            return True
        else:
            print('missing')
            return False

    @property
    def check_new_close_btn(self):
        ''''Check Close in the Add New Area screen'''
        # self.driver.find_element(*self.new_btn_loc).click()
        # self.driver.switch_to.window(self.driver.window_handles[-1])  # switch to new page
        new_close_btn = self.driver.find_element(*self.new_close_btn_loc)
        if new_close_btn.is_displayed:
            print("exist")
            return True
        else:
            print('missing')
            return False

if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("http:// ")
    driver.implicitly_wait(10)

    login = Travel_Area_Management(driver)
    login.typeUserName('aa@ecogaragedoors.com')
    login.typePassword('aabb')
    login.clickLogin()
    login.go_travel_area_management()
    # login.check_travel_area_url
    # login.check_travel_area_title
    # login.check_new_button
    # login.check_search_box
    login.check_search_result
    # login.check_new_screen
    # login.check_new_screen_input
    # login.check_new_save_btn
    # login.check_new_close_btn