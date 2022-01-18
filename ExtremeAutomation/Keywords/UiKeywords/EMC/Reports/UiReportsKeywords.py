from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.EMC.ReportsConstants import ReportsConstants


class UiReportsKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiReportsKeywords, self).__init__()
        self.api_const = self.constants.API_REPORTS
        self.command_const = ReportsConstants()

    def reports_select_sub_tab(self, element_name, tab_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [tab_name] -      Name of the sub tab to select

        Selects the specified sub tab of the main Reports tab.
        """
        args = {"tab_name": tab_name}

        return self.execute_keyword(element_name, args, self.command_const.REPORTS_SELECT_SUB_TAB, **kwargs)
