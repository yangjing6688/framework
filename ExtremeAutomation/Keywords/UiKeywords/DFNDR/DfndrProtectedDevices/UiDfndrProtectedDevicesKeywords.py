from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.DFNDR.DfndrprotecteddevicesConstants \
    import DfndrprotecteddevicesConstants


class UiDfndrProtectedDevicesKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiDfndrProtectedDevicesKeywords, self).__init__()
        self.api_const = self.constants.API_DFN_PROTECTED_DEVICES
        self.command_const = DfndrprotecteddevicesConstants()
