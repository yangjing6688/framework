from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.DFNDR.DfndrbrowserConstants \
    import DfndrbrowserConstants


class UiDfndrBrowserKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiDfndrBrowserKeywords, self).__init__()
        self.api_const = self.constants.API_DFN_BROWSER
        self.command_const = DfndrbrowserConstants()

    def dfndr_browser_open_web_page(self, element_name, url, browser=None, browser_width=None,
                                    browser_height=None, **kwargs):
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

        return self.execute_keyword(element_name, args, self.command_const.DFNDR_BROWSER_OPEN_WEB_PAGE,
                                    **kwargs)

    def dfndr_browser_login(self, element_name, username, password, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [username]  - Username from Defender admin
        [password] - Password from Defender password

        Login with Defender Admin username and password credentials
        """
        args = {"username": username,
                "password": password
                }

        return self.execute_keyword(element_name, args, self.command_const.DFNDR_BROWSER_LOGIN, **kwargs)

    def dfndr_browser_logout(self, element_name, app_name, **kwargs):
        """
        [element_name] - The UI element(s) the keyword should be run against.
        [app_name] - Name of the application to logout

        Logout from application for a given element.
        """
        args = {
            "app_name": app_name
        }

        return self.execute_keyword(element_name, args, self.command_const.DFNDR_BROWSER_LOGOUT, **kwargs)

    def dfndr_browser_close_web_page(self, element_name, **kwargs):
        """
        [element_name] - The UI element(s) the keyword should be run against.

        Closes the browser for a given element.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.DFNDR_BROWSER_CLOSE_WEB_PAGE, **kwargs)

    def dfndr_browser_only_url(self, element_name, url, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [url] - The URL the browser should open.

        Opens a given URL without reopening the same browser
        """
        args = {"url": url
                }

        return self.execute_keyword(element_name, args, self.command_const.DFNDR_BROWSER_ONLY_URL, **kwargs)
