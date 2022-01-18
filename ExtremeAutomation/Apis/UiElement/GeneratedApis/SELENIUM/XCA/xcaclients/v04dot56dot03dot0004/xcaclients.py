from ExtremeAutomation.Apis.UiElement.GeneratedApis.SELENIUM.XCA.xcaclients.v04dot26dot03dot0007.xcaclients import \
    Xcaclients as XcaclientsBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Xcaclients(XcaclientsBase):
    def verify_client_information(self, ui_cmd_obj, arg_dict):
        xpath = "//div[@class='ui-grid-cell-contents ng-binding' and .='" + str(arg_dict["client_mac_address"]) + "']"
        self.verify_client_exists(ui_cmd_obj, arg_dict)
        if ui_cmd_obj.error_state:

            return ui_cmd_obj
        if arg_dict["status"] and ('active' in str(arg_dict["status"]).lower()):
            status_xpath = xpath + "/../../preceding-sibling::div[2]/i[contains(@class, 'exol-status-green')]"
            self.builder.find_element(ui_cmd_obj, status_xpath)
        if arg_dict["ip_address"]:
            ip_xpath = xpath + "/../../preceding-sibling::div[1]//span[.='" + str(arg_dict["ip_address"]) + "']"
            self.builder.find_element(ui_cmd_obj, ip_xpath)
        if arg_dict["host_name"]:
            host_name_xpath = xpath + "/../../following-sibling::div[1]"
            self.builder.get_text_from_element_and_compare(ui_cmd_obj, host_name_xpath, str(arg_dict["host_name"]))
            if ui_cmd_obj.error_state:
                self.logger.log_debug("Host name doesn't match expectation.")

                return ui_cmd_obj
        if arg_dict["device_type"]:
            device_type_xpath = xpath + "/../../following-sibling::div[4]"
            self.builder.get_text_from_element_and_compare(ui_cmd_obj, device_type_xpath, str(arg_dict["device_type"]))
            if ui_cmd_obj.error_state:
                self.logger.log_debug("Device type doesn't match expectation.")

                return ui_cmd_obj
        if arg_dict["ap_name"]:
            ap_name_xpath = xpath + "/../../following-sibling::div[5]"
            self.builder.get_text_from_element_and_compare(ui_cmd_obj, ap_name_xpath, str(arg_dict["ap_name"]))
            if ui_cmd_obj.error_state:
                self.logger.log_debug("AP name doesn't match expectation.")

                return ui_cmd_obj
        if arg_dict["user_name"]:
            user_name_xpath = xpath + "/../../following-sibling::div[7]"
            self.builder.get_text_from_element_and_compare(ui_cmd_obj, user_name_xpath, str(arg_dict["user_name"]))
            if ui_cmd_obj.error_state:
                self.logger.log_debug("User name doesn't match expectation.")

                return ui_cmd_obj
        if arg_dict["role_name"]:
            role_name_xpath = xpath + "/../../following-sibling::div[8]"
            self.builder.get_text_from_element_and_compare(ui_cmd_obj, role_name_xpath, str(arg_dict["role_name"]))
            if ui_cmd_obj.error_state:
                self.logger.log_debug("Role name doesn't match expectation.")

                return ui_cmd_obj
        if arg_dict["network_name"]:
            network_name_xpath = xpath + "/../../following-sibling::div[9]"
            self.builder.get_text_from_element_and_compare(ui_cmd_obj,
                                                           network_name_xpath, str(arg_dict["network_name"]))
            if ui_cmd_obj.error_state:
                self.logger.log_debug("Network name doesn't match expectation.")

                return ui_cmd_obj

        return ui_cmd_obj
