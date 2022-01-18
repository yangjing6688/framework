"""
All demo supported rest commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.EndsystemElement.GeneratedApis.CommandApis.REST.demo.base.demobase import DemoBase
from ExtremeAutomation.Apis.EndsystemElement.GeneratedApis.CommandApis.REST.demo.GIM.base.baseversion.baseunit.\
    demoData import DemoData


class Demo(DeviceApi, DemoBase):
    def __init__(self, device):
        super(Demo, self).__init__(device)
        self.data_file = DemoData()

    def get_guest_user_data(self, arg_dict, **kwargs):
        uri = "GIM/rest/guestUsers/guestUserDetails/{0}".format(arg_dict['user'])
        request_type = "get"
        data = self.data_file.get_guest_user_data_data
        header = {"api-version": "v1.0",                        "Accept": "application/json",                        "Content-Type": "application/json" }

        return self.create_cmd_obj(uri, request_type, data, arg_dict, header)
