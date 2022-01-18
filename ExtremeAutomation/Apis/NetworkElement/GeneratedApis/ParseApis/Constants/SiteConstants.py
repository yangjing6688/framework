"""
This class outlines all the constants for the site API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(SiteConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class SiteConstants(ApiConstants):
    def __init__(self):
        super(SiteConstants, self).__init__()
        self.CHECK_SITE_AP_EXISTS = {"constant": "check_site_ap_exists",
                                     "tags": ["PARSE_CLI"],
                                     "link": self.link.check_site_ap_exists}
        self.CHECK_SITE_DNS_SERVER_EXISTS = {"constant": "check_site_dns_server_exists",
                                             "tags": ["PARSE_CLI"],
                                             "link": self.link.check_site_dns_server_exists}
        self.CHECK_SITE_EXISTS = {"constant": "check_site_exists",
                                  "tags": ["PARSE_CLI"],
                                  "link": self.link.check_site_exists}
        self.CHECK_SITE_WLAN_RADIO_MODE_EXISTS = {"constant": "check_site_wlan_radio_mode_exists",
                                                  "tags": ["PARSE_CLI"],
                                                  "link": self.link.check_site_wlan_radio_mode_exists}
