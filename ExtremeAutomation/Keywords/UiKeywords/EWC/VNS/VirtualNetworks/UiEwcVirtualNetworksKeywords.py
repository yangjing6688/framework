from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.EWC.EwcvirtualnetworksConstants \
    import EwcvirtualnetworksConstants


class UiEwcVirtualNetworksKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiEwcVirtualNetworksKeywords, self).__init__()
        self.api_const = self.constants.API_EWC_VIRTUAL_NETWORKS
        self.command_const = EwcvirtualnetworksConstants()

    def virtual_networks_create_vns(self, element_name, vns_name, wlan_service,
                                    non_auth_policy_name, auth_policy_name, status, **kwargs):
        """Returns the result of virtual_networks_create_vns."""
        args = {"vns_name": vns_name,
                "wlan_service": wlan_service,
                "non_auth_policy_name": non_auth_policy_name,
                "auth_policy_name": auth_policy_name,
                "status": status}

        return self.execute_keyword(element_name, args, self.command_const.VIRTUAL_NETWORKS_CREATE_VNS, **kwargs)

    def virtual_networks_delete_vns(self, element_name, vns_name, **kwargs):
        """Returns the result of virtual_networks_delete_vns."""
        args = {"vns_name": vns_name}

        return self.execute_keyword(element_name, args, self.command_const.VIRTUAL_NETWORKS_DELETE_VNS, **kwargs)

    def virtual_networks_vns_should_exist(self, element_name, vns_name, **kwargs):
        """Returns the result of virtual_networks_vns_should_exist."""
        args = {"vns_name": vns_name}

        return self.execute_keyword(element_name, args, self.command_const.VIRTUAL_NETWORKS_VNS_SHOULD_EXIST, **kwargs)

    def virtual_networks_vns_should_not_exist(self, element_name, vns_name, **kwargs):
        """Returns the result of virtual_networks_vns_should_not_exist."""
        args = {"vns_name": vns_name}

        return self.execute_keyword(element_name, args,
                                    self.command_const.VIRTUAL_NETWORKS_VNS_SHOULD_NOT_EXIST, **kwargs)

    def virtual_networks_edit_wlan_service_in_vns(self, element_name, vns_name, wlan_name, **kwargs):
        """Returns the result of virtual_networks_edit_wlan_service_in_vns."""
        args = {"vns_name": vns_name,
                "wlan_name": wlan_name}

        return self.execute_keyword(element_name, args,
                                    self.command_const.VIRTUAL_NETWORKS_EDIT_WLAN_SERVICE_IN_VNS, **kwargs)

    def virtual_networks_edit_non_authenticated_policy_role_in_vns(self, element_name, vns_name, non_auth_policy_name,
                                                                   **kwargs):
        """Returns the result of virtual_networks_edit_non_authenticated_policy_role_in_vns."""
        args = {"vns_name": vns_name,
                "non_auth_policy_name": non_auth_policy_name}

        return self.execute_keyword(element_name, args,
                                    self.command_const.VIRTUAL_NETWORKS_EDIT_NON_AUTHENTICATED_POLICY_ROLE_IN_VNS,
                                    **kwargs)

    def virtual_networks_edit_authenticated_policy_role_in_vns(self, element_name, vns_name, auth_policy_name,
                                                               **kwargs):
        """Returns the result of virtual_networks_edit_authenticated_policy_role_in_vns."""
        args = {"vns_name": vns_name,
                "auth_policy_name": auth_policy_name}

        return self.execute_keyword(element_name, args,
                                    self.command_const.VIRTUAL_NETWORKS_EDIT_AUTHENTICATED_POLICY_ROLE_IN_VNS, **kwargs)

    def virtual_networks_vns_should_be_enabled(self, element_name, vns_name, **kwargs):
        """Returns the result of virtual_networks_vns_should_be_enabled."""
        args = {"vns_name": vns_name}

        return self.execute_keyword(element_name, args,
                                    self.command_const.VIRTUAL_NETWORKS_VNS_SHOULD_BE_ENABLED, **kwargs)

    def virtual_networks_click_save_button(self, element_name, **kwargs):
        """Returns the result of virtual_networks_click_save_button."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.VIRTUAL_NETWORKS_CLICK_SAVE_BUTTON, **kwargs)
