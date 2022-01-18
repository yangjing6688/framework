class BgpData(object):
    @staticmethod
    def create_as_data(arg_dict):
        data = {'openconfig-bgp:config': {
            "as": arg_dict["asnum"]}}
        return data

    @staticmethod
    def set_router_id_data(arg_dict):
        data = {'openconfig-bgp:config': {
            "router-id": arg_dict["rtrid"]}}
        return data

    @staticmethod
    def delete_as_data(arg_dict):
        data = {'openconfig-bgp:config': {
            "as": 0}}
        return data

    @staticmethod
    def clear_router_id_data(arg_dict):
        data = {'openconfig-bgp:config': {
            "router-id": "0.0.0.0"}}
        return data

    @staticmethod
    def create_neighbor_data(arg_dict):
        data = {'openconfig-bgp:neighbor': [
                {
                    "neighbor-address": arg_dict["ip"],
                    "config": {
                        "neighbor-address": arg_dict["ip"],
                        "peer-as": arg_dict["remoteas"],
                    },
                }, ]}
        return data

    @staticmethod
    def enable_neighbor_data(arg_dict):
        data = {'openconfig-bgp:config': {
            "enabled": True}}
        return data

    @staticmethod
    def disable_neighbor_data(arg_dict):
        data = {'openconfig-bgp:config': {
            "enabled": False}}
        return data

    @staticmethod
    def delete_neighbor_data(arg_dict):
        pass

    @staticmethod
    def show_status_data(arg_dict):
        pass

    @staticmethod
    def show_neighbors_data(arg_dict):
        pass

    @staticmethod
    def set_auto_peering_data(arg_dict):
        data = {'openconfig-bgp:config': {
            "router-id": arg_dict["rtrid"],
            "as": arg_dict["asnum"],
            "auto-peering": 1}}
        return data

    @staticmethod
    def clear_auto_peering_data(arg_dict):
        data = {'openconfig-bgp:config': {
            "auto-peering": 0}}
        return data

    @staticmethod
    def enable_graceful_restart_data(arg_dict):
        data = {
            "openconfig-bgp:graceful-restart": {
                "config": {
                    "enabled": True,
                    "helper-only": False
                }}}
        return data

    @staticmethod
    def disable_graceful_restart_data(arg_dict):
        data = {
            "openconfig-bgp:graceful-restart": {
                "config": {
                    "enabled": False,
                    "helper-only": False
                }}}
        return data

    @staticmethod
    def set_graceful_restart_time_data(arg_dict):
        data = {
            "openconfig-bgp:graceful-restart": {
                "config": {
                    "restart-time": int(arg_dict['restart_time'])
                }}}
        return data

    @staticmethod
    def enable_multiple_as_data(arg_dict):
        data = {"openconfig-bgp:use-multiple-paths": {
                "ebgp": {"config": {"allow-multiple-as": True}}}}
        return data

    @staticmethod
    def disable_multiple_as_data(arg_dict):
        data = {"openconfig-bgp:use-multiple-paths":
                {"ebgp": {"config": {"allow-multiple-as": False}}}}
        return data

    @staticmethod
    def enable_advertise_inactive_routes_ipv4_unicast_data(arg_dict):
        data = {"openconfig-bgp:afi-safis": {"afi-safi": [
                {"afi-safi-name": "oc-bgp-types:IPV4_UNICAST",
                    "config": {
                        "afi-safi-name": "oc-bgp-types:IPV4_UNICAST"
                    },
                    "route-selection-options": {
                        "config": {
                            "advertise-inactive-routes": True
                        }}}]}}
        return data

    @staticmethod
    def disable_advertise_inactive_routes_ipv4_unicast_data(arg_dict):
        data = {"openconfig-bgp:afi-safis": {"afi-safi": [
                {"afi-safi-name": "oc-bgp-types:IPV4_UNICAST",
                    "config": {
                        "afi-safi-name": "oc-bgp-types:IPV4_UNICAST"
                    },
                    "route-selection-options": {
                        "config": {
                            "advertise-inactive-routes": False
                        }}}]}}
        return data

    @staticmethod
    def enable_advertise_inactive_routes_l3vpn_ipv4_unicast_data(arg_dict):
        data = {"openconfig-bgp:afi-safis": {"afi-safi": [
                {"afi-safi-name": "oc-bgp-types:L3VPN_IPV4_UNICAST",
                    "config": {
                        "afi-safi-name": "oc-bgp-types:L3VPN_IPV4_UNICAST"
                    },
                    "route-selection-options": {
                        "config": {
                            "advertise-inactive-routes": True
                        }}}]}}
        return data

    @staticmethod
    def disable_advertise_inactive_routes_l3vpn_ipv4_unicast_data(arg_dict):
        data = {"openconfig-bgp:afi-safis": {"afi-safi": [
                {"afi-safi-name": "oc-bgp-types:L3VPN_IPV4_UNICAST",
                    "config": {
                        "afi-safi-name": "oc-bgp-types:L3VPN_IPV4_UNICAST"
                    },
                    "route-selection-options": {
                        "config": {
                            "advertise-inactive-routes": False
                        }}}]}}
        return data

    @staticmethod
    def enable_advertise_inactive_routes_ipv6_unicast_data(arg_dict):
        data = {"openconfig-bgp:afi-safis": {"afi-safi": [
                {"afi-safi-name": "oc-bgp-types:IPV6_UNICAST",
                    "config": {
                        "afi-safi-name": "oc-bgp-types:IPV6_UNICAST"
                    },
                    "route-selection-options": {
                        "config": {
                            "advertise-inactive-routes": True
                        }}}]}}
        return data

    @staticmethod
    def disable_advertise_inactive_routes_ipv6_unicast_data(arg_dict):
        data = {"openconfig-bgp:afi-safis": {"afi-safi": [
                {"afi-safi-name": "oc-bgp-types:IPV6_UNICAST",
                    "config": {
                        "afi-safi-name": "oc-bgp-types:IPV6_UNICAST"
                    },
                    "route-selection-options": {
                        "config": {
                            "advertise-inactive-routes": False
                        }}}]}}
        return data

    @staticmethod
    def set_confederation_id_data(arg_dict):
        data = {"openconfig-bgp:confederation": {
                "config": {
                    "identifier": int(arg_dict["confed_id"])}}}
        return data

    @staticmethod
    def set_confederation_peer_member_as_data(arg_dict):
        data = {"openconfig-bgp:confederation": {"config": {"member-as": [int(arg_dict["member_as"])]}}}
        return data

    @staticmethod
    def enable_allow_multiple_as_data(arg_dict):
        data = {"openconfig-bgp:config": {"allow-multiple-as": True}}
        return data

    @staticmethod
    def disable_allow_multiple_as_data(arg_dict):
        data = {"openconfig-bgp:config": {"allow-multiple-as": False}}
        return data

    @staticmethod
    def show_confederation_id_data(arg_dict):
        pass

    @staticmethod
    def enable_always_compare_med_data(arg_dict):
        data = {"openconfig-bgp:route-selection-options": {
                "config": {"always-compare-med": True}}}
        return data

    @staticmethod
    def disable_always_compare_med_data(arg_dict):
        data = {"openconfig-bgp:route-selection-options": {"config": {"always-compare-med": False}}}
        return data

    @staticmethod
    def show_confederation_data(arg_dict):
        pass

    @staticmethod
    def show_graceful_restart_data(arg_dict):
        pass

    @staticmethod
    def show_use_multiple_paths_data(arg_dict):
        pass

    @staticmethod
    def show_always_compare_med_data(arg_dict):
        pass

    @staticmethod
    def show_advertise_inactive_routes_l3vpn_ipv4_unicast_data(arg_dict):
        pass

    @staticmethod
    def show_advertise_inactive_routes_ipv6_unicast_data(arg_dict):
        pass

    @staticmethod
    def clear_confederation_id_data(arg_dict):
        data = {"openconfig-bgp:confederation": {"config": {"identifier": 0}}}
        return data

    @staticmethod
    def clear_stale_routes_time_data(arg_dict):
        data = {"openconfig-bgp:graceful-restart": {
                "config": {
                    "stale-routes-time": '360.00'}}}
        return data

    @staticmethod
    def show_advertise_inactive_routes_ipv4_unicast_data(arg_dict):
        pass

    @staticmethod
    def clear_graceful_restart_time_data(arg_dict):
        data = {"openconfig-bgp:graceful-restart": {
                "config": {
                    "restart-time": 120}}}
        return data

    @staticmethod
    def set_maximum_paths_data(arg_dict):
        data = {"openconfig-bgp:use-multiple-paths": {
                "ebgp": {
                    "config": {
                        "maximum-paths": int(arg_dict['paths'])}},
                "ibgp": {
                    "config": {
                        "maximum-paths": int(arg_dict['paths'])}}}}
        return data

    @staticmethod
    def clear_maximum_paths_data(arg_dict):
        data = {"openconfig-bgp:use-multiple-paths": {
                "ebgp": {
                    "config": {
                        "maximum-paths": 1}},
                "ibgp": {
                    "config": {
                        "maximum-paths": 1}}}}
        return data

    @staticmethod
    def set_graceful_stale_route_time_data(arg_dict):
        data = {"openconfig-bgp:graceful-restart": {
                "config": {
                    "stale-routes-time": arg_dict['stale_route_time']
                }}}
        return data

    @staticmethod
    def clear_graceful_stale_route_time_data(arg_dict):
        data = {"openconfig-bgp:graceful-restart": {
                "config": {
                    "stale-routes-time": '360.00'
                }}}
        return data

    @staticmethod
    def show_neighbor_timers_data(arg_dict):
        pass

    @staticmethod
    def set_neighbor_transport_address_data(arg_dict):
        data = {"openconfig-bgp:config": {"local-address": arg_dict['local_address']}}
        return data

    @staticmethod
    def set_neighbor_keep_alive_interval_and_hold_time_data(arg_dict):
        data = {"openconfig-bgp:config": {
                "hold-time": arg_dict['hold_time'],
                "keepalive-interval": arg_dict['keep_alive_time']}
                }
        return data

    @staticmethod
    def clear_confederation_peer_member_as_data(arg_dict):
        data = {"openconfig-bgp:config": {
                "identifier": int(arg_dict['member_as']),
                "member-as": []}}
        return data
