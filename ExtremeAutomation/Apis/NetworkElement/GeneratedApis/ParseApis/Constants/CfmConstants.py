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
        self.CHECK_CFM_CMAC_LEVEL = {"constant": "check_cfm_cmac_level",
                                     "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                     "link": self.link.check_cfm_cmac_level}
        self.CHECK_CFM_CMAC_MAC = {"constant": "check_cfm_cmac_mac",
                                   "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                   "link": self.link.check_cfm_cmac_mac}
        self.CHECK_CFM_CMAC_MEPID = {"constant": "check_cfm_cmac_mepid",
                                     "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                     "link": self.link.check_cfm_cmac_mepid}
        self.CHECK_CFM_CMAC_STATE = {"constant": "check_cfm_cmac_state",
                                     "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                     "link": self.link.check_cfm_cmac_state}
        self.CHECK_CFM_DOMAIN = {"constant": "check_cfm_domain",
                                 "tags": ["PARSE_CLI"],
                                 "link": self.link.check_cfm_domain}
        self.CHECK_CFM_GROUP = {"constant": "check_cfm_group",
                                "tags": ["PARSE_CLI"],
                                "link": self.link.check_cfm_group}
        self.CHECK_CFM_MAINTENANCE_ASSOCIATION_DOMAIN_INDEX = {"constant": "check_cfm_maintenance_association_domain_index",
                                                               "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                               "link": self.link.check_cfm_maintenance_association_domain_index}
        self.CHECK_CFM_MAINTENANCE_ASSOCIATION_DOMAIN_NAME = {"constant": "check_cfm_maintenance_association_domain_name",
                                                              "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                              "link": self.link.check_cfm_maintenance_association_domain_name}
        self.CHECK_CFM_MAINTENANCE_ASSOCIATION_INDEX = {"constant": "check_cfm_maintenance_association_index",
                                                        "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                        "link": self.link.check_cfm_maintenance_association_index}
        self.CHECK_CFM_MAINTENANCE_ASSOCIATION_NAME = {"constant": "check_cfm_maintenance_association_name",
                                                       "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                       "link": self.link.check_cfm_maintenance_association_name}
        self.CHECK_CFM_MAINTENANCE_DOMAIN = {"constant": "check_cfm_maintenance_domain",
                                             "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                             "link": self.link.check_cfm_maintenance_domain}
        self.CHECK_CFM_MAINTENANCE_DOMAIN_INDEX = {"constant": "check_cfm_maintenance_domain_index",
                                                   "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                   "link": self.link.check_cfm_maintenance_domain_index}
        self.CHECK_CFM_MAINTENANCE_DOMAIN_LEVEL = {"constant": "check_cfm_maintenance_domain_level",
                                                   "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                   "link": self.link.check_cfm_maintenance_domain_level}
        self.CHECK_CFM_MAINTENANCE_DOMAIN_NAME = {"constant": "check_cfm_maintenance_domain_name",
                                                  "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                  "link": self.link.check_cfm_maintenance_domain_name}
        self.CHECK_CFM_MAINTENANCE_DOMAIN_TYPE = {"constant": "check_cfm_maintenance_domain_type",
                                                  "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                  "link": self.link.check_cfm_maintenance_domain_type}
        self.CHECK_CFM_MAINTENANCE_ENDPOINT_ASSOCIATION_NAME = {"constant": "check_cfm_maintenance_endpoint_association_name",
                                                                "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                                "link": self.link.check_cfm_maintenance_endpoint_association_name}
        self.CHECK_CFM_MAINTENANCE_ENDPOINT_DOMAIN_NAME = {"constant": "check_cfm_maintenance_endpoint_domain_name",
                                                           "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                           "link": self.link.check_cfm_maintenance_endpoint_domain_name}
        self.CHECK_CFM_MAINTENANCE_ENDPOINT_MEPID = {"constant": "check_cfm_maintenance_endpoint_mepid",
                                                     "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                     "link": self.link.check_cfm_maintenance_endpoint_mepid}
        self.CHECK_CFM_MAINTENANCE_ENDPOINT_STATE = {"constant": "check_cfm_maintenance_endpoint_state",
                                                     "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                     "link": self.link.check_cfm_maintenance_endpoint_state}
        self.CHECK_CFM_SEGMENT = {"constant": "check_cfm_segment",
                                  "tags": ["PARSE_CLI"],
                                  "link": self.link.check_cfm_segment}
        self.CHECK_CFM_SPBM_LEVEL = {"constant": "check_cfm_spbm_level",
                                     "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                     "link": self.link.check_cfm_spbm_level}
        self.CHECK_CFM_SPBM_MAC = {"constant": "check_cfm_spbm_mac",
                                   "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                   "link": self.link.check_cfm_spbm_mac}
        self.CHECK_CFM_SPBM_MEPID = {"constant": "check_cfm_spbm_mepid",
                                     "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                     "link": self.link.check_cfm_spbm_mepid}
        self.CHECK_CFM_SPBM_STATE = {"constant": "check_cfm_spbm_state",
                                     "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                     "link": self.link.check_cfm_spbm_state}
        self.CHECK_CFM_SPBM_STATE_ENABLE = {"constant": "check_cfm_spbm_state_enable",
                                            "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                            "link": self.link.check_cfm_spbm_state_enable}
        self.CHECK_CFM_STATE = {"constant": "check_cfm_state",
                                "tags": ["PARSE_CLI"],
                                "link": self.link.check_cfm_state}
