# Author:Yi Sun(Tim) 2024-9-04

'''Add a Quote with a standard door function'''

import selenium
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from pages.login_admin import Admin_Portal
# from pages.add_quote import Add_Quote
# from pages.add_standar_door import Add_Standard_Door
# from pages.standard_door import *
from pages.add_quote_with_door import Add_Quote_With_Door
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.action_chains import ActionChains

class Quotation_Panel():
    """
        Note: For security and confidentiality, specific XPath/CSS selectors
        have been replaced with 'test_sample', and additional private locators
        have been omitted from this public sample.
    """

    '''the quotation option in the drop down list'''
    setting_btn_loc = (By.ID,'test_sample')
    quotation_loc = (By.CSS_SELECTOR,"label[for='test_sample']")

    # [Remaining 40+ locators redacted for confidentiality]
    '''Major sections on Quotation screen'''
    '''Each element in Quotation section'''
    '''Each element in Job Summary section'''
    '''Each element in Condition of Contract section'''
    '''Each element in Payment section'''
    '''Each element in Proposal Documents section'''
    '''Each element in Door section'''

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
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(self.job_summary_section_loc))

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
        return (quotation_section,job_summary_section,condition_section,payment_section,proposal_doc_section,
                door1_section,back_btn_des,save_btn_des)

    def check_door_setting_btn(self):
        '''Check the door settings button'''
        door_setting_btn = self.driver.find_element(*self.door1_setting_btn_loc)
        if door_setting_btn.is_displayed:
            return True
        else:
            return False

    def check_payment_deposit(self):
        '''Check the payment deposit percentage in Payment section,should be "0"'''
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight / 2);") #
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.payment_terms_loc))
        sleep(5)
        payment_deposit = self.driver.find_element(*self.account_deposit_box_loc).get_attribute('value')
        print("payment deposit is",payment_deposit)
        if payment_deposit == "0.00":
            return True
        else:
            return False

    def check_payment_net(self):
        '''Check the payment Net percentage in Payment section,should be "100%"'''
        # sleep(2)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.payment_terms_loc))
        sleep(5)
        payment_net = self.driver.find_element(*self.account_net_box_loc).get_attribute('value')
        print("payment net is",payment_net)
        if payment_net == "100.00":
            return True
        else:
            return False

    def check_cash_net(self):
        '''Check the payment Net percentage in Payment section,should be "50% if it's cash sale"'''
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        back_btn  = self.driver.find_element(*self.back_btn_loc)
        link = back_btn.get_attribute('href')
        self.driver.get(link)
        self.add_quote.change_to_cash()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight / 2);")
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.payment_terms_loc))
        payment_deposit_new = self.driver.find_element(*self.account_deposit_box_loc).get_attribute('value')
        # print('payment_new: ',payment_deposit_new)
        if payment_deposit_new == "50.00":
            return True
        else:
            return False

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
    driver.get("http://test_sample ")
    driver.implicitly_wait(10)

    login = Admin_Portal(driver)
    login.typeUserName('test_sample')
    login.typePassword('test_sample')
    login.clickLogin()
    login1 = Quotation_Panel(driver)
    login1.goto_quotation_page()


