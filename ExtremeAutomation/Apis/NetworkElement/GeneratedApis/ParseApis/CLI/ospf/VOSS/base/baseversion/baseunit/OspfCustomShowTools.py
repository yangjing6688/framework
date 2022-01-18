from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.ospf.base.OspfBaseCustomShowTools import \
    OspfBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


def create_instance(device):
    return OspfCustomShowTools(device)


class OspfCustomShowTools(OspfBaseCustomShowTools):
    def __init__(self, device):
        super(OspfCustomShowTools, self).__init__(device)

    def verify_ospf_globally_enabled(self, output, args, **kwargs):
        state = None
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == "AdminStat:":
                    state = line.split()[1]
                    break

        result = True if state == "enabled" else False
        return result, {"ret_state": state}

    def verify_ospf_globally_disabled(self, output, args, **kwargs):
        state = None
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == "AdminStat:":
                    state = line.split()[1]
                    break

        result = True if state == "disabled" else False
        return result, {"ret_state": state}

    def verify_ospf_enabled_on_interface(self, output, args, **kwargs):
        state = self.pw.get_exact_value_by_offset(output.lower(), args["interface"], 1)

        result = True if state == "true" else False
        return result, {"ret_int_state": state}

    def verify_ospf_disabled_on_interface(self, output, args, **kwargs):
        state = self.pw.get_exact_value_by_offset(output.lower(), args["interface"], 1)

        result = True if state == "false" else False
        return result, {"ret_int_state": state}

    def verify_ospf_enabled_on_vlan(self, output, args, **kwargs):
        state = None
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == args["vlan"]:
                    state = line.split()[1]
                    break

        result = True if state == "true" else False
        return result, {"ret_vlan_state": state}

    def verify_ospf_disabled_on_vlan(self, output, args, **kwargs):
        state = None
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == args["vlan"]:
                    state = line.split()[1]
                    break

        result = True if state == "false" else False
        return result, {"ret_vlan_state": state}

    def verify_ospf_router_id(self, output, args, **kwargs):
        router_id = None
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == "RouterId:":
                    router_id = line.split()[1]
                    break

        result = True if router_id == args["router_id"] else False
        return result, {"ret_router_id": router_id}

    def verify_ospf_router_id_is_removed(self, output, args, **kwargs):
        router_id = None
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == "RouterId:":
                    router_id = line.split()[1]
                    break

        result = True if router_id == "0.0.0.0" else False
        return result, {"ret_router_id": router_id}
