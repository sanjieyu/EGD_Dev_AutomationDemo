# Author:Yi Sun(Tim) 2025-10-14

'''Test OptiRoll Doors Production Page'''

import time
import unittest
from selenium import webdriver
from time import *
from pages.optiroll_production import *
from utils.read_config import *
from selenium.webdriver.support.ui import WebDriverWait

class OptiRoll_Production_UI_Test(unittest.TestCase,OptiRoll_Production):
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
        cls.goproduction_wa = Production_WA(cls.driver)
        cls.goproduction_wa.go_production_wa()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_optiroll_production_ui_001(self):
        '''Verify each section in OptiRoll Production page'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Order','Rollforming','Assembly','Modifications','Extras Orders','QC'),
                         self.check_optiroll_doors_section)

    def test_optiroll_production_ui_002(self):
        '''Verify each column in Order table'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Number of Doors:','Proposal No','Client Name','Supply Type','Door No',
                          'Status','    Extras Orders & Documents'),self.check_order_table)

    def test_optiroll_production_ui_003(self):
            '''Verify each elements in Rollforming table'''
            self.driver.implicitly_wait(2)
            self.assertEqual(('Number of Doors:', 'Reschedule from:'), self.check_rollforming_table)

    def test_optiroll_production_ui_004(self):
        '''Verify Date Filter fun in Rollforming table'''
        self.driver.implicitly_wait(2)
        self.assertEqual(True, self.check_rollforming_date_filter)

    def test_optiroll_production_ui_005(self):
        '''Verify Save Changes button in Rollforming table'''
        self.driver.implicitly_wait(2)
        self.assertEqual(True, self.check_rollforming_save)

    def test_optiroll_production_ui_006(self):
            '''Verify Table display in Rollforming screen'''
            self.driver.implicitly_wait(2)
            self.assertEqual(True, self.check_rollforming_tableframe)

    def test_optiroll_production_ui_007(self):
        '''Verify each elements in Assembly table'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Number of Doors:', 'Prop. No', 'Door No', 'Status'), self.check_assembly_table)

    def test_optiroll_production_ui_008(self):
        '''Verify the Save btn in Assembly table'''
        self.driver.implicitly_wait(2)
        self.assertTrue(self.check_assembly_save)

    def test_optiroll_production_ui_009(self):
        '''Verify each elements in Modification table'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Number of Doors:', 'Prop. No', 'Door Colour', '    Extras Orders & Documents'),
                         self.check_modification_table)

    def test_optiroll_production_ui_010(self):
        '''Verify the Save btn in Assembly table'''
        self.driver.implicitly_wait(2)
        self.assertTrue(self.check_modification_save)

    def test_optiroll_production_ui_011(self):
        '''Verify each elements in Extras Orders table'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Number of Doors:', 'Prop. No', 'Colour Category', '    Extras Orders & Documents'),
                         self.check_extraorder_table)
    #
    def test_optiroll_production_ui_012(self):
        '''Verify the Save btn in Extras Orders table'''
        self.driver.implicitly_wait(2)
        self.assertTrue(self.check_extrasorders_save)

    def test_optiroll_production_ui_013(self):
            '''Verify each elements in QC table'''
            self.driver.implicitly_wait(2)
            self.assertEqual(('Number of Doors:', 'Proposal No', 'Actual Width', 'Status'),
                             self.check_qc_table)

    def test_optiroll_production_ui_014(self):
        '''Verify the Save btn in QC table'''
        self.driver.implicitly_wait(2)
        self.assertTrue(self.check_qc_save)

    def test_optiroll_production_ui_015(self):
            '''Verify qc pass and qc fail radio box in QC table'''
            self.driver.implicitly_wait(2)
            self.assertEqual(('QC Fail', 'QC Pass',),self.check_qc_table_new)

    def test_optiroll_production_ui_016(self):
            '''Verify qc fail radio box status'''
            self.driver.implicitly_wait(2)
            self.assertTrue(self.check_qc_fail)

    def test_optiroll_production_ui_017(self):
            '''Verify qc fail radio box status'''
            self.driver.implicitly_wait(2)
            self.assertTrue(self.check_qc_pass)


if __name__ == '__main__':
    unittest.main(verbosity=2)