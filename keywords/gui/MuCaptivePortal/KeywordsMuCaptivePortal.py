# Standard Keyword imports
from extauto.common.CommonValidation import CommonValidation
from extauto.common.KeywordUtils import KeywordUtils
import inspect
from ExtremeAutomation.Library.Utils.Singleton import Singleton


# Keyword imports required to run keywords implemented in this file
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

        # Object used to run keywords implemented in this file
        self.mucaptiveportal = MuCaptivePortal()

    def validate_cwp_social_login_with_facebook(self, username, password, **kwargs):
        """
        Register network via facebook login Captive Web Portal(CWP)

        This keyword is neither XAPI nor GUI based.
        This keyword validates Captive Web Portal social login with facebook credentials.

        - Keyword Prerequisites:
        -       Device is onboarded             [Onboard Device Quick]
        -       Device connected to cloud       [Configure Device To Connect To Cloud]
        -       Device upgraded                 [Upgrade Device]
        -       Network policy is created       [Create Network Policy]
        -       Network policy is updated to AP [Update Network Policy To Ap]
        -       Connect MU to open ssid         [Connect Open Network]
        -       Opening CP Web browser on MU    [Open Cp Browser]
        -
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
        -    This does not access a WebApplication and therefore does not have a GUI or XAPI implementation

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

        # We'll assume a failure and change the value if successful
        return_code = -1

        # Call the helper function that implements this keyword
        try:
            self.keyword_utils.timing.start(keyword_name, "GUI")
            return_code = self.mucaptiveportal.gui_validate_cwp_social_login_with_facebook(username, password)
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

        This keyword is neither XAPI nor GUI based.
        This keyword validates Captive Web Portal social login with Linkedin credentials.

        - Keyword Prerequisites:
        -       Device is onboarded             [Onboard Device Quick]
        -       Device connected to cloud       [Configure Device To Connect To Cloud]
        -       Device upgraded                 [Upgrade Device]
        -       Network policy is created       [Create Network Policy]
        -       Network policy is updated to AP [Update Network Policy To Ap]
        -       Connect MU to open ssid         [Connect Open Network]
        -       Opening CP Web browser on MU    [Open Cp Browser]
        -
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
        -    This does not access a WebApplication and therefore does not have a GUI or XAPI implementation

        :param username: Username of Linkedin Account
        :param password: Password of Linkedin Account
        :return: Returns 1 if successful. Returns -1 if not successful.
        """
        # Notes:
        #   - The work for this keyword is in a separate file
        #   - The amount of time this keyword takes will be recorded and optionally recorded in a database
        #   - This method will catch any errors that are raised and not handled in the keyword
        keyword_name = inspect.stack()[0][3]
        self.keyword_utils.implementations.set_keyword_uuid("48206a8d-2eb3-4c5c-9179-2e7090ac968f", keyword_name)

        # We'll assume a failure and change the value if successful
        return_code = -1

        # Call the helper function that implements this keyword
        try:
            self.keyword_utils.timing.start(keyword_name, "GUI")
            return_code = self.mucaptiveportal.gui_validate_cwp_social_login_with_linkedin_account(username, password)
        except Exception as e:
            kwargs['fail_msg'] = f"Error raised for keyword [{keyword_name}] Error: {e}"
            self.common_validation.fault(**kwargs)
        finally:
            self.keyword_utils.timing.end(keyword_name)

        # Return the return value of the keyword
        return return_code

