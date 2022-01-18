"""
All arp supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.arp.base.arpbase import ArpBase


class Arp(DeviceApi, ArpBase):
    def __init__(self, device_input):
        super(Arp, self).__init__(device_input)

    def create_entry_interface(self, arg_dictionary, **kwargs):
        uuid = "24a3e643-81cd-46e5-99ba-0e2aba2150ea"
        cmd = "ip arp {0} {1} {2} vid {3}".format(arg_dictionary['ip_address'],
                                                  arg_dictionary['mac'],
                                                  arg_dictionary['interface'],
                                                  arg_dictionary['interface'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def delete_entry(self, arg_dictionary, **kwargs):
        uuid = "78efc289-9630-4ce7-842e-f1927fab2fd6"
        cmd = "no ip arp {0}".format(arg_dictionary['ip_address'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def create_entry_port(self, arg_dictionary, **kwargs):
        uuid = "b18ddc94-cccb-498e-a1df-5ebb199f9e7c"
        cmd = "ip arp {0} {1} {2}".format(arg_dictionary['ip_address'],
                                          arg_dictionary['mac'],
                                          arg_dictionary['port'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def create_entry_port_vlan(self, arg_dictionary, **kwargs):
        uuid = "dbf72d3f-e00b-42af-b5ea-75d6d8ae223c"
        cmd = "ip arp {0} {1} {2} vid {3}".format(arg_dictionary['ip_address'],
                                                  arg_dictionary['mac'],
                                                  arg_dictionary['port'],
                                                  arg_dictionary['vlan'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_all_entries(self, arg_dictionary, **kwargs):
        uuid = "43496482-51b0-4626-8199-1146fce297b1"
        cmd = "show ip arp"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_entry(self, arg_dictionary, **kwargs):
        uuid = "71c7a6cf-8ee3-4ad9-bdeb-9b0dfda3aebc"
        cmd = "show ip arp {0}".format(arg_dictionary['ip_address'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_vrf_entry(self, arg_dictionary, **kwargs):
        uuid = "6a572153-56f7-4dbd-8d80-9b3f0e108442"
        cmd = "show ip arp vrf {0}".format(arg_dictionary['vrf_name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
