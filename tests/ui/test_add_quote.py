# Author:Yi Sun(Tim) 2023-09-04

'''Test Add Quote Page'''

import time
import unittest
from selenium import webdriver
from time import *
from pages.add_quote import *
from utils.read_config import *

class AddQuote_UI_Test(unittest.TestCase,Add_Quote):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.config_read = ReadConfig()
        cls.url = cls.config_read.get_url()
        cls.admin_username = cls.config_read.admin_username()
        cls.admin_password = cls.config_read.admin_password()
        cls.login = Admin_Portal(cls.driver)
        cls.driver.get(cls.url)
        cls.login.login(cls.admin_username,cls.admin_password)
        cls.driver.implicitly_wait(5)
        cls.goaddquote = Add_Quote(cls.driver)
        cls.goaddquote.go_addquote()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_addquote_ui_001(self):
        '''Verify the url for Add Quotes page'''
        self.driver.implicitly_wait(2)
        self.assertEqual('http://aabb/Quote/Create',self.check_addquote_url)

    def test_addquote_ui_002(self):
        '''Verify the default section in Add Quotes page'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Proposal Details','Contact Details','Site Details','Doors'),self.check_defaulsection)

    def test_addquote_ui_003(self):
        '''Verify the Save Quote button in Add Quotes page'''
        self.driver.implicitly_wait(2)
        self.assertEqual(True,self.check_savequote_btn)


    def test_addquote_ui_004(self):
        '''Verify each description of Proplsal Details in Add Quotes page'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Proposal Number','Pricing Category','User','Account Type','Order Date',
                          'Quote Status','Account Customer','Supply Type'),self.check_proposal_details)

    def test_addquote_ui_005(self):
        '''Verify each value in "Pricing Category" list'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Category 1\nCategory 2\nCategory 3\nCategory 4\nCompany 1\nWholesale'),
                         self.check_pricing_cate_value)

    def test_addquote_ui_006(self):
        '''Verify the default value in "Pricing Category" list'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Category 4'),self.check_default_pricing)

    def test_addquote_ui_007(self):
        '''Verify the default value in "User" list, it should be current login user'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Yi Sun'),self.check_default_user)

    def test_addquote_ui_008(self):
        '''Verify each value in "Account Type" list'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Cash sale\nAccount'),self.check_accounttype_value)

    def test_addquote_ui_009(self):
        '''Verify the default value in "Account Type" list, it should be "Cash sale"'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Cash sale'),self.check_default_accounttype)

    def test_addquote_ui_010(self):
        '''Verify each value in "Quote Status" list, it should be 'Cash sale','Quote','Active',"Close"'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Lead\nQuote\nActive\nClose'),self.check_quotestatus_value)

    def test_addquote_ui_011(self):
        '''Verify the default value in "Quote Status" list, it should be "Quote"'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Cash sale'),self.check_default_accounttype)

    def test_addquote_ui_012(self):
        '''Verify each value in "Supply Type" list'''
        self.driver.implicitly_wait(2)
        self.assertIn(('VIC – Install\nVIC – Pick Up\nVIC – Deliver\nNSW – Install\nNSW – Pick Up\nNSW – Deliver\n'
                       'ACT – Deliver\nTAS – Deliver\nSA – Deliver\nQLD – Deliver\nQLD – Pick Up\n'
                       'QLD – Install\nWA – Install\nWA – Deliver\nWA – Pick Up'),self.check_supplytype_value)

    def test_addquote_ui_013(self):
        '''Verify the default value in "Supply Type" list, it should be "Please Select"'''
        self.driver.implicitly_wait(2)
        self.assertEqual('Please Select',self.check_supplytype_default)

    def test_addquote_ui_014(self):
        '''Verify The "Account Customer" list should enable after select "Account" in "Account Type" list'''
        self.driver.implicitly_wait(2)
        self.assertEqual(False,self.check_changeto_Account)

    def test_addquote_ui_015(self):
        '''Verify each section in "Contact Details"'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Client Contact Details','Site Contact Details'),self.check_contact_details)

    def test_addquote_ui_016(self):
        '''Verify each element in "Client Contact Details"'''
        self.driver.implicitly_wait(2)
        self.assertEqual( ('Client Name', 'Customer Purchase Order','Contact Name','Contact Mobile',
                           'Contact Email','Contact Address','Contact Suburb','Contact Postcode'),
                          self.check_client_contact_details)

    def test_addquote_ui_017(self):
        '''Verify  the input editbox for "Client Name"'''
        self.driver.implicitly_wait(2)
        self.assertEqual(True,self.check_client_name_box)

    def test_addquote_ui_018(self):
        '''Verify  the input editbox for "Customer Purchase Order"'''
        self.driver.implicitly_wait(2)
        self.assertEqual(True,self.check_order_num_box)

    def test_addquote_ui_019(self):
            '''Verify  the input editbox for "Contact Name"'''
            self.driver.implicitly_wait(2)
            self.assertEqual( True,self.check_contact_name_box)

    def test_addquote_ui_020(self):
            '''Verify  the input editbox for "Contact Mobile"'''
            self.driver.implicitly_wait(2)
            self.assertEqual( True,self.check_contact_mobile_box)

    def test_addquote_ui_021(self):
            '''Verify  the input editbox for "Contact Email"'''
            self.driver.implicitly_wait(2)
            self.assertEqual( True,self.check_contact_email_box)

    def test_addquote_ui_022(self):
        '''Verify  the input editbox for "Contact Address"'''
        self.driver.implicitly_wait(2)
        self.assertEqual( True,self.check_contact_address_box)

    def test_addquote_ui_023(self):
            '''Verify  the input editbox for "Contact Suburb"'''
            self.driver.implicitly_wait(2)
            self.assertEqual( True,self.check_contact_suburb_box)

    def test_addquote_ui_024(self):
            '''Verify  the input editbox for "Contact Postcode"'''
            self.driver.implicitly_wait(2)
            self.assertEqual( True,self.check_contact_postcode_box)

    def test_addquote_ui_025(self):
        '''Verify each element in "Site Contact Details"'''
        self.driver.implicitly_wait(2)
        self.assertEqual( ('Site Contact Name', 'Site Phone','Site Email','Site/Delivery/Pickup Address',
                           'Site Suburb','Site Postcode'),self.check_site_contact_details)

    def test_addquote_ui_026(self):
            '''Verify the default status for checkbox for "Copy Client details"'''
            self.driver.implicitly_wait(2)
            self.assertEqual( False,self.check_copy_checkbox)

    def test_addquote_ui_027(self):
            '''Verify  the input editbox for "Site Contact Name"'''
            self.driver.implicitly_wait(2)
            self.assertEqual( True,self.check_site_contactname_box)

    def test_addquote_ui_028(self):
        '''Verify  the input editbox for "Site Phone"'''
        self.driver.implicitly_wait(2)
        self.assertEqual( True,self.check_site_phone_box)

    def test_addquote_ui_029(self):
            '''Verify  the input editbox for "Site Email"'''
            self.driver.implicitly_wait(2)
            self.assertEqual( True,self.check_site_email_box)

    def test_addquote_ui_030(self):
            '''Verify  the input editbox for "Site Address"'''
            self.driver.implicitly_wait(2)
            self.assertEqual( True,self.check_site_address_box)

    def test_addquote_ui_031(self):
            '''Verify  the input editbox for "Site Suburb"'''
            self.driver.implicitly_wait(2)
            self.assertEqual(True,self.check_site_suburb_box)

    def test_addquote_ui_032(self):
            '''Verify  the input editbox for "Site Postcode"'''
            self.driver.implicitly_wait(2)
            self.assertEqual(True,self.check_site_postcode_box)
    #
    def test_addquote_ui_033(self):
            '''Verify  the "Add New Door" button"'''
            self.driver.implicitly_wait(2)
            self.assertEqual( 'Add New Door',self.check_adddoor_btn)

    def test_addquote_ui_034(self):
            '''Verify the add new door menu'''
            self.driver.refresh()
            self.driver.implicitly_wait(2)
            self.assertEqual((['Standard\nCustom\nShutter']),self.check_adddoor_menu)

    def test_addquote_ui_035(self):
            '''Verify the validation in Add Quote page'''
            self.driver.implicitly_wait(2)
            self.assertEqual(('Validation Errors','1. Please select Supply Type.',
                              '2. Please enter Client Email address.'),self.check_validation)

    def test_addquote_ui_036(self):
        '''Verify Add a Quote Successfully'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('(Quote successfully created)'),self.check_add_quote_success)

if __name__ == '__main__':
    unittest.main(verbosity=2)

