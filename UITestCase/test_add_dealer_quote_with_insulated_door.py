# Author:Yi Sun(Tim) 2025-2-11

'''Test Add a Dealer Quote with a insulated door function'''

import time
import unittest
from selenium import webdriver
from time import *
from UIModule.add_dealer_quote_with_insulated_door import *
from CommonModule.read_config import *

class Add_Dealer_Quote_With_InsulatedDoor_UI_Test(unittest.TestCase,Add_Dealer_Quote_With_Insulated_Door):
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
        cls.add_dealer_quote_with_insulatederdoor = Add_Dealer_Quote_With_Insulated_Door(cls.driver)
        cls.add_dealer_quote_with_insulatederdoor.add_dealer_insulateddoor_fun()
        cls.add_dealer_quote_with_insulatederdoor.get_proposal_number
        cls.add_dealer_quote_with_insulatederdoor.search_new_quote()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_add_dealer_quote_with_insulateddoor_fun_001(self):
            '''Verify  Add a Dealer Quote with a Roller door function'''
            self.driver.implicitly_wait(2)
            self.assertEqual(('Door 1(A1)', 'Quote'), self.verify_new_quote)

    def test_add_dealer_quote_with_insulateddoor_fun_002(self):
            '''Verify the Quote status after submit'''
            self.driver.implicitly_wait(2)
            self.add_dealer_quote_with_insulatederdoor.go_quotation()
            self.assertEqual('Processing', self.verify_new_quote_submitted)

if __name__ == '__main__':
        unittest.main(verbosity=2)