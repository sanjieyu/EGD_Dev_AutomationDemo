# Author:Yi Sun(Tim) 2024-08-05

'''Test Account Customer Page'''


import unittest
from selenium import webdriver
from time import *
from UIModule.account_customer import *
from CommonModule.read_config import *

class AccountCustomer_UI_Test(unittest.TestCase, Account_Customer):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.config_read = ReadConfig()
        cls.url = cls.config_read.get_url()
        cls.username = cls.config_read.admin_username()
        cls.password = cls.config_read.admin_password()
        cls.login = Admin_Portal(cls.driver)
        cls.driver.get(cls.url)
        cls.login.login(cls.username,cls.password)
        cls.driver.implicitly_wait(5)
        cls.go_accountcustomer = Account_Customer(cls.driver)
        cls.go_accountcustomer.goto_account_customer()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_account_customer_ui_001(self):
        '''Verify the url'''
        self.driver.implicitly_wait(2)
        self.assertEqual('http://aabb/List',self.check_accountcustomer_url)

    def test_account_customer_ui_002(self):
        '''Verify the title'''
        self.driver.implicitly_wait(2)
        self.assertEqual('Account Customers Search',self.check_accountcustomer_title)

    def test_account_customer_ui_003(self):
        '''Verify the search button'''
        self.driver.implicitly_wait(2)
        self.assertTrue(self.check_search_btn)

    def test_account_customer_ui_004(self):
        '''Verify the search box'''
        self.driver.implicitly_wait(2)
        self.assertTrue(self.check_searchbox)

    def test_account_customer_ui_005(self):
        '''Verify each column on this screen'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Customer Name','Contact Name','Address','Email','Suburb'),self.check_columns)

    def test_account_customer_ui_006(self):
        '''Verify the Search function'''
        self.driver.implicitly_wait(2)
        self.assertEqual('tim2 with priced items',self.check_search_result)



if __name__ == '__main__':
    unittest.main(verbosity=2)

