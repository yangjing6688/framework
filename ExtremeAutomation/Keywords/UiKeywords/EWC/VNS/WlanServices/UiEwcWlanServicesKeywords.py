from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.EWC.EwcwlanConstants import EwcwlanConstants


class UiEwcWlanServicesKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiEwcWlanServicesKeywords, self).__init__()
        self.api_const = self.constants.API_EWC_WLAN
        self.command_const = EwcwlanConstants()

    def wlan_create_wlan(self, element_name, wlan_name, service_type, ssid, hotspot, status, **kwargs):
        """Returns the result of wlan_create_wlan."""
        args = {"wlan_name": wlan_name,
                "service_type": service_type,
                "ssid": ssid,
                "hotspot": hotspot,
                "status": status}

        return self.execute_keyword(element_name, args, self.command_const.WLAN_CREATE_WLAN, **kwargs)

    def wlan_delete_wlan(self, element_name, wlan_name, **kwargs):
        """Returns the result of wlan_delete_wlan."""
        args = {"wlan_name": wlan_name}

        return self.execute_keyword(element_name, args, self.command_const.WLAN_DELETE_WLAN, **kwargs)

    def wlan_save_wlan_settings(self, element_name, **kwargs):
        """Returns the result of wlan_save_wlan_settings."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.WLAN_SAVE_WLAN_SETTINGS, **kwargs)

    def wlan_select_sub_tab(self, element_name, tab_name, **kwargs):
        """Returns the result of wlan_select_sub_tab."""
        args = {"tab_name": tab_name}

        return self.execute_keyword(element_name, args, self.command_const.WLAN_SELECT_SUB_TAB, **kwargs)

    def wlan_edit_wlan_name(self, element_name, wlan_name, **kwargs):
        """Returns the result of wlan_edit_wlan_name."""
        args = {"wlan_name": wlan_name}

        return self.execute_keyword(element_name, args, self.command_const.WLAN_EDIT_WLAN_NAME, **kwargs)

    def wlan_edit_ssid(self, element_name, ssid, **kwargs):
        """Returns the result of wlan_edit_ssid."""
        args = {"ssid": ssid}

        return self.execute_keyword(element_name, args, self.command_const.WLAN_EDIT_SSID, **kwargs)

    def wlan_select_default_topology(self, element_name, topology_name, **kwargs):
        """Returns the result of wlan_select_."""
        args = {"topology_name": topology_name}

        return self.execute_keyword(element_name, args, self.command_const.WLAN_SELECT_DEFAULT_TOPOLOGY, **kwargs)

    def wlan_select_default_cos(self, element_name, cos_name, **kwargs):
        """Returns the result of wlan_select_."""
        args = {"cos_name": cos_name}

        return self.execute_keyword(element_name, args, self.command_const.WLAN_SELECT_DEFAULT_COS, **kwargs)

    def wlan_select_default_traffic(self, element_name, traffic_mode, **kwargs):
        """Returns the result of wlan_select_."""
        args = {"traffic_mode": traffic_mode}

        return self.execute_keyword(element_name, args, self.command_const.WLAN_SELECT_DEFAULT_TRAFFIC, **kwargs)

    def wlan_check_application_visibility(self, element_name, **kwargs):
        """Returns the result of wlan_check_application_visibility."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.WLAN_CHECK_APPLICATION_VISIBILITY, **kwargs)

    def wlan_uncheck_application_visibility(self, element_name, **kwargs):
        """Returns the result of wlan_uncheck_application_visibility."""
        args = {}

        return self.execute_keyword(element_name, args,
                                    self.command_const.WLAN_UNCHECK_APPLICATION_VISIBILITY, **kwargs)

    def wlan_enable_wlan(self, element_name, **kwargs):
        """Returns the result of wlan_enable_wlan."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.WLAN_ENABLE_WLAN, **kwargs)

    def wlan_disable_wlan(self, element_name, **kwargs):
        """Returns the result of wlan_disable_wlan."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.WLAN_DISABLE_WLAN, **kwargs)

    def wlan_select_privacy_mode(self, element_name, privacy_mode, **kwargs):
        """Returns the result of wlan_select_privacy_mode."""
        args = {"privacy_mode": privacy_mode}

        return self.execute_keyword(element_name, args, self.command_const.WLAN_SELECT_PRIVACY_MODE, **kwargs)

    def wlan_select_authentication_mode(self, element_name, authentication_mode, **kwargs):
        """Returns the result of wlan_select_authentication_mode."""
        args = {"authentication_mode": authentication_mode}

        return self.execute_keyword(element_name, args, self.command_const.WLAN_SELECT_AUTHENTICATION_MODE, **kwargs)

    def wlan_enable_mac_authentication(self, element_name, **kwargs):
        """Returns the result of wlan_enable_mac_authentication."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.WLAN_ENABLE_MAC_AUTHENTICATION, **kwargs)

    def wlan_disable_mac_authentication(self, element_name, **kwargs):
        """Returns the result of wlan_disable_mac_authentication."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.WLAN_DISABLE_MAC_AUTHENTICATION, **kwargs)

    def wlan_enable_radius_accounting(self, element_name, **kwargs):
        """Returns the result of wlan_enable_radius_accounting."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.WLAN_ENABLE_RADIUS_ACCOUNTING, **kwargs)

    def wlan_disable_radius_accounting(self, element_name, **kwargs):
        """Returns the result of wlan_disable_radius_accounting."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.WLAN_DISABLE_RADIUS_ACCOUNTING, **kwargs)

    def wlan_select_radius_server(self, element_name, radius_server, **kwargs):
        """Returns the result of wlan_select_radius_server."""
        args = {"radius_server": radius_server}

        return self.execute_keyword(element_name, args, self.command_const.WLAN_SELECT_RADIUS_SERVER, **kwargs)

    def wlan_select_radius_accounting_server(self, element_name, radius_accounting_server, **kwargs):
        """Returns the result of wlan_select_radius_accounting_server."""
        args = {"radius_accounting_server": radius_accounting_server}

        return self.execute_keyword(element_name, args,
                                    self.command_const.WLAN_SELECT_RADIUS_ACCOUNTING_SERVER, **kwargs)

    def wlan_select_wep_key_input_method(self, element_name, wep_key_input_method, **kwargs):
        """Returns the result of wlan_select_wep_key_input_method."""
        args = {"wep_key_input_method": wep_key_input_method}

        return self.execute_keyword(element_name, args, self.command_const.WLAN_SELECT_WEP_KEY_INPUT_METHOD, **kwargs)

    def wlan_edit_wep_key_string(self, element_name, wep_key_string, **kwargs):
        """Returns the result of wlan_edit_wep_key_string."""
        args = {"wep_key_string": wep_key_string}

        return self.execute_keyword(element_name, args, self.command_const.WLAN_EDIT_WEP_KEY_STRING, **kwargs)

    def wlan_click_radius_tlvs_button(self, element_name, **kwargs):
        """Returns the result of wlan_click_radius_tlvs_button."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.WLAN_CLICK_RADIUS_TLVS_BUTTON, **kwargs)

    def wlan_check_ssid_vsa(self, element_name, **kwargs):
        """Returns the result of wlan_check_ssid_vsa."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.WLAN_CHECK_SSID_VSA, **kwargs)

    def wlan_uncheck_ssid_vsa(self, element_name, **kwargs):
        """Returns the result of wlan_uncheck_ssid_vsa."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.WLAN_UNCHECK_SSID_VSA, **kwargs)

    def wlan_check_ap_name_vsa(self, element_name, status, **kwargs):
        """Returns the result of wlan_check_ap_name_vsa."""
        args = {"status": status}

        return self.execute_keyword(element_name, args, self.command_const.WLAN_CHECK_AP_NAME_VSA, **kwargs)

    def wlan_radius_message_options_popup_click_ok(self, element_name, **kwargs):
        """Returns the result of wlan_radius_message_options_popup_click_ok."""
        args = {}

        return self.execute_keyword(element_name, args,
                                    self.command_const.WLAN_RADIUS_MESSAGE_OPTIONS_POPUP_CLICK_OK, **kwargs)
