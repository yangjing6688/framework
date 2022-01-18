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

    def check_bgp_enabled(self, output, args, **kwargs):
        output = output.replace("\n", "\r\n")
        bgp_state = self.pw.get_value_by_offset(output, "BGP on/off", 3)

        result = True if bgp_state == "ON" else False
        return result, {"ret_bgp_state": bgp_state}

    def check_bgp_disabled(self, output, args, **kwargs):
        output = output.replace("\n", "\r\n")
        bgp_state = self.pw.get_value_by_offset(output, "BGP on/off", 3)

        result = True if bgp_state == "OFF" else False
        return result, {"ret_bgp_state": bgp_state}

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

    def check_bgp_as(self, output, args, **kwargs):
        output = output.replace("\n", "\r\n")
        as_num = self.pw.get_value_by_offset(output, "local-as", 2)

        result = True if as_num == args["asnum"] else False
        return result, {"ret_bgp_as": as_num}

    def check_neighbor_exists(self, output, args, **kwargs):
        output = output.replace("\n", "\r\n")
        neighbor = str(args["ip"])
        asnum = str(args["asnum"])
        neighbor_found = str(self.pw.get_value_by_offset(output, "BGP neighbor is", 3))
        asnum_found = str(self.pw.get_value_by_offset(output, "BGP neighbor is", 6).replace(",", ""))

        if neighbor_found == neighbor and asnum_found == asnum:
            result = True
        elif neighbor_found == neighbor:
            result = True
        else:
            result = False
        return result, {"ret_bgp_neighbor": neighbor_found,
                        "ret_bgp_remote_as": asnum_found}

    def check_bgp_router_id(self, output, args, **kwargs):
        output = output.replace("\n", "\r\n")
        router_id = self.pw.get_value_by_offset(output, "Identifier", 2)

        result = True if router_id == args["rtrid"] else False
        return result, {"ret_router_id": router_id}

    def check_redistributed_route_exists(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_peer_group_exists(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_neighbor_state(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_network_exists(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_linklocal_neighbor_state(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_bgp_deleted(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None
