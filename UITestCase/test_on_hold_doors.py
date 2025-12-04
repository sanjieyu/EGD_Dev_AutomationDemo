# Author:Yi Sun(Tim) 2024-11-14

'''Test On Holder Doors Page'''

import unittest
from selenium import webdriver
from CommonModule.read_config import *
from UIModule.on_hold_doors import *

class On_Hold_Test(unittest.TestCase,On_Hold):
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
        cls.login.login(cls.admin_username, cls.admin_password)
        cls.driver.implicitly_wait(5)
        cls.go_onhold = On_Hold(cls.driver)
        cls.go_onhold.go_hold_doors()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_on_hold_ui_001(self):
        '''Verify the URL for On Hold Doors screen'''
        self.driver.implicitly_wait(2)
        self.assertEqual("http://aabb/Quote/OnHold",self.check_onhold_url)

    def test_on_hold_ui_002(self):
        '''Verify the title for On Hold Doors screen'''
        self.driver.implicitly_wait(2)
        self.assertEqual("On-Hold Quotes",self.check_onhold_title)
    def test_on_hold_ui_003(self):
        '''Verify the elements for Details section'''
        self.driver.implicitly_wait(2)
        self.assertEqual(("Client Details","Client Name","Contact Number","Location","Suburb",
                          "Site Address","Quote Information","Proposal No","User"),self.check_details)

    def test_on_hold_ui_004(self):
            '''Verify the title for Job Accepted screen'''
            self.driver.implicitly_wait(2)
            self.assertTrue(self.search_quotes_btn_loc)

    def test_on_hold_ui_005(self):
            '''Verify the title for On Hold Doors screen'''
            self.driver.implicitly_wait(2)
            self.assertIn("Results Found", self.check_results_found)

    def test_on_hold_ui_006(self):
        '''Verify each column of On Hold Doors'''
        self.driver.implicitly_wait(2)
        self.assertEqual(("Proposal", "Created Date",  "Client Name", "Order Date","Door Number",  "Door Status"),
                         self.check_columns)

    def test_on_hold_ui_007(self):
        '''Verify the Save Changes button in On Hold Doors screen'''
        self.driver.implicitly_wait(2)
        self.assertTrue(self.check_save_button)

if __name__ == "__main__":
    unittest.main(verbosity=2)