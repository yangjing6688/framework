from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.EMC.EndsystemsConstants import EndsystemsConstants


class UiEndSystemsKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiEndSystemsKeywords, self).__init__()
        self.api_const = self.constants.API_ENDSYSTEMS
        self.command_const = EndsystemsConstants()

    def end_systems_confirm_device_exists_by_ip_address(self, element_name, ip_address, **kwargs):
        """Returns the result of end_systems_confirm_device_exists_by_ip_address."""
        args = {"ip_address": ip_address}

        return self.execute_keyword(element_name, args,
                                    self.command_const.ENDSYSTEMS_CONFIRM_DEVICE_EXISTS_BY_IP_ADDRESS, **kwargs)

    def end_systems_confirm_device_exists_by_mac_address(self, element_name, mac_address, **kwargs):
        """Returns the result of end_systems_confirm_device_exists_by_mac_address."""
        args = {"mac_address": mac_address}

        return self.execute_keyword(element_name, args,
                                    self.command_const.ENDSYSTEMS_CONFIRM_DEVICE_EXISTS_BY_MAC_ADDRESS, **kwargs)

    def endsystems_verify_cell_display_value_in_end_systems_grid(self, element_name, mac_address, column_header,
                                                                 expected_value, **kwargs):
        """Returns the result of endsystems_verify_cell_display_value_in_end_systems_grid."""
        args = {"mac_address": mac_address,
                "column_header": column_header,
                "expected_value": expected_value}

        return self.execute_keyword(element_name, args,
                                    self.command_const.ENDSYSTEMS_VERIFY_CELL_DISPLAY_VALUE_IN_END_SYSTEMS_GRID,
                                    **kwargs)

    def endsystems_verify_state_or_risk_in_end_systems_grid(self, element_name, mac_address, column_header,
                                                            expected_value, **kwargs):
        """Returns the result of endsystems_verify_state_or_risk_in_end_systems_grid."""
        args = {"mac_address": mac_address,
                "column_header": column_header,
                "expected_value": expected_value}

        return self.execute_keyword(element_name, args, self.command_const.
                                    ENDSYSTEMS_VERIFY_STATE_OR_RISK_IN_END_SYSTEMS_GRID, **kwargs)

    def endsystems_verify_authorization_type_display_value_in_end_systems_grid(self, element_name, mac_address,
                                                                               expected_value, **kwargs):
        """Returns the result of endsystems_verify_authorization_type_display_value_in_end_systems_grid."""
        args = {"mac_address": mac_address,
                "expected_value": expected_value}

        return self.execute_keyword(element_name, args, self.command_const.
                                    ENDSYSTEMS_VERIFY_AUTHORIZATION_TYPE_DISPLAY_VALUE_IN_END_SYSTEMS_GRID, **kwargs)

    def endsystems_verify_extended_state_display_value_in_end_systems_grid(self, element_name, mac_address,
                                                                           expected_value, **kwargs):
        """Returns the result of endsystems_verify_extended_state_display_value_in_end_systems_grid."""
        args = {"mac_address": mac_address,
                "expected_value": expected_value}

        return self.execute_keyword(element_name, args, self.command_const.
                                    ENDSYSTEMS_VERIFY_EXTENDED_STATE_DISPLAY_VALUE_IN_END_SYSTEMS_GRID, **kwargs)

    def endsystems_delete_device_by_mac_address(self, element_name, mac_address, is_force_delete, **kwargs):
        """Returns the result of endsystems_delete_device_by_mac_address."""
        args = {"mac_address": mac_address,
                "is_force_delete": is_force_delete}

        return self.execute_keyword(element_name, args, self.command_const.ENDSYSTEMS_DELETE_DEVICE_BY_MAC_ADDRESS,
                                    **kwargs)

    def endsystems_select_device_by_mac_address(self, element_name, mac_address, **kwargs):
        """Returns the result of endsystems_select_device_by_mac_address."""
        args = {"mac_address": mac_address}

        return self.execute_keyword(element_name, args, self.command_const.ENDSYSTEMS_SELECT_DEVICE_BY_MAC_ADDRESS,
                                    **kwargs)

    def endsystems_click_force_reauthentication_button(self, element_name, **kwargs):
        """Returns the result of endsystems_click_force_reauthentication_button."""
        args = {}

        return self.execute_keyword(element_name, args,
                                    self.command_const.ENDSYSTEMS_CLICK_FORCE_REAUTHENTICATION_BUTTON, **kwargs)

    def endsystems_click_refresh_button(self, element_name, **kwargs):
        """Returns the result of endsystems_click_refresh_button."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.ENDSYSTEMS_CLICK_REFRESH_BUTTON, **kwargs)
