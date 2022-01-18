"""
This class outlines all the constants for the hostservices API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(HostservicesConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class HostservicesConstants(ApiConstants):
    def __init__(self):
        super(HostservicesConstants, self).__init__()
        self.VERIFY_AUTOTOPOLOGY_NMM_TABLE_ENTRIES = {"constant": "verify_autotopology_nmm_table_entries",
                                                      "tags": ["PARSE_CLI"],
                                                      "link": self.link.verify_autotopology_nmm_table_entries}
        self.VERIFY_SYS_CLIPID_TOPOLOGY_IP = {"constant": "verify_sys_clipid_topology_ip",
                                              "tags": ["PARSE_CLI"],
                                              "link": self.link.verify_sys_clipid_topology_ip}
        self.VERIFY_SYS_FORCE_TOPOLOGY_IP_FLAG_IS_DISABLED = {"constant": "verify_sys_force_topology_ip_flag_is_disabled",
                                                              "tags": ["PARSE_CLI"],
                                                              "link": self.link.verify_sys_force_topology_ip_flag_is_disabled}
        self.VERIFY_SYS_FORCE_TOPOLOGY_IP_FLAG_IS_ENABLED = {"constant": "verify_sys_force_topology_ip_flag_is_enabled",
                                                             "tags": ["PARSE_CLI"],
                                                             "link": self.link.verify_sys_force_topology_ip_flag_is_enabled}
