# Author:Yi Sun(Tim) 2025-01-21

'''Search Quote Page on Dealer Portal'''

import selenium
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from UIModule.dealer_portal import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Search_Quote_DP(Deal_Portal):
    '''loc for default values in this page'''
    search_title_loc = (By.XPATH,'/html/body/div[3]/div[2]/div/div/h1')
    quotes_sub_loc = (By.XPATH,'/html/body/div[3]/div[2]/div/div/div/form/ul/li[1]/a')
    doors_sub_loc = (By.XPATH,'/html/body/div[3]/div[2]/div/div/div/form/ul/li[2]/a')
    searchresult_loc = (By.XPATH,'/html/body/div[3]/div[2]/div/div/div/div/div/h4')

    '''loc for default values in "Quotes" section'''
    date_range_loc =(By.XPATH,'/html/body/div[3]/div[2]/div/div/div/form/div/div/div[1]/div/div[1]/div[1]/h4')
    client_details_loc = (By.XPATH,'/html/body/div[3]/div[2]/div/div/div/form/div/div/div[1]/div/div[2]/div[1]/h4')
    quote_info_loc = (By.XPATH,'/html/body/div[3]/div[2]/div/div/div/form/div/div/div[1]/div/div[3]/div[1]/h4')
    searchquotes_btn_loc = (By.XPATH,'/html/body/div[3]/div[2]/div/div/div/form/div/div/div[1]/div/div[4]/div/input')

    filter_date_loc =(By.XPATH,'/html/body/div[3]/div[2]/div/div/div/form/div/div/div[1]/div/div[1]/div[2]/label')
    user_loc = (By.XPATH,'/html/body/div[3]/div[2]/div/div/div/form/div/div/div[1]/div/div[1]/div[3]/label')
    user_box_loc = (By.XPATH,'//*[@id="UserAssignedId"]')
    quote_status_loc = (By.XPATH,'/html/body/div[3]/div[2]/div/div/div/form/div/div/div[1]/div/div[1]/div[4]/label')

    client_name_loc =(By.XPATH,'/html/body/div[3]/div[2]/div/div/div/form/div/div/div[1]/div/div[2]/div[2]/label')
    contact_number_loc = (By.XPATH,'/html/body/div[3]/div[2]/div/div/div/form/div/div/div[1]/div/div[2]/div[3]/label')
    suburb_loc = (By.XPATH,'/html/body/div[3]/div[2]/div/div/div/form/div/div/div[1]/div/div[2]/div[4]/label')
    postcode_loc = (By.XPATH, '/html/body/div[3]/div[2]/div/div/div/form/div/div/div[1]/div/div[2]/div[5]/label')

    proposal_no_loc =(By.XPATH,'/html/body/div[3]/div[2]/div/div/div/form/div/div/div[1]/div/div[3]/div[2]/label')
    door_design_loc = (By.XPATH,'/html/body/div[3]/div[2]/div/div/div/form/div/div/div[1]/div/div[3]/div[3]/label')
    colour_category_loc = (By.XPATH,'/html/body/div[3]/div[2]/div/div/div/form/div/div/div[1]/div/div[3]/div[4]/label')
    door_colour_loc = (By.XPATH, '/html/body/div[3]/div[2]/div/div/div/form/div/div/div[1]/div/div[3]/div[5]/label')

    '''Input box for each filter'''
    clientname_box_loc = (By.ID, 'ClientName')
    proposal_no_box_loc = (By.ID, 'ProposalNo')
    contact_num_box_loc = (By.ID,'Contact_Number')
    suburb_box_loc = (By.ID,'Suburb')
    postcode_box_loc = (By.ID,'Postcode')
    door_design_select_loc = (By.ID,'DoorDesign')
    door_colour_select_loc =(By.ID,'DoorColor')
    door_category_select_loc = (By.ID,'ColourCategory')
    site_address_box_loc = (By.ID,'SiteAddress')

    '''search by client name'''
    proposalno_searched_loc = (By.XPATH,'/html/body/div[3]/div[2]/div/div/div/div/div/div/div/div/table/tbody/tr/td[2]/a')

    def go_search_quotes(self):
        '''go to search quotes page'''
        self.driver.find_element(*self.find_quote_btn).click()
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.search_title_loc))

    @property
    def check_title(self):
        '''check the title for Search Quotes page'''
        searchquote_title = self.driver.find_element(*self.search_title_loc).text
        print(searchquote_title)
        return searchquote_title

    @property
    def check_searchurl(self):
        '''check the url for Search Quotes page'''
        searchquotes_url = self.driver.current_url
        print(searchquotes_url)
        return searchquotes_url

    @property
    def check_search_btn(self):
        '''check the search quotes button'''
        search_btn = self.driver.find_element(*self.searchquotes_btn_loc)
        if search_btn:
            print('exist')
            return True
        else:
            print('not exist')
            return  False

    @property
    def check_defaultelements(self):
        '''check the default elements in Search Quotes page'''
        quotes_sub = self.driver.find_element(*self.quotes_sub_loc).text
        doors_sub = self.driver.find_element(*self.doors_sub_loc).text
        search_result = self.driver.find_element(*self.searchresult_loc).text
        print(quotes_sub,doors_sub,search_result)
        return quotes_sub,doors_sub,search_result

    @property
    def check_section_quotes(self):
        '''check each section of Quotes filter table in Search Quotes page'''
        date_range = self.driver.find_element(*self.date_range_loc).text
        client_details = self.driver.find_element(*self.client_details_loc).text
        quote_info = self.driver.find_element(*self.quote_info_loc).text
        print(date_range,client_details,quote_info)
        return date_range,client_details,quote_info

    @property
    def check_date_range(self):
        '''check each filter in "Date Range" in Quotes filter table'''
        filter_date = self.driver.find_element(*self.filter_date_loc).text
        user = self.driver.find_element(*self.user_loc).text
        quote_status = self.driver.find_element(*self.quote_status_loc).text
        print(filter_date,user,quote_status)
        return filter_date,user,quote_status

    @property
    def check_client_details(self):
        '''check each filter in "Client Details" in Quotes filter table'''
        client_name = self.driver.find_element(*self.client_name_loc).text
        contact_number = self.driver.find_element(*self.contact_number_loc).text
        suburb = self.driver.find_element(*self.suburb_loc).text
        postcode = self.driver.find_element(*self.postcode_loc).text
        print(client_name,contact_number,suburb,postcode)
        return client_name,contact_number,suburb,postcode

    @property
    def check_quote_info(self):
        '''check each filter in "Quote Infomation" in Quotes filter table'''
        proposal_no = self.driver.find_element(*self.proposal_no_loc).text
        door_design = self.driver.find_element(*self.door_design_loc).text
        colour_category = self.driver.find_element(*self.colour_category_loc).text
        door_colour = self.driver.find_element(*self.door_colour_loc).text
        print(proposal_no,door_design,colour_category,door_colour)
        return proposal_no,door_design,colour_category,door_colour
    @property
    def check_default_user(self):
        '''check the default user name in "User" filter in Quotes filter table'''
        user_dropdown = Select(self.driver.find_element(*self.user_box_loc))
        default_user = user_dropdown.first_selected_option
        user_name = default_user.text
        print(user_name)
        return user_name

    @property
    def search_proposal_id(self):
        '''check the search by Proposal ID function'''
        input_proposalid = self.driver.find_element(*self.proposal_no_box_loc).send_keys('209239')
        self.driver.find_element(*self.searchquotes_btn_loc).click()
        searched_proposalno = self.driver.find_element(*self.proposalno_searched_loc).text
        self.driver.find_element(*self.proposal_no_box_loc).clear()
        print(searched_proposalno)
        return searched_proposalno


if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("http:// ")
    driver.implicitly_wait(10)

    login = Search_Quote_DP(driver)
    login.typeUserName('aa@ecogaragedoors.com')
    login.typePassword('aabb')
    login.clickLogin()
    login.go_search_quotes()
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
    login.search_proposal_id
    # login.search_contact_num
    # login.search_door_design
    # login.search_door_colour
    # login.search_door_category
    # login.search_suburb
    # login.search_postcode
    # login.search_site_address