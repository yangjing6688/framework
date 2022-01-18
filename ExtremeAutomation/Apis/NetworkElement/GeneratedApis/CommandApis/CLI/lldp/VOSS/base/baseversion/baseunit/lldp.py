"""
All lldp supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.lldp.base.lldpbase import LldpBase


class Lldp(DeviceApi, LldpBase):
    def __init__(self, device_input):
        super(Lldp, self).__init__(device_input)

    def set_tx_interval(self, arg_dictionary, **kwargs):
        uuid = "6d9bd153-8795-4c40-95f3-2a06039393b9"
        cmd = "lldp tx-interval {0}".format(arg_dictionary['interval'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_tx_hold_multiplier(self, arg_dictionary, **kwargs):
        uuid = "66eb3cef-0c24-4f81-b8f4-123be3838a24"
        cmd = "lldp tx-hold-multiplier {0}".format(arg_dictionary['multiplier'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_info(self, arg_dictionary, **kwargs):
        uuid = "62450147-99e0-443c-aaad-b21b4c9925d1"
        cmd = "show lldp"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
