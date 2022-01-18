from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.XCA.XcaviewConstants import XcaviewConstants


class UiXcaViewKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiXcaViewKeywords, self).__init__()
        self.api_const = self.constants.API_XCA_VIEW
        self.command_const = XcaviewConstants()

    def view_open_overview_page(self, element_names, **kwargs):
        """Returns the result of view_open_overview_page."""
        args = {}
        return self.execute_keyword(element_names, args, self.command_const.OPEN_OVERVIEW_PAGE, **kwargs)

    def view_open_sites_page(self, element_names, **kwargs):
        """Returns the result of view_open_sites_page."""
        args = {}
        return self.execute_keyword(element_names, args, self.command_const.OPEN_SITES_PAGE, **kwargs)

    def view_open_sites_page_in_expanded_menu(self, element_names, **kwargs):
        """Returns the result of view_open_sites_page_in_expanded_menu."""
        args = {}
        return self.execute_keyword(element_names, args, self.command_const.OPEN_SITES_PAGE_IN_EXPANDED_MENU, **kwargs)

    def view_open_networks_page(self, element_names, **kwargs):
        """Returns the result of view_open_networks_page."""
        args = {}
        return self.execute_keyword(element_names, args, self.command_const.OPEN_NETWORKS_PAGE, **kwargs)

    def view_open_networks_page_in_expanded_menu(self, element_names, **kwargs):
        """Returns the result of view_open_networks_page_in_expanded_menu."""
        args = {}
        return self.execute_keyword(element_names, args, self.command_const.OPEN_NETWORKS_PAGE_IN_EXPANDED_MENU,
                                    **kwargs)

    def view_open_clients_page(self, element_names, **kwargs):
        """Returns the result of view_open_clients_page."""
        args = {}
        return self.execute_keyword(element_names, args, self.command_const.OPEN_CLIENTS_PAGE, **kwargs)

    def view_open_clients_page_in_expanded_menu(self, element_names, **kwargs):
        """Returns the result of view_open_clients_page_in_expanded_menu."""
        args = {}
        return self.execute_keyword(element_names, args, self.command_const.OPEN_CLIENTS_PAGE_IN_EXPANDED_MENU,
                                    **kwargs)

    def view_open_adoption_page_in_devices_section(self, element_names, **kwargs):
        """Returns the result of view_open_adoption_page_in_devices_section."""
        args = {}
        return self.execute_keyword(element_names, args, self.command_const.OPEN_ADOPTION_PAGE_IN_DEVICES_SECTION,
                                    **kwargs)

    def view_open_access_point_page_in_devices_section(self, element_names, **kwargs):
        """Returns the result of view_open_access_point_page_in_devices_section."""
        args = {}
        return self.execute_keyword(element_names, args, self.command_const.OPEN_ACCESS_POINT_PAGE_IN_DEVICES_SECTION,
                                    **kwargs)

    def view_open_switches_page_in_devices_section(self, element_names, **kwargs):
        """Returns the result of view_open_switches_page_in_devices_section."""
        args = {}
        return self.execute_keyword(element_names, args, self.command_const.OPEN_SWITCHES_PAGE_IN_DEVICES_SECTION,
                                    **kwargs)

    def view_open_aaa_page_in_onboard_section(self, element_names, **kwargs):
        """Returns the result of view_open_aaa_page_in_onboard_section."""
        args = {}
        return self.execute_keyword(element_names, args, self.command_const.OPEN_AAA_PAGE_IN_ONBOARD_SECTION, **kwargs)

    def view_open_portal_page_in_onboard_section(self, element_names, **kwargs):
        """Returns the result of view_open_portal_page_in_onboard_section."""
        args = {}
        return self.execute_keyword(element_names, args, self.command_const.OPEN_PORTAL_PAGE_IN_ONBOARD_SECTION,
                                    **kwargs)

    def view_open_groups_page_in_onboard_section(self, element_names, **kwargs):
        """Returns the result of view_open_groups_page_in_onboard_section."""
        args = {}
        return self.execute_keyword(element_names, args, self.command_const.OPEN_GROUPS_PAGE_IN_ONBOARD_SECTION,
                                    **kwargs)

    def view_open_rules_page_in_onboard_section(self, element_names, **kwargs):
        """Returns the result of view_open_rules_page_in_onboard_section."""
        args = {}
        return self.execute_keyword(element_names, args, self.command_const.OPEN_RULES_PAGE_IN_ONBOARD_SECTION,
                                    **kwargs)

    def view_open_roles_page_in_policy_section(self, element_names, **kwargs):
        """Returns the result of view_open_roles_page_in_policy_section."""
        args = {}
        return self.execute_keyword(element_names, args, self.command_const.OPEN_ROLES_PAGE_IN_POLICY_SECTION, **kwargs)

    def view_open_class_of_service_page_in_policy_section(self, element_names, **kwargs):
        """Returns the result of view_open_class_of_service_page_in_policy_section."""
        args = {}
        return self.execute_keyword(element_names, args,
                                    self.command_const.OPEN_CLASS_OF_SERVICE_PAGE_IN_POLICY_SECTION, **kwargs)

    def view_open_vlans_page_in_policy_section(self, element_names, **kwargs):
        """Returns the result of view_open_vlans_page_in_policy_section."""
        args = {}
        return self.execute_keyword(element_names, args, self.command_const.OPEN_VLANS_PAGE_IN_POLICY_SECTION, **kwargs)

    def view_open_vlan_groups_page_in_policy_section(self, element_names, **kwargs):
        """Returns the result of view_open_vlan_groups_page_in_policy_section."""
        args = {}
        return self.execute_keyword(element_names, args, self.command_const.OPEN_VLAN_GROUPS_PAGE_IN_POLICY_SECTION,
                                    **kwargs)

    def view_open_rates_page_in_policy_section(self, element_names, **kwargs):
        """Returns the result of view_open_rates_page_in_policy_section."""
        args = {}
        return self.execute_keyword(element_names, args, self.command_const.OPEN_RATES_PAGE_IN_POLICY_SECTION, **kwargs)

    def view_open_system_page_in_admin_section(self, element_names, **kwargs):
        """Returns the result of view_open_system_page_in_admin_section."""
        args = {}
        return self.execute_keyword(element_names, args, self.command_const.OPEN_SYSTEM_PAGE_IN_ADMIN_SECTION, **kwargs)

    def view_open_utilities_page_in_admin_section(self, element_names, **kwargs):
        """Returns the result of view_open_utilities_page_in_admin_section."""
        args = {}
        return self.execute_keyword(element_names, args, self.command_const.OPEN_UTILITIES_PAGE_IN_ADMIN_SECTION,
                                    **kwargs)

    def view_open_license_page_in_admin_section(self, element_names, **kwargs):
        """Returns the result of view_open_license_page_in_admin_section."""
        args = {}
        return self.execute_keyword(element_names, args, self.command_const.OPEN_LICENSE_PAGE_IN_ADMIN_SECTION,
                                    **kwargs)

    def view_open_logs_page_in_admin_section(self, element_names, **kwargs):
        """Returns the result of view_open_logs_page_in_admin_section."""
        args = {}
        return self.execute_keyword(element_names, args, self.command_const.OPEN_LOGS_PAGE_IN_ADMIN_SECTION, **kwargs)

    def view_open_accounts_page_in_admin_section(self, element_names, **kwargs):
        """Returns the result of view_open_accounts_page_in_admin_section."""
        args = {}
        return self.execute_keyword(element_names, args, self.command_const.OPEN_ACCOUNTS_PAGE_IN_ADMIN_SECTION,
                                    **kwargs)

    def view_open_applications_page_in_admin_section(self, element_names, **kwargs):
        """Returns the result of view_open_applications_page_in_admin_section."""
        args = {}
        return self.execute_keyword(element_names, args, self.command_const.OPEN_APPLICATIONS_PAGE_IN_ADMIN_SECTION,
                                    **kwargs)

    def view_open_wlans_page_in_networks_section(self, element_names, **kwargs):
        """Returns the result of view_open_wlans_page_in_networks_section."""
        args = {}
        return self.execute_keyword(element_names, args, self.command_const.OPEN_WLANS_PAGE_IN_NETWORKS_SECTION,
                                    **kwargs)

    def view_open_meshpoints_page_in_networks_section(self, element_names, **kwargs):
        """Returns the result of view_open_meshpoints_page_in_networks_section."""
        args = {}
        return self.execute_keyword(element_names, args, self.command_const.OPEN_MESHPOINTS_PAGE_IN_NETWORKS_SECTION,
                                    **kwargs)
