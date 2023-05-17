
from extauto.common.CommonValidation import CommonValidation
from extauto.common.KeywordUtils import KeywordUtils
from tools.xapi.XapiHelper import XapiHelper
import inspect
from ExtremeAutomation.Library.Utils.Singleton import Singleton 
from extauto.xiq.flows.globalsettings.PasswordReset import PasswordReset


class KeywordsPasswordReset(object, metaclass=Singleton):
    def __init__(self):
        # This is a singleton, avoid initializing for each instance 
        if hasattr(self, 'initialized'): 
            return 
        self.initialized = True
        
        # Objects used by all keywords 
        self.common_validation = CommonValidation() 
        self.keyword_utils = KeywordUtils() 
        self.xapi_helper = XapiHelper()

        self.password_reset = PasswordReset()

    def add_account(self, name, _email, **kwargs):
        """
        Adds a new account under account management

        This method creates new admin account from GlobalSettings->Account management page of XIQ
        
        - Keyword Usage:
        -   Robot:
        -      Library  keywords/gui/passwordreset/KeywordsPasswordReset.py
        -      Add Account
        -   Pytest:
        -      Imports:
        -         from keywords.gui.passwordreset.KeywordsPasswordReset import KeywordsPasswordReset
        -      Calling Keyword:
        -         password_reset = KeywordsPasswordReset()
        -         password_reset.add_account()
        -
        - Keyword Implementations:
        -    GUI
        -    XAPI - ** Not Implemented **

        :param name: Name of the new account
        :param _email: email id of the new account
        :return: Returns 1 if success, -1 if not success.
        """
        keyword_name = inspect.stack()[0][3]
        self.keyword_utils.implementations.set_keyword_uuid("a37847d8-f304-11ed-a05b-0242ac120003", keyword_name)
        self.keyword_utils.implementations.gui_implemented(keyword_name, prefer_gui=True)
        
        # Assume a window hasn't been opened 
        return_code = -1
        
        # Call the helper function that implements this keyword
        try:
            implementation_to_run = \
                self.keyword_utils.implementations.select_keyword_implementation(keyword_name, **kwargs)
            if implementation_to_run != '':
                self.keyword_utils.timing.start(keyword_name, 'GUI')
                if implementation_to_run == "GUI":
                    return_code = self.password_reset.gui_add_account(name, _email, **kwargs)
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

    def get_link(self, _email, _password, **kwargs):
        """
        Get the URL link for password set to new account sent to email

        Get the URL link to set password for the new account
        
        - Keyword Usage:
        -   Robot:
        -      Library  keywords/gui/passwordreset/KeywordsPasswordReset.py
        -      Get Link
        -   Pytest:
        -      Imports:
        -         from keywords.gui.passwordreset.KeywordsPasswordReset import KeywordsPasswordReset
        -      Calling Keyword:
        -         password_reset = KeywordsPasswordReset()
        -         password_reset.get_link()
        -
        - Keyword Implementations:
        -    GUI
        -    XAPI - ** Not Supported **

        :param _email: email id to get the link
        :param _password: password to set for new account
        :return: Returns 1 if success, -1 if not success.
        """
        keyword_name = inspect.stack()[0][3]
        self.keyword_utils.implementations.set_keyword_uuid("15dca458-f310-11ed-a05b-0242ac120003", keyword_name)
        self.keyword_utils.implementations.gui_implemented(keyword_name)
        
        # Assume a window hasn't been opened 
        return_code = -1
        
        # Call the helper function that implements this keyword
        try:
            implementation_to_run = \
                self.keyword_utils.implementations.select_keyword_implementation(keyword_name, **kwargs)
            if implementation_to_run != '':
                self.keyword_utils.timing.start(keyword_name, 'GUI')
                if implementation_to_run == "GUI":
                    return_code = self.password_reset.gui_get_link(_email, _password)
                else:
                    return_code = self.keyword_utils.implementations.not_supported(**kwargs)
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
        
    