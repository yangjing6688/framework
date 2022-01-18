"""
All loginconfig supported SNMP commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.SNMP.loginconfig.base.loginconfigbase import \
    LoginconfigBase


class Loginconfig(DeviceApi, LoginconfigBase):
    def __init__(self, device):
        super(Loginconfig, self).__init__(device)
        self.device = device

    def enable_cli_ro_user(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.19.23.0"
        data_type = "i"
        value = "1"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def disable_cli_ro_user(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.19.23.0"
        data_type = "i"
        value = "2"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def enable_cli_rw_user(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.19.19.0"
        data_type = "i"
        value = "1"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def disable_cli_rw_user(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.19.19.0"
        data_type = "i"
        value = "2"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def enable_cli_l1_user(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.19.20.0"
        data_type = "i"
        value = "1"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def disable_cli_l1_user(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.19.20.0"
        data_type = "i"
        value = "2"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def enable_cli_l2_user(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.19.21.0"
        data_type = "i"
        value = "1"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def disable_cli_l2_user(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.19.21.0"
        data_type = "i"
        value = "2"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def enable_cli_l3_user(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.19.22.0"
        data_type = "i"
        value = "1"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def disable_cli_l3_user(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.19.22.0"
        data_type = "i"
        value = "2"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_read_only_user(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.19.9.0||" \
              "1.3.6.1.4.1.2272.1.19.10.0"
        data_type = "s||s"
        value = "{0}||{1}".format(arg_dict['username'],
                                  arg_dict['new_passwd'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_read_write_user(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.19.3.0||" \
              "1.3.6.1.4.1.2272.1.19.4.0"
        data_type = "s||s"
        value = "{0}||{1}".format(arg_dict['username'],
                                  arg_dict['new_passwd'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_read_write_all_user(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.19.1.0||" \
              "1.3.6.1.4.1.2272.1.19.2.0"
        data_type = "s||s"
        value = "{0}||{1}".format(arg_dict['username'],
                                  arg_dict['new_passwd'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_max_telnet_sessions(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.19.11.0"
        data_type = "i"
        value = "{0}".format(arg_dict['max_sessions'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_max_rlogin_sessions(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.19.12.0"
        data_type = "i"
        value = "{0}".format(arg_dict['max_sessions'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_l1_user(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.19.15.0||" \
              "1.3.6.1.4.1.2272.1.19.16.0"
        data_type = "s||s"
        value = "{0}||{1}".format(arg_dict['username'],
                                  arg_dict['new_passwd'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_l2_user(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.19.7.0||" \
              "1.3.6.1.4.1.2272.1.19.8.0"
        data_type = "s||s"
        value = "{0}||{1}".format(arg_dict['username'],
                                  arg_dict['new_passwd'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_l3_user(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.19.5.0||" \
              "1.3.6.1.4.1.2272.1.19.6.0"
        data_type = "s||s"
        value = "{0}||{1}".format(arg_dict['username'],
                                  arg_dict['new_passwd'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_cli_timeout(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.19.13.0"
        data_type = "i"
        value = "{0}".format(arg_dict['timeout'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def show_cli_info(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.4.1.2272.1.19"

        return self.create_cmd_obj(command_type, oid)

    def show_cli_users_state(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.2272.1.19.19.0||" \
              "1.3.6.1.4.1.2272.1.19.20.0||" \
              "1.3.6.1.4.1.2272.1.19.21.0||" \
              "1.3.6.1.4.1.2272.1.19.22.0||" \
              "1.3.6.1.4.1.2272.1.19.23.0||" \
              "1.3.6.1.4.1.2272.1.19.24.0"

        return self.create_cmd_obj(command_type, oid)

    def show_cli_num_access_violations(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.2272.1.19.14.0"

        return self.create_cmd_obj(command_type, oid)
