from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as XcaclientsBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Xcaclients(XcaclientsBase):
    def select_all_clients(self, ui_cmd_obj, arg_dict):
        self.builder.get_attribute_from_element_and_compare(ui_cmd_obj,
                                                            "//md-checkbox[@ng-model='grid.selection.selectAll']",
                                                            "aria-checked", "true")
        if ui_cmd_obj.error_state:
            ui_cmd_obj.error_state = False
            self.builder.click(ui_cmd_obj, "//md-checkbox[@ng-model='grid.selection.selectAll']")

        return ui_cmd_obj

    def click_client_mac_address_to_open_client_info(self, ui_cmd_obj, arg_dict):
        self.verify_client_exists(ui_cmd_obj, arg_dict)
        if not ui_cmd_obj.error_state:
            self.builder.click(ui_cmd_obj, "//div[@class='ui-grid-cell-contents ng-binding' and .='" +
                               str(arg_dict["client_mac_address"]) + "']")

        return ui_cmd_obj

    def refresh_clients_page(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//button[@aria-label='refresh']")

        return ui_cmd_obj

    def verify_client_exists(self, ui_cmd_obj, arg_dict):
        self.builder.find_element(ui_cmd_obj, "//div[@class='ui-grid-cell-contents ng-binding' and .='" +
                                  str(arg_dict["client_mac_address"]) + "']")
        if ui_cmd_obj.error_state:
            self.logger.log_debug("Client with mac address " + str(arg_dict["client_mac_address"]) + " doesn't exist.")
        else:
            self.logger.log_debug("Client with mac address " + str(arg_dict["client_mac_address"]) + " exists.")

        return ui_cmd_obj

    def verify_client_does_not_exist(self, ui_cmd_obj, arg_dict):
        self.builder.find_element(ui_cmd_obj, "//div[@class='ui-grid-cell-contents ng-binding' and .='" +
                                  str(arg_dict["client_mac_address"]) + "']")
        if ui_cmd_obj.error_state:
            ui_cmd_obj.error_state = False
            self.logger.log_debug("Client with mac address " + str(arg_dict["client_mac_address"]) + " doesn't exist.")
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_debug("Client with mac address " + str(arg_dict["client_mac_address"]) + " still exists.")

        return ui_cmd_obj

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
            device_type_xpath = xpath + "/../../following-sibling::div[3]"
            self.builder.get_text_from_element_and_compare(ui_cmd_obj, device_type_xpath, str(arg_dict["device_type"]))
            if ui_cmd_obj.error_state:
                self.logger.log_debug("Device type doesn't match expectation.")

                return ui_cmd_obj
        if arg_dict["ap_name"]:
            ap_name_xpath = xpath + "/../../following-sibling::div[4]"
            self.builder.get_text_from_element_and_compare(ui_cmd_obj, ap_name_xpath, str(arg_dict["ap_name"]))
            if ui_cmd_obj.error_state:
                self.logger.log_debug("AP name doesn't match expectation.")

                return ui_cmd_obj
        if arg_dict["user_name"]:
            user_name_xpath = xpath + "/../../following-sibling::div[6]"
            self.builder.get_text_from_element_and_compare(ui_cmd_obj, user_name_xpath, str(arg_dict["user_name"]))
            if ui_cmd_obj.error_state:
                self.logger.log_debug("User name doesn't match expectation.")

                return ui_cmd_obj
        if arg_dict["role_name"]:
            role_name_xpath = xpath + "/../../following-sibling::div[7]"
            self.builder.get_text_from_element_and_compare(ui_cmd_obj, role_name_xpath, str(arg_dict["role_name"]))
            if ui_cmd_obj.error_state:
                self.logger.log_debug("Role name doesn't match expectation.")

                return ui_cmd_obj
        if arg_dict["network_name"]:
            network_name_xpath = xpath + "/../../following-sibling::div[8]"
            self.builder.get_text_from_element_and_compare(ui_cmd_obj,
                                                           network_name_xpath, str(arg_dict["network_name"]))
            if ui_cmd_obj.error_state:
                self.logger.log_debug("Network name doesn't match expectation.")

                return ui_cmd_obj

        return ui_cmd_obj
