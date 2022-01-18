"""
Base class for all ospf commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.CliBaseApi import CliBaseApi


class OspfBase(CliBaseApi):
    def __init__(self, device):
        super(OspfBase, self).__init__()
        self.device = device

    def enable_global(self, *args, **kwargs):
        return self.base_function()

    def disable_global(self, *args, **kwargs):
        return self.base_function()

    def set_router_id(self, *args, **kwargs):
        return self.base_function()

    def clear_router_id(self, *args, **kwargs):
        return self.base_function()

    def set_metric_table_100g(self, *args, **kwargs):
        return self.base_function()

    def set_metric_table_100m(self, *args, **kwargs):
        return self.base_function()

    def set_metric_table_10g(self, *args, **kwargs):
        return self.base_function()

    def set_metric_table_10m(self, *args, **kwargs):
        return self.base_function()

    def set_metric_table_1g(self, *args, **kwargs):
        return self.base_function()

    def set_metric_table_2dot5g(self, *args, **kwargs):
        return self.base_function()

    def set_metric_table_25g(self, *args, **kwargs):
        return self.base_function()

    def set_metric_table_40g(self, *args, **kwargs):
        return self.base_function()

    def set_metric_table_50g(self, *args, **kwargs):
        return self.base_function()

    def set_metric_table_5g(self, *args, **kwargs):
        return self.base_function()

    def set_vlan_auth_md5(self, *args, **kwargs):
        return self.base_function()

    def set_vlan_auth_none(self, *args, **kwargs):
        return self.base_function()

    def set_add_vlan(self, *args, **kwargs):
        return self.base_function()

    def set_del_vlan(self, *args, **kwargs):
        return self.base_function()

    def show_info(self, *args, **kwargs):
        return self.base_function()

    def show_neighbor(self, *args, **kwargs):
        return self.base_function()

    def show_vlan_interface(self, *args, **kwargs):
        return self.base_function()

    def enable_interface(self, *args, **kwargs):
        return self.base_function()

    def disable_interface(self, *args, **kwargs):
        return self.base_function()

    def enable_vlan(self, *args, **kwargs):
        return self.base_function()

    def disable_vlan(self, *args, **kwargs):
        return self.base_function()

    def show_interface(self, *args, **kwargs):
        return self.base_function()
