# Author:Yi Sun(Tim) 2023-11-13

'''Add Service Page'''

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.admin_portal import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class Add_Service(Admin_Page):

    search_service_title_loc = (By.XPATH,'//*[@id="serviceTitle"]/div/div[1]/span')     # new added
    search_service_loc = (By.XPATH,'//*[@id="serviceId"]/div/div[2]/span')
    add_new_service_btn = (By.ID,'btnServiceAdd')
    success_confirm_btn = (By.ID,'btnServiceConfirm')

    '''loc for each section in this page'''
    doors_section_loc = (By.CSS_SELECTOR, "[aria-label='doorsection']")
    service_details_loc = (By.CSS_SELECTOR, "[aria-label='servicedetails']")
    site_contact_details_loc = (By.CSS_SELECTOR, "[aria-label='sitecontact']")
    service_item_loc = (By.CSS_SELECTOR, "[aria-label='serviceitem']")
    service_documents_loc = (By.CSS_SELECTOR, "[aria-label='document']")
    back_service_btn = (By.ID,'btnBackToQuote')
    save_service_btn = (By.ID,'btnSaveService')
    add_service_item_btn = (By.ID, 'btnServiceItem')
    add_attachement_btn_loc = (By.ID,'servicenewfiles')

    '''loc for each element in "Doors" section"'''
    door_type_loc = (By.CSS_SELECTOR, "[aria-label='doortype']")
    door_type_select = (By.ID,'serviceDoorType')
    additional_info_loc = (By.CSS_SELECTOR, "[aria-label='additionalinfo']")
    additional_info_box = (By.ID,'serviceAdditionalDoorInfo')

    '''loc for each element in "Service Details" section"'''
    service_type_loc = (By.CSS_SELECTOR, "[aria-label='servicetype']")
    service_type_select = (By.ID,'serviceSupplyType')
    service_area_loc = (By.CSS_SELECTOR, "[aria-label='servicearea']")
    service_area_select = (By.ID,'serviceTypeValue')
    service_status_loc = (By.CSS_SELECTOR, "[aria-label='status']")
    service_status_select = (By.ID,'serviceStatusId')
    invoice_no_loc = (By.CSS_SELECTOR, "[aria-label='invoice']")
    invoice_no_box = (By.ID,'serviceInvoiceNo')
    account_type_loc = (By.CSS_SELECTOR, "[aria-label='accountype']")
    account_type_select = (By.ID,'servicePaymentTypeId')
    account_customer_loc = (By.CSS_SELECTOR, "[aria-label='accountcustomer']")
    account_customer_select = (By.ID,'serviceAccountCustomer')
    order_date_loc = (By.CSS_SELECTOR, "[aria-label='orderdate']")
    order_date_filter = (By.ID,'serviceOrderDate')
    service_date_loc = (By.CSS_SELECTOR, "[aria-label='servicedate']")
    service_date_filter = (By.ID,'serviceServiceDate')
    customer_po_loc = (By.CSS_SELECTOR, "[aria-label='customerpo']")
    customer_po_box = (By.ID,'serviceCustomerPO')
    user_loc = (By.CSS_SELECTOR, "[aria-label='userid']")
    user_select = (By.ID,'serviceUserAssigned')
    service_tech_loc = (By.CSS_SELECTOR, "[aria-label='servicetech']")
    service_tech_select = (By.ID,'serviceInstaller')
    service_tech_name_loc = (By.CSS_SELECTOR, "[aria-label='techname']")
    service_tech_name_box = (By.ID,'serviceTechName')
    description_loc = (By.CSS_SELECTOR, "[aria-label='description']")
    description_box = (By.ID,'serviceDescription')

    '''loc for each element in "Site Contact Details" section"'''
    client_name_box = (By.ID,'ClientNameTextBox')
    contact_address_box = (By.ID,'ContactAddressTextBox')
    contact_suburbb_box = (By.ID,'ContactSuburbTextBox')
    contact_mobile_box = (By.ID,'ContactMobileTextBox')

    def go_addservice(self):
        '''Switch to Add Service from LIST Menu'''
        self.driver.find_element(*self.list_loc).click()
        service_item_menu = self.driver.find_element(*self.services_list_loc)
        actions = ActionChains(self.driver)
        actions.move_to_element(service_item_menu).perform()   #move mouse to this menu item
        self.driver.find_element(*self.search_service_loc).click()
        WebDriverWait(self.driver,15).until(EC.visibility_of_element_located(self.search_service_title_loc))   #new added
        self.driver.find_element(*self.add_new_service_btn).click()
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.service_details_loc))    #new added
        # sleep(2)

    @property
    def check_add_service_url(self):
        '''check the url for Add Service page'''
        add_service_url = self.driver.current_url
        print(add_service_url)
        return add_service_url

    @property
    def check_sections(self):
        '''check each section in Add Service page'''
        doors_section = self.driver.find_element(*self.doors_section_loc).text
        service_details = self.driver.find_element(*self.service_details_loc).text
        site_contact_details = self.driver.find_element(*self.site_contact_details_loc).text
        service_items = self.driver.find_element(*self.service_item_loc).text
        service_documents = self.driver.find_element(*self.service_documents_loc).text
        print(doors_section,service_details,site_contact_details,service_items,service_documents)
        return doors_section,service_details,site_contact_details,service_items,service_documents

    @property
    def check_buttons(self):
        '''check each button in Add Service page'''
        back_service = self.driver.find_element(*self.back_service_btn).text
        save_service = self.driver.find_element(*self.save_service_btn).text
        print(back_service,save_service)
        return back_service

    @property
    def check_doors_section(self):
        '''check each elements in "Doors" section'''
        door_type = self.driver.find_element(*self.door_type_loc).text
        self.driver.find_element(*self.door_type_select).click()
        door_type_select = self.driver.find_element(*self.door_type_select).text
        additional_info = self.driver.find_element(*self.additional_info_loc).text
        print(door_type,door_type_select,additional_info)
        return door_type,door_type_select,additional_info

    @property
    def check_addition_box(self):
        '''check the Additional Door Infomation box in "Doors" section'''
        additional_info_box = self.driver.find_element(*self.additional_info_box)
        if additional_info_box.is_displayed:
            print('yes')
            return  True
        else:
            print('no')
            return  False

    @property
    def check_service_details(self):
        '''check each elements in "Service Details" section'''
        service_type = self.driver.find_element(*self.service_type_loc).text
        service_area = self.driver.find_element(*self.service_area_loc).text
        service_status = self.driver.find_element(*self.service_status_loc).text
        invoice_no = self.driver.find_element(*self.invoice_no_loc).text
        account_type = self.driver.find_element(*self.account_type_loc).text
        account_customer = self.driver.find_element(*self.account_customer_loc).text
        order_date = self.driver.find_element(*self.order_date_loc).text
        service_date = self.driver.find_element(*self.service_date_loc).text
        customer_po = self.driver.find_element(*self.customer_po_loc).text
        user = self.driver.find_element(*self.user_loc).text
        service_tech     = self.driver.find_element(*self.service_tech_loc).text
        service_tech_name = self.driver.find_element(*self.service_tech_name_loc).text
        description = self.driver.find_element(*self.description_loc).text
        print(service_type,service_area,service_status,invoice_no,account_type,account_customer,order_date,
              service_date,customer_po,user,service_tech,service_tech_name,description)
        return (service_type,service_area,service_status,invoice_no,account_type,account_customer,order_date,
                service_date,customer_po,user,service_tech,service_tech_name,description)

    def add_service_func(self):
        '''put details and add a new service'''
        wait = WebDriverWait(self.driver,5)
        door_type_select = Select(self.driver.find_element(*self.door_type_select))
        door_type_select.select_by_visible_text('Custom Door')
        self.driver.find_element(*self.additional_info_box).send_keys('Custom1000x3000 by Automation')
        service_type_select = Select(self.driver.find_element(*self.service_type_select))
        service_type_select.select_by_visible_text('Residential')
        service_area_select = Select(self.driver.find_element(*self.service_area_select))
        service_area_select.select_by_visible_text('Vic Metro')
        self.driver.find_element(*self.client_name_box).send_keys('Add_by_Automation')
        self.driver.find_element(*self.contact_address_box).send_keys('99 Auto added')
        self.driver.find_element(*self.contact_suburbb_box).send_keys('Kew')
        self.driver.find_element(*self.contact_mobile_box).send_keys('0400999999')
        # invoice_no = self.driver.find_element(*self.invoice_no_box).get_attribute('value')
        # return  invoice_no

    def save_service(self):
        ''''click the save service'''
        self.driver.find_element(*self.save_service_btn).click()
        success_confirm = WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(self.success_confirm_btn))
        success_confirm.click()




if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("http:// ")
    driver.implicitly_wait(10)

    login = Add_Service(driver)
    login.typeUserName('aa@ecogaragedoors.com')
    login.typePassword('aabb')
    login.clickLogin()
    login.go_addservice()
    login.check_add_service_url
    # login.check_sections
    # login.check_buttons
    # login.check_doors_section
    # login.check_addition_box
    # login.check_service_details
    login.add_service_func()
    login.save_service()