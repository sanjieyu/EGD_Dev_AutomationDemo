# Author:Yi Sun(Tim) 2024-9-05

'''Test Quotation screen'''

import unittest
from selenium import webdriver
from CommonModule.read_config import *
from UIModule.quotation_panel_door import *

class Quotation_Panel_Test(unittest.TestCase,Quotation_Panel):
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
        cls.go_quotation = Quotation_Panel(cls.driver)
        cls.go_quotation.goto_quotation_page()
        cls.proposal_num = cls.go_quotation.proposal_number


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_quotation_ui_001(self):
        '''Verify the major sections on Quotation screen"'''
        self.driver.implicitly_wait(2)
        # self.go_quotation.goto_quotation_page()
        self.assertEqual(('Quotation','Job Summary','Condition of Contract','Payment Details',
                          'Proposal Documents','Door 1','Back to Site Details','Save Quote'),self.check_major_sections())

    def test_quotation_ui_002(self):
        '''Verify each element in quotation section"'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Client Name','Contact Mobile','Proposal Number','Contact Full Address',
                          'Salesperson','Contact Name','Site Phone','Site Full Address','Quote Status: Quote'),
                         self.check_quotation_section())

    def test_quotation_ui_003(self):
        '''Verify the values for each contact detail"'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('For Automation Testing','041111122',self.proposal_num,'11 bonview Mel 3004',
                          'Yi_Account Sun'),self.check_contact_details())

    def test_quotation_ui_004(self):
        '''Verify each element in job summary section"'''
        self.driver.implicitly_wait(2)
        self.assertEqual('Door 1 Summary',self.check_job_summary_section())

    def test_quotation_ui_005(self):
        '''Verify the door settings button"'''
        self.driver.implicitly_wait(2)
        self.assertTrue(self.check_door_setting_btn())

    def test_quotation_ui_006(self):
        '''Verify the door1's details in Door Summary section"'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Panel Lift-Safe','Classic panel','Woodgrain Texture','ColorBond, Monument',
                          'Commercial Cat 1','Opener: Use Existing'),self.check_door1_details())

    def test_quotation_ui_007(self):
        '''Verify the door1's sizes in Door Summary section"'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('2010','2560','Opening Size LH: 2000','Opening Size RH: 2000',
                          'Opening Size Width: 2500','SR Left: 200','HR: 300','SR Right: 200'),self.check_door1_size())
    def test_quotation_ui_008(self):
        '''Verify each element in Condition of Contract section"'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Condition of Contract','Date','Signature','I accept all terms and conditions',
                          'Lock Signature','Clear Signature'),self.check_condition_section())

    def test_quotation_ui_009(self):
            '''Verify each element in Payment section"'''
            self.driver.implicitly_wait(2)
            self.assertEqual(('Payment Type:', 'Total Cost ?','Banking details','Payment Terms'),
                             self.check_payments_section())

    def test_quotation_ui_010(self):
        '''Verify the payment type in Payment section,should be "Account"'''
        self.driver.implicitly_wait(2)
        self.assertTrue(self.check_payment_type())

    def test_quotation_ui_011(self):
        '''Verify the payment deposit percentage in Payment section,should be "0"'''
        self.driver.implicitly_wait(2)
        self.assertTrue(self.check_payment_deposit())

    # @unittest.skip
    def test_quotation_ui_012(self):
            '''Verify the payment Net percentage in Payment section,should be "100%"'''
            self.driver.implicitly_wait(2)
            self.assertTrue(self.check_payment_net())

    def test_quotation_ui_013(self):
        '''Verify the payment deposit percentage in Payment section,should be "50% if it's cash sale'''
        self.driver.implicitly_wait(2)
        self.assertTrue(self.go_quotation.check_cash_net())

    def test_quotation_ui_014(self):
            '''Verify each element in Proposal Documents section"'''
            self.driver.implicitly_wait(2)
            self.assertEqual(('Sign Off attached', 'Add / Replace document', 'Print'),
                             self.check_proposal_documents_section())

    def test_quotation_ui_015(self):
        '''Verify the Print Sheet in Proposal Documents section"'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Quote\nSchedule Sheet\nMYOB Sheet\nProduction Sheet\nPro-Former Invoice\n'
                          'Tax Invoice\nOrder Confirmation'), self.check_print_sheet())

    def test_quotation_ui_016(self):
            '''Verify each element in Door section"'''
            self.driver.implicitly_wait(2)
            self.assertEqual(('Measure Documents', 'Site Pictures', 'Add / Replace document'),
                             self.check_door_section())

if __name__ == "__main__":
    unittest.main(verbosity=2)