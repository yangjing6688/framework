from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.ECIQ.EciqonboardConstants import EciqonboardConstants


class UiEciqOnboardKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiEciqOnboardKeywords, self).__init__()
        self.api_const = self.constants.API_ECIQ_ONBOARD
        self.command_const = EciqonboardConstants()

    def eciq_onboard_bypass_onboarding_routine(self, element_name, **kwargs):
        """Returns the result of bypass_onboarding_routine."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.BYPASS_ONBOARDING_ROUTINE, **kwargs)

    def eciq_onboard_dialog_add_new_policy_name(self, element_name, policy_name, **kwargs):
        """Returns the result of onboard_dialog_add_new_policy_name."""
        args = {"policy_name": policy_name}

        return self.execute_keyword(element_name, args, self.command_const.ONBOARD_DIALOG_ADD_NEW_POLICY_NAME, **kwargs)

    def eciq_onboard_dialog_add_serial_number(self, element_name, device_type, serial_number, **kwargs):
        """Returns the result of onboard_dialog_add_serial_number."""
        args = {"device_type": device_type,
                "serial_number": serial_number}

        return self.execute_keyword(element_name, args, self.command_const.ONBOARD_DIALOG_ADD_SERIAL_NUMBER, **kwargs)

    def eciq_onboard_dialog_assign_location_check_device_checkbox(self, element_name, serial_number, **kwargs):
        """
        On the onboard dialog assign location page, checks the device checkbox using the serial number.
        Returns the result of onboard_dialog_assign_location_check_device_checkbox.
        [element_name] - The UI element(s) the keyword should be run against.
        [serial_number] - The serial number of the device with the checkbox to be checked.
        """
        args = {"serial_number": serial_number}

        return self.execute_keyword(element_name, args,
                                    self.command_const.ONBOARD_DIALOG_ASSIGN_LOCATION_CHECK_DEVICE_CHECKBOX, **kwargs)

    def eciq_onboard_dialog_assign_location_popup_click_assign_button(self, element_name, **kwargs):
        """Returns the result of onboard_dialog_assign_location_popup_click_assign_button."""
        args = {}

        return self.execute_keyword(element_name, args,
                                    self.command_const.ONBOARD_DIALOG_ASSIGN_LOCATION_POPUP_CLICK_ASSIGN_BUTTON,
                                    **kwargs)

    def eciq_onboard_dialog_assign_location_popup_click_cancel_button(self, element_name, **kwargs):
        """Returns the result of onboard_dialog_assign_location_popup_click_cancel_button."""
        args = {}

        return self.execute_keyword(element_name, args,
                                    self.command_const.ONBOARD_DIALOG_ASSIGN_LOCATION_POPUP_CLICK_CANCEL_BUTTON,
                                    **kwargs)

    def eciq_onboard_dialog_click_assign_location_button(self, element_name, **kwargs):
        """Returns the result of onboard_dialog_click_assign_location_button."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.ONBOARD_DIALOG_CLICK_ASSIGN_LOCATION_BUTTON,
                                    **kwargs)

    def eciq_onboard_dialog_click_device_type_real_button(self, element_name, **kwargs):
        """Returns the result of onboard_dialog_click_device_type_real_button."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.ONBOARD_DIALOG_CLICK_DEVICE_TYPE_REAL_BUTTON,
                                    **kwargs)

    def eciq_onboard_dialog_click_device_type_simulated_button(self, element_name, **kwargs):
        """Returns the result of onboard_dialog_click_device_type_simulated_button."""
        args = {}

        return self.execute_keyword(element_name,
                                    args, self.command_const.ONBOARD_DIALOG_CLICK_DEVICE_TYPE_SIMULATED_BUTTON,
                                    **kwargs)

    def eciq_onboard_dialog_click_done_button(self, element_name, **kwargs):
        """Returns the result of onboard_dialog_click_done_button."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.ONBOARD_DIALOG_CLICK_DONE_BUTTON, **kwargs)

    def eciq_onboard_dialog_click_finish_button(self, element_name, **kwargs):
        """Returns the result of onboard_dialog_click_finish_button."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.ONBOARD_DIALOG_CLICK_FINISH_BUTTON, **kwargs)

    def eciq_onboard_dialog_click_get_started_button(self, element_name, **kwargs):
        """Returns the result of onboard_dialog_click_get_started_button."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.ONBOARD_DIALOG_CLICK_GET_STARTED_BUTTON,
                                    **kwargs)

    def eciq_onboard_dialog_click_next_button(self, element_name, **kwargs):
        """Returns the result of onboard_dialog_click_next_button."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.ONBOARD_DIALOG_CLICK_NEXT_BUTTON, **kwargs)

    def eciq_onboard_dialog_click_skip_button(self, element_name, **kwargs):
        """Returns the result of onboard_dialog_click_skip_button."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.ONBOARD_DIALOG_CLICK_SKIP_BUTTON, **kwargs)

    def eciq_onboard_dialog_select_create_new_network_policy(self, element_name, **kwargs):
        """Returns the result of onboard_dialog_select_create_new_network_policy."""
        args = {}

        return self.execute_keyword(element_name, args,
                                    self.command_const.ONBOARD_DIALOG_SELECT_CREATE_NEW_NETWORK_POLICY, **kwargs)

    def eciq_onboard_dialog_select_device_type(self, element_name, device_type, **kwargs):
        """Returns the result of onboard_dialog_select_device_type."""
        args = {"device_type": device_type}

        return self.execute_keyword(element_name, args, self.command_const.ONBOARD_DIALOG_SELECT_DEVICE_TYPE, **kwargs)

    def eciq_onboard_dialog_select_network_policy(self, element_name, network_policy, **kwargs):
        """Returns the result of onboard_dialog_select_network_policy."""
        args = {"network_policy": network_policy}

        return self.execute_keyword(element_name, args, self.command_const.ONBOARD_DIALOG_SELECT_NETWORK_POLICY,
                                    **kwargs)

    def eciq_onboard_dialog_select_use_an_existing_network_policy(self, element_name, **kwargs):
        """Returns the result of onboard_dialog_select_use_an_existing_network_policy."""
        args = {}

        return self.execute_keyword(element_name, args,
                                    self.command_const.ONBOARD_DIALOG_SELECT_USE_AN_EXISTING_NETWORK_POLICY, **kwargs)

    def eciq_onboard_dialog_uncheck_network_policy_type(self, element_name, policy_type, **kwargs):
        """Returns the result of onboard_dialog_uncheck_network_policy_type."""
        args = {"policy_type": policy_type}

        return self.execute_keyword(element_name, args, self.command_const.ONBOARD_DIALOG_UNCHECK_NETWORK_POLICY_TYPE,
                                    **kwargs)
