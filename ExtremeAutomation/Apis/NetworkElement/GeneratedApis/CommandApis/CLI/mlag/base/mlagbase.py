"""
Base class for all mlag commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.CliBaseApi import CliBaseApi


class MlagBase(CliBaseApi):
    def __init__(self, device):
        super(MlagBase, self).__init__()
        self.device = device

    def enable_port_peer_id(self, *args, **kwargs):
        return self.base_function()

    def enable_port_reload_delay(self, *args, **kwargs):
        return self.base_function()

    def disable_port(self, *args, **kwargs):
        return self.base_function()

    def disable_port_reload_delay(self, *args, **kwargs):
        return self.base_function()

    def create_peer(self, *args, **kwargs):
        return self.base_function()

    def create_peer_auth_md5_key(self, *args, **kwargs):
        return self.base_function()

    def create_peer_auth_md5_key_name(self, *args, **kwargs):
        return self.base_function()

    def create_peer_auth_md5_key_encrypted(self, *args, **kwargs):
        return self.base_function()

    def delete_peer(self, *args, **kwargs):
        return self.base_function()

    def set_peer(self, *args, **kwargs):
        return self.base_function()

    def set_peer_alternate_ip(self, *args, **kwargs):
        return self.base_function()

    def set_peer_alternate_ip_none(self, *args, **kwargs):
        return self.base_function()

    def set_peer_alternate_ip_vr(self, *args, **kwargs):
        return self.base_function()

    def set_peer_auth_none(self, *args, **kwargs):
        return self.base_function()

    def set_peer_auth_md5_key(self, *args, **kwargs):
        return self.base_function()

    def set_peer_auth_md5_key_name(self, *args, **kwargs):
        return self.base_function()

    def set_peer_auth_md5_key_encrypted(self, *args, **kwargs):
        return self.base_function()

    def set_peer_interval(self, *args, **kwargs):
        return self.base_function()

    def set_peer_ipaddress(self, *args, **kwargs):
        return self.base_function()

    def set_peer_ipaddress_vr(self, *args, **kwargs):
        return self.base_function()

    def set_peer_lacp_mac(self, *args, **kwargs):
        return self.base_function()

    def set_peer_lacp_mac_auto(self, *args, **kwargs):
        return self.base_function()

    def set_peer_new_name(self, *args, **kwargs):
        return self.base_function()

    def show_peer(self, *args, **kwargs):
        return self.base_function()

    def show_peer_all(self, *args, **kwargs):
        return self.base_function()

    def show_ports(self, *args, **kwargs):
        return self.base_function()

    def show_ports_all(self, *args, **kwargs):
        return self.base_function()
