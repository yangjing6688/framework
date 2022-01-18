"""
Base class for all radius commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.CliBaseApi import CliBaseApi


class RadiusBase(CliBaseApi):
    def __init__(self, device):
        super(RadiusBase, self).__init__()
        self.device = device

    def enable_global(self, *args, **kwargs):
        return self.base_function()

    def enable_acct(self, *args, **kwargs):
        return self.base_function()

    def disable_global(self, *args, **kwargs):
        return self.base_function()

    def disable_acct(self, *args, **kwargs):
        return self.base_function()

    def set_server(self, *args, **kwargs):
        return self.base_function()

    def set_acct_server(self, *args, **kwargs):
        return self.base_function()

    def set_retries_global(self, *args, **kwargs):
        return self.base_function()

    def set_timeout_global(self, *args, **kwargs):
        return self.base_function()

    def set_algorithm_global_std(self, *args, **kwargs):
        return self.base_function()

    def set_algorithm_global_rr(self, *args, **kwargs):
        return self.base_function()

    def set_algorithm_global_srr(self, *args, **kwargs):
        return self.base_function()

    def set_accounting_retries_global(self, *args, **kwargs):
        return self.base_function()

    def set_accounting_timeout_global(self, *args, **kwargs):
        return self.base_function()

    def clear_server(self, *args, **kwargs):
        return self.base_function()

    def clear_acct_server(self, *args, **kwargs):
        return self.base_function()

    def clear_acct_server_global(self, *args, **kwargs):
        return self.base_function()

    def clear_algorithm_global(self, *args, **kwargs):
        return self.base_function()

    def clear_retries_global(self, *args, **kwargs):
        return self.base_function()

    def clear_timeout_global(self, *args, **kwargs):
        return self.base_function()

    def clear_state(self, *args, **kwargs):
        return self.base_function()

    def show_global(self, *args, **kwargs):
        return self.base_function()

    def show_state(self, *args, **kwargs):
        return self.base_function()

    def show_acct_state(self, *args, **kwargs):
        return self.base_function()

    def show_acct_global(self, *args, **kwargs):
        return self.base_function()

    def show_retries_global(self, *args, **kwargs):
        return self.base_function()

    def show_timeout_global(self, *args, **kwargs):
        return self.base_function()

    def show_algorithm(self, *args, **kwargs):
        return self.base_function()

    def enable_mgmt(self, *args, **kwargs):
        return self.base_function()

    def enable_netlogin(self, *args, **kwargs):
        return self.base_function()

    def disable_mgmt(self, *args, **kwargs):
        return self.base_function()

    def disable_netlogin(self, *args, **kwargs):
        return self.base_function()

    def enable_include_cli_cmds(self, *args, **kwargs):
        return self.base_function()

    def enable_cli_profile(self, *args, **kwargs):
        return self.base_function()

    def enable_src_ip_flag(self, *args, **kwargs):
        return self.base_function()

    def disable_include_cli_cmds(self, *args, **kwargs):
        return self.base_function()

    def disable_cli_profile(self, *args, **kwargs):
        return self.base_function()

    def disable_src_ip_flag(self, *args, **kwargs):
        return self.base_function()

    def set_max_servers(self, *args, **kwargs):
        return self.base_function()

    def set_access_priority(self, *args, **kwargs):
        return self.base_function()

    def set_acct_attr(self, *args, **kwargs):
        return self.base_function()

    def set_mcast_addr_attr(self, *args, **kwargs):
        return self.base_function()

    def set_auth_info_attr(self, *args, **kwargs):
        return self.base_function()

    def set_cmd_access_attr(self, *args, **kwargs):
        return self.base_function()

    def set_cli_cmd_attr(self, *args, **kwargs):
        return self.base_function()

    def set_cli_cmd_count(self, *args, **kwargs):
        return self.base_function()

    def set_server_for_cli(self, *args, **kwargs):
        return self.base_function()

    def clear_server_for_cli(self, *args, **kwargs):
        return self.base_function()

    def clear_stats_global(self, *args, **kwargs):
        return self.base_function()

    def show_servers(self, *args, **kwargs):
        return self.base_function()

    def show_global_scalars(self, *args, **kwargs):
        return self.base_function()

    def show_global_snmp_scalars(self, *args, **kwargs):
        return self.base_function()
