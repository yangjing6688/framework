from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.EMC.PolicyvlansConstants import PolicyvlansConstants


class UiPolicyVlansKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiPolicyVlansKeywords, self).__init__()
        self.api_const = self.constants.API_POLICY_VLANS
        self.command_const = PolicyvlansConstants()

    def policy_vlans_reload_vlans(self, element_name, **kwargs):
        """Returns the result of policy_vlans_reload_vlans."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.POLICY_VLANS_RELOAD_VLANS, **kwargs)

    def policy_vlans_open_create_vlan_window(self, element_name, **kwargs):
        """Returns the result of policy_vlans_open_create_vlan_window."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.POLICY_VLANS_OPEN_CREATE_VLAN_WINDOW,
                                    **kwargs)

    def policy_vlans_enter_vlan_name_and_vid(self, element_name, vlan_name, vlan_id, **kwargs):
        """Returns the result of policy_vlans_enter_vlan_name_and_vid."""
        args = {"vlan_name": vlan_name,
                "vlan_id": vlan_id}

        return self.execute_keyword(element_name, args, self.command_const.POLICY_VLANS_ENTER_VLAN_NAME_AND_VID,
                                    **kwargs)

    def policy_vlans_click_next_available_vid_button(self, element_name, **kwargs):
        """Returns the result of policy_vlans_click_next_available_vid_button."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.POLICY_VLANS_CLICK_NEXT_AVAILABLE_VID_BUTTON,
                                    **kwargs)

    def policy_vlans_click_ok_to_save_new_vlan(self, element_name, **kwargs):
        """Returns the result of policy_vlans_click_ok_to_save_new_vlan."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.POLICY_VLANS_CLICK_OK_TO_SAVE_NEW_VLAN,
                                    **kwargs)

    def policy_vlans_click_cancel_to_discard_new_vlan(self, element_name, **kwargs):
        """Returns the result of policy_vlans_click_cancel_to_discard_new_vlan."""
        args = {}

        return self.execute_keyword(element_name, args,
                                    self.command_const.POLICY_VLANS_CLICK_CANCEL_TO_DISCARD_NEW_VLAN, **kwargs)

    def policy_vlans_click_vlan_to_open_vlan_setting_page(self, element_name, vlan_display_name, **kwargs):
        """Returns the result of policy_vlans_click_vlan_to_open_vlan_setting_page."""
        args = {"vlan_display_name": vlan_display_name}

        return self.execute_keyword(element_name, args,
                                    self.command_const.POLICY_VLANS_CLICK_VLAN_TO_OPEN_VLAN_SETTING_PAGE, **kwargs)

    def policy_vlans_click_dynamic_egress_checkbox(self, element_name, **kwargs):
        """Returns the result of policy_vlans_click_dynamic_egress_checkbox."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.POLICY_VLANS_CLICK_DYNAMIC_EGRESS_CHECKBOX,
                                    **kwargs)

    def policy_vlans_click_always_to_write_vlan_to_devices_checkbox(self, element_name, **kwargs):
        """Returns the result of policy_vlans_click_always_to_write_vlan_to_devices_checkbox."""
        args = {}

        return self.execute_keyword(element_name, args,
                                    self.command_const.POLICY_VLANS_CLICK_ALWAYS_TO_WRITE_VLAN_TO_DEVICES_CHECKBOX,
                                    **kwargs)
