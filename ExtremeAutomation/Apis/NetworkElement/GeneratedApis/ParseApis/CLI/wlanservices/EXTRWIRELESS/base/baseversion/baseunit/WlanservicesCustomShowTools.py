from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.wlanservices.base.\
    WlanservicesBaseCustomShowTools import WlanservicesBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


def create_instance(device):
    return WlanservicesCustomShowTools(device)


class WlanservicesCustomShowTools(WlanservicesBaseCustomShowTools):
    def __init__(self, device):
        super(WlanservicesCustomShowTools, self).__init__(device)

    # #################################################################################################################
    #   Current Parser Functions   ####################################################################################
    # #################################################################################################################
    def check_wlan_service_exists(self, output, args, **kwargs):
        result = self.pw.is_exact_string_present_in_output(output, args["wlan_service_name"])

        return result, result
