# Author:Yi Sun(Tim) 2024-5-23

'''Test MYOB Quotes Page'''

import unittest
from selenium import webdriver
from CommonModule.read_config import *
from UIModule.myob_quote import *

class MYOB_Quotes_Test(unittest.TestCase,MYOB_Quotes):

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
        cls.go_myob = MYOB_Quotes(cls.driver)
        cls.go_myob.go_myob_quotes()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_myob_quotes_ui_001(self):
        '''Verify the URL'''
        self.driver.implicitly_wait(2)
        self.assertEqual("http://aabb/Quote/MYOB",self.check_myob_url)

    def test_myob_quotes_ui_002(self):
        '''Verify the title'''
        self.driver.implicitly_wait(2)
        self.assertEqual("MYOB Quotes",self.check_myob_title)

    def test_myob_quotes_ui_003(self):
        '''Verify client details section'''
        self.driver.implicitly_wait(2)
        self.assertEqual(("Client Details","Client Name","Contact Number"),self.check_client_details)
    def test_myob_quotes_ui_004(self):
        '''Verify Location section'''
        self.driver.implicitly_wait(2)
        self.assertEqual(("Location","Suburb","Site Address"),self.check_location)

    def test_myob_quotes_ui_005(self):
            '''Verify Quote Information section'''
            self.driver.implicitly_wait(2)
            self.assertEqual(("Quote Information", "Proposal No", "User"), self.check_quote_info)

    def test_myob_quotes_ui_006(self):
        '''Verify the Client Name box'''
        self.driver.implicitly_wait(2)
        self.assertEqual(True, self.check_client_name_box)


    def test_myob_quotes_ui_007(self):
        '''Verify the Contact Number  box'''
        self.driver.implicitly_wait(2)
        self.assertEqual(True, self.check_contact_num_box)

    def test_myob_quotes_ui_008(self):
        '''Verify the Suburb box'''
        self.driver.implicitly_wait(2)
        self.assertEqual(True, self.check_suburb_box)

    def test_myob_quotes_ui_009(self):
        '''Verify the Site Address box'''
        self.driver.implicitly_wait(2)
        self.assertEqual(True, self.check_site_address_box)

    def test_myob_quotes_ui_010(self):
        '''Verify the Proposal No box'''
        self.driver.implicitly_wait(2)
        self.assertEqual(True, self.check_proposal_no_box)

    def test_myob_quotes_ui_011(self):
        '''Verify the default user in User box'''
        self.driver.implicitly_wait(2)
        self.assertEqual("All users", self.check_default_user)

    def test_myob_quotes_ui_012(self):
        '''Verify  search function in MYOB by user, ONLY for DEV'''
        self.driver.implicitly_wait(2)
        self.assertEqual("209492", self.search_myob_fun)

if __name__ == "__main__":
    unittest.main(verbosity=2)