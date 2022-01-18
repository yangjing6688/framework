"""
All acl supported SNMP commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.SNMP.acl.base.aclbase import AclBase


class Acl(DeviceApi, AclBase):
    def __init__(self, device):
        super(Acl, self).__init__(device)
        self.device = device

    def create_ipv4(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.202.1.1.2.3.1.1.11.{0}||" \
              "1.3.6.1.4.1.2272.1.202.1.1.2.3.1.1.13.{0}||" \
              "1.3.6.1.4.1.2272.1.202.1.1.2.3.1.1.3.{0}||" \
              "1.3.6.1.4.1.2272.1.202.1.1.2.3.1.1.4.{0}".format(arg_dict['acl_id'])
        data_type = "i||i||s||i"
        value = "4||3||{0}||{1}".format(arg_dict['name'],
                                        arg_dict['voss_acl_type'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def create_ipv6(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.202.1.1.2.3.1.1.11.{0}||" \
              "1.3.6.1.4.1.2272.1.202.1.1.2.3.1.1.13.{0}||" \
              "1.3.6.1.4.1.2272.1.202.1.1.2.3.1.1.3.{0}||" \
              "1.3.6.1.4.1.2272.1.202.1.1.2.3.1.1.4.{0}".format(arg_dict['acl_id'])
        data_type = "i||i||s||i"
        value = "4||2||{0}||{1}".format(arg_dict['name'],
                                        arg_dict['voss_acl_type'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def delete_list(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.202.1.1.2.3.1.1.11.{0}".format(arg_dict['acl_id'])
        data_type = "i"
        value = "6"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def create_ace_index(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.202.1.1.2.4.1.1.19.{0}||" \
              "1.3.6.1.4.1.2272.1.202.1.1.2.4.1.1.3.{0}".format(arg_dict['acl_id'])
        data_type = "i||s"
        value = "4||{0}".format(arg_dict['ace_name'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def delete_ace_index(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.202.1.1.2.4.1.1.19.{0}".format(arg_dict['acl_id'])
        data_type = "i"
        value = "6"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def enable_list(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.202.1.1.2.3.1.1.8.{0}".format(arg_dict['acl_id'])
        data_type = "i"
        value = "1"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def disable_list(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.202.1.1.2.3.1.1.8.{0}".format(arg_dict['acl_id'])
        data_type = "i"
        value = "2"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def enable_ace(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.202.1.1.2.4.1.1.10.{1}.{0}".format(arg_dict['ace_index'],
                                                       arg_dict['acl_id'])
        data_type = "i"
        value = "1"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def disable_ace(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.202.1.1.2.4.1.1.10.{1}.{0}".format(arg_dict['ace_index'],
                                                       arg_dict['acl_id'])
        data_type = "i"
        value = "2"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_name(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.202.1.1.2.3.1.1.3.{0}".format(arg_dict['acl_id'])
        data_type = "s"
        value = "{0}".format(arg_dict['name'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_default_action(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.202.1.1.2.3.1.1.6.{0}".format(arg_dict['acl_id'])
        data_type = "i"
        value = "{0}".format(arg_dict['action'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_port(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.202.1.1.2.3.1.1.10.{0}".format(arg_dict['acl_id'])
        data_type = "s"
        value = "{0}".format(arg_dict['port'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def clear_port(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.202.1.1.2.3.1.1.10.{0}".format(arg_dict['acl_id'])
        data_type = "s"
        value = "{0}".format(arg_dict['port'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_vlan(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.202.1.1.2.3.1.1.9.{0}".format(arg_dict['acl_id'])
        data_type = "s"
        value = "{0}".format(arg_dict['vlan'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def clear_vlan(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.202.1.1.2.3.1.1.9.{0}".format(arg_dict['acl_id'])
        data_type = "s"
        value = "{0}".format(arg_dict['vlan'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_ace_action(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.202.1.1.2.4.1.1.4.{1}.{0}".format(arg_dict['ace_index'],
                                                      arg_dict['acl_id'])
        data_type = "i"
        value = "{0}".format(arg_dict['ace_action'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_ace_name(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.202.1.1.2.4.1.1.3.{1}.{0}".format(arg_dict['ace_index'],
                                                      arg_dict['acl_id'])
        data_type = "s"
        value = "{0}".format(arg_dict['ace_name'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_ace_ethernet_ethertype(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.202.1.1.2.4.4.1.3.{1}.{0}||" \
              "1.3.6.1.4.1.2272.1.202.1.1.2.4.4.1.6.{1}.{0}||" \
              "1.3.6.1.4.1.2272.1.202.1.1.2.4.4.1.5.{1}.{0}".format(arg_dict['ace_index'],
                                                                    arg_dict['acl_id'])
        data_type = "s||i||i"
        value = "{0}||4||1".format(arg_dict['ace_ethertype'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def clear_ace_ethernet_ethertype(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.202.1.1.2.4.4.1.6.{1}.{0}".format(arg_dict['ace_index'],
                                                      arg_dict['acl_id'])
        data_type = "i"
        value = "6"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def show_all_ipv4(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.4.1.2272.1.202.1.1.2.3.1"

        return self.create_cmd_obj(command_type, oid)

    def show_all_ipv6(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.4.1.2272.1.202.1.1.2.3.1"

        return self.create_cmd_obj(command_type, oid)

    def show_ports(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.2272.1.202.1.1.2.3.1.1.10.{0}".format(arg_dict['acl_id'])

        return self.create_cmd_obj(command_type, oid)

    def show_vlans(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.2272.1.202.1.1.2.3.1.1.9.{0}".format(arg_dict['acl_id'])

        return self.create_cmd_obj(command_type, oid)

    def show_all_aces(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.4.1.2272.1.202.1.1.2.4.1"

        return self.create_cmd_obj(command_type, oid)

    def show_id(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.2272.1.202.1.1.2.3.1.1.3.{0}||" \
              "1.3.6.1.4.1.2272.1.202.1.1.2.3.1.1.4.{0}||" \
              "1.3.6.1.4.1.2272.1.202.1.1.2.3.1.1.5.{0}||" \
              "1.3.6.1.4.1.2272.1.202.1.1.2.3.1.1.6.{0}||" \
              "1.3.6.1.4.1.2272.1.202.1.1.2.3.1.1.8.{0}||" \
              "1.3.6.1.4.1.2272.1.202.1.1.2.3.1.1.9.{0}||" \
              "1.3.6.1.4.1.2272.1.202.1.1.2.3.1.1.10.{0}||" \
              "1.3.6.1.4.1.2272.1.202.1.1.2.3.1.1.12.{0}||" \
              "1.3.6.1.4.1.2272.1.202.1.1.2.3.1.1.13.{0}||" \
              "1.3.6.1.4.1.2272.1.202.1.1.2.3.1.1.14.{0}||" \
              "1.3.6.1.4.1.2272.1.202.1.1.2.3.1.1.16.{0}||" \
              "1.3.6.1.4.1.2272.1.202.1.1.2.3.1.1.17.{0}".format(arg_dict['acl_id'])

        return self.create_cmd_obj(command_type, oid)

    def show_ace_index_oper_state(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.2272.1.202.1.1.2.4.1.1.11.{1}.{0}".format(arg_dict['ace_index'],
                                                       arg_dict['acl_id'])

        return self.create_cmd_obj(command_type, oid)

    def show_ace_index_name(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.2272.1.202.1.1.2.4.1.1.3.{1}.{0}".format(arg_dict['ace_index'],
                                                      arg_dict['acl_id'])

        return self.create_cmd_obj(command_type, oid)

    def show_ace_index_action(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.2272.1.202.1.1.2.4.1.1.4.{1}.{0}".format(arg_dict['ace_index'],
                                                      arg_dict['acl_id'])

        return self.create_cmd_obj(command_type, oid)

    def show_ace_index_ethernet_ethertype(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.2272.1.202.1.1.2.4.4.1.3.{1}.{0}".format(arg_dict['ace_index'],
                                                      arg_dict['acl_id'])

        return self.create_cmd_obj(command_type, oid)
