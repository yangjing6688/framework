"""
This class outlines all the constants for the analytics API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(AnalyticsConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class AnalyticsConstants(ApiConstants):
    def __init__(self):
        super(AnalyticsConstants, self).__init__()
        self.COLLAPSE_ALL_CONFIG_TREE_NODES = {"constant": "collapse_all_config_tree_nodes",
                                               "tags": ["COMMAND_SELENIUM"],
                                               "link": self.link.collapse_all_config_tree_nodes}
        self.SELECT_APPTELEMETRY_SOURCE = {"constant": "select_apptelemetry_source",
                                           "tags": ["COMMAND_SELENIUM"],
                                           "link": self.link.select_apptelemetry_source}
        self.VERIFY_FLOW_SOURCES_ADDED = {"constant": "verify_flow_sources_added",
                                          "tags": ["COMMAND_SELENIUM"],
                                          "link": self.link.verify_flow_sources_added}
