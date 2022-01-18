"""
Base class for all autopeering rest commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.RestBaseApi import RestBaseApi
from ExtremeAutomation.Library.Device.Common.CommandObjects.RestCommandObject import RestCommandObject


class AutopeeringBase(RestBaseApi):
    def __init__(self, device):
        super(AutopeeringBase, self).__init__()
        self.device = device

    def set_anycast_mac(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request

    def set_anycast_mac_and_id(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request

    def set_anycast_mac_and_route_target(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request

    def clear_anycast_mac(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request

    def clear_anycast_mac_and_id(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request

    def clear_anycast_mac_and_route_target(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request

    def set_host_address_host_vrf_static_route_network_static_route_next_hop(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request

    def clear_all_hosts(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request

    def clear_host(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request

    def clear_static_route_from_host(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request

    def set_service_nsi_nsi_type_vrf_address_ip_address_prefix_length(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request

    def set_host_static_route(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request

    def clear_all_services(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request

    def clear_service(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request

    def show_global(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request

    def show_hosts(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request

    def show_host_static_routes(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request

    def show_service(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request

    def show_all_services(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request
