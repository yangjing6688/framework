from extauto.xiq.defs.GuestAccessNetworkWebElementsDefinitions import *
from extauto.common.WebElementHandler import WebElementHandler


class GuestAccessNetworkWebElements(GuestAccessNetworkWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    @staticmethod
    def get_displayed_element(elements):
        """

        :param elements:
        :return:
        """
        for el in elements:
            if el.is_displayed():
                return el

    def get_wireless_nw_add_button(self):
        return self.weh.get_element(self.wireless_nw_add_button)

    def get_guest_access_network_save_button(self):
        elements = self.weh.get_elements(self.guest_access_network_save_button)
        return self.get_displayed_element(elements)

    def get_guest_access_network_close_button(self):
        elements = self.weh.get_elements(self.guest_access_network_close_button)
        return self.get_displayed_element(elements)

    def get_guest_network_go_to_deploy_button(self):
        els = self.weh.get_elements(self.guest_network_go_to_deploy_button)
        return self.get_displayed_element(els)

    def get_guest_access_nw_menu_item(self):
        return self.weh.get_element(self.guest_access_nw_menu_item)

    def get_ssid_name_field(self):
        elements = self.weh.get_elements(self.ssid_name_field)
        return self.get_displayed_element(elements)

    def get_ssid_broadcost_name_field(self):
        elements = self.weh.get_elements(self.ssid_broadcost_name_field)
        return self.get_displayed_element(elements)

    def get_unsecured_network_radio_button(self):
        return self.weh.get_element(self.unsecured_network_radio_button)

    def get_guest_access_nw_without_login_radio_button(self):
        return self.weh.get_element(self.guest_access_nw_without_login_radio_button)

    def get_guest_access_usr_policy_bf_accessing_nw(self):
        return self.weh.get_element(self.guest_access_usr_policy_bf_accessing_nw)

    def get_customized_cwp(self):
        return self.weh.get_element(self.customized_cwp)

    def get_cwp_name_field(self):
        els = self.weh.get_elements(self.cwp_name_field)
        return self.get_displayed_element(els)

    def get_user_policy_acceptance_slide_bar(self):
        els = self.weh.get_elements(self.user_policy_acceptance_slide_bar)
        return self.get_displayed_element(els)

    def get_success_page_slide_bar(self):
        els = self.weh.get_elements(self.success_page_slide_bar)
        return self.get_displayed_element(els)

    def get_cwp_landing_page_side_bar(self):
        els = self.weh.get_elements(self.cwp_landing_page_side_bar)
        return self.get_displayed_element(els)

    def get_cwp_done_button(self):
        els = self.weh.get_elements(self.cwp_done_button)
        return self.get_displayed_element(els)

    def get_guest_self_register_sign_in_radio_button(self):
        return self.weh.get_element(self.guest_self_register_sign_in_radio_button)

    def get_user_group_drop_down(self):
        els = self.weh.get_elements(self.user_group_drop_down)
        return self.get_displayed_element(els)

    def get_user_group_create(self):
        els = self.weh.get_elements(self.user_group_create)
        return self.get_displayed_element(els)

    def get_user_group_name(self):
        els = self.weh.get_elements(self.user_group_name)
        return self.get_displayed_element(els)

    def get_user_group_save_button(self):
        els = self.weh.get_elements(self.user_group_save_button)
        return self.get_displayed_element(els)

    def get_add_employee_approval_button(self):
        els = self.weh.get_elements(self.add_employee_approval_button)
        return self.get_displayed_element(els)

    def get_domain_name(self):
        return self.weh.get_element(self.domain_name)

    def get_domain_name_add_button(self):
        els = self.weh.get_elements(self.domain_name_add_button)
        return self.get_displayed_element(els)

    def get_employee_approval_domain_name_done_button(self):
        els = self.weh.get_elements(self.employee_approval_domain_name_done_button)
        return self.get_displayed_element(els)

    def get_secured_network_radio_button(self):
        return self.weh.get_element(self.secured_network_radio_button)

    def get_create_guest_credentials_to_login_nw(self):
        return self.weh.get_element(self.create_guest_credentials_to_login_nw)

    def get_guests_self_reg_sign_in_employee_approve(self):
        return self.weh.get_element(self.guests_self_reg_sign_in_employee_approve)

    def get_global_passwd_cred_for_guest_to_login(self):
        return self.weh.get_element(self.global_passwd_cred_for_guest_to_login)

    def get_max_num_clients_per_ppsk(self):
        return self.weh.get_element(self.max_num_clients_per_ppsk)

    def get_max_clients_per_ppsk(self):
        return self.weh.get_element(self.max_clients_per_ppsk)

    def get_mac_binding_num_per_ppsk(self):
        return self.weh.get_element(self.mac_binding_num_per_ppsk)

    def get_mac_binding_number(self):
        return self.weh.get_element(self.mac_binding_number)

    def get_auth_db_drop_down(self):
        return self.weh.get_element(self.auth_db_drop_down)

    def get_bulk_user_prefix(self):
        return self.weh.get_element(self.bulk_user_prefix)

    def get_bulk_guest_count(self):
        return self.weh.get_element(self.bulk_guest_count)

    def get_guest_self_registration_ssid(self):
        return self.weh.get_element(self.guest_self_registration_ssid)

    def get_enable_cwp_check_box(self):
        return self.weh.get_element(self.enable_cwp_check_box)

    def get_psk_password(self):
        return self.weh.get_element(self.psk_password)
