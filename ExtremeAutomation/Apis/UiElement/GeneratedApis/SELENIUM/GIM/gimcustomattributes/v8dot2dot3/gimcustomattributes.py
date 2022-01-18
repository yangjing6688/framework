from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as GimcustomattributesBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Gimcustomattributes(GimcustomattributesBase):
    def cu_tab_check(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "(//span[text()='Onboarding Templates'])[1]",
                           self.builder.constants.STRATEGY_XPATH)
        self.spinner_loading(ui_cmd_obj)
        true_or_false = self.builder.get_attribute_from_element(ui_cmd_obj, "//span[text()='Custom Attributes']",
                                                                "aria-selected")
        if not true_or_false:
            self.builder.click(ui_cmd_obj, "//span[text()='Custom Attributes']", self.builder.constants.STRATEGY_XPATH)
            ui_cmd_obj.error_state = False
        else:
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def cu_guest_users_tab_check(self, ui_cmd_obj, arg_dict):
        true_or_false = self.builder.get_attribute_from_element(ui_cmd_obj, "(//span[text()='Guest Users'])[2]",
                                                                "aria-selected")
        if not true_or_false == 'None':
            self.builder.click(ui_cmd_obj, "(//span[text()='Guest Users'])[2]", self.builder.constants.STRATEGY_XPATH)
            ui_cmd_obj.error_state = False
        else:
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def cu_devices_tab_check(self, ui_cmd_obj, arg_dict):
        true_or_false = self.builder.get_attribute_from_element(ui_cmd_obj, "(//span[text()='Devices'])[2]",
                                                                "aria-selected")
        if not true_or_false == 'None':
            self.builder.click(ui_cmd_obj, "(//span[text()='Devices'])[2]", self.builder.constants.STRATEGY_XPATH)
            ui_cmd_obj.error_state = False
        else:
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def cu_add_locale(self, ui_cmd_obj, arg_dict):
        self.base_builder.delay(ui_cmd_obj, 5000)
        self.builder.click(ui_cmd_obj, "//span[text()='Administration']", self.builder.constants.STRATEGY_XPATH)
        self.spinner_loading(ui_cmd_obj)
        self.builder.click(ui_cmd_obj, "(//span[text()='Preferences'])[1]", self.builder.constants.STRATEGY_XPATH)
        self.builder.click(ui_cmd_obj, "//span[text()='Add']", self.builder.constants.STRATEGY_XPATH)
        self.spinner_loading(ui_cmd_obj)
        self.builder.click(ui_cmd_obj, "//input[@name='lang']", self.builder.constants.STRATEGY_XPATH)
        if arg_dict['lang'] == "France":
            self.builder.click(ui_cmd_obj, "//ul[@class='x-list-plain']/li/img[contains(@src, 'flag_fr.png')]",
                               self.builder.constants.STRATEGY_XPATH)
        elif arg_dict['lang'] == "Duetsch":
            self.builder.click(ui_cmd_obj, "//ul[@class='x-list-plain']/li/img[contains(@src, 'flag_de.png')]",
                               self.builder.constants.STRATEGY_XPATH)
        elif arg_dict['lang'] == "Espanol":
            self.builder.click(ui_cmd_obj, "//ul[@class='x-list-plain']/li/img[contains(@src, 'flag_es.png')]",
                               self.builder.constants.STRATEGY_XPATH)
        elif arg_dict['lang'] == "Italiano":
            self.builder.click(ui_cmd_obj, "//ul[@class='x-list-plain']/li/img[contains(@src, 'flag_it.png')]",
                               self.builder.constants.STRATEGY_XPATH)
        elif arg_dict['lang'] == "Portugues":
            self.builder.click(ui_cmd_obj, "//ul[@class='x-list-plain']/li/img[contains(@src, 'flag_pt.png')]",
                               self.builder.constants.STRATEGY_XPATH)
        elif arg_dict['lang'] == "Svenska":
            self.builder.click(ui_cmd_obj, "//ul[@class='x-list-plain']/li/img[contains(@src, 'flag_sv.png')]",
                               self.builder.constants.STRATEGY_XPATH)
        elif arg_dict['lang'] == "Nederlands":
            self.builder.click(ui_cmd_obj, "//ul[@class='x-list-plain']/li/img[contains(@src, 'flag_nl.png')]",
                               self.builder.constants.STRATEGY_XPATH)
        elif arg_dict['lang'] == "Russia":
            self.builder.click(ui_cmd_obj, "//ul[@class='x-list-plain']/li/img[contains(@src, 'flag_ru.png')]",
                               self.builder.constants.STRATEGY_XPATH)
        self.builder.click(ui_cmd_obj, "[role='dialog'] .x-btn-inner-blue-small",
                           self.builder.constants.STRATEGY_CSS_SELECTOR)
        self.spinner_loading(ui_cmd_obj)
        self.builder.click(ui_cmd_obj, "//a[@data-qtip='Save Look & Feel Settings']",
                           self.builder.constants.STRATEGY_XPATH)
        self.spinner_loading(ui_cmd_obj)

        return ui_cmd_obj

    def cu_ot_with_custom_attributes(self, ui_cmd_obj, arg_dict):
        self.base_builder.delay(ui_cmd_obj, 5000)
        if arg_dict["gu_or_de"] == "GuestUsers":
            self.builder.click(ui_cmd_obj, "//div[@role='form']/div/div[@role='presentation']/div[@role='tablist']/"
                                           "div[1]/div[2]/div/a[3]", self.builder.constants.STRATEGY_XPATH)
            # cus1_man1
            self.builder.click(ui_cmd_obj, "//input[@name='userCustom1']", self.builder.constants.STRATEGY_XPATH)
            if arg_dict["cf1_man_or_opt"] == "Mandate":
                cus1_man1 = self.builder.find_element(ui_cmd_obj, "//input[@name='userCustom1Man']")
                tr_or_false = self.base_builder.get_attribute_from_element(ui_cmd_obj, cus1_man1, "checked")
                if not tr_or_false:
                    self.builder.click(ui_cmd_obj, "//input[@name='userCustom1Man']",
                                       self.builder.constants.STRATEGY_XPATH)
            # cus2_man1
            self.builder.click(ui_cmd_obj, "//input[@name='userCustom2']", self.builder.constants.STRATEGY_XPATH)
            if arg_dict["cf2_man_or_opt"] == "Mandate":
                cus1_man1 = self.builder.find_element(ui_cmd_obj, "//input[@name='userCustom2Man']")
                tr_or_false = self.base_builder.get_attribute_from_element(ui_cmd_obj, cus1_man1, "checked")
                if not tr_or_false:
                    self.builder.click(ui_cmd_obj, "//input[@name='userCustom2Man']",
                                       self.builder.constants.STRATEGY_XPATH)
            # cus3_man1
            self.builder.click(ui_cmd_obj, "//input[@name='userCustom3']", self.builder.constants.STRATEGY_XPATH)
            if arg_dict["cf3_man_or_opt"] == "Mandate":
                cus1_man1 = self.builder.find_element(ui_cmd_obj, "//input[@name='userCustom3Man']")
                tr_or_false = self.base_builder.get_attribute_from_element(ui_cmd_obj, cus1_man1, "checked")
                if not tr_or_false:
                    self.builder.click(ui_cmd_obj, "//input[@name='userCustom3Man']",
                                       self.builder.constants.STRATEGY_XPATH)
            # cus4_man1
            self.builder.click(ui_cmd_obj, "//input[@name='userCustom4']", self.builder.constants.STRATEGY_XPATH)
            if arg_dict["cf4_man_or_opt"] == "Mandate":
                cus1_man1 = self.builder.find_element(ui_cmd_obj, "//input[@name='userCustom4Man']")
                tr_or_false = self.base_builder.get_attribute_from_element(ui_cmd_obj, cus1_man1, "checked")
                if not tr_or_false:
                    self.builder.click(ui_cmd_obj, "//input[@name='userCustom4Man']",
                                       self.builder.constants.STRATEGY_XPATH)
            # cus5_man1
            self.builder.click(ui_cmd_obj, "//input[@name='userCustom5']", self.builder.constants.STRATEGY_XPATH)
            if arg_dict["cf5_man_or_opt"] == "Mandate":
                cus1_man1 = self.builder.find_element(ui_cmd_obj, "//input[@name='userCustom5Man']")
                tr_or_false = self.base_builder.get_attribute_from_element(ui_cmd_obj, cus1_man1, "checked")
                if not tr_or_false:
                    self.builder.click(ui_cmd_obj, "//input[@name='userCustom5Man']",
                                       self.builder.constants.STRATEGY_XPATH)
            # cus6_man1
            self.builder.click(ui_cmd_obj, "//input[@name='userCustom6']", self.builder.constants.STRATEGY_XPATH)
            if arg_dict["cf6_man_or_opt"] == "Mandate":
                cus1_man1 = self.builder.find_element(ui_cmd_obj, "//input[@name='userCustom6Man']")
                tr_or_false = self.base_builder.get_attribute_from_element(ui_cmd_obj, cus1_man1, "checked")
                if not tr_or_false:
                    self.builder.click(ui_cmd_obj, "//input[@name='userCustom6Man']",
                                       self.builder.constants.STRATEGY_XPATH)
            if arg_dict['ot_save'] == "save":
                self.builder.click(ui_cmd_obj, "//div[@class='x-panel x-tabpanel-child x-panel-default']/"
                                               "div/div/div/div/a[1]", self.builder.constants.STRATEGY_XPATH)
                self.spinner_loading(ui_cmd_obj)
        elif arg_dict["gu_or_de"] == "Devices":
            self.builder.click(ui_cmd_obj, "//div[@role='form']/div/div[@role='presentation']/div[@role='tablist']/"
                                           "div[1]/div[2]/div/a[5]", self.builder.constants.STRATEGY_XPATH)
            # cust1_man
            self.builder.click(ui_cmd_obj, "//input[@name='deviceCustom1']",
                               self.builder.constants.STRATEGY_XPATH)
            if arg_dict["cf1_man_or_opt"] == "Mandate":
                cus1_man = self.builder.find_element(ui_cmd_obj, "//input[@name='deviceCustom1Man']")
                tr_or_false = self.base_builder.get_attribute_from_element(ui_cmd_obj, cus1_man, "checked")
                if not tr_or_false:
                    self.builder.click(ui_cmd_obj, "//input[@name='deviceCustom1Man']",
                                       self.builder.constants.STRATEGY_XPATH)
            # cust2_man
            self.builder.click(ui_cmd_obj, "//input[@name='deviceCustom2']",
                               self.builder.constants.STRATEGY_XPATH)
            if arg_dict["cf2_man_or_opt"] == "Mandate":
                cus1_man = self.builder.find_element(ui_cmd_obj, "//input[@name='deviceCustom2Man']")
                tr_or_false = self.base_builder.get_attribute_from_element(ui_cmd_obj, cus1_man, "checked")
                if not tr_or_false:
                    self.builder.click(ui_cmd_obj, "//input[@name='deviceCustom2Man']",
                                       self.builder.constants.STRATEGY_XPATH)
            # cust3_man
            self.builder.click(ui_cmd_obj, "//input[@name='deviceCustom3']",
                               self.builder.constants.STRATEGY_XPATH)
            if arg_dict["cf3_man_or_opt"] == "Mandate":
                cus1_man = self.builder.find_element(ui_cmd_obj, "//input[@name='deviceCustom3Man']")
                tr_or_false = self.base_builder.get_attribute_from_element(ui_cmd_obj, cus1_man, "checked")
                if not tr_or_false:
                    self.builder.click(ui_cmd_obj, "//input[@name='deviceCustom3Man']",
                                       self.builder.constants.STRATEGY_XPATH)
            # cust1_man
            self.builder.click(ui_cmd_obj, "//input[@name='deviceCustom4']",
                               self.builder.constants.STRATEGY_XPATH)
            if arg_dict["cf4_man_or_opt"] == "Mandate":
                cus1_man = self.builder.find_element(ui_cmd_obj, "//input[@name='deviceCustom4Man']")
                tr_or_false = self.base_builder.get_attribute_from_element(ui_cmd_obj, cus1_man, "checked")
                if not tr_or_false:
                    self.builder.click(ui_cmd_obj, "//input[@name='deviceCustom4Man']",
                                       self.builder.constants.STRATEGY_XPATH)
            # cust1_man
            self.builder.click(ui_cmd_obj, "//input[@name='deviceCustom5']",
                               self.builder.constants.STRATEGY_XPATH)
            if arg_dict["cf5_man_or_opt"] == "Mandate":
                cus1_man = self.builder.find_element(ui_cmd_obj, "//input[@name='deviceCustom5Man']")
                tr_or_false = self.base_builder.get_attribute_from_element(ui_cmd_obj, cus1_man, "checked")
                if not tr_or_false:
                    self.builder.click(ui_cmd_obj, "//input[@name='deviceCustom5Man']",
                                       self.builder.constants.STRATEGY_XPATH)
            # cust1_man
            self.builder.click(ui_cmd_obj, "//input[@name='deviceCustom6']",
                               self.builder.constants.STRATEGY_XPATH)
            if arg_dict["cf6_man_or_opt"] == "Mandate":
                cus1_man = self.builder.find_element(ui_cmd_obj, "//input[@name='deviceCustom6Man']")
                tr_or_false = self.base_builder.get_attribute_from_element(ui_cmd_obj, cus1_man, "checked")
                if not tr_or_false:
                    self.builder.click(ui_cmd_obj, "//input[@name='deviceCustom6Man']",
                                       self.builder.constants.STRATEGY_XPATH)
            if arg_dict['ot_save'] == "save":
                self.builder.click(ui_cmd_obj, "//div[@class='x-panel x-tabpanel-child x-panel-default']/"
                                               "div/div/div/div/a[1]", self.builder.constants.STRATEGY_XPATH)
                self.spinner_loading(ui_cmd_obj)
                self.is_ldap_pop_up_exists(ui_cmd_obj)

        return ui_cmd_obj

    def cu_gu_with_custom_attributes(self, ui_cmd_obj, arg_dict):
        self.base_builder.delay(ui_cmd_obj, 5000)
        if arg_dict["prov_or_self"] == "prov":
            self.select_ot_from_dropdown(ui_cmd_obj, arg_dict)
            self.builder.enter_text(ui_cmd_obj, arg_dict['gu_fname'], "//input[@name='firstName']")
            self.builder.enter_text(ui_cmd_obj, arg_dict['gu_lname'], "//input[@name='lastName']")
            self.builder.enter_text(ui_cmd_obj, arg_dict['gu_uname'], "//input[@name='loginId']")
            self.builder.enter_text(ui_cmd_obj, arg_dict['gu_pwd'], "//input[@name='password']")
            self.builder.enter_text(ui_cmd_obj, arg_dict['gu_email'], "//input[@name='email']")
            self.builder.enter_text(ui_cmd_obj, arg_dict['gu_cell_phone'], "//input[@name='cellPhone']")
        elif arg_dict["prov_or_self"] == "self":
            self.builder.enter_text(ui_cmd_obj, arg_dict['gu_fname'], "//input[@name='userFirstName']")
            self.builder.enter_text(ui_cmd_obj, arg_dict['gu_lname'], "//input[@name='userLastName']")
            self.builder.enter_text(ui_cmd_obj, arg_dict['gu_uname'], "//input[@name='username']")
            self.builder.enter_text(ui_cmd_obj, arg_dict['gu_pwd'], "//input[@name='userPassword']")
            self.builder.enter_text(ui_cmd_obj, arg_dict['gu_email'], "//input[@name='userEmail']")
            self.builder.enter_text(ui_cmd_obj, arg_dict['gu_cell_phone'], "//input[@name='userCellPhone']")

        return ui_cmd_obj

    def cu_de_with_custom_attributes(self, ui_cmd_obj, arg_dict):
        self.base_builder.delay(ui_cmd_obj, 5000)
        try:
            if arg_dict["prov_or_self"] == "prov":
                self.builder.click(ui_cmd_obj, "//span[text()='Devices']", self.builder.constants.STRATEGY_XPATH)
                self.spinner_loading(ui_cmd_obj)
                self.builder.click(ui_cmd_obj, "//span[@class='x-tab-inner x-tab-inner-extr-main-tab-panel' "
                                               "and text()='Devices']", self.builder.constants.STRATEGY_XPATH)
                self.builder.click(ui_cmd_obj,
                                   "//span[@class='x-btn-inner x-btn-inner-default-toolbar-small' and text()='Add']",
                                   self.builder.constants.STRATEGY_XPATH)
                self.spinner_loading(ui_cmd_obj)
                self.builder.click(ui_cmd_obj, "//input[@name='onboardingTemplate']",
                                   self.builder.constants.STRATEGY_XPATH)
                self.spinner_loading(ui_cmd_obj)
                index = 1
                observed_value = ''
                while index < 25:
                    web_obj = self.builder.find_element(ui_cmd_obj, "//ul[@role='listbox']/li[" + str(index) + "]")
                    return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
                    self.logger.log_info("ot_uname: " + str(index) + "::" + return_text)
                    if return_text == arg_dict['de_otname']:
                        self.logger.log_info("selected otname: " + str(index) + "::" + return_text)
                        self.builder.click(ui_cmd_obj, "//ul[@role='listbox']/li[" + str(index) + "]")
                        break
                    elif return_text == observed_value:
                        ui_cmd_obj.error_state = True
                        break
                    else:
                        observed_value = return_text
                        index += 1
                self.builder.delay(ui_cmd_obj, 5)
                self.builder.enter_text(ui_cmd_obj, arg_dict['de_mac'], "//input[@name='mac']")
                self.builder.enter_text(ui_cmd_obj, arg_dict['de_name'], "//input[@name='deviceName']")
                self.builder.click(ui_cmd_obj, "//input[@name='deviceFamilyGroup']",
                                   self.builder.constants.STRATEGY_XPATH)
                self.builder.click(ui_cmd_obj, "(//li[text()='Android'])[1]", self.builder.constants.STRATEGY_XPATH)
                self.builder.click(ui_cmd_obj, "//input[@name='deviceTypes']", self.builder.constants.STRATEGY_XPATH)
                self.builder.click(ui_cmd_obj, "(//li[text()='Android'])[2]", self.builder.constants.STRATEGY_XPATH)
            elif arg_dict["prov_or_self"] == "self":
                self.builder.delay(ui_cmd_obj, 5)
                self.builder.click(ui_cmd_obj, "//input[@name='macAddress']", self.builder.constants.STRATEGY_XPATH)
                mac_array = arg_dict['de_mac'].split(":")
                for x in mac_array:
                    self.builder.enter_text(ui_cmd_obj, str(x), "//input[@name='macAddress']", clear_existing=False)
                self.builder.click(ui_cmd_obj, "//input[@name='deviceFamily']", self.builder.constants.STRATEGY_XPATH)
                self.builder.click(ui_cmd_obj, "(//li[text()='Android'])[1]", self.builder.constants.STRATEGY_XPATH)
                self.builder.click(ui_cmd_obj, "//input[@name='deviceType']", self.builder.constants.STRATEGY_XPATH)
                self.builder.click(ui_cmd_obj, "(//li[text()='Android'])[2]", self.builder.constants.STRATEGY_XPATH)
                self.builder.delay(ui_cmd_obj, 5)
            return ui_cmd_obj
        except TypeError:
            return ui_cmd_obj

    def cu_validate_gu_with_custom_attributes(self, ui_cmd_obj, arg_dict):
        self.base_builder.delay(ui_cmd_obj, 5000)
        web_obj_cu1 = None
        if arg_dict['prov_or_self'] == "prov":
            web_obj_cu1 = self.builder.find_element(ui_cmd_obj, "//input[@name='custom1']/preceding::label[1]",
                                                    self.builder.constants.STRATEGY_XPATH)
        elif arg_dict['prov_or_self'] == "self":
            web_obj_cu1 = self.builder.find_element(ui_cmd_obj, "//input[@name='deviceCustom1' or "
                                                                "@name='userCustom1']/preceding::label[1]")
        return_text_cu1 = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj_cu1)
        self.logger.log_info("return_text_cu1: " + return_text_cu1)

        if return_text_cu1 != arg_dict['label1']:
            self.logger.log_info(return_text_cu1 + " is not equal to " + str(arg_dict['label1']))
            ui_cmd_obj.error_state = True
        else:
            self.logger.log_info(return_text_cu1 + " is equal to " + str(arg_dict['label1']))
            ui_cmd_obj.error_state = False

        # Validation for Custom Attribute2
        web_obj_cu2 = None
        if arg_dict['prov_or_self'] == "prov":
            web_obj_cu2 = self.builder.find_element(ui_cmd_obj, "//input[@name='custom2']/preceding::label[1]",
                                                    self.builder.constants.STRATEGY_XPATH)
        elif arg_dict['prov_or_self'] == "self":
            web_obj_cu2 = self.builder.find_element(ui_cmd_obj, "//input[@name='deviceCustom2' or "
                                                                "@name='userCustom2']/preceding::label[1]")
        return_text_cu2 = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj_cu2)
        self.logger.log_info("return_text_cu2: " + return_text_cu2)
        if return_text_cu2 != arg_dict['label2']:
            self.logger.log_info(return_text_cu2 + " is not equal to " + str(arg_dict['label2']))
            ui_cmd_obj.error_state = True
        else:
            self.logger.log_info(return_text_cu2 + " is equal to " + str(arg_dict['label2']))
            ui_cmd_obj.error_state = False

        # Validation for Custom Attribute3
        web_obj_cu3 = None
        if arg_dict['prov_or_self'] == "prov":
            web_obj_cu3 = self.builder.find_element(ui_cmd_obj, "//input[@name='custom3']/preceding::label[1]",
                                                    self.builder.constants.STRATEGY_XPATH)
        elif arg_dict['prov_or_self'] == "self":
            web_obj_cu3 = self.builder.find_element(ui_cmd_obj, "//input[@name='deviceCustom3' or "
                                                                "@name='userCustom3']/preceding::label[1]")

        return_text_cu3 = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj_cu3)
        self.logger.log_info("return_text_cu3: " + return_text_cu3)
        if return_text_cu3 != arg_dict['label3']:
            self.logger.log_info(return_text_cu3 + " is not equal to " + str(arg_dict['label3']))
            ui_cmd_obj.error_state = True
        else:
            self.logger.log_info(return_text_cu3 + " is equal to " + str(arg_dict['label3']))
            ui_cmd_obj.error_state = False

        # Validation for Custom Attribute4
        web_obj_cu4 = None
        if arg_dict['prov_or_self'] == "prov":
            web_obj_cu4 = self.builder.find_element(ui_cmd_obj, "//input[@name='custom4']/preceding::label[1]",
                                                    self.builder.constants.STRATEGY_XPATH)
        elif arg_dict['prov_or_self'] == "self":
            web_obj_cu4 = self.builder.find_element(ui_cmd_obj, "//input[@name='deviceCustom4' or "
                                                                "@name='userCustom4']/preceding::label[1]")

        return_text_cu4 = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj_cu4)
        self.logger.log_info("return_text_cu4: " + return_text_cu4)

        if return_text_cu4 != arg_dict['label4']:
            self.logger.log_info(return_text_cu4 + " is not equal to " + str(arg_dict['label4']))
            ui_cmd_obj.error_state = True
        else:
            self.logger.log_info(return_text_cu4 + " is equal to " + str(arg_dict['label4']))
            ui_cmd_obj.error_state = False

        # Validation for Custom Attribute5
        web_obj_cu5 = None
        if arg_dict['prov_or_self'] == "prov":
            web_obj_cu5 = self.builder.find_element(ui_cmd_obj, "//input[@name='custom5']/preceding::label[1]",
                                                    self.builder.constants.STRATEGY_XPATH)
        elif arg_dict['prov_or_self'] == "self":
            web_obj_cu5 = self.builder.find_element(ui_cmd_obj, "//input[@name='deviceCustom5' or "
                                                                "@name='userCustom5']/preceding::label[1]")

        return_text_cu5 = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj_cu5)
        self.logger.log_info("return_text_cu5: " + return_text_cu5)
        if return_text_cu5 != arg_dict['label5']:
            self.logger.log_info(return_text_cu5 + " is not equal to " + str(arg_dict['label5']))
            ui_cmd_obj.error_state = True
        else:
            self.logger.log_info(return_text_cu5 + " is equal to " + str(arg_dict['label5']))
            ui_cmd_obj.error_state = False

        # Validation for Custom Attribute6
        web_obj_cu6 = None
        if arg_dict['prov_or_self'] == "prov":
            web_obj_cu6 = self.builder.find_element(ui_cmd_obj, "//input[@name='custom6']/preceding::label[1]",
                                                    self.builder.constants.STRATEGY_XPATH)
        elif arg_dict['prov_or_self'] == "self":
            web_obj_cu6 = self.builder.find_element(ui_cmd_obj, "//input[@name='deviceCustom6' or "
                                                                "@name='userCustom6']/preceding::label[1]")

        return_text_cu6 = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj_cu6)
        self.logger.log_info("return_text_cu6: " + return_text_cu6)

        if return_text_cu6 != arg_dict['label6']:
            self.logger.log_info(return_text_cu6 + " is not equal to " + str(arg_dict['label6']))
            ui_cmd_obj.error_state = True
        else:
            self.logger.log_info(return_text_cu6 + " is equal to " + str(arg_dict['label6']))
            ui_cmd_obj.error_state = False

        return ui_cmd_obj

    def cu_gu_input_mandatory_values(self, ui_cmd_obj, arg_dict):
        self.base_builder.delay(ui_cmd_obj, 5000)
        if arg_dict["prov_or_self"] == "prov":
            self.builder.enter_text(ui_cmd_obj, arg_dict['custom1'], "//input[@name='custom1']")
            self.builder.enter_text(ui_cmd_obj, arg_dict['custom2'], "//input[@name='custom2']")
            self.builder.enter_text(ui_cmd_obj, arg_dict['custom3'], "//input[@name='custom3']")
            self.builder.enter_text(ui_cmd_obj, arg_dict['custom4'], "//input[@name='custom4']")
            self.builder.enter_text(ui_cmd_obj, arg_dict['custom5'], "//input[@name='custom5']")
            self.builder.enter_text(ui_cmd_obj, arg_dict['custom6'], "//input[@name='custom6']")
            self.builder.click(ui_cmd_obj, "//span[text()='Save']")
            self.spinner_loading(ui_cmd_obj)
            if arg_dict['group'] == "gu":
                web_obj = self.builder.find_element(ui_cmd_obj, "(//div[@class='x-title-text x-title-text-default "
                                                    "x-title-item'])[2]", self.builder.constants.STRATEGY_XPATH)
                popup_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
                if popup_text == "Successful Guest Creation":
                    self.builder.click(ui_cmd_obj, "//span[text()='OK']")
                    self.spinner_loading(ui_cmd_obj)
                else:
                    self.builder.click(ui_cmd_obj, "//span[text()='OK']")
                    self.spinner_loading(ui_cmd_obj)
                    self.builder.click(ui_cmd_obj, "(//span[text()='Cancel'])[1]")
                    self.spinner_loading(ui_cmd_obj)
            elif arg_dict['group'] == "de":
                if arg_dict['error_or_no'] == "error":
                    web_obj = self.builder.find_element(ui_cmd_obj, "//div[text()='Error']",
                                                        self.builder.constants.STRATEGY_XPATH)
                    popup_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
                    if popup_text == "Error":
                        self.builder.click(ui_cmd_obj, "//span[text()='OK']", self.builder.constants.STRATEGY_XPATH)
                        self.spinner_loading(ui_cmd_obj)
                        self.builder.click(ui_cmd_obj, "(//span[text()='Cancel'])[1]",
                                           self.builder.constants.STRATEGY_XPATH)
                        self.spinner_loading(ui_cmd_obj)
                        ui_cmd_obj.error_state = False
                    else:
                        ui_cmd_obj.error_state = True
        elif arg_dict["prov_or_self"] == "self":
            if arg_dict['group'] == "gu":
                self.builder.click(ui_cmd_obj, "//div[@class='cookie-content']/span",
                                   self.builder.constants.STRATEGY_XPATH)
                self.builder.enter_text(ui_cmd_obj, arg_dict['custom1'], "//input[@name='userCustom1']")
                self.builder.enter_text(ui_cmd_obj, arg_dict['custom2'], "//input[@name='userCustom2']")
                self.builder.enter_text(ui_cmd_obj, arg_dict['custom3'], "//input[@name='userCustom3']")
                self.builder.enter_text(ui_cmd_obj, arg_dict['custom4'], "//input[@name='userCustom4']")
                self.builder.enter_text(ui_cmd_obj, arg_dict['custom5'], "//input[@name='userCustom5']")
                self.builder.enter_text(ui_cmd_obj, arg_dict['custom6'], "//input[@name='userCustom6']")
                self.builder.delay(ui_cmd_obj, 2)
                if arg_dict['approval'] == "sponsor_approval":
                    self.builder.enter_text(ui_cmd_obj, arg_dict['custom1'], "//input[@name='sponsorFirstName']")
                    self.builder.enter_text(ui_cmd_obj, arg_dict['custom2'], "//input[@name='sponsorLastName']")
                    self.builder.enter_text(ui_cmd_obj, arg_dict['custom1'], "//div[2]/div[@role='presentation']/div"
                                                                             "[5]/div[@role='presentation']/div[@role="
                                                                             "'presentation']//input[@role='textbox']")
                    self.builder.click(ui_cmd_obj, "(//input[@readonly='readonly'])[3]",
                                       self.builder.constants.STRATEGY_XPATH)
                    self.builder.click(ui_cmd_obj, "//li[@role='option']", self.builder.constants.STRATEGY_XPATH)
                    self.builder.enter_text(ui_cmd_obj, "1234567890", "//input[@name='sponsorCellPhone']")
                    self.builder.click(ui_cmd_obj, "//span[text()='Request Approval']",
                                       self.builder.constants.STRATEGY_XPATH)
                    self.spinner_loading(ui_cmd_obj)
                else:
                    self.builder.click(ui_cmd_obj, "//span[text()='Submit']")
                    self.spinner_loading(ui_cmd_obj)
                if arg_dict['error_or_no'] == "error":
                    web_obj = self.builder.find_element(ui_cmd_obj, "//div[text()='Error']",
                                                        self.builder.constants.STRATEGY_XPATH)
                    popup_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
                    if popup_text == "Error":
                        self.builder.click(ui_cmd_obj, "//span[text()='OK']", self.builder.constants.STRATEGY_XPATH)
                        self.spinner_loading(ui_cmd_obj)
                        ui_cmd_obj.error_state = False
                    else:
                        ui_cmd_obj.error_state = True
                else:
                    self.builder.click(ui_cmd_obj, "//span[text()='OK']", self.builder.constants.STRATEGY_XPATH)
            elif arg_dict['group'] == "de":
                self.builder.click(ui_cmd_obj, "//div[@class='cookie-content']/span",
                                   self.builder.constants.STRATEGY_XPATH)
                self.builder.enter_text(ui_cmd_obj, arg_dict['custom1'], "//input[@name='deviceCustom1']")
                self.builder.enter_text(ui_cmd_obj, arg_dict['custom2'], "//input[@name='deviceCustom2']")
                self.builder.enter_text(ui_cmd_obj, arg_dict['custom3'], "//input[@name='deviceCustom3']")
                self.builder.enter_text(ui_cmd_obj, arg_dict['custom4'], "//input[@name='deviceCustom4']")
                self.builder.enter_text(ui_cmd_obj, arg_dict['custom5'], "//input[@name='deviceCustom5']")
                self.builder.enter_text(ui_cmd_obj, arg_dict['custom6'], "//input[@name='deviceCustom6']")
                self.builder.delay(ui_cmd_obj, 2)
                self.builder.click(ui_cmd_obj, "//span[text()='Submit']")
                self.spinner_loading(ui_cmd_obj)
                if arg_dict['error_or_no'] == "error":
                    web_obj = self.builder.find_element(ui_cmd_obj, "//div[text()='Error']",
                                                        self.builder.constants.STRATEGY_XPATH)
                    popup_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
                    if popup_text == "Error":
                        ui_cmd_obj.error_state = False
                    else:
                        ui_cmd_obj.error_state = True
                else:
                    web_obj = self.builder.find_element(ui_cmd_obj, "//div[text()='Success']",
                                                        self.builder.constants.STRATEGY_XPATH)
                    popup_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
                    if popup_text == "Success":
                        self.builder.click(ui_cmd_obj, "//span[text()='OK']", self.builder.constants.STRATEGY_XPATH)
                        self.spinner_loading(ui_cmd_obj)
                        ui_cmd_obj.error_state = False
                    else:
                        ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def cu_self_service(self, ui_cmd_obj, arg_dict):
        self.base_builder.delay(ui_cmd_obj, 5000)
        self.builder.click(ui_cmd_obj, "//span[text()='Self-Services']", self.builder.constants.STRATEGY_XPATH)
        self.spinner_loading(ui_cmd_obj)
        self.builder.click(ui_cmd_obj, "//span[text()='Self-Service Provisioners']",
                           self.builder.constants.STRATEGY_XPATH)
        self.spinner_loading(ui_cmd_obj)
        self.builder.click(ui_cmd_obj, "//span[text()='Add']", self.builder.constants.STRATEGY_XPATH)
        self.spinner_loading(ui_cmd_obj)
        self.builder.enter_text(ui_cmd_obj, arg_dict['ss_name'], "//input[@data-ref='inputEl' and @name='loginId']")
        self.builder.click(ui_cmd_obj, "//input[@data-ref='inputEl' and @name='serviceType']")
        if arg_dict["gu_or_de"] == "GuestUser":
            self.builder.click(ui_cmd_obj, "//li[@role='option' and text()='Guest User']")
        elif arg_dict["gu_or_de"] == "Device":
            self.builder.click(ui_cmd_obj, "//li[@role='option' and text()='Device']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['ss_pwd'],
                                "//input[@data-ref='inputEl' and @name='userCredential']",
                                self.builder.constants.STRATEGY_XPATH)
        self.builder.enter_text(ui_cmd_obj, arg_dict['ss_pwd'],
                                "(//input[@data-ref='inputEl' and @type='password'])[2]",
                                self.builder.constants.STRATEGY_XPATH)
        self.builder.enter_text(ui_cmd_obj, arg_dict['ss_email'],
                                "//input[@data-ref='inputEl' and @name='userEmailAddress']",
                                self.builder.constants.STRATEGY_XPATH)
        self.builder.click(ui_cmd_obj, "//input[@data-ref='inputEl' and @name='userProvOnboardingTemplate']",
                           self.builder.constants.STRATEGY_XPATH)
        self.spinner_loading(ui_cmd_obj)
        self.builder.click(ui_cmd_obj, "//li[text()='" + arg_dict['ot'] + "']", self.builder.constants.STRATEGY_XPATH)
        self.builder.click(ui_cmd_obj, "//span[text()='Save']", self.builder.constants.STRATEGY_XPATH)
        self.base_builder.delay(ui_cmd_obj, 5000)

        return ui_cmd_obj

    def cu_self_service_provisioning(self, ui_cmd_obj, arg_dict):
        self.base_builder.delay(ui_cmd_obj, 5000)
        self.builder.click(ui_cmd_obj, "//span[text()='Self-Services']", self.builder.constants.STRATEGY_XPATH)
        self.spinner_loading(ui_cmd_obj)
        self.builder.enter_text(ui_cmd_obj, "//input[@name='userFirstName']", self.builder.constants.STRATEGY_XPATH)
        self.builder.enter_text(ui_cmd_obj,
                                "//input[@name='userFirstName']", self.builder.constants.STRATEGY_XPATH)
        self.builder.enter_text(ui_cmd_obj, "//input[@name='userFirstName']", self.builder.constants.STRATEGY_XPATH)
        self.builder.enter_text(ui_cmd_obj, "//input[@name='userFirstName']", self.builder.constants.STRATEGY_XPATH)
        self.builder.enter_text(ui_cmd_obj, "//input[@name='userFirstName']", self.builder.constants.STRATEGY_XPATH)
        self.builder.enter_text(ui_cmd_obj, "//input[@name='userFirstName']", self.builder.constants.STRATEGY_XPATH)
        self.builder.enter_text(ui_cmd_obj, "//input[@name='userFirstName']", self.builder.constants.STRATEGY_XPATH)

        return ui_cmd_obj

    def config_email_notification(self, ui_cmd_obj, arg_dict):
        self.base_builder.delay(ui_cmd_obj, 5000)
        self.builder.click(ui_cmd_obj, "//span[text()='Administration']", self.builder.constants.STRATEGY_XPATH)
        self.spinner_loading(ui_cmd_obj)
        self.builder.click(ui_cmd_obj, "//span[text()='Notification']", self.builder.constants.STRATEGY_XPATH)
        self.spinner_loading(ui_cmd_obj)
        self.builder.click(ui_cmd_obj, "//span[text()='E-mail']", self.builder.constants.STRATEGY_XPATH)
        web_obj = self.builder.find_element(ui_cmd_obj, "//input[@name='enableEmail']")
        true_or_false = self.base_builder.get_attribute_from_element(ui_cmd_obj, web_obj, "checked")
        if not true_or_false:
            self.set_check_box_value(ui_cmd_obj, "//input[@name='enableEmail']",
                                     self.builder.constants.STRATEGY_XPATH, True)
            self.builder.enter_text(ui_cmd_obj, arg_dict['ss_email'],
                                    "//input[@name='fromAddress']", self.builder.constants.STRATEGY_XPATH)
            self.builder.enter_text(ui_cmd_obj, arg_dict['email_server'],
                                    "//input[@name='server']", self.builder.constants.STRATEGY_XPATH)
            self.builder.click(ui_cmd_obj, "(//span[text()='Save'])[2]", self.builder.constants.STRATEGY_XPATH)

        return ui_cmd_obj

    def cu_input_custom_field(self, ui_cmd_obj, arg_dict):
        if arg_dict['lang_number'] == "lang1":
            table = 1
        elif arg_dict['lang_number'] == "lang2":
            table = 2
        else:
            table = 3
        if arg_dict['gu_or_de'] == "gu":
            self.builder.enter_text(ui_cmd_obj, arg_dict['label1'],
                                    "//input[@name='userCustomLabel1Lang" + str(table) + "']",
                                    self.builder.constants.STRATEGY_XPATH)
            self.builder.enter_text(ui_cmd_obj, arg_dict['label2'],
                                    "//input[@name='userCustomLabel2Lang" + str(table) + "']",
                                    self.builder.constants.STRATEGY_XPATH)
            self.builder.enter_text(ui_cmd_obj, arg_dict['label3'],
                                    "//input[@name='userCustomLabel3Lang" + str(table) + "']",
                                    self.builder.constants.STRATEGY_XPATH)
            self.builder.enter_text(ui_cmd_obj, arg_dict['label4'],
                                    "//input[@name='userCustomLabel4Lang" + str(table) + "']",
                                    self.builder.constants.STRATEGY_XPATH)
            self.builder.enter_text(ui_cmd_obj, arg_dict['label5'],
                                    "//input[@name='userCustomLabel5Lang" + str(table) + "']",
                                    self.builder.constants.STRATEGY_XPATH)
            self.builder.enter_text(ui_cmd_obj, arg_dict['label6'],
                                    "//input[@name='userCustomLabel6Lang" + str(table) + "']",
                                    self.builder.constants.STRATEGY_XPATH)
            self.builder.click(ui_cmd_obj, "//a[@data-qtip='Save Guest User Custom Field Labels']",
                               self.builder.constants.STRATEGY_XPATH)
            self.spinner_loading(ui_cmd_obj)
        elif arg_dict['gu_or_de'] == "de":
            self.builder.enter_text(ui_cmd_obj, arg_dict['label1'],
                                    "//input[@name='deviceCustomLabel1Lang" + str(table) + "']",
                                    self.builder.constants.STRATEGY_XPATH)
            self.builder.enter_text(ui_cmd_obj, arg_dict['label2'],
                                    "//input[@name='deviceCustomLabel2Lang" + str(table) + "']",
                                    self.builder.constants.STRATEGY_XPATH)
            self.builder.enter_text(ui_cmd_obj, arg_dict['label3'],
                                    "//input[@name='deviceCustomLabel3Lang" + str(table) + "']",
                                    self.builder.constants.STRATEGY_XPATH)
            self.builder.enter_text(ui_cmd_obj, arg_dict['label4'],
                                    "//input[@name='deviceCustomLabel4Lang" + str(table) + "']",
                                    self.builder.constants.STRATEGY_XPATH)
            self.builder.enter_text(ui_cmd_obj, arg_dict['label5'],
                                    "//input[@name='deviceCustomLabel5Lang" + str(table) + "']",
                                    self.builder.constants.STRATEGY_XPATH)
            self.builder.enter_text(ui_cmd_obj, arg_dict['label6'],
                                    "//input[@name='deviceCustomLabel6Lang" + str(table) + "']",
                                    self.builder.constants.STRATEGY_XPATH)
            self.builder.click(ui_cmd_obj, "//a[@data-qtip='Save Device Custom Field Labels']",
                               self.builder.constants.STRATEGY_XPATH)
            self.spinner_loading(ui_cmd_obj)
        self.builder.delay(ui_cmd_obj, 5)

        return ui_cmd_obj

    def cu_validate_ssn_in_services_page(self, ui_cmd_obj, arg_dict):
        self.base_builder.delay(ui_cmd_obj, 5000)
        self.builder.click(ui_cmd_obj, "//span[text()='Self-Services']", self.builder.constants.STRATEGY_XPATH)
        self.spinner_loading(ui_cmd_obj)
        self.builder.click(ui_cmd_obj, "//span[text()='Self-Provisioning Services']",
                           self.builder.constants.STRATEGY_XPATH)
        self.spinner_loading(ui_cmd_obj)
        all_index = self.builder.find_elements(ui_cmd_obj, "//div[starts-with(@id,'selfProvisioningService')]/div/"
                                                           "div[@class='x-grid-item-container']/table")
        end_index = len(all_index)
        for index in range(1, end_index + 1):
            web_obj = self.builder.find_element(ui_cmd_obj, "(//div[starts-with(@id, 'selfProvisioningService')]/div/"
                                                            "div[@class='x-grid-item-container']/table)"
                                                            "[" + str(index) + "]/tbody/tr/td[1]")
            return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
            self.logger.log_info("ss_name: " + str(index) + "::" + return_text)
            if return_text == arg_dict['ss_name']:
                web_obj = self.builder.find_element(ui_cmd_obj, "(//div[starts-with(@id, 'selfProvisioningService')]/"
                                                                "div/div[@class='x-grid-item-container']/table)"
                                                                "[" + str(index) + "]/tbody/tr/td[4]")
                this_url = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)

                self.builder.click(ui_cmd_obj, "//div[@role='presentation']/div[@role='presentation']/"
                                               "div[@role='presentation']/div/a[2]")
                self.builder.click(ui_cmd_obj, "//a/span[text()='Logout']")
                self.builder.delay(ui_cmd_obj, 5)
                arg_dict["browser"] = "chrome"
                self.builder.open_web_page(ui_cmd_obj, arg_dict["browser"], this_url, implicit_wait=1,
                                           delete_all_cookies=True)
                self.wait_for_page_load_completely(ui_cmd_obj)
                # self.builder.driver.get(this_url)
                # self.wait_for_page_load_completely(ui_cmd_obj)
                # self.builder.delay(ui_cmd_obj, 5)
                ui_cmd_obj.error_state = False
                break
            else:
                ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def entry_should_not_exist(self, ui_cmd_obj, arg_dict):
        if arg_dict["gu_or_de"] == "gu":
            self.builder.click(ui_cmd_obj, "//span[@class='x-btn-inner x-btn-inner-extr-nav-toolbar-button-small' and "
                                           "text()='Guest Users']")
            self.spinner_loading(ui_cmd_obj)
            self.builder.click(ui_cmd_obj, "(//span[text()='Guest Users'])[2]")
            self.spinner_loading(ui_cmd_obj)
            all_count = self.builder.find_elements(ui_cmd_obj, "//div[@class ='x-grid-item-container']/table")
            row_count = len(all_count)
            self.logger.log_info("row_count: " + str(row_count))
            count = 0
            for index in range(1, (row_count + 1)):
                web_obj = self.builder.find_element(ui_cmd_obj, "//div[@class ='x-grid-item-container']"
                                                                "/table[" + str(index) + "]/tbody/tr/td[1]")
                return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
                self.logger.log_info("gu_uname: " + str(index) + "::" + return_text)
                # first name
                if return_text == arg_dict['gu_uname']:
                    count += 1
                else:
                    continue
            if count == 0:
                ui_cmd_obj.error_state = False
            else:
                ui_cmd_obj.error_state = True
        elif arg_dict["gu_or_de"] == "de":
            self.builder.click(ui_cmd_obj, "//span[@class='x-btn-inner x-btn-inner-extr-nav-toolbar-button-"
                                           "small' and text()='Devices']")
            self.spinner_loading(ui_cmd_obj)
            self.builder.click(ui_cmd_obj, "(//span[text()='Devices'])[2]")
            self.spinner_loading(ui_cmd_obj)
            all_count = self.builder.find_elements(ui_cmd_obj, "//div[@class ='x-grid-item-container']/table")
            row_count = len(all_count)
            self.logger.log_info("row_count: " + str(row_count))
            count = 0
            for index in range(1, (row_count + 1)):
                web_obj = self.builder.find_element(ui_cmd_obj, "//div[@class ='x-grid-item-container']"
                                                                "/table[" + str(index) + "]/tbody/tr/td[1]")
                return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
                self.logger.log_info("MAC: " + str(index) + "::" + return_text)
                # first name
                if return_text == arg_dict['gu_uname']:
                    count = count + 1
                else:
                    continue
            if count == 0:
                ui_cmd_obj.error_state = False
            else:
                ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def verify_device_added(self, ui_cmd_obj, arg_dict):
        self.base_builder.delay(ui_cmd_obj, 3000)
        self.builder.click(ui_cmd_obj,
                           "//span[@class='x-btn-inner x-btn-inner-extr"
                           "-nav-toolbar-button-small' and text()='Devices']")
        self.spinner_loading(ui_cmd_obj)
        self.builder.click(ui_cmd_obj, "(//span[text()='Devices'])[2]")
        self.spinner_loading(ui_cmd_obj)
        web_ele = self.builder.find_element(ui_cmd_obj,
                                            "(//div[@class='x-toolbar-text "
                                            "x-box-item x-toolbar-item x-toolbar-text"
                                            "-default'])[3]",
                                            self.builder.constants.STRATEGY_XPATH)
        no_of_pages = self.base_builder.get_text_from_element(ui_cmd_obj, web_ele)
        get_page_count = no_of_pages.strip('of ')
        next_page_count = int(get_page_count)
        for x in range(next_page_count):
            self.builder.delay(ui_cmd_obj, 10)
            all_count = self.builder.find_elements(ui_cmd_obj, "//div[@class ='x-grid-item-container']/table")
            row_count = len(all_count)
            self.logger.log_info("row_count: " + str(row_count))
            if row_count >= 1:
                for index in range(1, row_count + 1):
                    web_obj = self.builder.find_element(ui_cmd_obj, "//div[@class ='x-grid-item-container']"
                                                                    "/table[" + str(index) + "]/tbody/tr/td[1]")
                    return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
                    self.logger.log_info("me device_mac: " + str(index) + "::" + return_text)
                    if return_text == arg_dict['device_mac']:
                        self.logger.log_info(return_text + " equal to: " + arg_dict['device_mac'])
                        ui_cmd_obj.error_state = False
                        break
                    else:
                        ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def spinner_loading(self, ui_cmd_obj):
        self.builder.webdriver_wait_until(ui_cmd_obj, ".x-mask-msg-text", retry=5,
                                          strategy=self.builder.constants.STRATEGY_CSS_SELECTOR,
                                          condition=self.builder.constants.CONDITION_INVISIBILITY_OF_ELEMENT)
        return ui_cmd_obj

    def wait_for_page_load_completely(self, ui_cmd_obj):
        self.logger.log_info("waiting for the page to load ...")
        for x in range(1, 25):
            self.base_builder.delay(ui_cmd_obj, 250)
            self.base_builder.execute_script(ui_cmd_obj, "return document.readyState;")
            self.logger.log_info("page readyState:  " + str(ui_cmd_obj.return_data))
            if ui_cmd_obj.return_data == "complete":
                self.logger.log_info("page loaded completely: ")
                break

        return ui_cmd_obj

    def set_check_box_value(self, ui_cmd_obj, locator, strategy, is_checked):
        is_input_checked = self.builder.get_attribute_from_element(ui_cmd_obj, locator, 'checked', strategy)
        self.logger.logger.info("current check box status: " + str(is_input_checked))
        if (not is_input_checked) and is_checked:
            self.builder.click(ui_cmd_obj, locator, strategy)
        elif is_input_checked and (not is_checked):
            self.builder.click(ui_cmd_obj, locator, strategy)

        return ui_cmd_obj

    def select_ot_from_dropdown(self, ui_cmd_obj, arg_dict):
        self.base_builder.delay(ui_cmd_obj, 5000)
        self.builder.click(ui_cmd_obj, "//span[@class='x-btn-inner x-btn-inner-extr-nav-toolbar-button-small' "
                                       "and text()='Guest Users']")
        self.spinner_loading(ui_cmd_obj)
        self.builder.click(ui_cmd_obj, "//span[@class='x-tab-inner x-tab-inner-extr-main-tab-panel' "
                                       "and text()='Guest Users']")
        self.builder.click(ui_cmd_obj, "//a[@class ='x-btn x-unselectable x-box-item x-toolbar-item x-btn-"
                                       "default-toolbar-small'][1]")
        self.spinner_loading(ui_cmd_obj)
        self.builder.click(ui_cmd_obj, "//input[@name='onboardingTemplate']")
        self.spinner_loading(ui_cmd_obj)
        index = 1
        observed_value = ''
        while index < 25:
            web_obj = self.builder.find_element(ui_cmd_obj, "//ul[@role='listbox']/li[" + str(index) + "]")
            return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
            self.logger.log_info("ot_uname: " + str(index) + "::" + return_text)
            if return_text == arg_dict['gu_otname']:
                self.logger.log_info("selected otname: " + str(index) + "::" + return_text)
                self.builder.click(ui_cmd_obj, "//ul[@role='listbox']/li[" + str(index) + "]")
                self.base_builder.delay(ui_cmd_obj, 1000)
                break
            elif return_text == observed_value:
                ui_cmd_obj.error_state = True
                break
            else:
                observed_value = return_text
                index += 1

        return ui_cmd_obj

    def is_ldap_pop_up_exists(self, ui_cmd_obj):
        web_obj = self.base_builder.find_element_by_css_selector(ui_cmd_obj, "[role='alertdialog'] div "
                                                                             "[hidefocus='on']:nth-of-type(1)")
        if self.base_builder.is_element_displayed(ui_cmd_obj, web_obj):
            self.logger.log_info("element exists")
            self.base_builder.click(ui_cmd_obj, web_obj)
            self.spinner_loading(ui_cmd_obj)
        else:
            self.logger.log_info("element not exists")

        return ui_cmd_obj
