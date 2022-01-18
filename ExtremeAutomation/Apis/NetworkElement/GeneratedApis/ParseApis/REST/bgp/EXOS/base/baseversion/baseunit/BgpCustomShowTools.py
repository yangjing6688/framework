from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.REST.bgp.base.BgpBaseCustomShowTools import \
    BgpBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


def create_instance(device):
    return BgpCustomShowTools(device)


class BgpCustomShowTools(BgpBaseCustomShowTools):
    def __init__(self, device):
        super(BgpCustomShowTools, self).__init__(device)

    def check_bgp_as(self, output, args, **kwargs):
        asnum = output['openconfig-bgp:config']['as']
        result = True if str(asnum) == args["asnum"] else False
        return result, {"ret_as_num": str(asnum)}

    def check_bgp_router_id(self, output, args, **kwargs):
        rtrid = output['openconfig-bgp:config']['router-id']
        result = True if str(rtrid) == args["rtrid"] else False
        return result, {"ret_router_id": str(rtrid)}

    def check_bgp_auto_peering(self, output, args, **kwargs):
        autopeering = output['openconfig-bgp:config']["extreme-mod-oc-bgp:auto-peering"]
        result = True if str(autopeering) == args["peering_value"] else False
        return result, {"ret_state": str(autopeering)}

    def check_neighbor_state(self, output, args, **kwargs):
        neighbors = output['openconfig-bgp:neighbors']['neighbor']
        for item in range(len(neighbors)):
            neighbor_state = neighbors[item]['state']['enabled']
            if str(neighbor_state).lower() == args["state"].lower():
                return True, {"state": str(neighbor_state)}
        return False, {"state": str(args["state"])}

    def check_neighbor_exists(self, output, args, **kwargs):
        neighbors = output['openconfig-bgp:neighbors']['neighbor']
        for neighbor in neighbors:
            neighbor_addr = neighbor['config']['neighbor-address']
            if str(neighbor_addr) == args["ip"]:
                return True, {"ret_ip": str(neighbor_addr)}
        return False, {"ret_ip": str(neighbors)}

    def check_graceful_restart(self, output, args, **kwargs):
        graceful_restart = output['openconfig-bgp:config']['enabled']
        result = True if str(graceful_restart).lower() == (args["graceful_restart"].lower()) else False
        return result, {"graceful_restart": str(graceful_restart)}

    def check_stale_route_time(self, output, args, **kwargs):
        stale_route_time = output['openconfig-bgp:config']['stale-routes-time']
        result = True if str(stale_route_time) == str(args["stale_route_time"]) else False
        return result, {"stale_route_time": str(stale_route_time)}

    def check_advertise_inactive_routed(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_confederation_id(self, output, args, **kwargs):
        confed_id = output['openconfig-bgp:config']['identifier']
        result = True if str(confed_id) == args["confed_id"] else False
        return result, {"confed_id": str(confed_id)}

    def check_confederation_peer_member_as(self, output, args, **kwargs):
        member_as = output['openconfig-bgp:config']['member-as']
        for member in member_as:
            if str(member) == args["peer"]:
                if StringUtils.string_to_boolean(args['exists']):
                    return True, {"peer": str(member_as)}
                return False, {"peer": str(member_as)}
        if not StringUtils.string_to_boolean(args['exists']):
            return True, {"peer": str(member_as)}
        return False, {"peer": str(member_as)}

    def check_allow_multiple_as(self, output, args, **kwargs):
        allow_multiple_as = output['openconfig-bgp:config']['allow-multiple-as']
        result = True if str(allow_multiple_as).lower() == str(args["allow_multiple_as"]).lower() else False
        return result, {"allow_multiple_as": str(allow_multiple_as)}

    def check_always_compare_med(self, output, args, **kwargs):
        always_compare_med = output['openconfig-bgp:config']['always-compare-med']
        result = True if str(always_compare_med).lower() == str(args["always_compare_med"]).lower() else False
        return result, {"always_compare_med": str(always_compare_med)}

    def check_maximum_paths(self, output, args, **kwargs):
        maximum_paths = output['openconfig-bgp:config']['maximum-paths']
        result = True if str(maximum_paths) == str(args["maximum_paths"]) else False
        return result, {"maximum_paths": str(maximum_paths)}

    def check_graceful_restart_time(self, output, args, **kwargs):
        restart_time = output['openconfig-bgp:config']['restart-time']
        result = True if str(restart_time) == str(args["restart_time"]) else False
        return result, {"restart_time": str(restart_time)}

    def check_advertise_inactive_routes(self, output, args, **kwargs):
        advertise_inactive_routes = output['openconfig-bgp:config']['advertise-inactive-routes']
        result = True if str(advertise_inactive_routes).lower() == str(args['advertise_inactive_routes']).lower()\
            else False
        return result, {'advertise_inactive_routes': str(advertise_inactive_routes)}

    def check_neighbor_keep_alive_time(self, output, args, **kwargs):
        keep_alive_interval = output['openconfig-bgp:config']['keepalive-interval']
        result = True if str(keep_alive_interval) == str(args['keep_alive_interval']) else False
        return result, {'keep_alive_interval': str(keep_alive_interval)}

    def check_neighbor_hold_time(self, output, args, **kwargs):
        hold_time = output['openconfig-bgp:config']['hold-time']
        result = True if str(hold_time) == str(args['hold_time']) else False
        return result, {'hold_time': str(hold_time)}
