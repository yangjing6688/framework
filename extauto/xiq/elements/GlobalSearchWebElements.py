from extauto.common.WebElementHandler import *
from xiq.defs.GlobalSearchWebElementsDefinitions import *


class GlobalSearchWebElements(GlobalSearchWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_search_icon(self):
        return self.weh.get_element(self.global_search_icon)

    def get_global_search_textbox(self):
        return self.weh.get_element(self.global_search_textbox)

    def get_global_search_result(self):
        return self.weh.get_elements(self.global_search_result)

    def get_system_info(self):
        return self.weh.get_element(self.system_info_button)

    def get_system_info_ap_name(self):
        return self.weh.get_element(self.system_info_ap_name)

    def get_system_info_ap_serial_number(self):
        return self.weh.get_element(self.system_info_ap_serial_number)

    def get_system_info_ap_mac(self):
        return self.weh.get_element(self.system_info_ap_mac)

    def get_close_dialog(self):
        return self.weh.get_element(self.close_dialog)

    def get_application_name(self):
        return self.weh.get_element(self.application_name)

    def get_application_category(self):
        return self.weh.get_element(self.application_category)

    def get_net_policy_sum_view(self):
        return self.weh.get_element(self.net_policy_sum_view)

    def get_net_policy_ssid_title(self):
        return self.weh.get_element(self.net_policy_ssid_title)

    def get_client_title(self):
        return self.weh.get_element(self.client_title)

    def get_client_ip(self):
        return self.weh.get_element(self.client_ip)

    def get_client_mac(self):
        return self.weh.get_element(self.client_mac)

    def get_system_info_ap_ip(self):
        return self.weh.get_element(self.system_info_ap_ip)

    def get_view_organization_button(self):
        return self.weh.get_element(self.view_organizations_button)

    def get_select_all_organizations(self):
        return self.weh.get_element(self.view_org_select)

    def get_view_org_close_button(self):
        return self.weh.get_element(self.view_org_close_button)
