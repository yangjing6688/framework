"""
Base class for all snmp commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.CliBaseApi import CliBaseApi


class SnmpBase(CliBaseApi):
    def __init__(self, device):
        super(SnmpBase, self).__init__()
        self.device = device

    def create_all_trap_server(self, *args, **kwargs):
        return self.base_function()

    def delete_trap_servers(self, *args, **kwargs):
        return self.base_function()

    def create_readonly_community(self, *args, **kwargs):
        return self.base_function()

    def create_readwrite_community(self, *args, **kwargs):
        return self.base_function()

    def delete_community(self, *args, **kwargs):
        return self.base_function()

    def delete_user(self, *args, **kwargs):
        return self.base_function()

    def set_user_no_authentication(self, *args, **kwargs):
        return self.base_function()

    def set_user_authentication(self, *args, **kwargs):
        return self.base_function()

    def set_user_privacy(self, *args, **kwargs):
        return self.base_function()

    def set_user_no_authentication_engine_id(self, *args, **kwargs):
        return self.base_function()

    def set_user_authentication_engine_id(self, *args, **kwargs):
        return self.base_function()

    def set_user_privacy_engine_id(self, *args, **kwargs):
        return self.base_function()

    def enable_access_global(self, *args, **kwargs):
        return self.base_function()

    def disable_access_global(self, *args, **kwargs):
        return self.base_function()

    def show_vr(self, *args, **kwargs):
        return self.base_function()

    def set_trap_param(self, *args, **kwargs):
        return self.base_function()

    def clear_trap_param(self, *args, **kwargs):
        return self.base_function()

    def set_notify(self, *args, **kwargs):
        return self.base_function()

    def clear_notify(self, *args, **kwargs):
        return self.base_function()

    def enable_authentication_trap(self, *args, **kwargs):
        return self.base_function()

    def disable_authentication_trap(self, *args, **kwargs):
        return self.base_function()

    def enable_same_snmp_and_ip_sender_flag(self, *args, **kwargs):
        return self.base_function()

    def disable_same_snmp_and_ip_sender_flag(self, *args, **kwargs):
        return self.base_function()

    def enable_same_snmp_trap_sender_ip(self, *args, **kwargs):
        return self.base_function()

    def disable_same_snmp_trap_sender_ip(self, *args, **kwargs):
        return self.base_function()

    def create_v1_trap_server(self, *args, **kwargs):
        return self.base_function()

    def delete_v1_trap_server(self, *args, **kwargs):
        return self.base_function()

    def create_v2c_trap_server(self, *args, **kwargs):
        return self.base_function()

    def delete_v2c_trap_server(self, *args, **kwargs):
        return self.base_function()

    def create_v2c_inform_server(self, *args, **kwargs):
        return self.base_function()

    def delete_v2c_inform_server(self, *args, **kwargs):
        return self.base_function()

    def create_v3_trap_server(self, *args, **kwargs):
        return self.base_function()

    def delete_v3_trap_server(self, *args, **kwargs):
        return self.base_function()

    def create_v3_inform_server(self, *args, **kwargs):
        return self.base_function()

    def delete_v3_inform_server(self, *args, **kwargs):
        return self.base_function()

    def set_notify_filter(self, *args, **kwargs):
        return self.base_function()

    def clear_notify_filter(self, *args, **kwargs):
        return self.base_function()

    def delete_user_engine_id(self, *args, **kwargs):
        return self.base_function()

    def create_group_and_access(self, *args, **kwargs):
        return self.base_function()

    def delete_group_and_access(self, *args, **kwargs):
        return self.base_function()

    def create_view(self, *args, **kwargs):
        return self.base_function()

    def delete_view(self, *args, **kwargs):
        return self.base_function()

    def show_globals(self, *args, **kwargs):
        return self.base_function()

    def show_community(self, *args, **kwargs):
        return self.base_function()

    def show_context(self, *args, **kwargs):
        return self.base_function()

    def show_group(self, *args, **kwargs):
        return self.base_function()

    def show_access(self, *args, **kwargs):
        return self.base_function()

    def show_host(self, *args, **kwargs):
        return self.base_function()

    def show_notify_filter(self, *args, **kwargs):
        return self.base_function()

    def show_user(self, *args, **kwargs):
        return self.base_function()

    def show_view(self, *args, **kwargs):
        return self.base_function()
