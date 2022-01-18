from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as XcavlansBase
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


class Xcavlans(XcavlansBase):
    def click_add_to_create_new_vlan(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//button[@ng-click='$parent.onCreate()']")

        return ui_cmd_obj

    def click_vlan_name_to_open_vlan_settings(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//div[@class='ui-grid-cell-contents ng-binding ng-scope' and .='" +
                           str(arg_dict['vlan_name']) + "']")

        return ui_cmd_obj

    def edit_info_for_vlan_in_bridged_at_ac_mode(self, ui_cmd_obj, arg_dict):
        if arg_dict["vlan_name"]:
            self.builder.enter_text(ui_cmd_obj, arg_dict["vlan_name"], "//input[@placeholder='VLAN Name']")
        self.builder.click(ui_cmd_obj, "//select[@id='topologyMode']/option[@value='string:BridgedAtAc']")
        self.builder.get_attribute_from_element_and_compare(ui_cmd_obj,
                                                            "//md-checkbox[@name='topologyTagged']",
                                                            "aria-checked", "true")
        if (not ui_cmd_obj.error_state) and arg_dict["vlan_id"]:
            self.builder.enter_text(ui_cmd_obj, arg_dict["vlan_id"], "//input[@id='topologyVlanID']")
        elif ui_cmd_obj.error_state and arg_dict["vlan_id"]:
            self.builder.click(ui_cmd_obj, "//md-checkbox[@name='topologyTagged']")
            self.builder.enter_text(ui_cmd_obj, arg_dict["vlan_id"], "//input[@id='topologyVlanID']")
        if StringUtils.string_to_boolean(arg_dict['is_tagged']) is ui_cmd_obj.error_state:
            self.builder.click(ui_cmd_obj, "//md-checkbox[@name='topologyTagged']")
        ui_cmd_obj.error_state = False
        if arg_dict["topology_port"]:
            self.builder.click(ui_cmd_obj, "//select[@id='topologyPort']/option[@label='" +
                               arg_dict["topology_port"] + "']")

        return ui_cmd_obj

    def edit_info_for_vlan_in_bridged_at_ap_mode(self, ui_cmd_obj, arg_dict):
        if arg_dict["vlan_name"]:
            self.builder.enter_text(ui_cmd_obj, arg_dict["vlan_name"], "//input[@placeholder='VLAN Name']")
        self.builder.click(ui_cmd_obj, "//select[@id='topologyMode']/option[@value='string:BridgedAtAp']")
        self.builder.get_attribute_from_element_and_compare(ui_cmd_obj,
                                                            "//md-checkbox[@name='topologyTagged']",
                                                            "aria-checked", "true")
        if (not ui_cmd_obj.error_state) and arg_dict["vlan_id"]:
            self.builder.enter_text(ui_cmd_obj, arg_dict["vlan_id"], "//input[@id='topologyVlanID']")
        elif ui_cmd_obj.error_state and arg_dict["vlan_id"]:
            self.builder.click(ui_cmd_obj, "//md-checkbox[@name='topologyTagged']")
            self.builder.enter_text(ui_cmd_obj, arg_dict["vlan_id"], "//input[@id='topologyVlanID']")
        if StringUtils.string_to_boolean(arg_dict['is_tagged']) is ui_cmd_obj.error_state:
            self.builder.click(ui_cmd_obj, "//md-checkbox[@name='topologyTagged']")
        ui_cmd_obj.error_state = False

        return ui_cmd_obj

    def edit_info_for_vlan_in_fabric_attach_mode(self, ui_cmd_obj, arg_dict):
        if arg_dict["vlan_name"]:
            self.builder.enter_text(ui_cmd_obj, arg_dict["vlan_name"], "//input[@placeholder='VLAN Name']")
        self.builder.click(ui_cmd_obj, "//select[@id='topologyMode']/option[@value='string:FabricAttach']")
        if arg_dict["vlan_id"]:
            self.builder.enter_text(ui_cmd_obj, arg_dict["vlan_id"], "//input[@id='topologyVlanID']")
        if arg_dict["isid"]:
            self.builder.enter_text(ui_cmd_obj, arg_dict["isid"], "//input[@id='isid']")

        return ui_cmd_obj

    def edit_advanced_settings_for_vlan(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            return super(Xcavlans, self).edit_advanced_settings_for_vlan(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def edit_layer3_settings_for_vlan(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            return super(Xcavlans, self).edit_layer3_settings_for_vlan(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def config_dhcp_relay_servers(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            return super(Xcavlans, self).config_dhcp_relay_servers(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def config_dhcp_local_server(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            return super(Xcavlans, self).config_dhcp_local_server(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def save_settings_and_back_to_vlans_page(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//button[@ng-click='$parent.save()' and @aria-hidden='false']")
        self.builder.delay(ui_cmd_obj, 2000)
        self.builder.click(ui_cmd_obj, "//button[@ng-click='setBack()']")
        self.builder.delay(ui_cmd_obj, 2000)

        return ui_cmd_obj

    def delete_existing_vlan(self, ui_cmd_obj, arg_dict):
        self.click_vlan_name_to_open_vlan_settings(ui_cmd_obj, arg_dict)
        self.builder.click(ui_cmd_obj, "//button[@ng-click='$parent.showDelete()']")
        self.builder.click(ui_cmd_obj, "//button[@ng-click='closeDialog(true)']")
        self.builder.delay(ui_cmd_obj, 2000)

        return ui_cmd_obj

    def verify_vlan_exists(self, ui_cmd_obj, arg_dict):
        xpath = "//*[contains(@role, 'gridcell') and normalize-space(.)='" + arg_dict['vlan_name'] + "']"
        self.builder.find_element(ui_cmd_obj, xpath)
        if ui_cmd_obj.error_state:
            self.logger.log_debug("Vlan " + str(arg_dict["vlan_name"]) + " doesn't exist.")

            return ui_cmd_obj
        self.builder.get_text_from_element_and_compare(ui_cmd_obj, xpath +
                                                       "/following-sibling::div[1]", arg_dict['vlan_mode'])
        if ui_cmd_obj.error_state:
            self.logger.log_debug("Vlan mode doesn't match expectation.")

            return ui_cmd_obj
        self.builder.find_element(ui_cmd_obj, xpath + "/following-sibling::div[2]/i[@ng-if='row.entity.tagged']")
        if ui_cmd_obj.error_state and not StringUtils.string_to_boolean(arg_dict['tagged']):
            ui_cmd_obj.error_state = False
        elif not ui_cmd_obj.error_state and not StringUtils.string_to_boolean(arg_dict['tagged']):
            ui_cmd_obj.error_state = True
        if ui_cmd_obj.error_state:
            self.logger.log_debug("Vlan tagged status doesn't match expectation.")

        return ui_cmd_obj

    def verify_vlan_does_not_exist(self, ui_cmd_obj, arg_dict):
        xpath = "//*[contains(@role, 'gridcell') and normalize-space(.)='" + arg_dict['vlan_name'] + "']"
        self.builder.find_element(ui_cmd_obj, xpath)
        if ui_cmd_obj.error_state:
            ui_cmd_obj.error_state = False
            self.logger.log_debug("Vlan " + str(arg_dict["vlan_name"]) + " doesn't exist.")
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_debug("Vlan " + str(arg_dict["vlan_name"]) + " still exist.")

        return ui_cmd_obj
