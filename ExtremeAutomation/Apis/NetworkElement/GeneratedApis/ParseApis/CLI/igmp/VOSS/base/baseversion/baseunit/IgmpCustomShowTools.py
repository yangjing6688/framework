from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.igmp.base.IgmpBaseCustomShowTools import \
    IgmpBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


def create_instance(device):
    return IgmpCustomShowTools(device)


class IgmpCustomShowTools(IgmpBaseCustomShowTools):
    def __init__(self, device):
        super(IgmpCustomShowTools, self).__init__(device)

    def check_igmp_state(self, output, args, **kwargs):
        state = "true"
        result = []
        ret_state = ""
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == args["vlan"]:
                    result = line.split()[7]
                    ret_state = result
                    break
        result = True if result == state else False

        return result, {"ret_igmp_vlans": ret_state}

    def check_igmp_version(self, output, args, **kwargs):
        result = []
        ret_version = ""
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == args["vlan"]:
                    result = line.split()[4]
                    ret_version = result
                    break
        result = True if result == args["igmp_ver"] else False

        return result, {"ret_igmp_version": ret_version}

    def check_igmp_snooping_state(self, output, args, **kwargs):
        state = "true"
        result = []
        ret_state = ""
        ret_vlan = ""
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == args["vlan"]:
                    result = line.split()[7]
                    ret_state = result
                    ret_vlan = args["vlan"]
                    break
        result = True if result == state else False

        return result, {"ret_vlan_found": ret_vlan, "ret_igmp_snooping_vlan_state": ret_state}

    def check_igmp_snooping_querier_state(self, output, args, **kwargs):
        state = "true"
        result = []
        ret_state = ""
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == args["vlan"]:
                    result.append(line.split()[1])
                    ret_state = line.split()[1]

        result = True if state in result else False

        return result, {"ret_querier_state": ret_state}

    def check_igmp_snooping_proxy_state(self, output, args, **kwargs):
        state = "true"
        result = []
        ret_vlan = ""
        ret_state = ""
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == args["vlan"]:
                    result = line.split()[6]
                    ret_vlan = args["vlan"]
                    ret_state = result
                    break

        result = True if result == state else False

        return result, {"ret_vlan_found": ret_vlan, "ret_snooping_proxy_state": ret_state}

    def check_igmp_snooping_dynamic_downgrade_state(self, output, args, **kwargs):
        state = "enable"
        result = []
        ret_state = ""
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == args["vlan"]:
                    result.append(line.split()[3])
                    ret_state = line.split()[3]

        result = True if state in result else False

        return result, {"ret_igmp_state": ret_state}

    def check_igmp_snooping_compatibility_mode_state(self, output, args, **kwargs):
        state = "enable"
        result = []
        ret_state = ""
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == args["vlan"]:
                    result.append(line.split()[4])
                    ret_state = line.split()[4]

        result = True if state in result else False

        return result, {"ret_igmp_state": ret_state}

    def check_igmp_snooping_explicit_host_tracking_state(self, output, args, **kwargs):
        state = "enable"
        result = []
        ret_state = ""
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == args["vlan"]:
                    result.append(line.split()[5])
                    ret_state = line.split()[5]

        result = True if state in result else False

        return result, {"ret_igmp_state": ret_state}

    def check_igmp_vlan_state(self, output, args, **kwargs):
        state = "true"
        result = []
        ret_vlan = ""
        ret_state = ""
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == args["vlan"]:
                    result = line.split()[7]
                    ret_vlan = args["vlan"]
                    ret_state = result
                    break

        result = True if result == state else False

        return result, {"ret_vlan_found": ret_vlan, "ret_igmp_vlan_state": ret_state}

    def check_igmp_snooping_vlan_state(self, output, args, **kwargs):
        state = "true"
        result = []
        ret_vlan = ""
        ret_state = ""
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == args["vlan"]:
                    result = line.split()[7]
                    ret_vlan = args["vlan"]
                    ret_state = result
                    break

        result = True if result == state else False

        return result, {"ret_vlan_found": ret_vlan, "ret_igmp_snooping_vlan_state": ret_state}

    def check_igmp_snooping_querier_address(self, output, args, **kwargs):
        querier_address = []
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == args["vlan"]:
                    querier_address.append(line.split()[2])

        result = True if args["ip"] in querier_address else False

        return result, {"ret_querier": ', '.join(querier_address)}

    def check_igmp_snooping_querier_address_is_removed(self, output, args, **kwargs):
        ip = "0.0.0.0"
        querier_address = []
        ret_address = ""
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == args["vlan"]:
                    querier_address.append(line.split()[2])
                    ret_address = line.split()[2]

        result = True if ip in querier_address else False

        return result, {"ret_igmp_querier_addr": ret_address}

    def verify_igmp_group(self, output, args, **kwargs):
        match = "no"
        ret_dict = {"ret_vlan": None,
                    "ret_port": None}
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == args["group"]:
                    vlan_port_found = line.split()[1]
                    vlan_port_found = vlan_port_found.split("-")
                    vlan_found = vlan_port_found[0]
                    port_found = vlan_port_found[1]
                    ret_dict["ret_vlan"] = vlan_found
                    ret_dict["ret_port"] = port_found
                    if vlan_found == args["vlan"] \
                            and port_found == args["port"]:
                        match = "yes"
                        break

        result = True if match == "yes" else False

        return result, ret_dict
