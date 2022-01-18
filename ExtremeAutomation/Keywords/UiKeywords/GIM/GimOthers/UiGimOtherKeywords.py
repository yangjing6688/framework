from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.GIM.GimothersConstants import GimothersConstants


class UiGimOtherKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiGimOtherKeywords, self).__init__()
        self.api_const = self.constants.API_GIM_OTHERS
        self.command_const = GimothersConstants()
