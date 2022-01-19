from common.WebElementHandler import *
from xiq.defs.IPFirewallPoliciesDefinitions import *


class GlobalSearchWebElements(IPFirewallPoliciesDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_ip_firewall_policy_button(self):
        return self.weh.get_element(self.ip_firewall_policy_button)

    def get_ip_firewall_policy_add(self):
        return self.weh.get_element(self.ip_firewall_policy_add)

    def get_ip_firewall_policy_edit(self):
        return self.weh.get_element(self.ip_firewall_policy_edit)

    def get_ip_firewall_policy_clone(self):
        return self.weh.get_element(self.ip_firewall_policy_clone)

    def get_ip_firewall_policy_delete(self):
        return self.weh.get_element(self.ip_firewall_policy_delete)

    def get_ip_firewall_policy_row(self):
        return self.weh.get_elements(self.ip_firewall_policy_row)

    def get_ip_firewall_policy_add_name(self):
        return self.weh.get_element(self.ip_firewall_policy_add_name)

    def get_ip_firewall_policy_add_desc(self):
        return self.weh.get_element(self.ip_firewall_policy_add_desc)

    def get_ip_firewall_policy_add_add_button(self):
        return self.weh.get_element(self.ip_firewall_policy_add_add_button)

    def get_ip_firewall_policy_add_edit_button(self):
        return self.weh.get_element(self.ip_firewall_policy_add_edit_button)

    def get_ip_firewall_policy_add_delete_button(self):
        return self.weh.get_element(self.ip_firewall_policy_add_delete_button)

    def get_ip_firewall_policy_add_service(self):
        return self.weh.get_element(self.ip_firewall_policy_add_service)

    def get_ip_firewall_policy_add_source_ip_input(self):
        return self.weh.get_element(self.ip_firewall_policy_add_source_ip_input)

    def get_ip_firewall_policy_add_source_ip_select(self):
        return self.weh.get_element(self.ip_firewall_policy_add_source_ip_select)

    def get_ip_firewall_policy_add_source_ip_sel_lst(self):
        return self.weh.get_elements(self.ip_firewall_policy_add_source_ip_sel_lst)

    def get_ip_firewall_policy_add_source_ip_add(self):
        return self.weh.get_element(self.ip_firewall_policy_add_source_ip_add)

    def get_ip_firewall_policy_add_source_ip_add_lst(self):
        return self.weh.get_elements(self.ip_firewall_policy_add_source_ip_add_lst)

    def get_ip_firewall_policy_add_source_ip_edit(self):
        return self.weh.get_element(self.ip_firewall_policy_add_source_ip_edit)

    def get_ip_firewall_policy_add_dest_ip_input(self):
        return self.weh.get_element(self.ip_firewall_policy_add_dest_ip_input)

    def get_ip_firewall_policy_add_dest_ip_select(self):
        return self.weh.get_element(self.ip_firewall_policy_add_dest_ip_select)

    def get_ip_firewall_policy_add_dest_ip_sel_lst(self):
        return self.weh.get_elements(self.ip_firewall_policy_add_dest_ip_sel_lst)

    def get_ip_firewall_policy_add_dest_ip_add(self):
        return self.weh.get_element(self.ip_firewall_policy_add_dest_ip_add)

    def get_ip_firewall_policy_add_dest_ip_add_lst(self):
        return self.weh.get_elements(self.ip_firewall_policy_add_dest_ip_add_lst)

    def get_ip_firewall_policy_add_dest_ip_edit(self):
        return self.weh.get_element(self.ip_firewall_policy_add_dest_ip_edit)

    def get_ip_firewall_policy_add_action(self):
        return self.weh.get_element(self.ip_firewall_policy_add_action)

    def get_ip_firewall_policy_add_action_lst(self):
        return self.weh.get_elements(self.ip_firewall_policy_add_action_lst)

    def get_ip_firewall_policy_add_logging(self):
        return self.weh.get_element(self.ip_firewall_policy_add_logging)

    def get_ip_firewall_policy_add_logging_lst(self):
        return self.weh.get_elements(self.ip_firewall_policy_add_logging_lst)

    def get_ip_firewall_policy_save(self):
        return self.weh.get_element(self.ip_firewall_policy_save)

    def get_ip_firewall_policy_add_service_select(self):
        return self.weh.get_element(self.ip_firewall_policy_add_service_select)

    def get_ip_firewall_policy_add_service_sel_net_searchbox(self):
        return self.weh.get_element(self.ip_firewall_policy_add_service_sel_net_searchbox)

    def get_ip_firewall_policy_add_service_sel_net_cat_list(self):
        return self.weh.get_elements(self.ip_firewall_policy_add_service_sel_net_cat_list)

    def get_ip_firewall_policy_add_service_sel_net_search_btn(self):
        return self.weh.get_element(self.ip_firewall_policy_add_service_sel_net_search_btn)

    def get_ip_firewall_policy_add_service_sel_app_type(self):
        return self.weh.get_element(self.ip_firewall_policy_add_service_sel_app_type)

    def get_ip_firewall_policy_add_service_sel_net_app_lst(self):
        return self.weh.get_elements(self.ip_firewall_policy_add_service_sel_net_app_lst)

    def get_ip_firewall_policy_add_service_sel_app_searchbox(self):
        return self.weh.get_element(self.ip_firewall_policy_add_service_sel_app_searchbox)

    def get_ip_firewall_policy_add_service_sel_app_search_btn(self):
        return self.weh.get_element(self.ip_firewall_policy_add_service_sel_app_search_btn)

    def get_ip_firewall_policy_add_service_sel_app_app_lst(self):
        return self.weh.get_elements(self.ip_firewall_policy_add_service_sel_app_app_lst)

    def get_ip_firewall_policy_add_service_add(self):
        return self.weh.get_element(self.ip_firewall_policy_add_service_add)

    def get_ip_firewall_policy_add_service_add_name(self):
        return self.weh.get_element(self.ip_firewall_policy_add_service_add_name)

    def get_ip_firewall_policy_add_service_add_desc(self):
        return self.weh.get_element(self.ip_firewall_policy_add_service_add_desc)

    def get_ip_firewall_policy_add_service_add_idle_timeout(self):
        return self.weh.get_element(self.ip_firewall_policy_add_service_add_idle_timeout)

    def get_ip_firewall_policy_add_service_add_ip_protocol(self):
        return self.weh.get_element(self.ip_firewall_policy_add_service_add_ip_protocol)

    def get_ip_firewall_policy_add_service_add_ip_proto_lst(self):
        return self.weh.get_elements(self.ip_firewall_policy_add_service_add_ip_proto_lst)

    def get_ip_firewall_policy_add_service_add_port(self):
        return self.weh.get_element(self.ip_firewall_policy_add_service_add_port)

    def get_ip_firewall_policy_add_service_add_alg_type(self):
        return self.weh.get_element(self.ip_firewall_policy_add_service_add_alg_type)

    def get_ip_firewall_policy_add_service_add_alg_type_lst(self):
        return self.weh.get_elements(self.ip_firewall_policy_add_service_add_alg_type_lst)
