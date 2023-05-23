# Standard Keyword imports
from extauto.common.CommonValidation import CommonValidation
from extauto.common.KeywordUtils import KeywordUtils
import inspect
from tools.xapi.XapiHelper import XapiHelper
from ExtremeAutomation.Library.Utils.Singleton import Singleton
from extauto.xiq.xapi.globalsettings.XapiGlobalSettings import XapiGlobalSettings
# Keyword imports required to run keywords implemented in this file
from extauto.xiq.flows.globalsettings.Communications import Communications


class KeywordsCommunications(object, metaclass=Singleton):
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
        self.communications = None

    def validate_communications_page(self, **kwargs):
        """
        Validate that the communication page is displayed

        This Keyword will navigate to communications menu in Global settings page and then validate that the
        correct page is displayed. If the keyword confirms that the correct page is displayed then it will
        return 1; if not then it will return -1.

        - Keyword Usage:
        -   Robot:
        -      Library  keywords/gui/banner_top/KeywordsCommunications.py
        -      Validate Communications Page
        -   Pytest:
        -      Imports:
        -         from keywords.gui.banner_top.KeywordsCommunications import KeywordsCommunications
        -      Calling Keyword:
        -         keywords_communications = KeywordsCommunications()
        -         keywords_communications.validate_communications_page()
        -
        - Keyword Implementations:
        -    GUI
        -    XAPI - ** Not Supported **

        :return: 1 if the communication page is validated else return -1
        """

        # Notes:
        #   - The work for this keyword is in a separate file
        #   - The amount of time this keyword takes will be recorded and optionally recorded in a database
        #   - This method will catch any errors that are raised and not handled in the keyword
        keyword_name = inspect.stack()[0][3]
        self.keyword_utils.implementations.set_keyword_uuid("340e6eb7-0a79-4964-9fed-b02174e41990", keyword_name)
        self.keyword_utils.implementations.gui_implemented(keyword_name, prefer_gui=True)
        self.keyword_utils.implementations.xapi_implemented(keyword_name)
        # Object used to run keywords implemented in this file
        self.communications = Communications()
        return_code = -1

        # Call the helper function that implements this keyword
        try:
            implementation_to_run = self.keyword_utils.implementations.select_keyword_implementation(keyword_name,
                                                                                                     **kwargs)
            if implementation_to_run != '':
                self.keyword_utils.timing.start(keyword_name, implementation_to_run)
                if implementation_to_run == "GUI":
                    return_code = self.communications.gui_validate_communications_page()
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

        return return_code
