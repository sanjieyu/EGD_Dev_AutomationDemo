# Author:Yi Sun(Tim) 2023-09-04

'''Add Quote Page'''

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.admin_portal import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException

class Add_Quote(Admin_Page):
    """
        Note: For security and confidentiality, specific XPath/CSS selectors
        have been replaced with 'test_sample', and additional private locators
        have been omitted from this public sample.
        """

    main_page_loc = (By.ID,'test_sample')

    '''loc for each section in this page'''
    proposal_details_loc = (By.NAME,'test_sample')
    contact_details_loc = (By.NAME,'test_sample')

    # [Remaining 50+ locators redacted for confidentiality]


    def go_add(self):
        '''Switch to ADD Menu'''
        self.driver.find_element(*self.add_loc).click()

    def go_addquote(self):
        '''Switch to Add Quotes from Add Menu'''
        self.driver.find_element(*self.add_loc).click()
        self.driver.find_element(*self.quote_add_loc).click()
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(self.contact_details_loc))


    @property
    def check_addquote_url(self):
        '''check the url for Add Quote page'''
        add_quote_url = self.driver.current_url
        print(add_quote_url)
        return add_quote_url

    @property
    def check_defaulsection(self):
        '''check the default section in Add Quotes page'''
        proposal_details = self.driver.find_element(*self.proposal_details_loc).text
        contact_details = self.driver.find_element(*self.contact_details_loc).text
        site_details = self.driver.find_element(*self.site_details_loc).text
        doors = self.driver.find_element(*self.doors_loc).text
        print(proposal_details,contact_details,site_details,doors)
        return proposal_details,contact_details,site_details,doors

    @property
    def check_savequote_btn(self):
        '''check the save quote buton in Add Quotes page'''
        savequote_btn = self.driver.find_element(*self.save_quote_btn)
        if savequote_btn:
            return  True
        else:
            return False
    @property
    def check_proposal_details(self):
        '''check each description of Proplsal Details in Add Quotes page'''
        proposal_num = self.driver.find_element(*self.proposal_num_loc).text
        pricing_cate = self.driver.find_element(*self.pricing_cate_loc).text
        user_quote = self.driver.find_element(*self.user_quote_loc).text
        account_type = self.driver.find_element(*self.account_type_loc).text
        order_date = self.driver.find_element(*self.order_date_loc).text
        quote_status = self.driver.find_element(*self.quote_status_loc).text
        account_cus = self.driver.find_element(*self.account_customer_loc).text
        supply_type = self.driver.find_element(*self.supply_type_loc).text
        print(proposal_num,pricing_cate,user_quote,account_type,order_date,quote_status,account_cus,supply_type)
        return proposal_num,pricing_cate,user_quote,account_type,order_date,quote_status,account_cus,supply_type

    @property
    def check_pricing_cate_value(self):
        '''check each value in "Pricing Category" list'''
        self.driver.find_element(*self.pricing_cate_select).click()
        pricing_value = self.driver.find_element(*self.pricing_cate_select).text
        print(pricing_value)
        return pricing_value


    @property
    def check_default_pricing(self):
        '''check the default value in "Pricing Category" list'''
        self.driver.find_element(*self.pricing_cate_select).click()
        default_pricing_value = Select(self.driver.find_element(*self.pricing_cate_select)).first_selected_option.text
        print(default_pricing_value)
        return default_pricing_value

    @property
    def check_default_user(self):
        '''check the default value in "User" list'''
        self.driver.find_element(*self.user_quote_select).click()
        default_user_value = Select(self.driver.find_element(*self.user_quote_select)).first_selected_option.text
        print(default_user_value)
        return default_user_value

    @property
    def check_accounttype_value(self):
        '''check each value in "Account Type" list'''
        self.driver.find_element(*self.account_type_select).click()
        account_type_value = self.driver.find_element(*self.account_type_select).text
        print(account_type_value)
        return account_type_value


    @property
    def check_default_accounttype(self):
        '''check the default value in "Account Type" list'''
        self.driver.find_element(*self.account_type_select).click()
        default_accounttype_value = Select(self.driver.find_element(*self.account_type_select)).first_selected_option.text
        print(default_accounttype_value)
        return default_accounttype_value

    @property
    def check_quotestatus_value(self):
        '''check each value in "Quote Status" list'''
        self.driver.find_element(*self.quote_status_select).click()
        quote_status_value = self.driver.find_element(*self.quote_status_select).text
        print(quote_status_value)
        return quote_status_value


    @property
    def check_default_quotestatus(self):
        '''check the default value in "Quote Status" list'''
        self.driver.find_element(*self.quote_status_select).click()
        default_quotestatus_value = Select(self.driver.find_element(*self.quote_status_select)).first_selected_option.text
        print(default_quotestatus_value)
        return default_quotestatus_value

    @property
    def check_supplytype_value(self):
        '''check all values in "Supply Type" list'''
        self.driver.find_element(*self.supply_type_select).click()
        supplytype_value = self.driver.find_element(*self.supply_type_select).text
        print(supplytype_value)
        return supplytype_value

    @property
    def check_supplytype_default(self):
        '''check default values in "Supply Type" list'''
        self.driver.find_element(*self.supply_type_select).click()
        default_supplytype_value = Select(self.driver.find_element(*self.supply_type_select)).first_selected_option.text
        print(default_supplytype_value)
        return default_supplytype_value

    @property
    def check_changeto_Account(self):
        '''The "Account Customer" list should enable after select "Account" in "Account Type" list'''
        wait = WebDriverWait(self.driver,5)
        self.driver.find_element(*self.account_type_select).click()
        account_type_select = Select(wait.until(EC.presence_of_element_located(self.account_type_select)))
        account_type_select.select_by_visible_text('Account')
        account_customer_dropdown1 = wait.until(EC.presence_of_element_located(self.account_customer_select))
        print('attribute is:',account_customer_dropdown1.get_attribute)
        is_disabled = account_customer_dropdown1.get_attribute("disabled")
        if is_disabled:
            print("Account Customer is disabled")
            return  True
        else:
            print("Account Customer is enabled")
            return False

    @property
    def check_contact_details(self):
        '''check each section in "Contact Details"'''
        client_contact_details = self.driver.find_element(*self.client_contact_details_loc).text
        site_contact_details = self.driver.find_element(*self.site_contact_details_loc).text
        print(client_contact_details,site_contact_details)
        return client_contact_details,site_contact_details

    @property
    def check_client_contact_details(self):
        '''check each section in "Client Contact Details"'''
        client_name_details = self.driver.find_element(*self.client_name_loc).text
        cus_pur_order = self.driver.find_element(*self.customer_purchase_order_loc).text
        contact_name_details = self.driver.find_element(*self.contact_name_loc).text
        contact_mobile_details = self.driver.find_element(*self.contact_mobile_loc).text
        contact_email_details = self.driver.find_element(*self.contact_email_loc).text
        contact_address_details = self.driver.find_element(*self.contact_address_loc).text
        contact_suburb_details = self.driver.find_element(*self.contact_suburb_loc).text
        contact_postcode_details = self.driver.find_element(*self.contact_postcode_loc).text
        print(client_name_details,cus_pur_order,contact_name_details,contact_mobile_details,contact_email_details,contact_address_details,contact_suburb_details,contact_postcode_details)
        return client_name_details,cus_pur_order,contact_name_details,contact_mobile_details,contact_email_details,contact_address_details,contact_suburb_details,contact_postcode_details

    @property
    def check_client_name_box(self):
        '''check the input editbox for "Client Name"'''
        client_name_box_display = self.driver.find_element(*self.client_name_box)
        if client_name_box_display.is_displayed():
            print('true')
            return True
        else:
            print("false")
            return False

    @property
    def check_order_num_box(self):
        '''check the input editbox for "Customer Purchase Order"'''
        cus_order_display = self.driver.find_element(*self.order_num_box)
        if cus_order_display.is_displayed():
            print('true')
            return True
        else:
            print("false")
            return False

    @property
    def check_contact_name_box(self):
        '''check the input editbox for "Contact Name"'''
        contact_name_display = self.driver.find_element(*self.contact_name_box)
        if contact_name_display.is_displayed():
            print('true')
            return True
        else:
            print("false")
            return False

    @property
    def check_contact_mobile_box(self):
        '''check the input editbox for "Contact Mobile"'''
        contact_mobile_display = self.driver.find_element(*self.contact_mobile_box)
        if contact_mobile_display.is_displayed():
            print('true')
            return True
        else:
            print("false")
            return False

    @property
    def check_contact_email_box(self):
        '''check the input editbox for "Contact Email"'''
        contact_email_display = self.driver.find_element(*self.contact_email_box)
        if contact_email_display.is_displayed():
            print('true')
            return True
        else:
            print("false")
            return False

    @property
    def check_contact_address_box(self):
        '''check the input editbox for "Contact Address"'''
        contact_address_display = self.driver.find_element(*self.contact_address_box)
        if contact_address_display.is_displayed():
            print('true')
            return True
        else:
            print("false")
            return False

    @property
    def check_contact_suburb_box(self):
        '''check the input editbox for "Contact Suburb"'''
        contact_suburb_display = self.driver.find_element(*self.contact_suburb_box)
        if contact_suburb_display.is_displayed():
            print('true')
            return True
        else:
            print("false")
            return False

    @property
    def check_contact_postcode_box(self):
        '''check the input editbox for "Contact Postcode"'''
        contact_postcode_display = self.driver.find_element(*self.contact_postcode_box)
        if contact_postcode_display.is_displayed():
            print('true')
            return True
        else:
            print("false")
            return False

    @property
    def check_site_contact_details(self):
        '''check each section in "Site Contact Details"'''
        site_contact_name = self.driver.find_element(*self.site_contact_name).text
        site_phone = self.driver.find_element(*self.site_phone_loc).text
        site_email = self.driver.find_element(*self.site_email_loc).text
        site_address = self.driver.find_element(*self.site_address_loc).text
        site_suburb = self.driver.find_element(*self.site_suburb_loc).text
        site_postcode = self.driver.find_element(*self.site_postcode_loc).text
        print(site_contact_name,site_phone,site_email,site_address,site_suburb,site_postcode)
        return site_contact_name,site_phone,site_email,site_address,site_suburb,site_postcode

    @property
    def check_copy_checkbox(self):
        '''check the default status for checkbox for "Copy Client details"'''
        copy_checkbox= self.driver.find_element(*self.copy_checkbox_loc)
        if copy_checkbox.is_selected():
            print('true')
            return True
        else:
            print('false')
            return False

    @property
    def check_site_postcode_box(self):
        '''check the input editbox for "Site Postcode"'''
        site_postcode_box = self.driver.find_element(*self.site_postcode_box)
        if site_postcode_box.is_displayed():
            print('true')
            return True
        else:
            print("false")
            return False

    @property
    def check_site_contactname_box(self):
        '''check the input editbox for "Site Contact Name"'''
        site_contactname_box = self.driver.find_element(*self.site_contactname_box)
        if site_contactname_box.is_displayed():
            print('true')
            return True
        else:
            print("false")
            return False

    @property
    def check_site_phone_box(self):
        '''check the input editbox for "Site Phone"'''
        site_phone_box = self.driver.find_element(*self.site_phone_box)
        if site_phone_box.is_displayed():
            print('true')
            return True
        else:
            print("false")
            return False

    @property
    def check_site_email_box(self):
        '''check the input editbox for "Site Email"'''
        site_email_box = self.driver.find_element(*self.site_email_box)
        if site_email_box.is_displayed():
            print('true')
            return True
        else:
            print("false")
            return False

    @property
    def check_site_address_box(self):
        '''check the input editbox for "Site Address"'''
        site_address_box = self.driver.find_element(*self.site_email_box)
        if site_address_box.is_displayed():
            print('true')
            return True
        else:
            print("false")
            return False

    @property
    def check_site_suburb_box(self):
        '''check the input editbox for "Site Suburb"'''
        site_suburb_box = self.driver.find_element(*self.site_suburb_box)
        if site_suburb_box.is_displayed():
            print('true')
            return True
        else:
            print("false")
            return False

    @property
    def check_adddoor_btn(self):
        '''check the add new door button'''
        self.driver.find_element(*self.add_door_btn).click()
        add_door_btn = self.driver.find_element(*self.add_door_btn).text
        print(add_door_btn)
        return  add_door_btn

    @property
    def check_adddoor_menu(self):
        '''check the add new door menu'''
        door_item = []
        self.driver.implicitly_wait(3)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        self.driver.find_element(*self.add_door_btn).click()
        add_door_menu = self.driver.find_element(*self.add_door_menu)
        menu_element = add_door_menu.find_elements(By.XPATH,"test_sample")
        for item in menu_element:
            # print('menu item is:',item.text)
            door_item.append(item.text)
        print(door_item)
        return door_item

    @property
    def check_validation(self):
        '''check the validation for Add Quote page'''
        self.driver.find_element(*self.save_quote_btn).click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        validation_error = self.driver.find_element(*self.validation_error_loc).text
        validation_1 = self.driver.find_element(*self.validation_1_loc).text
        validation_2  = self.driver.find_element(*self.validation_2_loc).text
        self.driver.find_element(*self.validation_ok_btn).click()
        print(validation_error,validation_1,validation_2)
        return validation_error,validation_1,validation_2

    @property
    def check_add_quote_success(self):
        '''check Add Quote Successfully'''
        select_supplytype = Select(self.driver.find_element(*self.supply_type_select))
        select_supplytype.select_by_index(1)
        self.driver.find_element(*self.contact_email_box).send_keys('test')
        select_accounttype = Select(self.driver.find_element(*self.account_type_select))
        select_accounttype.select_by_visible_text("Account")
        self.driver.find_element(*self.account_customer_btn).click()
        self.driver.find_element(*self.propertygroup_customer_loc).click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element(*self.save_quote_btn).click()
        self.driver.execute_script("window.scrollTo(0, 0);")
        quote_success_created = WebDriverWait(self.driver,3).until(EC.visibility_of_element_located
                                                                   (self.quote_success_created_loc)).text
        print(quote_success_created)
        return quote_success_created

    def change_quote_detail(self):
        '''Change quote details from Account Cusomter to Cash sale, use for "add quote with door.py"'''
        select_supplytype = Select(self.driver.find_element(*self.supply_type_select))
        select_supplytype.select_by_index(2)
        select_accounttype = Select(self.driver.find_element(*self.account_type_select))
        select_accounttype.select_by_visible_text("Cash sale")
        self.driver.find_element(*self.client_name_box).send_keys("test_sample")
        self.driver.find_element(*self.contact_name_box).send_keys("test_sample")
        self.driver.find_element(*self.contact_mobile_box).send_keys("test_sample")
        self.driver.find_element(*self.contact_email_box).send_keys("test_sample")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element(*self.save_quote_btn).click()
        self.driver.find_element(*self.proceed_quote_btn).click()
        alert = self.driver.switch_to.alert
        alert.accept()

if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("http://xxxx/")
    driver.implicitly_wait(10)

    login = Add_Quote(driver)
    login.typeUserName('xxxx@test_sample')
    login.typePassword('test_sample')
    login.clickLogin()
    login.go_addquote()
    # login.check_addquote_url
    # login.check_searchurl
    # login.check_defaulsection
    # login.check_savequote_btn
    # login.check_proposal_details
    # login.check_pricing_cate_value
    # login.check_default_pricing
    # login.check_default_user
    # login.check_accounttype_value
    # login.check_default_accounttype
    # login.check_quotestatus_value
    login.check_default_quotestatus
    # login.check_account_customer_select
    # login.check_supplytype_value
    # login.check_supplytype_default
    # login.check_changeto_Account
    # login.check_contact_details
    # login.check_client_contact_details
    # login.check_client_name_box
    # login.check_order_num_box
    # login.check_client_name_box
    # login.check_contact_mobile_box
    # login.check_contact_email_box
    # login.check_contact_address_box
    # login.check_contact_suburb_box
    # login.check_contact_postcode_box
    # login.check_site_contact_details
    # login.check_copy_checkbox
    # login.check_site_contactname_box
    # login.check_site_phone_box
    # login.check_site_email_box
    # login.check_site_address_box
    # login.check_site_suburb_box
    # login.check_site_postcode_box
    # login.check_adddoor_btn
    # login.check_adddoor_menu
    # login.check_validation
    # login.check_add_quote_success
    # login.change_quote_detail()







