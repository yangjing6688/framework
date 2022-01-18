from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.EWC.EwcglobalConstants import EwcglobalConstants


class UiEwcGlobalKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiEwcGlobalKeywords, self).__init__()
        self.api_const = self.constants.API_EWC_GLOBAL
        self.command_const = EwcglobalConstants()

    def global_authentication_check_strict_mode(self, element_name, **kwargs):
        """Returns the result of global_authentication_check_strict_mode."""
        args = {}

        return self.execute_keyword(element_name, args,
                                    self.command_const.GLOBAL_AUTHENTICATION_CHECK_STRICT_MODE, **kwargs)

    def global_authentication_uncheck_strict_mode(self, element_name, **kwargs):
        """Returns the result of global_authentication_uncheck_strict_mode."""
        args = {}

        return self.execute_keyword(element_name, args,
                                    self.command_const.GLOBAL_AUTHENTICATION_UNCHECK_STRICT_MODE, **kwargs)

    def global_click_save_button(self, element_name, **kwargs):
        """Returns the result of global_click_save_button."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.GLOBAL_CLICK_SAVE_BUTTON, **kwargs)
