"""
All ospf supported SNMP commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.SNMP.ospf.base.ospfbase import OspfBase


class Ospf(DeviceApi, OspfBase):
    def __init__(self, device):
        super(Ospf, self).__init__(device)
        self.device = device

    def enable_global(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.2.1.14.1.2.0"
        data_type = "i"
        value = "1"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def disable_global(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.2.1.14.1.2.0"
        data_type = "i"
        value = "2"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_router_id(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.2.1.14.1.1.0"
        data_type = "a"
        value = "{0}".format(arg_dict['router_id'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def clear_router_id(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.2.1.14.1.1.0"
        data_type = "a"
        value = "0.0.0.0"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def enable_interface(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.8.1.1.1.6.{0}".format(arg_dict['interface'])
        data_type = "i"
        value = "1"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def disable_interface(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.8.1.1.1.6.{0}".format(arg_dict['interface'])
        data_type = "i"
        value = "2"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def enable_vlan(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.8.1.1.1.6.{0}".format(arg_dict['vlan'])
        data_type = "i"
        value = "1"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def disable_vlan(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.8.1.1.1.6.{0}".format(arg_dict['vlan'])
        data_type = "i"
        value = "2"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def show_info(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.2.1.14.1||" \
              "1.3.6.1.4.1.2272.1.8.1.3||" \
              "1.3.6.1.4.1.2272.1.8.1.4"

        return self.create_cmd_obj(command_type, oid)

    def show_vlan_interface(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.2.1.14.7||" \
              "1.3.6.1.4.1.2272.1.8.1.1.1.6"

        return self.create_cmd_obj(command_type, oid)

    def show_interface(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.2.1.14.7||" \
              "1.3.6.1.4.1.2272.1.8.1.1.1.6"

        return self.create_cmd_obj(command_type, oid)
