# Author:Yi Sun(Tim) 2024-10-17

'''Test Create Dealer Quote Page'''

import time
import unittest
from selenium import webdriver
from time import *
from pages.add_dealer_quote import *
from utils.read_config import *

class AddDealerQuote_UI_Test(unittest.TestCase,Add_Dealer_Quote):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.config_read = ReadConfig()
        cls.url = cls.config_read.get_url()
        cls.dealer_username = cls.config_read.dealer_username()
        cls.dealer_password = cls.config_read.dealer_password()
        cls.login = Admin_Portal(cls.driver)
        cls.driver.get(cls.url)
        cls.login.login(cls.dealer_username,cls.dealer_password)
        cls.driver.implicitly_wait(5)
        cls.dealerquote = Add_Dealer_Quote(cls.driver)
        cls.dealerquote.creat_quote()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_dealer_quote_ui_001(self):
        '''Verify the url for Create Dealer Quotes page'''
        self.driver.implicitly_wait(2)
        self.assertEqual('http://aabb/Dealer/Create',self.check_creatquote_url)

    def test_dealer_quote_ui_002(self):
        '''Verify the default section in Create Dealer Quotes page"'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Quote Details','Doors Panel Lift-Safe Insulated Sectional ExoRoll Door','Save Quote'),
                         self.check_defaulsection)

    def test_dealer_quote_ui_003(self):
        '''Verify the Save Quote button in Create Dealer Quotes page'''
        self.driver.implicitly_wait(2)
        self.assertEqual(True,self.check_savequote_btn)


    def test_dealer_quote_ui_004(self):
        '''Verify each description of Quote Details in Add Dealer Quotes page"'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Proposal Number','Customer Purchase Order','User','Job Notes'),self.check_quote_details)

    def test_dealer_quote_ui_005(self):
        '''Verify the default value in "User" list, it should be current login user'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('tim2 sun2'),self.check_default_user)

    def test_dealer_quote_ui_006(self):
        '''Verify the input editbox for "proposal_number"'''
        self.driver.implicitly_wait(2)
        self.assertTrue(self.check_proposal_num_box)

    def test_dealer_quote_ui_007(self):
        '''Verify the input editbox for "Customer Purchase order"'''
        self.driver.implicitly_wait(2)
        self.assertTrue(self.check_purchase_order_box)

    def test_dealer_quote_ui_008(self):
        '''Verify the job notes from the Job Notes box'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('test for note_516\n516-test for note'),self.check_job_notes)

    def test_dealer_quote_ui_009(self):
        '''Verify the job notes from the Job Notes box'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Insulated Sectional','Panel Lift-Safe','ExoRoll Door','There are no items to display'),
                         self.check_doors_details)





if __name__ == '__main__':
    unittest.main(verbosity=2)

