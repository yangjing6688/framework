from ExtremeAutomation.Apis.UiElement.GeneratedApis.SELENIUM.EMC.engines.v8dot1dot3.engines import Engines as \
    EnginesBase
# All imports above this line will be removed after generation.
# User imports must be added below.
from selenium.webdriver.common.action_chains import ActionChains


class Engines(EnginesBase):
    def engines_add_engine_properties(self, ui_cmd_obj, arg_dict):
        self.builder.get_attribute_from_element_and_compare(ui_cmd_obj,
                                                            "//span[contains(@class, 'x-tree-node-text') "
                                                            "and .='Default']/../../..", "aria-expanded", "true")
        if ui_cmd_obj.error_state is True:
            ui_cmd_obj.error_state = False
            self.builder.click(ui_cmd_obj,
                               "//span[contains(@class, 'x-tree-node-text') and .='Default']/preceding-sibling::div[2]")
        self.builder.get_attribute_from_element_and_compare(ui_cmd_obj,
                                                            "//span[contains(@class, 'x-tree-node-text') "
                                                            "and .='All Engines']/../../..", "aria-expanded", "false")
        if ui_cmd_obj.error_state is True:
            ui_cmd_obj.error_state = False
            self.builder.click(ui_cmd_obj, "//span[contains(@class, 'x-tree-node-text') and  .='All Engines']")
        self.builder.right_click(ui_cmd_obj, "//span[.='" + str(arg_dict["primary_engine_name"]) +
                                 "/" + str(arg_dict["primary_engine_ip"]) + "']")
        self.builder.click(ui_cmd_obj, "//div[@role='menu' and @aria-hidden='false']//a[@role='menuitem' "
                                       "and .='Engine Properties...']")
        self.builder.click(ui_cmd_obj, "//span[contains(@class, 'x-btn-inner-default-toolbar-small') and .='Add']")
        self.builder.enter_text(ui_cmd_obj, str(arg_dict["property_name"]), "//input[@name='name' and @role='textbox']")
        self.builder.click(ui_cmd_obj, "//div[@class='x-column-header-text' and .='Name']")
        self.builder.double_click(ui_cmd_obj, "//div[.='" + str(arg_dict["property_name"]) +
                                  "']/../following-sibling::td/div")
        self.builder.enter_text(ui_cmd_obj, str(arg_dict["property_value"]),
                                "//input[@name='value' and @role='textbox']")
        self.builder.click(ui_cmd_obj, "//span[contains(@class,'x-btn-button-blue-small') and .='Save']")

        return ui_cmd_obj

    def engines_remove_engine_properties(self, ui_cmd_obj, arg_dict):
        self.builder.get_attribute_from_element_and_compare(ui_cmd_obj,
                                                            "//span[contains(@class, 'x-tree-node-text') "
                                                            "and .='Default']/../../..", "aria-expanded", "true")
        if ui_cmd_obj.error_state is True:
            ui_cmd_obj.error_state = False
            self.builder.click(ui_cmd_obj, "//span[contains(@class, 'x-tree-node-text') "
                                           "and .='Default']/preceding-sibling::div[2]")
        self.builder.get_attribute_from_element_and_compare(ui_cmd_obj,
                                                            "//span[contains(@class, 'x-tree-node-text') "
                                                            "and .='All Engines']/../../..", "aria-expanded", "false")
        if ui_cmd_obj.error_state is True:
            ui_cmd_obj.error_state = False
            self.builder.click(ui_cmd_obj, "//span[contains(@class, 'x-tree-node-text') and .='All Engines']")
        self.builder.right_click(ui_cmd_obj, "//span[.='" +
                                 str(arg_dict["primary_engine_name"]) + "/" + str(arg_dict["primary_engine_ip"]) + "']")
        self.builder.click(ui_cmd_obj,
                           "//div[@role='menu' and @aria-hidden='false']//a[@role='menuitem' "
                           "and .='Engine Properties...']")
        self.builder.click(ui_cmd_obj, "//td[@role='gridcell' and .='" + str(arg_dict["property_name"]) + "']")
        self.builder.click(ui_cmd_obj, "//a[contains(@class, 'x-btn-default-toolbar-small') and .='Remove']")
        self.builder.click(ui_cmd_obj, "//span[contains(@class,'x-btn-button-blue-small') and .='Save']")

        return ui_cmd_obj

    def engines_gim_default_validation_gim_tab(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//span[text()='Control']")
        self.builder.click(ui_cmd_obj, "//span[text()='Access Control']")
        web_obj = self.builder.find_element(ui_cmd_obj, "Guest and IoT Managers",
                                            self.builder.constants.STRATEGY_LINK_TEXT)
        return_text = self.base_builder.get_attribute_from_element(ui_cmd_obj, web_obj, "aria-selected")
        self.logger.log_info(return_text)
        if return_text != "true":
            ui_cmd_obj.error_state = False
        else:
            ui_cmd_obj.error_state = True
        # After Click on tab and Guest And IOT Managers  - Enabled
        self.builder.click(ui_cmd_obj, "Guest and IoT Managers", self.builder.constants.STRATEGY_LINK_TEXT)
        web_obj = self.builder.find_element(ui_cmd_obj, "Guest and IoT Managers",
                                            self.builder.constants.STRATEGY_LINK_TEXT)
        return_text = self.base_builder.get_attribute_from_element(ui_cmd_obj, web_obj, "aria-selected")
        self.logger.log_info(return_text)
        if return_text != "true":
            ui_cmd_obj.error_state = True
        else:
            ui_cmd_obj.error_state = False

        return ui_cmd_obj

    def engines_gim_default_buttons_validation(self, ui_cmd_obj, arg_dict):
        # Default status of Add, Edit and Delete buttons -- Add
        web_obj = self.builder.find_element(ui_cmd_obj, "Add...", self.builder.constants.STRATEGY_LINK_TEXT)
        return_text = self.base_builder.get_attribute_from_element(ui_cmd_obj, web_obj, "aria-disabled")
        self.logger.log_info(return_text)
        if return_text != "true":
            ui_cmd_obj.error_state = False
        else:
            ui_cmd_obj.error_state = True
        # Default status of  -- Edit
        web_obj = self.builder.find_element(ui_cmd_obj, "Edit...",
                                            self.builder.constants.STRATEGY_LINK_TEXT)
        return_text = self.base_builder.get_attribute_from_element(ui_cmd_obj, web_obj, "aria-disabled")
        self.logger.log_info(return_text)
        if return_text:
            ui_cmd_obj.error_state = False
        else:
            ui_cmd_obj.error_state = True
        # Default status of -- Delete
        web_obj = self.builder.find_element(ui_cmd_obj, "Delete",
                                            self.builder.constants.STRATEGY_LINK_TEXT)
        return_text = self.base_builder.get_attribute_from_element(ui_cmd_obj, web_obj, "aria-disabled")
        self.logger.log_info(return_text)
        if return_text:
            ui_cmd_obj.error_state = False
        else:
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def engines_gim_add_gim_ip(self, ui_cmd_obj, arg_dict):
        # adding _gim_ip
        if arg_dict['delete_row'] == 'yes':
            self.builder.click(ui_cmd_obj, "//table[@role='presentation']//div[.='" + arg_dict['ip_address'] + "']")
            self.builder.click(ui_cmd_obj, "Delete", self.builder.constants.STRATEGY_LINK_TEXT)
            self.builder.click(ui_cmd_obj, "div[id^='messagebox-'] a:nth-child(2)",
                               self.builder.constants.STRATEGY_CSS_SELECTOR)
        self.builder.click(ui_cmd_obj, "Add...", self.builder.constants.STRATEGY_LINK_TEXT)
        self.builder.enter_text(ui_cmd_obj, arg_dict['ip_address'], "//input[@name='ipAddress']")
        self.builder.enter_text(ui_cmd_obj, "GIM", "//input[@name='name']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['secret'], "//input[@name='secret']")
        self.builder.click(ui_cmd_obj, "div[id^='addEditGimManagersPanel'] a:nth-child(1)",
                           self.builder.constants.STRATEGY_CSS_SELECTOR)
        self.builder.click(ui_cmd_obj, "//span[text()='OK']")
        self.builder.delay(ui_cmd_obj, 5)
        self.builder.click(ui_cmd_obj, "//table[@role='presentation']//div[.='" + arg_dict['ip_address'] + "']")
        # Checking Edit Option is enabled once after adding GIM ipaddress
        web_obj = self.builder.find_element(ui_cmd_obj, "Edit...",
                                            self.builder.constants.STRATEGY_LINK_TEXT)
        return_text = self.base_builder.get_attribute_from_element(ui_cmd_obj, web_obj, "aria-disabled")
        self.logger.log_info(return_text)
        if return_text != "true":
            ui_cmd_obj.error_state = False
        else:
            ui_cmd_obj.error_state = True
        # Checking Delete Option is enabled after adding GIM ip address
        web_obj = self.builder.find_element(ui_cmd_obj, "Delete",
                                            self.builder.constants.STRATEGY_LINK_TEXT)
        return_text = self.base_builder.get_attribute_from_element(ui_cmd_obj, web_obj, "aria-disabled")
        self.logger.log_info(return_text)
        if return_text != "true":
            ui_cmd_obj.error_state = False
        else:
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def engines_gim_edit_gim_ip(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//table[@role='presentation']//div[.='" + arg_dict['ip_address'] + "']")
        self.builder.click(ui_cmd_obj, "Edit...", self.builder.constants.STRATEGY_LINK_TEXT)
        self.builder.delay(ui_cmd_obj, 5)
        web_obj = self.builder.find_element(ui_cmd_obj, "//input[@name='secret']")
        self.base_builder.click(ui_cmd_obj, web_obj)
        self.builder.delay(ui_cmd_obj, 5)
        self.builder.enter_text(ui_cmd_obj, arg_dict["edit_secret"], "//input[@name='secret']", clear_existing=True)
        self.builder.click(ui_cmd_obj, "div[id^='addEditGimManagersPanel'] a:nth-child(1)",
                           self.builder.constants.STRATEGY_CSS_SELECTOR)
        self.builder.click(ui_cmd_obj, "//span[text()='OK']")

        return ui_cmd_obj

    def engines_gim_delete_gim_ip(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//table[@role='presentation']//div[.='" + arg_dict['ip_address'] + "']")
        self.builder.click(ui_cmd_obj, "Delete", self.builder.constants.STRATEGY_LINK_TEXT)
        self.builder.click(ui_cmd_obj, "div[id^='messagebox-'] a:nth-child(2)",
                           self.builder.constants.STRATEGY_CSS_SELECTOR)

        return ui_cmd_obj

    def engines_gim_default_validation_details_tab(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//span[text()='Details']")
        self.builder.delay(ui_cmd_obj, 5)
        # Validate Guest and IoT Manager panel exists
        self.builder.element_exists(ui_cmd_obj, "[data-componentid] .x-autocontainer-innerCt:nth-of-type(1) "
                                                "[role='presentation']:nth-of-type(6)",
                                                self.builder.constants.STRATEGY_CSS_SELECTOR)
        # Validate Guest and IOT configuration text in panel
        self.builder.get_text_from_element_and_compare(ui_cmd_obj, "[data-componentid] [role='presentation']:"
                                                                   "nth-of-type(6) > [role='presentation']:"
                                                                   "nth-of-type(1) .x-box-inner [role] [role]"
                                                                   " [unselectable]", arg_dict["gim_conf_text"],
                                                                   self.builder.constants.STRATEGY_CSS_SELECTOR)
        # Validate Edit button exist or not
        self.builder.element_exists(ui_cmd_obj, "[data-componentid] [role='presentation']:nth-of-type(6) [hidefocus]",
                                                self.builder.constants.STRATEGY_CSS_SELECTOR)

        # Validate default domain label and LPR label
        self.builder.element_exists(ui_cmd_obj, "[data-componentid] [role='presentation']:nth-of-type(6) "
                                                "[role='presentation']:nth-of-type(1) > .x-table-layout-cell:"
                                                "nth-of-type(1)",
                                                self.builder.constants.STRATEGY_CSS_SELECTOR)
        self.builder.element_exists(ui_cmd_obj, "[data-componentid] [role='presentation']:nth-of-type(6) "
                                                "[role='presentation']:nth-of-type(1) > .x-table-layout-cell:"
                                                "nth-of-type(2)",
                                                self.builder.constants.STRATEGY_CSS_SELECTOR)
        # Validate domain and LPR names
        self.builder.get_text_from_element_and_compare(ui_cmd_obj, "[data-componentid] [role='presentation']:"
                                                                   "nth-of-type(6) [role='presentation']:"
                                                                   "nth-of-type(1) > .x-table-layout-cell:"
                                                                   "nth-of-type(2)", arg_dict["domain_name"],
                                                                   self.builder.constants.STRATEGY_CSS_SELECTOR)
        self.builder.get_text_from_element_and_compare(ui_cmd_obj, "[data-componentid] [role='presentation']:"
                                                                   "nth-of-type(6) [role='presentation']:"
                                                                   "nth-of-type(2) > .x-table-layout-cell:"
                                                                   "nth-of-type(2)", arg_dict["lpr_name"],
                                                                   self.builder.constants.STRATEGY_CSS_SELECTOR)
        self.gim_enforce(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def engines_gim_add_domain(self, ui_cmd_obj, arg_dict):
        self.gim_create_domain(ui_cmd_obj, arg_dict)
        self.gim_enforce(ui_cmd_obj, arg_dict)
        self.builder.delay(ui_cmd_obj, 5)

        return ui_cmd_obj

    def engines_gim_click_on_edit_png(self, ui_cmd_obj, element_locator, strategy):
        element = self.builder.find_element(ui_cmd_obj, element_locator, strategy)
        size = element.size
        action_chain = ActionChains(self.builder.driver)
        action_chain.move_to_element_with_offset(element, size['width'], 0)
        action_chain.click()
        action_chain.perform()

        return ui_cmd_obj

    def engines_gim_create_domain(self, ui_cmd_obj, arg_dict):
        # custom domain to default LPR
        self.gim_details_domain(ui_cmd_obj, arg_dict)
        self.builder.click(ui_cmd_obj, "//li/div/em/b[text()='New...']")
        self.builder.click(ui_cmd_obj, "//input[@name='gimDomain']", self.builder.constants.STRATEGY_XPATH)
        self.builder.enter_text(ui_cmd_obj, arg_dict['domain_name'], "//input[@name='gimDomain']")
        self.builder.click(ui_cmd_obj, "//input[@name='localPasswordRepo']")
        self.builder.click(ui_cmd_obj, "//li/div[text()='Default']")
        self.builder.click(ui_cmd_obj, "div[id^='gimDomainDialog'] [id$='bodyWrap'] a:nth-child(1)",
                           self.builder.constants.STRATEGY_CSS_SELECTOR)
        self.builder.delay(ui_cmd_obj, 5)
        self.builder.click(ui_cmd_obj, "div[id^='editGimConfigurationPanel'] [id$='bodyWrap'] a:nth-child(1)",
                           self.builder.constants.STRATEGY_CSS_SELECTOR)
        self.builder.delay(ui_cmd_obj, 5)

        return ui_cmd_obj

    def engines_gim_details_domain(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//span[text()='Details']")
        self.builder.click(ui_cmd_obj, "//span[text()='Edit...']")
        self.builder.click(ui_cmd_obj, "//input[@name='domain']")
        self.builder.delay(ui_cmd_obj, 5)

        return ui_cmd_obj

    def engines_gim_enforce(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//span[text()='Enforce']")
        self.builder.click(ui_cmd_obj, "//span[text()='All...']")
        self.builder.click(ui_cmd_obj, "//span[text()='Enforce All']")
        self.builder.delay(ui_cmd_obj, 10)
        self.builder.click(ui_cmd_obj, "//span[text()='Close']")
        self.builder.delay(5)
        self.builder.click(ui_cmd_obj, ".x-btn-extr-nav-action-embedded-toolbar-selectionless-button-small "
                           "[data-ref='btnEl']", self.builder.constants.STRATEGY_CSS_SELECTOR)
        self.builder.click(ui_cmd_obj, "//a/span[text()='Logout']")
        self.builder.delay(ui_cmd_obj, 5)

        return ui_cmd_obj

    def engines_gim_map_domain_lpr_none(self, ui_cmd_obj, arg_dict):
        # custom domain to None
        self.gim_details_domain(ui_cmd_obj, arg_dict)
        self.click_on_edit_png(ui_cmd_obj, "//li/div[text()='" + arg_dict['domain_name'] + "']",
                               self.builder.constants.STRATEGY_XPATH)
        self.builder.click(ui_cmd_obj, "//input[@name='localPasswordRepo']")
        self.builder.click(ui_cmd_obj, "//ul[starts-with(@id, 'localPasswordRepoCombo')]/li/"
                                       "div[text()='" + arg_dict['lpr_name'] + "']")
        self.builder.click(ui_cmd_obj, "div[id^='gimDomainDialog'] [id$='bodyWrap'] a:nth-child(1)",
                           self.builder.constants.STRATEGY_CSS_SELECTOR)
        self.builder.delay(ui_cmd_obj, 5)
        if not arg_dict['lpr_name'] == "None":
            self.builder.click(ui_cmd_obj, "//input[@name='domain']")
            self.builder.click(ui_cmd_obj, "//ul[starts-with(@id, 'gimDomainCombo')]/li/"
                                           "div[text()='" + arg_dict['domain_name'] + "']")
            self.builder.delay(ui_cmd_obj, 5)
        self.builder.click(ui_cmd_obj, "//span[text()='OK']")
        self.builder.click(ui_cmd_obj, "div[id^='editGimConfigurationPanel'] [id$='bodyWrap'] a:nth-child(1)",
                           self.builder.constants.STRATEGY_CSS_SELECTOR)
        self.builder.delay(ui_cmd_obj, 5)
        self.gim_enforce(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def engines_gim_duplicate_ip(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "Add...", self.builder.constants.STRATEGY_LINK_TEXT)
        self.builder.enter_text(ui_cmd_obj, arg_dict['ip_address'], "//input[@name='ipAddress']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['secret'], "//input[@name='secret']")
        self.builder.click(ui_cmd_obj, "div[id^='addEditGimManagersPanel'] a:nth-child(1)",
                           self.builder.constants.STRATEGY_CSS_SELECTOR)
        self.builder.click(ui_cmd_obj, "//span[text()='OK']")
        self.builder.delay(ui_cmd_obj, 5)
        web_obj = self.builder.find_element(ui_cmd_obj, ".x-window-text", self.builder.constants.STRATEGY_CSS_SELECTOR)
        if self.base_builder.get_text_from_element(ui_cmd_obj, web_obj) == "This IP Address is present " \
                                                                           "in Engine Group: Default":
            ui_cmd_obj.error_state = False
        else:
            ui_cmd_obj.error_state = True
        self.builder.click(ui_cmd_obj, "div[id^='messagebox'] [id$='header-innerCt'] >div>div:nth-child(2)",
                           self.builder.constants.STRATEGY_CSS_SELECTOR)
        self.builder.click(ui_cmd_obj, "div[id^='addEditGimManagersPanel'] a:nth-child(2)",
                           self.builder.constants.STRATEGY_CSS_SELECTOR)

        return ui_cmd_obj

    def engines_gim_select_row_from_lpr_table(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "Add...", self.builder.constants.STRATEGY_LINK_TEXT)
        self.builder.enter_text(ui_cmd_obj, arg_dict['ip_address'], "//input[@name='ipAddress']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['secret'], "//input[@name='secret']")
        self.builder.click(ui_cmd_obj, "div[id^='addEditGimManagersPanel'] a:nth-child(1)",
                           self.builder.constants.STRATEGY_CSS_SELECTOR)
        self.builder.click(ui_cmd_obj, "//span[text()='OK']")
        self.builder.delay(ui_cmd_obj, 5)
        web_obj = self.builder.find_element(ui_cmd_obj, ".x-window-text", self.builder.constants.STRATEGY_CSS_SELECTOR)
        if self.base_builder.get_text_from_element(ui_cmd_obj, web_obj) == "This IP Address is present " \
                                                                           "in Engine Group: Default":
            ui_cmd_obj.error_state = False
        else:
            ui_cmd_obj.error_state = True
        self.builder.click(ui_cmd_obj, "div[id^='messagebox'] [id$='header-innerCt'] >div>div:nth-child(2)",
                           self.builder.constants.STRATEGY_CSS_SELECTOR)
        self.builder.click(ui_cmd_obj, "div[id^='addEditGimManagersPanel'] a:nth-child(2)",
                           self.builder.constants.STRATEGY_CSS_SELECTOR)

        return ui_cmd_obj

    def engines_gim_select_row_from_manage_table(self, ui_cmd_obj, arg_dict):
        self.builder.delay(ui_cmd_obj, 5)
        for index in range(1, 10):
            web_obj = self.builder.find_elements(ui_cmd_obj, "//div[@class='x-panel-body x-grid-with-row-lines "
                                                             "x-grid-body x-panel-body-default x-panel-body-default']/"
                                                             "div/div/table[" + str(index) + "]/tbody/tr/td[1]")
            return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
            self.logger.log_info("domain_name: " + str(index) + "::" + return_text)
            if return_text == arg_dict['domain_name']:
                self.builder.click(ui_cmd_obj, "//div[@class='x-panel-body x-grid-with-row-lines "
                                               "x-grid-body x-panel-body-default x-panel-body-default']/"
                                               "div/div/table[" + str(index) + "]/tbody/tr/td[1]")
                ui_cmd_obj.error_state = False
                break
            else:
                ui_cmd_obj.error_state = True

        return ui_cmd_obj
