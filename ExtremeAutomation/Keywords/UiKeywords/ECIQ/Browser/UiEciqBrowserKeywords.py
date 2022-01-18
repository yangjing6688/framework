from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.ECIQ.EciqbrowserConstants import EciqbrowserConstants


class UiEciqBrowserKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiEciqBrowserKeywords, self).__init__()
        self.api_const = self.constants.API_ECIQ_BROWSER
        self.command_const = EciqbrowserConstants()

    def eciq_browser_open_web_page(self, element_name, url, browser=None, browser_width=None, browser_height=None,
                                   **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [url] - The URL the browser should open.

        Opens a given URL within the browser.
        """
        args = {"url": url,
                "browser": browser if browser is not None else "chrome",
                "browser_width": browser_width,
                "browser_height": browser_height}

        return self.execute_keyword(element_name, args, self.command_const.OPEN_WEB_PAGE, **kwargs)

    def eciq_browser_login(self, element_name, username, password, browser=None, **kwargs):
        """Returns the result of login."""
        args = {"username": username,
                "password": password,
                "browser": browser if browser is not None else "chrome"}

        return self.execute_keyword(element_name, args, self.command_const.LOGIN, **kwargs)

    def eciq_browser_close_web_page(self, element_name, **kwargs):
        """
        [element_name] - The UI element(s) the keyword should be run against.

        Closes the browser for a given element.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.CLOSE_WEB_PAGE, **kwargs)

    def eciq_browser_click_do_not_show_again_checkbox(self, element_name, **kwargs):
        """Returns the result of click_do_not_show_again_checkbox."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.CLICK_DO_NOT_SHOW_AGAIN_CHECKBOX, **kwargs)

    def eciq_browser_click_close_button(self, element_name, **kwargs):
        """Returns the result of click_close_button."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.CLICK_CLOSE_BUTTON, **kwargs)

    def eciq_browser_bypass_certificate_popup(self, element_name, **kwargs):
        """Returns the result of bypass_certificate_popup."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.BYPASS_CERTIFICATE_POPUP, **kwargs)
