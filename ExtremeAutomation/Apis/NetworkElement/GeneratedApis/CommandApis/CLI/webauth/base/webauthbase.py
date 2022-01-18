"""
Base class for all webauth commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.CliBaseApi import CliBaseApi


class WebauthBase(CliBaseApi):
    def __init__(self, device):
        super(WebauthBase, self).__init__()
        self.device = device

    def enable_global(self, *args, **kwargs):
        return self.base_function()

    def disable_global(self, *args, **kwargs):
        return self.base_function()

    def enable_control_port(self, *args, **kwargs):
        return self.base_function()

    def disable_control_port(self, *args, **kwargs):
        return self.base_function()

    def enable_redirect_page(self, *args, **kwargs):
        return self.base_function()

    def disable_redirect_page(self, *args, **kwargs):
        return self.base_function()

    def enable_logout_page(self, *args, **kwargs):
        return self.base_function()

    def disable_logout_page(self, *args, **kwargs):
        return self.base_function()

    def enable_session_refresh(self, *args, **kwargs):
        return self.base_function()

    def disable_session_refresh(self, *args, **kwargs):
        return self.base_function()

    def enable_reauthentication_on_refresh(self, *args, **kwargs):
        return self.base_function()

    def disable_reauthentication_on_refresh(self, *args, **kwargs):
        return self.base_function()

    def set_hostname(self, *args, **kwargs):
        return self.base_function()

    def set_init_mac_port(self, *args, **kwargs):
        return self.base_function()

    def set_init_port(self, *args, **kwargs):
        return self.base_function()

    def set_init_mac(self, *args, **kwargs):
        return self.base_function()

    def set_init_all(self, *args, **kwargs):
        return self.base_function()

    def set_redirect_page(self, *args, **kwargs):
        return self.base_function()

    def set_session_timeout(self, *args, **kwargs):
        return self.base_function()

    def set_idle_timeout(self, *args, **kwargs):
        return self.base_function()

    def set_lease_time(self, *args, **kwargs):
        return self.base_function()

    def set_session_refresh(self, *args, **kwargs):
        return self.base_function()

    def set_allowed_refresh_failures(self, *args, **kwargs):
        return self.base_function()

    def set_protocol_order(self, *args, **kwargs):
        return self.base_function()

    def set_protocol_order_web_dot1x_mac(self, *args, **kwargs):
        return self.base_function()

    def set_protocol_order_web_mac_dot1x(self, *args, **kwargs):
        return self.base_function()

    def set_db_order_local(self, *args, **kwargs):
        return self.base_function()

    def set_db_order_local_radius(self, *args, **kwargs):
        return self.base_function()

    def set_db_order_radius(self, *args, **kwargs):
        return self.base_function()

    def set_db_order_radius_local(self, *args, **kwargs):
        return self.base_function()

    def clear_hostname(self, *args, **kwargs):
        return self.base_function()

    def clear_redirect_page(self, *args, **kwargs):
        return self.base_function()

    def clear_session_timeout(self, *args, **kwargs):
        return self.base_function()

    def clear_idle_timeout(self, *args, **kwargs):
        return self.base_function()

    def clear_lease_time(self, *args, **kwargs):
        return self.base_function()

    def clear_session_refresh(self, *args, **kwargs):
        return self.base_function()

    def clear_allowed_refresh_failures(self, *args, **kwargs):
        return self.base_function()

    def clear_protocol_order(self, *args, **kwargs):
        return self.base_function()

    def clear_db_order(self, *args, **kwargs):
        return self.base_function()

    def show_summary_snapshot(self, *args, **kwargs):
        return self.base_function()

    def show_port(self, *args, **kwargs):
        return self.base_function()

    def show_timeout_values(self, *args, **kwargs):
        return self.base_function()

    def show_vlan_dhcp_netlogin_lease_time(self, *args, **kwargs):
        return self.base_function()
