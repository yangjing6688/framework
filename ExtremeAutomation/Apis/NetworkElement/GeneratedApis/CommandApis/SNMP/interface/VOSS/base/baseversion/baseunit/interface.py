"""
All interface supported SNMP commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.SNMP.interface.base.interfacebase import \
    InterfaceBase


class Interface(DeviceApi, InterfaceBase):
    def __init__(self, device):
        super(Interface, self).__init__(device)
        self.device = device

    def enable_ipv6_forwarding(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.2.1.4.30.1.5.{0}".format(arg_dict['interface'])
        data_type = "i"
        value = "1"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def disable_ipv6_forwarding(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.2.1.4.30.1.5.{0}".format(arg_dict['interface'])
        data_type = "i"
        value = "2"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_ipv4_primary_addr_prefix(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.8.2.1.3.{0}||" \
              "1.3.6.1.4.1.2272.1.8.2.1.6.{0}||" \
              "1.3.6.1.4.1.2272.1.8.2.1.7.{0}||" \
              "1.3.6.1.4.1.2272.1.8.2.1.9.{0}||" \
              "1.3.6.1.4.1.2272.1.8.2.1.12.{0}".format(arg_dict['interface'])
        data_type = "a||i||i||i||u"
        value = "{0}||4||{1}||0||0".format(arg_dict['netmask'],
                                           arg_dict['interface'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_ipv4_primary_addr_netmask(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.8.2.1.3.{0}||" \
              "1.3.6.1.4.1.2272.1.8.2.1.6.{0}||" \
              "1.3.6.1.4.1.2272.1.8.2.1.7.{0}||" \
              "1.3.6.1.4.1.2272.1.8.2.1.9.{0}||" \
              "1.3.6.1.4.1.2272.1.8.2.1.12.{0}".format(arg_dict['interface'])
        data_type = "a||i||i||i||u"
        value = "{0}||4||{1}||0||0".format(arg_dict['netmask'],
                                           arg_dict['interface'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_ipv4_loopback_addr_netmask(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.8.2.1.3.{0}||" \
              "1.3.6.1.4.1.2272.1.8.2.1.6.{0}||" \
              "1.3.6.1.4.1.2272.1.8.2.1.7.{0}||" \
              "1.3.6.1.4.1.2272.1.8.2.1.9.{0}||" \
              "1.3.6.1.4.1.2272.1.8.2.1.12.{0}".format(arg_dict['interface'])
        data_type = "a||i||i||i||u"
        value = "{0}||4||0||0||0".format(arg_dict['netmask'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_ipv6_loopback_address(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.62.1.1.3.1.4.{0}||" \
              "1.3.6.1.4.1.2272.1.62.1.1.3.1.10.{0}".format(arg_dict['voss_oid_index'])
        data_type = "i||i"
        value = "{0}||4".format(arg_dict['prefix'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def clear_ipv4_addr_prefix(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.8.2.1.6.{0}".format(arg_dict['interface'])
        data_type = "i"
        value = "6"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def clear_ipv4_loopback_addr_netmask(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.8.2.1.6.{0}".format(arg_dict['interface'])
        data_type = "i"
        value = "6"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def clear_ipv6_loopback_address(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.62.1.1.3.1.10.{0}".format(arg_dict['interface'])
        data_type = "i"
        value = "6"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def enable_ip_forwarding_global(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.2.1.4.1.0"
        data_type = "i"
        value = "1"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def disable_ip_forwarding_global(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.2.1.4.1.0"
        data_type = "i"
        value = "2"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def enable_ipv6_forwarding_global(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.2.1.4.25.0"
        data_type = "i"
        value = "1"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def disable_ipv6_forwarding_global(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.2.1.4.25.0"
        data_type = "i"
        value = "2"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def enable_chassis_force_topology_ip_flag(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.4.53.0"
        data_type = "i"
        value = "1"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def disable_chassis_force_topology_ip_flag(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.4.53.0"
        data_type = "i"
        value = "2"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_ipv4_brouter_port(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.8.2.1.3.{0}||" \
              "1.3.6.1.4.1.2272.1.8.2.1.6.{0}||" \
              "1.3.6.1.4.1.2272.1.8.2.1.7.{0}||" \
              "1.3.6.1.4.1.2272.1.8.2.1.9.{0}||" \
              "1.3.6.1.4.1.2272.1.8.2.1.12.{0}".format(arg_dict['port'])
        data_type = "a||i||i||i||u"
        value = "{0}||4||{1}||{2}||0".format(arg_dict['netmask'],
                                             arg_dict['vlan'],
                                             arg_dict['mac_offset'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def clear_ipv4_brouter_port(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.8.2.1.6.{0}".format(arg_dict['port'])
        data_type = "i"
        value = "6"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def show_loopback_info(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.4.1.2272.1.8.2||" \
              "1.3.6.1.4.1.2272.1.62.1.1.3"

        return self.create_cmd_obj(command_type, oid)

    def show_brouter_port_vlan(self, arg_dict, **kwargs):
        command_type = "snmpgetnext"
        oid = "1.3.6.1.4.1.2272.1.8.2.1.7.{0}".format(arg_dict['port'])

        return self.create_cmd_obj(command_type, oid)

    def show_brouter_port_ipv4(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.2272.1.8.2.1.2.{0}".format(arg_dict['port'])

        return self.create_cmd_obj(command_type, oid)

    def show_chassis_force_topology_ip_flag(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.2272.1.4.53.0"

        return self.create_cmd_obj(command_type, oid)
