# Author:Yi Sun(Tim) 2025-03-17

'''Add Shutter Door Details Page'''

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from UIModule.add_quote import *

class Shutter_Door(Add_Quote):

    add_door_menu_loc = (By.ID,'btnDoorSectionadd')
    add_shutter_btn_loc = (By.ID,'add-door-shutter')
    door_main_page_loc = (By.XPATH, '//*[@id="main"]/div/span')
    add_btn_loc = (By.ID,'shutterAdd')
    close_btn_loc = (By.ID, 'shutterClose')

    '''loc for each element for install details'''
    title_loc = (By.NAME, 'QuoteTitle')
    unit_no_loc = (By.NAME, 'UnitNum')
    unit_no_inputbox_loc = (By.ID,'UnitNumberSutter')
    packaging_type_loc = (By.NAME,'PackagingType')
    packaging_type_select_loc = (By.ID,'PackagingTypeShutter')

    install_type_loc = (By.NAME,'InstallTypeEdit')
    install_type_select_loc = (By.ID,'InstallTypeSutter')
    door_duty_cycle_loc = (By.NAME,'DoorDuty')
    door_duty_cycle_select_loc = (By.ID,'DutyCycle')
    slat_type_loc = (By.NAME,'SlatTypeEdit')
    slat_type_select_loc = (By.ID,'SlatType')
    slat_design_loc = (By.NAME,'SlatDesignEdit')
    slat_design_select_loc = (By.ID,'SlatDesign')
    slat_ventilation_loc = (By.NAME,'SlatVentilationEdit')
    slat_ventilation_select_loc = (By.ID,'SlatVentilation')
    slat_material_loc = (By.NAME,'SlatMaterialEdit')
    slat_material_select_loc = (By.ID,'SlatMaterial')
    slat_finish_loc = (By.NAME,'SlatFinishEdit')
    slat_finish_select_loc = (By.ID,'SlatFinish')
    slat_finish_custom_loc = (By.NAME,'SlatFinishCustomEdit')
    slat_finish_custom_box_loc = (By.ID,'SlatFinishCustom')
    technician_measure_loc = (By.NAME,'IsTechnicianMeasureShutterEdit')
    technician_measure_checkbox_loc = (By.ID,'IsTechnicianMeasureShutter')
    measure_required_loc = (By.NAME,'IsMeasureRequiredShutterEdit')
    measure_required_checkbox_loc = (By.ID,'IsMeasureRequiredShutter')

    '''loc for each element for SIZE details'''
    opensize_lh_loc = (By.NAME,'OpeningSizeLHEdit')
    opensize_lh_select_loc = (By.ID,'OpeningSizeLHShutter')
    opensize_rh_loc = (By.NAME,'OpeningSizeRHEdit')
    opensize_rh_select_loc = (By.ID,'OpeningSizeRHShutter')
    opensize_width_loc = (By.NAME,'OpeningSizeWidthEdit')
    opensize_width_select_loc =(By.ID,'OpeningSizeWidthShutter')
    sr_left_loc = (By.NAME,'SRLeftEdit')
    sr_left_select_loc =(By.ID,'SRLeftShutter')
    hr_loc = (By.NAME,'HREdit')
    hr_select_loc = (By.ID,'HRShutter')
    sr_right_loc = (By.NAME,'SRRightEdit')
    sr_right_select_loc =(By.ID,'SRRightShutter')
    additional_fabrication_loc = (By.NAME,'HeavyAngleEdit')
    additional_fabrication_select_loc = (By.ID,'HeavyAngleShutter')
    additional_fabrication_required_loc = (By.NAME,'HeavyAngleDetailsEdit')
    additional_fabrication_required_inputbox_loc = (By.ID,'HeavyAngleDetailsShutter')
    shop_drawings_loc = (By.NAME,'ShopDrawingsEdit')
    shop_drawings_select_loc = (By.ID,'ShopDrawingsShutter')
    lifting_equipment_loc = (By.NAME,'LiftEdit')
    lifting_equipment_btn_loc = (By.ID,'btnLift')

    '''loc for each element for checkboxes details'''
    induction_loop_loc = (By.XPATH,'//*[@id="induction"]/div/div[1]')
    induction_loop_checkbox_loc = (By.ID,'IsInductionLoopShutter')
    reverse_rollerdoor_loc = (By.XPATH,'//*[@id="reverse"]/div/div[1]/span')
    reverse_rollerdoor_checkbox_loc = (By.ID,'IsReverseRollShutter')
    eco_wifi_loc = (By.XPATH,'//*[@id="ecowifi"]/div/div[2]/span')
    eco_wifi_checkbox_loc = (By.ID,'IsWiFiShutter')
    taper_loc = (By.XPATH,'//*[@id="tape"]/div/div[2]/span')
    taper_checkbox_loc = (By.ID,'IsTaperShutter')
    reverse_rollcolour_loc = (By.XPATH,'//*[@id="reversecolour"]/div/div[2]/span')
    reverse_rollcolour_checkbox_loc = (By.ID,'IsReverseRollColourShutter')

    '''loc for Operation Side details'''
    operation_side_loc = (By.CSS_SELECTOR,"label[for='OperationSide']")
    operation_side_select_loc = (By.ID,'OperationSide')
    operation_type_loc = (By.CSS_SELECTOR,"label[for='OperationType']")
    operation_type_select_loc = (By.ID,'OperationType')
    battery_backup_loc = (By.CSS_SELECTOR,"label[for='BatteryBackup']")
    battery_backup_select_loc = (By.ID,'BatteryBackup')

    '''loc for Opener details'''
    opener_loc = (By.CSS_SELECTOR,"label[for='LhCover']")
    opener_select_loc = (By.ID,'OpenerShutter')
    handsets_loc = (By.CSS_SELECTOR,"label[for='LhCover']")
    handsets_select_loc = (By.ID,'NoOfHandsetsShutter')
    wall_btn_loc = (By.CSS_SELECTOR,"label[for='LhCover']")
    wall_btn_select_loc = (By.ID,'WallButtonShutter')
    opener_detail_loc = (By.XPATH,'//*[@id="opener"]/div/div[1]/div[2]/span')
    opener_detail_box_loc = (By.ID,'OpenerDetailsShutter')
    digital_keypad_loc = (By.XPATH,'//*[@id="keypad"]/div/div[1]')
    digital_keypad_select_loc = (By.ID,'DigitalKeypadShutter')
    internal_pushbtn_loc = (By.XPATH,'//*[@id="pushbtn"]/div/div[2]')
    internal_pushbtn_select_loc = (By.ID,'InternalPushButtonShutter')
    pe_beam_loc = (By.XPATH,'//*[@id="pe_beam"]/div/div[2]/span')
    pe_beam_select_loc = (By.ID,'PEBeam')
    pe_beam_sets_loc = (By.XPATH,'//*[@id="beam_sets"]/div/div[2]/span')
    pe_beam_sets_select_loc = (By.ID,'PEBeamSets')

    '''loc for other elements details '''
    windlock_loc = (By.CSS_SELECTOR,"label[for='Windlock']")
    windlock_select_loc = (By.ID,'Windlock')
    track_loc = (By.CSS_SELECTOR,"label[for='Track']")
    track_select_loc = (By.ID,'Track')
    remove_and_dispose_loc = (By.CSS_SELECTOR,"label[for='Remove']")
    remove_and_dispose_select_loc = (By.ID,'RemoveAndDisposeShutter')
    seals_loc = (By.CSS_SELECTOR,"label[for='Seals']")
    seals_select_loc = (By.ID,'SealsShutter')
    hang_door_loc = (By.CSS_SELECTOR,"label[for='HangDoor']")
    hang_door_select_loc = (By.ID,'HangDoorFromShutter')
    lintel_type_loc = (By.CSS_SELECTOR,"label[for='LintelType']")
    lintel_type_select_loc = (By.ID,'LintelTypeShutter')
    fixing_type_loc = (By.CSS_SELECTOR,"label[for='FixingType']")
    fixing_type_select_loc = (By.ID,'FixingTypeShutter')
    door_area_loc = (By.CSS_SELECTOR,"label[for='Area']")
    door_area_select_loc = (By.ID,'DoorArea')
    door_status_loc = (By.CSS_SELECTOR,"label[for='JobStatusId']")
    door_status_select_loc = (By.ID,'JobStatusIdShutter')
    expected_deliverydate_loc = (By.CSS_SELECTOR,"label[for='ExpectedDeliveryDate']")
    expected_deliverydate_box = (By.ID,'ExpectedDeliveryDateShutter')

    '''loc for other extras details '''
    other_extras_loc = (By.CSS_SELECTOR,"label[for='OtherExtras']")
    value_loc = (By.CSS_SELECTOR,"label[for='Value']")
    edit_box1_loc = (By.ID,'OtherExtrasName1')
    value_box1_loc = (By.NAME,'OtherExtrasAmount1')
    edit_box2_loc = (By.ID, 'OtherExtrasName2')
    value_box2_loc = (By.NAME, 'OtherExtrasAmount2')
    edit_box3_loc = (By.ID, 'OtherExtrasName3')
    value_box3_loc = (By.NAME, 'OtherExtrasAmount3')
    edit_box4_loc = (By.ID, 'OtherExtrasName4')
    value_box4_loc = (By.NAME, 'OtherExtrasAmount4')
    edit_box5_loc = (By.ID, 'OtherExtrasName5')
    value_box5_loc = (By.NAME, 'OtherExtrasAmount5')

    '''loc for additional infomation details '''
    additional_info_loc = (By.CSS_SELECTOR,"label[for='Additional']")
    additional_info_box = (By.ID,'NotesShutter')
    production_notes_loc = (By.CSS_SELECTOR,"label[for='Production']")
    production_notes_box = (By.ID,'ProductionNotesShutter')

    '''loc for Extra and Site Pictures'''
    extras_loc = (By.CSS_SELECTOR,"label[for='Extras']")
    site_picture_loc = (By.CSS_SELECTOR,"label[for='SitePicture']")

    '''loc for each element in Extra'''
    lh_jamb_loc = (By.CSS_SELECTOR,"label[for='LhJamb']")
    lh_jamb_select_loc = (By.CSS_SELECTOR,"label[for='LhCover']")
    lh_size_loc = (By.CSS_SELECTOR,"label[for='LhSize']")
    lh_size_width_btn_loc = (By.ID,'btnWidth')
    lh_size_depth_btn_loc = (By.ID,'btnDepth')
    lh_size_width_select_loc = (By.ID,'ui-id-34')
    lh_size_depth_select_loc = (By.ID, 'ui-id-35')
    rh_jamb_loc = (By.CSS_SELECTOR,"label[for='RhJamb']")
    rh_jamb_select_loc = (By.ID,'RH_JambTypeShutter')
    rh_size_loc = (By.CSS_SELECTOR,"label[for='RhSize']")
    rh_size_width_btn_loc = (By.CSS_SELECTOR,"label[for='RhWidth']")
    rh_size_depth_btn_loc = (By.CSS_SELECTOR,"label[for='RhDepth']")
    rh_size_width_select_loc = (By.ID,'ui-id-36')
    rh_size_depth_select_loc = (By.ID,'ui-id-37')
    pelmet_type_loc = (By.CSS_SELECTOR,"label[for='PelmetType']")
    pelmet_type_select_loc = (By.ID,'PelmetTypeShutter')
    pelmet_size_loc = (By.CSS_SELECTOR,"label[for='PelmetSize']")
    pelmet_height_btn_loc = (By.CSS_SELECTOR,"label[for='PelmetHeight']")
    pelmet_height_select_loc = (By.ID,'ui-id-38')
    pelmet_depth_btn_loc = (By.ID,'btnPelmetDepth')
    pelmet_depth_select_loc = (By.ID,'ui-id-39')
    pelmet_colour_loc = (By.CSS_SELECTOR,"label[for='LhCover']")
    pelmet_colour_select_loc = (By.ID,'PelmetColourShutter')
    hardware_colour_category_loc = (By.CSS_SELECTOR,"label[for='HardwareCategory']")
    hardware_colour_category_select_loc = (By.ID,'HardwareCategoryShutter')
    hardware_colour_loc = (By.CSS_SELECTOR,"label[for='Hardware']")
    hardware_colour_select_loc = (By.ID,'HardwareColourShutter')
    track_colour_category_loc = (By.CSS_SELECTOR,"label[for='TrackCategory']")
    track_colour_category_select_loc = (By.ID,'TrackCategoryShutter')
    track_colour_loc = (By.CSS_SELECTOR,"label[for='TrackColour']")
    track_colour_select_loc = (By.ID, 'TrackColourShutter')
    hang_door_other_loc = (By.CSS_SELECTOR,"label[for='HangDoor']")
    hang_door_other_box_loc = (By.ID,'HangDoorOtherShutter')
    fixing_type_other_loc = (By.CSS_SELECTOR,"label[for='FixingType']")
    finxing_type_other_box_loc = (By.ID,'FixingTypeOtherShutter')
    noggins_other_loc = (By.CSS_SELECTOR,"label[for='Noggins']")
    noggins_other_box_loc = (By.ID,'NogginsOtherShutter')

    def go_add_shutter_door(self):
        '''Open the Add a Shutter Door from Quote Page'''
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element(*self.add_door_menu_loc).click()
        self.driver.find_element(*self.add_shutter_btn_loc).click()
        sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[-1])   # switch to the add door details page

    @property
    def check_shutterdoor_page(self):
        '''check the main elements in the page'''
        form_element = self.driver.find_element(*self.door_main_page_loc)
        shutterdoor_title = self.driver.find_element(*self.title_loc).text
        self.driver.execute_script("arguments[0].scrollIntoView(false);", form_element)
        print(shutterdoor_title)
        return shutterdoor_title

    @property
    def check_unit_packaging(self):
        '''check unit and packaging type'''
        unit_number = self.driver.find_element(*self.unit_no_loc).text
        packaging_type = self.driver.find_element(*self.packaging_type_loc).text
        print(unit_number,packaging_type)
        return  unit_number,packaging_type

    @property
    def check_install_details(self):
        '''check each element for install details'''
        install_type = self.driver.find_element(*self.install_type_loc).text
        door_duty_cycle = self.driver.find_element(*self.door_duty_cycle_loc).text
        slat_type = self.driver.find_element(*self.slat_type_loc).text
        slat_design = self.driver.find_element(*self.slat_design_loc).text
        slat_ventilation = self.driver.find_element(*self.slat_ventilation_loc).text
        slat_material = self.driver.find_element(*self.slat_material_loc).text
        slat_finish_ = self.driver.find_element(*self.slat_finish_loc).text
        slat_finish_custom = self.driver.find_element(*self.slat_finish_custom_loc).text
        technician_measure = self.driver.find_element(*self.technician_measure_loc).text
        measure_required = self.driver.find_element(*self.measure_required_loc).text
        print(install_type,door_duty_cycle,slat_type,slat_design,slat_ventilation,slat_material,slat_finish_,
              slat_finish_custom,technician_measure,measure_required)
        return  (install_type,door_duty_cycle,slat_type,slat_design,slat_ventilation,slat_material,slat_finish_,
                 slat_finish_custom,technician_measure,measure_required)


    @property
    def check_install_type(self):
        '''check the install type dropdown'''
        self.driver.find_element(*self.install_type_select_loc).click()
        install_type_list = self.driver.find_element(*self.install_type_select_loc).text
        print(install_type_list)
        return  install_type_list

    @property
    def check_door_duty_cycle(self):
        '''check the Door duty cycle dropdown'''
        self.driver.find_element(*self.door_duty_cycle_select_loc).click()
        door_duty_cycle_list = self.driver.find_element(*self.door_duty_cycle_select_loc).text
        print(door_duty_cycle_list)
        return  door_duty_cycle_list

    @property
    def check_slat_type(self):
        '''check the Slat type'''
        self.driver.find_element(*self.slat_type_select_loc).click()
        slat_type_list = self.driver.find_element(*self.slat_type_select_loc).text
        print(slat_type_list)
        return  slat_type_list

    @property
    def check_slat_design(self):
        '''check the Slat design'''
        self.driver.find_element(*self.slat_design_select_loc).click()
        slat_design_list = self.driver.find_element(*self.slat_design_select_loc).text
        print(slat_design_list)
        return  slat_design_list

    @property
    def check_slat_ventilation(self):
        '''check the Slat ventilation'''
        self.driver.find_element(*self.slat_ventilation_select_loc).click()
        slat_ventilation_list = self.driver.find_element(*self.slat_ventilation_select_loc).text
        print(slat_ventilation_list)
        return  slat_ventilation_list

    @property
    def check_slat_material(self):
        '''check the Slat material'''
        self.driver.find_element(*self.slat_material_select_loc).click()
        slat_material_list = self.driver.find_element(*self.slat_material_select_loc).text
        print(slat_material_list)
        return  slat_material_list

    @property
    def check_slat_finish(self):
        '''check the Slat finish'''
        self.driver.find_element(*self.slat_finish_select_loc).click()
        slat_finish_list = self.driver.find_element(*self.slat_finish_select_loc).text
        print(slat_finish_list)
        return  slat_finish_list

    @property
    def check_technician_measure(self):
        '''check the status for technician_measure checkbox'''
        technician_measure_checkbox = self.driver.find_element(*self.technician_measure_checkbox_loc).get_attribute('value')
        if technician_measure_checkbox == 'true':
            print('enabled')
            return  True
        else:
            print("disable, wrong")
            return  False

    @property
    def check_measure_required(self):
        '''check the status for Measure Required checkbox'''
        measure_required_checkbox = self.driver.find_element(*self.measure_required_checkbox_loc).get_attribute('value')
        if measure_required_checkbox == 'true':
            print('enabled')
            return  True
        else:
            print("disable, wrong")
            return  False

    @property
    def check_size_details(self):
        '''check each element for size details'''
        opensize_lh = self.driver.find_element(*self.opensize_lh_loc).text
        opensize_rh = self.driver.find_element(*self.opensize_rh_loc).text
        opensize_width = self.driver.find_element(*self.opensize_width_loc).text
        sr_left = self.driver.find_element(*self.sr_left_loc).text
        hr = self.driver.find_element(*self.hr_loc).text
        sr_right = self.driver.find_element(*self.sr_right_loc).text
        print(opensize_lh,opensize_rh,opensize_width,sr_left,hr,sr_right)
        return  opensize_lh,opensize_rh,opensize_width,sr_left,hr,sr_right

    @property
    def check_openinglh_default(self):
        '''check the default value for Opening Size LH'''
        openinglh_default = self.driver.find_element(*self.opensize_lh_select_loc).get_attribute('value')
        print(openinglh_default)
        return  openinglh_default

    @property
    def check_openingrh_default(self):
        '''check the default value for Opening Size RH'''
        openingrh_default = self.driver.find_element(*self.opensize_rh_select_loc).get_attribute('value')
        print(openingrh_default)
        return  openingrh_default

    @property
    def check_openingwidth_default(self):
        '''check the default value for Opening Size Width'''
        openingwidth_default = self.driver.find_element(*self.opensize_width_select_loc).get_attribute('value')  #
        print(openingwidth_default)
        return  openingwidth_default

    @property
    def check_srleft_default(self):
        '''check the default value for SR Left'''
        srleft_default = self.driver.find_element(*self.sr_left_select_loc).get_attribute('value')
        print(srleft_default)
        return  srleft_default

    @property
    def check_hr_default(self):
        '''check the default value for HR'''
        hr_default = self.driver.find_element(*self.hr_select_loc).get_attribute('value')
        print(hr_default)
        return  hr_default

    @property
    def check_srright_default(self):
        '''check the default value for SR Right'''
        srright_default = self.driver.find_element(*self.sr_right_select_loc).get_attribute('value')
        print(srright_default)
        return  srright_default

    @property
    def check_additional_fabrication(self):
        '''check each element for additional_fabrication details'''
        additional_fabrication = self.driver.find_element(*self.additional_fabrication_loc).text
        additional_fabrication_required = self.driver.find_element(*self.additional_fabrication_required_loc).text
        shop_drawings = self.driver.find_element(*self.shop_drawings_loc).text
        lifting = self.driver.find_element(*self.lifting_equipment_loc).text
        print(additional_fabrication,additional_fabrication_required,shop_drawings,lifting)
        return  additional_fabrication,additional_fabrication_required,shop_drawings,lifting

    @property
    def check_additional_fabrication_list(self):
        '''check the list for additional_fabrication dropdown'''
        self.driver.find_element(*self.additional_fabrication_select_loc).click()
        additional_fabrication_list = self.driver.find_element(*self.additional_fabrication_select_loc).text
        print(additional_fabrication_list)
        return  additional_fabrication_list

    @property
    def check_shop_drawings_list(self):
        '''check the list for shop drawings dropdown'''
        self.driver.find_element(*self.shop_drawings_select_loc).click()
        shop_drawings_list = self.driver.find_element(*self.shop_drawings_select_loc).text
        print(shop_drawings_list)
        return  shop_drawings_list

    @property
    def check_lifting_equipment_list(self):
        '''check the list for lifting_equipment dropdown'''
        self.driver.find_element(*self.lifting_equipment_btn_loc).click()
        lifting_equipment_list = self.driver.find_element(*self.lifting_equipment_btn_loc).text
        print(lifting_equipment_list)
        return  lifting_equipment_list

    @property
    def check_checkbox_option(self):
        '''check each checkbox option'''
        induction_loop = self.driver.find_element(*self.induction_loop_loc).text
        reverse_rollerdoor = self.driver.find_element(*self.reverse_rollerdoor_loc).text
        eco_wifi = self.driver.find_element(*self.eco_wifi_loc).text
        taper = self.driver.find_element(*self.taper_loc).text
        reverse_rollcolour = self.driver.find_element(*self.reverse_rollcolour_loc).text
        print(induction_loop,reverse_rollerdoor,eco_wifi,taper,reverse_rollcolour)
        return  induction_loop,reverse_rollerdoor,eco_wifi,taper,reverse_rollcolour
    @property
    def check_eco_wifi_checkbox(self):
        '''check the status for Eco wifi checkbox'''
        eco_wifi_checkbox = self.driver.find_element(*self.eco_wifi_checkbox_loc)
        if eco_wifi_checkbox.is_enabled():
            print('enabled,wrong')
            return  False
        else:
            print("disable, correct")
            return  True

    @property
    def check_operation_details(self):
            '''check operation_details'''
            operation_side = self.driver.find_element(*self.operation_side_loc).text
            operation_type = self.driver.find_element(*self.operation_type_loc).text
            battery_backup = self.driver.find_element(*self.battery_backup_loc).text
            print(operation_side,operation_type,battery_backup)
            return operation_side,operation_type,battery_backup

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
        print(opener,handsets_no,wall_btn,opener_details,digital_keypad,internal_push_btn,pe_beam,pe_beam_sets)
        return  opener,handsets_no,wall_btn,opener_details,digital_keypad,internal_push_btn,pe_beam,pe_beam_sets

    @property
    def check_opener_list(self):
        '''check the list for Opener dropdown'''
        self.driver.find_element(*self.opener_select_loc).click()
        opener_list = self.driver.find_element(*self.opener_select_loc).text
        print(opener_list)
        return  opener_list

    @property
    def check_handsets_default(self):
        '''check the default value for Handsets'''
        handsets_default = self.driver.find_element(*self.handsets_select_loc).get_attribute('value')
        print(handsets_default)
        return  handsets_default

    @property
    def check_wallbtn_default(self):
        '''check the default value for Wall button'''
        wallbtn_default = self.driver.find_element(*self.wall_btn_select_loc).get_attribute('value')
        print(wallbtn_default)
        return  wallbtn_default

    @property
    def check_digital_keypad_default(self):
        '''check the default value for Digital Keypad'''
        digital_keypad_default = self.driver.find_element(*self.digital_keypad_select_loc).get_attribute('value')
        print(digital_keypad_default)
        return  digital_keypad_default

    @property
    def check_pushbtn_default(self):
        '''check the default value for Internal Push'''
        pushbtn_default = self.driver.find_element(*self.internal_pushbtn_select_loc).get_attribute('value')
        print(pushbtn_default)
        return  pushbtn_default

    @property
    def check_beam_set_default(self):
        '''check the default value for PE Beam Sets'''
        beam_set_default = self.driver.find_element(*self.pe_beam_sets_select_loc).get_attribute('value')
        print(beam_set_default)
        return  beam_set_default

    @property
    def check_pe_beam_list(self):
        '''check the list for PE Beam dropdown'''
        self.driver.find_element(*self.pe_beam_select_loc).click()
        pe_beam_list = self.driver.find_element(*self.pe_beam_select_loc).text
        print(pe_beam_list)
        return  pe_beam_list

    @property
    def check_other_details(self):
        '''check each element for other elements'''
        windlock = self.driver.find_element(*self.windlock_loc).text
        track = self.driver.find_element(*self.track_loc).text
        remove_and_dispose = self.driver.find_element(*self.remove_and_dispose_loc).text
        seals = self.driver.find_element(*self.seals_loc).text
        hang_door_from = self.driver.find_element(*self.hang_door_loc).text
        lintel_type = self.driver.find_element(*self.lintel_type_loc).text
        fixing_type = self.driver.find_element(*self.fixing_type_loc).text
        door_area = self.driver.find_element(*self.door_area_loc).text
        door_status = self.driver.find_element(*self.door_status_loc).text
        expected_delivery_date = self.driver.find_element(*self.expected_deliverydate_loc).text
        print(windlock,track,remove_and_dispose,seals,hang_door_from,lintel_type, fixing_type,door_area,door_status,
              expected_delivery_date)
        return  (windlock,track,remove_and_dispose,seals,hang_door_from,lintel_type, fixing_type,door_area,door_status,
                 expected_delivery_date)

    @property
    def check_other_extras_value(self):
        '''check each element for other extras and values'''
        other_extras = self.driver.find_element(*self.other_extras_loc).text
        value = self.driver.find_element(*self.value_loc).text
        additional_info = self.driver.find_element(*self.additional_info_loc).text
        production_notes = self.driver.find_element(*self.production_notes_loc).text
        print(other_extras,value,additional_info,production_notes)
        return  other_extras,value,additional_info,production_notes



    @property
    def check_extras_jamb(self):
        '''check each element for jamb and pelmet of extras section'''
        self.driver.find_element(*self.extras_loc).click()
        form_element = self.driver.find_element(*self.door_main_page)
        self.driver.execute_script("arguments[0].scrollIntoView(false);", form_element)
        lh_jamb = self.driver.find_element(*self.lh_jamb_loc).text
        lh_size = self.driver.find_element(*self.lh_size_loc).text
        rh_jamb = self.driver.find_element(*self.rh_jamb_loc).text
        rh_size = self.driver.find_element(*self.rh_size_loc).text
        pelmet_type = self.driver.find_element(*self.pelmet_type_loc).text
        pelmet_size = self.driver.find_element(*self.pelmet_size_loc).text
        pelmet_colour = self.driver.find_element(*self.pelmet_colour_loc).text
        # print(lh_jamb,lh_size,rh_jamb,rh_size,pelmet_type,pelmet_size,pelmet_colour)
        return  lh_jamb,lh_size,rh_jamb,rh_size,pelmet_type,pelmet_size,pelmet_colour

    @property
    def lh_jamb_type(self):
        '''check the list for LH JAMB Type'''
        self.driver.find_element(*self.extras_loc).click()
        form_element = self.driver.find_element(*self.door_main_page)
        self.driver.execute_script("arguments[0].scrollIntoView(false);", form_element)
        self.driver.find_element(*self.lh_jamb_select_loc).click()
        lh_jambtype_list = self.driver.find_element(*self.lh_jamb_select_loc).text
        self.driver.find_element(*self.extras_loc).click()
        print(lh_jambtype_list)
        return  lh_jambtype_list

    @property
    def lh_jamb_width(self):
        '''check the list for LH JAMB Width Size'''
        self.driver.find_element(*self.extras_loc).click()
        form_element = self.driver.find_element(*self.door_main_page)
        self.driver.execute_script("arguments[0].scrollIntoView(false);", form_element)
        self.driver.find_element(*self.lh_size_width_btn_loc).click()
        lh_width_list = self.driver.find_element(*self.lh_size_width_select_loc).text
        # self.driver.find_element(*self.extras_loc).click()
        print(lh_width_list)
        return  lh_width_list

    @property
    def lh_jamb_depth(self):
        '''check the list for LH JAMB Depth Size'''
        # self.driver.find_element(*self.extras_loc).click()
        # form_element = self.driver.find_element(*self.door_main_page)
        # self.driver.execute_script("arguments[0].scrollIntoView(false);", form_element)
        sleep(1)
        self.driver.find_element(*self.lh_size_depth_btn_loc).click()
        lh_depth_list = self.driver.find_element(*self.lh_size_depth_select_loc).text
        # self.driver.find_element(*self.extras_loc).click()
        print(lh_depth_list)
        return  lh_depth_list

    @property
    def rh_jamb_type(self):
        '''check the list for RH JAMB Type'''
        # self.driver.find_element(*self.extras_loc).click()
        # form_element = self.driver.find_element(*self.door_main_page)
        # self.driver.execute_script("arguments[0].scrollIntoView(false);", form_element)
        # sleep(2)
        self.driver.find_element(*self.rh_jamb_select_loc).click()
        rh_jambtype_list = self.driver.find_element(*self.rh_jamb_select_loc).text
        # self.driver.find_element(*self.extras_loc).click()
        print(rh_jambtype_list)
        return  rh_jambtype_list

    @property
    def rh_jamb_width(self):
        '''check the list for RH JAMB Width Size'''
        # self.driver.find_element(*self.extras_loc).click()
        # form_element = self.driver.find_element(*self.door_main_page)
        # self.driver.execute_script("arguments[0].scrollIntoView(false);", form_element)
        self.driver.find_element(*self.rh_size_width_btn_loc).click()
        rh_width_list = self.driver.find_element(*self.rh_size_width_select_loc).text
        # self.driver.find_element(*self.extras_loc).click()
        print(rh_width_list)
        return  rh_width_list

    @property
    def rh_jamb_depth(self):
        '''check the list for RH JAMB Depth Size'''
        # self.driver.find_element(*self.extras_loc).click()
        # form_element = self.driver.find_element(*self.door_main_page)
        # self.driver.execute_script("arguments[0].scrollIntoView(false);", form_element)
        sleep(1)
        self.driver.find_element(*self.rh_size_depth_btn_loc).click()
        rh_depth_list = self.driver.find_element(*self.rh_size_depth_select_loc).text
        # self.driver.find_element(*self.extras_loc).click()
        print(rh_depth_list)
        return  rh_depth_list

    @property
    def pelmet_type(self):
        '''check the list for Pelmet Type'''
        # self.driver.find_element(*self.extras_loc).click()
        # form_element = self.driver.find_element(*self.door_main_page)
        # self.driver.execute_script("arguments[0].scrollIntoView(false);", form_element)
        # sleep(2)
        self.driver.find_element(*self.pelmet_type_select_loc).click()
        pelmet_type_list = self.driver.find_element(*self.pelmet_type_select_loc).text
        # self.driver.find_element(*self.extras_loc).click()
        print(pelmet_type_list)
        return  pelmet_type_list

    @property
    def pelmet_height(self):
        '''check the list for Pelmet Width Size'''
        # self.driver.find_element(*self.extras_loc).click()
        # form_element = self.driver.find_element(*self.door_main_page)
        # self.driver.execute_script("arguments[0].scrollIntoView(false);", form_element)
        self.driver.find_element(*self.pelmet_height_btn_loc).click()
        pelmet_height_list = self.driver.find_element(*self.pelmet_height_select_loc).text
        # self.driver.find_element(*self.extras_loc).click()
        print(pelmet_height_list)
        return  pelmet_height_list

    @property
    def pelmet_depth(self):
        '''check the list for Pelmet Depth Size'''
        # self.driver.find_element(*self.extras_loc).click()
        # form_element = self.driver.find_element(*self.door_main_page)
        # self.driver.execute_script("arguments[0].scrollIntoView(false);", form_element)
        sleep(1)
        self.driver.find_element(*self.pelmet_depth_btn_loc).click()
        pelmet_depth_list = self.driver.find_element(*self.pelmet_depth_select_loc).text
        # self.driver.find_element(*self.extras_loc).click()
        print(pelmet_depth_list)
        return  pelmet_depth_list

    @property
    def pelmet_colour(self):
        '''check the list for Pelmet Colour list'''
        # self.driver.find_element(*self.extras_loc).click()
        # form_element = self.driver.find_element(*self.door_main_page)
        # self.driver.execute_script("arguments[0].scrollIntoView(false);", form_element)
        sleep(1)
        self.driver.find_element(*self.pelmet_colour_select_loc).click()
        pelmet_colour_list = self.driver.find_element(*self.pelmet_colour_select_loc).text
        # self.driver.find_element(*self.extras_loc).click()
        print(pelmet_colour_list)
        return  pelmet_colour_list

    @property
    def hardware_colour_category(self):
        '''check the list for Hardware Colour Category list'''
        # self.driver.find_element(*self.extras_loc).click()
        # form_element = self.driver.find_element(*self.door_main_page)
        # self.driver.execute_script("arguments[0].scrollIntoView(false);", form_element)
        sleep(1)
        self.driver.find_element(*self.hardware_colour_category_select_loc).click()
        hardware_colour_category_list = self.driver.find_element(*self.hardware_colour_category_select_loc).text
        # self.driver.find_element(*self.extras_loc).click()
        print(hardware_colour_category_list)
        return  hardware_colour_category_list

    @property
    def track_colour_category(self):
        '''check the list for Track Colour Category list'''
        # self.driver.find_element(*self.extras_loc).click()
        # form_element = self.driver.find_element(*self.door_main_page)
        # self.driver.execute_script("arguments[0].scrollIntoView(false);", form_element)
        sleep(1)
        self.driver.find_element(*self.track_colour_category_select_loc).click()
        track_colour_category_list = self.driver.find_element(*self.track_colour_category_select_loc).text
        # self.driver.find_element(*self.extras_loc).click()
        print(track_colour_category_list)
        return  track_colour_category_list

if __name__ == '__main__':
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get("http:// ")
        driver.implicitly_wait(10)

        login = Shutter_Door(driver)
        login.typeUserName('aa@ecogaragedoors.com')
        login.typePassword('aabb')
        login.clickLogin()
        login.go_addquote()
        login.go_add_shutter_door()
        # login.check_shutterdoor_page
        # login.check_unit_packaging
        # login.check_install_details
        # login.check_install_type
        # login.check_door_duty_cycle
        # login.check_slat_type
        # login.check_slat_design
        # login.check_slat_ventilation
        # login.check_slat_material
        # login.check_slat_finish
        # login.check_technician_measure
        # login.check_size_details
        # login.check_openinglh_default
        # login.check_additional_fabrication
        # login.check_additional_fabrication_list
        # login.check_shop_drawings_list
        # login.check_lifting_equipment_list
        # login.check_checkbox_option
        # login.check_eco_wifi_checkbox
        # login.check_operation_details
        login.check_opener_details
        # login.check_opener_list
        # login.check_handsets_default
        # login.check_pe_beam_list
        # login.check_other_details
        # login.check_other_extras_value
        # login.check_extras_jamb
        # login.lh_jamb_type
        # login.lh_jamb_width
        # login.lh_jamb_depth
        # login.rh_jamb_type
        # login.rh_jamb_width
        # login.rh_jamb_depth
        # login.pelmet_type
        # login.pelmet_height
        # login.pelmet_depth
        # login.pelmet_colour
        # login.hardware_colour_category
        # login.track_colour_category
