"""
Base class for all fabricattach commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.CliBaseApi import CliBaseApi


class FabricattachBase(CliBaseApi):
    def __init__(self, device):
        super(FabricattachBase, self).__init__()
        self.device = device

    def enable_global(self, *args, **kwargs):
        return self.base_function()

    def disable_global(self, *args, **kwargs):
        return self.base_function()

    def enable_port(self, *args, **kwargs):
        return self.base_function()

    def disable_port(self, *args, **kwargs):
        return self.base_function()

    def delete_port(self, *args, **kwargs):
        return self.base_function()

    def enable_mlt(self, *args, **kwargs):
        return self.base_function()

    def disable_mlt(self, *args, **kwargs):
        return self.base_function()

    def delete_mlt(self, *args, **kwargs):
        return self.base_function()

    def enable_port_auth(self, *args, **kwargs):
        return self.base_function()

    def disable_port_auth(self, *args, **kwargs):
        return self.base_function()

    def enable_mlt_auth(self, *args, **kwargs):
        return self.base_function()

    def disable_mlt_auth(self, *args, **kwargs):
        return self.base_function()

    def set_assignment_timeout(self, *args, **kwargs):
        return self.base_function()

    def set_discovery_timeout(self, *args, **kwargs):
        return self.base_function()

    def set_port_auth_key(self, *args, **kwargs):
        return self.base_function()

    def set_mlt_auth_key(self, *args, **kwargs):
        return self.base_function()

    def set_port_mgmt_isid(self, *args, **kwargs):
        return self.base_function()

    def set_mlt_mgmt_isid(self, *args, **kwargs):
        return self.base_function()

    def set_port_mgmt_isid_and_cvid(self, *args, **kwargs):
        return self.base_function()

    def set_mlt_mgmt_isid_and_cvid(self, *args, **kwargs):
        return self.base_function()

    def clear_port_mgmt_isid(self, *args, **kwargs):
        return self.base_function()

    def clear_mlt_mgmt_isid(self, *args, **kwargs):
        return self.base_function()

    def set_zero_touch_client_isid(self, *args, **kwargs):
        return self.base_function()

    def clear_zero_touch_client(self, *args, **kwargs):
        return self.base_function()

    def show_agent(self, *args, **kwargs):
        return self.base_function()

    def show_service_state(self, *args, **kwargs):
        return self.base_function()

    def show_element_type(self, *args, **kwargs):
        return self.base_function()

    def show_provision_mode(self, *args, **kwargs):
        return self.base_function()

    def show_global_timeouts(self, *args, **kwargs):
        return self.base_function()

    def show_port(self, *args, **kwargs):
        return self.base_function()

    def show_mlt(self, *args, **kwargs):
        return self.base_function()

    def show_elements_port(self, *args, **kwargs):
        return self.base_function()

    def show_assignment_port(self, *args, **kwargs):
        return self.base_function()

    def show_stats_global(self, *args, **kwargs):
        return self.base_function()

    def show_stats_port(self, *args, **kwargs):
        return self.base_function()

    def show_zero_touch_client(self, *args, **kwargs):
        return self.base_function()

    def show_isid(self, *args, **kwargs):
        return self.base_function()

    def show_client_proxy_status(self, *args, **kwargs):
        return self.base_function()

    def show_standalone_proxy_status(self, *args, **kwargs):
        return self.base_function()

    def show_agent_timeout(self, *args, **kwargs):
        return self.base_function()

    def show_extended_logging_status(self, *args, **kwargs):
        return self.base_function()

    def show_primary_server_id(self, *args, **kwargs):
        return self.base_function()

    def show_server_description(self, *args, **kwargs):
        return self.base_function()

    def show_neighbors(self, *args, **kwargs):
        return self.base_function()

    def show_elements(self, *args, **kwargs):
        return self.base_function()

    def show_auto_provision_setting(self, *args, **kwargs):
        return self.base_function()

    def show_zero_touch_status(self, *args, **kwargs):
        return self.base_function()
