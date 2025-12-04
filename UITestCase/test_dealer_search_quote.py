# Author:Yi Sun(Tim) 2025-01-21

'''Test Search Quote Page on Dealer Portal'''

import time
import unittest
from selenium import webdriver
from time import *
from UIModule.dealer_search_quote import *
from CommonModule.read_config import *

class SearchQuote_DP_UI_Test(unittest.TestCase,Search_Quote_DP):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.config_read = ReadConfig()
        cls.url = cls.config_read.get_url()
        cls.dealer_usename = cls.config_read.dealer_username()
        cls.dealer_password = cls.config_read.dealer_password()
        cls.login = Admin_Portal(cls.driver)
        cls.driver.get(cls.url)
        cls.login.login(cls.dealer_usename,cls.dealer_password)
        cls.driver.implicitly_wait(5)
        cls.go_searchquotes_dp = Search_Quote_DP(cls.driver)
        cls.go_searchquotes_dp.go_search_quotes()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_searchquotes_dp_ui_001(self):
        '''Verify the url for Search Quotes page'''
        self.driver.implicitly_wait(2)
        self.assertEqual('http://aabb/Dealer/List',self.check_searchurl)

    def test_searchquotes_dp_ui_002(self):
        '''Verify the title for Search Quotes page'''
        self.driver.implicitly_wait(2)
        self.assertEqual('Search Quotes',self.check_title)

    def test_searchquotes_dp_ui_003(self):
            '''Verify the Search Quotes button'''
            self.driver.implicitly_wait(2)
            self.assertTrue(self.check_search_btn)

    def test_searchquotes_dp_ui_004(self):
        '''Verify the default elements in Search Quotes page'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Quotes','Doors','Search Results'),self.check_defaultelements)

    def test_searchquotes_dp_ui_005(self):
        '''Verify each section of Quotes filter table in Search Quotes page'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Date Range', 'Client Details', 'Quote Information'), self.check_section_quotes)

    def test_searchquotes_dp_ui_006(self):
        '''Verify each filter in "Date Range" in Quotes filter table'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Filter Date','User','Quote Status'),self.check_date_range)

    def test_searchquotes_dp_ui_007(self):
        '''Verify each filter in "Client Details" in Quotes filter table'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Client Name', 'Contact Number', 'Suburb', 'Postcode'), self.check_client_details)

    def test_searchquotes_dp_ui_008(self):
        '''Verify each filter in "Quote Information" in Quotes filter table'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Proposal No','Door Design','Colour Category','Door Colour'),
                         self.check_quote_info)

    def test_searchquotes_dp_ui_009(self):
        '''Verify the default user name in "User" filter in Quotes filter table, should be the current login user'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('tim2 sun2'),self.check_default_user)

    def test_searchquotes_dp_ui_010(self):
        '''Verify the search by Proposal ID function'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('209239'),self.search_proposal_id)

if __name__ == '__main__':
    unittest.main(verbosity=2)
