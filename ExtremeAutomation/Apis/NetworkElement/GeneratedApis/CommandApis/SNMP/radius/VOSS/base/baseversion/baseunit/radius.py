"""
All radius supported SNMP commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.SNMP.radius.base.radiusbase import RadiusBase


class Radius(DeviceApi, RadiusBase):
    def __init__(self, device):
        super(Radius, self).__init__(device)
        self.device = device

    def enable_global(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.29.1.1.0"
        data_type = "i"
        value = "1"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def enable_acct(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.29.1.1.0||" \
              "1.3.6.1.4.1.2272.1.29.1.5.0"
        data_type = "i||i"
        value = "1||1"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def disable_global(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.29.1.1.0"
        data_type = "i"
        value = "2"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def disable_acct(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.29.1.5.0"
        data_type = "i"
        value = "2"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def enable_include_cli_cmds(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.29.1.7.0"
        data_type = "i"
        value = "1"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def enable_cli_profile(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.29.1.14.0"
        data_type = "i"
        value = "1"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def enable_src_ip_flag(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.29.1.16.0"
        data_type = "i"
        value = "1"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def disable_include_cli_cmds(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.29.1.7.0"
        data_type = "i"
        value = "2"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def disable_cli_profile(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.29.1.14.0"
        data_type = "i"
        value = "2"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def disable_src_ip_flag(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.29.1.16.0"
        data_type = "i"
        value = "2"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_max_servers(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.29.1.2.0"
        data_type = "i"
        value = "{0}".format(arg_dict['max_servers'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_access_priority(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.29.1.3.0"
        data_type = "i"
        value = "{0}".format(arg_dict['attr_value'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_acct_attr(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.29.1.6.0"
        data_type = "i"
        value = "{0}".format(arg_dict['attr_value'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_mcast_addr_attr(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.29.1.9.0"
        data_type = "i"
        value = "{0}".format(arg_dict['attr_value'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_auth_info_attr(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.29.1.10.0"
        data_type = "i"
        value = "{0}".format(arg_dict['attr_value'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_cmd_access_attr(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.29.1.11.0"
        data_type = "i"
        value = "{0}".format(arg_dict['attr_value'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_cli_cmd_attr(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.29.1.12.0"
        data_type = "i"
        value = "{0}".format(arg_dict['attr_value'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_cli_cmd_count(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.29.1.18.0"
        data_type = "i"
        value = "{0}".format(arg_dict['value'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_server_for_cli(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.29.5.1.9.{0}||" \
              "1.3.6.1.4.1.2272.1.29.5.1.8.{0}||" \
              "1.3.6.1.4.1.2272.1.29.5.1.4.{0}||" \
              "1.3.6.1.4.1.2272.1.29.5.1.7.{0}||" \
              "1.3.6.1.4.1.2272.1.29.5.1.6.{0}||" \
              "1.3.6.1.4.1.2272.1.29.5.1.5.{0}||" \
              "1.3.6.1.4.1.2272.1.29.5.1.18.{0}||" \
              "1.3.6.1.4.1.2272.1.29.5.1.17.{0}||" \
              "1.3.6.1.4.1.2272.1.29.5.1.30.{0}||" \
              "1.3.6.1.4.1.2272.1.29.5.1.16.{0}".format(arg_dict['addr'])
        data_type = "s||i||i||i||i||i||i||i||s||i"
        value = "{0}||{1}||{2}||{3}||1||{4}||{5}||1||{6}||4".format(arg_dict['secret'],
                                                                    arg_dict['auth_port'],
                                                                    arg_dict['priority'],
                                                                    arg_dict['max_retries'],
                                                                    arg_dict['timeout'],
                                                                    arg_dict['acct_port'],
                                                                    arg_dict['source_ip'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def clear_server_for_cli(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.29.5.1.16.{0}".format(arg_dict['addr'])
        data_type = "i"
        value = "6"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def clear_stats_global(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.29.1.8.0"
        data_type = "i"
        value = "1"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def show_global(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.4.1.2272.1.29"

        return self.create_cmd_obj(command_type, oid)

    def show_state(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.2272.1.29.1.1.0"

        return self.create_cmd_obj(command_type, oid)

    def show_acct_state(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.2272.1.29.1.5.0"

        return self.create_cmd_obj(command_type, oid)

    def show_servers(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.4.1.2272.1.29.5"

        return self.create_cmd_obj(command_type, oid)

    def show_global_scalars(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.4.1.2272.1.29.1"

        return self.create_cmd_obj(command_type, oid)

    def show_global_snmp_scalars(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.4.1.2272.1.29.4"

        return self.create_cmd_obj(command_type, oid)

    def show_global_auth_invalid_srv_addrs(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.2272.1.29.1.15.0"

        return self.create_cmd_obj(command_type, oid)
