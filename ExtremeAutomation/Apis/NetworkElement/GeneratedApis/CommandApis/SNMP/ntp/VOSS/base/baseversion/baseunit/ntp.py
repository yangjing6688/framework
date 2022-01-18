"""
All ntp supported SNMP commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.SNMP.ntp.base.ntpbase import NtpBase


class Ntp(DeviceApi, NtpBase):
    def __init__(self, device):
        super(Ntp, self).__init__(device)
        self.device = device

    def enable_client(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.33.1.1.0"
        data_type = "i"
        value = "1"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def disable_client(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.33.1.1.0"
        data_type = "i"
        value = "2"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def create_server(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.33.2.1.8.{0}".format(arg_dict['server'])
        data_type = "i"
        value = "4"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def create_server_key(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.33.2.1.4.{0}".format(arg_dict['server'])
        data_type = "i"
        value = "{0}".format(arg_dict['key'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def delete_server(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.33.2.1.8.{0}".format(arg_dict['server'])
        data_type = "i"
        value = "6"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def enable_server(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.33.2.1.2.{0}".format(arg_dict['server'])
        data_type = "i"
        value = "1"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def disable_server(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.33.2.1.2.{0}".format(arg_dict['server'])
        data_type = "i"
        value = "2"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def enable_server_auth(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.33.2.1.3.{0}".format(arg_dict['server'])
        data_type = "i"
        value = "1"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def disable_server_auth(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.33.2.1.3.{0}".format(arg_dict['server'])
        data_type = "i"
        value = "2"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_global_interval(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.33.1.2.0"
        data_type = "i"
        value = "{0}".format(arg_dict['interval'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_server_source_ip(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.33.2.1.15.{0}".format(arg_dict['server'])
        data_type = "a"
        value = "{0}".format(arg_dict['source_ip'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_auth(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.33.3.1.3.{0}||" \
              "1.3.6.1.4.1.2272.1.33.3.1.2.{0}".format(arg_dict['index'])
        data_type = "i||s"
        value = "4||initialkey"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_auth_key(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.33.3.1.2.{0}".format(arg_dict['index'])
        data_type = "s"
        value = "{0}".format(arg_dict['secret'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_auth_md5(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.33.3.1.4.{0}".format(arg_dict['index'])
        data_type = "i"
        value = "1"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_auth_sha1(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.33.3.1.4.{0}".format(arg_dict['index'])
        data_type = "i"
        value = "2"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def clear_auth_key(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.33.3.1.3.{0}".format(arg_dict['index'])
        data_type = "i"
        value = "6"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def show_info(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.4.1.2272.1.33."

        return self.create_cmd_obj(command_type, oid)

    def show_servers(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.4.1.2272.1.33.2."

        return self.create_cmd_obj(command_type, oid)

    def show_key(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.4.1.2272.1.33.3."

        return self.create_cmd_obj(command_type, oid)

    def show_statistics(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.4.1.2272.1.33.2."

        return self.create_cmd_obj(command_type, oid)
