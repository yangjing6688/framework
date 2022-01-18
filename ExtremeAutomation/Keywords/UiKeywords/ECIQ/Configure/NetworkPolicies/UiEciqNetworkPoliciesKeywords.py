from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.ECIQ.EciqnetworkpoliciesConstants import \
    EciqnetworkpoliciesConstants


class UiEciqNetworkPoliciesKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiEciqNetworkPoliciesKeywords, self).__init__()
        self.api_const = self.constants.API_ECIQ_NETWORK_POLICIES
        self.command_const = EciqnetworkpoliciesConstants()

    def eciq_network_policies_click_add_network_policy_button(self, element_name, **kwargs):
        """
        Returns the result of network_policies_click_add_network_policy_button.
        [element_name] - The UI element(s) the keyword should be run against.
        """
        args = {}

        return self.execute_keyword(element_name, args,
                                    self.command_const.NETWORK_POLICIES_CLICK_ADD_NETWORK_POLICY_BUTTON, **kwargs)

    def eciq_network_policies_click_express_policy_setup_button(self, element_name, **kwargs):
        """
        Returns the result of network_policies_click_express_policy_setup_button.
        [element_name] - The UI element(s) the keyword should be run against.
        """
        args = {}

        return self.execute_keyword(element_name, args,
                                    self.command_const.NETWORK_POLICIES_CLICK_EXPRESS_POLICY_SETUP_BUTTON, **kwargs)

    def eciq_network_policies_delete_network_policy(self, element_name, network_policy_name, **kwargs):
        """
        Returns the result of network_policies_delete_network_policy.
        [element_name] - The UI element(s) the keyword should be run against.
        """
        args = {"network_policy_name": network_policy_name}

        return self.execute_keyword(element_name, args, self.command_const.NETWORK_POLICIES_DELETE_NETWORK_POLICY,
                                    **kwargs)

    def eciq_network_policies_dialog_add_network_policy_name(self, element_name, network_policy_name, **kwargs):
        """
        Returns the result of network_policies_dialog_add_network_policy_name.
        [element_name] - The UI element(s) the keyword should be run against.
        """
        args = {"network_policy_name": network_policy_name}

        return self.execute_keyword(element_name, args,
                                    self.command_const.NETWORK_POLICIES_DIALOG_ADD_NETWORK_POLICY_NAME, **kwargs)

    def eciq_network_policies_dialog_add_network_policy_description(self, element_name, network_policy_desc, **kwargs):
        """
        Returns the result of network_policies_dialog_add_network_policy_description.
        [element_name] - The UI element(s) the keyword should be run against.
        """
        args = {"network_policy_desc": network_policy_desc}

        return self.execute_keyword(element_name, args,
                                    self.command_const.NETWORK_POLICIES_DIALOG_ADD_NETWORK_POLICY_DESCRIPTION, **kwargs)

    def eciq_network_policies_dialog_check_routing_policy_type_checkbox(self, element_name, status, **kwargs):
        """
        Checks or unchecks the policy type checkbox for Routing.
        Returns the result of network_policies_dialog_check_routing_policy_type_checkbox.
        [element_name] - The UI element(s) the keyword should be run against.
        [status] - If status is true, checkbox should be checked.  If status is false, checkbox should not be checked.
        """
        args = {"status": status}

        return self.execute_keyword(element_name, args,
                                    self.command_const.NETWORK_POLICIES_DIALOG_CHECK_ROUTING_POLICY_TYPE_CHECKBOX,
                                    **kwargs)

    def eciq_network_policies_dialog_check_switches_policy_type_checkbox(self, element_name, status, **kwargs):
        """
        Checks or unchecks the policy type checkbox for Switches.
        Returns the result of network_policies_dialog_check_switches_policy_type_checkbox.
        [element_name] - The UI element(s) the keyword should be run against.
        [status] - If status is true, checkbox should be checked.  If status is false, checkbox should not be checked.
        """
        args = {"status": status}

        return self.execute_keyword(element_name, args,
                                    self.command_const.NETWORK_POLICIES_DIALOG_CHECK_SWITCHES_POLICY_TYPE_CHECKBOX,
                                    **kwargs)

    def eciq_network_policies_dialog_check_wireless_policy_type_checkbox(self, element_name, status, **kwargs):
        """
        Checks or unchecks the policy type checkbox for Wireless.
        Returns the result of network_policies_dialog_check_wireless_policy_type_checkbox.
        [element_name] - The UI element(s) the keyword should be run against.
        [status] - If status is true, checkbox should be checked.  If status is false, checkbox should not be checked.
        """
        args = {"status": status}

        return self.execute_keyword(element_name, args,
                                    self.command_const.NETWORK_POLICIES_DIALOG_CHECK_WIRELESS_POLICY_TYPE_CHECKBOX,
                                    **kwargs)

    def eciq_network_policies_dialog_click_exit_button(self, element_name, **kwargs):
        """
        Returns the result of network_policies_dialog_click_exit_button.
        [element_name] - The UI element(s) the keyword should be run against.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.NETWORK_POLICIES_DIALOG_CLICK_EXIT_BUTTON,
                                    **kwargs)

    def eciq_network_policies_dialog_click_next_button(self, element_name, **kwargs):
        """
        Returns the result of network_policies_dialog_click_next_button.
        [element_name] - The UI element(s) the keyword should be run against.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.NETWORK_POLICIES_DIALOG_CLICK_NEXT_BUTTON,
                                    **kwargs)

    def eciq_network_policies_dialog_click_save_button(self, element_name, **kwargs):
        """
        Returns the result of network_policies_dialog_click_save_button.
        [element_name] - The UI element(s) the keyword should be run against.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.NETWORK_POLICIES_DIALOG_CLICK_SAVE_BUTTON,
                                    **kwargs)

    def eciq_network_policies_dialog_click_tab_header(self, element_name, tab_name, **kwargs):
        """
        Returns the result of network_policies_dialog_click_tab_header.
        [element_name] - The UI element(s) the keyword should be run against.
        """
        args = {"tab_name": tab_name}

        return self.execute_keyword(element_name, args, self.command_const.NETWORK_POLICIES_DIALOG_CLICK_TAB_HEADER,
                                    **kwargs)

    def eciq_network_policies_select_policy(self, element_name, network_policy_name, **kwargs):
        """
        Selects the network policy name displayed on the page.
        Returns the result of network_policies_select_policy.
        [element_name] - The UI element(s) the keyword should be run against.
        """
        args = {"network_policy_name": network_policy_name}

        return self.execute_keyword(element_name, args, self.command_const.NETWORK_POLICIES_SELECT_POLICY, **kwargs)
