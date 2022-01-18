"""
All hostinformation supported SNMP commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.SNMP.hostinformation.base.hostinformationbase \
    import HostinformationBase


class Hostinformation(DeviceApi, HostinformationBase):
    def __init__(self, device):
        super(Hostinformation, self).__init__(device)
        self.device = device

    def set_host_contact(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.2.1.1.4.0"
        data_type = "s"
        value = "{0}".format(arg_dict['contact'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_host_name(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.2.1.1.5.0"
        data_type = "s"
        value = "{0}".format(arg_dict['name'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_host_location(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.2.1.1.6.0"
        data_type = "s"
        value = "{0}".format(arg_dict['location'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def show_host_contact(self, arg_dict, **kwargs):
        command_type = "snmpgetnext"
        oid = "1.3.6.1.2.1.1.4."

        return self.create_cmd_obj(command_type, oid)

    def show_host_name(self, arg_dict, **kwargs):
        command_type = "snmpgetnext"
        oid = "1.3.6.1.2.1.1.5."

        return self.create_cmd_obj(command_type, oid)

    def show_host_location(self, arg_dict, **kwargs):
        command_type = "snmpgetnext"
        oid = "1.3.6.1.2.1.1.6."

        return self.create_cmd_obj(command_type, oid)

    def show_host_description(self, arg_dict, **kwargs):
        command_type = "snmpgetnext"
        oid = "1.3.6.1.2.1.1.1."

        return self.create_cmd_obj(command_type, oid)

    def show_host_uptime(self, arg_dict, **kwargs):
        command_type = "snmpgetnext"
        oid = "1.3.6.1.2.1.1.3."

        return self.create_cmd_obj(command_type, oid)

    def show_host_services(self, arg_dict, **kwargs):
        command_type = "snmpgetnext"
        oid = "1.3.6.1.2.1.1.7."

        return self.create_cmd_obj(command_type, oid)

    def show_host_object_id(self, arg_dict, **kwargs):
        command_type = "snmpgetnext"
        oid = "1.3.6.1.2.1.1.2."

        return self.create_cmd_obj(command_type, oid)
