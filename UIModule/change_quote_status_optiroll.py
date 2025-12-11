# Author:Yi Sun(Tim) 2025-11-12

'''Change Quote Status for OptiRoll Doors'''

import selenium
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from UIModule.login_admin import Admin_Portal
from UIModule.add_quote_with_optiroll_door import Add_Quote_With_OptiRoll_Door
from UIModule.myob_quote import MYOB_Quotes
from UIModule.optiroll_production import OptiRoll_Production
from UIModule.production_wa import Production_WA
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.keys import Keys

class Change_Quote_Status_OptiRoll():

    '''loc for the status dropdown'''
    setting_btn_loc = (By.ID, 'btnSetting')
    status_loc = (By.XPATH, '//*[@id="statusquote"]/div/span')

    '''The search result by proposal number in MYOB screen'''
    proposal_num_myob_loc = (By.NAME,'pronum')

    '''loc for the elements in Status page'''
    status_select_loc = (By.ID,'JobStatusId')
    date_box_loc = (By.NAME,'ExpectedDeliveryDate')
    save_btn_loc = (By.ID,'saveStatuses')

    def __init__(self,driver):
        self.driver = driver
        self.add_quote_optiroll = Add_Quote_With_OptiRoll_Door(self.driver)
        self.go_myob = MYOB_Quotes(self.driver)
        self.go_product_wa = Production_WA(self.driver)
        self.go_optiroll_door = OptiRoll_Production(self.driver)
        self.proposal_number = None

    def go_status_page(self):
        '''Add a new quote with door, then search this new quote'''
        self.add_quote_optiroll.add_door_func()
        self.proposal_number = self.add_quote_optiroll.get_proposal_number
        self.add_quote_optiroll.search_new_quote
        self.driver.find_element(*self.setting_btn_loc).click()
        self.driver.find_element(*self.status_loc).click()

    def change_status_new_order(self):
        '''Change the status to New Order for this new quote'''

    def change_status_order(self):
            '''Change the status to MYOB - Ready for this new quote'''
            select_status = Select(self.driver.find_element(*self.status_select_loc))
            select_status.select_by_visible_text("MYOB - Ready")
            self.driver.find_element(*self.date_box_loc).click()
            self.driver.find_element(*self.date_box_loc).send_keys("30/12/2025")
            self.driver.find_element(*self.save_btn_loc).click()

    def check_myob_status(self):
        '''Check the quote status in MYOB Page'''
        self.go_myob.go_myob_quotes()
        if self.proposal_number:
            self.go_myob.input_proposal(self.proposal_number)
            sleep(2)
            searched_result = self.driver.find_element(*self.proposal_num_myob_loc).text
            if searched_result == self.proposal_number:
                print("same")
                return  True
            else:
                return False
        else:
            print("Proposal number is not available.")

    def check_order_status(self):
        '''Change the quote status from MYOB Ready to Order'''
        status_dropdown_loc = self.go_myob.door_status_dropdown_loc
        save_btn_loc = self.go_myob.save_btn_loc
        status_dropdown = Select(self.driver.find_element(*status_dropdown_loc))
        status_dropdown.select_by_visible_text("Order")
        self.driver.find_element(*save_btn_loc).click()  # change to roder status
        sleep(3)
        self.go_product_wa.go_production_wa()
        sleep(2)
        first_order = self.go_optiroll_door.get_first_orderid
        if first_order == self.proposal_number + "A1":
            print('move to Order successfully')
            return True
        else:
            print('move to Order fail')
            return False

    def check_rollforming_status(self):
        '''Change the quote status from Order to Rollforming'''
        search_order_btn = self.go_optiroll_door.search_order_box_loc
        self.driver.find_element(*search_order_btn).send_keys(self.proposal_number + "A1")
        self.driver.find_element(*search_order_btn).send_keys(Keys.ENTER)
        sleep(9)
        searched_order_statusbox_loc = (By.NAME,self.proposal_number + 'A1')
        searched_order_status_element = self.driver.find_element(*searched_order_statusbox_loc)
        searched_order_status_select = Select(searched_order_status_element)
        searched_order_status_select.select_by_visible_text("In Production - Rollforming")
        save_changes_order_btn = self.driver.find_element(*self.go_optiroll_door.save_changes_order_btn)
        save_changes_order_btn.click()
        sleep(4)
        self.add_quote_optiroll.search_new_quote  # searched this quote from Find a quote box
        quote_status_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody/tr/td[11]/span')
        quote_status = self.driver.find_element(*quote_status_loc).text
        if quote_status == 'In Production - Rollforming':
            print('job status is correct, moved to rollforming sucessfully')
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
    login.typeUserName('aa@ecogaragedoors.com')
    login.typePassword('aabb')
    login.clickLogin()
    login1 = Change_Quote_Status_OptiRoll(driver)
    login1.go_status_page()
    login1.change_status_order()
    login1.check_myob_status()
    login1.check_order_status()
    login1.check_rollforming_status()
