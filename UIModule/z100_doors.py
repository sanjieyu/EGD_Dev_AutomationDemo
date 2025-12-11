# Author:Yi Sun(Tim) 2025-9-04

'''Change Quote Status for 100 doors'''

import selenium
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from UIModule.quotation_panel_door import Quotation_Panel
from UIModule.add_quote_with_door import Add_Quote_With_Door
from UIModule.search_quote import Search_Quote
from UIModule.change_quote_status import Change_Quote_Status
from UIModule.login_admin import Admin_Portal
from UIModule.production import Production
from UIModule.panel_left_safe import Panel_lift_Safe
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException,ElementNotInteractableException
from selenium.webdriver.common.keys import Keys


class Move_100_Doors():
    '''loc for the status dropdown'''
    copy_quote_option_loc = (By.CSS_SELECTOR, "label[for='CopyQuote']")
    new_job_number_loc = (By.CSS_SELECTOR, "label[for='JobId']")

    '''loc for the Status screen'''
    status_dropdown_loc = (By.ID,'JobStatusId')


    def __init__(self,driver):
        self.driver = driver
        self.quotation_panel = Quotation_Panel(self.driver)
        self.add_quote_door = Add_Quote_With_Door(self.driver)
        self.search_quote = Search_Quote(self.driver)
        self.change_status = Change_Quote_Status(self.driver)
        self.product = Production(self.driver)
        self.panel_lift_production = Panel_lift_Safe(self.driver)
        self.new_job_number = None

    def find_copy_job(self):
        '''find the sample job, then copy it'''
        self.driver.find_element(*self.add_quote_door.find_quote_input).send_keys("209513")  #original job with 100 doors
        self.driver.find_element(*self.add_quote_door.find_quote_btn).click()
        sleep(2)
        self.driver.find_element(*self.quotation_panel.setting_btn_loc).click()
        self.driver.find_element(*self.copy_quote_option_loc).click()

    def goto_new_job(self):
        '''find the new copied job'''
        self.driver.find_element(*self.search_quote.searchquotes_btn_loc).click()

    @property
    def get_job_number(self):
        '''get the job number for the new copied job'''
        global new_job_number
        new_job_number = self.driver.find_element(*self.new_job_number_loc).text
        print("copied job is ",new_job_number)
        return new_job_number


    def goto_status(self):
        '''go to the status screen'''
        self.driver.find_element(*self.quotation_panel.setting_btn_loc).click()
        self.driver.find_element(*self.change_status.status_loc).click()

    @property
    def check_myob_screen(self):
        '''Check if it's moved to MYOB screen'''
        self.change_status.change_status_new_order()

        try:
            try:
                WebDriverWait(self.driver, 1200).until(
                    EC.invisibility_of_element_located((By.CLASS_NAME, "modalAjax"))
                )
                print("the frame window is gone")
            except TimeoutException:
                print("please try it again")

            status_dropdown_element = WebDriverWait(self.driver, 1200).until(
                EC.element_to_be_clickable(self.status_dropdown_loc)
            )
            status_dropdown = Select(self.driver.find_element(*self.status_dropdown_loc))
            status_dropdown.select_by_visible_text("MYOB - Ready")
        except TimeoutException:
            print("time out")
        self.driver.find_element(*self.change_status.date_box_loc).click()
        self.driver.find_element(*self.change_status.date_box_loc).send_keys("02/11/2025")
        self.driver.find_element(*self.change_status.save_btn_loc).click()
        self.change_status.go_myob.go_myob_quotes()
        print(new_job_number)
        if new_job_number:
            self.change_status.go_myob.input_proposal(new_job_number)
            sleep(2)
            searched_result = self.driver.find_element(*self.change_status.proposal_num_myob_loc).text
            if searched_result == new_job_number:
                print("it's in MYOB")
                return True
            else:
                print("it's not in MYOB")
                return False
        else:
            print("Proposal number is not available.")

    @property
    def move_check_order(self):
        '''move to Order status'''
        self.driver.find_element(*self.add_quote_door.find_quote_input).send_keys(new_job_number)  # find the 100 job
        self.driver.find_element(*self.add_quote_door.find_quote_btn).click()
        self.goto_status()
        status_dropdown = Select(self.driver.find_element(*self.status_dropdown_loc))
        status_dropdown.select_by_visible_text("Order")
        self.driver.find_element(*self.change_status.date_box_loc).click()
        self.driver.find_element(*self.change_status.date_box_loc).send_keys("02/11/2025")
        self.driver.find_element(*self.change_status.save_btn_loc).click()
        self.product.go_production()
        self.panel_lift_production.go_panel_lift_safe()
        sleep(1)
        first_order = self.panel_lift_production.get_first_orderid
        if first_order == new_job_number + "C3":
            print('move to Order successfully')
            return True
        else:
            print('move to Order fail')
            return False


if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("http:// ")
    driver.implicitly_wait(10)

    login = Admin_Portal(driver)
    login.typeUserName('aa@ecogaragedoors.com')
    login.typePassword('aabb')
    login.clickLogin()
    login1 = Move_100_Doors(driver)
    login1.find_copy_job()
    login1.goto_new_job()
    login1.get_job_number
    login1.goto_status()
    login1.check_myob_screen
    login1.move_check_order







