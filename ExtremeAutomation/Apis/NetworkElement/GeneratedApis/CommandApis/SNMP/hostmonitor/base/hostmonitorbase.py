"""
Base class for all hostmonitor SNMP commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.SnmpBaseApi import SnmpBaseApi


class HostmonitorBase(SnmpBaseApi):
    def __init__(self, device):
        super(HostmonitorBase, self).__init__()
        self.device = device

    def show_cpu_interval(self, *args, **kwargs):
        return self.base_function()

    def show_cpu_total_utilization(self, *args, **kwargs):
        return self.base_function()

    def show_cpu_5_second_utilization(self, *args, **kwargs):
        return self.base_function()

    def show_cpu_10_second_utilization(self, *args, **kwargs):
        return self.base_function()

    def show_cpu_30_second_utilization(self, *args, **kwargs):
        return self.base_function()

    def show_cpu_1_minute_utilization(self, *args, **kwargs):
        return self.base_function()

    def show_cpu_5_minute_utilization(self, *args, **kwargs):
        return self.base_function()

    def show_cpu_30_minute_utilization(self, *args, **kwargs):
        return self.base_function()

    def show_cpu_1_hour_utilization(self, *args, **kwargs):
        return self.base_function()

    def show_cpu_max_utilization(self, *args, **kwargs):
        return self.base_function()

    def show_cpu_threshold(self, *args, **kwargs):
        return self.base_function()

    def show_cpu_process_state(self, *args, **kwargs):
        return self.base_function()

    def show_cpu_process_5_second_utilization(self, *args, **kwargs):
        return self.base_function()

    def show_cpu_process_10_second_utilization(self, *args, **kwargs):
        return self.base_function()

    def show_cpu_process_30_second_utilization(self, *args, **kwargs):
        return self.base_function()

    def show_cpu_process_1_minute_utilization(self, *args, **kwargs):
        return self.base_function()

    def show_cpu_process_5_minute_utilization(self, *args, **kwargs):
        return self.base_function()

    def show_cpu_process_30_minute_utilization(self, *args, **kwargs):
        return self.base_function()

    def show_cpu_process_1_hour_utilization(self, *args, **kwargs):
        return self.base_function()

    def show_cpu_process_max_utilization(self, *args, **kwargs):
        return self.base_function()

    def show_cpu_process_application_time(self, *args, **kwargs):
        return self.base_function()

    def show_cpu_process_kernel_time(self, *args, **kwargs):
        return self.base_function()

    def show_total_memory(self, *args, **kwargs):
        return self.base_function()

    def show_free_memory(self, *args, **kwargs):
        return self.base_function()

    def show_used_system_service_memory(self, *args, **kwargs):
        return self.base_function()

    def show_used_user_application_memory(self, *args, **kwargs):
        return self.base_function()

    def show_used_memory_for_process(self, *args, **kwargs):
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
