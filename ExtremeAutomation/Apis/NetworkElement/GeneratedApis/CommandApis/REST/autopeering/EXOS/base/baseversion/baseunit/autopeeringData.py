class AutopeeringData(object):
    @staticmethod
    def set_anycast_mac_data(arg_dict):
        data = {"extreme-auto-peering:auto-peering": {
                "anycast-mac": arg_dict['anycast_mac']}}
        return data

    @staticmethod
    def clear_anycast_mac_data(arg_dict):
        data = {"extreme-auto-peering:auto-peering": {
                "anycast-mac": '00:00:00:00:00:00'}}
        return data

    @staticmethod
    def set_anycast_mac_and_id_data(arg_dict):
        data = {"extreme-auto-peering:auto-peering": {
                "anycast-mac": arg_dict['anycast_mac'],
                "id": int(arg_dict['peer_id'])}}
        return data

    @staticmethod
    def set_anycast_mac_and_route_target_data(arg_dict):
        data = {"extreme-auto-peering:auto-peering": {
                "anycast-mac": arg_dict['anycast_mac'],
                "route-target": int(arg_dict['route_target'])}}
        return data

    @staticmethod
    def clear_anycast_mac_and_id_data(arg_dict):
        data = {"extreme-auto-peering:auto-peering": {
                "anycast-mac": '00:00:00:00:00:00',
                "id": 0}}
        return data

    @staticmethod
    def clear_anycast_mac_and_route_target_data(arg_dict):
        data = {"extreme-auto-peering:auto-peering": {
                "anycast-mac": '00:00:00:00:00:00',
                "route-target": 0}}
        return data

    @staticmethod
    def set_host_address_host_vrf_static_route_network_static_route_next_hop_data(arg_dict):
        data = {"extreme-auto-peering:hosts": {"host": [{"host-address": arg_dict['host_address'],
                                                         "vrf": arg_dict['host_vrf'],
                                                         "static-routes":
                                                             {"static-route": [{"network": arg_dict['network'],
                                                                                "nexthop": [arg_dict['next_hop']]}]}}]}}
        return data

    @staticmethod
    def clear_all_hosts_data(arg_dict):
        data = {"extreme-auto-peering:hosts": {
                'host': []}}
        return data

    @staticmethod
    def clear_host_data(arg_dict):
        pass

    @staticmethod
    def show_auto_peering_global_data(arg_dict):
        pass

    @staticmethod
    def show_autopeering_global_data(arg_dict):
        pass

    @staticmethod
    def show_autopeering_hosts_data(arg_dict):
        pass

    @staticmethod
    def show_global_data(arg_dict):
        pass

    @staticmethod
    def show_hosts_data(arg_dict):
        pass

    @staticmethod
    def clear_static_route_from_host_data(arg_dict):
        pass

    @staticmethod
    def show_host_static_routes_data(arg_dict):
        pass

    @staticmethod
    def set_service_nsi_nsi_type_vrf_address_ip_address_prefix_length_data(arg_dict):
        data = {"extreme-auto-peering:services": {"service": [{"nsi": int(arg_dict['nsi']),
                                                               "nsi-type": arg_dict['nsi_type'], "vrf": arg_dict['vrf'],
                                                               "addresses": {"address": [{"ip": arg_dict['address_ip'],
                                                                                         "prefix-length":
                                                                                             int(arg_dict
                                                                                                 ['address_prefix_'
                                                                                                  'length'])}]}}]}}
        return data

    @staticmethod
    def show_service_data(arg_dict):
        pass

    @staticmethod
    def set_host_static_route_data(arg_dict):
        data = {"extreme-auto-peering:host": [{"host-address": arg_dict['host_address'], "static-routes":
                {"static-route": [{"network": arg_dict['network_address'], "nexthop": [arg_dict['nexthop_address']]}]},
                "vrf": arg_dict['host_vrf']}]}
        return data

    @staticmethod
    def clear_all_services_data(arg_dict):
        data = {"extreme-auto-peering:services": {"service": []}}
        return data

    @staticmethod
    def clear_service_data(arg_dict):
        pass

    @staticmethod
    def show_all_services_data(arg_dict):
        pass
