from ExtremeAutomation.Apis.EndsystemElement.GeneratedApis.ParseApis.CLI.dhcp.base.DhcpBaseCustomShowTools import \
    DhcpBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


class DhcpCustomShowTools(DhcpBaseCustomShowTools):
    def __init__(self, device):
        DhcpBaseCustomShowTools.__init__(self, device)

    def check_dhcp_process(self, output, process):
        return self.pw.is_string_present_in_output(output, str(process)), None
