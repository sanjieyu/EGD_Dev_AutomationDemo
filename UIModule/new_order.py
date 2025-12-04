# Author:Yi Sun(Tim) 2024-11-11

'''New Order Page'''

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from UIModule.admin_portal import *

class New_Order(Admin_Page):

    new_order_title_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/h1')
    proposal_no_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[2]/div[1]/div[1]/div/table/thead/tr/th[2]/div/span')
    create_date_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[2]/div[1]/div[1]/div/table/thead/tr/th[3]/div/a')
    client_name_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[2]/div[1]/div[1]/div/table/thead/tr/th[4]/div/a')
    door_number_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[2]/div[1]/div[1]/div/table/thead/tr/th[5]/div/span')
    order_date_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[2]/div[1]/div[1]/div/table/thead/tr/th[6]/div/span')
    door_status_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[2]/div[1]/div[1]/div/table/thead/tr/th[7]/div/span')
    document_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[2]/div[1]/div[1]/div/table/thead/tr/th[8]/div/span')
    save_btn_loc = (By.ID,'saveListData')

    def go_new_order(self):
        self.driver.find_element(*self.list_loc).click()
        self.driver.find_element(*self.neworder_list_loc).click()
        WebDriverWait(self.driver,35).until(EC.visibility_of_element_located(self.new_order_title_loc))

    @property
    def check_neworder_url(self):
        '''Check the url for New Order screen'''
        new_order_url = self.driver.current_url
        print(new_order_url)
        return new_order_url

    @property
    def check_neworder_title(self):
        '''Check the title of New Order screen'''
        new_order_title = self.driver.find_element(*self.new_order_title_loc).text
        print(new_order_title)
        return new_order_title

    @property
    def check_columns(self):
        '''Check each column'''
        proposal_no = self.driver.find_element(*self.proposal_no_loc).text
        create_date = self.driver.find_element(*self.create_date_loc).text
        client_name = self.driver.find_element(*self.client_name_loc).text
        door_number = self.driver.find_element(*self.door_number_loc).text
        order_date = self.driver.find_element(*self.order_date_loc).text
        door_status = self.driver.find_element(*self.door_status_loc).text
        document = self.driver.find_element(*self.document_loc).text
        print(proposal_no,create_date,client_name,door_number,order_date,door_status,document)
        return proposal_no,create_date,client_name,door_number,order_date,door_status,document

    @property
    def check_save_button(self):
        '''Check the Save changes button'''
        try:
            save_btn = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.save_btn_loc))
            print("it's clickable")
            return True
        except TimeoutException:
            print("it's not clickable")
            return False


if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("http:// ")
    driver.implicitly_wait(10)

    login = New_Order(driver)
    login.typeUserName('aa@ecogaragedoors.com')
    login.typePassword('aabb')
    login.clickLogin()
    login.go_new_order()
    # login.check_neworder_url
    # login.check_neworder_title
    # login.check_columns
    login.check_save_button
