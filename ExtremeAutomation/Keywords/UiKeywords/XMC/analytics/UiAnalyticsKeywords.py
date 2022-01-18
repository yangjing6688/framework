from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.XMC.AnalyticsConstants import AnalyticsConstants


class UiAnalyticsKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiAnalyticsKeywords, self).__init__()
        self.api_const = self.constants.API_XMC_ANALYTICS
        self.command_const = AnalyticsConstants()

    def select_apptelemetry_source(self, element_name, tree_node, **kwargs):
        """
        Keyword Arguments:
        [element_names]         - List of elements the keyword will be run against
        [tree_node]             - Tree node item with absolute navigation path delimited by pipeline (|)

        Select the source button
        """
        args = {"tree_node": tree_node}

        return self.execute_keyword(element_name, args, self.command_const.SELECT_APPTELEMETRY_SOURCE, **kwargs)

    def collapse_all_config_tree_nodes(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names]         - List of elements the keyword will be run against

        Collapse All analytics Config Tree nodes
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.COLLAPSE_ALL_CONFIG_TREE_NODES, **kwargs)

    def verify_flow_sources_added(self, element_name, device_ip, **kwargs):
        """
        Keyword Arguments:
        [element_names]         - List of elements the keyword will be run against
        [device_ip]             - IP of a device added for verification

        Verify flow source(s) is addedd successfully
        """
        args = {"device_ip": device_ip}

        return self.execute_keyword(element_name, args, self.command_const.VERIFY_FLOW_SOURCES_ADDED, **kwargs)
