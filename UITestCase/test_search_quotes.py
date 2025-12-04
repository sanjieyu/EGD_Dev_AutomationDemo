# Author:Yi Sun(Tim) 2023-08-29

'''Test Search Quotes Page'''
import time
import unittest
from selenium import webdriver
from time import *
from UIModule.search_quote import *
from CommonModule.read_config import *

class SearchQuotes_UI_Test(unittest.TestCase,Search_Quote):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.config_read = ReadConfig()
        cls.url = cls.config_read.get_url()
        cls.admin_username = cls.config_read.admin_username()
        cls.admin_password = cls.config_read.admin_password()
        cls.login = Admin_Portal(cls.driver)
        cls.driver.get(cls.url)
        cls.login.login(cls.admin_username,cls.admin_password)
        cls.driver.implicitly_wait(5)
        cls.gosearchquotes = Search_Quote(cls.driver)
        cls.gosearchquotes.go_searchquotes()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_searchquotes_ui_001(self):
        '''Verify the url for Search Quotes page'''
        self.driver.implicitly_wait(2)
        self.assertEqual('http://aabb/Quote/List',self.check_searchurl)

    def test_searchquotes_ui_002(self):
        '''Verify the title for Search Quotes page'''
        self.driver.implicitly_wait(2)
        self.assertEqual('Search Quotes',self.check_title)
    def test_searchquotes_ui_003(self):
        '''Verify the default section should be "Quotes" in Search Quotes page'''
        self.driver.implicitly_wait(2)
        self.assertEqual(True,self.check_defaulsection)

    def test_searchquotes_ui_004(self):
        '''Verify the default elements in Search Quotes page'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Quotes','Doors','Search Results'),self.check_defaultelements)

    def test_searchquotes_ui_005(self):
        '''Verify each section of Quotes filter table in Search Quotes page'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Date Range','Client Details','Quote Information'),self.check_section_quotes)

    def test_searchquotes_ui_006(self):
        '''Verify each filter in "Date Range" in Quotes filter table'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Filter Date','User','Quote Status'),self.check_date_range)

    def test_searchquotes_ui_007(self):
        '''Verify each filter in "Client Details" in Quotes filter table'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Client Name','Contact Number','Suburb','Postcode'),self.check_client_details)

    def test_searchquotes_ui_008(self):
        '''Verify each filter in "Quote Information" in Quotes filter table'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Proposal No','Door Design','Colour Category','Door Colour','Site Address'),
                         self.check_quote_info)

    def test_searchquotes_ui_009(self):
        '''Verify the default user name in "User" filter in Quotes filter table, should be the current login user'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Yi Sun'),self.check_default_user)

    def test_searchquotes_ui_010(self):
        '''Verify the search by client name function, should find the correct proposal No. for this client'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('208849'),self.search_client_name)

    def test_searchquotes_ui_011(self):
        '''Verify the search by Proposal ID function, should find the correct proposal No. for this client'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('210088'),self.search_proposal_id)

    def test_searchquotes_ui_012(self):
        '''Verify the search by Contact Number function, should find the correct proposal No. for this client'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('210088'),self.search_contact_num)

    def test_searchquotes_ui_013(self):
        '''Verify the search by Suburb function, should find the correct proposal No. for this client'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('210088'),self.search_suburb)

    def test_searchquotes_ui_014(self):
        '''Verify the search by Postcode function, should find the correct proposal No. for this client'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('210088'),self.search_postcode)

    def test_searchquotes_ui_015(self):
        '''Verify the search by Door Design function, should find the correct proposal No. for this client'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('204532'),self.search_door_design)

    def test_searchquotes_ui_016(self):
        '''Verify the search by Door Colour function, should find the correct proposal No. for this client'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('210392'),self.search_door_colour)

    def test_searchquotes_ui_017(self):
        '''Verify the search by Colour Category function, should find the correct proposal No. for this client'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('204531'),self.search_door_category)


if __name__ == '__main__':
    unittest.main(verbosity=2)
