from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.DFNDR.DfndrlicensingConstants \
    import DfndrlicensingConstants


class UiDfndrLicensingKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiDfndrLicensingKeywords, self).__init__()
        self.api_const = self.constants.API_DFN_LICENSING
        self.command_const = DfndrlicensingConstants()
