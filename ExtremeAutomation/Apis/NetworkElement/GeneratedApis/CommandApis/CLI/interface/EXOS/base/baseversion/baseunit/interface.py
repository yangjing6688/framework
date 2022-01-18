"""
All interface supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.interface.base.interfacebase import \
    InterfaceBase


class Interface(DeviceApi, InterfaceBase):
    def __init__(self, device_input):
        super(Interface, self).__init__(device_input)

    def delete_interface(self, arg_dictionary, **kwargs):
        uuid = "2f7731c4-8177-4d5d-8cdd-cc08a0f5b973"
        cmd = "delete vlan {0}".format(arg_dictionary['interface'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def create_loopback(self, arg_dictionary, **kwargs):
        uuid = "2bcbdcdf-2fff-4e3f-b5ac-c3502a06458d"
        cmd = "create vlan {0}".format(arg_dictionary['interface'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def delete_loopback(self, arg_dictionary, **kwargs):
        uuid = "bd23349d-790b-4ab6-97ed-57cebbfefa34"
        cmd = "delete vlan {0}".format(arg_dictionary['interface'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_interface(self, arg_dictionary, **kwargs):
        uuid = "868e70b1-cdad-49e8-bf4d-21c57260c778"
        cmd = "enable vlan {0}".format(arg_dictionary['interface'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_interface(self, arg_dictionary, **kwargs):
        uuid = "e0ae15d1-2638-420b-9e85-553cbfd83300"
        cmd = "disable vlan {0}".format(arg_dictionary['interface'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_ip_forwarding(self, arg_dictionary, **kwargs):
        uuid = "254578ba-4b09-4b11-94ab-54e2e35b6d80"
        cmd = "enable ipforwarding vlan {0}".format(arg_dictionary['interface'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_ip_forwarding(self, arg_dictionary, **kwargs):
        uuid = "8cdb265e-1431-402f-83d7-7802591dcc4c"
        cmd = "disable ipforwarding vlan {0}".format(arg_dictionary['interface'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_ipv6_forwarding(self, arg_dictionary, **kwargs):
        uuid = "55461a7a-832c-43ba-9686-4f3041c2fa68"
        cmd = "enable ipforwarding ipv6 vlan {0}".format(arg_dictionary['interface'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_ipv6_forwarding(self, arg_dictionary, **kwargs):
        uuid = "7f1cb95a-154e-4345-b5cc-696b449f733a"
        cmd = "disable ipforwarding ipv6 vlan {0}".format(arg_dictionary['interface'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_loopback(self, arg_dictionary, **kwargs):
        uuid = "698df2b4-d089-47d8-8bad-16810ca0dfa4"
        cmd = "enable loopback-mode vlan {0}".format(arg_dictionary['interface'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_loopback(self, arg_dictionary, **kwargs):
        uuid = "7b5568fb-59c7-4e53-84ee-fdba6d87d981"
        cmd = "disable loopback-mode vlan {0}".format(arg_dictionary['interface'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_ipv4_primary_addr_prefix(self, arg_dictionary, **kwargs):
        uuid = "c1ad8979-6fde-43a8-875a-68d081681141"
        cmd = "configure vlan {0} ipaddress {1}/{2}".format(arg_dictionary['interface'],
                                                            arg_dictionary['ip'],
                                                            arg_dictionary['prefix'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_ipv4_primary_addr_netmask(self, arg_dictionary, **kwargs):
        uuid = "4ab3999b-dd5b-49c8-823c-1662e6d27577"
        cmd = "configure vlan {0} ipaddress {1} {2}".format(arg_dictionary['interface'],
                                                            arg_dictionary['ip'],
                                                            arg_dictionary['netmask'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_ipv4_loopback_addr_prefix(self, arg_dictionary, **kwargs):
        uuid = "70097850-8529-4f50-aecb-94c8ad335ffe"
        cmd = "configure vlan {0} ipaddress {1}/{2}".format(arg_dictionary['interface'],
                                                            arg_dictionary['ip'],
                                                            arg_dictionary['prefix'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_ipv4_loopback_addr_netmask(self, arg_dictionary, **kwargs):
        uuid = "c6b81f78-a585-44d5-a8a6-9133f6040147"
        cmd = "configure vlan {0} ipaddress {1} {2}".format(arg_dictionary['interface'],
                                                            arg_dictionary['ip'],
                                                            arg_dictionary['netmask'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_ipv4_secondary_addr_prefix(self, arg_dictionary, **kwargs):
        uuid = "69dabb6e-504e-4ffa-b90e-06ce2d0ac9ca"
        cmd = "configure vlan {0} add secondary-ipaddress {1}/{2}".format(arg_dictionary['interface'],
                                                                          arg_dictionary['ip'],
                                                                          arg_dictionary['prefix'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_ipv4_secondary_addr_netmask(self, arg_dictionary, **kwargs):
        uuid = "7a54c0e5-3317-452d-a7af-450d8a8d72da"
        cmd = "configure vlan {0} add secondary-ipaddress {1} {2}".format(arg_dictionary['interface'],
                                                                          arg_dictionary['ip'],
                                                                          arg_dictionary['netmask'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_ipv6_address(self, arg_dictionary, **kwargs):
        uuid = "7b9b6449-4a37-49aa-94c2-684e7c9b16e1"
        cmd = "configure vlan {0} ipaddress {1}/{2}".format(arg_dictionary['interface'],
                                                            arg_dictionary['ipv6_addr'],
                                                            arg_dictionary['prefix'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_ipv6_link_local_addr(self, arg_dictionary, **kwargs):
        uuid = "b7dbcb5f-9cc1-427c-a664-57ca4a3ffb9e"
        cmd = "configure vlan {0} ipaddress {1}/{2}".format(arg_dictionary['interface'],
                                                            arg_dictionary['ipv6_addr'],
                                                            arg_dictionary['prefix'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_ipv6_eui64_address(self, arg_dictionary, **kwargs):
        uuid = "d20198be-8ab6-499b-90bf-ec2fac05ab76"
        cmd = "configure vlan {0} ipaddress eui64 {1}/{2}".format(arg_dictionary['interface'],
                                                                  arg_dictionary['prefix'],
                                                                  arg_dictionary['prefix_len'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_ipv6_loopback_address(self, arg_dictionary, **kwargs):
        uuid = "6b58151f-b851-473e-91e3-f5a93558d704"
        cmd = "configure vlan {0} ipaddress {1}/{2}".format(arg_dictionary['interface'],
                                                            arg_dictionary['ipv6_addr'],
                                                            arg_dictionary['prefix'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_ipv4_addr_prefix(self, arg_dictionary, **kwargs):
        uuid = "b71694e4-08c1-4349-8731-8f4eda47aa4b"
        cmd = "unconfigure vlan {0} ipaddress".format(arg_dictionary['interface'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_ipv4_loopback_addr_netmask(self, arg_dictionary, **kwargs):
        uuid = "76011191-e5f1-485a-8972-a733c8aac574"
        cmd = "unconfigure vlan {0} ipaddress".format(arg_dictionary['interface'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_ipv6_address(self, arg_dictionary, **kwargs):
        uuid = "2ce752f3-b2f6-41bc-be3b-851216112a9c"
        cmd = "unconfigure vlan {0} ipaddress".format(arg_dictionary['interface'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_ipv6_loopback_address(self, arg_dictionary, **kwargs):
        uuid = "a1eb4078-0a5b-4d5a-af46-fef7e95ffced"
        cmd = "unconfigure vlan {0} ipaddress".format(arg_dictionary['interface'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_info(self, arg_dictionary, **kwargs):
        uuid = "15cdbea8-ad6f-4fb9-9b52-e77cf8d4cf84"
        cmd = "show vlan {0}".format(arg_dictionary['interface'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_info_basic(self, arg_dictionary, **kwargs):
        uuid = "06c7a0d8-5f87-4c5b-9da6-fbc301fb3286"
        cmd = "show vlan {0}".format(arg_dictionary['interface'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_loopback_info(self, arg_dictionary, **kwargs):
        uuid = "236da547-93df-4d0c-85ec-a90a58052239"
        cmd = "show vlan {0}".format(arg_dictionary['interface'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_all(self, arg_dictionary, **kwargs):
        uuid = "d9b49c07-4e41-4aa8-99b0-591c4b8c5842"
        cmd = "show vlan"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_ipv6_info(self, arg_dictionary, **kwargs):
        uuid = "3fd0af31-77fc-4b10-a61d-994c08e33347"
        cmd = "show vlan {0}".format(arg_dictionary['interface'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
