from ExtremeAutomation.Apis.EndsystemElement.GeneratedApis.ParseApis.CLI.networking.base.NetworkingBaseCustomShowTools \
    import NetworkingBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


class NetworkingCustomShowTools(NetworkingBaseCustomShowTools):
    def __init__(self, device):
        NetworkingBaseCustomShowTools.__init__(self, device)

    def check_wireless_network_connected(self, output, arg_dict):
        con_ssid = None

        for line in output.splitlines():
            if "SSID                   :" in line:
                con_ssid = line.split(":")[1].strip()
                break

        result = False
        if con_ssid == arg_dict["ssid"]:
            result = True
        return result, {"ret_ssid": con_ssid}

    def check_wireless_network_disconnected(self, output, arg_dict):
        con_state = None

        for line in output.splitlines():
            if "State                  :" in line:
                con_state = line.split(":")[1].strip()
                break

        result = False
        if con_state == "disconnected":
            result = True
        return result, {"ret_state": con_state}
