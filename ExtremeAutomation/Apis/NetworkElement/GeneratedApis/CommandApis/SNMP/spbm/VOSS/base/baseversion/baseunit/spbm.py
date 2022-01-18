"""
All spbm supported SNMP commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.SNMP.spbm.base.spbmbase import SpbmBase


class Spbm(DeviceApi, SpbmBase):
    def __init__(self, device):
        super(Spbm, self).__init__(device)
        self.device = device

    def set_ethertype(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.78.1.4.0"
        data_type = "i"
        value = "{0}".format(arg_dict['ethertype'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def clear_ethertype(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.78.1.4.0"
        data_type = "i"
        value = "33024"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def enable_global(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.78.1.2.0"
        data_type = "i"
        value = "1"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def disable_global(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.78.1.2.0"
        data_type = "i"
        value = "2"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def enable_ip_shortcut(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.63.4.1.7.{0}".format(arg_dict['spbm_id'])
        data_type = "i"
        value = "1"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def disable_ip_shortcut(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.63.4.1.7.{0}".format(arg_dict['spbm_id'])
        data_type = "i"
        value = "2"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def enable_ipv6_shortcut(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.63.4.1.14.{0}".format(arg_dict['spbm_id'])
        data_type = "i"
        value = "1"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def disable_ipv6_shortcut(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.63.4.1.14.{0}".format(arg_dict['spbm_id'])
        data_type = "i"
        value = "2"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def enable_lsdb_trap(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.63.4.1.5.{0}".format(arg_dict['spbm_id'])
        data_type = "i"
        value = "1"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def disable_lsdb_trap(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.63.4.1.5.{0}".format(arg_dict['spbm_id'])
        data_type = "i"
        value = "2"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_isis_instance_id(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.63.4.1.2.{0}".format(arg_dict['spbm_id'])
        data_type = "i"
        value = "4"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def clear_isis_instance_id(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.63.4.1.2.{0}".format(arg_dict['spbm_id'])
        data_type = "i"
        value = "6"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_isis_nickname(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.63.4.1.3.{0}".format(arg_dict['spbm_id'])
        data_type = "s"
        value = "{0}".format(arg_dict['nickname'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def clear_isis_nickname(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.63.4.1.3.{0}".format(arg_dict['spbm_id'])
        data_type = "s"
        value = "{0}".format(arg_dict['nickname'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_isis_bvid(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.63.4.1.4.{0}||" \
              "1.3.6.1.4.1.2272.1.63.4.1.8.{0}".format(arg_dict['spbm_id'])
        data_type = "s||i"
        value = "{0}||{1}".format(arg_dict['sec_vlan'],
                                  arg_dict['pri_vlan'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def clear_isis_bvid(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.63.4.1.4.{0}".format(arg_dict['spbm_id'])
        data_type = "s"
        value = "{0}".format(arg_dict['pri_vlan'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def enable_isis_multicast(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.63.4.1.12.{0}".format(arg_dict['spbm_id'])
        data_type = "i"
        value = "1"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def disable_isis_multicast(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.63.4.1.12.{0}".format(arg_dict['spbm_id'])
        data_type = "i"
        value = "2"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_isis_multicast_fwd_cache_timeout(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.63.4.1.13.{0}".format(arg_dict['spbm_id'])
        data_type = "i"
        value = "{0}".format(arg_dict['timeout'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def clear_isis_multicast_fwd_cache_timeout(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.63.4.1.13.{0}".format(arg_dict['spbm_id'])
        data_type = "i"
        value = "210"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_isis_smlt_virtual_bmac(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.63.4.1.10.{0}".format(arg_dict['spbm_id'])
        data_type = "s"
        value = "{0}".format(arg_dict['bmac'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def clear_isis_smlt_virtual_bmac(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.63.4.1.10.{0}".format(arg_dict['spbm_id'])
        data_type = "s"
        value = "{0}".format(arg_dict['bmac'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_isis_smlt_peer_system_id(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.63.4.1.11.{0}".format(arg_dict['spbm_id'])
        data_type = "s"
        value = "{0}".format(arg_dict['peer_id'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def clear_isis_smlt_peer_system_id(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.63.4.1.11.{0}".format(arg_dict['spbm_id'])
        data_type = "s"
        value = "{0}".format(arg_dict['peer_id'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_port_isis_instance_id(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.63.5.1.3.{1}.{0}||" \
              "1.3.6.1.4.1.2272.1.63.5.1.4.{1}.{0}".format(arg_dict['spbm_id'],
                                                           arg_dict['port'])
        data_type = "i||i"
        value = "4||1"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def clear_port_isis_instance_id(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.63.5.1.3.{1}.{0}".format(arg_dict['spbm_id'],
                                             arg_dict['port'])
        data_type = "i"
        value = "6"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_mlt_isis_instance_id(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.63.5.1.3.{0}.{1}||" \
              "1.3.6.1.4.1.2272.1.63.5.1.4.{0}.{1}".format(arg_dict['mlt_id'],
                                                           arg_dict['spbm_id'])
        data_type = "i||i"
        value = "4||1"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def clear_mlt_isis_instance_id(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.63.5.1.3.{0}.{1}".format(arg_dict['mlt_id'],
                                             arg_dict['spbm_id'])
        data_type = "i"
        value = "6"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_port_isis_interface_type_broadcast(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.63.5.1.5.{1}.{0}".format(arg_dict['spbm_id'],
                                             arg_dict['port'])
        data_type = "i"
        value = "1"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_port_isis_interface_type_p2p(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.63.5.1.5.{1}.{0}".format(arg_dict['spbm_id'],
                                             arg_dict['port'])
        data_type = "i"
        value = "2"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def clear_port_isis_interface_type(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.63.5.1.5.{1}.{0}".format(arg_dict['spbm_id'],
                                             arg_dict['port'])
        data_type = "i"
        value = "2"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_mlt_isis_interface_type_broadcast(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.63.5.1.5.{0}.{1}".format(arg_dict['mlt_id'],
                                             arg_dict['spbm_id'])
        data_type = "i"
        value = "1"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_mlt_isis_interface_type_p2p(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.63.5.1.5.{0}.{1}".format(arg_dict['mlt_id'],
                                             arg_dict['spbm_id'])
        data_type = "i"
        value = "2"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def clear_mlt_isis_interface_type(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.63.5.1.5.{0}.{1}".format(arg_dict['mlt_id'],
                                             arg_dict['spbm_id'])
        data_type = "i"
        value = "2"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_port_isis_l1_metric(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.63.5.1.7.{1}.{0}".format(arg_dict['spbm_id'],
                                             arg_dict['port'])
        data_type = "i"
        value = "{0}".format(arg_dict['metric'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def clear_port_isis_l1_metric(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.63.5.1.7.{1}.{0}".format(arg_dict['spbm_id'],
                                             arg_dict['port'])
        data_type = "i"
        value = "10"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_mlt_isis_l1_metric(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.63.5.1.7.{0}.{1}".format(arg_dict['mlt_id'],
                                             arg_dict['spbm_id'])
        data_type = "i"
        value = "{0}".format(arg_dict['metric'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def clear_mlt_isis_l1_metric(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.63.5.1.7.{0}.{1}".format(arg_dict['mlt_id'],
                                             arg_dict['spbm_id'])
        data_type = "i"
        value = "10"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_logical_interface_isis_instance_id(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.63.5.1.3.{0}.{1}||" \
              "1.3.6.1.4.1.2272.1.63.5.1.4.{0}.{1}".format(arg_dict['isis_id'],
                                                           arg_dict['spbm_id'])
        data_type = "i||i"
        value = "4||1"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def clear_logical_interface_isis_instance_id(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.63.5.1.3.{0}.{1}".format(arg_dict['isis_id'],
                                             arg_dict['spbm_id'])
        data_type = "i"
        value = "6"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_logical_interface_isis_interface_type_broadcast(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.63.5.1.5.{0}.{1}".format(arg_dict['isis_id'],
                                             arg_dict['spbm_id'])
        data_type = "i"
        value = "1"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_logical_interface_isis_interface_type_p2p(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.63.5.1.5.{0}.{1}".format(arg_dict['isis_id'],
                                             arg_dict['spbm_id'])
        data_type = "i"
        value = "2"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def clear_logical_interface_isis_interface_type(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.63.5.1.5.{0}.{1}".format(arg_dict['isis_id'],
                                             arg_dict['spbm_id'])
        data_type = "i"
        value = "2"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_logical_interface_isis_l1_metric(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.63.5.1.7.{0}.{1}".format(arg_dict['isis_id'],
                                             arg_dict['spbm_id'])
        data_type = "i"
        value = "{0}".format(arg_dict['metric'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def clear_logical_interface_isis_l1_metric(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.63.5.1.7.{0}.{1}".format(arg_dict['isis_id'],
                                             arg_dict['spbm_id'])
        data_type = "i"
        value = "1000"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def show_info(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.2272.1.78.1.2.0||" \
              "1.3.6.1.4.1.2272.1.78.1.4.0"

        return self.create_cmd_obj(command_type, oid)

    def show_isis_info(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.4.1.2272.1.63.4"

        return self.create_cmd_obj(command_type, oid)

    def show_isis_interface(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.4.1.2272.1.63.2.1||" \
              "1.3.6.1.4.1.2272.1.63.5.1"

        return self.create_cmd_obj(command_type, oid)

    def show_isis_ip_multicast_fib(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.4.1.2272.1.63.27"

        return self.create_cmd_obj(command_type, oid)

    def show_isis_ip_multicast_route(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.4.1.2272.1.63.24"

        return self.create_cmd_obj(command_type, oid)

    def show_isis_ip_multicast_route_all(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.4.1.2272.1.63.24"

        return self.create_cmd_obj(command_type, oid)

    def show_isis_ip_multicast_route_detail(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.4.1.2272.1.63.24"

        return self.create_cmd_obj(command_type, oid)

    def show_isis_ip_unicast_fib(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.4.1.2272.1.63.21"

        return self.create_cmd_obj(command_type, oid)

    def show_isis_ip_unicast_fib_spbm_nh_as_mac(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.4.1.2272.1.63.21"

        return self.create_cmd_obj(command_type, oid)

    def show_isis_multicast(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.2272.1.63.4.1.12.0||" \
              "1.3.6.1.4.1.2272.1.63.4.1.13.0"

        return self.create_cmd_obj(command_type, oid)

    def show_isis_multicast_fib(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.4.1.2272.1.63.14.1"

        return self.create_cmd_obj(command_type, oid)

    def show_isis_multicast_fib_detail(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.4.1.2272.1.63.27"

        return self.create_cmd_obj(command_type, oid)

    def show_isis_unicast_fib(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.4.1.2272.1.63.13"

        return self.create_cmd_obj(command_type, oid)
