from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.EMC.HelpConstants import HelpConstants


class UiHelpKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiHelpKeywords, self).__init__()
        self.api_const = self.constants.API_HELP
        self.command_const = HelpConstants()

    def help_show_context_help(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Displays the context help panel.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.HELP_SHOW_CONTEXT_HELP, **kwargs)

    def help_hide_context_help(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Closes the context help panel.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.HELP_HIDE_CONTEXT_HELP, **kwargs)

    def help_show_getting_started(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Displays the Getting Started panel within the context help panel.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.HELP_SHOW_GETTING_STARTED, **kwargs)

    def help_hide_getting_started(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Hides the Getting Started panel within the context help panel.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.HELP_HIDE_GETTING_STARTED, **kwargs)

    def help_click_pause(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the Pause button in the context help panel.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.HELP_CLICK_PAUSE, **kwargs)

    def help_click_resume(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the Resume button in the context help panel.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.HELP_CLICK_RESUME, **kwargs)

    def help_click_launch_new_tab(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the Launch New Tab button in the context help panel.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.HELP_CLICK_LAUNCH_NEW_TAB, **kwargs)

    def help_confirm_context_help_is_visible(self, element_name, is_visible, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [is_visible] -    Indicates if the context help is expected to be visible or not (True/False)

        Confirms whether or not the context help panel is being displayed.
        Passes/fails based on the expected value.
        """
        args = {"is_visible": is_visible}

        return self.execute_keyword(element_name, args, self.command_const.HELP_CONFIRM_CONTEXT_HELP_IS_VISIBLE,
                                    **kwargs)

    def help_confirm_getting_started_is_visible(self, element_name, is_visible, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [is_visible] -    Indicates if the Getting Started panel in the context help is expected to be visible or not
                          (True/False)

        Confirms whether or not the Getting Started panel is being displayed in the context help panel.
        Passes/fails based on the expected value.
        """
        args = {"is_visible": is_visible}

        return self.execute_keyword(element_name, args, self.command_const.HELP_CONFIRM_GETTING_STARTED_IS_VISIBLE,
                                    **kwargs)

    def help_confirm_getting_started_exists(self, element_name, exists, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [exists] -        Indicates if the Getting Started panel in the context help is expected to exist or not
                          (True/False)

        Confirms whether or not the Getting Started panel exists.
        Passes/fails based on the expected value.
        """
        args = {"exists": exists}

        return self.execute_keyword(element_name, args, self.command_const.HELP_CONFIRM_GETTING_STARTED_EXISTS,
                                    **kwargs)
