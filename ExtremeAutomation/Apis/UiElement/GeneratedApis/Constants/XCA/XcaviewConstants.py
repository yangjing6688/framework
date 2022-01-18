"""
This class outlines all the constants for the xcaview API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(XcaviewConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class XcaviewConstants(ApiConstants):
    def __init__(self):
        super(XcaviewConstants, self).__init__()
        self.OPEN_AAA_PAGE_IN_ONBOARD_SECTION = {"constant": "open_aaa_page_in_onboard_section",
                                                 "tags": ["COMMAND_SELENIUM"],
                                                 "link": self.link.open_aaa_page_in_onboard_section}
        self.OPEN_ACCESS_POINT_PAGE_IN_DEVICES_SECTION = {"constant": "open_access_point_page_in_devices_section",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.open_access_point_page_in_devices_section}
        self.OPEN_ACCOUNTS_PAGE_IN_ADMIN_SECTION = {"constant": "open_accounts_page_in_admin_section",
                                                    "tags": ["COMMAND_SELENIUM"],
                                                    "link": self.link.open_accounts_page_in_admin_section}
        self.OPEN_ADOPTION_PAGE_IN_DEVICES_SECTION = {"constant": "open_adoption_page_in_devices_section",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.open_adoption_page_in_devices_section}
        self.OPEN_APPLICATIONS_PAGE_IN_ADMIN_SECTION = {"constant": "open_applications_page_in_admin_section",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.open_applications_page_in_admin_section}
        self.OPEN_CLASS_OF_SERVICE_PAGE_IN_POLICY_SECTION = {"constant": "open_class_of_service_page_in_policy_section",
                                                             "tags": ["COMMAND_SELENIUM"],
                                                             "link": self.link.open_class_of_service_page_in_policy_section}
        self.OPEN_CLIENTS_PAGE = {"constant": "open_clients_page",
                                  "tags": ["COMMAND_SELENIUM"],
                                  "link": self.link.open_clients_page}
        self.OPEN_CLIENTS_PAGE_IN_EXPANDED_MENU = {"constant": "open_clients_page_in_expanded_menu",
                                                   "tags": ["COMMAND_SELENIUM"],
                                                   "link": self.link.open_clients_page_in_expanded_menu}
        self.OPEN_GROUPS_PAGE_IN_ONBOARD_SECTION = {"constant": "open_groups_page_in_onboard_section",
                                                    "tags": ["COMMAND_SELENIUM"],
                                                    "link": self.link.open_groups_page_in_onboard_section}
        self.OPEN_LICENSE_PAGE_IN_ADMIN_SECTION = {"constant": "open_license_page_in_admin_section",
                                                   "tags": ["COMMAND_SELENIUM"],
                                                   "link": self.link.open_license_page_in_admin_section}
        self.OPEN_LOGS_PAGE_IN_ADMIN_SECTION = {"constant": "open_logs_page_in_admin_section",
                                                "tags": ["COMMAND_SELENIUM"],
                                                "link": self.link.open_logs_page_in_admin_section}
        self.OPEN_MESHPOINTS_PAGE_IN_NETWORKS_SECTION = {"constant": "open_meshpoints_page_in_networks_section",
                                                         "tags": ["COMMAND_SELENIUM"],
                                                         "link": self.link.open_meshpoints_page_in_networks_section}
        self.OPEN_NETWORKS_PAGE = {"constant": "open_networks_page",
                                   "tags": ["COMMAND_SELENIUM"],
                                   "link": self.link.open_networks_page}
        self.OPEN_NETWORKS_PAGE_IN_EXPANDED_MENU = {"constant": "open_networks_page_in_expanded_menu",
                                                    "tags": ["COMMAND_SELENIUM"],
                                                    "link": self.link.open_networks_page_in_expanded_menu}
        self.OPEN_OVERVIEW_PAGE = {"constant": "open_overview_page",
                                   "tags": ["COMMAND_SELENIUM"],
                                   "link": self.link.open_overview_page}
        self.OPEN_PAGE_IN_LEFT_VIEW_EXPANDED_MENU = {"constant": "open_page_in_left_view_expanded_menu",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.open_page_in_left_view_expanded_menu}
        self.OPEN_PAGE_IN_LEFT_VIEW_MENU = {"constant": "open_page_in_left_view_menu",
                                            "tags": ["COMMAND_SELENIUM"],
                                            "link": self.link.open_page_in_left_view_menu}
        self.OPEN_PAGE_IN_LEFT_VIEW_SUBMENU = {"constant": "open_page_in_left_view_submenu",
                                               "tags": ["COMMAND_SELENIUM"],
                                               "link": self.link.open_page_in_left_view_submenu}
        self.OPEN_PORTAL_PAGE_IN_ONBOARD_SECTION = {"constant": "open_portal_page_in_onboard_section",
                                                    "tags": ["COMMAND_SELENIUM"],
                                                    "link": self.link.open_portal_page_in_onboard_section}
        self.OPEN_RATES_PAGE_IN_POLICY_SECTION = {"constant": "open_rates_page_in_policy_section",
                                                  "tags": ["COMMAND_SELENIUM"],
                                                  "link": self.link.open_rates_page_in_policy_section}
        self.OPEN_ROLES_PAGE_IN_POLICY_SECTION = {"constant": "open_roles_page_in_policy_section",
                                                  "tags": ["COMMAND_SELENIUM"],
                                                  "link": self.link.open_roles_page_in_policy_section}
        self.OPEN_RULES_PAGE_IN_ONBOARD_SECTION = {"constant": "open_rules_page_in_onboard_section",
                                                   "tags": ["COMMAND_SELENIUM"],
                                                   "link": self.link.open_rules_page_in_onboard_section}
        self.OPEN_SITES_PAGE = {"constant": "open_sites_page",
                                "tags": ["COMMAND_SELENIUM"],
                                "link": self.link.open_sites_page}
        self.OPEN_SITES_PAGE_IN_EXPANDED_MENU = {"constant": "open_sites_page_in_expanded_menu",
                                                 "tags": ["COMMAND_SELENIUM"],
                                                 "link": self.link.open_sites_page_in_expanded_menu}
        self.OPEN_SWITCHES_PAGE_IN_DEVICES_SECTION = {"constant": "open_switches_page_in_devices_section",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.open_switches_page_in_devices_section}
        self.OPEN_SYSTEM_PAGE_IN_ADMIN_SECTION = {"constant": "open_system_page_in_admin_section",
                                                  "tags": ["COMMAND_SELENIUM"],
                                                  "link": self.link.open_system_page_in_admin_section}
        self.OPEN_UTILITIES_PAGE_IN_ADMIN_SECTION = {"constant": "open_utilities_page_in_admin_section",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.open_utilities_page_in_admin_section}
        self.OPEN_VLANS_PAGE_IN_POLICY_SECTION = {"constant": "open_vlans_page_in_policy_section",
                                                  "tags": ["COMMAND_SELENIUM"],
                                                  "link": self.link.open_vlans_page_in_policy_section}
        self.OPEN_VLAN_GROUPS_PAGE_IN_POLICY_SECTION = {"constant": "open_vlan_groups_page_in_policy_section",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.open_vlan_groups_page_in_policy_section}
        self.OPEN_WLANS_PAGE_IN_NETWORKS_SECTION = {"constant": "open_wlans_page_in_networks_section",
                                                    "tags": ["COMMAND_SELENIUM"],
                                                    "link": self.link.open_wlans_page_in_networks_section}
