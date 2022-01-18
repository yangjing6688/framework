from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.EMC.ViewConstants import ViewConstants


class UiViewKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiViewKeywords, self).__init__()
        self.api_const = self.constants.API_VIEW
        self.command_const = ViewConstants()

    def view_select_tab(self, element_name, tab_name, **kwargs):
        """Returns the result of view_select_tab."""
        args = {"tab_name": tab_name}

        return self.execute_keyword(element_name, args, self.command_const.VIEW_SELECT_TAB, **kwargs)

    def view_menu_about(self, element_name, **kwargs):
        """Returns the result of view_menu_about."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.VIEW_MENU_ABOUT, **kwargs)

    def view_menu_logout(self, element_name, **kwargs):
        """Returns the result of view_menu_logout."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.VIEW_MENU_LOGOUT, **kwargs)

    def view_confirm_logged_in(self, element_name, logged_in, **kwargs):
        """Returns the result of view_confirm_logged_in."""
        args = {"logged_in": logged_in}

        return self.execute_keyword(element_name, args, self.command_const.VIEW_CONFIRM_LOGGED_IN, **kwargs)
