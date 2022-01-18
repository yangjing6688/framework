"""
All devices supported northbound commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Library.Device.Common.CommandObjects.RestCommandObject import RestCommandObject
from ExtremeAutomation.Apis.EndsystemElement.GeneratedApis.CommandApis.NORTHBOUND.datadriven.base.datadrivenbase \
    import DatadrivenBase


class Datadriven(DeviceApi, DatadrivenBase):
    def __init__(self, device):
        super(Datadriven, self).__init__(device)

    def verify_northbound_query(self, arg_dict):
        rest_request = RestCommandObject()
        rest_request.uri = "/nbi/graphql/"
        rest_request.data = arg_dict['query_string']
        rest_request.request_type = "post"

        return self.device.send_command_object(rest_request)

    def verify_northbound_query_with_regex(self, arg_dict):
        rest_request = RestCommandObject()
        rest_request.uri = "/nbi/graphql/"
        rest_request.data = arg_dict['query_string']
        rest_request.request_type = "post"

        return self.device.send_command_object(rest_request)
