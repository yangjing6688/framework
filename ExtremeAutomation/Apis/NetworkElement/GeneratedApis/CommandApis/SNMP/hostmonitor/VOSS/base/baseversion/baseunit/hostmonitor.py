"""
All hostmonitor supported SNMP commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.SNMP.hostmonitor.base.hostmonitorbase import \
    HostmonitorBase


class Hostmonitor(DeviceApi, HostmonitorBase):
    def __init__(self, device):
        super(Hostmonitor, self).__init__(device)
        self.device = device

    def show_cpu_current_total_utilization(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.2272.1.85.10.1.1.2.{0}".format(arg_dict['slot'])

        return self.create_cmd_obj(command_type, oid)

    def show_cpu_5_minute_total_utilization(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.2272.1.85.10.1.1.3.{0}".format(arg_dict['slot'])

        return self.create_cmd_obj(command_type, oid)

    def show_cpu_highest_5_minute_total_utilization(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.2272.1.85.10.1.1.4.{0}".format(arg_dict['slot'])

        return self.create_cmd_obj(command_type, oid)

    def show_cpu_5_minute_hi_time_total_utilization(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.2272.1.85.10.1.1.5.{0}".format(arg_dict['slot'])

        return self.create_cmd_obj(command_type, oid)

    def show_used_total_memory(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.2272.1.85.10.1.1.6.{0}".format(arg_dict['slot'])

        return self.create_cmd_obj(command_type, oid)

    def show_free_total_memory(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.2272.1.85.10.1.1.7.{0}".format(arg_dict['slot'])

        return self.create_cmd_obj(command_type, oid)

    def show_memory_total_utilization(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.2272.1.85.10.1.1.8.{0}".format(arg_dict['slot'])

        return self.create_cmd_obj(command_type, oid)

    def show_memory_5_minute_total_utilization(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.2272.1.85.10.1.1.9.{0}".format(arg_dict['slot'])

        return self.create_cmd_obj(command_type, oid)

    def show_memory_highest_5_minute_total_utilization(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.2272.1.85.10.1.1.10.{0}".format(arg_dict['slot'])

        return self.create_cmd_obj(command_type, oid)

    def show_memory_5_minute_hi_time_total_utilization(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.2272.1.85.10.1.1.11.{0}".format(arg_dict['slot'])

        return self.create_cmd_obj(command_type, oid)

    def show_used_fbuf(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.2272.1.85.10.1.1.12.{0}".format(arg_dict['slot'])

        return self.create_cmd_obj(command_type, oid)

    def show_free_fbuf(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.2272.1.85.10.1.1.13.{0}".format(arg_dict['slot'])

        return self.create_cmd_obj(command_type, oid)

    def show_exhausted_fbufs(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.2272.1.85.10.1.1.14.{0}".format(arg_dict['slot'])

        return self.create_cmd_obj(command_type, oid)

    def show_net_stack_system_free_mbuf(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.2272.1.85.10.1.1.15.{0}".format(arg_dict['slot'])

        return self.create_cmd_obj(command_type, oid)

    def show_net_stack_data_free_mbuf(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.2272.1.85.10.1.1.16.{0}".format(arg_dict['slot'])

        return self.create_cmd_obj(command_type, oid)

    def show_net_stack_system_used_mbuf(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.2272.1.85.10.1.1.17.{0}".format(arg_dict['slot'])

        return self.create_cmd_obj(command_type, oid)

    def show_net_stack_data_used_mbuf(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.2272.1.85.10.1.1.18.{0}".format(arg_dict['slot'])

        return self.create_cmd_obj(command_type, oid)

    def show_net_stack_system_socket_mbuf(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.2272.1.85.10.1.1.19.{0}".format(arg_dict['slot'])

        return self.create_cmd_obj(command_type, oid)

    def show_highest_queue_entries_consumed(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.2272.1.85.10.1.1.20.{0}".format(arg_dict['slot'])

        return self.create_cmd_obj(command_type, oid)

    def show_current_queue_entries_consumed(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.2272.1.85.10.1.1.21.{0}".format(arg_dict['slot'])

        return self.create_cmd_obj(command_type, oid)

    def show_free_queue_entries(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.2272.1.85.10.1.1.22.{0}".format(arg_dict['slot'])

        return self.create_cmd_obj(command_type, oid)
