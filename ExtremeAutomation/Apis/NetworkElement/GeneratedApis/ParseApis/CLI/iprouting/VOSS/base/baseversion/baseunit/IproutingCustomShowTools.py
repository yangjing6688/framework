from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.iprouting.base.IproutingBaseCustomShowTools \
    import IproutingBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


class IproutingCustomShowTools(IproutingBaseCustomShowTools):
    def __init__(self, device):
        super(IproutingCustomShowTools, self).__init__(device)

    def validate_route_entry(self, output, args, **kwargs):
        ret_dict = None
        for line in output.splitlines():
            match = True
            if len(line) > 1:
                if line.split()[0] == args["route"]:
                    found_dest = line.split()[0]
                    found_mask = line.split()[1]
                    found_nexthop = line.split()[2]
                    found_vrf_name = line.split()[3]
                    found_cost = line.split()[4]
                    found_interface = line.split()[5]
                    found_protocol = line.split()[6]
                    found_age = line.split()[7]
                    found_type = line.split()[8]
                    found_preferece = line.split()[9]

                    if found_dest != args["route"]:
                        ret_dict = {"ret_nexthop": found_nexthop,
                                    "ret_mask": found_mask,
                                    "ret_vrf": found_vrf_name,
                                    "ret_cost": found_cost,
                                    "ret_interface": found_interface,
                                    "ret_protocol": found_protocol,
                                    "ret_age": found_age,
                                    "ret_type": found_type,
                                    "ret_preference": found_preferece}
                        if found_nexthop != args["nexthop"]:
                            match = False
                        if args["mask"] is not None:
                            if found_mask != args["mask"]:
                                match = False
                        if args["nexthop"] is not None:
                            if found_nexthop != args["nexthop"]:
                                match = False
                        if args["vrf_name"] is not None:
                            if found_vrf_name != args["vrf_name"]:
                                match = False
                        if args["cost"] is not None:
                            if found_cost != args["cost"]:
                                match = False
                        if args["interface"] is not None:
                            if found_interface != args["interface"]:
                                match = False
                        if args["protocol"] is not None:
                            if found_protocol != args["protocol"]:
                                match = False
                        if args["age"] is not None:
                            if found_age != args["age"]:
                                match = False
                        if args["type"] is not None:
                            if found_type != args["type"]:
                                match = False
                        if args["preference"] is not None:
                            if found_preferece != args["preference"]:
                                match = False
                    if match:
                        return True, ret_dict

        return False, ret_dict

    def validate_ipv6_route_entry(self, output, args, **kwargs):
        ret_dict = None
        for line in output.splitlines():
            match = True
            if len(line) > 1:
                if line.split()[0] == args["route"]:
                    found_dest = line.split()[0]
                    found_nexthop = line.split()[1]
                    found_interface = line.split()[2]
                    found_protocol = line.split()[3]
                    found_cost = line.split()[4]
                    found_age = line.split()[5]
                    found_route_type = line.split()[6]
                    found_preferece = line.split()[7]

                    if found_dest != args["route"]:
                        ret_dict = {"ret_nexthop": found_nexthop,
                                    "ret_cost": found_cost,
                                    "ret_interface": found_interface,
                                    "ret_protocol": found_protocol,
                                    "ret_age": found_age,
                                    "ret_type": found_route_type,
                                    "ret_preference": found_preferece}
                        if found_nexthop != args["nexthop"]:
                            match = False
                        if args["nexthop"] is not None:
                            if found_nexthop != args["nexthop"]:
                                match = False
                        if args["cost"] is not None:
                            if found_cost != args["cost"]:
                                match = False
                        if args["interface"] is not None:
                            if found_interface != args["interface"]:
                                match = False
                        if args["protocol"] is not None:
                            if found_protocol != args["protocol"]:
                                match = False
                        if args["age"] is not None:
                            if found_age != args["age"]:
                                match = False
                        if args["route_type"] is not None:
                            if found_route_type != args["route_type"]:
                                match = False
                        if args["preference"] is not None:
                            if found_preferece != args["preference"]:
                                match = False
                    if match:
                        return True, ret_dict
        return False, ret_dict

    def validate_vrf_route_entry(self, output, args, **kwargs):
        ret_dict = None
        for line in output.splitlines():
            match = True
            if len(line) > 1:
                if line.split()[0] == args["route"]:
                    found_dest = line.split()[0]
                    found_mask = line.split()[1]
                    found_nexthop = line.split()[2]
                    found_vrf_name = line.split()[3]
                    found_cost = line.split()[4]
                    found_interface = line.split()[5]
                    found_protocol = line.split()[6]
                    found_age = line.split()[7]
                    found_type = line.split()[8]
                    found_preferece = line.split()[9]

                    if found_dest != args["route"]:
                        ret_dict = {"ret_nexthop": found_nexthop,
                                    "ret_mask": found_mask,
                                    "ret_vrf": found_vrf_name,
                                    "ret_cost": found_cost,
                                    "ret_interface": found_interface,
                                    "ret_protocol": found_protocol,
                                    "ret_age": found_age,
                                    "ret_type": found_type,
                                    "ret_preference": found_preferece}
                        if found_nexthop != args["nexthop"]:
                            match = False
                        if args["mask"] is not None:
                            if found_mask != args["mask"]:
                                match = False
                        if args["nexthop"] is not None:
                            if found_nexthop != args["nexthop"]:
                                match = False
                        if args["vrf_name"] is not None:
                            if found_vrf_name != args["vrf_name"]:
                                match = False
                        if args["cost"] is not None:
                            if found_cost != args["cost"]:
                                match = False
                        if args["interface"] is not None:
                            if found_interface != args["interface"]:
                                match = False
                        if args["protocol"] is not None:
                            if found_protocol != args["protocol"]:
                                match = False
                        if args["age"] is not None:
                            if found_age != args["age"]:
                                match = False
                        if args["type"] is not None:
                            if found_type != args["type"]:
                                match = False
                        if args["preference"] is not None:
                            if found_preferece != args["preference"]:
                                match = False
                    if match:
                        return True, ret_dict

        return False, ret_dict

    def validate_ipv6_vrf_route_entry(self, output, args, **kwargs):
        ret_dict = None
        for line in output.splitlines():
            match = True
            if len(line) > 1:
                if line.split()[0] == args["route"]:
                    found_dest = line.split()[0]
                    found_nexthop = line.split()[2]
                    found_vrf_name = line.split()[3]
                    found_cost = line.split()[4]
                    found_interface = line.split()[5]
                    found_protocol = line.split()[6]
                    found_age = line.split()[7]
                    found_type = line.split()[8]
                    found_preferece = line.split()[9]

                    if found_dest != args["route"]:
                        ret_dict = {"ret_nexthop": found_nexthop,
                                    "ret_vrf": found_vrf_name,
                                    "ret_cost": found_cost,
                                    "ret_interface": found_interface,
                                    "ret_protocol": found_protocol,
                                    "ret_age": found_age,
                                    "ret_type": found_type,
                                    "ret_preference": found_preferece}
                        if found_nexthop != args["nexthop"]:
                            match = False
                        if args["nexthop"] is not None:
                            if found_nexthop != args["nexthop"]:
                                match = False
                        if args["vrf_name"] is not None:
                            if found_vrf_name != args["vrf_name"]:
                                match = False
                        if args["cost"] is not None:
                            if found_cost != args["cost"]:
                                match = False
                        if args["interface"] is not None:
                            if found_interface != args["interface"]:
                                match = False
                        if args["protocol"] is not None:
                            if found_protocol != args["protocol"]:
                                match = False
                        if args["age"] is not None:
                            if found_age != args["age"]:
                                match = False
                        if args["type"] is not None:
                            if found_type != args["type"]:
                                match = False
                        if args["preference"] is not None:
                            if found_preferece != args["preference"]:
                                match = False
                    if match:
                        return True, ret_dict

        return False, ret_dict
