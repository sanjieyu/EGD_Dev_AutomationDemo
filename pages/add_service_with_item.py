# Author:Yi Sun(Tim) 2023-11-28

'''Add a Service with service items function'''

import selenium
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from pages.login_admin import Admin_Portal
from pages.add_service import Add_Service
from pages.add_service_item import Add_Service_Item
from pages.add_service_doc import Add_Service_Doc
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.action_chains import ActionChains

class Add_Service_With_Items():

    invoice_no_box1 = (By.ID,'serviceInvoiceNo')   #get the proposal number for the edit box
    list_loc = (By.ID,'list')
    list_menu_loc = (By.ID,'listmenu')
    services_list_loc = (By.ID,'servicelist')
    search_service_loc = (By.ID, 'searchservice')
    invoice_no_box2 = (By.ID, 'ServiceSearchModel_InvoiceNo')
    searchservice_btn_loc = (By.ID, 'btnSearch')
    searched_invoiceno_loc = (By.CSS_SELECTOR, "[aria-label='invoiceid']")
    searched_client_name = (By.ID, 'clientname')

    '''new added service item section'''
    quantity_loc = (By.XPATH,'//*[@id="quantity"]/div/div[2]/span')
    service_type_loc = (By.XPATH,'//*[@id="servicetype"]/div/div[2]/span')
    name_loc = (By.XPATH,'//*[@id="name"]/div/div[2]/span')
    original_price_loc = (By.XPATH,'//*[@id="originalprice"]/div/div[2]/span')
    item_discount_loc = (By.XPATH,'//*[@id="discount"]/div/div[2]/span')
    final_price_loc = (By.XPATH,'//*[@id="finalprice"]/div/div[2]/span')
    total_price_loc = (By.ID,'totalPriceServiceItem')

    upload_doc_loc = (By.XPATH,'//*[@id="upload"]/div/div[1]/span')
    service_doc_loc = (By.XPATH,'//*[@id="servicedoc"]/div/div[2]/span')



    def __init__(self,driver):
        self.driver = driver
        self.add_service = Add_Service(self.driver)
        self.add_service_item = Add_Service_Item(self.driver)
        self.add_service_doc = Add_Service_Doc(self.driver)

    def add_service_fun(self):
        self.add_service.go_addservice()
        self.add_service.add_service_func()
        self.add_service_item.go_service_item()
        self.add_service_item.add_item_success
        self.add_service_doc.upload_attachement()
        sleep(2)
        self.add_service.save_service()
        sleep(2)
        self.driver.refresh()

    @property
    def get_invoice_no(self):
        global invoice_no
        invoice_no = self.driver.find_element(*self.invoice_no_box1).get_attribute('value')  #取对话框里面的job nubmer的值
        print('number is:',invoice_no)
        return invoice_no

    @property
    def get_service_upload_doc(self):
        '''Upload Attachement function'''
        upload_doc = self.driver.find_element(*self.upload_doc_loc).text
        print(upload_doc)
        return upload_doc
    @property
    def get_service_quote_doc(self):
        '''Generate the Service Quote Document function'''
        service_quote_doc = self.driver.find_element(*self.service_doc_loc).text
        print(service_quote_doc)
        return service_quote_doc

    @property
    def check_quantity(self):
        '''Check the Quantity amount for the new added item'''
        item_quantity = self.driver.find_element(*self.quantity_loc).text
        print(item_quantity)
        return item_quantity

    @property
    def check_service_type(self):
        '''Check the Service Type for the new added item'''
        service_type = self.driver.find_element(*self.service_type_loc).text
        print(service_type)
        return service_type

    @property
    def check_item_name(self):
        '''Check the Item name for the new added item'''
        item_name = self.driver.find_element(*self.name_loc).text
        print(item_name)
        return item_name

    @property
    def check_original_price(self):
        '''Check the Original Price for the new added item'''
        original_price = self.driver.find_element(*self.original_price_loc).text
        print(original_price)
        return original_price

    @property
    def check_discount(self):
        '''Check the Discount for the new added item'''
        item_discount = self.driver.find_element(*self.item_discount_loc).text
        print(item_discount)
        return item_discount

    @property
    def check_final_price(self):
        '''Check the Final Price for the new added item'''
        final_price = self.driver.find_element(*self.final_price_loc).text
        print(final_price)
        return final_price

    @property
    def check_total_price(self):
        '''Check the Total Price for the new added item'''
        total_price = self.driver.find_element(*self.total_price_loc).text
        print(total_price)
        return total_price


    @property
    def search_new_service(self):
        self.driver.find_element(*self.list_loc).click()
        list_menu = self.driver.find_element(*self.list_menu_loc)
        service_item_menu = self.driver.find_element(*self.services_list_loc)
        actions = ActionChains(self.driver)
        actions.move_to_element(list_menu).pause(1).move_to_element(service_item_menu).perform()   #move mouse to this menu item
        # sleep(1)
        self.driver.find_element(*self.search_service_loc).click()   #go to search service page
        input_invoice_no = self.driver.find_element(*self.invoice_no_box2).send_keys(invoice_no)   #search the added invoice no.
        self.driver.find_element(*self.searchservice_btn_loc).click()
        searched_client_name = self.driver.find_element(*self.searched_client_name).text
        self.driver.find_element(*self.invoice_no_box2).clear()
        print(searched_client_name)
        return searched_client_name



if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("http:// ")
    driver.implicitly_wait(10)

    login = Admin_Portal(driver)
    login.typeUserName('aa@ecogaragedoors.com')
    login.typePassword('aabb')
    login.clickLogin()
    login1 = Add_Service_With_Items(driver)
    login1.add_service_fun()
    login1.get_invoice_no
    # login1.get_service_quote_doc
    # login1.check_quantity
    # login1.check_service_type
    # login1.check_item_name
    # login1.check_original_price
    # login1.check_discount
    # login1.check_final_price
    # login1.check_total_price
    login1.search_new_service




