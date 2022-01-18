"""
This class outlines all the constants for the lldp API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(LldpConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class LldpConstants(ApiConstants):
    def __init__(self):
        super(LldpConstants, self).__init__()
        self.CLEAR_SYS_NAME = {"constant": "clear_sys_name",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.clear_sys_name}
        self.DISABLE = {"constant": "disable",
                        "tags": ["COMMAND_CLI"],
                        "link": self.link.disable}
        self.DISABLE_PORT = {"constant": "disable_port",
                             "tags": ["COMMAND_CLI", "COMMAND_REST"],
                             "link": self.link.disable_port}
        self.DISABLE_TLV_ALL = {"constant": "disable_tlv_all",
                                "tags": ["COMMAND_CLI"],
                                "link": self.link.disable_tlv_all}
        self.DISABLE_TLV_APPLICATION_PRI = {"constant": "disable_tlv_application_pri",
                                            "tags": ["COMMAND_CLI"],
                                            "link": self.link.disable_tlv_application_pri}
        self.DISABLE_TLV_CONGESTION_NOTIF = {"constant": "disable_tlv_congestion_notif",
                                             "tags": ["COMMAND_CLI"],
                                             "link": self.link.disable_tlv_congestion_notif}
        self.DISABLE_TLV_ENERGY_EFF_ETH = {"constant": "disable_tlv_energy_eff_eth",
                                           "tags": ["COMMAND_CLI"],
                                           "link": self.link.disable_tlv_energy_eff_eth}
        self.DISABLE_TLV_ENHANCED_TRANS_CONFIG = {"constant": "disable_tlv_enhanced_trans_config",
                                                  "tags": ["COMMAND_CLI"],
                                                  "link": self.link.disable_tlv_enhanced_trans_config}
        self.DISABLE_TLV_ENHANCED_TRANS_REC = {"constant": "disable_tlv_enhanced_trans_rec",
                                               "tags": ["COMMAND_CLI"],
                                               "link": self.link.disable_tlv_enhanced_trans_rec}
        self.DISABLE_TLV_GVRP = {"constant": "disable_tlv_gvrp",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.disable_tlv_gvrp}
        self.DISABLE_TLV_LACP = {"constant": "disable_tlv_lacp",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.disable_tlv_lacp}
        self.DISABLE_TLV_LINK_AGGR = {"constant": "disable_tlv_link_aggr",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.disable_tlv_link_aggr}
        self.DISABLE_TLV_MAC_PHY = {"constant": "disable_tlv_mac_phy",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.disable_tlv_mac_phy}
        self.DISABLE_TLV_MAX_FRAME = {"constant": "disable_tlv_max_frame",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.disable_tlv_max_frame}
        self.DISABLE_TLV_MED_CAP = {"constant": "disable_tlv_med_cap",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.disable_tlv_med_cap}
        self.DISABLE_TLV_MED_LOC = {"constant": "disable_tlv_med_loc",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.disable_tlv_med_loc}
        self.DISABLE_TLV_MED_POE = {"constant": "disable_tlv_med_poe",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.disable_tlv_med_poe}
        self.DISABLE_TLV_MED_POL = {"constant": "disable_tlv_med_pol",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.disable_tlv_med_pol}
        self.DISABLE_TLV_MGMT_ADDR = {"constant": "disable_tlv_mgmt_addr",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.disable_tlv_mgmt_addr}
        self.DISABLE_TLV_POE = {"constant": "disable_tlv_poe",
                                "tags": ["COMMAND_CLI"],
                                "link": self.link.disable_tlv_poe}
        self.DISABLE_TLV_PORT_DESC = {"constant": "disable_tlv_port_desc",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.disable_tlv_port_desc}
        self.DISABLE_TLV_PRIORITY_FLOWCTRL = {"constant": "disable_tlv_priority_flowctrl",
                                              "tags": ["COMMAND_CLI"],
                                              "link": self.link.disable_tlv_priority_flowctrl}
        self.DISABLE_TLV_STP = {"constant": "disable_tlv_stp",
                                "tags": ["COMMAND_CLI"],
                                "link": self.link.disable_tlv_stp}
        self.DISABLE_TLV_SYS_CAP = {"constant": "disable_tlv_sys_cap",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.disable_tlv_sys_cap}
        self.DISABLE_TLV_SYS_DESC = {"constant": "disable_tlv_sys_desc",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.disable_tlv_sys_desc}
        self.DISABLE_TLV_SYS_NAME = {"constant": "disable_tlv_sys_name",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.disable_tlv_sys_name}
        self.DISABLE_TLV_VLAN_ID = {"constant": "disable_tlv_vlan_id",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.disable_tlv_vlan_id}
        self.ENABLE = {"constant": "enable",
                       "tags": ["COMMAND_CLI"],
                       "link": self.link.enable}
        self.ENABLE_PORT_BOTH = {"constant": "enable_port_both",
                                 "tags": ["COMMAND_CLI", "COMMAND_REST"],
                                 "link": self.link.enable_port_both}
        self.ENABLE_PORT_RX = {"constant": "enable_port_rx",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.enable_port_rx}
        self.ENABLE_PORT_TX = {"constant": "enable_port_tx",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.enable_port_tx}
        self.ENABLE_RX = {"constant": "enable_rx",
                          "tags": ["COMMAND_CLI"],
                          "link": self.link.enable_rx}
        self.ENABLE_TLV_ALL = {"constant": "enable_tlv_all",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.enable_tlv_all}
        self.ENABLE_TLV_APPLICATION_PRI = {"constant": "enable_tlv_application_pri",
                                           "tags": ["COMMAND_CLI"],
                                           "link": self.link.enable_tlv_application_pri}
        self.ENABLE_TLV_CONGESTION_NOTIF = {"constant": "enable_tlv_congestion_notif",
                                            "tags": ["COMMAND_CLI"],
                                            "link": self.link.enable_tlv_congestion_notif}
        self.ENABLE_TLV_ENERGY_EFF_ETH = {"constant": "enable_tlv_energy_eff_eth",
                                          "tags": ["COMMAND_CLI"],
                                          "link": self.link.enable_tlv_energy_eff_eth}
        self.ENABLE_TLV_ENHANCED_TRANS_CONFIG = {"constant": "enable_tlv_enhanced_trans_config",
                                                 "tags": ["COMMAND_CLI"],
                                                 "link": self.link.enable_tlv_enhanced_trans_config}
        self.ENABLE_TLV_ENHANCED_TRANS_REC = {"constant": "enable_tlv_enhanced_trans_rec",
                                              "tags": ["COMMAND_CLI"],
                                              "link": self.link.enable_tlv_enhanced_trans_rec}
        self.ENABLE_TLV_GVRP = {"constant": "enable_tlv_gvrp",
                                "tags": ["COMMAND_CLI"],
                                "link": self.link.enable_tlv_gvrp}
        self.ENABLE_TLV_LACP = {"constant": "enable_tlv_lacp",
                                "tags": ["COMMAND_CLI"],
                                "link": self.link.enable_tlv_lacp}
        self.ENABLE_TLV_LINK_AGGR = {"constant": "enable_tlv_link_aggr",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.enable_tlv_link_aggr}
        self.ENABLE_TLV_MAC_PHY = {"constant": "enable_tlv_mac_phy",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.enable_tlv_mac_phy}
        self.ENABLE_TLV_MAX_FRAME = {"constant": "enable_tlv_max_frame",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.enable_tlv_max_frame}
        self.ENABLE_TLV_MED_CAP = {"constant": "enable_tlv_med_cap",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.enable_tlv_med_cap}
        self.ENABLE_TLV_MED_LOC = {"constant": "enable_tlv_med_loc",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.enable_tlv_med_loc}
        self.ENABLE_TLV_MED_POE = {"constant": "enable_tlv_med_poe",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.enable_tlv_med_poe}
        self.ENABLE_TLV_MED_POL = {"constant": "enable_tlv_med_pol",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.enable_tlv_med_pol}
        self.ENABLE_TLV_MGMT_ADDR = {"constant": "enable_tlv_mgmt_addr",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.enable_tlv_mgmt_addr}
        self.ENABLE_TLV_POE = {"constant": "enable_tlv_poe",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.enable_tlv_poe}
        self.ENABLE_TLV_PORT_DESC = {"constant": "enable_tlv_port_desc",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.enable_tlv_port_desc}
        self.ENABLE_TLV_PRIORITY_FLOWCTRL = {"constant": "enable_tlv_priority_flowctrl",
                                             "tags": ["COMMAND_CLI"],
                                             "link": self.link.enable_tlv_priority_flowctrl}
        self.ENABLE_TLV_STP = {"constant": "enable_tlv_stp",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.enable_tlv_stp}
        self.ENABLE_TLV_SYS_CAP = {"constant": "enable_tlv_sys_cap",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.enable_tlv_sys_cap}
        self.ENABLE_TLV_SYS_DESC = {"constant": "enable_tlv_sys_desc",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.enable_tlv_sys_desc}
        self.ENABLE_TLV_SYS_NAME = {"constant": "enable_tlv_sys_name",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.enable_tlv_sys_name}
        self.ENABLE_TLV_VLAN_ID = {"constant": "enable_tlv_vlan_id",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.enable_tlv_vlan_id}
        self.ENABLE_TX = {"constant": "enable_tx",
                          "tags": ["COMMAND_CLI"],
                          "link": self.link.enable_tx}
        self.SET_PROFILE = {"constant": "set_profile",
                            "tags": ["COMMAND_CLI"],
                            "link": self.link.set_profile}
        self.SET_PROFILE_INTERFACE = {"constant": "set_profile_interface",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.set_profile_interface}
        self.SET_SYS_NAME = {"constant": "set_sys_name",
                             "tags": ["COMMAND_CLI"],
                             "link": self.link.set_sys_name}
        self.SET_TX_HOLD_MULTIPLIER = {"constant": "set_tx_hold_multiplier",
                                       "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                       "link": self.link.set_tx_hold_multiplier}
        self.SET_TX_INTERVAL = {"constant": "set_tx_interval",
                                "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                "link": self.link.set_tx_interval}
        self.SHOW_INFO = {"constant": "show_info",
                          "tags": ["COMMAND_CLI", "COMMAND_REST", "COMMAND_SNMP"],
                          "link": self.link.show_info}
        self.SHOW_NEIGHBORS = {"constant": "show_neighbors",
                               "tags": ["COMMAND_CLI", "COMMAND_REST"],
                               "link": self.link.show_neighbors}
        self.SHOW_NEIGHBORS_DETAIL = {"constant": "show_neighbors_detail",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.show_neighbors_detail}
        self.SHOW_NEIGHBORS_PORT = {"constant": "show_neighbors_port",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.show_neighbors_port}
        self.SHOW_NEIGHBORS_PORT_DETAIL = {"constant": "show_neighbors_port_detail",
                                           "tags": ["COMMAND_CLI"],
                                           "link": self.link.show_neighbors_port_detail}
        self.SHOW_PORT_STATUS = {"constant": "show_port_status",
                                 "tags": ["COMMAND_CLI", "COMMAND_REST"],
                                 "link": self.link.show_port_status}
        self.SHOW_PORT_TLV_APPLICATION_PRI = {"constant": "show_port_tlv_application_pri",
                                              "tags": ["COMMAND_CLI"],
                                              "link": self.link.show_port_tlv_application_pri}
        self.SHOW_PORT_TLV_CONGESTION_NOTIF = {"constant": "show_port_tlv_congestion_notif",
                                               "tags": ["COMMAND_CLI"],
                                               "link": self.link.show_port_tlv_congestion_notif}
        self.SHOW_PORT_TLV_ENERGY_EFF_ETH = {"constant": "show_port_tlv_energy_eff_eth",
                                             "tags": ["COMMAND_CLI"],
                                             "link": self.link.show_port_tlv_energy_eff_eth}
        self.SHOW_PORT_TLV_ENHANCED_TRANS_CONFIG = {"constant": "show_port_tlv_enhanced_trans_config",
                                                    "tags": ["COMMAND_CLI"],
                                                    "link": self.link.show_port_tlv_enhanced_trans_config}
        self.SHOW_PORT_TLV_ENHANCED_TRANS_REC = {"constant": "show_port_tlv_enhanced_trans_rec",
                                                 "tags": ["COMMAND_CLI"],
                                                 "link": self.link.show_port_tlv_enhanced_trans_rec}
        self.SHOW_PORT_TLV_GVRP = {"constant": "show_port_tlv_gvrp",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.show_port_tlv_gvrp}
        self.SHOW_PORT_TLV_LACP = {"constant": "show_port_tlv_lacp",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.show_port_tlv_lacp}
        self.SHOW_PORT_TLV_LINK_AGGR = {"constant": "show_port_tlv_link_aggr",
                                        "tags": ["COMMAND_CLI"],
                                        "link": self.link.show_port_tlv_link_aggr}
        self.SHOW_PORT_TLV_MAC_PHY = {"constant": "show_port_tlv_mac_phy",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.show_port_tlv_mac_phy}
        self.SHOW_PORT_TLV_MAX_FRAME = {"constant": "show_port_tlv_max_frame",
                                        "tags": ["COMMAND_CLI"],
                                        "link": self.link.show_port_tlv_max_frame}
        self.SHOW_PORT_TLV_MED_CAP = {"constant": "show_port_tlv_med_cap",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.show_port_tlv_med_cap}
        self.SHOW_PORT_TLV_MED_LOC = {"constant": "show_port_tlv_med_loc",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.show_port_tlv_med_loc}
        self.SHOW_PORT_TLV_MED_POE = {"constant": "show_port_tlv_med_poe",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.show_port_tlv_med_poe}
        self.SHOW_PORT_TLV_MED_POL = {"constant": "show_port_tlv_med_pol",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.show_port_tlv_med_pol}
        self.SHOW_PORT_TLV_MGMT_ADDR = {"constant": "show_port_tlv_mgmt_addr",
                                        "tags": ["COMMAND_CLI"],
                                        "link": self.link.show_port_tlv_mgmt_addr}
        self.SHOW_PORT_TLV_POE = {"constant": "show_port_tlv_poe",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.show_port_tlv_poe}
        self.SHOW_PORT_TLV_PORT_DESC = {"constant": "show_port_tlv_port_desc",
                                        "tags": ["COMMAND_CLI"],
                                        "link": self.link.show_port_tlv_port_desc}
        self.SHOW_PORT_TLV_PRIORITY_FLOWCTRL = {"constant": "show_port_tlv_priority_flowctrl",
                                                "tags": ["COMMAND_CLI"],
                                                "link": self.link.show_port_tlv_priority_flowctrl}
        self.SHOW_PORT_TLV_STP = {"constant": "show_port_tlv_stp",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.show_port_tlv_stp}
        self.SHOW_PORT_TLV_SYS_CAP = {"constant": "show_port_tlv_sys_cap",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.show_port_tlv_sys_cap}
        self.SHOW_PORT_TLV_SYS_DESC = {"constant": "show_port_tlv_sys_desc",
                                       "tags": ["COMMAND_CLI"],
                                       "link": self.link.show_port_tlv_sys_desc}
        self.SHOW_PORT_TLV_SYS_NAME = {"constant": "show_port_tlv_sys_name",
                                       "tags": ["COMMAND_CLI"],
                                       "link": self.link.show_port_tlv_sys_name}
        self.SHOW_PORT_TLV_VLAN_ID = {"constant": "show_port_tlv_vlan_id",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.show_port_tlv_vlan_id}
        self.SHOW_REMOTE_INFO = {"constant": "show_remote_info",
                                 "tags": ["COMMAND_CLI", "COMMAND_REST"],
                                 "link": self.link.show_remote_info}
        self.SHOW_STATISTICS = {"constant": "show_statistics",
                                "tags": ["COMMAND_CLI"],
                                "link": self.link.show_statistics}
        self.SHOW_STATISTICS_PORT = {"constant": "show_statistics_port",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.show_statistics_port}
