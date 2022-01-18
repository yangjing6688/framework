"""
All filemanagement supported SNMP commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.SNMP.filemanagement.base.filemanagementbase \
    import FilemanagementBase


class Filemanagement(DeviceApi, FilemanagementBase):
    def __init__(self, device):
        super(Filemanagement, self).__init__(device)
        self.device = device

    def set_system_config(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.1916.1.1.1.6.0||" \
              "1.3.6.1.4.1.1916.1.1.1.49.0"
        data_type = "i||s"
        value = "3||{0}".format(arg_dict['config'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def save_current_config(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.1916.1.1.1.3.0"
        data_type = "i"
        value = "3"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def save_config_to_primary(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.1916.1.1.1.3.0"
        data_type = "i"
        value = "1"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def save_config_to_secondary(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.1916.1.1.1.3.0"
        data_type = "i"
        value = "2"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def save_config_to_file(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.1916.1.1.1.3.0||" \
              "1.3.6.1.4.1.1916.1.1.1.48.0"
        data_type = "i||s"
        value = "4||{0}".format(arg_dict['config'])

        return self.create_cmd_obj(command_type, oid, data_type, value)
