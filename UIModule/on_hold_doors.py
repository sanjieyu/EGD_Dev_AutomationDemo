# Author:Yi Sun(Tim) 2024-11-13

'''On-Hold Doors Page'''

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from UIModule.admin_portal import *
from selenium.common.exceptions import TimeoutException

class On_Hold(Admin_Page):

    on_hold_title_loc = (By.XPATH,'/html/body/div[3]/div[2]/div/h1')

    '''elements in Client Details section'''
    client_details_loc = (By.XPATH,'/html/body/div[3]/div[2]/div/div[1]/form/div/div/div[1]/div[1]/div[1]/h4')
    client_name_loc = (By.XPATH,'/html/body/div[3]/div[2]/div/div[1]/form/div/div/div[1]/div[1]/div[2]/label')
    client_name_box_loc = (By.ID,'ClientName')
    contact_num_loc = (By.XPATH,'/html/body/div[3]/div[2]/div/div[1]/form/div/div/div[1]/div[1]/div[3]/label')
    contact_num_box_loc = (By.ID,'ContactNumber')
    location_loc = (By.XPATH,'/html/body/div[3]/div[2]/div/div[1]/form/div/div/div[1]/div[2]/div[1]/h4')
    suburb_loc = (By.XPATH,'/html/body/div[3]/div[2]/div/div[1]/form/div/div/div[1]/div[2]/div[2]/label')
    suburb_box_loc = (By.ID,'Suburb')
    site_address_loc = (By.XPATH,'/html/body/div[3]/div[2]/div/div[1]/form/div/div/div[1]/div[2]/div[3]/label')
    site_address_box_loc = (By.ID,'SiteAddress')
    quote_info_loc = (By.XPATH,'/html/body/div[3]/div[2]/div/div[1]/form/div/div/div[1]/div[3]/div[1]/h4')
    proposal_no_loc = (By.XPATH,'/html/body/div[3]/div[2]/div/div[1]/form/div/div/div[1]/div[3]/div[2]/label')
    proposal_no_box_loc = (By.ID,'ProposalNo')
    user_loc = (By.XPATH,'/html/body/div[3]/div[2]/div/div[1]/form/div/div/div[1]/div[3]/div[3]/label')
    user_select_loc = (By.ID,'UserAssignedId')
    search_quotes_btn_loc = (By.XPATH,'/html/body/div[3]/div[2]/div/div[1]/form/div/div/div[2]/div/input')

    '''elements in Results section'''
    results_found_loc = (By.XPATH,'/html/body/div[3]/div[2]/div/div[1]/div/h4')
    proposal_loc = (By.XPATH,'/html/body/div[3]/div[2]/div/div[1]/div/div[1]/div/table/thead/tr/th[1]/div/span')
    created_date_loc = (By.XPATH,'/html/body/div[3]/div[2]/div/div[1]/div/div[1]/div/table/thead/tr/th[2]/div/a')
    client_name1_loc = (By.XPATH,'/html/body/div[3]/div[2]/div/div[1]/div/div[1]/div/table/thead/tr/th[3]/div/a')
    order_date_loc = (By.XPATH,'/html/body/div[3]/div[2]/div/div[1]/div/div[1]/div/table/thead/tr/th[4]/div/span')
    door_no_loc = (By.XPATH,'/html/body/div[3]/div[2]/div/div[1]/div/div[1]/div/table/thead/tr/th[5]/div/span')
    door_status_loc = (By.XPATH,'/html/body/div[3]/div[2]/div/div[1]/div/div[1]/div/table/thead/tr/th[6]/div/span')
    save_changes_btn_loc = (By.ID,'saveOnHoldListData')

    def go_hold_doors(self):
        self.driver.find_element(*self.list_loc).click()
        self.driver.find_element(*self.onhold_list_loc).click()
        WebDriverWait(self.driver,15).until(EC.visibility_of_element_located(self.on_hold_title_loc))

    @property
    def check_onhold_url(self):
        '''Check the URL for Job Accepted screen'''
        on_hold_url = self.driver.current_url
        print(on_hold_url)
        return on_hold_url

    @property
    def check_onhold_title(self):
        '''Check the title of Job Accepted screen'''
        on_hold_title = self.driver.find_element(*self.on_hold_title_loc).text
        print(on_hold_title)
        return on_hold_title

    @property
    def check_details(self):
        '''Check each elements in Details section'''
        client_details = self.driver.find_element(*self.client_details_loc).text
        client_name = self.driver.find_element(*self.client_name_loc).text
        contact_num = self.driver.find_element(*self.contact_num_loc).text
        location = self.driver.find_element(*self.location_loc).text
        suburb = self.driver.find_element(*self.suburb_loc).text
        site_address = self.driver.find_element(*self.site_address_loc).text
        quote_info = self.driver.find_element(*self.quote_info_loc).text
        proposal_no = self.driver.find_element(*self.proposal_no_loc).text
        user = self.driver.find_element(*self.user_loc).text
        print(client_details,client_name,contact_num,location,suburb,site_address,quote_info,proposal_no,user)
        return client_details,client_name,contact_num,location,suburb,site_address,quote_info,proposal_no,user

    @property
    def check_search_btn(self):
        '''Check the Search Quotes btn'''
        try:
            search_btn = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.search_quotes_btn_loc))
            print("it's clickable")
            return True
        except TimeoutException:
            print("it's not clickable")
            return False

    @property
    def check_results_found(self):
        '''Check the Results Found'''
        results_found = self.driver.find_element(*self.results_found_loc).text
        print(results_found)
        return results_found

    @property
    def check_columns(self):
        '''Check each column'''
        proposal = self.driver.find_element(*self.proposal_loc).text
        created_date = self.driver.find_element(*self.created_date_loc).text
        client_name1 = self.driver.find_element(*self.client_name1_loc).text
        order_date = self.driver.find_element(*self.order_date_loc).text
        door_no = self.driver.find_element(*self.door_no_loc).text
        door_status = self.driver.find_element(*self.door_status_loc).text
        print(proposal,created_date,client_name1,order_date,door_no,door_status)
        return proposal,created_date,client_name1,order_date,door_no,door_status

    @property
    def check_save_button(self):
        '''Check the Save changes button'''
        try:
            save_btn = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.save_changes_btn_loc))
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

    login = On_Hold(driver)
    login.typeUserName('aa@ecogaragedoors.com')
    login.typePassword('aabb')
    login.clickLogin()
    login.go_hold_doors()
    login.check_onhold_url
    login.check_onhold_title
    login.check_details
    login.check_search_btn
    login.check_columns
    login.check_save_button


