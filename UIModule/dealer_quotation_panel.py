# Author:Yi Sun(Tim) 2025-2-07

'''Check the Quotation screen for a dealer quote with a panel lift door'''

import selenium
from selenium import webdriver
from time import sleep
from  selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from UIModule.login_admin import Admin_Portal
from UIModule.add_dealer_quote_with_panel_door import Add_Dealer_Quote_With_Panel_Door

class Dealer_Quotation_Panel():

    '''the quotation option in the drop down list'''
    setting_btn_loc = (By.ID,'btnSettings')
    quotation_loc = (By.CSS_SELECTOR,"label[for='Quotation']")

    '''Major sections on Quotation screen'''
    quotation_section_loc = (By.CSS_SELECTOR,"label[for='QuotationSec']")
    job_summary_section_loc = (By.CSS_SELECTOR,"label[for='JobSummary']")
    total_cost_loc  = (By.CSS_SELECTOR,"label[for='TotalCost']")
    proposal_doc_section_loc = (By.CSS_SELECTOR,"label[for='ProposalDoc']")
    door1_section_loc = (By.CSS_SELECTOR,"label[for='DoorSection']")
    back_btn_loc = (By.XPATH,'//*[@id="backlink"]')
    save_btn_loc = (By.ID,'btnSaveFinal')
    send_email_btn_loc = (By.ID, 'btnSendEmail')
    submit_quote_btn_loc = (By.ID, 'btnSubmitQuoteFinal')

    '''Each element in Quotation section'''
    client_name_loc = (By.CSS_SELECTOR,"label[for='ClientName']")
    mobile_loc = (By.CSS_SELECTOR,"label[for='Mobile']")
    proposal_num_loc = (By.CSS_SELECTOR,"label[for='ProposalNum']")
    contact_full_adds_loc = (By.CSS_SELECTOR,"label[for='ContactAddress']")
    salesperson_loc = (By.CSS_SELECTOR,"label[for='SalesPerson']")

    client_name_box_loc = (By.ID,'ClientName')
    mobile_box_loc = (By.ID, 'ContactMobile')
    proposal_num_box_loc = (By.ID, 'ProposalNo')
    contact_full_adds_box_loc = (By.ID, 'ContactFullAddress')
    salesperson_box_loc = (By.ID, 'SalesPerson')

    '''Each element in Job Summary section'''
    door1_summary_loc = (By.CSS_SELECTOR,"label[for='DoorSummary']")
    door1_setting_btn_loc = (By.ID, 'btnDoorSettings')
    door_type_value_loc = (By.CSS_SELECTOR,"label[for='DoorType']")
    actual_height_value_loc = (By.CSS_SELECTOR,"label[for='ActualHeight']")
    door_design_value_loc = (By.CSS_SELECTOR,"label[for='DoorDesign']")
    actual_width_value_loc = (By.CSS_SELECTOR,"label[for='ActualWidth']")
    door_finish_value_loc = (By.CSS_SELECTOR,"label[for='DoorFinish']")
    category_value_loc = (By.CSS_SELECTOR,"label[for='Category']")
    opening_sizeLH_value_loc = (By.CSS_SELECTOR,"label[for='OpeningLH']")
    opening_sizeRH_value_loc = (By.CSS_SELECTOR,"label[for='OpeningRH']")
    opening_sizeWidth_value_loc = (By.CSS_SELECTOR,"label[for='OpeningWidth']")
    opener_value_loc = (By.CSS_SELECTOR,"label[for='Opener']")

    '''Each element in Condition of Contract section'''
    condition_contract_loc = (By.CSS_SELECTOR,"label[for='Contract']")
    condition_contract_box_loc = (By.ID,'ConditionsOfContract')

    '''Each element in Cost section'''
    sale_amount_loc = (By.CSS_SELECTOR,"label[for='SaleAmount']")
    sale_amount_box_loc = (By.ID,'SaleAmount')
    gst_loc = (By.CSS_SELECTOR,"label[for='GST']")
    gst_box_loc = (By.ID,'GST')
    total_sales_amount_loc = (By.CSS_SELECTOR,"label[for='TotalSale']")
    total_sales_amount_box_loc = (By.ID,'SaleAmountIncGST')

    '''Each element in Proposal Documents section'''
    sign_off_des_loc = (By.XPATH,'//*[@id="IsSignOffAddedText"]')
    sign_off_btn_loc = (By.CSS_SELECTOR,"label[for='SignOff']")
    add_replace_des_loc = (By.CSS_SELECTOR,"label[for='AddressReplace']")
    sheet_select_loc = (By.ID,'docTypeQuote')
    print_btn_loc = (By.ID,"btnPrint")
    add_signoff_btn_loc = (By.ID,'signOffnewfiles')
    add_attach_btn_loc = (By.ID,'quotenewfiles')

    '''Each element in Door section'''
    add_attachment_btn_loc = (By.ID,'door_new_files866336')

    def __init__(self,driver):
        self.driver = driver
        self.add_dealer_quote = Add_Dealer_Quote_With_Panel_Door(self.driver)
        self.proposal_number = None

    def go_dealer_quotation(self):
        '''Add a new dealer quote with a panel door, search this new quote, then go to the quotation page'''
        self.add_dealer_quote.add_dealer_paneldoor_fun()
        self.proposal_number = self.add_dealer_quote.get_proposal_number
        self.add_dealer_quote.search_new_quote()
        self.driver.find_element(*self.setting_btn_loc).click()
        self.driver.find_element(*self.quotation_loc).click()
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(self.job_summary_section_loc))

    def check_major_sections(self):
        '''Check the major sections on Quotation screen'''
        quotation_section = self.driver.find_element(*self.quotation_section_loc).text
        job_summary_section = self.driver.find_element(*self.job_summary_section_loc).text
        total_cost = self.driver.find_element(*self.total_cost_loc).text
        proposal_doc_section = self.driver.find_element(*self.proposal_doc_section_loc).text
        door1_section = self.driver.find_element(*self.door1_section_loc).text
        back_btn_des = self.driver.find_element(*self.back_btn_loc).text
        save_btn_des = self.driver.find_element(*self.save_btn_loc).text
        send_email_btn_des = self.driver.find_element(*self.send_email_btn_loc).text
        submit_quote_btn_des = self.driver.find_element(*self.submit_quote_btn_loc).text
        print(quotation_section,job_summary_section,total_cost,proposal_doc_section,
              door1_section,back_btn_des,save_btn_des,send_email_btn_des,submit_quote_btn_des)
        return (quotation_section,job_summary_section,total_cost,proposal_doc_section,
                door1_section,back_btn_des,save_btn_des,send_email_btn_des,submit_quote_btn_des)

    def check_quotation_section(self):
        '''Check each element in quotation section'''
        client_name_des = self.driver.find_element(*self.client_name_loc).text
        contact_mobile_des = self.driver.find_element(*self.mobile_loc).text
        proposal_num_des = self.driver.find_element(*self.proposal_num_loc).text
        contact_full_adds_des = self.driver.find_element(*self.contact_full_adds_loc).text
        salesperson_des = self.driver.find_element(*self.salesperson_loc).text
        print(client_name_des,contact_mobile_des,proposal_num_des,contact_full_adds_des,salesperson_des)
        return (client_name_des,contact_mobile_des,proposal_num_des,contact_full_adds_des,salesperson_des)

    def check_contact_details(self):
        '''Check the values for each contact detail'''
        client_name = self.driver.find_element(*self.client_name_box_loc).get_attribute('value')
        contact_mobile = self.driver.find_element(*self.mobile_box_loc).get_attribute('value')
        proposal_num = self.driver.find_element(*self.proposal_num_box_loc).get_attribute('value')
        contact_full_adds = self.driver.find_element(*self.contact_full_adds_box_loc).get_attribute('value')
        salesperson = self.driver.find_element(*self.salesperson_box_loc).get_attribute('value')
        print(client_name,contact_mobile,proposal_num,contact_full_adds,salesperson)
        return client_name,contact_mobile,proposal_num,contact_full_adds,salesperson

    def check_job_summary_section(self):
        '''Check each element in job summary section'''
        door_summary_des = self.driver.find_element(*self.door1_summary_loc).text
        # print(door_summary_des)
        return door_summary_des

    def check_door_setting_btn(self):
        '''Check the door settings button'''
        door_setting_btn = self.driver.find_element(*self.door1_setting_btn_loc)
        if door_setting_btn.is_displayed:
            return True
        else:
            return False

    def check_door1_details(self):
        '''Check the door1's details in Door Summary section'''
        door_type_detail = self.driver.find_element(*self.door_type_value_loc).text
        door_design_detail = self.driver.find_element(*self.door_design_value_loc).text
        door_finish_detail = self.driver.find_element(*self.door_finish_value_loc).text
        category_colour_detail = self.driver.find_element(*self.category_value_loc).text
        opener = self.driver.find_element(*self.opener_value_loc).text
        print(door_type_detail,door_design_detail,door_finish_detail,category_colour_detail,install_type_detail)
        return  door_type_detail,door_design_detail,door_finish_detail,category_colour_detail,opener

    def check_door1_size(self):
        '''Check the door1's sizes in Door Summary section'''
        actual_height = self.driver.find_element(*self.actual_height_value_loc).text
        actual_width = self.driver.find_element(*self.actual_width_value_loc).text
        opening_size_lh = self.driver.find_element(*self.opening_sizeLH_value_loc).text
        opening_size_rh = self.driver.find_element(*self.opening_sizeRH_value_loc).text
        opening_size_width = self.driver.find_element(*self.opening_sizeWidth_value_loc).text
        print(actual_height,actual_width,opening_size_lh,opening_size_rh,opening_size_width,sr_left,hr,sr_right)
        return actual_height,actual_width,opening_size_lh,opening_size_rh,opening_size_width

    def check_condition_section(self):
        '''Check each element in Condition of Contract section'''
        condition_contract_des = self.driver.find_element(*self.condition_contract_loc).text
        print(condition_contract_des)
        return condition_contract_des

    def check_cost_section(self):
        '''Check each element in Cost section'''
        total_cost_des = self.driver.find_element(*self.total_cost_loc).text
        gst_des = self.driver.find_element(*self.gst_loc).text
        sale_amount_des = self.driver.find_element(*self.sale_amount_loc).text
        total_sale_amount_des = self.driver.find_element(*self.total_sales_amount_loc).text
        print(total_cost_des,gst_des,sale_amount_des,total_sale_amount_des)
        return total_cost_des,gst_des,sale_amount_des,total_sale_amount_des

    def check_cost_amount(self):
        '''Check each Amount in Cost section'''
        gst = self.driver.find_element(*self.gst_box_loc).get_attribute('value')
        sale_amount = self.driver.find_element(*self.sale_amount_box_loc).get_attribute('value')
        total_sale_amount = self.driver.find_element(*self.total_sales_amount_box_loc).get_attribute('value')
        print(gst,sale_amount,total_sale_amount)
        return gst,sale_amount,total_sale_amount

    def check_proposal_documents_section(self):
        '''Check each element in Proposal Documents section'''
        add_replace_des = self.driver.find_element(*self.add_replace_des_loc).text
        print_btn = self.driver.find_element(*self.print_btn_loc).text
        print(add_replace_des,print_btn)
        return add_replace_des,print_btn

    def check_print_sheet(self):
        '''Check the Print Sheet in Proposal Documents section'''
        print_sheet_select = self.driver.find_element(*self.sheet_select_loc).text
        print(print_sheet_select)
        return print_sheet_select


if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("http:// ")
    driver.implicitly_wait(10)

    login = Admin_Portal(driver)
    login.typeUserName('aa@ecogaragedoors.com')
    login.typePassword('aabb')
    login.clickLogin()
    login1 = Dealer_Quotation_Panel(driver)
    login1.go_dealer_quotation()
    # login1.check_major_sections()
    # login1.check_quotation_section()
    # login1.check_contact_details()
    # login1.check_job_summary_section()
    # login1.check_cost_section()
    login1.check_cost_amount()
    # login1.check_door_setting_btn()
    # login1.check_door1_details()
    # login1.check_door1_size()
    # login1.check_condition_section()
    # login1.check_cash_net()
    # login1.check_proposal_documents_section()
    # login1.check_print_sheet()
    # login1.check_signoff_btn()
    # login1.check_door_section()
