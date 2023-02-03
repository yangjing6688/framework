from extauto.xiq.defs.WebhookDefs import WebhookDefs
from extauto.common.WebElementHandler import WebElementHandler


class WebhookWebElements(WebhookDefs):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_webhook_add_btn(self):
        return self.weh.get_element(self.webhook_add_btn)
    def get_webhook_edit_btn(self):
        return self.weh.get_element(self.webhook_edit_btn)
    def get_webhook_del_btn(self):
        return self.weh.get_element(self.webhook_del_btn)
    def get_webhook_grid_rows(self):
        return self.weh.get_elements(self.webhook_grid_rows)
    def get_webhook_grid_row_cells(self, row):
        return self.weh.get_elements(self.webhook_grid_row_cells, row)
    def get_confirm_yes_btn(self):
        return self.weh.get_element(self.confirm_yes_btn)
    def get_webhook_url_input(self):
        return self.weh.get_element(self.webhook_url_input)
    def get_webhook_secret_input(self):
        return self.weh.get_element(self.webhook_secret_input)
    def get_webhook_description_input(self):
        return self.weh.get_element(self.webhook_description_input)
    def get_webhook_sendme_radio(self):
        return self.weh.get_element(self.webhook_sendme_radio)
    def get_webhook_bind_radio(self):
        return self.weh.get_element(self.webhook_bind_radio)
    def get_webhook_bind_items(self):
        return self.weh.get_elements(self.webhook_bind_items)
    def get_webhook_enable_check(self):
        return self.weh.get_element(self.webhook_enable_check)
    def get_webhook_save_btn(self):
        return self.weh.get_element(self.webhook_save_btn)
    def get_wwebhook_cancel_btn(self):
        return self.weh.get_element(self.webhook_cancel_btn)