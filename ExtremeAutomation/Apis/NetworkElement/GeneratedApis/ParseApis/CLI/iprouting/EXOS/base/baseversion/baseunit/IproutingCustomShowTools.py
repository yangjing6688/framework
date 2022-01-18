from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.iprouting.base.IproutingBaseCustomShowTools \
    import IproutingBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


def create_instance(device):
    return IproutingCustomShowTools(device)


class IproutingCustomShowTools(IproutingBaseCustomShowTools):
    def __init__(self, device):
        super(IproutingCustomShowTools, self).__init__(device)

    def validate_route_entry(self, output, args, **kwargs):
        if args["route"] in output:
            gateway = self.pw.get_value_by_offset(output, args["route"], 2)

            return True if gateway == args["nexthop"] else False, {"ret_gateway": gateway}

        else:
            return False, None

    def store_default_gateway(self, output, args, **kwargs):
        gateway_ip = "valueNotPresent"
        if " Default Route " in output:
            gateway_ip = self.pw.get_value_by_offset(output, " Default Route ", 3)

        result = True if gateway_ip is not None else False

        self.value_storage.add_value(self.device.name, args["gateway_name"], gateway_ip)
        self.logger.log_info("Default Gateway is: " + gateway_ip)

        return result, {"ret_gateway": gateway_ip}
