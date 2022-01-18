"""
All port supported SNMP commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.SNMP.port.base.portbase import PortBase


class Port(DeviceApi, PortBase):
    def __init__(self, device):
        super(Port, self).__init__(device)
        self.device = device

    def enable_state(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.2.1.2.2.1.7.{0}".format(arg_dict['port'])
        data_type = "i"
        value = "1"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def disable_state(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.2.1.2.2.1.7.{0}".format(arg_dict['port'])
        data_type = "i"
        value = "2"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_alias(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.2.1.31.1.1.1.18.{0}".format(arg_dict['port'])
        data_type = "s"
        value = "{0}".format(arg_dict['name'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def show_names(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.2.1.31.1.1.1.1"

        return self.create_cmd_obj(command_type, oid)

    def show_alias(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.2.1.31.1.1.1.18.{0}".format(arg_dict['port'])

        return self.create_cmd_obj(command_type, oid)

    def show_admin_status(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.2.1.2.2.1.7."

        return self.create_cmd_obj(command_type, oid)

    def show_oper_status(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.2.1.2.2.1.8."

        return self.create_cmd_obj(command_type, oid)

    def show_info_detail(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.2.1.2.2.1.7."

        return self.create_cmd_obj(command_type, oid)

    def show_mtu(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.2.1.2.2.1.4.{0}".format(arg_dict['port'])

        return self.create_cmd_obj(command_type, oid)

    def show_mac_address(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.2.1.2.2.1.6.{0}".format(arg_dict['port'])

        return self.create_cmd_obj(command_type, oid)

    def show_high_speed(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.2.1.31.1.1.1.15.{0}".format(arg_dict['port'])

        return self.create_cmd_obj(command_type, oid)

    def show_in_octets(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.2.1.2.2.1.10.{0}".format(arg_dict['port'])

        return self.create_cmd_obj(command_type, oid)

    def show_in_unicast_packets(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.2.1.2.2.1.11.{0}".format(arg_dict['port'])

        return self.create_cmd_obj(command_type, oid)

    def show_in_discard_packets(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.2.1.2.2.1.13.{0}".format(arg_dict['port'])

        return self.create_cmd_obj(command_type, oid)

    def show_in_error_packets(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.2.1.2.2.1.14.{0}".format(arg_dict['port'])

        return self.create_cmd_obj(command_type, oid)

    def show_in_unknown_protocol_packets(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.2.1.2.2.1.15.{0}".format(arg_dict['port'])

        return self.create_cmd_obj(command_type, oid)

    def show_out_octets(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.2.1.2.2.1.16.{0}".format(arg_dict['port'])

        return self.create_cmd_obj(command_type, oid)

    def show_out_unicast_packets(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.2.1.2.2.1.17.{0}".format(arg_dict['port'])

        return self.create_cmd_obj(command_type, oid)

    def show_out_discard_packets(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.2.1.2.2.1.19.{0}".format(arg_dict['port'])

        return self.create_cmd_obj(command_type, oid)

    def show_out_error_packets(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.2.1.2.2.1.20.{0}".format(arg_dict['port'])

        return self.create_cmd_obj(command_type, oid)

    def show_in_multicast_packets(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.2.1.31.1.1.1.2.{0}".format(arg_dict['port'])

        return self.create_cmd_obj(command_type, oid)

    def show_in_broadcast_packets(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.2.1.31.1.1.1.3.{0}".format(arg_dict['port'])

        return self.create_cmd_obj(command_type, oid)

    def show_out_multicast_packets(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.2.1.31.1.1.1.4.{0}".format(arg_dict['port'])

        return self.create_cmd_obj(command_type, oid)

    def show_out_broadcast_packets(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.2.1.31.1.1.1.5.{0}".format(arg_dict['port'])

        return self.create_cmd_obj(command_type, oid)

    def show_64_bit_in_octets(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.2.1.31.1.1.1.6.{0}".format(arg_dict['port'])

        return self.create_cmd_obj(command_type, oid)

    def show_64_bit_in_unicast_packets(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.2.1.31.1.1.1.7.{0}".format(arg_dict['port'])

        return self.create_cmd_obj(command_type, oid)

    def show_64_bit_in_multicast_packets(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.2.1.31.1.1.1.8.{0}".format(arg_dict['port'])

        return self.create_cmd_obj(command_type, oid)

    def show_64_bit_in_broadcast_packets(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.2.1.31.1.1.1.9.{0}".format(arg_dict['port'])

        return self.create_cmd_obj(command_type, oid)

    def show_64_bit_out_octets(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.2.1.31.1.1.1.10.{0}".format(arg_dict['port'])

        return self.create_cmd_obj(command_type, oid)

    def show_64_bit_out_unicast_packets(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.2.1.31.1.1.1.11.{0}".format(arg_dict['port'])

        return self.create_cmd_obj(command_type, oid)

    def show_64_bit_out_multicast_packets(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.2.1.31.1.1.1.12.{0}".format(arg_dict['port'])

        return self.create_cmd_obj(command_type, oid)

    def show_64_bit_out_broadcast_packets(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.2.1.31.1.1.1.13.{0}".format(arg_dict['port'])

        return self.create_cmd_obj(command_type, oid)

    def show_dot1d_ifindex(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.2.1.17.1.4.1.2"

        return self.create_cmd_obj(command_type, oid)
