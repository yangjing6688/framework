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
        oid = "1.3.6.1.4.1.2272.1.1.8.0||" \
              "1.3.6.1.4.1.2272.1.1.34.0"
        data_type = "i||s"
        value = "15||{0}".format(arg_dict['config'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def save_current_config(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.1.8.0"
        data_type = "i"
        value = "13"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def save_config_to_file(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.1.8.0||" \
              "1.3.6.1.4.1.2272.1.1.34.0"
        data_type = "i||s"
        value = "13||{0}".format(arg_dict['config'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def set_system_to_backup_config(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.2272.1.1.8.0||" \
              "1.3.6.1.4.1.2272.1.1.34.0"
        data_type = "i||s"
        value = "16||{0}".format(arg_dict['config'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def show_default_boot_config_file(self, arg_dict, **kwargs):
        command_type = "snmpget"
        oid = "1.3.6.1.4.1.2272.1.1.32.0"

        return self.create_cmd_obj(command_type, oid)
