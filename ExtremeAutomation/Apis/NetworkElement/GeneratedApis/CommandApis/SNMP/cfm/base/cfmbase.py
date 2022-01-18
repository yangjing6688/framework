"""
Base class for all cfm SNMP commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.SnmpBaseApi import SnmpBaseApi


class CfmBase(SnmpBaseApi):
    def __init__(self, device):
        super(CfmBase, self).__init__()
        self.device = device

    def enable_spbm(self, *args, **kwargs):
        return self.base_function()

    def disable_spbm(self, *args, **kwargs):
        return self.base_function()

    def enable_maintenance_endpoint(self, *args, **kwargs):
        return self.base_function()

    def disable_maintenance_endpoint(self, *args, **kwargs):
        return self.base_function()

    def set_spbm_mepid(self, *args, **kwargs):
        return self.base_function()

    def set_spbm_level(self, *args, **kwargs):
        return self.base_function()

    def set_maintenance_domain(self, *args, **kwargs):
        return self.base_function()

    def set_maintenance_domain_name(self, *args, **kwargs):
        return self.base_function()

    def set_maintenance_domain_index(self, *args, **kwargs):
        return self.base_function()

    def set_maintenance_domain_level(self, *args, **kwargs):
        return self.base_function()

    def set_maintenance_association(self, *args, **kwargs):
        return self.base_function()

    def set_maintenance_endpoint(self, *args, **kwargs):
        return self.base_function()

    def clear_spbm_mepid(self, *args, **kwargs):
        return self.base_function()

    def clear_spbm_level(self, *args, **kwargs):
        return self.base_function()

    def clear_maintenance_domain(self, *args, **kwargs):
        return self.base_function()

    def clear_maintenance_association(self, *args, **kwargs):
        return self.base_function()

    def clear_maintenance_endpoint(self, *args, **kwargs):
        return self.base_function()

    def show_cmac(self, *args, **kwargs):
        return self.base_function()

    def show_spbm(self, *args, **kwargs):
        return self.base_function()

    def show_maintenance_endpoint(self, *args, **kwargs):
        return self.base_function()

    def show_maintenance_association(self, *args, **kwargs):
        return self.base_function()

    def show_maintenance_domain(self, *args, **kwargs):
        return self.base_function()

    def show_association_name(self, *args, **kwargs):
        return self.base_function()

    def show_domain_name(self, *args, **kwargs):
        return self.base_function()
