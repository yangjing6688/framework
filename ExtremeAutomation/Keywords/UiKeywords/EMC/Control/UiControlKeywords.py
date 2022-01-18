from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.EMC.ControlConstants import ControlConstants


class UiControlKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiControlKeywords, self).__init__()
        self.api_const = self.constants.API_CONTROL
        self.cmd = ControlConstants()

    def control_select_sub_tab(self, element_name, tab_name, **kwargs):
        """Returns the result of control_select_sub_tab."""
        args = {"tab_name": tab_name}

        return self.execute_keyword(element_name, args, self.cmd.CONTROL_SELECT_SUB_TAB, **kwargs)
