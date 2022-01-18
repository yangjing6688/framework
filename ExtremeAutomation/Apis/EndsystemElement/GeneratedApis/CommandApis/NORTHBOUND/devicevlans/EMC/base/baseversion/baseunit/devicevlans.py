"""
All devicevlans supported northbound commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Library.Device.Common.CommandObjects.RestCommandObject import RestCommandObject
from ExtremeAutomation.Apis.EndsystemElement.GeneratedApis.CommandApis.NORTHBOUND.devicevlans.base.devicevlansbase \
    import DevicevlansBase


class Devicevlans(DeviceApi, DevicevlansBase):
    def __init__(self, device):
        super(Devicevlans, self).__init__(device)

    def placeholder(self, arg_dict):
        rest_request = RestCommandObject()
        rest_request.uri = "/nbi/graphql/"
        rest_request.data = 'placeholder'
        rest_request.request_type = "post"

        return self.device.send_command_object(rest_request)
