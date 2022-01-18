from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as GimguestusersBase
# All imports above this line will be removed after generation.
# User imports must be added below.
import datetime
import re


class Gimguestusers(GimguestusersBase):
    def gu_create_guest_user(self, ui_cmd_obj, arg_dict):
        self.select_ot_from_dropdown(ui_cmd_obj, arg_dict)
        self.builder.enter_text(ui_cmd_obj, arg_dict['gu_fname'], "//input[@name='firstName']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['gu_lname'], "//input[@name='lastName']")
        if arg_dict['gu_uname'] != "None":
            self.builder.enter_text(ui_cmd_obj, arg_dict['gu_uname'], "//input[@name='loginId']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['gu_pwd'], "//input[@name='password']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['gu_email'], "//input[@name='email']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['gu_cellPhone'], "//input[@name='cellPhone']")
        self.builder.click(ui_cmd_obj, "//span[text()='Save']")
        self.wait_for_element_present(ui_cmd_obj, "//span[text()='OK']")
        self.builder.click(ui_cmd_obj, "//span[text()='OK']")
        self.spinner_loading(ui_cmd_obj)

        return ui_cmd_obj

    def gu_guest_user_should_exist(self, ui_cmd_obj, arg_dict):
        self.gu_click_nav_bar(ui_cmd_obj, arg_dict)
        self.filtering_guest_users_based_on_username(ui_cmd_obj, arg_dict)
        all_count = self.builder.find_elements(ui_cmd_obj, "//div[@class ='x-grid-item-container']/table")
        row_count = len(all_count)
        self.logger.log_info("row_count: " + str(row_count))
        for index in range(1, (row_count + 1)):
            web_obj = self.builder.find_element(ui_cmd_obj, "//div[@class ='x-grid-item-container']"
                                                            "/table[" + str(index) + "]/tbody/tr/td[1]")
            return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
            self.logger.log_info("gu_uname: " + str(index) + "::" + return_text)
            # first name
            if return_text == arg_dict['gu_uname']:
                web_obj = self.builder.find_element(ui_cmd_obj, "//div[@class ='x-grid-item-container']/"
                                                                "table[" + str(index) + "]/tbody/tr/td[2]")
                return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
                self.builder.delay(ui_cmd_obj, 2)
                if return_text != arg_dict['gu_fname']:
                    self.logger.log_info("<" + arg_dict['gu_fname'] + "> gu_fname: is not equal to ::" + return_text)
                    ui_cmd_obj.error_state = True
                    break
                # lname
                if return_text == arg_dict['gu_fname']:
                    web_obj = self.builder.find_element(ui_cmd_obj, "//div[@class ='x-grid-item-container']"
                                                                    "/table[" + str(index) + "]/tbody/tr/td[3]")
                    return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
                if return_text != arg_dict['gu_lname']:
                    self.logger.log_info("<" + arg_dict['gu_lname'] + "> gu_lname: is not equal to ::" + return_text)
                    ui_cmd_obj.error_state = True
                    break
                # email
                if return_text == arg_dict['gu_lname']:
                    web_obj = self.builder.find_element(ui_cmd_obj, "//div[@class ='x-grid-item-container']"
                                                                    "/table[" + str(index) + "]/tbody/tr/td[4]")
                    return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
                if return_text != arg_dict['gu_email']:
                    self.logger.log_info("<" + arg_dict['gu_email'] + "> gu_email: is not equal to ::" + return_text)
                    ui_cmd_obj.error_state = True
                    break
                # ot_name
                if return_text == arg_dict['gu_email']:
                    web_obj = self.builder.find_element(ui_cmd_obj, "//div[@class ='x-grid-item-container']"
                                                                    "/table[" + str(index) + "]/tbody/tr/td[10]")
                    return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
                if return_text != arg_dict['gu_otname']:
                    self.logger.log_info("<" + arg_dict['gu_otname'] + "> gu_otname: is not equal to ::" + return_text)
                    ui_cmd_obj.error_state = True
                    break
                # provisioner name
                if return_text == arg_dict['gu_otname']:
                    web_obj = self.builder.find_element(ui_cmd_obj, "//div[@class ='x-grid-item-container']"
                                                                    "/table[" + str(index) + "]/tbody/tr/td[11]")
                    return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
                if return_text == arg_dict['gu_prv']:
                    ui_cmd_obj.error_state = False
                    break
                elif return_text != arg_dict['gu_prv']:
                    self.logger.log_info("<" + arg_dict['gu_prv'] + "> gu_prv: is not equal to ::" + return_text)
                    ui_cmd_obj.error_state = True
                    break
            elif return_text == '':
                ui_cmd_obj.error_state = True
                break
            else:
                self.logger.log_info("<" + arg_dict['gu_uname'] + "> gu_uname: is not equal to ::" + return_text)
                ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def gu_click_nav_bar(self, ui_cmd_obj, arg_dict):
        self.builder.webdriver_wait_until(ui_cmd_obj, "//span[@class='x-btn-inner x-btn-inner-extr-nav-"
                                                      "toolbar-button-small' and text()='Guest Users']", retry=5)
        self.builder.click(ui_cmd_obj, "//span[@class='x-btn-inner x-btn-inner-extr-nav-toolbar-button-small' "
                                       "and text()='Guest Users']")
        self.builder.webdriver_wait_until(ui_cmd_obj, "//span[@class='x-btn-inner x-btn-inner-extr-nav-toolbar-"
                                                      "button-small' and text()='Guest Users']", retry=5)
        self.builder.click(ui_cmd_obj, "//span[@class='x-tab-inner x-tab-inner-extr-main-tab-panel' and "
                                       "text()='Guest Users']")
        self.base_builder.delay(ui_cmd_obj, 1000)

        return ui_cmd_obj

    def gu_table_start_end_time(self, ui_cmd_obj, arg_dict):
        self.gu_click_nav_bar(ui_cmd_obj, arg_dict)
        self.filtering_guest_users_based_on_username(ui_cmd_obj, arg_dict)
        all_count = self.builder.find_elements(ui_cmd_obj, "//div[@class ='x-grid-item-container']/table")
        row_count = len(all_count)
        self.logger.log_info("row_count: " + str(row_count))
        index = 1
        observed_value = ''
        while index < row_count + 1:
            web_obj = self.builder.find_element(ui_cmd_obj, "//div[@class ='x-grid-item-container']/"
                                                            "table[" + str(index) + "]/tbody/tr/td[1]")
            return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
            self.logger.log_info("gu_uname: " + str(index) + "::" + return_text)
            # start Time
            if return_text == arg_dict['gu_uname']:
                web_obj = self.builder.find_element(ui_cmd_obj, "//div[@class ='x-grid-item-container']/"
                                                                "table[" + str(index) + "]/tbody/tr/td[8]")
                return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
            if return_text == arg_dict['gu_str_time']:
                self.logger.log_info("gu_str_time: " + str(index) + "::" + return_text)
            elif return_text == observed_value:
                ui_cmd_obj.error_state = True
            # end time
            if return_text == arg_dict['gu_str_time']:
                web_obj = self.builder.find_element(ui_cmd_obj, "//div[@class ='x-grid-item-container']/"
                                                                "table[" + str(index) + "]/tbody/tr/td[9]")
                return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
            if return_text == arg_dict['gu_end_time']:
                self.logger.log_info("gu_end_time: " + str(index) + "::" + return_text)
                break
            elif return_text == observed_value:
                ui_cmd_obj.error_state = True
                break
            else:
                observed_value = return_text
                index += 1

        return ui_cmd_obj

    def gu_table_sms(self, ui_cmd_obj, arg_dict):
        self.gu_click_nav_bar(ui_cmd_obj, arg_dict)
        self.filtering_guest_users_based_on_username(ui_cmd_obj, arg_dict)
        row_count = self.base_builder.execute_script("return document.getElementsByTagName('table').length")
        self.logger.log_info("row_count: " + str(row_count))
        index = 1
        observed_value = ''
        while index < (row_count + 1):
            web_obj = self.builder.find_element(ui_cmd_obj, "//div[@class ='x-grid-item-container']"
                                                            "/table[" + str(index) + "]/tbody/tr/td[1]")
            return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
            self.logger.log_info("gu_uname: " + str(index) + "::" + return_text)
            # sms
            if return_text == arg_dict['gu_uname']:
                web_obj = self.builder.find_element(ui_cmd_obj, "//div[@class ='x-grid-item-container']"
                                                                "/table[" + str(index) + "]/tbody/tr/td[5]")
                return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
            if return_text == arg_dict['gu_sms']:
                self.logger.log_info("gu_sms: " + str(index) + "::" + return_text)
                break
            elif return_text == observed_value:
                ui_cmd_obj.error_state = True
                break
            else:
                observed_value = return_text
                index += 1

        return ui_cmd_obj

    def gu_table_meeting_id(self, ui_cmd_obj, arg_dict):
        self.gu_click_nav_bar(ui_cmd_obj, arg_dict)
        self.filtering_guest_users_based_on_username(ui_cmd_obj, arg_dict)
        all_count = self.builder.find_elements(ui_cmd_obj, "//div[@class ='x-grid-item-container']/table")
        row_count = len(all_count)
        self.logger.log_info("row_count: " + str(row_count))
        for index in range(1, (row_count + 1)):
            web_obj = self.builder.find_element(ui_cmd_obj, "//div[@class ='x-grid-item-container']"
                                                            "/table[" + str(index) + "]/tbody/tr/td[1]")
            return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
            self.logger.log_info("gu_uname: " + str(index) + "::" + return_text)
            # gu_meeting_id
            if return_text == arg_dict['gu_uname']:
                web_obj = self.builder.find_element(ui_cmd_obj, "//div[@class ='x-grid-item-container']/"
                                                                "table[" + str(index) + "]/tbody/tr/td[12]")
                return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
                self.builder.delay(ui_cmd_obj, 2)
                # meeting id
                if return_text == arg_dict['gu_meeting_id']:
                    ui_cmd_obj.error_state = False
                    break
                elif return_text != arg_dict['gu_meeting_id']:
                    self.logger.log_info(
                        "<" + arg_dict['gu_meeting_id'] + "> gu_meeting_id: is not equal to ::" + return_text)
                    ui_cmd_obj.error_state = True
                    break
            elif return_text == '':
                ui_cmd_obj.error_state = True
                break
            else:
                self.logger.log_info("<" + arg_dict['gu_uname'] + "> gu_uname: is not equal to ::" + return_text)
                ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def gu_table_sponsor_name(self, ui_cmd_obj, arg_dict):
        self.gu_click_nav_bar(ui_cmd_obj, arg_dict)
        self.filtering_guest_users_based_on_username(ui_cmd_obj, arg_dict)
        all_count = self.builder.find_elements(ui_cmd_obj, "//div[@class ='x-grid-item-container']/table")
        row_count = len(all_count)
        self.logger.log_info("row_count: " + str(row_count))
        for index in range(1, (row_count + 1)):
            web_obj = self.builder.find_element(ui_cmd_obj, "//div[@class ='x-grid-item-container']"
                                                            "/table[" + str(index) + "]/tbody/tr/td[1]")
            return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
            self.logger.log_info("gu_uname: " + str(index) + "::" + return_text)
            # gu_sponsor_name
            if return_text == arg_dict['gu_uname']:
                web_obj = self.builder.find_element(ui_cmd_obj, "//div[@class ='x-grid-item-container']/"
                                                                "table[" + str(index) + "]/tbody/tr/td[13]")
                return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
                self.builder.delay(ui_cmd_obj, 2)
                # gu_sponsor_name
                if return_text == arg_dict['gu_sponsor_name']:
                    ui_cmd_obj.error_state = False
                    break
                elif return_text != arg_dict['gu_sponsor_name']:
                    self.logger.log_info(
                        "<" + arg_dict['gu_sponsor_name'] + "> gu_sponsor_name: is not equal to ::" + return_text)
                    ui_cmd_obj.error_state = True
                    break
            elif return_text == '':
                ui_cmd_obj.error_state = True
                break
            else:
                self.logger.log_info("<" + arg_dict['gu_uname'] + "> gu_uname: is not equal to ::" + return_text)
                ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def gu_table_sponsor_email(self, ui_cmd_obj, arg_dict):
        self.gu_click_nav_bar(ui_cmd_obj, arg_dict)
        self.filtering_guest_users_based_on_username(ui_cmd_obj, arg_dict)
        all_count = self.builder.find_elements(ui_cmd_obj, "//div[@class ='x-grid-item-container']/table")
        row_count = len(all_count)
        self.logger.log_info("row_count: " + str(row_count))
        for index in range(1, (row_count + 1)):
            web_obj = self.builder.find_element(ui_cmd_obj, "//div[@class ='x-grid-item-container']"
                                                            "/table[" + str(index) + "]/tbody/tr/td[1]")
            return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
            self.logger.log_info("gu_uname: " + str(index) + "::" + return_text)
            # gu_sponsor_email
            if return_text == arg_dict['gu_uname']:
                web_obj = self.builder.find_element(ui_cmd_obj, "//div[@class ='x-grid-item-container']/"
                                                                "table[" + str(index) + "]/tbody/tr/td[14]")
                return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
                self.builder.delay(ui_cmd_obj, 2)
                # gu_sponsor_email
                if return_text == arg_dict['gu_sponsor_email']:
                    ui_cmd_obj.error_state = False
                    break
                elif return_text != arg_dict['gu_sponsor_email']:
                    self.logger.log_info(
                        "<" + arg_dict['gu_sponsor_email'] + "> gu_sponsor_email: is not equal to ::" + return_text)
                    ui_cmd_obj.error_state = True
                    break
            elif return_text == '':
                ui_cmd_obj.error_state = True
                break
            else:
                self.logger.log_info("<" + arg_dict['gu_uname'] + "> gu_uname: is not equal to ::" + return_text)
                ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def gu_table_sponsor_response(self, ui_cmd_obj, arg_dict):
        self.gu_click_nav_bar(ui_cmd_obj, arg_dict)
        self.filtering_guest_users_based_on_username(ui_cmd_obj, arg_dict)
        all_count = self.builder.find_elements(ui_cmd_obj, "//div[@class ='x-grid-item-container']/table")
        row_count = len(all_count)
        self.logger.log_info("row_count: " + str(row_count))
        for index in range(1, (row_count + 1)):
            web_obj = self.builder.find_element(ui_cmd_obj, "//div[@class ='x-grid-item-container']"
                                                            "/table[" + str(index) + "]/tbody/tr/td[1]")
            return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
            self.logger.log_info("gu_uname: " + str(index) + "::" + return_text)
            # gu_sponsor_response
            if return_text == arg_dict['gu_uname']:
                web_obj = self.builder.find_element(ui_cmd_obj, "//div[@class ='x-grid-item-container']/"
                                                                "table[" + str(index) + "]/tbody/tr/td[15]")
                return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
                self.builder.delay(ui_cmd_obj, 2)
                # gu_sponsor_response
                if return_text == arg_dict['gu_sponsor_response']:
                    ui_cmd_obj.error_state = False
                    break
                elif return_text != arg_dict['gu_sponsor_response']:
                    self.logger.log_info(
                        "<" + arg_dict['gu_sponsor_response'] + "> gu_sponsor_response: is not equal to ::" +
                        return_text)
                    ui_cmd_obj.error_state = True
                    break
            elif return_text == '':
                ui_cmd_obj.error_state = True
                break
            else:
                self.logger.log_info("<" + arg_dict['gu_uname'] + "> gu_uname: is not equal to ::" + return_text)
                ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def gu_duration_val_add_gu(self, ui_cmd_obj, arg_dict):
        self.select_ot_from_dropdown(ui_cmd_obj, arg_dict)
        self.builder.delay(ui_cmd_obj, 5)
        web_obj = self.builder.find_element(ui_cmd_obj, "//span[text()='Duration:']")
        return_text = self.base_builder.is_element_displayed(ui_cmd_obj, web_obj)
        self.logger.log_info(str(return_text))
        if not return_text:
            ui_cmd_obj.error_state = False
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info(ui_cmd_obj.error_state)
        self.builder.click(ui_cmd_obj, "//span[text()='Cancel']")

        return ui_cmd_obj

    def gu_account_on_val_add_gu(self, ui_cmd_obj, arg_dict):
        self.select_ot_from_dropdown(ui_cmd_obj, arg_dict)
        self.builder.delay(ui_cmd_obj, 5)
        web_obj = self.builder.find_element(ui_cmd_obj, "//span[text()='Activate Account On:']")
        return_text = self.base_builder.is_element_displayed(ui_cmd_obj, web_obj)
        self.logger.log_info(return_text)
        if not return_text:
            ui_cmd_obj.error_state = False
        else:
            ui_cmd_obj.error_state = True
        self.logger.log_info(ui_cmd_obj.error_state)
        self.builder.click(ui_cmd_obj, "//span[text()='Cancel']")

        return ui_cmd_obj

    def gu_add(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//span[@role='presentation']//span[text()='Add']")
        self.spinner_loading(ui_cmd_obj)

        return ui_cmd_obj

    def gu_edit(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//span[@role='presentation']//span[text()='Edit']")
        self.spinner_loading(ui_cmd_obj)

        return ui_cmd_obj

    def gu_delete(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//span[@role='presentation']//span[text()='Delete']")
        self.spinner_loading(ui_cmd_obj)

        return ui_cmd_obj

    def gu_ext_exp(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//span[@role='presentation']//span[text()='Extend Expiration']")
        self.spinner_loading(ui_cmd_obj)
        web_obj = self.builder.find_element(ui_cmd_obj, "[role='dialog'] [role='gridcell']:nth-of-type(1) "
                                                        ".x-grid-cell-inner",
                                            self.builder.constants.STRATEGY_CSS_SELECTOR)
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_text)
        if return_text != arg_dict['gu_name']:
            ui_cmd_obj.error_state = True
        else:
            ui_cmd_obj.error_state = False
        web_obj = self.builder.find_element(ui_cmd_obj, "[role='dialog'] [role='gridcell']:nth-of-type(3) "
                                                        ".x-grid-cell-inner",
                                            self.builder.constants.STRATEGY_CSS_SELECTOR)
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_text)
        if return_text != arg_dict['gu_name']:
            ui_cmd_obj.error_state = True
        else:
            ui_cmd_obj.error_state = False
        self.builder.click(ui_cmd_obj, "//span[text()='Close']")

        return ui_cmd_obj

    def gu_resend_pwd(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//span[@role='presentation']//span[text()='Resend Password']")
        self.spinner_loading(ui_cmd_obj)

        return ui_cmd_obj

    def gu_print(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//span[@role='presentation']//span[text()='Print']")
        self.spinner_loading(ui_cmd_obj)

        return ui_cmd_obj

    def gu_load(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//span[@role='presentation']//span[text()='Load']")
        self.spinner_loading(ui_cmd_obj)

        return ui_cmd_obj

    def gu_show_filters(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//span[@role='presentation']//span[text()='Show Filters']")
        self.spinner_loading(ui_cmd_obj)

        return ui_cmd_obj

    def gu_add_success_msg(self, ui_cmd_obj, arg_dict):
        self.select_ot_from_dropdown(ui_cmd_obj, arg_dict)
        self.builder.enter_text(ui_cmd_obj, arg_dict['gu_fname'], "//input[@name='firstName']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['gu_lname'], "//input[@name='lastName']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['gu_uname'], "//input[@name='loginId']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['gu_pwd'], "//input[@name='password']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['gu_email'], "//input[@name='email']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['gu_cellPhone'], "//input[@name='cellPhone']")
        self.builder.click(ui_cmd_obj, "//span[text()='Save']")
        self.wait_for_element_present(ui_cmd_obj, "//span[text()='OK']")
        web_obj = self.builder.find_element(ui_cmd_obj, "//div[@role='alertdialog']/div[1]/"
                                                        "div[@role='presentation']/div/div[1]/"
                                                        "div[@role='presentation']")
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_text)
        if return_text != arg_dict['success_msg']:
            ui_cmd_obj.error_state = True
        else:
            ui_cmd_obj.error_state = False
        web_obj = self.builder.find_element(ui_cmd_obj, ".x-window-text", self.builder.constants.STRATEGY_CSS_SELECTOR)
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(return_text)
        if return_text != arg_dict['un_pwd']:
            ui_cmd_obj.error_state = True
        else:
            ui_cmd_obj.error_state = False
        self.builder.click(ui_cmd_obj, "//span[text()='OK']")
        self.spinner_loading(ui_cmd_obj)

        return ui_cmd_obj

    def gu_show_load_data(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//span[@role='presentation']//span[text()='Load']")
        self.spinner_loading(ui_cmd_obj)

        return ui_cmd_obj

    def gu_user_name_should_not_exist(self, ui_cmd_obj, arg_dict):
        self.gu_click_nav_bar(ui_cmd_obj, arg_dict)
        all_count = self.builder.find_elements(ui_cmd_obj, "//div[@class ='x-grid-item-container']/table")
        row_count = len(all_count)
        self.logger.log_info("row_count: " + str(row_count))
        for index in range(1, (row_count + 1)):
            web_obj = self.builder.find_element(ui_cmd_obj, "//div[@class ='x-grid-item-container']"
                                                            "/table[" + str(index) + "]/tbody/tr/td[1]")
            return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
            self.logger.log_info("gu_username: " + str(index) + "::" + return_text)
            if return_text == arg_dict['gu_username']:
                ui_cmd_obj.error_state = True
                self.logger.log_info("<" + arg_dict['gu_username'] + "> gu_username: exists ::" + return_text)
                break
            elif return_text == '':
                ui_cmd_obj.error_state = True
                break
            else:
                self.logger.log_info("<" + arg_dict['gu_username'] + "> gu_username: does not exists ::" + return_text)
                ui_cmd_obj.error_state = False

        return ui_cmd_obj

    def gu_validation_username_field(self, ui_cmd_obj, arg_dict):
        self.select_ot_from_dropdown(ui_cmd_obj, arg_dict)
        self.builder.delay(ui_cmd_obj, 5)
        web_obj = self.builder.find_element(ui_cmd_obj, "//input[@name='loginId']")
        return_text = web_obj.is_enabled()
        self.logger.log_info(return_text)
        web_txt = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        self.logger.log_info(web_txt)
        if arg_dict['enabled_or_disabled'] == "enabled" and return_text is True:
            self.logger.log_info("1 :enabled: " + arg_dict['enabled_or_disabled'])
            ui_cmd_obj.error_state = False
        elif arg_dict['enabled_or_disabled'] == "disabled" and return_text is False:
            self.logger.log_info("2 :disabled: " + arg_dict['enabled_or_disabled'])
            ui_cmd_obj.error_state = False
        else:
            ui_cmd_obj.error_state = True
        self.builder.click(ui_cmd_obj, "//span[text()='Cancel']")

        return ui_cmd_obj

    def gu_create_gu_username_field(self, ui_cmd_obj, arg_dict):
        self.select_ot_from_dropdown(ui_cmd_obj, arg_dict)
        self.builder.enter_text(ui_cmd_obj, arg_dict['gu_fname'], "//input[@name='firstName']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['gu_lname'], "//input[@name='lastName']")
        if arg_dict['gu_uname'] != "None":
            self.builder.enter_text(ui_cmd_obj, arg_dict['gu_uname'], "//input[@name='loginId']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['gu_pwd'], "//input[@name='password']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['gu_email'], "//input[@name='email']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['gu_cellPhone'], "//input[@name='cellPhone']")
        self.builder.click(ui_cmd_obj, "//span[text()='Save']")
        self.builder.delay(ui_cmd_obj, 1000)
        web_text = self.builder.get_attribute_from_element(ui_cmd_obj, ".x-window-text", "innerHTML",
                                                           self.builder.constants.STRATEGY_CSS_SELECTOR)
        self.logger.log_info(web_text)
        web_text = web_text.split("<br>")
        username = web_text[0].split(":")
        un = username[1].strip()
        self.logger.log_info(un)
        self.builder.click(ui_cmd_obj, "//span[text()='OK']")
        self.spinner_loading(ui_cmd_obj)
        self.gu_click_nav_bar(ui_cmd_obj, arg_dict)
        self.filtering_guest_users_based_on_username(ui_cmd_obj, arg_dict)
        all_count = self.builder.find_elements(ui_cmd_obj, "//div[@class ='x-grid-item-container']/table")
        row_count = len(all_count)
        self.logger.log_info("row_count: " + str(row_count))
        for index in range(1, (row_count + 1)):
            web_obj = self.builder.find_element(ui_cmd_obj, "//div[@class ='x-grid-item-container']"
                                                            "/table[" + str(index) + "]/tbody/tr/td[1]")
            return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
            self.logger.log_info("gu_uname: " + str(index) + "::" + return_text)
            if return_text == un:
                ui_cmd_obj.error_state = False
                self.logger.log_info("<" + un + "> gu_uname: exists ::" + return_text)
                break
            elif return_text == '':
                ui_cmd_obj.error_state = True
                break
            else:
                self.logger.log_info("<" + un + "> gu_uname: does not exists ::" + return_text)
                ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def gu_expired_gu(self, ui_cmd_obj, arg_dict):
        self.gu_click_nav_bar(ui_cmd_obj, arg_dict)
        self.filtering_guest_users_based_on_username(ui_cmd_obj, arg_dict)
        all_count = self.builder.find_elements(ui_cmd_obj, "//div[@class ='x-grid-item-container']/table")
        row_count = len(all_count)
        self.logger.log_info("row_count: " + str(row_count))
        for index in range(1, (row_count + 1)):
            web_obj = self.builder.find_element(ui_cmd_obj, "//div[@class ='x-grid-item-container']"
                                                            "/table[" + str(index) + "]/tbody/tr/td[1]")
            return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
            self.logger.log_info("gu_uname: " + str(index) + "::" + return_text)
            # gu_meeting_id
            if return_text == arg_dict['gu_uname']:
                web_obj = self.builder.find_element(ui_cmd_obj, "//div[@class ='x-grid-item-container']/"
                                                                "table[" + str(index) + "]/tbody/tr/td[10]")
                return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
                self.builder.delay(ui_cmd_obj, 2)
                # meeting id
                if return_text == arg_dict['gu_expired_end_time']:
                    ui_cmd_obj.error_state = False
                    break
                elif return_text != arg_dict['gu_expired_end_time']:
                    self.logger.log_info(
                        "<" + arg_dict['gu_expired_end_time'] + "> gu_expired_time: is not equal to ::" + return_text)
                    ui_cmd_obj.error_state = True
                    break
            elif return_text == '':
                ui_cmd_obj.error_state = True
                break
            else:
                self.logger.log_info("<" + arg_dict['gu_uname'] + "> gu_uname: is not equal to ::" + return_text)
                ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def gu_create_gu_validate_un_pwd(self, ui_cmd_obj, arg_dict):
        return_text = ""
        self.select_ot_from_dropdown(ui_cmd_obj, arg_dict)
        self.builder.enter_text(ui_cmd_obj, arg_dict['gu_fname'], "//input[@name='firstName']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['gu_lname'], "//input[@name='lastName']")
        if arg_dict['username_type'] == "guest_defined":
            self.logger.log_info("selected option: " + str(arg_dict['username_type']))
            self.builder.enter_text(ui_cmd_obj, arg_dict['gu_uname'], "//input[@name='loginId']")
            self.builder.enter_text(ui_cmd_obj, arg_dict['email'], "//input[@name='email']")
            self.builder.enter_text(ui_cmd_obj, arg_dict['cellPhone'], "//input[@name='cellPhone']")
        elif arg_dict['username_type'] == "random":
            self.logger.log_info("selected option: " + str(arg_dict['username_type']))
            self.builder.enter_text(ui_cmd_obj, arg_dict['email'], "//input[@name='email']")
            self.builder.enter_text(ui_cmd_obj, arg_dict['cellPhone'], "//input[@name='cellPhone']")
            self.builder.delay(ui_cmd_obj, 2)
            web_obj = self.builder.find_element(ui_cmd_obj, "//input[@name='loginId']",
                                                self.builder.constants.STRATEGY_XPATH)
            self.base_builder.execute_script(ui_cmd_obj, "arguments[0].scrollIntoView(true);", web_obj)
            self.builder.delay(ui_cmd_obj, 5)
            return_text = self.builder.get_attribute_from_element(ui_cmd_obj, "//input[@name='loginId']", "value",
                                                                  self.builder.constants.STRATEGY_XPATH)
            total_length = len(return_text)
            if total_length != arg_dict['un_length']:
                ui_cmd_obj.error_state = True
            count_lc = 0
            count_uc = 0
            count_nu = 0
            count_unlisted = 0
            for i in return_text:
                if i.islower():
                    count_lc = count_lc + 1
                elif i.isupper():
                    count_uc = count_uc + 1
                elif i.isdigit():
                    count_nu = count_nu + 1
                else:
                    count_unlisted = count_unlisted + 1
            if arg_dict['un_case_type'] == "lower":
                self.logger.log_info("selected option: " + str(arg_dict['un_case_type']))
                if count_lc != 0 and count_uc == 0 and count_nu == 0:
                    ui_cmd_obj.error_state = False
                else:
                    ui_cmd_obj.error_state = True
            elif arg_dict['un_case_type'] == "upper":
                self.logger.log_info("selected option: " + str(arg_dict['un_case_type']))
                if count_lc == 0 and count_uc != 0 and count_nu == 0:
                    ui_cmd_obj.error_state = False
                else:
                    ui_cmd_obj.error_state = True
            elif arg_dict['un_case_type'] == "number":
                self.logger.log_info("selected option: " + str(arg_dict['un_case_type']))
                if count_lc == 0 and count_uc == 0 and count_nu != 0:
                    ui_cmd_obj.error_state = False
                else:
                    ui_cmd_obj.error_state = True
            elif arg_dict['un_case_type'] == "lower_upper":
                self.logger.log_info("selected option: " + str(arg_dict['un_case_type']))
                if count_lc != 0 and count_uc != 0 and count_nu == 0:
                    ui_cmd_obj.error_state = False
                else:
                    ui_cmd_obj.error_state = True
            elif arg_dict['un_case_type'] == "upper_number":
                self.logger.log_info("selected option: " + str(arg_dict['un_case_type']))
                if count_lc == 0 and count_uc != 0 and count_nu != 0:
                    ui_cmd_obj.error_state = False
                else:
                    ui_cmd_obj.error_state = True
            elif arg_dict['un_case_type'] == "lower_number":
                self.logger.log_info("selected option: " + str(arg_dict['un_case_type']))
                if count_lc != 0 and count_uc == 0 and count_nu != 0:
                    ui_cmd_obj.error_state = False
                else:
                    ui_cmd_obj.error_state = True
            elif arg_dict['un_case_type'] == "all":
                self.logger.log_info("selected option: " + str(arg_dict['un_case_type']))
                if (count_lc and count_uc and count_nu) != 0:
                    ui_cmd_obj.error_state = False
                else:
                    ui_cmd_obj.error_state = True
        elif arg_dict['username_type'] == "firstnamelastname":
            self.logger.log_info("selected option: " + str(arg_dict['username_type']))
            self.gu_create_gu_validate_un_pwd_firstnamelastname(ui_cmd_obj, arg_dict)
        elif arg_dict['username_type'] == "firstinitiallastname":
            self.logger.log_info("selected option: " + str(arg_dict['username_type']))
            self.gu_create_gu_validate_un_pwd_firstnamelastname(ui_cmd_obj, arg_dict)
        elif arg_dict['username_type'] == "email":
            self.logger.log_info("selected option: " + str(arg_dict['username_type']))
            web_obj = self.builder.find_element(ui_cmd_obj, "//span[contains(text(),'Used As Username')]",
                                                self.builder.constants.STRATEGY_XPATH)
            return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
            self.logger.log_info(return_text)
            if return_text not in "Email(Used As Username) *:":
                self.logger.log_info("email return text is not equal: " + return_text)
                ui_cmd_obj.error_state = True
            self.builder.enter_text(ui_cmd_obj, arg_dict['email'], "//input[@name='email']")
            self.builder.enter_text(ui_cmd_obj, arg_dict['cellPhone'], "//input[@name='cellPhone']")
        elif arg_dict['username_type'] == "mobile":
            self.logger.log_info("selected option: " + str(arg_dict['username_type']))
            self.builder.enter_text(ui_cmd_obj, arg_dict['email'], "//input[@name='email']")
            web_obj = self.builder.find_element(ui_cmd_obj, "//span[contains(text(),'Used As Username')]",
                                                self.builder.constants.STRATEGY_XPATH)
            return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
            if return_text != "Mobile(Used As Username): *:":
                self.logger.log_info("mobile return text is not equal: " + return_text)
                ui_cmd_obj.error_state = True
            self.builder.enter_text(ui_cmd_obj, arg_dict['cellPhone'], "//input[@name='cellPhone']")
        if arg_dict['pwd_type'] == "guest_defined":
            self.logger.log_info("selected pwd_type option: " + str(arg_dict['pwd_type']))
            self.builder.enter_text(ui_cmd_obj, arg_dict['gu_pwd'], "//input[@name='password']")
            if arg_dict['confirm_pwd'] == "confirm_pwd":
                self.builder.enter_text(ui_cmd_obj, arg_dict['gu_pwd'], "//input[@name='confirmPassword']")
        self.builder.click(ui_cmd_obj, "//span[text()='Save']")
        self.wait_for_element_present(ui_cmd_obj, "//span[text()='OK']")
        web_text = self.builder.get_attribute_from_element(ui_cmd_obj, ".x-window-text", "innerHTML",
                                                           self.builder.constants.STRATEGY_CSS_SELECTOR)
        self.logger.log_info(web_text)
        web_text = web_text.split("<br>")
        username = web_text[0].split(":")
        un = username[1].strip()
        self.logger.log_info(un)
        password = web_text[1].split(":")
        pwd = password[1].strip()
        self.logger.log_info(pwd)
        if arg_dict['username_type'] == "random":
            if un != return_text:
                ui_cmd_obj.error_state = True
        elif arg_dict['username_type'] == "guest_defined":
            if un != arg_dict['gu_uname']:
                ui_cmd_obj.error_state = True
        elif arg_dict['username_type'] == "email":
            if un != arg_dict['email']:
                ui_cmd_obj.error_state = True
        elif arg_dict['username_type'] == "mobile":
            if un != arg_dict['cellPhone']:
                ui_cmd_obj.error_state = True
        pwd_length = len(pwd)
        if arg_dict['pwd_range_or_number'] == "number":
            self.logger.log_info("selected pwd_range_or_number option: " + str(arg_dict['pwd_range_or_number']))
            if pwd_length != arg_dict['pwd_length']:
                ui_cmd_obj.error_state = True
        elif arg_dict['pwd_range_or_number'] == "range":
            self.logger.log_info("selected pwd_range_or_number option: " + str(arg_dict['pwd_range_or_number']))
            pwd_list = arg_dict['pwd_length'].split("-")
            if int(pwd_list[0]) > pwd_length or pwd_length > int(pwd_list[1]):
                ui_cmd_obj.error_state = True
        pwd_count_lc = 0
        pwd_count_uc = 0
        pwd_count_nu = 0
        pwd_count_sp = 0
        for i in pwd:
            if i.islower():
                pwd_count_lc = pwd_count_lc + 1
            elif i.isupper():
                pwd_count_uc = pwd_count_uc + 1
            elif i.isdigit():
                pwd_count_nu = pwd_count_nu + 1
            else:
                pwd_count_sp = pwd_count_sp + 1
                # Password Validation
        if arg_dict['pwd_type'] == "guest_defined" or arg_dict['pwd_type'] == "random":
            self.logger.log_info("selected pwd_type option: " + str(arg_dict['pwd_type']))
            if arg_dict['pwd_case_type'] == "lower":
                self.logger.log_info("selected pwd_case_type option: " + str(arg_dict['pwd_case_type']))
                if pwd_count_lc != 0 and pwd_count_uc == 0 and pwd_count_nu == 0 and pwd_count_sp == 0:
                    ui_cmd_obj.error_state = False
                else:
                    ui_cmd_obj.error_state = True
            elif arg_dict['pwd_case_type'] == "upper":
                self.logger.log_info("selected pwd_case_type option: " + str(arg_dict['pwd_case_type']))
                if pwd_count_lc == 0 and pwd_count_uc != 0 and pwd_count_nu == 0 and pwd_count_sp == 0:
                    ui_cmd_obj.error_state = False
                else:
                    ui_cmd_obj.error_state = True
            elif arg_dict['pwd_case_type'] == "number":
                self.logger.log_info("selected pwd_case_type option: " + str(arg_dict['pwd_case_type']))
                if pwd_count_lc == 0 and pwd_count_uc == 0 and pwd_count_nu != 0 and pwd_count_sp == 0:
                    ui_cmd_obj.error_state = False
                else:
                    ui_cmd_obj.error_state = True
            elif arg_dict['pwd_case_type'] == "special":
                self.logger.log_info("selected pwd_case_type option: " + str(arg_dict['pwd_case_type']))
                if pwd_count_lc == 0 and pwd_count_uc == 0 and pwd_count_nu == 0 and pwd_count_sp != 0:
                    ui_cmd_obj.error_state = False
                else:
                    ui_cmd_obj.error_state = True
            elif arg_dict['pwd_case_type'] == "lower_upper":
                self.logger.log_info("selected pwd_case_type option: " + str(arg_dict['pwd_case_type']))
                if pwd_count_lc != 0 and pwd_count_uc != 0 and pwd_count_nu == 0 and pwd_count_sp == 0:
                    ui_cmd_obj.error_state = False
                else:
                    ui_cmd_obj.error_state = True
            elif arg_dict['pwd_case_type'] == "lower_number":
                self.logger.log_info("selected pwd_case_type option: " + str(arg_dict['pwd_case_type']))
                if pwd_count_lc != 0 and pwd_count_uc == 0 and pwd_count_nu != 0 and pwd_count_sp == 0:
                    ui_cmd_obj.error_state = False
                else:
                    ui_cmd_obj.error_state = True
            elif arg_dict['pwd_case_type'] == "lower_special":
                self.logger.log_info("selected pwd_case_type option: " + str(arg_dict['pwd_case_type']))
                if pwd_count_lc != 0 and pwd_count_uc == 0 and pwd_count_nu == 0 and pwd_count_sp != 0:
                    ui_cmd_obj.error_state = False
                else:
                    ui_cmd_obj.error_state = True
            elif arg_dict['pwd_case_type'] == "upper_number":
                self.logger.log_info("selected pwd_case_type option: " + str(arg_dict['pwd_case_type']))
                if pwd_count_lc == 0 and pwd_count_uc != 0 and pwd_count_nu != 0 and pwd_count_sp == 0:
                    ui_cmd_obj.error_state = False
                else:
                    ui_cmd_obj.error_state = True
            elif arg_dict['pwd_case_type'] == "upper_special":
                self.logger.log_info("selected pwd_case_type option: " + str(arg_dict['pwd_case_type']))
                if pwd_count_lc == 0 and pwd_count_uc != 0 and pwd_count_nu == 0 and pwd_count_sp != 0:
                    ui_cmd_obj.error_state = False
                else:
                    ui_cmd_obj.error_state = True
            elif arg_dict['pwd_case_type'] == "number_special":
                self.logger.log_info("selected pwd_case_type option: " + str(arg_dict['pwd_case_type']))
                if pwd_count_lc == 0 and pwd_count_uc == 0 and pwd_count_nu != 0 and pwd_count_sp != 0:
                    ui_cmd_obj.error_state = False
                else:
                    ui_cmd_obj.error_state = True
            elif arg_dict['pwd_case_type'] == "lower_upper_number":
                self.logger.log_info("selected pwd_case_type option: " + str(arg_dict['pwd_case_type']))
                if pwd_count_lc == 0 and pwd_count_uc != 0 and pwd_count_nu != 0 and pwd_count_sp == 0:
                    ui_cmd_obj.error_state = False
                else:
                    ui_cmd_obj.error_state = True
            elif arg_dict['pwd_case_type'] == "lower_upper_special":
                self.logger.log_info("selected pwd_case_type option: " + str(arg_dict['pwd_case_type']))
                if pwd_count_lc != 0 and pwd_count_uc != 0 and pwd_count_nu == 0 and pwd_count_sp != 0:
                    ui_cmd_obj.error_state = False
                else:
                    ui_cmd_obj.error_state = True
            elif arg_dict['pwd_case_type'] == "lower_number_special":
                self.logger.log_info("selected pwd_case_type option: " + str(arg_dict['pwd_case_type']))
                if pwd_count_lc != 0 and pwd_count_uc == 0 and pwd_count_nu != 0 and pwd_count_sp != 0:
                    ui_cmd_obj.error_state = False
                else:
                    ui_cmd_obj.error_state = True
            elif arg_dict['pwd_case_type'] == "upper_number_special":
                self.logger.log_info("selected pwd_case_type option: " + str(arg_dict['pwd_case_type']))
                if pwd_count_lc == 0 and pwd_count_uc != 0 and pwd_count_nu != 0 and pwd_count_sp != 0:
                    ui_cmd_obj.error_state = False
                else:
                    ui_cmd_obj.error_state = True
            elif arg_dict['pwd_case_type'] == "all":
                self.logger.log_info("selected pwd_case_type option: " + str(arg_dict['pwd_case_type']))
                if pwd_count_lc != 0 and pwd_count_uc != 0 and pwd_count_nu != 0 and pwd_count_sp != 0:
                    ui_cmd_obj.error_state = False
                else:
                    ui_cmd_obj.error_state = True
            if pwd != arg_dict['gu_pwd']:
                ui_cmd_obj.error_state = True
        elif arg_dict['pwd_type'] == "username":
            self.logger.log_info("selected pwd_type option: " + str(arg_dict['pwd_type']))
            if pwd != arg_dict['gu_uname']:
                ui_cmd_obj.error_state = True
        elif arg_dict['pwd_type'] == "email":
            self.logger.log_info("selected pwd_type option: " + str(arg_dict['pwd_type']))
            if pwd != arg_dict['email']:
                ui_cmd_obj.error_state = True
        elif arg_dict['pwd_type'] == "static":
            self.logger.log_info("selected pwd_type option: " + str(arg_dict['pwd_type']))
            self.logger.log_info("password is already created as static password")
        self.builder.delay(ui_cmd_obj, 5)
        self.builder.click(ui_cmd_obj, "//span[text()='OK']")
        self.spinner_loading(ui_cmd_obj)
        n = 0
        while n <= 1:
            if n == 1:
                arg_dict["browser"] = "chrome"
                self.builder.open_web_page(ui_cmd_obj, arg_dict["browser"], arg_dict["gim_url"], implicit_wait=1,
                                           delete_all_cookies=True)
                self.wait_for_page_load_completely(ui_cmd_obj)
                self.builder.enter_text(ui_cmd_obj, arg_dict['admin_un'], 'username',
                                        self.builder.constants.STRATEGY_NAME)
                self.builder.click(ui_cmd_obj, 'password', self.builder.constants.STRATEGY_NAME)
                self.builder.enter_text(ui_cmd_obj, arg_dict['admin_pwd'], 'password',
                                        self.builder.constants.STRATEGY_NAME)
                self.builder.click(ui_cmd_obj, "//button[@type='submit']")
                self.spinner_loading(ui_cmd_obj)
            self.builder.click(ui_cmd_obj, "//span[@class='x-btn-inner x-btn-inner-extr-nav-toolbar-button-small' and "
                                           "text()='Guest Users']")
            self.spinner_loading(ui_cmd_obj)
            self.builder.click(ui_cmd_obj, "(//span[text()='Guest Users'])[2]")
            self.spinner_loading(ui_cmd_obj)
            self.builder.click(ui_cmd_obj, "//span[text()='Show Filter']", self.builder.constants.STRATEGY_XPATH)
            self.spinner_loading(ui_cmd_obj)
            self.builder.click(ui_cmd_obj, "//label[contains(text(),'Specify Filter')]",
                               self.builder.constants.STRATEGY_XPATH)
            self.builder.click(ui_cmd_obj, "[valign] [role='presentation']:nth-of-type(3) .x-form-trigger-wrap-default "
                                           "[role='presentation']:nth-of-type(2)",
                               self.builder.constants.STRATEGY_CSS_SELECTOR)
            self.builder.click(ui_cmd_obj, "//li[text()='Username']", self.builder.constants.STRATEGY_XPATH)
            self.builder.click(ui_cmd_obj, "[valign] [role='presentation']:nth-of-type(5) .x-form-trigger-wrap-default "
                                           "[role='presentation']:nth-of-type(2)",
                               self.builder.constants.STRATEGY_CSS_SELECTOR)
            self.builder.click(ui_cmd_obj, "//li[text()='Equals']", self.builder.constants.STRATEGY_XPATH)
            self.builder.enter_text(ui_cmd_obj, un, "//input[@name='textValue']")
            self.builder.click(ui_cmd_obj, "//span[text()='Apply Filter']", self.builder.constants.STRATEGY_XPATH)
            self.spinner_loading(ui_cmd_obj)
            all_count = self.builder.find_elements(ui_cmd_obj, "//div[@class ='x-grid-item-container']/table")
            row_count = len(all_count)
            if row_count == 0:
                ui_cmd_obj.error_state = True
            else:
                for index in range(1, (row_count + 1)):
                    web_obj = self.builder.find_element(ui_cmd_obj, "//div[@class ='x-grid-item-container']"
                                                                    "/table[" + str(index) + "]/tbody/tr/td[1]")
                    return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
                    self.logger.log_info("gu_uname: " + str(index) + "::" + return_text)
                    if return_text == un:
                        ui_cmd_obj.error_state = False
                        self.logger.log_info("<" + un + "> gu_uname: exists ::" + return_text)
                        break
                    elif return_text == '':
                        ui_cmd_obj.error_state = True
                        break
                    else:
                        self.logger.log_info("<" + un + "> gu_uname: does not exists ::" + return_text)
                        ui_cmd_obj.error_state = True

            self.builder.delay(ui_cmd_obj, 5)
            self.builder.click(ui_cmd_obj, "//div[@role='presentation']/div[@role='presentation']/"
                                           "div[@role='presentation']/div/a[2]")
            self.builder.delay(ui_cmd_obj, 2)
            self.builder.click(ui_cmd_obj, "//a/span[text()='Logout']")
            n = n + 1

        return ui_cmd_obj

    def gu_create_gu_validate_acc_validity(self, ui_cmd_obj, arg_dict):
        self.select_ot_from_dropdown(ui_cmd_obj, arg_dict)
        if arg_dict['change_nochan'] == "change":
            list_duration = re.findall('[0-9]+', arg_dict['change_time'])
            list_durationunit = re.findall('[a-z]+', arg_dict['change_time'])
            self.builder.delay(ui_cmd_obj, 5)
            web_element = self.builder.find_element(ui_cmd_obj, "//input[@name='durationUnits']")
            self.base_builder.execute_script(ui_cmd_obj, "arguments[0].scrollIntoView(true);", web_element)
            self.builder.delay(ui_cmd_obj, 5)
            self.base_builder.click(ui_cmd_obj, web_element)
            web_items = self.builder.find_elements(ui_cmd_obj, "(//ul[@role='listbox'])[2]/li[@role='option']")
            for item in web_items:
                if item.get_attribute("innerText") == list_durationunit[0]:
                    item.click()
                    self.builder.delay(ui_cmd_obj, 5)
                    break
            timestamp = self.builder.get_attribute_from_element(ui_cmd_obj, "//input[@name='duration']", "value")
            if timestamp != list_duration[0]:
                self.builder.delay(ui_cmd_obj, 5)
                self.builder.enter_text(ui_cmd_obj, list_duration[0], "//input[@name='duration']",
                                        self.builder.constants.STRATEGY_XPATH, clear_existing=True)
        self.builder.enter_text(ui_cmd_obj, arg_dict['gu_fname'], "//input[@name='firstName']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['gu_lname'], "//input[@name='lastName']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['gu_uname'], "//input[@name='loginId']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['pwd'], "//input[@name='password']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['gu_email'], "//input[@name='email']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['cellphone'], "//input[@name='cellPhone']")
        self.builder.click(ui_cmd_obj, "//span[text()='Save']", self.builder.constants.STRATEGY_XPATH)
        self.wait_for_element_present(ui_cmd_obj, "//span[text()='OK']")
        if arg_dict['error_no_error'] == "error":
            web_obj_text = self.builder.get_attribute_from_element(ui_cmd_obj, "//div[@role='alertdialog']/div[1]",
                                                                   "textContent")
            self.builder.click(ui_cmd_obj, "//span[text()='OK']")
            self.spinner_loading(ui_cmd_obj)
            self.builder.click(ui_cmd_obj, "(//span[text()='Cancel'])[1]")
            self.spinner_loading(ui_cmd_obj)
            if web_obj_text != "Error":
                ui_cmd_obj.error_state = True
        else:
            web_obj_text = self.builder.get_attribute_from_element(ui_cmd_obj, "(//div[@class='x-title-text "
                                                                               "x-title-text-default "
                                                                               "x-title-item'])[2]", "textContent")

            if web_obj_text != "Successful Guest Creation":
                ui_cmd_obj.error_state = True
            else:
                self.builder.click(ui_cmd_obj, "//span[text()='OK']", self.builder.constants.STRATEGY_XPATH)
                self.spinner_loading(ui_cmd_obj)
            self.builder.click(ui_cmd_obj, "//span[text()='Show Filter']", self.builder.constants.STRATEGY_XPATH)
            self.spinner_loading(ui_cmd_obj)
            self.builder.click(ui_cmd_obj, "//label[contains(text(),'Specify Filter')]",
                               self.builder.constants.STRATEGY_XPATH)
            self.builder.click(ui_cmd_obj, "[valign] [role='presentation']:nth-of-type(3) .x-form-trigger-wrap-default "
                                           "[role='presentation']:nth-of-type(2)",
                               self.builder.constants.STRATEGY_CSS_SELECTOR)
            self.builder.click(ui_cmd_obj, "//li[text()='Username']", self.builder.constants.STRATEGY_XPATH)
            self.builder.click(ui_cmd_obj, "[valign] [role='presentation']:nth-of-type(5) .x-form-trigger-wrap-default "
                                           "[role='presentation']:nth-of-type(2)",
                               self.builder.constants.STRATEGY_CSS_SELECTOR)
            self.builder.click(ui_cmd_obj, "//li[text()='Equals']", self.builder.constants.STRATEGY_XPATH)
            self.builder.enter_text(ui_cmd_obj, arg_dict['gu_uname'], "//input[@name='textValue']")
            self.builder.click(ui_cmd_obj, "//span[text()='Apply Filter']", self.builder.constants.STRATEGY_XPATH)
            self.spinner_loading(ui_cmd_obj)
            all_count = self.builder.find_elements(ui_cmd_obj, "//div[@class ='x-grid-item-container']/table")
            row_count = len(all_count)
            if row_count == 0:
                ui_cmd_obj.error_state = True
            else:
                for index in range(1, (row_count + 1)):
                    web_obj = self.builder.find_element(ui_cmd_obj, "//div[@class ='x-grid-item-container']"
                                                                    "/table[" + str(index) + "]/tbody/tr/td[1]")
                    return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
                    self.logger.log_info("gu_uname: " + str(index) + "::" + return_text)
                    if return_text == arg_dict['gu_uname']:
                        ui_cmd_obj.error_state = False
                        self.logger.log_info("<" + arg_dict['gu_uname'] + "> gu_uname: exists ::" + return_text)
                        start_time_obj = self.builder.find_element(ui_cmd_obj, "//div[@class ='x-grid-item-container']"
                                                                               "/table[" + str(index) + "]/"
                                                                                                        "tbody/tr/"
                                                                                                        "td[8]")
                        start_time = start_time_obj.get_attribute('innerText')
                        end_time_obj = self.builder.find_element(ui_cmd_obj, "//div[@class ='x-grid-item-container']"
                                                                             "/table[" + str(index) + "]/"
                                                                                                      "tbody/tr/"
                                                                                                      "td[9]")
                        end_time = end_time_obj.get_attribute('innerText')
                        date_time_format = '%Y/%m/%d %I:%M:%S %p %Z'
                        diff = datetime.datetime.strptime(end_time, date_time_format) - datetime.datetime.strptime(
                            start_time, date_time_format)
                        self.logger.log_info("Difference:" + str(diff))
                        self.logger.log_info("Days:" + str(diff.days))
                        self.logger.log_info("Seconds:" + str(diff.total_seconds()))
                        if arg_dict['change_nochan'] == "change":
                            if "days" in arg_dict["change_time"]:
                                time_d = int(arg_dict['change_time'].strip("days"))
                                total_time = time_d * 60 * 60 * 24
                                if diff.total_seconds() != total_time:
                                    ui_cmd_obj.error_state = True
                            elif "hours" in arg_dict["change_time"]:
                                time_d = int(arg_dict['change_time'].strip("hours"))
                                total_time = time_d * 60 * 60
                                if diff.total_seconds() != total_time:
                                    ui_cmd_obj.error_state = True
                            elif "minutes" in arg_dict["change_time"]:
                                time_d = (arg_dict['change_time']).strip("minutes")
                                self.logger.log_info("TIme:" + time_d)
                                time_d = int(time_d)
                                total_time = time_d * 60
                                self.logger.log_info("total time in sec:" + str(total_time))
                                if diff.total_seconds() != total_time:
                                    ui_cmd_obj.error_state = True
                        else:
                            if "days" in arg_dict["time"]:
                                time_d = int(arg_dict['time'].strip("days"))
                                total_time = time_d * 60 * 60 * 24
                                if diff.total_seconds() != total_time:
                                    ui_cmd_obj.error_state = True
                            elif "hrs" in arg_dict["time"]:
                                time_d = int(arg_dict['time'].strip("hrs"))
                                total_time = time_d * 60 * 60
                                if diff.total_seconds() != total_time:
                                    ui_cmd_obj.error_state = True
                            elif "min" in arg_dict["time"]:
                                time_d = int(arg_dict['time'].strip("min"))
                                total_time = time_d * 60
                                self.logger.log_info("total time in sec:" + str(total_time))
                                if diff.total_seconds() != total_time:
                                    ui_cmd_obj.error_state = True
                        break
                    elif return_text == '':
                        ui_cmd_obj.error_state = True
                        break
                    else:
                        self.logger.log_info(
                            "<" + arg_dict['gu_uname'] + "> gu_uname: does not exists ::" + return_text)
                        ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def gu_create_gu_validate_un_pwd_sponsor(self, ui_cmd_obj, arg_dict):
        self.builder.webdriver_wait_until(ui_cmd_obj, "//input[@name='userFirstName']", retry=5)
        self.builder.enter_text(ui_cmd_obj, arg_dict['gu_fname'], "//input[@name='userFirstName']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['gu_lname'], "//input[@name='userLastName']")
        self.is_cookies_exists(ui_cmd_obj)
        self.builder.enter_text(ui_cmd_obj, arg_dict['email'], "//input[@name='userEmail']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['cellPhone'], "//input[@name='userCellPhone']")
        return_text_un = ""
        if arg_dict['username_type'] == "guest_defined":
            self.builder.enter_text(ui_cmd_obj, arg_dict['gu_uname'], "//input[@name='username']")
        elif arg_dict['username_type'] == "random":
            web_obj = self.builder.find_element(ui_cmd_obj, "//input[@name='username']",
                                                self.builder.constants.STRATEGY_XPATH)
            return_text_un = web_obj.get_attribute('value')
            total_length = len(return_text_un)
            if total_length != arg_dict['un_length']:
                ui_cmd_obj.error_state = True
            count_lc = 0
            count_uc = 0
            count_nu = 0
            count_unlisted = 0
            for i in return_text_un:
                if i.islower():
                    count_lc = count_lc + 1
                elif i.isupper():
                    count_uc = count_uc + 1
                elif i.isdigit():
                    count_nu = count_nu + 1
                else:
                    count_unlisted = count_unlisted + 1
            if arg_dict['un_case_type'] == "lower":
                if count_lc != 0 and count_uc == 0 and count_nu == 0:
                    ui_cmd_obj.error_state = False
                else:
                    ui_cmd_obj.error_state = True
            elif arg_dict['un_case_type'] == "upper":
                if count_lc == 0 and count_uc != 0 and count_nu == 0:
                    ui_cmd_obj.error_state = False
                else:
                    ui_cmd_obj.error_state = True
            elif arg_dict['un_case_type'] == "number":
                if count_lc == 0 and count_uc == 0 and count_nu != 0:
                    ui_cmd_obj.error_state = False
                else:
                    ui_cmd_obj.error_state = True
            elif arg_dict['un_case_type'] == "lower_upper":
                if count_lc != 0 and count_uc != 0 and count_nu == 0:
                    ui_cmd_obj.error_state = False
                else:
                    ui_cmd_obj.error_state = True
            elif arg_dict['un_case_type'] == "upper_number":
                if count_lc == 0 and count_uc != 0 and count_nu != 0:
                    ui_cmd_obj.error_state = False
                else:
                    ui_cmd_obj.error_state = True
            elif arg_dict['un_case_type'] == "lower_number":
                if count_lc != 0 and count_uc == 0 and count_nu != 0:
                    ui_cmd_obj.error_state = False
                else:
                    ui_cmd_obj.error_state = True
            elif arg_dict['un_case_type'] == "all":
                if (count_lc and count_uc and count_nu) != 0:
                    ui_cmd_obj.error_state = False
                else:
                    ui_cmd_obj.error_state = True
        elif arg_dict['username_type'] == "firstnamelastname":
            return_text = self.builder.get_attribute_from_element(ui_cmd_obj, "//input[@name='username']", "value")
            if arg_dict['prefix_suffix'] == "no_pre_suf":
                if return_text[0].isdigit():
                    ui_cmd_obj.error_state = True
            elif arg_dict['prefix_suffix'] == "prefix":
                if arg_dict['random_static'] == "random":
                    if arg_dict['number'] == 1:
                        if not return_text[0].isdigit():
                            ui_cmd_obj.error_state = True
                    elif arg_dict['number'] == 2:
                        if not return_text[0:2].isdigit():
                            ui_cmd_obj.error_state = True
                    elif arg_dict['number'] == 3:
                        if not return_text[0:3].isdigit():
                            ui_cmd_obj.error_state = True
                elif arg_dict['random_static'] == "static":
                    if not return_text.startswith("arg_dict['static']"):
                        ui_cmd_obj.error_state = True
            elif arg_dict['prefix_suffix'] == "suffix":
                if arg_dict['random_static'] == "random":
                    if arg_dict['number'] == 0:
                        if return_text[0].isdigit():
                            ui_cmd_obj.error_state = True
                    elif arg_dict['number'] == 1:
                        if not return_text[-1].isdigit():
                            ui_cmd_obj.error_state = True
                    elif arg_dict['number'] == 2:
                        if not return_text[-2:].isdigit():
                            ui_cmd_obj.error_state = True
                    elif arg_dict['number'] == 3:
                        if not return_text[-3:].isdigit():
                            ui_cmd_obj.error_state = True
                elif arg_dict['random_static'] == "static":
                    if not return_text.endswith("arg_dict['static']"):
                        ui_cmd_obj.error_state = True
            if return_text.find("arg_dict['gu_fname']" + "arg_dict['gu_lname']"):
                ui_cmd_obj.error_state = False
            else:
                ui_cmd_obj.error_state = True
        elif arg_dict['username_type'] == "firstinitiallastname":
            return_text = self.builder.get_attribute_from_element(ui_cmd_obj, "//input[@name='username']", "value")
            if arg_dict['prefix_suffix'] == "no_pre_suf":
                if return_text[0].isdigit():
                    ui_cmd_obj.error_state = True
            elif arg_dict['prefix_suffix'] == "prefix":
                if arg_dict['random_static'] == "random":
                    if arg_dict['number'] == 1:
                        if not return_text[0].isdigit():
                            ui_cmd_obj.error_state = True
                    elif arg_dict['number'] == 2:
                        if not return_text[0:2].isdigit():
                            ui_cmd_obj.error_state = True
                    elif arg_dict['number'] == 3:
                        if not return_text[0:3].isdigit():
                            ui_cmd_obj.error_state = True
                elif arg_dict['random_static'] == "static":
                    if not return_text.startswith("arg_dict['static']"):
                        ui_cmd_obj.error_state = True
            elif arg_dict['prefix_suffix'] == "suffix":
                if arg_dict['random_static'] == "random":
                    if arg_dict['number'] == 0:
                        if return_text[0].isdigit():
                            ui_cmd_obj.error_state = True
                    elif arg_dict['number'] == 1:
                        if not return_text[-1].isdigit():
                            ui_cmd_obj.error_state = True
                    elif arg_dict['number'] == 2:
                        if not return_text[-2:].isdigit():
                            ui_cmd_obj.error_state = True
                    elif arg_dict['number'] == 3:
                        if not return_text[-3:].isdigit():
                            ui_cmd_obj.error_state = True
                elif arg_dict['random_static'] == "static":
                    if not return_text.endswith("arg_dict['static']"):
                        ui_cmd_obj.error_state = True
            if return_text.find("arg_dict['gu_fname'][0] + arg_dict['gu_lname']"):
                ui_cmd_obj.error_state = False
            else:
                ui_cmd_obj.error_state = True
        if arg_dict['pwd_type'] == "guest_defined":
            self.builder.enter_text(ui_cmd_obj, arg_dict['gu_pwd'], "//input[@name='userPassword']")
            if arg_dict['confirm_pwd'] == "confirm_pwd":
                self.builder.enter_text(ui_cmd_obj, arg_dict['gu_pwd'], "(//input[@type='password'])[2]")
        if arg_dict['self_sponsor'] == "self":
            self.builder.click(ui_cmd_obj, "//span[text()='Submit']")
            self.builder.delay(ui_cmd_obj, 5)
        elif arg_dict['self_sponsor'] == "sponsor":
            self.builder.enter_text(ui_cmd_obj, arg_dict['gu_fname'], "//input[@name='sponsorFirstName']")
            self.builder.enter_text(ui_cmd_obj, arg_dict['gu_lname'], "//input[@name='sponsorLastName']")
            self.builder.enter_text(ui_cmd_obj, arg_dict['email'], "//div[2]/div[@role='presentation']/div"
                                                                   "[5]/div[@role='presentation']/div[@role="
                                                                   "'presentation']//input[@role='textbox']")
            self.builder.click(ui_cmd_obj, "(//input[@readonly='readonly'])[3]",
                               self.builder.constants.STRATEGY_XPATH)
            self.builder.click(ui_cmd_obj, "//li[@role='option']", self.builder.constants.STRATEGY_XPATH)
            self.builder.enter_text(ui_cmd_obj, "1234567890", "//input[@name='sponsorCellPhone']")
            self.builder.click(ui_cmd_obj, "//span[text()='Request Approval']",
                               self.builder.constants.STRATEGY_XPATH)
            self.builder.webdriver_wait_until(ui_cmd_obj, "//span[text()='OK']", retry=5)
        web_text = self.builder.get_attribute_from_element(ui_cmd_obj, ".x-window-text", "outerText",
                                                           self.builder.constants.STRATEGY_CSS_SELECTOR)
        web_text = web_text.split("\n")
        un = ""
        pwd = ""
        if arg_dict['self_sponsor'] == "self":
            username = web_text[0].split(":")
            un = username[1].strip()
            password = web_text[1].split(":")
            pwd = password[1].strip()
        elif arg_dict['self_sponsor'] == "sponsor":
            username = web_text[2].split(":")
            un = username[1].strip()
            password = web_text[3].split(":")
            pwd = password[1].strip()
        if arg_dict['username_type'] == "random":
            if un != return_text_un:
                ui_cmd_obj.error_state = True
        elif arg_dict['username_type'] == "guest_defined":
            if un != arg_dict['gu_uname']:
                ui_cmd_obj.error_state = True
        elif arg_dict['username_type'] == "email":
            if un != arg_dict['email']:
                ui_cmd_obj.error_state = True
        elif arg_dict['username_type'] == "mobile":
            if un != arg_dict['cellPhone']:
                ui_cmd_obj.error_state = True
        pwd_length = len(pwd)
        if arg_dict['pwd_range_or_number'] == "number":
            if pwd_length != arg_dict['pwd_length']:
                ui_cmd_obj.error_state = True
        elif arg_dict['pwd_range_or_number'] == "range":
            pwd_list = arg_dict['pwd_length'].split("-")
            if pwd_list[0] > pwd_length or pwd_length > pwd_list[1]:
                ui_cmd_obj.error_state = True
        pwd_count_lc = 0
        pwd_count_uc = 0
        pwd_count_nu = 0
        pwd_count_sp = 0
        for i in pwd:
            if i.islower():
                pwd_count_lc = pwd_count_lc + 1
            elif i.isupper():
                pwd_count_uc = pwd_count_uc + 1
            elif i.isdigit():
                pwd_count_nu = pwd_count_nu + 1
            else:
                pwd_count_sp = pwd_count_sp + 1
        # Password Validation
        if arg_dict['pwd_type'] == "guest_defined" or arg_dict['pwd_type'] == "random":
            if arg_dict['pwd_case_type'] == "lower":
                if pwd_count_lc != 0 and pwd_count_uc == 0 and pwd_count_nu == 0 and pwd_count_sp == 0:
                    ui_cmd_obj.error_state = False
                else:
                    ui_cmd_obj.error_state = True
            elif arg_dict['pwd_case_type'] == "upper":
                if pwd_count_lc == 0 and pwd_count_uc != 0 and pwd_count_nu == 0 and pwd_count_sp == 0:
                    ui_cmd_obj.error_state = False
                else:
                    ui_cmd_obj.error_state = True
            elif arg_dict['pwd_case_type'] == "number":
                if pwd_count_lc == 0 and pwd_count_uc == 0 and pwd_count_nu != 0 and pwd_count_sp == 0:
                    ui_cmd_obj.error_state = False
                else:
                    ui_cmd_obj.error_state = True
            elif arg_dict['pwd_case_type'] == "special":
                if pwd_count_lc == 0 and pwd_count_uc == 0 and pwd_count_nu == 0 and pwd_count_sp != 0:
                    ui_cmd_obj.error_state = False
                else:
                    ui_cmd_obj.error_state = True
            elif arg_dict['pwd_case_type'] == "lower_upper":
                if pwd_count_lc != 0 and pwd_count_uc != 0 and pwd_count_nu == 0 and pwd_count_sp == 0:
                    ui_cmd_obj.error_state = False
                else:
                    ui_cmd_obj.error_state = True
            elif arg_dict['pwd_case_type'] == "lower_number":
                if pwd_count_lc != 0 and pwd_count_uc == 0 and pwd_count_nu != 0 and pwd_count_sp == 0:
                    ui_cmd_obj.error_state = False
                else:
                    ui_cmd_obj.error_state = True
            elif arg_dict['pwd_case_type'] == "lower_special":
                if pwd_count_lc != 0 and pwd_count_uc == 0 and pwd_count_nu == 0 and pwd_count_sp != 0:
                    ui_cmd_obj.error_state = False
                else:
                    ui_cmd_obj.error_state = True
            elif arg_dict['pwd_case_type'] == "upper_number":
                if pwd_count_lc == 0 and pwd_count_uc != 0 and pwd_count_nu != 0 and pwd_count_sp == 0:
                    ui_cmd_obj.error_state = False
                else:
                    ui_cmd_obj.error_state = True
            elif arg_dict['pwd_case_type'] == "upper_special":
                if pwd_count_lc == 0 and pwd_count_uc != 0 and pwd_count_nu == 0 and pwd_count_sp != 0:
                    ui_cmd_obj.error_state = False
                else:
                    ui_cmd_obj.error_state = True
            elif arg_dict['pwd_case_type'] == "number_special":
                if pwd_count_lc == 0 and pwd_count_uc == 0 and pwd_count_nu != 0 and pwd_count_sp != 0:
                    ui_cmd_obj.error_state = False
                else:
                    ui_cmd_obj.error_state = True
            elif arg_dict['pwd_case_type'] == "lower_upper_number":
                if pwd_count_lc == 0 and pwd_count_uc != 0 and pwd_count_nu != 0 and pwd_count_sp == 0:
                    ui_cmd_obj.error_state = False
                else:
                    ui_cmd_obj.error_state = True
            elif arg_dict['pwd_case_type'] == "lower_upper_special":
                if pwd_count_lc != 0 and pwd_count_uc != 0 and pwd_count_nu == 0 and pwd_count_sp != 0:
                    ui_cmd_obj.error_state = False
                else:
                    ui_cmd_obj.error_state = True
            elif arg_dict['pwd_case_type'] == "lower_number_special":
                if pwd_count_lc != 0 and pwd_count_uc == 0 and pwd_count_nu != 0 and pwd_count_sp != 0:
                    ui_cmd_obj.error_state = False
                else:
                    ui_cmd_obj.error_state = True
            elif arg_dict['pwd_case_type'] == "upper_number_special":
                if pwd_count_lc == 0 and pwd_count_uc != 0 and pwd_count_nu != 0 and pwd_count_sp != 0:
                    ui_cmd_obj.error_state = False
                else:
                    ui_cmd_obj.error_state = True
            elif arg_dict['pwd_case_type'] == "all":
                if pwd_count_lc != 0 and pwd_count_uc != 0 and pwd_count_nu != 0 and pwd_count_sp != 0:
                    ui_cmd_obj.error_state = False
                else:
                    ui_cmd_obj.error_state = True
            if pwd != arg_dict['gu_pwd']:
                ui_cmd_obj.error_state = True
        elif arg_dict['pwd_type'] == "username":
            if pwd != arg_dict['gu_uname']:
                ui_cmd_obj.error_state = True
        elif arg_dict['pwd_type'] == "email":
            if pwd != arg_dict['email']:
                ui_cmd_obj.error_state = True
        self.builder.delay(ui_cmd_obj, 5)
        self.builder.click(ui_cmd_obj, "//span[text()='OK']")
        self.builder.delay(ui_cmd_obj, 5)
        n = 1
        while n <= 1:
            if n == 1:
                arg_dict["browser"] = "chrome"
                self.builder.open_web_page(ui_cmd_obj, arg_dict["browser"], arg_dict["gim_url"], implicit_wait=1,
                                           delete_all_cookies=True)
                self.wait_for_page_load_completely(ui_cmd_obj)
                self.builder.enter_text(ui_cmd_obj, "admin", 'username', self.builder.constants.STRATEGY_NAME)
                self.builder.click(ui_cmd_obj, 'password', self.builder.constants.STRATEGY_NAME)
                self.builder.enter_text(ui_cmd_obj, "admin", 'password',
                                        self.builder.constants.STRATEGY_NAME)
                self.builder.click(ui_cmd_obj, "//button[@type='submit']")
                self.spinner_loading(ui_cmd_obj)

            self.builder.click(ui_cmd_obj, "//span[@class='x-btn-inner x-btn-inner-extr-nav-toolbar-button-small' and "
                                           "text()='Guest Users']")
            self.spinner_loading(ui_cmd_obj)
            self.builder.click(ui_cmd_obj, "(//span[text()='Guest Users'])[2]")
            self.spinner_loading(ui_cmd_obj)
            self.builder.click(ui_cmd_obj, "//span[text()='Show Filter']", self.builder.constants.STRATEGY_XPATH)
            self.spinner_loading(ui_cmd_obj)
            self.builder.click(ui_cmd_obj, "//label[contains(text(),'Specify Filter')]",
                               self.builder.constants.STRATEGY_XPATH)
            self.builder.click(ui_cmd_obj, "[valign] [role='presentation']:nth-of-type(3) .x-form-trigger-wrap-default "
                                           "[role='presentation']:nth-of-type(2)",
                               self.builder.constants.STRATEGY_CSS_SELECTOR)
            self.builder.click(ui_cmd_obj, "//li[text()='Username']", self.builder.constants.STRATEGY_XPATH)
            self.builder.click(ui_cmd_obj, "[valign] [role='presentation']:nth-of-type(5) .x-form-trigger-wrap-default "
                                           "[role='presentation']:nth-of-type(2)",
                               self.builder.constants.STRATEGY_CSS_SELECTOR)
            self.builder.click(ui_cmd_obj, "//li[text()='Equals']", self.builder.constants.STRATEGY_XPATH)
            self.builder.enter_text(ui_cmd_obj, un, "//input[@name='textValue']")
            self.builder.click(ui_cmd_obj, "//span[text()='Apply Filter']", self.builder.constants.STRATEGY_XPATH)
            self.spinner_loading(ui_cmd_obj)
            all_count = self.builder.find_elements(ui_cmd_obj, "//div[@class ='x-grid-item-container']/table")
            row_count = len(all_count)
            if row_count == 0:
                ui_cmd_obj.error_state = True
            else:
                for index in range(1, (row_count + 1)):
                    web_obj = self.builder.find_element(ui_cmd_obj, "//div[@class ='x-grid-item-container']"
                                                                    "/table[" + str(index) + "]/tbody/tr/td[1]")
                    return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
                    self.logger.log_info("gu_uname: " + str(index) + "::" + return_text)
                    if return_text == un:
                        ui_cmd_obj.error_state = False
                        self.logger.log_info("<" + un + "> gu_uname: exists ::" + return_text)
                        break
                    elif return_text == '':
                        ui_cmd_obj.error_state = True
                        break
                    else:
                        self.logger.log_info("<" + un + "> gu_uname: does not exists ::" + return_text)
                        ui_cmd_obj.error_state = True
            n = n + 1

        return ui_cmd_obj

    def gu_summary_validation(self, ui_cmd_obj, arg_dict):
        self.gu_click_nav_bar(ui_cmd_obj, arg_dict)
        self.filtering_guest_users_based_on_username(ui_cmd_obj, arg_dict)
        all_count = self.builder.find_elements(ui_cmd_obj, "//div[@class ='x-grid-item-container']/table")
        row_count = len(all_count)
        for index in range(1, (row_count + 1)):
            web_obj = self.builder.find_element(ui_cmd_obj, "//div[@class ='x-grid-item-container']"
                                                            "/table[" + str(index) + "]/tbody/tr/td[1]")
            return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
            self.logger.log_info("gu_uname: " + str(index) + "::" + return_text)
            if return_text == arg_dict['gu_uname']:
                self.builder.double_click(ui_cmd_obj, "//div[@class ='x-grid-item-container']"
                                                      "/table[" + str(index) + "]/tbody/tr/td[1]",
                                          self.builder.constants.STRATEGY_XPATH)
                self.spinner_loading(ui_cmd_obj)
                if arg_dict['gu_summary_value'] == 'Verizon Wireless':
                    self.builder.get_text_from_element_and_compare(ui_cmd_obj,
                                                                   "//span[@class='x-form-item-label-text' and text() "
                                                                   "=" + "'" + arg_dict['gu_summary_key'] + "'" +
                                                                   "]/following::div[1]", "XFinity Mobile")
                    self.logger.log_info("if condition: ")
                    break
                else:
                    self.builder.get_text_from_element_and_compare(ui_cmd_obj,
                                                                   "//span[@class='x-form-item-label-text' and text() "
                                                                   "=" + "'" + arg_dict['gu_summary_key'] + "'" +
                                                                   "]/following::div[1]", arg_dict['gu_summary_value'])
                    self.logger.log_info("else condition: ")
                break
            elif return_text == '':
                ui_cmd_obj.error_state = True
                break
            else:
                self.logger.log_info("<" + arg_dict['gu_uname'] + "> gu_uname: is not equal to ::" + return_text)
                ui_cmd_obj.error_state = True
        self.builder.click(ui_cmd_obj, "Close", self.builder.constants.STRATEGY_LINK_TEXT)
        self.base_builder.delay(ui_cmd_obj, 2000)

        return ui_cmd_obj

    def gu_notification_email_sms_un_pwd(self, ui_cmd_obj, arg_dict):
        try:
            self.is_element_displayed(ui_cmd_obj, ".x-tab-default-top:nth-of-type(3) [data-ref='btnInnerEl']",
                                      self.builder.constants.STRATEGY_CSS_SELECTOR)
            self.builder.click(ui_cmd_obj, "//a[3]/span[@role='presentation']/span[@role='presentation']"
                                           "/span[text()='Guest Users']")
            self.spinner_loading(ui_cmd_obj)
            self.is_element_selected(ui_cmd_obj, "//input[@name='userManageRight']",
                                     self.builder.constants.STRATEGY_XPATH)
            self.is_element_displayed(ui_cmd_obj, "//fieldset[@aria-label='Guest Notification field set']",
                                      self.builder.constants.STRATEGY_XPATH)
            if arg_dict['gu_notification'] == "email":
                self.set_check_box_value(ui_cmd_obj, "(//input[@name='guestNotification'])[1]",
                                         self.builder.constants.STRATEGY_XPATH, True)
                self.set_check_box_value(ui_cmd_obj, "(//input[@name='guestNotification'])[2]",
                                         self.builder.constants.STRATEGY_XPATH, False)
                self.set_check_box_value(ui_cmd_obj, "(//input[@name='guestNotification'])[3]",
                                         self.builder.constants.STRATEGY_XPATH, False)
                self.set_check_box_value(ui_cmd_obj, "(//input[@name='guestNotification'])[4]",
                                         self.builder.constants.STRATEGY_XPATH, False)
                self.builder.delay(ui_cmd_obj, 5)
            if arg_dict['gu_notification'] == "sms":
                self.set_check_box_value(ui_cmd_obj, "(//input[@name='guestNotification'])[1]",
                                         self.builder.constants.STRATEGY_XPATH, False)
                self.set_check_box_value(ui_cmd_obj, "(//input[@name='guestNotification'])[2]",
                                         self.builder.constants.STRATEGY_XPATH, True)
                self.set_check_box_value(ui_cmd_obj, "(//input[@name='guestNotification'])[3]",
                                         self.builder.constants.STRATEGY_XPATH, False)
                self.set_check_box_value(ui_cmd_obj, "(//input[@name='guestNotification'])[4]",
                                         self.builder.constants.STRATEGY_XPATH, False)
            if arg_dict['gu_notification'] == "display_un":
                self.set_check_box_value(ui_cmd_obj, "(//input[@name='guestNotification'])[1]",
                                         self.builder.constants.STRATEGY_XPATH, False)
                self.set_check_box_value(ui_cmd_obj, "(//input[@name='guestNotification'])[2]",
                                         self.builder.constants.STRATEGY_XPATH, False)
                self.set_check_box_value(ui_cmd_obj, "(//input[@name='guestNotification'])[3]",
                                         self.builder.constants.STRATEGY_XPATH, True)
                self.set_check_box_value(ui_cmd_obj, "(//input[@name='guestNotification'])[4]",
                                         self.builder.constants.STRATEGY_XPATH, False)
            if arg_dict['gu_notification'] == "display_pwd":
                self.set_check_box_value(ui_cmd_obj, "(//input[@name='guestNotification'])[1]",
                                         self.builder.constants.STRATEGY_XPATH, False)
                self.set_check_box_value(ui_cmd_obj, "(//input[@name='guestNotification'])[2]",
                                         self.builder.constants.STRATEGY_XPATH, False)
                self.set_check_box_value(ui_cmd_obj, "(//input[@name='guestNotification'])[3]",
                                         self.builder.constants.STRATEGY_XPATH, False)
                self.set_check_box_value(ui_cmd_obj, "(//input[@name='guestNotification'])[4]",
                                         self.builder.constants.STRATEGY_XPATH, True)
            if arg_dict['gu_notification'] == "gu_email_sms":
                self.set_check_box_value(ui_cmd_obj, "(//input[@name='guestNotification'])[1]",
                                         self.builder.constants.STRATEGY_XPATH, True)
                self.set_check_box_value(ui_cmd_obj, "(//input[@name='guestNotification'])[2]",
                                         self.builder.constants.STRATEGY_XPATH, True)
                self.set_check_box_value(ui_cmd_obj, "(//input[@name='guestNotification'])[3]",
                                         self.builder.constants.STRATEGY_XPATH, False)
                self.set_check_box_value(ui_cmd_obj, "(//input[@name='guestNotification'])[4]",
                                         self.builder.constants.STRATEGY_XPATH, False)
            if arg_dict['gu_notification'] == "dis_un_pwd":
                self.set_check_box_value(ui_cmd_obj, "(//input[@name='guestNotification'])[1]",
                                         self.builder.constants.STRATEGY_XPATH, False)
                self.set_check_box_value(ui_cmd_obj, "(//input[@name='guestNotification'])[2]",
                                         self.builder.constants.STRATEGY_XPATH, False)
                self.set_check_box_value(ui_cmd_obj, "(//input[@name='guestNotification'])[3]",
                                         self.builder.constants.STRATEGY_XPATH, True)
                self.set_check_box_value(ui_cmd_obj, "(//input[@name='guestNotification'])[4]",
                                         self.builder.constants.STRATEGY_XPATH, True)
            if arg_dict['gu_notification'] == "gu_email_un":
                self.set_check_box_value(ui_cmd_obj, "(//input[@name='guestNotification'])[1]",
                                         self.builder.constants.STRATEGY_XPATH, True)
                self.set_check_box_value(ui_cmd_obj, "(//input[@name='guestNotification'])[2]",
                                         self.builder.constants.STRATEGY_XPATH, False)
                self.set_check_box_value(ui_cmd_obj, "(//input[@name='guestNotification'])[3]",
                                         self.builder.constants.STRATEGY_XPATH, True)
                self.set_check_box_value(ui_cmd_obj, "(//input[@name='guestNotification'])[4]",
                                         self.builder.constants.STRATEGY_XPATH, False)
            if arg_dict['gu_notification'] == "gu_email_pwd":
                self.set_check_box_value(ui_cmd_obj, "(//input[@name='guestNotification'])[1]",
                                         self.builder.constants.STRATEGY_XPATH, True)
                self.set_check_box_value(ui_cmd_obj, "(//input[@name='guestNotification'])[2]",
                                         self.builder.constants.STRATEGY_XPATH, False)
                self.set_check_box_value(ui_cmd_obj, "(//input[@name='guestNotification'])[3]",
                                         self.builder.constants.STRATEGY_XPATH, False)
                self.set_check_box_value(ui_cmd_obj, "(//input[@name='guestNotification'])[4]",
                                         self.builder.constants.STRATEGY_XPATH, True)
            if arg_dict['gu_notification'] == "gu_sms_un":
                self.set_check_box_value(ui_cmd_obj, "(//input[@name='guestNotification'])[1]",
                                         self.builder.constants.STRATEGY_XPATH, False)
                self.set_check_box_value(ui_cmd_obj, "(//input[@name='guestNotification'])[2]",
                                         self.builder.constants.STRATEGY_XPATH, True)
                self.set_check_box_value(ui_cmd_obj, "(//input[@name='guestNotification'])[3]",
                                         self.builder.constants.STRATEGY_XPATH, True)
                self.set_check_box_value(ui_cmd_obj, "(//input[@name='guestNotification'])[4]",
                                         self.builder.constants.STRATEGY_XPATH, False)
            if arg_dict['gu_notification'] == "gu_sms_pwd":
                self.set_check_box_value(ui_cmd_obj, "(//input[@name='guestNotification'])[1]",
                                         self.builder.constants.STRATEGY_XPATH, False)
                self.set_check_box_value(ui_cmd_obj, "(//input[@name='guestNotification'])[2]",
                                         self.builder.constants.STRATEGY_XPATH, True)
                self.set_check_box_value(ui_cmd_obj, "(//input[@name='guestNotification'])[3]",
                                         self.builder.constants.STRATEGY_XPATH, False)
                self.set_check_box_value(ui_cmd_obj, "(//input[@name='guestNotification'])[4]",
                                         self.builder.constants.STRATEGY_XPATH, True)
            if arg_dict['gu_notification'] == "gu_sms_un_pwd":
                self.set_check_box_value(ui_cmd_obj, "(//input[@name='guestNotification'])[1]",
                                         self.builder.constants.STRATEGY_XPATH, True)
                self.set_check_box_value(ui_cmd_obj, "(//input[@name='guestNotification'])[2]",
                                         self.builder.constants.STRATEGY_XPATH, True)
                self.set_check_box_value(ui_cmd_obj, "(//input[@name='guestNotification'])[3]",
                                         self.builder.constants.STRATEGY_XPATH, True)
                self.set_check_box_value(ui_cmd_obj, "(//input[@name='guestNotification'])[4]",
                                         self.builder.constants.STRATEGY_XPATH, True)
            if arg_dict['ot_save'] == "save":
                self.builder.click(ui_cmd_obj, "//div[@class='x-panel x-tabpanel-child x-panel-default']/div/"
                                               "div/div/div/a[@data-qtip='Save Onboarding Template']")
                self.spinner_loading(ui_cmd_obj)
                self.is_ldap_pop_up_exists(ui_cmd_obj)
                self.builder.click(ui_cmd_obj, "//span[@role='presentation']/span[text()='Refresh']")
            if arg_dict['ot_cancel'] == "cancel":
                self.builder.click(ui_cmd_obj, "//div[@class='x-panel x-tabpanel-child x-panel-default']/div/"
                                               "div/div/div/a[@data-qtip='Save Onboarding Template']/following::a[1]")
                self.spinner_loading(ui_cmd_obj)
            return ui_cmd_obj
        except TypeError:
            return ui_cmd_obj

    def gu_notification_create_gu(self, ui_cmd_obj, arg_dict):
        self.spinner_loading(ui_cmd_obj)
        self.select_ot_from_dropdown(ui_cmd_obj, arg_dict)
        self.builder.enter_text(ui_cmd_obj, arg_dict['gu_fname'], "//input[@name='firstName']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['gu_lname'], "//input[@name='lastName']")
        if arg_dict['gu_uname'] != "None":
            self.builder.enter_text(ui_cmd_obj, arg_dict['gu_uname'], "//input[@name='loginId']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['gu_pwd'], "//input[@name='password']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['gu_email'], "//input[@name='email']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['gu_cellPhone'], "//input[@name='cellPhone']")
        self.builder.delay(ui_cmd_obj, 5)
        if arg_dict['user_email'] == "user_email":
            self.builder.delay(ui_cmd_obj, 5)
            self.builder.find_element(ui_cmd_obj, "//input[@name='sendNotifGuestEmail']")
            self.builder.delay(ui_cmd_obj, 5)
            self.builder.get_text_from_element_and_compare(ui_cmd_obj, "//input[@name='sendNotifGuestEmail']"
                                                                       "/following::label[1]", "Guest User Email")
            self.builder.click(ui_cmd_obj, "//input[@name='sendNotifGuestEmail']")
            self.builder.get_text_from_element_and_compare(ui_cmd_obj, "//span[@class='x-form-item-label-inner x-"
                                                                       "form-item-label-inner-default']/"
                                                                       "span[text()='Email']", "Email *:")
        if arg_dict['user_sms'] == "user_sms":
            self.builder.delay(ui_cmd_obj, 5)
            self.builder.find_element(ui_cmd_obj, "//input[@name='sendNotifGuestCellPhone']")
            self.builder.delay(ui_cmd_obj, 5)
            self.builder.click(ui_cmd_obj, "//input[@name='sendNotifGuestCellPhone']")
            self.builder.get_text_from_element_and_compare(ui_cmd_obj, "//input[@name='sendNotifGuestCellPhone']/"
                                                                       "following::label[1]", "Password to Guest "
                                                                                              "User Mobile Phone")
            self.builder.get_text_from_element_and_compare(ui_cmd_obj, "//span[@class='x-form-item-label-inner x-"
                                                                       "form-item-label-inner-default']/"
                                                                       "span[text()='Mobile']", "Mobile *:")
        self.builder.click(ui_cmd_obj, "//span[text()='Save']")
        self.base_builder.delay(ui_cmd_obj, 10000)
        if arg_dict['read_from_pop'] == "yes_read_from_pop":
            web_obj = self.builder.find_element(ui_cmd_obj, ".x-window-text",
                                                self.builder.constants.STRATEGY_CSS_SELECTOR)
            return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
            self.logger.log_info(return_text)
            if return_text != arg_dict['text_from_pop']:
                ui_cmd_obj.error_state = True
            else:
                ui_cmd_obj.error_state = False
        if arg_dict['ok'] == "ok":
            self.builder.click(ui_cmd_obj, "//span[text()='OK']")
            self.spinner_loading(ui_cmd_obj)

        return ui_cmd_obj

    def gu_notification_ss_gu(self, ui_cmd_obj, arg_dict):
        try:
            self.builder.delay(ui_cmd_obj, 5)
            self.is_cookies_exists(ui_cmd_obj)
            if arg_dict['self_prov'] == "self_prov":
                self.builder.enter_text(ui_cmd_obj, arg_dict['gu_fname'], "//input[@name='userFirstName']")
                self.builder.enter_text(ui_cmd_obj, arg_dict['gu_lname'], "//input[@name='userLastName']")
                self.builder.enter_text(ui_cmd_obj, arg_dict['gu_uname'], "//input[@name='username']")
                self.builder.enter_text(ui_cmd_obj, arg_dict['gu_pwd'], "//input[@name='userPassword']")
                self.builder.enter_text(ui_cmd_obj, arg_dict['gu_email'], "//input[@name='userEmail']")
                if arg_dict['user_email'] == "user_email":
                    self.builder.get_text_from_element_and_compare(ui_cmd_obj,
                                                                   "//input[@name='userEmail']/preceding::label[1]",
                                                                   "Email *:", self.builder.constants.STRATEGY_XPATH)
                if arg_dict['user_sms'] == "user_sms":
                    self.builder.get_text_from_element_and_compare(ui_cmd_obj,
                                                                   "//input[@name='userCellPhone']/"
                                                                   "preceding::label[1]", "Mobile Phone *:",
                                                                   self.builder.constants.STRATEGY_XPATH)
                self.builder.enter_text(ui_cmd_obj, arg_dict['gu_cell_phone'], "//input[@name='userCellPhone']")
            if arg_dict['req_approval'] == "sponsor_approval":
                self.builder.enter_text(ui_cmd_obj, arg_dict['sponsor_fname'], "//input[@name='sponsorFirstName']")
                self.builder.enter_text(ui_cmd_obj, arg_dict['sponsor_lname'], "//input[@name='sponsorLastName']")
                self.builder.enter_text(ui_cmd_obj, arg_dict['sponsor_email'],
                                        "//div[2]/div[@role='presentation']/div"
                                        "[5]/div[@role='presentation']/div[@role="
                                        "'presentation']//input[@role='textbox']",
                                        self.builder.constants.STRATEGY_XPATH)
                self.builder.click(ui_cmd_obj, "(//input[@readonly='readonly'])[3]",
                                   self.builder.constants.STRATEGY_XPATH)
                self.builder.click(ui_cmd_obj, "//li[@role='option']", self.builder.constants.STRATEGY_XPATH)
                self.builder.enter_text(ui_cmd_obj, "1234567890", "//input[@name='sponsorCellPhone']")
                self.builder.click(ui_cmd_obj, "//span[text()='Request Approval']",
                                   self.builder.constants.STRATEGY_XPATH)
                # self.spinner_loading(ui_cmd_obj)
            if arg_dict['sponsor_type'] == "pre_sponsor1":
                self.builder.click(ui_cmd_obj, "//div[2]/div[@role='presentation']/div[2]/div[@role='presentation']"
                                               "/div[@role='presentation']/div[2]",
                                   self.builder.constants.STRATEGY_XPATH)
                self.spinner_loading(ui_cmd_obj)
                self.builder.click(ui_cmd_obj, "//ul[@role='listbox']/li[@role='option']")
                self.builder.click(ui_cmd_obj, "//span[text()='Request Approval']",
                                   self.builder.constants.STRATEGY_XPATH)
                # self.spinner_loading(ui_cmd_obj)
            if arg_dict['sponsor_type'] == "pre_sponsor2":
                self.builder.enter_text(ui_cmd_obj, arg_dict['sponsor_email'], "//input[@name='sponsorEmail']")
                self.builder.delay(ui_cmd_obj, 2)
                self.builder.click(ui_cmd_obj, "//span[text()='Request Approval']",
                                   self.builder.constants.STRATEGY_XPATH)
                # self.spinner_loading(ui_cmd_obj)
            if arg_dict['sponsor_type'] == "fixed":
                self.builder.click(ui_cmd_obj, "//span[text()='Request Approval']",
                                   self.builder.constants.STRATEGY_XPATH)
                # self.spinner_loading(ui_cmd_obj)
            if arg_dict['sp_submit'] == "submit":
                self.builder.click(ui_cmd_obj, "//span[text()='Submit']")
            self.spinner_loading(ui_cmd_obj)
            web_obj = self.builder.find_element(ui_cmd_obj, ".x-window-text",
                                                self.builder.constants.STRATEGY_CSS_SELECTOR)
            return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
            self.logger.log_info(return_text)
            if return_text != arg_dict['text_from_pop']:
                ui_cmd_obj.error_state = True
            else:
                ui_cmd_obj.error_state = False
            if arg_dict['sp_ok'] == "ok":
                self.builder.click(ui_cmd_obj, "//span[@class='x-btn-inner x-btn-inner-blue-small' and text()='OK']")
                self.spinner_loading(ui_cmd_obj)
            return ui_cmd_obj
        except TypeError:
            return ui_cmd_obj

    def gu_create_accessible_to_prov_options(self, ui_cmd_obj, arg_dict):
        self.builder.delay(ui_cmd_obj, 5)
        self.select_ot_from_dropdown(ui_cmd_obj, arg_dict)
        if arg_dict['fl_name'] == "fl_name_yes":
            self.builder.enter_text(ui_cmd_obj, arg_dict['gu_fname'], "//input[@name='firstName']")
            self.builder.enter_text(ui_cmd_obj, arg_dict['gu_lname'], "//input[@name='lastName']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['gu_uname'], "//input[@name='loginId']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['pwd'], "//input[@type='password' and @name='password']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['gu_email'], "//input[@name='email']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['cellphone'], "//input[@name='cellPhone']")
        if arg_dict['sms_gateway_list'] == "sms_yes":
            self.builder.get_text_from_element_and_compare(ui_cmd_obj, "//div[@class='x-field x-form-item "
                                                                       "x-form-item-default x-form-type-text "
                                                                       "x-box-item x-field-default "
                                                                       "x-vbox-form-item x-form-dirty']/"
                                                                       "label/span/span[text()='Carrier:']",
                                                           "Carrier:")
        if arg_dict['acc_exp_option'] == "max_exp_time":
            if arg_dict['acc_exp'] == "acc_exp_yes":
                self.builder.get_text_from_element_and_compare(ui_cmd_obj, "//div[@class='x-field x-form-item "
                                                                           "x-form-item-default x-form-type-text "
                                                                           "x-box-item x-field-default "
                                                                           "x-hbox-form-item x-form-dirty']/label/"
                                                                           "span/span", "Duration *:")
            if arg_dict['doe_yes_or_no'] == "doe_yes":
                if arg_dict['doe_option'] == "delete_on_expire":
                    self.builder.get_attribute_from_element_and_compare(ui_cmd_obj, "//input[@name='deleteOnExpire']",
                                                                        "checked", "true")
                if arg_dict['doe_option'] == "do_not_doe":
                    web_obj = self.builder.get_attribute_from_element(ui_cmd_obj, "//input[@name='deleteOnExpire']",
                                                                      "checked")
                    self.logger.log_info("checked false: " + str(web_obj))
                    if web_obj != "None":
                        ui_cmd_obj.error_state = True
        self.builder.click(ui_cmd_obj, "//span[text()='Save']", self.builder.constants.STRATEGY_XPATH)
        self.wait_for_element_present(ui_cmd_obj, "//span[text()='OK']")
        if arg_dict['error_no_error'] == "error":
            self.builder.get_text_from_element_and_compare(ui_cmd_obj, "(//div[@class='x-title-text x-title-"
                                                                       "text-default x-title-item'])[3]", "Error")
            self.builder.click(ui_cmd_obj, "//span[text()='OK']")
            self.spinner_loading(ui_cmd_obj)
            self.builder.click(ui_cmd_obj, "(//span[text()='Cancel'])[1]")
        else:
            self.builder.get_text_from_element_and_compare(ui_cmd_obj, "(//div[@role='alertdialog']/div)[1]",
                                                           "Successful Guest Creation")
            self.builder.click(ui_cmd_obj, "//span[text()='OK']", self.builder.constants.STRATEGY_XPATH)
            self.spinner_loading(ui_cmd_obj)
            self.filtering_guest_users_based_on_username(ui_cmd_obj, arg_dict)
            all_count = self.builder.find_elements(ui_cmd_obj, "//div[@class ='x-grid-item-container']/table")
            row_count = len(all_count)
            if row_count == 0:
                ui_cmd_obj.error_state = True
            else:
                for index in range(1, (row_count + 1)):
                    web_obj = self.builder.find_element(ui_cmd_obj, "//div[@class ='x-grid-item-container']"
                                                                    "/table[" + str(index) + "]/tbody/tr/td[1]")
                    return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
                    self.logger.log_info("gu_uname: " + str(index) + "::" + return_text)
                    if return_text == arg_dict['gu_uname']:
                        ui_cmd_obj.error_state = False
                        self.logger.log_info("<" + arg_dict['gu_uname'] + "> gu_uname: exists ::" + return_text)

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

    def is_cookies_exists(self, ui_cmd_obj):
        web_obj = self.base_builder.find_element_by_xpath(ui_cmd_obj, "//div[@class='cookie-content']/span")
        if self.base_builder.is_element_displayed(ui_cmd_obj, web_obj):
            self.logger.log_info("cookies element exists")
            self.base_builder.click(ui_cmd_obj, web_obj)
            self.spinner_loading(ui_cmd_obj)
        else:
            self.logger.log_info("cookies element not exists")

        return ui_cmd_obj

    def spinner_loading(self, ui_cmd_obj):
        self.builder.webdriver_wait_until(ui_cmd_obj, ".x-mask-msg-text", retry=5,
                                          strategy=self.builder.constants.STRATEGY_CSS_SELECTOR,
                                          condition=self.builder.constants.CONDITION_INVISIBILITY_OF_ELEMENT)
        return ui_cmd_obj

    def is_element_selected(self, ui_cmd_obj, locator, strategy):
        web_obj = self.builder.find_element(ui_cmd_obj, locator, strategy)
        return_txt = self.base_builder.is_element_selected(ui_cmd_obj, web_obj)
        self.logger.log_info(return_txt)
        if not return_txt:
            ui_cmd_obj.error_state = True
            self.logger.log_info(ui_cmd_obj.error_state)

        return ui_cmd_obj

    def is_element_displayed(self, ui_cmd_obj, locator, strategy):
        web_obj = self.builder.find_element(ui_cmd_obj, locator, strategy)
        return_txt = self.base_builder.is_element_displayed(ui_cmd_obj, web_obj)
        self.logger.log_info(return_txt)
        if not return_txt:
            ui_cmd_obj.error_state = True
            self.logger.log_info(ui_cmd_obj.error_state)

        return ui_cmd_obj

    def set_check_box_value(self, ui_cmd_obj, locator, strategy, is_checked):
        is_input_checked = self.builder.get_attribute_from_element(ui_cmd_obj, locator, 'checked', strategy)
        self.logger.logger.info("current check box status: " + str(is_input_checked))
        if (not is_input_checked) and is_checked:
            self.builder.click(ui_cmd_obj, locator, strategy)
        elif is_input_checked and (not is_checked):
            self.builder.click(ui_cmd_obj, locator, strategy)

        return ui_cmd_obj

    def filtering_guest_users_based_on_username(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//span[text()='Show Filter']", self.builder.constants.STRATEGY_XPATH)
        self.spinner_loading(ui_cmd_obj)
        self.builder.click(ui_cmd_obj, "//label[contains(text(),'Specify Filter')]",
                           self.builder.constants.STRATEGY_XPATH)
        self.builder.click(ui_cmd_obj, "//input[@name='primaryFilterValue']")
        self.builder.click(ui_cmd_obj, "//li[text()='Username']", self.builder.constants.STRATEGY_XPATH)
        self.spinner_loading(ui_cmd_obj)
        self.builder.click(ui_cmd_obj, "//input[@name='comparisionValue']")
        self.builder.click(ui_cmd_obj, "//li[text()='Equals']", self.builder.constants.STRATEGY_XPATH)
        self.builder.enter_text(ui_cmd_obj, arg_dict['gu_uname'], "//input[@name='textValue']")
        self.builder.click(ui_cmd_obj, "//span[text()='Apply Filter']", self.builder.constants.STRATEGY_XPATH)
        self.spinner_loading(ui_cmd_obj)

        return ui_cmd_obj

    def wait_for_page_load_completely(self, ui_cmd_obj):
        self.logger.log_info("waiting for the page to load...")
        for x in range(1, 25):
            self.base_builder.delay(ui_cmd_obj, 1000)
            self.base_builder.execute_script(ui_cmd_obj, "return document.readyState;")
            self.logger.log_info("page readyState:  " + str(ui_cmd_obj.return_data))
            if ui_cmd_obj.return_data == "complete":
                self.logger.log_info("page loaded completely: ")
                break

        return ui_cmd_obj

    def select_ot_from_dropdown(self, ui_cmd_obj, arg_dict):
        self.gu_click_nav_bar(ui_cmd_obj, arg_dict)
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
                self.wait_for_element_present(ui_cmd_obj, "//span[text()='Save']")
                break
            elif return_text == observed_value:
                ui_cmd_obj.error_state = True
                break
            else:
                observed_value = return_text
                index += 1

        return ui_cmd_obj

    def wait_for_element_present(self, ui_cmd_obj, xpath_locator):
        self.base_builder.webdriver_wait_until(ui_cmd_obj, xpath_locator, retry=5)

        return ui_cmd_obj

    def gu_table_complete_validation(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            return super(Gimguestusers, self).gu_table_complete_validation(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def gu_admin_gu_filters(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//span[@class='x-btn-inner x-btn-inner-extr-nav-toolbar-button-small' and "
                                       "text()='Guest Users']")
        self.builder.click(ui_cmd_obj, "//span[text()='Show Filter']", self.builder.constants.STRATEGY_XPATH)
        self.spinner_loading(ui_cmd_obj)
        self.builder.click(ui_cmd_obj, "//label[contains(text(),'Specify Filter')]",
                           self.builder.constants.STRATEGY_XPATH)
        # DropDown1
        self.builder.click(ui_cmd_obj, "//input[@name='primaryFilterValue']")
        if arg_dict['primary_value'] == "username":
            self.builder.click(ui_cmd_obj, "//li[text()='Username']", self.builder.constants.STRATEGY_XPATH)
        if arg_dict['primary_value'] == "firstname":
            self.builder.click(ui_cmd_obj, "//li[text()='First Name']", self.builder.constants.STRATEGY_XPATH)
        if arg_dict['primary_value'] == "lastname":
            self.builder.click(ui_cmd_obj, "//li[text()='Last Name']", self.builder.constants.STRATEGY_XPATH)
        if arg_dict['primary_value'] == "email":
            self.builder.click(ui_cmd_obj, "//li[text()='Email']", self.builder.constants.STRATEGY_XPATH)
        if arg_dict['primary_value'] == "smsaddress":
            self.builder.click(ui_cmd_obj, "//li[text()='SMS Address']", self.builder.constants.STRATEGY_XPATH)
        if arg_dict['primary_value'] == "starttime":
            self.builder.click(ui_cmd_obj, "//li[text()='Start Time']", self.builder.constants.STRATEGY_XPATH)
        if arg_dict['primary_value'] == "endtime":
            self.builder.click(ui_cmd_obj, "//li[text()='End Time']", self.builder.constants.STRATEGY_XPATH)
        if arg_dict['primary_value'] == "guestuserstate":
            self.builder.click(ui_cmd_obj, "//li[text()='Guest User State']", self.builder.constants.STRATEGY_XPATH)
        if arg_dict['primary_value'] == "gu_activated_last":
            self.builder.click(ui_cmd_obj, "//li[text()='Guest Users Activated In The Last']",
                               self.builder.constants.STRATEGY_XPATH)
        if arg_dict['primary_value'] == "first_login_pending":
            self.builder.click(ui_cmd_obj, "//li[text()='First Login Pending And Created Before']",
                               self.builder.constants.STRATEGY_XPATH)
        if arg_dict['primary_value'] == "gu_expiry":
            self.builder.click(ui_cmd_obj, "//li[text()='Guest Users Expiring In The Next']",
                               self.builder.constants.STRATEGY_XPATH)
        if arg_dict['primary_value'] == "gu_expired":
            self.builder.click(ui_cmd_obj, "//li[text()='Expired Guest Users']", self.builder.constants.STRATEGY_XPATH)
        if arg_dict['primary_value'] == "sponsor_responce":
            self.builder.click(ui_cmd_obj, "//li[text()='Sponsor Response']", self.builder.constants.STRATEGY_XPATH)
        if arg_dict['primary_value'] == "gu_provisioner":
            self.builder.click(ui_cmd_obj, "//li[text()='Provisioner']", self.builder.constants.STRATEGY_XPATH)
        if arg_dict['primary_value'] == "meeting_id":
            self.builder.click(ui_cmd_obj, "//li[text()='Meeting ID']", self.builder.constants.STRATEGY_XPATH)
        if arg_dict['primary_value'] == "gu_ot":
            self.builder.click(ui_cmd_obj, "//li[text()='Onboarding Template']", self.builder.constants.STRATEGY_XPATH)
        if arg_dict['primary_value'] == "sponsor_email":
            self.builder.click(ui_cmd_obj, "//li[text()='Sponsor Email']", self.builder.constants.STRATEGY_XPATH)
        # DropDown2
        self.builder.click(ui_cmd_obj, "//input[@name='comparisionValue']")
        if arg_dict['compare_value'] == "startwith":
            self.builder.click(ui_cmd_obj, "//li[text()='Starts With']", self.builder.constants.STRATEGY_XPATH)
        if arg_dict['compare_value'] == "endwith":
            self.builder.click(ui_cmd_obj, "//li[text()='Ends With']", self.builder.constants.STRATEGY_XPATH)
        if arg_dict['compare_value'] == "contains":
            self.builder.click(ui_cmd_obj, "//li[text()='Contains']", self.builder.constants.STRATEGY_XPATH)
        if arg_dict['compare_value'] == "equals":
            self.builder.click(ui_cmd_obj, "//li[text()='Equals']", self.builder.constants.STRATEGY_XPATH)
        if arg_dict['compare_value'] == "not_equals":
            self.builder.click(ui_cmd_obj, "//li[text()='Not Equals']", self.builder.constants.STRATEGY_XPATH)
        if arg_dict['compare_value'] == "greaterthan":
            self.builder.click(ui_cmd_obj, "//li[text()='Greater than']", self.builder.constants.STRATEGY_XPATH)
        if arg_dict['compare_value'] == "greaterthan_equal":
            self.builder.click(ui_cmd_obj, "//li[text()='Greater than or Equal']",
                               self.builder.constants.STRATEGY_XPATH)
        if arg_dict['compare_value'] == "lessthan":
            self.builder.click(ui_cmd_obj, "//li[text()='Lesser than']", self.builder.constants.STRATEGY_XPATH)
        if arg_dict['compare_value'] == "less_equal":
            self.builder.click(ui_cmd_obj, "//li[text()='Lesser than or Equal']", self.builder.constants.STRATEGY_XPATH)
        if arg_dict['compare_value'] == "gu_enabled":
            self.builder.click(ui_cmd_obj, "//li[text()='Enabled']", self.builder.constants.STRATEGY_XPATH)
        if arg_dict['compare_value'] == "gu_disabled":
            self.builder.click(ui_cmd_obj, "//li[text()='Disabled']", self.builder.constants.STRATEGY_XPATH)
        if arg_dict['compare_value'] == "less_equal":
            self.builder.click(ui_cmd_obj, "//li[text()='textValue']", self.builder.constants.STRATEGY_XPATH)
        if arg_dict['compare_value'] == "sponsor_approve":
            self.builder.click(ui_cmd_obj, "//li[text()='Approved']", self.builder.constants.STRATEGY_XPATH)
        if arg_dict['compare_value'] == "sponsor_denied":
            self.builder.click(ui_cmd_obj, "//li[text()='Denied']", self.builder.constants.STRATEGY_XPATH)
        if arg_dict['compare_value'] == "sponsor_approve_pending":
            self.builder.click(ui_cmd_obj, "//li[text()='Pending']", self.builder.constants.STRATEGY_XPATH)
        if arg_dict['compare_value'] == "sponsor_auto_approve":
            self.builder.click(ui_cmd_obj, "//li[text()='Auto-Approved']", self.builder.constants.STRATEGY_XPATH)
        if arg_dict['compare_value'] == "sponsor_auto_denied":
            self.builder.click(ui_cmd_obj, "//li[text()='Auto-Denied']", self.builder.constants.STRATEGY_XPATH)
        if arg_dict['compare_value'] == "not_applicable":
            self.builder.click(ui_cmd_obj, "//li[text()='Not Applicable']", self.builder.constants.STRATEGY_XPATH)
        self.builder.enter_text(ui_cmd_obj, arg_dict['text_value'], "//input[@name='textValue']")
        self.builder.click(ui_cmd_obj, "//span[text()='Apply Filter']", self.builder.constants.STRATEGY_XPATH)
        self.spinner_loading(ui_cmd_obj)

        return ui_cmd_obj

    def gu_enable_or_disable_delete_expiry(self, ui_cmd_obj, arg_dict):
        self.select_ot_from_dropdown(ui_cmd_obj, arg_dict)
        self.builder.enter_text(ui_cmd_obj, arg_dict['gu_fname'], "//input[@name='firstName']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['gu_lname'], "//input[@name='lastName']")
        if arg_dict['gu_uname'] != "None":
            self.builder.enter_text(ui_cmd_obj, arg_dict['gu_uname'], "//input[@name='loginId']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['gu_pwd'], "//input[@name='password']")
        if arg_dict['gu_enable'] == "gu_enable":
            self.set_check_box_value(ui_cmd_obj, "//input[@name='enabled']",
                                     self.builder.constants.STRATEGY_XPATH, True)
        if arg_dict['gu_enable'] == "gu_disable":
            self.set_check_box_value(ui_cmd_obj, "//input[@name='enabled']",
                                     self.builder.constants.STRATEGY_XPATH, False)
        self.builder.enter_text(ui_cmd_obj, arg_dict['gu_email'], "//input[@name='email']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['gu_cellPhone'], "//input[@name='cellPhone']")
        self.builder.click(ui_cmd_obj, "//span[text()='Save']")
        self.wait_for_element_present(ui_cmd_obj, "//span[text()='OK']")
        self.builder.click(ui_cmd_obj, "//span[text()='OK']")
        self.spinner_loading(ui_cmd_obj)

        return ui_cmd_obj

    def gu_sponsor_approval_from_provisioner_login(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//span[@class='x-btn-inner x-btn-inner-extr-nav-toolbar-button-small' "
                                       "and text()='Sponsor']")
        self.select_row_from_sponsor_table(ui_cmd_obj, arg_dict)
        if arg_dict['approve_or_deny'] == "approve":
            self.builder.click(ui_cmd_obj, "Approve", self.builder.constants.STRATEGY_LINK_TEXT)
            self.builder.click(ui_cmd_obj, "//span[@class='x-btn-inner x-btn-inner-blue-small' and text()='Approve']")
            self.builder.click(ui_cmd_obj, "//span[@class='x-btn-inner x-btn-inner-default-small' and text()='Close']")
        if arg_dict['approve_or_deny'] == "deny":
            self.builder.click(ui_cmd_obj, "Deny/Lock", self.builder.constants.STRATEGY_LINK_TEXT)
            self.builder.click(ui_cmd_obj, "//span[@class='x-btn-inner x-btn-inner-blue-small' and text()='Deny/Lock']")
            self.builder.click(ui_cmd_obj, "//span[@class='x-btn-inner x-btn-inner-default-small' and text()='Close']")

        return ui_cmd_obj

    def select_row_from_sponsor_table(self, ui_cmd_obj, arg_dict):
        self.wait_for_page_load_completely(ui_cmd_obj)
        all_count = self.builder.find_elements(ui_cmd_obj, "//div[@class ='x-grid-item-container']/table")
        row_count = len(all_count)
        self.logger.log_info("row_count: " + str(row_count))
        for index in range(1, (row_count + 1)):
            web_obj = self.builder.find_element(ui_cmd_obj, "//div[@class ='x-grid-item-container']/"
                                                            "table[" + str(index) + "]/tbody/tr/td[1]")
            return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
            self.logger.log_info("spon_name: " + str(index) + "::" + return_text)
            if return_text == arg_dict['spon_name']:
                self.builder.click(ui_cmd_obj, "//div[@class ='x-grid-item-container']/"
                                               "table[" + str(index) + "]")
                self.logger.log_info("selected spon_name: " + str(arg_dict['spon_name']))
                ui_cmd_obj.error_state = False
                break
            else:
                ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def gu_resend_details(self, ui_cmd_obj, arg_dict):
        self.is_cookies_exists(ui_cmd_obj)
        if arg_dict['approval'] == "sponsor_approval":
            self.builder.enter_text(ui_cmd_obj, arg_dict['fname'], "//input[@name='sponsorFirstName']")
            self.builder.enter_text(ui_cmd_obj, arg_dict['lname'], "//input[@name='sponsorLastName']")
            self.builder.enter_text(ui_cmd_obj, arg_dict['mail_pwd'], "//div[2]/div[@role='presentation']/"
                                                                      "div[5]/div[@role='presentation']/div"
                                                                      "[@role='presentation']//input[@role='textbox']")
            self.builder.click(ui_cmd_obj, "(//input[@readonly='readonly'])[3]",
                               self.builder.constants.STRATEGY_XPATH)
            self.builder.click(ui_cmd_obj, "//li[@role='option']", self.builder.constants.STRATEGY_XPATH)
            self.builder.enter_text(ui_cmd_obj, arg_dict['mobile'], "//input[@name='sponsorCellPhone']")
        if arg_dict['resend_details'] == "resend_details":
            resend_txt = self.builder.get_text_from_element(ui_cmd_obj, "(//span[@class='x-btn-inner "
                                                                        "x-btn-inner-default-small'])[3]",
                                                            self.builder.constants.STRATEGY_XPATH)
            if resend_txt != "Resend Details":
                ui_cmd_obj.error_state = True
        elif arg_dict['resend_details'] == "resend_pwd":
            resend_txt = self.builder.get_text_from_element(ui_cmd_obj, "(//span[@class='x-btn-inner "
                                                                        "x-btn-inner-default-small'])[2]",
                                                            self.builder.constants.STRATEGY_XPATH)
            if resend_txt != "Resend Password":
                ui_cmd_obj.error_state = True
        if arg_dict['approval'] == "sponsor_approval":
            self.builder.click(ui_cmd_obj, "//span[text()='Request Approval']", self.builder.constants.STRATEGY_XPATH)
        else:
            self.builder.click(ui_cmd_obj, "//span[@class='x-btn-inner x-btn-inner-blue-small' and text()='Submit']",
                               self.builder.constants.STRATEGY_XPATH)
        self.builder.click(ui_cmd_obj, "//span[text()='OK']", self.builder.constants.STRATEGY_XPATH)
        self.wait_for_page_load_completely(ui_cmd_obj)
        if arg_dict['resend_details'] != "no_resend":
            if arg_dict['approval'] == "no_sponsor_approval":
                self.builder.enter_text(ui_cmd_obj, arg_dict['gu_uname'], "//input[@name='username']",
                                        self.builder.constants.STRATEGY_XPATH)
                if arg_dict['resend_details'] == "resend_details":
                    self.builder.click(ui_cmd_obj, "(//span[@class='x-btn-inner x-btn-inner-default-small'])[3]",
                                       self.builder.constants.STRATEGY_XPATH)
                elif arg_dict['resend_details'] == "resend_pwd":
                    self.builder.click(ui_cmd_obj, "(//span[@class='x-btn-inner x-btn-inner-default-small'])[2]",
                                       self.builder.constants.STRATEGY_XPATH)

                popup_txt = self.builder.get_text_from_element(ui_cmd_obj, "//div[@class='x-component x-window-text "
                                                                           "x-box-item x-component-default']",
                                                               self.builder.constants.STRATEGY_XPATH)
                if arg_dict['resend_details'] == "resend_details":
                    if popup_txt != "Details has been successfully resent.":
                        ui_cmd_obj.error_state = True
                elif arg_dict['resend_details'] == "resend_pwd":
                    if popup_txt != "Password has been successfully resent.":
                        ui_cmd_obj.error_state = True
                self.builder.click(ui_cmd_obj, "//span[text()='OK']")

        return ui_cmd_obj
