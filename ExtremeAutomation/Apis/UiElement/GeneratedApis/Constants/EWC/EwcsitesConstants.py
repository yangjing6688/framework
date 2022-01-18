"""
This class outlines all the constants for the ewcsites API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(EwcsitesConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class EwcsitesConstants(ApiConstants):
    def __init__(self):
        super(EwcsitesConstants, self).__init__()
        self.SITES_ADD_AP_TO_SITE = {"constant": "sites_add_ap_to_site",
                                     "tags": ["COMMAND_SELENIUM"],
                                     "link": self.link.sites_add_ap_to_site}
        self.SITES_ADD_DEFAULT_DNS_SERVER_TO_SITE = {"constant": "sites_add_default_dns_server_to_site",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.sites_add_default_dns_server_to_site}
        self.SITES_ADD_WLAN_RADIOS_TO_SITE = {"constant": "sites_add_wlan_radios_to_site",
                                              "tags": ["COMMAND_SELENIUM"],
                                              "link": self.link.sites_add_wlan_radios_to_site}
        self.SITES_AP_SHOULD_BE_ENABLED_FOR_SITE = {"constant": "sites_ap_should_be_enabled_for_site",
                                                    "tags": ["COMMAND_SELENIUM"],
                                                    "link": self.link.sites_ap_should_be_enabled_for_site}
        self.SITES_CLICK_SAVE_BUTTON = {"constant": "sites_click_save_button",
                                        "tags": ["COMMAND_SELENIUM"],
                                        "link": self.link.sites_click_save_button}
        self.SITES_CREATE_SITE = {"constant": "sites_create_site",
                                  "tags": ["COMMAND_SELENIUM"],
                                  "link": self.link.sites_create_site}
        self.SITES_DELETE_SITE = {"constant": "sites_delete_site",
                                  "tags": ["COMMAND_SELENIUM"],
                                  "link": self.link.sites_delete_site}
        self.SITES_REMOVE_AP_FROM_SITE = {"constant": "sites_remove_ap_from_site",
                                          "tags": ["COMMAND_SELENIUM"],
                                          "link": self.link.sites_remove_ap_from_site}
        self.SITES_REMOVE_WLAN_RADIOS_FROM_SITE = {"constant": "sites_remove_wlan_radios_from_site",
                                                   "tags": ["COMMAND_SELENIUM"],
                                                   "link": self.link.sites_remove_wlan_radios_from_site}
        self.SITES_SELECT_TAB_IN_SITE_PAGE = {"constant": "sites_select_tab_in_site_page",
                                              "tags": ["COMMAND_SELENIUM"],
                                              "link": self.link.sites_select_tab_in_site_page}
        self.SITES_SITE_SHOULD_EXIST = {"constant": "sites_site_should_exist",
                                        "tags": ["COMMAND_SELENIUM"],
                                        "link": self.link.sites_site_should_exist}
        self.SITES_SITE_SHOULD_NOT_EXIST = {"constant": "sites_site_should_not_exist",
                                            "tags": ["COMMAND_SELENIUM"],
                                            "link": self.link.sites_site_should_not_exist}
        self.SITES_VALIDATE_DEFAULT_DNS_SERVER_IP_FOR_SITE = {"constant": "sites_validate_default_dns_server_ip_for_site",
                                                              "tags": ["COMMAND_SELENIUM"],
                                                              "link": self.link.sites_validate_default_dns_server_ip_for_site}
        self.SITES_WLAN_SHOULD_BE_ENABLED_FOR_SITE = {"constant": "sites_wlan_should_be_enabled_for_site",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.sites_wlan_should_be_enabled_for_site}
