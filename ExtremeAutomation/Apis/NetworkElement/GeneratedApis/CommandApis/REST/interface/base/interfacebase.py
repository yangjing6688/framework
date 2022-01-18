"""
Base class for all interface rest commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.RestBaseApi import RestBaseApi
from ExtremeAutomation.Library.Device.Common.CommandObjects.RestCommandObject import RestCommandObject


class InterfaceBase(RestBaseApi):
    def __init__(self, device):
        super(InterfaceBase, self).__init__()
        self.device = device

    def delete_interface(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request

    def set_ipv4_primary_addr_prefix(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request

    def set_ipv4_primary_addr_netmask(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request

    def show_info(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request

    def show_all(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request
