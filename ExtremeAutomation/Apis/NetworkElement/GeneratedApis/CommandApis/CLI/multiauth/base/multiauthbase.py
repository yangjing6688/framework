"""
Base class for all multiauth commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.CliBaseApi import CliBaseApi


class MultiauthBase(CliBaseApi):
    def __init__(self, device):
        super(MultiauthBase, self).__init__()
        self.device = device

    def enable_session_refresh(self, *args, **kwargs):
        return self.base_function()

    def disable_session_refresh(self, *args, **kwargs):
        return self.base_function()

    def set_session_timeout(self, *args, **kwargs):
        return self.base_function()

    def set_session_type_timeout(self, *args, **kwargs):
        return self.base_function()

    def clear_session_type_timeout(self, *args, **kwargs):
        return self.base_function()

    def set_session_refresh(self, *args, **kwargs):
        return self.base_function()

    def clear_session_refresh(self, *args, **kwargs):
        return self.base_function()

    def set_vlan(self, *args, **kwargs):
        return self.base_function()

    def clear_vlan(self, *args, **kwargs):
        return self.base_function()

    def set_idle_timeout(self, *args, **kwargs):
        return self.base_function()

    def set_idle_type_timeout(self, *args, **kwargs):
        return self.base_function()

    def clear_idle_type_timeout(self, *args, **kwargs):
        return self.base_function()

    def set_port_mode(self, *args, **kwargs):
        return self.base_function()

    def set_port_numusers(self, *args, **kwargs):
        return self.base_function()

    def clear_station_mac_port(self, *args, **kwargs):
        return self.base_function()

    def clear_station_port(self, *args, **kwargs):
        return self.base_function()

    def clear_station_mac(self, *args, **kwargs):
        return self.base_function()

    def clear_station_agent(self, *args, **kwargs):
        return self.base_function()

    def show_session_timeout(self, *args, **kwargs):
        return self.base_function()

    def show_idle_timeout(self, *args, **kwargs):
        return self.base_function()

    def show_session(self, *args, **kwargs):
        return self.base_function()

    def show_info(self, *args, **kwargs):
        return self.base_function()

    def show_session_all(self, *args, **kwargs):
        return self.base_function()

    def show_session_mac(self, *args, **kwargs):
        return self.base_function()

    def show_session_port(self, *args, **kwargs):
        return self.base_function()

    def set_mode(self, *args, **kwargs):
        return self.base_function()

    def set_port_force_auth(self, *args, **kwargs):
        return self.base_function()
