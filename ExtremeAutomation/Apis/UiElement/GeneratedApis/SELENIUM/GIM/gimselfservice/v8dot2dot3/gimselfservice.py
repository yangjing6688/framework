from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as GimselfserviceBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Gimselfservice(GimselfserviceBase):
    def self_service_add(self, ui_cmd_obj, arg_dict):
        self.navigate_to_self_service_proviosioner(ui_cmd_obj, arg_dict)
        self.builder.click(ui_cmd_obj, "//a[@data-qtip='Add Self-Service Provisioner']")
        self.spinner_loading(ui_cmd_obj)
        self.builder.enter_text(ui_cmd_obj, arg_dict['serv_name'], "loginId", self.builder.constants.STRATEGY_NAME)
        self.builder.click(ui_cmd_obj, "serviceType", self.builder.constants.STRATEGY_NAME)
        st = arg_dict['serv_type']
        self.select_option_from_drop_down(ui_cmd_obj, 1, st)
        self.builder.enter_text(ui_cmd_obj, arg_dict['pwd'], "userCredential", self.builder.constants.STRATEGY_NAME)
        self.builder.click(ui_cmd_obj, "//div[5]/div[@role='presentation']/div[@role='presentation']"
                                       "/div[@role='presentation']/input[@role='textbox']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['conf_pwd'],
                                "//div[5]/div[@role='presentation']/div[@role='presentation']"
                                "/div[@role='presentation']/input[@role='textbox']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['serv_email'], "userEmailAddress",
                                self.builder.constants.STRATEGY_NAME)
        self.builder.click(ui_cmd_obj, "//input[@name='userProvOnboardingTemplate']")
        self.spinner_loading(ui_cmd_obj)
        ot = arg_dict['ot_name']
        self.select_option_from_drop_down(ui_cmd_obj, 2, ot)
        self.spinner_loading(ui_cmd_obj)
        if arg_dict['serv_type'] == "Device" and arg_dict['dev_check'] == "True":
            web_obj = self.builder.find_element(ui_cmd_obj, "//input[@name='requireUserAuth']")
            true_or_false = self.base_builder.get_attribute_from_element(ui_cmd_obj, web_obj, "checked")
            self.logger.log_info(true_or_false)
            if not true_or_false:
                web_obj.click()
        self.builder.enter_text(ui_cmd_obj, arg_dict['terms'], "termOfUse", self.builder.constants.STRATEGY_NAME)
        self.builder.enter_text(ui_cmd_obj, arg_dict['intervals'], "refreshTimeout",
                                self.builder.constants.STRATEGY_NAME)
        if arg_dict['redirection'] == "self-service":
            self.builder.click(ui_cmd_obj, "[valign] > [role='presentation']:nth-of-type(1) .x-form-cb-input",
                               self.builder.constants.STRATEGY_CSS_SELECTOR)
        if arg_dict['redirection'] == "url":
            self.builder.click(ui_cmd_obj, "[valign] > [role='presentation']:nth-of-type(2) .x-form-cb-input",
                               self.builder.constants.STRATEGY_CSS_SELECTOR)
            self.builder.enter_text(ui_cmd_obj, arg_dict['url_text'], "redirectUrl",
                                    self.builder.constants.STRATEGY_NAME)
        if arg_dict['redirection'] == "nothing":
            self.builder.click(ui_cmd_obj, "[valign] > [role='presentation']:nth-of-type(3) .x-form-cb-input",
                               self.builder.constants.STRATEGY_CSS_SELECTOR)
        self.builder.click(ui_cmd_obj, "[role='dialog'] .x-btn-inner-blue-small",
                           self.builder.constants.STRATEGY_CSS_SELECTOR)
        self.spinner_loading(ui_cmd_obj)

        return ui_cmd_obj

    def self_service_delete(self, ui_cmd_obj, arg_dict):
        self.navigate_to_self_service_proviosioner(ui_cmd_obj, arg_dict)
        self.select_row_from_self_service_table(ui_cmd_obj, 1, arg_dict)
        self.builder.click(ui_cmd_obj, "//a[@aria-disabled='false']/span/span/span[text()='Delete']")
        self.builder.click(ui_cmd_obj, "//span[text()='Yes']")
        self.builder.delay(ui_cmd_obj, 2000)

        return ui_cmd_obj

    def self_service_edit(self, ui_cmd_obj, arg_dict):
        self.navigate_to_self_service_proviosioner(ui_cmd_obj, arg_dict)
        self.select_row_from_self_service_table(ui_cmd_obj, 1, arg_dict)
        self.builder.click(ui_cmd_obj,
                           "//span[@class='x-btn-inner x-btn-inner-default-toolbar-small' and text()='Edit']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['edit_email'], "userEmailAddress",
                                self.builder.constants.STRATEGY_NAME)
        self.builder.enter_text(ui_cmd_obj, arg_dict['intervals'], "refreshTimeout",
                                self.builder.constants.STRATEGY_NAME)
        self.builder.enter_text(ui_cmd_obj, arg_dict['terms'], "termOfUse", self.builder.constants.STRATEGY_NAME)
        self.builder.click(ui_cmd_obj, "//div[starts-with(@id, 'AddEditSelfServiceProvisionersDialog')]/div/"
                                       "div/div/div/a[1]")
        self.builder.delay(ui_cmd_obj, 5)

        return ui_cmd_obj

    def self_service_provisioners_page_validation(self, ui_cmd_obj, arg_dict):
        self.navigate_to_self_service_proviosioner(ui_cmd_obj, arg_dict)
        self.is_element_displayed(ui_cmd_obj, "//a[@data-qtip='Add Self-Service Provisioner' and "
                                              "@aria-disabled='false']", self.builder.constants.STRATEGY_XPATH)
        self.is_element_displayed(ui_cmd_obj, "//a[@data-qtip='Edit Self-Service Provisioner' and "
                                              "@aria-disabled='true']", self.builder.constants.STRATEGY_XPATH)
        self.is_element_displayed(ui_cmd_obj, "//a[@data-qtip='Delete Self-Service Provisioner(s)' and "
                                              "@aria-disabled='true']", self.builder.constants.STRATEGY_XPATH)
        self.select_row_from_self_service_table(ui_cmd_obj, 1, arg_dict)
        self.builder.delay(ui_cmd_obj, 2000)
        self.is_element_displayed(ui_cmd_obj, "//a[@data-qtip='Add Self-Service Provisioner' and "
                                              "@aria-disabled='false']", self.builder.constants.STRATEGY_XPATH)
        self.is_element_displayed(ui_cmd_obj, "//a[@data-qtip='Edit Self-Service Provisioner' and "
                                              "@aria-disabled='false']", self.builder.constants.STRATEGY_XPATH)
        self.is_element_displayed(ui_cmd_obj, "//a[@data-qtip='Delete Self-Service Provisioner(s)' and "
                                              "@aria-disabled='false']", self.builder.constants.STRATEGY_XPATH)

        return ui_cmd_obj

    def self_service_should_exist(self, ui_cmd_obj, arg_dict):
        self.navigate_to_self_service_proviosioner(ui_cmd_obj, arg_dict)
        all_count = self.builder.find_elements(ui_cmd_obj, "//div[@class ='x-grid-item-container']/table")
        row_count = len(all_count)
        self.logger.log_info("row_count: " + str(row_count))
        for index in range(1, (row_count + 1)):
            web_obj = self.builder.find_element(ui_cmd_obj, "//div[@class ='x-grid-item-container']/"
                                                            "table[" + str(index) + "]/tbody/tr/td[1]")
            return_txt = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
            self.logger.log_info("serv_name: " + str(index) + "::" + return_txt)
            # service email
            if return_txt == arg_dict['serv_name']:
                web_obj = self.builder.find_element(ui_cmd_obj, "//div[@class ='x-grid-item-container']/"
                                                                "table[" + str(index) + "]/tbody/tr/td[2]")
                return_txt = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
                if return_txt != arg_dict['serv_email']:
                    self.logger.log_info("serv_email: " + str(index) + "::" + return_txt)
                    self.logger.log_info("<" + arg_dict['serv_email'] + "> serv_email: is not "
                                                                        "equal to ::" + return_txt)
                    ui_cmd_obj.error_state = True
                    break
                # service type
                if return_txt == arg_dict['serv_email']:
                    web_obj = self.builder.find_element(ui_cmd_obj, "//div[@class ='x-grid-item-container']/"
                                                                    "table[" + str(index) + "]/tbody/tr/td[3]")
                    return_txt = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
                if return_txt != arg_dict['serv_type']:
                    self.logger.log_info("serv_type: " + str(index) + "::" + return_txt)
                    self.logger.log_info("<" + arg_dict['serv_type'] + "> serv_type: is not "
                                                                       "equal to ::" + return_txt)
                    ui_cmd_obj.error_state = True
                    break
                # ot name
                if return_txt == arg_dict['serv_type']:
                    web_obj = self.builder.find_element(ui_cmd_obj, "//div[@class ='x-grid-item-container']/"
                                                                    "table[" + str(index) + "]/tbody/tr/td[4]")
                    return_txt = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
                if return_txt == arg_dict['ot_name']:
                    self.logger.log_info("<" + arg_dict['ot_name'] + "> ot_name: is equal to ::" + return_txt)
                    ui_cmd_obj.error_state = False
                    break
                elif return_txt != arg_dict['ot_name']:
                    self.logger.log_info("<" + arg_dict['ot_name'] + "> ot_name: is not equal to ::" + return_txt)
                    ui_cmd_obj.error_state = True
                    break
            elif return_txt == '':
                ui_cmd_obj.error_state = True
            else:
                self.logger.log_info("<" + arg_dict['serv_name'] + "> serv_name: is not equal to ::" + return_txt)
                ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def self_service_should_not_exist(self, ui_cmd_obj, arg_dict):
        self.navigate_to_self_service_proviosioner(ui_cmd_obj, arg_dict)
        all_count = self.builder.find_elements(ui_cmd_obj, "//div[starts-with(@id,'selfServiceProvisionersPanel')]"
                                                           "//div[@class ='x-grid-item-container']/table")
        row_count = len(all_count)
        self.logger.log_info("row_count: " + str(row_count))
        for index in range(1, (row_count + 1)):
            web_obj = self.builder.find_element(ui_cmd_obj, "//div[starts-with(@id,'selfServiceProvisionersPanel')]"
                                                            "//div[@class ='x-grid-item-container']"
                                                            "/table[" + str(index) + "]/tbody/tr/td[1]")
            return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
            self.logger.log_info("serv_name: " + str(index) + "::" + return_text)
            if return_text == arg_dict['serv_name']:
                ui_cmd_obj.error_state = True
                self.logger.log_info("<" + arg_dict['serv_name'] + "> serv_name: exists ::" + return_text)
                break
            elif return_text == '':
                ui_cmd_obj.error_state = True
                break
            else:
                self.logger.log_info("<" + arg_dict['serv_name'] + "> serv_name: does not exists ::" + return_text)
                ui_cmd_obj.error_state = False

        return ui_cmd_obj

    def self_provisioning_service_page_validation(self, ui_cmd_obj, arg_dict):
        self.navigate_to_self_provisioning_services(ui_cmd_obj, arg_dict)
        self.is_element_displayed(ui_cmd_obj, "//a[@data-qtip='Edit selected Self-Provisioning Service' and "
                                              "@aria-disabled='true']", self.builder.constants.STRATEGY_XPATH)
        self.is_element_displayed(ui_cmd_obj, "//a[@data-qtip='Refresh Self-Provisioning Service List' and "
                                              "@aria-disabled='false']", self.builder.constants.STRATEGY_XPATH)
        self.select_row_from_self_service_table(ui_cmd_obj, 2, arg_dict)
        self.base_builder.delay(ui_cmd_obj, 2000)
        self.is_element_displayed(ui_cmd_obj, "//a[@data-qtip='Edit selected Self-Provisioning Service' and "
                                              "@aria-disabled='false']", self.builder.constants.STRATEGY_XPATH)
        self.is_element_displayed(ui_cmd_obj, "//a[@data-qtip='Refresh Self-Provisioning Service List' and "
                                              "@aria-disabled='false']", self.builder.constants.STRATEGY_XPATH)

        return ui_cmd_obj

    def self_provisioning_service_should_exist(self, ui_cmd_obj, arg_dict):
        self.navigate_to_self_provisioning_services(ui_cmd_obj, arg_dict)
        arg_dict = [arg_dict['serv_name'], arg_dict['serv_type'], arg_dict['serv_status'], arg_dict['serv_url'],
                    arg_dict['copy_url']]
        self.uti_table_complete_validation(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def select_option_from_phone_carrier(self, ui_cmd_obj, arg_dict, element_locator, strategy):
        self.builder.delay(ui_cmd_obj, 5)
        self.builder.click(ui_cmd_obj, element_locator, strategy)
        self.builder.delay(ui_cmd_obj, 2)
        items = self.builder.find_elements(ui_cmd_obj, "//li[@class='x-boundlist-item']")
        for item in items:
            if arg_dict['phone_carrier'] in item.text:
                item.click()
                break

        return ui_cmd_obj

    def self_provisioning_service_should_not_exist(self, ui_cmd_obj, arg_dict):
        self.navigate_to_self_provisioning_services(ui_cmd_obj, arg_dict)
        all_count = self.builder.find_elements(ui_cmd_obj, "//div[starts-with(@id,'selfProvisioningServicesPanel')]"
                                                           "//div[@class ='x-grid-item-container']/table")
        row_count = len(all_count)
        self.logger.log_info("row_count: " + str(row_count))
        for index in range(1, (row_count + 1)):
            web_obj = self.builder.find_element(ui_cmd_obj, "//div[starts-with(@id,'selfProvisioningServicesPanel')]"
                                                            "//div[@class ='x-grid-item-container']"
                                                            "/table[" + str(index) + "]/tbody/tr/td[1]")
            return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
            self.logger.log_info("serv_name: " + str(index) + "::" + return_text)
            if return_text == arg_dict['serv_name']:
                ui_cmd_obj.error_state = True
                self.logger.log_info("<" + arg_dict['serv_name'] + "> serv_name: exists ::" + return_text)
                break
            elif return_text == '':
                ui_cmd_obj.error_state = True
                break
            else:
                self.logger.log_info("<" + arg_dict['serv_name'] + "> serv_name: does not exists ::" + return_text)
                ui_cmd_obj.error_state = False

        return ui_cmd_obj

    def self_service_duplicate_handling(self, ui_cmd_obj, arg_dict):
        self.base_builder.delay(ui_cmd_obj, 2000)
        web_obj = self.builder.find_element(ui_cmd_obj, ".x-window-text", self.builder.constants.STRATEGY_CSS_SELECTOR)
        return_txt = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_txt)
        if return_txt == "Error creating Self-Service Provisioner. The Username already exists.":
            self.builder.error_state = False
        self.builder.delay(ui_cmd_obj, 5)
        self.builder.click(ui_cmd_obj, "//span[@class='x-btn-inner x-btn-inner-blue-small' and text()='OK']")
        self.builder.delay(ui_cmd_obj, 5)
        self.builder.click(ui_cmd_obj, "[role='dialog'] [data-qtip]", self.builder.constants.STRATEGY_CSS_SELECTOR)
        self.builder.delay(ui_cmd_obj, 5)

        return ui_cmd_obj

    def self_service_gu_registration_page_validation(self, ui_cmd_obj, arg_dict):
        # Validating Self-Service Guest User Registration page
        self.builder.webdriver_wait_until(ui_cmd_obj, "//input[@name='userFirstName']/preceding::b[1]", retry=5)
        self.is_cookies_exists(ui_cmd_obj)
        self.builder.get_text_from_element_and_compare(ui_cmd_obj, "//input[@name='userFirstName']/preceding::b[1]",
                                                       "Register New Guest User")
        self.builder.get_text_from_element_and_compare(ui_cmd_obj, "//input[@name='userFirstName']/"
                                                                   "preceding::label[1]/span/span", "First Name:")
        self.builder.get_text_from_element_and_compare(ui_cmd_obj, "//input[@name='userLastName']/"
                                                                   "preceding::label[1]/span/span", "Last Name:")
        self.builder.get_text_from_element_and_compare(ui_cmd_obj, "//input[@name='username']/"
                                                                   "preceding::label[1]/span/span", "Username *:")
        self.builder.get_text_from_element_and_compare(ui_cmd_obj, "//input[@name='userPassword']/"
                                                                   "preceding::label[1]/span/span", "Password *:")
        self.builder.get_text_from_element_and_compare(ui_cmd_obj, "//input[@name='userEmail']/"
                                                                   "preceding::label[1]/span/span", "Email *:")
        self.builder.get_text_from_element_and_compare(ui_cmd_obj, "//input[@name='userCellPhone']/"
                                                                   "preceding::label[1]/span/span", "Mobile Phone *:")
        self.builder.get_text_from_element_and_compare(ui_cmd_obj, "//input[@name='userCellPhoneCarrier']/"
                                                                   "preceding::label[1]/span/span", "Carrier *:")
        self.builder.get_text_from_element_and_compare(ui_cmd_obj, "//label[starts-with(@style, 'font-weight: bold;')"
                                                                   " and @class='x-component x-box-item "
                                                                   "x-component-default'][3]",
                                                       "Your guest account access details will be provided to"
                                                       " you via Email/SMS.")
        self.builder.get_text_from_element_and_compare(ui_cmd_obj, "//label[starts-with(@style, 'font-weight: bold;')"
                                                                   " and @class='x-component x-box-item "
                                                                   "x-component-default'][4]", "Terms of Use:")
        # Checking Submit, Clear, Resend Password buttons
        self.is_element_displayed(ui_cmd_obj, "//span[@class='x-btn-inner x-btn-inner-blue-small' and "
                                              "text()='Submit']", self.builder.constants.STRATEGY_XPATH)
        self.is_element_displayed(ui_cmd_obj, "//span[@class='x-btn-inner x-btn-inner-default-small' and "
                                              "text()='Clear']", self.builder.constants.STRATEGY_XPATH)
        self.is_element_displayed(ui_cmd_obj, "//span[@class='x-btn-inner x-btn-inner-default-small' and "
                                              "text()='Resend Password']", self.builder.constants.STRATEGY_XPATH)

        return ui_cmd_obj

    def self_service_device_registration_page_validation(self, ui_cmd_obj, arg_dict):
        # Validating Self-Service Device Registration page
        self.builder.webdriver_wait_until(ui_cmd_obj, "//input[@name='macAddress']", retry=5)
        self.builder.get_text_from_element_and_compare(ui_cmd_obj, "//input[@name='macAddress']/preceding::b[1]",
                                                       "Register New Device")
        self.builder.get_text_from_element_and_compare(ui_cmd_obj, "//input[@name='macAddress']/preceding::label[1]",
                                                       "MAC Address *:")
        self.builder.get_text_from_element_and_compare(ui_cmd_obj, "//input[@name='deviceFamily']/preceding::label[1]",
                                                       "Device Type Group *:")
        self.builder.get_text_from_element_and_compare(ui_cmd_obj, "//input[@name='deviceType']/preceding::label[1]",
                                                       "Device Type *:")
        self.builder.get_text_from_element_and_compare(ui_cmd_obj, "//input[@name='deviceType']/following::label[7]",
                                                       "Terms of Use:")
        self.is_element_displayed(ui_cmd_obj, "//span[@class='x-btn-inner x-btn-inner-blue-small' and "
                                              "text()='Submit']", self.builder.constants.STRATEGY_XPATH)
        self.is_element_displayed(ui_cmd_obj, "//span[@class='x-btn-inner x-btn-inner-default-small' and "
                                              "text()='Clear']", self.builder.constants.STRATEGY_XPATH)

        return ui_cmd_obj

    def self_service_gu_reg_sponsor_appr_page_validation(self, ui_cmd_obj, arg_dict):
        self.builder.webdriver_wait_until(ui_cmd_obj, "//input[@name='userFirstName']", retry=5)
        self.builder.get_text_from_element_and_compare(ui_cmd_obj, "//input[@name='userFirstName']/preceding::b[1]",
                                                       "Register New Guest User")
        self.builder.get_text_from_element_and_compare(ui_cmd_obj, "//input[@name='userFirstName']/preceding::label[1]"
                                                                   "/span/span", "First Name:")
        self.builder.get_text_from_element_and_compare(ui_cmd_obj, "//input[@name='userLastName']/preceding::label[1]"
                                                                   "/span/span", "Last Name:")
        self.builder.get_text_from_element_and_compare(ui_cmd_obj, "//input[@name='username']/preceding::label[1]"
                                                                   "/span/span", "Username *:")
        self.builder.get_text_from_element_and_compare(ui_cmd_obj, "//input[@name='userPassword']/preceding::label[1]"
                                                                   "/span/span", "Password *:")
        self.builder.get_text_from_element_and_compare(ui_cmd_obj, "//input[@name='userEmail']/preceding::label[1]"
                                                                   "/span/span", "Email *:")
        self.builder.get_text_from_element_and_compare(ui_cmd_obj, "//input[@name='userCellPhone']/preceding::label[1]"
                                                                   "/span/span", "Mobile Phone *:")
        self.builder.get_text_from_element_and_compare(ui_cmd_obj,
                                                       "//input[@name='userCellPhoneCarrier']/preceding::label[1]"
                                                       "/span/span", "Carrier *:")
        self.builder.get_text_from_element_and_compare(ui_cmd_obj,
                                                       "//input[@name='userCellPhoneCarrier']/following::b[1]",
                                                       "Sponsor")
        self.builder.get_text_from_element_and_compare(ui_cmd_obj,
                                                       "//input[@name='sponsorFirstName']/preceding::label[1]",
                                                       "First Name *:")
        self.builder.get_text_from_element_and_compare(ui_cmd_obj,
                                                       "//input[@name='sponsorLastName']/preceding::label[1]",
                                                       "Last Name:")
        self.builder.get_text_from_element_and_compare(ui_cmd_obj,
                                                       "//input[@name='sponsorLastName']/following::label[1]",
                                                       "Email *:")
        self.builder.get_text_from_element_and_compare(ui_cmd_obj,
                                                       "//input[@name='sponsorCellPhone']/preceding::label[1]",
                                                       "Mobile Phone:")
        self.builder.get_text_from_element_and_compare(ui_cmd_obj,
                                                       "//div[@class='x-form-display-field x-form-display-"
                                                       "field-default']", "Note: Your access request requires "
                                                                          "Sponsor approval")
        self.builder.get_text_from_element_and_compare(ui_cmd_obj,
                                                       "//input[@name='userCellPhoneCarrier']/following::label[18]",
                                                       "Your guest account access details will be provided "
                                                       "to you via Email/SMS.")
        self.builder.get_text_from_element_and_compare(ui_cmd_obj,
                                                       "//input[@name='userCellPhoneCarrier']/following::label[19]",
                                                       "Terms of Use:")
        # Checking Request Approval, Clear, Resend Password buttons
        self.is_element_displayed(ui_cmd_obj, "//span[@class='x-btn-inner x-btn-inner-blue-small' and "
                                              "text()='Request Approval']", self.builder.constants.STRATEGY_XPATH)
        self.is_element_displayed(ui_cmd_obj, "//span[@class='x-btn-inner x-btn-inner-default-small' and "
                                              "text()='Clear']", self.builder.constants.STRATEGY_XPATH)
        self.is_element_displayed(ui_cmd_obj, "//span[@class='x-btn-inner x-btn-inner-default-small' and "
                                              "text()='Resend Password']", self.builder.constants.STRATEGY_XPATH)

        return ui_cmd_obj

    def self_provisioning_service_edit(self, ui_cmd_obj, arg_dict):
        self.navigate_to_self_provisioning_services(ui_cmd_obj, arg_dict)
        self.select_row_from_self_service_table(ui_cmd_obj, 2, arg_dict)
        self.builder.click(ui_cmd_obj, "//a[@data-qtip='Edit selected Self-Provisioning Service']")
        self.builder.delay(ui_cmd_obj, 5)
        self.builder.enter_text(ui_cmd_obj, arg_dict['edit_email'], "userEmailAddress",
                                self.builder.constants.STRATEGY_NAME)
        self.builder.enter_text(ui_cmd_obj, arg_dict['terms'], "termOfUse", self.builder.constants.STRATEGY_NAME)
        self.builder.enter_text(ui_cmd_obj, arg_dict['intervals'], "refreshTimeout",
                                self.builder.constants.STRATEGY_NAME)
        self.builder.click(ui_cmd_obj, "//div[starts-with(@id, 'AddEditSelfServiceProvisionersDialog')]/div/"
                                       "div/div/div/a[1]")
        self.builder.delay(ui_cmd_obj, 5)

        return ui_cmd_obj

    def self_service_gu_registration(self, ui_cmd_obj, arg_dict):
        self.builder.webdriver_wait_until(ui_cmd_obj, "//input[@name='userFirstName']", retry=5)
        self.builder.enter_text(ui_cmd_obj, arg_dict['gu_fname'], "//input[@name='userFirstName']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['gu_lname'], "//input[@name='userLastName']")
        self.is_cookies_exists(ui_cmd_obj)
        self.builder.enter_text(ui_cmd_obj, arg_dict['gu_uname'], "//input[@name='username']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['gu_pwd'], "//input[@name='userPassword']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['gu_email'], "//input[@name='userEmail']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['gu_cell_phone'], "//input[@name='userCellPhone']")
        self.builder.click(ui_cmd_obj, "//input[@name='userCellPhoneCarrier']")
        self.select_sms_carrier_from_drop_down(ui_cmd_obj, arg_dict)
        self.builder.click(ui_cmd_obj, "//span[@class='x-btn-inner x-btn-inner-blue-small' and text()='Submit']")
        self.builder.webdriver_wait_until(ui_cmd_obj, "//span[@class='x-btn-inner x-btn-inner-blue-small' and "
                                                      "text()='OK']", retry=5)
        self.builder.click(ui_cmd_obj, "//span[@class='x-btn-inner x-btn-inner-blue-small' and text()='OK']")
        self.builder.delay(ui_cmd_obj, 5)

        return ui_cmd_obj

    def self_service_gu_registration_sponsor_approval(self, ui_cmd_obj, arg_dict):
        self.builder.webdriver_wait_until(ui_cmd_obj, "//input[@name='userFirstName']", retry=5)
        self.builder.enter_text(ui_cmd_obj, arg_dict['gu_fname'], "//input[@name='userFirstName']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['gu_lname'], "//input[@name='userLastName']")
        self.is_cookies_exists(ui_cmd_obj)
        self.builder.enter_text(ui_cmd_obj, arg_dict['gu_uname'], "//input[@name='username']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['gu_pwd'], "//input[@name='userPassword']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['gu_email'], "//input[@name='userEmail']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['gu_cell_phone'], "//input[@name='userCellPhone']")
        self.builder.click(ui_cmd_obj, "//input[@name='userCellPhoneCarrier']")
        self.select_sms_carrier_from_drop_down(ui_cmd_obj, arg_dict)
        self.builder.delay(ui_cmd_obj, 5)
        if arg_dict['sponsor_type'] == "manual_sponsor":
            self.builder.enter_text(ui_cmd_obj, arg_dict['spon_fname'], "//input[@name='sponsorFirstName']")
            self.builder.enter_text(ui_cmd_obj, arg_dict['spon_lname'], "//input[@name='sponsorLastName']")
            self.builder.enter_text(ui_cmd_obj, arg_dict['spon_email'], "//input[@name='sponsorLastName']/"
                                                                        "following::input[1]")
            self.builder.click(ui_cmd_obj, "//input[@name='sponsorLastName']/following::input[2]")
            self.select_sponsor_email_domain_from_drop_down(ui_cmd_obj, arg_dict)
            self.builder.delay(ui_cmd_obj, 5)
            self.builder.enter_text(ui_cmd_obj, "1234567890", "//input[@name='sponsorCellPhone']")
            self.builder.click(ui_cmd_obj, "//span[text()='Request Approval']",
                               self.builder.constants.STRATEGY_XPATH)
            self.builder.delay(ui_cmd_obj, 1000)
        if arg_dict['sponsor_type'] == "pre_defined1":
            self.builder.click(ui_cmd_obj, "//div[2]/div[@role='presentation']/div[2]/div[@role='presentation']"
                                           "/div[@role='presentation']/div[2]",
                               self.builder.constants.STRATEGY_XPATH)
            self.builder.delay(ui_cmd_obj, 2)
            self.select_predefined_mail_from_drop_down(ui_cmd_obj, arg_dict)
            self.builder.click(ui_cmd_obj, "//span[text()='Request Approval']",
                               self.builder.constants.STRATEGY_XPATH)
            self.builder.delay(ui_cmd_obj, 1000)
        if arg_dict['sponsor_type'] == "pre_defined2":
            self.builder.enter_text(ui_cmd_obj, arg_dict['spon_email'], "//input[@name='sponsorEmail']")
            self.builder.delay(ui_cmd_obj, 2)
            self.builder.click(ui_cmd_obj, "//span[text()='Request Approval']",
                               self.builder.constants.STRATEGY_XPATH)
            self.builder.delay(ui_cmd_obj, 1000)
        if arg_dict['sponsor_type'] == "fixed":
            self.builder.click(ui_cmd_obj, "//span[text()='Request Approval']",
                               self.builder.constants.STRATEGY_XPATH)
        if arg_dict['sponsor_type'] == "ldap":
            self.builder.enter_text(ui_cmd_obj, "emp1",
                                    "//label/span/span[text()='Sponsor']/following::div[1]/div/div/input")
            self.builder.click(ui_cmd_obj, "//ul[@role='listbox']/ul/li[1]")
            self.builder.click(ui_cmd_obj, "//span[text()='Request Approval']",
                               self.builder.constants.STRATEGY_XPATH)
            self.builder.delay(ui_cmd_obj, 1000)
            self.builder.click(ui_cmd_obj, "//span[@class='x-btn-inner x-btn-inner-blue-small' and text()='OK']")

        return ui_cmd_obj

    def self_service_edit_authenticator(self, ui_cmd_obj, arg_dict):
        self.navigate_to_self_provisioning_services(ui_cmd_obj, arg_dict)
        self.select_row_from_self_service_table(ui_cmd_obj, 2, arg_dict)
        self.builder.click(ui_cmd_obj, "//a[@aria-disabled='false']/span/span/span[text()='Edit']")
        self.builder.delay(ui_cmd_obj, 5)
        true_or_false = arg_dict['true_false']
        self.set_check_box_value(ui_cmd_obj, "//input[@name='requireUserAuth']", self.builder.constants.
                                 STRATEGY_XPATH, bool(true_or_false))
        self.builder.click(ui_cmd_obj, "//div[starts-with(@id, 'AddEditSelfServiceProvisionersDialog')]/div/"
                                       "div/div/div/a[1]")
        self.builder.delay(ui_cmd_obj, 2000)

        return ui_cmd_obj

    def self_service_locale_header_footer_val(self, ui_cmd_obj, arg_dict):
        # tool bar text validation
        web_obj = self.builder.find_element(ui_cmd_obj, ".x-toolbar-text-default",
                                            self.builder.constants.STRATEGY_CSS_SELECTOR)
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_text)
        if return_text != arg_dict['toolbar_text']:
            self.logger.log_info(return_text + " is not equal to " + arg_dict['toolbar_text'])
            ui_cmd_obj.error_state = True
        # tool bar menu
        self.builder.click(ui_cmd_obj, "//div[@role='presentation']/div[@role='presentation']/"
                                       "div[@role='presentation']/div/a[2]")
        web_obj = self.builder.find_element(ui_cmd_obj, "//div[@class='x-menu-item x-menu-item-default x-box-item']"
                                                        "[1]/a/span")
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_text)
        if return_text != arg_dict['menu_support']:
            self.logger.log_info(return_text + " is not equal to " + arg_dict['menu_support'])
            ui_cmd_obj.error_state = True
        web_obj = self.builder.find_element(ui_cmd_obj, "//div[@class='x-menu-item x-menu-item-default x-box-item']"
                                                        "[2]/a/span")
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_text)
        if return_text != arg_dict['menu_about']:
            self.logger.log_info(return_text + " is not equal to " + arg_dict['menu_about'])
            ui_cmd_obj.error_state = True
        self.builder.click(ui_cmd_obj, "//div[@role='presentation']/div[@role='presentation']/"
                                       "div[@role='presentation']/div/a[2]")
        # footer
        web_obj = self.builder.find_element(ui_cmd_obj, "//div[@class='x-box-scroller x-box-scroller-left "
                                                        "x-box-scroller-toolbar x-box-scroller-toolbar-footer "
                                                        "x-unselectable']/following::div/div/a[1]")
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_text)
        if return_text != arg_dict['submit_button']:
            self.logger.log_info(return_text + " is not equal to " + arg_dict['submit_button'])
            ui_cmd_obj.error_state = True
        web_obj = self.builder.find_element(ui_cmd_obj, "//div[@class='x-box-scroller x-box-scroller-left "
                                                        "x-box-scroller-toolbar x-box-scroller-toolbar-footer "
                                                        "x-unselectable']/following::div/div/a[2]")
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_text)
        if return_text != arg_dict['clear_button']:
            self.logger.log_info(return_text + " is not equal to " + arg_dict['clear_button'])
            ui_cmd_obj.error_state = True
        # footer tool bar validation
        web_obj = self.builder.find_element(ui_cmd_obj, "//div[@class='x-box-scroller x-box-scroller-left "
                                                        "x-box-scroller-toolbar x-box-scroller-toolbar-footer "
                                                        "x-unselectable']/following::div/div/a[1]")
        return_text = self.base_builder.get_attribute_from_element(ui_cmd_obj, web_obj, "data-qtip")
        self.logger.log_info(return_text)
        if return_text != arg_dict['submit_tool_tip']:
            self.logger.log_info(return_text + " is not equal to " + arg_dict['submit_tool_tip'])
            ui_cmd_obj.error_state = True
        web_obj = self.builder.find_element(ui_cmd_obj, "//div[@class='x-box-scroller x-box-scroller-left "
                                                        "x-box-scroller-toolbar x-box-scroller-toolbar-footer "
                                                        "x-unselectable']/following::div/div/a[2]")
        return_text = self.base_builder.get_attribute_from_element(ui_cmd_obj, web_obj, "data-qtip")
        self.logger.log_info(return_text)
        if return_text != arg_dict['clear_tool_tip']:
            self.logger.log_info(return_text + " is not equal to " + arg_dict['clear_tool_tip'])
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def self_service_locale_body_val(self, ui_cmd_obj, arg_dict):
        self.builder.webdriver_wait_until(ui_cmd_obj, "//input[@name='macAddress']", retry=5)
        self.get_text_from_element(ui_cmd_obj, "//input[@name='macAddress']/preceding::b[1]",
                                   self.builder.constants.STRATEGY_XPATH, arg_dict['register_device'])
        if arg_dict['with_authenticator'] == "yes_authenticator":
            self.builder.get_text_from_element_and_compare(ui_cmd_obj, "//input[@name='deviceUsername']/"
                                                                       "preceding::label[1]",
                                                           arg_dict['prv_un'] + " *:")
            self.builder.delay(ui_cmd_obj, 1)
            self.builder.get_text_from_element_and_compare(ui_cmd_obj, "//input[@name='deviceUserPassword']/"
                                                                       "preceding::label[1]",
                                                           arg_dict['prv_pwd'] + " *:")
        self.builder.delay(ui_cmd_obj, 1)
        self.builder.get_text_from_element_and_compare(ui_cmd_obj, "//input[@name='macAddress']/"
                                                                   "preceding::label[1]",
                                                       arg_dict['device_mac_ad'] + " *:")
        self.builder.delay(ui_cmd_obj, 1)
        self.builder.get_text_from_element_and_compare(ui_cmd_obj, "//input[@name='deviceFamily']/"
                                                                   "preceding::label[1]",
                                                       arg_dict['device_type_grp'] + " *:")
        self.builder.delay(ui_cmd_obj, 1)
        self.builder.get_text_from_element_and_compare(ui_cmd_obj, "//input[@name='deviceType']/"
                                                                   "preceding::label[1]",
                                                       arg_dict['device_type'] + " *:")
        self.builder.delay(ui_cmd_obj, 1)
        self.builder.get_text_from_element_and_compare(ui_cmd_obj, "//input[@name='deviceType']/"
                                                                   "following::label[7]", arg_dict['device_terms'])
        self.builder.delay(ui_cmd_obj, 1)

        return ui_cmd_obj

    def spinner_loading(self, ui_cmd_obj):
        self.builder.webdriver_wait_until(ui_cmd_obj, ".x-mask-msg-text", retry=5,
                                          strategy=self.builder.constants.STRATEGY_CSS_SELECTOR,
                                          condition=self.builder.constants.CONDITION_INVISIBILITY_OF_ELEMENT)
        return ui_cmd_obj

    def is_element_displayed(self, ui_cmd_obj, locator, strategy):
        web_obj = self.builder.find_element(ui_cmd_obj, locator, strategy)
        return_txt = self.base_builder.is_element_displayed(ui_cmd_obj, web_obj)
        self.logger.log_info(return_txt)
        if not return_txt:
            ui_cmd_obj.error_state = True
            self.logger.log_info(ui_cmd_obj.error_state)

        return ui_cmd_obj

    def select_predefined_mail_from_drop_down(self, ui_cmd_obj, arg_dict):
        self.builder.delay(ui_cmd_obj, 1000)
        items = self.builder.find_elements(ui_cmd_obj, "//li[@role='option']")
        for item in items:
            self.logger.log_info("element name " + item.text)
            if arg_dict['spon_email'] in item.text:
                item.click()
                self.builder.delay(ui_cmd_obj, 500)
                break
        self.builder.delay(ui_cmd_obj, 2)

        return ui_cmd_obj

    def is_cookies_exists(self, ui_cmd_obj):
        web_obj = self.base_builder.find_element_by_xpath(ui_cmd_obj, "//div[@class='cookie-content']/span")
        if self.base_builder.is_element_displayed(ui_cmd_obj, web_obj):
            self.logger.log_info("cookies element exists")
            self.base_builder.click(ui_cmd_obj, web_obj)
            self.spinner_loading(ui_cmd_obj)
        else:
            self.logger.log_info("cookies element not exists")

        return ui_cmd_obj

    def select_sponsor_email_domain_from_drop_down(self, ui_cmd_obj, arg_dict):
        self.builder.delay(ui_cmd_obj, 1000)
        items = self.builder.find_elements(ui_cmd_obj, "//li[@role='option']")
        for item in items:
            self.logger.log_info("element name " + item.text)
            if arg_dict['spon_email_domain'] in item.text:
                item.click()
                self.builder.delay(ui_cmd_obj, 500)
                break
        self.builder.delay(ui_cmd_obj, 2)

        return ui_cmd_obj

    def select_sms_carrier_from_drop_down(self, ui_cmd_obj, arg_dict):
        self.builder.delay(ui_cmd_obj, 1000)
        items = self.builder.find_elements(ui_cmd_obj, "//li[@role='option']")
        for item in items:
            self.logger.log_info("element name " + item.text)
            if arg_dict['user_cell_phone_carrier'] == item.text.strip():
                item.click()
                self.builder.delay(ui_cmd_obj, 500)
                break
        self.builder.delay(ui_cmd_obj, 2)

        return ui_cmd_obj

    def navigate_to_self_service_proviosioner(self, ui_cmd_obj, arg_dict):
        self.builder.delay(ui_cmd_obj, 1000)
        self.builder.click(ui_cmd_obj, "//span[@class='x-btn-inner x-btn-inner-extr-nav-toolbar-button-small' "
                                       "and text()='Self-Services']")
        self.spinner_loading(ui_cmd_obj)
        self.builder.click(ui_cmd_obj, "//span[@class='x-tab-inner x-tab-inner-extr-main-tab-panel' "
                                       "and text()='Self-Service Provisioners']")
        self.builder.delay(ui_cmd_obj, 1000)

        return ui_cmd_obj

    def navigate_to_self_provisioning_services(self, ui_cmd_obj, arg_dict):
        self.builder.delay(ui_cmd_obj, 1000)
        self.builder.click(ui_cmd_obj, "//span[@class='x-btn-inner x-btn-inner-extr-nav-toolbar-button-small' "
                                       "and text()='Self-Services']")
        self.spinner_loading(ui_cmd_obj)
        self.builder.click(ui_cmd_obj, "//span[@class='x-tab-inner x-tab-inner-extr-main-tab-panel' "
                                       "and text()='Self-Provisioning Services']")
        self.builder.delay(ui_cmd_obj, 1000)

        return ui_cmd_obj

    def select_row_from_self_service_table(self, ui_cmd_obj, table_id, arg_dict):
        t_name = None
        if table_id == 1:
            t_name = "selfServiceProvisionersPanel"
            self.logger.log_info("selected option <:" + str(table_id) + ": >")
        if table_id == 2:
            t_name = "selfProvisioningServicesPanel"
            self.logger.log_info("selected option <:" + str(table_id) + ": >")
        all_count = self.builder.find_elements(ui_cmd_obj,
                                               "//div[starts-with(@id, '" + t_name + "') and "
                                                                                     "@data-ref='body']/div/div/table")
        row_count = len(all_count)
        self.logger.log_info("row_count: " + str(row_count))
        for index in range(1, row_count + 1):
            web_obj = self.builder.find_element(ui_cmd_obj, "//div[starts-with"
                                                            "(@id, '" + t_name + "') and @data-ref='body']/div/"
                                                                                 "div/table[" + str(index) + "]/"
                                                                                                             "tbody/"
                                                                                                             "tr/td[1]")
            return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
            self.logger.log_info("serv_name: " + str(index) + "::" + return_text)
            if return_text == arg_dict['serv_name']:
                self.builder.click(ui_cmd_obj,
                                   "//div[starts-with(@id, '" + t_name + "') and @data-ref='body']/"
                                                                         "div/div/table[" + str(index) + "]/tbody/"
                                                                                                         "tr/td[1]")
                ui_cmd_obj.error_state = False
                break
            else:
                ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def select_option_from_drop_down(self, ui_cmd_obj, dl_number, args_dict):
        index = 1
        observed_value = ''
        while index < 25:
            web_obj = self.builder.find_element(ui_cmd_obj, "(//ul[@role='listbox'])"
                                                            "[" + str(dl_number) + "]//li[" + str(index) + "]")
            return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
            self.logger.log_info("arg name: " + str(index) + "::" + return_text)
            if return_text == args_dict:
                web_obj.click()
                self.builder.delay(ui_cmd_obj, 500)
                break
            elif return_text == observed_value:
                ui_cmd_obj.error_state = True
                break
            else:
                observed_value = return_text
                index += 1

        return ui_cmd_obj

    def uti_table_complete_validation(self, ui_cmd_obj, arg_dict):
        self.builder.delay(ui_cmd_obj, 3)
        all_count = self.builder.find_elements(ui_cmd_obj, "//div[starts-with(@id, 'selfProvisioningServicesPanel') "
                                                           "and @data-ref='body']/div/div/table")
        row_count = len(all_count)
        self.logger.log_info("row_count: " + str(row_count))
        for index_r in range(1, (row_count + 1)):
            web_obj = self.builder.find_element(ui_cmd_obj, "//div[starts-with(@id, 'selfProvisioningServicesPanel') "
                                                            "and @data-ref='body']/div/"
                                                            "div/table[" + str(index_r) + "]/tbody/tr/td[1]")
            return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
            self.logger.log_info(str(index_r) + "::" + return_text)
            if return_text == arg_dict[0]:
                self.builder.delay(ui_cmd_obj, 3)
                all_c1_count = self.builder.find_elements(ui_cmd_obj,
                                                          "//div[starts-with(@id, 'selfProvisioningServicesPanel') "
                                                          "and @data-ref='body']/div/div/table[1]/tbody/tr/td")
                c_count = len(all_c1_count)
                self.logger.log_info("column_count: " + str(c_count))
                for index_c in range(2, (c_count + 1)):
                    web_obj = self.builder.find_element(ui_cmd_obj,
                                                        "//div[starts-with(@id, 'selfProvisioningServicesPanel') "
                                                        "and @data-ref='body']/div/div/table[" + str(
                                                            index_r) + "]/tbody/tr/td[" + str(index_c) + "]")
                    return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
                    self.builder.delay(ui_cmd_obj, 2)
                    if return_text == arg_dict[index_c - 1]:
                        self.logger.log_info(("<" + str(index_c) + "> PASS expected <" + arg_dict[
                            index_c - 1] + "> is equal to actual <" + return_text + ">"))
                        ui_cmd_obj.error_state = False
                    if self.base_builder.get_attribute_from_element(ui_cmd_obj, web_obj, "innerText") == "" \
                            and "/GIM/" in arg_dict[index_c - 1]:
                        self.builder.click(ui_cmd_obj, "//div[starts-with(@id, 'selfProvisioningServicesPanel') "
                                                       "and @data-ref='body']/div/div/"
                                                       "table[" + str(index_r) + "]/tbody/tr/td[" + str(index_c) +
                                           "]/div/div")
                        # Handling copy url popup
                        self.builder.delay(ui_cmd_obj, 5)
                        pop_obj = self.builder.find_element(ui_cmd_obj, "//div[@class='x-component x-window-text "
                                                                        "x-box-item x-component-default']")
                        pop_txt = self.base_builder.get_text_from_element(ui_cmd_obj, pop_obj)
                        pop_txt = pop_txt.split(":", 1)
                        self.logger.log_info(pop_txt)
                        pop_txt = pop_txt[1].strip()
                        self.logger.log_info(str(pop_txt))
                        self.builder.click(ui_cmd_obj, "//span[@role='presentation']/span[text()='OK']")
                        actual_text = str(pop_txt)
                        if actual_text == arg_dict[index_c - 1]:
                            self.logger.log_info(("<" + str(index_c) + "> PASS expected <" + arg_dict[
                                index_c - 1] + "> is equal to actual <" + actual_text + ">"))
                            ui_cmd_obj.error_state = False
                            break
                    if return_text != arg_dict[index_c - 1]:
                        self.logger.log_info("<" + str(index_c) + "> FAIL expected <" + arg_dict[
                            index_c - 1] + "> is not equal to actual <" + return_text + ">")
                        ui_cmd_obj.error_state = True
                        break
                    elif return_text == '':
                        ui_cmd_obj.error_state = True
                break
            else:
                self.logger.log_info("Not Exists: <" + arg_dict[0] + "> is not equal to ::" + return_text)
                ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def select_dev_type_from_drop_self_prov(self, ui_cmd_obj, element_locator, strategy, exp_text):
        self.builder.delay(ui_cmd_obj, 1000)
        self.builder.click(ui_cmd_obj, element_locator, strategy)
        self.builder.delay(ui_cmd_obj, 2)
        items = self.builder.find_elements(ui_cmd_obj, "//li[@class='x-boundlist-item']")
        for item in items:
            if exp_text in item.text:
                item.click()
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

    def self_service_device_reg_page_val_locale(self, ui_cmd_obj, arg_dict):
        self.builder.get_text_from_element_and_compare(ui_cmd_obj, "//input[@name='macAddress']/preceding::b[1]",
                                                       arg_dict['locale_reg_device'])
        self.builder.get_text_from_element_and_compare(ui_cmd_obj, "//input[@name='macAddress']/preceding::label[1]",
                                                       arg_dict['locale_mac_ad'] + " *:")
        self.builder.get_text_from_element_and_compare(ui_cmd_obj, "//input[@name='deviceFamily']/preceding::label[1]",
                                                       arg_dict['locale_type_grp'] + " *:")
        self.builder.get_text_from_element_and_compare(ui_cmd_obj, "//input[@name='deviceType']/preceding::label[1]",
                                                       arg_dict['locale_type'] + " *:")
        self.builder.get_text_from_element_and_compare(ui_cmd_obj, "//input[@name='deviceType']/following::label[7]",
                                                       arg_dict['locale_terms'] + ":")
        self.builder.get_text_from_element_and_compare(ui_cmd_obj, "//div[@role='form']//div[@role='toolbar']/"
                                                                   "div[2]/div/a[1]", arg_dict['locale_submit'])
        self.builder.get_text_from_element_and_compare(ui_cmd_obj, "//div[@role='form']//div[@role='toolbar']/div[2]/"
                                                                   "div/a[2]", arg_dict['locale_clear'])
        # tool bar menu
        self.builder.click(ui_cmd_obj, "//div[@role='presentation']/div[@role='presentation']/"
                                       "div[@role='presentation']/div/a[2]")
        web_obj = self.builder.find_element(ui_cmd_obj, "//div[@class='x-menu-item x-menu-item-default x-box-item']"
                                                        "[1]/a/span")
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_text)
        if return_text != arg_dict['menu_support']:
            self.logger.log_info(return_text + " is not equal to " + arg_dict['menu_support'])
            ui_cmd_obj.error_state = True
        web_obj = self.builder.find_element(ui_cmd_obj, "//div[@class='x-menu-item x-menu-item-default x-box-item']"
                                                        "[2]/a/span")
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_text)
        if return_text != arg_dict['menu_about']:
            self.logger.log_info(return_text + " is not equal to " + arg_dict['menu_about'])
            ui_cmd_obj.error_state = True
        self.builder.click(ui_cmd_obj, "//div[@role='presentation']/div[@role='presentation']/"
                                       "div[@role='presentation']/div/a[2]")

        return ui_cmd_obj

    def self_service_dev_reg_page_select_locale(self, ui_cmd_obj, arg_dict):
        self.logger.log_info("expected_locale: " + arg_dict['locale'])
        self.builder.webdriver_wait_until(ui_cmd_obj, "//input[@name='macAddress']", retry=5)
        for index in range(1, 6):
            web_obj = self.builder.find_element(ui_cmd_obj, "#top-locales-toolbar div [hidefocus='on']:"
                                                            "nth-of-type(" + str(index) + ")", self.builder.constants.
                                                STRATEGY_CSS_SELECTOR)
            return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
            self.logger.log_info("locale name: " + str(index) + "::" + return_text)
            if arg_dict['locale'] == return_text:
                web_obj.click()
                self.logger.log_info("clicked on " + return_text)
                break
            if arg_dict['locale'] == return_text:
                web_obj.click()
                self.logger.log_info("clicked on " + return_text)
                break
            if arg_dict['locale'] == return_text:
                web_obj.click()
                self.logger.log_info("clicked on " + return_text)
                break
            if arg_dict['locale'] == return_text:
                web_obj.click()
                self.logger.log_info("clicked on " + return_text)
                break
            if arg_dict['locale'] == return_text:
                web_obj.click()
                self.logger.log_info("clicked on " + return_text)
                break
            if arg_dict['locale'] == return_text:
                web_obj.click()
                self.logger.log_info("clicked on " + return_text)
                break
            if arg_dict['locale'] == return_text:
                web_obj.click()
                self.logger.log_info("clicked on " + return_text)
                break
            if arg_dict['locale'] == return_text:
                web_obj.click()
                self.logger.log_info("clicked on " + return_text)
                break
            if arg_dict['locale'] == return_text:
                web_obj.click()
                self.logger.log_info("clicked on " + return_text)
                break
        self.builder.delay(ui_cmd_obj, 3000)

        return ui_cmd_obj
