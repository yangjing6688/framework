"""
All mlt supported SNMP commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.SNMP.mlt.base.mltbase import MltBase


class Mlt(DeviceApi, MltBase):
    def __init__(self, device):
        super(Mlt, self).__init__(device)
        self.device = device

    def create_id(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.17.10.1.7.{0}".format(arg_dict['mlt_id'])
        data_type = "i"
        value = "4"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def delete_id(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.17.10.1.7.{0}".format(arg_dict['mlt_id'])
        data_type = "i"
        value = "6"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def enable_flex_uni(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.17.10.1.49.{0}".format(arg_dict['mlt_id'])
        data_type = "i"
        value = "1"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def disable_flex_uni(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.17.10.1.49.{0}".format(arg_dict['mlt_id'])
        data_type = "i"
        value = "2"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def enable_lacp(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.17.10.1.18.{0}".format(arg_dict['mlt_id'])
        data_type = "i"
        value = "1"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def disable_lacp(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.17.10.1.18.{0}".format(arg_dict['mlt_id'])
        data_type = "i"
        value = "2"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_port_member(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.17.10.1.3.{0}".format(arg_dict['mlt_id'])
        data_type = "s"
        value = "{0}".format(arg_dict['port'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def clear_port_member(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.17.10.1.3.{0}".format(arg_dict['mlt_id'])
        data_type = "s"
        value = "{0}".format(arg_dict['port'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_type_split_mlt(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.17.10.1.12.{0}".format(arg_dict['mlt_id'])
        data_type = "i"
        value = "3"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_type_normal_mlt(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.17.10.1.12.{0}".format(arg_dict['mlt_id'])
        data_type = "i"
        value = "1"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_encapsulation_dot1q(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.17.10.1.4.{0}".format(arg_dict['mlt_id'])
        data_type = "i"
        value = "2"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def clear_encapsulation_dot1q(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.17.10.1.4.{0}".format(arg_dict['mlt_id'])
        data_type = "i"
        value = "1"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def show_logical_index(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.2272.1.17.10.1.11.{0}".format(arg_dict['mlt_id'])

        return self.create_cmd_obj(command_type, oid)

    def show_id(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.2272.1.17.10.1.1.{0}".format(arg_dict['mlt_id'])

        return self.create_cmd_obj(command_type, oid)

    def show_admin_type(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.2272.1.17.10.1.12.{0}".format(arg_dict['mlt_id'])

        return self.create_cmd_obj(command_type, oid)

    def show_running_type(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.2272.1.17.10.1.14.{0}".format(arg_dict['mlt_id'])

        return self.create_cmd_obj(command_type, oid)

    def show_flex_uni_status(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.2272.1.17.10.1.49.{0}".format(arg_dict['mlt_id'])

        return self.create_cmd_obj(command_type, oid)

    def show_lacp_admin_status(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.2272.1.17.10.1.18.{0}".format(arg_dict['mlt_id'])

        return self.create_cmd_obj(command_type, oid)

    def show_lacp_oper_status(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.2272.1.17.10.1.22.{0}".format(arg_dict['mlt_id'])

        return self.create_cmd_obj(command_type, oid)

    def show_ports(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.2272.1.17.10.1.3.{0}".format(arg_dict['mlt_id'])

        return self.create_cmd_obj(command_type, oid)

    def show_encapsulation(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.2272.1.17.10.1.4.{0}".format(arg_dict['mlt_id'])

        return self.create_cmd_obj(command_type, oid)
