"""
This class outlines all the constants for the vpex API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(VpexConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class VpexConstants(ApiConstants):
    def __init__(self):
        super(VpexConstants, self).__init__()
        self.CLEAR_PORTS = {"constant": "clear_ports",
                            "tags": ["COMMAND_CLI"],
                            "link": self.link.clear_ports}
        self.DISABLE_AUTO_CONFIGURATION = {"constant": "disable_auto_configuration",
                                           "tags": ["COMMAND_CLI"],
                                           "link": self.link.disable_auto_configuration}
        self.DISABLE_GLOBAL = {"constant": "disable_global",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.disable_global}
        self.ENABLE_AUTO_CONFIGURATION = {"constant": "enable_auto_configuration",
                                          "tags": ["COMMAND_CLI"],
                                          "link": self.link.enable_auto_configuration}
        self.ENABLE_GLOBAL = {"constant": "enable_global",
                              "tags": ["COMMAND_CLI"],
                              "link": self.link.enable_global}
        self.SET_PORTS = {"constant": "set_ports",
                          "tags": ["COMMAND_CLI"],
                          "link": self.link.set_ports}
        self.SET_RING_REBALANCING_AUTO = {"constant": "set_ring_rebalancing_auto",
                                          "tags": ["COMMAND_CLI"],
                                          "link": self.link.set_ring_rebalancing_auto}
        self.SET_RING_REBALANCING_OFF = {"constant": "set_ring_rebalancing_off",
                                         "tags": ["COMMAND_CLI"],
                                         "link": self.link.set_ring_rebalancing_off}
        self.SHOW_BPE = {"constant": "show_bpe",
                         "tags": ["COMMAND_CLI"],
                         "link": self.link.show_bpe}
        self.SHOW_BPE_CPU_UTILIZATION = {"constant": "show_bpe_cpu_utilization",
                                         "tags": ["COMMAND_CLI"],
                                         "link": self.link.show_bpe_cpu_utilization}
        self.SHOW_BPE_ENVIRONMENT = {"constant": "show_bpe_environment",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.show_bpe_environment}
        self.SHOW_BPE_SLOT = {"constant": "show_bpe_slot",
                              "tags": ["COMMAND_CLI"],
                              "link": self.link.show_bpe_slot}
        self.SHOW_BPE_SLOT_CPU_UTILIZATION = {"constant": "show_bpe_slot_cpu_utilization",
                                              "tags": ["COMMAND_CLI"],
                                              "link": self.link.show_bpe_slot_cpu_utilization}
        self.SHOW_BPE_SLOT_ENVIRONMENT = {"constant": "show_bpe_slot_environment",
                                          "tags": ["COMMAND_CLI"],
                                          "link": self.link.show_bpe_slot_environment}
        self.SHOW_BPE_SLOT_STATISTICS = {"constant": "show_bpe_slot_statistics",
                                         "tags": ["COMMAND_CLI"],
                                         "link": self.link.show_bpe_slot_statistics}
        self.SHOW_BPE_SLOT_STATISTICS_DETAIL = {"constant": "show_bpe_slot_statistics_detail",
                                                "tags": ["COMMAND_CLI"],
                                                "link": self.link.show_bpe_slot_statistics_detail}
        self.SHOW_BPE_SLOT_VERSION_DETAIL = {"constant": "show_bpe_slot_version_detail",
                                             "tags": ["COMMAND_CLI"],
                                             "link": self.link.show_bpe_slot_version_detail}
        self.SHOW_BPE_STATISTICS = {"constant": "show_bpe_statistics",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.show_bpe_statistics}
        self.SHOW_BPE_STATISTICS_DETAIL = {"constant": "show_bpe_statistics_detail",
                                           "tags": ["COMMAND_CLI"],
                                           "link": self.link.show_bpe_statistics_detail}
        self.SHOW_BPE_STATISTICS_DETAIL_SLOT = {"constant": "show_bpe_statistics_detail_slot",
                                                "tags": ["COMMAND_CLI"],
                                                "link": self.link.show_bpe_statistics_detail_slot}
        self.SHOW_BPE_VERSION_DETAIL = {"constant": "show_bpe_version_detail",
                                        "tags": ["COMMAND_CLI"],
                                        "link": self.link.show_bpe_version_detail}
        self.SHOW_INFO = {"constant": "show_info",
                          "tags": ["COMMAND_CLI"],
                          "link": self.link.show_info}
        self.SHOW_PORTS = {"constant": "show_ports",
                           "tags": ["COMMAND_CLI"],
                           "link": self.link.show_ports}
        self.SHOW_PORTS_ECP_STATISTICS = {"constant": "show_ports_ecp_statistics",
                                          "tags": ["COMMAND_CLI"],
                                          "link": self.link.show_ports_ecp_statistics}
        self.SHOW_PORTS_STATISTICS = {"constant": "show_ports_statistics",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.show_ports_statistics}
        self.SHOW_PORTS_STATISTICS_DETAIL = {"constant": "show_ports_statistics_detail",
                                             "tags": ["COMMAND_CLI"],
                                             "link": self.link.show_ports_statistics_detail}
        self.SHOW_TOPOLOGY = {"constant": "show_topology",
                              "tags": ["COMMAND_CLI"],
                              "link": self.link.show_topology}
        self.SHOW_TOPOLOGY_DETAIL = {"constant": "show_topology_detail",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.show_topology_detail}
        self.SHOW_TOPOLOGY_DETAIL_PORT = {"constant": "show_topology_detail_port",
                                          "tags": ["COMMAND_CLI"],
                                          "link": self.link.show_topology_detail_port}
        self.SHOW_TOPOLOGY_PORT = {"constant": "show_topology_port",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.show_topology_port}
        self.SHOW_TOPOLOGY_PORT_DETAIL = {"constant": "show_topology_port_detail",
                                          "tags": ["COMMAND_CLI"],
                                          "link": self.link.show_topology_port_detail}
        self.SHOW_TOPOLOGY_PORT_SUMMARY = {"constant": "show_topology_port_summary",
                                           "tags": ["COMMAND_CLI"],
                                           "link": self.link.show_topology_port_summary}
        self.SHOW_TOPOLOGY_SUMMARY = {"constant": "show_topology_summary",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.show_topology_summary}
        self.SHOW_TOPOLOGY_SUMMARY_PORT = {"constant": "show_topology_summary_port",
                                           "tags": ["COMMAND_CLI"],
                                           "link": self.link.show_topology_summary_port}
