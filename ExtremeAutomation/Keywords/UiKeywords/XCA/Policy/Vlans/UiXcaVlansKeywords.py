from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.XCA.XcavlansConstants import XcavlansConstants


class UiXcaVlansKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiXcaVlansKeywords, self).__init__()
        self.api_const = self.constants.API_XCA_VLANS
        self.command_const = XcavlansConstants()

    def vlans_click_add_to_create_new_vlan(self, element_names, **kwargs):
        """Returns the result of vlans_click_add_to_create_new_vlan."""
        args = {}

        return self.execute_keyword(element_names, args, self.command_const.CLICK_ADD_TO_CREATE_NEW_VLAN, **kwargs)

    def vlans_click_vlan_name_to_open_vlan_settings(self, element_names, vlan_name, **kwargs):
        """Returns the result of vlans_click_vlan_name_to_open_vlan_settings."""
        args = {"vlan_name": vlan_name}

        return self.execute_keyword(element_names, args, self.command_const.CLICK_VLAN_NAME_TO_OPEN_VLAN_SETTINGS,
                                    **kwargs)

    def vlans_edit_info_for_vlan_in_bridged_at_ac_mode(self, element_names, vlan_name, vlan_id, is_tagged,
                                                       topology_port, **kwargs):
        """
        :param element_names:
        :param vlan_name:
        :param vlan_id:
        :param is_tagged: Pass None type data if not tagged.
        :param topology_port:
        :return:
        """
        args = {"vlan_name": vlan_name,
                "vlan_id": vlan_id,
                "is_tagged": is_tagged,
                "topology_port": topology_port}

        return self.execute_keyword(element_names, args, self.command_const.EDIT_INFO_FOR_VLAN_IN_BRIDGED_AT_AC_MODE,
                                    **kwargs)

    def vlans_edit_info_for_vlan_in_bridged_at_ap_mode(self, element_names, vlan_name, vlan_id, is_tagged, **kwargs):
        """
        :param element_names:
        :param vlan_name:
        :param vlan_id:
        :param is_tagged: Pass None type data if not tagged.
        :param kwargs:
        :return:
        """
        args = {"vlan_name": vlan_name,
                "vlan_id": vlan_id,
                "is_tagged": is_tagged}

        return self.execute_keyword(element_names, args, self.command_const.EDIT_INFO_FOR_VLAN_IN_BRIDGED_AT_AP_MODE,
                                    **kwargs)

    def vlans_edit_info_for_vlan_in_fabric_attach_mode(self, element_names, vlan_name, vlan_id, isid, **kwargs):
        """

        :param element_names:
        :param vlan_name:
        :param vlan_id:
        :param isid:
        :param kwargs:
        :return:
        """
        args = {"vlan_name": vlan_name,
                "vlan_id": vlan_id,
                "isid": isid}

        return self.execute_keyword(element_names, args, self.command_const.EDIT_INFO_FOR_VLAN_IN_FABRIC_ATTACH_MODE,
                                    **kwargs)

    def vlans_edit_advanced_settings_for_vlan(self, element_names, **kwargs):
        """Returns the result of vlans_edit_advanced_settings_for_vlan."""
        args = {}

        return self.execute_keyword(element_names, args, self.command_const.EDIT_ADVANCED_SETTINGS_FOR_VLAN, **kwargs)

    def vlans_edit_layer3_settings_for_vlan(self, element_names, **kwargs):
        """Returns the result of vlans_edit_layer3_settings_for_vlan."""
        args = {}

        return self.execute_keyword(element_names, args, self.command_const.EDIT_LAYER3_SETTINGS_FOR_VLAN, **kwargs)

    def vlans_config_dhcp_relay_servers(self, element_names, **kwargs):
        """Returns the result of vlans_config_dhcp_relay_servers."""
        args = {}

        return self.execute_keyword(element_names, args, self.command_const.CONFIG_DHCP_RELAY_SERVERS, **kwargs)

    def vlans_config_dhcp_local_server(self, element_names, **kwargs):
        """Returns the result of vlans_config_dhcp_local_server."""
        args = {}

        return self.execute_keyword(element_names, args, self.command_const.CONFIG_DHCP_LOCAL_SERVER, **kwargs)

    def vlans_save_settings_and_back_to_vlans_page(self, element_names, **kwargs):
        """Returns the result of vlans_save_settings_and_back_to_vlans_page."""
        args = {}

        return self.execute_keyword(element_names, args, self.command_const.SAVE_SETTINGS_AND_BACK_TO_VLANS_PAGE,
                                    **kwargs)

    def vlans_delete_existing_vlan(self, element_names, vlan_name, **kwargs):
        """Returns the result of vlans_delete_existing_vlan."""
        args = {"vlan_name": vlan_name}

        return self.execute_keyword(element_names, args, self.command_const.DELETE_EXISTING_VLAN, **kwargs)

    def vlans_verify_vlan_exists(self, element_names, vlan_name, vlan_mode, vlan_id, tagged, **kwargs):
        """Returns the result of vlans_verify_vlan_exists."""
        args = {"vlan_name": vlan_name,
                "vlan_mode": vlan_mode,
                "vlan_id": vlan_id,
                "tagged": tagged}

        return self.execute_keyword(element_names, args, self.command_const.VERIFY_VLAN_EXISTS, **kwargs)

    def vlans_verify_vlan_does_not_exist(self, element_names, vlan_name, **kwargs):
        """Returns the result of vlans_verify_vlan_does_not_exist."""
        args = {"vlan_name": vlan_name}

        return self.execute_keyword(element_names, args, self.command_const.VERIFY_VLAN_DOES_NOT_EXIST, **kwargs)
