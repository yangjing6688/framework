from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.REST.autopeering.base.\
    AutopeeringBaseCustomShowTools import AutopeeringBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


class AutopeeringCustomShowTools(AutopeeringBaseCustomShowTools):
    def __init__(self, device):
        super(AutopeeringCustomShowTools, self).__init__(device)

    def check_autopeering_anycast_mac(self, output, args, **kwargs):
        anycast_mac = output['extreme-auto-peering:auto-peering']["auto-peering-anycast-mac"]
        result = True if str(anycast_mac) == args["anycast_mac"] else False
        return result, {"anycast_mac": str(anycast_mac)}

    def check_autopeering_id(self, output, args, **kwargs):
        peer_id = output['extreme-auto-peering:auto-peering']["auto-peering-id"]
        result = True if str(peer_id) == args["peer_id"] else False
        return result, {"id": str(peer_id)}

    def check_autopeering_route_target(self, output, args, **kwargs):
        route_target = output['extreme-auto-peering:auto-peering']["auto-peering-route-target"]
        result = True if str(route_target) == args["route_target"] else False
        return result, {"route_target": str(route_target)}

    def check_autopeering_host_exists(self, output, args, **kwargs):
        hosts = output['extreme-auto-peering:hosts']["host"]
        for item in hosts:
            if item['host-address'] == args["host_address"]:
                return True, item['host-address']
        return False, args["host_address"]

    def check_autopeering_hosts_vrf(self, output, args, **kwargs):
        hosts = output['extreme-auto-peering:hosts']["host"]
        for item in hosts:
            if item['host-address'] == args['host_address']:
                if item['vrf'] == args["host_vrf"]:
                    return True, item['vrf']
        return False, args["host_vrf"]

    def check_autopeering_hosts_static_route_network_address_exists(self, output, args, **kwargs):
        host_data = output['extreme-auto-peering:static-routes']["static-route"]
        for route in host_data:
            if route['network'] == args['network_address']:
                return True, route['network']
        return False, args['network_address']

    def check_autopeering_hosts_static_route_nexthop_address_exists(self, output, args, **kwargs):
        host_data = output['extreme-auto-peering:static-routes']["static-route"]
        for route in host_data:
            next_hop_list = route['nexthop']
            for item in next_hop_list:
                if item == args['nexthop']:
                    return True, route['network']
        return False, args['nexthop']

    def check_service_nsi_value(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_service_nsi_type(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_service_nsi_vrf(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_service_address_ip(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_service_address_prefix_length(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_autopeering_host_does_not_exist(self, output, args, **kwargs):
        hosts = output['extreme-auto-peering:hosts']["host"]
        for item in hosts:
            if item['host-address'] == args["host_address"]:
                return False, item['host-address']
        return True, args["host_address"]

    def check_autopeering_hosts_static_route_network_address_does_not_exist(self, output, args, **kwargs):
        host_data = output['extreme-auto-peering:static-routes']["static-route"]
        for route in host_data:
            if route['network'] == args['network_address']:
                return False, route['network']
        return True, args['network_address']

    def check_autopeering_hosts_vrf_does_not_exist(self, output, args, **kwargs):
        hosts = output['extreme-auto-peering:hosts']["host"]
        for item in hosts:
            if item['host-address'] == args['host_address']:
                if item['vrf'] == args["host_vrf"]:
                    return False, item['vrf']
        return True, args["host_vrf"]

    def check_autopeering_service_exists(self, output, args, **kwargs):
        try:
            service = output['extreme-auto-peering:service'][0]
            if service['nsi'] == args['nsi']:
                if service['nsi-type'] == args['nsi_type']:
                    if service['vrf'] == args['vrf']:
                        address_dict = service['addresses']['address'][0]
                        if address_dict['ip'] == args['address_ip']:
                            if address_dict['prefix-length'] == int(args['address_prefix_length']):
                                return True, args['nsi']
            return False, args['nsi']
        except KeyError:
            return False, args['nsi']

    def check_autopeering_service_does_not_exist(self, output, args, **kwargs):
        service = output['extreme-auto-peering:services']
        for item in service['service']:
            if item['nsi'] == args['nsi']:
                return False, args['nsi']
        return True, args['nsi']
