from extauto.common.CommonValidation import CommonValidation
from extauto.common.KeywordUtils import KeywordUtils
from tools.xapi.XapiHelper import XapiHelper
import inspect
from ExtremeAutomation.Library.Utils.Singleton import Singleton
from extauto.xiq.flows.globalsettings.AccountManagement import AccountManagement
from extauto.xiq.elements.AccntMgmtWebElements import AccntMgmtWebElements


class KeywordsAccountManagement(AccntMgmtWebElements, metaclass=Singleton):
    def __init__(self):
        if hasattr(self, 'initialized'):
            return
        self.initialized = True
        super().__init__()
        # Objects used by all keywords
        self.common_validation = CommonValidation()
        self.keyword_utils = KeywordUtils()
        self.xapi_helper = XapiHelper()

        self.account_mgmt = AccountManagement()

    def create_role_based_account(self, account_config, **kwargs):
        """
        Creates a new account under account management

        This method creates a new account and will configure the role for the account
        For example:
            &{OPERATOR_ROLE} or &{MONITOR_ROLE} or &{HELPDESK_ROLE} or &{Guest_Management_Role}or &{Observer_Role}
        Keyword Usage:
            Robot:
                Library  keywords/gui/account_management/KeywordsAccountManagement.py
                Create Role Based Account   ${GUEST_MANAGEMENT_ROLE}
            Pytest:
                Imports:
                    from keywords.gui.account_management.KeywordsAccountManagement import KeywordsAccountManagement
                Calling Keyword:
                    account_mgmt = KeywordsAccountManagement()
                    account_mgmt.create_role_based_account(accnt_config, **kwargs)

        Keyword Implementations:
            GUI
            XAPI - ** Not Implemented **

        :param account_config: Name of the new account
        :return: Returns 1 if success, -1 if not success.
        """

        keyword_name = inspect.stack()[0][3]
        self.keyword_utils.implementations.set_keyword_uuid("32e34132-f94c-11ed-be56-0242ac120002", keyword_name)
        self.keyword_utils.implementations.gui_implemented(keyword_name, prefer_gui=True)

        # Assume Failure
        return_code = -1

        # Call the helper function that implements this keyword
        try:
            implementation_to_run = \
                self.keyword_utils.implementations.select_keyword_implementation(keyword_name, **kwargs)
            if implementation_to_run != '':
                self.keyword_utils.timing.start(keyword_name, 'GUI')
                if implementation_to_run == "GUI":
                    return_code = self.account_mgmt.gui_create_role_based_account(account_config, **kwargs)
                else:
                    # XAPI is not implemented
                    kwargs['fail_msg'] = f"XAPI is not implemented for the keyword: [{keyword_name}]"
                    self.common_validation.fault(**kwargs)
        except Exception as e:
            kwargs['fail_msg'] = f"Error raised for keyword [{keyword_name}] Error: {e}"
            self.common_validation.fault(**kwargs)
        finally:
            self.keyword_utils.timing.end(keyword_name)

        # Return the return value of the keyword
        return return_code

    def delete_management_account(self, email_addr, **kwargs):
        """
        Deletes a management account

        This method will delete a management account from Account Management tab

        Keyword Usage:
            Robot:
                Library  keywords/gui/account_management/KeywordsAccountManagement.py
                Delete Management Account       ${TENANT_EMAIL_ID}
            Pytest:
                Imports:
                    from keywords.gui.account_management.KeywordsAccountManagement import KeywordsAccountManagement
                Calling Keyword:
                    account_mgmt = KeywordsAccountManagement()
                    account_mgmt.delete_management_account(email_addr, **kwargs)

        Keyword Implementations:
            GUI
            XAPI - ** Not Implemented **

        :param email_addr: Email id of the management account
        :return: Returns 1 if success, -1 if not success.
        """
        keyword_name = inspect.stack()[0][3]
        self.keyword_utils.implementations.set_keyword_uuid("32e3457e-f94c-11ed-be56-0242ac120002", keyword_name)
        self.keyword_utils.implementations.gui_implemented(keyword_name, prefer_gui=True)

        # Assume Failure
        return_code = -1

        # Call the helper function that implements this keyword
        try:
            implementation_to_run = \
                self.keyword_utils.implementations.select_keyword_implementation(keyword_name, **kwargs)
            if implementation_to_run != '':
                self.keyword_utils.timing.start(keyword_name, 'GUI')
                if implementation_to_run == "GUI":
                    return_code = self.account_mgmt.gui_delete_management_account(email_addr, **kwargs)
                else:
                    # XAPI is not implemented
                    kwargs['fail_msg'] = f"XAPI is not implemented for the keyword: [{keyword_name}]"
                    self.common_validation.fault(**kwargs)
        except Exception as e:
            kwargs['fail_msg'] = f"Error raised for keyword [{keyword_name}] Error: {e}"
            self.common_validation.fault(**kwargs)
        finally:
            self.keyword_utils.timing.end(keyword_name)

        # Return the return value of the keyword
        return return_code

    def delete_guest_management_accounts(self, **kwargs):
        """
        Deletes guest management accounts

        This method will delete all the guest management account from the list of Account Management tab

        Keyword Usage:
            Robot:
                Library  keywords/gui/account_management/KeywordsAccountManagement.py
                Delete Guest Management Accounts
            Pytest:
                Imports:
                    from keywords.gui.account_management.KeywordsAccountManagement import KeywordsAccountManagement
                Calling Keyword:
                    account_mgmt = KeywordsAccountManagement()
                    account_mgmt.delete_guest_management_accounts(**kwargs)

        Keyword Implementations:
            GUI
            XAPI - ** Not Implemented **

        :param:
        :return: Returns 1 if success, -1 if not success.
        """
        keyword_name = inspect.stack()[0][3]
        self.keyword_utils.implementations.set_keyword_uuid("32e346c8-f94c-11ed-be56-0242ac120002", keyword_name)
        self.keyword_utils.implementations.gui_implemented(keyword_name, prefer_gui=True)

        # Assume Failure
        return_code = -1

        # Call the helper function that implements this keyword
        try:
            implementation_to_run = \
                self.keyword_utils.implementations.select_keyword_implementation(keyword_name, **kwargs)
            if implementation_to_run != '':
                self.keyword_utils.timing.start(keyword_name, 'GUI')
                if implementation_to_run == "GUI":
                    return_code = self.account_mgmt.gui_delete_guest_management_accounts(**kwargs)
                else:
                    # XAPI is not implemented
                    kwargs['fail_msg'] = f"XAPI is not implemented for the keyword: [{keyword_name}]"
                    self.common_validation.fault(**kwargs)
        except Exception as e:
            kwargs['fail_msg'] = f"Error raised for keyword [{keyword_name}] Error: {e}"
            self.common_validation.fault(**kwargs)
        finally:
            self.keyword_utils.timing.end(keyword_name)

        # Return the return value of the keyword
        return return_code

