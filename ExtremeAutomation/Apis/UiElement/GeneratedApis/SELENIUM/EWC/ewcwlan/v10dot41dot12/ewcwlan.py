from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as EwcwlanBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Ewcwlan(EwcwlanBase):
    def wlan_create_wlan(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//input[@type='button' and @value='New']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['ssid'], "//input[@id='ssid']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['wlan_name'], "//input[@id='name']")
        self.builder.click(ui_cmd_obj, "//td[.='" + arg_dict['service_type'] + "']/../td/input[@type='radio']")
        if arg_dict['hotspot']:
            self.builder.click(ui_cmd_obj, "//select[@id='rfsHsType']/option[.='" + arg_dict['hotspot'] + "']")
        if str(arg_dict['status']).lower() == 'disable':
            self.builder.click(ui_cmd_obj, "//input[@type='checkbox' and @id='enable']")
        self.wlan_save_wlan_settings(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def wlan_delete_wlan(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//div[contains(@class, 'accordion-label') and .='WLAN Services']")
        self.builder.click(ui_cmd_obj, "//a[contains(@class, 'cnSiteLink') and .='" + arg_dict['wlan_name'] + "']")
        self.builder.click(ui_cmd_obj, "//input[@name='deleteRfsButton']")
        alt = self.builder.driver.switch_to_alert()
        alt.accept()

        return ui_cmd_obj

    def wlan_save_wlan_settings(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//input[@name='btnSave']")
        return ui_cmd_obj

    def wlan_select_sub_tab(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//a[.='" + arg_dict['tab_name'] + "']")

        return ui_cmd_obj

    def wlan_edit_wlan_name(self, ui_cmd_obj, arg_dict):
        self.builder.enter_text(ui_cmd_obj, arg_dict['wlan_name'], "//*[@id='name']")

        return ui_cmd_obj

    def wlan_edit_ssid(self, ui_cmd_obj, arg_dict):
        self.builder.enter_text(ui_cmd_obj, arg_dict['ssid'], "//*[@id='ssid']")

        return ui_cmd_obj

    def wlan_select_default_topology(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//select[@id='rfsTopology']/option[contains(text(),'" +
                           str(arg_dict['topology_name']) + "')]")

        return ui_cmd_obj

    def wlan_select_default_cos(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//select[@id='rfsCos']/option[@value='" + arg_dict['cos_name'] + "']")

        return ui_cmd_obj

    def wlan_select_default_traffic(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//select[@id='rfsDefaultTrafficMirrorN']/option[.='" +
                           arg_dict['traffic_mode'] + "']")

        return ui_cmd_obj

    def wlan_check_application_visibility(self, ui_cmd_obj, arg_dict):
        self.builder.find_element(ui_cmd_obj, "//input[@name='appVisibility']")
        checkbox = self.builder.driver.find_element_by_xpath("//input[@name='appVisibility']")
        checked = checkbox.get_attribute("checked")
        if not checked:
            self.builder.click(ui_cmd_obj, "//input[@name='appVisibility']")

        return ui_cmd_obj

    def wlan_uncheck_application_visibility(self, ui_cmd_obj, arg_dict):
        self.builder.find_element(ui_cmd_obj, "//input[@name='appVisibility']")
        checkbox = self.builder.driver.find_element_by_xpath("//input[@name='appVisibility']")
        checked = checkbox.get_attribute("checked")
        if checked:
            self.builder.click(ui_cmd_obj, "//input[@name='appVisibility']")

        return ui_cmd_obj

    def wlan_enable_wlan(self, ui_cmd_obj, arg_dict):
        self.builder.find_element(ui_cmd_obj, "//input[@id='enable']")
        checkbox = self.builder.driver.find_element_by_xpath("//input[@id='enable']")
        checked = checkbox.get_attribute("checked")
        if not checked:
            self.builder.click(ui_cmd_obj, "//input[@id='enable']")

        return ui_cmd_obj

    def wlan_disable_wlan(self, ui_cmd_obj, arg_dict):
        self.builder.find_element(ui_cmd_obj, "//input[@id='enable']")
        checkbox = self.builder.driver.find_element_by_xpath("//input[@id='enable']")
        checked = checkbox.get_attribute("checked")
        if checked:
            self.builder.click(ui_cmd_obj, "//input[@id='enable']")

        return ui_cmd_obj

    def wlan_select_privacy_mode(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//b[.='" + arg_dict['privacy_mode'] + "']/ancestor::tr[1]/child::td[1]")
        if 'WPA' not in str(arg_dict['privacy_mode']):
            alt = self.builder.driver.switch_to_alert()
            alt.accept()

        return ui_cmd_obj

    def wlan_select_authentication_mode(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//select[@id='cp_type']/option[.='" + arg_dict['authentication_mode'] + "']")

        return ui_cmd_obj

    def wlan_enable_mac_authentication(self, ui_cmd_obj, arg_dict):
        self.builder.find_element(ui_cmd_obj, "//input[@id='enablemac']")
        checkbox = self.builder.driver.find_element_by_xpath("//input[@id='enablemac']")
        checked = checkbox.get_attribute("checked")
        if not checked:
            self.builder.click(ui_cmd_obj, "//input[@id='enablemac']")

        return ui_cmd_obj

    def wlan_disable_mac_authentication(self, ui_cmd_obj, arg_dict):
        self.builder.find_element(ui_cmd_obj, "//input[@id='enablemac']")
        checkbox = self.builder.driver.find_element_by_xpath("//input[@id='enablemac']")
        checked = checkbox.get_attribute("checked")
        if checked:
            self.builder.click(ui_cmd_obj, "//input[@id='enablemac']")

        return ui_cmd_obj

    def wlan_enable_radius_accounting(self, ui_cmd_obj, arg_dict):
        self.builder.find_element(ui_cmd_obj, "//input[@id='rfsAuthAcctChkbox']")
        checkbox = self.builder.driver.find_element_by_xpath("//input[@id='rfsAuthAcctChkbox']")
        checked = checkbox.get_attribute("checked")
        if not checked:
            self.builder.click(ui_cmd_obj, "//input[@id='rfsAuthAcctChkbox']")

        return ui_cmd_obj

    def wlan_disable_radius_accounting(self, ui_cmd_obj, arg_dict):
        self.builder.find_element(ui_cmd_obj, "//input[@id='rfsAuthAcctChkbox']")
        checkbox = self.builder.driver.find_element_by_xpath("//input[@id='rfsAuthAcctChkbox']")
        checked = checkbox.get_attribute("checked")
        if checked:
            self.builder.click(ui_cmd_obj, "//input[@id='rfsAuthAcctChkbox']")

        return ui_cmd_obj

    def wlan_select_radius_server(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//input[@id='MACNewBtn']")
        display_value = "RADIUS_" + str(arg_dict["radius_server"]).replace(".", "_")
        self.builder.click(ui_cmd_obj, "//div[.='" + display_value + "']")
        self.builder.click(ui_cmd_obj, "//input[@onclick='return fnAddRadius();']")

        return ui_cmd_obj

    def wlan_select_radius_accounting_server(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//input[@id='AccountingNewBtn']")
        display_value = "RADIUS_" + str(arg_dict["radius_accounting_server"]).replace(".", "_")
        self.builder.click(ui_cmd_obj, "//div[.='" + display_value + "']")
        self.builder.click(ui_cmd_obj, "//input[@onclick='return fnAddRadius();']")

        return ui_cmd_obj

    def wlan_select_wep_key_input_method(self, ui_cmd_obj, arg_dict):
        if str(arg_dict['wep_key_input_method']).lower() == 'hex':
            self.builder.click(ui_cmd_obj, "//input[@id='inputMtd' and @value='Hex']")
        if str(arg_dict['wep_key_input_method']).lower() == 'string':
            self.builder.click(ui_cmd_obj, "//input[@id='inputMtd' and @value='Str']")

        return ui_cmd_obj

    def wlan_edit_wep_key_string(self, ui_cmd_obj, arg_dict):
        self.builder.enter_text(ui_cmd_obj, arg_dict['wep_key_string'], "//input[@id='b5s_str']")

        return ui_cmd_obj

    def wlan_click_radius_tlvs_button(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//input[@id='btnRadiusTlvConfig']")

        return ui_cmd_obj

    def wlan_check_ssid_vsa(self, ui_cmd_obj, arg_dict):
        self.builder.find_element(ui_cmd_obj, "//input[@name='vsa_ssid']")
        checkbox = self.builder.driver.find_element_by_xpath("//input[@name='vsa_ssid']")
        checked = checkbox.get_attribute("checked")
        if not checked:
            self.builder.click(ui_cmd_obj, "//input[@name='vsa_ssid']")

        return ui_cmd_obj

    def wlan_uncheck_ssid_vsa(self, ui_cmd_obj, arg_dict):
        self.builder.find_element(ui_cmd_obj, "//input[@name='vsa_ssid']")
        checkbox = self.builder.driver.find_element_by_xpath("//input[@name='vsa_ssid']")
        checked = checkbox.get_attribute("checked")
        if checked:
            self.builder.click(ui_cmd_obj, "//input[@name='vsa_ssid']")

        return ui_cmd_obj

    def wlan_check_ap_name_vsa(self, ui_cmd_obj, arg_dict):
        self.builder.get_attribute_from_element(ui_cmd_obj, "//input[@name='vsa_bp']", "checked")
        if "true" in str(arg_dict["status"]).lower() and not bool(ui_cmd_obj.return_data):
            self.builder.click(ui_cmd_obj, "//input[@name='vsa_bp']")
        elif "false" in str(arg_dict["status"]).lower() and bool(ui_cmd_obj.return_data):
            self.builder.click(ui_cmd_obj, "//input[@name='vsa_bp']")

        return ui_cmd_obj

    def wlan_radius_message_options_popup_click_ok(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//input[@value='OK' and contains(@onclick, 'radiusTlvConfigPopup')]")

        return ui_cmd_obj
