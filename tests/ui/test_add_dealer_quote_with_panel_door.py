# Author:Yi Sun(Tim) 2025-1-24

'''Test Add a Dealer Quote with a panel door function'''

import time
import unittest
from selenium import webdriver
from time import *
from pages.add_dealer_quote_with_panel_door import *
from utils.read_config import *

class Add_Dealer_Quote_With_PanelDoor_UI_Test(unittest.TestCase,Add_Dealer_Quote_With_Panel_Door):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.config_read =ReadConfig()
        cls.url = cls.config_read.get_url()
        cls.dealer_username = cls.config_read.dealer_username()
        cls.dealer_password = cls.config_read.dealer_password()
        cls.login = Admin_Portal(cls.driver)
        cls.driver.get(cls.url)
        cls.login.login(cls.dealer_username,cls.dealer_password)
        cls.driver.implicitly_wait(5)
        cls.add_dealer_quote_with_paneldoor = Add_Dealer_Quote_With_Panel_Door(cls.driver)
        cls.add_dealer_quote_with_paneldoor.add_dealer_paneldoor_fun()
        cls.add_dealer_quote_with_paneldoor.get_proposal_number
        cls.add_dealer_quote_with_paneldoor.search_new_quote()


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_add_dealer_quote_with_paneldoor_fun_001(self):
            '''Verify  Add a Dealer Quote with a Panel door function'''
            self.driver.implicitly_wait(2)
            self.assertEqual(('Door 1(A1)', 'Quote'), self.verify_new_quote)

    def test_add_dealer_quote_with_paneldoor_fun_002(self):
            '''Verify the Quote status after submit'''
            self.driver.implicitly_wait(2)
            self.add_dealer_quote_with_paneldoor.go_quotation()
            self.assertEqual('Processing', self.verify_new_quote_submitted)

if __name__ == '__main__':
        unittest.main(verbosity=2)