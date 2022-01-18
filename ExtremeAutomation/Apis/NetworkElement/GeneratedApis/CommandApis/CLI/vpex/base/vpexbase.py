"""
Base class for all vpex commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.CliBaseApi import CliBaseApi


class VpexBase(CliBaseApi):
    def __init__(self, device):
        super(VpexBase, self).__init__()
        self.device = device

    def enable_global(self, *args, **kwargs):
        return self.base_function()

    def disable_global(self, *args, **kwargs):
        return self.base_function()

    def enable_auto_configuration(self, *args, **kwargs):
        return self.base_function()

    def disable_auto_configuration(self, *args, **kwargs):
        return self.base_function()

    def set_ports(self, *args, **kwargs):
        return self.base_function()

    def clear_ports(self, *args, **kwargs):
        return self.base_function()

    def set_ring_rebalancing_auto(self, *args, **kwargs):
        return self.base_function()

    def set_ring_rebalancing_off(self, *args, **kwargs):
        return self.base_function()

    def show_info(self, *args, **kwargs):
        return self.base_function()

    def show_bpe(self, *args, **kwargs):
        return self.base_function()

    def show_bpe_cpu_utilization(self, *args, **kwargs):
        return self.base_function()

    def show_bpe_environment(self, *args, **kwargs):
        return self.base_function()

    def show_bpe_version_detail(self, *args, **kwargs):
        return self.base_function()

    def show_bpe_slot(self, *args, **kwargs):
        return self.base_function()

    def show_bpe_slot_cpu_utilization(self, *args, **kwargs):
        return self.base_function()

    def show_bpe_slot_environment(self, *args, **kwargs):
        return self.base_function()

    def show_bpe_slot_statistics(self, *args, **kwargs):
        return self.base_function()

    def show_bpe_slot_statistics_detail(self, *args, **kwargs):
        return self.base_function()

    def show_bpe_slot_version_detail(self, *args, **kwargs):
        return self.base_function()

    def show_bpe_statistics(self, *args, **kwargs):
        return self.base_function()

    def show_bpe_statistics_detail(self, *args, **kwargs):
        return self.base_function()

    def show_bpe_statistics_detail_slot(self, *args, **kwargs):
        return self.base_function()

    def show_ports(self, *args, **kwargs):
        return self.base_function()

    def show_ports_ecp_statistics(self, *args, **kwargs):
        return self.base_function()

    def show_ports_statistics(self, *args, **kwargs):
        return self.base_function()

    def show_ports_statistics_detail(self, *args, **kwargs):
        return self.base_function()

    def show_topology(self, *args, **kwargs):
        return self.base_function()

    def show_topology_detail(self, *args, **kwargs):
        return self.base_function()

    def show_topology_detail_port(self, *args, **kwargs):
        return self.base_function()

    def show_topology_port(self, *args, **kwargs):
        return self.base_function()

    def show_topology_port_detail(self, *args, **kwargs):
        return self.base_function()

    def show_topology_port_summary(self, *args, **kwargs):
        return self.base_function()

    def show_topology_summary(self, *args, **kwargs):
        return self.base_function()

    def show_topology_summary_port(self, *args, **kwargs):
        return self.base_function()
