from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.EMC.NetworkConstants import NetworkConstants


class UiNetworkKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiNetworkKeywords, self).__init__()
        self.api_const = self.constants.API_NETWORK
        self.cmd = NetworkConstants()

    def network_select_sub_tab(self, element_name, tab_name, **kwargs):
        """Returns the result of network_select_sub_tab."""
        args = {"tab_name": tab_name}

        return self.execute_keyword(element_name, args, self.cmd.NETWORK_SELECT_SUB_TAB, **kwargs)
