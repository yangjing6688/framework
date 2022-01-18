from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.XCA.XcasitesConstants import XcasitesConstants


class UiXcaSitesKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiXcaSitesKeywords, self).__init__()
        self.api_const = self.constants.API_XCA_SITES
        self.command_const = XcasitesConstants()

    def sites_select_site_and_config(self, element_names, site_name, **kwargs):
        """Returns the result of sites_select_site_and_config."""
        args = {"site_name": site_name}

        return self.execute_keyword(element_names, args, self.command_const.SELECT_SITE_AND_CONFIG, **kwargs)

    def sites_open_site_device_groups_page(self, element_names, **kwargs):
        """Returns the result of sites_open_site_device_groups_page."""
        args = {}

        return self.execute_keyword(element_names, args, self.command_const.OPEN_SITE_DEVICE_GROUPS_PAGE, **kwargs)

    def sites_click_site_open_detail_page(self, element_names, **kwargs):
        """Returns the result of sites_click_site_open_detail_page."""
        args = {}

        return self.execute_keyword(element_names, args, self.command_const.CLICK_SITE_OPEN_DETAIL_PAGE, **kwargs)

    def sites_open_site_floor_plans_page(self, element_names, **kwargs):
        """Returns the result of sites_open_site_floor_plans_page."""
        args = {}

        return self.execute_keyword(element_names, args, self.command_const.OPEN_SITE_FLOOR_PLANS_PAGE, **kwargs)

    def sites_open_site_location_page(self, element_names, **kwargs):
        """Returns the result of sites_open_site_location_page."""
        args = {}

        return self.execute_keyword(element_names, args, self.command_const.OPEN_SITE_LOCATION_PAGE, **kwargs)

    def sites_open_site_switches_page(self, element_names, **kwargs):
        """Returns the result of sites_open_site_switches_page."""
        args = {}

        return self.execute_keyword(element_names, args, self.command_const.OPEN_SITE_SWITCHES_PAGE, **kwargs)

    def sites_open_site_snmp_page(self, element_names, **kwargs):
        """Returns the result of sites_open_site_snmp_page."""
        args = {}

        return self.execute_keyword(element_names, args, self.command_const.OPEN_SITE_SNMP_PAGE, **kwargs)

    def sites_click_name_to_open_device_group_edit_window(self, element_names, **kwargs):
        """Returns the result of sites_click_name_to_open_device_group_edit_window."""
        args = {}

        return self.execute_keyword(element_names, args,
                                    self.command_const.CLICK_NAME_TO_OPEN_DEVICE_GROUP_EDIT_WINDOW, **kwargs)

    def sites_close_device_group_edit_window(self, element_names, **kwargs):
        """Returns the result of sites_close_device_group_edit_window."""
        args = {}

        return self.execute_keyword(element_names, args, self.command_const.CLOSE_DEVICE_GROUP_EDIT_WINDOW, **kwargs)

    def sites_open_device_group_profile_edit_window(self, element_names, **kwargs):
        """Returns the result of sites_open_device_group_profile_edit_window."""
        args = {}

        return self.execute_keyword(element_names, args, self.command_const.OPEN_DEVICE_GROUP_PROFILE_EDIT_WINDOW,
                                    **kwargs)

    def sites_config_radios_for_device_group_profile(self, element_names, **kwargs):
        """Returns the result of sites_config_radios_for_device_group_profile."""
        args = {}

        return self.execute_keyword(element_names, args, self.command_const.CONFIG_RADIOS_FOR_DEVICE_GROUP_PROFILE,
                                    **kwargs)

    def sites_select_roles_for_device_group_profile(self, element_names, **kwargs):
        """Returns the result of sites_select_roles_for_device_group_profile."""
        args = {}

        return self.execute_keyword(element_names, args, self.command_const.SELECT_ROLES_FOR_DEVICE_GROUP_PROFILE,
                                    **kwargs)

    def sites_deselect_roles_for_device_group_profile(self, element_names, **kwargs):
        """Returns the result of sites_deselect_roles_for_device_group_profile."""
        args = {}

        return self.execute_keyword(element_names, args, self.command_const.DESELECT_ROLES_FOR_DEVICE_GROUP_PROFILE,
                                    **kwargs)

    def sites_save_device_group_profile_config(self, element_names, **kwargs):
        """Returns the result of sites_save_device_group_profile_config."""
        args = {}

        return self.execute_keyword(element_names, args, self.command_const.SAVE_DEVICE_GROUP_PROFILE_CONFIG, **kwargs)

    def sites_save_site_config_and_back_to_site_page(self, element_names, **kwargs):
        """Returns the result of sites_save_site_config_and_back_to_site_page."""
        args = {}

        return self.execute_keyword(element_names, args, self.command_const.SAVE_SITE_CONFIG_AND_BACK_TO_SITE_PAGE,
                                    **kwargs)
