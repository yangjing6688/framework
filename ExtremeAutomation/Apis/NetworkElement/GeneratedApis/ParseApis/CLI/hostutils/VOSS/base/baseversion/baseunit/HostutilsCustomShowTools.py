from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.hostutils.base.HostutilsBaseCustomShowTools \
    import HostutilsBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


class HostutilsCustomShowTools(HostutilsBaseCustomShowTools):
    def __init__(self, device):
        super(HostutilsCustomShowTools, self).__init__(device)

    def check_ping_result(self, output, args, **kwargs):
        host = self.pw.get_value_by_offset(output, args["host_address"], 0)

        result = True if args["host_address"] in host else False
        return result, result

    def check_l2ping_ipaddr_result(self, output, args, **kwargs):
        output = output.lower()
        ip_address_found = self.pw.get_value_by_offset(output, args["ip_address"] + ",", 5)
        percent_loss = self.pw.get_value_by_offset(output, "0.00%", 5)

        result = True if ip_address_found == args["ip_address"] + "," and percent_loss == "0.00%" else False
        return result, {"ret_percent_loss": percent_loss}
