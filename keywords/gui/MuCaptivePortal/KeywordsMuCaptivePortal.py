# Standard Keyword imports
from extauto.common.CommonValidation import CommonValidation
from extauto.common.KeywordUtils import KeywordUtils
import inspect
from tools.xapi.XapiHelper import XapiHelper
from ExtremeAutomation.Library.Utils.Singleton import Singleton
from extauto.xiq.xapi.globalsettings.XapiGlobalSettings import XapiGlobalSettings


# Keyword imports required to run keywords implemented in this file
from extauto.xiq.xapi.common.XapiLogin import XapiLogin
from extauto.xiq.flows.common.MuCaptivePortal import MuCaptivePortal


class KeywordsMuCaptivePortal(object, metaclass=Singleton):
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
        self.mucaptiveportal = MuCaptivePortal()
        self.xapi_login = XapiLogin()

    def validate_cwp_social_login_with_facebook(self, username, password, **kwargs):
        """
        Register network via facebook login Captive Web Portal(CWP)

        This method validates Captive Web Portal social login with facebook credentials.
        Pre-requisites for this keyword is Onboard device, configure device, online device check, Get device status,
        Device Reboot, Create network policy, update network policy.

        - Keyword Usage:
        -   Robot:
        -      Library  keywords/gui/MuCaptivePortal/KeywordsMuCaptivePortal.py
        -      validate cwp social login with facebook      ${username}     ${password}
        -   Pytest:
        -      Imports:
        -         from keywords.gui.MuCaptivePortal.KeywordsMuCaptivePortal import KeywordsMuCaptivePortal
        -      Calling Keyword:
        -         keywords_MuCaptivePortal = KeywordsMuCaptivePortal()
        -         keywords_MuCaptivePortal.validate_cwp_social_login_with_facebook()
        -
        - Keyword Implementations:
        -    GUI
        -    XAPI - ** Not Supported **

        :param username: Username of FB Account
        :param password: Password of FB Account
        :return: Returns 1 if successful. Returns -1 if not successful.
        """
        # Notes:
        #   - The work for this keyword is in a separate file
        #   - The amount of time this keyword takes will be recorded and optionally recorded in a database
        #   - This method will catch any errors that are raised and not handled in the keyword
        keyword_name = inspect.stack()[0][3]
        self.keyword_utils.implementations.set_keyword_uuid("b66f8e51-55f8-4670-83ca-57bcd399fa5c", keyword_name)
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
                    return_code = self.mucaptiveportal.gui_validate_cwp_social_login_with_facebook(username, password)
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

    def validate_cwp_social_login_with_linkedin_account(self, username, password, **kwargs):
        """
        Register network via Linkedin login Captive Web Portal(CWP)

        This method validates Captive Web Portal social login with linkedin credentials.
        Pre-requisites for this keyword is Onboard device, configure device, online device check, Get device status,
        Device Reboot, Create network policy, update network policy.

        - Keyword Usage:
        -   Robot:
        -      Library  keywords/gui/MuCaptivePortal/KeywordsMuCaptivePortal.py
        -      validate cwp social login with linkedin account      ${username}     ${password}
        -   Pytest:
        -      Imports:
        -         from keywords.gui.MuCaptivePortal.KeywordsMuCaptivePortal import KeywordsMuCaptivePortal
        -      Calling Keyword:
        -         keywords_MuCaptivePortal = KeywordsMuCaptivePortal()
        -         keywords_MuCaptivePortal.validate_cwp_social_login_with_linkedin_account()
        -
        - Keyword Implementations:
        -    GUI
        -    XAPI - ** Not Supported **

        :param username: Username of Linkedin Account
        :param password: Password of Linkedin Account
        :return: Returns 1 if successful. Returns -1 if not successful.
        """
        # Notes:
        #   - The work for this keyword is in a separate file
        #   - The amount of time this keyword takes will be recorded and optionally recorded in a database
        #   - This method will catch any errors that are raised and not handled in the keyword
        keyword_name = inspect.stack()[0][3]
        self.keyword_utils.implementations.set_keyword_uuid("79bed63f-3a92-460f-bb6e-07cff041ff88", keyword_name)
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
                    return_code = self.mucaptiveportal.gui_validate_cwp_social_login_with_linkedin_account(username, password)
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

