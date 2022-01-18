from ExtremeAutomation.Apis.EndsystemElement.GeneratedApis.ParseApis.CLI.hostservices.base.\
    HostservicesBaseCustomShowTools import HostservicesBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


class HostservicesCustomShowTools(HostservicesBaseCustomShowTools):
    def __init__(self, device):
        super(HostservicesCustomShowTools, self).__init__(device)

    def check_ping_result_on_endsys(self, output, host_address_arg):
        host_address = self.pw.get_value_by_offset(output, host_address_arg, 3)
        result = True

        if host_address_arg not in host_address:
            result = False
        return result, None
