from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.DFNDR.DfndroverviewConstants \
    import DfndroverviewConstants


class UiDfndrOverviewKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiDfndrOverviewKeywords, self).__init__()
        self.api_const = self.constants.API_DFN_OVERVIEW
        self.command_const = DfndroverviewConstants()
