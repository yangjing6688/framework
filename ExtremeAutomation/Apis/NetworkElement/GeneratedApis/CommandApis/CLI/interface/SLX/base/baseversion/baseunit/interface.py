"""
All interface supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.interface.base.interfacebase import \
    InterfaceBase


class Interface(DeviceApi, InterfaceBase):
    def __init__(self, device_input):
        super(Interface, self).__init__(device_input)

    def create_loopback(self, arg_dictionary, **kwargs):
        uuid = "2bcbdcdf-2fff-4e3f-b5ac-c3502a06458d"
        cmd = "interface Loopback {0}".format(arg_dictionary['interface'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def delete_loopback(self, arg_dictionary, **kwargs):
        uuid = "bd23349d-790b-4ab6-97ed-57cebbfefa34"
        cmd = "no interface loopback {0}".format(arg_dictionary['interface'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_interface(self, arg_dictionary, **kwargs):
        uuid = "868e70b1-cdad-49e8-bf4d-21c57260c778"
        cmd = "no shutdown"
        prompt = "intfPrompt"
        prompt_args = "interface Loopback {0}".format(arg_dictionary['interface'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def disable_interface(self, arg_dictionary, **kwargs):
        uuid = "e0ae15d1-2638-420b-9e85-553cbfd83300"
        cmd = "shutdown"
        prompt = "intfPrompt"
        prompt_args = "interface Loopback {0}".format(arg_dictionary['interface'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_ipv4_primary_addr_prefix_on_port(self, arg_dictionary, **kwargs):
        uuid = "3cd9a3e3-01b4-4f49-9175-01115be2a3fa"
        cmd = "ip address {0}/{1}".format(arg_dictionary['ip'],
                                          arg_dictionary['prefix'])
        prompt = "intfPrompt"
        prompt_args = "interface Ethernet {0}".format(arg_dictionary['interface'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_ipv4_loopback_addr_prefix(self, arg_dictionary, **kwargs):
        uuid = "70097850-8529-4f50-aecb-94c8ad335ffe"
        cmd = "ip address {0}/{1}".format(arg_dictionary['ip'],
                                          arg_dictionary['prefix'])
        prompt = "intfPrompt"
        prompt_args = "interface Loopback {0}".format(arg_dictionary['interface'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_ipv4_secondary_addr_prefix_on_port(self, arg_dictionary, **kwargs):
        uuid = "d91bf647-2141-431c-a333-7c18ec068987"
        cmd = "ip address {0}/{1} secondary".format(arg_dictionary['ip'],
                                                    arg_dictionary['prefix'])
        prompt = "intfPrompt"
        prompt_args = "interface Ethernet {0}".format(arg_dictionary['interface'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_ipv6_address_on_port(self, arg_dictionary, **kwargs):
        uuid = "492c31d1-b34f-4c4b-9618-410fe6f5cb1b"
        cmd = "ipv6 address {0}/{1}".format(arg_dictionary['ipv6_addr'],
                                            arg_dictionary['prefix'])
        prompt = "intfPrompt"
        prompt_args = "interface Ethernet {0}".format(arg_dictionary['interface'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_ipv6_link_local_addr_on_port(self, arg_dictionary, **kwargs):
        uuid = "b17f7577-754e-4232-98ed-50d70106777e"
        cmd = "ipv6 address use-link-local-only"
        prompt = "intfPrompt"
        prompt_args = "interface Ethernet {0}".format(arg_dictionary['interface'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_ipv6_eui64_address_on_port(self, arg_dictionary, **kwargs):
        uuid = "1e9e5bd7-4010-40ea-8f29-16d5c4539d0c"
        cmd = "ipv6 address {0}/{1} eui-64".format(arg_dictionary['prefix'],
                                                   arg_dictionary['prefix_len'])
        prompt = "intfPrompt"
        prompt_args = "interface Ethernet {0}".format(arg_dictionary['interface'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_ipv6_loopback_address(self, arg_dictionary, **kwargs):
        uuid = "6b58151f-b851-473e-91e3-f5a93558d704"
        cmd = "ipv6 address {0}/{1}".format(arg_dictionary['ipv6_addr'],
                                            arg_dictionary['prefix'])
        prompt = "intfPrompt"
        prompt_args = "interface Loopback {0}".format(arg_dictionary['interface'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def clear_ipv4_addr_prefix_on_port(self, arg_dictionary, **kwargs):
        uuid = "846dd3ea-46e2-4f4f-9391-14d796733a43"
        cmd = "no ip address"
        prompt = "intfPrompt"
        prompt_args = "interface Ethernet {0}".format(arg_dictionary['interface'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def clear_ipv6_address_on_port(self, arg_dictionary, **kwargs):
        uuid = "7d48aa22-eb31-4dff-b466-994965984199"
        cmd = "no ipv6 address"
        prompt = "intfPrompt"
        prompt_args = "interface Ethernet {0}".format(arg_dictionary['interface'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def clear_ipv6_loopback_address(self, arg_dictionary, **kwargs):
        uuid = "a1eb4078-0a5b-4d5a-af46-fef7e95ffced"
        cmd = "no ipv6 address"
        prompt = "intfPrompt"
        prompt_args = "interface Loopback {0}".format(arg_dictionary['interface'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def show_info_port(self, arg_dictionary, **kwargs):
        uuid = "4c9736a8-4f91-4f5c-8b3f-cdae7f88bc1f"
        cmd = "show interface ethernet {0}".format(arg_dictionary['interface'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_info_port_basic(self, arg_dictionary, **kwargs):
        uuid = "733a9bb3-1ab7-406a-9d79-07aaaffcea64"
        cmd = "show interface ethernet {0}".format(arg_dictionary['interface'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_loopback_info(self, arg_dictionary, **kwargs):
        uuid = "236da547-93df-4d0c-85ec-a90a58052239"
        cmd = "show interface loopback {0}".format(arg_dictionary['interface'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_all_ports(self, arg_dictionary, **kwargs):
        uuid = "2c5f8b8b-936a-4684-b5ed-86d88866d042"
        cmd = "show interface status"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_ipv6_port_info(self, arg_dictionary, **kwargs):
        uuid = "505276c0-f2b1-423d-a14a-582183dd3930"
        cmd = "show ipv6 interface ethernet {0}".format(arg_dictionary['interface'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_loopback(self, arg_dictionary, **kwargs):
        uuid = "b9307bf3-9ca0-47c7-9eab-7262ac8b9500"
        cmd = "show interface loopback {0}".format(arg_dictionary['loopback_id'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
