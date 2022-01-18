"""
This class outlines all the constants for the cfm API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(CfmConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class CfmConstants(ApiConstants):
    def __init__(self):
        super(CfmConstants, self).__init__()
        self.CLEAR_MAINTENANCE_ASSOCIATION = {"constant": "clear_maintenance_association",
                                              "tags": ["COMMAND_SNMP"],
                                              "link": self.link.clear_maintenance_association}
        self.CLEAR_MAINTENANCE_DOMAIN = {"constant": "clear_maintenance_domain",
                                         "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                         "link": self.link.clear_maintenance_domain}
        self.CLEAR_MAINTENANCE_ENDPOINT = {"constant": "clear_maintenance_endpoint",
                                           "tags": ["COMMAND_SNMP"],
                                           "link": self.link.clear_maintenance_endpoint}
        self.CLEAR_SPBM_LEVEL = {"constant": "clear_spbm_level",
                                 "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                 "link": self.link.clear_spbm_level}
        self.CLEAR_SPBM_MEPID = {"constant": "clear_spbm_mepid",
                                 "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                 "link": self.link.clear_spbm_mepid}
        self.DISABLE_MAINTENANCE_ENDPOINT = {"constant": "disable_maintenance_endpoint",
                                             "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                             "link": self.link.disable_maintenance_endpoint}
        self.DISABLE_SPBM = {"constant": "disable_spbm",
                             "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                             "link": self.link.disable_spbm}
        self.ENABLE_MAINTENANCE_ENDPOINT = {"constant": "enable_maintenance_endpoint",
                                            "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                            "link": self.link.enable_maintenance_endpoint}
        self.ENABLE_SPBM = {"constant": "enable_spbm",
                            "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                            "link": self.link.enable_spbm}
        self.SET_MAINTENANCE_ASSOCIATION = {"constant": "set_maintenance_association",
                                            "tags": ["COMMAND_SNMP"],
                                            "link": self.link.set_maintenance_association}
        self.SET_MAINTENANCE_DOMAIN = {"constant": "set_maintenance_domain",
                                       "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                       "link": self.link.set_maintenance_domain}
        self.SET_MAINTENANCE_DOMAIN_INDEX = {"constant": "set_maintenance_domain_index",
                                             "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                             "link": self.link.set_maintenance_domain_index}
        self.SET_MAINTENANCE_DOMAIN_LEVEL = {"constant": "set_maintenance_domain_level",
                                             "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                             "link": self.link.set_maintenance_domain_level}
        self.SET_MAINTENANCE_DOMAIN_NAME = {"constant": "set_maintenance_domain_name",
                                            "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                            "link": self.link.set_maintenance_domain_name}
        self.SET_MAINTENANCE_ENDPOINT = {"constant": "set_maintenance_endpoint",
                                         "tags": ["COMMAND_SNMP"],
                                         "link": self.link.set_maintenance_endpoint}
        self.SET_SPBM_LEVEL = {"constant": "set_spbm_level",
                               "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                               "link": self.link.set_spbm_level}
        self.SET_SPBM_MEPID = {"constant": "set_spbm_mepid",
                               "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                               "link": self.link.set_spbm_mepid}
        self.SHOW_ASSOCIATION_NAME = {"constant": "show_association_name",
                                      "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                      "link": self.link.show_association_name}
        self.SHOW_CMAC = {"constant": "show_cmac",
                          "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                          "link": self.link.show_cmac}
        self.SHOW_DOMAIN_NAME = {"constant": "show_domain_name",
                                 "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                 "link": self.link.show_domain_name}
        self.SHOW_MAINTENANCE_ASSOCIATION = {"constant": "show_maintenance_association",
                                             "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                             "link": self.link.show_maintenance_association}
        self.SHOW_MAINTENANCE_DOMAIN = {"constant": "show_maintenance_domain",
                                        "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                        "link": self.link.show_maintenance_domain}
        self.SHOW_MAINTENANCE_ENDPOINT = {"constant": "show_maintenance_endpoint",
                                          "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                          "link": self.link.show_maintenance_endpoint}
        self.SHOW_SPBM = {"constant": "show_spbm",
                          "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                          "link": self.link.show_spbm}
