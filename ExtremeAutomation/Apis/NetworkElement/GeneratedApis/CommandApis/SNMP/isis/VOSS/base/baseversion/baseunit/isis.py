"""
All isis supported SNMP commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.SNMP.isis.base.isisbase import IsisBase


class Isis(DeviceApi, IsisBase):
    def __init__(self, device):
        super(Isis, self).__init__(device)
        self.device = device

    def enable_global(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.3.37.1.1.1.8.0"
        data_type = "i"
        value = "1"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def disable_global(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.3.37.1.1.1.8.0"
        data_type = "i"
        value = "2"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_system_id(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.3.37.1.1.1.3.0"
        data_type = "s"
        value = "{0}".format(arg_dict['sys_id'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def clear_system_id(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.3.37.1.1.1.3.0"
        data_type = "s"
        value = "0x100000000000"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_manual_area(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.3.37.1.1.2.1.2.{0}".format(arg_dict['manual_area'])
        data_type = "i"
        value = "4"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def clear_manual_area(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.3.37.1.1.2.1.2.{0}".format(arg_dict['manual_area'])
        data_type = "i"
        value = "6"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_sys_name(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.63.1.10.0"
        data_type = "s"
        value = "{0}".format(arg_dict['name'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def clear_sys_name(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.63.1.10.0"
        data_type = "s"
        value = ""

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_ipv4_source_address(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.63.1.13.0"
        data_type = "s"
        value = "{0}".format(arg_dict['ip'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def clear_ipv4_source_address(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.63.1.13.0"
        data_type = "s"
        value = "0.0.0.0"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_ipv6_source_address(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.63.1.15.0"
        data_type = "s"
        value = "{0}".format(arg_dict['ipv6_addr'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def clear_ipv6_source_address(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.63.1.15.0"
        data_type = "s"
        value = "::"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_ipv4_tunnel_source_address(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.63.1.17.0"
        data_type = "a"
        value = "{0}".format(arg_dict['ip'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def clear_ipv4_tunnel_source_address(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.63.1.17.0"
        data_type = "a"
        value = "0.0.0.0"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_redistribute_bgp(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.8.100.22.1.15.{0}".format(arg_dict['oid_index'])
        data_type = "i"
        value = "4"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def clear_redistribute_bgp(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.8.100.22.1.15.{0}".format(arg_dict['oid_index'])
        data_type = "i"
        value = "6"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def enable_redistribute_bgp(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.8.100.22.1.5.{0}".format(arg_dict['oid_index'])
        data_type = "i"
        value = "1"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def disable_redistribute_bgp(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.8.100.22.1.5.{0}".format(arg_dict['oid_index'])
        data_type = "i"
        value = "2"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_redistribute_direct(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.8.100.22.1.15.0.3.0.1"
        data_type = "i"
        value = "4"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def clear_redistribute_direct(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.8.100.22.1.15.0.3.0.1"
        data_type = "i"
        value = "6"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def enable_redistribute_direct(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.8.100.22.1.5.0.3.0.1"
        data_type = "i"
        value = "1"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def disable_redistribute_direct(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.8.100.22.1.5.0.3.0.1"
        data_type = "i"
        value = "2"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def enable_redistribute_direct_ipv6(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.8.100.22.1.5.0.12.0.1"
        data_type = "i"
        value = "1"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def disable_redistribute_direct_ipv6(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.8.100.22.1.5.0.12.0.1"
        data_type = "i"
        value = "2"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_redistribute_direct_apply(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.8.100.22.1.5.0.3.0.1||" \
              "1.3.6.1.4.1.2272.1.8.100.15.0"
        data_type = "i||i"
        value = "1||1"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_redistribute_direct_route_map_policy(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.8.100.22.1.11.0.3.0.1"
        data_type = "s"
        value = "{0}".format(arg_dict['policy_name'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def clear_redistribute_direct_route_map_policy(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.8.100.22.1.11.0.3.0.1"
        data_type = "s"
        value = ""

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_redistribute_ospf(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.8.100.22.1.15.{0}".format(arg_dict['oid_index'])
        data_type = "i"
        value = "4"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def clear_redistribute_ospf(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.8.100.22.1.15.{0}".format(arg_dict['oid_index'])
        data_type = "i"
        value = "6"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def enable_redistribute_ospf(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.8.100.22.1.5.{0}".format(arg_dict['oid_index'])
        data_type = "i"
        value = "1"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def disable_redistribute_ospf(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.8.100.22.1.5.{0}".format(arg_dict['oid_index'])
        data_type = "i"
        value = "2"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_redistribute_rip(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.8.100.22.1.15.{0}".format(arg_dict['oid_index'])
        data_type = "i"
        value = "4"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def clear_redistribute_rip(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.8.100.22.1.15.{0}".format(arg_dict['oid_index'])
        data_type = "i"
        value = "6"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def enable_redistribute_rip(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.8.100.22.1.5.{0}".format(arg_dict['oid_index'])
        data_type = "i"
        value = "1"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def disable_redistribute_rip(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.8.100.22.1.5.{0}".format(arg_dict['oid_index'])
        data_type = "i"
        value = "2"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_redistribute_static(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.8.100.22.1.15.{0}".format(arg_dict['oid_index'])
        data_type = "i"
        value = "4"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def clear_redistribute_static(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.8.100.22.1.15.{0}".format(arg_dict['oid_index'])
        data_type = "i"
        value = "6"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def enable_redistribute_static(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.8.100.22.1.5.{0}".format(arg_dict['oid_index'])
        data_type = "i"
        value = "1"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def disable_redistribute_static(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.8.100.22.1.5.{0}".format(arg_dict['oid_index'])
        data_type = "i"
        value = "2"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_redistribute_apply(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.8.100.15.{0}".format(arg_dict['oid_index'])
        data_type = "i"
        value = "1"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_circuit_on_port(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.3.37.1.3.2.1.2.{0}||" \
              "1.3.6.1.3.37.1.3.2.1.3.{0}||" \
              "1.3.6.1.3.37.1.3.2.1.4.{0}".format(arg_dict['isis_circuit'])
        data_type = "i||i||i"
        value = "{0}||2||4".format(arg_dict['port'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def enable_circuit_on_port(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.3.37.1.3.2.1.3.{0}".format(arg_dict['port'])
        data_type = "i"
        value = "1"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def disable_circuit_on_port(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.3.37.1.3.2.1.3.{0}".format(arg_dict['port'])
        data_type = "i"
        value = "2"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def clear_circuit_on_port(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.3.37.1.3.2.1.4.{0}".format(arg_dict['port'])
        data_type = "i"
        value = "6"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_circuit_on_mlt(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.3.37.1.3.2.1.2.{0}||" \
              "1.3.6.1.3.37.1.3.2.1.3.{0}||" \
              "1.3.6.1.3.37.1.3.2.1.4.{0}".format(arg_dict['isis_circuit'])
        data_type = "i||i||i"
        value = "{0}||2||4".format(arg_dict['mlt_id'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def enable_circuit_on_mlt(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.3.37.1.3.2.1.3.{0}".format(arg_dict['mlt_id'])
        data_type = "i"
        value = "1"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def disable_circuit_on_mlt(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.3.37.1.3.2.1.3.{0}".format(arg_dict['mlt_id'])
        data_type = "i"
        value = "2"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def clear_circuit_on_mlt(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.3.37.1.3.2.1.4.{0}".format(arg_dict['mlt_id'])
        data_type = "i"
        value = "6"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_auth_on_port(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.63.2.1.3.{0}||" \
              "1.3.6.1.4.1.2272.1.63.2.1.4.{0}||" \
              "1.3.6.1.4.1.2272.1.63.2.1.5.{0}".format(arg_dict['port'])
        data_type = "i||i||s"
        value = "{0}||{1}||{2}".format(arg_dict['auth_type'],
                                       arg_dict['key_id'],
                                       arg_dict['auth_key'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_auth_on_mlt(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.63.2.1.3.{0}||" \
              "1.3.6.1.4.1.2272.1.63.2.1.4.{0}||" \
              "1.3.6.1.4.1.2272.1.63.2.1.5.{0}".format(arg_dict['mlt_id'])
        data_type = "i||i||s"
        value = "{0}||{1}||{2}".format(arg_dict['auth_type'],
                                       arg_dict['key_id'],
                                       arg_dict['auth_key'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def clear_auth_on_port(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.63.2.1.3.{0}".format(arg_dict['port'])
        data_type = "i"
        value = "0"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def clear_auth_on_mlt(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.63.2.1.3.{0}".format(arg_dict['mlt_id'])
        data_type = "i"
        value = "0"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_l1_dr_priority_on_port(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.3.37.1.4.1.1.4.{0}".format(arg_dict['port'])
        data_type = "u"
        value = "{0}".format(arg_dict['priority'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_l1_dr_priority_on_mlt(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.3.37.1.4.1.1.4.{0}".format(arg_dict['mlt_id'])
        data_type = "u"
        value = "{0}".format(arg_dict['priority'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_l1_hello_interval_on_port(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.3.37.1.4.1.1.9.{0}".format(arg_dict['port'])
        data_type = "u"
        value = "{0}".format(arg_dict['interval'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_l1_hello_interval_on_mlt(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.3.37.1.4.1.1.9.{0}".format(arg_dict['mlt_id'])
        data_type = "u"
        value = "{0}".format(arg_dict['interval'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_l1_hello_multiplier_on_port(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.3.37.1.4.1.1.8.{0}".format(arg_dict['port'])
        data_type = "u"
        value = "{0}".format(arg_dict['multiplier'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_l1_hello_multiplier_on_mlt(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.3.37.1.4.1.1.8.{0}".format(arg_dict['mlt_id'])
        data_type = "u"
        value = "{0}".format(arg_dict['multiplier'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_logical_interface_port(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.63.26.1.5.{0}||" \
              "1.3.6.1.4.1.2272.1.63.26.1.6.{0}||" \
              "1.3.6.1.4.1.2272.1.63.26.1.7.{0}||" \
              "1.3.6.1.4.1.2272.1.63.26.1.9.{0}".format(arg_dict['isis_id'])
        data_type = "i||s||i||i"
        value = "{0}||{1}||{2}||4".format(arg_dict['port'],
                                          arg_dict['primary_vlan'],
                                          arg_dict['primary_vlan'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_logical_interface_port_name(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.63.26.1.5.{0}||" \
              "1.3.6.1.4.1.2272.1.63.26.1.6.{0}||" \
              "1.3.6.1.4.1.2272.1.63.26.1.7.{0}||" \
              "1.3.6.1.4.1.2272.1.63.26.1.8.{0}||" \
              "1.3.6.1.4.1.2272.1.63.26.1.9.{0}".format(arg_dict['isis_id'])
        data_type = "i||s||i||s||i"
        value = "{0}||{1}||{2}||{3}||4".format(arg_dict['port'],
                                               arg_dict['primary_vlan'],
                                               arg_dict['primary_vlan'],
                                               arg_dict['name'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_logical_interface_mlt(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.63.26.1.5.{0}||" \
              "1.3.6.1.4.1.2272.1.63.26.1.6.{0}||" \
              "1.3.6.1.4.1.2272.1.63.26.1.7.{0}||" \
              "1.3.6.1.4.1.2272.1.63.26.1.9.{0}".format(arg_dict['isis_id'])
        data_type = "i||s||i||i"
        value = "{0}||{1}||{2}||4".format(arg_dict['mlt_id'],
                                          arg_dict['primary_vlan'],
                                          arg_dict['primary_vlan'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_logical_interface_mlt_name(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.63.26.1.5.{0}||" \
              "1.3.6.1.4.1.2272.1.63.26.1.6.{0}||" \
              "1.3.6.1.4.1.2272.1.63.26.1.7.{0}||" \
              "1.3.6.1.4.1.2272.1.63.26.1.8.{0}||" \
              "1.3.6.1.4.1.2272.1.63.26.1.9.{0}".format(arg_dict['isis_id'])
        data_type = "i||s||i||s||i"
        value = "{0}||{1}||{2}||{3}||4".format(arg_dict['mlt_id'],
                                               arg_dict['primary_vlan'],
                                               arg_dict['primary_vlan'],
                                               arg_dict['name'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_logical_interface_ipv4(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.63.26.1.4.{0}||" \
              "1.3.6.1.4.1.2272.1.63.26.1.9.{0}".format(arg_dict['isis_id'])
        data_type = "a||i"
        value = "{0}||4".format(arg_dict['ip'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_logical_interface_ipv4_name(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.63.26.1.4.{0}||" \
              "1.3.6.1.4.1.2272.1.63.26.1.8.{0}||" \
              "1.3.6.1.4.1.2272.1.63.26.1.9.{0}".format(arg_dict['isis_id'])
        data_type = "a||s||i"
        value = "{0}||{1}||4".format(arg_dict['ip'],
                                     arg_dict['name'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def clear_logical_interface(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.63.26.1.9.{0}".format(arg_dict['isis_id'])
        data_type = "i"
        value = "6"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_circuit_on_logical_interface(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.3.37.1.3.2.1.2.{0}||" \
              "1.3.6.1.3.37.1.3.2.1.3.{0}||" \
              "1.3.6.1.3.37.1.3.2.1.4.{0}".format(arg_dict['isis_id'])
        data_type = "i||i||i"
        value = "{0}||2||4".format(arg_dict['isis_id'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def enable_circuit_on_logical_interface(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.3.37.1.3.2.1.3.{0}".format(arg_dict['isis_id'])
        data_type = "i"
        value = "1"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def disable_circuit_on_logical_interface(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.3.37.1.3.2.1.3.{0}".format(arg_dict['isis_id'])
        data_type = "i"
        value = "2"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def clear_circuit_on_logical_interface(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.3.37.1.3.2.1.4.{0}".format(arg_dict['isis_id'])
        data_type = "i"
        value = "6"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_auth_on_logical_interface(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.63.2.1.3.{0}||" \
              "1.3.6.1.4.1.2272.1.63.2.1.4.{0}||" \
              "1.3.6.1.4.1.2272.1.63.2.1.5.{0}".format(arg_dict['isis_id'])
        data_type = "i||i||s"
        value = "{0}||{1}||{2}".format(arg_dict['auth_type'],
                                       arg_dict['key_id'],
                                       arg_dict['auth_key'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def clear_auth_on_logical_interface(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.63.2.1.3.{0}".format(arg_dict['isis_id'])
        data_type = "i"
        value = "0"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_l1_dr_priority_on_logical_interface(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.3.37.1.4.1.1.4.{0}".format(arg_dict['isis_id'])
        data_type = "u"
        value = "{0}".format(arg_dict['priority'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_l1_hello_interval_on_logical_interface(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.3.37.1.4.1.1.9.{0}".format(arg_dict['isis_id'])
        data_type = "u"
        value = "{0}".format(arg_dict['interval'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_l1_hello_multiplier_on_logical_interface(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.3.37.1.4.1.1.8.{0}".format(arg_dict['isis_id'])
        data_type = "u"
        value = "{0}".format(arg_dict['multiplier'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def show_circuit(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.3.37.1.3.1.{0}".format(arg_dict['isis_circuit'])

        return self.create_cmd_obj(command_type, oid)

    def show_circuit_interfaces(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.3.37.1.3.2.1.2"

        return self.create_cmd_obj(command_type, oid)

    def show_info(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.3.37.1.1||" \
              "1.3.6.1.4.1.2272.1.63.1"

        return self.create_cmd_obj(command_type, oid)

    def show_interface(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.3.37.1.3.2.1||" \
              "1.3.6.1.4.1.2272.1.63.2.1"

        return self.create_cmd_obj(command_type, oid)

    def show_area(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.3.37.1.1.3.1.1"

        return self.create_cmd_obj(command_type, oid)

    def show_lsdb(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.3.37.1.9"

        return self.create_cmd_obj(command_type, oid)

    def show_manual_area(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.3.37.1.1.2.1.2"

        return self.create_cmd_obj(command_type, oid)

    def show_spb_mcast_summary(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.4.1.2272.1.63.14||" \
              "1.3.6.1.4.1.2272.1.63.24"

        return self.create_cmd_obj(command_type, oid)

    def show_statistics(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.3.37.1.5"

        return self.create_cmd_obj(command_type, oid)

    def show_sys_id(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.3.37.1.1.1.3.0"

        return self.create_cmd_obj(command_type, oid)

    def show_adjacencies(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.4.1.2272.1.63.10||" \
              "1.3.6.1.3.37.1.6"

        return self.create_cmd_obj(command_type, oid)

    def show_interface_auth(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.4.1.2272.1.63.2"

        return self.create_cmd_obj(command_type, oid)

    def show_interface_timers(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.3.37.1.4.1"

        return self.create_cmd_obj(command_type, oid)

    def show_system_stats(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.3.37.1.5.1"

        return self.create_cmd_obj(command_type, oid)

    def show_logical_interface(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.4.1.2272.1.63.26"

        return self.create_cmd_obj(command_type, oid)

    def show_logical_interface_name(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.4.1.2272.1.63.26.1.8"

        return self.create_cmd_obj(command_type, oid)

    def show_interface_stats(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.3.37.1.5.2"

        return self.create_cmd_obj(command_type, oid)

    def show_interface_l1_packet_stats(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.3.37.1.5.3"

        return self.create_cmd_obj(command_type, oid)

    def show_interface_l2_packet_stats(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.3.37.1.5.3"

        return self.create_cmd_obj(command_type, oid)

    def show_ip_redistribute(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.4.1.2272.1.8.100.22"

        return self.create_cmd_obj(command_type, oid)
