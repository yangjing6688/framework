from ExtremeAutomation.Library.Device.Common.Apis.BaseShowApi import BaseShowApi
from ExtremeAutomation.Library.Device.Common.CommandObjects.CliCommandObject import CliCommandObject


class VrrpBaseCustomShowTools(BaseShowApi):
    def __init__(self, device):
        super(VrrpBaseCustomShowTools, self).__init__()
        self.device = device
        self.it = self.device.inspection_toolkit

    def check_vrrp_globally_enabled(self, *func_args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_vrrp_globally_disabled(self, *func_args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_vrrp_vlan_exists(self, *func_args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_vrrp_group_exists(self, *func_args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_vrrp_vlan_fabric_routing_is_set(self, *func_args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_vrrp_vlan_priority_is_set(self, *func_args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_vrrp_vlan_ip_address_is_set(self, *func_args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_vrrp_vlan_is_enabled(self, *func_args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_vrrp_state_is_master(self, *func_args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_vrrp_state_is_backup(self, *func_args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def base_function(self, *args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def __getattr__(self, item):
        # Return the base_function if the called function does not exist.
        return self.base_function
