# Author:Yi Sun(Tim) 2024-08-06

'''Test Edit Account Customer Page'''


import unittest
from selenium import webdriver
from time import *
from pages.edit_account_customer import *
from utils.read_config import *

class Edit_AccountCustomer_UI_Test(unittest.TestCase,Edit_Account_Customer):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.read_config = ReadConfig()
        cls.url = cls.read_config.get_url()
        cls.username = cls.read_config.admin_username()
        cls.password = cls.read_config.admin_password()
        cls.login = Admin_Portal(cls.driver)
        cls.driver.get(cls.url)
        cls.login.login(cls.username,cls.password)
        cls.driver.implicitly_wait(5)
        cls.go_edit_accountcustomer = Edit_Account_Customer(cls.driver)
        cls.go_edit_accountcustomer.goto_account_customer()
        cls.go_edit_accountcustomer.goto_edit_account()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()


    def test_edit_account_customer_ui_001(self):
        '''Verify the url'''
        self.driver.implicitly_wait(2)
        self.assertIn('http://aabb/Customer/Edit',self.check_edit_url)

    def test_edit_account_customer_ui_002(self):
            '''Verify general elements on this screen'''
            self.driver.implicitly_wait(2)
            self.assertEqual(('Edit Customer  ', 'Is active (on)', 'Access to Dealer Portal (on)', 'Customer Name',
                              'First Name','Back to Customers','Save Customer'), self.check_general_elements)

    def test_edit_account_customer_ui_003(self):
        '''Verify the Active Status'''
        self.driver.implicitly_wait(2)
        self.assertTrue(self.check_active_status)

    def test_edit_account_customer_ui_004(self):
            '''Verify active off status'''
            self.driver.implicitly_wait(2)
            self.check_active_status
            self.assertEqual('Is active (off)', self.check_active_off)

if __name__ == '__main__':
        unittest.main(verbosity=2)

