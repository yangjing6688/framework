"""
All dutlearning supported SNMP commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.SNMP.dutlearning.base.dutlearningbase import \
    DutlearningBase


class Dutlearning(DeviceApi, DutlearningBase):
    def __init__(self, device):
        super(Dutlearning, self).__init__(device)
        self.device = device

    def getnext_system_location_dot_zero(self, arg_dict, **kwargs):
        command_type = "snmpgetnext"
        oid = "1.3.6.1.2.1.1.6.0."

        return self.create_cmd_obj(command_type, oid)

    def walk_system(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.2.1.1."

        return self.create_cmd_obj(command_type, oid)

    def bulkwalk_system(self, arg_dict, **kwargs):
        command_type = "snmpbulkwalk"
        oid = "1.3.6.1.2.1.1."

        return self.create_cmd_obj(command_type, oid)
