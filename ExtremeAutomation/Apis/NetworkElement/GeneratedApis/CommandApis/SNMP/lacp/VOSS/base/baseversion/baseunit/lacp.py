"""
All lacp supported SNMP commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.SNMP.lacp.base.lacpbase import LacpBase


class Lacp(DeviceApi, LacpBase):
    def __init__(self, device):
        super(Lacp, self).__init__(device)
        self.device = device

    def set_mlt_actor_key(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.2.840.10006.300.43.1.1.1.1.6.{0}".format(arg_dict['mlt_id'])
        data_type = "i"
        value = "{0}".format(arg_dict['actor_admin_key'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_mlt_actor_system_priority(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.2.840.10006.300.43.1.1.1.1.3.{0}".format(arg_dict['mlt_id'])
        data_type = "i"
        value = "{0}".format(arg_dict['actor_system_priority'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def show_mlt_port(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.2.840.10006.300.43.1.1.1.1.2.{0}||" \
              "1.2.840.10006.300.43.1.1.1.1.3.{0}||" \
              "1.2.840.10006.300.43.1.1.1.1.4.{0}||" \
              "1.2.840.10006.300.43.1.1.1.1.5.{0}||" \
              "1.2.840.10006.300.43.1.1.1.1.6.{0}||" \
              "1.2.840.10006.300.43.1.1.1.1.7.{0}||" \
              "1.2.840.10006.300.43.1.1.1.1.8.{0}||" \
              "1.2.840.10006.300.43.1.1.1.1.9.{0}||" \
              "1.2.840.10006.300.43.1.1.1.1.10.{0}||" \
              "1.2.840.10006.300.43.1.1.1.1.11.{0}".format(arg_dict['mlt_id'])

        return self.create_cmd_obj(command_type, oid)

    def show_mlt_id_logical_index(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.2272.1.17.10.1.11.{0}".format(arg_dict['mlt_id'])

        return self.create_cmd_obj(command_type, oid)
