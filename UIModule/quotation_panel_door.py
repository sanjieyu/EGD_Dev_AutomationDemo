# Author:Yi Sun(Tim) 2024-9-04

'''Add a Quote with a standard door function'''

import selenium
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from UIModule.login_admin import Admin_Portal
# from UIModule.add_quote import Add_Quote
# from UIModule.add_standar_door import Add_Standard_Door
# from UIModule.standard_door import *
from UIModule.add_quote_with_door import Add_Quote_With_Door
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.action_chains import ActionChains

class Quotation_Panel():

    '''the quotation option in the drop down list'''
    setting_btn_loc = (
    By.XPATH, '/html/body/div[3]/div[2]/div/div/div/div/div/div/div/div/table/tbody/tr/td[12]/div/button/i')
    quotation_loc = (By.XPATH,'/html/body/div[3]/div[2]/div/div/div/div/div/div/div/div/table/tbody/tr/td[12]/div/ul/'
                              'li[1]/a')

    '''Major sections on Quotation screen'''
    quotation_section_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/form/h1[1]')
    job_summary_section_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/form/h1[2]')
    condition_section_loc  = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/form/h1[3]')
    payment_section_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/form/h1[4]')
    proposal_doc_section_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/form/h1[5]')
    door1_section_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/form/div[6]/div[2]/h3')
    back_btn_loc = (By.XPATH,'//*[@id="backlink"]')
    save_btn_loc = (By.ID,'btnSaveFinal')

    '''Each element in Quotation section'''
    client_name_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/form/div[1]/fieldset/div[1]/div[1]/label')
    mobile_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/form/div[1]/fieldset/div[1]/div[2]/label')
    proposal_num_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/form/div[1]/fieldset/div[1]/div[3]/label')
    contact_full_adds_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/form/div[1]/fieldset/div[2]/div[1]/div[1]/label')
    salesperson_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/form/div[1]/fieldset/div[2]/div[1]/div[2]/label')
    contact_name_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/form/div[1]/fieldset/div[2]/div[1]/div[3]/div[1]/label')
    site_phone_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/form/div[1]/fieldset/div[2]/div[1]/div[3]/div[2]/label')
    site_full_adds_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/form/div[1]/fieldset/div[2]/div[1]/div[4]/label')
    quote_status_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/form/div[1]/div')

    client_name_box_loc = (By.ID,'ClientName')
    mobile_box_loc = (By.ID, 'ContactMobile')
    proposal_num_box_loc = (By.ID, 'ProposalNo')
    contact_full_adds_box_loc = (By.ID, 'ContactFullAddress')
    salesperson_box_loc = (By.ID, 'SalesPerson')
    contact_name_box_loc = (By.ID, 'ContactName')
    site_phone_box_loc = (By.ID, 'SitePhone')
    site_full_adds_box_loc = (By.ID, 'SiteFullAddress')

    '''Each element in Job Summary section'''
    door1_summary_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/form/div[3]/fieldset/div/div/div[1]/div[1]/h3/span')
    door1_setting_btn_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/form/div[3]/fieldset/div/div/div[1]/div[1]/h3/'
                                      'span/a')

    door_type_value_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/form/div[3]/fieldset/div/div/div[2]/div[1]/table/'
                                    'tbody/tr[1]/td[2]')
    actual_height_value_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/form/div[3]/fieldset/div/div/div[2]/div[2]/'
                                        'table/tbody/tr[1]/td[2]')
    door_design_value_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/form/div[3]/fieldset/div/div/div[2]/div[1]/'
                                      'table/tbody/tr[2]/td[2]/span[1]')
    actual_width_value_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/form/div[3]/fieldset/div/div/div[2]/div[2]/'
                                       'table/tbody/tr[2]/td[2]')
    door_finish_value_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/form/div[3]/fieldset/div/div/div[2]/div[1]/'
                                      'table/tbody/tr[3]/td[2]')
    category_value_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/form/div[3]/fieldset/div/div/div[2]/div[1]/table/'
                                   'tbody/tr[4]/td[2]')
    install_type_value_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/form/div[3]/fieldset/div/div/div[2]/div[1]/'
                                       'table/tbody/tr[5]/td[2]')

    opening_sizeLH_value_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/form/div[3]/fieldset/div/div/div[3]/div[1]')
    opening_sizeRH_value_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/form/div[3]/fieldset/div/div/div[3]/div[2]')
    opening_sizeWidth_value_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/form/div[3]/fieldset/div/div/div[3]/div[3]')
    sr_left_value_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/form/div[3]/fieldset/div/div/div[4]/div[1]')
    hr_value_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/form/div[3]/fieldset/div/div/div[4]/div[2]')
    sr_right_value_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/form/div[3]/fieldset/div/div/div[4]/div[3]')
    opener_value_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/form/div[3]/fieldset/div/div/div[5]/div')

    '''Each element in Condition of Contract section'''
    condition_contract_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/form/div[4]/fieldset/div[1]/div/label')
    condition_contract_box_loc = (By.ID,'ConditionsOfContract')
    date_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/form/div[4]/fieldset/fieldset/div/div[1]/div/div[1]/label')
    date_box_loc = (By.ID,'SignatureDate')
    signature_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/form/div[4]/fieldset/fieldset/div/div[2]/div/div[1]/'
                              'span')
    lock_btn_loc = (By.ID,'btnLockCanvas')
    clear_btn_loc = (By.ID,'btnClearCanvas')
    accept_des_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/form/div[4]/fieldset/fieldset/div/div[1]/div/div[2]/'
                               'div/label')

    '''Each element in Payment section'''
    payment_type_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/form/div[5]/fieldset/div[1]/div/b')
    account_type_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/form/div[5]/fieldset/div[2]/div[1]/label')
    special_type_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/form/div[5]/fieldset/div[2]/fieldset/label')
    eft_type_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/form/div[5]/fieldset/div[2]/div[2]/label')
    credit_card_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/form/div[5]/fieldset/div[2]/div[3]/label')
    cash_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/form/div[5]/fieldset/div[2]/div[4]/label')
    cheque_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/form/div[5]/fieldset/div[2]/div[5]/label')
    account_radiobox_loc = (By.ID,'AccountRadio')
    special_box_loc = (By.ID,'SpecialRadio')
    total_cost_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/form/div[5]/fieldset/div[3]/div[1]/div[1]/div/h3/span')
    total_cost_icon_loc = (By.CSS_SELECTOR, 'div.form-horizontal:nth-child(1) > div:nth-child(1) > div:nth-child(1) > '
                                            'h3:nth-child(1) > span:nth-child(1) > a:nth-child(1)')

    banking_details_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/form/div[5]/fieldset/div[3]/div[2]/div[1]/h3/span')
    payment_terms_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/form/div[5]/fieldset/div[4]/div/h3/span')
    account_deposit_box_loc = (By.ID,'term1percent')
    account_net_box_loc = (By.ID,'term2percent')
    total_discount_amount_loc = (By.ID,'total-discount-amount')

    '''Each element in Proposal Documents section'''
    sign_off_des_loc = (By.XPATH,'//*[@id="IsSignOffAddedText"]')
    sign_off_btn_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/form/div[6]/div[1]/div[1]/h3/span/label[1]')
    add_replace_des_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/form/div[6]/div[1]/div[2]/fieldset[1]/div/label')
    sheet_select_loc = (By.ID,'docTypeQuote')
    print_btn_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/form/div[6]/div[1]/div[2]/fieldset[2]/button')
    add_signoff_btn_loc = (By.ID,'signOffnewfiles')
    add_attach_btn_loc = (By.ID,'quotenewfiles')

    '''Each element in Door section'''
    measure_doc_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/form/div[6]/div[2]/div[1]/h3/span/label')
    site_picture_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/form/div[6]/div[2]/div[2]/h3/span/label')
    add_replace_door_loc = (By.XPATH,'/html/body/div[3]/div[2]/div[1]/form/div[6]/div[2]/div[3]/fieldset[1]/div/label')
    print_sheet_door_loc = (By.XPATH,'//*[@id="docTypeDoor634775"]')


    def __init__(self, driver):
        self.driver = driver
        self.add_quote = Add_Quote_With_Door(self.driver)
        self.proposal_number = None

    def goto_quotation_page(self):
        '''Add a new quote with door, then search this new quote, then go to the quotation page'''
        self.add_quote.add_door_fun()
        self.proposal_number = self.add_quote.get_proposal_number
        self.add_quote.search_new_quote()
        self.driver.find_element(*self.setting_btn_loc).click()
        self.driver.find_element(*self.quotation_loc).click()
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(self.job_summary_section_loc))   # new added
        # sleep(3)

    def check_major_sections(self):
        '''Check the major sections on Quotation screen'''
        quotation_section = self.driver.find_element(*self.quotation_section_loc).text
        job_summary_section = self.driver.find_element(*self.job_summary_section_loc).text
        condition_section = self.driver.find_element(*self.condition_section_loc).text
        payment_section = self.driver.find_element(*self.payment_section_loc).text
        proposal_doc_section = self.driver.find_element(*self.proposal_doc_section_loc).text
        door1_section = self.driver.find_element(*self.door1_section_loc).text
        back_btn_des = self.driver.find_element(*self.back_btn_loc).text
        save_btn_des = self.driver.find_element(*self.save_btn_loc).text
        print(quotation_section,job_summary_section,condition_section,payment_section,proposal_doc_section,
              door1_section,back_btn_des,save_btn_des)
        return (quotation_section,job_summary_section,condition_section,payment_section,proposal_doc_section,
                door1_section,back_btn_des,save_btn_des)

    def check_quotation_section(self):
        '''Check each element in quotation section'''
        client_name_des = self.driver.find_element(*self.client_name_loc).text
        contact_mobile_des = self.driver.find_element(*self.mobile_loc).text
        proposal_num_des = self.driver.find_element(*self.proposal_num_loc).text
        contact_full_adds_des = self.driver.find_element(*self.contact_full_adds_loc).text
        salesperson_des = self.driver.find_element(*self.salesperson_loc).text
        contact_name_des = self.driver.find_element(*self.contact_name_loc).text
        site_phone_des = self.driver.find_element(*self.site_phone_loc).text
        site_full_adds_des = self.driver.find_element(*self.site_full_adds_loc).text
        quote_status_des = self.driver.find_element(*self.quote_status_loc).text
        # print(client_name,contact_mobile,proposal_num,contact_full_adds,salesperson,contact_name,site_phone,
        #       site_full_adds,quote_status)
        return (client_name_des,contact_mobile_des,proposal_num_des,contact_full_adds_des,salesperson_des,
                contact_name_des,site_phone_des,site_full_adds_des,quote_status_des)

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
        install_type_detail = self.driver.find_element(*self.install_type_value_loc).text
        opener = self.driver.find_element(*self.opener_value_loc).text
        print(door_type_detail,door_design_detail,door_finish_detail,category_colour_detail,install_type_detail)
        return  door_type_detail,door_design_detail,door_finish_detail,category_colour_detail,install_type_detail,opener

    def check_door1_size(self):
        '''Check the door1's sizes in Door Summary section'''
        actual_height = self.driver.find_element(*self.actual_height_value_loc).text
        actual_width = self.driver.find_element(*self.actual_width_value_loc).text
        opening_size_lh = self.driver.find_element(*self.opening_sizeLH_value_loc).text
        opening_size_rh = self.driver.find_element(*self.opening_sizeRH_value_loc).text
        opening_size_width = self.driver.find_element(*self.opening_sizeWidth_value_loc).text
        sr_left = self.driver.find_element(*self.sr_left_value_loc).text
        hr = self.driver.find_element(*self.hr_value_loc).text
        sr_right = self.driver.find_element(*self.sr_right_value_loc).text
        print(actual_height,actual_width,opening_size_lh,opening_size_rh,opening_size_width,sr_left,hr,sr_right)
        return actual_height,actual_width,opening_size_lh,opening_size_rh,opening_size_width,sr_left,hr,sr_right

    def check_condition_section(self):
        '''Check each element in Condition of Contract section'''
        condition_contract_des = self.driver.find_element(*self.condition_contract_loc).text
        date_des = self.driver.find_element(*self.date_loc).text
        signature_des = self.driver.find_element(*self.signature_loc).text
        accept_des = self.driver.find_element(*self.accept_des_loc).text
        lock_btn_des = self.driver.find_element(*self.lock_btn_loc).text
        clear_btn_des = self.driver.find_element(*self.clear_btn_loc).text
        # print(condition_contract_des,date_des,signature_des,accept_des,lock_btn_des,clear_btn_des)
        return condition_contract_des,date_des,signature_des,accept_des,lock_btn_des,clear_btn_des

    def check_payments_section(self):
        '''Check each element in Payment section'''
        payment_type = self.driver.find_element(*self.payment_type_loc).text
        total_cost = self.driver.find_element(*self.total_cost_loc).text
        banking_details = self.driver.find_element(*self.banking_details_loc).text
        payment_terms = self.driver.find_element(*self.payment_terms_loc).text
        print(payment_type,total_cost,banking_details,payment_terms)
        return payment_type,total_cost,banking_details,payment_terms

    def check_payment_type(self):
        '''Check the payment type in Payment section,should be "Account"'''
        account_radiobox = self.driver.find_element(*self.account_radiobox_loc)
        if account_radiobox.is_selected():
            return True
        else:
            return False

    def check_payment_deposit(self):
        '''Check the payment deposit percentage in Payment section,should be "0"'''
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight / 2);") #
        # sleep(2)
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.payment_terms_loc))    # new added
        sleep(5)
        payment_deposit = self.driver.find_element(*self.account_deposit_box_loc).get_attribute('value')
        print("payment deposit is",payment_deposit)
        if payment_deposit == "0.00":
            print('correct')
            return True
        else:
            print('wrong')
            return False

    def check_payment_net(self):
        '''Check the payment Net percentage in Payment section,should be "100%"'''
        # sleep(2)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.payment_terms_loc))  # new added
        sleep(5)
        payment_net = self.driver.find_element(*self.account_net_box_loc).get_attribute('value')
        print("payment net is",payment_net)
        if payment_net == "100.00":
            print('correct')
            return True
        else:
            print('wrong')
            return False

    def check_cash_net(self):
        '''Check the payment Net percentage in Payment section,should be "50% if it's cash sale"'''
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(2)
        back_btn  = self.driver.find_element(*self.back_btn_loc)
        # self.driver.execute_script("arguments[0].click90",back_btn)
        # actions = ActionChains(self.driver)
        # actions.move_to_element(back_btn).click().perform()
        link = back_btn.get_attribute('href')
        self.driver.get(link)
        self.add_quote.change_to_cash()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight / 2);")
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.payment_terms_loc))  # new added
        payment_deposit_new = self.driver.find_element(*self.account_deposit_box_loc).get_attribute('value')
        # print('payment_new: ',payment_deposit_new)
        if payment_deposit_new == "50.00":
            print('50.00')
            return True
        else:
            print('wrong')
            return False

    def check_proposal_documents_section(self):
        '''Check each element in Proposal Documents section'''
        sign_off_des = self.driver.find_element(*self.sign_off_des_loc).text
        add_replace_des = self.driver.find_element(*self.add_replace_des_loc).text
        print_btn = self.driver.find_element(*self.print_btn_loc).text
        # print(sign_off_des,add_replace_des,print_btn)
        return sign_off_des,add_replace_des,print_btn

    def check_print_sheet(self):
        '''Check the Print Sheet in Proposal Documents section'''
        print_sheet_select = self.driver.find_element(*self.sheet_select_loc).text
        # print(print_sheet_select)
        return print_sheet_select

    def check_door_section(self):
        '''Check each element in Door section'''
        measure_doc_des = self.driver.find_element(*self.measure_doc_loc).text
        site_picture_des = self.driver.find_element(*self.site_picture_loc).text
        add_replace_door_des = self.driver.find_element(*self.add_replace_door_loc).text
        print(measure_doc_des,site_picture_des,add_replace_door_des)
        return measure_doc_des,site_picture_des,add_replace_door_des

    def goto_quotation_discount(self):
        '''this is for Discount Check module'''
        self.proposal_number = self.add_quote.get_proposal_number
        self.add_quote.search_new_quote()
        self.driver.find_element(*self.setting_btn_loc).click()
        self.driver.find_element(*self.quotation_loc).click()

    def check_discount(self):
        '''Check the price discount'''
        self.driver.find_element(*self.total_cost_icon_loc).click()
        total_discount_amount = self.driver.find_element(*self.total_discount_amount_loc).text
        print('discount is:',total_discount_amount)
        return total_discount_amount


if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("http:// ")
    driver.implicitly_wait(10)

    login = Admin_Portal(driver)
    login.typeUserName('aa@ecogaragedoors.com')
    login.typePassword('aabb')
    login.clickLogin()
    login1 = Quotation_Panel(driver)
    login1.goto_quotation_page()
    # login1.check_major_sections()
    # login1.check_quotation_section()
    # login1.check_contact_details()
    # login1.check_job_summary_section()
    # login1.check_door_setting_btn()
    # login1.check_door1_details()
    # login1.check_door1_size()
    # login1.check_condition_section()
    # login1.check_payments_section()
    # login1.check_payment_type()
    login1.check_payment_deposit()
    # login1.check_payment_net()
    login1.check_cash_net()
    # login1.check_proposal_documents_section()
    # login1.check_print_sheet()
    # login1.check_signoff_btn()
    # login1.check_door_section()

