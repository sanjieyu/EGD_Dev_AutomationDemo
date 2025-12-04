# Author:Yi Sun(Tim) 2025-9-08

'''Change Quote Status to Invoiced for Panel lift doors'''

import selenium
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from UIModule.login_admin import Admin_Portal
from UIModule.change_quote_status import Change_Quote_Status
from UIModule.add_quote_with_door import Add_Quote_With_Door
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.keys import Keys

class Change_Invoiced_Panellift():

    def __init__(self,driver):
        self.driver = driver
        self.admin_portal = Admin_Portal(self.driver)
        self.change_quote_status = Change_Quote_Status(self.driver)
        self.add_quote_with_door = Add_Quote_With_Door(self.driver)
        self.proposal_number = None

    def change_status_myobready(self):
        '''change status to MyOB reday'''
        self.change_quote_status.goto_status_page()
        self.change_quote_status.change_status_new_order()
        WebDriverWait(self.driver, 20).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "modalAjax"))
        )                                                                              # 等待模态窗口消失
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.change_quote_status.status_select_loc))  # 等待status下拉列表可点击
        # sleep(10)
        self.change_quote_status.change_status_order()
        WebDriverWait(self.driver, 20).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "modalAjax"))
        )
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.change_quote_status.status_select_loc))  # 等待status下拉列表可点击
        # sleep(10)

    def change_status_invoiced(self):
        '''change status to Invoiced'''
        select_status = Select(self.driver.find_element(*self.change_quote_status.status_select_loc))
        select_status.select_by_visible_text("Order")
        self.driver.find_element(*self.change_quote_status.date_box_loc).click()
        self.driver.find_element(*self.change_quote_status.date_box_loc).send_keys("02/11/2025")
        self.driver.find_element(*self.change_quote_status.save_btn_loc).click()
        WebDriverWait(self.driver, 15).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "modalAjax"))
        )
        WebDriverWait(self.driver,20).until(EC.element_to_be_clickable(self.change_quote_status.status_select_loc))
        # sleep(10)
        select_status2 = Select(self.driver.find_element(*self.change_quote_status.status_select_loc))
        select_status2.select_by_visible_text("Invoiced")
        self.driver.find_element(*self.change_quote_status.date_box_loc).click()
        self.driver.find_element(*self.change_quote_status.date_box_loc).send_keys("02/11/2025")
        self.driver.find_element(*self.change_quote_status.save_btn_loc).click()

    def check_invoiced_status(self):
        '''check the invoiced status'''
        self.add_quote_with_door.search_new_quote()  # searched this quote from Find a quote box
        quote_status_loc = (
        By.XPATH, '/html/body/div[3]/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody/tr/td[11]/span')
        quote_status = self.driver.find_element(*quote_status_loc).text
        if quote_status == 'Invoiced':
            print('job status is correct')
            return True
        else:
            print('job status is wrong')
            return False

if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("http:// ")
    driver.implicitly_wait(10)

    login = Admin_Portal(driver)
    # login = Change_Invoiced_Panellift(driver)
    login.typeUserName('aa@ecogaragedoors.com')
    login.typePassword('aabb')
    login.clickLogin()
    login1 = Change_Invoiced_Panellift(driver)
    login1.change_status_myobready()
    login1.change_status_invoiced()
    login1.check_invoiced_status()