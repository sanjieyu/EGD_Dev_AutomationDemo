# Author:Yi Sun(Tim) 2025-11-13

'''Test Change Quote Status for OptiRoll doors '''

import unittest
from selenium import webdriver
from CommonModule.read_config import *
from UIModule.change_quote_status_optiroll import *

class Change_Quote_Status_OptiRoll_Test(unittest.TestCase,Change_Quote_Status_OptiRoll):
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
        cls.go_status = Change_Quote_Status_OptiRoll(cls.driver)


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_status_change_optiroll_ui_001(self):
            '''Verify the status change function, change a quote status to "MYOB Ready"'''
            self.driver.implicitly_wait(2)
            self.go_status.go_status_page()
            self.go_status.change_status_order()
            self.driver.implicitly_wait(2)
            result = self.go_status.check_myob_status()
            self.assertTrue(result)

    def test_status_change_optiroll_ui_002(self):
            '''Verify the status change function, change a quote status to "Order" then check if
            it is listed in Order Screen'''
            self.driver.implicitly_wait(2)
            result = self.go_status.check_order_status()
            self.assertTrue(result)

    def test_status_change_optiroll_ui_003(self):
            '''Verify the status change function, change a quote status to "Rollforming"'''
            self.driver.implicitly_wait(2)
            result = self.go_status.check_rollforming_status()
            self.assertTrue(result)

if __name__ == "__main__":
    unittest.main(verbosity=2)