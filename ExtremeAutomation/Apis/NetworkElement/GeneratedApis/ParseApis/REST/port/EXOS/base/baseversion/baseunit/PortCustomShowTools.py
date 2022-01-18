from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.REST.port.base.PortBaseCustomShowTools import \
    PortBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


def create_instance(device):
    return PortCustomShowTools(device)


class PortCustomShowTools(PortBaseCustomShowTools):
    def __init__(self, device):
        super(PortCustomShowTools, self).__init__(device)

    def verify_port_enabled(self, output, args, **kwargs):
        output = StringUtils.format_json_output(output)

        admin_state = output["result"][1]["show_ports_info_detail"]["adminState"]

        if admin_state == 1:
            admin_state = "enabled"
        else:
            admin_state = "disabled"

        result = True if admin_state.lower() == "enabled" else False
        return result, {"ret_state": admin_state}

    def verify_port_alias(self, output, args, **kwargs):
        output = StringUtils.format_json_output(output)
        output_alias = output["result"][1]["show_ports_info_detail"]["descriptionString"]

        result = True if output_alias == args["alias"] else False
        return result, {"ret_alias": output_alias}
