# Author:Yi Sun(Tim) 2025-08-12

'''Add Standard Door Details Page'''

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from UIModule.add_quote import *

class Standard_Door(Add_Quote):

    standard_door_menu = (By.ID,'add-door-btn')
    add_standarddoor_btn = (By.ID,'btnDoorAdd')
    close_standarddoor_btn = (By.ID,'btnDoorClose')
    door_main_page = (By.XPATH, '//*[@id="main"]/div/span')

    '''loc for each element for install details'''
    title_loc = (By.NAME, 'QuoteTitle')
    storage_bay_no_loc = (By.NAME, 'StorageBay')
    unit_no_loc = (By.NAME, 'UnitNum')
    unit_no_inputbox = (By.ID,'UnitNumber')
    packaging_type_loc = (By.NAME,'PackagingType')
    packaging_type_select = (By.ID,'PackagingType')

    install_type_loc = (By.NAME,'InstallTypeStandardEdit')
    install_type_select = (By.ID,'InstallTypeStandard')
    door_type_loc = (By.NAME,'DoorTypeEdit')
    door_type_select = (By.ID,'DoorType')
    design_loc = (By.NAME,'DesignEdit')
    design_select = (By.ID,'Door_Design')
    colour_category_loc = (By.NAME,'CategoryEdit')
    colour_category_select = (By.ID,'Door_Color_Category')
    door_colour_loc = (By.NAME,'ColorEdit')
    door_colour_select = (By.ID,'DoorColor')
    door_finish_loc = (By.NAME,'FinishEdit')
    door_finish_select = (By.ID,'DoorFinish')
    custom_colour_loc = (By.NAME,'CustomColorEdit')
    custom_colour_inputbox = (By.ID,'Door_Custom_Color')
    tech_measure_loc = (By.NAME,'TechEdit')
    measure_require_loc = (By.NAME,'MeasureEdit')

    '''loc for each element for SIZE details'''
    opensize_lh_loc = (By.NAME,'OpeningSizeLHEdit')
    opensize_lh_select = (By.ID,'OpeningSizeLH')
    opensize_rh_loc = (By.NAME,'OpeningSizeRHEdit')
    opensize_rh_select = (By.ID,'OpeningSizeRH')
    opensize_width_loc = (By.NAME,'OpeningSizeWidthEdit')
    opensize_width_select =(By.ID,'OpeningSizeWidth')
    sr_left_loc = (By.NAME,'SRLeftEdit')
    sr_left_select =(By.ID,'SR_left')
    hr_loc = (By.NAME,'HREdit')
    hr_select = (By.ID,'HR')
    sr_right_loc = (By.NAME,'SRRightEdit')
    sr_right_select =(By.ID,'SR_right')
    lhrk_loc = (By.NAME,'LHRKEdit')
    lhrk_select = (By.ID,'LHRK')
    sms_bracket_loc = (By.NAME,'SMSEdit')
    lsr_kit_loc = (By.NAME,'LsrEdit')
    timber_packers_loc = (By.NAME,'TimberPackersEdit')
    timber_packers_select = (By.ID,'TimberPackers')
    taper_loc = (By.NAME,'TapeEdit')
    taper_select = (By.ID,'Taper')
    additional_fabrication_loc = (By.NAME,'HeavyAngleEdit')
    additional_fabrication_select = (By.ID,'HeavyAngle')
    additional_fabrication_required_loc = (By.NAME,'HeavyAngleDetailsEdit')
    additional_fabrication_required_inputbox = (By.ID,'HeavyAngleDetails')
    shop_drawings_loc = (By.NAME,'ShopDrawingsEdit')
    shop_drawings_select = (By.ID,'ShopDrawings')
    lifting_equipment_loc = (By.NAME,'LiftEdit')
    lifting_equipment_btn = (By.ID,'btnLift')

    '''loc for each element for checkboxes details'''
    induction_loop_loc = (By.XPATH,'//*[@id="induction"]/div/div[1]')
    induction_loop_box_loc = (By.ID,'IsInductionLoopStandard')
    fully_sloctted_loc = (By.XPATH,'//*[@id="sloctted"]/div/div[1]/div[2]/span')
    fully_slotted_box_loc = (By.ID,'IsFullySlottedStandard')
    emergency_key_loc = (By.XPATH,'//*[@id="emergency"]/div/div[2]/span')
    emergency_key_box_loc = (By.ID,'PriceEmergencyKeyRelease')
    reverse_colour_loc = (By.XPATH,'//*[@id="reversecolour"]/div/div[2]/span')
    reverse_colour_box_loc = (By.ID,'IsReverseColourStandard')
    battery_backup_loc = (By.XPATH,'//*[@id="battery"]/div/div[3]/span')
    battery_backup_box_loc = (By.ID,'IsBatteryBackupStandard')
    eco_wifi_loc = (By.XPATH,'//*[@id="ecowifi"]/div/div[2]/span')
    eco_wifi_box_loc = (By.ID,'IsWiFi')

    '''loc for Opener details'''
    opener_loc = (By.XPATH,'//*[@id="opener"]/div/div[1]/div[2]/span')
    opener_select = (By.ID,'Motors')
    handsets_loc = (By.XPATH,'//*[@id="handsets"]/div/div[1]/div[2]/span')
    handsets_select = (By.ID,'Handset')
    wall_btn_loc = (By.XPATH,'//*[@id="wallbtn"]/div/div[1]/span')
    wall_btn_select = (By.ID,'Door_Wall_Button')
    opener_detail_loc = (By.XPATH,'//*[@id="motorsother"]/div/div[2]/span')
    opener_detail_box = (By.ID,'MotorsOther')
    digital_keypad_loc = (By.XPATH,'//*[@id="keypad"]/div/div[1]')
    digital_keypad_select = (By.ID,'DigitalKeypad')
    internal_pushbtn_loc = (By.XPATH,'//*[@id="pushbtn"]/div/div[2]')
    internal_pushbtn_select = (By.ID,'InternalPushButton')
    pe_beam_loc = (By.XPATH,'//*[@id="pe_beam"]/div/div[2]/span')
    pe_beam_select = (By.ID,'PEBeamGeneral')
    pe_beam_sets_loc = (By.XPATH,'//*[@id="beam_sets"]/div/div[2]/span')
    pe_beam_sets_select = (By.ID,'PEBeamSetsGeneral')
    keys_loc = (By.XPATH,'//*[@id="keys"]/div/div[2]/span')
    keys_select = (By.ID,'Keys')

    '''loc for other elements details '''
    weight_added_loc = (By.CSS_SELECTOR,"label[for='WeightBeingAdded']")
    weight_added_select = (By.ID,'WeightAddedStandard')
    seals_loc = (By.CSS_SELECTOR,"label[for='CustomSeals']")
    seals_select = (By.ID,'Seals')
    dealer_seals2500_loc = (By.CSS_SELECTOR,"label[for='CustomSeals2500']")
    dealer_seals3000_loc = (By.CSS_SELECTOR,"label[for='CustomSeals3000']")
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


    def go_addstandarddoor(self):
        '''Open the Add Standard Door from Quote Page'''
        Select(self.driver.find_element(*self.supply_type_select)).select_by_visible_text(
            'WA – Install')  # set the supply type to WA
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        standard_door_add = self.driver.find_element(*self.add_door_btn)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(standard_door_add)).click()
        self.driver.find_element(*self.standard_door_menu).click()
        self.driver.switch_to.window(self.driver.window_handles[-1])   # switch to the add door details page

    @property
    def check_door_page(self):
        '''check the main elements in the page'''
        form_element = self.driver.find_element(*self.door_main_page)
        standarddoor_title = self.driver.find_element(*self.title_loc).text
        self.driver.execute_script("arguments[0].scrollIntoView(false);", form_element)
        add_button = self.driver.find_element(*self.add_standarddoor_btn).text
        print(standarddoor_title,add_button)
        return standarddoor_title,add_button

    @property
    def check_install_details(self):
        '''check each element for install details'''
        install_type = self.driver.find_element(*self.install_type_loc).text
        door_type = self.driver.find_element(*self.door_type_loc).text
        design = self.driver.find_element(*self.design_loc).text
        colour_category = self.driver.find_element(*self.colour_category_loc).text
        door_colour = self.driver.find_element(*self.door_colour_loc).text
        door_finish = self.driver.find_element(*self.door_finish_loc).text
        custom_colour = self.driver.find_element(*self.custom_colour_loc).text
        tech_measure = self.driver.find_element(*self.tech_measure_loc).text
        measure_require = self.driver.find_element(*self.measure_require_loc).text
        print(install_type,door_type,design,colour_category,door_colour,door_finish,custom_colour,tech_measure,
              measure_require)
        return  (install_type,door_type,design,colour_category,door_colour,door_finish,custom_colour,tech_measure,
                 measure_require)

    @property
    def check_install_type(self):
        '''check the install type dropdown'''
        self.driver.find_element(*self.install_type_select).click()
        install_type_list = self.driver.find_element(*self.install_type_select).text
        print(install_type_list)
        return  install_type_list

    @property
    def check_door_type(self):
        '''check the Door type dropdown'''
        self.driver.find_element(*self.door_type_select).click()
        door_type_list = self.driver.find_element(*self.door_type_select).text
        print(door_type_list)
        return  door_type_list

    @property
    def check_colour_category(self):
        '''check the Colour Category dropdown'''
        self.driver.find_element(*self.colour_category_select).click()
        colour_category_list = self.driver.find_element(*self.colour_category_select).text
        print(colour_category_list)
        return  colour_category_list

    @property
    def check_design_panel(self):
        '''check the Design dropdown for Panel Lift-Safe Door'''
        global door_type
        door_type = Select(self.driver.find_element(*self.door_type_select))
        panel_lift_safe = door_type.select_by_visible_text('Panel Lift-Safe')
        self.driver.find_element(*self.design_select).click()
        design_list = self.driver.find_element(*self.design_select).text
        print(design_list)
        return  design_list

    @property
    def check_design_insulated(self):
        '''check the Design dropdown for Insulated Sectional Door'''
        door_type = Select(self.driver.find_element(*self.door_type_select))
        insulated_sectional= door_type.select_by_visible_text('Insulated Sectional')
        self.driver.find_element(*self.design_select).click()
        design_list = self.driver.find_element(*self.design_select).text
        print(design_list)
        return  design_list

    @property
    def check_design_roller(self):
        '''check the Design dropdown for Roller Door'''
        door_type = Select(self.driver.find_element(*self.door_type_select))
        roller_door= door_type.select_by_visible_text('ExoRoll')
        self.driver.find_element(*self.design_select).click()
        design_list = self.driver.find_element(*self.design_select).text
        door_type.select_by_visible_text('Please Select')
        print(design_list)
        return  design_list

    @property
    def check_design_optilift(self):
        '''check the Design dropdown for OptiLift Door'''
        door_type = Select(self.driver.find_element(*self.door_type_select))
        roller_door= door_type.select_by_visible_text('OptiLift')
        sleep(3)
        self.driver.find_element(*self.design_select).click()
        design_list = self.driver.find_element(*self.design_select).text
        door_type.select_by_visible_text('Please Select')
        print(design_list)
        return  design_list

    @property
    def check_design_optiroll(self):
        '''check the Design dropdown for OptiLift Door'''
        door_type = Select(self.driver.find_element(*self.door_type_select))
        roller_door= door_type.select_by_visible_text('OptiRoll')
        sleep(3)
        self.driver.find_element(*self.design_select).click()
        design_list = self.driver.find_element(*self.design_select).text
        door_type.select_by_visible_text('Please Select')
        print(design_list)
        return  design_list

    @property
    def check_colour_colorbond(self):
        '''check the Door Colour dropdown for ColorBond Category'''
        global colour_category
        colour_category = Select(self.driver.find_element(*self.colour_category_select))
        colorbond = colour_category.select_by_visible_text('ColorBond')
        self.driver.find_element(*self.door_colour_select).click()
        sleep(1)
        door_colour_list = self.driver.find_element(*self.door_colour_select).text
        print(door_colour_list)
        return  door_colour_list

    @property
    def check_colour_custom(self):
        '''check the Door Colour dropdown for Custom Category'''
        colour_category = Select(self.driver.find_element(*self.colour_category_select))
        custom = colour_category.select_by_visible_text('Custom')
        custom_colour = self.driver.find_element(*self.door_colour_select)
        if custom_colour.is_enabled():
            print('wrong')
            return  False
        else:
            print('correct')
            return True

    @property
    def check_colour_flexigraphic(self):
        '''check the Door Colour dropdown for Flexigraphic Category'''
        colour_category = Select(self.driver.find_element(*self.colour_category_select))
        flexigraphic = colour_category.select_by_visible_text('Flexigraphic')
        self.driver.find_element(*self.door_colour_select).click()
        door_colour_list = self.driver.find_element(*self.door_colour_select).text
        print(door_colour_list)
        return  door_colour_list

    @property
    def check_colour_flexographic(self):
        '''check the Door Colour dropdown for Flexographic Category'''
        colour_category = Select(self.driver.find_element(*self.colour_category_select))
        flexographic = colour_category.select_by_visible_text('Flexographic')
        self.driver.find_element(*self.door_colour_select).click()
        door_colour_list = self.driver.find_element(*self.door_colour_select).text
        print(door_colour_list)
        return  door_colour_list

    @property
    def check_colour_metalfx(self):
        '''check the Door Colour dropdown for MetalFx Category'''
        colour_category = Select(self.driver.find_element(*self.colour_category_select))
        metalfx = colour_category.select_by_visible_text('MetalFx')
        self.driver.find_element(*self.door_colour_select).click()
        sleep(1)
        door_colour_list = self.driver.find_element(*self.door_colour_select).text
        print(door_colour_list)
        return  door_colour_list

    @property
    def check_colour_paintedfinish(self):
        '''check the Door Colour dropdown for PaintedFinish Category'''
        colour_category = Select(self.driver.find_element(*self.colour_category_select))
        paintedfinish = colour_category.select_by_visible_text('Painted Finish')
        self.driver.find_element(*self.door_colour_select).click()
        door_colour_list = self.driver.find_element(*self.door_colour_select).text
        print(door_colour_list)
        return  door_colour_list

    @property
    def check_colour_portabella(self):
        '''check the Door Colour dropdown for Portabella Category'''
        colour_category = Select(self.driver.find_element(*self.colour_category_select))
        portabella = colour_category.select_by_visible_text('Portabella')
        self.driver.find_element(*self.door_colour_select).click()
        door_colour_list = self.driver.find_element(*self.door_colour_select).text
        print(door_colour_list)
        return  door_colour_list

    @property
    def check_colour_timberfx(self):
        '''check the Door Colour dropdown for TimberFX Category'''
        colour_category = Select(self.driver.find_element(*self.colour_category_select))
        timberfx = colour_category.select_by_visible_text('TimberFX')
        self.driver.find_element(*self.door_colour_select).click()
        sleep(1)
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
            if custom_colour_box.is_enabled():
                print('correct')
                colour_category1.select_by_visible_text('Please Select')
                return True
            else:
                print('wrong')
                colour_category1.select_by_visible_text('Please Select')
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
        print(opensize_lh,opensize_rh,opensize_width,sr_left,hr,sr_right,lhrk)
        return  opensize_lh,opensize_rh,opensize_width,sr_left,hr,sr_right,lhrk

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
        sleep(1)
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
        # reverse_install = self.driver.find_element(*self.reverse_install_loc).text
        fully_slotted = self.driver.find_element(*self.fully_sloctted_loc).text
        emergency_key = self.driver.find_element(*self.emergency_key_loc).text
        reverse_colour = self.driver.find_element(*self.reverse_colour_loc).text
        battery_backup = self.driver.find_element(*self.battery_backup_loc).text
        eco_wifi = self.driver.find_element(*self.eco_wifi_loc).text
        print(induction_loop,fully_slotted,emergency_key,reverse_colour,battery_backup,eco_wifi)
        return  induction_loop,fully_slotted,emergency_key,reverse_colour,battery_backup,eco_wifi

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
        seals_2500 = self.driver.find_element(*self.dealer_seals2500_loc).text
        seals_3000 = self.driver.find_element(*self.dealer_seals3000_loc).text
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
        print(weight_being_added,seals,seals_2500,seals_3000,hang_door_from,lintel_type,
                 fixing_type,ibeam_noggins,remove_dispose,job_status,expected_delivery_date,cut_date,
                 paint_date,qc_date,other_date)
        return  (weight_being_added,seals,seals_2500,seals_3000,hang_door_from,lintel_type,
                 fixing_type,ibeam_noggins,remove_dispose,job_status,expected_delivery_date,cut_date,
                 paint_date,qc_date,other_date)

    @property
    def check_additional_details(self):
        '''check each element for additional information elements'''
        additional_info  = self.driver.find_element(*self.additional_info_loc).text
        production_notes = self.driver.find_element(*self.production_notes_loc).text
        print(additional_info,production_notes)
        return  additional_info,production_notes


    @property
    def check_default_doorfinish(self):
        '''check the default options in Door Finish dropdown'''
        door_type_select = Select(self.driver.find_element(*self.door_type_select))
        door_type_select.select_by_visible_text("Panel Lift-Safe")
        self.driver.find_element(*self.door_finish_select).click()
        door_finish_list = self.driver.find_element(*self.door_finish_select).text
        # print(door_finish_list)
        return  door_finish_list

    @property
    def check_classic_doorfinish(self):
        '''check the Door finish option for Classic door'''
        door_type_select = Select(self.driver.find_element(*self.door_type_select))
        door_type_select.select_by_visible_text("Panel Lift-Safe")
        Select(self.driver.find_element(*self.design_select)).select_by_visible_text("Classic panel")
        self.driver.find_element(*self.door_finish_select).click()
        classic_door_finish= self.driver.find_element(*self.door_finish_select).text
        print(classic_door_finish)
        return  classic_door_finish

    @property
    def check_slimline_doorfinish(self):
        '''check the Door finish option for Slimline door'''
        # door_type_select = Select(self.driver.find_element(*self.door_type_select))
        # door_type_select.select_by_visible_text("Panel Lift-Safe")
        Select(self.driver.find_element(*self.design_select)).select_by_visible_text("Slimline")
        self.driver.find_element(*self.door_finish_select).click()
        slimline_door_finish= self.driver.find_element(*self.door_finish_select).text
        print(slimline_door_finish)
        return  slimline_door_finish

    @property
    def check_lincoln_doorfinish(self):
        '''check the Door finish option for Lincoln panel door'''
        # door_type_select = Select(self.driver.find_element(*self.door_type_select))
        # door_type_select.select_by_visible_text("Panel Lift-Safe")
        Select(self.driver.find_element(*self.design_select)).select_by_visible_text("Lincoln panel")
        self.driver.find_element(*self.door_finish_select).click()
        lincoln_door_finish= self.driver.find_element(*self.door_finish_select).text
        print(lincoln_door_finish)
        return  lincoln_door_finish

    @property
    def check_ultraline_doorfinish(self):
        '''check the Door finish option for Ultraline panel door'''
        # door_type_select = Select(self.driver.find_element(*self.door_type_select))
        # door_type_select.select_by_visible_text("Panel Lift-Safe")
        Select(self.driver.find_element(*self.design_select)).select_by_visible_text("Ultraline")
        self.driver.find_element(*self.door_finish_select).click()
        ultraline_door_finish= self.driver.find_element(*self.door_finish_select).text
        print(ultraline_door_finish)
        return  ultraline_door_finish

    @property
    def check_wideline_doorfinish(self):
        '''check the Door finish option for Wideline panel door'''
        # door_type_select = Select(self.driver.find_element(*self.door_type_select))
        # door_type_select.select_by_visible_text("Panel Lift-Safe")
        Select(self.driver.find_element(*self.design_select)).select_by_visible_text("Wideline")
        self.driver.find_element(*self.door_finish_select).click()
        wideline_door_finish= self.driver.find_element(*self.door_finish_select).text
        print(wideline_door_finish)
        return  wideline_door_finish

    @property
    def reverse_colour_panel(self):
        '''Check the reverse colour box status for Panel Lift door, should be disabled'''
        Select(self.driver.find_element(*self.design_select)).select_by_visible_text("Please Select")
        reverse_colour_panel = self.driver.find_element(*self.reverse_colour_box_loc)
        if reverse_colour_panel.is_enabled():
            print("'it's enabled, wrong")
            return False
        else:
            print("it's disabled,correct")
            return True

    @property
    def fully_slotted_panel(self):
        '''Check the Fully Slotted box status for Panel Lift door, should be disabled'''
        # Select(self.driver.find_element(*self.design_select)).select_by_visible_text("Please Select")
        fully_slotted_panel = self.driver.find_element(*self.fully_slotted_box_loc)
        if fully_slotted_panel.is_enabled():
            print("'it's enabled, wrong")
            return False
        else:
            print("it's disabled,correct")
            return True

    @property
    def induction_loop_panel(self):
        '''Check the Induction Loop box status for Panel Lift door, should be enabled'''
        # Select(self.driver.find_element(*self.design_select)).select_by_visible_text("Please Select")
        induction_loop_panel = self.driver.find_element(*self.induction_loop_box_loc)
        if induction_loop_panel.is_enabled():
            print("'it's enabled, correct")
            return True
        else:
            print("it's disabled,correct")
            return False

    @property
    def emergency_key_panel(self):
        '''Check the Emergency Key Release box status for Panel Lift door, should be enabled'''
        # Select(self.driver.find_element(*self.design_select)).select_by_visible_text("Please Select")
        emergency_key_panel = self.driver.find_element(*self.emergency_key_box_loc)
        if emergency_key_panel.is_enabled():
            print("'it's enabled, correct")
            return True
        else:
            print("it's disabled,correct")
            return False

    @property
    def smart_wifi_panel(self):
        '''Check the ECO Smart wifi box status for Panel Lift door, should be enabled'''
        # Select(self.driver.find_element(*self.design_select)).select_by_visible_text("Please Select")
        smart_wifi_panel = self.driver.find_element(*self.eco_wifi_box_loc)
        if smart_wifi_panel.is_enabled():
            print("'it's enabled, correct")
            return True
        else:
            print("it's disabled,correct")
            return False

    @property
    def battery_backup_panel(self):
        '''Check the Battery Backup box status for Panel Lift door, should be enabled'''
        # Select(self.driver.find_element(*self.design_select)).select_by_visible_text("Please Select")
        battery_backup_panel = self.driver.find_element(*self.battery_backup_box_loc)
        if battery_backup_panel.is_enabled():
            print("'it's enabled, correct")
            return True
        else:
            print("it's disabled,correct")
            return False

    @property
    def reverse_colour_roller(self):
        '''Check the reverse colour box status for Roller door, should be enabled'''
        Select(self.driver.find_element(*self.door_type_select)).select_by_visible_text("ExoRoll")
        reverse_colour_roller = self.driver.find_element(*self.reverse_colour_box_loc)
        if reverse_colour_roller.is_enabled():
            print("'it's enabled, correct")
            return True
        else:
            print("it's disabled,wrong")
            return False

    @property
    def fully_slotted_roller(self):
        '''Check the Fully Slotted box status for Roller door, should be disabled'''
        # Select(self.driver.find_element(*self.design_select)).select_by_visible_text("Please Select")
        fully_slotted_roller = self.driver.find_element(*self.fully_slotted_box_loc)
        if fully_slotted_roller.is_enabled():
            print("'it's enabled, wrong")
            return False
        else:
            print("it's disabled,correct")
            return True

    @property
    def reverse_colour_insulated(self):
        '''Check the reverse colour box status for Insulated Sectional door, should be disabled'''
        Select(self.driver.find_element(*self.door_type_select)).select_by_visible_text("Insulated Sectional")
        reverse_colour_insulated = self.driver.find_element(*self.reverse_colour_box_loc)
        if reverse_colour_insulated.is_enabled():
            print("'it's enabled, wrong")
            return False
        else:
            print("it's disabled,correct")
            return True

    @property
    def fully_slotted_insulated(self):
        '''Check the Fully Slotted box status for Insulated Sectional door, should be disabled'''
        # Select(self.driver.find_element(*self.design_select)).select_by_visible_text("Please Select")
        fully_slotted_insulated = self.driver.find_element(*self.fully_slotted_box_loc)
        if fully_slotted_insulated.is_enabled():
            print("'it's enabled, wrong")
            return False
        else:
            print("it's disabled,correct")
            return True

if __name__ == '__main__':
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get("http:// ")
        driver.implicitly_wait(10)

        login = Standard_Door(driver)
        login.typeUserName('aa@ecogaragedoors.com')
        login.typePassword('aabb')
        login.clickLogin()
        login.go_addquote()
        login.go_addstandarddoor()
        # login.check_design_optilift
        # login.check_door_page
        # login.check_install_details
        login.check_install_type
        # login.check_door_type
        # login.check_colour_category
        # login.check_design_panel
        # login.check_design_insulated
        # login.check_design_roller
        # login.check_colour_colorbond
        # login.check_colour_custom
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
        # login.windows_type_panellift
        # login.windows_position_custom
        # login.check_default_doorfinish
        # login.check_classic_doorfinish
        # login.check_slimline_doorfinish
        # login.check_wideline_doorfinish
