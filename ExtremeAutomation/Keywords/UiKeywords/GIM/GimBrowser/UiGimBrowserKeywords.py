from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.GIM.GimbrowserConstants import GimbrowserConstants


class UiGimBrowserKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiGimBrowserKeywords, self).__init__()
        self.api_const = self.constants.API_GIM_BROWSER
        self.command_const = GimbrowserConstants()

    def gim_browser_open_web_page(self, element_name, url, browser=None, browser_width=None, browser_height=None,
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

        return self.execute_keyword(element_name, args, self.command_const.BROWSER_OPEN_WEB_PAGE, **kwargs)

    def gim_browser_login(self, element_name, username, password, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [username]  - Username from GIM Admin/Provisioner
        [password] - Password from GIM Admin/Provisioner

        Login with GIM Admin/Provisioner username and password credentials
        """
        args = {"username": username,
                "password": password
                }

        return self.execute_keyword(element_name, args, self.command_const.BROWSER_LOGIN, **kwargs)

    def gim_browser_logout(self, element_name, **kwargs):
        """
        [element_name] - The UI element(s) the keyword should be run against.

        Logout from application for a given element.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.BROWSER_LOGOUT, **kwargs)

    def gim_browser_close_web_page(self, element_name, **kwargs):
        """
        [element_name] - The UI element(s) the keyword should be run against.

        Closes the browser for a given element.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.BROWSER_CLOSE_WEB_PAGE, **kwargs)

    def gim_browser_only_url(self, element_name, url, browser=None, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [url] - The URL the browser should open.

        Opens a given URL without reopening the same browser
        """
        args = {"url": url,
                "browser": browser if browser is not None else "chrome"
                }

        return self.execute_keyword(element_name, args, self.command_const.BROWSER_ONLY_URL, **kwargs)
