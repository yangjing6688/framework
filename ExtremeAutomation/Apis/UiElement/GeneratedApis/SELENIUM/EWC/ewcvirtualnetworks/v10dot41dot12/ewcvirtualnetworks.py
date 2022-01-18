from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as EwcvirtualnetworksBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Ewcvirtualnetworks(EwcvirtualnetworksBase):
    def virtual_networks_create_vns(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//div[contains(@class, 'accordion-label') and .='Virtual Networks']")
        self.builder.click(ui_cmd_obj, "//input[@type='button' and @onclick='addVns()']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['vns_name'], "//td[.='VNS Name:']/following-sibling::"
                                                                  "td/input[@id='name']")
        self.builder.click(ui_cmd_obj, "//td[.='WLAN Service:']/following-sibling::"
                                       "td/select[@id='rfs']/option[.='" + arg_dict['wlan_service'] + "']")
        if arg_dict['non_auth_policy_name']:
            self.builder.click(ui_cmd_obj, "//select[@id='non_auth']/option[.='" +
                               arg_dict['non_auth_policy_name'] + "']")
        if arg_dict['auth_policy_name']:
            self.builder.click(ui_cmd_obj, "//select[@id='auth']/option[.='" + arg_dict['auth_policy_name'] + "']")
        if str(arg_dict['status']).lower() == 'disable':
            self.builder.click(ui_cmd_obj, "//input[@type='checkbox' and @name='enabled']")
            self.builder.delay(ui_cmd_obj, 1000)
        self.virtual_networks_click_save_button(ui_cmd_obj, arg_dict)
        self.virtual_networks_vns_should_exist(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def virtual_networks_vns_should_be_enabled(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//div[contains(@class, 'accordion-label') and .='Virtual Networks']")
        self.builder.click(ui_cmd_obj, "//a[contains(@class, 'cnSiteLink') and .='" + arg_dict['vns_name'] + "']")
        checkbox = self.builder.driver.find_element_by_xpath("//input[@type='checkbox' and @name='enabled']")
        checked = checkbox.get_attribute("checked")
        if checked:
            self.logger.log_debug("VNS " + str(arg_dict["vns_name"]) + " is enabled.")
        else:
            self.logger.log_debug("VNS " + str(arg_dict["vns_name"]) + " is disable.")
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def virtual_networks_edit_wlan_service_in_vns(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//div[contains(@class, 'accordion-label') and .='Virtual Networks']")
        self.builder.click(ui_cmd_obj, "//a[contains(@class, 'cnSiteLink') and .='" + arg_dict['vns_name'] + "']")
        self.builder.click(ui_cmd_obj, "//td[.='WLAN Service:']/following-sibling::td/select[@id='rfs']/option[.='" +
                           arg_dict['wlan_name'] + "']")
        self.virtual_networks_click_save_button(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def virtual_networks_edit_non_authenticated_policy_role_in_vns(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//div[contains(@class, 'accordion-label') and .='Virtual Networks']")
        self.builder.click(ui_cmd_obj, "//a[contains(@class, 'cnSiteLink') and .='" + arg_dict['vns_name'] + "']")
        self.builder.click(ui_cmd_obj, "//select[@id='non_auth']/option[.='" + arg_dict['non_auth_policy_name'] + "']")
        self.virtual_networks_click_save_button(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def virtual_networks_edit_authenticated_policy_role_in_vns(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//div[contains(@class, 'accordion-label') and .='Virtual Networks']")
        self.builder.click(ui_cmd_obj, "//a[contains(@class, 'cnSiteLink') and .='" + arg_dict['vns_name'] + "']")
        self.builder.click(ui_cmd_obj, "//select[@id='auth']/option[.='" + arg_dict['auth_policy_name'] + "']")
        self.virtual_networks_click_save_button(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def virtual_networks_delete_vns(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//div[contains(@class, 'accordion-label') and .='Virtual Networks']")
        self.builder.click(ui_cmd_obj, "//a[contains(@class, 'cnSiteLink') and .='" + arg_dict['vns_name'] + "']")
        self.builder.click(ui_cmd_obj, "//input[@type='button' and @name='deleteVnsButton']")
        alt = self.builder.driver.switch_to_alert()
        alt.accept()
        self.virtual_networks_vns_should_not_exist(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def virtual_networks_vns_should_exist(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//div[contains(@class, 'accordion-label') and .='Virtual Networks']")
        self.builder.get_text_from_element_and_compare(ui_cmd_obj, "//table[@id='vnsListtable']//div[.='" +
                                                       arg_dict['vns_name'] + "']", arg_dict['vns_name'])
        if ui_cmd_obj.error_state is False:
            self.logger.log_debug("VNS " + str(arg_dict["vns_name"]) + " exists.")
        else:
            self.logger.log_debug("VNS " + str(arg_dict["vns_name"]) + " DOES NOT exist!")

        return ui_cmd_obj

    def virtual_networks_vns_should_not_exist(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//div[contains(@class, 'accordion-label') and .='Virtual Networks']")
        self.builder.get_text_from_element_and_compare(ui_cmd_obj, "//table[@id='vnsListtable']//div[.='" +
                                                       arg_dict['vns_name'] + "']", arg_dict['vns_name'])
        if ui_cmd_obj.error_state is True:
            self.logger.log_debug("VNS " + str(arg_dict["vns_name"]) + " does not exist.")
            ui_cmd_obj.error_state = False
        else:
            self.logger.log_debug("VNS " + str(arg_dict["vns_name"]) + " EXISTS!")
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def virtual_networks_click_save_button(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//input[@type='submit' and @name='btnSave']")

        return ui_cmd_obj
