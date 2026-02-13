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

    '''loc for default values in this page'''
    searchquote_title_loc = (By.NAME,'searchquote')
    quotes_sub_loc = (By.CSS_SELECTOR, "[aria-label='quotes_sub']")
    doors_sub_loc = (By.CSS_SELECTOR, "[aria-label='doors_sub']")
    searchresult_loc = (By.CSS_SELECTOR, "[aria-label='search_result']")

    '''loc for default values in "Quotes" section'''
    date_range_loc = (By.CSS_SELECTOR, "[aria-label='date_range']")
    client_details_loc = (By.CSS_SELECTOR, "[aria-label='client_details']")
    quote_info_loc = (By.CSS_SELECTOR, "[aria-label='quote_info']")
    searchquotes_btn_loc = (By.ID,'btnSearchQuote')

    filter_date_loc = (By.CSS_SELECTOR, "[aria-label='filter_date']")
    user_loc = (By.CSS_SELECTOR, "[aria-label='user']")
    user_box_loc = (By.XPATH,'//*[@id="UserAssignedId"]')
    quote_status_loc = (By.CSS_SELECTOR, "[aria-label='quote_status']")

    client_name_loc = (By.CSS_SELECTOR, "[aria-label='client_name']")
    contact_number_loc = (By.CSS_SELECTOR, "[aria-label='contact_number']")
    suburb_loc = (By.CSS_SELECTOR, "[aria-label='suburb']")
    postcode_loc = (By.CSS_SELECTOR, "[aria-label='postcode']")

    proposal_no_loc = (By.CSS_SELECTOR, "[aria-label='proposal_no']")
    door_design_loc = (By.CSS_SELECTOR, "[aria-label='door_design']")
    colour_category_loc = (By.CSS_SELECTOR, "[aria-label='colour_category']")
    door_colour_loc = (By.CSS_SELECTOR, "[aria-label='door_colour']")
    site_address_loc = (By.CSS_SELECTOR, "[aria-label='site_address']")

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
    proposalno_searched_loc = (By.CSS_SELECTOR, "[aria-label='proposalno_searched']")

    def go_list(self):
        '''Switch to LIST Menu'''
        self.driver.find_element(*self.list_loc).click()

    def go_searchquotes(self):
        '''Switch to Search Quotes from LIST Menu'''
        self.driver.find_element(*self.list_loc).click()
        self.driver.find_element(*self.quote_list_loc).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.searchquote_title_loc))  # new added

    @property
    def check_title(self):
        '''check the title for Search Quotes page'''
        searchquote_title = self.driver.find_element(*self.searchquote_title_loc).text
        print(searchquote_title)
        return searchquote_title

    @property
    def check_searchurl(self):
        '''check the url for Search Quotes page'''
        searchquotes_url = self.driver.current_url
        print(searchquotes_url)
        return searchquotes_url

    @property
    def check_defaulsection(self):
        '''check the default section in Search Quotes page'''
        searchquote_btn = self.driver.find_element(*self.searchquotes_btn_loc)
        if searchquote_btn:
            print('exist')
            return  True
        else:
            print("not exist")
            return False

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
        site_address = self.driver.find_element(*self.site_address_loc).text
        print(proposal_no,door_design,colour_category,door_colour,site_address)
        return proposal_no,door_design,colour_category,door_colour,site_address

    @property
    def check_default_user(self):
        '''check the default user name in "User" filter in Quotes filter table'''
        user_dropdown = Select(self.driver.find_element(*self.user_box_loc))
        default_user = user_dropdown.first_selected_option
        user_name = default_user.text
        print(user_name)
        return user_name

    @property
    def search_client_name(self):
        '''check the search by client name function'''
        input_clientname = self.driver.find_element(*self.clientname_box_loc).send_keys('Test Automation')
        self.driver.find_element(*self.searchquotes_btn_loc).click()
        searched_proposalno = self.driver.find_element(*self.proposalno_searched_loc).text
        self.driver.find_element(*self.clientname_box_loc).clear()
        print(searched_proposalno)
        return searched_proposalno

    @property
    def search_proposal_id(self):
        '''check the search by Proposal ID function'''
        input_proposalid = self.driver.find_element(*self.proposal_no_box_loc).send_keys('210088')
        self.driver.find_element(*self.searchquotes_btn_loc).click()
        searched_proposalno = self.driver.find_element(*self.proposalno_searched_loc).text
        self.driver.find_element(*self.proposal_no_box_loc).clear()
        print(searched_proposalno)
        return searched_proposalno

    @property
    def search_contact_num(self):
        '''check the search by Contact Number function'''
        input_contactnum = self.driver.find_element(*self.contact_num_box_loc).send_keys('046999999')
        self.driver.find_element(*self.searchquotes_btn_loc).click()
        searched_proposalno = self.driver.find_element(*self.proposalno_searched_loc).text
        self.driver.find_element(*self.contact_num_box_loc).clear()
        print(searched_proposalno)
        return searched_proposalno

    @property
    def search_suburb(self):
        '''check the search by Suburb function'''
        input_suburb = self.driver.find_element(*self.suburb_box_loc).send_keys('BURWOOD EAST')
        self.driver.find_element(*self.searchquotes_btn_loc).click()
        searched_proposalno = self.driver.find_element(*self.proposalno_searched_loc).text
        self.driver.find_element(*self.suburb_box_loc).clear()
        print(searched_proposalno)
        return searched_proposalno

    @property
    def search_postcode(self):
        '''check the search by Postcode function'''
        input_postcode= self.driver.find_element(*self.postcode_box_loc).send_keys('3151')
        self.driver.find_element(*self.searchquotes_btn_loc).click()
        searched_proposalno = self.driver.find_element(*self.proposalno_searched_loc).text
        self.driver.find_element(*self.postcode_box_loc).clear()
        print(searched_proposalno)
        return searched_proposalno

    @property
    def search_door_design(self):
        '''check the search by Door Design function'''
        wait = WebDriverWait(self.driver,5)
        door_design_select = Select(self.driver.find_element(*self.door_design_select_loc))
        door_design_select.select_by_visible_text('Wideline')
        self.driver.find_element(*self.searchquotes_btn_loc).click()
        searched_proposalno = self.driver.find_element(*self.proposalno_searched_loc).text
        door_design_select = Select(wait.until(EC.presence_of_element_located(self.door_design_select_loc)))
        door_design_select.select_by_index(0)
        print(searched_proposalno)
        return searched_proposalno

    @property
    def search_door_colour(self):
        '''check the search by Door Colour function'''
        wait = WebDriverWait(self.driver,5)
        door_colour_select = Select(self.driver.find_element(*self.door_colour_select_loc))
        door_colour_select.select_by_visible_text('Wallaby')
        self.driver.find_element(*self.searchquotes_btn_loc).click()
        searched_proposalno = self.driver.find_element(*self.proposalno_searched_loc).text
        door_colour_select = Select(wait.until(EC.presence_of_element_located(self.door_colour_select_loc)))
        door_colour_select.select_by_index(0)
        print(searched_proposalno)
        return searched_proposalno

    @property
    def search_door_category(self):
        '''check the search by Colour Category function'''
        wait = WebDriverWait(self.driver,5)
        door_category_select = Select(self.driver.find_element(*self.door_category_select_loc))
        door_category_select.select_by_visible_text('Timber Essence')
        self.driver.find_element(*self.searchquotes_btn_loc).click()
        searched_proposalno = self.driver.find_element(*self.proposalno_searched_loc).text
        door_category_select = Select(wait.until(EC.presence_of_element_located(self.door_category_select_loc)))
        door_category_select.select_by_index(0)
        print(searched_proposalno)
        return searched_proposalno

    @property
    def search_site_address(self):
        '''check the search by Site Address function'''
        input_site_address= self.driver.find_element(*self.site_address_box_loc).send_keys('Automation')
        self.driver.find_element(*self.searchquotes_btn_loc).click()
        searched_proposalno = self.driver.find_element(*self.proposalno_searched_loc).text
        self.driver.find_element(*self.postcode_box_loc).clear()
        print(searched_proposalno)
        return searched_proposalno


if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(" ")
    driver.implicitly_wait(10)

    login = Search_Quote(driver)
    login.typeUserName('aa@ecogaragedoors.com')
    login.typePassword('aabb')
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







