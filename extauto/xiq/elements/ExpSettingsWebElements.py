from extauto.xiq.defs.ExpSettingsWebElementsDefinitions import *
from extauto.common.WebElementHandler import WebElementHandler


class ExpSettingsWebElements(ExpSettingsWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_account_expiration_drop_down(self):
        return self.weh.get_element(self.account_expiration_drop_down)

    def get_account_expiration_drop_down_options(self):
        return self.weh.get_elements(self.account_expiration_drop_down_options)

    def get_valid_for_time_period_in(self):
        return self.weh.get_element(self.valid_for_time_period_in)

    def get_valid_for_time_period_in_drop_down(self):
        return self.weh.get_element(self.valid_for_time_period_in_drop_down)

    def get_valid_for_time_period_in_drop_down_options(self):
        return self.weh.get_elements(self.valid_for_time_period_in_drop_down_options)

    def get_valid_for_time_period_after_drop_down(self):
        return self.weh.get_element(self.valid_for_time_period_after_drop_down)

    def get_valid_for_time_period_after_drop_down_options(self):
        return self.weh.get_elements(self.valid_for_time_period_after_drop_down_options)

    def get_renew_user_credentials_check_box(self):
        return self.weh.get_element(self.renew_user_credentials_check_box)

    def get_dlt_cred_imm_aft_expiration_check_box(self):
        return self.weh.get_element(self.dlt_cred_imm_aft_expiration_check_box)

    def get_delete_cred_after_check_box(self):
        return self.weh.get_element(self.delete_cred_after_check_box)

    def get_delete_cred_after_input_field(self):
        return self.weh.get_element(self.delete_cred_after_input_field)

    def get_delete_cred_after_drop_down(self):
        return self.weh.get_element(self.delete_cred_after_drop_down)

    def get_delete_cred_after_drop_down_options(self):
        return self.weh.get_elements(self.delete_cred_after_drop_down_options)

    def get_action_at_exp_access_rejected_radio_button(self):
        return self.weh.get_element(self.action_at_exp_access_rejected_radio_button)

    def get_action_at_exp_show_expi_msg_radio_button(self):
        return self.weh.get_element(self.action_at_exp_show_expi_msg_radio_button)

    def get_access_key_must_be_used_within(self):
        return self.weh.get_element(self.access_key_must_be_used_within)

    def get_access_key_must_be_used_within_period_drop_down(self):
        return self.weh.get_element(self.access_key_must_be_used_within_period_drop_down)

    def get_access_key_must_be_used_within_period_optns(self):
        return self.weh.get_elements(self.access_key_must_be_used_within_period_optns)

    def get_req_auth_after_check_box(self):
        return self.weh.get_element(self.req_auth_after_check_box)

    def get_req_auth_after_input_field(self):
        return self.weh.get_element(self.req_auth_after_input_field)