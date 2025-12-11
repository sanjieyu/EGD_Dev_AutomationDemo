# Author:Yi Sun(Tim) 2024-5-22

'''User Management Page'''

import selenium
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from UIModule.admin_portal import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class User_Management(Admin_Page):

    user_title_loc = (By.NAME,'usermanager')
    roles_assigned_loc = (By.CSS_SELECTOR, "[aria-label='roles_assigned']")
    registered_users_loc = (By.CSS_SELECTOR, "[aria-label='registered_users']")
    new_btn_loc = (By.ID,'btnAddUser')

    '''Add New User screen'''
    newuser_title_loc = (By.CSS_SELECTOR, "label[for='NewUser']")
    first_name_loc = (By.CSS_SELECTOR, "label[for='FirstName']")
    last_name_loc = (By.CSS_SELECTOR, "label[for='LastName']")
    email_loc  = (By.CSS_SELECTOR, "label[for='Email']")
    first_name_box_lox = (By.ID,'userFirstName')
    last_name_box_loc = (By.ID,'userLastName')
    email_box_loc = (By.ID,'userEmail')
    save_user_btn_loc = (By.XPATH,'//*[@id="btnUserSave"]')
    close_user_btn_loc = (By.ID, 'btnClose')

    error_msg_loc = (By.CSS_SELECTOR, "label[for='ErrorMsg']")


    def go_user_management(self):
        self.driver.find_element(*self.account_loc).click()
        self.driver.find_element(*self.usermanage_loc).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.user_title_loc))  # new added

    @property
    def check_user_url(self):
        '''Check the URL'''
        user_url = self.driver.current_url
        return user_url

    @property
    def check_user_title(self):
        '''Check the title'''
        user_title = self.driver.find_element(*self.user_title_loc).text
        return user_title

    @property
    def check_section(self):
        '''Check each section'''
        roles_assigned = self.driver.find_element(*self.roles_assigned_loc).text
        registered_user = self.driver.find_element(*self.registered_users_loc).text
        return roles_assigned,registered_user

    @property
    def check_new_button(self):
        '''Check the New button'''
        new_button = self.driver.find_element(*self.new_btn_loc)
        if new_button.is_displayed:
            return  True
        else:
            return False

    @property
    def check_add_user(self):
        '''Check Add New User Screen'''
        self.driver.find_element(*self.new_btn_loc).click()
        self.driver.switch_to.window(self.driver.window_handles[-1]) # switch to new page
        newuser_title = self.driver.find_element(*self.newuser_title_loc).text
        first_name = self.driver.find_element(*self.first_name_loc).text
        last_name = self.driver.find_element(*self.last_name_loc).text
        email = self.driver.find_element(*self.email_loc).text
        print(newuser_title,first_name,last_name,email)
        return newuser_title,first_name,last_name,email

    @property
    def validate_duplicate_user(self):
        '''Check the validation for adding the duplicate user'''
        # self.driver.find_element(*self.new_btn_loc).click()
        # self.driver.switch_to.window(self.driver.window_handles[-1]) # switch to new page
        self.driver.find_element(*self.first_name_box_lox).send_keys("Yi")
        self.driver.find_element(*self.last_name_box_loc).send_keys("Sun")
        self.driver.find_element(*self.email_box_loc).send_keys("ysun@ecogaragedoors.com.au")
        save_user_btn = self.driver.find_element(*self.save_user_btn_loc)
        save_user_btn.click()
        error_msg = self.driver.find_element(*self.error_msg_loc).text
        print(error_msg)
        return error_msg


if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("http:// ")
    driver.implicitly_wait(10)

    login = User_Management(driver)
    login.typeUserName('aa@ecogaragedoors.com')
    login.typePassword('aabb')
    login.clickLogin()
    login.go_user_management()
    # login.check_user_url
    # login.check_user_title
    # login.check_section
    # login.check_new_button
    login.check_add_user
    login.validate_duplicate_user