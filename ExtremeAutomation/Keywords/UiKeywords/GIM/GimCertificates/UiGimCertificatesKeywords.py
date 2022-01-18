from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.GIM.GimcertificatesConstants import \
    GimcertificatesConstants


class UiGimCertificatesKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiGimCertificatesKeywords, self).__init__()
        self.api_const = self.constants.API_GIM_CERTIFICATES
        self.command_const = GimcertificatesConstants()
