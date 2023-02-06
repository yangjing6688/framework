from extauto.xiq.defs.NPExpressPolicySetupDefinitions import NPExpressPolicySetupDefinitions
from extauto.common.WebElementHandler import WebElementHandler


class NPExpressPolicyWebElements(NPExpressPolicySetupDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_network_policy_card_view(self):
        return self.weh.get_element(self.card_view)

    def get_network_policy_list_from_card_view(self):
        return self.weh.get_elements(self.network_policy_list)

    def get_new_account_express_policy_setup_button(self):
        return self.weh.get_element(self.new_account_express_policy_setup_button)

    def get_express_policy_setup_button(self):
        return self.weh.get_element(self.express_policy_setup_button)

    def get_policy_name_text(self):
        return self.weh.get_element(self.policy_name_text)

    def get_wireless_auth_drop_down(self):
        return self.weh.get_element(self.auth_type_drop_down)

    def get_wireless_auth_select_elements(self):
        return self.weh.get_elements(self.auth_type_drop_down_options)

    def get_wireless_network_toggle_check_box(self):
        return self.weh.get_element(self.network_toggle_checkbox)

    def get_ssid_field(self):
        return self.weh.get_element(self.ssid_name_text_field)

    def get_cwp_toggle_check_box(self):
        return self.weh.get_element(self.cwp_checkbox)

    def get_cwp_name_text_field(self):
        return self.weh.get_element(self.cwp_name_text_field)

    def get_network_policy_create_button(self):
        return self.weh.get_element(self.express_policy_create_button)

    def get_network_policy_dialog_done_button(self):
        return self.weh.get_element(self.express_policy_create_dialog_done_button)

    def get_network_policy_card_items(self):
        return self.weh.get_elements(self.network_policy_card_item)

    def get_network_policy_cancel_button(self):
        return self.weh.get_element(self.express_policy_cancel_button)
