"""
Base class for all vlan commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.CliBaseApi import CliBaseApi


class VlanBase(CliBaseApi):
    def __init__(self, device):
        super(VlanBase, self).__init__()
        self.device = device

    def create_vlan(self, *args, **kwargs):
        return self.base_function()

    def delete_vlan(self, *args, **kwargs):
        return self.base_function()

    def create_vman(self, *args, **kwargs):
        return self.base_function()

    def delete_vman(self, *args, **kwargs):
        return self.base_function()

    def enable_vlan(self, *args, **kwargs):
        return self.base_function()

    def disable_vlan(self, *args, **kwargs):
        return self.base_function()

    def enable_dynamic_egress(self, *args, **kwargs):
        return self.base_function()

    def disable_dynamic_egress(self, *args, **kwargs):
        return self.base_function()

    def set_egress_untagged(self, *args, **kwargs):
        return self.base_function()

    def set_egress_tagged(self, *args, **kwargs):
        return self.base_function()

    def set_egress_forbidden(self, *args, **kwargs):
        return self.base_function()

    def clear_egress(self, *args, **kwargs):
        return self.base_function()

    def clear_egress_type(self, *args, **kwargs):
        return self.base_function()

    def set_description(self, *args, **kwargs):
        return self.base_function()

    def clear_description(self, *args, **kwargs):
        return self.base_function()

    def set_name(self, *args, **kwargs):
        return self.base_function()

    def clear_name(self, *args, **kwargs):
        return self.base_function()

    def set_pvid(self, *args, **kwargs):
        return self.base_function()

    def clear_pvid(self, *args, **kwargs):
        return self.base_function()

    def show_all_info(self, *args, **kwargs):
        return self.base_function()

    def show_info(self, *args, **kwargs):
        return self.base_function()

    def show_name(self, *args, **kwargs):
        return self.base_function()

    def show_description(self, *args, **kwargs):
        return self.base_function()

    def show_status(self, *args, **kwargs):
        return self.base_function()

    def show_pvid(self, *args, **kwargs):
        return self.base_function()

    def show_static(self, *args, **kwargs):
        return self.base_function()

    def show_port_egress(self, *args, **kwargs):
        return self.base_function()

    def show_all_vman_info(self, *args, **kwargs):
        return self.base_function()

    def create_vlan_with_name(self, *args, **kwargs):
        return self.base_function()

    def set_vman_egress_untagged(self, *args, **kwargs):
        return self.base_function()

    def set_vman_egress_tagged(self, *args, **kwargs):
        return self.base_function()

    def clear_vman_egress(self, *args, **kwargs):
        return self.base_function()

    def set_nsi(self, *args, **kwargs):
        return self.base_function()

    def clear_nsi(self, *args, **kwargs):
        return self.base_function()

    def set_isid(self, *args, **kwargs):
        return self.base_function()

    def clear_isid(self, *args, **kwargs):
        return self.base_function()

    def show_vman_info(self, *args, **kwargs):
        return self.base_function()

    def show_fabric_attach_assignments(self, *args, **kwargs):
        return self.base_function()

    def show_nsi(self, *args, **kwargs):
        return self.base_function()

    def show_isid(self, *args, **kwargs):
        return self.base_function()

    def create_spbm(self, *args, **kwargs):
        return self.base_function()

    def set_member(self, *args, **kwargs):
        return self.base_function()

    def clear_member(self, *args, **kwargs):
        return self.base_function()

    def set_port_encapsulation_dot1q(self, *args, **kwargs):
        return self.base_function()

    def clear_port_encapsulation_dot1q(self, *args, **kwargs):
        return self.base_function()

    def show_members(self, *args, **kwargs):
        return self.base_function()

    def show_members_port(self, *args, **kwargs):
        return self.base_function()

    def show_port(self, *args, **kwargs):
        return self.base_function()
