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

    def show_cpu_interval(self, arg_dict, **kwargs):
        command_type = "snmpgetnext"
        oid = "1.3.6.1.4.1.1916.1.32.1.1."

        return self.create_cmd_obj(command_type, oid)

    def show_cpu_total_utilization(self, arg_dict, **kwargs):
        command_type = "snmpgetnext"
        oid = "1.3.6.1.4.1.1916.1.32.1.2."

        return self.create_cmd_obj(command_type, oid)

    def show_cpu_5_second_utilization(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.1916.1.32.1.4.1.5.{0}".format(arg_dict['slot'])

        return self.create_cmd_obj(command_type, oid)

    def show_cpu_10_second_utilization(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.1916.1.32.1.4.1.6.{0}".format(arg_dict['slot'])

        return self.create_cmd_obj(command_type, oid)

    def show_cpu_30_second_utilization(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.1916.1.32.1.4.1.7.{0}".format(arg_dict['slot'])

        return self.create_cmd_obj(command_type, oid)

    def show_cpu_1_minute_utilization(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.1916.1.32.1.4.1.8.{0}".format(arg_dict['slot'])

        return self.create_cmd_obj(command_type, oid)

    def show_cpu_5_minute_utilization(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.1916.1.32.1.4.1.9.{0}".format(arg_dict['slot'])

        return self.create_cmd_obj(command_type, oid)

    def show_cpu_30_minute_utilization(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.1916.1.32.1.4.1.10.{0}".format(arg_dict['slot'])

        return self.create_cmd_obj(command_type, oid)

    def show_cpu_1_hour_utilization(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.1916.1.32.1.4.1.11.{0}".format(arg_dict['slot'])

        return self.create_cmd_obj(command_type, oid)

    def show_cpu_max_utilization(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.1916.1.32.1.4.1.12.{0}".format(arg_dict['slot'])

        return self.create_cmd_obj(command_type, oid)

    def show_cpu_threshold(self, arg_dict, **kwargs):
        command_type = "snmpgetnext"
        oid = "1.3.6.1.4.1.1916.1.32.1.5."

        return self.create_cmd_obj(command_type, oid)

    def show_cpu_process_state(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.1916.1.32.1.3.1.4.{0}".format(arg_dict['process_name'])

        return self.create_cmd_obj(command_type, oid)

    def show_cpu_process_5_second_utilization(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.1916.1.32.1.3.1.5.{0}".format(arg_dict['process_name'])

        return self.create_cmd_obj(command_type, oid)

    def show_cpu_process_10_second_utilization(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.1916.1.32.1.3.1.6.{0}".format(arg_dict['process_name'])

        return self.create_cmd_obj(command_type, oid)

    def show_cpu_process_30_second_utilization(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.1916.1.32.1.3.1.7.{0}".format(arg_dict['process_name'])

        return self.create_cmd_obj(command_type, oid)

    def show_cpu_process_1_minute_utilization(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.1916.1.32.1.3.1.8.{0}".format(arg_dict['process_name'])

        return self.create_cmd_obj(command_type, oid)

    def show_cpu_process_5_minute_utilization(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.1916.1.32.1.3.1.9.{0}".format(arg_dict['process_name'])

        return self.create_cmd_obj(command_type, oid)

    def show_cpu_process_30_minute_utilization(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.1916.1.32.1.3.1.10.{0}".format(arg_dict['process_name'])

        return self.create_cmd_obj(command_type, oid)

    def show_cpu_process_1_hour_utilization(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.1916.1.32.1.3.1.11.{0}".format(arg_dict['process_name'])

        return self.create_cmd_obj(command_type, oid)

    def show_cpu_process_max_utilization(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.1916.1.32.1.3.1.12.{0}".format(arg_dict['process_name'])

        return self.create_cmd_obj(command_type, oid)

    def show_cpu_process_application_time(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.1916.1.32.1.3.1.13.{0}".format(arg_dict['process_name'])

        return self.create_cmd_obj(command_type, oid)

    def show_cpu_process_kernel_time(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.1916.1.32.1.3.1.14.{0}".format(arg_dict['process_name'])

        return self.create_cmd_obj(command_type, oid)

    def show_total_memory(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.1916.1.32.2.2.1.2.{0}".format(arg_dict['slot'])

        return self.create_cmd_obj(command_type, oid)

    def show_free_memory(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.1916.1.32.2.2.1.3.{0}".format(arg_dict['slot'])

        return self.create_cmd_obj(command_type, oid)

    def show_used_system_service_memory(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.1916.1.32.2.2.1.4.{0}".format(arg_dict['slot'])

        return self.create_cmd_obj(command_type, oid)

    def show_used_user_application_memory(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.1916.1.32.2.2.1.5.{0}".format(arg_dict['slot'])

        return self.create_cmd_obj(command_type, oid)

    def show_used_memory_for_process(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.1916.1.32.2.3.1.3.{0}".format(arg_dict['oid_index'])

        return self.create_cmd_obj(command_type, oid)
