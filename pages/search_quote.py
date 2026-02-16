# Author:Yi Sun(Tim) 2023-08-29

'''Search Quote Page'''

import selenium
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from pages.admin_portal import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Search_Quote(Admin_Page):
    """
        Note: For security and confidentiality, specific XPath/CSS selectors
        have been replaced with 'test_sample', and additional private locators
        have been omitted from this public sample.
    """
    '''loc for default values in this page'''
    searchquote_title_loc = (By.NAME,'test_sample')
    quotes_sub_loc = (By.CSS_SELECTOR, "[aria-label='test_sample']")
    doors_sub_loc = (By.ID, 'test_sample')

    # [Remaining 30+ locators redacted for confidentiality]
    '''loc for default values in "Quotes" section'''
    '''Input box for each filter'''
    '''search by client name'''


    def go_list(self):
        '''Switch to LIST Menu'''
        self.driver.find_element(*self.list_loc).click()

    def go_searchquotes(self):
        '''Switch to Search Quotes from LIST Menu'''
        self.driver.find_element(*self.list_loc).click()
        self.driver.find_element(*self.quote_list_loc).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.searchquote_title_loc))

    @property
    def check_title(self):
        '''check the title for Search Quotes page'''
        searchquote_title = self.driver.find_element(*self.searchquote_title_loc).text
        return searchquote_title

    @property
    def check_defaulsection(self):
        '''check the default section in Search Quotes page'''
        searchquote_btn = self.driver.find_element(*self.searchquotes_btn_loc)
        if searchquote_btn:
            return  True
        else:
            return False


    @property
    def search_proposal_id(self):
        '''check the search by Proposal ID function'''
        input_proposalid = self.driver.find_element(*self.proposal_no_box_loc).send_keys('test_sample')
        self.driver.find_element(*self.searchquotes_btn_loc).click()
        searched_proposalno = self.driver.find_element(*self.proposalno_searched_loc).text
        self.driver.find_element(*self.proposal_no_box_loc).clear()
        return searched_proposalno

    @property
    def search_contact_num(self):
        '''check the search by Contact Number function'''
        input_contactnum = self.driver.find_element(*self.contact_num_box_loc).send_keys('test_sample')
        self.driver.find_element(*self.searchquotes_btn_loc).click()
        searched_proposalno = self.driver.find_element(*self.proposalno_searched_loc).text
        self.driver.find_element(*self.contact_num_box_loc).clear()
        return searched_proposalno

    @property
    def search_suburb(self):
        '''check the search by Suburb function'''
        input_suburb = self.driver.find_element(*self.suburb_box_loc).send_keys('test_sample')
        self.driver.find_element(*self.searchquotes_btn_loc).click()
        searched_proposalno = self.driver.find_element(*self.proposalno_searched_loc).text
        self.driver.find_element(*self.suburb_box_loc).clear()
        return searched_proposalno

    @property
    def search_postcode(self):
        '''check the search by Postcode function'''
        input_postcode= self.driver.find_element(*self.postcode_box_loc).send_keys('test_sample')
        self.driver.find_element(*self.searchquotes_btn_loc).click()
        searched_proposalno = self.driver.find_element(*self.proposalno_searched_loc).text
        self.driver.find_element(*self.postcode_box_loc).clear()
        return searched_proposalno

    @property
    def search_door_design(self):
        '''check the search by Door Design function'''
        wait = WebDriverWait(self.driver,5)
        door_design_select = Select(self.driver.find_element(*self.door_design_select_loc))
        door_design_select.select_by_visible_text('test_sample')
        self.driver.find_element(*self.searchquotes_btn_loc).click()
        searched_proposalno = self.driver.find_element(*self.proposalno_searched_loc).text
        door_design_select = Select(wait.until(EC.presence_of_element_located(self.door_design_select_loc)))
        door_design_select.select_by_index(0)
        return searched_proposalno



if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("test_sample")
    driver.implicitly_wait(10)

    login = Search_Quote(driver)
    login.typeUserName('test_sample')
    login.typePassword('test_sample')
    login.clickLogin()
    login.go_searchquotes()
    # login.check_searchurl
    # login.check_title
    # login.check_defaulsection
    # login.check_defaultvalue
    # login.check_defaultelements
    # login.check_section_quotes
    # login.check_date_range
    # login.check_client_details
    # login.check_quote_info
    # login.check_default_user
    # login.search_client_name
    # login.search_proposal_id
    # login.search_contact_num
    login.search_door_design
    # login.search_door_colour
    # login.search_door_category
    # login.search_suburb
    # login.search_postcode
    # login.search_site_address







