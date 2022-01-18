from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.EMC.AdministrationConstants import AdministrationConstants


class UiAdministrationKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiAdministrationKeywords, self).__init__()
        self.cmd = AdministrationConstants()
        self.api_const = self.constants.API_ADMINISTRATION

    def administration_select_sub_tab(self, element_name, tab_name, **kwargs):
        """Returns the result of administration_select_sub_tab."""
        args = {"tab_name": tab_name}

        return self.execute_keyword(element_name, args, self.cmd.ADMINISTRATION_SELECT_SUB_TAB, **kwargs)
