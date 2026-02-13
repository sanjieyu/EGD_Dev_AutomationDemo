# Author:Yi Sun(Tim) 2024-11-13

'''Job Accepted Doors Page'''

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from pages.admin_portal import *
from selenium.common.exceptions import TimeoutException

class Job_Accepted(Admin_Page):

    job_accepted_title_loc = (By.NAME,'jobtitle')

    '''elements in Client Details section'''
    client_details_loc = (By.CSS_SELECTOR,"label[for='ClientDetails']")
    client_name_loc = (By.CSS_SELECTOR,"label[for='Name']")
    client_name_box_loc = (By.ID,'ClientName')
    contact_num_loc = (By.CSS_SELECTOR,"label[for='ContactNum']")
    contact_num_box_loc = (By.ID,'ContactNumber')
    location_loc = (By.CSS_SELECTOR,"label[for='Location']")
    suburb_loc = (By.CSS_SELECTOR,"label[for='Subrub']")
    suburb_box_loc = (By.ID,'Suburb')
    site_address_loc = (By.CSS_SELECTOR,"label[for='SiteAddress']")
    site_address_box_loc = (By.ID,'SiteAddress')
    quote_info_loc = (By.CSS_SELECTOR,"label[for='QuoteInfo']")
    proposal_no_loc = (By.CSS_SELECTOR,"label[for='ProposalNo']")
    proposal_no_box_loc = (By.ID,'ProposalNo')
    user_loc = (By.CSS_SELECTOR,"label[for='User']")
    user_select_loc = (By.ID,'UserAssignedId')
    search_quotes_btn_loc = (By.ID,"btnSearch")

    '''elements in Results section'''
    results_found_loc = (By.CSS_SELECTOR,"label[for='Result']")
    proposal_loc = (By.CSS_SELECTOR,"label[for='ProposalId']")
    account_loc = (By.CSS_SELECTOR,"label[for='Account']")
    payment_type_loc = (By.CSS_SELECTOR,"label[for='PaymentType']")
    client_name1_loc = (By.CSS_SELECTOR,"label[for='ClientName']")
    site_address1_loc = (By.CSS_SELECTOR,"label[for='SiteAddress']")
    door_no_loc = (By.CSS_SELECTOR,"label[for='DoorId']")
    sale_amount_loc = (By.CSS_SELECTOR,"label[for='SaleAmount']")
    deposit_loc = (By.CSS_SELECTOR,"label[for='Deposit']")
    door_status_loc = (By.CSS_SELECTOR,"label[for='DoorStatus']")
    save_changes_btn_loc = (By.ID,'saveJobExceptedListData')

    def go_job_accepted(self):
        self.driver.find_element(*self.list_loc).click()
        self.driver.find_element(*self.jobaccept_list_loc).click()
        WebDriverWait(self.driver,80).until(EC.visibility_of_element_located(self.job_accepted_title_loc))

    @property
    def check_jobaccepted_url(self):
        '''Check the URL for Job Accepted screen'''
        job_accetped_url = self.driver.current_url
        print(job_accetped_url)
        return job_accetped_url

    @property
    def check_jobaccepted_title(self):
        '''Check the title of Job Accepted screen'''
        job_accepted_title = self.driver.find_element(*self.job_accepted_title_loc).text
        print(job_accepted_title)
        return job_accepted_title

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
        account = self.driver.find_element(*self.account_loc).text
        payment_type = self.driver.find_element(*self.payment_type_loc).text
        client_name1 = self.driver.find_element(*self.client_name1_loc).text
        site_address1 = self.driver.find_element(*self.site_address1_loc).text
        door_no = self.driver.find_element(*self.door_no_loc).text
        sale_amount = self.driver.find_element(*self.sale_amount_loc).text
        deposit = self.driver.find_element(*self.deposit_loc).text
        door_status = self.driver.find_element(*self.door_status_loc).text
        print(proposal,account,payment_type,client_name1,site_address1,door_no,sale_amount,deposit,door_status)
        return proposal,account,payment_type,client_name1,site_address1,door_no,sale_amount,deposit,door_status

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

    login = Job_Accepted(driver)
    login.typeUserName('aa@ecogaragedoors.com')
    login.typePassword('aabb')
    login.clickLogin()
    login.go_job_accepted()
    # login.check_jobaccepted_url
    # login.check_jobaccepted_title
    # login.check_details
    login.check_search_btn
    # login.check_columns


