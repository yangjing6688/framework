
# Standard Keyword imports
from extauto.common.CommonValidation import CommonValidation
from extauto.common.KeywordUtils import KeywordUtils
import inspect
from tools.xapi.XapiHelper import XapiHelper
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
        Create a new webhook

        This method creates a webhook from GlobalSettings->Webhooks which is under AlertNotifications tab

        - Keyword Usage:
        -   Robot:
        -      Library  keywords/gui/webhook/KeywordsWebhook.py
        -      Create Webhook  ${webhook1}
        -   Pytest:
        -      Imports:
        -         from keywords.gui.webhook.KeywordsWebhook import KeywordsWebhook
        -      Calling Keyword:
        -         webhook = KeywordsWebhook()
        -         webhook.create_webhook(webhook)
        -
        - Keyword Implementations:
        -    GUI
        -    XAPI - ** Not Implemented **

        :param webhook: This parameter accepts webhook.yaml which will have webhook settings.
            For Example the yaml file will have:
                webhook1:
                    url: "https://58l8z.mocklab.io/"
                    secret: ""
                    description: "this is a test webhook can not use it"
                    sendme: true
                    enable: true
        :return: Returns 1 if success, -1 if not success.
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

    def edit_webhook(self, webhook1, webhook2, **kwargs):
        """
        Edits an existing webhook

        This method modifies the configuration of webhook 1  to webhook 2

        - Keyword Usage:
        -   Robot:
        -      Library  keywords/gui/webhook/KeywordsWebhook.py
        -      Edit Webhook  ${webhook1}    ${webhook2}
        -   Pytest:
        -      Imports:
        -         from keywords.gui.webhook.KeywordsWebhook import KeywordsWebhook
        -      Calling Keyword:
        -         webhook = KeywordsWebhook()
        -         webhook.edit_webhook(webhook1, webhook2)
        -
        - Keyword Implementations:
        -    GUI
        -    XAPI - ** Not Implemented **

        :param webhook1: This parameter will have the webhook needs to be modified.
        :param webhook2:  This parameter  will have the new webhook settings
            Both params accepts yaml file.
            For Example the yaml file will have webhook settings as below:
                webhook1:
                    url: "https://58l8z.mocklab.io/"
                    secret: ""
                    description: "this is a test webhook can not use it"
                    sendme: true
                    enable: true
        :return: Returns 1 if success, -1 if not success.
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

    def delete_webhook(self, webhook, **kwargs):
        """
        Deletes an existing webhook

        This method deletes the webhook from the page GlobalSettings->Webhooks which is under AlertNotifications tab

        - Keyword Usage:
        -   Robot:
        -      Library  keywords/gui/webhook/KeywordsWebhook.py
        -      Delete Webhook  ${webhook}
        -   Pytest:
        -      Imports:
        -         from keywords.gui.webhook.KeywordsWebhook import KeywordsWebhook
        -      Calling Keyword:
        -         webhook = KeywordsWebhook()
        -         webhook.delete_webhook(webhook)
        -
        - Keyword Implementations:
        -    GUI
        -    XAPI - ** Not Implemented **

        :param webhook: This parameter accepts webhook.yaml which will have a webhook settings.
        For Example the yaml file will have:
                webhook1:
                    url: "https://58l8z.mocklab.io/"
                    secret: ""
                    description: "this is a test webhook can not use it"
                    sendme: true
                    enable: true
        :return: Returns 1 if success, -1 if not success.
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
