# Standard Keyword imports
from extauto.common.CommonValidation import CommonValidation
from extauto.common.KeywordUtils import KeywordUtils
import inspect
from tools.xapi.XapiHelper import XapiHelper
from ExtremeAutomation.Library.Utils.Singleton import Singleton
from extauto.xiq.xapi.globalsettings.XapiGlobalSettings import XapiGlobalSettings


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
        self.XapiGlobalSettings = XapiGlobalSettings()

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
        if self.xapi_helper.is_xapi_enabled(**kwargs):
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
        -         keywords_login.quit_browser()
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

    def get_page_title(self, **kwargs):
        """
        Gets the title of the page

        This method gets the current page title.

        - Keyword Usage:
        -   Robot:
        -      Library  keywords/gui/login/KeywordsLogin.py
        -      Get Page Title
        -   Pytest:
        -      Imports:
        -         from keywords.gui.login.KeywordsLogin import KeywordsLogin
        -      Calling Keyword:
        -         keywords_login = KeywordsLogin()
        -         keywords_login.get_page_title()
        -
        - Keyword Implementations:
        -    GUI
        -    XAPI - ** Not Supported **

        :return: Returns the page title that "ExtremeCloud IQ" if successful. Returns "" if not successful.
        """

        # Notes:
        #   - The work for this keyword is in a separate file
        #   - The amount of time this keyword takes will be recorded and optionally recorded in a database
        #   - This method will catch any errors that are raised and not handled in the keyword
        keyword_name = inspect.stack()[0][3]
        self.keyword_utils.implementations.set_keyword_uuid("bc887c5e-0c31-41ba-89b3-ff426fde1699", keyword_name)
        self.keyword_utils.implementations.gui_implemented(keyword_name, prefer_gui=True)
        self.keyword_utils.implementations.xapi_implemented(keyword_name)

        # Assume if no page title
        return_code = ""

        # Call the helper function that implements this keyword
        try:
            implementation_to_run = self.keyword_utils.implementations.select_keyword_implementation(keyword_name, **kwargs)
            if implementation_to_run != '':
                self.keyword_utils.timing.start(keyword_name, 'GUI')
                if implementation_to_run == "GUI":
                    return_code = self.login.gui_get_page_title()
                else:
                    return_code = self.keyword_utils.implementations.not_supported(**kwargs)
                    return_code = ""
        except Exception as e:
            kwargs['fail_msg'] = f"Error raised for keyword [{keyword_name}] Error: {e}"
            self.common_validation.fault(**kwargs)
        finally:
            self.keyword_utils.timing.end(keyword_name)

        # Return the return value of the keyword
        return return_code

    def get_current_page_url(self, **kwargs):
        """
        Gets the current page url

        This method gets the current page url.

        - Keyword Usage:
        -   Robot:
        -      Library  keywords/gui/login/KeywordsLogin.py
        -      Get Current Page URL
        -   Pytest:
        -      Imports:
        -         from keywords.gui.login.KeywordsLogin import KeywordsLogin
        -      Calling Keyword:
        -         keywords_login = KeywordsLogin()
        -         keywords_login.get_current_page_url()
        -
        - Keyword Implementations:
        -    GUI
        -    XAPI - ** Not Supported **

        :return: Returns the Current page URL if successful. Returns "" if not successful.
        """

        # Notes:
        #   - The work for this keyword is in a separate file
        #   - The amount of time this keyword takes will be recorded and optionally recorded in a database
        #   - This method will catch any errors that are raised and not handled in the keyword
        keyword_name = inspect.stack()[0][3]
        self.keyword_utils.implementations.set_keyword_uuid("2558f0e3-5f82-4bf6-be15-41e114f7b656", keyword_name)
        self.keyword_utils.implementations.gui_implemented(keyword_name, prefer_gui=True)
        self.keyword_utils.implementations.xapi_implemented(keyword_name)

        # Assume if no page url
        return_code = ""

        # Call the helper function that implements this keyword
        try:
            implementation_to_run = self.keyword_utils.implementations.select_keyword_implementation(keyword_name, **kwargs)
            if implementation_to_run != '':
                self.keyword_utils.timing.start(keyword_name, 'GUI')
                if implementation_to_run == "GUI":
                    return_code = self.login.gui_get_current_page_url()
                else:
                    return_code = self.keyword_utils.implementations.not_supported(**kwargs)
                    return_code = ""
        except Exception as e:
            kwargs['fail_msg'] = f"Error raised for keyword [{keyword_name}] Error: {e}"
            self.common_validation.fault(**kwargs)
        finally:
            self.keyword_utils.timing.end(keyword_name)

        # Return the return value of the keyword
        return return_code

    def get_base_url_of_current_page(self, **kwargs):
        """
        Gets the base url of current page

        This method gets the website address of the current page for example https://va2.extremecloudiq.com

        - Keyword Usage:
        -   Robot:
        -      Library  keywords/gui/login/KeywordsLogin.py
        -      Get Base URL of Current Page
        -   Pytest:
        -      Imports:
        -         from keywords.gui.login.KeywordsLogin import KeywordsLogin
        -      Calling Keyword:
        -         keywords_login = KeywordsLogin()
        -         keywords_login.get_base_url_of_current_page()
        -
        - Keyword Implementations:
        -    GUI
        -    XAPI - ** Not Supported **

        :return: Returns the base url of Current page that "https://va2.extremecloudiq.com" if successful. Returns "" if not successful.
        """

        # Notes:
        #   - The work for this keyword is in a separate file
        #   - The amount of time this keyword takes will be recorded and optionally recorded in a database
        #   - This method will catch any errors that are raised and not handled in the keyword
        keyword_name = inspect.stack()[0][3]
        self.keyword_utils.implementations.set_keyword_uuid("f7415546-411f-4102-bbdc-086b585b21dd", keyword_name)
        self.keyword_utils.implementations.gui_implemented(keyword_name, prefer_gui=True)
        self.keyword_utils.implementations.xapi_implemented(keyword_name)

        # Assume if no base url
        return_code = ""

        # Call the helper function that implements this keyword
        try:
            implementation_to_run = self.keyword_utils.implementations.select_keyword_implementation(keyword_name, **kwargs)
            if implementation_to_run != '':
                self.keyword_utils.timing.start(keyword_name, 'GUI')
                if implementation_to_run == "GUI":
                    return_code = self.login.gui_get_base_url_of_current_page()
                else:
                    return_code = self.keyword_utils.implementations.not_supported(**kwargs)
                    return_code = ""
        except Exception as e:
            kwargs['fail_msg'] = f"Error raised for keyword [{keyword_name}] Error: {e}"
            self.common_validation.fault(**kwargs)
        finally:
            self.keyword_utils.timing.end(keyword_name)

        # Return the return value of the keyword
        return return_code

    def get_xiq_version(self, **kwargs):
        """
        Gets the XIQ Build version details

        This method clicks on "About ExtremeCloud IQ" at the top right and gets the Build version details from the "About ExtremeCloud IQ" popup. For example "Build Version: 23.2.0.30"

        - Keyword Usage:
        -   Robot:
        -      Library  keywords/gui/login/KeywordsLogin.py
        -      Get XIQ Version
        -   Pytest:
        -      Imports:
        -         from keywords.gui.login.KeywordsLogin import KeywordsLogin
        -      Calling Keyword:
        -         keywords_login = KeywordsLogin()
        -         keywords_login.get_xiq_version()
        -
        - Keyword Implementations:
        -    GUI
        -    XAPI - ** Not Supported **

        :return: Returns the XIQ Version details ex:23.1.5.4 if successful. Returns "" if not successful.
        """

        # Notes:
        #   - The work for this keyword is in a separate file
        #   - The amount of time this keyword takes will be recorded and optionally recorded in a database
        #   - This method will catch any errors that are raised and not handled in the keyword
        keyword_name = inspect.stack()[0][3]
        self.keyword_utils.implementations.set_keyword_uuid("40486809-8145-4fdf-8000-0f9f865733d8", keyword_name)
        self.keyword_utils.implementations.gui_implemented(keyword_name, prefer_gui=True)
        self.keyword_utils.implementations.xapi_implemented(keyword_name)

        # Assume if no XIQ Build version details
        return_code = ""

        # Call the helper function that implements this keyword
        try:
            implementation_to_run = self.keyword_utils.implementations.select_keyword_implementation(keyword_name, **kwargs)
            if implementation_to_run != '':
                self.keyword_utils.timing.start(keyword_name, 'GUI')
                if implementation_to_run == "GUI":
                    return_code = self.login.gui_get_xiq_version()
                else:
                    return_code = self.keyword_utils.implementations.not_supported(**kwargs)
                    return_code = ""
        except Exception as e:
            kwargs['fail_msg'] = f"Error raised for keyword [{keyword_name}] Error: {e}"
            self.common_validation.fault(**kwargs)
        finally:
            self.keyword_utils.timing.end(keyword_name)

        # Return the return value of the keyword
        return return_code

    def get_viq_id(self, **kwargs):
        """
        Gets the VIQ ID.

        This method clicks on "About ExtremeCloud IQ" at the top right and gets the VIQ ID details from the "About ExtremeCloud IQ" popup. For example "VIQ ID: 306811".

        - Keyword Usage:
        -   Robot:
        -      Library  keywords/gui/login/KeywordsLogin.py
        -      Get viq id
        -   Pytest:
        -      Imports:
        -         from keywords.gui.login.KeywordsLogin import KeywordsLogin
        -      Calling Keyword:
        -         keywords_login = KeywordsLogin()
        -         keywords_login.get_viq_id()
        -
        - Keyword Implementations:
        -    GUI
        -    XAPI

        :return: Returns the VIQ ID (string) if successful. Returns "" if not successful.
        """

        # Notes:
        #   - The work for this keyword is in a separate file
        #   - The amount of time this keyword takes will be recorded and optionally recorded in a database
        #   - This method will catch any errors that are raised and not handled in the keyword
        keyword_name = inspect.stack()[0][3]
        self.keyword_utils.implementations.set_keyword_uuid("8ef7bee7-5436-4a5d-b809-a6d7ec37e27a", keyword_name)
        self.keyword_utils.implementations.gui_implemented(keyword_name)
        self.keyword_utils.implementations.xapi_implemented(keyword_name)

        #Assume if no VIQ ID
        return_code = ""

        # Call the helper function that implements this keyword
        try:
            implementation_to_run = self.keyword_utils.implementations.select_keyword_implementation(keyword_name, **kwargs)
            if implementation_to_run != '':
                self.keyword_utils.timing.start(keyword_name, 'GUI')
                if implementation_to_run == "GUI":
                    return_code = self.login.gui_get_viq_id()
                    return return_code
                elif implementation_to_run == "XAPI":
                    return_code = self.XapiGlobalSettings.xapi_get_viq_id(**kwargs)
                    return return_code
        except Exception as e:
            kwargs['fail_msg'] = f"Error raised for keyword [{keyword_name}] Error: {e}"
            self.common_validation.fault(**kwargs)
        finally:
            self.keyword_utils.timing.end(keyword_name)

        return return_code

    def get_data_center_name(self, **kwargs):
        """
        Gets the Data Center Name details

        This method clicks on "About ExtremeCloud IQ" at the top right and gets the Data Center Name details from the "About ExtremeCloud IQ" popup. For example "Data Center Name: US_East2"

        - Keyword Usage:
        -   Robot:
        -      Library  keywords/gui/login/KeywordsLogin.py
        -      Get Data Center Name
        -   Pytest:
        -      Imports:
        -         from keywords.gui.login.KeywordsLogin import KeywordsLogin
        -      Calling Keyword:
        -         keywords_login = KeywordsLogin()
        -         keywords_login.get_data_center_name()
        -
        - Keyword Implementations:
        -    GUI
        -    XAPI - ** "Not Implemented" **

        :return: Returns the Data Center Name if successful. Returns "" if not successful.
        """

        # Notes:
        #   - The work for this keyword is in a separate file
        #   - The amount of time this keyword takes will be recorded and optionally recorded in a database
        #   - This method will catch any errors that are raised and not handled in the keyword
        keyword_name = inspect.stack()[0][3]
        self.keyword_utils.implementations.set_keyword_uuid("0e6d527e-be34-4f60-b112-af4136ee71d9", keyword_name)
        self.keyword_utils.implementations.gui_implemented(keyword_name, prefer_gui=True)

        # Assume if no XIQ Data Center Name
        return_code = ""

        # Call the helper function that implements this keyword
        try:
            implementation_to_run = self.keyword_utils.implementations.select_keyword_implementation(keyword_name, **kwargs)
            if implementation_to_run != '':
                self.keyword_utils.timing.start(keyword_name, 'GUI')
                if implementation_to_run == "GUI":
                    return_code = self.login.gui_get_data_center_name()
                else:
                    # XAPI is not implemented
                    self.common_validation.fault(**kwargs)
                    return_code = ""
        except Exception as e:
            kwargs['fail_msg'] = f"Error raised for keyword [{keyword_name}] Error: {e}"
            self.common_validation.fault(**kwargs)
        finally:
            self.keyword_utils.timing.end(keyword_name)

        # Return the return value of the keyword
        return return_code

    def logo_check_on_login_screen(self, **kwargs):
        """
        Checks the banner image on the login screen

        This method checks the banner image on the right side of the login screen. For example "ExtremeCloud IQ  Mobile Companion"

        - Keyword Usage:
        -   Robot:
        -      Library  keywords/gui/login/KeywordsLogin.py
        -      logo check on login screen
        -   Pytest:
        -      Imports:
        -         from keywords.gui.login.KeywordsLogin import KeywordsLogin
        -      Calling Keyword:
        -         keywords_login = KeywordsLogin()
        -         keywords_login.logo_check_on_login_screen()
        -
        - Keyword Implementations:
        -    GUI
        -    XAPI - ** Not Supported **

        :return: Returns the login page logo screenshot if successful. Returns "" if not successful.
        """

        # Notes:
        #   - The work for this keyword is in a separate file
        #   - The amount of time this keyword takes will be recorded and optionally recorded in a database
        #   - This method will catch any errors that are raised and not handled in the keyword
        keyword_name = inspect.stack()[0][3]
        self.keyword_utils.implementations.set_keyword_uuid("50323a43-ebc6-459c-b857-130e93b118f8", keyword_name)
        self.keyword_utils.implementations.gui_implemented(keyword_name, prefer_gui=True)
        self.keyword_utils.implementations.xapi_implemented(keyword_name)

        # Assume if no login logo
        return_code = ""

        # Call the helper function that implements this keyword
        try:
            implementation_to_run = self.keyword_utils.implementations.select_keyword_implementation(keyword_name, **kwargs)
            if implementation_to_run != '':
                self.keyword_utils.timing.start(keyword_name, 'GUI')
                if implementation_to_run == "GUI":
                    return_code = self.login.gui_logo_check_on_login_screen()
                else:
                    return_code = self.keyword_utils.implementations.not_supported(**kwargs)
                    return_code = ""
        except Exception as e:
            kwargs['fail_msg'] = f"Error raised for keyword [{keyword_name}] Error: {e}"
            self.common_validation.fault(**kwargs)
        finally:
            self.keyword_utils.timing.end(keyword_name)

        # Return the return value of the keyword
        return return_code

    def refresh_page(self, refresh_delay=10, **kwargs):
        """
        Refreshes the current page

        This method uses the browser's refresh button to refresh the current page. Default refresh delay is 10 seconds.

        - Keyword Usage:
        -   Robot:
        -      Library  keywords/gui/login/KeywordsLogin.py
        -      Refresh page
        -   Pytest:
        -      Imports:
        -         from keywords.gui.login.KeywordsLogin import KeywordsLogin
        -      Calling Keyword:
        -         keywords_login = KeywordsLogin()
        -         keywords_login.refresh_page()
        -
        - Keyword Implementations:
        -    GUI
        -    XAPI - ** Not Supported **

        :param refresh_delay: Default refresh delay is 10 seconds. Waits 10 seconds of time after the page is refreshed.
        :return: Returns None
        """

        # Notes:
        #   - The work for this keyword is in a separate file
        #   - The amount of time this keyword takes will be recorded and optionally recorded in a database
        #   - This method will catch any errors that are raised and not handled in the keyword
        keyword_name = inspect.stack()[0][3]
        self.keyword_utils.implementations.set_keyword_uuid("b617c89f-a5de-4fae-950a-5326ad0e8c05", keyword_name)
        self.keyword_utils.implementations.gui_implemented(keyword_name, prefer_gui=True)
        self.keyword_utils.implementations.xapi_implemented(keyword_name)

        # Call the helper function that implements this keyword
        try:
            implementation_to_run = self.keyword_utils.implementations.select_keyword_implementation(keyword_name, **kwargs)
            if implementation_to_run != '':
                self.keyword_utils.timing.start(keyword_name, 'GUI')
                if implementation_to_run == "GUI":
                    self.login.gui_refresh_page(refresh_delay)
                else:
                    self.keyword_utils.implementations.not_supported(**kwargs)
        except Exception as e:
            kwargs['fail_msg'] = f"Error raised for keyword [{keyword_name}] Error: {e}"
            self.common_validation.fault(**kwargs)
        finally:
            self.keyword_utils.timing.end(keyword_name)

    def click_advanced_onboard_popup(self, **kwargs):
        """
        Clicks the advanced Onboard popup sliding window

        This method clicks the advanced Onboard popup sliding window that appears during the first login or after reset VIQ.

        - Keyword Usage:
        -   Robot:
        -      Library  keywords/gui/login/KeywordsLogin.py
        -      Click advanced Onboard popup
        -   Pytest:
        -      Imports:
        -         from keywords.gui.login.KeywordsLogin import KeywordsLogin
        -      Calling Keyword:
        -         keywords_login = KeywordsLogin()
        -         keywords_login.click_advanced_onboard_popup()
        -
        - Keyword Implementations:
        -    GUI
        -    XAPI - ** Not Supported **

        :return: Returns None
        """

        # Notes:
        #   - The work for this keyword is in a separate file
        #   - The amount of time this keyword takes will be recorded and optionally recorded in a database
        #   - This method will catch any errors that are raised and not handled in the keyword
        keyword_name = inspect.stack()[0][3]
        self.keyword_utils.implementations.set_keyword_uuid("0dc755ce-5fec-4b09-838e-a4fbb24511ba", keyword_name)
        self.keyword_utils.implementations.gui_implemented(keyword_name, prefer_gui=True)
        self.keyword_utils.implementations.xapi_implemented(keyword_name)

        # Call the helper function that implements this keyword
        try:
            implementation_to_run = self.keyword_utils.implementations.select_keyword_implementation(keyword_name, **kwargs)
            if implementation_to_run != '':
                self.keyword_utils.timing.start(keyword_name, 'GUI')
                if implementation_to_run == "GUI":
                    self.login.gui_click_advanced_onboard_popup()
                else:
                    self.keyword_utils.implementations.not_supported(**kwargs)
        except Exception as e:
            kwargs['fail_msg'] = f"Error raised for keyword [{keyword_name}] Error: {e}"
            self.common_validation.fault(**kwargs)
        finally:
            self.keyword_utils.timing.end(keyword_name)

    def load_web_page(self, url="default", **kwargs):
        """
        Loads the webpage of extremecloudiq

        This method loads the webpage url which is the ${TEST_URL} parameter provided in the internal_api.robot file if url='default'.
        To pass a url value, example url="https://10.16.118.155"

        - Keyword Usage:
        -   Robot:
        -      Library  keywords/gui/login/KeywordsLogin.py
        -      Load web page
        -   Pytest:
        -      Imports:
        -         from keywords.gui.login.KeywordsLogin import KeywordsLogin
        -      Calling Keyword:
        -         keywords_login = KeywordsLogin()
        -         keywords_login.load_web_page()
        -
        - Keyword Implementations:
        -    GUI
        -    XAPI - ** Not Supported **

        :param url: webpage url to load.For example url="https://extremecloud.com" or url="default". If url is default loads the "https://extremecloudiq.com" webpage.
        :return: Returns None
        """

        # Notes:
        #   - The work for this keyword is in a separate file
        #   - The amount of time this keyword takes will be recorded and optionally recorded in a database
        #   - This method will catch any errors that are raised and not handled in the keyword
        keyword_name = inspect.stack()[0][3]
        self.keyword_utils.implementations.set_keyword_uuid("e5c444e6-64ec-4d45-860a-801c7d068137", keyword_name)
        self.keyword_utils.implementations.gui_implemented(keyword_name, prefer_gui=True)
        self.keyword_utils.implementations.xapi_implemented(keyword_name)

        # Call the helper function that implements this keyword
        try:
            implementation_to_run = self.keyword_utils.implementations.select_keyword_implementation(keyword_name, **kwargs)
            if implementation_to_run != '':
                self.keyword_utils.timing.start(keyword_name, 'GUI')
                if implementation_to_run == "GUI":
                    self.login.gui_load_web_page(url)
                else:
                    self.keyword_utils.implementations.not_supported(**kwargs)
        except Exception as e:
            kwargs['fail_msg'] = f"Error raised for keyword [{keyword_name}] Error: {e}"
            self.common_validation.fault(**kwargs)
        finally:
            self.keyword_utils.timing.end(keyword_name)

    def forgot_password(self, _email, url='default', **kwargs):
        """
        Sends a link to email to reset a forgotten password

        This method sends a link to the provided email to reset the password
        _email is the mandatory parameter.
        Examples of parameters _email = "xiqextremeqa+adess-va2@gmail.com" and url="https://extremecloud.com" or url="default"

        - Keyword Usage:
        -   Robot:
        -      Library  keywords/gui/login/KeywordsLogin.py
        -      Forgot Password      _email=${email}   # ${email}= xiqextremeqa+adess-va2@gmail.com
        -   Pytest:
        -      Imports:
        -         from keywords.gui.login.KeywordsLogin import KeywordsLogin
        -      Calling Keyword:
        -         keywords_login = KeywordsLogin()
        -         keywords_login.forgot_password()
        -
        - Keyword Implementations:
        -    GUI
        -    XAPI - ** Not Supported **

        :param _email: Email id of the user to reset the password. Example _email = "xiqextremeqa+adess-va2@gmail.com"
        :param url: Forgot Password URL. Examples url="https://extremecloud.com" or url="default"
        :return: Returns 1 if successful. Returns -1 if not successful.
        """
        # Notes:
        #   - The work for this keyword is in a separate file
        #   - The amount of time this keyword takes will be recorded and optionally recorded in a database
        #   - This method will catch any errors that are raised and not handled in the keyword
        keyword_name = inspect.stack()[0][3]
        self.keyword_utils.implementations.set_keyword_uuid("eae76737-aa73-41d4-a6f9-e7aead2d57e5", keyword_name)
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
                    return_code = self.login.gui_forgot_password(_email, url)
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

    def get_switch_connection_host(self, **kwargs):
        """
        Gets the Switch Connection Host details.

        This method clicks on "About ExtremeCloud IQ" at the top right and gets the Switch Connection Host details from the "About ExtremeCloud IQ" popup.
        For example "Switch Connection Host: va2.extremecloudiq.com"

        - Keyword Usage:
        -   Robot:
        -      Library  keywords/gui/login/KeywordsLogin.py
        -      Get Switch Connection Host
        -   Pytest:
        -      Imports:
        -         from keywords.gui.login.KeywordsLogin import KeywordsLogin
        -      Calling Keyword:
        -         keywords_login = KeywordsLogin()
        -         keywords_login.get_switch_connection_host()
        -
        - Keyword Implementations:
        -    GUI
        -    XAPI - ** Not Implemented **

        :return: Returns the Switch Connection Host that "va2.extremecloudiq.com" if success. Returns "" if not success.
        """

        # Notes:
        #   - The work for this keyword is in a separate file
        #   - The amount of time this keyword takes will be recorded and optionally recorded in a database
        #   - This method will catch any errors that are raised and not handled in the keyword
        keyword_name = inspect.stack()[0][3]
        self.keyword_utils.implementations.set_keyword_uuid("9b91eaa8-0486-4679-88a3-5dea1f45fe29", keyword_name)
        self.keyword_utils.implementations.gui_implemented(keyword_name, prefer_gui=True)

        # Assume if no Switch Connection Host
        return_code = ""

        # Call the helper function that implements this keyword
        try:
            implementation_to_run = self.keyword_utils.implementations.select_keyword_implementation(keyword_name, **kwargs)
            if implementation_to_run != '':
                self.keyword_utils.timing.start(keyword_name, 'GUI')
                if implementation_to_run == "GUI":
                    return_code = self.login.gui_get_switch_connection_host()
                else:
                    self.common_validation.fault(**kwargs)
                    return_code = ""
        except Exception as e:
            kwargs['fail_msg'] = f"Error raised for keyword [{keyword_name}] Error: {e}"
            self.common_validation.fault(**kwargs)
        finally:
            self.keyword_utils.timing.end(keyword_name)

        # Return the return value of the keyword
        return return_code

    def switch_to_window(self, win_index, **kwargs):
        """
        To switch from one window to another window of the browser

        This method is used to switch from one window to another window of the browser.

        - Keyword Usage:
        -   Robot:
        -      Library  keywords/gui/login/KeywordsLogin.py
        -      Switch to window     ${win_index}
        -   Pytest:
        -      Imports:
        -         from keywords.gui.login.KeywordsLogin import KeywordsLogin
        -      Calling Keyword:
        -         keywords_login = KeywordsLogin()
        -         keywords_login.switch_to_window()
        -
        - Keyword Implementations:
        -    GUI
        -    XAPI - ** Not Supported **

        :param win_index:  Index of the window to switch to, this should be integer ex. 0 or 1 or 2
        :return: Returns None
        """

        # Notes:
        #   - The work for this keyword is in a separate file
        #   - The amount of time this keyword takes will be recorded and optionally recorded in a database
        #   - This method will catch any errors that are raised and not handled in the keyword
        keyword_name = inspect.stack()[0][3]
        self.keyword_utils.implementations.set_keyword_uuid("7471b963-c9f0-42f2-ab81-c6731661198b", keyword_name)
        self.keyword_utils.implementations.gui_implemented(keyword_name, prefer_gui=True)

        # Assume if unable to switch window
        return_code = -1

        # Call the helper function that implements this keyword
        try:
            implementation_to_run = self.keyword_utils.implementations.select_keyword_implementation(keyword_name, **kwargs)
            if implementation_to_run != '':
                self.keyword_utils.timing.start(keyword_name, 'GUI')
                if implementation_to_run == "GUI":
                    return_code = self.login.gui_switch_to_window(win_index)
                else:
                    return_code = self.keyword_utils.implementations.not_supported(**kwargs)
                    return_code = -1
        except Exception as e:
            kwargs['fail_msg'] = f"Error raised for keyword [{keyword_name}] Error: {e}"
            self.common_validation.fault(**kwargs)
        finally:
            self.keyword_utils.timing.end(keyword_name)

        # Return the return value of the keyword
        return return_code

    def close_window(self, win_index, **kwargs):
        """
        To close the window of the browser

        This method is used to close the window of the browser.

        - Keyword Usage:
        -   Robot:
        -      Library  keywords/gui/login/KeywordsLogin.py
        -      Close window     ${win_index}
        -   Pytest:
        -      Imports:
        -         from keywords.gui.login.KeywordsLogin import KeywordsLogin
        -      Calling Keyword:
        -         keywords_login = KeywordsLogin()
        -         keywords_login.close_window()
        -
        - Keyword Implementations:
        -    GUI
        -    XAPI - ** Not Supported **

        :param win_index:  Index of the window to close, this should be integer ex. 0 or 1 or 2
        :return: Returns None
        """

        # Notes:
        #   - The work for this keyword is in a separate file
        #   - The amount of time this keyword takes will be recorded and optionally recorded in a database
        #   - This method will catch any errors that are raised and not handled in the keyword
        keyword_name = inspect.stack()[0][3]
        self.keyword_utils.implementations.set_keyword_uuid("33bc046f-ccb5-4219-9d8d-f1c3ba459d90", keyword_name)
        self.keyword_utils.implementations.gui_implemented(keyword_name, prefer_gui=True)

        # Assume if unable to switch window
        return_code = -1

        # Call the helper function that implements this keyword
        try:
            implementation_to_run = self.keyword_utils.implementations.select_keyword_implementation(keyword_name, **kwargs)
            if implementation_to_run != '':
                self.keyword_utils.timing.start(keyword_name, 'GUI')
                if implementation_to_run == "GUI":
                    return_code = self.login.gui_close_window(win_index)
                else:
                    return_code = self.keyword_utils.implementations.not_supported(**kwargs)
                    return_code = -1
        except Exception as e:
            kwargs['fail_msg'] = f"Error raised for keyword [{keyword_name}] Error: {e}"
            self.common_validation.fault(**kwargs)
        finally:
            self.keyword_utils.timing.end(keyword_name)

        # Return the return value of the keyword
        return return_code

    def skip_if_account_90_days(self, **kwargs):
        """
        Detects a license of 90 days and clicks on the option of 90 days

        This method detects a license of 90 days on home page and clicks on the option of 90 days

        - Keyword Usage:
        -   Robot:
        -      Library  keywords/gui/login/KeywordsLogin.py
        -      Skip If Account 90 Days
        -   Pytest:
        -      Imports:
        -         from keywords.gui.login.KeywordsLogin import KeywordsLogin
        -      Calling Keyword:
        -         keywords_login = KeywordsLogin()
        -         keywords_login.skip_if_account_90_days()
        -
        - Keyword Implementations:
        -    GUI
        -    XAPI - ** Not Supported **

        :return: Returns 1 if success. Returns -1 if not success.
        """
        # Notes:
        #   - The work for this keyword is in a separate file
        #   - The amount of time this keyword takes will be recorded and optionally recorded in a database
        #   - This method will catch any errors that are raised and not handled in the keyword
        keyword_name = inspect.stack()[0][3]
        self.keyword_utils.implementations.set_keyword_uuid("a01301b5-ef58-4e9f-9d0d-ae33f307768d", keyword_name)
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
                    return_code = self.login.gui_skip_if_account_90_days()
                    #return_code = int(return_code)
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

    def verify_upgrade_option_for_connect_user(self, **kwargs):
        """
        Clicks on the upgrade button and navigates connect user to license management UI

        This method checks if upgrade button is displayed and clicks on the upgrade button and navigates connect user to license management UI

        - Keyword Usage:
        -   Robot:
        -      Library  keywords/gui/login/KeywordsLogin.py
        -      Verify Upgrade Option For Connect User
        -   Pytest:
        -      Imports:
        -         from keywords.gui.login.KeywordsLogin import KeywordsLogin
        -      Calling Keyword:
        -         keywords_login = KeywordsLogin()
        -         keywords_login.verify_upgrade_option_for_connect_user()
        -
        - Keyword Implementations:
        -    GUI
        -    XAPI - ** Not Supported **

        :return: Returns 1 if success. Returns -1 if not success.
        """
        # Notes:
        #   - The work for this keyword is in a separate file
        #   - The amount of time this keyword takes will be recorded and optionally recorded in a database
        #   - This method will catch any errors that are raised and not handled in the keyword
        keyword_name = inspect.stack()[0][3]
        self.keyword_utils.implementations.set_keyword_uuid("777346b6-8887-41e3-8d94-ef7bbc8f359d", keyword_name)
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
                    return_code = self.login.gui_verify_upgrade_option_for_connect_user()
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

