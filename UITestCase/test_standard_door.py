# Author:Yi Sun(Tim) 2025-08-12

'''Test Add Standard Door Page'''

import time
import unittest
from selenium import webdriver
from time import *
from UIModule.standard_door import *
from CommonModule.read_config import *


class Add_StandardDoor_UI_Test(unittest.TestCase,Standard_Door):
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
        cls.goaddquote = Add_Quote(cls.driver)
        cls.goaddquote.go_addquote()
        cls.gostandarddoor = Standard_Door(cls.driver)
        cls.gostandarddoor.go_addstandarddoor()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_add_standarddoor_ui_001(self):
        '''Verify the main elements in the page, should including correct title, Add button and Close button '''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Standard Door Details', 'Add'), self.check_door_page)

    def test_add_standarddoor_ui_002(self):
        '''Verify each element for install details '''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Install Type', 'Door Type', 'Design', 'Colour Category', 'Door Colour', 'Door Finish',
                          'Custom Colour', 'Technician Measure', 'Measure Required'), self.check_install_details)

    def test_add_standarddoor_ui_003(self):
        '''Verify the Install Type dropdown list'''
        self.driver.implicitly_wait(2)
        self.assertIn(('Commercial Cat 1\nCommercial Cat 2\nCommercial STD\nFull Panel Replacement\nPanel Replacement\n'
                       'Residential'), self.check_install_type)

    def test_add_standarddoor_ui_004(self):
        '''Verify the Door Type dropdown list '''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Please Select\nExoRoll\nInsulated Sectional\nOptiLift\nOptiRoll\nPanel Lift-Safe'),
                         self.check_door_type)

    def test_add_standarddoor_ui_005(self):
            '''Verify the Colour Category dropdown list'''
            self.driver.implicitly_wait(2)
            self.assertIn(('ColorBond\nColourbond Non Std\nCustom\nFlexigraphic\nFlexographic\nMetalFx\nOilColor\n'
                           'Painted Finish\nPortabella\nPowderCoatStandard\nPowderCoatUpgrade\nSealedColor\n'
                           'Timber Essence\nTimberFX'),self.check_colour_category)

    def test_add_standarddoor_ui_006(self):
            '''Verify the Design dropdown for Panel Lift-Safe Door'''
            self.driver.implicitly_wait(2)
            self.assertIn(('Slimline\nClassic panel\nLincoln panel\nUltraline\nWideline'),self.check_design_panel)

    def test_add_standarddoor_ui_007(self):
        '''Verify the Design dropdown for Insulated Sectional Door '''
        self.driver.implicitly_wait(2)
        self.assertIn(('Ribline\nFineline\nFlatline\nStanford'), self.check_design_insulated)

    def test_add_standarddoor_ui_008(self):
            '''Verify the Design dropdown for Roller Door'''
            self.driver.implicitly_wait(2)
            self.assertIn(('ExoRoll eS\nExoRoll eD\nExoRoll eC'), self.check_design_roller)

    def test_add_standarddoor_ui_009(self):
            '''Verify the Design dropdown for OptiLift Door'''
            self.driver.implicitly_wait(2)
            self.assertEqual(('Please Select\nLinea\nTraditional\nEstate\nContempo\nRiviera'), self.check_design_optilift)

    def test_add_standarddoor_ui_010(self):
            '''Verify the Design dropdown for OptiRoll Door'''
            self.driver.implicitly_wait(2)
            self.assertEqual(('Please Select\nOptiRoll eS\nOptiRoll eD\nOptiRoll eC'), self.check_design_optiroll)

    def test_add_standarddoor_ui_011(self):
        '''Verify the Door Colour dropdown for ColorBond Category'''
        self.driver.implicitly_wait(2)
        self.assertIn(('Basalt\nBlue Gum\nClassic Cream\nCove\nDover White\nDune\nEvening Haze\nGully\nIronstone\n'
                       'Jasper\nManor Red\nMonument\nNight Sky\nPaperbark\nShale Grey\nSoutherly\nSurfmist\nTBA\n'
                       'Wallaby\nWindspray\nWoodland Grey'),self.check_colour_colorbond)

    def test_add_standarddoor_ui_012(self):
            '''Verify the Door Colour dropdown for Custom Category, should be disabled'''
            self.driver.implicitly_wait(2)
            self.assertEqual(True, self.check_colour_custom)

    def test_add_standarddoor_ui_013(self):
            '''Verify the Door Colour dropdown for Flexigraphic Category'''
            self.driver.implicitly_wait(2)
            self.assertIn(('Caoba Dawn\nClassic Cedar\nTBA'), self.check_colour_flexigraphic)

    def test_add_standarddoor_ui_014(self):
            '''Verify the Door Colour dropdown for Flexographic Category'''
            self.driver.implicitly_wait(2)
            self.assertIn(('Caoba Dawn\nClassic Cedar\nTBA'), self.check_colour_flexographic)

    def test_add_standarddoor_ui_015(self):
            '''Verify the Door Colour dropdown for MetalFx Category'''
            self.driver.implicitly_wait(2)
            self.assertIn(('Deep Bronze\nNew Copper\nPrecious Silver Pearl\nTBA'), self.check_colour_metalfx)

    def test_add_standarddoor_ui_016(self):
            '''Verify the Door Colour dropdown for PaintedFinish Category '''
            self.driver.implicitly_wait(2)
            self.assertIn(('Cottage Green\nCove\nDeep Ocean\nGully\nMangrove\nManor Red\nMonument Matt\nPale Eucalypt\n'
                           'Terrain'),self.check_colour_paintedfinish)

    def test_add_standarddoor_ui_017(self):
        '''Verify the Door Colour dropdown for Portabella Category '''
        self.driver.implicitly_wait(2)
        self.assertIn(('African Ebony\nEuropean Oak\nGolden Oak\nGrey Ironbark\nKnotted Walnut\nRed Gum\nTBA'),
                      self.check_colour_portabella)

    def test_add_standarddoor_ui_018(self):
            '''Verify the Door Colour dropdown for TimberFX Category '''
            self.driver.implicitly_wait(2)
            self.assertIn(('Cedar\nJarrah\nTBA\nWalnut'), self.check_colour_timberfx)

    def test_add_standarddoor_ui_019(self):
            '''Verify the Custom Colour input box, should be Disabled by default'''
            self.driver.implicitly_wait(2)
            self.assertEqual(True, self.check_customcolour_box)

    def test_add_standarddoor_ui_020(self):
            '''Verify the Custom Colour input box, should be Enabled for Custom Colour Category'''
            self.driver.implicitly_wait(2)
            self.assertEqual(True, self.check_customcolourbox_custom)

    def test_add_standarddoor_ui_021(self):
        '''Verify each element for size details'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Opening Size LH', 'Opening Size RH', 'Opening Size Width', 'SR Left', 'HR', 'SR Right',
                          'LHRK (Required if HR is 200-269mm)'), self.check_size_details)

    def test_add_standarddoor_ui_022(self):
            '''Verify the default value for Opening Size LH, should be "0" '''
            self.driver.implicitly_wait(2)
            self.assertEqual(('0'), self.check_openinglh_default)

    def test_add_standarddoor_ui_023(self):
            '''Verify the default value for Opening Size RH, should be "0" '''
            self.driver.implicitly_wait(2)
            self.assertEqual(('0'), self.check_openingrh_default)

    def test_add_standarddoor_ui_024(self):
            '''Verify the default value for Opening Size Width, should be "0" '''
            self.driver.implicitly_wait(2)
            self.assertEqual(('0'), self.check_openingwidth_default)

    def test_add_standarddoor_ui_025(self):
            '''Verify the default value for SR Left, should be "0" '''
            self.driver.implicitly_wait(2)
            self.assertEqual(('0'), self.check_srleft_default)

    def test_add_standarddoor_ui_026(self):
            '''Verify the default value for HR, should be "0" '''
            self.driver.implicitly_wait(2)
            self.assertEqual(('0'), self.check_hr_default)
    def test_add_standarddoor_ui_027(self):
            '''Verify the default value for SR Right, should be "0" '''
            self.driver.implicitly_wait(2)
            self.assertEqual(('0'), self.check_srright_default)

    def test_add_standarddoor_ui_028(self):
            '''Verify the LHRK dropdown, should including "FMLHR","High Lift" and "Verticle Lift" '''
            self.driver.implicitly_wait(2)
            self.assertIn(('FMLHR\nHigh Lift\nVerticle Lift'), self.check_lhrk_list)

    def test_add_standarddoor_ui_029(self):
        '''Verify each element for Timer/Taper/AdditionalFab details'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Timber Packers', 'Taper (Max taper 250mm)', 'Additional Fabrication',
                          'Additional Fabrication Required', 'Shop Drawings', 'Lifting/Access Equipment'),
                         self.check_timber_details)

    def test_add_standarddoor_ui_030(self):
        '''Verify each element for all checkboxes '''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Induction Loop',  'Fully Slotted', 'Emergency Key Release',
                          'Reverse Colour', 'Battery Backup','Eco Smart WiFi'), self.check_checkboxes_details)

    def test_add_standarddoor_ui_031(self):
        '''Verify each element for Opener '''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Opener', 'No of Handsets', 'Wall Button', 'Opener Details', 'Digital Keypad',
                          'Internal Push Button','PE Beam','No. of PE Beam Sets'), self.check_opener_details)

    def test_add_standarddoor_ui_032(self):
            '''Verify each element for other elements'''
            self.driver.implicitly_wait(2)
            self.assertEqual(('Weight Being Added', 'Seals', 'Seals 2500mm (QTY)','Seals 3000mm (QTY)','Hang Door From',
                              'Lintel Type', 'Fixing Type','IBeam Noggins', 'Remove and Dispose', 'Job Status',
                              'Expected Delivery Date','Cut Date','Paint Date','QC Date','Other Date'), self.check_other_details)

    def test_add_standarddoor_ui_033(self):
        '''Verify each element for Aditional Infomation'''
        self.driver.implicitly_wait(2)
        self.assertEqual(('Additional Door Information', 'Production Notes   (0 / 50)'),
                         self.check_additional_details)

    def test_add_standarddoor_ui_034(self):
        '''Verify the default options in Door Finish dropdown '''
        self.driver.implicitly_wait(3)
        self.assertEqual(('Please Select\nSmooth Texture\nTextured\nWoodgrain Texture'), self.check_default_doorfinish)

    def test_add_standarddoor_ui_035(self):
            '''Verify the Door finish option for Classic door '''
            self.driver.implicitly_wait(3)
            self.assertEqual(('Please Select\nWoodgrain Texture'),self.check_classic_doorfinish)

    def test_add_standarddoor_ui_036(self):
        '''Verify the Door finish option for Slimline door '''
        self.driver.implicitly_wait(3)
        self.assertEqual(('Please Select\nSmooth Texture\nTextured\nWoodgrain Texture'), self.check_slimline_doorfinish)

    def test_add_standarddoor_ui_037(self):
            '''Verify the Door finish option for Lincoln door '''
            self.driver.implicitly_wait(3)
            self.assertEqual(('Please Select\nWoodgrain Texture'),self.check_lincoln_doorfinish)

    def test_add_standarddoor_ui_038(self):
            '''Verify the Door finish option for Ultraline door '''
            self.driver.implicitly_wait(3)
            self.assertEqual(('Please Select\nWoodgrain Texture'),self.check_ultraline_doorfinish)

    def test_add_standarddoor_ui_039(self):
        '''Verify the Door finish option for Wideline door '''
        self.driver.implicitly_wait(3)
        self.assertEqual(('Please Select\nSmooth Texture\nWoodgrain Texture'), self.check_wideline_doorfinish)

    def test_add_standarddoor_ui_040(self):
        '''Verify the reverse colour box status for Panel Lift door, should be disabled'''
        self.driver.implicitly_wait(3)
        self.assertTrue(self.reverse_colour_panel)

    def test_add_standarddoor_ui_041(self):
        '''Verify the Fully Slotted box status for Panel Lift door, should be disabled'''
        self.driver.implicitly_wait(3)
        self.assertTrue(self.fully_slotted_panel)

    def test_add_standarddoor_ui_042(self):
        '''Verify the Induction Loop box status for Panel Lift door, should be enabled'''
        self.driver.implicitly_wait(3)
        self.assertTrue(self.induction_loop_panel)

    def test_add_standarddoor_ui_043(self):
        '''Verify the Emergency Key Release box status for Panel Lift door, should be enabled'''
        self.driver.implicitly_wait(3)
        self.assertTrue(self.emergency_key_panel)

    def test_add_standarddoor_ui_044(self):
        '''Verify the ECO Smart wifi box status for Panel Lift door, should be enabled'''
        self.driver.implicitly_wait(3)
        self.assertTrue(self.smart_wifi_panel)

    def test_add_standarddoor_ui_045(self):
        '''Verify the Battery Backup box status for Panel Lift door, should be enabled'''
        self.driver.implicitly_wait(3)
        self.assertTrue(self.battery_backup_panel)

    def test_add_standarddoor_ui_046(self):
        '''Verify the reverse colour box status for Roller door, should be enabled'''
        self.driver.implicitly_wait(3)
        self.assertTrue(self.reverse_colour_roller)

    def test_add_standarddoor_ui_047(self):
        '''Verify the Fully Slotted box status for Roller door, should be disabled'''
        self.driver.implicitly_wait(3)
        self.assertTrue(self.fully_slotted_roller)

    def test_add_standarddoor_ui_048(self):
        '''Verify the reverse colour box status for Insulated Sectional door, should be disabled'''
        self.driver.implicitly_wait(3)
        self.assertTrue(self.reverse_colour_insulated)

    def test_add_standarddoor_ui_049(self):
        '''Verify the Fully Slotted box status for Insulated Sectional door, should be disabled'''
        self.driver.implicitly_wait(3)
        self.assertTrue(self.fully_slotted_insulated)

if __name__ == "__main__":
    unittest.main(verbosity=2)

