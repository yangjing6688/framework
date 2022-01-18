"""
All networking supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.EndsystemElement.GeneratedApis.CommandApis.CLI.networking.base.networkingbase import \
    NetworkingBase


class Networking(DeviceApi, NetworkingBase):
    def __init__(self, device_input):
        super(Networking, self).__init__(device_input)

    def connect_to_wireless_network(self, arg_dictionary, **kwargs):
        cmd = "netsh wlan connect ssid={0} name={1}".format(arg_dictionary['ssid'],
                                                            arg_dictionary['ssid'])
        prompt = "userPrompt"

        return self.create_cmd_obj(cmd, prompt=prompt)

    def disconnect_from_wireless_network(self, arg_dictionary, **kwargs):
        cmd = "netsh wlan disconnect"
        prompt = "userPrompt"

        return self.create_cmd_obj(cmd, prompt=prompt)

    def show_wireless_network(self, arg_dictionary, **kwargs):
        cmd = "netsh wlan show interfaces"
        prompt = "userPrompt"

        return self.create_cmd_obj(cmd, prompt=prompt)
