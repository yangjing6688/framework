from ExtremeAutomation.Library.Device.Common.Apis.BaseApi import BaseApi
from ExtremeAutomation.Library.Device.Common.CommandObjects.SnmpCommandObject import SnmpCommandObject


class SnmpBaseApi(BaseApi):
    @staticmethod
    def create_cmd_obj(command_type, oid, data_type=None, value=None):
        """Creates the command object to send to the current_agent."""
        cmd_obj = SnmpCommandObject()

        cmd_obj.command_type = command_type
        cmd_obj.oid = oid

        if data_type:
            cmd_obj.data_type = data_type

        if value:
            cmd_obj.value = value

        return cmd_obj
