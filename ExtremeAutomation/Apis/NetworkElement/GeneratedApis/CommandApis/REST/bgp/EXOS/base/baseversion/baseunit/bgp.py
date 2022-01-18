"""
All bgp supported rest commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.REST.bgp.base.bgpbase import BgpBase
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.REST.bgp.EXOS.base.baseversion.baseunit.bgpData \
    import BgpData


class Bgp(DeviceApi, BgpBase):
    def __init__(self, device):
        super(Bgp, self).__init__(device)
        self.data_file = BgpData()

    def create_as(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/openconfig-bgp:bgp/global/config"
        request_type = "patch"
        data = self.data_file.create_as_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def delete_as(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/openconfig-bgp:bgp/global/config"
        request_type = "patch"
        data = self.data_file.delete_as_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def set_router_id(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/openconfig-bgp:bgp/global/config"
        request_type = "patch"
        data = self.data_file.set_router_id_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def clear_router_id(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/openconfig-bgp:bgp/global/config"
        request_type = "patch"
        data = self.data_file.clear_router_id_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def create_neighbor(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/openconfig-bgp:bgp/neighbors"
        request_type = "post"
        data = self.data_file.create_neighbor_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def delete_neighbor(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/openconfig-bgp:bgp/neighbors/neighbor={0}".format(arg_dict['ip'])
        request_type = "delete"
        data = self.data_file.delete_neighbor_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def enable_neighbor(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/openconfig-bgp:bgp/neighbors/neighbor={0}/config".format(arg_dict['ip'])
        request_type = "patch"
        data = self.data_file.enable_neighbor_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def disable_neighbor(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/openconfig-bgp:bgp/neighbors/neighbor={0}/config".format(arg_dict['ip'])
        request_type = "patch"
        data = self.data_file.disable_neighbor_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def set_auto_peering(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/openconfig-bgp:bgp/global/config"
        request_type = "patch"
        data = self.data_file.set_auto_peering_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def clear_auto_peering(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/openconfig-bgp:bgp/global/config"
        request_type = "patch"
        data = self.data_file.clear_auto_peering_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def set_confederation_id(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/openconfig-bgp:bgp/global/confederation"
        request_type = "patch"
        data = self.data_file.set_confederation_id_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def clear_confederation_id(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/openconfig-bgp:bgp/global/confederation"
        request_type = "patch"
        data = self.data_file.clear_confederation_id_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def set_confederation_peer_member_as(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/openconfig-bgp:bgp/global/confederation"
        request_type = "patch"
        data = self.data_file.set_confederation_peer_member_as_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def clear_confederation_peer_member_as(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/openconfig-bgp:bgp/global/confederation/config"
        request_type = "put"
        data = self.data_file.clear_confederation_peer_member_as_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def set_graceful_restart_time(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/openconfig-bgp:bgp/global/graceful-restart"
        request_type = "patch"
        data = self.data_file.set_graceful_restart_time_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def clear_graceful_restart_time(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/openconfig-bgp:bgp/global/graceful-restart"
        request_type = "patch"
        data = self.data_file.clear_graceful_restart_time_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def set_graceful_stale_route_time(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/openconfig-bgp:bgp/global/graceful-restart"
        request_type = "patch"
        data = self.data_file.set_graceful_stale_route_time_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def clear_graceful_stale_route_time(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/openconfig-bgp:bgp/global/graceful-restart"
        request_type = "patch"
        data = self.data_file.clear_graceful_stale_route_time_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def set_maximum_paths(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/openconfig-bgp:bgp/global/use-multiple-paths"
        request_type = "patch"
        data = self.data_file.set_maximum_paths_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def clear_maximum_paths(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/openconfig-bgp:bgp/global/use-multiple-paths"
        request_type = "patch"
        data = self.data_file.clear_maximum_paths_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def set_neighbor_keep_alive_interval_and_hold_time(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/openconfig-bgp:bgp/neighbors/neighbor={0}/timers/config".format(arg_dict['neighbor_ip'])
        request_type = "patch"
        data = self.data_file.set_neighbor_keep_alive_interval_and_hold_time_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def set_neighbor_transport_address(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/openconfig-bgp:bgp/neighbors/neighbor={0}/transport/config".format(arg_dict['neighbor_ip'])
        request_type = "patch"
        data = self.data_file.set_neighbor_transport_address_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def enable_graceful_restart(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/openconfig-bgp:bgp/global/graceful-restart"
        request_type = "patch"
        data = self.data_file.enable_graceful_restart_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def disable_graceful_restart(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/openconfig-bgp:bgp/global/graceful-restart"
        request_type = "patch"
        data = self.data_file.disable_graceful_restart_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def enable_allow_multiple_as(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/openconfig-bgp:bgp/global/use-multiple-paths/ebgp/config"
        request_type = "patch"
        data = self.data_file.enable_allow_multiple_as_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def disable_allow_multiple_as(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/openconfig-bgp:bgp/global/use-multiple-paths/ebgp/config"
        request_type = "patch"
        data = self.data_file.disable_allow_multiple_as_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def enable_always_compare_med(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/openconfig-bgp:bgp/global/route-selection-options"
        request_type = "patch"
        data = self.data_file.enable_always_compare_med_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def disable_always_compare_med(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/openconfig-bgp:bgp/global/route-selection-options"
        request_type = "patch"
        data = self.data_file.disable_always_compare_med_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def enable_advertise_inactive_routes_ipv4_unicast(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/openconfig-bgp:bgp/global/afi-safis"
        request_type = "patch"
        data = self.data_file.enable_advertise_inactive_routes_ipv4_unicast_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def disable_advertise_inactive_routes_ipv4_unicast(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/openconfig-bgp:bgp/global/afi-safis"
        request_type = "patch"
        data = self.data_file.disable_advertise_inactive_routes_ipv4_unicast_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def enable_advertise_inactive_routes_l3vpn_ipv4_unicast(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/openconfig-bgp:bgp/global/afi-safis"
        request_type = "patch"
        data = self.data_file.enable_advertise_inactive_routes_l3vpn_ipv4_unicast_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def disable_advertise_inactive_routes_l3vpn_ipv4_unicast(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/openconfig-bgp:bgp/global/afi-safis"
        request_type = "patch"
        data = self.data_file.disable_advertise_inactive_routes_l3vpn_ipv4_unicast_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def enable_advertise_inactive_routes_ipv6_unicast(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/openconfig-bgp:bgp/global/afi-safis"
        request_type = "patch"
        data = self.data_file.enable_advertise_inactive_routes_ipv6_unicast_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def disable_advertise_inactive_routes_ipv6_unicast(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/openconfig-bgp:bgp/global/afi-safis"
        request_type = "patch"
        data = self.data_file.disable_advertise_inactive_routes_ipv6_unicast_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def show_always_compare_med(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/openconfig-bgp:bgp/global/route-selection-options/config"
        request_type = "get"
        data = self.data_file.show_always_compare_med_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def show_advertise_inactive_routes_ipv6_unicast(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/openconfig-bgp:bgp/global/afi-safis/afi-safi=oc-bgp-types:IPV6_UNICAST/route-selection-options/config"
        request_type = "get"
        data = self.data_file.show_advertise_inactive_routes_ipv6_unicast_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def show_advertise_inactive_routes_l3vpn_ipv4_unicast(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/openconfig-bgp:bgp/global/afi-safis/afi-safi=oc-bgp-types:L3VPN_IPV4_UNICAST/route-selection-options/config"
        request_type = "get"
        data = self.data_file.show_advertise_inactive_routes_l3vpn_ipv4_unicast_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def show_advertise_inactive_routes_ipv4_unicast(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/openconfig-bgp:bgp/global/afi-safis/afi-safi=oc-bgp-types:IPV4_UNICAST/route-selection-options/config"
        request_type = "get"
        data = self.data_file.show_advertise_inactive_routes_ipv4_unicast_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def show_use_multiple_paths(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/openconfig-bgp:bgp/global/use-multiple-paths/ebgp/config"
        request_type = "get"
        data = self.data_file.show_use_multiple_paths_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def show_neighbor_timers(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/openconfig-bgp:bgp/neighbors/neighbor={0}/timers/config".format(arg_dict['neighbor_ip'])
        request_type = "get"
        data = self.data_file.show_neighbor_timers_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def show_confederation(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/openconfig-bgp:bgp/global/confederation/config"
        request_type = "get"
        data = self.data_file.show_confederation_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def show_graceful_restart(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/openconfig-bgp:bgp/global/graceful-restart/config"
        request_type = "get"
        data = self.data_file.show_graceful_restart_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def show_neighbors(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/openconfig-bgp:bgp/neighbors"
        request_type = "get"
        data = self.data_file.show_neighbors_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def show_status(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/openconfig-bgp:bgp/global/config"
        request_type = "get"
        data = self.data_file.show_status_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)
