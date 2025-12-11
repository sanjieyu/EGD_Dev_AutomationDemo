# Author:Yi Sun(Tim) 2023-11-9

'''Search Service Page'''

import selenium
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from UIModule.admin_portal import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class Search_Service(Admin_Page):

    search_service_loc = (By.ID,'serviceSearch')

    '''loc for default values in this page'''
    searchservice_title_loc = (By.NAME,'searchservice')
    quotes_sub_loc = (By.ID,'li-quote-search')
    service_sub_loc = (By.ID,'li-service-search')
    searchresult_loc = (By.CSS_SELECTOR, "[aria-label='search_result']")

    '''loc for default values in "Service" section'''
    date_range_loc = (By.CSS_SELECTOR, "[aria-label='date_range']")
    client_details_loc = (By.CSS_SELECTOR, "[aria-label='client_details']")
    service_info_loc = (By.CSS_SELECTOR, "[aria-label='service_info']")
    searchservice_btn_loc = (By.ID,'btnSearch')
    addservice_btn_loc = (By.ID, 'btnAdd')

    filter_date_loc = (By.CSS_SELECTOR, "[aria-label='filter_date']")
    user_loc = (By.CSS_SELECTOR, "[aria-label='user']")
    user_box = (By.ID,'ServiceSearchModel_UserAssignedId')
    filter_date_box = (By.ID,'ServiceFilterDate')
    searched_invoiceno_loc = (By.CSS_SELECTOR, "[aria-label='invoice']")

    client_name_loc = (By.CSS_SELECTOR, "[aria-label='client_name']")
    client_name_box = (By.ID,'ServiceSearchModel_ClientName')
    address_loc = (By.CSS_SELECTOR, "[aria-label='address']")
    address_box = (By.ID,'ServiceSearchModel_ContactAddress')
    contact_number_loc = (By.CSS_SELECTOR, "[aria-label='contact_number']")
    contact_number_box = (By.ID,'ServiceSearchModel_ContactNumber')
    suburb_loc = (By.CSS_SELECTOR, "[aria-label='suburb']")
    suburb_box = (By.ID,'ServiceSearchModel_Suburb')
    postcode_loc = (By.CSS_SELECTOR, "[aria-label='postcode']")
    postcode_box = (By.ID,'ServiceSearchModel_Postcode')

    service_status_loc = (By.CSS_SELECTOR, "[aria-label='service_status']")
    service_status_select = (By.ID,'ServiceSearchModel_ServiceStatusId')
    service_area_loc = (By.CSS_SELECTOR, "[aria-label='service_area']")
    service_area_select = (By.ID,'ServiceSearchModel_ServiceTypeId')
    service_type_loc = (By.CSS_SELECTOR, "[aria-label='service_type']")
    service_type_select = (By.ID,'ServiceSearchModel_ServiceSupplyTypeId')
    invoice_no_loc = (By.CSS_SELECTOR, "[aria-label='invoice_no']")
    invoice_no_box = (By.ID,'ServiceSearchModel_InvoiceNo')
    customer_po_loc = (By.CSS_SELECTOR, "[aria-label='customer_po']")
    customer_po_box = (By.ID,'ServiceSearchModel_CustomerPO')

    def go_searchservice(self):
        '''Switch to Search Service from LIST Menu'''
        self.driver.find_element(*self.list_loc).click()
        service_item_menu = self.driver.find_element(*self.services_list_loc)
        actions = ActionChains(self.driver)
        actions.move_to_element(service_item_menu).perform()   #move mouse to this menu item
        self.driver.find_element(*self.search_service_loc).click()
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.searchservice_title_loc))  # new added

    @property
    def check_title(self):
        '''check the title for Search Service page'''
        search_service_title = self.driver.find_element(*self.searchservice_title_loc).text
        print(search_service_title)
        return search_service_title

    @property
    def check_searchurl(self):
        '''check the url for Search Service page'''
        search_service_url = self.driver.current_url
        print(search_service_url)
        return search_service_url

    @property
    def check_defaulsection(self):
        '''check the default section in Search Service page'''
        search_service_btn = self.driver.find_element(*self.service_sub_loc)
        if search_service_btn:
            print('exist')
            return  True
        else:
            print("not exist")
            return False

    @property
    def check_defaultelements(self):
        '''check the default elements in Search Service page'''
        quotes_sub = self.driver.find_element(*self.quotes_sub_loc).text
        service_sub = self.driver.find_element(*self.service_sub_loc).text
        search_result = self.driver.find_element(*self.searchresult_loc).text
        print(quotes_sub,service_sub,search_result)
        return quotes_sub,service_sub,search_result

    @property
    def check_section_service(self):
        '''check each section of Service filter table in Search Service page'''
        date_range = self.driver.find_element(*self.date_range_loc).text
        client_details = self.driver.find_element(*self.client_details_loc).text
        service_info = self.driver.find_element(*self.service_info_loc).text
        print(date_range,client_details,service_info)
        return date_range,client_details,service_info

    @property
    def check_date_range(self):
        '''check each filter in "Date Range" in Service filter table'''
        filter_date = self.driver.find_element(*self.filter_date_loc).text
        user = self.driver.find_element(*self.user_loc).text
        print(filter_date,user)
        return filter_date,user

    @property
    def check_client_details(self):
        '''check each filter in "Client Details" in Service filter table'''
        client_name = self.driver.find_element(*self.client_name_loc).text
        contact_number = self.driver.find_element(*self.contact_number_loc).text
        suburb = self.driver.find_element(*self.suburb_loc).text
        postcode = self.driver.find_element(*self.postcode_loc).text
        address = self.driver.find_element(*self.address_loc).text
        print(client_name,address,suburb,postcode,contact_number)
        return client_name,address,suburb,postcode,contact_number

    @property
    def check_service_info(self):
        '''check each filter in "Service Infomation" in Service filter table'''
        service_status = self.driver.find_element(*self.service_status_loc).text
        service_area = self.driver.find_element(*self.service_area_loc).text
        service_type = self.driver.find_element(*self.service_type_loc).text
        invoice_no = self.driver.find_element(*self.invoice_no_loc).text
        customer_po = self.driver.find_element(*self.customer_po_loc).text
        print(service_status,service_area,service_type,invoice_no,customer_po)
        return service_status,service_area,service_type,invoice_no,customer_po

    @property
    def check_default_user(self):
        '''check the default user name in "User" filter in Service filter table'''
        user_dropdown = Select(self.driver.find_element(*self.user_box))
        default_user = user_dropdown.first_selected_option
        user_name = default_user.text
        print(user_name)
        return user_name

    @property
    def search_client_name(self):
        '''check the search by client name function'''
        input_clientname = self.driver.find_element(*self.client_name_box).send_keys('Automation Test')
        self.driver.find_element(*self.searchservice_btn_loc).click()
        searched_invoiceno = self.driver.find_element(*self.searched_invoiceno_loc).text
        self.driver.find_element(*self.client_name_box).clear()
        print(searched_invoiceno)
        return searched_invoiceno

    @property
    def search_address(self):
        '''check the search by Address function'''
        input_address = self.driver.find_element(*self.address_box).send_keys('Bonview')
        self.driver.find_element(*self.searchservice_btn_loc).click()
        searched_invoiceno = self.driver.find_element(*self.searched_invoiceno_loc).text
        self.driver.find_element(*self.address_box).clear()
        print(searched_invoiceno)
        return searched_invoiceno

    @property
    def search_suburb(self):
        '''check the search by Suburb function'''
        input_suburb = self.driver.find_element(*self.suburb_box).send_keys('BURWOOD EAST')
        self.driver.find_element(*self.searchservice_btn_loc).click()
        searched_invoiceno = self.driver.find_element(*self.searched_invoiceno_loc).text
        self.driver.find_element(*self.suburb_box).clear()
        print(searched_invoiceno)
        return searched_invoiceno

    @property
    def search_postcode(self):
        '''check the search by Postcode function'''
        input_postcode= self.driver.find_element(*self.postcode_box).send_keys('3151')
        self.driver.find_element(*self.searchservice_btn_loc).click()
        searched_invoiceno = self.driver.find_element(*self.searched_invoiceno_loc).text
        self.driver.find_element(*self.postcode_box).clear()
        print(searched_invoiceno)
        return searched_invoiceno

    @property
    def search_contact_num(self):
        '''check the search by Contact Number function'''
        input_contactnum = self.driver.find_element(*self.contact_number_box).send_keys('0469888888')
        self.driver.find_element(*self.searchservice_btn_loc).click()
        searched_invoiceno = self.driver.find_element(*self.searched_invoiceno_loc).text
        self.driver.find_element(*self.contact_number_box).clear()
        print(searched_invoiceno)
        return searched_invoiceno

    @property
    def check_service_status(self):
        '''check the Service Status dropdown list'''
        self.driver.find_element(*self.service_status_select).click()
        service_status_list = self.driver.find_element(*self.service_status_select).text
        print(service_status_list)
        return service_status_list

    @property
    def check_service_area(self):
        '''check the Service Area dropdown list'''
        self.driver.find_element(*self.service_area_select).click()
        service_area_list = self.driver.find_element(*self.service_area_select).text
        print(service_area_list)
        return service_area_list

    @property
    def check_service_type(self):
        '''check the Service Type dropdown list'''
        self.driver.find_element(*self.service_type_select).click()
        service_type_list = self.driver.find_element(*self.service_type_select).text
        print(service_type_list)
        return service_type_list

    @property
    def search_invoice_no(self):
        '''check the search by Invoice No. function'''
        input_invoice_no = self.driver.find_element(*self.invoice_no_box).send_keys('204325S1')
        self.driver.find_element(*self.searchservice_btn_loc).click()
        searched_invoiceno = self.driver.find_element(*self.searched_invoiceno_loc).text
        self.driver.find_element(*self.invoice_no_box).clear()
        print(searched_invoiceno)
        return searched_invoiceno

    @property
    def search_customer_po(self):
        '''check the search by Customer PO function'''
        input_customer_po= self.driver.find_element(*self.customer_po_box).send_keys('Automation Test')
        self.driver.find_element(*self.searchservice_btn_loc).click()
        searched_invoiceno = self.driver.find_element(*self.searched_invoiceno_loc).text
        self.driver.find_element(*self.customer_po_box).clear()
        print(searched_invoiceno)
        return searched_invoiceno

if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("http:// ")
    driver.implicitly_wait(10)

    login = Search_Service(driver)
    login.typeUserName('aa@ecogaragedoors.com')
    login.typePassword('aabb')
    login.clickLogin()
    login.go_searchservice()
    # login.check_searchurl
    # login.check_title
    # login.check_defaulsection
    # login.check_defaultvalue
    # login.check_defaultelements
    # login.check_section_service
    # login.check_date_range
    # login.check_client_details
    # login.check_service_info
    # login.check_default_user
    login.search_client_name
    # login.search_address
    # login.search_suburb
    # login.search_postcode
    # login.search_contact_num
    # login.check_service_status
    # login.check_service_area
    # login.check_service_type

    # login.search_invoice_no
    # login.search_customer_po







