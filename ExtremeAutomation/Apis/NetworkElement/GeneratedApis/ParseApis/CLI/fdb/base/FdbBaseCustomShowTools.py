from ExtremeAutomation.Library.Device.Common.Apis.BaseShowApi import BaseShowApi
from ExtremeAutomation.Library.Device.Common.CommandObjects.CliCommandObject import CliCommandObject


class FdbBaseCustomShowTools(BaseShowApi):
    def __init__(self, device):
        super(FdbBaseCustomShowTools, self).__init__()
        self.device = device
        self.it = self.device.inspection_toolkit

    def check_fdb_entry_exists(self, *func_args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_fdb_entry_only_exists_once(self, *func_args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_fdb_agetime(self, *func_args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_fdb_stats_total_equal(self, *func_args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_fdb_stats_static_equal(self, *func_args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_fdb_stats_perm_equal(self, *func_args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_fdb_stats_dynamic_equal(self, *func_args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_fdb_stats_dropped_equal(self, *func_args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_fdb_stats_locked_equal(self, *func_args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_fdb_stats_locked_with_timeout_equal(self, *func_args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_fdb_stats_total_port_equal(self, *func_args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_fdb_stats_dynamic_port_equal(self, *func_args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_fdb_stats_static_port_equal(self, *func_args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_fdb_stats_dropped_port_equal(self, *func_args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_fdb_stats_total_vlan_equal(self, *func_args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_fdb_stats_dynamic_vlan_equal(self, *func_args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_fdb_stats_static_vlan_equal(self, *func_args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_fdb_stats_dropped_vlan_equal(self, *func_args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_fdb_entry_exists_twice(self, *func_args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def base_function(self, *args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def __getattr__(self, item):
        # Return the base_function if the called function does not exist.
        return self.base_function
