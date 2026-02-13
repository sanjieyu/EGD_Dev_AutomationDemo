# Author:Yi Sun(Tim) 2024-10-18

'''Add a Dealer Panel Lift Door Details Page'''

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from pages.add_dealer_quote import *

class Dealer_Panel_Door(Add_Dealer_Quote):

    details_title_loc  = (By.NAME,'details')
    add_paneldoor_btn_loc = (By.ID,'btnDoorAdd')
    close_paneldoor_btn_loc = (By.ID,'btnDoorClose')
    door_details_page_loc = (By.ID, 'standardDoorForm')

    '''loc for each element for install details'''
    door_type_loc = (By.CSS_SELECTOR,"label[for='DoorType']")
    design_loc = (By.CSS_SELECTOR,"label[for='Design']")
    colour_category_loc = (By.CSS_SELECTOR,"label[for='ColourCate']")
    door_colour_loc = (By.CSS_SELECTOR,"label[for='DoorColour']")
    door_finish_loc = (By.CSS_SELECTOR,"label[for='DoorFinish']")
    custom_colour_loc = (By.CSS_SELECTOR,"label[for='CustomColour']")
    door_type_box_loc = (By.ID,'DoorType')
    design_select_loc = (By.ID,'Door_Design')
    colour_category_select_loc = (By.ID,'Door_Color_Category')
    door_colour_select_loc = (By.ID,'DoorColor')
    door_finish_select_loc = (By.ID,'DoorFinish')
    custom_colour_box_loc = (By.ID,'Door_Custom_Color')


    '''loc for each element for SIZE details'''
    size_lh_loc = (By.CSS_SELECTOR,"label[for='SizeLh']")
    size_lh_box_loc = (By.ID,'OpeningSizeLH')
    size_rh_loc = (By.CSS_SELECTOR,"label[for='SizeRh']")
    size_rh_box_loc = (By.ID,'OpeningSizeRH')
    size_width_loc = (By.CSS_SELECTOR,"label[for='SizeWidth']")
    size_width_box_loc = (By.ID,'OpeningSizeWidth')
    lhrk_loc = (By.CSS_SELECTOR,"label[for='LHRK']")
    lhrk_select_loc = (By.ID,'LHRK')
    taper_loc = (By.CSS_SELECTOR,"label[for='Taper']")
    taper_select_loc = (By.ID,'Taper')
    seals_2500_loc = (By.CSS_SELECTOR,"label[for='Seals2500']")
    dealer_seals_select_loc = (By.ID,'DealerSeals')
    seals_3000_loc = (By.CSS_SELECTOR,"label[for='Seals3000']")
    seals_quantity_select_loc = (By.ID,'DealerSealsQuantity')
    seals_quantity_2500_loc = (By.ID,'DealerSeals2500mmQuantity')
    seals_quantity_3000_loc = (By.ID, 'DealerSeals3000mmQuantity')

    '''loc for each element for checkboxes details'''
    emergency_key_loc = (By.CSS_SELECTOR,"label[for='EmergencyKey']")
    emergency_box_loc = (By.ID,'PriceEmergencyKeyRelease')
    reverse_colour_loc = (By.CSS_SELECTOR,"label[for='ReverseColour']")
    reverse_box_loc = (By.ID,'IsReverseColourStandard')
    battery_backup_loc = (By.CSS_SELECTOR,"label[for='Battery']")
    battery_box_loc = (By.ID,'IsBatteryBackupStandard')
    eco_wifi_loc = (By.CSS_SELECTOR,"label[for='EcoWIFI']")
    eco_wifi_box_loc = (By.ID,'IsWiFi')
    swifit_sms_loc = (By.CSS_SELECTOR,"label[for='SwiftSMS']")
    swifit_sms_box_loc = (By.ID,'IsSwiFitSMSBracket')
    lsr_kit_loc = (By.CSS_SELECTOR,"label[for='LsrKit']")
    lsr_kit_box_loc = (By.ID,'IsLSRKit')

    '''loc for Opener details'''
    opener_loc = (By.CSS_SELECTOR,"label[for='Opener']")
    opener_select_loc = (By.ID,'Motors')
    handsets_loc = (By.CSS_SELECTOR,"label[for='Handsets']")
    wall_button_loc = (By.CSS_SELECTOR,"label[for='Wallbtn']")
    pe_beam_loc = (By.CSS_SELECTOR,"label[for='PeBeam']")
    beam_sets_loc = (By.CSS_SELECTOR,"label[for='BeamSets']")
    keypad_loc = (By.CSS_SELECTOR,"label[for='KeyPad']")

    '''loc for additional infomation details '''
    additional_info_loc = (By.CSS_SELECTOR,"label[for='AdditionalInfo']")
    additional_info_box_loc = (By.ID,'AdditionalInfo')

    '''loc for Extra'''
    extras_loc = (By.CSS_SELECTOR,"label[for='Extras']")

    '''loc for each element in Extra'''
    windows_type_loc = (By.CSS_SELECTOR,"label[for='WindowsType']")
    windows_type_select_loc = (By.ID,'WindowType')
    no_windows_loc = (By.CSS_SELECTOR,"label[for='NoWindows']")
    no_windows_box_loc = (By.ID,'Windows')
    windows_colour_loc = (By.CSS_SELECTOR,"label[for='WindowsColour']")
    windows_colour_btn_loc = (By.ID,"btnWindowsColour")
    windows_colour_dropdown_loc = (By.XPATH,'//*[@id="ui-id-1"]')

    def go_panel_door(self):
        '''Open the Add Panel Door from Dealer Quote Page'''
        self.driver.find_element(*self.panel_btn_loc).click()
        sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[-1])   # switch to the add door details page

    @property
    def check_door_page(self):
        '''check the main elements in the page'''
        form_element = self.driver.find_element(*self.door_details_page_loc)
        panel_detail_title = self.driver.find_element(*self.details_title_loc).text
        self.driver.execute_script("arguments[0].scrollIntoView(false);", form_element)
        add_button = self.driver.find_element(*self.add_paneldoor_btn_loc).text
        print(panel_detail_title,add_button)
        return panel_detail_title,add_button

    @property
    def check_install_details(self):
        '''check each element for install details'''
        door_type = self.driver.find_element(*self.door_type_loc).text
        design = self.driver.find_element(*self.design_loc).text
        colour_category = self.driver.find_element(*self.colour_category_loc).text
        door_colour = self.driver.find_element(*self.door_colour_loc).text
        door_finish = self.driver.find_element(*self.door_finish_loc).text
        custom_colour = self.driver.find_element(*self.custom_colour_loc).text
        print(door_type,design,colour_category,door_colour,door_finish,custom_colour)
        return  door_type,design,colour_category,door_colour,door_finish,custom_colour


    @property
    def check_door_type(self):
        '''check if the Door type dropdown is disabled'''
        door_type_select = self.driver.find_element(*self.door_type_box_loc)
        if door_type_select.is_enabled():
            print("it's enabled")
            return  True
        else:
            print("it's disabled")
            return False

    @property
    def check_default_door_type(self):
        '''check the default value of the Door type dropdown'''
        door_type_list = self.driver.find_element(*self.door_type_box_loc)
        default_value = door_type_list.get_attribute("value")
        selected_option_text = door_type_list.find_element("xpath", f"//option[@value='{default_value}']").text
        print(selected_option_text)
        return  selected_option_text

    @property
    def check_design(self):
        '''check the Design dropdown'''
        self.driver.find_element(*self.design_select_loc).click()
        design_select_list = self.driver.find_element(*self.design_select_loc).text
        print(design_select_list)
        return  design_select_list

    @property
    def check_colour_category(self):
        '''check the Colour Category dropdown'''
        self.driver.find_element(*self.colour_category_select_loc).click()
        colour_category_list = self.driver.find_element(*self.colour_category_select_loc).text
        print(colour_category_list)
        return  colour_category_list

    @property
    def check_colour_colorbond(self):
        '''check the Door Colour dropdown for ColorBond Category'''
        global colour_category
        colour_category = Select(self.driver.find_element(*self.colour_category_select_loc))
        colorbond = colour_category.select_by_visible_text('ColorBond')
        self.driver.find_element(*self.door_colour_select_loc).click()
        sleep(1)
        door_colour_list = self.driver.find_element(*self.door_colour_select_loc).text
        # print(door_colour_list)
        return  door_colour_list

    @property
    def check_colour_custom(self):
        '''check the Door Colour dropdown for Custom Category'''
        # colour_category = Select(self.driver.find_element(*self.colour_category_select))
        custom = colour_category.select_by_visible_text('Custom')
        custom_colour = self.driver.find_element(*self.door_colour_select_loc)
        if custom_colour.is_enabled():
            print('wrong')
            return  False
        else:
            print('correct,it is disalbed')
            return True

    @property
    def check_colour_flexographic(self):
        '''check the Door Colour dropdown for Flexigraphic Category'''
        # colour_category = Select(self.driver.find_element(*self.colour_category_select))
        flexigraphic = colour_category.select_by_visible_text('Flexographic')
        self.driver.find_element(*self.door_colour_select_loc).click()
        door_colour_list = self.driver.find_element(*self.door_colour_select_loc).text
        # print(door_colour_list)
        return  door_colour_list

    @property
    def check_colour_metalfx(self):
        '''check the Door Colour dropdown for MetalFx Category'''
        # colour_category = Select(self.driver.find_element(*self.colour_category_select))
        metalfx = colour_category.select_by_visible_text('MetalFx')
        self.driver.find_element(*self.door_colour_select_loc).click()
        door_colour_list = self.driver.find_element(*self.door_colour_select_loc).text
        print(door_colour_list)
        return  door_colour_list

    @property
    def check_colour_paintedfinish(self):
        '''check the Door Colour dropdown for PaintedFinish Category'''
        # colour_category = Select(self.driver.find_element(*self.colour_category_select_loc))
        paintedfinish = colour_category.select_by_visible_text('Painted Finish')
        self.driver.find_element(*self.door_colour_select_loc).click()
        sleep(1)
        door_colour_list = self.driver.find_element(*self.door_colour_select_loc).text
        print(door_colour_list)
        return  door_colour_list

    @property
    def check_colour_portabella(self):
        '''check the Door Colour dropdown for Portabella Category'''
        # colour_category = Select(self.driver.find_element(*self.colour_category_select))
        portabella = colour_category.select_by_visible_text('Portabella')
        self.driver.find_element(*self.door_colour_select_loc).click()
        door_colour_list = self.driver.find_element(*self.door_colour_select_loc).text
        print(door_colour_list)
        return  door_colour_list

    @property
    def check_colour_timberfx(self):
        '''check the Door Colour dropdown for TimberFX Category'''
        # colour_category = Select(self.driver.find_element(*self.colour_category_select))
        timberfx = colour_category.select_by_visible_text('TimberFX')
        self.driver.find_element(*self.door_colour_select_loc).click()
        sleep(1)
        door_colour_list = self.driver.find_element(*self.door_colour_select_loc).text
        print(door_colour_list)
        return  door_colour_list

    @property
    def check_customcolour_box(self):
        '''check the Custom Colour input box should be disable by default'''
        custom_colour_box = self.driver.find_element(*self.custom_colour_box_loc)
        if custom_colour_box.is_enabled():
            print('wrong')
            return  False
        else:
            print('correct')
            return True

    @property
    def check_customcolourbox_custom(self):
            '''check the Custom Colour input box should be enable for Custom Colour Category'''
            colour_category1 = Select(self.driver.find_element(*self.colour_category_select_loc))
            custom = colour_category1.select_by_visible_text('Custom')
            custom_colour_box = self.driver.find_element(*self.custom_colour_box_loc)
            if custom_colour_box.is_enabled():  # 判断input box是可输入的
                print('correct')
                return True
            else:
                print('wrong')
                return False

    @property
    def check_size_details(self):
        '''check each element for size details'''
        size_lh = self.driver.find_element(*self.size_lh_loc).text
        size_rh = self.driver.find_element(*self.size_rh_loc).text
        size_width = self.driver.find_element(*self.size_width_loc).text
        lhrk = self.driver.find_element(*self.lhrk_loc).text
        tape = self.driver.find_element(*self.taper_loc).text
        seals_2500 = self.driver.find_element(*self.seals_2500_loc).text
        seals_3000 = self.driver.find_element(*self.seals_3000_loc).text
        print(size_lh,size_rh,size_width,lhrk,tape,seals_2500,seals_3000)
        return  size_lh,size_rh,size_width,lhrk,tape,seals_2500,seals_3000

    @property
    def check_lh_default(self):
        '''check the default value for Door Size LH'''
        lh_default = self.driver.find_element(*self.size_rh_box_loc).get_attribute('value')
        print(lh_default)
        return  lh_default

    @property
    def check_rh_default(self):
        '''check the default value for Door Size RH'''
        rh_default = self.driver.find_element(*self.size_rh_box_loc).get_attribute('value')
        print(rh_default)
        return  rh_default

    @property
    def check_width_default(self):
        '''check the default value for Door Size Width'''
        width_default = self.driver.find_element(*self.size_width_box_loc).get_attribute('value')
        print(width_default)
        return  width_default

    @property
    def check_lhrk_list(self):
        '''check the LHRK dropdown list'''
        self.driver.find_element(*self.lhrk_select_loc).click()
        sleep(1)
        lhrk_list = self.driver.find_element(*self.lhrk_select_loc).text
        print(lhrk_list)
        return  lhrk_list

    @property
    def check_taper_list(self):
        '''check the Taper dropdown list'''
        self.driver.find_element(*self.taper_select_loc).click()
        sleep(1)
        tape_list = self.driver.find_element(*self.taper_select_loc).text
        print(tape_list)
        return  tape_list

    @property
    def check_seals_list(self):
        '''check the Dealer Seals dropdown list'''
        self.driver.find_element(*self.dealer_seals_select_loc).click()
        sleep(1)
        seals_list = self.driver.find_element(*self.dealer_seals_select_loc).text
        print(seals_list)
        return  seals_list

    @property
    def check_quantity_2500(self):
        '''check the default value for Dealer Seals 2500mm Quantity'''
        quantity_2500 = self.driver.find_element(*self.seals_quantity_2500_loc).get_attribute('value')
        print(quantity_2500)
        return  quantity_2500

    @property
    def check_quantity_3000(self):
        '''check the default value for Dealer Seals 3000mm Quantity'''
        quantity_3000 = self.driver.find_element(*self.seals_quantity_3000_loc).get_attribute('value')
        print(quantity_3000)
        return  quantity_3000


    @property
    def check_quantity_default(self):
        '''check the default value for Dealer Seals Quantity'''
        quantity_default = self.driver.find_element(*self.seals_quantity_select_loc).get_attribute('value')
        print(quantity_default)
        return  quantity_default

    @property
    def check_checkboxes_details(self):
        '''check each element for all checkboxes'''
        emergency_key = self.driver.find_element(*self.emergency_key_loc).text
        reverse_colour = self.driver.find_element(*self.reverse_colour_loc).text
        battery_backup = self.driver.find_element(*self.battery_backup_loc).text
        eco_wifi = self.driver.find_element(*self.eco_wifi_loc).text
        swifit_sms = self.driver.find_element(*self.swifit_sms_loc).text
        lsr_kit = self.driver.find_element(*self.lsr_kit_loc).text
        print(emergency_key,reverse_colour,battery_backup,eco_wifi,swifit_sms,lsr_kit)
        return  emergency_key,reverse_colour,battery_backup,eco_wifi,swifit_sms,lsr_kit

    @property
    def check_reverse_colour_status(self):
        '''check the reverse colour box status, should be disabled by default'''
        reverse_colour_box = self.driver.find_element(*self.reverse_box_loc)
        if reverse_colour_box.is_enabled():
            print("it's enabled, wrong")
            return False
        else:
            print("it's disabled, correct")
            return True

    @property
    def check_emergency_key_status(self):
        '''check the Emergency Key Release box status, should be enabled by default'''
        emergency_key = self.driver.find_element(*self.emergency_box_loc)
        if emergency_key.is_enabled():
            print("it's enabled, correct")
            return True
        else:
            print("it's disabled, wrong")
            return False

    @property
    def check_battery_backup_status(self):
        '''check the Battery Backup box status, should be enabled by default'''
        battery_backup = self.driver.find_element(*self.battery_box_loc)
        if battery_backup.is_enabled():
            print("it's enabled, correct")
            return True
        else:
            print("it's disabled, wrong")
            return False

    @property
    def check_smart_wifi_status(self):
        '''check the ECO Smart wifi box status, should be enabled by default'''
        smart_wifi = self.driver.find_element(*self.eco_wifi_box_loc)
        if smart_wifi.is_enabled():
            print("it's enabled, correct")
            return True
        else:
            print("it's disabled, wrong")
            return False

    @property
    def check_swifit_sms_status(self):
        '''check the Swifit SMS Bracket box status, should be enabled by default'''
        swifit_sms = self.driver.find_element(*self.swifit_sms_box_loc)
        if swifit_sms.is_enabled():
            print("it's enabled, correct")
            return True
        else:
            print("it's disabled, wrong")
            return False

    @property
    def check_lsr_kit_status(self):
        '''check the LSR Kit box status, should be enabled by default'''
        lsr_kit = self.driver.find_element(*self.lsr_kit_box_loc)
        if lsr_kit.is_enabled():
            print("it's enabled, correct")
            return True
        else:
            print("it's disabled, wrong")
            return False

    @property
    def check_opener_details(self):
        '''check each element for Opener'''
        opener = self.driver.find_element(*self.opener_loc).text
        handsets_no  = self.driver.find_element(*self.handsets_loc).text
        wall_btn = self.driver.find_element(*self.wall_button_loc).text
        pe_beam = self.driver.find_element(*self.pe_beam_loc).text
        pe_beam_sets = self.driver.find_element(*self.beam_sets_loc).text
        keypad = self.driver.find_element(*self.keypad_loc).text
        print(opener,handsets_no,wall_btn,pe_beam,pe_beam_sets,keypad)
        return  opener,handsets_no,wall_btn,pe_beam,pe_beam_sets,keypad

    @property
    def check_additional_details(self):
        '''check each element for additional door information'''
        additional_info  = self.driver.find_element(*self.additional_info_loc).text
        print(additional_info)
        return  additional_info

    @property
    def check_extras_details(self):
        '''check each element for Extras'''
        self.driver.find_element(*self.extras_loc).click()
        sleep(1)
        windows_type = self.driver.find_element(*self.windows_type_loc).text
        no_widnows = self.driver.find_element(*self.no_windows_loc).text
        windows_colour = self.driver.find_element(*self.windows_colour_loc).text
        # print(windows_type,no_widnows,windows_colour)
        return  windows_type,no_widnows,windows_colour

    @property
    def check_windows_type(self):
        '''check the windows type dropdown list'''
        # self.driver.find_element(*self.extras_loc).click()
        self.driver.find_element(*self.windows_type_select_loc).click()
        windows_type_dropdown = self.driver.find_element(*self.windows_type_select_loc).text
        print(windows_type_dropdown)
        return  windows_type_dropdown


    @property
    def check_windows_colour(self):
        '''check the windows colour dropdown list'''
        # self.driver.find_element(*self.extras_loc).click()
        form_element = self.driver.find_element(*self.door_details_page_loc)
        self.driver.find_element(*self.windows_colour_btn_loc).click()
        self.driver.execute_script("arguments[0].scrollIntoView(false);", form_element)  # 滚动条拉到Form最下面
        windows_colour_dropdown = self.driver.find_element(*self.windows_colour_dropdown_loc).text
        print(windows_colour_dropdown)
        return  windows_colour_dropdown

if __name__ == '__main__':
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get("http:// ")
        driver.implicitly_wait(10)

        login = Dealer_Panel_Door(driver)
        login.typeUserName('aa@ecogaragedoors.com')
        login.typePassword('aabb')
        login.clickLogin()
        login.creat_quote()
        login.go_panel_door()
        # login.check_door_type
        # login.check_default_door_type
        # login.check_design
        # login.check_colour_category
        login.check_colour_colorbond
        # login.check_colour_custom
        # login.check_colour_flexographic
        # login.check_colour_metalfx
        login.check_colour_paintedfinish
        # login.check_colour_portabella
        # login.check_colour_timberfx
        # login.check_customcolour_box
        # login.check_customcolourbox_custom
        # login.check_size_details
        # login.check_lh_default
        # login.check_rh_default
        # login.check_width_default
        # login.check_lhrk_list
        # login.check_seals_list
        # login.check_checkboxes_details
        # login.check_reverse_colour_status
        # login.check_emergency_key_status
        # login.check_opener_details
        # login.check_extras_details
        # login.check_windows_type
        # login.check_windows_colour
















































