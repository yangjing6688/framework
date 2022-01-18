from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as GimadministrationBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Gimadministration(GimadministrationBase):
    def admin_add_nac_appliance(self, ui_cmd_obj, arg_dict):
        self.builder.webdriver_wait_until(ui_cmd_obj, "//span[@class='x-btn-inner x-btn-inner-extr-nav-toolbar-"
                                                      "button-small' and text()='Administration']", retry=5)
        self.builder.click(ui_cmd_obj, "//span[@class='x-btn-inner x-btn-inner-extr-nav-toolbar-button-small' and "
                                       "text()='Administration']")
        self.spinner_loading(ui_cmd_obj)
        self.builder.click(ui_cmd_obj, "//span[text()='Access Control Engine']", self.builder.constants.STRATEGY_XPATH)
        self.spinner_loading(ui_cmd_obj)
        self.builder.click(ui_cmd_obj, "//span[@class='x-tab-inner x-tab-inner-default' and text()='Engine Details']")
        self.spinner_loading(ui_cmd_obj)
        self.add_primary_nac_details(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def add_primary_nac_details(self, ui_cmd_obj, arg_dict):
        self.builder.webdriver_wait_until(ui_cmd_obj, "//input[@name='primaryIpAddress']", retry=5)
        self.builder.click(ui_cmd_obj, "//input[@name='primaryIpAddress']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['nac_ip'], "//input[@name='primaryIpAddress']")
        self.builder.webdriver_wait_until(ui_cmd_obj, "//input[@name='username']", retry=5)
        self.builder.click(ui_cmd_obj, "//input[@name='username']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['xmc_un'], "//input[@name='username']")
        self.builder.click(ui_cmd_obj, "//input[@name='password']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['xmc_pwd'], "//input[@name='password']")
        self.builder.click(ui_cmd_obj, "Save", self.builder.constants.STRATEGY_LINK_TEXT)
        self.builder.webdriver_wait_until(ui_cmd_obj, "//div[@style='font-weight: bold; color: green;']", retry=5)
        self.builder.get_text_from_element_and_compare(ui_cmd_obj, "//div[@style='font-weight: bold; color: green;']",
                                                       "Up")

        return ui_cmd_obj

    def add_radius_details(self, ui_cmd_obj, arg_dict):
        self.builder.webdriver_wait_until(ui_cmd_obj, "//input[@name='secret']", retry=5)
        self.builder.click(ui_cmd_obj, "//input[@name='secret']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['gim_secret'], "//input[@name='secret']")
        self.builder.webdriver_wait_until(ui_cmd_obj, "//input[@name='timeout']", retry=5)
        self.builder.click(ui_cmd_obj, "//input[@name='timeout']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['rad_timeout'], "//input[@name='timeout']")
        self.builder.webdriver_wait_until(ui_cmd_obj, "//div/a[@data-qtip='Save RADIUS Configuration']", retry=5)
        self.builder.click(ui_cmd_obj, "//div/a[@data-qtip='Save RADIUS Configuration']")
        self.builder.webdriver_wait_until(ui_cmd_obj, "//span[text()='OK']", retry=5)
        self.builder.click(ui_cmd_obj, "//span[text()='OK']")
        self.builder.delay(ui_cmd_obj, 2000)

        return ui_cmd_obj

    def admin_add_radius(self, ui_cmd_obj, arg_dict):
        self.builder.webdriver_wait_until(ui_cmd_obj, "//span[@class='x-btn-inner x-btn-inner-extr-nav-toolbar-"
                                                      "button-small' and text()='Administration']", retry=5)
        self.builder.click(ui_cmd_obj, "//span[@class='x-btn-inner x-btn-inner-extr-nav-toolbar-button-small' and "
                                       "text()='Administration']")
        self.spinner_loading(ui_cmd_obj)
        self.builder.click(ui_cmd_obj, "//span[text()='Access Control Engine']", self.builder.constants.STRATEGY_XPATH)
        self.spinner_loading(ui_cmd_obj)
        self.builder.click(ui_cmd_obj, "//span[@class='x-tab-inner x-tab-inner-default' and text()='RADIUS']")
        if arg_dict['save'] == "save":
            self.add_radius_details(ui_cmd_obj, arg_dict)
        if arg_dict['restore_to_defaults'] == "restore":
            self.builder.click(ui_cmd_obj, "//div/a[@data-qtip='Save RADIUS Configuration']/following::a[1]")
            self.builder.delay(ui_cmd_obj, 2000)
            self.builder.get_attribute_from_element_and_compare(ui_cmd_obj, ".x-window-text", "innerHTML",
                                                                arg_dict['restore_rad_text'],
                                                                strategy=self.builder.constants.STRATEGY_CSS_SELECTOR)
            self.builder.click(ui_cmd_obj, "//span[@class='x-btn-inner x-btn-inner-blue-small' and text()='Yes']")
            self.builder.delay(ui_cmd_obj, 3000)
            self.add_radius_details(ui_cmd_obj, arg_dict)
            self.builder.delay(ui_cmd_obj, 3000)

        return ui_cmd_obj

    def admin_pref_add_locale(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//span[text()='Administration']", self.builder.constants.STRATEGY_XPATH)
        self.spinner_loading(ui_cmd_obj)
        self.builder.click(ui_cmd_obj, "(//span[text()='Preferences'])[1]", self.builder.constants.STRATEGY_XPATH)
        self.spinner_loading(ui_cmd_obj)
        if arg_dict['click_only_add'] == "yes_click_only_add":
            self.builder.click(ui_cmd_obj, "//span[text()='Add']", self.builder.constants.STRATEGY_XPATH)
            self.spinner_loading(ui_cmd_obj)
        elif arg_dict['click_only_add'] == "no_click_only_add":
            self.builder.click(ui_cmd_obj, "//span[text()='Add']", self.builder.constants.STRATEGY_XPATH)
            self.spinner_loading(ui_cmd_obj)
            self.builder.click(ui_cmd_obj, "//input[@name='lang']", self.builder.constants.STRATEGY_XPATH)
            self.builder.delay(ui_cmd_obj, 3000)
            flag = arg_dict['flag_name']
            self.logger.log_info(flag)
            self.builder.click(ui_cmd_obj, "//li/img[contains(@src, '" + flag + "')]")
            self.builder.click(ui_cmd_obj, "[role='dialog'] .x-btn-inner-blue-small",
                               self.builder.constants.STRATEGY_CSS_SELECTOR)
            self.builder.click(ui_cmd_obj, "//a[@data-qtip='Save Look & Feel Settings']",
                               self.builder.constants.STRATEGY_XPATH)
            self.spinner_loading(ui_cmd_obj)
        if arg_dict['set_as_default'] == "yes_set_as_default":
            self.logger.log_info("set as default block")
            web_obj = self.builder.find_elements(ui_cmd_obj, "(//div[@class='x-grid-item-container'])[1]/table")
            table_count = len(web_obj)
            self.logger.log_info("table_count: " + str(table_count))
            for index in range(1, (table_count + 1)):
                web_obj = self.builder.find_element(ui_cmd_obj, "(//div[@class='x-grid-item-container'])[1]"
                                                                "/table[" + str(index) + "]")
                web_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
                self.logger.log_info("web_text: " + web_text)
                self.logger.log_info("arg_text: " + arg_dict['flag_name'])
                if web_text.strip() == arg_dict['flag_name'].strip():
                    web_obj.click()
                    break
            return_text = self.builder.get_attribute_from_element(ui_cmd_obj, "[role] [role='presentation']:"
                                                                              "nth-of-type(3) [role] "
                                                                              "[hidefocus='on']:nth-child(4)",
                                                                  "aria-disabled",
                                                                  self.builder.constants.STRATEGY_CSS_SELECTOR)
            self.logger.log_info("aria-disabled" + return_text)
            if return_text == "false":
                self.builder.click(ui_cmd_obj, "//a[@data-qtip='Set Selected Locale as Default']")
                self.logger.log_info("set as default: done" + arg_dict['flag_name'])
            self.builder.click(ui_cmd_obj, "//a[@data-qtip='Save Look & Feel Settings']",
                               self.builder.constants.STRATEGY_XPATH)
            self.base_builder.delay(ui_cmd_obj, 5000)

        return ui_cmd_obj

    def admin_pref_del_locale(self, ui_cmd_obj, arg_dict):
        self.builder.webdriver_wait_until(ui_cmd_obj, "//span[text()='Administration']", retry=5)
        self.builder.click(ui_cmd_obj, "//span[text()='Administration']", self.builder.constants.STRATEGY_XPATH)
        self.spinner_loading(ui_cmd_obj)
        self.builder.click(ui_cmd_obj, "(//span[text()='Preferences'])[1]", self.builder.constants.STRATEGY_XPATH)
        self.spinner_loading(ui_cmd_obj)
        web_obj = self.builder.find_elements(ui_cmd_obj, "//div[3]/div[2]/div[@role='presentation']/div[@role='"
                                                         "presentation']//div[@role='grid']/div/div[@role='"
                                                         "presentation']/div[@role='rowgroup']/"
                                                         "div[@role='presentation']/table")
        table_count = len(web_obj)
        self.logger.log_info("table_count: " + str(table_count))
        if table_count > 1:
            for index in range(1, table_count):
                count = ((table_count + 1) - index)
                self.logger.log_info("count: " + str(count))
                web_obj = self.builder.find_element(ui_cmd_obj, "//div[3]/div[2]/div[@role='presentation']/div["
                                                                "@role='presentation']//div[@role='grid']/"
                                                                "div/div[@role='presentation']/div[@role='"
                                                                "rowgroup']/div[@role='presentation']/"
                                                                "table[" + str(count) + "]")
                self.base_builder.click(ui_cmd_obj, web_obj)
                self.builder.click(ui_cmd_obj, "//span[text()='Delete']", self.builder.constants.STRATEGY_XPATH)
                self.logger.log_info("deleted " + str(count) + " row")
                self.builder.delay(ui_cmd_obj, 5000)
            self.logger.log_info("deleted locales successfully")
            self.builder.click(ui_cmd_obj, "//a[@data-qtip='Save Look & Feel Settings']",
                               self.builder.constants.STRATEGY_XPATH)
            self.base_builder.delay(ui_cmd_obj, 5000)
        else:
            self.logger.log_info("locale count is 1, no need to delete any locale")

        return ui_cmd_obj

    def gim_admin_test_connection_nac_appliance_connection(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//span[@class='x-btn-inner x-btn-inner-default-small' and text()='Test']")
        self.builder.delay(ui_cmd_obj, 5)
        self.builder.get_attribute_from_element_and_compare(ui_cmd_obj, ".x-window-text", "innerHTML",
                                                            arg_dict['entire_text'],
                                                            strategy=self.builder.constants.STRATEGY_CSS_SELECTOR)
        self.builder.webdriver_wait_until(ui_cmd_obj, "//span[text()='OK']", retry=5)
        self.builder.click(ui_cmd_obj, "//span[text()='OK']")

        return ui_cmd_obj

    def gim_admin_email_notification(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//span[@class='x-tab-inner x-tab-inner-extr-main-tab-panel' "
                                       "and text()='Notification']")
        self.spinner_loading(ui_cmd_obj)
        self.builder.click(ui_cmd_obj, "//span[@class='x-tab-inner x-tab-inner-default' and text()='E-mail']")
        if arg_dict['email_notification'] == "enable_notification":
            self.set_check_box_value(ui_cmd_obj, "//input[@name='enableEmail']", self.builder.constants.STRATEGY_XPATH,
                                     True)
            self.builder.click(ui_cmd_obj, "//input[@name='fromAddress']")
            self.builder.enter_text(ui_cmd_obj, arg_dict['from_address'], "//input[@name='fromAddress']")
            self.builder.click(ui_cmd_obj, "//input[@name='server']")
            self.builder.enter_text(ui_cmd_obj, arg_dict['email_server'], "//input[@name='server']")
            self.builder.click(ui_cmd_obj, "//a[@data-qtip='Save Email Settings']")
            self.spinner_loading(ui_cmd_obj)
        if arg_dict['email_notification'] == "restore_to_default":
            self.builder.click(ui_cmd_obj, "//a[@data-qtip='Restore to Default Email Settings']")
            self.builder.click(ui_cmd_obj, "//span[@class='x-btn-inner x-btn-inner-blue-small' and text()='Yes']")
            self.builder.delay(ui_cmd_obj, 5)
            self.builder.element_exists(ui_cmd_obj, "(//div[@class='x-field x-form-item "
                                                    "x-form-item-default x-form-type-text "
                                                    "x-field-default x-anchor-form-item "
                                                    "x-item-disabled'])[1]")
            self.builder.element_exists(ui_cmd_obj, "(//div[@class='x-field x-form-item "
                                                    "x-form-item-default x-form-type-text "
                                                    "x-field-default x-anchor-form-item "
                                                    "x-item-disabled'])[2]")
            self.builder.element_exists(ui_cmd_obj, "(//div[@class='x-field x-form-item "
                                                    "x-form-item-default x-form-type-text "
                                                    "x-field-default x-anchor-form-item "
                                                    "x-item-disabled'])[1]")
            self.builder.element_exists(ui_cmd_obj, "//div[@class='x-field x-form-item "
                                                    "x-form-item-default x-form-type-text "
                                                    "x-field-default x-anchor-form-item "
                                                    "x-form-dirty x-item-disabled']")
            self.builder.element_exists(ui_cmd_obj, "//div[@class='x-field x-form-item "
                                                    "x-form-item-default x-form-type-checkbox "
                                                    "x-field-default x-anchor-form-item "
                                                    "x-form-item-no-label x-item-disabled']")
            self.builder.element_exists(ui_cmd_obj, "//div/a[@class='x-btn x-unselectable x-btn-blue-small "
                                                    "x-item-disabled x-btn-disabled']")
            self.builder.click(ui_cmd_obj, "//input[@name='enableEmail']")
            self.builder.click(ui_cmd_obj, "//input[@name='fromAddress']")
            self.builder.enter_text(ui_cmd_obj, arg_dict['from_address'], "//input[@name='fromAddress']")
            self.builder.click(ui_cmd_obj, "//input[@name='server']")
            self.builder.enter_text(ui_cmd_obj, arg_dict['email_server'], "//input[@name='server']")
            self.builder.click(ui_cmd_obj, "//a[@data-qtip='Save Email Settings']")
            self.spinner_loading(ui_cmd_obj)

        return ui_cmd_obj

    def gim_admin_restore_default_nac_appliance_configuration(self, ui_cmd_obj, arg_dict):
        # Restore Configuration to Restore Default
        self.builder.click(ui_cmd_obj, "//span[@class='x-btn-inner x-btn-inner-extr-nav-toolbar-button-small' and "
                                       "text()='Administration']")
        self.spinner_loading(ui_cmd_obj)
        self.builder.click(ui_cmd_obj, "//span[text()='Access Control Engine']", self.builder.constants.STRATEGY_XPATH)
        self.spinner_loading(ui_cmd_obj)
        self.builder.click(ui_cmd_obj, "//span[@class='x-tab-inner x-tab-inner-default' and text()='Engine Details']")
        self.builder.click(ui_cmd_obj, "(//span[@class='x-btn-inner x-btn-inner-default-small' "
                                       "and text()='Restore to Defaults'])[1]")
        self.builder.delay(ui_cmd_obj, 10)
        web_text = self.builder.get_attribute_from_element(ui_cmd_obj, ".x-window-text", "innerHTML",
                                                           self.builder.constants.STRATEGY_CSS_SELECTOR)
        self.logger.log_info(web_text)
        if web_text != arg_dict['restore_text']:
            ui_cmd_obj.error_state = True
        self.builder.click(ui_cmd_obj, "//span[@class='x-btn-inner x-btn-inner-blue-small' and text()='Yes']")
        self.builder.delay(ui_cmd_obj, 5)
        return_text = self.builder.get_text_from_element(ui_cmd_obj, "//div[@style='font-weight: bold; color: red;']")
        self.logger.log_info("return_text: " + return_text)
        if return_text != "Not Configured":
            self.logger.log_info(return_text + "is not equal to Not Configured")
            ui_cmd_obj.error_state = True
        self.add_primary_nac_details(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def gim_admin_add_sms_gateway(self, ui_cmd_obj, arg_dict):
        self.builder.delay(ui_cmd_obj, 5)
        self.builder.click(ui_cmd_obj, "//span[@class='x-btn-inner x-btn-inner-extr-nav-toolbar-button-small' "
                                       "and text()='Administration']")
        self.builder.click(ui_cmd_obj, "//span[@class='x-tab-inner x-tab-inner-extr-main-tab-panel' "
                                       "and text()='Notification']")
        self.builder.click(ui_cmd_obj, "//span[@class='x-tab-inner x-tab-inner-default' and text()='E-mail']")
        self.builder.click(ui_cmd_obj, "//span[@class='x-tab-inner x-tab-inner-default' and text()='SMS']")
        self.wait_for_page_load_completely(ui_cmd_obj)
        self.builder.click(ui_cmd_obj, "//span[text()='Add']")
        self.builder.click(ui_cmd_obj, "//div[1]/a[@role='menuitem']/span[@role='presentation']")
        self.builder.click(ui_cmd_obj, "//input[@name='phoneCarrier']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['phone_carrier'], "//input[@name='phoneCarrier']")
        self.builder.click(ui_cmd_obj, "//input[@name='phoneCarrierGateways']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['phone_gateway'], "//input[@name='phoneCarrierGateways']")
        self.builder.click(ui_cmd_obj, "//input[@name='phoneNumber']")
        li_number = arg_dict['pn_option']
        self.builder.click(ui_cmd_obj, "//body[@role='application']//ul[@role='listbox']/li[" + li_number + "]",
                           self.builder.constants.STRATEGY_XPATH)
        if li_number == "3":
            self.builder.delay(ui_cmd_obj, 5)
            self.builder.click(ui_cmd_obj, "//input[@name='otherDigitsLength']")
            self.builder.enter_text(ui_cmd_obj, "10", "//input[@name='otherDigitsLength']")
        self.builder.delay(ui_cmd_obj, 5)
        if arg_dict['save'] == "Save":
            self.builder.click(ui_cmd_obj, "[role='dialog'] [role='toolbar'] .x-btn-inner-blue-small",
                               self.builder.constants.STRATEGY_CSS_SELECTOR)

        return ui_cmd_obj

    def wait_for_page_load_completely(self, ui_cmd_obj):
        self.logger.log_info("waiting for the page to load...")
        for x in range(1, 25):
            self.base_builder.delay(ui_cmd_obj, 250)
            self.base_builder.execute_script(ui_cmd_obj, "return document.readyState;")
            self.logger.log_info("page readyState:  " + str(ui_cmd_obj.return_data))
            if ui_cmd_obj.return_data == "complete":
                self.logger.log_info("page loaded completely: ")
                break

        return ui_cmd_obj

    def gim_admin_add_sms_provider(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//span[@class='x-btn-inner x-btn-inner-extr-nav-toolbar-button-small' "
                                       "and text()='Administration']")
        self.builder.click(ui_cmd_obj, "//span[@class='x-tab-inner x-tab-inner-extr-main-tab-panel' "
                                       "and text()='Notification']")
        self.builder.click(ui_cmd_obj, "//span[@class='x-tab-inner x-tab-inner-default' and text()='SMS']")
        self.builder.delay(ui_cmd_obj, 5)
        if arg_dict['add_edit_delete'] == "add":
            self.builder.click(ui_cmd_obj, "//span[text()='Add']")
            self.builder.click(ui_cmd_obj, "//div[2]/a[@role='menuitem']/span[@role='presentation']")
            self.builder.click(ui_cmd_obj, "//input[@name='phoneCarrier']")
            self.builder.enter_text(ui_cmd_obj, arg_dict['phone_carrier'], "//input[@name='phoneCarrier']")
            self.builder.click(ui_cmd_obj, "//input[@name='apiKey']")
            self.builder.enter_text(ui_cmd_obj, "ABCDFGE13D4FGTIQWE", "//input[@name='apiKey']")
            self.select_api_type_from_sms_provider(ui_cmd_obj, arg_dict)
            self.builder.click(ui_cmd_obj, "[role='dialog'] [role='toolbar'] .x-btn-inner-blue-small",
                               self.builder.constants.STRATEGY_CSS_SELECTOR)
            self.builder.delay(ui_cmd_obj, 5)
        if arg_dict['add_edit_delete'] == "edit":
            self.select_row_from_sms_table(ui_cmd_obj, arg_dict)
            self.builder.click(ui_cmd_obj, "[role] [hidefocus='on']:nth-of-type(2) .x-btn-inner-default-toolbar-small",
                               self.builder.constants.STRATEGY_CSS_SELECTOR)
            self.builder.click(ui_cmd_obj, "//input[@name='apiKey']")
            self.builder.enter_text(ui_cmd_obj, "ABCDFGE13D4FGTIQWE12", "//input[@name='apiKey']")
            self.builder.click(ui_cmd_obj, "[role='dialog'] [role='toolbar'] .x-btn-inner-blue-small",
                               self.builder.constants.STRATEGY_CSS_SELECTOR)
            self.builder.delay(ui_cmd_obj, 5)
        if arg_dict['add_edit_delete'] == "delete":
            self.select_row_from_sms_table(ui_cmd_obj, arg_dict)
            self.builder.click(ui_cmd_obj, "//a[@data-qtip='Delete selected SMS Gateway(s)/Provider(s)']")
            self.builder.click(ui_cmd_obj, "//span[@class='x-btn-inner x-btn-inner-blue-small' and text()='Yes']")

        return ui_cmd_obj

    def gim_admin_secondary_nac_appliance_configuration(self, ui_cmd_obj, arg_dict):
        self.builder.webdriver_wait_until(ui_cmd_obj, "//span[@class='x-btn-inner x-btn-inner-extr-nav-toolbar-"
                                                      "button-small' and text()='Administration']", retry=5)
        self.builder.click(ui_cmd_obj, "//span[@class='x-btn-inner x-btn-inner-extr-nav-toolbar-button-small' and "
                                       "text()='Administration']")
        self.spinner_loading(ui_cmd_obj)
        self.builder.click(ui_cmd_obj, "//span[text()='Access Control Engine']", self.builder.constants.STRATEGY_XPATH)
        self.spinner_loading(ui_cmd_obj)
        self.builder.click(ui_cmd_obj, "//span[@class='x-tab-inner x-tab-inner-default' and text()='Engine Details']")
        self.builder.click(ui_cmd_obj, "//input[@name='secondaryIpAddress']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['nac_ip2'], "//input[@name='secondaryIpAddress']")
        self.builder.delay(ui_cmd_obj, 2)
        self.builder.click(ui_cmd_obj, "//input[@name='username']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['xmc_un'], "//input[@name='username']")
        self.builder.click(ui_cmd_obj, "//input[@name='password']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['xmc_pwd'], "//input[@name='password']")
        self.builder.click(ui_cmd_obj, "//a[@data-qtip='Save Access Control Engine Details']")
        self.builder.webdriver_wait_until(ui_cmd_obj, "//span[text()='OK']", retry=5)
        self.builder.click(ui_cmd_obj, "//span[text()='OK']")

        return ui_cmd_obj

    def gim_admin_ace_tabs_page_validation(self, ui_cmd_obj, arg_dict):
        self.builder.webdriver_wait_until(ui_cmd_obj, "//span[@class='x-btn-inner x-btn-inner-extr-nav-toolbar-"
                                                      "button-small' and text()='Administration']", retry=5)
        self.builder.click(ui_cmd_obj, "//span[@class='x-btn-inner x-btn-inner-extr-nav-toolbar-button-small' "
                                       "and text()='Administration']")
        self.builder.click(ui_cmd_obj, "//span[text()='Access Control Engine']",
                           self.builder.constants.STRATEGY_XPATH)
        self.builder.click(ui_cmd_obj, "//span[@class='x-tab-inner x-tab-inner-default' and text()='Engine Details']")
        # Primary Ip-address
        return_text = self.builder.get_text_from_element(ui_cmd_obj, "//input[@name='primaryIpAddress']"
                                                                     "/preceding::label[1]/span/span")
        self.logger.log_info(return_text)
        if return_text == arg_dict['primary_engine']:
            ui_cmd_obj.error_state = False
        else:
            ui_cmd_obj.error_state = True
        # Ip-address Value
        self.builder.get_attribute_from_element(ui_cmd_obj, "//input[@name='primaryIpAddress']", "value")
        self.logger.log_info(return_text)
        if return_text == arg_dict['nac_ip']:
            ui_cmd_obj.error_state = False
        else:
            ui_cmd_obj.error_state = True
        # Secondary Ip-address
        return_text = self.builder.get_text_from_element(ui_cmd_obj, "//input[@name='secondaryIpAddress']"
                                                                     "/preceding::label[1]/span/span")
        self.logger.log_info(return_text)
        if return_text == arg_dict['second_nac_engine']:
            ui_cmd_obj.error_state = False
        else:
            ui_cmd_obj.error_state = True
        # Note
        return_text = self.builder.get_text_from_element(ui_cmd_obj, "//input[@name='secondaryIpAddress']/"
                                                                     "following::div[1]")
        self.logger.log_info(return_text)
        if return_text == arg_dict['note']:
            ui_cmd_obj.error_state = False
        else:
            ui_cmd_obj.error_state = True
        # Port
        self.builder.get_text_from_element(ui_cmd_obj, "//input[@name='port']/preceding::label[1]/span/span")
        self.logger.log_info(return_text)
        if return_text == arg_dict['port']:
            ui_cmd_obj.error_state = False
        else:
            ui_cmd_obj.error_state = True
        # Port Value
        return_text = self.builder.get_attribute_from_element(ui_cmd_obj, "//input[@name='port']", "value")
        self.logger.log_info(return_text)
        if return_text == arg_dict['port_value']:
            ui_cmd_obj.error_state = False
        else:
            self.builder.error_state = True
        # Username
        return_text = self.builder.get_text_from_element(ui_cmd_obj, "//input[@name='username']/"
                                                                     "preceding::label[1]/span/span")
        self.logger.log_info(return_text)
        if return_text == arg_dict['xmc_admin_username']:
            self.builder.error_state = False
        else:
            self.builder.error_state = True
        # Username Value
        self.builder.get_attribute_from_element(ui_cmd_obj, "//input[@name='username']", "value")
        self.logger.log_info(return_text)
        if return_text == arg_dict['xmc_un']:
            self.builder.error_state = False
        else:
            self.builder.error_state = True
        # Password
        return_text = self.builder.get_text_from_element(ui_cmd_obj,
                                                         "//input[@name='password']/preceding::label[1]/span/span")
        self.logger.log_info(return_text)
        if return_text == arg_dict['xmc_admin_password']:
            self.builder.error_state = False
        else:
            self.builder.error_state = True
        # Password Value
        return_text = self.builder.get_attribute_from_element(ui_cmd_obj, "//input[@name='password']", "value")
        self.logger.log_info(return_text)
        if return_text == arg_dict['xmc_pwd']:
            self.builder.error_state = False
        else:
            self.builder.error_state = True
        # ACE -Status
        return_text = self.builder.get_text_from_element(ui_cmd_obj, "//span[@class='x-form-item-label-text'"
                                                                     "and text()='Access Control Engine Status:']")
        self.logger.log_info(return_text)
        if return_text == arg_dict['ace_status']:
            self.builder.error_state = False
        else:
            self.builder.error_state = True
        # Save Button
        return_text = self.builder.get_text_from_element(ui_cmd_obj, "//span[@class='x-btn-inner x-btn-inner-"
                                                                     "blue-small' and text()='Save']")
        self.logger.log_info(return_text)
        if return_text == arg_dict['save_button']:
            self.builder.error_state = False
        else:
            self.builder.error_state = True
        # Test Button
        return_text = self.builder.get_text_from_element(ui_cmd_obj, "//span[@class='x-btn-inner x-btn-inner-"
                                                                     "default-small' and text()='Test']")
        self.logger.log_info(return_text)
        if return_text == arg_dict['test_button']:
            self.builder.error_state = False
        else:
            self.builder.error_state = True
        # Restore Button
        return_text = self.builder.get_text_from_element(ui_cmd_obj, "//span[@class='x-btn-inner x-btn-inner-default-"
                                                                     "small' and text()='Restore to Defaults']")
        self.logger.log_info(return_text)
        if return_text == arg_dict['restore_button']:
            self.builder.error_state = False
        else:
            self.builder.error_state = True

        return ui_cmd_obj

    def gim_admin_ace_radius_page_validation(self, ui_cmd_obj, arg_dict):
        # RADIUS TAB Page
        self.builder.click(ui_cmd_obj, "//span[@class='x-tab-inner x-tab-inner-default' and text()='RADIUS']")
        # RADIUS Port
        return_text = self.builder.get_text_from_element(ui_cmd_obj,
                                                         "(//input[@name='port']/preceding::label[1]/span/span)[2]")
        self.logger.log_info(return_text)
        if return_text == arg_dict['radius_port']:
            self.builder.error_state = False
        else:
            self.builder.error_state = True
        # Radius Port Value
        return_text = self.builder.get_attribute_from_element(ui_cmd_obj, "(//input[@name='port'])[1]", "value")
        self.logger.log_info(return_text)
        if return_text == arg_dict['radius_port_value']:
            self.builder.error_state = False
        else:
            self.builder.error_state = True
        # Key
        return_text = self.builder.get_text_from_element(ui_cmd_obj,
                                                         "//input[@name='secret']/preceding::label[1]/span/span")
        self.logger.log_info(return_text)
        if return_text == arg_dict['radius_shared_secret']:
            self.builder.error_state = False
        else:
            self.builder.error_state = True
        # Key Value
        return_text = self.builder.get_attribute_from_element(ui_cmd_obj, "//input[@name='secret']", "value")
        self.logger.log_info(return_text)
        if return_text == arg_dict['secret']:
            self.builder.error_state = False
        else:
            self.builder.error_state = True
        # TimeOut
        return_text = self.builder.get_text_from_element(ui_cmd_obj,
                                                         "//input[@name='timeout']/preceding::label[1]/span/span")
        self.logger.log_info(return_text)
        if return_text == arg_dict['radius_timeout']:
            self.builder.error_state = False
        else:
            self.builder.error_state = True
        # Time out Note
        return_text = self.builder.get_text_from_element(ui_cmd_obj, ".x-autocontainer-innerCt .x-component-"
                                                                     "default:nth-of-type(5)",
                                                         self.builder.constants.STRATEGY_CSS_SELECTOR)
        self.logger.log_info(return_text)
        if return_text == arg_dict['timeout_note']:
            self.builder.error_state = False
        else:
            self.builder.error_state = True
        # Note
        return_text = self.builder.get_text_from_element(ui_cmd_obj,
                                                         ".x-autocontainer-innerCt .x-component-"
                                                         "default:nth-of-type(6)",
                                                         self.builder.constants.STRATEGY_CSS_SELECTOR)

        self.logger.log_info(return_text)
        if return_text == arg_dict['radius_note']:
            self.builder.error_state = False
        else:
            self.builder.error_state = True
        # Save
        return_text = self.builder.get_text_from_element(ui_cmd_obj, "(//span[@class='x-btn-inner x-btn-inner-"
                                                                     "blue-small' and text()='Save'])[2]")
        self.logger.log_info(return_text)
        if return_text == arg_dict['save_button']:
            self.builder.error_state = False
        else:
            self.builder.error_state = True
        # Restore Button
        return_text = self.builder.get_text_from_element(ui_cmd_obj, "//div/a[@data-qtip='Save RADIUS "
                                                                     "Configuration']/following::a[1]")
        self.logger.log_info(return_text)
        if return_text == arg_dict['restore_button']:
            self.builder.error_state = False
        else:
            self.builder.error_state = True
        return ui_cmd_obj

    def gim_admin_account_settings_validation(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//span[@class='x-tab-inner x-tab-inner-extr-main-tab-panel' "
                                       "and text()='Account']")
        self.builder.click(ui_cmd_obj, "//span[@class='x-tab-inner x-tab-inner-default' and text()='Settings']")
        self.builder.delay(ui_cmd_obj, 5)
        # Administration Text
        true_or_false = self.builder.get_attribute_from_element(ui_cmd_obj,
                                                                ".x-autocontainer-innerCt:nth-of-type(1) > "
                                                                "[role='presentation']:nth-of-type(1) b",
                                                                "innerText",
                                                                self.builder.constants.STRATEGY_CSS_SELECTOR)
        self.logger.log_info(true_or_false)
        if true_or_false == "true":
            self.builder.error_state = False
        else:
            self.builder.error_state = True
        self.builder.delay(ui_cmd_obj, 3)
        return_text = self.builder.get_text_from_element(ui_cmd_obj, "//input[@name='adminName']/preceding::label[1]")
        self.logger.log_info(return_text)
        if return_text == arg_dict['admin_name']:
            self.builder.error_state = False
        else:
            self.builder.error_state = True
        # Validate Change Password
        self.is_element_enabled(ui_cmd_obj, "//input[@name='changeAdminPwd']/following::label[1]")
        self.logger.log_info("By Default Change password checkbox is not enabled")
        return_text = self.builder.get_text_from_element(ui_cmd_obj, "//input[@name='changeAdminPwd']/"
                                                                     "following::label[1]")
        self.logger.log_info(return_text)
        if return_text == arg_dict['change_pwd']:
            self.builder.error_state = False
        else:
            self.builder.error_state = True
        self.builder.delay(ui_cmd_obj, 5)
        # Change Password Current Password , Change Password
        self.builder.click(ui_cmd_obj, "//input[@name='changeAdminPwd']")
        return_text = self.builder.get_text_from_element(ui_cmd_obj, "//input[@name='changeAdminPwd']/"
                                                                     "following::label[2]")
        self.logger.log_info(return_text)
        if return_text == arg_dict['current_pwd']:
            self.builder.error_state = False
        else:
            self.builder.error_state = True
        # New password
        return_text = self.builder.get_text_from_element(ui_cmd_obj, "//input[@name='changeAdminPwd']/"
                                                                     "following::label[3]")
        self.logger.log_info(return_text)
        if return_text == arg_dict['new_pwd']:
            self.builder.error_state = False
        else:
            self.builder.error_state = True
        # Confirm Password
        return_text = self.builder.get_text_from_element(ui_cmd_obj, "//input[@name='changeAdminPwd']/"
                                                                     "following::label[4]")
        self.logger.log_info(return_text)
        if return_text == arg_dict['confirm_pwd']:
            self.builder.error_state = False
        else:
            self.builder.error_state = True
        self.builder.delay(ui_cmd_obj, 5)
        self.builder.click(ui_cmd_obj, "//input[@name='changeAdminPwd']")
        # Inactivity Timeout
        true_or_false = self.builder.get_attribute_from_element(ui_cmd_obj, "[role='form'] [role='presentation']:"
                                                                            "nth-of-type(2) b", "innerText",
                                                                self.builder.constants.STRATEGY_CSS_SELECTOR)
        self.logger.log_info(true_or_false)
        if true_or_false == "true":
            self.builder.error_state = False
        else:
            self.builder.error_state = True
        # Provisioner Idle Timeout
        return_text = self.builder.get_text_from_element(ui_cmd_obj, "//input[@name='provisionerIdleTimeout']"
                                                                     "/preceding::label[1]")
        self.logger.log_info(return_text)
        if return_text == arg_dict['idle_timeout']:
            self.builder.error_state = False
        else:
            self.builder.error_state = True
        # Minutes
        return_text = self.builder.get_attribute_from_element(ui_cmd_obj, "//input[@name='provisionerIdleTimeout']",
                                                              "value")
        self.logger.log_info(return_text)
        if return_text == arg_dict['idle_timevalue']:
            self.builder.error_state = False
        else:
            self.builder.error_state = True
        # Outlook Minutes
        return_text = self.builder.get_text_from_element(ui_cmd_obj, "//input[@name='outlookIdleTimeout']/"
                                                                     "preceding::label[1]")
        self.logger.log_info(return_text)
        if return_text == arg_dict['idle_timeout_outlook']:
            self.builder.error_state = False
        else:
            self.builder.error_state = True
        # Hours
        return_text = self.builder.get_attribute_from_element(ui_cmd_obj, "//input[@name='outlookIdleTimeoutUnit']",
                                                              "value")
        self.logger.log_info(return_text)
        if return_text == arg_dict['idle_outlook_value']:
            self.builder.error_state = False
        else:
            self.builder.error_state = True
        # Note
        return_text = self.builder.get_text_from_element(ui_cmd_obj, "//input[@name='outlookIdleTimeoutUnit']/"
                                                                     "following::label[1]")
        self.logger.log_info(return_text)
        if return_text == arg_dict['account_note']:
            self.builder.error_state = False
        else:
            self.builder.error_state = True
        return ui_cmd_obj

    def gim_admin_change_sms_default_gateway(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//span[@class='x-tab-inner x-tab-inner-extr-main-tab-panel' "
                                       "and text()='Notification']")
        self.builder.click(ui_cmd_obj, "//span[@class='x-tab-inner x-tab-inner-default' and text()='SMS']")
        self.select_row_from_sms_table(ui_cmd_obj, arg_dict)
        self.builder.click(ui_cmd_obj, "//span[@class='x-btn-inner x-btn-inner-default-toolbar-small' "
                                       "and text()='Set as Default']")

        return ui_cmd_obj

    def gim_admin_validating_sms_gateways(self, ui_cmd_obj, arg_dict):
        all_count = ""
        self.builder.click(ui_cmd_obj, "//span[@class='x-tab-inner x-tab-inner-extr-main-tab-panel' "
                                       "and text()='Notification']")
        self.builder.click(ui_cmd_obj, "//span[@class='x-tab-inner x-tab-inner-default' and text()='E-mail']")
        self.builder.click(ui_cmd_obj, "//span[@class='x-tab-inner x-tab-inner-default' and text()='SMS']")
        self.wait_for_page_load_completely(ui_cmd_obj)
        if arg_dict['add_or_edit'] == "add":
            all_count = self.builder.find_elements(ui_cmd_obj, "//div[@class ='x-grid-item-container']/table/tbody/"
                                                               "tr/td[3]")
        if arg_dict['add_or_edit'] == "edit":
            all_count = self.builder.find_elements(ui_cmd_obj, "//div[@class ='x-grid-item-container']/table/tbody/"
                                                               "tr/td[4]")
        row_count = len(all_count)
        self.logger.log_info("row_count: " + str(row_count))
        for x in all_count:
            self.logger.log_info("x value: " + str(x.text))
            if str(x.text) == arg_dict['phone_carrier']:
                ui_cmd_obj.error_state = False
                self.logger.log_info("<" + arg_dict['phone_carrier'] + "> phone_carrier/gateways: exists ::" +
                                     str(x.text))
                break
            else:
                self.logger.log_info("<" + arg_dict['phone_carrier'] + "> phone_carrier/gateways: does not exists ::" +
                                     str(x.text))
                ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def gim_admin_delete_sms_gateway(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//span[@class='x-tab-inner x-tab-inner-extr-main-tab-panel' "
                                       "and text()='Notification']")
        self.builder.click(ui_cmd_obj, "//span[@class='x-tab-inner x-tab-inner-default' and text()='SMS']")
        self.select_row_from_sms_table(ui_cmd_obj, arg_dict)
        self.builder.click(ui_cmd_obj, "//a[@data-qtip='Delete selected SMS Gateway(s)/Provider(s)']")
        self.builder.click(ui_cmd_obj, "//span[@class='x-btn-inner x-btn-inner-blue-small' and text()='Yes']")
        self.builder.delay(ui_cmd_obj, 5)

        return ui_cmd_obj

    def select_row_from_sms_table(self, ui_cmd_obj, arg_dict):
        self.builder.delay(ui_cmd_obj, 5)
        all_count = self.builder.find_elements(ui_cmd_obj, "//div[@class ='x-grid-item-container']/table/tbody/"
                                                           "tr/td[3]")
        row_count = len(all_count)
        self.logger.log_info("row_count: " + str(row_count))
        for x in all_count:
            self.logger.log_info("x value: " + str(x.text))
            if str(x.text) == arg_dict['phone_carrier']:
                self.base_builder.execute_script(ui_cmd_obj, "arguments[0].scrollIntoView(true);", x)
                self.base_builder.click(ui_cmd_obj, x)
                self.logger.log_info("<" + arg_dict['phone_carrier'] + "> phone_carrier/gateways: clicked ::" +
                                     str(x.text))
                break
            else:
                self.logger.log_info("<" + arg_dict['phone_carrier'] + "> phone_carrier/gateways: not clicked ::" +
                                     str(x.text))

        return ui_cmd_obj

    def gim_admin_email_page_validation(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//span[@class='x-tab-inner x-tab-inner-extr-main-tab-panel' "
                                       "and text()='Notification']")
        self.builder.click(ui_cmd_obj, "//span[@class='x-tab-inner x-tab-inner-default' and text()='E-mail']")
        self.is_element_enabled(ui_cmd_obj, "//input[@name='enableEmail']/following::label[1]")
        self.logger.log_info("By Default Sending of Email Notification checkbox is not enabled")
        self.builder.delay(ui_cmd_obj, 5)
        # Enable Send email notification validation
        web_obj = self.builder.find_element(ui_cmd_obj, "//input[@name='enableEmail']/following::label[1]")
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_text)
        if return_text == arg_dict['enable_notification']:
            self.builder.error_state = False
        else:
            self.builder.error_state = True
        self.builder.delay(ui_cmd_obj, 5)
        # From Address
        web_obj = self.builder.find_element(ui_cmd_obj, "//input[@name='fromAddress']/preceding::label[1]")
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_text)
        if return_text == arg_dict['email_address']:
            self.builder.error_state = False
        else:
            self.builder.error_state = True
        # Server Ip-address
        web_obj = self.builder.find_element(ui_cmd_obj, "//input[@name='server']/preceding::label[1]")
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_text)
        if return_text == arg_dict['email_server']:
            self.builder.error_state = False
        else:
            self.builder.error_state = True
        # Security
        web_obj = self.builder.find_element(ui_cmd_obj, "//input[@name='security']/preceding::label[1]")
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_text)
        if return_text == arg_dict['email_security']:
            self.builder.error_state = False
        else:
            self.builder.error_state = True
        # Port
        web_obj = self.builder.find_element(ui_cmd_obj, "//input[@name='port']/preceding::label[1]")
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_text)
        if return_text == arg_dict['email_port']:
            self.builder.error_state = False
        else:
            self.builder.error_state = True
        # User Authentication
        self.is_element_enabled(ui_cmd_obj, "//input[@name='userAuth']/following::label[1]")
        self.logger.log_info("By Default User Authentication checkbox is not enabled")
        self.builder.delay(ui_cmd_obj, 5)
        web_obj = self.builder.find_element(ui_cmd_obj, "//input[@name='userAuth']/following::label[1]")
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_text)
        if return_text == arg_dict['email_user_authentication']:
            self.builder.error_state = False
        else:
            self.builder.error_state = True

        return ui_cmd_obj

    def gim_admin_test_email_notification(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//span[@class='x-tab-inner x-tab-inner-extr-main-tab-panel'"
                                       "and text()='Notification']")
        self.builder.click(ui_cmd_obj, "//span[@class='x-tab-inner x-tab-inner-default' and text()='E-mail']")
        self.builder.click(ui_cmd_obj, "//span[@class='x-btn-inner x-btn-inner-blue-small' and text()='Test']")
        self.builder.click(ui_cmd_obj, "//input[@name='toAddress']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['to_address'], "//input[@name='toAddress']")
        self.builder.click(ui_cmd_obj, "//span[@class='x-btn-inner x-btn-inner-blue-small' "
                                       "and text()='Send Test Email']")
        self.builder.delay(ui_cmd_obj, 15)
        web_obj = self.builder.find_element(ui_cmd_obj, ".x-window-text", self.builder.constants.STRATEGY_CSS_SELECTOR)
        self.builder.delay(ui_cmd_obj, 5)
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info("return_text: " + return_text)
        if return_text != "Successfully sent Test email.":
            self.logger.log_info("return text is not equal: <" + return_text + ">Successfully sent Test email")
            self.builder.error_state = True
        self.builder.click(ui_cmd_obj, "//span[text()='OK']")
        self.builder.delay(ui_cmd_obj, 10)

        return ui_cmd_obj

    def gim_administration_default_page_validation(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//span[@class='x-btn-inner x-btn-inner-extr-nav-toolbar-button-small' and "
                                       "text()='Administration']")
        # Account
        return_text = self.builder.get_text_from_element(ui_cmd_obj, "//span[@class='x-tab-inner x-tab-inner-"
                                                                     "extr-main-tab-panel' and text()='Account']")
        self.logger.log_info(return_text)
        if return_text == arg_dict['account_tab']:
            self.builder.error_state = False
        else:
            self.builder.error_state = True
        # Account TAB selected or not
        true_or_false = self.builder.get_attribute_from_element(ui_cmd_obj, ".x-tab-bar-body-extr-main-tab-panel "
                                                                            "div [hidefocus='on']:nth-of-type(1)",
                                                                "aria-selected",
                                                                self.builder.constants.STRATEGY_CSS_SELECTOR)
        self.logger.log_info(true_or_false)
        if true_or_false == "false":
            self.builder.error_state = False
        else:
            self.builder.error_state = True
        # Preference
        web_obj = self.builder.find_element(ui_cmd_obj, "//span[@class='x-tab-inner x-tab-inner-extr-main-"
                                                        "tab-panel' and text()='Preferences']")
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_text)
        if return_text == arg_dict['preferences_tab']:
            self.builder.error_state = False
        else:
            self.builder.error_state = True
        # Preference Selected or not
        web_obj = self.builder.find_element(ui_cmd_obj, ".x-tab-bar-body-extr-main-tab-panel div [hidefocus='on']"
                                                        ":nth-of-type(2)",
                                            self.builder.constants.STRATEGY_CSS_SELECTOR)
        true_or_false = self.base_builder.get_attribute_from_element(ui_cmd_obj, web_obj, "aria-selected")
        self.logger.log_info(true_or_false)
        if true_or_false == "false":
            self.builder.error_state = False
        else:
            self.builder.error_state = True
        # Backup/Restore
        web_obj = self.builder.find_element(ui_cmd_obj, "//span[@class='x-tab-inner x-tab-inner-extr-main"
                                                        "-tab-panel' and text()='Backup/Restore']")
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_text)
        if return_text == arg_dict['back_restore_tab']:
            self.builder.error_state = False
        else:
            self.builder.error_state = True
        # B/R selected or not
        web_obj = self.builder.find_element(ui_cmd_obj, ".x-tab-bar-body-extr-main-tab-panel div [hidefocus='on']"
                                                        ":nth-of-type(3)",
                                            self.builder.constants.STRATEGY_CSS_SELECTOR)
        true_or_false = self.base_builder.get_attribute_from_element(ui_cmd_obj, web_obj, "aria-selected")
        if true_or_false == "false":
            self.builder.error_state = False
        else:
            self.builder.error_state = True
        # Certificates
        web_obj = self.builder.find_element(ui_cmd_obj, "//span[@class='x-tab-inner x-tab-inner-extr-main-tab-panel' "
                                                        "and text()='Certificates']")
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_text)
        if return_text == arg_dict['certificates_tab']:
            self.builder.error_state = False
        else:
            self.builder.error_state = True
        # cert Selected ot not
        web_obj = self.builder.find_element(ui_cmd_obj, ".x-tab-bar-body-extr-main-tab-panel div [hidefocus='on']"
                                                        ":nth-of-type(4)",
                                            self.builder.constants.STRATEGY_CSS_SELECTOR)
        true_or_false = self.base_builder.get_attribute_from_element(ui_cmd_obj, web_obj, "aria-selected")
        self.logger.log_info(true_or_false)
        if true_or_false == "false":
            self.builder.error_state = False
        else:
            self.builder.error_state = True
        # Access control Engine TAB
        web_obj = self.builder.find_element(ui_cmd_obj, "//span[@class='x-tab-inner x-tab-inner-extr-main-tab-panel' "
                                                        "and text()='Access Control Engine']")
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_text)
        if return_text == arg_dict['ace_tab']:
            self.builder.error_state = False
        else:
            self.builder.error_state = True
        # ACE Selected or not
        true_or_false = self.builder.get_attribute_from_element(ui_cmd_obj, ".x-tab-bar-body-extr-main-tab-panel div "
                                                                            "[hidefocus='on']:nth-of-type(5)",
                                                                "aria-selected",
                                                                self.builder.constants.STRATEGY_CSS_SELECTOR)
        self.logger.log_info(true_or_false)
        if true_or_false == "true":
            self.builder.error_state = False
        else:
            self.builder.error_state = True
        # Notification TAB
        return_text = self.builder.get_text_from_element(ui_cmd_obj, "//span[@class='x-tab-inner x-tab-inner-extr-"
                                                                     "main-tab-panel' and text()='Notification']")
        self.logger.log_info(return_text)
        if return_text == arg_dict['notification_tab']:
            self.builder.error_state = False
        else:
            self.builder.error_state = True
        # Notification TAB Selected or not
        true_or_false = self.builder.get_attribute_from_element(ui_cmd_obj, ".x-tab-bar-body-extr-main-tab-panel div "
                                                                            "[hidefocus='on']:nth-of-type(6)",
                                                                "aria-selected",
                                                                self.builder.constants.STRATEGY_CSS_SELECTOR)
        self.logger.log_info(true_or_false)
        if true_or_false == "false":
            self.builder.error_state = False
        else:
            self.builder.error_state = True
        # Troubleshooting TAB
        return_text = self.builder.get_text_from_element(ui_cmd_obj, "//span[@class='x-tab-inner x-tab-inner-extr"
                                                                     "-main-tab-panel' and text()='Troubleshooting']")
        self.logger.log_info(return_text)
        if return_text == arg_dict['troubleshooting_tab']:
            self.builder.error_state = False
        else:
            self.builder.error_state = True
        # Troubleshooting TAB Selected or not
        true_or_false = self.builder.get_attribute_from_element(ui_cmd_obj, ".x-tab-bar-body-extr-main-tab-panel "
                                                                            "div [hidefocus='on']"
                                                                            ":nth-of-type(7)", "aria-selected",
                                                                self.builder.constants.STRATEGY_CSS_SELECTOR)
        self.logger.log_info(true_or_false)
        if true_or_false == "false":
            self.builder.error_state = False
        else:
            self.builder.error_state = True

        return ui_cmd_obj

    def gim_ace_page_validation(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//span[text()='Access Control Engine']", self.builder.constants.STRATEGY_XPATH)
        self.builder.click(ui_cmd_obj, "//span[@class='x-tab-inner x-tab-inner-default' and text()='Engine Details']")
        # Engine Details option
        return_text = self.builder.get_text_from_element(ui_cmd_obj, "//span[@class='x-tab-inner x-tab-inner-"
                                                                     "default' and text()='Engine Details']")
        self.logger.log_info(return_text)
        if return_text == arg_dict['engine_tab']:
            self.builder.error_state = False
        else:
            self.builder.error_state = True
        # Engine Details
        true_or_false = self.builder.get_attribute_from_element(ui_cmd_obj, "//div[@class='x-tab-bar-body x-tab-"
                                                                            "bar-body-default  x-box-layout-ct']/"
                                                                            "div/div/a[1]", "aria-selected")
        self.logger.log_info(true_or_false)
        if true_or_false == "true":
            self.builder.error_state = False
        else:
            self.builder.error_state = True
        # Radius Option
        return_text = self.builder.get_text_from_element(ui_cmd_obj, "//span[@class='x-tab-inner x-tab-"
                                                                     "inner-default' and text()='RADIUS']")
        self.logger.log_info(return_text)
        if return_text == arg_dict['radius_tab']:
            self.builder.error_state = False
        else:
            self.builder.error_state = True
        # RADIUS
        true_or_false = self.builder.get_text_from_element(ui_cmd_obj, "//div[@class='x-tab-bar-body x-tab-bar-"
                                                                       "body-default  x-box-layout-ct']/div/div/a[2]")
        self.logger.log_info(true_or_false)
        if true_or_false == "false":
            self.builder.error_state = False
        else:
            self.builder.error_state = True
        # Root Cert
        return_text = self.builder.get_text_from_element(ui_cmd_obj, "//span[@class='x-tab-inner x-tab-inner"
                                                                     "-default' and text()='Root Certificates']")
        self.logger.log_info(return_text)
        if return_text == arg_dict['cert_tab']:
            self.builder.error_state = False
        else:
            self.builder.error_state = True
        # Root Certificates
        true_or_false = self.builder.get_attribute_from_element(ui_cmd_obj, "//div[@class='x-tab-bar-body x-tab-"
                                                                            "bar-body-default  x-box-layout-ct']/"
                                                                            "div/div/a[3]", "aria-selected")
        self.logger.log_info(true_or_false)
        if true_or_false == "false":
            self.builder.error_state = False
        else:
            self.builder.error_state = True
        # License Option
        return_text = self.builder.get_text_from_element(ui_cmd_obj, "//span[@class='x-tab-inner x-tab-inner"
                                                                     "-default' and text()='License']")
        self.logger.log_info(return_text)
        if return_text == arg_dict['lic_tab']:
            self.builder.error_state = False
        else:
            self.builder.error_state = True
        # License
        true_or_false = self.builder.get_attribute_from_element(ui_cmd_obj, "//div[@class='x-tab-bar-body x-tab-"
                                                                            "bar-body-default  x-box-layout-ct']/"
                                                                            "div/div/a[4]", "aria-selected")
        self.logger.log_info(true_or_false)
        if true_or_false == "false":
            self.builder.error_state = False
        else:
            self.builder.error_state = True

        return ui_cmd_obj

    def gim_admin_license_validation(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//span[text()='Access Control Engine']", self.builder.constants.STRATEGY_XPATH)
        self.builder.click(ui_cmd_obj, "//span[@class='x-tab-inner x-tab-inner-default' and text()='License']")
        return_text = self.builder.get_text_from_element(ui_cmd_obj, "//div[@style='font-weight:bold;color:green']")
        self.logger.log_info("return_text: " + return_text)
        if return_text != "Valid":
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def gim_admin_notification_page_validation(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//span[@class='x-tab-inner x-tab-inner-extr-main-tab-panel' "
                                       "and text()='Notification']")
        # Email Option
        return_text = self.builder.get_text_from_element(ui_cmd_obj, "//span[@class='x-tab-inner x-tab-inner-default' "
                                                                     "and text()='E-mail']")
        self.logger.log_info(return_text)
        if return_text == arg_dict['email_tab']:
            self.builder.error_state = False
        else:
            self.builder.error_state = True
        # Notification page-Email TAB
        true_or_false = self.builder.get_attribute_from_element(ui_cmd_obj,
                                                                ".x-tab-bar-body-default div "
                                                                "[hidefocus='on']:nth-of-type(1)",
                                                                "aria-selected",
                                                                self.builder.constants.STRATEGY_CSS_SELECTOR)
        self.logger.log_info(true_or_false)
        if true_or_false == "true":
            self.builder.error_state = False
        else:
            self.builder.error_state = True
        # Notification Option
        return_text = self.builder.get_text_from_element(ui_cmd_obj, "//span[@class='x-tab-inner x-tab-inner-default' "
                                                                     "and text()='SMS']")
        self.logger.log_info(return_text)
        if return_text == arg_dict['sms_tab']:
            self.builder.error_state = False
        else:
            self.builder.error_state = True
        # Notification page-SMS TAB
        true_or_false = self.builder.get_attribute_from_element(ui_cmd_obj,
                                                                ".x-tab-bar-body-default div "
                                                                "[hidefocus='on']:nth-of-type(1)",
                                                                "aria-selected",
                                                                self.builder.constants.STRATEGY_CSS_SELECTOR)
        self.logger.log_info(true_or_false)
        if true_or_false == "false":
            self.builder.error_state = False
        else:
            self.builder.error_state = True

        return ui_cmd_obj

    def spinner_loading(self, ui_cmd_obj):
        self.builder.webdriver_wait_until(ui_cmd_obj, ".x-mask-msg-text", retry=5,
                                          strategy=self.builder.constants.STRATEGY_CSS_SELECTOR,
                                          condition=self.builder.constants.CONDITION_INVISIBILITY_OF_ELEMENT)
        return ui_cmd_obj

    def set_check_box_value(self, ui_cmd_obj, locator, strategy, is_checked):
        is_input_checked = self.builder.get_attribute_from_element(ui_cmd_obj, locator, 'checked', strategy)
        self.logger.logger.info("current check box status: " + str(is_input_checked))
        if (not is_input_checked) and is_checked:
            self.builder.click(ui_cmd_obj, locator, strategy)
        elif is_input_checked and (not is_checked):
            self.builder.click(ui_cmd_obj, locator, strategy)

        return ui_cmd_obj

    def gim_admin_change_visibility(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            return super(Gimadministration, self).gim_admin_change_visibility(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def gim_admin_edit_delete_sms_gateway(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//span[@class='x-btn-inner x-btn-inner-extr-nav-toolbar-button-small' "
                                       "and text()='Administration']")
        self.builder.click(ui_cmd_obj, "//span[@class='x-tab-inner x-tab-inner-extr-main-tab-panel' "
                                       "and text()='Notification']")
        self.builder.click(ui_cmd_obj, "//span[@class='x-tab-inner x-tab-inner-default' and text()='SMS']")
        self.builder.delay(ui_cmd_obj, 5)
        if arg_dict['action'] == "edit":
            self.select_row_from_sms_table(ui_cmd_obj, arg_dict)
            self.builder.click(ui_cmd_obj, "[role] [hidefocus='on']:nth-of-type(2) .x-btn-inner-default-toolbar-small",
                               self.builder.constants.STRATEGY_CSS_SELECTOR)
            self.builder.click(ui_cmd_obj, "//input[@name='phoneCarrierGateways']")
            self.builder.enter_text(ui_cmd_obj, arg_dict['phone_gateway'], "//input[@name='phoneCarrierGateways']")
            self.builder.click(ui_cmd_obj, "//input[@name='phoneNumber']")
            li_number = arg_dict['pn_option']
            self.builder.click(ui_cmd_obj, "//body[@role='application']//ul[@role='listbox']/li[" + li_number + "]",
                               self.builder.constants.STRATEGY_XPATH)
            if li_number == "3":
                self.builder.delay(ui_cmd_obj, 5)
                self.builder.click(ui_cmd_obj, "//input[@name='otherDigitsLength']")
                self.builder.enter_text(ui_cmd_obj, "12", "//input[@name='otherDigitsLength']")
            self.builder.delay(ui_cmd_obj, 5)
            if arg_dict['save'] == "save":
                self.builder.click(ui_cmd_obj, "[role='dialog'] [role='toolbar'] .x-btn-inner-blue-small",
                                   self.builder.constants.STRATEGY_CSS_SELECTOR)
        if arg_dict['action'] == "delete":
            self.select_row_from_sms_table(ui_cmd_obj, arg_dict)
            self.builder.click(ui_cmd_obj, "//a[@data-qtip='Delete selected SMS Gateway(s)/Provider(s)']")
            self.builder.click(ui_cmd_obj, "//span[@class='x-btn-inner x-btn-inner-blue-small' and text()='Yes']")
            self.builder.delay(ui_cmd_obj, 5)

        return ui_cmd_obj

    def gim_admin_sms_gateway_should_not_exist(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//span[@class='x-tab-inner x-tab-inner-extr-main-tab-panel' "
                                       "and text()='Notification']")
        self.builder.click(ui_cmd_obj, "//span[@class='x-tab-inner x-tab-inner-default' and text()='E-mail']")
        self.builder.click(ui_cmd_obj, "//span[@class='x-tab-inner x-tab-inner-default' and text()='SMS']")
        self.wait_for_page_load_completely(ui_cmd_obj)
        all_count = self.builder.find_elements(ui_cmd_obj, "//div[@class ='x-grid-item-container']/table/tbody/"
                                                           "tr/td[3]")
        row_count = len(all_count)
        self.logger.log_info("row_count: " + str(row_count))
        for x in all_count:
            self.logger.log_info("x value: " + str(x.text))
            if str(x.text) == arg_dict['phone_carrier']:
                ui_cmd_obj.error_state = True
                self.logger.log_info(
                    "<" + arg_dict['phone_carrier'] + "> not expected behaviour" + str(x.text))
                break
            else:
                self.logger.log_info("<" + arg_dict['phone_carrier'] + "> expected behaviour::" + str(x.text))
                ui_cmd_obj.error_state = False

        return ui_cmd_obj
