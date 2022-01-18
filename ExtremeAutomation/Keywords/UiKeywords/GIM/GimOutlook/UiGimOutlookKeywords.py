from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.GIM.GimoutlookConstants import GimoutlookConstants


class UiGimOutlookKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiGimOutlookKeywords, self).__init__()
        self.api_const = self.constants.API_GIM_OUTLOOK
        self.command_const = GimoutlookConstants()
