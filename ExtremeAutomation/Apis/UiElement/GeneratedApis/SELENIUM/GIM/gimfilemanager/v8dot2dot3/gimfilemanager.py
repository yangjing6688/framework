from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as GimfilemanagerBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Gimfilemanager(GimfilemanagerBase):
    def fm_pref_tab_exist(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//span[text()='Administration']",
                           self.builder.constants.STRATEGY_XPATH,)
        web_obj = self.builder.find_element(ui_cmd_obj, "//span[text()='Preferences']",
                                            self.builder.constants.STRATEGY_XPATH)
        return_text = web_obj.text
        if return_text == "Preferences":
            web_obj = self.builder.find_element(ui_cmd_obj, "//span[text()='Preferences']",
                                                self.builder.constants.STRATEGY_XPATH)
            return_text = web_obj.is_enabled()
            if not return_text:
                ui_cmd_obj.error_state = True
            else:
                self.builder.click(ui_cmd_obj, "//span[text()='Preferences']", self.builder.constants.STRATEGY_XPATH)
        else:
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def fm_contents_under_file_manager(self, ui_cmd_obj, arg_dict):
        if arg_dict['file_name'] == "NO":
            self.is_element_displayed(ui_cmd_obj, "//a[@data-qtip='Add file to File Manager' "
                                                  "and @aria-disabled='false']", self.builder.constants.STRATEGY_XPATH)
            self.is_element_displayed(ui_cmd_obj,
                                      "//a[@data-qtip='Delete File from File Manager' and @aria-disabled='true']",
                                      self.builder.constants.STRATEGY_XPATH)
            self.is_element_displayed(ui_cmd_obj,
                                      "//a[@data-qtip='Download selected file from File Manager' "
                                      "and @aria-disabled='true']", self.builder.constants.STRATEGY_XPATH)
        elif arg_dict['file_name'] == "Sample_Logo":
            self.builder.click(ui_cmd_obj, "//div[text()='sample_logo.gif']", self.builder.constants.STRATEGY_XPATH)
            self.is_element_displayed(ui_cmd_obj,
                                      "//a[@data-qtip='Delete File from File Manager' and @aria-disabled='true']",
                                      self.builder.constants.STRATEGY_XPATH)
            self.is_element_displayed(ui_cmd_obj,
                                      "//a[@data-qtip='Download selected file from File Manager' "
                                      "and @aria-disabled='false']", self.builder.constants.STRATEGY_XPATH)
        elif arg_dict['file_name'] == "Sample_Print":
            self.builder.click(ui_cmd_obj, "//div[text()='sample_print.css']", self.builder.constants.STRATEGY_XPATH)
            self.is_element_displayed(ui_cmd_obj,
                                      "//a[@data-qtip='Delete File from File Manager' and @aria-disabled='true']",
                                      self.builder.constants.STRATEGY_XPATH)
            self.is_element_displayed(ui_cmd_obj,
                                      "//a[@data-qtip='Download selected file from File Manager' "
                                      "and @aria-disabled='false']", self.builder.constants.STRATEGY_XPATH)
        elif arg_dict['file_name'] == "Sample_Print_Page":
            self.builder.click(ui_cmd_obj, "//div[text()='sample_print_page.html']",
                               self.builder.constants.STRATEGY_XPATH)
            self.is_element_displayed(ui_cmd_obj,
                                      "//a[@data-qtip='Delete File from File Manager' and @aria-disabled='true']",
                                      self.builder.constants.STRATEGY_XPATH)
            self.is_element_displayed(ui_cmd_obj,
                                      "//a[@data-qtip='Download selected file from File Manager' "
                                      "and @aria-disabled='false']", self.builder.constants.STRATEGY_XPATH)
        elif arg_dict['file_name'] == "Sample_Style":
            self.builder.click(ui_cmd_obj, "//div[text()='sample_style.css']", self.builder.constants.STRATEGY_XPATH)
            self.is_element_displayed(ui_cmd_obj,
                                      "//a[@data-qtip='Delete File from File Manager' and @aria-disabled='true']",
                                      self.builder.constants.STRATEGY_XPATH)
            self.is_element_displayed(ui_cmd_obj,
                                      "//a[@data-qtip='Download selected file from File Manager' "
                                      "and @aria-disabled='false']", self.builder.constants.STRATEGY_XPATH)

        return ui_cmd_obj

    def fm_default_sample_files(self, ui_cmd_obj, arg_dict):
        web_obj = self.builder.find_element(ui_cmd_obj, "//div[4]/div[2]/div[1]//div[@class='x-grid-item-container']"
                                                        "/table[1]/tbody/tr/td[1]",
                                            self.builder.constants.STRATEGY_XPATH)
        return_text1 = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        web_obj = self.builder.find_element(ui_cmd_obj, "//div[4]/div[2]/div[1]//div[@class='x-grid-item-container']"
                                                        "/table[2]/tbody/tr/td[1]",
                                            self.builder.constants.STRATEGY_XPATH)
        return_text2 = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        web_obj = self.builder.find_element(ui_cmd_obj, "//div[4]/div[2]/div[1]//div[@class='x-grid-item-container']"
                                                        "/table[3]/tbody/tr/td[1]",
                                            self.builder.constants.STRATEGY_XPATH)
        return_text3 = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        web_obj = self.builder.find_element(ui_cmd_obj, "//div[4]/div[2]/div[1]//div[@class='x-grid-item-container']"
                                                        "/table[4]/tbody/tr/td[1]",
                                            self.builder.constants.STRATEGY_XPATH)
        return_text4 = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        if return_text1 != "sample_logo.gif":
            self.logger.log_info(return_text1 + " is not equal to sample_logo.gif")
            ui_cmd_obj.error_state = True
        if return_text2 != "sample_print.css":
            self.logger.log_info(return_text2 + " is not equal to sample_print.css")
            ui_cmd_obj.error_state = True
        if return_text3 != "sample_print_page.html":
            self.logger.log_info(return_text3 + " is not equal to sample_print_page.html")
            ui_cmd_obj.error_state = True
        if return_text4 != "sample_style.css":
            self.logger.log_info(return_text4 + " is not equal to sample_style.css")
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def fm_file_manager_availability(self, ui_cmd_obj, arg_dict):
        web_obj = self.builder.find_element(ui_cmd_obj, "//div[starts-with(@id, 'lookAndFeelPanel')]/div[4]/div",
                                            self.builder.constants.STRATEGY_XPATH)
        return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
        if return_text == "File Manager":
            ui_cmd_obj.error_state = False
        else:
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def is_element_displayed(self, ui_cmd_obj, locator, strategy):
        web_obj = self.builder.find_element(ui_cmd_obj, locator, strategy)
        return_txt = self.base_builder.is_element_displayed(ui_cmd_obj, web_obj)
        self.logger.log_info(return_txt)
        if not return_txt:
            ui_cmd_obj.error_state = True
            self.logger.log_info(ui_cmd_obj.error_state)

        return ui_cmd_obj
