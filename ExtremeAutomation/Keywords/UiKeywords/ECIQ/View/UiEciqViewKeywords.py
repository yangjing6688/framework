from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.ECIQ.EciqviewConstants import EciqviewConstants


class UiEciqViewKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiEciqViewKeywords, self).__init__()
        self.api_const = self.constants.API_ECIQ_VIEW
        self.command_const = EciqviewConstants()

    def eciq_view_select_tab(self, element_name, tab_name, **kwargs):
        """
        Returns the result of view_select_tab.
        [element_name] - The UI element(s) the keyword should be run against.
        [tab_name] - The tab to be selected.
        """
        args = {"tab_name": tab_name}

        return self.execute_keyword(element_name, args, self.command_const.VIEW_SELECT_TAB, **kwargs)

    def eciq_view_select_sub_tab(self, element_name, tab_name, subtab_name, **kwargs):
        """
        Returns the result of view_select_sub_tab.
        [element_name] - The UI element(s) the keyword should be run against.
        [tab_name] - The tab containing the subtab.
        [subtab_name] - The subtab to be selected.
        """
        args = {"tab_name": tab_name,
                "subtab_name": subtab_name}

        return self.execute_keyword(element_name, args, self.command_const.VIEW_SELECT_SUB_TAB, **kwargs)
