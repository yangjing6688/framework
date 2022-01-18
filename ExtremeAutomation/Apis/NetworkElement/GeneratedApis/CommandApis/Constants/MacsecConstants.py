"""
This class outlines all the constants for the macsec API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(MacsecConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class MacsecConstants(ApiConstants):
    def __init__(self):
        super(MacsecConstants, self).__init__()
        self.CLEAR_COUNTERS_ALL = {"constant": "clear_counters_all",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.clear_counters_all}
        self.CLEAR_COUNTERS_ON_PORT = {"constant": "clear_counters_on_port",
                                       "tags": ["COMMAND_CLI"],
                                       "link": self.link.clear_counters_on_port}
        self.CREATE_CA = {"constant": "create_ca",
                          "tags": ["COMMAND_CLI"],
                          "link": self.link.create_ca}
        self.CREATE_CA_ENCRYPTED = {"constant": "create_ca_encrypted",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.create_ca_encrypted}
        self.DELETE_CA = {"constant": "delete_ca",
                          "tags": ["COMMAND_CLI"],
                          "link": self.link.delete_ca}
        self.DISABLE_CA_PORT = {"constant": "disable_ca_port",
                                "tags": ["COMMAND_CLI"],
                                "link": self.link.disable_ca_port}
        self.ENABLE_CA_PORT = {"constant": "enable_ca_port",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.enable_ca_port}
        self.SET_CIPHER_SUITE_128 = {"constant": "set_cipher_suite_128",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.set_cipher_suite_128}
        self.SET_CIPHER_SUITE_256 = {"constant": "set_cipher_suite_256",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.set_cipher_suite_256}
        self.SET_CONFIDENTIALITY_OFFSET_0 = {"constant": "set_confidentiality_offset_0",
                                             "tags": ["COMMAND_CLI"],
                                             "link": self.link.set_confidentiality_offset_0}
        self.SET_CONFIDENTIALITY_OFFSET_30 = {"constant": "set_confidentiality_offset_30",
                                              "tags": ["COMMAND_CLI"],
                                              "link": self.link.set_confidentiality_offset_30}
        self.SET_CONFIDENTIALITY_OFFSET_50 = {"constant": "set_confidentiality_offset_50",
                                              "tags": ["COMMAND_CLI"],
                                              "link": self.link.set_confidentiality_offset_50}
        self.SET_HW_MODE_HALF_DUPLEX_MODE = {"constant": "set_hw_mode_half_duplex_mode",
                                             "tags": ["COMMAND_CLI"],
                                             "link": self.link.set_hw_mode_half_duplex_mode}
        self.SET_HW_MODE_MACSEC_MODE = {"constant": "set_hw_mode_macsec_mode",
                                        "tags": ["COMMAND_CLI"],
                                        "link": self.link.set_hw_mode_macsec_mode}
        self.SET_INCLUDE_SCI_DISABLE = {"constant": "set_include_sci_disable",
                                        "tags": ["COMMAND_CLI"],
                                        "link": self.link.set_include_sci_disable}
        self.SET_INCLUDE_SCI_ENABLE = {"constant": "set_include_sci_enable",
                                       "tags": ["COMMAND_CLI"],
                                       "link": self.link.set_include_sci_enable}
        self.SET_INITIALIZE_PORTS = {"constant": "set_initialize_ports",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.set_initialize_ports}
        self.SET_MKA_ACTOR_PRIORITY = {"constant": "set_mka_actor_priority",
                                       "tags": ["COMMAND_CLI"],
                                       "link": self.link.set_mka_actor_priority}
        self.SET_REPLAY_PROTECT = {"constant": "set_replay_protect",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.set_replay_protect}
        self.SET_REPLAY_PROTECT_DISABLE = {"constant": "set_replay_protect_disable",
                                           "tags": ["COMMAND_CLI"],
                                           "link": self.link.set_replay_protect_disable}
        self.SHOW = {"constant": "show",
                     "tags": ["COMMAND_CLI"],
                     "link": self.link.show}
        self.SHOW_CONNECTIVITY_ASSOCIATION = {"constant": "show_connectivity_association",
                                              "tags": ["COMMAND_CLI"],
                                              "link": self.link.show_connectivity_association}
        self.SHOW_CONNECTIVITY_ASSOCIATION_ALL = {"constant": "show_connectivity_association_all",
                                                  "tags": ["COMMAND_CLI"],
                                                  "link": self.link.show_connectivity_association_all}
        self.SHOW_PORT = {"constant": "show_port",
                          "tags": ["COMMAND_CLI"],
                          "link": self.link.show_port}
        self.SHOW_PORT_ALL = {"constant": "show_port_all",
                              "tags": ["COMMAND_CLI"],
                              "link": self.link.show_port_all}
        self.SHOW_PORT_ALL_CONFIG = {"constant": "show_port_all_config",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.show_port_all_config}
        self.SHOW_PORT_ALL_DETAIL = {"constant": "show_port_all_detail",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.show_port_all_detail}
        self.SHOW_PORT_CONFIGURATION = {"constant": "show_port_configuration",
                                        "tags": ["COMMAND_CLI"],
                                        "link": self.link.show_port_configuration}
        self.SHOW_PORT_COUNTERS = {"constant": "show_port_counters",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.show_port_counters}
        self.SHOW_PORT_DETAIL = {"constant": "show_port_detail",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.show_port_detail}
