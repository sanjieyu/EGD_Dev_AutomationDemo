# Author:Yi Sun(Tim) 2024-10-17

'''Add Dealer Quote Page'''

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.dealer_portal import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException

class Add_Dealer_Quote(Deal_Portal):

    quote_details_loc = (By.NAME,'details')
    doors_loc = (By.NAME,'doorid')
    save_quote_btn_loc = (By.ID,'btnSaveQuote')
    quote_success_created_loc = (By.XPATH,"//button[text()='Result']")

    '''Quote Details section'''
    proposal_num_loc = (By.XPATH,"//div[contains(@class,'proposalnum')]")
    proposal_num_box_loc = (By.ID,'ProposalNo')
    purchase_order_loc = (By.XPATH,"//div[contains(@class,'proposalorder')]")
    purchase_order_box_loc = (By.ID,'ClientPurchaseOrderNumber')
    user_loc = (By.NAME,'username')
    user_select_loc = (By.ID,'UserAssignedId')
    job_notes_loc = (By.XPATH,"//div[contains(@class,'jobnote')]")
    job_notes_box_loc = (By.ID,'JobNotes')

    '''Doors section'''
    insulated_btn_loc = (By.ID,'insulated-sectional-add-door-btn')
    panel_btn_loc = (By.ID,'panel-lift-safe-add-door-btn')
    roller_btn_loc = (By.ID,'roller-type-add-door-btn')
    default_des_loc = (By.XPATH,"//div[contains(@class,'defaultdes')]")


    def creat_quote(self):
        '''Creat a dealer quote'''
        self.driver.find_element(*self.add_dealer_quote_loc).click()
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(self.doors_loc))
        # sleep(2)

    @property
    def check_creatquote_url(self):
        '''check the url for Add Dealer Quote page'''
        create_quote_url = self.driver.current_url
        print(create_quote_url)
        return create_quote_url

    @property
    def check_defaulsection(self):
        '''check the default sections in Add Dealer Quotes page'''
        quote_details = self.driver.find_element(*self.quote_details_loc).text
        doors = self.driver.find_element(*self.doors_loc).text
        save_btn = self.driver.find_element(*self.save_quote_btn_loc).text
        print(quote_details,doors,save_btn)
        return quote_details,doors,save_btn

    @property
    def check_savequote_btn(self):
        '''check the save quote buton in Add Dealer Quotes page'''
        save_quote_btn = self.driver.find_element(*self.save_quote_btn_loc)
        if save_quote_btn:
            print('exist')
            return  True
        else:
            print("not exist")
            return False
    @property
    def check_quote_details(self):
        '''check each description of Quote Details in Add Dealer Quotes page'''
        proposal_num = self.driver.find_element(*self.proposal_num_loc).text
        purchase_order = self.driver.find_element(*self.purchase_order_loc).text
        user = self.driver.find_element(*self.user_loc).text
        job_notes = self.driver.find_element(*self.job_notes_loc).text
        print(proposal_num,purchase_order,user,job_notes)
        return proposal_num,purchase_order,user,job_notes

    @property
    def check_default_user(self):
        '''check the default value in "User" list'''
        self.driver.find_element(*self.user_select_loc).click()
        default_user_value = Select(self.driver.find_element(*self.user_select_loc)).first_selected_option.text
        print(default_user_value)
        return default_user_value

    @property
    def check_proposal_num_box(self):
        '''check the input editbox for "proposal_number"'''
        proposal_num_box = self.driver.find_element(*self.proposal_num_box_loc)
        if proposal_num_box.get_attribute('readonly'):
            print('Edit box is read-only and behaves like a disabled input.')
            return True
        else:
            print("Edit box is enabled.")
            return False

    @property
    def check_purchase_order_box(self):
        '''check the input editbox for "Customer Purchase order"'''
        purchase_order_box = self.driver.find_element(*self.purchase_order_box_loc)
        if purchase_order_box.is_enabled():
            print('true')
            return True
        else:
            print("false")
            return False

    @property
    def check_job_notes(self):
        '''check the job notes from the Job Notes box'''
        job_notes = self.driver.find_element(*self.job_notes_box_loc).text
        print(job_notes)
        return job_notes

    @property
    def check_doors_details(self):
        '''check each elements in "Doors"'''
        insulated_btn_des = self.driver.find_element(*self.insulated_btn_loc).text
        panel_btn_des = self.driver.find_element(*self.panel_btn_loc).text
        roller_btn_des = self.driver.find_element(*self.roller_btn_loc).text
        default_des = self.driver.find_element(*self.default_des_loc).text
        print(insulated_btn_des,panel_btn_des,roller_btn_des,default_des)
        return insulated_btn_des,panel_btn_des,roller_btn_des,default_des

    @property
    def check_add_dealer_quote_success(self):
        '''check Add Dealer Quote Successfully'''
        self.driver.find_element(*self.purchase_order_box_loc).send_keys('Add by Automation')
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # 滚动条拉到最下面
        self.driver.find_element(*self.save_quote_btn_loc).click()
        sleep(2)

        self.driver.execute_script("window.scrollTo(0, 0);")   # 滚动条拉到最上面
        quote_success_created = WebDriverWait(self.driver,3).until(EC.visibility_of_element_located
                                                                   (self.quote_success_created_loc)).text
        print(quote_success_created)
        return quote_success_created


if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("http:// ")
    driver.implicitly_wait(10)

    login = Add_Dealer_Quote(driver)
    login.typeUserName('aa@ecogaragedoors.com')
    login.typePassword('aabb')
    login.clickLogin()
    login.creat_quote()
    # login.check_creatquote_url
    # login.check_defaulsection
    # login.check_savequote_btn
    # login.check_quote_details
    # login.check_default_user
    # login.check_proposal_num_box
    # login.check_purchase_order_box
    # login.check_job_notes
    login.check_doors_details










