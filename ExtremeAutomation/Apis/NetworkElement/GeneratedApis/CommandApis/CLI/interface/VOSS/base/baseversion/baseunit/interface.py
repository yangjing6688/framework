"""
All interface supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.interface.base.interfacebase import \
    InterfaceBase


class Interface(DeviceApi, InterfaceBase):
    def __init__(self, device_input):
        super(Interface, self).__init__(device_input)

    def create_interface(self, arg_dictionary, **kwargs):
        uuid = "b5e7580f-4520-49c9-bd91-ebeb5b224013"
        cmd = ""
        prompt = "intfPrompt"
        prompt_args = "vlan {0}".format(arg_dictionary['interface'])
        conf = "exit"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args, conf=conf)

    def delete_interface(self, arg_dictionary, **kwargs):
        uuid = "2f7731c4-8177-4d5d-8cdd-cc08a0f5b973"
        cmd = "no vlan {0}".format(arg_dictionary['interface'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_ipv6_forwarding(self, arg_dictionary, **kwargs):
        uuid = "55461a7a-832c-43ba-9686-4f3041c2fa68"
        cmd = "ipv6 forwarding"
        prompt = "intfPrompt"
        prompt_args = "vlan {0}".format(arg_dictionary['interface'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def disable_ipv6_forwarding(self, arg_dictionary, **kwargs):
        uuid = "7f1cb95a-154e-4345-b5cc-696b449f733a"
        cmd = "no ipv6 forwarding"
        prompt = "intfPrompt"
        prompt_args = "vlan {0}".format(arg_dictionary['interface'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_ipv4_primary_addr_prefix(self, arg_dictionary, **kwargs):
        uuid = "c1ad8979-6fde-43a8-875a-68d081681141"
        cmd = "ip address {0}/{1}".format(arg_dictionary['ip'],
                                          arg_dictionary['prefix'])
        prompt = "intfPrompt"
        prompt_args = "vlan {0}".format(arg_dictionary['interface'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_ipv4_primary_addr_netmask(self, arg_dictionary, **kwargs):
        uuid = "4ab3999b-dd5b-49c8-823c-1662e6d27577"
        cmd = "ip address {0} {1}".format(arg_dictionary['ip'],
                                          arg_dictionary['netmask'])
        prompt = "intfPrompt"
        prompt_args = "vlan {0}".format(arg_dictionary['interface'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_ipv4_loopback_addr_prefix(self, arg_dictionary, **kwargs):
        uuid = "70097850-8529-4f50-aecb-94c8ad335ffe"
        cmd = "ip address {0}/{1}".format(arg_dictionary['ip'],
                                          arg_dictionary['prefix'])
        prompt = "intfPrompt"
        prompt_args = "loopback {0}".format(arg_dictionary['interface'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_ipv4_loopback_addr_netmask(self, arg_dictionary, **kwargs):
        uuid = "c6b81f78-a585-44d5-a8a6-9133f6040147"
        cmd = "ip address {0} {1} {2}".format(arg_dictionary['interface'],
                                              arg_dictionary['ip'],
                                              arg_dictionary['netmask'])
        prompt = "intfPrompt"
        prompt_args = "loopback {0}".format(arg_dictionary['interface'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_ipv6_address(self, arg_dictionary, **kwargs):
        uuid = "7b9b6449-4a37-49aa-94c2-684e7c9b16e1"
        cmd = "ipv6 interface address {0}/{1}".format(arg_dictionary['ipv6_addr'],
                                                      arg_dictionary['prefix'])
        prompt = "intfPrompt"
        prompt_args = "vlan {0}".format(arg_dictionary['interface'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_ipv6_link_local_addr(self, arg_dictionary, **kwargs):
        uuid = "b7dbcb5f-9cc1-427c-a664-57ca4a3ffb9e"
        cmd = "ipv6 interface link-local {0}".format(arg_dictionary['ipv6_addr'])
        prompt = "intfPrompt"
        prompt_args = "vlan {0}".format(arg_dictionary['interface'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_ipv6_loopback_address(self, arg_dictionary, **kwargs):
        uuid = "6b58151f-b851-473e-91e3-f5a93558d704"
        cmd = "ipv6 interface address {0}/{1}".format(arg_dictionary['ipv6_addr'],
                                                      arg_dictionary['prefix'])
        prompt = "intfPrompt"
        prompt_args = "loopback {0}".format(arg_dictionary['interface'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def clear_ipv4_addr_prefix(self, arg_dictionary, **kwargs):
        uuid = "b71694e4-08c1-4349-8731-8f4eda47aa4b"
        cmd = "no ip address {0}".format(arg_dictionary['ip'])
        prompt = "intfPrompt"
        prompt_args = "vlan {0}".format(arg_dictionary['interface'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def clear_ipv4_loopback_addr_netmask(self, arg_dictionary, **kwargs):
        uuid = "76011191-e5f1-485a-8972-a733c8aac574"
        cmd = "no ip address {0} {1}".format(arg_dictionary['interface'],
                                             arg_dictionary['ip'])
        prompt = "intfPrompt"
        prompt_args = "loopback {0}".format(arg_dictionary['interface'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def clear_ipv6_address(self, arg_dictionary, **kwargs):
        uuid = "2ce752f3-b2f6-41bc-be3b-851216112a9c"
        cmd = "no ipv6 interface address {0}".format(arg_dictionary['ipv6_addr'])
        prompt = "intfPrompt"
        prompt_args = "vlan {0}".format(arg_dictionary['interface'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def clear_ipv6_loopback_address(self, arg_dictionary, **kwargs):
        uuid = "a1eb4078-0a5b-4d5a-af46-fef7e95ffced"
        cmd = "no ipv6 interface address {0}".format(arg_dictionary['ipv6_addr'])
        prompt = "intfPrompt"
        prompt_args = "loopback {0}".format(arg_dictionary['interface'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def enable_ipv6_vlan(self, arg_dictionary, **kwargs):
        uuid = "83fdb41e-e564-4965-9745-d916eb6ab086"
        cmd = "ipv6 interface enable"
        prompt = "intfPrompt"
        prompt_args = "vlan {0}".format(arg_dictionary['interface'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def disable_ipv6_vlan(self, arg_dictionary, **kwargs):
        uuid = "ebb0c2a9-2647-49e0-a822-0f038f36f2d0"
        cmd = "no ipv6 interface enable"
        prompt = "intfPrompt"
        prompt_args = "vlan {0}".format(arg_dictionary['interface'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def enable_ip_forwarding_global(self, arg_dictionary, **kwargs):
        uuid = "341d0432-4af1-4193-81e2-b4fc78474495"
        cmd = "ip routing"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_ip_forwarding_global(self, arg_dictionary, **kwargs):
        uuid = "96cdbab4-c572-4776-9293-49dcb26a8b13"
        cmd = "no ip routing"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_ipv6_forwarding_global(self, arg_dictionary, **kwargs):
        uuid = "6d0bf439-55ff-4fef-9fe8-41921db1d612"
        cmd = "ipv6 forwarding"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_ipv6_forwarding_global(self, arg_dictionary, **kwargs):
        uuid = "4e3ca9b4-acbc-4cde-a93d-95630a943507"
        cmd = "no ipv6 forwarding"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_vlan_spb_multicast(self, arg_dictionary, **kwargs):
        uuid = "ad88dae7-329a-4f54-990e-02994e9797c2"
        cmd = "ip spb-multicast enable"
        prompt = "intfPrompt"
        prompt_args = "vlan {0}".format(arg_dictionary['interface'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def disable_vlan_spb_multicast(self, arg_dictionary, **kwargs):
        uuid = "f2d7faac-7535-4ac4-9274-be5991750c73"
        cmd = "no ip spb-multicast enable"
        prompt = "intfPrompt"
        prompt_args = "vlan {0}".format(arg_dictionary['interface'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def enable_chassis_force_topology_ip_flag(self, arg_dictionary, **kwargs):
        uuid = "548a81df-daa9-44ed-b511-5cc9da7ba746"
        cmd = "sys force-topology-ip-flag enable"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_chassis_force_topology_ip_flag(self, arg_dictionary, **kwargs):
        uuid = "c0f16a1b-2b8e-4a47-af20-b2144ca26db5"
        cmd = "no sys force-topology-ip-flag enable"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_ipv4_brouter_port(self, arg_dictionary, **kwargs):
        uuid = "aad1181d-e49c-4288-80d2-3f39043e1aa0"
        cmd = "brouter port {0} vlan {1} subnet {2} {3} mac-offset {4}".format(arg_dictionary['port'],
                                                                               arg_dictionary['vlan'],
                                                                               arg_dictionary['ip'],
                                                                               arg_dictionary['netmask'],
                                                                               arg_dictionary['mac_offset'])
        prompt = "intfPrompt"
        prompt_args = "GigabitEthernet {0}".format(arg_dictionary['port'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def clear_ipv4_brouter_port(self, arg_dictionary, **kwargs):
        uuid = "3c49a65a-5612-4fad-9dc4-c8235763425b"
        cmd = "no brouter port {0}".format(arg_dictionary['port'])
        prompt = "intfPrompt"
        prompt_args = "GigabitEthernet {0}".format(arg_dictionary['port'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def show_info(self, arg_dictionary, **kwargs):
        uuid = "15cdbea8-ad6f-4fb9-9b52-e77cf8d4cf84"
        cmd = "show interfaces vlan ip {0}".format(arg_dictionary['interface'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_info_basic(self, arg_dictionary, **kwargs):
        uuid = "06c7a0d8-5f87-4c5b-9da6-fbc301fb3286"
        cmd = "show interfaces vlan ip {0}".format(arg_dictionary['interface'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_loopback_info(self, arg_dictionary, **kwargs):
        uuid = "236da547-93df-4d0c-85ec-a90a58052239"
        cmd = "show interfaces vlan ip {0}".format(arg_dictionary['interface'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_all(self, arg_dictionary, **kwargs):
        uuid = "d9b49c07-4e41-4aa8-99b0-591c4b8c5842"
        cmd = "show interfaces vlan ip"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_ipv6_info(self, arg_dictionary, **kwargs):
        uuid = "3fd0af31-77fc-4b10-a61d-994c08e33347"
        cmd = "show ipv6 address interface vlan {0}".format(arg_dictionary['interface'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_loopback(self, arg_dictionary, **kwargs):
        uuid = "b9307bf3-9ca0-47c7-9eab-7262ac8b9500"
        cmd = "show interfaces loopback"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_brouter_port_vlan(self, arg_dictionary, **kwargs):
        uuid = "05830d6c-7ed5-408e-a134-fc9c73806a84"
        cmd = "show brouter | include {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_brouter_port_ipv4(self, arg_dictionary, **kwargs):
        uuid = "715182e6-dc59-49b0-818c-c66452ea44ca"
        cmd = "show interfaces {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_chassis_force_topology_ip_flag(self, arg_dictionary, **kwargs):
        uuid = "f74a7839-db65-4830-ab01-a5b09061e90d"
        cmd = "show sys setting"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_ipv6_vlan(self, arg_dictionary, **kwargs):
        uuid = "f6b298c6-b4d2-4208-a6d9-312f982a9bfc"
        cmd = "show ipv6 interface vlan {0}".format(arg_dictionary['interface'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_vlan_vrf(self, arg_dictionary, **kwargs):
        uuid = "972489ae-f177-4716-8e4b-1a225c12bd35"
        cmd = "show interfaces vlan vrf {0}".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_vlan_vrf_spb(self, arg_dictionary, **kwargs):
        uuid = "7372931f-f04c-4554-8799-5e9b47e27058"
        cmd = "show ip mroute interface vrf {0}".format(arg_dictionary['vrf_name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_vlan_spb(self, arg_dictionary, **kwargs):
        uuid = "12a39efd-1b96-4b35-8b4e-113833270f0d"
        cmd = "show ip mroute interface"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
