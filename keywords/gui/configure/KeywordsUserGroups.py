# Standard Keyword imports
from extauto.common.CommonValidation import CommonValidation
from extauto.common.KeywordUtils import KeywordUtils
import inspect
from tools.xapi.XapiHelper import XapiHelper
from ExtremeAutomation.Library.Utils.Singleton import Singleton

# Keyword imports required to run keywords implemented in this file
from extauto.xiq.flows.configure.UserGroups import UserGroups


class KeywordsUserGroups(object, metaclass=Singleton):
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
        self.user_groups = UserGroups()

    def create_user_group(self, group_name='Demo', user_group_profile=None, **kwargs):
        """
        Create User Groups and add users to user Groups
        This keyword creates the user group and bulk users
        Flow: Configure --> Users --> User Groups
        Example:
        Create User Group   group_name=${GROUP_NAME}   user_group_profile=&{USER_GROUP_PROFILE}
        for supported combination of  &{USER_GROUP_PROFILE} creation refer  "user_group_config.robot"

        - Keyword Usage:
        -   Robot:
        -      Library  keywords/gui/configure/KeywordsUserGroups.py
        -
        -   Pytest:
        -      Imports:
        -         from keywords.gui.configure.KeywordsUserGroups import KeywordsUserGroups
        -      Calling Keyword:
        -         keywords_user_groups = KeywordsUserGroups()
        -         keywords_user_groups.create_user_group(group_name='Demo', user_group_profile=None)
        -
        - Keyword Implementations:
        -    GUI

        Supported Modes:
            GUI  - default mode
            XAPI - not implemented

        :param group_name: Name of the user group
        :param user_group_profile: (dict)  configuration parameter
        :return: 1 if created else -1
        """

        keyword_name = inspect.stack()[0][3]
        self.keyword_utils.implementations.set_keyword_uuid("ef46558b-9116-418d-b083-b5154441055b", keyword_name)
        self.keyword_utils.implementations.gui_implemented(keyword_name)

        # The value returned will be based on which implementations we run.  We'll return -1 if we fail to create
        # user groups to any implementations.  We'll return 1 if there is no error raised in any of the implementations.
        return_code = -1

        try:
            implementation_to_run = self.keyword_utils.implementations.select_keyword_implementation(keyword_name,
                                                                                                     **kwargs)
            if implementation_to_run != '':
                self.keyword_utils.timing.start(keyword_name, 'GUI')
                if implementation_to_run == "GUI":
                    return_code = self.user_groups.gui_create_user_group(group_name, user_group_profile, **kwargs)
                else:
                    kwargs['fail_msg'] = f"Keyword: {keyword_name} has not been implemented for XAPI"
                    self.common_validation.fault(**kwargs)
        except Exception as e:
            kwargs['fail_msg'] = f"Error raised for keyword [{keyword_name}] Error: {e}"
            self.common_validation.fault(**kwargs)
        finally:
            self.keyword_utils.timing.end(keyword_name)

        # Return an error if any of the create user group failed
        return -1 if (return_code == -1) else 1
