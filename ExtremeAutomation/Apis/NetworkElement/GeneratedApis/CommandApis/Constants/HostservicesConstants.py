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
        self.CLEAR_SYS_CLIPID_TOPOLOGY_IP = {"constant": "clear_sys_clipid_topology_ip",
                                             "tags": ["COMMAND_CLI"],
                                             "link": self.link.clear_sys_clipid_topology_ip}
        self.DISABLE_SYS_FORCE_TOPOLOGY_IP_FLAG = {"constant": "disable_sys_force_topology_ip_flag",
                                                   "tags": ["COMMAND_CLI"],
                                                   "link": self.link.disable_sys_force_topology_ip_flag}
        self.ENABLE_SYS_FORCE_TOPOLOGY_IP_FLAG = {"constant": "enable_sys_force_topology_ip_flag",
                                                  "tags": ["COMMAND_CLI"],
                                                  "link": self.link.enable_sys_force_topology_ip_flag}
        self.SET_SYS_CLIPID_TOPOLOGY_IP = {"constant": "set_sys_clipid_topology_ip",
                                           "tags": ["COMMAND_CLI"],
                                           "link": self.link.set_sys_clipid_topology_ip}
        self.SHOW_AUTOTOPOLOGY_NMM_TABLE = {"constant": "show_autotopology_nmm_table",
                                            "tags": ["COMMAND_CLI"],
                                            "link": self.link.show_autotopology_nmm_table}
        self.SHOW_SYS_SETTING = {"constant": "show_sys_setting",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.show_sys_setting}
