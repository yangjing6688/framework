"""
Base class for all mlt SNMP commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.SnmpBaseApi import SnmpBaseApi


class MltBase(SnmpBaseApi):
    def __init__(self, device):
        super(MltBase, self).__init__()
        self.device = device

    def create_id(self, *args, **kwargs):
        return self.base_function()

    def delete_id(self, *args, **kwargs):
        return self.base_function()

    def enable_flex_uni(self, *args, **kwargs):
        return self.base_function()

    def disable_flex_uni(self, *args, **kwargs):
        return self.base_function()

    def enable_lacp(self, *args, **kwargs):
        return self.base_function()

    def disable_lacp(self, *args, **kwargs):
        return self.base_function()

    def set_port_member(self, *args, **kwargs):
        return self.base_function()

    def clear_port_member(self, *args, **kwargs):
        return self.base_function()

    def set_type_split_mlt(self, *args, **kwargs):
        return self.base_function()

    def set_type_normal_mlt(self, *args, **kwargs):
        return self.base_function()

    def set_encapsulation_dot1q(self, *args, **kwargs):
        return self.base_function()

    def clear_encapsulation_dot1q(self, *args, **kwargs):
        return self.base_function()

    def show_logical_index(self, *args, **kwargs):
        return self.base_function()

    def show_id(self, *args, **kwargs):
        return self.base_function()

    def show_admin_type(self, *args, **kwargs):
        return self.base_function()

    def show_running_type(self, *args, **kwargs):
        return self.base_function()

    def show_flex_uni_status(self, *args, **kwargs):
        return self.base_function()

    def show_lacp_admin_status(self, *args, **kwargs):
        return self.base_function()

    def show_lacp_oper_status(self, *args, **kwargs):
        return self.base_function()

    def show_ports(self, *args, **kwargs):
        return self.base_function()

    def show_encapsulation(self, *args, **kwargs):
        return self.base_function()
