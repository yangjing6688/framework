from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as PolicyvlansBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Policyvlans(PolicyvlansBase):
    def policy_vlans_right_click_on_global_vlans(self, ui_cmd_obj, arg_dict):
        self.ext_builder.right_click(ui_cmd_obj,
                                     "#policyNavTab #PolicyDomainView #policyDomainViewNavigationTrees "
                                     "#policyTreesPanel #vlanTree treeview => "
                                     ".x-tree-node-text:textEquals(Global VLANs)")

        return ui_cmd_obj

    def policy_vlans_reload_vlans(self, ui_cmd_obj, arg_dict):
        self.policy_vlans_right_click_on_global_vlans(ui_cmd_obj, arg_dict)
        self.ext_builder.click(ui_cmd_obj, "menuitem[text=Reload VLANs] => .x-menu-item-link")

        return ui_cmd_obj

    def policy_vlans_open_create_vlan_window(self, ui_cmd_obj, arg_dict):
        self.policy_vlans_right_click_on_global_vlans(ui_cmd_obj, arg_dict)
        self.ext_builder.click(ui_cmd_obj, r"menuitem[text=Create VLAN\.\.\.] => .x-menu-item-link")

        return ui_cmd_obj

    def policy_vlans_enter_vlan_name_and_vid(self, ui_cmd_obj, arg_dict):
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict["vlan_name"]), "#CreateVlanWin #VlanNameValueSet => "
                                                                            ".x-form-text")
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict["vlan_id"]), "#CreateVlanWin #VlanVidValueSet => "
                                                                          ".x-form-text")

        return ui_cmd_obj

    def policy_vlans_click_next_available_vid_button(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "#CreateVlanWin button[text=Next Available VID] => .x-btn-inner-default-small")

        return ui_cmd_obj

    def policy_vlans_click_ok_to_save_new_vlan(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "#CreateVlanWin #createVlanOkBtn => .x-btn-inner-blue-small")

        return ui_cmd_obj

    def policy_vlans_click_cancel_to_discard_new_vlan(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "#CreateVlanWin button[text=Cancel] => .x-btn-inner-default-small")

        return ui_cmd_obj

    def policy_vlans_click_vlan_to_open_vlan_setting_page(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "#policyNavTab #PolicyDomainView #policyDomainViewNavigationTrees #policyTreesPanel "
                               "#vlanTree treeview => "
                               ".x-tree-node-text:textEquals(" + str(arg_dict["vlan_display_name"]) + ")")

        return ui_cmd_obj

    def policy_vlans_click_dynamic_egress_checkbox(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "#policyNavTab #PolicyDomainView #domainNodeDetailsPanelContainer "
                               "checkbox[boxLabel=Dynamic Egress] => .x-form-cb-input")

        return ui_cmd_obj

    def policy_vlans_click_always_to_write_vlan_to_devices_checkbox(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               r"#policyNavTab #PolicyDomainView #domainNodeDetailsPanelContainer "
                               r"checkbox[boxLabel=Always write VLAN to device\(s\)] => .x-form-cb-input")

        return ui_cmd_obj
