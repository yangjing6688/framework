from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.DFNDR.DfndractivationConstants \
    import DfndractivationConstants


class UiDfndrActivationKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiDfndrActivationKeywords, self).__init__()
        self.api_const = self.constants.API_DFN_ACTIVATION
        self.command_const = DfndractivationConstants()
