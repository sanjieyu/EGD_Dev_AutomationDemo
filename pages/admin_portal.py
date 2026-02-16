# Author:Yi Sun(Tim) 2023-08-29

'''Admin Page'''

from selenium.webdriver.common.by import By
from selenium import webdriver
from pages.login_admin import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Admin_Page(Admin_Portal):
    """
        Note: For security and confidentiality, specific XPath/CSS selectors
        have been replaced with 'test_sample', and additional private locators
        have been omitted from this public sample.
    """
    '''loc for default values in this page'''
    eco_icon_loc = (By.ID,'test_sample')
    add_loc = (By.CSS_SELECTOR, 'test_sample')
    list_loc = (By.NAME,'test_sample')

    # [Remaining 30+ locators redacted for confidentiality]
    '''Add Menu'''
    '''List Menu'''
    '''Account Menu'''

    @property
    def getURL(self):
        '''get the url of Admin login portal'''
        # sleep(2)
        WebDriverWait(self.driver,15).until(EC.visibility_of_element_located(self.copyright_loc))
        print('url is:',self.driver.current_url)
        return self.driver.current_url
    @property
    def check_defaultmenu(self):
        '''check the default values in Admin Login page'''
        add_menu = self.driver.find_element(*self.add_loc).text
        list_menu = self.driver.find_element(*self.list_loc).text
        account_menu = self.driver.find_element(*self.account_loc).text
        print(add_menu,list_menu,account_menu)
        return add_menu,list_menu,account_menu

    @property
    def check_findquote(self):
        '''check the Find Quote in Admin Login page'''
        find_quote = self.driver.find_element(*self.findquote_box_loc)
        if find_quote.is_displayed():
            return True
        else:
            return False

    @property
    def check_findaddress(self):
        '''check the Find Address in Admin Login page'''
        find_address = self.driver.find_element(*self.findaddress_box_loc)
        if find_address.is_displayed():
            return  True
        else:
            return False

    @property
    def check_findclient(self):
            '''check the Find Client in Admin Login page'''
            find_client = self.driver.find_element(*self.findclient_box_loc)
            if find_client.is_displayed():
                return True
            else:
                return False

    @property
    def add_menu(self):
        '''check the Add Menu'''
        self.driver.find_element(*self.add_loc).click()
        quote_add = self.driver.find_element(*self.quote_add_loc).text
        lead_add = self.driver.find_element(*self.lead_add_loc).text
        account_add = self.driver.find_element(*self.account_add_loc).text
        installer_add = self.driver.find_element(*self.installer_add_loc).text
        print(quote_add,lead_add,account_add,installer_add)
        return quote_add,lead_add,account_add,installer_add

    @property
    def go_panel_rollforming(self):
        '''Go to panel lift rollforming screen'''
        self.driver.find_element(*self.list_loc).click()

    @property
    def list_menu(self):
        '''check the List Menu'''
        self.driver.find_element(*self.list_loc).click()
        quote_list = self.driver.find_element(*self.quote_list_loc).text
        services_list = self.driver.find_element(*self.services_list_loc).text
        account_list = self.driver.find_element(*self.account_list_loc).text
        report_list = self.driver.find_element(*self.report_list_loc).text
        installer_list = self.driver.find_element(*self.installer_list_loc).text
        myob_list = self.driver.find_element(*self.myob_list_loc).text
        jobaccept_list = self.driver.find_element(*self.jobaccept_list_loc).text
        onhold_list = self.driver.find_element(*self.onhold_list_loc).text
        neworder_list = self.driver.find_element(*self.neworder_list_loc).text
        production_list = self.driver.find_element(*self.production_list_loc).text
        productionWA_list = self.driver.find_element(*self.productionWA_list_loc).text
        schedule_list = self.driver.find_element(*self.schedule_list_loc).text
        pipeline_list = self.driver.find_element(*self.pipeline_list_loc).text
        activepipeline_list = self.driver.find_element(*self.activepipeline_list_loc).text
        return (quote_list,services_list,account_list,report_list,installer_list,myob_list,jobaccept_list,
                onhold_list,neworder_list,production_list,productionWA_list,schedule_list,pipeline_list,activepipeline_list)

    @property
    def account_menu(self):
        '''check the Account Menu'''
        self.driver.find_element(*self.account_loc).click()
        changepwd = self.driver.find_element(*self.changepwd_loc).text
        updateprofile = self.driver.find_element(*self.updateprofile_loc).text
        updateemail = self.driver.find_element(*self.updateemail_loc).text
        usermanage = self.driver.find_element(*self.usermanage_loc).text
        travel_area = self.driver.find_element(*self.travel_area_loc).text
        rollcycle = self.driver.find_element(*self.rollcycle_loc).text
        sms = self.driver.find_element(*self.sms_loc).text
        logoff = self.driver.find_element(*self.logoff_loc).text
        return changepwd,updateprofile,updateemail,usermanage,travel_area,rollcycle,sms,logoff

    @property
    def check_copyright(self):
        '''check the Copyright and Terms'''
        copyright2023 = self.driver.find_element(*self.copyright_loc).text
        terms = self.driver.find_element(*self.terms_loc).text
        return copyright2023,terms


if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("http://test_sample ")
    driver.implicitly_wait(10)

    login = Admin_Page(driver)
    login.typeUserName('test_sample')
    login.typePassword('test_sample')
    login.clickLogin()
    # login.getURL
    login.check_defaultmenu







