from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as GimonboardingtemplatesBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Gimonboardingtemplates(GimonboardingtemplatesBase):
    def ot_signed_in_user_should_exist(self, ui_cmd_obj, arg_dict):
        self.builder.get_text_from_element_and_compare(ui_cmd_obj, ".loginText", arg_dict["signed_in_user"],
                                                       self.builder.constants.STRATEGY_CSS_SELECTOR)
        self.builder.get_text_from_element_and_compare(ui_cmd_obj, "#basic-statusbar-targetEl [data-ref] .x-tool"
                                                                   "bar-text-default:nth-of-type(1)",
                                                       arg_dict["signed_user_footer_text"],
                                                       self.builder.constants.STRATEGY_CSS_SELECTOR)

        return ui_cmd_obj

    def ot_add(self, ui_cmd_obj, arg_dict):
        if arg_dict['obt_name'] != "None":
            self.builder.click(ui_cmd_obj, "//a[@data-qtip='Add Onboarding Template']")
            self.base_builder.webdriver_wait_until(ui_cmd_obj, "//span[text()='Common']", retry=5)
            self.builder.enter_text(ui_cmd_obj, arg_dict['obt_name'], "OTName", self.builder.constants.STRATEGY_NAME)
            self.builder.enter_text(ui_cmd_obj, "description" + arg_dict['obt_name'], "OTDescription",
                                    self.builder.constants.STRATEGY_NAME)
            self.builder.enter_text(ui_cmd_obj, "notes" + arg_dict['obt_name'], "OTNotes",
                                    self.builder.constants.STRATEGY_NAME)
        none = "None"
        if arg_dict['ot_type'] == "default":
            self.logger.log_info("default")
            self.builder.click(ui_cmd_obj, "//label[text()='Guest User and Device Provisioning']")
        elif arg_dict['ot_type'] == "sponsor":
            self.logger.log_info("sponsor")
            self.builder.click(ui_cmd_obj, "//label[text()='Self Service with Sponsor Approval']")
        elif arg_dict['ot_type'] == "api" and arg_dict['ot_api_chk'] == none:
            self.logger.log_info("api")
            self.builder.click(ui_cmd_obj, "//label[text()='Guest User and Device Provisioning using API']")
        elif arg_dict['ot_type'] == "api" and arg_dict['ot_api_chk'] != none:
            self.logger.log_info("api and chkbox")
            self.builder.click(ui_cmd_obj, "//label[text()='Guest User and Device Provisioning using API']")
            self.builder.click(ui_cmd_obj, ".x-form-type-checkbox.x-vbox-form-item [data-ref='boxLabelEl']",
                               self.builder.constants.STRATEGY_CSS_SELECTOR)
        elif arg_dict['ot_type'] == "outlook":
            self.logger.log_info("outlook")
            self.builder.click(ui_cmd_obj, "//label[text()='Guest User Provisioning using Outlook Add-in']")
        elif arg_dict['ot_type'] == "voucher":
            self.logger.log_info("voucher")
            self.builder.click(ui_cmd_obj, "//label[text()='Guest User Provisioning using Voucher']")
        elif arg_dict['ot_type'] == "csv":
            self.logger.log_info("csv")
            self.builder.click(ui_cmd_obj, "//label[text()='Guest User and Device Provisioning using CSV']")
        elif arg_dict['ot_type'] == "zerotouch":
            self.logger.log_info("zerotouch")
            self.builder.click(ui_cmd_obj, "//label[text()='Zero Touch Guest User Provisioning']")
        else:
            self.logger.log_info("not selected correctly, something went wrong!")
        if arg_dict['ot_global'] != none:
            self.logger.log_info("globalchkbox")
            self.builder.click(ui_cmd_obj, ".x-panel-default:nth-of-type(2) .x-form-type-checkbox.x-anchor-"
                                           "form-item [data-ref='boxLabelEl']",
                               self.builder.constants.STRATEGY_CSS_SELECTOR)
        self.builder.delay(ui_cmd_obj, 5)
        if arg_dict['ot_duration'] != none:
            self.logger.log_info("ot_duration")
            self.builder.enter_text(ui_cmd_obj, arg_dict['ot_duration'], "//input[@name='duration']")
        if arg_dict['ot_time'] == "minutes":
            self.logger.log_info("ot_time minutes")
            self.builder.click(ui_cmd_obj, "//label[text()='minute(s)']")
        elif arg_dict['ot_time'] == "days":
            self.logger.log_info("ot_time days")
            self.builder.click(ui_cmd_obj, "//label[text()='day(s)']")
        else:
            self.logger.log_info("ot_time_hours")
            self.builder.click(ui_cmd_obj, "//label[text()='hour(s)']")
        if arg_dict['ot_save'] == "save":
            self.ot_save(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def ot_should_exist(self, ui_cmd_obj, arg_dict):
        self.builder.delay(ui_cmd_obj, 5)
        all_count = self.builder.find_elements(ui_cmd_obj, "//div[@class ='x-grid-item-container']/table")
        row_count = len(all_count)
        self.logger.log_info("row_count: " + str(row_count))
        for index in range(1, (row_count + 1)):
            web_obj = self.builder.find_element(ui_cmd_obj, "//div[@class ='x-grid-item-container']"
                                                            "/table[" + str(index) + "]/tbody/tr/td[1]")
            return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
            self.logger.log_info("1 .otname: " + str(index) + "::" + return_text)
            if return_text == arg_dict['ot_name']:
                web_obj = self.builder.find_element(ui_cmd_obj, "//div[@class ='x-grid-item-container']"
                                                                "/table[" + str(index) + "]/tbody/tr/td[2]")
                return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
                web_obj1 = self.builder.find_element(ui_cmd_obj, "//div[@class ='x-grid-item-container']"
                                                                 "/table[" + str(index) + "]/tbody/tr/td[3]")
                return_text1 = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj1)
                self.builder.delay(ui_cmd_obj, 2)
                if return_text == arg_dict['ot_type'] and return_text1 == "description" + arg_dict['ot_name']:
                    self.logger.log_info("< 2.1 " + arg_dict['ot_type'] + " > ot_type:" +
                                         str(index) + " equal: " + return_text)
                    self.logger.log_info("< 2.2 " + "description" + arg_dict['ot_name'] + " >" +
                                         str(index) + " equal: " + return_text1)
                    ui_cmd_obj.error_state = False
                    break
                if return_text != arg_dict['ot_type'] or return_text1 != "description" + arg_dict['ot_name']:
                    self.logger.log_info("<3.1 " + arg_dict['ot_type'] + "> ot_type: is not equal to ::" + return_text)
                    self.logger.log_info("<3.2 description " +
                                         arg_dict['ot_name'] + " >: is not equal to ::" + return_text1)
                    ui_cmd_obj.error_state = True
                    break
            elif return_text == '':
                ui_cmd_obj.error_state = True
            else:
                self.logger.log_info("<" + arg_dict['ot_name'] + "> ot_name: is not equal to ::" + return_text)
                ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def ot_verify_admin_signed(self, ui_cmd_obj, arg_dict):
        self.builder.get_text_from_element_and_compare(ui_cmd_obj, ".loginText", arg_dict["signed_in_user"],
                                                       self.builder.constants.STRATEGY_CSS_SELECTOR)
        self.logger.log_info(arg_dict["signed_in_user"])

        return ui_cmd_obj

    def ot_common_tab(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//a[@data-qtip='Add Onboarding Template']")
        self.spinner_loading(ui_cmd_obj)
        self.logger.log_info("default")
        self.ot_tab_validation(ui_cmd_obj, 3)
        self.ot_tab_validation(ui_cmd_obj, 5)
        self.ot_tab_validation(ui_cmd_obj, 7)
        self.ot_tab_validation(ui_cmd_obj, 8)
        self.ot_tab_validation(ui_cmd_obj, 9)
        self.logger.log_info("sponsor")
        self.builder.click(ui_cmd_obj, "//label[text()='Self Service with Sponsor Approval']")
        self.ot_tab_validation(ui_cmd_obj, 3)
        self.ot_tab_validation(ui_cmd_obj, 4)
        self.ot_tab_validation(ui_cmd_obj, 8)
        self.ot_tab_validation(ui_cmd_obj, 9)
        self.logger.log_info("api")
        self.builder.click(ui_cmd_obj, "//label[text()='Guest User and Device Provisioning using API']")
        self.ot_tab_validation(ui_cmd_obj, 3)
        self.ot_tab_validation(ui_cmd_obj, 5)
        self.ot_tab_validation(ui_cmd_obj, 7)
        self.ot_tab_validation(ui_cmd_obj, 8)
        self.ot_tab_validation(ui_cmd_obj, 9)
        self.logger.log_info("api and chkbox")
        self.builder.click(ui_cmd_obj, "//label[text()='Guest User and Device Provisioning using API']")
        self.builder.click(ui_cmd_obj, ".x-form-type-checkbox.x-vbox-form-item [data-ref='boxLabelEl']",
                           self.builder.constants.STRATEGY_CSS_SELECTOR)
        self.ot_tab_validation(ui_cmd_obj, 3)
        self.ot_tab_validation(ui_cmd_obj, 5)
        self.ot_tab_validation(ui_cmd_obj, 7)
        self.ot_tab_validation(ui_cmd_obj, 8)
        self.ot_tab_validation(ui_cmd_obj, 9)
        self.logger.log_info("outlook")
        self.builder.click(ui_cmd_obj, "//label[text()='Guest User Provisioning using Outlook Add-in']")
        self.ot_tab_validation(ui_cmd_obj, 3)
        self.ot_tab_validation(ui_cmd_obj, 8)
        self.ot_tab_validation(ui_cmd_obj, 9)
        self.logger.log_info("back to default")
        self.builder.click(ui_cmd_obj, "//label[text()='Guest User and Device Provisioning']")
        self.ot_cancel(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def ot_guest_users(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//a[@data-qtip='Add Onboarding Template']")
        self.base_builder.webdriver_wait_until(ui_cmd_obj, "//span[text()='Common']", retry=5)
        self.is_element_displayed(ui_cmd_obj, ".x-tab-default-top:nth-of-type(3) [data-ref='btnInnerEl']",
                                  self.builder.constants.STRATEGY_CSS_SELECTOR)
        self.builder.click(ui_cmd_obj, ".x-tab-default-top:nth-of-type(3) [data-ref='btnInnerEl']",
                           self.builder.constants.STRATEGY_CSS_SELECTOR)
        self.is_element_selected(ui_cmd_obj, "//input[@name='userManageRight']", self.builder.constants.STRATEGY_XPATH)
        self.is_element_displayed(ui_cmd_obj, "//fieldset[@aria-label='Guest Notification field set']",
                                  self.builder.constants.STRATEGY_XPATH)
        self.is_element_displayed(ui_cmd_obj, "//fieldset[@aria-label='Username field set']",
                                  self.builder.constants.STRATEGY_XPATH)
        self.is_element_displayed(ui_cmd_obj, "//fieldset[@aria-label='Password field set']",
                                  self.builder.constants.STRATEGY_XPATH)
        self.is_element_displayed(ui_cmd_obj, "//fieldset[@aria-label='Password Complexity Check: field set']",
                                  self.builder.constants.STRATEGY_XPATH)
        self.is_element_displayed(ui_cmd_obj, "//fieldset[@aria-label='Guest User Account Limit field set']",
                                  self.builder.constants.STRATEGY_XPATH)
        self.is_element_displayed(ui_cmd_obj, "//fieldset[@aria-label='Customize Printer Friendly Page field set']",
                                  self.builder.constants.STRATEGY_XPATH)
        self.is_element_displayed(ui_cmd_obj, "//fieldset[@aria-label='Access Groups field set']",
                                  self.builder.constants.STRATEGY_XPATH)
        self.is_element_displayed(ui_cmd_obj, "//fieldset[@aria-label='Accessible To Provisioner field set']",
                                  self.builder.constants.STRATEGY_XPATH)
        self.is_element_displayed(ui_cmd_obj, "//fieldset[@aria-label='Custom Attributes field set']",
                                  self.builder.constants.STRATEGY_XPATH)
        # Guest Notification
        self.is_element_selected(ui_cmd_obj, ".x-fieldset-default:nth-of-type(1) .x-fieldset-default:nth-of-type(1) "
                                             ".x-form-check-group:nth-of-type(1) [autocomplete]",
                                 self.builder.constants.STRATEGY_CSS_SELECTOR)
        self.is_element_selected(ui_cmd_obj, ".x-fieldset-default:nth-of-type(1) .x-fieldset-default:nth-of-type(1) "
                                             ".x-form-check-group:nth-of-type(2) [autocomplete]",
                                 self.builder.constants.STRATEGY_CSS_SELECTOR)
        self.is_element_selected(ui_cmd_obj, ".x-fieldset-default:nth-of-type(1) .x-fieldset-default:nth-of-type(1) "
                                             ".x-form-check-group:nth-of-type(3) [autocomplete]",
                                 self.builder.constants.STRATEGY_CSS_SELECTOR)
        self.is_element_selected(ui_cmd_obj, ".x-fieldset-default:nth-of-type(1) .x-fieldset-default:nth-of-type(1) "
                                             ".x-form-check-group:nth-of-type(4) [autocomplete]",
                                 self.builder.constants.STRATEGY_CSS_SELECTOR)
        # username
        self.is_element_selected(ui_cmd_obj, "//input[@name='autoGenUsernameType' and @checked='checked']",
                                 self.builder.constants.STRATEGY_XPATH)
        # password
        self.is_element_selected(ui_cmd_obj, "//input[@name='autoGenPasswordType' and @checked='checked']",
                                 self.builder.constants.STRATEGY_XPATH)
        # password Complexity check
        self.is_element_selected(ui_cmd_obj, "//td[1]//input[@name='passwordComplexity' and @checked='checked']",
                                 self.builder.constants.STRATEGY_XPATH)
        self.is_element_selected(ui_cmd_obj, "//td[2]//input[@name='passwordComplexity' and @checked='checked']",
                                 self.builder.constants.STRATEGY_XPATH)
        self.is_element_selected(ui_cmd_obj, "//td[3]//input[@name='passwordComplexity' and @checked='checked']",
                                 self.builder.constants.STRATEGY_XPATH)
        self.is_element_selected(ui_cmd_obj, "//td[4]//input[@name='passwordComplexity' and @checked='checked']",
                                 self.builder.constants.STRATEGY_XPATH)
        self.builder.delay(ui_cmd_obj, 5)
        self.ot_cancel(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def ot_notification(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//a[@data-qtip='Add Onboarding Template']")
        self.base_builder.webdriver_wait_until(ui_cmd_obj, "//span[text()='Common']", retry=5)
        self.builder.enter_text(ui_cmd_obj, arg_dict['ot_name'], "//input[@role='textbox']")
        self.is_element_displayed(ui_cmd_obj, ".x-tab-default-top:nth-of-type(8) [data-ref='btnInnerEl']",
                                  self.builder.constants.STRATEGY_CSS_SELECTOR)
        self.builder.click(ui_cmd_obj, ".x-tab-default-top:nth-of-type(8) [data-ref='btnInnerEl']",
                           self.builder.constants.STRATEGY_CSS_SELECTOR)
        self.builder.click(ui_cmd_obj, "//span[@role='presentation']/span[text()='General']")
        # sms template:
        self.is_element_displayed(ui_cmd_obj, "//label[text()='SMS Template:'][1]",
                                  self.builder.constants.STRATEGY_XPATH)
        # sms tem avaialable variable
        self.builder.get_text_from_element_and_compare(ui_cmd_obj, "//label[text()='SMS Template:']/"
                                                                   "following::label[1]",
                                                       arg_dict['sms_temp_avilable_var'],
                                                       self.builder.constants.STRATEGY_XPATH)
        # sms tem avaialable variable names
        self.builder.get_text_from_element_and_compare(ui_cmd_obj, "//label[text()='SMS Template:']/following::"
                                                                   "label[2]", arg_dict['sms_temp_avilable_var_names'])
        # message header:
        self.builder.get_text_from_element_and_compare(ui_cmd_obj, "//label[text()='SMS characters'][1]/preceding::"
                                                                   "label[4]", arg_dict['sms_message_text'])
        # message text area:
        self.builder.get_text_from_element_and_compare(ui_cmd_obj, "//textarea[@name='SMSTemplateMessage']",
                                                       arg_dict['sms_message_text_area'])
        # sms textArea:
        self.is_element_displayed(ui_cmd_obj, "//input[@name='SMSChars' and @value='80']",
                                  self.builder.constants.STRATEGY_XPATH)
        # Email TEmplate Text:
        self.is_element_displayed(ui_cmd_obj, "//label[text()='Email Template:'][1]",
                                  self.builder.constants.STRATEGY_XPATH)
        # Email TEmplate Available Variable:
        self.builder.get_text_from_element_and_compare(ui_cmd_obj, "//label[text()='Email Template:'][1]/following::"
                                                                   "label[1]", arg_dict['email_available_var'])
        # Email TEmplate Available Variable names:
        self.builder.get_text_from_element_and_compare(ui_cmd_obj, "//label[text()='Email Template:'][1]/following::"
                                                                   "label[2]", arg_dict['email_available_var_names'])
        # email subject text
        self.builder.get_text_from_element_and_compare(ui_cmd_obj, "//label[text()='Email Template:'][1]/following::"
                                                                   "label[4]", arg_dict['email_subject_text'])
        # email template subject area
        self.is_element_displayed(ui_cmd_obj, "//input[@name='emailTemplateSubject' and @value='Guest User Account']",
                                  self.builder.constants.STRATEGY_XPATH)
        # email template message text area
        self.builder.get_text_from_element_and_compare(ui_cmd_obj, "//textarea[@name='emailTemplateMessage']",
                                                       arg_dict['email_message_text'])
        # terms
        self.builder.get_text_from_element_and_compare(ui_cmd_obj, "//textarea[text()='Welcome to Extreme Networks']"
                                                                   "[1]/preceding::label[2]", arg_dict['tems_text'])
        self.builder.get_text_from_element_and_compare(ui_cmd_obj, "//textarea[text()='Welcome to Extreme Networks']",
                                                       arg_dict['tems_text_area'])
        # enter terms area
        self.builder.enter_text(ui_cmd_obj, arg_dict['term_of_use'], "//textarea[text()='Welcome "
                                                                     "to Extreme Networks']",
                                self.builder.constants.STRATEGY_XPATH)
        self.ot_save(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def ot_summary_common(self, ui_cmd_obj, arg_dict):
        self.builder.get_text_from_element_and_compare(ui_cmd_obj, "//fieldset[1]//span[text()=" + "'" +
                                                       arg_dict['summary_key'] + "'" + "][1]/following::div[2]",
                                                       arg_dict['summary_value'])

        return ui_cmd_obj

    def ot_summary_guest_users(self, ui_cmd_obj, arg_dict):
        self.builder.get_text_from_element_and_compare(ui_cmd_obj, "//fieldset[2]//span[text()=" + "'" +
                                                       arg_dict['summary_key'] + "'" + "][1]/following::div[2]",
                                                       arg_dict['summary_value'].strip())

        return ui_cmd_obj

    def ot_summary_sponsor(self, ui_cmd_obj, arg_dict):
        self.builder.get_text_from_element_and_compare(ui_cmd_obj, "//fieldset[3]//span[text()=" + "'" +
                                                       arg_dict['summary_key'] + "'" + "][1]/following::div[2]",
                                                       arg_dict['summary_value'])

        return ui_cmd_obj

    def ot_summary_iot_user_devices(self, ui_cmd_obj, arg_dict):
        self.builder.get_text_from_element_and_compare(ui_cmd_obj, "//fieldset[4]//span[text()=" + "'" +
                                                       arg_dict['summary_key'] + "'" + "][1]/following::div[2]",
                                                       arg_dict['summary_value'])

        return ui_cmd_obj

    def ot_summary_mobile_app(self, ui_cmd_obj, arg_dict):
        self.builder.get_text_from_element_and_compare(ui_cmd_obj, "//fieldset[5]//span[text()=" + "'" +
                                                       arg_dict['summary_key'] + "'" + "][1]/following::div[2]",
                                                       arg_dict['summary_value'])

        return ui_cmd_obj

    def ot_summary_device_family(self, ui_cmd_obj, arg_dict):
        self.builder.get_text_from_element_and_compare(ui_cmd_obj, "//fieldset[6]//span[text()=" + "'" +
                                                       arg_dict['summary_key'] + "'" + "][1]/following::div[2]",
                                                       arg_dict['summary_value'])

        return ui_cmd_obj

    def ot_summary_notification(self, ui_cmd_obj, arg_dict):
        self.builder.get_text_from_element_and_compare(ui_cmd_obj, "//fieldset[7]//span[text()=" + "'" +
                                                       arg_dict['summary_key'] + "'" + "][1]/following::div[2]",
                                                       arg_dict['summary_value'])

        return ui_cmd_obj

    def ot_summary_advanced(self, ui_cmd_obj, arg_dict):
        self.builder.get_text_from_element_and_compare(ui_cmd_obj, "//fieldset[8]//span[text()=" + "'" +
                                                       arg_dict['summary_key'] + "'" + "][1]/following::div[2]",
                                                       arg_dict['summary_value'])

        return ui_cmd_obj

    def ot_select_ot_edit(self, ui_cmd_obj, arg_dict):
        self.select_row_from_ot_table(ui_cmd_obj, arg_dict)
        self.builder.click(ui_cmd_obj, "//a[@data-qtip='Edit Onboarding Template']")
        self.base_builder.webdriver_wait_until(ui_cmd_obj, "//span[text()='Summary']", retry=5)

        return ui_cmd_obj

    def ot_cancel(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//div[@class='x-panel x-tabpanel-child x-panel-default']/div/"
                                       "div/div/div/a[@data-qtip='Save Onboarding Template']/following::a[1]")
        self.spinner_loading(ui_cmd_obj)

        return ui_cmd_obj

    def ot_save(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//div[@class='x-panel x-tabpanel-child x-panel-default']/div/"
                                       "div/div/div/a[@data-qtip='Save Onboarding Template']")
        self.spinner_loading(ui_cmd_obj)
        self.is_ldap_pop_up_exists(ui_cmd_obj)

        return ui_cmd_obj

    def ot_select_ot_copy(self, ui_cmd_obj, arg_dict):
        self.wait_for_page_load_completely(ui_cmd_obj)
        self.select_row_from_ot_table(ui_cmd_obj, arg_dict)
        self.builder.click(ui_cmd_obj, "//a[@data-qtip='Copy Onboarding Template']")
        self.spinner_loading(ui_cmd_obj)
        self.builder.click(ui_cmd_obj, "//input[@name='OTName']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['ot_copy_name'], "//input[@name='OTName']")
        self.builder.enter_text(ui_cmd_obj, "description" + arg_dict['ot_copy_name'], "OTDescription",
                                self.builder.constants.STRATEGY_NAME)
        self.builder.enter_text(ui_cmd_obj, "notes" + arg_dict['ot_copy_name'], "OTNotes",
                                self.builder.constants.STRATEGY_NAME)
        self.ot_save(ui_cmd_obj, arg_dict)
        self.builder.delay(ui_cmd_obj, 5)
        self.builder.click(ui_cmd_obj, "//span[@role='presentation']/span[text()='Refresh']")

        return ui_cmd_obj

    def ot_select_ot_delete(self, ui_cmd_obj, arg_dict):
        self.wait_for_page_load_completely(ui_cmd_obj)
        web_obj = self.builder.find_element(ui_cmd_obj, "Delete", self.builder.constants.STRATEGY_LINK_TEXT)
        return_text = self.base_builder.get_attribute_from_element(ui_cmd_obj, web_obj, "aria-disabled")
        self.logger.log_info("return_text1::" + str(return_text))
        if return_text != "true":
            self.builder.click(ui_cmd_obj, "//span[text()='Delete']")
            self.spinner_loading(ui_cmd_obj)
            self.builder.delay(ui_cmd_obj, 5)
            if arg_dict['ot_delete'] == "1":
                self.builder.click(ui_cmd_obj, "//div[1]/a[@role='menuitem']/span[@role='presentation']")
                self.builder.delay(ui_cmd_obj, 1000)
                self.builder.click(ui_cmd_obj, "//span[@role='presentation']/span[text()='Yes']")
                self.spinner_loading(ui_cmd_obj)
            if arg_dict['ot_delete'] == "2":
                self.builder.click(ui_cmd_obj, "//div[2]/a[@role='menuitem']/span[@role='presentation']")
                self.builder.delay(ui_cmd_obj, 1000)
                self.builder.click(ui_cmd_obj, "//label[text()='Internal Provisioner(s) & "
                                               "Self-Service Provisioner(s)']")
                self.builder.click(ui_cmd_obj, "//label[text()='Guest User(s)']")
                self.builder.click(ui_cmd_obj, "//label[text()='Device(s)']")
                self.builder.delay(ui_cmd_obj, 1000)
                self.builder.click(ui_cmd_obj, "//a[@class='x-btn x-unselectable x-box-item"
                                               " x-toolbar-item x-btn-blue-small']")
                self.wait_for_ot_deletion(ui_cmd_obj)
            if arg_dict['ot_delete'] == "3":
                self.builder.click(ui_cmd_obj, "//div[3]/a[@role='menuitem']/span[@role='presentation']")
                self.builder.delay(ui_cmd_obj, 1000)
                self.builder.click(ui_cmd_obj, "//span[@role='presentation']/span[text()='Yes']")
            self.spinner_loading(ui_cmd_obj)
        else:
            self.logger.log_info("no rows to select, no need to click on delete button")

        return ui_cmd_obj

    def ot_click_nav_bar(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//span[@class='x-btn-inner x-btn-inner-extr-nav-toolbar-button-small' and "
                                       "text()='Onboarding Templates']")
        self.spinner_loading(ui_cmd_obj)
        self.builder.click(ui_cmd_obj, "//span[@class='x-tab-inner x-tab-inner-extr-main-tab-panel' and "
                                       "text()='Onboarding Templates']")
        self.spinner_loading(ui_cmd_obj)

        return ui_cmd_obj

    def ot_default_validation(self, ui_cmd_obj, arg_dict):
        self.is_element_displayed(ui_cmd_obj, "//a[@data-qtip='Add Onboarding Template' and @aria-disabled='false']",
                                  self.builder.constants.STRATEGY_XPATH)
        self.is_element_displayed(ui_cmd_obj, "//a[@data-qtip='Edit Onboarding Template' and @aria-disabled='true']",
                                  self.builder.constants.STRATEGY_XPATH)
        self.is_element_displayed(ui_cmd_obj, "//a[@data-qtip='Copy Onboarding Template' and @aria-disabled='true']",
                                  self.builder.constants.STRATEGY_XPATH)
        self.is_element_displayed(ui_cmd_obj, "//a[@data-qtip='Delete Onboarding Template(s)' and "
                                              "@aria-disabled='true']",
                                  self.builder.constants.STRATEGY_XPATH)
        self.is_element_displayed(ui_cmd_obj,
                                  "//a[@data-qtip='Delete Onboarding Template(s)' and @aria-disabled='true']",
                                  self.builder.constants.STRATEGY_XPATH)
        self.is_element_displayed(ui_cmd_obj,
                                  "//a[@data-qtip='Refresh Onboarding Template(s) List' and @aria-disabled='false']",
                                  self.builder.constants.STRATEGY_XPATH)
        self.is_element_displayed(ui_cmd_obj,
                                  "//div[@role='row']//span[text()='Name']", self.builder.constants.STRATEGY_XPATH)
        self.is_element_displayed(ui_cmd_obj, "//div[@role='row']//span[text()='Template Type']",
                                  self.builder.constants.STRATEGY_XPATH)
        self.select_row_from_ot_table(ui_cmd_obj, arg_dict)
        self.is_element_displayed(ui_cmd_obj, "//a[@data-qtip='Edit Onboarding Template' and @aria-disabled='false']",
                                  self.builder.constants.STRATEGY_XPATH)
        self.is_element_displayed(ui_cmd_obj, "//a[@data-qtip='Copy Onboarding Template' and @aria-disabled='false']",
                                  self.builder.constants.STRATEGY_XPATH)
        self.is_element_displayed(ui_cmd_obj,
                                  "//a[@data-qtip='Delete Onboarding Template(s)' and @aria-disabled='false']",
                                  self.builder.constants.STRATEGY_XPATH)

        return ui_cmd_obj

    def ot_edit_common(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//span[text()='Common']")
        self.spinner_loading(ui_cmd_obj)
        self.is_element_displayed(ui_cmd_obj, "//input[@name='OTName' and @aria-readonly='true']",
                                  self.builder.constants.STRATEGY_XPATH)
        none = "None"
        if arg_dict['ot_edit_duration'] != none:
            self.logger.log_info("ot_edit_duration")
            self.builder.enter_text(ui_cmd_obj, arg_dict['ot_edit_duration'], "//input[@name='duration']")
        if arg_dict['ot_edit_time'] == "minutes":
            self.logger.log_info("ot_edit_time minutes")
            self.builder.click(ui_cmd_obj, "//label[text()='minute(s)']")
        elif arg_dict['ot_edit_time'] == "days":
            self.logger.log_info("ot_edit_time days")
            self.builder.click(ui_cmd_obj, "//label[text()='day(s)']")
        else:
            self.logger.log_info("ot_edit_time_hours")
            self.builder.click(ui_cmd_obj, "//label[text()='hour(s)']")
        if arg_dict['ot_save'] == "save":
            self.ot_save(ui_cmd_obj, arg_dict)
            self.builder.delay(ui_cmd_obj, 5)
            self.builder.click(ui_cmd_obj, "//span[@role='presentation']/span[text()='Refresh']")

        return ui_cmd_obj

    def ot_edit_guest_users(self, ui_cmd_obj, arg_dict):
        self.wait_for_page_load_completely(ui_cmd_obj)
        self.builder.click(ui_cmd_obj, "//a[3]/span[@role='presentation']/span[@role='presentation']"
                                       "/span[text()='Guest Users']")
        self.spinner_loading(ui_cmd_obj)
        web_obj = self.builder.find_element(ui_cmd_obj, ".x-fieldset-default:nth-of-type(1) "
                                                        ".x-fieldset-default:nth-of-type(1) "
                                                        ".x-form-check-group:nth-of-type(1) [autocomplete]",
                                            self.builder.constants.STRATEGY_CSS_SELECTOR)
        result = self.base_builder.is_element_selected(ui_cmd_obj, web_obj)
        self.logger.log_info(result)
        if result:
            self.builder.click(ui_cmd_obj, ".x-fieldset-default:nth-of-type(1) .x-fieldset-default:nth-of-type(1)"
                                           " .x-form-check-group:nth-of-type(1) [autocomplete]",
                               self.builder.constants.STRATEGY_CSS_SELECTOR)
            self.logger.log_info("Selected email successfully")
        web_obj = self.builder.find_element(ui_cmd_obj, ".x-fieldset-default:nth-of-type(1) "
                                                        ".x-fieldset-default:nth-of-type(1) "
                                                        ".x-form-check-group:nth-of-type(2) [autocomplete]",
                                            self.builder.constants.STRATEGY_CSS_SELECTOR)
        result = self.base_builder.is_element_selected(ui_cmd_obj, web_obj)
        self.logger.log_info(result)
        if result:
            self.builder.click(ui_cmd_obj, ".x-fieldset-default:nth-of-type(1) .x-fieldset-default:nth-of-type(1) "
                                           ".x-form-check-group:nth-of-type(2) [autocomplete]",
                               self.builder.constants.STRATEGY_CSS_SELECTOR)
            self.logger.log_info("Selected sms successfully")
        if arg_dict['ot_gu_rights'] == "uncheck":
            self.builder.click(ui_cmd_obj, "//input[@name='userManageRight']")
            self.builder.click(ui_cmd_obj, "//span[@role='presentation']/span[text()='OK']")
        if arg_dict['ot_save'] == "save":
            self.ot_save(ui_cmd_obj, arg_dict)
            self.builder.click(ui_cmd_obj, "//span[@role='presentation']/span[text()='Refresh']")

        return ui_cmd_obj

    def ot_edit_devices(self, ui_cmd_obj, arg_dict):
        self.wait_for_page_load_completely(ui_cmd_obj)
        self.builder.click(ui_cmd_obj, "//a[5]/span[@role='presentation']/span[@role='presentation']/"
                                       "span[text()='Devices']")
        self.spinner_loading(ui_cmd_obj)
        self.builder.click(ui_cmd_obj, "//input[@name='deviceManageRight']")
        self.builder.click(ui_cmd_obj, "//span[@role='presentation']/span[text()='OK']")
        self.builder.click(ui_cmd_obj, ".x-panel-default:nth-of-type(5) .x-btn-blue-small [data-ref='btnInnerEl']",
                           self.builder.constants.STRATEGY_CSS_SELECTOR)
        self.builder.delay(ui_cmd_obj, 5)
        self.is_ldap_pop_up_exists(ui_cmd_obj)
        self.builder.click(ui_cmd_obj, "//span[@role='presentation']/span[text()='Refresh']")

        return ui_cmd_obj

    def ot_add_sponsor(self, ui_cmd_obj, arg_dict):
        self.wait_for_page_load_completely(ui_cmd_obj)
        self.builder.click(ui_cmd_obj, "//span[text()='Sponsor']")
        self.spinner_loading(ui_cmd_obj)
        self.builder.delay(ui_cmd_obj, 5)
        self.builder.click(ui_cmd_obj, "//input[@type='checkbox' and @name='sponsorApproval']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['ot_spon_domain'], "//input[@name='sponsorEmailDomain']")
        self.builder.click(ui_cmd_obj, ".x-form-item-no-label:nth-of-type(1) >"
                                       " [data-ref] > [data-ref] > [data-ref] > [data-ref] > "
                                       ".x-form-item-no-label:nth-of-type(2) .x-btn-default-small",
                           self.builder.constants.STRATEGY_CSS_SELECTOR)
        self.builder.click(ui_cmd_obj, ".x-panel-default:nth-of-type(4) .x-btn-blue-small",
                           self.builder.constants.STRATEGY_CSS_SELECTOR)
        self.is_ldap_pop_up_exists(ui_cmd_obj)
        self.builder.click(ui_cmd_obj, "//span[@role='presentation']/span[text()='Refresh']")

        return ui_cmd_obj

    def ot_select_otname_row_table(self, ui_cmd_obj, arg_dict):
        self.wait_for_page_load_completely(ui_cmd_obj)
        all_count = self.builder.find_elements(ui_cmd_obj, "//div[@class ='x-grid-item-container']/table")
        row_count = len(all_count)
        self.logger.log_info("row_count: " + str(row_count))
        for index in range(1, (row_count + 1)):
            web_obj = self.builder.find_element(ui_cmd_obj, "//div[@class ='x-grid-item-container']/"
                                                            "table[" + str(index) + "]/tbody/tr/td[1]")
            return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
            self.logger.log_info("ot_name: " + str(index) + "::" + return_text)
            if return_text == arg_dict['ot_name']:
                self.builder.click(ui_cmd_obj, "//div[@class ='x-grid-item-container']/"
                                               "table[" + str(index) + "]/tbody/tr/td[1]")
                ui_cmd_obj.error_state = False
                break
            else:
                ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def ot_expected_exist_table(self, ui_cmd_obj, arg_dict):
        self.wait_for_page_load_completely(ui_cmd_obj)
        all_count = self.builder.find_elements(ui_cmd_obj, "//div[@class ='x-grid-item-container']/table")
        row_count = len(all_count)
        self.logger.log_info("row_count: " + str(row_count))
        for index in range(1, (row_count + 1)):
            web_obj = self.builder.find_element(ui_cmd_obj, "//div[@class ='x-grid-item-container']/"
                                                            "table[" + str(index) + "]/tbody/tr/td[1]")
            return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
            self.logger.log_info("ui_cmd_obj.info_return: " + str(index) + "::" + return_text)
            if return_text == arg_dict['ot_name']:
                ui_cmd_obj.error_state = True
                break
            else:
                ui_cmd_obj.error_state = False
                break

        return ui_cmd_obj

    def ot_gu_notification(self, ui_cmd_obj, arg_dict):
        self.wait_for_page_load_completely(ui_cmd_obj)
        self.builder.click(ui_cmd_obj, "//a[3]/span[@role='presentation']/span[@role='presentation']"
                                       "/span[text()='Guest Users']")
        self.spinner_loading(ui_cmd_obj)
        if arg_dict['ot_gu_notif'] == "email":
            self.ot_gu_selection(ui_cmd_obj, arg_dict)
        elif arg_dict['ot_gu_notif'] == "sms":
            self.logger.log_info("sms")
            self.ot_gu_selection(ui_cmd_obj, arg_dict)
        elif arg_dict['ot_gu_notif'] == "username":
            self.logger.log_info("display username")
            self.ot_gu_selection(ui_cmd_obj, arg_dict)
        elif arg_dict['ot_gu_notif'] == "password":
            self.logger.log_info("display password")
            self.ot_gu_selection(ui_cmd_obj, arg_dict)
        else:
            self.logger.log_info("not selected correctly, something wrong")

        self.builder.delay(ui_cmd_obj, 2)

        return ui_cmd_obj

    def ot_gu_username(self, ui_cmd_obj, arg_dict):
        self.wait_for_page_load_completely(ui_cmd_obj)
        self.builder.click(ui_cmd_obj, "//a[3]/span[@role='presentation']/span[@role='presentation']/span[text()="
                                       "'Guest Users']")
        self.spinner_loading(ui_cmd_obj)
        if arg_dict['username_type'] == "guest_defined":
            self.builder.click(ui_cmd_obj, "//label[text()='Guest Defines Username']/..//input[@name='autoGenUsername"
                                           "Type']", self.builder.constants.STRATEGY_XPATH)
        elif arg_dict['username_type'] == "generate_username":
            self.builder.click(ui_cmd_obj, "//label[text()='Generate Username with:']/..//input[@name='autoGenUsername"
                                           "Type']", self.builder.constants.STRATEGY_XPATH)
        elif arg_dict['username_type'] == "email":
            self.builder.click(ui_cmd_obj, "//label[text()='Use Email as Username']/..//input[@name='autoGenUsername"
                                           "Type']", self.builder.constants.STRATEGY_XPATH)
        elif arg_dict['username_type'] == "mobile":
            self.builder.click(ui_cmd_obj, "//label[text()='Use Mobile Phone as Username']/..//input[@name='autoGen"
                                           "UsernameType']", self.builder.constants.STRATEGY_XPATH)

        return ui_cmd_obj

    def ot_gu_random_un(self, ui_cmd_obj, arg_dict):
        self.wait_for_page_load_completely(ui_cmd_obj)
        self.builder.click(ui_cmd_obj, "//label[text()='Generate Username with:']/..//input[@name='autoGenUsername"
                                       "Type']", self.builder.constants.STRATEGY_XPATH)
        self.builder.click(ui_cmd_obj, "//label[text()='Random Generated Username']/..//input"
                                       "[@name='genUsernameType']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['un_length'], "//input[@name='randomUsernameChars']",
                                self.builder.constants.STRATEGY_XPATH)
        if arg_dict['random_un_type_lower'] == "lower":
            web_obj_lc = self.builder.find_element(ui_cmd_obj, "//label[text()='lower case']/..//input[@name='random"
                                                               "UsernameComplexity']",
                                                   self.builder.constants.STRATEGY_XPATH)
            true_or_false_lc = self.base_builder.get_attribute_from_element(ui_cmd_obj, web_obj_lc, "checked")
            if not true_or_false_lc:
                self.set_check_box_value(ui_cmd_obj, "//label[text()='lower case']/..//input[@name='randomUsername"
                                                     "Complexity']",
                                         self.builder.constants.STRATEGY_XPATH, True)
        else:
            web_obj_lc = self.builder.find_element(ui_cmd_obj, "//label[text()='lower case']/..//input[@name='random"
                                                               "UsernameComplexity']",
                                                   self.builder.constants.STRATEGY_XPATH)
            true_or_false_lc = self.base_builder.get_attribute_from_element(ui_cmd_obj, web_obj_lc, "checked")
            if true_or_false_lc:
                self.set_check_box_value(ui_cmd_obj,
                                         "//label[text()='lower case']/..//input[@name='randomUsernameComplexity']",
                                         self.builder.constants.STRATEGY_XPATH, False)
        if arg_dict['random_un_type_upper'] == "upper":
            web_obj_uc = self.builder.find_element(ui_cmd_obj, "//label[text()='upper case']/..//input[@name='random"
                                                               "UsernameComplexity']",
                                                   self.builder.constants.STRATEGY_XPATH)
            true_or_false_uc = self.base_builder.get_attribute_from_element(ui_cmd_obj, web_obj_uc, "checked")
            if not true_or_false_uc:
                self.set_check_box_value(ui_cmd_obj,
                                         "//label[text()='upper case']/..//input[@name='randomUsernameComplexity']",
                                         self.builder.constants.STRATEGY_XPATH, True)
        else:
            web_obj_uc = self.builder.find_element(ui_cmd_obj, "//label[text()='upper case']/..//input[@name='random"
                                                               "UsernameComplexity']",
                                                   self.builder.constants.STRATEGY_XPATH)
            true_or_false_uc = self.base_builder.get_attribute_from_element(ui_cmd_obj, web_obj_uc, "checked")
            if true_or_false_uc:
                self.set_check_box_value(ui_cmd_obj,
                                         "//label[text()='upper case']/..//input[@name='randomUsernameComplexity']",
                                         self.builder.constants.STRATEGY_XPATH, False)
        if arg_dict['random_un_type_number'] == "number":
            web_obj_nu = self.builder.find_element(ui_cmd_obj, "//label[text()='number']/..//input[@name='random"
                                                               "UsernameComplexity']",
                                                   self.builder.constants.STRATEGY_XPATH)
            true_or_false_nu = self.base_builder.get_attribute_from_element(ui_cmd_obj, web_obj_nu, "checked")
            if not true_or_false_nu:
                self.set_check_box_value(ui_cmd_obj,
                                         "//label[text()='number']/..//input[@name='randomUsernameComplexity']",
                                         self.builder.constants.STRATEGY_XPATH, True)
        else:
            web_obj_nu = self.builder.find_element(ui_cmd_obj,
                                                   "//label[text()='number']/..//input[@name='"
                                                   "randomUsernameComplexity']",
                                                   self.builder.constants.STRATEGY_XPATH)
            true_or_false_nu = self.base_builder.get_attribute_from_element(ui_cmd_obj, web_obj_nu, "checked")
            if true_or_false_nu:
                self.set_check_box_value(ui_cmd_obj,
                                         "//label[text()='number']/..//input[@name='randomUsernameComplexity']",
                                         self.builder.constants.STRATEGY_XPATH, False)
        if arg_dict['error_or_noerror'] == "error":
            web_obj = self.builder.find_element(ui_cmd_obj, "//input[@name='randomUsernameChars']")
            return_text = self.base_builder.get_attribute_from_element(ui_cmd_obj, web_obj, "value")
            if return_text < '3' or return_text > '40':
                ui_cmd_obj.error_state = False
            else:
                ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def ot_gu_first_lastname(self, ui_cmd_obj, arg_dict):
        self.wait_for_page_load_completely(ui_cmd_obj)
        self.builder.click(ui_cmd_obj, "//label[contains(text(),'FirstnameLastname')]/..//input[@name='genUsername"
                                       "Type']", self.builder.constants.STRATEGY_XPATH)
        if arg_dict['un_type'] == "no_pre_suf":
            self.builder.click(ui_cmd_obj, "//label[contains(text(),'No Prefix Suffix')]/..//input[@name='prefix"
                                           "SuffixRadioGroup_FirstLast']", self.builder.constants.STRATEGY_XPATH)
        elif arg_dict['un_type'] == "prefix":
            self.builder.click(ui_cmd_obj, "//label[contains(text(),'Add Prefix')]/..//input[@name='prefixSuffix"
                                           "RadioGroup_FirstLast']", self.builder.constants.STRATEGY_XPATH)
            if arg_dict['rand_or_static'] == "random":
                self.builder.click(ui_cmd_obj, "//label[text()='Random Numbers']/..//input[@name='prefixSuffix"
                                               "Type_FirstLast']", self.builder.constants.STRATEGY_XPATH)
                self.builder.enter_text(ui_cmd_obj, arg_dict['number'], "//input[@name='prefixSuffixType_"
                                                                        "FirstLastRandomValue']")
            elif arg_dict['rand_or_static'] == "static":
                self.builder.click(ui_cmd_obj, "//label[text()='Static:']/..//input[@name='prefixSuffixType_"
                                               "FirstLast']", self.builder.constants.STRATEGY_XPATH)
                self.builder.enter_text(ui_cmd_obj, arg_dict['static'], "//input[@name='prefixSuffixType_"
                                                                        "FirstLastStaticValue']")
        elif arg_dict['un_type'] == "suffix":
            self.builder.click(ui_cmd_obj, "//label[contains(text(),'Add Suffix')]/..//input[@name='prefixSuffix"
                                           "RadioGroup_FirstLast']", self.builder.constants.STRATEGY_XPATH)
            if arg_dict['rand_or_static'] == "random":
                self.builder.click(ui_cmd_obj, "//label[text()='Random Numbers']/..//input[@name='prefixSuffix"
                                               "Type_FirstLast']", self.builder.constants.STRATEGY_XPATH)
                self.builder.enter_text(ui_cmd_obj, arg_dict['number'], "//input[@name='prefixSuffixType_"
                                                                        "FirstLastRandomValue']")
            elif arg_dict['rand_or_static'] == "static":
                self.builder.click(ui_cmd_obj, "//label[text()='Static:']/..//input[@name='prefixSuffixType_"
                                               "FirstLast']", self.builder.constants.STRATEGY_XPATH)
                self.builder.enter_text(ui_cmd_obj, arg_dict['static'], "//input[@name='prefixSuffixType_"
                                                                        "FirstLastStaticValue']")

        return ui_cmd_obj

    def ot_gu_finitial_lastname(self, ui_cmd_obj, arg_dict):
        self.wait_for_page_load_completely(ui_cmd_obj)
        self.builder.click(ui_cmd_obj, "//label[contains(text(),'firstinitiallastname')]/..//input[@name='genUsername"
                                       "Type']", self.builder.constants.STRATEGY_XPATH)
        if arg_dict['un_type'] == "no_pre_suf":
            self.builder.click(ui_cmd_obj, "//label[contains(text(),'No Prefix Suffix')]/..//input[@name='prefix"
                                           "SuffixRadioGroup_firstinitial']", self.builder.constants.STRATEGY_XPATH)
            self.builder.delay(ui_cmd_obj, 2)
        elif arg_dict['un_type'] == "prefix":
            self.builder.click(ui_cmd_obj, "//label[contains(text(),'Add Prefix')]/..//input[@name='prefixSuffix"
                                           "RadioGroup_firstinitial']", self.builder.constants.STRATEGY_XPATH)
            if arg_dict['rand_or_static'] == "random":
                self.builder.click(ui_cmd_obj, "//label[text()='Random Numbers']/..//input[@name='prefixSuffix"
                                               "Type_firstinitial']", self.builder.constants.STRATEGY_XPATH)
                self.builder.enter_text(ui_cmd_obj, arg_dict['number'], "//input[@name='prefixSuffixType_"
                                                                        "firstinitialRandomValue']")
            elif arg_dict['rand_or_static'] == "static":
                self.builder.click(ui_cmd_obj, "//label[text()='Static:']/..//input[@name='prefixSuffixType_"
                                               "firstinitial']", self.builder.constants.STRATEGY_XPATH)
                self.builder.enter_text(ui_cmd_obj, arg_dict['static'], "//input[@name='prefixSuffixType_"
                                                                        "firstinitialStaticValue']")
        elif arg_dict['un_type'] == "suffix":
            self.builder.click(ui_cmd_obj, "//label[contains(text(),'Add Suffix')]/..//input[@name='prefixSuffix"
                                           "RadioGroup_firstinitial']", self.builder.constants.STRATEGY_XPATH)
            if arg_dict['rand_or_static'] == "random":
                self.builder.click(ui_cmd_obj, "//label[text()='Random Numbers']/..//input[@name='prefixSuffix"
                                               "Type_firstinitial']", self.builder.constants.STRATEGY_XPATH)
                self.builder.enter_text(ui_cmd_obj, arg_dict['number'], "//input[@name='prefixSuffixType_"
                                                                        "firstinitialRandomValue']")
            elif arg_dict['rand_or_static'] == "static":
                self.builder.click(ui_cmd_obj, "//label[text()='Static:']/..//input[@name='prefixSuffixType_"
                                               "firstinitial']", self.builder.constants.STRATEGY_XPATH)
                self.builder.enter_text(ui_cmd_obj, arg_dict['static'], "//input[@name='prefixSuffixType_"
                                                                        "firstinitialStaticValue']")

        return ui_cmd_obj

    def ot_gu_password(self, ui_cmd_obj, arg_dict):
        self.wait_for_page_load_completely(ui_cmd_obj)
        if arg_dict['pwd_type'] == "guest_defined":
            self.builder.click(ui_cmd_obj,
                               "//label[text()='Guest Defines Password']/..//input[@name='autoGenPasswordType']",
                               self.builder.constants.STRATEGY_XPATH)
            if arg_dict['confirm_pwd'] == "confirm_pwd":
                self.set_check_box_value(ui_cmd_obj, "//input[@name='confirmPassword']",
                                         self.builder.constants.STRATEGY_XPATH, True)
        elif arg_dict['pwd_type'] == "random":
            self.builder.click(ui_cmd_obj,
                               "//label[text()='Random Generated Password']/..//input[@name='autoGenPasswordType']",
                               self.builder.constants.STRATEGY_XPATH)
        elif arg_dict['pwd_type'] == "username":
            self.builder.click(ui_cmd_obj,
                               "//label[text()='Use Username as Password']/..//input[@name='autoGenPasswordType']",
                               self.builder.constants.STRATEGY_XPATH)
        elif arg_dict['pwd_type'] == "static":
            self.builder.click(ui_cmd_obj,
                               "//label[contains(text(),'Static Password:')]/..//input[@name='autoGenPasswordType']",
                               self.builder.constants.STRATEGY_XPATH)
            self.builder.enter_text(ui_cmd_obj, "Ext@123", "//input[@name='staticPasswordValue']")

        return ui_cmd_obj

    def click_on_ot_add_gu_tab(self, ui_cmd_obj):
        self.builder.click(ui_cmd_obj, "//a[3]/span[@role='presentation']/span[@role='presentation']"
                                       "/span[text()='Guest Users']")
        self.logger.log_info("clicked on guest users tab from add OT")
        self.builder.delay(ui_cmd_obj, 5)

        return ui_cmd_obj

    def ot_gu_acc_prv_gen_acc_act(self, ui_cmd_obj, arg_dict):
        self.wait_for_page_load_completely(ui_cmd_obj)
        if arg_dict['add_ot_click_gu'] == "yes":
            self.click_on_ot_add_gu_tab(ui_cmd_obj)
        if arg_dict['ot_account_act'] == "time_based":
            self.builder.click(ui_cmd_obj, "//div[1]/div[@role='presentation']/div[@role='presentation']/"
                                           "span[@role='presentation']/input[@name='userAccountActivationType']")
            self.logger.log_info("selected time-based")
        elif arg_dict['ot_account_act'] == "first_login":
            self.builder.click(ui_cmd_obj, "//div[2]/div[@role='presentation']/div[@role='presentation']/"
                                           "span[@role='presentation']/input[@name='userAccountActivationType']")
            self.logger.log_info("selected first login")
        else:
            self.logger.log_info("nothing selected")
        if arg_dict['ot_save'] == "save":
            self.ot_save(ui_cmd_obj, arg_dict)
            self.builder.delay(ui_cmd_obj, 5)
            self.builder.click(ui_cmd_obj, "//span[@role='presentation']/span[text()='Refresh']")

        return ui_cmd_obj

    def ot_gu_acc_prv_gen_acc_exp(self, ui_cmd_obj, arg_dict):
        self.wait_for_page_load_completely(ui_cmd_obj)
        if arg_dict['add_ot_click_gu'] == "yes":
            self.click_on_ot_add_gu_tab(ui_cmd_obj)
        self.is_element_selected(ui_cmd_obj, "//input[@name='userAccountExpiration']",
                                 self.builder.constants.STRATEGY_XPATH)
        self.logger.log_info("expiration check box default is selected")
        web_obj = self.builder.find_element(ui_cmd_obj, "//fieldset[10]/div/div[@role='presentation']/div[@role="
                                                        "'presentation']/fieldset[1]//label[text()="
                                                        "'Account Activation']",
                                            self.builder.constants.STRATEGY_XPATH)
        return_txt = web_obj.is_enabled()
        self.logger.log_info(return_txt)
        self.logger.log_info("account activation field exists")
        if not return_txt:
            ui_cmd_obj.error_state = False
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info(ui_cmd_obj.error_state)
        self.builder.delay(ui_cmd_obj, 2)
        web_obj = self.builder.find_element(ui_cmd_obj, "//div[@role='presentation']/div[@role='presentation']"
                                                        "/span[@role='presentation']"
                                                        "/input[@name='userAccountExpirationType' and "
                                                        "@checked='checked']",
                                            self.builder.constants.STRATEGY_XPATH)
        return_txt = self.base_builder.is_element_selected(ui_cmd_obj, web_obj)
        self.logger.log_info(return_txt)
        self.logger.log_info("Max expiration default is selected")
        if not return_txt:
            ui_cmd_obj.error_state = False
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info(ui_cmd_obj.error_state)
        web_obj = self.builder.find_element(ui_cmd_obj, "//div[@role='presentation']/div[@role='presentation']"
                                                        "/span[@role='presentation']/input[@name='userAccount"
                                                        "ExpirationType' and @aria-disabled='false']",
                                            self.builder.constants.STRATEGY_XPATH)
        return_txt = self.base_builder.is_element_selected(ui_cmd_obj, web_obj)
        self.logger.log_info(return_txt)
        self.logger.log_info("Permanent default is disabled")
        if not return_txt:
            ui_cmd_obj.error_state = False
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info(ui_cmd_obj.error_state)
        self.builder.click(ui_cmd_obj, "//input[@name='userAccountExpiration']")
        self.logger.log_info("unselected account expiration checkbox")
        self.builder.click(ui_cmd_obj, "//div[2]/div[@role='presentation']/div[@role='presentation']/"
                                       "span[@role='presentation']/input[@name='userAccountExpirationType']")
        self.logger.log_info("selected permanent radio button")
        self.builder.delay(ui_cmd_obj, 5)
        web_obj = self.builder.find_element(ui_cmd_obj, "//fieldset[10]/"
                                                        "div/div[@role='presentation']/div[@role='presentation']/"
                                                        "fieldset[1]//label[text()='Account Activation']")
        return_txt = self.base_builder.is_element_displayed(ui_cmd_obj, web_obj)
        self.logger.log_info(return_txt)
        self.logger.log_info("account activation field should not displayed")
        if not return_txt:
            ui_cmd_obj.error_state = False
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info(ui_cmd_obj.error_state)
        self.builder.click(ui_cmd_obj, "//div[1]/div[@role='presentation']/div[@role='presentation']/"
                                       "span[@role='presentation']/input[@name='userAccountExpirationType']")
        self.logger.log_info("selected Max expiration radio button")
        self.builder.delay(ui_cmd_obj, 5)
        web_obj = self.builder.find_element(ui_cmd_obj, "//fieldset[10]/div/div[@role='presentation']/"
                                                        "div[@role='presentation']/fieldset[1]//"
                                                        "label[text()='Account Activation']")
        return_txt = self.base_builder.is_element_displayed(ui_cmd_obj, web_obj)
        self.logger.log_info(return_txt)
        self.logger.log_info("account activation field should be displayed")
        if return_txt:
            ui_cmd_obj.error_state = False
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info(ui_cmd_obj.error_state)
        self.builder.click(ui_cmd_obj, "//div[2]/div[@role='presentation']/div[@role='presentation']/"
                                       "span[@role='presentation']/input[@name='userAccountExpirationType']")
        self.logger.log_info("selected permanent radio button once again")
        self.builder.delay(ui_cmd_obj, 5)
        web_obj = self.builder.find_element(ui_cmd_obj, "//fieldset[10]/div/div[@role='presentation']/"
                                                        "div[@role='presentation']/fieldset[1]//"
                                                        "label[text()='Account Activation']")
        return_txt = self.base_builder.is_element_displayed(ui_cmd_obj, web_obj)
        self.logger.log_info(return_txt)
        self.logger.log_info("account activation field should not displayed once again")
        if not return_txt:
            ui_cmd_obj.error_state = False
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info(ui_cmd_obj.error_state)
        if arg_dict['ot_save'] == "save":
            self.ot_save(ui_cmd_obj, arg_dict)
            self.builder.click(ui_cmd_obj, "//span[@role='presentation']/span[text()='Refresh']")

        return ui_cmd_obj

    def ot_signed_user_footer(self, ui_cmd_obj, arg_dict):
        self.wait_for_page_load_completely(ui_cmd_obj)
        self.builder.get_text_from_element_and_compare(ui_cmd_obj, "#basic-statusbar-targetEl [data-ref] "
                                                                   ".x-toolbar-text-default:nth-of-type(1)",
                                                       arg_dict["signed_user_footer_text"],
                                                       self.builder.constants.STRATEGY_CSS_SELECTOR)

        return ui_cmd_obj

    def ot_tab_validation(self, ui_cmd_obj, ind):
        try:
            web_obj = self.builder.find_element(ui_cmd_obj, "//div[@role='form']/div/div[@role='presentation']"
                                                            "/div[@role='tablist']/div[1]/div[2]"
                                                            "/div/a[" + str(ind) + "][@aria-hidden='false']")
            return_text = self.base_builder.is_element_displayed(ui_cmd_obj, web_obj)
            self.logger.log_info(return_text)
            if not return_text:
                self.logger.log_info(return_text + "is not equal to" + "True")
                ui_cmd_obj.error_state = True
            return ui_cmd_obj
        except AttributeError:
            return ui_cmd_obj

    def wait_for_ot_deletion(self, ui_cmd_obj):
        self.builder.webdriver_wait_until(ui_cmd_obj, "div[role=dialog]", retry=5,
                                          strategy=self.builder.constants.STRATEGY_CSS_SELECTOR,
                                          condition=self.builder.constants.CONDITION_INVISIBILITY_OF_ELEMENT)
        return ui_cmd_obj

    def ot_gu_selection(self, ui_cmd_obj, arg_dict):
        index = 0
        if arg_dict['ot_gu_notif'] == "email":
            index = 1
        elif arg_dict['ot_gu_notif'] == "sms":
            index = 2
        elif arg_dict['ot_gu_notif'] == "username":
            index = 3
        elif arg_dict['ot_gu_notif'] == "password":
            index = 4
        web_obj = self.builder.find_element(ui_cmd_obj, ".x-fieldset-default:nth-of-type(1) "
                                                        ".x-fieldset-default:nth-of-type(1) "
                                                        ".x-form-check-group:nth-of-type"
                                                        "(" + str(index) + ") [autocomplete]",
                                            self.builder.constants.STRATEGY_CSS_SELECTOR)
        result = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(result)
        if (not result) and (arg_dict['check'] == "True"):
            self.builder.click(ui_cmd_obj, ".x-fieldset-default:nth-of-type(1) .x-fieldset-default:nth-of-type(1) "
                                           ".x-form-check-group:nth-of-type(" + str(index) + ") [autocomplete]",
                               self.builder.constants.STRATEGY_CSS_SELECTOR)
        if result and (arg_dict['check'] == "False"):
            self.builder.click(ui_cmd_obj, ".x-fieldset-default:nth-of-type(1) .x-fieldset-default:nth-of-type(1) "
                                           ".x-form-check-group:nth-of-type(" + str(index) + ") [autocomplete]",
                               self.builder.constants.STRATEGY_CSS_SELECTOR)

        return ui_cmd_obj

    def ot_should_not_exist(self, ui_cmd_obj, arg_dict):
        self.wait_for_page_load_completely(ui_cmd_obj)
        all_count = self.builder.find_elements(ui_cmd_obj, "//div[@class ='x-grid-item-container']/table")
        row_count = len(all_count)
        self.logger.log_info("row_count: " + str(row_count))
        for index in range(1, (row_count + 1)):
            web_obj = self.builder.find_element(ui_cmd_obj, "//div[@class ='x-grid-item-container']"
                                                            "/table[" + str(index) + "]/tbody/tr/td[1]")
            return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
            self.logger.log_info("otname: " + str(index) + "::" + return_text)
            if return_text == arg_dict['ot_name']:
                ui_cmd_obj.error_state = True
                self.logger.log_info("<" + arg_dict['ot_name'] + "> ot_name: exists ::" + return_text)
                break
            elif return_text == '':
                ui_cmd_obj.error_state = True
                break
            else:
                self.logger.log_info("<" + arg_dict['ot_name'] + "> ot_name: does not exists ::" + return_text)
                ui_cmd_obj.error_state = False

        return ui_cmd_obj

    def ot_gu_edit_username_field(self, ui_cmd_obj, arg_dict):
        self.wait_for_page_load_completely(ui_cmd_obj)
        self.is_element_displayed(ui_cmd_obj, ".x-tab-default-top:nth-of-type(3) [data-ref='btnInnerEl']",
                                  self.builder.constants.STRATEGY_CSS_SELECTOR)
        # username
        self.builder.click(ui_cmd_obj, ".x-tab-default-top:nth-of-type(3) [data-ref='btnInnerEl']",
                           self.builder.constants.STRATEGY_CSS_SELECTOR)
        self.is_element_selected(ui_cmd_obj, "//input[@name='autoGenUsernameType' and @checked='checked']",
                                 self.builder.constants.STRATEGY_XPATH)
        self.builder.click(ui_cmd_obj, "//label[text()='Generate Username with:']")
        self.builder.delay(ui_cmd_obj, 5)
        if arg_dict['uncheck'] == "uncheck":
            self.builder.click(ui_cmd_obj, "//input[@name='usernameEditable']")
            self.builder.delay(ui_cmd_obj, 5)
            web_obj = self.builder.find_element(ui_cmd_obj, "//input[@name='usernameEditable']")
            b_check = self.base_builder.get_attribute_from_element(ui_cmd_obj, web_obj, "value")
            self.logger.log_info(b_check)
        else:
            web_obj = self.builder.find_element(ui_cmd_obj, "//input[@name='usernameEditable']")
            un_check = self.base_builder.get_attribute_from_element(ui_cmd_obj, web_obj, "value")
            self.logger.log_info(un_check)
            if un_check == "off":
                ui_cmd_obj.error_state = True
        if arg_dict['ot_save'] == "save":
            self.ot_save(ui_cmd_obj, arg_dict)
        else:
            self.ot_cancel(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def ot_delete_error_text(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//span[text()='Delete']")
        self.spinner_loading(ui_cmd_obj)
        self.builder.click(ui_cmd_obj, "//div[1]/a[@role='menuitem']/span[@role='presentation']")
        self.builder.click(ui_cmd_obj, "//span[@role='presentation']/span[text()='Yes']")
        self.builder.get_text_from_element_and_compare(ui_cmd_obj, ".x-window-text", arg_dict["ot_error_text"],
                                                       self.builder.constants.STRATEGY_CSS_SELECTOR)
        self.builder.click(ui_cmd_obj, "//span[text()='OK']")
        self.spinner_loading(ui_cmd_obj)

        return ui_cmd_obj

    def ot_multiple_row_selection(self, ui_cmd_obj, arg_dict):
        self.wait_for_page_load_completely(ui_cmd_obj)
        self.builder.delay(ui_cmd_obj, 5)
        all_count = self.builder.find_elements(ui_cmd_obj, "//div[@class ='x-grid-item-container']/table")
        row_count = len(all_count)
        self.logger.log_info("row_count: " + str(row_count))
        if row_count > 0:
            web_obj_from = self.builder.find_element(ui_cmd_obj,
                                                     "//div[@class ='x-grid-item-container']/table[1]/tbody/tr/td[1]")
            web_obj_to = self.builder.find_element(ui_cmd_obj,
                                                   "//div[@class ='x-grid-item-container']/"
                                                   "table[" + str(row_count) + "]/tbody/tr/td[1]")
            self.base_builder.select_and_click_multiple_elements(ui_cmd_obj, web_obj_from, web_obj_to)

        return ui_cmd_obj

    def ot_table_should_empty(self, ui_cmd_obj, arg_dict):
        self.wait_for_page_load_completely(ui_cmd_obj)
        self.base_builder.execute_script(ui_cmd_obj, "return document.getElementsByTagName('table').length;")
        self.logger.log_info("ui_cmd_obj.return_data:  " + str(ui_cmd_obj.return_data))
        if ui_cmd_obj.return_data == 0:
            ui_cmd_obj.error_state = False
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info(ui_cmd_obj.error_state)

        return ui_cmd_obj

    def ot_gu_pwd_complexity_config(self, ui_cmd_obj, arg_dict):
        self.builder.enter_text(ui_cmd_obj, arg_dict['pwd_length'], "//input[@name='passwordChars']")
        self.builder.delay(ui_cmd_obj, 5)
        if arg_dict['pwd_type_lower'] == "lower":
            web_obj_lc = self.builder.find_element(ui_cmd_obj,
                                                   "(//input[@name = 'passwordComplexity'])[1]",
                                                   self.builder.constants.STRATEGY_XPATH)
            true_or_false_lc = self.base_builder.get_attribute_from_element(ui_cmd_obj, web_obj_lc, "checked")
            if not true_or_false_lc:
                self.set_check_box_value(ui_cmd_obj,
                                         "(//input[@name = 'passwordComplexity'])[1]",
                                         self.builder.constants.STRATEGY_XPATH, True)
        else:
            web_obj_lc = self.builder.find_element(ui_cmd_obj,
                                                   "(//input[@name = 'passwordComplexity'])[1]",
                                                   self.builder.constants.STRATEGY_XPATH)
            true_or_false_lc = self.base_builder.get_attribute_from_element(ui_cmd_obj, web_obj_lc, "checked")
            if true_or_false_lc:
                self.set_check_box_value(ui_cmd_obj,
                                         "(//input[@name = 'passwordComplexity'])[1]",
                                         self.builder.constants.STRATEGY_XPATH, False)
        if arg_dict['pwd_type_upper'] == "upper":
            web_obj_uc = self.builder.find_element(ui_cmd_obj,
                                                   "(//input[@name = 'passwordComplexity'])[2]",
                                                   self.builder.constants.STRATEGY_XPATH)
            true_or_false_uc = self.base_builder.get_attribute_from_element(ui_cmd_obj, web_obj_uc, "checked")
            if not true_or_false_uc:
                self.set_check_box_value(ui_cmd_obj,
                                         "(//input[@name = 'passwordComplexity'])[2]",
                                         self.builder.constants.STRATEGY_XPATH, True)
        else:
            web_obj_uc = self.builder.find_element(ui_cmd_obj,
                                                   "(//input[@name = 'passwordComplexity'])[2]",
                                                   self.builder.constants.STRATEGY_XPATH)
            true_or_false_uc = self.base_builder.get_attribute_from_element(ui_cmd_obj, web_obj_uc, "checked")
            if true_or_false_uc:
                self.set_check_box_value(ui_cmd_obj,
                                         "(//input[@name = 'passwordComplexity'])[2]",
                                         self.builder.constants.STRATEGY_XPATH, False)
        if arg_dict['pwd_type_number'] == "number":
            web_obj_num = self.builder.find_element(ui_cmd_obj, "(//input[@name = 'passwordComplexity'])[3]",
                                                    self.builder.constants.STRATEGY_XPATH)
            true_or_false_num = self.base_builder.get_attribute_from_element(ui_cmd_obj, web_obj_num, "checked")
            if not true_or_false_num:
                self.set_check_box_value(ui_cmd_obj,
                                         "(//input[@name = 'passwordComplexity'])[3]",
                                         self.builder.constants.STRATEGY_XPATH, True)
        else:
            web_obj_num = self.builder.find_element(ui_cmd_obj,
                                                    "(//input[@name = 'passwordComplexity'])[3]",
                                                    self.builder.constants.STRATEGY_XPATH)
            true_or_false_num = self.base_builder.get_attribute_from_element(ui_cmd_obj, web_obj_num, "checked")
            if true_or_false_num:
                self.set_check_box_value(ui_cmd_obj,
                                         "(//input[@name = 'passwordComplexity'])[3]",
                                         self.builder.constants.STRATEGY_XPATH, False)
        if arg_dict['pwd_type_special'] == "special":
            web_obj_sp = self.builder.find_element(ui_cmd_obj, "(//input[@name = 'passwordComplexity'])[4]",
                                                   self.builder.constants.STRATEGY_XPATH)
            true_or_false_sp = self.base_builder.get_attribute_from_element(ui_cmd_obj, web_obj_sp, "checked")
            if not true_or_false_sp:
                self.set_check_box_value(ui_cmd_obj,
                                         "(//input[@name = 'passwordComplexity'])[4]",
                                         self.builder.constants.STRATEGY_XPATH, True)
        else:
            web_obj_sp = self.builder.find_element(ui_cmd_obj,
                                                   "(//input[@name = 'passwordComplexity'])[4]",
                                                   self.builder.constants.STRATEGY_XPATH)
            true_or_false_sp = self.base_builder.get_attribute_from_element(ui_cmd_obj, web_obj_sp, "checked")
            if true_or_false_sp:
                self.set_check_box_value(ui_cmd_obj,
                                         "(//input[@name = 'passwordComplexity'])[4]",
                                         self.builder.constants.STRATEGY_XPATH, False)
        if arg_dict['error_or_noerror'] == "error":
            web_obj = self.builder.find_element(ui_cmd_obj, "(//span[contains(text(),'[4,30]')])[2]")
            web_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
            a = web_text.split(",")
            lower_limit = a[0][-1]
            upper_limit = a[1].strip("]")
            if arg_dict['pwd_length'] < lower_limit or arg_dict['pwd_length'] > upper_limit:
                ui_cmd_obj.error_state = False
            else:
                ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def ot_validation_advanced_tab(self, ui_cmd_obj, arg_dict):
        true_or_false = self.builder.is_element_displayed(ui_cmd_obj, ".x-tab-default-top:nth-of-type(9) "
                                                                      "[data-ref='btnInnerEl']",
                                                          self.builder.constants.STRATEGY_CSS_SELECTOR)
        if true_or_false == "True":
            ui_cmd_obj.error_state = False
        else:
            ui_cmd_obj.error_state = True
        self.builder.click(ui_cmd_obj, ".x-tab-default-top:nth-of-type(9) [data-ref='btnInnerEl']",
                           self.builder.constants.STRATEGY_CSS_SELECTOR)
        self.wait_for_page_load_completely(ui_cmd_obj)
        # time zone label
        web_obj = self.builder.find_element(ui_cmd_obj, "//span[@id='time-labelTextEl']")
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.builder.logger.log_info(return_text)
        if return_text == arg_dict['time_zone_label']:
            ui_cmd_obj.error_state = False
        else:
            ui_cmd_obj.error_state = True
        # default time zone value
        web_obj = self.builder.find_element(ui_cmd_obj, "//input[@name='timezone']")
        return_text = self.base_builder.get_attribute_from_element(ui_cmd_obj, web_obj, "value")
        self.logger.log_info(return_text)
        if return_text == arg_dict['default_time_zone']:
            ui_cmd_obj.error_state = False
        else:
            ui_cmd_obj.error_state = True
        # checkbox status
        web_obj = self.builder.find_element(ui_cmd_obj, "//input[@name='ADdefaultOT']")
        return_text = self.base_builder.is_element_selected(ui_cmd_obj, web_obj)
        self.logger.log_info("checkbox is in checked state: " + str(return_text))
        if str(return_text) == str(False):
            self.logger.log_info("the current state " + str(return_text) + " is same")
            ui_cmd_obj.error_state = False
        else:
            self.logger.log_info("the current state " + str(return_text) + " is not same")
            ui_cmd_obj.error_state = True
        # ldap provsioner label
        web_obj = self.builder.find_element(ui_cmd_obj, "//div[starts-with(@id, 'OTAdvancedPanel') and "
                                                        "@data-ref='innerCt']/div[2]/div")
        return_text = self.base_builder.get_attribute_from_element(ui_cmd_obj, web_obj, "innerText")
        self.logger.log_info(return_text)
        if return_text == arg_dict['default_label_for_ldap_prov']:
            self.build.error_state = False
        else:
            ui_cmd_obj.error_state = True
        # Associated LDAP Groups
        web_obj = self.builder.find_element(ui_cmd_obj, "//div[text()='Associated LDAP Groups:']")
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.builder.logger.log_info(return_text)
        if return_text == arg_dict['associated_label_ldap_groups']:
            ui_cmd_obj.error_state = False
        else:
            ui_cmd_obj.error_state = True
        # Associated LDAP Textbox
        web_obj = self.builder.find_element(ui_cmd_obj, "//input[@name='ADGroupName']",
                                            self.builder.constants.STRATEGY_XPATH)
        return_txt = self.base_builder.is_element_displayed(ui_cmd_obj, web_obj)
        self.logger.log_info(return_txt)
        if return_txt:
            ui_cmd_obj.error_state = False
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info(ui_cmd_obj.error_state)
        # Add Button Greyedout
        web_obj = self.builder.find_element(ui_cmd_obj, "//a[@class='x-btn x-unselectable x-box-item "
                                                        "x-btn-default-small x-item-disabled x-btn-disabled']")
        return_text = self.base_builder.get_attribute_from_element(ui_cmd_obj, web_obj, "aria-disabled")
        self.builder.logger.log_info(return_text)
        if return_text:
            ui_cmd_obj.error_state = False
        else:
            ui_cmd_obj.error_state = True
        # Remove Button Greyedout
        web_obj = self.builder.find_element(ui_cmd_obj, "//a[@class='x-btn x-unselectable x-item-disabled "
                                                        "x-box-item x-btn-default-small x-btn-disabled']")
        return_text = self.base_builder.get_attribute_from_element(ui_cmd_obj, web_obj, "aria-disabled")
        self.builder.logger.log_info(return_text)
        if return_text:
            ui_cmd_obj.error_state = False
        else:
            ui_cmd_obj.error_state = True
        # Example Configuration
        web_obj = self.builder.find_element(ui_cmd_obj, "//div[@role='form']/div[@role='presentation']/div"
                                                        "[@role='presentation']/div[5]/div[@role='presentation']/"
                                                        "div[@role='textbox']")
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_text)
        if return_text == "Ex. CN=GimTemplate,CN=Test,DC=ADGroup,DC=com":
            ui_cmd_obj.error_state = False
        else:
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def ot_temp_acc_validity(self, ui_cmd_obj, arg_dict):
        self.builder.webdriver_wait_until(ui_cmd_obj, "//span[text()='Common']", retry=5)
        self.builder.click(ui_cmd_obj, "//span[text()='Common']", self.builder.constants.STRATEGY_XPATH)
        self.builder.delay(ui_cmd_obj, 2)
        self.builder.enter_text(ui_cmd_obj, arg_dict['duration'], "//input[@name='duration']",
                                self.builder.constants.STRATEGY_XPATH)
        if arg_dict['time_type'] == 'minutes':
            self.builder.click(ui_cmd_obj, "//label[contains(text(),'minute')]")
        elif arg_dict['time_type'] == 'hours':
            self.builder.click(ui_cmd_obj, "//label[contains(text(),'hour')]")
        elif arg_dict['time_type'] == 'days':
            self.builder.click(ui_cmd_obj, "//label[contains(text(),'day')]")
        if arg_dict['err_no_err'] == "Error":
            web_obj = self.builder.find_element(ui_cmd_obj, "//input[@name='duration']",
                                                self.builder.constants.STRATEGY_XPATH)
            time_value = self.base_builder.get_attribute_from_element(ui_cmd_obj, web_obj, "value")
            if 1 < int(time_value) < 9999:
                ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def ot_accessible_to_prov_gu(self, ui_cmd_obj, arg_dict):
        self.wait_for_page_load_completely(ui_cmd_obj)
        self.builder.click(ui_cmd_obj, "//div[@role='form']/div/div[@role='presentation']/div[@role='tablist']/"
                                       "div[1]/div[2]/div/a[3]", self.builder.constants.STRATEGY_XPATH)
        self.spinner_loading(ui_cmd_obj)
        if arg_dict['sms_gateway_list'] == "sms_yes":
            self.set_check_box_value(ui_cmd_obj, "//input[@name='userSMSGateway']",
                                     self.builder.constants.STRATEGY_XPATH, True)
        elif arg_dict['sms_gateway_list'] == "sms_no":
            self.set_check_box_value(ui_cmd_obj, "//input[@name='userSMSGateway']",
                                     self.builder.constants.STRATEGY_XPATH, False)
        if arg_dict['acc_exp'] == "acc_exp_yes":
            self.set_check_box_value(ui_cmd_obj, "//input[@name='userAccountExpiration']",
                                     self.builder.constants.STRATEGY_XPATH, True)
            if arg_dict['acc_exp_option'] == "max_exp_time":
                self.builder.click(ui_cmd_obj, "(//input[@name='userAccountExpirationType'])[1]")
            perm_obj = self.builder.find_element(ui_cmd_obj, "(//input[@name='userAccountExpirationType'])[2]")
            perm_status = self.base_builder.is_element_selected(ui_cmd_obj, perm_obj)
            self.logger.log_info("perm_status:" + str(perm_status))
            if str(perm_status) != "False":
                ui_cmd_obj.error_state = True
            if arg_dict['delete_on_expiry'] == "doe_yes":
                self.set_check_box_value(ui_cmd_obj, "//input[@name='userDeleteOnExpire']",
                                         self.builder.constants.STRATEGY_XPATH, True)
            elif arg_dict['delete_on_expiry'] == "doe_no":
                self.set_check_box_value(ui_cmd_obj, "//input[@name='userDeleteOnExpire']",
                                         self.builder.constants.STRATEGY_XPATH, False)
            if arg_dict['doe_option'] == "delete_on_expire":
                self.builder.click(ui_cmd_obj, "(//input[@class='x-form-cb-input' and "
                                               "@name='userDeleteOnExpireDefaultValue'])[1]")
            elif arg_dict['doe_option'] == "do_not_doe":
                self.builder.click(ui_cmd_obj, "(//input[@class='x-form-cb-input' and "
                                               "@name='userDeleteOnExpireDefaultValue'])[2]")
        elif arg_dict['acc_exp'] == "acc_exp_no":
            self.set_check_box_value(ui_cmd_obj, "//input[@name='userAccountExpiration']",
                                     self.builder.constants.STRATEGY_XPATH, False)
            if arg_dict['acc_exp_option'] == "max_exp_time":
                self.builder.click(ui_cmd_obj, "//input[@name='userAccountExpirationType']/../../"
                                               "label[text()='Max Expiration Time']")
                if arg_dict['delete_on_expiry'] == "doe_yes":
                    self.set_check_box_value(ui_cmd_obj, "//input[@name='userDeleteOnExpire']",
                                             self.builder.constants.STRATEGY_XPATH, True)
                elif arg_dict['delete_on_expiry'] == "doe_no":
                    self.set_check_box_value(ui_cmd_obj, "//input[@name='userDeleteOnExpire']",
                                             self.builder.constants.STRATEGY_XPATH, False)
                if arg_dict['doe_option'] == "delete_on_expire":
                    self.builder.click(ui_cmd_obj, "(//input[@class='x-form-cb-input' and "
                                                   "@name='userDeleteOnExpireDefaultValue'])[1]")
                elif arg_dict['doe_option'] == "do_not_doe":
                    self.builder.click(ui_cmd_obj, "(//input[@class='x-form-cb-input' and "
                                                   "@name='userDeleteOnExpireDefaultValue'])[2]")
            elif arg_dict['acc_exp_option'] == "permanent":
                self.builder.click(ui_cmd_obj, "//input[@name='userAccountExpirationType']/../../"
                                               "label[text()='Permanent']")
        if arg_dict['access_groups'] == "ag_yes":
            self.set_check_box_value(ui_cmd_obj, "//input[@class='x-form-cb-input' and @name='userAccessGroups']",
                                     self.builder.constants.STRATEGY_XPATH, True)
        elif arg_dict['access_groups'] == "ag_no":
            self.set_check_box_value(ui_cmd_obj, "//input[@class='x-form-cb-input' and @name='userAccessGroups']",
                                     self.builder.constants.STRATEGY_XPATH, False)
        if arg_dict['first_last_name'] == "fl_name_yes":
            self.set_check_box_value(ui_cmd_obj, "//input[@name='userFirstLastname']",
                                     self.builder.constants.STRATEGY_XPATH, True)
            if arg_dict['first_last_name_option'] == "fl_name_man":
                self.builder.click(ui_cmd_obj, "//input[@name='userFirstLastnameMan']/../../label[text()='Mandatory']")
            elif arg_dict['first_last_name_option'] == "fl_name_opt":
                self.builder.click(ui_cmd_obj, "//input[@name='userFirstLastnameMan']/../../label[text()='Optional']")
        elif arg_dict['first_last_name'] == "fl_name_no":
            self.builder.click(ui_cmd_obj, "//input[@name='userFirstLastnameMan']/../../label[text()='Optional']")
            self.set_check_box_value(ui_cmd_obj, "//input[@name='userFirstLastname']",
                                     self.builder.constants.STRATEGY_XPATH, False)
        self.builder.click(ui_cmd_obj, "//div[@class='x-panel x-tabpanel-child x-panel-default']/div/"
                                       "div/div/div/a[@data-qtip='Save Onboarding Template']")
        self.spinner_loading(ui_cmd_obj)
        self.builder.click(ui_cmd_obj, "//span[text()='OK']")
        self.spinner_loading(ui_cmd_obj)
        self.builder.delay(ui_cmd_obj, 5)
        self.builder.click(ui_cmd_obj, "//span[@role='presentation']/span[text()='Refresh']")

        return ui_cmd_obj

    def ot_accessible_to_prov_de(self, ui_cmd_obj, arg_dict):
        self.wait_for_page_load_completely(ui_cmd_obj)
        self.builder.click(ui_cmd_obj, "//div[@role='form']/div/div[@role='presentation']/div[@role='tablist']/"
                                       "div[1]/div[2]/div/a[5]", self.builder.constants.STRATEGY_XPATH)
        self.spinner_loading(ui_cmd_obj)
        if arg_dict['name_option'] == "name_man":
            self.builder.click(ui_cmd_obj, "(//input[@name='deviceNameMan'])[1]")
        elif arg_dict['name_option'] == "name_opt":
            self.builder.click(ui_cmd_obj, "(//input[@name='deviceNameMan'])[2]")
            if arg_dict['name'] == "name_yes":
                self.set_check_box_value(ui_cmd_obj, "//input[@name='deviceName']",
                                         self.builder.constants.STRATEGY_XPATH, True)
            elif arg_dict['name'] == "name_no":
                self.set_check_box_value(ui_cmd_obj, "//input[@name='deviceName']",
                                         self.builder.constants.STRATEGY_XPATH, False)
        if arg_dict['limit_devices'] == "limit_yes":
            self.set_check_box_value(ui_cmd_obj, "//input[@name='deviceProvisionerLimit']",
                                     self.builder.constants.STRATEGY_XPATH, True)
            self.builder.enter_text(ui_cmd_obj, arg_dict['device_limit_number'],
                                    "//input[@name='deviceProvisionerLimitMaxValue']")
        elif arg_dict['limit_devices'] == "limit_no":
            self.set_check_box_value(ui_cmd_obj, "//input[@name='deviceProvisionerLimit']",
                                     self.builder.constants.STRATEGY_XPATH, False)
        if arg_dict['display_admin_comments'] == "comment_yes":
            self.set_check_box_value(ui_cmd_obj, "//input[@name='deviceAdminComments']",
                                     self.builder.constants.STRATEGY_XPATH, True)
            self.builder.delay(ui_cmd_obj, 2)
            self.builder.enter_text(ui_cmd_obj, arg_dict['admin_comment'],
                                    "//textarea[@name='deviceAdminCommentsValue']",
                                    self.builder.constants.STRATEGY_XPATH)
        elif arg_dict['display_admin_comments'] == "comment_no":
            self.set_check_box_value(ui_cmd_obj, "//input[@name='deviceAdminComments']",
                                     self.builder.constants.STRATEGY_XPATH, False)
        if arg_dict['source'] == "source_yes":
            self.set_check_box_value(ui_cmd_obj, "//input[@name='deviceSource']",
                                     self.builder.constants.STRATEGY_XPATH, True)
        elif arg_dict['source'] == "source_no":
            self.set_check_box_value(ui_cmd_obj, "//input[@name='deviceSource']",
                                     self.builder.constants.STRATEGY_XPATH, False)
        if arg_dict['source_option'] == "auto":
            self.builder.click(ui_cmd_obj, "(//input[@name='deviceSourceType'])[1]")
        elif arg_dict['source_option'] == "static":
            self.builder.click(ui_cmd_obj, "(//input[@name='deviceSourceType'])[2]")
            self.builder.delay(ui_cmd_obj, 2)
            self.builder.enter_text(ui_cmd_obj, arg_dict['static_source_value'],
                                    "//input[@name='deviceSourceStaticValue']", self.builder.constants.STRATEGY_XPATH)
        if arg_dict['asset_type'] == "asset_yes":
            self.set_check_box_value(ui_cmd_obj, "//input[@name='deviceAsset']",
                                     self.builder.constants.STRATEGY_XPATH, True)
            if arg_dict['asset_type_option'] == "permanent":
                self.builder.click(ui_cmd_obj, "(//input[@name='deviceAssetType'])[1]")
            elif arg_dict['asset_type_option'] == "temporary":
                self.builder.click(ui_cmd_obj, "(//input[@name='deviceAssetType'])[2]")
            if arg_dict['doe_yes_or_no'] == "doe_yes":
                self.set_check_box_value(ui_cmd_obj, "//input[@name='deviceDeleteOnExpire']",
                                         self.builder.constants.STRATEGY_XPATH, True)
            elif arg_dict['doe_yes_or_no'] == "doe_no":
                self.set_check_box_value(ui_cmd_obj, "//input[@name='deviceDeleteOnExpire']",
                                         self.builder.constants.STRATEGY_XPATH, False)
            if arg_dict['doe_option'] == "delete_on_expire":
                self.builder.click(ui_cmd_obj, "(//input[@name='deviceDeleteOnExpireDefaultValue'])[1]")
            elif arg_dict['doe_option'] == "do_not_doe":
                self.builder.click(ui_cmd_obj, "(//input[@name='deviceDeleteOnExpireDefaultValue'])[2]")
            if arg_dict['acc_exp'] == "acc_exp_yes":
                self.set_check_box_value(ui_cmd_obj, "//input[@name='deviceAccountExpiration']",
                                         self.builder.constants.STRATEGY_XPATH, True)
            elif arg_dict['acc_exp'] == "acc_exp_no":
                self.set_check_box_value(ui_cmd_obj, "//input[@name='deviceAccountExpiration']",
                                         self.builder.constants.STRATEGY_XPATH, False)
        elif arg_dict['asset_type'] == "asset_no":
            self.set_check_box_value(ui_cmd_obj, "//input[@name='deviceAsset']",
                                     self.builder.constants.STRATEGY_XPATH, False)
            if arg_dict['asset_type_option'] == "permanent":
                self.builder.click(ui_cmd_obj, "(//input[@name='deviceAssetType'])[1]")
            elif arg_dict['asset_type_option'] == "temporary":
                self.builder.click(ui_cmd_obj, "(//input[@name='deviceAssetType'])[2]")
                if arg_dict['doe_yes_or_no'] == "doe_yes":
                    self.set_check_box_value(ui_cmd_obj, "//input[@name='deviceDeleteOnExpire']",
                                             self.builder.constants.STRATEGY_XPATH, True)
                elif arg_dict['doe_yes_or_no'] == "doe_no":
                    self.set_check_box_value(ui_cmd_obj, "//input[@name='deviceDeleteOnExpire']",
                                             self.builder.constants.STRATEGY_XPATH, False)
                if arg_dict['doe_option'] == "delete_on_expire":
                    self.builder.click(ui_cmd_obj, "(//input[@name='deviceDeleteOnExpireDefaultValue'])[1]")
                elif arg_dict['doe_option'] == "do_not_doe":
                    self.builder.click(ui_cmd_obj, "(//input[@name='deviceDeleteOnExpireDefaultValue'])[2]")
                if arg_dict['acc_exp'] == "acc_exp_yes":
                    self.set_check_box_value(ui_cmd_obj, "//input[@name='deviceAccountExpiration']",
                                             self.builder.constants.STRATEGY_XPATH, True)
                elif arg_dict['acc_exp'] == "acc_exp_no":
                    self.set_check_box_value(ui_cmd_obj, "//input[@name='deviceAccountExpiration']",
                                             self.builder.constants.STRATEGY_XPATH, False)
        if arg_dict['asset_type'] == "asset_yes":
            if arg_dict['account_activation_type'] == "timebased":
                self.builder.click(ui_cmd_obj, "//input[@name='deviceAccountActivationType']/../../"
                                               "label[text()='Time Based']", self.builder.constants.STRATEGY_XPATH)
            elif arg_dict['account_activation_type'] == "firstlogin":
                self.builder.click(ui_cmd_obj, "//input[@name='deviceAccountActivationType']/../../"
                                               "label[text()='First Login']", self.builder.constants.STRATEGY_XPATH)
        if arg_dict['device_type_group'] == "dtg_yes":
            dtg_obj = self.builder.find_element(ui_cmd_obj, "//input[@name='deviceFamily']")
            dtg_checked_status = dtg_obj.get_attribute("checked")
            if dtg_checked_status != "true":
                self.builder.click(ui_cmd_obj, "//input[@name='deviceFamily']")
            if arg_dict['device_type_group_option'] == "dtg_man_yes":
                self.builder.click(ui_cmd_obj, "(//input[@name='deviceFamilyMan'])[1]")
            elif arg_dict['device_type_group_option'] == "dtg_opt_yes":
                self.builder.click(ui_cmd_obj, "(//input[@name='deviceFamilyMan'])[2]")
        elif arg_dict['device_type_group'] == "dtg_no":
            self.builder.click(ui_cmd_obj, "(//input[@name='deviceFamilyMan'])[2]")
            dtg_obj = self.builder.find_element(ui_cmd_obj, "//input[@name='deviceFamily']")
            dtg_checked_status = self.base_builder.get_attribute_from_element(ui_cmd_obj, dtg_obj, "checked")
            if dtg_checked_status != "false":
                self.builder.click(ui_cmd_obj, "//input[@name='deviceFamily']")
        self.builder.click(ui_cmd_obj, "//div[@class='x-panel x-tabpanel-child x-panel-default']/div/"
                                       "div/div/div/a[@data-qtip='Save Onboarding Template']")
        self.builder.click(ui_cmd_obj, "//span[text()='OK']")
        if arg_dict['error_or_no'] == "error":
            web_obj = self.builder.find_element(ui_cmd_obj, "(//div[@class='x-title-text x-title-text-default "
                                                            "x-title-item'])[3]")
            web_text = self.base_builder.get_attribute_from_element(ui_cmd_obj, web_obj, "innerText")
            if web_text != "Error":
                ui_cmd_obj.error_state = True
            self.builder.delay(ui_cmd_obj, 2)
            self.builder.click(ui_cmd_obj, "//span[text()='OK']")
            self.builder.delay(ui_cmd_obj, 2)
            self.builder.click(ui_cmd_obj, "#addEditOnboardingTemplateDialog [role='tabpanel']:nth-of-type(5) "
                                           ".x-btn-inner-default-small", self.builder.constants.STRATEGY_CSS_SELECTOR)
        self.spinner_loading(ui_cmd_obj)

        return ui_cmd_obj

    def ot_add_ldap_group(self, ui_cmd_obj, arg_dict):
        self.wait_for_page_load_completely(ui_cmd_obj)
        self.builder.click(ui_cmd_obj, ".x-tab-default-top:nth-of-type(9) [data-ref='btnInnerEl']",
                           self.builder.constants.STRATEGY_CSS_SELECTOR)
        self.spinner_loading(ui_cmd_obj)
        if arg_dict['check_box_status'] == "True":
            self.set_check_box_value(ui_cmd_obj, "//input[@name='ADdefaultOT']",
                                     self.builder.constants.STRATEGY_XPATH, True)
        if arg_dict['check_box_status'] == "False":
            self.set_check_box_value(ui_cmd_obj, "//input[@name='ADdefaultOT']",
                                     self.builder.constants.STRATEGY_XPATH, False)
        if arg_dict['time_zone'] == "yes_time_zone":
            self.select_time_zone_name_from_drop_down(ui_cmd_obj, arg_dict)
        if arg_dict['ad_group'] == "yes_ad_group":
            self.builder.click(ui_cmd_obj, "//input[@name='ADGroupName']")
            self.builder.enter_text(ui_cmd_obj, arg_dict['ad_group_name'], "//input[@name='ADGroupName']")
            self.builder.click(ui_cmd_obj, "//input[@name='ADGroupName']/following::a[1]")
        if arg_dict['remove_group'] == "yes_remove_group":
            self.builder.click(ui_cmd_obj, "#addEditOnboardingTemplateDialog [role='presentation'] td "
                                           "div.x-grid-cell-inner", self.builder.constants.STRATEGY_CSS_SELECTOR)
            self.builder.click(ui_cmd_obj, "#addEditOnboardingTemplateDialog [role='presentation']:nth-of-type(4) "
                                           ".x-btn-inner-default-small", self.builder.constants.STRATEGY_CSS_SELECTOR)
        self.ot_save(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def spinner_loading(self, ui_cmd_obj):
        self.builder.webdriver_wait_until(ui_cmd_obj, ".x-mask-msg-text", retry=5,
                                          strategy=self.builder.constants.STRATEGY_CSS_SELECTOR,
                                          condition=self.builder.constants.CONDITION_INVISIBILITY_OF_ELEMENT)
        return ui_cmd_obj

    def select_time_zone_name_from_drop_down(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//div[@id='time-trigger-picker']")
        time_zone = arg_dict['time_zone_name']
        a, b, c = time_zone.split()
        self.logger.log_info("abc" + a + b + c)
        mod_time_zone = a + "  " + b + "  " + c
        self.logger.log_info("mod_time_zone: " + mod_time_zone)
        self.builder.enter_text(ui_cmd_obj, mod_time_zone, "//input[@name='timezone']")
        self.builder.click(ui_cmd_obj, "//div[@id='time-trigger-picker']")

        return ui_cmd_obj

    def is_ldap_pop_up_exists(self, ui_cmd_obj):
        web_obj = self.builder.find_element(ui_cmd_obj, "[role='alertdialog'] div [hidefocus='on']:nth-of-type(1)",
                                            self.builder.constants.STRATEGY_CSS_SELECTOR)
        if self.base_builder.is_element_displayed(ui_cmd_obj, web_obj):
            self.logger.log_info("element exists")
            self.base_builder.click(ui_cmd_obj, web_obj)
            self.spinner_loading(ui_cmd_obj)
        else:
            self.logger.log_info("element not exists")

        return ui_cmd_obj

    def is_element_displayed(self, ui_cmd_obj, locator, strategy):
        web_obj = self.builder.find_element(ui_cmd_obj, locator, strategy)
        return_txt = self.base_builder.is_element_displayed(ui_cmd_obj, web_obj)
        self.logger.log_info(return_txt)
        if not return_txt:
            ui_cmd_obj.error_state = True
            self.logger.log_info(ui_cmd_obj.error_state)

        return ui_cmd_obj

    def is_element_selected(self, ui_cmd_obj, locator, strategy):
        web_obj = self.builder.find_element(ui_cmd_obj, locator, strategy)
        return_txt = self.base_builder.is_element_selected(ui_cmd_obj, web_obj)
        self.logger.log_info(return_txt)
        if not return_txt:
            ui_cmd_obj.error_state = True
            self.logger.log_info(ui_cmd_obj.error_state)

        return ui_cmd_obj

    def select_row_from_ot_table(self, ui_cmd_obj, arg_dict):
        self.wait_for_page_load_completely(ui_cmd_obj)
        all_count = self.builder.find_elements(ui_cmd_obj, "//div[@class ='x-grid-item-container']/table")
        row_count = len(all_count)
        self.logger.log_info("row_count: " + str(row_count))
        for index in range(1, (row_count + 1)):
            web_obj = self.builder.find_element(ui_cmd_obj, "//div[@class ='x-grid-item-container']/"
                                                            "table[" + str(index) + "]/tbody/tr/td[1]")
            return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
            self.logger.log_info("ot_name: " + str(index) + "::" + return_text)
            if return_text == arg_dict['ot_name']:
                self.builder.click(ui_cmd_obj, "//div[@class ='x-grid-item-container']/"
                                               "table[" + str(index) + "]/tbody/tr/td[1]")
                self.logger.log_info("selected ot: " + str(arg_dict['ot_name']))
                ui_cmd_obj.error_state = False
                break
            else:
                ui_cmd_obj.error_state = True

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

    def ot_sponsor_auto_approve_deny(self, ui_cmd_obj, arg_dict):
        self.wait_for_page_load_completely(ui_cmd_obj)
        self.builder.click(ui_cmd_obj, "//span[text()='Sponsor']")
        self.spinner_loading(ui_cmd_obj)
        self.builder.delay(ui_cmd_obj, 5)
        self.builder.click(ui_cmd_obj, "//input[@type='checkbox' and @name='sponsorApproval']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['ot_spon_domain'], "//input[@name='sponsorEmailDomain']")
        self.builder.click(ui_cmd_obj, ".x-form-item-no-label:nth-of-type(1) >"
                                       " [data-ref] > [data-ref] > [data-ref] > [data-ref] > "
                                       ".x-form-item-no-label:nth-of-type(2) .x-btn-default-small",
                           self.builder.constants.STRATEGY_CSS_SELECTOR)
        self.set_check_box_value(ui_cmd_obj, "//input[@name='sponsorResonseTimeout']",
                                 self.builder.constants.STRATEGY_XPATH, True)
        self.builder.click(ui_cmd_obj, "//input[@name='sponsorResonseTimeoutValue']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['spon_response'], "//input[@name='sponsorResonseTimeoutValue']")
        if arg_dict['auto_approve_deny'] == 'approve':
            self.builder.click(ui_cmd_obj, "(//input[@name='responseTimeoutAction'])[1]")
        if arg_dict['auto_approve_deny'] == 'deny':
            self.builder.click(ui_cmd_obj, "(//input[@name='responseTimeoutAction'])[2]")
        self.builder.click(ui_cmd_obj, ".x-panel-default:nth-of-type(4) .x-btn-blue-small",
                           self.builder.constants.STRATEGY_CSS_SELECTOR)
        self.is_ldap_pop_up_exists(ui_cmd_obj)
        self.builder.click(ui_cmd_obj, "//span[@role='presentation']/span[text()='Refresh']")

        return ui_cmd_obj

    def ot_resend_details(self, ui_cmd_obj, arg_dict):
        self.wait_for_page_load_completely(ui_cmd_obj)
        self.builder.click(ui_cmd_obj, "//div[@role='form']/div/div[@role='presentation']/div[@role='tablist']/"
                                       "div[1]/div[2]/div/a[3]", self.builder.constants.STRATEGY_XPATH)
        self.spinner_loading(ui_cmd_obj)
        self.is_element_displayed(ui_cmd_obj, "//label[text()='Resend Details']",
                                  self.builder.constants.STRATEGY_XPATH)
        self.is_element_displayed(ui_cmd_obj, "//label[text()='Resend All Details']",
                                  self.builder.constants.STRATEGY_XPATH)
        self.is_element_displayed(ui_cmd_obj, "//label[text()='Resend Password Only']",
                                  self.builder.constants.STRATEGY_XPATH)

        if arg_dict['resend_yes_no'] == "resend_yes":
            self.set_check_box_value(ui_cmd_obj, "//input[@name='userResendPwd']",
                                     self.builder.constants.STRATEGY_XPATH, True)
        elif arg_dict['resend_yes_no'] == "resend_no":
            self.set_check_box_value(ui_cmd_obj, "//input[@name='userResendPwd']",
                                     self.builder.constants.STRATEGY_XPATH, False)

        if arg_dict['resend_option'] == "resend_all_details":
            self.builder.click(ui_cmd_obj, "(//input[@name='userResendType'])[1]",
                               self.builder.constants.STRATEGY_XPATH)
        elif arg_dict['resend_option'] == "resend_pwd":
            self.builder.click(ui_cmd_obj, "(//input[@name='userResendType'])[2]",
                               self.builder.constants.STRATEGY_XPATH)

        self.builder.click(ui_cmd_obj, "//div[@class='x-panel x-tabpanel-child x-panel-default']/div/"
                                       "div/div/div/a[@data-qtip='Save Onboarding Template']")
        self.spinner_loading(ui_cmd_obj)
        self.builder.click(ui_cmd_obj, "//span[text()='OK']")
        self.spinner_loading(ui_cmd_obj)
        self.builder.delay(ui_cmd_obj, 5)
        self.builder.click(ui_cmd_obj, "//span[@role='presentation']/span[text()='Refresh']")

        return ui_cmd_obj

    def ot_access_groups(self, ui_cmd_obj, arg_dict):
        self.wait_for_page_load_completely(ui_cmd_obj)
        if arg_dict['gu_or_de'] == "guestuser":
            self.builder.click(ui_cmd_obj, "//div[@role='form']/div/div[@role='presentation']/div[@role='tablist']/"
                                           "div[1]/div[2]/div/a[3]", self.builder.constants.STRATEGY_XPATH)
            if arg_dict['access_yes_or_no'] == "access_yes":
                self.set_check_box_value(ui_cmd_obj, "(//label[text()='Access Groups']/../span)[1]",
                                         self.builder.constants.STRATEGY_XPATH, True)
            elif arg_dict['access_yes_or_no'] == "access_no":
                self.set_check_box_value(ui_cmd_obj, "(//label[text()='Access Groups']/../span)[1]",
                                         self.builder.constants.STRATEGY_XPATH, False)
        elif arg_dict['gu_or_de'] == "device":
            self.builder.click(ui_cmd_obj, "//div[@role='form']/div/div[@role='presentation']/div[@role='tablist']/"
                                           "div[1]/div[2]/div/a[5]", self.builder.constants.STRATEGY_XPATH)
            if arg_dict['access_yes_or_no'] == "access_yes":
                self.set_check_box_value(ui_cmd_obj, "(//label[text()='Access Groups']/../span)[2]",
                                         self.builder.constants.STRATEGY_XPATH, True)
            elif arg_dict['access_yes_or_no'] == "access_no":
                self.set_check_box_value(ui_cmd_obj, "(//label[text()='Access Groups']/../span)[2]",
                                         self.builder.constants.STRATEGY_XPATH, False)

        return ui_cmd_obj
