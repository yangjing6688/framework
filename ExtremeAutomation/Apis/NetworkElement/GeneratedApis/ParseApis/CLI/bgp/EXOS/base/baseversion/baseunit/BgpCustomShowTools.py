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
            local_peer = args["peer"] + "%" + StringUtils.exos_vlan_string(args["vlan"])
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
        neighbor_state = self.pw.get_value_by_offset(output, args["neighbor"], 4)

        result = True if neighbor_state == args["state"] else False
        return result, {"ret_neighbor_state": neighbor_state}

    def check_linklocal_neighbor_state(self, output, args, **kwargs):
        peer = args["neighbor"] + "%" + StringUtils.exos_vlan_string(args["vlan"])
        neighbor_state = self.pw.get_value_by_offset(output, peer, 4)

        result = True if neighbor_state == args["state"] else False
        return result, {"ret_neighbor_state": neighbor_state}

    def check_bgp_deleted(self, output, args, **kwargs):
        bgp_state = self.pw.get_value_by_offset(output, "Enabled", 2).split()[0]
        bgp_as = self.pw.get_value_by_offset(output, "RouterId", 5)

        result = True if bgp_state == "No" and bgp_as == "0" else False
        return result, {"ret_bgp_as": bgp_as,
                        "ret_bgp_state": bgp_state}

    def check_bgp_enabled(self, output, args, **kwargs):
        bgp_state = self.pw.get_value_by_offset(output, "Enabled", 2).split()[0]

        result = True if bgp_state == "Yes" else False
        return result, {"ret_bgp_state": bgp_state}

    def check_bgp_disabled(self, output, args, **kwargs):
        bgp_state = self.pw.get_value_by_offset(output, "Enabled", 2).split()[0]

        result = True if bgp_state == "No" else False
        return result, {"ret_bgp_state": bgp_state}

    def check_bgp_as(self, output, args, **kwargs):
        as_num = self.pw.get_value_by_offset(output, "RouterId", 5)

        result = True if as_num == args["asnum"] else False
        return result, {"ret_bgp_as": as_num}

    def check_neighbor_exists(self, output, args, **kwargs):
        neighbor = str(args["ip"])
        asnum = str(args["asnum"])
        neighbor_found = self.pw.get_value_at_location(output, column=1, name=args["ip"])
        asnum_found = self.pw.get_value_at_location(output, column=2, name=args["ip"])

        result = True if neighbor_found == neighbor and asnum_found == asnum else False
        return result, {"ret_bgp_neighbor": neighbor_found,
                        "ret_bgp_remote_as": asnum_found}

    def check_bgp_router_id(self, output, args, **kwargs):
        output = output.replace("\n", "\r\n")
        router_id = self.pw.get_value_by_offset(output, "RouterId", 2)

        result = True if router_id == args["rtrid"] else False
        return result, {"ret_router_id": router_id}

    def check_bgp_auto_peering(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None
