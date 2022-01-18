"""
Base class for all vlan rest commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.RestBaseApi import RestBaseApi
from ExtremeAutomation.Library.Device.Common.CommandObjects.RestCommandObject import RestCommandObject


class VlanBase(RestBaseApi):
    def __init__(self, device):
        super(VlanBase, self).__init__()
        self.device = device

    def create_vlan(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request

    def delete_vlan(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request

    def show_all_info(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request

    def show_info(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request

    def set_egress_untagged(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request

    def set_egress_tagged(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request
