"""
All vlan supported SNMP commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.SNMP.vlan.base.vlanbase import VlanBase


class Vlan(DeviceApi, VlanBase):
    def __init__(self, device):
        super(Vlan, self).__init__(device)
        self.device = device

    def create_vlan(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.3.2.1.9.{0}||" \
              "1.3.6.1.4.1.2272.1.3.2.1.10.{0}||" \
              "1.3.6.1.4.1.2272.1.3.2.1.20.{0}".format(arg_dict['vlan'])
        data_type = "i||i||i"
        value = "1||1||4"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def delete_vlan(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.3.2.1.20.{0}".format(arg_dict['vlan'])
        data_type = "i"
        value = "6"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_name(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.3.2.1.2.{0}".format(arg_dict['vlan'])
        data_type = "s"
        value = "{0}".format(arg_dict['name'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_isid(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.3.2.1.61.{0}".format(arg_dict['vlan'])
        data_type = "i"
        value = "{0}".format(arg_dict['i_sid'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def clear_isid(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.3.2.1.61.{0}".format(arg_dict['vlan'])
        data_type = "i"
        value = "0"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def create_spbm(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.3.2.1.9.{0}||" \
              "1.3.6.1.4.1.2272.1.3.2.1.10.{0}||" \
              "1.3.6.1.4.1.2272.1.3.2.1.20.{0}".format(arg_dict['vlan'])
        data_type = "i||i||i"
        value = "63||11||4"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_member(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.3.2.1.11.{0}".format(arg_dict['vlan'])
        data_type = "s"
        value = "{0}".format(arg_dict['port'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def clear_member(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.3.2.1.11.{0}".format(arg_dict['vlan'])
        data_type = "s"
        value = "{0}".format(arg_dict['port'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_port_encapsulation_dot1q(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.3.3.1.4.{0}".format(arg_dict['port'])
        data_type = "i"
        value = "2"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def clear_port_encapsulation_dot1q(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.3.3.1.4.{0}".format(arg_dict['port'])
        data_type = "i"
        value = "1"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def show_all_info(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.4.1.2272.1.3.2"

        return self.create_cmd_obj(command_type, oid)

    def show_name(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.2272.1.3.2.1.2.{0}".format(arg_dict['vlan'])

        return self.create_cmd_obj(command_type, oid)

    def show_names(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.4.1.2272.1.3.2.1.2.1"

        return self.create_cmd_obj(command_type, oid)

    def show_isid(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.2272.1.3.2.1.61.{0}".format(arg_dict['vlan'])

        return self.create_cmd_obj(command_type, oid)

    def show_members_port(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.2272.1.3.2.1.11.{0}".format(arg_dict['vlan'])

        return self.create_cmd_obj(command_type, oid)
