# Author:Yi Sun(Tim) 2024-11-11

'''Test New Order Page'''

import unittest
from selenium import webdriver
from CommonModule.read_config import *
from UIModule.new_order import *

class New_Order_Test(unittest.TestCase,New_Order):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.read_config = ReadConfig()
        cls.url = cls.read_config.get_url()
        cls.admin_username = cls.read_config.admin_username()
        cls.admin_password = cls.read_config.admin_password()
        cls.login = Admin_Portal(cls.driver)
        cls.driver.get(cls.url)
        cls.login.login(cls.admin_username,cls.admin_password)
        cls.driver.implicitly_wait(5)
        cls.go_neworder = New_Order(cls.driver)
        cls.go_neworder.go_new_order()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_new_order_ui_001(self):
        '''Verify the URL for New Order screen'''
        self.driver.implicitly_wait(2)
        self.assertEqual("http://aabb/Quote/NewOrder",self.check_neworder_url)

    def test_new_order_ui_002(self):
        '''Verify the title for New Order screen'''
        self.driver.implicitly_wait(2)
        self.assertEqual("New Order",self.check_neworder_title)
    def test_new_order_ui_003(self):
        '''Verify each column of New Order screen'''
        self.driver.implicitly_wait(2)
        self.assertEqual(("Proposal No","Created Date","Client Name","Door Number","Order Date",
                          "Door Status","Documents"),self.check_columns)

    def test_new_order_ui_004(self):
        '''Verify the Save Changes button in New Order screen'''
        self.driver.implicitly_wait(2)
        self.assertTrue(self.check_save_button)


if __name__ == "__main__":
    unittest.main(verbosity=2)