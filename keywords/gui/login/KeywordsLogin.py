# Standard Keyword imports
from extauto.common.CommonValidation import CommonValidation
from extauto.common.KeywordUtils import KeywordUtils
import inspect
from tools.xapi.XapiHelper import XapiHelper
from ExtremeAutomation.Library.Utils.Singleton import Singleton

# Keyword imports required to run keywords implemented in this file
from extauto.xiq.xapi.common.XapiLogin import XapiLogin
from extauto.xiq.flows.common.Login import Login

class KeywordsLogin(object, metaclass=Singleton):
    def __init__(self):
        # This is a singleton, avoid initializing for each instance
        if hasattr(self, 'initialized'):
            return
        self.initialized = True

        # Objects used by all keywords
        self.common_validation = CommonValidation()
        self.keyword_utils = KeywordUtils()
        self.xapi_helper = XapiHelper()

        # Object used to run keywords implemented in this file
        self.login = Login()
        self.xapi_login = XapiLogin()

    def login_user(self, username, password, capture_version=False, login_option="30-day-trial", url="default",
                   incognito_mode="False", co_pilot_status=False, entitlement_key=False, salesforce_username=False,
                   salesforce_password=False, salesforce_shared_cuid=False, quick=False, check_warning_msg=False,
                   max_retries=3, recover_login=True, map_override=None, ignore_map=False, **kwargs):
        """
         Login to Xiq account with username and password (we will try up to 3 times)

         Note: By default the url will load from the topology file

        - Keyword Usage:
        -   Robot:
        -      Library  keywords/gui/login/KeywordsLogin.py
        -      Login User  ${USERNAME}   ${PASSWORD}    capture_version=True
        -
        -   Pytest:
        -      Imports:
        -         from keywords.gui.login.KeywordsLogin import KeywordsLogin
        -      Calling Keyword:
        -         keywords_login = KeywordsLogin()
        -         keywords_login.login_user(username, password, capture_version=True)
        -
        - Keyword Implementations:
        -    GUI
        -    XAPI

        Supported Modes:
            GUI  - default mode
            XAPI - kwargs XAPI_ONLY=True (Will only support XAPI keywords in your test)

        :param username: login account username
        :param password: login account password
        :param capture_version: true if want capture the xiq build version (will be printed to the logs)
        :param login_option: login option to get started with any of options:
                    30-day-trial,
                    License,
                    Legacy Entitlement,
                    Pilot License
                    Connect
        :param url: url to load.  Normally default is used to get the URL from the topology file
        :param incognito_mode: Enable/Disable incognito_mode
        :param co_pilot_status: Enable Co-Pilot Status in XIQ Login Page
        :param entitlement_key: Used only for the "Legacy Entitlement Key" login_option
        :param salesforce_username: Used only for the "ExtremeCloud IQ License" login_option
        :param salesforce_password: Used only for the "ExtremeCloud IQ License" login_option
        :param salesforce_shared_cuid: Used only for the "ExtremeCloud IQ License" login_option
        :param quick: Reduces the amount of "sleep" time during the login keyword (should be removed)
        :param check_warning_msg: Flag to Enable to Warning Messages validation during XIQ Login
        :param max_retries:  The number of times to retry logging in if the login fails and a failure is not expected
        :param recover_login: Allows an attempt to reload map and/or move to devices page if login not completed
        :param map_override: Used only for the "30-day-trial" option.  Allows caller to specify a map file.  If not
               specified the default map file will be used.
        :param ignore_map: If set to true the login process won't check for or upload a map in case of VIQ reset
        :param (**kwarg) expect_error: the keyword is expected to fail

        :return: 1 if login successful else -1
        """

        # Notes:
        #   - The work for this keyword is in a separate file
        #   - The amount of time this keyword takes will be recorded and optionally recorded in a database
        #   - This method will catch any errors that are raised and not handled in the keyword
        keyword_name = inspect.stack()[0][3]
        self.keyword_utils.implementations.set_keyword_uuid("1ae31911-3754-43fe-aaf3-ceb4a39d997e", keyword_name)
        self.keyword_utils.implementations.gui_implemented(keyword_name)
        self.keyword_utils.implementations.xapi_implemented(keyword_name)

        # The value returned will be based on which implementations we run.  We'll return -1 if we fail to login
        # to any implementations.  We'll return 1 if there is no error raised in any of the implementations.
        gui_return_code = 0
        xapi_return_code = 0

        # Log into the GUI unless explicitly requested not to
        xapi_only = kwargs.get('XAPI_ONLY', False)
        if not xapi_only:
            try:
                self.keyword_utils.timing.start(keyword_name, 'GUI')
                gui_return_code = self.login.gui_login_user(
                    username, password, capture_version, login_option, url,
                    incognito_mode, co_pilot_status, entitlement_key, salesforce_username,
                    salesforce_password, salesforce_shared_cuid, quick, check_warning_msg,
                    max_retries, recover_login, map_override, ignore_map, **kwargs
                )

                # We need to record the fact that we've logged into a GUI which enables all GUI based keywords
                if gui_return_code == 1:
                    self.keyword_utils.implementations.set_gui_active(True)

            except Exception as e:
                kwargs['fail_msg'] = f"Error raised for keyword [{keyword_name}] Error: {e}"
                self.common_validation.fault(**kwargs)
            finally:
                self.keyword_utils.timing.end(keyword_name)

        # Log into XAPI only if XAPI is enabled globally
        if self.xapi_helper.is_xapi_enabled():
            try:
                self.keyword_utils.timing.start(keyword_name, 'XAPI')
                xapi_return_code = self.xapi_login.login(username, password, **kwargs)

                # We need to record the fact that we've logged into XAPI which enables all XAPI based keywords
                if xapi_return_code == 1:
                    self.keyword_utils.implementations.set_xapi_active(True)

            except Exception as e:
                kwargs['fail_msg'] = f"Error raised for keyword [{keyword_name}] Error: {e}"
                self.common_validation.fault(**kwargs)
            finally:
                self.keyword_utils.timing.end(keyword_name)

        # Set the status of keywords implementations that are permitted to be run during this test run
        if self.keyword_utils.implementations.gui_active and self.keyword_utils.implementations.xapi_active == False:
            self.keyword_utils.implementations.gui_only = True
        elif self.keyword_utils.implementations.xapi_active and self.keyword_utils.implementations.gui_active == False:
            self.keyword_utils.implementations.xapi_only = True

        # Return an error if any of the logins failed
        return -1 if (gui_return_code == -1 or xapi_return_code == -1) else 1

    def logout_user(self, **kwargs):
        """
        Logs out of XAPI, GUI or both

        This method will log the user out of the active window and/or XAPI depending on whether or not the user has
        logged into XAPI and the GUI.

        - Keyword Usage:
        -   Robot:
        -      Library  keywords/gui/login/KeywordsLogin.py
        -      Logout User
        -   Pytest:
        -      Imports:
        -         from keywords.gui.login.KeywordsLogin import KeywordsLogin
        -      Calling Keyword:
        -         keywords_login = KeywordsLogin()
        -         keywords_login.logout_user()
        -
        - Keyword Implementations:
        -    GUI
        -    XAPI

        :return: 1 if logout successful, -1 if logout not successful
        """
        # Notes:
        #   - The work for this keyword is in a separate file
        #   - The amount of time this keyword takes will be recorded and optionally recorded in a database
        #   - This method will catch any errors that are raised and not handled in the keyword
        keyword_name = inspect.stack()[0][3]
        self.keyword_utils.implementations.set_keyword_uuid("c0aeadee-c6e1-4bb3-bf44-11e18f9af65f", keyword_name)
        self.keyword_utils.implementations.gui_implemented(keyword_name)
        self.keyword_utils.implementations.xapi_implemented(keyword_name)

        # Return -1 if we cannot log out of any of the accounts we expect to be able to logout of
        gui_return_code = 0
        xapi_return_code = 0

        # Log out of the GUI if GUI is active (was logged into during the test)
        if self.keyword_utils.implementations.gui_active:
            try:
                self.keyword_utils.timing.start(keyword_name, 'GUI')
                gui_return_code = self.login.gui_logout_user()

                # Update the count of GUI logins
                if gui_return_code and self.keyword_utils.implementations.gui_login_count:
                    self.keyword_utils.implementations.gui_login_count -= 1

            except Exception as e:
                kwargs['fail_msg'] = f"Error raised for keyword [{keyword_name}] Error: {e}"
                self.common_validation.fault(**kwargs)
            finally:
                self.keyword_utils.timing.end(keyword_name)

        # Log out of the XAPI if XAPI is active (was logged into during the test) and only if the GUI is no longer
        # active.  This avoids logging out of XAPI when logging out of additional windows while still be logged into
        # other windows.
        if self.keyword_utils.implementations.xapi_active and self.keyword_utils.implementations.gui_login_count == 0:
            try:
                self.keyword_utils.timing.start(keyword_name, 'XAPI')
                xapi_return_code = self.xapi_login.logout(**kwargs)
            except Exception as e:
                kwargs['fail_msg'] = f"Error raised for keyword [{keyword_name}] Error: {e}"
                self.common_validation.fault(**kwargs)
            finally:
                self.keyword_utils.timing.end(keyword_name)

        # Return an error if any of the logouts failed
        return -1 if (gui_return_code == -1 or xapi_return_code == -1) else 1

    def quit_browser(self, _driver=None, **kwargs):
        """
        Close browser window(s)

        Closes all the browser windows and ends the WebDriver session gracefully.  If the _driver object is passed in,
        then quit only the specified browser and return

        - Keyword Usage:
        -   Robot:
        -      Library  keywords/gui/login/KeywordsLogin.py
        -      Quit Browser
        -   Pytest:
        -      Imports:
        -         from keywords.gui.login.KeywordsLogin import KeywordsLogin
        -      Calling Keyword:
        -         keywords_login = KeywordsLogin()
        -         keywords_login.get_window_index()
        -
        - Keyword Implementations:
        -    GUI
        -    XAPI - ** Not Supported **

        :param _driver: Use this to close a specific browser window instead of all browser windows
        :return: 1 if success
        """
        # Notes:
        #   - The work for this keyword is in a separate file
        #   - The amount of time this keyword takes will be recorded and optionally recorded in a database
        #   - This method will catch any errors that are raised and not handled in the keyword
        keyword_name = inspect.stack()[0][3]
        self.keyword_utils.implementations.set_keyword_uuid("e4f48f25-089b-4499-b57d-8af504f249c7", keyword_name)
        self.keyword_utils.implementations.gui_implemented(keyword_name, prefer_gui=True)
        self.keyword_utils.implementations.xapi_implemented(keyword_name)

        # Assume a failure
        return_code = -1

        # Call the helper function that implements this keyword
        try:
            implementation_to_run = self.keyword_utils.implementations.select_keyword_implementation(keyword_name, **kwargs)
            if implementation_to_run != '':
                self.keyword_utils.timing.start(keyword_name, implementation_to_run)
                if implementation_to_run == "GUI":
                    return_code = self.login.gui_quit_browser()
                else:
                    return_code = self.keyword_utils.implementations.not_supported(**kwargs)
                    # not_supported() returns True if keyword should pass else returns False
                    if return_code:
                        return_code = 0
                    else:
                        return_code = -1
        except Exception as e:
            kwargs['fail_msg'] = f"Error raised for keyword [{keyword_name}] Error: {e}"
            self.common_validation.fault(**kwargs)
        finally:
            self.keyword_utils.timing.end(keyword_name)

        # Return the return value of the keyword
        return return_code

    def get_window_index(self, **kwargs):
        """
        Get the index of the frameworks window handle

        When a new window is opened using CloudDriver().open_window() it will return an index indicating the index
        number of the most recently opened window.  This method returns that value.  It is intended to be called
        immediately after opening a new window and allows test writers to switch between multiple windows loading
        different webpages during the test run.

        Note: This value will change any time a new window is open.  If the value is not recorded after opening the
        window you can get the list of child window indexes via the 'get_child_window_list' method in CloudDriver.py

        - Keyword Usage:
        -   Robot:
        -      Library  keywords/gui/login/KeywordsLogin.py
        -      Get Window Index
        -   Pytest:
        -      Imports:
        -         from keywords.gui.login.KeywordsLogin import KeywordsLogin
        -      Calling Keyword:
        -         keywords_login = KeywordsLogin()
        -         keywords_login.get_window_index()
        -
        - Keyword Implementations:
        -    GUI
        -    XAPI - ** Not Supported **

        :return: Current index of the window handle.  -1 If a window has not been opened
        """

        # Notes:
        #   - The work for this keyword is in a separate file
        #   - The amount of time this keyword takes will be recorded and optionally recorded in a database
        #   - This method will catch any errors that are raised and not handled in the keyword
        keyword_name = inspect.stack()[0][3]
        self.keyword_utils.implementations.set_keyword_uuid("a7c40275-30c2-41ef-a0e4-72518e21df0e", keyword_name)
        self.keyword_utils.implementations.gui_implemented(keyword_name, prefer_gui=True)
        self.keyword_utils.implementations.xapi_implemented(keyword_name)

        # Assume a window hasn't been opened
        return_code = -1

        # Call the helper function that implements this keyword
        try:
            implementation_to_run = self.keyword_utils.implementations.select_keyword_implementation(keyword_name, **kwargs)
            if implementation_to_run != '':
                self.keyword_utils.timing.start(keyword_name, 'GUI')
                if implementation_to_run == "GUI":
                    return_code = self.login.gui_get_window_index()
                else:
                    return_code = self.keyword_utils.implementations.not_supported(**kwargs)

                    # not_supported() returns True if keyword should pass else returns False
                    if return_code:
                        return_code = 0
                    else:
                        return_code = -1
        except Exception as e:
            kwargs['fail_msg'] = f"Error raised for keyword [{keyword_name}] Error: {e}"
            self.common_validation.fault(**kwargs)
        finally:
            self.keyword_utils.timing.end(keyword_name)

        # Return the return value of the keyword
        return return_code