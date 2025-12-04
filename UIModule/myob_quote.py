# Author:Yi Sun(Tim) 2024-5-23

'''MYOB Quotes Page'''

import selenium
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from UIModule.admin_portal import *

class MYOB_Quotes(Admin_Page):
    myob_title_loc = (By.XPATH,'/html/body/div[3]/div[2]/div/h1')
    search_btn_loc = (By.ID,'btnMYOBQuoteSearch')
    searched_proposal_loc = (By.XPATH,'/html/body/div[3]/div[2]/div/div[1]/div/div[1]/div/table/tbody/tr[1]/td[2]/a')
    save_btn_loc = (By.ID,'saveMYOBListData')
    door_status_dropdown_loc = (By.XPATH,"//select[contains(@id, '_status')]")


    '''client details'''
    client_details_loc = (By.XPATH,'/html/body/div[3]/div[2]/div/div[1]/form/div/div/div[1]/div[1]/div[1]/h4')
    client_name_loc = (By.XPATH,'/html/body/div[3]/div[2]/div/div[1]/form/div/div/div[1]/div[1]/div[2]/label')
    contact_num_loc = (By.XPATH,'/html/body/div[3]/div[2]/div/div[1]/form/div/div/div[1]/div[1]/div[3]/label')
    client_name_box_loc = (By.ID,'ClientName')
    contact_num_box_loc = (By.ID,'ContactNumber')

    '''Location'''
    location_loc = (By.XPATH,'/html/body/div[3]/div[2]/div/div[1]/form/div/div/div[1]/div[2]/div[1]/h4')
    suburb_loc = (By.XPATH,'/html/body/div[3]/div[2]/div/div[1]/form/div/div/div[1]/div[2]/div[2]/label')
    site_address_loc = (By.XPATH,'/html/body/div[3]/div[2]/div/div[1]/form/div/div/div[1]/div[2]/div[3]/label')
    suburb_box_loc = (By.ID,'Suburb')
    site_address_box_loc = (By.ID,'SiteAddress')

    '''Quote Information'''
    quote_info_loc = (By.XPATH,'/html/body/div[3]/div[2]/div/div[1]/form/div/div/div[1]/div[3]/div[1]/h4')
    proposal_no_loc = (By.XPATH,'/html/body/div[3]/div[2]/div/div[1]/form/div/div/div[1]/div[3]/div[2]/label')
    user_loc = (By.XPATH,'/html/body/div[3]/div[2]/div/div[1]/form/div/div/div[1]/div[3]/div[3]/label')
    proposal_no_box_loc = (By.ID,'ProposalNo')
    user_select_loc = (By.ID,'UserAssignedId')

    def go_myob_quotes(self):
        '''Switch to MYOB Quotes page'''
        self.driver.find_element(*self.list_loc).click()
        self.driver.find_element(*self.myob_list_loc).click()
        WebDriverWait(self.driver,50).until(EC.visibility_of_element_located(self.myob_title_loc))

    @property
    def check_myob_url(self):
        '''Check the URL'''
        myob_quotes_url = self.driver.current_url
        print(myob_quotes_url)
        return myob_quotes_url

    @property
    def check_myob_title(self):
        '''Check the title'''
        myob_quotes_title = self.driver.find_element(*self.myob_title_loc).text
        print(myob_quotes_title)
        return myob_quotes_title

    @property
    def check_client_details(self):
        '''Check the client details section'''
        client_details = self.driver.find_element(*self.client_details_loc).text
        client_name = self.driver.find_element(*self.client_name_loc).text
        contact_num = self.driver.find_element(*self.contact_num_loc).text
        return client_details,client_name,contact_num

    @property
    def check_location(self):
        '''Check the Location section'''
        location = self.driver.find_element(*self.location_loc).text
        suburb = self.driver.find_element(*self.suburb_loc).text
        site_address = self.driver.find_element(*self.site_address_loc).text
        return location,suburb,site_address

    @property
    def check_quote_info(self):
        '''Check the Quote Information section'''
        quote_info = self.driver.find_element(*self.quote_info_loc).text
        proposal_no = self.driver.find_element(*self.proposal_no_loc).text
        user = self.driver.find_element(*self.user_loc).text
        return quote_info,proposal_no,user

    @property
    def check_client_name_box(self):
        '''Check the Client Name box'''
        client_name_box = self.driver.find_element(*self.client_name_box_loc)
        if client_name_box.is_displayed:
            return True
        else:
            return False

    @property
    def check_contact_num_box(self):
        '''Check the Contact Number box'''
        contact_num_box = self.driver.find_element(*self.contact_num_box_loc)
        if contact_num_box.is_displayed:
            return True
        else:
            return False

    @property
    def check_suburb_box(self):
        '''Check the Suburb box'''
        suburb_box = self.driver.find_element(*self.suburb_box_loc)
        if suburb_box.is_displayed:
            return True
        else:
            return False

    @property
    def check_site_address_box(self):
        '''Check the Site Address box'''
        site_address_box = self.driver.find_element(*self.site_address_box_loc)
        if site_address_box.is_displayed:
            return True
        else:
            return False

    @property
    def check_proposal_no_box(self):
        '''Check the Proposal No box'''
        proposal_no_box = self.driver.find_element(*self.proposal_no_box_loc)
        if proposal_no_box.is_displayed:
            return True
        else:
            return False

    @property
    def check_default_user(self):
        '''Check the default value in User box'''
        user_dropdown = Select(self.driver.find_element(*self.user_select_loc))
        default_user = user_dropdown.first_selected_option
        user_name = default_user.text
        print(user_name)
        return user_name

    @property
    def search_myob_fun(self):
        '''Check search function in MYOB by user'''
        user_dropdown = Select(self.driver.find_element(*self.user_select_loc))
        user_dropdown.select_by_visible_text("Yi_Account Sun")
        sleep(3)
        search_btn_des = self.driver.find_element(*self.search_btn_loc).text
        self.driver.find_element(*self.search_btn_loc).click()
        searched_result = self.driver.find_element(*self.searched_proposal_loc).text
        print(search_btn_des,searched_result)
        return searched_result

    '''Can't use Property here because it is being accessed as a property instead of a method. 
    In Python, methods should be called with parentheses to pass arguments properly.'''
    def input_proposal(self,proposal_number):
        '''Used by change_quote_status module'''
        self.driver.find_element(*self.proposal_no_box_loc).send_keys(proposal_number)
        sleep(3)
        self.driver.find_element(*self.search_btn_loc).click()





if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("http:// ")
    driver.implicitly_wait(10)

    login = MYOB_Quotes(driver)
    login.typeUserName('aa@ecogaragedoors.com')
    login.typePassword('aabb')
    login.clickLogin()
    login.go_myob_quotes()
    # login.check_myob_url
    # login.check_myob_title
    # login.check_client_details
    # login.check_location
    # login.check_quote_info
    # login.check_client_name_box
    # login.check_contact_num_box
    # login.check_suburb_box
    # login.check_site_address_box
    # login.check_proposal_no_box
    # login.check_default_user
    login.search_myob_fun
