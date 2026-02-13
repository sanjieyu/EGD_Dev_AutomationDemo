# Author:Yi Sun(Tim) 2025-2-07

'''Test Dealer Quotation screen'''

import unittest
from selenium import webdriver
from utils.read_config import *
from pages.dealer_quotation_panel import *

class Dealer_Quotation_Panel_Test(unittest.TestCase,Dealer_Quotation_Panel):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.read_config = ReadConfig()
        cls.url = cls.read_config.get_url()
        cls.dealer_username = cls.read_config.dealer_username()
        cls.dealer_password = cls.read_config.dealer_password()
        cls.login = Admin_Portal(cls.driver)
        cls.driver.get(cls.url)
        cls.login.login(cls.dealer_username,cls.dealer_password)
        cls.driver.implicitly_wait(5)
        cls.go_quotation = Dealer_Quotation_Panel(cls.driver)
        cls.go_quotation.go_dealer_quotation()
        cls.proposal_num = cls.go_quotation.proposal_number


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_dealer_quotation_panel_ui_001(self):
        '''Verify the major sections on Quotation screen"'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Quotation','Job Summary','Total Cost','Proposal Documents','Door 1',
                          'Back to Site Details','Save Quote','Send Email','Submit Quote'),self.check_major_sections())

    def test_dealer_quotation_panel_ui_002(self):
            '''Verify each element in quotation section"'''
            self.driver.implicitly_wait(2)
            self.assertEqual(('Client Name', 'Contact Mobile', 'Proposal Number', 'Contact Full Address',
                              'Salesperson'),self.check_quotation_section())

    def test_dealer_quotation_panel_ui_003(self):
        '''Verify the values for each contact detail"'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Customer Tim dealer 2', '12345', self.proposal_num, '12 Bonview Mel 3004',
                          'tim2 sun2'), self.check_contact_details())

    def test_dealer_quotation_panel_ui_004(self):
            '''Verify each element in job summary section"'''
            self.driver.implicitly_wait(2)
            self.assertEqual('Door 1 Summary', self.check_job_summary_section())

    def test_dealer_quotation_panel_ui_005(self):
        '''Verify the door settings button"'''
        self.driver.implicitly_wait(2)
        self.assertTrue(self.check_door_setting_btn())

    def test_dealer_quotation_panel_ui_006(self):
        '''Verify the door1's details in Door Summary section"'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Panel Lift-Safe','Classic panel','Woodgrain Texture','ColorBond, Monument',
                          'Opener: Manual/No Opener or Lock'),self.check_door1_details())

    def test_dealer_quotation_panel_ui_007(self):
        '''Verify the door1's sizes in Door Summary section"'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('2200','3000','Opening Size LH: 2200','Opening Size RH: 2200',
                          'Opening Size Width: 3000'),self.check_door1_size())

    def test_dealer_quotation_panel_ui_008(self):
        '''Verify the door1's sizes in Condition of Contract section"'''
        self.driver.implicitly_wait(2)
        self.assertEqual('Condition of Contract',self.check_condition_section())

    def test_dealer_quotation_panel_ui_009(self):
            '''Verify each element in Cost section"'''
            self.driver.implicitly_wait(2)
            self.assertEqual(('Total Cost', 'GST','Sale Amount (Ex GST)',
                              'Total Sale Amount (Inc GST)'), self.check_cost_section())

    def test_dealer_quotation_panel_ui_010(self):
            '''Verify the price amount in Cost section"'''
            self.driver.implicitly_wait(2)
            self.assertEqual(( '117.60','1176.00','1293.60'), self.check_cost_amount())

    def test_dealer_quotation_panel_ui_011(self):
            '''Verify each element in Proposal Documents section"'''
            self.driver.implicitly_wait(2)
            self.assertEqual(( 'Add / Replace document', 'Print'),self.check_proposal_documents_section())

    def test_dealer_quotation_panel_ui_012(self):
        '''Verify the Print Sheet in Proposal Documents section"'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Order Confirmation'),self.check_print_sheet())

if __name__ == "__main__":
    unittest.main(verbosity=2)