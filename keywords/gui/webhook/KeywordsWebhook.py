from time import sleep
# Standard Keyword imports
from extauto.common.CommonValidation import CommonValidation
from extauto.common.KeywordUtils import KeywordUtils
import inspect
from tools.xapi.XapiHelper import XapiHelper
from extauto.xiq.xapi.globalsettings.XapiGlobalSettings import XapiGlobalSettings
from ExtremeAutomation.Library.Utils.Singleton import Singleton
from extauto.xiq.elements.WebhookWebElements import WebhookWebElements
from extauto.xiq.flows.globalsettings.Webhook import Webhook


class KeywordsWebhook(WebhookWebElements, metaclass=Singleton):
    def __init__(self):
        # This is a singleton, avoid initializing for each instance
        if hasattr(self, 'initialized'):
            return
        self.initialized = True
        super().__init__()

        self.common_validation = CommonValidation()
        self.keyword_utils = KeywordUtils()
        self.xapi_helper = XapiHelper()
        self.webhook = Webhook()

    def create_webhook(self, webhook, **kwargs):
        """
        - check create webhook works
        - Keyword Usage
        - ``Create Webhook  ${webhook}``

        :return: returns 1 if successfully create webhook else -1
        """
        keyword_name = inspect.stack()[0][3]
        self.keyword_utils.implementations.set_keyword_uuid("b2e4e076-f612-11ed-b67e-0242ac120002", keyword_name)
        self.keyword_utils.implementations.gui_implemented(keyword_name, prefer_gui=True)
        # Assume Failure
        return_code = -1
        # Call the helper function that implements this keyword
        try:
            implementation_to_run = self.keyword_utils.implementations.select_keyword_implementation(keyword_name,
                                                                                                     **kwargs)
            if implementation_to_run != '':
                self.keyword_utils.timing.start(keyword_name, implementation_to_run)
                if implementation_to_run == "GUI":
                    return_code = self.webhook.gui_create_webhook(webhook, **kwargs)
                else:
                    # XAPI is not implemented
                    kwargs['fail_msg'] = f"XAPI is not implemented for the keyword: [{keyword_name}]"
                    self.common_validation.fault(**kwargs)
        except Exception as e:
            kwargs['fail_msg'] = f"Error raised for keyword [{keyword_name}] Error: {e}"
            self.common_validation.fault(**kwargs)
        finally:
            self.keyword_utils.timing.end(keyword_name)

        return return_code

    def edit_webhook(self,webhook1,webhook2, **kwargs):
        """
        - check edit webhook works
        - Keyword Usage
        - ``Edit Webhook  ${webhook}``

        :return: returns 1 if successfully edit webhook else -1
        """
        keyword_name = inspect.stack()[0][3]
        self.keyword_utils.implementations.set_keyword_uuid("b2e4e404-f612-11ed-b67e-0242ac120002", keyword_name)
        self.keyword_utils.implementations.gui_implemented(keyword_name, prefer_gui=True)
        # Assume Failure
        return_code = -1
        # Call the helper function that implements this keyword
        try:
            implementation_to_run = self.keyword_utils.implementations.select_keyword_implementation(keyword_name,
                                                                                                     **kwargs)
            if implementation_to_run != '':
                self.keyword_utils.timing.start(keyword_name, implementation_to_run)
                if implementation_to_run == "GUI":
                    return_code = self.webhook.gui_edit_webhook(webhook1, webhook2, **kwargs)
                else:
                    # XAPI is not implemented
                    kwargs['fail_msg'] = f"XAPI is not implemented for the keyword: [{keyword_name}]"
                    self.common_validation.fault(**kwargs)
        except Exception as e:
            kwargs['fail_msg'] = f"Error raised for keyword [{keyword_name}] Error: {e}"
            self.common_validation.fault(**kwargs)
        finally:
            self.keyword_utils.timing.end(keyword_name)

        return return_code

    def delete_webhook(self,webhook, **kwargs):
        """
        - check delete webhook works
        - Keyword Usage
        - ``Delete Webhook  ${webhook}``

        :return: returns 1 if successfully delete webhook else -1
        """
        keyword_name = inspect.stack()[0][3]
        self.keyword_utils.implementations.set_keyword_uuid("b2e4e53a-f612-11ed-b67e-0242ac120002", keyword_name)
        self.keyword_utils.implementations.gui_implemented(keyword_name, prefer_gui=True)
        # Assume Failure
        return_code = -1
        # Call the helper function that implements this keyword
        try:
            implementation_to_run = self.keyword_utils.implementations.select_keyword_implementation(keyword_name,
                                                                                                     **kwargs)
            if implementation_to_run != '':
                self.keyword_utils.timing.start(keyword_name, implementation_to_run)
                if implementation_to_run == "GUI":
                    return_code = self.webhook.gui_delete_webhook(webhook, **kwargs)
                else:
                    # XAPI is not implemented
                    kwargs['fail_msg'] = f"XAPI is not implemented for the keyword: [{keyword_name}]"
                    self.common_validation.fault(**kwargs)
        except Exception as e:
            kwargs['fail_msg'] = f"Error raised for keyword [{keyword_name}] Error: {e}"
            self.common_validation.fault(**kwargs)
        finally:
            self.keyword_utils.timing.end(keyword_name)

        return return_code
