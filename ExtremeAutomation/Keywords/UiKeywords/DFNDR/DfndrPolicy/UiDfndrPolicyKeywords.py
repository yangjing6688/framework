from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.DFNDR.DfndrpolicyConstants \
    import DfndrpolicyConstants


class UiDfndrPolicyKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiDfndrPolicyKeywords, self).__init__()
        self.api_const = self.constants.API_DFN_POLICY
        self.command_const = DfndrpolicyConstants()
