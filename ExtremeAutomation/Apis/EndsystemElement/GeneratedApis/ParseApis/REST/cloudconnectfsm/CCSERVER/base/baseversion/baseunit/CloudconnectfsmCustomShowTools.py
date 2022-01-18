from ExtremeAutomation.Apis.EndsystemElement.GeneratedApis.ParseApis.REST.cloudconnectfsm.base.\
    CloudconnectfsmBaseCustomShowTools import CloudconnectfsmBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Keywords.Utils.DeviceValueStorage import DeviceValueStorage


class CloudconnectfsmCustomShowTools(CloudconnectfsmBaseCustomShowTools):
    def __init__(self, device):
        super(CloudconnectfsmCustomShowTools, self).__init__(device)

    def check_device_states(self, output, args, **kwargs):
        if not output["result"]:
            self.logger.log_info("Device states are currently: " + output["state_list"])
        return output["result"], {"ret_state_list": output["state_list"]}

    def store_mgmt_ip(self, output, args, **kwargs):
        if "mgmt_ip" not in output:
            self.logger.log_info("Device management IP was not found!")
            return False, {"ret_ip": None}
        else:
            DeviceValueStorage().add_value(self.device.name, args["var_name"], output["mgmt_ip"])
            return True, {"ret_ip": output["mgmt_ip"]}

    def check_device_version(self, output, args, **kwargs):
        result = False
        found_version = None
        try:
            assets = output["assets"]
            for asset in assets:
                if asset["assetName"] == args["asset_name"]:
                    found_version = asset["assetVersion"]
                    result = found_version == args["asset_version"]
        except KeyError:
            self.logger.log_error("Key Error")
        return result, {"ret_version": found_version}
