"""
All dhcp supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.dhcp.base.dhcpbase import DhcpBase


class Dhcp(DeviceApi, DhcpBase):
    def __init__(self, device_input):
        super(Dhcp, self).__init__(device_input)

    def enable_vlan(self, arg_dictionary, **kwargs):
        uuid = "95e41821-4973-49cf-8312-981cbb3160cf"
        cmd = "enable dhcp vlan {0}".format(arg_dictionary['vlan_name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_vlan(self, arg_dictionary, **kwargs):
        uuid = "44395079-d9af-4809-ae6d-0cd93722f7b9"
        cmd = "disable dhcp vlan {0}".format(arg_dictionary['vlan_name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_port(self, arg_dictionary, **kwargs):
        uuid = "4dfb6620-78ca-4385-b300-b25861893a72"
        cmd = "enable dhcp ports {0} vlan {1}".format(arg_dictionary['port'],
                                                      arg_dictionary['vlan_name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_port(self, arg_dictionary, **kwargs):
        uuid = "48ab5fcb-082d-4ed6-b33e-219920b3f1a7"
        cmd = "disable dhcp ports {0} vlan {1}".format(arg_dictionary['port'],
                                                       arg_dictionary['vlan_name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_bootprelay_vlan(self, arg_dictionary, **kwargs):
        uuid = "66669dfd-e515-42ed-96a3-a91040ab81f6"
        cmd = "enable bootprelay ipv4 vlan {0}".format(arg_dictionary['vlan_name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_address_range(self, arg_dictionary, **kwargs):
        uuid = "751f49d4-8fd5-4a9d-b177-bcbf1e8110bc"
        cmd = "configure vlan {0} dhcp-address-range {1} - {2}".format(arg_dictionary['vlan_name'],
                                                                       arg_dictionary['start_addr'],
                                                                       arg_dictionary['end_addr'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_lease_time(self, arg_dictionary, **kwargs):
        uuid = "74c693f6-a9f6-4e2c-8218-412df2631e82"
        cmd = "configure vlan {0} dhcp-lease-timer {1}".format(arg_dictionary['vlan_name'],
                                                               arg_dictionary['seconds'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_netlogin_lease_time(self, arg_dictionary, **kwargs):
        uuid = "d708d78b-4f60-4f47-92d7-a8878f97c96f"
        cmd = "configure vlan {0} netlogin-lease-timer {1}".format(arg_dictionary['vlan_name'],
                                                                   arg_dictionary['seconds'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_options_gateway(self, arg_dictionary, **kwargs):
        uuid = "c53e256f-6efa-4c43-9579-b21d3ba4885a"
        cmd = "configure vlan {0} dhcp-options default-gateway {1}".format(arg_dictionary['vlan_name'],
                                                                           arg_dictionary['gateway_addr'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_options_dns(self, arg_dictionary, **kwargs):
        uuid = "1bf8479f-6b23-418a-b64e-c1b607df125c"
        cmd = "configure vlan {0} dhcp-options dns-server {1}".format(arg_dictionary['vlan_name'],
                                                                      arg_dictionary['dns_addr'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_options_dns_pri(self, arg_dictionary, **kwargs):
        uuid = "b0ea2231-5950-43d8-90ae-b0e5e4624b86"
        cmd = "configure vlan {0} dhcp-options dns-server primary {1}".format(arg_dictionary['vlan_name'],
                                                                              arg_dictionary['dns_addr'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_options_dns_sec(self, arg_dictionary, **kwargs):
        uuid = "ba87f7ba-07a7-447a-b8af-8d07af7b304e"
        cmd = "configure vlan {0} dhcp-options dns-server secondary {1}".format(arg_dictionary['vlan_name'],
                                                                                arg_dictionary['dns_addr'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_bootprelay_ip(self, arg_dictionary, **kwargs):
        uuid = "b21625a1-7eb3-4836-b7e7-7aec620729d5"
        cmd = "configure bootprelay add {0} vr {1}".format(arg_dictionary['ip'],
                                                           arg_dictionary['vr'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_address_range(self, arg_dictionary, **kwargs):
        uuid = "fe3e3c6c-e698-4384-b64f-658b68054f92"
        cmd = "unconfigure vlan {0} dhcp-address-range".format(arg_dictionary['vlan_name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_lease_time(self, arg_dictionary, **kwargs):
        uuid = "c56985ed-e4d9-4ac8-9ca4-cdb304e912af"
        cmd = "configure vlan {0} dhcp-lease-timer 300".format(arg_dictionary['vlan_name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_netlogin_lease_time(self, arg_dictionary, **kwargs):
        uuid = "26aa9bb0-58d7-42ac-88c0-5f3b7865ec4a"
        cmd = "configure vlan {0} netlogin-lease-timer 10".format(arg_dictionary['vlan_name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_global(self, arg_dictionary, **kwargs):
        uuid = "5a3dc96a-b3f5-4a95-bea8-20afd1a27e27"
        cmd = "unconfigure vlan {0} dhcp".format(arg_dictionary['vlan_name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_options_gateway(self, arg_dictionary, **kwargs):
        uuid = "eb990672-d516-471d-bc82-0a79136bc4e8"
        cmd = "unconfigure vlan {0} dhcp-options default-gateway".format(arg_dictionary['vlan_name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_options_dns(self, arg_dictionary, **kwargs):
        uuid = "92351040-86fd-471d-bcec-1eedb2b37967"
        cmd = "configure vlan {0} dhcp-options dns-server".format(arg_dictionary['vlan_name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_options_dns_pri(self, arg_dictionary, **kwargs):
        uuid = "9035ed79-1b7d-48cc-b525-f8ddf589e889"
        cmd = "configure vlan {0} dhcp-options dns-server primary".format(arg_dictionary['vlan_name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_options_dns_sec(self, arg_dictionary, **kwargs):
        uuid = "4bce6caf-0ce0-41eb-afcd-39331cb4b12c"
        cmd = "configure vlan {0} dhcp-options dns-server secondary".format(arg_dictionary['vlan_name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_info(self, arg_dictionary, **kwargs):
        uuid = "bcd409ba-54fa-4127-acd3-c1283652926b"
        cmd = "show vlan {0} dhcp-config".format(arg_dictionary['vlan_name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_address_allocation(self, arg_dictionary, **kwargs):
        uuid = "f895139e-a019-43e0-bbde-406e33d7328a"
        cmd = "show vlan {0} dhcp-address-allocation".format(arg_dictionary['vlan_name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_bootprelay_info(self, arg_dictionary, **kwargs):
        uuid = "f34b0397-90ce-47c9-86bb-c243f31d5c2b"
        cmd = "show bootprelay configuration"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
