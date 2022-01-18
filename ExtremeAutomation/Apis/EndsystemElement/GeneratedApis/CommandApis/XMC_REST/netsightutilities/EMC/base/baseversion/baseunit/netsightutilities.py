"""
All netsightutilities supported rest commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.EndsystemElement.GeneratedApis.CommandApis.XMC_REST.netsightutilities.base.\
    netsightutilitiesbase import NetsightutilitiesBase
from ExtremeAutomation.Apis.EndsystemElement.GeneratedApis.CommandApis.XMC_REST.netsightutilities.EMC.base.baseversion.\
    baseunit.netsightutilitiesData import NetsightutilitiesData


class Netsightutilities(DeviceApi, NetsightutilitiesBase):
    def __init__(self, device):
        super(Netsightutilities, self).__init__(device)
        self.data_file = NetsightutilitiesData()

    def install_netsight(self, arg_dict, **kwargs):
        uri = "robot/v1/install_netsight"
        request_type = "post"
        data = self.data_file.install_netsight_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def restart_netsight_and_redeploy_war_file(self, arg_dict, **kwargs):
        uri = "robot/v1/restart_netsight_and_redeploy_war_file"
        request_type = "post"
        data = self.data_file.restart_netsight_and_redeploy_war_file_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def netsight_script_copy(self, arg_dict, **kwargs):
        uri = "robot/v1/netsight_script_copy"
        request_type = "post"
        data = self.data_file.netsight_script_copy_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def netsight_log_copy(self, arg_dict, **kwargs):
        uri = "robot/v1/netsight_log_copy"
        request_type = "post"
        data = self.data_file.netsight_log_copy_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)
