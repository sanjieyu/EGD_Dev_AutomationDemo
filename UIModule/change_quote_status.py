# Author:Yi Sun(Tim) 2024-3-14

'''Change Quote Status'''

import selenium
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from UIModule.login_admin import Admin_Portal
from UIModule.panel_left_safe import Panel_lift_Safe
from UIModule.production import Production
from UIModule.add_quote_with_door import Add_Quote_With_Door
from UIModule.myob_quote import MYOB_Quotes
from UIModule.panel_left_safe import Panel_lift_Safe
from UIModule.production import Production
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.keys import Keys

class Change_Quote_Status():
    '''loc for the status dropdown'''
    setting_btn_loc = (By.XPATH,'/html/body/div[3]/div[2]/div/div/div/div/div/div/div/div/table/tbody/tr/td[12]/div/button/i')
    status_loc = (By.XPATH,'/html/body/div[3]/div[2]/div/div/div/div/div/div/div/div/table/tbody/tr/td[12]/div/ul/li[2]/a')

    '''The search result by proposal number in MYOB screen'''
    proposal_num_myob_loc = (By.XPATH,'/html/body/div[3]/div[2]/div/div[1]/div/div[1]/div/table/tbody/tr/td[2]/a')

    '''loc for the elements in Status page'''
    status_select_loc = (By.ID,'JobStatusId')
    # date_box_loc = (By.ID,'ExpectedDeliveryDate271233')
    date_box_loc = (By.NAME,'ExpectedDeliveryDate')
    save_btn_loc = (By.ID,'saveStatuses')



    def __init__(self,driver):
        self.driver = driver
        self.production = Production(self.driver)
        self.production_panel = Panel_lift_Safe(self.driver)
        self.add_quote_door = Add_Quote_With_Door(self.driver)
        self.go_myob = MYOB_Quotes(self.driver)
        self.go_production = Production(self.driver)
        self.go_panel_lift_safe = Panel_lift_Safe(self.driver)
        self.proposal_number = None


    def goto_status_page(self):
        '''Add a new quote with door, then search this new quote'''
        self.add_quote_door.add_door_fun()
        self.proposal_number  = self.add_quote_door.get_proposal_number
        # self.add_quote_door.get_proposal_number
        self.add_quote_door.search_new_quote()
        self.driver.find_element(*self.setting_btn_loc).click()
        self.driver.find_element(*self.status_loc).click()

    def change_status_new_order(self):
        '''Change the status to New Order for this new quote'''
        select_status = Select(self.driver.find_element(*self.status_select_loc))
        select_status.select_by_visible_text("New Order")
        self.driver.find_element(*self.date_box_loc).click()
        self.driver.find_element(*self.date_box_loc).send_keys("30/12/2025")
        self.driver.find_element(*self.save_btn_loc).click()

    def change_status_order(self):
        '''Change the status to MYOB - Ready for this new quote'''
        select_status = Select(self.driver.find_element(*self.status_select_loc))
        select_status.select_by_visible_text("MYOB - Ready")
        self.driver.find_element(*self.date_box_loc).click()
        self.driver.find_element(*self.date_box_loc).send_keys("02/11/2025")
        self.driver.find_element(*self.save_btn_loc).click()

    def check_myob_status(self):
        '''Check the quote status in MYOB Page'''
        self.go_myob.go_myob_quotes()
        if self.proposal_number:
            self.go_myob.input_proposal(self.proposal_number)
            sleep(2)
            searched_result = self.driver.find_element(*self.proposal_num_myob_loc).text
            if searched_result == self.proposal_number:
                print("it's in MYOB")
                return  True
            else:
                print("it's not in MYOB")
                return False
        else:
            print("Proposal number is not available.")

    def check_order_status(self):
        '''Change the quote status from MYOB Ready to Order'''
        status_dropdown_loc = self.go_myob.door_status_dropdown_loc
        save_btn_loc = self.go_myob.save_btn_loc
        status_dropdown = Select(self.driver.find_element(*status_dropdown_loc))
        status_dropdown.select_by_visible_text("Order")
        self.driver.find_element(*save_btn_loc).click()    # change to roder status
        sleep(3)
        self.go_production.go_production()
        sleep(2)
        self.go_panel_lift_safe.go_panel_lift_safe()
        sleep(1)
        first_order = self.go_panel_lift_safe.get_first_orderid
        if first_order  == self.proposal_number + "A1":
            print('move to Order successfully')
            return True
        else:
            print('move to Order fail')
            return False

    def check_rollforming_status(self):
        '''Change the quote status from Order to Rollforming'''
        search_order_btn = self.go_panel_lift_safe.search_order_box_loc
        self.driver.find_element(*search_order_btn).send_keys(self.proposal_number + "A1")


        searched_order_statusbox_loc = (By.NAME,self.proposal_number + 'A1')
        searched_order_status_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(searched_order_statusbox_loc))
        searched_order_status_select = Select(searched_order_status_element)
        searched_order_status_select.select_by_value('9')
        save_changes_order_btn = self.driver.find_element(*self.go_panel_lift_safe.save_changes_order_btn_loc)
        save_changes_order_btn.click()
        sleep(4)

        self.add_quote_door.search_new_quote()  # searched this quote from Find a quote box
        quote_status_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody/tr/td[11]/span')
        quote_status = self.driver.find_element(*quote_status_loc).text
        if quote_status == 'In Production - Rollforming':
            print('job status is correct, moved to rollforming sucessfully')
            return True
        else:
            print('job status is wrong')
            return False

    def check_rollforming_size(self):
        '''Check the Actual size of the door on Rollforming screen'''
        self.production.go_production()
        self.production_panel.go_panel_lift_safe()
        self.production_panel.go_rollforming()
        search_quote_box = self.driver.find_element(*self.production_panel.search_job_box)
        search_quote_btn = self.driver.find_element(*self.production_panel.search_job_btn)
        WebDriverWait(self.driver, 180).until(EC.visibility_of_element_located(self.production_panel.table_frame_loc))
        search_quote_box.send_keys(self.proposal_number)
        search_quote_btn.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.production_panel.searched_popup_loc))
        searched_job = self.driver.find_element(*self.production_panel.searched_result_job_loc)
        searched_job.click()


if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("http:// ")
    driver.implicitly_wait(10)

    # login = Admin_Portal(driver)
    login = Admin_Portal(driver)
    login.typeUserName('aa@ecogaragedoors.com')
    login.typePassword('aabb')
    login.clickLogin()
    login1 = Change_Quote_Status(driver)
    login1.goto_status_page()
    login1.change_status_order()
    login1.check_myob_status()
    login1.check_order_status()
    login1.check_rollforming_status()
    # login1.check_rollforming_size()

