"""
This class outlines all the constants for the dvr API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(DvrConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class DvrConstants(ApiConstants):
    def __init__(self):
        super(DvrConstants, self).__init__()
        self.VERIFY_DVR_DOMAIN_CONTROLLER_EXISTS = {"constant": "verify_dvr_domain_controller_exists",
                                                    "tags": ["PARSE_CLI"],
                                                    "link": self.link.verify_dvr_domain_controller_exists}
        self.VERIFY_DVR_DOMAIN_CONTROLLER_INJECT_DEFAULT_ROUTE_ALL_IS_DISABLED = {"constant": "verify_dvr_domain_controller_inject_default_route_all_is_disabled",
                                                                                  "tags": ["PARSE_CLI"],
                                                                                  "link": self.link.verify_dvr_domain_controller_inject_default_route_all_is_disabled}
        self.VERIFY_DVR_DOMAIN_CONTROLLER_INJECT_DEFAULT_ROUTE_IS_DISABLED = {"constant": "verify_dvr_domain_controller_inject_default_route_is_disabled",
                                                                              "tags": ["PARSE_CLI"],
                                                                              "link": self.link.verify_dvr_domain_controller_inject_default_route_is_disabled}
        self.VERIFY_DVR_LEAF_ID_IS_SET = {"constant": "verify_dvr_leaf_id_is_set",
                                          "tags": ["PARSE_CLI"],
                                          "link": self.link.verify_dvr_leaf_id_is_set}
        self.VERIFY_DVR_LEAF_VIRTUAL_IST_LOCAL_AND_PEER_IP_IS_SET = {"constant": "verify_dvr_leaf_virtual_ist_local_and_peer_ip_is_set",
                                                                     "tags": ["PARSE_CLI"],
                                                                     "link": self.link.verify_dvr_leaf_virtual_ist_local_and_peer_ip_is_set}
        self.VERIFY_DVR_ON_INTERFACE_IS_ENABLED = {"constant": "verify_dvr_on_interface_is_enabled",
                                                   "tags": ["PARSE_CLI"],
                                                   "link": self.link.verify_dvr_on_interface_is_enabled}
        self.VERIFY_DVR_REDISTRIBUTE_DIRECT_IS_DISABLED = {"constant": "verify_dvr_redistribute_direct_is_disabled",
                                                           "tags": ["PARSE_CLI"],
                                                           "link": self.link.verify_dvr_redistribute_direct_is_disabled}
        self.VERIFY_DVR_REDISTRIBUTE_DIRECT_IS_ENABLED = {"constant": "verify_dvr_redistribute_direct_is_enabled",
                                                          "tags": ["PARSE_CLI"],
                                                          "link": self.link.verify_dvr_redistribute_direct_is_enabled}
        self.VERIFY_DVR_REDISTRIBUTE_DIRECT_METRIC_IS_SET = {"constant": "verify_dvr_redistribute_direct_metric_is_set",
                                                             "tags": ["PARSE_CLI"],
                                                             "link": self.link.verify_dvr_redistribute_direct_metric_is_set}
        self.VERIFY_DVR_REDISTRIBUTE_STATIC_IS_DISABLED = {"constant": "verify_dvr_redistribute_static_is_disabled",
                                                           "tags": ["PARSE_CLI"],
                                                           "link": self.link.verify_dvr_redistribute_static_is_disabled}
        self.VERIFY_DVR_REDISTRIBUTE_STATIC_IS_ENABLED = {"constant": "verify_dvr_redistribute_static_is_enabled",
                                                          "tags": ["PARSE_CLI"],
                                                          "link": self.link.verify_dvr_redistribute_static_is_enabled}
        self.VERIFY_DVR_REDISTRIBUTE_STATIC_METRIC_IS_SET = {"constant": "verify_dvr_redistribute_static_metric_is_set",
                                                             "tags": ["PARSE_CLI"],
                                                             "link": self.link.verify_dvr_redistribute_static_metric_is_set}
        self.VERIFY_INTERFACE_VLAN_DVR_GATEWAY_IPV4_IS_SET = {"constant": "verify_interface_vlan_dvr_gateway_ipv4_is_set",
                                                              "tags": ["PARSE_CLI"],
                                                              "link": self.link.verify_interface_vlan_dvr_gateway_ipv4_is_set}
