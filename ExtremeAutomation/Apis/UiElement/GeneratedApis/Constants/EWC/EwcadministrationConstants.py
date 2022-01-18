"""
This class outlines all the constants for the ewcadministration API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(EwcadministrationConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class EwcadministrationConstants(ApiConstants):
    def __init__(self):
        super(EwcadministrationConstants, self).__init__()
        self.ADMINISTRATION_ADD_PRIMARY_DNS_SERVER_ON_HOST = {"constant": "administration_add_primary_dns_server_on_host",
                                                              "tags": ["COMMAND_SELENIUM"],
                                                              "link": self.link.administration_add_primary_dns_server_on_host}
        self.ADMINISTRATION_CLICK_SAVE_BUTTON = {"constant": "administration_click_save_button",
                                                 "tags": ["COMMAND_SELENIUM"],
                                                 "link": self.link.administration_click_save_button}
        self.ADMINISTRATION_DELETE_PRIMARY_DNS_SERVER_ON_HOST = {"constant": "administration_delete_primary_dns_server_on_host",
                                                                 "tags": ["COMMAND_SELENIUM"],
                                                                 "link": self.link.administration_delete_primary_dns_server_on_host}
        self.ADMINISTRATION_DOMAIN_NAME_SHOULD_EXIST = {"constant": "administration_domain_name_should_exist",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.administration_domain_name_should_exist}
        self.ADMINISTRATION_DOMAIN_NAME_SHOULD_NOT_EXIST = {"constant": "administration_domain_name_should_not_exist",
                                                            "tags": ["COMMAND_SELENIUM"],
                                                            "link": self.link.administration_domain_name_should_not_exist}
        self.ADMINISTRATION_HOSTNAME_SHOULD_EXIST = {"constant": "administration_hostname_should_exist",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.administration_hostname_should_exist}
        self.ADMINISTRATION_HOSTNAME_SHOULD_NOT_EXIST = {"constant": "administration_hostname_should_not_exist",
                                                         "tags": ["COMMAND_SELENIUM"],
                                                         "link": self.link.administration_hostname_should_not_exist}
        self.ADMINISTRATION_RENAME_DOMAIN_NAME = {"constant": "administration_rename_domain_name",
                                                  "tags": ["COMMAND_SELENIUM"],
                                                  "link": self.link.administration_rename_domain_name}
        self.ADMINISTRATION_RENAME_HOSTNAME = {"constant": "administration_rename_hostname",
                                               "tags": ["COMMAND_SELENIUM"],
                                               "link": self.link.administration_rename_hostname}
        self.ADMINISTRATION_VALIDATE_PRIMARY_DNS_SERVER_IP_ON_HOST = {"constant": "administration_validate_primary_dns_server_ip_on_host",
                                                                      "tags": ["COMMAND_SELENIUM"],
                                                                      "link": self.link.administration_validate_primary_dns_server_ip_on_host}
