"""
All dns supported SNMP commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.SNMP.dns.base.dnsbase import DnsBase


class Dns(DeviceApi, DnsBase):
    def __init__(self, device):
        super(Dns, self).__init__(device)
        self.device = device

    def create_domain_name(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.1.70.0"
        data_type = "s"
        value = "{0}".format(arg_dict['domain_name'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def delete_domain_name(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.1.70.0"
        data_type = "s"
        value = ""

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_primary_server_ip(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.1.64.1.6.0||" \
              "1.3.6.1.4.1.2272.1.1.64.1.7.0||" \
              "1.3.6.1.4.1.2272.1.1.64.1.8.0"
        data_type = "i||i||s"
        value = "4||{0}||{1}".format(arg_dict['ip_type'],
                                     arg_dict['ip_addr'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_secondary_server_ip(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.1.64.1.6.1||" \
              "1.3.6.1.4.1.2272.1.1.64.1.7.1||" \
              "1.3.6.1.4.1.2272.1.1.64.1.8.1"
        data_type = "i||i||s"
        value = "4||{0}||{1}".format(arg_dict['ip_type'],
                                     arg_dict['ip_addr'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_tertiary_server_ip(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.1.64.1.6.2||" \
              "1.3.6.1.4.1.2272.1.1.64.1.7.2||" \
              "1.3.6.1.4.1.2272.1.1.64.1.8.2"
        data_type = "i||i||s"
        value = "4||{0}||{1}".format(arg_dict['ip_type'],
                                     arg_dict['ip_addr'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def clear_primary_server_ip(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.1.64.1.6.0"
        data_type = "i"
        value = "6"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def clear_secondary_server_ip(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.1.64.1.6.1"
        data_type = "i"
        value = "6"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def clear_tertiary_server_ip(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.1.64.1.6.2"
        data_type = "i"
        value = "6"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def show_domain_name(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.2272.1.1.70.0"

        return self.create_cmd_obj(command_type, oid)

    def show_servers(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.4.1.2272.1.1.64"

        return self.create_cmd_obj(command_type, oid)

    def show_host_by_name(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.2272.1.1.65.1.2.{0}||" \
              "1.3.6.1.4.1.2272.1.1.65.1.5.{0}||" \
              "1.3.6.1.4.1.2272.1.1.65.1.6.{0}".format(arg_dict['host_name'])

        return self.create_cmd_obj(command_type, oid)

    def show_host_by_ip(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.2272.1.1.65.1.2.{0}||" \
              "1.3.6.1.4.1.2272.1.1.65.1.5.{0}||" \
              "1.3.6.1.4.1.2272.1.1.65.1.6.{0}".format(arg_dict['host_ip'])

        return self.create_cmd_obj(command_type, oid)
