from ExtremeAutomation.Apis.UiElement.GeneratedApis.SELENIUM.XCA.xcavlans.v04dot26dot03dot0007.xcavlans import \
    Xcavlans as XcavlansBase
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


class Xcavlans(XcavlansBase):
    def edit_info_for_vlan_in_bridged_at_ac_mode(self, ui_cmd_obj, arg_dict):
        if arg_dict["vlan_name"]:
            self.builder.enter_text(ui_cmd_obj, arg_dict["vlan_name"], "//input[@placeholder='VLAN Name']")
        self.builder.click(ui_cmd_obj, "//select[@id='topologyMode']/option[@value='string:BridgedAtAc']")
        if arg_dict["vlan_id"]:
            self.builder.enter_text(ui_cmd_obj, arg_dict["vlan_id"], "//input[@id='topologyVlanID']")
        self.builder.get_attribute_from_element_and_compare(ui_cmd_obj,
                                                            "//md-checkbox[@name='topologyTagged']",
                                                            "aria-checked", "true")
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
        if arg_dict["vlan_id"]:
            self.builder.enter_text(ui_cmd_obj, arg_dict["vlan_id"], "//input[@id='topologyVlanID']")
        self.builder.get_attribute_from_element_and_compare(ui_cmd_obj,
                                                            "//md-checkbox[@name='topologyTagged']",
                                                            "aria-checked", "true")
        if StringUtils.string_to_boolean(arg_dict['is_tagged']) is ui_cmd_obj.error_state:
            self.builder.click(ui_cmd_obj, "//md-checkbox[@name='topologyTagged']")
        ui_cmd_obj.error_state = False

        return ui_cmd_obj

    def save_settings_and_back_to_vlans_page(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//button[@ng-click='$parent.save()' and @aria-hidden='false']")
        self.builder.delay(ui_cmd_obj, 2000)
        self.builder.get_attribute_from_element_and_compare(ui_cmd_obj,
                                                            "//*[@uib-tooltip='Configure']", "aria-expanded", "true")
        if ui_cmd_obj.error_state:
            ui_cmd_obj.error_state = False
            self.builder.click(ui_cmd_obj, "//*[@uib-tooltip='Configure']")
        self.builder.click(ui_cmd_obj, "//*[@id='side-menu-configure']//button[@uib-tooltip='Policy']")
        self.builder.click(ui_cmd_obj, "//div[contains(@class, 'md-clickable')]//a/div[normalize-space(.)='VLANs']")

        return ui_cmd_obj
