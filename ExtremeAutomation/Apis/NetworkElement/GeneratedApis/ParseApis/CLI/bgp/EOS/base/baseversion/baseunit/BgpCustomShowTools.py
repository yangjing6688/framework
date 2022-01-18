from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.bgp.base.BgpBaseCustomShowTools import \
    BgpBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


def create_instance(device):
    return BgpCustomShowTools(device)


class BgpCustomShowTools(BgpBaseCustomShowTools):
    def __init__(self, device):
        super(BgpCustomShowTools, self).__init__(device)

    def check_route_exists(self, output, args, **kwargs):
        if args["vlan"] is None:
            route_in_table = self.pw.get_value_by_offset(output, args["route"], 1)
            nexthop_in_table = self.pw.get_value_by_offset(output, args["route"], 3)
            peer_in_table = self.pw.get_value_by_offset(output, args["route"], 2)
            result = True
            if args["route"] not in route_in_table:
                result = False
            if args["nexthop"] not in nexthop_in_table:
                result = False
            if args["peer"] not in peer_in_table:
                result = False

        else:
            local_peer = args["peer"] + "%" + StringUtils.eos_interface(args["vlan"])
            route_in_table = self.pw.get_value_by_offset(output, args["route"], 1)
            nexthop_in_table = self.pw.get_value_by_offset(output, args["route"], 3)
            peer_in_table = self.pw.get_value_by_offset(output, args["route"], 2)
            result = True
            if args["route"] not in route_in_table:
                result = False
            if args["nexthop"] not in nexthop_in_table:
                result = False
            if local_peer not in peer_in_table:
                result = False
        return result, {"ret_route": str(route_in_table),
                        "ret_nexthop": str(nexthop_in_table),
                        "ret_local_peer": str(peer_in_table)}

    def check_neighbor_state(self, output, args, **kwargs):
        neighbor_list = self.pw.get_value_by_offset(output, "BGP neighbor is:", 3).split()
        neighbor_state_list = self.pw.get_value_by_offset(output, "Current state is:", 3).split()

        for i, peer in enumerate(neighbor_list):
            if peer == args["neighbor"]:
                result = True if neighbor_state_list[i] else False
                return result, {"ret_neighbor_state": str(neighbor_state_list[i])}
        return False, {"ret_neighbor_state": None}

    def check_linklocal_neighbor_state(self, output, args, **kwargs):
        peer = args["neighbor"] + "%" + StringUtils.exos_vlan_string(args["vlan"])
        neighbor_state = self.pw.get_value_by_offset(output, peer, 4)

        result = True if neighbor_state == args["state"] else False
        return result, {"ret_neighbor_state": neighbor_state}

    def check_bgp_deleted(self, output, args, **kwargs):
        enabled = "Route status codes: > - active" in output

        result = True if not enabled else False
        return result, result

    def check_bgp_enabled(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_bgp_disabled(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_neighbor_exists(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_bgp_as(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_bgp_router_id(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None
