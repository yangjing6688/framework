from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.GIM.GimlocaleConstants import GimlocaleConstants


class UiGimLocaleKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiGimLocaleKeywords, self).__init__()
        self.api_const = self.constants.API_GIM_LOCALE
        self.command_const = GimlocaleConstants()
