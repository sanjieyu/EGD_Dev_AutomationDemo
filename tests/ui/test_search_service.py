# Author:Yi Sun(Tim) 2023-11-9

'''Test Search Serivce Page'''
import time
import unittest
from selenium import webdriver
from time import *
from pages.search_service import *
from utils.read_config import *

class SearchService_UI_Test(unittest.TestCase,Search_Service):
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
        cls.gosearchservice = Search_Service(cls.driver)
        cls.gosearchservice.go_searchservice()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_searchservice_ui_001(self):
        '''Verify the url for Search Service page'''
        self.driver.implicitly_wait(2)
        self.assertIn('http://aabb/Service/List',self.check_searchurl)

    def test_searchservice_ui_002(self):
        '''Verify the title for Search Service page'''
        self.driver.implicitly_wait(2)
        self.assertEqual('Search Services',self.check_title)

    def test_searchservice_ui_003(self):
        '''Verify the default section in Search Service page'''
        self.driver.implicitly_wait(2)
        self.assertEqual(True,self.check_defaulsection)

    def test_searchservice_ui_004(self):
        '''Verify the default elements in Search Service page'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Quotes','Services','Search Results'),self.check_defaultelements)

    def test_searchservice_ui_005(self):
        '''Verify each section of Service filter table in Search Service page'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Date Range','Client Details','Service Information'),self.check_section_service)

    def test_searchservice_ui_006(self):
        '''Verify each filter in "Date Range" in Service filter table'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Filter Date','User'),self.check_date_range)
    def test_searchservice_ui_007(self):
        '''Verify each filter in "Client Details" in Service filter table'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Client Name','Address','Suburb','Postcode','Contact Number'),
                         self.check_client_details)

    def test_searchservice_ui_008(self):
            '''Verify each filter in "Service Infomation" in Service filter table'''
            self.driver.implicitly_wait(2)
            self.assertEqual(('Service Status', 'Service Area', 'Service Type', 'Invoice No', 'Customer PO'),
                             self.check_service_info)
    def test_searchservice_ui_009(self):
            '''Verify each filter in "Service Infomation" in Service filter table'''
            self.driver.implicitly_wait(2)
            self.assertEqual(('Yi Sun'),self.check_default_user)
    def test_searchservice_ui_010(self):
            '''Verify the search by client name function'''
            self.driver.implicitly_wait(2)
            self.assertEqual(('204325S1'),self.search_client_name)
    def test_searchservice_ui_011(self):
            '''Verify the search by address function'''
            self.driver.implicitly_wait(2)
            self.assertEqual(('204325S1'),self.search_address)

    def test_searchservice_ui_012(self):
            '''Verify the search by Suburb function'''
            self.driver.implicitly_wait(2)
            self.assertEqual(('204325S1'),self.search_suburb)

    def test_searchservice_ui_013(self):
            '''Verify the search by Postcode function'''
            self.driver.implicitly_wait(2)
            self.assertEqual(('204325S1'),self.search_postcode)

    def test_searchservice_ui_014(self):
        '''Verify the search by Contact Number function'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('204325S1'), self.search_contact_num)

    def test_searchservice_ui_015(self):
        '''Verify the Service Status dropdown list'''
        self.driver.implicitly_wait(2)
        self.assertIn(('Quote\nMYOB Ready\nOrder'), self.check_service_status)

    def test_searchservice_ui_016(self):
        '''Verify the Service Area dropdown list'''
        self.driver.implicitly_wait(2)
        self.assertIn(('Vic Metro\nVic Country\nVic Pick up\nVic Delivery\nSydney metro\nSydney pick up\n'
                       'Sydney delivery\nNSW country'), self.check_service_area)

    def test_searchservice_ui_017(self):
        '''Verify the Service Type dropdown list'''
        self.driver.implicitly_wait(2)
        self.assertIn(('Residential\nCommercial\nWarranty\nGoodwill\nNon Conformance'), self.check_service_type)

    def test_searchservice_ui_018(self):
        '''Verify the search by Invoice No. function'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('204325S1'), self.search_invoice_no)

    def test_searchservice_ui_019(self):
        '''Verify the search by Customer PO function'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('204325S1'), self.search_customer_po)

if __name__ == '__main__':
    unittest.main(verbosity=2)