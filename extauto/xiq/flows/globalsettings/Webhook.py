from time import sleep
from extauto.common.Screen import Screen
from extauto.common.Utils import Utils
from extauto.common.AutoActions import AutoActions
from extauto.xiq.flows.common.Navigator import Navigator
from extauto.xiq.elements.WebhookWebElements import WebhookWebElements
from extauto.common.CommonValidation import CommonValidation
from ExtremeAutomation.Library.Utils.Singleton import Singleton
from ExtremeAutomation.Utilities.deprecated import deprecated

class Webhook(WebhookWebElements, metaclass=Singleton):
    def __init__(self):
        # This is a singleton, avoid initializing for each instance
        if hasattr(self, 'initialized'):
            return
        self.initialized = True
        super().__init__()
        self.navigator = Navigator()
        self.screen = Screen()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.common_validation = CommonValidation()

    @deprecated('Please use the {create_webhook} keyword in keywords/gui/webhook/KeywordsWebhook.py'
                'This method can be removed after 7/1/2023')
    def create_webhook(self, webhook, **kwargs):
        return self.gui_create_webhook(webhook, **kwargs)

    def gui_create_webhook(self, webhook, **kwargs):
        """
        - check create webhook works
        - Keyword Usage
        - ``Create Webhook  ${webhook}``

        :return: returns 1 if successfully create webhook else -1
        """
        self.utils.print_info("Opening webhook dialog for create")
        self.auto_actions.click_reference(self.get_webhook_add_btn)
        sleep(2)
        self._webhook_dialog_input(webhook)
        self.auto_actions.click_reference(self.get_webhook_save_btn)
        sleep(2)
        self.screen.save_screen_shot()
        return self._find_url_in_webhook_grid(webhook, **kwargs)

    @deprecated('Please use the {edit_webhook} keyword in keywords/gui/webhook/KeywordsWebhook.py'
                'This method can be removed after 7/1/2023')
    def edit_webhook(self, webhook1, webhook2, **kwargs):
        return self.gui_edit_webhook(webhook1, webhook2, **kwargs)

    def gui_edit_webhook(self, webhook1, webhook2, **kwargs):
        """
        - check edit webhook works
        - Keyword Usage
        - ``Edit Webhook  ${webhook}``

        :return: returns 1 if successfully edit webhook else -1
        """
        self.utils.print_info("Searching webhook url:"+webhook1.url)
        if self._find_url_in_webhook_grid(webhook1) == 1:
            self.utils.print_info("Opening webhook dialog for edit")
            self.auto_actions.click_reference(self.get_webhook_edit_btn)
            sleep(2)
            self._webhook_dialog_input(webhook2)
            self.auto_actions.click_reference(self.get_webhook_save_btn)
            sleep(2)
            self.screen.save_screen_shot()
            return self._find_url_in_webhook_grid(webhook2)
        else:
            kwargs['fail_msg'] = "Unable to edit webhook"
            self.common_validation.fault(**kwargs)
            return -1

    def _webhook_dialog_input(self, webhook):
        self.utils.print_info("Inputing webhook - start")
        self.utils.print_info("Inputing webhook post url:"+webhook.url)
        self.auto_actions.send_keys(self.get_webhook_url_input(), webhook.url)
        self.utils.print_info("Inputing webhook access token:"+webhook.secret)
        self.auto_actions.send_keys(self.get_webhook_secret_input(), webhook.secret)
        self.utils.print_info("Inputing webhook description:"+webhook.description)
        self.auto_actions.send_keys(self.get_webhook_description_input(), webhook.description)
        if webhook.sendme:
            self.auto_actions.click_reference(self.get_webhook_sendme_radio)
        else:
            self.auto_actions.click_reference(self.get_webhook_bind_radio)
            bind_item_eles = self.get_webhook_bind_items()
            if bind_item_eles:
                for item in webhook.bind_items:
                    for item_ele in bind_item_eles:
                        if item_ele.text == item:
                            self.auto_actions.click(item_ele)
        if webhook.enable:
            self.auto_actions.enable_check_box(self.get_webhook_enable_check())
        else:
            self.auto_actions.disable_check_box(self.get_webhook_enable_check())
        self.screen.save_screen_shot()
        self.utils.print_info("Inputing webhook - end")

    def _find_url_in_webhook_grid(self, webhook, **kwargs):
        """
        - find one webhook url if it in the grid
        - if it can be found also click on it(select the one)
        - Keyword Usage
        - ``Find Url In Webhook Grid  ${webhook}``

        :return: returns 1 if successfully find the url else -1
        """
        webhook_rows = self.get_webhook_grid_rows()
        for row in webhook_rows:
            cells = self.get_webhook_grid_row_cells(row)
            if cells[1].text == webhook.url:
                self.utils.print_info("Searching webhook url(success):"+webhook.url)
                self.auto_actions.click(cells[1])
                kwargs['pass_msg'] = "Successfully searching webhook url"
                self.common_validation.passed(**kwargs)
                return 1
        kwargs['fail_msg'] = f"Unable to find webhook url: {webhook.url}"
        #self.common_validation.fault(**kwargs)
        return -1

    @deprecated('Please use the {delete_webhook} keyword in keywords/gui/webhook/KeywordsWebhook.py'
                'This method can be removed after 7/1/2023')
    def delete_webhook(self, webhook, **kwargs):
        return self.gui_delete_webhook(webhook, **kwargs)

    def gui_delete_webhook(self, webhook, **kwargs):
        """
        - check delete webhook works
        - Keyword Usage
        - ``Delete Webhook  ${webhook}``

        :return: returns 1 if successfully delete webhook else -1
        """
        sleep(2)
        self.utils.print_info("Searching webhook url:"+webhook.url)
        if self._find_url_in_webhook_grid(webhook) == 1:
            self.auto_actions.click_reference(self.get_webhook_del_btn)
            sleep(2)
            self.auto_actions.click_reference(self.get_confirm_yes_btn)
            sleep(2)
            if self._find_url_in_webhook_grid(webhook) == -1:
                kwargs['pass_msg'] = f"Successfully delete webhook url: {webhook.url}"
                self.common_validation.passed(**kwargs)
                return 1
            else:
                kwargs['fail_msg'] = f"Unable to delete webhook url: {webhook.url}"
                self.common_validation.failed(**kwargs)
                return -1
        else:
            kwargs['fail_msg'] = f"Failed to delete webhook url: {webhook.url}"
            self.common_validation.fault(**kwargs)
            return -1
