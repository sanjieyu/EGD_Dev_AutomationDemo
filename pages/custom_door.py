# Author:Yi Sun(Tim) 2023-11-02

'''Add Custom Door Details Page'''

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from pages.add_quote import *

class Custom_Door(Add_Quote):

    add_door_menu = (By.ID,'btnDoorSectionadd')
    add_custom_btn = (By.ID,'add-door-custom')
    add_btn_loc = (By.ID, 'customAdd')
    close_customdoor_btn = (By.ID,'customClose')
    door_main_page = (By.XPATH, '//*[@id="main"]/div/span')

    '''loc for each element for install details'''
    title_loc = (By.NAME,'QuoteTitle')
    unit_no_loc = (By.NAME,'UnitNum')
    unit_no_inputbox = (By.ID,'CustomUnitNumber')
    packaging_type_loc = (By.NAME,'PackagingType')
    packaging_type_select = (By.ID,'PackagingTypeCustom')
    install_type_loc = (By.NAME,'InstallTypeEdit')
    install_type_select = (By.ID,'InstallType')
    design_loc = (By.NAME,'DesignEdit')
    design_select = (By.ID,'CustomDesign')
    colour_category_loc = (By.NAME,'ColourCategoryEdit')
    colour_category_select = (By.ID,'CustomColourCategory')
    door_colour_loc = (By.NAME,'DoorColourEdit')
    door_colour_select = (By.ID,'CustomDoorColour')
    frame_colour_loc = (By.NAME,'FrameColourEdit')
    frame_colour_select = (By.ID,'CustomFrameColour')
    timber_profile_loc = (By.NAME,'TimberEdit')
    timber_profile_select = (By.ID,'ui-id-16')
    insert_material_loc = (By.NAME,'MaterialEdit')
    insert_material_select = (By.ID,'CustomInsertMaterial')
    insert_location_loc = (By.NAME,'LocationEdit')
    insert_location_select= (By.ID,'CustomInsertLocation')
    insert_type_loc = (By.NAME,'InsertTypeEdit')
    insert_type_select = (By.ID,'CustomInsertType')
    insert_colour_loc = (By.NAME,'InsertTypeEdit')
    insert_colour_select = (By.ID,'CustomInsertColour')
    insert_other_loc = (By.NAME,'InsertOtherEdit')
    insert_other_inputbox = (By.ID,'CustomInsertOther')
    custom_colour_loc = (By.NAME,'CustomColourEdit')
    custom_colour_inputbox = (By.ID,'CustomCustomColour')

    '''loc for each element for SIZE details'''
    opensize_lh_loc = (By.NAME,'OpeningSizeLHEdit')
    opensize_lh_select = (By.ID,'CustomOpeningSizeLH')
    opensize_rh_loc = (By.NAME,'OpeningSizeRHEdit')
    opensize_rh_select = (By.ID,'CustomOpeningSizeRH')
    opensize_width_loc = (By.NAME,'OpeningSizeWidthEdit')
    opensize_width_select =(By.ID,'CustomOpeningSizeWidth')
    sr_left_loc = (By.NAME,'SRLeftEdit')
    sr_left_select =(By.ID,'CustomSRLeft')
    hr_loc = (By.NAME,'HREdit')
    hr_select = (By.ID,'CustomHR')
    sr_right_loc = (By.NAME,'SRRightEdit')
    sr_right_select =(By.ID,'CustomSRRight')
    lhrk_loc = (By.NAME,'LHRKEdit')
    lhrk_select = (By.ID,'CustomLHRK')
    sms_bracket_loc = (By.NAME,'SMSEdit')
    lsr_kit_loc = (By.NAME,'LsrEdit')
    timber_packers_loc = (By.NAME,'TimberPackersEdit')
    timber_packers_select = (By.ID,'CustomTimberPackers')
    taper_loc = (By.NAME,'TapeEdit')
    taper_select = (By.ID,'CustomTaper')
    additional_fabrication_loc = (By.NAME,'HeavyAngleEdit')
    additional_fabrication_select = (By.ID,'CustomHeavyAngle')
    additional_fabrication_required_loc = (By.NAME,'HeavyAngleDetailsEdit')
    additional_fabrication_required_inputbox = (By.ID,'CustomHeavyAngleDetails')
    shop_drawings_loc = (By.NAME,'ShopDrawingsEdit')
    shop_drawings_select = (By.ID,'CustomShopDrawings')
    lifting_equipment_loc = (By.NAME,'LiftEdit')
    lifting_equipment_btn = (By.ID,'btnLift')

    '''loc for each element for Panels details'''
    panel_high_loc = (By.CSS_SELECTOR, "[aria-label='panelhigh']")
    panel_high_select_loc = (By.ID,'panels_high')
    panel_wide_loc = (By.CSS_SELECTOR, "[aria-label='panelwide']")
    panel_wide_btn_loc = (By.ID, 'btnPanelWide')
    panel_wide_input_loc = (By.ID, 'panels_wide_part')

    '''loc for each element for checkboxes details'''
    induction_loop_loc = (By.XPATH,'//*[@id="induction"]/div/div[1]')
    reverse_install_loc = (By.XPATH,'//*[@id="reverse"]/div/div[1]/span')
    fully_sloctted_loc = (By.XPATH,'//*[@id="sloctted"]/div/div[1]/div[2]/span')
    emergency_key_loc = (By.XPATH,'//*[@id="emergency"]/div/div[2]/span')
    reverse_colour_loc = (By.XPATH,'//*[@id="reversecolour"]/div/div[2]/span')
    battery_backup_loc = (By.XPATH,'//*[@id="battery"]/div/div[3]/span')
    eco_wifi_loc = (By.XPATH,'//*[@id="ecowifi"]/div/div[2]/span')

    '''loc for Opener details'''
    opener_loc = (By.XPATH,'//*[@id="opener"]/div/div[1]/div[2]/span')
    opener_select = (By.ID,'CustomMotors')
    handsets_loc = (By.XPATH,'//*[@id="handsets"]/div/div[1]/div[2]/span')
    handsets_select = (By.ID,'CustomNoOfHandsets')
    wall_btn_loc = (By.XPATH,'//*[@id="wallbtn"]/div/div[1]/span')
    wall_btn_select = (By.ID,'CustomWallButton')
    opener_detail_loc = (By.XPATH,'//*[@id="motorsother"]/div/div[2]/span')
    opener_detail_box = (By.ID,'CustomMotorsOther')
    digital_keypad_loc = (By.XPATH,'//*[@id="keypad"]/div/div[1]')
    digital_keypad_select = (By.ID,'CustomDigitalKeypad')
    internal_pushbtn_loc = (By.XPATH,'//*[@id="pushbtn"]/div/div[2]')
    internal_pushbtn_select = (By.ID,'CustomInternalPushButton')
    pe_beam_loc = (By.XPATH,'//*[@id="pe_beam"]/div/div[2]/span')
    pe_beam_select = (By.ID,'PEBeamCustom')
    pe_beam_sets_loc = (By.XPATH,'//*[@id="beam_sets"]/div/div[2]/span')
    pe_beam_sets_select = (By.ID,'PEBeamSetsCustom')


    '''loc for other elements details '''
    weight_added_loc = (By.CSS_SELECTOR,"label[for='WeightBeingAdded']")
    weight_added_select = (By.ID,'WeightAddedStandard')
    seals_loc = (By.CSS_SELECTOR,"label[for='CustomSeals']")
    seals_select = (By.ID,'Seals')
    hang_door_loc = (By.CSS_SELECTOR,"label[for='CustomHangDoorFrom']")
    hang_door_select = (By.ID,'hang_door_from_standard_part')
    lintel_type_loc = (By.CSS_SELECTOR,"label[for='CustomLintelType']")
    lintel_type_select = (By.ID,'LintelType')
    fixing_type_loc = (By.CSS_SELECTOR,"label[for='CustomFixingType']")
    fixing_type_select = (By.ID,'fixing_type_standard_part')
    ibeam_noggins_loc = (By.CSS_SELECTOR,"label[for='CustomIBeamNoggins']")
    ibeam_noggins_select = (By.ID,'noggins_standard_part')
    remove_dispose_loc = (By.CSS_SELECTOR,"label[for='RemoveDispose']")
    remove_dispose_select = (By.ID,'RemoveAndDispose')
    job_status_loc = (By.CSS_SELECTOR,"label[for='JobStatus']")
    job_status_select = (By.ID,'JobStatusId')
    expected_deliverydate_loc = (By.CSS_SELECTOR,"label[for='DeliveryDate']")
    expected_deliverydate_box = (By.ID,'ExpectedDeliveryDate')
    cut_date_loc = (By.CSS_SELECTOR,"label[for='CutDate']")
    cut_date_box = (By.ID,'CutDate')
    paint_date_loc  = (By.CSS_SELECTOR,"label[for='PaintDate']")
    paint_date_box = (By.ID,'PaintDate')
    qc_date_loc = (By.CSS_SELECTOR,"label[for='QcDate']")
    qc_date_box = (By.ID,'QCDate')
    other_date_loc = (By.CSS_SELECTOR,"label[for='OtherDate']")
    other_date_box = (By.ID,'OtherDate')

    '''loc for additional infomation details '''
    additional_info_loc = (By.CSS_SELECTOR,"label[for='AdditionalInfo']")
    additional_info_box = (By.ID,'AdditionalInfo')
    production_notes_loc = (By.CSS_SELECTOR,"label[for='ProductionNotes']")
    production_notes_box = (By.ID,'ProductionNotes')

    '''loc for Extra and Site Pictures'''
    extras_loc = (By.CSS_SELECTOR,"label[for='Extras']")
    site_picture_loc = (By.CSS_SELECTOR,"label[for='SitePicture']")

    '''loc for each element in Extra'''
    lh_jamb_loc = (By.CSS_SELECTOR,"label[for='LhJamb']")
    lh_jamb_select = (By.ID,'LH_JambTypeStandard')
    lh_size_loc = (By.CSS_SELECTOR,"label[for='LhSize']")
    lh_size_width_btn = (By.ID,'btnWidth')
    lh_size_depth_btn_loc = (By.ID,'btnDepth')
    lh_size_width_select = (By.XPATH,'//*[@id="ui-id-5"]')
    lh_size_depth_select = (By.ID, 'ui-id-6')
    rh_jamb_loc = (By.CSS_SELECTOR,"label[for='RhJamb']")
    rh_jamb_select = (By.ID,'RH_JambTypeStandard')
    rh_size_loc = (By.CSS_SELECTOR,"label[for='RhSize']")
    rh_size_width_btn = (By.CSS_SELECTOR,"label[for='RhWidth']")
    rh_size_depth_btn = (By.CSS_SELECTOR,"label[for='RhDepth']")
    rh_size_width_select = (By.ID,'ui-id-7')
    rh_size_depth_select = (By.ID,'ui-id-8')
    lh_cover_type_loc = (By.CSS_SELECTOR,"label[for='LhCover']")
    lh_cover_select = (By.ID,'LH_CoverTypeStandard')
    lh_cover_width_size_loc = (By.CSS_SELECTOR,"label[for='LhCoverWidth']")
    lh_cover_width_btn = (By.ID,"btnLhWidth")
    lh_cover_depth_btn = (By.ID,"btnLhDepth")
    lh_cover_width_select = (By.ID,'ui-id-9')
    lh_cover_depth_select = (By.ID, 'ui-id-10')
    lh_cover_colour_loc = (By.CSS_SELECTOR,"label[for='LhCoverColour']")
    lh_cover_colour_select = (By.ID,'LHCoverColour')
    rh_cover_type_loc = (By.CSS_SELECTOR,"label[for='rhCoverType']")
    rh_cover_select = (By.ID,'RH_CoverTypeStandard')
    rh_cover_width_size_loc = (By.CSS_SELECTOR,"label[for='RhCoverWidth']")
    rh_cover_width_btn = (By.ID,"btnRhWidth")
    rh_cover_width_select = (By.ID,'ui-id-11')
    rh_cover_depth_select = (By.ID, 'ui-id-12')
    rh_cover_colour_loc = (By.CSS_SELECTOR,"label[for='RhCoverColour']")
    rh_cover_colour_select = (By.ID,'RHCoverColour')


    def go_addcustomdoor(self):
        '''Open the Add Custom Door from Quote Page'''
        self.driver.find_element(*self.add_door_menu).click()
        self.driver.find_element(*self.add_custom_btn).click()
        self.driver.switch_to.window(self.driver.window_handles[-1])   # switch to the add door details page

    @property
    def check_customdoor_page(self):
        '''check the main elements in the page'''
        form_element = self.driver.find_element(*self.door_main_page)
        standarddoor_title = self.driver.find_element(*self.title_loc).text
        self.driver.execute_script("arguments[0].scrollIntoView(false);", form_element)
        print(standarddoor_title)
        return standarddoor_title

    @property
    def check_install_details(self):
        '''check each element for install details'''
        install_type = self.driver.find_element(*self.install_type_loc).text
        design = self.driver.find_element(*self.design_loc).text
        colour_category = self.driver.find_element(*self.colour_category_loc).text
        door_colour = self.driver.find_element(*self.door_colour_loc).text
        frame_colour = self.driver.find_element(*self.frame_colour_loc).text
        timber_profile = self.driver.find_element(*self.timber_profile_loc).text
        insert_material = self.driver.find_element(*self.insert_material_loc).text
        insert_location = self.driver.find_element(*self.insert_location_loc).text
        insert_type = self.driver.find_element(*self.insert_type_loc).text
        insert_colour = self.driver.find_element(*self.insert_colour_loc).text
        insert_other = self.driver.find_element(*self.insert_other_loc).text
        custom_colour = self.driver.find_element(*self.custom_colour_loc).text
        print(install_type,design,colour_category,door_colour,frame_colour,timber_profile,insert_material,
              insert_location,insert_type,insert_colour,insert_other,custom_colour)
        return  (install_type,design,colour_category,door_colour,frame_colour,timber_profile,insert_material,
                 insert_location,insert_type,insert_colour,insert_other,custom_colour)

    @property
    def check_install_type(self):
        '''check the install type dropdown'''
        self.driver.find_element(*self.install_type_select).click()
        install_type_list = self.driver.find_element(*self.install_type_select).text
        print(install_type_list)
        return  install_type_list

    @property
    def check_design(self):
        '''check the Design dropdown'''
        self.driver.find_element(*self.design_select).click()
        design_list = self.driver.find_element(*self.design_select).text
        print(design_list)
        return  design_list

    @property
    def check_colour_category(self):
        '''check the Colour Category dropdown'''
        self.driver.find_element(*self.colour_category_select).click()
        colour_category_list = self.driver.find_element(*self.colour_category_select).text
        print(colour_category_list)
        return  colour_category_list

    @property
    def check_door_colour_custom(self):
        '''check the Door Colour dropdown for Custom Colour Category'''
        global colour_category
        colour_category = Select(self.driver.find_element(*self.colour_category_select))
        custom_colour = colour_category.select_by_visible_text('Custom')
        door_colour_list = self.driver.find_element(*self.door_colour_select)
        if door_colour_list.is_enabled():
            print('Enabled')
            return  True
        else:
            print("Disabled")
            return False

    @property
    def check_door_colour_oilcolour(self):
        '''check the Door Colour dropdown for OilColour Colour Category'''
        custom_colour = colour_category.select_by_visible_text('OilColour')
        door_colour_list1 = self.driver.find_element(*self.door_colour_select).text
        print(door_colour_list1)
        return door_colour_list1

    @property
    def check_door_colour_painted(self):
        '''check the Door Colour dropdown for Painted Colour Category'''
        # colour_category = Select(self.driver.find_element(*self.colour_category_select))
        custom_colour = colour_category.select_by_visible_text('Painted')
        door_colour_list2 = self.driver.find_element(*self.door_colour_select).text
        print(door_colour_list2)
        return door_colour_list2

    @property
    def check_door_colour_raw(self):
        '''check the Door Colour dropdown for Raw Colour Category'''
        # colour_category = Select(self.driver.find_element(*self.colour_category_select))
        custom_colour = colour_category.select_by_visible_text('Raw')
        door_colour_list3 = self.driver.find_element(*self.door_colour_select).text
        print(door_colour_list3)
        return door_colour_list3

    @property
    def check_door_colour_sealedcolour(self):
        '''check the Door Colour dropdown for SealedColour Colour Category'''
        # colour_category = Select(self.driver.find_element(*self.colour_category_select))
        custom_colour = colour_category.select_by_visible_text('SealedColour')
        door_colour_list4 = self.driver.find_element(*self.door_colour_select).text
        print(door_colour_list4)
        return door_colour_list4

    @property
    def check_frame_colour(self):
        '''check the Frame Colour dropdown list'''
        self.driver.find_element(*self.frame_colour_select).click()
        frame_colour_list = self.driver.find_element(*self.frame_colour_select).text
        print(frame_colour_list)
        return frame_colour_list

    @property
    def check_timber_profile(self):
        '''check the Timber Profile dropdown list'''
        self.driver.find_element(By.XPATH,'/html/body/div[3]/div[2]/div[3]/div/div/form/div/div[1]/div[4]/div[6]/'
                                          'fieldset/span/a/span[1]').click()
        timber_profile_list = self.driver.find_element(*self.timber_profile_select).text
        print(timber_profile_list)
        return timber_profile_list

    @property
    def check_insert_material(self):
        '''check the Insert Material dropdown list'''
        self.driver.find_element(*self.insert_material_select).click()
        insert_material_list = self.driver.find_element(*self.insert_material_select).text
        print(insert_material_list)
        return insert_material_list

    @property
    def check_insert_location(self):
        '''check the Insert Location dropdown list'''
        self.driver.find_element(*self.insert_location_select).click()
        insert_location_list = self.driver.find_element(*self.insert_location_select).text
        print(insert_location_list)
        return insert_location_list

    @property
    def check_insert_type_default(self):
        '''check the Insert Type dropdown list default value'''
        self.driver.find_element(*self.insert_type_select).click()
        insert_type_list = self.driver.find_element(*self.insert_type_select).text
        print(insert_type_list)
        return insert_type_list

    @property
    def check_insert_type_cat1(self):
        '''check the Insert Type dropdown if set "ACPS Cat1" in Insert Material category'''
        global insert_material
        insert_material = Select(self.driver.find_element(*self.insert_material_select))
        material_value = insert_material.select_by_visible_text('ACPS Upgrade - Cat 1')
        self.driver.find_element(*self.insert_type_select).click()
        insert_type_list1 = self.driver.find_element(*self.insert_type_select).text
        print(insert_type_list1)
        return insert_type_list1

    @property
    def check_insert_type_cat2(self):
        '''check the Insert Type dropdown if set "ACPS Cat2" in Insert Material category'''
        material_value = insert_material.select_by_visible_text('ACPS Upgrade - Cat 2')
        self.driver.find_element(*self.insert_type_select).click()
        insert_type_list2 = self.driver.find_element(*self.insert_type_select).text
        print(insert_type_list2)
        return insert_type_list2

    @property
    def check_insert_type_acrylic(self):
        '''check the Insert Type dropdown if set "Acrylic" in Insert Material category'''
        material_value = insert_material.select_by_visible_text('Acrylic')
        self.driver.find_element(*self.insert_type_select).click()
        insert_type_list3 = self.driver.find_element(*self.insert_type_select).text
        print(insert_type_list3)
        return insert_type_list3

    @property
    def check_insert_type_aluminium(self):
        '''check the Insert Type dropdown if set "Aluminium" in Insert Material category'''
        material_value = insert_material.select_by_visible_text('Aluminium')
        self.driver.find_element(*self.insert_type_select).click()
        insert_type_list4 = self.driver.find_element(*self.insert_type_select).text
        print(insert_type_list4)
        return insert_type_list4

    @property
    def check_design_insulated(self):
        '''check the Design dropdown for Insulated Sectional Door'''
        # door_type = Select(self.driver.find_element(*self.door_type_select))
        insulated_sectional= door_type.select_by_visible_text('Insulated Sectional')
        self.driver.find_element(*self.design_select).click()
        design_list = self.driver.find_element(*self.design_select).text
        print(design_list)
        return  design_list

    @property
    def check_design_roller(self):
        '''check the Design dropdown for Roller Door'''
        # door_type = Select(self.driver.find_element(*self.door_type_select))
        roller_door= door_type.select_by_visible_text('Roller Door')
        self.driver.find_element(*self.design_select).click()
        design_list = self.driver.find_element(*self.design_select).text
        back_default = door_type.select_by_visible_text('Please Select')
        print(design_list)
        return  design_list

    @property
    def check_colour_colorbond(self):
        '''check the Door Colour dropdown for ColorBond Category'''
        global colour_category
        colour_category = Select(self.driver.find_element(*self.colour_category_select))
        colorbond = colour_category.select_by_visible_text('ColorBond')
        self.driver.find_element(*self.door_colour_select).click()
        door_colour_list = self.driver.find_element(*self.door_colour_select).text
        print(door_colour_list)
        return  door_colour_list

    @property
    def check_colour_custom(self):
        '''check the Door Colour dropdown for Custom Category'''
        # colour_category = Select(self.driver.find_element(*self.colour_category_select))
        custom = colour_category.select_by_visible_text('Custom')
        custom_colour = self.driver.find_element(*self.door_colour_select)
        if custom_colour.is_enabled():                                        #判断dropdown list是不可点击的
            print('wrong')
            return  False
        else:
            print('correct')
            return True

    @property
    def check_colour_flexigraphic(self):
        '''check the Door Colour dropdown for Flexigraphic Category'''
        # colour_category = Select(self.driver.find_element(*self.colour_category_select))
        flexigraphic = colour_category.select_by_visible_text('Flexigraphic')
        self.driver.find_element(*self.door_colour_select).click()
        door_colour_list = self.driver.find_element(*self.door_colour_select).text
        print(door_colour_list)
        return  door_colour_list

    @property
    def check_colour_flexographic(self):
        '''check the Door Colour dropdown for Flexographic Category'''
        # colour_category = Select(self.driver.find_element(*self.colour_category_select))
        flexographic = colour_category.select_by_visible_text('Flexographic')
        self.driver.find_element(*self.door_colour_select).click()
        door_colour_list = self.driver.find_element(*self.door_colour_select).text
        print(door_colour_list)
        return  door_colour_list

    @property
    def check_colour_metalfx(self):
        '''check the Door Colour dropdown for MetalFx Category'''
        # colour_category = Select(self.driver.find_element(*self.colour_category_select))
        metalfx = colour_category.select_by_visible_text('MetalFx')
        self.driver.find_element(*self.door_colour_select).click()
        door_colour_list = self.driver.find_element(*self.door_colour_select).text
        print(door_colour_list)
        return  door_colour_list
    @property
    def check_colour_paintedfinish(self):
        '''check the Door Colour dropdown for PaintedFinish Category'''
        # colour_category = Select(self.driver.find_element(*self.colour_category_select))
        paintedfinish = colour_category.select_by_visible_text('Painted Finish')
        self.driver.find_element(*self.door_colour_select).click()
        door_colour_list = self.driver.find_element(*self.door_colour_select).text
        print(door_colour_list)
        return  door_colour_list

    @property
    def check_colour_portabella(self):
        '''check the Door Colour dropdown for Portabella Category'''
        # colour_category = Select(self.driver.find_element(*self.colour_category_select))
        portabella = colour_category.select_by_visible_text('Portabella')
        self.driver.find_element(*self.door_colour_select).click()
        door_colour_list = self.driver.find_element(*self.door_colour_select).text
        print(door_colour_list)
        return  door_colour_list

    @property
    def check_colour_timberfx(self):
        '''check the Door Colour dropdown for TimberFX Category'''
        # colour_category = Select(self.driver.find_element(*self.colour_category_select))
        timberfx = colour_category.select_by_visible_text('TimberFX')
        self.driver.find_element(*self.door_colour_select).click()
        door_colour_list = self.driver.find_element(*self.door_colour_select).text
        print(door_colour_list)
        return  door_colour_list

    @property
    def check_customcolour_box(self):
        '''check the Custom Colour input box should be disable by default'''
        custom_colour_box = self.driver.find_element(*self.custom_colour_inputbox)
        if custom_colour_box.is_enabled():
            print('wrong')
            return  False
        else:
            print('correct')
            return True

    @property
    def check_customcolourbox_custom(self):
            '''check the Custom Colour input box should be enable for Custom Colour Category'''
            colour_category1 = Select(self.driver.find_element(*self.colour_category_select))
            custom = colour_category1.select_by_visible_text('Custom')
            custom_colour_box = self.driver.find_element(*self.custom_colour_inputbox)
            if custom_colour_box.is_enabled():  # 判断input box是可输入的
                print('correct')
                return True
            else:
                print('wrong')
                return False

    @property
    def check_size_details(self):
        '''check each element for size details'''
        opensize_lh = self.driver.find_element(*self.opensize_lh_loc).text
        opensize_rh = self.driver.find_element(*self.opensize_rh_loc).text
        opensize_width = self.driver.find_element(*self.opensize_width_loc).text
        sr_left = self.driver.find_element(*self.sr_left_loc).text
        hr = self.driver.find_element(*self.hr_loc).text
        sr_right = self.driver.find_element(*self.sr_right_loc).text
        lhrk = self.driver.find_element(*self.lhrk_loc).text
        sms_bracket = self.driver.find_element(*self.sms_bracket_loc).text
        lsr_kit = self.driver.find_element(*self.lsr_kit_loc).text
        print(opensize_lh,opensize_rh,opensize_width,sr_left,hr,sr_right,lhrk,sms_bracket,lsr_kit)
        return  opensize_lh,opensize_rh,opensize_width,sr_left,hr,sr_right,lhrk,sms_bracket,lsr_kit


    @property
    def check_openinglh_default(self):
        '''check the default value for Opening Size LH'''
        openinglh_default = self.driver.find_element(*self.opensize_lh_select).get_attribute('value')
        print(openinglh_default)
        return  openinglh_default

    @property
    def check_openingrh_default(self):
        '''check the default value for Opening Size RH'''
        openingrh_default = self.driver.find_element(*self.opensize_rh_select).get_attribute('value')
        print(openingrh_default)
        return  openingrh_default

    @property
    def check_openingwidth_default(self):
        '''check the default value for Opening Size Width'''
        openingwidth_default = self.driver.find_element(*self.opensize_width_select).get_attribute('value')
        print(openingwidth_default)
        return  openingwidth_default

    @property
    def check_srleft_default(self):
        '''check the default value for SR Left'''
        srleft_default = self.driver.find_element(*self.sr_left_select).get_attribute('value')
        print(srleft_default)
        return  srleft_default

    @property
    def check_hr_default(self):
        '''check the default value for HR'''
        hr_default = self.driver.find_element(*self.hr_select).get_attribute('value')
        print(hr_default)
        return  hr_default

    @property
    def check_srright_default(self):
        '''check the default value for SR Right'''
        srright_default = self.driver.find_element(*self.sr_right_select).get_attribute('value')
        print(srright_default)
        return  srright_default

    @property
    def check_lhrk_list(self):
        '''check the LHRK dropdown list'''
        self.driver.find_element(*self.lhrk_select).click()
        lhrk_list = self.driver.find_element(*self.lhrk_select).text
        print(lhrk_list)
        return  lhrk_list
    @property
    def check_timber_details(self):
        '''check each element for Timer/Taper/AdditionalFab details'''
        timber_pack = self.driver.find_element(*self.timber_packers_loc).text
        taper = self.driver.find_element(*self.taper_loc).text
        addition_fab = self.driver.find_element(*self.additional_fabrication_loc).text
        addition_fab_req = self.driver.find_element(*self.additional_fabrication_required_loc).text
        shop_drawings = self.driver.find_element(*self.shop_drawings_loc).text
        lifting = self.driver.find_element(*self.lifting_equipment_loc).text
        print(timber_pack,taper,addition_fab,addition_fab_req,shop_drawings,lifting)
        return  timber_pack,taper,addition_fab,addition_fab_req,shop_drawings,lifting

    @property
    def check_checkboxes_details(self):
        '''check each element for all checkboxes'''
        induction_loop   = self.driver.find_element(*self.induction_loop_loc).text
        reverse_install = self.driver.find_element(*self.reverse_install_loc).text
        fully_slotted = self.driver.find_element(*self.fully_sloctted_loc).text
        emergency_key = self.driver.find_element(*self.emergency_key_loc).text
        reverse_colour = self.driver.find_element(*self.reverse_colour_loc).text
        battery_backup = self.driver.find_element(*self.battery_backup_loc).text
        eco_wifi = self.driver.find_element(*self.eco_wifi_loc).text
        print(induction_loop,reverse_install,fully_slotted,emergency_key,reverse_colour,battery_backup,eco_wifi)
        return  induction_loop,reverse_install,fully_slotted,emergency_key,reverse_colour,battery_backup,eco_wifi

    @property
    def check_opener_details(self):
        '''check each element for Opener'''
        opener = self.driver.find_element(*self.opener_loc).text
        handsets_no  = self.driver.find_element(*self.handsets_loc).text
        wall_btn = self.driver.find_element(*self.wall_btn_loc).text
        opener_details = self.driver.find_element(*self.opener_detail_loc).text
        digital_keypad = self.driver.find_element(*self.digital_keypad_loc).text
        internal_push_btn = self.driver.find_element(*self.internal_pushbtn_loc).text
        pe_beam = self.driver.find_element(*self.pe_beam_loc).text
        pe_beam_sets = self.driver.find_element(*self.pe_beam_sets_loc).text
        keys = self.driver.find_element(*self.keys_loc).text
        print(opener,handsets_no,wall_btn,opener_details,digital_keypad,internal_push_btn,pe_beam,pe_beam_sets)
        return  opener,handsets_no,wall_btn,opener_details,digital_keypad,internal_push_btn,pe_beam,pe_beam_sets

    @property
    def check_other_details(self):
        '''check each element for other elements'''
        weight_being_added = self.driver.find_element(*self.weight_added_loc).text
        seals = self.driver.find_element(*self.seals_loc).text
        hang_door_from = self.driver.find_element(*self.hang_door_loc).text
        lintel_type = self.driver.find_element(*self.lintel_type_loc).text
        fixing_type = self.driver.find_element(*self.fixing_type_loc).text
        ibeam_noggins = self.driver.find_element(*self.ibeam_noggins_loc).text
        remove_dispose = self.driver.find_element(*self.remove_dispose_loc).text
        job_status = self.driver.find_element(*self.job_status_loc).text
        expected_delivery_date = self.driver.find_element(*self.expected_deliverydate_loc).text
        cut_date=self.driver.find_element(*self.cut_date_loc).text
        paint_date = self.driver.find_element(*self.paint_date_loc).text
        qc_date = self.driver.find_element(*self.qc_date_loc).text
        other_date = self.driver.find_element(*self.other_date_loc).text
        print(weight_being_added,seals,hang_door_from,lintel_type,fixing_type,ibeam_noggins,remove_dispose,
              job_status,expected_delivery_date,cut_date,paint_date,qc_date,other_date)
        return  (weight_being_added,seals,hang_door_from,lintel_type,fixing_type,ibeam_noggins,remove_dispose,
                 job_status,expected_delivery_date,cut_date,paint_date,qc_date,other_date)

    @property
    def check_additional_details(self):
        '''check each element for additional information elements'''
        additional_info  = self.driver.find_element(*self.additional_info_loc).text
        production_notes = self.driver.find_element(*self.production_notes_loc).text
        print(additional_info,production_notes)
        return  additional_info,production_notes

    @property
    def check_extra_picture(self):
        '''check the details for Jamb in Extras section'''
        extra = self.driver.find_element(*self.extras_loc).text
        site_pciture = self.driver.find_element(*self.site_picture_loc).text
        print(extra,site_pciture)
        return  extra,site_pciture

    @property
    def check_jamb_extras(self):
        '''check the details for Jamb in Extras section'''
        self.driver.find_element(*self.extras_loc).click()
        form_element = self.driver.find_element(*self.door_main_page)
        self.driver.execute_script("arguments[0].scrollIntoView(false);", form_element)
        lh_jamb = self.driver.find_element(*self.lh_jamb_loc).text
        lh_size = self.driver.find_element(*self.lh_size_loc).text
        rh_jamb = self.driver.find_element(*self.rh_jamb_loc).text
        rh_size = self.driver.find_element(*self.rh_size_loc).text
        print(lh_jamb,lh_size,rh_jamb,rh_size)
        return  lh_jamb,lh_size,rh_jamb,rh_size

    @property
    def lh_jamb_type(self):
        '''check the list for LH JAMB Type'''
        self.driver.find_element(*self.extras_loc).click()
        form_element = self.driver.find_element(*self.door_main_page)
        self.driver.execute_script("arguments[0].scrollIntoView(false);", form_element)
        self.driver.find_element(*self.lh_jamb_select).click()
        lh_jambtype_list = self.driver.find_element(*self.lh_jamb_select).text
        self.driver.find_element(*self.extras_loc).click()
        print(lh_jambtype_list)
        return  lh_jambtype_list

    @property
    def lh_width_size(self):
        '''check the list for LH JAMB Width Size'''
        self.driver.find_element(*self.extras_loc).click()
        form_element = self.driver.find_element(*self.door_main_page)
        self.driver.execute_script("arguments[0].scrollIntoView(false);", form_element)
        self.driver.find_element(*self.lh_size_width_btn).click()
        lh_width_size = self.driver.find_element(*self.lh_size_width_select).text
        self.driver.find_element(*self.extras_loc).click()
        print(lh_width_size)
        return  lh_width_size

    @property
    def lh_depth_size(self):
        '''check the list for LH JAMB Depth Size'''
        self.driver.find_element(*self.extras_loc).click()
        form_element = self.driver.find_element(*self.door_main_page)
        self.driver.execute_script("arguments[0].scrollIntoView(false);", form_element)
        self.driver.find_element(*self.lh_size_depth_btn).click()
        lh_depth_size = self.driver.find_element(*self.lh_size_depth_select).text
        self.driver.find_element(*self.extras_loc).click()
        print(lh_depth_size)
        return  lh_depth_size

    @property
    def rh_jamb_type(self):
        '''check the list for RH JAMB Type'''
        self.driver.find_element(*self.extras_loc).click()
        form_element = self.driver.find_element(*self.door_main_page)
        self.driver.execute_script("arguments[0].scrollIntoView(false);", form_element)
        self.driver.find_element(*self.rh_jamb_select).click()
        rh_jambtype_list = self.driver.find_element(*self.rh_jamb_select).text
        self.driver.find_element(*self.extras_loc).click()
        print(rh_jambtype_list)
        return  rh_jambtype_list

    @property
    def rh_width_size(self):
        '''check the list for RH JAMB Width Size'''
        self.driver.find_element(*self.extras_loc).click()
        form_element = self.driver.find_element(*self.door_main_page)
        self.driver.execute_script("arguments[0].scrollIntoView(false);", form_element)
        self.driver.find_element(*self.rh_size_width_btn).click()
        rh_width_size = self.driver.find_element(*self.rh_size_width_select).text
        self.driver.find_element(*self.extras_loc).click()
        print(rh_width_size)
        return  rh_width_size

    @property
    def rh_depth_size(self):
        '''check the list for RH JAMB Depth Size'''
        self.driver.find_element(*self.extras_loc).click()
        form_element = self.driver.find_element(*self.door_main_page)
        self.driver.execute_script("arguments[0].scrollIntoView(false);", form_element)
        self.driver.find_element(*self.rh_size_depth_btn).click()
        rh_depth_size = self.driver.find_element(*self.rh_size_depth_select).text
        self.driver.find_element(*self.extras_loc).click()
        print(rh_depth_size)
        return  rh_depth_size

    @property
    def check_cover_type(self):
        '''check the details for Cover Type in Extras section'''
        self.driver.find_element(*self.extras_loc).click()
        form_element = self.driver.find_element(*self.door_main_page)
        self.driver.execute_script("arguments[0].scrollIntoView(false);", form_element)
        lh_cover_type = self.driver.find_element(*self.lh_cover_type_loc).text
        lh_cover_width_size = self.driver.find_element(*self.lh_cover_width_size_loc).text
        lh_cover_coloure = self.driver.find_element(*self.lh_cover_colour_loc).text
        rh_cover_type = self.driver.find_element(*self.rh_cover_type_loc).text
        rh_cover_width_size = self.driver.find_element(*self.rh_cover_width_size_loc).text
        rh_cover_coloure = self.driver.find_element(*self.rh_cover_colour_loc).text
        self.driver.find_element(*self.extras_loc).click()
        # print(lh_cover_type,lh_cover_width_size,lh_cover_coloure,rh_cover_type,rh_cover_width_size,rh_cover_coloure)
        return  lh_cover_type,lh_cover_width_size,lh_cover_coloure,rh_cover_type,rh_cover_width_size,rh_cover_coloure


    @property
    def lh_cover_width_size(self):
        '''check the list for LH Cover Width Size'''
        self.driver.find_element(*self.extras_loc).click()
        form_element = self.driver.find_element(*self.door_main_page)
        self.driver.execute_script("arguments[0].scrollIntoView(false);", form_element)
        self.driver.find_element(*self.lh_cover_width_btn).click()
        lh_cover_width_select = self.driver.find_element(*self.lh_cover_width_select).text
        self.driver.find_element(*self.extras_loc).click()
        print(lh_cover_width_select)
        return  lh_cover_width_select

    @property
    def lh_cover_depth_size(self):
        '''check the list for LH Cover Depth Size'''
        self.driver.find_element(*self.extras_loc).click()
        form_element = self.driver.find_element(*self.door_main_page)
        self.driver.execute_script("arguments[0].scrollIntoView(false);", form_element)
        self.driver.find_element(*self.lh_cover_depth_btn).click()
        lh_cover_depth_select = self.driver.find_element(*self.lh_cover_depth_select).text
        self.driver.find_element(*self.extras_loc).click()
        print(lh_cover_depth_select)
        return   lh_cover_depth_select

    @property
    def lh_cover_type(self):
        '''check the list for LH Cover Type'''
        self.driver.find_element(*self.extras_loc).click()
        form_element = self.driver.find_element(*self.door_main_page)
        self.driver.execute_script("arguments[0].scrollIntoView(false);", form_element)
        self.driver.find_element(*self.lh_cover_select).click()
        lh_cover_list = self.driver.find_element(*self.lh_cover_select).text
        self.driver.find_element(*self.extras_loc).click()
        print(lh_cover_list)
        return  lh_cover_list

if __name__ == '__main__':
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get("http:// ")
        driver.implicitly_wait(10)

        login = Custom_Door(driver)
        login.typeUserName('aa@ecogaragedoors.com')
        login.typePassword('aabb')
        login.clickLogin()
        login.go_addquote()
        login.go_addcustomdoor()
        login.check_customdoor_page
        # login.check_install_details
        # login.check_install_type
        # login.check_design
        # login.check_colour_category
        # login.check_door_colour_custom
        # login.check_door_colour_oilcolour
        # login.check_door_colour_painted
        # login.check_door_colour_raw
        # login.check_door_colour_sealedcolour
        # login.check_frame_colour
        # login.check_timber_profile
        # login.check_insert_material
        # login.check_insert_location
        # login.check_insert_type_default
        # login.check_insert_type_cat1
        # login.check_insert_type_acrylic
        # login.check_insert_type_aluminium

        # login.check_colour_flexigraphic
        # login.check_colour_metalfx
        # login.check_colour_paintedfinish
        # login.check_colour_portabella
        # login.check_colour_timberfx
        # login.check_customcolour_box
        # login.check_customcolourbox_custom
        # login.check_size_details
        # login.check_openinglh_default
        # login.check_lhrk_list
        # login.check_timber_details
        # login.check_checkboxes_details
        # login.check_opener_details
        # login.check_other_details
        # login.check_additional_details
        # login.check_extra_picture
        # login.check_jamb_extras
        # login.check_cover_type
        # login.lh_jamb_type
        # login.lh_width_size
        # login.lh_depth_size
        # login.rh_jamb_type
        # login.rh_width_size
        # login.rh_depth_size
        # # login.check_cover_type
        # login.lh_cover_type
        # login.lh_cover_width_size
        # login.lh_cover_depth_size














































