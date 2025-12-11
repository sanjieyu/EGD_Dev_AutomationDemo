# Author:Yi Sun(Tim) 2023-11-27

'''Add Service Function for non-existing quote'''

import selenium
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from UIModule.add_service import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class Add_Service_Func(Add_Service):


    '''loc for each section in this page'''
    doors_section_loc = (By.CSS_SELECTOR, "[aria-label='doorsection']")

    def go_addservice(self):
        '''Switch to Add Service from LIST Menu'''
        self.driver.find_element(*self.list_loc).click()
        service_item_menu = self.driver.find_element(*self.services_list_loc)
        actions = ActionChains(self.driver)
        actions.move_to_element(service_item_menu).perform()   #move mouse to this menu item
        self.driver.find_element(*self.search_service_loc).click()
        self.driver.find_element(*self.add_new_service_btn).click()
        sleep(2)

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
    # login.check_add_service_url
    # login.check_sections
    # login.check_buttons
    # login.check_doors_section
    # login.check_addition_box
    login.check_service_details