from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.XCA.XcadevicegroupsConstants \
    import XcadevicegroupsConstants


class UiXcaDeviceGroupsKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiXcaDeviceGroupsKeywords, self).__init__()
        self.api_const = self.constants.API_XCA_DEVICE_GROUPS
        self.command_const = XcadevicegroupsConstants()

    def device_groups_select_device_group(self, element_names, device_group_name, **kwargs):
        """Returns the result of device_groups_select_device_group."""
        args = {"device_group_name": device_group_name}

        return self.execute_keyword(element_names, args, self.command_const.SELECT_DEVICE_GROUP, **kwargs)

    def device_groups_select_device_group_edit_config(self, element_names, device_group_name, **kwargs):
        """Returns the result of device_groups_select_device_group_edit_config."""
        args = {"device_group_name": device_group_name}

        return self.execute_keyword(element_names, args, self.command_const.SELECT_DEVICE_GROUP_EDIT_CONFIG, **kwargs)

    def device_groups_click_device_group_edit_profile_button(self, element_names, **kwargs):
        """Returns the result of device_groups_click_device_group_edit_profile_button."""
        args = {}

        return self.execute_keyword(element_names, args, self.command_const.CLICK_DEVICE_GROUP_EDIT_PROFILE_BUTTON,
                                    **kwargs)

    def device_groups_config_device_group_name_and_country(self, element_names, **kwargs):
        """Returns the result of device_groups_config_device_group_name_and_country."""
        args = {}

        return self.execute_keyword(element_names, args, self.command_const.CONFIG_DEVICE_GROUP_NAME_AND_COUNTRY,
                                    **kwargs)

    def device_groups_config_device_group_networks(self, element_names, network_name, radio_ports, **kwargs):
        """Returns the result of device_groups_config_device_group_networks."""
        args = {"network_name": network_name,
                "radio_ports": radio_ports}

        return self.execute_keyword(element_names, args, self.command_const.CONFIG_DEVICE_GROUP_NETWORKS, **kwargs)

    def device_groups_config_device_group_devices(self, element_names, device_name, **kwargs):
        """Returns the result of device_groups_config_device_group_devices."""
        args = {"device_name": device_name}

        return self.execute_keyword(element_names, args, self.command_const.CONFIG_DEVICE_GROUP_DEVICES, **kwargs)

    def device_groups_config_device_group_roles(self, element_names, roles, **kwargs):
        """Returns the result of device_groups_config_device_group_roles."""
        args = {"roles": roles}

        return self.execute_keyword(element_names, args, self.command_const.CONFIG_DEVICE_GROUP_ROLES, **kwargs)

    def device_groups_config_device_group_advanced_settings(self, element_names, **kwargs):
        """Returns the result of device_groups_config_device_group_advanced_settings."""
        args = {}

        return self.execute_keyword(element_names, args, self.command_const.CONFIG_DEVICE_GROUP_ADVANCED_SETTINGS,
                                    **kwargs)

    def device_groups_save_config_and_back_to_groups_page(self, element_names, **kwargs):
        """Returns the result of device_groups_save_config_and_back_to_groups_page."""
        args = {}

        return self.execute_keyword(element_names, args, self.command_const.SAVE_CONFIG_AND_BACK_TO_GROUPS_PAGE,
                                    **kwargs)

    def device_groups_delete_existing_device_group(self, element_names, **kwargs):
        """Returns the result of device_groups_delete_existing_device_group."""
        args = {}

        return self.execute_keyword(element_names, args, self.command_const.DELETE_EXISTING_DEVICE_GROUP, **kwargs)

    def device_groups_clone_device_group(self, element_names, **kwargs):
        """Returns the result of device_groups_clone_device_group."""
        args = {}

        return self.execute_keyword(element_names, args, self.command_const.CLONE_DEVICE_GROUP, **kwargs)

    def device_groups_verify_device_group_exists(self, element_names, device_group_name, network_name,
                                                 policy_role_name, **kwargs):
        """Returns the result of device_groups_verify_device_group_exists."""
        args = {"device_group_name": device_group_name,
                "network_name": network_name,
                "policy_role_name": policy_role_name}

        return self.execute_keyword(element_names, args, self.command_const.VERIFY_DEVICE_GROUP_EXISTS, **kwargs)
