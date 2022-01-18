"""
Base class for all hostmonitor commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.CliBaseApi import CliBaseApi


class HostmonitorBase(CliBaseApi):
    def __init__(self, device):
        super(HostmonitorBase, self).__init__()
        self.device = device

    def show_slot(self, *args, **kwargs):
        return self.base_function()

    def show_cpu_current_total_utilization(self, *args, **kwargs):
        return self.base_function()

    def show_cpu_5_minute_total_utilization(self, *args, **kwargs):
        return self.base_function()

    def show_cpu_highest_5_minute_total_utilization(self, *args, **kwargs):
        return self.base_function()

    def show_cpu_5_minute_hi_time_total_utilization(self, *args, **kwargs):
        return self.base_function()

    def show_used_total_memory(self, *args, **kwargs):
        return self.base_function()

    def show_free_total_memory(self, *args, **kwargs):
        return self.base_function()

    def show_memory_total_utilization(self, *args, **kwargs):
        return self.base_function()

    def show_memory_5_minute_total_utilization(self, *args, **kwargs):
        return self.base_function()

    def show_memory_highest_5_minute_total_utilization(self, *args, **kwargs):
        return self.base_function()

    def show_memory_5_minute_hi_time_total_utilization(self, *args, **kwargs):
        return self.base_function()

    def show_used_fbuf(self, *args, **kwargs):
        return self.base_function()

    def show_free_fbuf(self, *args, **kwargs):
        return self.base_function()

    def show_exhausted_fbufs(self, *args, **kwargs):
        return self.base_function()

    def show_net_stack_system_free_mbuf(self, *args, **kwargs):
        return self.base_function()

    def show_net_stack_data_free_mbuf(self, *args, **kwargs):
        return self.base_function()

    def show_net_stack_system_used_mbuf(self, *args, **kwargs):
        return self.base_function()

    def show_net_stack_data_used_mbuf(self, *args, **kwargs):
        return self.base_function()

    def show_net_stack_system_socket_mbuf(self, *args, **kwargs):
        return self.base_function()

    def show_highest_queue_entries_consumed(self, *args, **kwargs):
        return self.base_function()

    def show_current_queue_entries_consumed(self, *args, **kwargs):
        return self.base_function()

    def show_free_queue_entries(self, *args, **kwargs):
        return self.base_function()
