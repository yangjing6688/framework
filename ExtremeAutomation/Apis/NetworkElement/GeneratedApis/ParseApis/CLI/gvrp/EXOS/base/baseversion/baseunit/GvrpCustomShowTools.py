from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.gvrp.base.GvrpBaseCustomShowTools import \
    GvrpBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


def create_instance(device):
    return GvrpCustomShowTools(device)


class GvrpCustomShowTools(GvrpBaseCustomShowTools):
    def __init__(self, device):
        super(GvrpCustomShowTools, self).__init__(device)

    def check_gvrp_state(self, output, args, **kwargs):
        output = output.replace("MVRP enabled ports", "MVRP ports")
        state = self.pw.get_value_by_offset(output.lower(), "mvrp enabled", 3)

        result = True if state == "enabled" else False

        return result, {"ret_gvrp_state": state}

    def check_gvrp_state_port(self, output, args, **kwargs):
        output = output.lower().splitlines()
        gvrp_enabled_ports = ""

        for index, line in enumerate(output):
            if line.find("mvrp enabled ports") != -1:
                while output[index].find("flags") == -1:
                    tmp_line = output[index].replace("mvrp enabled ports", "")
                    tmp_line = tmp_line.replace(" : ", "")
                    tmp_line = tmp_line.replace("\r", "")

                    gvrp_enabled_ports += tmp_line
                    index += 1
                else:
                    break

        gvrp_enabled_ports = StringUtils.normalize_exos_ports(gvrp_enabled_ports.split())
        result = self.it.compare_port_values(gvrp_enabled_ports, args["port"], self.inspect_constants.FOUNDIN)

        return result, {"ret_gvrp_state": "enabled" if result else "disabled"}
