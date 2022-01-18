from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as DfndrwizardBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Dfndrwizard(DfndrwizardBase):
    def dfndr_wizard_configuration(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//mat-select/div/div/span")
        self.select_country_from_drop_down(ui_cmd_obj, arg_dict)
        self.builder.click(ui_cmd_obj, "//span[@dir='ltr']")
        self.select_timezone_from_drop_down(ui_cmd_obj, arg_dict)
        self.builder.click(ui_cmd_obj, "(//div[@class='mat-checkbox-inner-container'])[2]")
        self.builder.enter_text(ui_cmd_obj, "1234567812", "//div[@class='mat-input-infix mat-form-field-infix']/input")
        self.builder.click(ui_cmd_obj, "//button[@color='primary']")
        self.wait_for_page_load_completely(ui_cmd_obj)
        web_obj = self.builder.find_element(ui_cmd_obj, "//button[@color='primary']",
                                            self.builder.constants.STRATEGY_XPATH)
        return_txt = self.base_builder.is_element_displayed(ui_cmd_obj, web_obj)
        self.logger.log_info(return_txt)
        if return_txt:
            self.builder.click(ui_cmd_obj, "//button[@color='primary']")
        self.wait_for_page_load_completely(ui_cmd_obj)

        return ui_cmd_obj

    def dfndr_cleanup_for_wizard_run(self, ui_cmd_obj, arg_dict):
        # Delete Configure Defender created Site
        self.builder.click(ui_cmd_obj, "//div[@class='menu-name automation-menu-icon-sec-name ng-binding "
                                       "ng-scope' and text()='Configure']")
        self.builder.click(ui_cmd_obj, "[href='#/sites/configure'] [ng-if]",
                           self.builder.constants.STRATEGY_CSS_SELECTOR)
        self.spinner_loading(ui_cmd_obj)
        self.builder.click(ui_cmd_obj, "//div[@class='ui-grid-cell-contents ng-binding ng-scope' and "
                                       "text()='DFNDR_SITE']")
        self.spinner_loading(ui_cmd_obj)
        self.builder.click(ui_cmd_obj, "//button[@class='btn btn-primary exol-tb-btn automation-site-del "
                                       "ng-binding']")
        self.spinner_loading(ui_cmd_obj)
        self.builder.click(ui_cmd_obj, "//button[@class='btn btn-primary ng-binding']")
        # Delete Configure Defender created Network
        self.builder.click(ui_cmd_obj, "[href='#/networks/configure'] [ng-if]",
                           self.builder.constants.STRATEGY_CSS_SELECTOR)
        self.spinner_loading(ui_cmd_obj)
        self.builder.click(ui_cmd_obj, "//div[@class='ui-grid-cell-contents ng-binding' and text()='DFNDR_Service']")
        self.spinner_loading(ui_cmd_obj)
        self.builder.click(ui_cmd_obj, "//button[@class='btn btn-primary exol-tb-btn ng-binding'][2]")
        self.builder.click(ui_cmd_obj, "//button[@class='btn btn-primary ng-binding']")
        self.builder.click(ui_cmd_obj, "//div[@class='menu-name automation-menu-icon-sec-name ng-binding ng-scope' "
                                       "and text()='Configure']")
        # Delete Onboadring -Rules
        self.builder.click(ui_cmd_obj, "//div[@class='menu-name automation-menu-icon-sec-name ng-binding "
                                       "ng-scope' and text()='OnBoard']")
        self.builder.click(ui_cmd_obj, "[href='#/access-control/rules_list']",
                           self.builder.constants.STRATEGY_CSS_SELECTOR)
        self.builder.click(ui_cmd_obj, "//td[@class='ng-binding' and text()='DFNDR_PolicyGeneration_RULE']")
        self.spinner_loading(ui_cmd_obj)
        self.builder.click(ui_cmd_obj, "//i[@class='material-icons ng-scope' and text()='delete']")
        self.spinner_loading(ui_cmd_obj)
        self.builder.click(ui_cmd_obj, "//button[@class='btn btn-primary ng-binding']")
        self.builder.click(ui_cmd_obj, "//div[@class='menu-name automation-menu-icon-sec-name "
                                       "ng-binding ng-scope' and text()='OnBoard']")
        # Delete Policy Roles - Created by Defender
        self.builder.click(ui_cmd_obj, "//div[@class='menu-name automation-menu-icon-sec-name ng-binding ng-scope' "
                                       "and text()='Configure']")
        self.builder.click(ui_cmd_obj, "//ul[@id='side-menu-configure']/li[4]")
        self.builder.click(ui_cmd_obj, "//body/div[4]/md-menu-content[@role='menu']/md-menu-item[1]//a/div[1]")
        self.builder.click(ui_cmd_obj, "//div[1]/div[text()='DFNDR_DenyAll']")
        self.builder.click(ui_cmd_obj, "//button[@class='btn btn-primary exol-tb-btn ng-binding'][2]")
        self.builder.click(ui_cmd_obj, "//button[@class='btn btn-primary automation-role-config-del-btn ng-binding']")
        self.spinner_loading(ui_cmd_obj)
        self.builder.click(ui_cmd_obj, "//div[1]/div[text()='DFNDR_PolicyGeneration']")
        self.builder.click(ui_cmd_obj, "//button[@class='btn btn-primary exol-tb-btn ng-binding'][2]")
        self.builder.click(ui_cmd_obj, "//button[@class='btn btn-primary automation-role-config-del-btn ng-binding']")
        self.spinner_loading(ui_cmd_obj)
        self.builder.click(ui_cmd_obj, "//div[@class='menu-name automation-menu-icon-sec-name ng-binding ng-scope' "
                                       "and text()='Configure']")
        # Delete Onboadring -Groups
        self.builder.click(ui_cmd_obj,
                           "//div[@class='menu-name automation-menu-icon-sec-name ng-binding ng-scope' and "
                           "text()='OnBoard']")
        self.builder.click(ui_cmd_obj, "[href='#/access-control/groups']",
                           self.builder.constants.STRATEGY_CSS_SELECTOR)
        self.builder.click(ui_cmd_obj, "//div[1]/div[text()='DFNDR_PolicyGeneration']")
        self.builder.click(ui_cmd_obj, "(//button[@class='btn btn-primary exol-tb-btn ng-binding'])[4]")
        self.builder.click(ui_cmd_obj, "//button[@class='btn btn-primary ng-binding']")

        return ui_cmd_obj

    def wait_for_page_load_completely(self, ui_cmd_obj):
        self.logger.log_info("waiting for the page to load ...")
        for x in range(1, 25):
            self.base_builder.delay(ui_cmd_obj, 400)
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

    def spinner_loading(self, ui_cmd_obj):
        self.builder.webdriver_wait_until(ui_cmd_obj, "//div[text()='Please Wait...']", retry=5,
                                          strategy=self.builder.constants.STRATEGY_XPATH,
                                          condition=self.builder.constants.CONDITION_INVISIBILITY_OF_ELEMENT)
        return ui_cmd_obj

    def select_country_from_drop_down(self, ui_cmd_obj, arg_dict):
        items = self.builder.find_elements(ui_cmd_obj, "//div[@class='mat-select-content ng-trigger ng-trigger-"
                                                       "fadeInContent']/mat-option[@role='option']")
        for item in items:
            if arg_dict['country_name'] in item.text:
                item.click()
                break
        self.builder.delay(ui_cmd_obj, 5)

        return ui_cmd_obj

    def select_timezone_from_drop_down(self, ui_cmd_obj, arg_dict):
        items = self.builder.find_elements(ui_cmd_obj, "//li[@role='treeitem']")
        for item in items:
            if arg_dict['time_zone'] in item.text:
                item.click()
                break
        self.builder.delay(ui_cmd_obj, 5)

        return ui_cmd_obj
