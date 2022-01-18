"""
All arp supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.arp.base.arpbase import ArpBase


class Arp(DeviceApi, ArpBase):
    def __init__(self, device_input):
        super(Arp, self).__init__(device_input)

    def create_entry(self, arg_dictionary, **kwargs):
        uuid = "9e145f7e-5188-4a1a-9293-6169429256ba"
        cmd = "configure iparp add {0} {1}".format(arg_dictionary['ip_address'],
                                                   arg_dictionary['mac'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def create_entry_interface(self, arg_dictionary, **kwargs):
        uuid = "24a3e643-81cd-46e5-99ba-0e2aba2150ea"
        cmd = "configure iparp add {0} {1}".format(arg_dictionary['ip_address'],
                                                   arg_dictionary['mac'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def delete_entry(self, arg_dictionary, **kwargs):
        uuid = "78efc289-9630-4ce7-842e-f1927fab2fd6"
        cmd = "configure iparp delete {0}".format(arg_dictionary['ip_address'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_all_entries(self, arg_dictionary, **kwargs):
        uuid = "c7a01592-4d90-41dd-a9ce-04ec8a451c42"
        cmd = "clear iparp"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_all_entries(self, arg_dictionary, **kwargs):
        uuid = "43496482-51b0-4626-8199-1146fce297b1"
        cmd = "show iparp"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_entry(self, arg_dictionary, **kwargs):
        uuid = "71c7a6cf-8ee3-4ad9-bdeb-9b0dfda3aebc"
        cmd = "show iparp {0}".format(arg_dictionary['ip_address'])
        prompt = "userPrompt"

        self.device.error_checker.add_error_to_ignore_list(*["Error"])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
