from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.EWC.EwcviewConstants import EwcviewConstants


class UiEwcViewKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiEwcViewKeywords, self).__init__()
        self.api_const = self.constants.API_EWC_VIEW
        self.command_const = EwcviewConstants()

    def ewc_view_select_tab(self, element_name, tab_name, **kwargs):
        """Returns the result of ewc_view_select_tab."""
        args = {"tab_name": tab_name}

        return self.execute_keyword(element_name, args, self.command_const.VIEW_SELECT_TAB, **kwargs)
