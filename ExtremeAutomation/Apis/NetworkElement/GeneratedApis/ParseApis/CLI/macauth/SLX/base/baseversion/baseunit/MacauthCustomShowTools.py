from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.macauth.base.MacauthBaseCustomShowTools import \
    MacauthBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


class MacauthCustomShowTools(MacauthBaseCustomShowTools):
    def __init__(self, device):
        super(MacauthCustomShowTools, self).__init__(device)

    def verify_macauth_port_authentication(self, output, args, **kwargs):
        result = False
        mac_found = None
        mac_type_found = None
        state_found = None
        for line in output.splitlines():
            if len(line) > 1:
                mac_found = self.pw.get_value_by_offset(line, args["vlanid"], 2)
                mac_found = StringUtils.normalize_mac(mac_found.split())
                mac_type_found = self.pw.get_value_by_offset(line.lower(), args["vlanid"], 3).lower().split()
                state_found = self.pw.get_value_by_offset(line.lower(), args["vlanid"], 4).lower().split()
                if args["mac_addr"] in mac_found and args["mac_type"].lower() in mac_type_found and \
                        args["state"].lower() in state_found:
                    result = True
                    break

        return result, {"ret_mac_addr": mac_found,
                        "ret_mac_type": mac_type_found,
                        "ret_state": state_found}
