"""
Base class for all bgp rest commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.RestBaseApi import RestBaseApi
from ExtremeAutomation.Library.Device.Common.CommandObjects.RestCommandObject import RestCommandObject


class BgpBase(RestBaseApi):
    def __init__(self, device):
        super(BgpBase, self).__init__()
        self.device = device

    def create_as(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request

    def delete_as(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request

    def set_router_id(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request

    def clear_router_id(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request

    def create_neighbor(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request

    def delete_neighbor(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request

    def enable_neighbor(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request

    def disable_neighbor(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request

    def set_auto_peering(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request

    def clear_auto_peering(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request

    def set_confederation_id(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request

    def clear_confederation_id(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request

    def set_confederation_peer_member_as(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request

    def clear_confederation_peer_member_as(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request

    def set_graceful_restart_time(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request

    def clear_graceful_restart_time(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request

    def set_graceful_stale_route_time(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request

    def clear_graceful_stale_route_time(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request

    def set_maximum_paths(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request

    def clear_maximum_paths(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request

    def set_neighbor_keep_alive_interval_and_hold_time(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request

    def set_neighbor_transport_address(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request

    def enable_graceful_restart(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request

    def disable_graceful_restart(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request

    def enable_allow_multiple_as(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request

    def disable_allow_multiple_as(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request

    def enable_always_compare_med(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request

    def disable_always_compare_med(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request

    def enable_advertise_inactive_routes_ipv4_unicast(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request

    def disable_advertise_inactive_routes_ipv4_unicast(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request

    def enable_advertise_inactive_routes_l3vpn_ipv4_unicast(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request

    def disable_advertise_inactive_routes_l3vpn_ipv4_unicast(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request

    def enable_advertise_inactive_routes_ipv6_unicast(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request

    def disable_advertise_inactive_routes_ipv6_unicast(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request

    def show_always_compare_med(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request

    def show_advertise_inactive_routes_ipv6_unicast(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request

    def show_advertise_inactive_routes_l3vpn_ipv4_unicast(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request

    def show_advertise_inactive_routes_ipv4_unicast(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request

    def show_use_multiple_paths(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request

    def show_neighbor_timers(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request

    def show_confederation(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request

    def show_graceful_restart(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request

    def show_neighbors(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request

    def show_status(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request
