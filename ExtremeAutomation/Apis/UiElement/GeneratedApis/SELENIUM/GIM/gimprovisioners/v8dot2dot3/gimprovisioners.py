from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as GimprovisionersBase
# All imports above this line will be removed after generation.
# User imports must be added below.
# -*- coding: utf-8 -*-


class Gimprovisioners(GimprovisionersBase):
    def prv_associate_ot_with_provisioner(self, ui_cmd_obj, arg_dict):
        self.builder.webdriver_wait_until(ui_cmd_obj, "//span[@class ='x-btn-inner x-btn-inner-extr-nav-toolbar-"
                                                      "button-small' and text()='Provisioners']", retry=5)
        self.builder.click(ui_cmd_obj, "//span[@class ='x-btn-inner x-btn-inner-extr-nav-toolbar-button-small' "
                                       "and text()='Provisioners']", self.builder.constants.STRATEGY_XPATH)
        self.spinner_loading(ui_cmd_obj)
        self.builder.click(ui_cmd_obj, "//a[@class ='x-btn x-unselectable "
                                       "x-box-item x-toolbar-item x-btn-default-toolbar-small'][1]")
        self.spinner_loading(ui_cmd_obj)
        self.builder.enter_text(ui_cmd_obj, arg_dict['prv_uname'], "//input[@name='loginId']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['prv_fname'], "//input[@name='userFirstName']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['prv_lname'], "//input[@name='userLastName']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['prv_pwd'], "//input[@name='userCredential']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['prv_pwd'], "//div[6]/div[@role='presentation']/"
                                                                 "div[@role='presentation']/div[@role='presentation']/"
                                                                 "input[@role='textbox']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['prv_email'], "//input[@name='userEmailAddress']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['prv_email'], "//textarea[@name='comments']")
        self.builder.click(ui_cmd_obj, "//label[text() = '" + arg_dict['ot_name'] + "']")
        self.builder.click(ui_cmd_obj, "//span[text()='Save']")
        self.spinner_loading(ui_cmd_obj)

        return ui_cmd_obj

    def prv_should_exist(self, ui_cmd_obj, arg_dict):
        self.builder.webdriver_wait_until(ui_cmd_obj, "//span[@class ='x-btn-inner x-btn-inner-extr-nav-toolbar-"
                                                      "button-small' and text()='Provisioners']", retry=5)
        self.builder.click(ui_cmd_obj, "//span[@class ='x-btn-inner x-btn-inner-extr-nav-toolbar-button-small' "
                                       "and text()='Provisioners']", self.builder.constants.STRATEGY_XPATH)
        self.spinner_loading(ui_cmd_obj)
        self.builder.click(ui_cmd_obj, "//span[text()='Internal Provisioners']")
        self.spinner_loading(ui_cmd_obj)
        all_count = self.builder.find_elements(ui_cmd_obj, "//div[@class ='x-grid-item-container']/table")
        row_count = len(all_count)
        self.logger.log_info("row_count: " + str(row_count))
        for index in range(1, (row_count + 1)):
            web_obj = self.builder.find_element(ui_cmd_obj, "//div[@class ='x-grid-item-container']/"
                                                            "table[" + str(index) + "]/tbody/tr/td[1]")
            return_txt = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
            self.logger.log_info("prv_uname: " + str(index) + "::" + return_txt)
            # fname
            if return_txt == arg_dict['prv_uname']:
                web_obj = self.builder.find_element(ui_cmd_obj, "//div[@class ='x-grid-item-container']/"
                                                                "table[" + str(index) + "]/tbody/tr/td[2]")
                return_txt = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
                if return_txt != arg_dict['prv_fname']:
                    self.logger.log_info("prv_fname: " + str(index) + "::" + return_txt)
                    self.logger.log_info("<" + arg_dict['prv_fname'] + "> prv_fname: is not equal to ::" + return_txt)
                    ui_cmd_obj.error_state = True
                    break
                # lname
                if return_txt == arg_dict['prv_fname']:
                    web_obj = self.builder.find_element(ui_cmd_obj, "//div[@class ='x-grid-item-container']/"
                                                                    "table[" + str(index) + "]/tbody/tr/td[3]")
                    return_txt = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
                if return_txt != arg_dict['prv_lname']:
                    self.logger.log_info("prv_lname: " + str(index) + "::" + return_txt)
                    self.logger.log_info("<" + arg_dict['prv_lname'] + "> prv_lname: is not equal to ::" + return_txt)
                    ui_cmd_obj.error_state = True
                    break
                # email
                if return_txt == arg_dict['prv_lname']:
                    web_obj = self.builder.find_element(ui_cmd_obj, "//div[@class ='x-grid-item-container']/"
                                                                    "table[" + str(index) + "]/tbody/tr/td[4]")
                    return_txt = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
                if return_txt == arg_dict['prv_email']:
                    self.logger.log_info("<" + arg_dict['prv_email'] + "> prv_email: is equal to ::" + return_txt)
                    ui_cmd_obj.error_state = False
                    break
                elif return_txt != arg_dict['prv_email']:
                    self.logger.log_info("<" + arg_dict['prv_email'] + "> prv_email: is not equal to ::" + return_txt)
                    ui_cmd_obj.error_state = True
                    break
            elif return_txt == '':
                ui_cmd_obj.error_state = True
            else:
                self.logger.log_info("<" + arg_dict['prv_uname'] + "> prv_uname: is not equal to ::" + return_txt)
                ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def prv_verify_provisioner_signed(self, ui_cmd_obj, arg_dict):
        self.builder.webdriver_wait_until(ui_cmd_obj, "//div[@class='x-container x-form-fieldcontainer "
                                                      "x-form-item x-form-item-default x-box-item "
                                                      "x-container-default x-vbox-form-item "
                                                      "x-form-item-no-label']", retry=5)
        web_obj = self.builder.find_element(ui_cmd_obj, ".x-form-item-body-default [role] "
                                                        ".x-component-default:nth-of-type(1)",
                                            self.builder.constants.STRATEGY_CSS_SELECTOR)
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_text)
        if return_text != arg_dict['signed_in_prov']:
            self.logger.log_info(return_text + " is not equal to " + arg_dict['signed_in_prov'])
            ui_cmd_obj.error_state = True
            return ui_cmd_obj
        else:
            ui_cmd_obj.error_state = False
        return ui_cmd_obj

    def prv_should_not_exist(self, ui_cmd_obj, arg_dict):
        self.builder.webdriver_wait_until(ui_cmd_obj, "//span[@class ='x-btn-inner x-btn-inner-extr-nav-toolbar-"
                                                      "button-small' and text()='Provisioners']", retry=5)
        self.builder.click(ui_cmd_obj, "//span[@class ='x-btn-inner x-btn-inner-extr-nav-toolbar-button-small' "
                                       "and text()='Provisioners']",
                           self.builder.constants.STRATEGY_XPATH)
        self.spinner_loading(ui_cmd_obj)
        self.builder.click(ui_cmd_obj, "//span[text()='Internal Provisioners']")
        self.spinner_loading(ui_cmd_obj)
        all_count = self.builder.find_elements(ui_cmd_obj, "//div[@class ='x-grid-item-container']/table")
        row_count = len(all_count)
        self.logger.log_info("row_count: " + str(row_count))
        for index in range(1, (row_count + 1)):
            web_obj = self.builder.find_element(ui_cmd_obj, "//div[@class ='x-grid-item-container']"
                                                            "/table[" + str(index) + "]/tbody/tr/td[1]")
            return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
            self.logger.log_info("prv_name: " + str(index) + "::" + return_text)
            if return_text == arg_dict['prv_name']:
                ui_cmd_obj.error_state = True
                self.logger.log_info("<" + arg_dict['prv_name'] + "> prv_name: exists ::" + return_text)
                break
            elif return_text == '':
                ui_cmd_obj.error_state = True
                break
            else:
                self.logger.log_info("<" + arg_dict['prv_name'] + "> prv_name: does not exists ::" + return_text)
                ui_cmd_obj.error_state = False

        return ui_cmd_obj

    def prv_multiple_ot_association(self, ui_cmd_obj, arg_dict):
        self.builder.webdriver_wait_until(ui_cmd_obj, "//span[@class ='x-btn-inner x-btn-inner-extr-nav-toolbar-"
                                                      "button-small' and text()='Provisioners']", retry=5)
        self.builder.click(ui_cmd_obj, "//span[@class ='x-btn-inner x-btn-inner-extr-nav-toolbar-button-small' "
                                       "and text()='Provisioners']",
                           self.builder.constants.STRATEGY_XPATH)
        self.spinner_loading(ui_cmd_obj)
        self.builder.click(ui_cmd_obj, "//a[@class ='x-btn x-unselectable "
                                       "x-box-item x-toolbar-item x-btn-default-toolbar-small'][1]")
        self.spinner_loading(ui_cmd_obj)
        self.builder.enter_text(ui_cmd_obj, arg_dict['prv_uname'], "//input[@name='loginId']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['prv_fname'], "//input[@name='userFirstName']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['prv_lname'], "//input[@name='userLastName']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['prv_pwd'], "//input[@name='userCredential']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['prv_pwd'], "//div[6]/div[@role='presentation']/"
                                                                 "div[@role='presentation']/div[@role='presentation']/"
                                                                 "input[@role='textbox']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['prv_email'], "//input[@name='userEmailAddress']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['prv_email'], "//textarea[@name='comments']")
        if arg_dict['ot_name1'] != "None":
            self.builder.click(ui_cmd_obj, "//label[text() = '" + arg_dict['ot_name1'] + "']")
        if arg_dict['ot_name2'] != "None":
            self.builder.click(ui_cmd_obj, "//label[text() = '" + arg_dict['ot_name2'] + "']")
        if arg_dict['ot_name3'] != "None":
            self.builder.click(ui_cmd_obj, "//label[text() = '" + arg_dict['ot_name3'] + "']")
        if arg_dict['ot_name4'] != "None":
            self.builder.click(ui_cmd_obj, "//label[text() = '" + arg_dict['ot_name4'] + "']")
        if arg_dict['ot_name5'] != "None":
            self.builder.click(ui_cmd_obj, "//label[text() = '" + arg_dict['ot_name5'] + "']")
        self.builder.click(ui_cmd_obj, "//span[text()='Save']")
        self.spinner_loading(ui_cmd_obj)

        return ui_cmd_obj

    def prv_label_validation_login(self, ui_cmd_obj, arg_dict):
        if arg_dict['locale'] == "French":
            self.builder.click(ui_cmd_obj, "//li//a[@onclick=\"javascript:changeLocale('fr')\"]")
        elif arg_dict['locale'] == "Portuguese":
            self.builder.click(ui_cmd_obj, "//li//a[@onclick=\"javascript:changeLocale('pt')\"]")
        elif arg_dict['locale'] == "Spanish":
            self.builder.click(ui_cmd_obj, "//li//a[@onclick=\"javascript:changeLocale('es')\"]")
        elif arg_dict['locale'] == "Deutsch":
            self.builder.click(ui_cmd_obj, "//li//a[@onclick=\"javascript:changeLocale('de')\"]")
        elif arg_dict['locale'] == "Italy":
            self.builder.click(ui_cmd_obj, "//li//a[@onclick=\"javascript:changeLocale('it')\"]")
        elif arg_dict['locale'] == "Swedish":
            self.builder.click(ui_cmd_obj, "//li//a[@onclick=\"javascript:changeLocale('sv')\"]")
        elif arg_dict['locale'] == "Nederlands":
            self.builder.click(ui_cmd_obj, "//li//a[@onclick=\"javascript:changeLocale('nl')\"]")
        elif arg_dict['locale'] == "Russia":
            self.builder.click(ui_cmd_obj, "//li//a[@onclick=\"javascript:changeLocale('ru')\"]")
        elif arg_dict['locale'] == "English":
            self.builder.click(ui_cmd_obj, "//li//a[@onclick=\"javascript:changeLocale('en')\"]")
        web_obj = self.builder.find_element(ui_cmd_obj, "//input[@id='username']")
        user_text = self.base_builder.get_attribute_from_element(ui_cmd_obj, web_obj, "placeholder")
        self.logger.log_info("usertext: " + user_text)
        if user_text != arg_dict['u_label']:
            self.logger.log_info(user_text + " is not equal to " + arg_dict['u_label'])
            ui_cmd_obj.error_state = True
        web_obj = self.builder.find_element(ui_cmd_obj, "//input[@id='password']")
        pwd_text = self.base_builder.get_attribute_from_element(ui_cmd_obj, web_obj, "placeholder")
        self.logger.log_info("pwd_text: " + pwd_text)
        if pwd_text != arg_dict['pwd_label']:
            self.logger.log_info(pwd_text + " is not equal to " + arg_dict['pwd_label'])
            ui_cmd_obj.error_state = True
        web_obj = self.builder.find_element(ui_cmd_obj, "//button[@id='loginBtn']")
        login_button_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info("login_button_text: " + login_button_text)
        if login_button_text != arg_dict['login_label']:
            self.logger.log_info(login_button_text + " is not equal to " + arg_dict['login_label'])
            ui_cmd_obj.error_state = True
        web_obj = self.builder.find_element(ui_cmd_obj, "//a[@id='termsOfUse']")
        terms_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info("termsOfUse text: " + terms_text)
        if terms_text != arg_dict['terms_label']:
            self.logger.log_info(terms_text + " is not equal to " + arg_dict['terms_label'])
            ui_cmd_obj.error_state = True
        web_obj = self.builder.find_element(ui_cmd_obj, "//a[@id='about']")
        about_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info("about_text: " + about_text)
        if about_text != arg_dict['about_label']:
            self.logger.log_info(about_text + " is not equal to " + arg_dict['about_label'])
            ui_cmd_obj.error_state = True
        web_obj = self.builder.find_element(ui_cmd_obj, "//a[@id='downloadAddin']")
        outlook_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info("outlook_text: " + outlook_text)
        if outlook_text != arg_dict['outlook_label']:
            self.logger.log_info(outlook_text + " is not equal to " + arg_dict['outlook_label'])
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def prv_error_invalid_login(self, ui_cmd_obj, arg_dict):
        try:
            web_obj = self.builder.find_element(ui_cmd_obj, "//div[@id='errorString']")
            return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
            self.logger.log_info(return_text)
            if return_text != arg_dict['error_text']:
                self.logger.log_info(return_text + " is not equal to " + arg_dict['error_text'])
                ui_cmd_obj.error_state = True
            return ui_cmd_obj
        except AttributeError:
            return ui_cmd_obj

    def prv_logout(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//div[@role='presentation']/div[@role='presentation']/"
                                       "div[@role='presentation']/div/a[2]")
        log_out = arg_dict['log_out']
        self.logger.log_info(log_out)
        self.builder.click(ui_cmd_obj, "//a/span[text()='" + log_out + "']")

        return ui_cmd_obj

    def prv_label_page_validation_after_login(self, ui_cmd_obj, arg_dict):
        # from popup window
        self.builder.webdriver_wait_until(ui_cmd_obj, "//div[@class='x-container x-form-fieldcontainer "
                                                      "x-form-item x-form-item-default x-box-item "
                                                      "x-container-default x-vbox-form-item "
                                                      "x-form-item-no-label']", retry=5)
        web_obj = self.builder.find_element(ui_cmd_obj, ".x-form-item-body-default .x-box-inner",
                                            self.builder.constants.STRATEGY_CSS_SELECTOR)
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_text)
        return_text = return_text.split("\n")
        if return_text[0].strip() != arg_dict['signed_in_prov'].strip():
            self.logger.log_info(return_text[0] + " is not equal to " + arg_dict['signed_in_prov'].strip())
            ui_cmd_obj.error_state = True
        if return_text[1].strip() != arg_dict['member_of_onboarding_templates'].strip():
            self.logger.log_info(return_text[1] + " is not equal to " + arg_dict['member_of_'
                                                                                 'onboarding_templates'].strip())
            ui_cmd_obj.error_state = True
        if return_text[2].strip() != arg_dict['ot_name'].strip():
            self.logger.log_info(return_text[2] + " is not equal to " + arg_dict['ot_name'].strip())
            ui_cmd_obj.error_state = True
        # bottom logged in user
        web_obj = self.builder.find_element(ui_cmd_obj, "//div[@id='basic-statusbar-innerCt']")
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_text)
        if return_text.strip() != arg_dict['footer_prov'].strip():
            self.logger.log_info(return_text + " is not equal to " + arg_dict['footer_prov'].strip())
            ui_cmd_obj.error_state = True
        # top tool bar
        self.builder.delay(ui_cmd_obj, 5)
        web_obj = self.builder.find_element(ui_cmd_obj, "//div[@id='top-toolbar-innerCt']")
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_text)
        if return_text.strip() != arg_dict['application_name'].strip():
            self.logger.log_info(return_text + " is not equal to " + arg_dict['application_name'])
            ui_cmd_obj.error_state = True
        self.is_element_displayed(ui_cmd_obj, "//div[@role='presentation']/div[@role='presentation']/"
                                              "div[@role='presentation']/div/a[1]",
                                  self.builder.constants.STRATEGY_XPATH)
        self.is_element_displayed(ui_cmd_obj, "//div[@role='presentation']/div[@role='presentation']/"
                                              "div[@role='presentation']/div/a[2]",
                                  self.builder.constants.STRATEGY_XPATH)
        # nav bar
        self.is_element_displayed(ui_cmd_obj, "//img[@src='resources/images/company-logo-nav-expanded.png']",
                                  self.builder.constants.STRATEGY_XPATH)
        self.builder.delay(ui_cmd_obj, 5)
        web_obj = self.builder.find_element(ui_cmd_obj, "//div[@class='x-box-inner x-box-scroller-body-"
                                                        "vertical x-scroller']")
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_text)
        return_text = return_text.split("\n")
        if return_text[0].strip() != arg_dict['guest_users_title'].strip():
            self.logger.log_info(return_text[0].strip() + " is not equal to " + arg_dict['guest_users_title'].strip())
            ui_cmd_obj.error_state = True
        if return_text[1].strip() != arg_dict['devices_title'].strip():
            self.logger.log_info(return_text[1] + " is not equal to " + arg_dict['devices_title'])
            ui_cmd_obj.error_state = True
        self.builder.get_attribute_from_element_and_compare(ui_cmd_obj,
                                                            "//div[@class='x-box-inner x-box-scroller-body-vertical "
                                                            "x-scroller']/div/a[5]", "data-qtip", "Expand Navigation")

        return ui_cmd_obj

    def prv_label_guest_users_page_validation(self, ui_cmd_obj, arg_dict):
        # Guest users body
        self.builder.webdriver_wait_until(ui_cmd_obj, "(//span[@class='x-btn-inner x-btn-inner-extr-nav-"
                                                      "toolbar-button-small'])[1]", retry=5)
        self.builder.click(ui_cmd_obj, "(//span[@class='x-btn-inner x-btn-inner-extr-nav-toolbar-button-small'])[1]")
        self.spinner_loading(ui_cmd_obj)
        web_obj = self.builder.find_element(ui_cmd_obj, "//a[@role='tab']")
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_text)
        if return_text.strip() != arg_dict['guest_users_title'].strip():
            self.logger.log_info(return_text + " is not equal to " + arg_dict['guest_users_title'].strip())
            ui_cmd_obj.error_state = True
        web_obj = self.builder.find_element(ui_cmd_obj,
                                            "[role='grid'] [role='toolbar'] .x-box-scroller-body-horizontal",
                                            self.builder.constants.STRATEGY_CSS_SELECTOR)
        return_text = self.base_builder.get_attribute_from_element(ui_cmd_obj, web_obj, "innerText")
        self.logger.log_info(return_text)
        return_text = return_text.split("\n")
        self.builder.delay(ui_cmd_obj, 5)
        if return_text[0].strip() != arg_dict['button_add'].strip():
            self.logger.log_info("0: " + return_text[0] + " is not equal to " + arg_dict['button_add'])
            ui_cmd_obj.error_state = True
        if return_text[1].strip() != arg_dict['button_edit'].strip():
            self.logger.log_info("1: " + return_text[1] + " is not equal to " + arg_dict['button_edit'])
            ui_cmd_obj.error_state = True
        if return_text[2].strip() != arg_dict['button_delete'].strip():
            self.logger.log_info("2: " + return_text[2] + " is not equal to " + arg_dict['button_delete'])
            ui_cmd_obj.error_state = True
        if return_text[3].strip() != arg_dict['button_extend_expiration'].strip():
            self.logger.log_info("3: " + return_text[3] + " is not equal to " + arg_dict['button_extend_expiration'])
            ui_cmd_obj.error_state = True
        if return_text[4].strip() != arg_dict['button_resend_password'].strip():
            self.logger.log_info("4: " + return_text[4] + " is not equal to " + arg_dict['button_resend_password'])
            ui_cmd_obj.error_state = True
        if return_text[7].strip() != arg_dict['button_print'].strip():
            self.logger.log_info("7: " + return_text[7] + " is not equal to " + arg_dict['button_print'])
            ui_cmd_obj.error_state = True
        if return_text[8].strip() != arg_dict['button_filter'].strip():
            self.logger.log_info("8: " + return_text[8] + " is not equal to " + arg_dict['button_filter'])
            ui_cmd_obj.error_state = True
        # table headers
        self.builder.delay(ui_cmd_obj, 5)
        web_obj = self.builder.find_element(ui_cmd_obj, "//div[@role='columnheader'][1]")
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_text)
        if return_text.strip() != arg_dict['user_name'].strip():
            self.logger.log_info(return_text + " is not equal to " + arg_dict['user_name'])
            ui_cmd_obj.error_state = True
        web_obj = self.builder.find_element(ui_cmd_obj, "//div[@role='columnheader'][2]")
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_text)
        if return_text.strip() != arg_dict['first_name'].strip():
            self.logger.log_info(return_text + " is not equal to " + arg_dict['first_name'])
            ui_cmd_obj.error_state = True
        web_obj = self.builder.find_element(ui_cmd_obj, "//div[@role='columnheader'][3]")
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_text)
        if return_text.strip() != arg_dict['last_name'].strip():
            self.logger.log_info(return_text + " is not equal to " + arg_dict['last_name'])
            ui_cmd_obj.error_state = True
        web_obj = self.builder.find_element(ui_cmd_obj, "//div[@role='columnheader'][4]")
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_text)
        if return_text.strip() != arg_dict['email'].strip():
            self.logger.log_info(return_text + " is not equal to " + arg_dict['email'])
            ui_cmd_obj.error_state = True
        web_obj = self.builder.find_element(ui_cmd_obj, "//div[@role='columnheader'][5]")
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_text)
        if return_text.strip() != arg_dict['sms_address'].strip():
            self.logger.log_info(return_text + " is not equal to " + arg_dict['sms_address'])
            ui_cmd_obj.error_state = True
        web_obj = self.builder.find_element(ui_cmd_obj, "//div[@role='columnheader'][6]")
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_text)
        if return_text.strip() != arg_dict['enabled'].strip():
            self.logger.log_info(return_text + " is not equal to " + arg_dict['enabled'])
            ui_cmd_obj.error_state = True
        web_obj = self.builder.find_element(ui_cmd_obj, "//div[@role='columnheader'][8]")
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_text)
        if return_text.strip() != arg_dict['start_time'].strip():
            self.logger.log_info(return_text + " is not equal to " + arg_dict['start_time'])
            ui_cmd_obj.error_state = True
        self.builder.delay(ui_cmd_obj, 5)
        web_obj = self.builder.find_element(ui_cmd_obj, "//div[@role='columnheader'][9]")
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_text)
        if return_text.strip() != arg_dict['end_time'].strip():
            self.logger.log_info(return_text + " is not equal to " + arg_dict['end_time'])
            ui_cmd_obj.error_state = True
        web_obj = self.builder.find_element(ui_cmd_obj, "//div[@role='columnheader'][10]")
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_text)
        if return_text.strip() != arg_dict['onboarding_template'].strip():
            self.logger.log_info(return_text + " is not equal to " + arg_dict['onboarding_template'])
            ui_cmd_obj.error_state = True
        self.builder.move_cursor(ui_cmd_obj, "//div[@role='columnheader'][10]", self.builder.constants.STRATEGY_XPATH)
        self.builder.delay(ui_cmd_obj, 5)
        web_obj = self.builder.find_element(ui_cmd_obj, "//div[11]//span[@role='presentation']")
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_text)
        if return_text.strip() != arg_dict['provisioner'].strip():
            self.logger.log_info(return_text + " is not equal to " + arg_dict['provisioner'])
            ui_cmd_obj.error_state = True
        web_obj = self.builder.find_element(ui_cmd_obj, "//div[@role='columnheader'][12]")
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_text)
        if return_text.strip() != arg_dict['meeting_id'].strip():
            self.logger.log_info(return_text + " is not equal to " + arg_dict['meeting_id'])
            ui_cmd_obj.error_state = True
        web_obj = self.builder.find_element(ui_cmd_obj, "//div[@role='columnheader'][13]")
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_text)
        if return_text.strip() not in arg_dict['sponsor_name'].strip():
            self.logger.log_info(return_text + " is not equal to " + arg_dict['sponsor_name'])
            ui_cmd_obj.error_state = True
        web_obj = self.builder.find_element(ui_cmd_obj, "//div[@role='columnheader'][14]")
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_text)
        if return_text.strip() not in arg_dict['sponsor_email'].strip():
            self.logger.log_info(return_text + " is not equal to " + arg_dict['sponsor_email'])
            ui_cmd_obj.error_state = True
        web_obj = self.builder.find_element(ui_cmd_obj, "//div[@role='columnheader'][15]")
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_text)
        if return_text.strip() not in arg_dict['sponsor_response'].strip():
            self.logger.log_info(return_text + " is not equal to " + arg_dict['sponsor_response'])
            ui_cmd_obj.error_state = True
        # foot tool bar
        self.builder.delay(ui_cmd_obj, 5)
        web_obj = self.builder.find_element(ui_cmd_obj, "//div[@class='x-toolbar x-docked x-toolbar-extr-toolbar "
                                                        "x-docked-bottom x-toolbar-docked-bottom x-toolbar-extr-"
                                                        "toolbar-docked-bottom x-box-layout-ct x-noborder-rbl']")
        return_foot = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_foot)
        return_foot = return_foot.split("\n")
        if return_foot[0].strip() != arg_dict['users_pagination_msg'].strip():
            self.logger.log_info(return_foot[0] + " is not equal to " + arg_dict['users_pagination_msg'])
            ui_cmd_obj.error_state = True
        if return_foot[1].strip() != arg_dict['page_before_page_text'].strip():
            self.logger.log_info(return_foot[1] + " is not equal to " + arg_dict['page_before_page_text'])
            ui_cmd_obj.error_state = True
        if return_foot[2][:-2].strip() not in arg_dict['page_after_page_text'].strip():
            self.logger.log_info(return_foot[2] + " is not equal to " + arg_dict['page_after_page_text'])
            ui_cmd_obj.error_state = True
        if return_foot[3].strip() not in arg_dict['no_guest_to_display'].strip():
            self.logger.log_info(return_foot[3] + " is not equal to " + arg_dict['no_guest_to_display'])
            ui_cmd_obj.error_state = True
        self.is_element_displayed(ui_cmd_obj, "//div[@role='group']/div[2]/div[@role='presentation']/div[2]",
                                  self.builder.constants.STRATEGY_XPATH)
        self.builder.get_attribute_from_element_and_compare(ui_cmd_obj, "//div[@role='group']/div[2]/div[@role='"
                                                                        "presentation']/a[1]",
                                                            "data-qtip", "First Page")
        self.builder.get_attribute_from_element_and_compare(ui_cmd_obj, "//div[@role='group']/div[2]/div[@role='"
                                                                        "presentation']/a[2]",
                                                            "data-qtip", "Previous Page")
        self.builder.get_attribute_from_element_and_compare(ui_cmd_obj, "//div[@role='group']/div[2]/div[@role='"
                                                                        "presentation']/a[3]",
                                                            "data-qtip", "Next Page")
        self.builder.get_attribute_from_element_and_compare(ui_cmd_obj, "//div[@role='group']/div[2]/div[@role='"
                                                                        "presentation']/a[4]",
                                                            "data-qtip", "Last Page")
        self.is_element_displayed(ui_cmd_obj, "//span[@class='x-btn-icon-el x-btn-icon-el-plain-toolbar-small "
                                              "x-tool-refresh ']", self.builder.constants.STRATEGY_XPATH)

        self.is_element_displayed(ui_cmd_obj, "//div[@role='group']/div[2]/div[@role='presentation']/"
                                              "div[2]/div[@role='presentation']",
                                  self.builder.constants.STRATEGY_XPATH)
        self.is_element_displayed(ui_cmd_obj, "//div[2]/div[@role='presentation']/div[6]",
                                  self.builder.constants.STRATEGY_XPATH)

        return ui_cmd_obj

    def prv_logout_validation(self, ui_cmd_obj, arg_dict):
        # logout
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
        web_obj = self.builder.find_element(ui_cmd_obj, "//div[@class='x-menu-item x-menu-item-default x-box-item']"
                                                        "[3]/a/span")
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_text)
        if return_text != arg_dict['logout']:
            self.logger.log_info(return_text + " is not equal to " + arg_dict['logout'])
            ui_cmd_obj.error_state = True
        self.builder.click(ui_cmd_obj, "//div[@role='presentation']/div[@role='presentation']/"
                                       "div[@role='presentation']/div/a[2]")

        return ui_cmd_obj

    def prv_label_devices_page_validation(self, ui_cmd_obj, arg_dict):
        # Devices body
        self.builder.webdriver_wait_until(ui_cmd_obj, "(//span[@class='x-btn-inner x-btn-inner-extr-nav-"
                                                      "toolbar-button-small'])[2]", retry=5)
        self.builder.click(ui_cmd_obj, "(//span[@class='x-btn-inner x-btn-inner-extr-nav-toolbar-button-small'])[2]")
        self.spinner_loading(ui_cmd_obj)
        web_obj = self.builder.find_element(ui_cmd_obj, "//a[@role='tab']")
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_text)
        if return_text.strip() != arg_dict['device_title'].strip():
            self.logger.log_info(return_text + " is not equal to " + arg_dict['device_title'].strip())
            ui_cmd_obj.error_state = True
        web_obj = self.builder.find_element(ui_cmd_obj,
                                            "[role='grid'] [role='toolbar'] .x-box-scroller-body-horizontal",
                                            self.builder.constants.STRATEGY_CSS_SELECTOR)
        return_text = self.base_builder.get_attribute_from_element(ui_cmd_obj, web_obj, "innerText")
        self.logger.log_info(return_text)
        self.logger.log_info(return_text)
        return_text = return_text.split("\n")
        self.builder.delay(ui_cmd_obj, 5)
        if return_text[0].strip() != arg_dict['button_add'].strip():
            self.logger.log_info(return_text[0] + " is not equal to " + arg_dict['button_add'])
            ui_cmd_obj.error_state = True
        if return_text[1].strip() != arg_dict['button_edit'].strip():
            self.logger.log_info(return_text[1] + " is not equal to " + arg_dict['button_edit'])
            ui_cmd_obj.error_state = True
        if return_text[2].strip() != arg_dict['button_delete'].strip():
            self.logger.log_info(return_text[2] + " is not equal to " + arg_dict['button_delete'])
            ui_cmd_obj.error_state = True
        if return_text[3].strip() != arg_dict['button_extend_expiration'].strip():
            self.logger.log_info(return_text[3] + " is not equal to " + arg_dict['button_extend_expiration'])
            ui_cmd_obj.error_state = True
        if return_text[4].strip() != arg_dict['button_filter'].strip():
            self.logger.log_info(return_text[4] + " is not equal to " + arg_dict['button_filter'])
            ui_cmd_obj.error_state = True
        # table headers
        self.builder.delay(ui_cmd_obj, 5)
        web_obj = self.builder.find_element(ui_cmd_obj, "//div[@role='columnheader'][1]")
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_text)
        if return_text.strip() != arg_dict['mac_address'].strip():
            self.logger.log_info(return_text + " is not equal to " + arg_dict['mac_address'])
            ui_cmd_obj.error_state = True
        web_obj = self.builder.find_element(ui_cmd_obj, "//div[@role='columnheader'][2]")
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_text)
        if return_text.strip() != arg_dict['device_name'].strip():
            self.logger.log_info(return_text + " is not equal to " + arg_dict['device_name'])
            ui_cmd_obj.error_state = True
        web_obj = self.builder.find_element(ui_cmd_obj, "//div[@role='columnheader'][3]")
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_text)
        if return_text.strip() != arg_dict['device_type_group'].strip():
            self.logger.log_info(return_text + " is not equal to " + arg_dict['device_type_group'])
            ui_cmd_obj.error_state = True
        web_obj = self.builder.find_element(ui_cmd_obj, "//div[@role='columnheader'][4]")
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_text)
        if return_text.strip() != arg_dict['device_type'].strip():
            self.logger.log_info(return_text + " is not equal to " + arg_dict['device_type'])
            ui_cmd_obj.error_state = True
        web_obj = self.builder.find_element(ui_cmd_obj, "//div[@role='columnheader'][5]")
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_text)
        if return_text.strip() != arg_dict['source'].strip():
            self.logger.log_info(return_text + " is not equal to " + arg_dict['source'])
            ui_cmd_obj.error_state = True
        web_obj = self.builder.find_element(ui_cmd_obj, "//div[@role='columnheader'][6]")
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_text)
        if return_text.strip() != arg_dict['enabled'].strip():
            self.logger.log_info(return_text + " is not equal to " + arg_dict['enabled'])
            ui_cmd_obj.error_state = True
        web_obj = self.builder.find_element(ui_cmd_obj, "//div[@role='columnheader'][7]")
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_text)
        if return_text.strip() != arg_dict['asset_type'].strip():
            self.logger.log_info(return_text + " is not equal to " + arg_dict['asset_type'])
            ui_cmd_obj.error_state = True
        self.builder.delay(ui_cmd_obj, 5)
        web_obj = self.builder.find_element(ui_cmd_obj, "//div[@role='columnheader'][9]")
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_text)
        if return_text.strip() != arg_dict['start_time'].strip():
            self.logger.log_info(return_text + " is not equal to " + arg_dict['start_time'])
            ui_cmd_obj.error_state = True
        web_obj = self.builder.find_element(ui_cmd_obj, "//div[@role='columnheader'][10]")
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_text)
        if return_text.strip() != arg_dict['end_time'].strip():
            self.logger.log_info(return_text + " is not equal to " + arg_dict['end_time'])
            ui_cmd_obj.error_state = True
        self.builder.move_cursor(ui_cmd_obj, "//div[@role='columnheader'][10]", self.builder.constants.STRATEGY_XPATH)
        self.builder.delay(ui_cmd_obj, 5)
        web_obj = self.builder.find_element(ui_cmd_obj, "//div[@role='columnheader'][11]")
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_text)
        if return_text.strip() != arg_dict['onboarding_template'].strip():
            self.logger.log_info(return_text + " is not equal to " + arg_dict['onboarding_template'])
            ui_cmd_obj.error_state = True
        web_obj = self.builder.find_element(ui_cmd_obj, "//div[@role='columnheader'][12]")
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_text)
        if return_text.strip() != arg_dict['provisioner'].strip():
            self.logger.log_info(return_text + " is not equal to " + arg_dict['provisioner'])
            ui_cmd_obj.error_state = True
        self.builder.delay(ui_cmd_obj, 5)
        # foot tool bar
        self.builder.delay(ui_cmd_obj, 5)
        web_obj = self.builder.find_element(ui_cmd_obj, "[role='group'] .x-box-scroller-body-horizontal",
                                            self.builder.constants.STRATEGY_CSS_SELECTOR)
        return_foot = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_foot)
        return_foot = return_foot.split("\n")
        if return_foot[0].strip() != arg_dict['devices_per_page'].strip():
            self.logger.log_info(return_foot[0] + " is not equal to " + arg_dict['devices_per_page'])
            ui_cmd_obj.error_state = True
        if return_foot[1].strip() != arg_dict['page_before_page_text'].strip():
            self.logger.log_info(return_foot[1] + " is not equal to " + arg_dict['page_before_page_text'])
            ui_cmd_obj.error_state = True
        if return_foot[2][:-2].strip() not in arg_dict['page_after_page_text'].strip():
            self.logger.log_info(return_foot[2] + " is not equal to " + arg_dict['page_after_page_text'])
            ui_cmd_obj.error_state = True
        if return_foot[3].strip() not in arg_dict['no_device_to_display'].strip():
            self.logger.log_info(return_foot[3] + " is not equal to " + arg_dict['no_device_to_display'])
            ui_cmd_obj.error_state = True
        self.is_element_displayed(ui_cmd_obj, "//div[@role='group']/div[2]/div[@role='presentation']/div[2]",
                                  self.builder.constants.STRATEGY_XPATH)
        self.builder.get_attribute_from_element_and_compare(ui_cmd_obj, "//div[@role='group']/div[2]/div[@role='"
                                                                        "presentation']/a[1]",
                                                            "data-qtip", "First Page")
        self.builder.get_attribute_from_element_and_compare(ui_cmd_obj, "//div[@role='group']/div[2]/div[@role='"
                                                                        "presentation']/a[2]",
                                                            "data-qtip", "Previous Page")
        self.builder.get_attribute_from_element_and_compare(ui_cmd_obj, "//div[@role='group']/div[2]/div[@role='"
                                                                        "presentation']/a[3]",
                                                            "data-qtip", "Next Page")
        self.builder.get_attribute_from_element_and_compare(ui_cmd_obj, "//div[@role='group']/div[2]/div[@role='"
                                                                        "presentation']/a[4]",
                                                            "data-qtip", "Last Page")
        self.is_element_displayed(ui_cmd_obj, "//span[@class='x-btn-icon-el x-btn-icon-el-plain-toolbar-small "
                                              "x-tool-refresh ']", self.builder.constants.STRATEGY_XPATH)
        self.is_element_displayed(ui_cmd_obj, "//div[@role='group']/div[2]/div[@role='presentation']/"
                                              "div[2]/div[@role='presentation']",
                                  self.builder.constants.STRATEGY_XPATH)
        self.is_element_displayed(ui_cmd_obj, "//div[2]/div[@role='presentation']/div[6]",
                                  self.builder.constants.STRATEGY_XPATH)

        return ui_cmd_obj

    def spinner_loading(self, ui_cmd_obj):
        self.builder.webdriver_wait_until(ui_cmd_obj, ".x-mask-msg-text", retry=5,
                                          strategy=self.builder.constants.STRATEGY_CSS_SELECTOR,
                                          condition=self.builder.constants.CONDITION_INVISIBILITY_OF_ELEMENT)
        return ui_cmd_obj

    def is_element_displayed(self, ui_cmd_obj, locator, strategy):
        web_obj = self.builder.find_element(ui_cmd_obj, locator, strategy)
        self.base_builder.is_element_displayed(ui_cmd_obj, web_obj)
        self.logger.log_info("I am here: " + str(ui_cmd_obj.return_data))
        if not ui_cmd_obj.return_data:
            ui_cmd_obj.error_state = True
            self.logger.log_info(ui_cmd_obj.error_state)

        return ui_cmd_obj

    def wait_for_page_load_completely(self, ui_cmd_obj):
        self.logger.log_info("waiting for the page to load ...")
        for x in range(1, 25):
            self.base_builder.delay(ui_cmd_obj, 1000)
            self.base_builder.execute_script(ui_cmd_obj, "return document.readyState;")
            self.logger.log_info("page readyState:  " + str(ui_cmd_obj.return_data))
            if ui_cmd_obj.return_data == "complete":
                self.logger.log_info("page loaded completely: ")
                break

        return ui_cmd_obj

    def prv_label_sponsors_page_validation(self, ui_cmd_obj, arg_dict):
        # Sponsors body
        self.builder.webdriver_wait_until(ui_cmd_obj, "(//span[@class='x-btn-inner x-btn-inner-extr-nav-toolbar-"
                                                      "button-small'])[2]", retry=5)
        self.builder.click(ui_cmd_obj, "(//span[@class='x-btn-inner x-btn-inner-extr-nav-toolbar-button-small'])[2]")
        self.builder.delay(ui_cmd_obj, 5)
        web_obj = self.builder.find_element(ui_cmd_obj, "//a[@role='tab']")
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_text)
        if return_text.strip() != arg_dict['sponsor_title'].strip():
            self.logger.log_info(return_text + " is not equal to " + arg_dict['sponsor_title'].strip())
            ui_cmd_obj.error_state = True
        web_obj = self.builder.find_element(ui_cmd_obj,
                                            "[role='grid'] [role='toolbar'] .x-box-scroller-body-horizontal",
                                            self.builder.constants.STRATEGY_CSS_SELECTOR)
        return_text = self.base_builder.get_attribute_from_element(ui_cmd_obj, web_obj, "innerText")
        self.logger.log_info(return_text)
        return_text = return_text.split("\n")
        self.builder.delay(ui_cmd_obj, 5)
        if return_text[0].strip() != arg_dict['button_view'].strip():
            self.logger.log_info(return_text[0] + " is not equal to " + arg_dict['button_view'])
            ui_cmd_obj.error_state = True
        if return_text[1].strip() != arg_dict['button_approve'].strip():
            self.logger.log_info(return_text[1] + " is not equal to " + arg_dict['button_approve'])
            ui_cmd_obj.error_state = True
        if return_text[2].strip() != arg_dict['button_deny_lock'].strip():
            self.logger.log_info(return_text[2] + " is not equal to " + arg_dict['button_deny_lock'])
            ui_cmd_obj.error_state = True
        if return_text[3].strip() != arg_dict['button_extend_expiration'].strip():
            self.logger.log_info(return_text[3] + " is not equal to " + arg_dict['button_extend_expiration'])
            ui_cmd_obj.error_state = True
        if return_text[4].strip() != arg_dict['button_send_email'].strip():
            self.logger.log_info(return_text[4] + " is not equal to " + arg_dict['button_send_email'])
            ui_cmd_obj.error_state = True
        if return_text[5].strip() != arg_dict['button_resend_details'].strip():
            self.logger.log_info(return_text[5] + " is not equal to " + arg_dict['button_resend_details'])
            ui_cmd_obj.error_state = True
        if return_text[7].strip() != arg_dict['button_print'].strip():
            self.logger.log_info(return_text[7] + " is not equal to " + arg_dict['button_print'])
            ui_cmd_obj.error_state = True
        if return_text[8].strip() != arg_dict['button_filter'].strip():
            self.logger.log_info(return_text[8] + " is not equal to " + arg_dict['button_filter'])
            ui_cmd_obj.error_state = True
        # table headers
        self.builder.delay(ui_cmd_obj, 5)
        web_obj = self.builder.find_element(ui_cmd_obj, "//div[@role='columnheader'][1]")
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_text)
        if return_text.strip() != arg_dict['user_name'].strip():
            self.logger.log_info(return_text + " is not equal to " + arg_dict['user_name'])
            ui_cmd_obj.error_state = True
        web_obj = self.builder.find_element(ui_cmd_obj, "//div[@role='columnheader'][2]")
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_text)
        if return_text.strip() != arg_dict['first_name'].strip():
            self.logger.log_info(return_text + " is not equal to " + arg_dict['first_name'])
            ui_cmd_obj.error_state = True
        web_obj = self.builder.find_element(ui_cmd_obj, "//div[@role='columnheader'][3]")
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_text)
        if return_text.strip() != arg_dict['last_name'].strip():
            self.logger.log_info(return_text + " is not equal to " + arg_dict['last_name'])
            ui_cmd_obj.error_state = True
        web_obj = self.builder.find_element(ui_cmd_obj, "//div[@role='columnheader'][4]")
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_text)
        if return_text.strip() != arg_dict['sponsor_response'].strip():
            self.logger.log_info(return_text + " is not equal to " + arg_dict['sponsor_response'])
            ui_cmd_obj.error_state = True
        web_obj = self.builder.find_element(ui_cmd_obj, "//div[@role='columnheader'][5]")
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_text)
        if return_text.strip() != arg_dict['email'].strip():
            self.logger.log_info(return_text + " is not equal to " + arg_dict['email'])
            ui_cmd_obj.error_state = True
        web_obj = self.builder.find_element(ui_cmd_obj, "//div[@role='columnheader'][6]")
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_text)
        if return_text.strip() != arg_dict['sms_address'].strip():
            self.logger.log_info(return_text + " is not equal to " + arg_dict['sms_address'])
            ui_cmd_obj.error_state = True
        web_obj = self.builder.find_element(ui_cmd_obj, "//div[@role='columnheader'][8]")
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_text)
        if return_text.strip() != arg_dict['start_time'].strip():
            self.logger.log_info(return_text + " is not equal to " + arg_dict['start_time'])
            ui_cmd_obj.error_state = True
        self.builder.delay(ui_cmd_obj, 5)
        web_obj = self.builder.find_element(ui_cmd_obj, "//div[@role='columnheader'][9]")
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_text)
        if return_text.strip() != arg_dict['end_time'].strip():
            self.logger.log_info(return_text + " is not equal to " + arg_dict['end_time'])
            ui_cmd_obj.error_state = True
        web_obj = self.builder.find_element(ui_cmd_obj, "//div[@role='columnheader'][10]")
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_text)
        if return_text.strip() != arg_dict['onboarding_template'].strip():
            self.logger.log_info(return_text + " is not equal to " + arg_dict['onboarding_template'])
            ui_cmd_obj.error_state = True
        self.builder.move_cursor(ui_cmd_obj, "//div[@role='columnheader'][11]", self.builder.constants.STRATEGY_XPATH)
        self.builder.delay(ui_cmd_obj, 5)
        web_obj = self.builder.find_element(ui_cmd_obj, "//div[@role='columnheader'][11]")
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_text)
        if return_text.strip() != arg_dict['provisioner'].strip():
            self.logger.log_info(return_text + " is not equal to " + arg_dict['provisioner'])
            ui_cmd_obj.error_state = True
        web_obj = self.builder.find_element(ui_cmd_obj, "//div[12]//span[@role='presentation']")
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_text)
        if return_text.strip() != arg_dict['sponsor_name'].strip():
            self.logger.log_info(return_text + " is not equal to " + arg_dict['sponsor_name'])
            ui_cmd_obj.error_state = True
        web_obj = self.builder.find_element(ui_cmd_obj, "//div[13]//span[@role='presentation']")
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_text)
        if return_text.strip() != arg_dict['sponsor_email'].strip():
            self.logger.log_info(return_text + " is not equal to " + arg_dict['sponsor_email'])
            ui_cmd_obj.error_state = True
        self.builder.delay(ui_cmd_obj, 5)
        # foot tool bar
        self.builder.delay(ui_cmd_obj, 5)
        web_obj = self.builder.find_element(ui_cmd_obj, "[role='group'] .x-box-scroller-body-horizontal",
                                            self.builder.constants.STRATEGY_CSS_SELECTOR)
        return_foot = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_foot)
        return_foot = return_foot.split("\n")
        if return_foot[0].strip() != arg_dict['users_pagination_msg'].strip():
            self.logger.log_info(return_foot[0] + " is not equal to " + arg_dict['users_pagination_msg'])
            ui_cmd_obj.error_state = True
        if return_foot[1].strip() != arg_dict['page_before_page_text'].strip():
            self.logger.log_info(return_foot[1] + " is not equal to " + arg_dict['page_before_page_text'])
            ui_cmd_obj.error_state = True
        if return_foot[2][:-2].strip() not in arg_dict['page_after_page_text'].strip():
            self.logger.log_info(return_foot[2] + " is not equal to " + arg_dict['page_after_page_text'])
            ui_cmd_obj.error_state = True
        self.is_element_displayed(ui_cmd_obj, "//div[@role='group']/div[2]/div[@role='presentation']/div[2]",
                                  self.builder.constants.STRATEGY_XPATH)
        self.builder.get_attribute_from_element_and_compare(ui_cmd_obj, "//div[@role='group']/div[2]/div[@role='"
                                                                        "presentation']/a[1]",
                                                            "data-qtip", "First Page")
        self.builder.get_attribute_from_element_and_compare(ui_cmd_obj, "//div[@role='group']/div[2]/div[@role='"
                                                                        "presentation']/a[2]",
                                                            "data-qtip", "Previous Page")
        self.builder.get_attribute_from_element_and_compare(ui_cmd_obj, "//div[@role='group']/div[2]/div[@role='"
                                                                        "presentation']/a[3]",
                                                            "data-qtip", "Next Page")
        self.builder.get_attribute_from_element_and_compare(ui_cmd_obj, "//div[@role='group']/div[2]/div[@role='"
                                                                        "presentation']/a[4]",
                                                            "data-qtip", "Last Page")
        self.is_element_displayed(ui_cmd_obj, "//span[@class='x-btn-icon-el x-btn-icon-el-plain-"
                                              "toolbar-small x-tool-refresh ']", self.builder.constants.STRATEGY_XPATH)
        self.is_element_displayed(ui_cmd_obj, "//div[@role='group']/div[2]/div[@role='presentation']/"
                                              "div[2]/div[@role='presentation']",
                                  self.builder.constants.STRATEGY_XPATH)
        self.is_element_displayed(ui_cmd_obj, "//div[2]/div[@role='presentation']/div[6]",
                                  self.builder.constants.STRATEGY_XPATH)

        return ui_cmd_obj

    def xmc_enforce_all(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            return super(Gimprovisioners, self).xmc_enforce_all(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()
