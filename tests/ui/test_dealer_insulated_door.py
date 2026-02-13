# Author:Yi Sun(Tim) 2024-11-04

'''Test Dealer Roller Door Details Page'''

import time
import unittest
from selenium import webdriver
from time import *
from pages.dealer_insulated_door import *
from utils.read_config import *

class Add_InsulatedDoor_UI_Test(unittest.TestCase,Dealer_Insulated_Door):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.config_read = ReadConfig()
        cls.url = cls.config_read.get_url()
        cls.dealer_username = cls.config_read.dealer_username()
        cls.dealer_password = cls.config_read.dealer_password()
        cls.login = Admin_Portal(cls.driver)
        cls.driver.get(cls.url)
        cls.login.login(cls.dealer_username,cls.dealer_password)
        cls.driver.implicitly_wait(5)
        cls.insulated_door = Dealer_Insulated_Door(cls.driver)
        cls.insulated_door.creat_quote()
        cls.insulated_door.go_insulated_door()
        sleep(3)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_insulated_door_ui_001(self):
        '''Verify the main elements in the page, should including correct title, Add button and Close button '''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Standard Door Details','Add'),self.check_door_page)

    def test_insulated_door_ui_002(self):
            '''Verify each element for install details '''
            self.driver.implicitly_wait(2)
            self.assertEqual(('Door Type', 'Design','Colour Category','Door Colour','Door Finish',
                              'Custom Colour'), self.check_install_details)

    def test_insulated_door_ui_003(self):
        '''Verify if the Door type dropdown is disabled '''
        self.driver.implicitly_wait(2)
        self.assertFalse( self.check_door_type)

    def test_insulated_door_ui_004(self):
            '''Verify the default value of the Door type dropdown'''
            self.driver.implicitly_wait(2)
            self.assertEqual(('Insulated Sectional'), self.check_default_door_type)

    def test_insulated_door_ui_005(self):
            '''Verify the values in the Design dropdown'''
            self.driver.implicitly_wait(2)
            self.assertEqual(('Please Select\nRibline\nFineline\nFlatline\nStanford'), self.check_design)

    def test_insulated_door_ui_006(self):
            '''Verify the values in the Colour Category dropdown'''
            self.driver.implicitly_wait(2)
            self.assertEqual(('Please Select\nColorBond\nColourbond Non Std\nCustom\nMetalFx'), self.check_colour_category)

    def test_insulated_door_ui_007(self):
            '''Verify the Door Colour dropdown for ColorBond Category'''
            self.driver.implicitly_wait(2)
            self.assertEqual(('Please Select\nBasalt\nBlue Gum\nClassic Cream\nCove\nDover White\nDune\nEvening Haze\n'
                              'Gully\nIronstone\nJasper\nManor Red\nMonument\nNight Sky\nPaperbark\nShale Grey\nSoutherly\n'
                              'Surfmist\nWallaby\nWindspray\nWoodland Grey'), self.check_colour_colorbond)

    def test_insulated_door_ui_008(self):
        '''Verify the Door Colour dropdown status for Custom Category '''
        self.driver.implicitly_wait(2)
        self.assertTrue( self.check_colour_custom)

    def test_insulated_door_ui_009(self):
        '''Verify the Door Colour dropdown for Metalfx Category'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Please Select\nDeep Bronze\nNew Copper\nPrecious Silver Pearl'), self.check_colour_metalfx)

    def test_insulated_door_ui_010(self):
        '''Verify the Door Colour dropdown for Paintedfinish Category'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Please Select\nCottage Green\nDeep Ocean\nMangrove\nMonument Matt\nPale Eucalypt\nTerrain'),
                         self.check_colour_paintedfinish)

    def test_insulated_door_ui_011(self):
        '''Verify the Custom Colour input box should be disable by default '''
        self.driver.implicitly_wait(2)
        self.assertTrue( self.check_customcolour_box)

    def test_insulated_door_ui_012(self):
        '''Verify  each element for size details '''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Door Size LH','Door Size RH','Door Size Width','LHRK (Required if HR is 200-269mm)',
                          'Taper (Max taper 250mm)','Seals 2500mm (QTY)','Seals 3000mm (QTY)'),self.check_size_details)

    def test_insulated_door_ui_013(self):
            '''Verify the default value for Door Size LH'''
            self.driver.implicitly_wait(2)
            self.assertEqual(('0'), self.check_lh_default)

    def test_insulated_door_ui_014(self):
            '''Verify the default value for Door Size RH'''
            self.driver.implicitly_wait(2)
            self.assertEqual(('0'), self.check_rh_default)

    def test_insulated_door_ui_015(self):
            '''Verify the default value for Door Size Width'''
            self.driver.implicitly_wait(2)
            self.assertEqual(('0'), self.check_width_default)

    def test_insulated_door_ui_016(self):
        '''Verify the LHRK dropdown list'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Please Select\nFMLHR'), self.check_lhrk_list)

    def test_insulated_door_ui_017(self):
        '''Verify the Tape dropdown list'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Please Select\nFixed'), self.check_taper_list)

    def test_insulated_door_ui_018(self):
        '''Verify the Dealer Seals dropdown list'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Please Select\n2500mm\n3000mm'), self.check_seals_list)

    def test_insulated_door_ui_018(self):
            '''Verify the default value for Seals 2500mm Quantity'''
            self.driver.implicitly_wait(2)
            self.assertEqual(('0'), self.check_quantity_2500)

    def test_insulated_door_ui_019(self):
        '''Verify the default value for Seals 3000mm Quantity'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('0'), self.check_quantity_3000)

    def test_insulated_door_ui_020(self):
        '''Verify each element for all checkboxes'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Emergency Key Release','Reverse Colour','Battery Backup','Eco Smart WiFi',
                          'SwiFit SMS Bracket (Side Mount Spring)','LSR Kit\n(Low Side Room)'),self.check_checkboxes_details)

    def test_insulated_door_ui_021(self):
        '''Verify the reverse colour box status, should be disabled by default'''
        self.driver.implicitly_wait(2)
        self.assertFalse( self.check_reverse_colour_status)

    def test_insulated_door_ui_022(self):
        '''Verify the Emergency Key Release box status, should be enabled by default'''
        self.driver.implicitly_wait(2)
        self.assertTrue( self.check_emergency_key_status)

    def test_insulated_door_ui_023(self):
        '''Verify the Battery Backup box status, should be enabled by default'''
        self.driver.implicitly_wait(2)
        self.assertTrue( self.check_battery_backup_status)

    def test_insulated_door_ui_024(self):
        '''Verify the ECO Smart wifi box status, should be enabled by default'''
        self.driver.implicitly_wait(2)
        self.assertTrue( self.check_smart_wifi_status)

    def test_insulated_door_ui_025(self):
        '''Verify the SwiFit SMS Bracket box status, should be enabled by default'''
        self.driver.implicitly_wait(2)
        self.assertTrue( self.check_swifit_sms_status)

    def test_insulated_door_ui_026(self):
        '''Verify the LSR Kit box status, should be enabled by default'''
        self.driver.implicitly_wait(2)
        self.assertTrue( self.check_lsr_kit_status)

    def test_insulated_door_ui_027(self):
        '''Verify each element for Opener'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Opener','No of Handsets','Wall Button','PE Beam','No. of PE Beam Sets',
                          'Digital Keypad'),self.check_opener_details)

    def test_insulated_door_ui_028(self):
        '''Verify the Dealer Seals dropdown list'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Additional Door Information'), self.check_additional_details)

    def test_insulated_door_ui_029(self):
        '''Verify each element for Extras'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Window Type','No. of Windows','Window Colour'), self.check_extras_details)

    def test_insulated_door_ui_030(self):
        '''Verify the windows type dropdown list'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Please Select\nColonial\nPlain - Stanford\nPort Hole\nSunrise'),self.check_windows_type)

    def test_insulated_door_ui_031(self):
        '''Verify the windows colour dropdown list'''
        self.driver.implicitly_wait(2)
        self.assertIn(('3mm Acrylic 000 – CLEAR'), self.check_windows_colour)

    def test_insulated_door_ui_033(self):
        '''Verify the Tape dropdown list'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Please Select\nEco HD Light Commercial SDO Belt\nEco HD Light Commercial SDO Chain\n'
                          'ECO1000N Belt Drive\nECO1000N Chain Drive\nManual/No Opener or Lock'), self.check_opener_list)

if __name__ == '__main__':
    unittest.main(verbosity=2)