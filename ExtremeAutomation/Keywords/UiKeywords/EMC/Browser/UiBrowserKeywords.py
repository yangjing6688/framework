from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.EMC.BrowserConstants import BrowserConstants


class UiBrowserKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiBrowserKeywords, self).__init__()
        self.api_const = self.constants.API_BROWSER
        self.command_const = BrowserConstants()

    def open_web_page(self, element_name, url, browser=None, browser_width=None, browser_height=None, **kwargs):
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

    def login(self, element_name, username, password, browser=None, **kwargs):
        """Returns the result of login."""
        args = {"username": username,
                "password": password,
                "browser": browser if browser is not None else "chrome"}

        return self.execute_keyword(element_name, args, self.command_const.LOGIN, **kwargs)

    def close_web_page(self, element_name, **kwargs):
        """
        [element_name] - The UI element(s) the keyword should be run against.

        Closes the browser for a given element.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.CLOSE_WEB_PAGE, **kwargs)
