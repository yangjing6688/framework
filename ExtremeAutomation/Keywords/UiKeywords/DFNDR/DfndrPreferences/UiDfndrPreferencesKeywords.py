from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.DFNDR.DfndrpreferencesConstants \
    import DfndrpreferencesConstants


class UiDfndrPreferencesKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiDfndrPreferencesKeywords, self).__init__()
        self.api_const = self.constants.API_DFN_PREFERENCES
        self.command_const = DfndrpreferencesConstants()
