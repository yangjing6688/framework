"""
All isis supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.isis.base.isisbase import IsisBase


class Isis(DeviceApi, IsisBase):
    def __init__(self, device_input):
        super(Isis, self).__init__(device_input)

    def enable_global(self, arg_dictionary, **kwargs):
        uuid = "5e8b2b77-f570-4a1c-b139-c933c7547bd6"
        cmd = "router isis enable"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_global(self, arg_dictionary, **kwargs):
        uuid = "695b2829-e1be-4156-878a-46a23c9ee9b9"
        cmd = "no router isis enable"
        prompt = "routerConfigPrompt"
        conf = "(y/n) ?"
        conf_args = "y"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf, conf_args=conf_args)

    def set_system_id(self, arg_dictionary, **kwargs):
        uuid = "e822f7ac-4816-4653-9a92-8e9407962160"
        cmd = "router isis||system-id {0}".format(arg_dictionary['sys_id'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_system_id(self, arg_dictionary, **kwargs):
        uuid = "7ea7fdb1-bfe2-42da-8034-04396957f7ba"
        cmd = "router isis||no system-id"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_manual_area(self, arg_dictionary, **kwargs):
        uuid = "f3d86c30-2ecd-4ce4-afca-1b3c59cb5757"
        cmd = "router isis||manual-area {0}".format(arg_dictionary['manual_area'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_manual_area(self, arg_dictionary, **kwargs):
        uuid = "9d3f74cd-aa7c-40a6-84dc-5090ab1821f3"
        cmd = "router isis||no manual-area {0}".format(arg_dictionary['manual_area'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_sys_name(self, arg_dictionary, **kwargs):
        uuid = "16686ac8-176a-40e9-9844-fade015600e5"
        cmd = "router isis||sys-name {0}".format(arg_dictionary['name'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_sys_name(self, arg_dictionary, **kwargs):
        uuid = "6ecbe2df-faf8-4ea0-b952-99405a04f618"
        cmd = "router isis||no sys-name"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_ipv4_source_address(self, arg_dictionary, **kwargs):
        uuid = "7e1e2500-a337-4c22-8923-6d86af2baa7d"
        cmd = "router isis||ip-source-address {0}||exit".format(arg_dictionary['ip'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_ipv4_source_address(self, arg_dictionary, **kwargs):
        uuid = "f519f5e3-fea8-4b48-a10c-2b3c9d0a56b5"
        cmd = "router isis||no ip-source-address||exit"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_ipv6_source_address(self, arg_dictionary, **kwargs):
        uuid = "20b845c4-0d34-4048-9c90-f919c9ffd485"
        cmd = "router isis||ipv6-source-address {0}||exit".format(arg_dictionary['ipv6_addr'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_ipv6_source_address(self, arg_dictionary, **kwargs):
        uuid = "c95faa61-10c5-4f0b-a7fa-4e15cafab5c3"
        cmd = "router isis||no ipv6-source-address||exit"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_ipv4_tunnel_source_address(self, arg_dictionary, **kwargs):
        uuid = "496e1ece-fba0-4acf-8850-fdba99593a44"
        cmd = "router isis||ip-tunnel-source-address {0}||exit".format(arg_dictionary['ip'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_ipv4_tunnel_source_address(self, arg_dictionary, **kwargs):
        uuid = "76e25363-c4ea-4d8a-9bab-e8b73138b869"
        cmd = "router isis||no ip-tunnel-source-address||exit"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_inband_mgmt_ip(self, arg_dictionary, **kwargs):
        uuid = "b198e339-a35f-460e-bb1d-e33b67b27722"
        cmd = "router isis||inband-mgmt-ip {0}".format(arg_dictionary['ip'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_inband_mgmt_ip(self, arg_dictionary, **kwargs):
        uuid = "a3ba0f4b-ca67-4422-89f9-2c20e76f61dc"
        cmd = "router isis||no inband-mgmt-ip"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_metric_narrow(self, arg_dictionary, **kwargs):
        uuid = "1c5d648c-872d-43e8-b429-933c306cc815"
        cmd = "router isis||metric narrow"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_metric_narrow(self, arg_dictionary, **kwargs):
        uuid = "1791f449-aaad-4d21-8db0-88214147709e"
        cmd = "router isis||no metric"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_metric_wide(self, arg_dictionary, **kwargs):
        uuid = "76da7bee-e0bf-484d-b26d-8c5a88263b5e"
        cmd = "router isis||metric wide"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_metric_wide(self, arg_dictionary, **kwargs):
        uuid = "c0fcf7c7-632a-4ad7-9a3f-22113bd9da38"
        cmd = "router isis||no metric"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_overload(self, arg_dictionary, **kwargs):
        uuid = "dd0b7750-44a2-4fb7-bc26-89442f3b03d4"
        cmd = "router isis||overload"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_overload(self, arg_dictionary, **kwargs):
        uuid = "ad2a98c5-e61e-424c-8673-42af44212485"
        cmd = "router isis||no overload"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_redistribute_bgp(self, arg_dictionary, **kwargs):
        uuid = "d64e0783-f82d-47aa-8b9c-fb1228323d6b"
        cmd = "router isis||redistribute bgp||exit"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_redistribute_bgp(self, arg_dictionary, **kwargs):
        uuid = "19e03588-ec5e-4322-b59a-93a73c1deea9"
        cmd = "router isis||no redistribute bgp||exit"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_redistribute_bgp(self, arg_dictionary, **kwargs):
        uuid = "d0a806dc-dec4-4261-8665-bec6ad3d2f24"
        cmd = "router isis||redistribute bgp enable||exit"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_redistribute_bgp(self, arg_dictionary, **kwargs):
        uuid = "e8d423aa-74c0-430c-9326-87be7dc41b18"
        cmd = "router isis||no redistribute bgp enable||exit"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_redistribute_direct(self, arg_dictionary, **kwargs):
        uuid = "20aefb6c-0894-4e13-a3a3-ff1541343dad"
        cmd = "router isis||redistribute direct||exit"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_redistribute_direct(self, arg_dictionary, **kwargs):
        uuid = "f37c174b-1650-4ae7-b20d-0af748785751"
        cmd = "router isis||no redistribute direct||exit"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_redistribute_direct(self, arg_dictionary, **kwargs):
        uuid = "09f6db17-41c7-4533-8a9f-2ac452f6173c"
        cmd = "router isis||redistribute direct enable||exit"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_redistribute_direct(self, arg_dictionary, **kwargs):
        uuid = "0ea31ada-4642-41ba-89cf-64b70d432b2b"
        cmd = "router isis||no redistribute direct enable||exit"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_redistribute_direct_ipv6(self, arg_dictionary, **kwargs):
        uuid = "495d343f-d8a9-492c-a1f4-d746dbd25fda"
        cmd = "router isis||ipv6 redistribute direct enable||exit"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_redistribute_direct_ipv6(self, arg_dictionary, **kwargs):
        uuid = "9b128fb6-ff78-4a70-b70c-6df61e6f4a95"
        cmd = "router isis||no ipv6 redistribute direct enable||exit"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_redistribute_direct_apply(self, arg_dictionary, **kwargs):
        uuid = "c5c6d7b8-c182-484f-a328-246031a1284f"
        cmd = "isis apply redistribute direct"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_redistribute_direct_route_map_policy(self, arg_dictionary, **kwargs):
        uuid = "3bd8cad2-55a6-4775-9d84-1a1dd0c5bc53"
        cmd = "router isis||redistribute direct route-map {0}||exit".format(arg_dictionary['policy_name'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_redistribute_direct_route_map_policy(self, arg_dictionary, **kwargs):
        uuid = "cffea40d-754d-4b00-b803-3265f345afb0"
        cmd = "router isis||no redistribute direct route-map ||exit"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_redistribute_ospf(self, arg_dictionary, **kwargs):
        uuid = "6a9af17b-8fe4-49e4-8e13-3c9c4c915dca"
        cmd = "router isis||redistribute ospf||exit"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_redistribute_ospf(self, arg_dictionary, **kwargs):
        uuid = "448c323c-e460-444d-afd9-c9797714c37f"
        cmd = "router isis||no redistribute ospf||exit"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_redistribute_ospf(self, arg_dictionary, **kwargs):
        uuid = "edb590f7-7bae-43c8-91ac-1e81d05bac91"
        cmd = "router isis||redistribute ospf enable||exit"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_redistribute_ospf(self, arg_dictionary, **kwargs):
        uuid = "8d67a62b-5750-46aa-965f-70971738de7b"
        cmd = "router isis||no redistribute ospf enable||exit"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_redistribute_rip(self, arg_dictionary, **kwargs):
        uuid = "571889fe-477c-46a4-980f-fc68c9c07945"
        cmd = "router isis||redistribute rip||exit"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_redistribute_rip(self, arg_dictionary, **kwargs):
        uuid = "e67af810-a0cc-499e-ae8e-782c9a553547"
        cmd = "router isis||no redistribute rip||exit"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_redistribute_rip(self, arg_dictionary, **kwargs):
        uuid = "16611f69-56cf-4fa8-b09f-ea599503cb57"
        cmd = "router isis||redistribute rip enable||exit"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_redistribute_rip(self, arg_dictionary, **kwargs):
        uuid = "adf56f6a-4266-44a5-a38d-5e05300a41db"
        cmd = "router isis||no redistribute rip enable||exit"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_redistribute_static(self, arg_dictionary, **kwargs):
        uuid = "63cdc549-5245-46f9-b5cd-3c50cd399d44"
        cmd = "router isis||redistribute static||exit"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_redistribute_static(self, arg_dictionary, **kwargs):
        uuid = "e03c7d05-b7e0-4149-b875-ea08c9156d03"
        cmd = "router isis||no redistribute static||exit"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_redistribute_static(self, arg_dictionary, **kwargs):
        uuid = "e74e23c1-2c91-47b4-8e83-ecfb889f8ada"
        cmd = "router isis||redistribute static enable||exit"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_redistribute_static(self, arg_dictionary, **kwargs):
        uuid = "3513c128-ad24-41f4-a6df-12338b62dc6d"
        cmd = "router isis||no redistribute static enable||exit"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_redistribute_apply(self, arg_dictionary, **kwargs):
        uuid = "6306c6cd-5828-4f83-87fc-f8e2196a8dcb"
        cmd = "isis apply redistribute||exit"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_spf_delay(self, arg_dictionary, **kwargs):
        uuid = "710ce659-c09c-4f29-9dc9-7ecba7e6c078"
        cmd = "router isis||spf-delay {0}".format(arg_dictionary['delay'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_spf_delay(self, arg_dictionary, **kwargs):
        uuid = "75a848f5-f768-402c-9d72-fb28adec3f5f"
        cmd = "router isis||no spf-delay"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_circuit_on_port(self, arg_dictionary, **kwargs):
        uuid = "6fb5a6ce-d257-4aa6-9b6b-218064622469"
        cmd = "isis"
        prompt = "intfPrompt"
        prompt_args = "GigabitEthernet {0}".format(arg_dictionary['port'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def enable_circuit_on_port(self, arg_dictionary, **kwargs):
        uuid = "81736c7f-0658-423c-ac8a-804632dfeeb4"
        cmd = "isis enable"
        prompt = "intfPrompt"
        prompt_args = "GigabitEthernet {0}".format(arg_dictionary['port'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def disable_circuit_on_port(self, arg_dictionary, **kwargs):
        uuid = "63620079-ea8b-44d6-8a30-d50c1b3771fc"
        cmd = "no isis enable"
        prompt = "intfPrompt"
        prompt_args = "GigabitEthernet {0}".format(arg_dictionary['port'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def clear_circuit_on_port(self, arg_dictionary, **kwargs):
        uuid = "a507ebbd-9d73-4db5-bce9-966c29e42954"
        cmd = "no isis"
        prompt = "intfPrompt"
        prompt_args = "GigabitEthernet {0}".format(arg_dictionary['port'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_circuit_on_mlt(self, arg_dictionary, **kwargs):
        uuid = "73f4e284-3f73-4faf-b3de-72bf65186267"
        cmd = "isis"
        prompt = "intfPrompt"
        prompt_args = "mlt {0}".format(arg_dictionary['mlt_id'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def enable_circuit_on_mlt(self, arg_dictionary, **kwargs):
        uuid = "fe1f3a9a-2ba5-4653-bb89-d961ba397eac"
        cmd = "isis enable"
        prompt = "intfPrompt"
        prompt_args = "mlt {0}".format(arg_dictionary['mlt_id'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def disable_circuit_on_mlt(self, arg_dictionary, **kwargs):
        uuid = "a7cd4661-5a80-476b-a5f2-ca98f8a66eb4"
        cmd = "no isis enable"
        prompt = "intfPrompt"
        prompt_args = "mlt {0}".format(arg_dictionary['mlt_id'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def clear_circuit_on_mlt(self, arg_dictionary, **kwargs):
        uuid = "ff807daf-f443-4d1c-9d8b-e30f200d4b36"
        cmd = "no isis"
        prompt = "intfPrompt"
        prompt_args = "mlt {0}".format(arg_dictionary['mlt_id'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_auth_on_port(self, arg_dictionary, **kwargs):
        uuid = "041f1993-d357-4926-9d14-efb8acbe5c68"
        cmd = "isis hello-auth type {0} key {1} key-id {2}".format(arg_dictionary['auth_type'],
                                                                   arg_dictionary['auth_key'],
                                                                   arg_dictionary['key_id'])
        prompt = "intfPrompt"
        prompt_args = "GigabitEthernet {0}".format(arg_dictionary['port'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_auth_on_mlt(self, arg_dictionary, **kwargs):
        uuid = "a2e60ffb-9f97-4bf0-9864-37f5e333c6bf"
        cmd = "isis hello-auth type {0} key {1} key-id {2}".format(arg_dictionary['auth_type'],
                                                                   arg_dictionary['auth_key'],
                                                                   arg_dictionary['key_id'])
        prompt = "intfPrompt"
        prompt_args = "mlt {0}".format(arg_dictionary['mlt_id'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def clear_auth_on_port(self, arg_dictionary, **kwargs):
        uuid = "1e95c189-151e-439d-a953-fc1d7f81bf8c"
        cmd = "no isis hello-auth"
        prompt = "intfPrompt"
        prompt_args = "GigabitEthernet {0}".format(arg_dictionary['port'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def clear_auth_on_mlt(self, arg_dictionary, **kwargs):
        uuid = "6e813614-15bc-4ce9-b5cd-f898942a1d00"
        cmd = "no isis hello-auth"
        prompt = "intfPrompt"
        prompt_args = "mlt {0}".format(arg_dictionary['mlt_id'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_l1_dr_priority_on_port(self, arg_dictionary, **kwargs):
        uuid = "8e30408c-7b97-4c58-9de1-5203240f5c14"
        cmd = "isis l1-dr-priority {0}".format(arg_dictionary['priority'])
        prompt = "intfPrompt"
        prompt_args = "GigabitEthernet {0}".format(arg_dictionary['port'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_l1_dr_priority_on_mlt(self, arg_dictionary, **kwargs):
        uuid = "33aca53f-ca4b-473e-a0a4-e3524c9e6652"
        cmd = "isis l1-dr-priority {0}".format(arg_dictionary['priority'])
        prompt = "intfPrompt"
        prompt_args = "mlt {0}".format(arg_dictionary['mlt_id'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_l1_hello_interval_on_port(self, arg_dictionary, **kwargs):
        uuid = "b9cd3f50-d847-4f00-b3bf-226aeaa3e1a7"
        cmd = "isis l1-hello-interval {0}".format(arg_dictionary['interval'])
        prompt = "intfPrompt"
        prompt_args = "GigabitEthernet {0}".format(arg_dictionary['port'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_l1_hello_interval_on_mlt(self, arg_dictionary, **kwargs):
        uuid = "915d4fb3-893c-48ca-ad79-cdb3b4f55fb8"
        cmd = "isis l1-hello-interval {0}".format(arg_dictionary['interval'])
        prompt = "intfPrompt"
        prompt_args = "mlt {0}".format(arg_dictionary['mlt_id'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_l1_hello_multiplier_on_port(self, arg_dictionary, **kwargs):
        uuid = "7cf5fb00-5403-484c-9c55-a8b210f08794"
        cmd = "isis l1-hello-multiplier {0}".format(arg_dictionary['multiplier'])
        prompt = "intfPrompt"
        prompt_args = "GigabitEthernet {0}".format(arg_dictionary['port'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_l1_hello_multiplier_on_mlt(self, arg_dictionary, **kwargs):
        uuid = "04e62c21-8b5e-49ef-8bd9-d17504b9d267"
        cmd = "isis l1-hello-multiplier {0}".format(arg_dictionary['multiplier'])
        prompt = "intfPrompt"
        prompt_args = "mlt {0}".format(arg_dictionary['mlt_id'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_logical_interface_port(self, arg_dictionary, **kwargs):
        uuid = "ebb09810-b864-434e-a1b2-71182d98a5e7"
        cmd = "logical-intf isis {0} vid {1},{2} primary-vid {3} port {4}".format(arg_dictionary['isis_id'],
                                                                                  arg_dictionary['primary_vlan'],
                                                                                  arg_dictionary['secondary_vlan'],
                                                                                  arg_dictionary['primary_vlan'],
                                                                                  arg_dictionary['port'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_logical_interface_port_name(self, arg_dictionary, **kwargs):
        uuid = "ecbfd0cf-38c3-40f8-bd28-2f8ba6b5d046"
        cmd = "logical-intf isis {0} vid {1},{2} primary-vid {3} port {4} name {5}".format(arg_dictionary['isis_id'],
                                                                                           arg_dictionary['primary_vlan'],
                                                                                           arg_dictionary['secondary_vlan'],
                                                                                           arg_dictionary['primary_vlan'],
                                                                                           arg_dictionary['port'],
                                                                                           arg_dictionary['name'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_logical_interface_mlt(self, arg_dictionary, **kwargs):
        uuid = "b6950cc9-9864-4cbf-b6eb-41b42073a2b7"
        cmd = "logical-intf isis {0} vid {1},{2} primary-vid {3} mlt {4}".format(arg_dictionary['isis_id'],
                                                                                 arg_dictionary['primary_vlan'],
                                                                                 arg_dictionary['secondary_vlan'],
                                                                                 arg_dictionary['primary_vlan'],
                                                                                 arg_dictionary['mlt_id'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_logical_interface_mlt_name(self, arg_dictionary, **kwargs):
        uuid = "65b86f45-faaf-42b0-b402-4270611fec81"
        cmd = "logical-intf isis {0} vid {1},{2} primary-vid {3} mlt {4} name {5}".format(arg_dictionary['isis_id'],
                                                                                          arg_dictionary['primary_vlan'],
                                                                                          arg_dictionary['secondary_vlan'],
                                                                                          arg_dictionary['primary_vlan'],
                                                                                          arg_dictionary['mlt_id'],
                                                                                          arg_dictionary['name'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_logical_interface_ipv4(self, arg_dictionary, **kwargs):
        uuid = "b516f64c-ea7a-4bc9-b06b-b7e48ea7d233"
        cmd = "logical-intf isis {0} dest-ip {1}".format(arg_dictionary['isis_id'],
                                                         arg_dictionary['ip'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_logical_interface_ipv4_name(self, arg_dictionary, **kwargs):
        uuid = "4787609a-74d8-473a-91a9-c23ed2f93f16"
        cmd = "logical-intf isis {0} dest-ip {1} name {2}".format(arg_dictionary['isis_id'],
                                                                  arg_dictionary['ip'],
                                                                  arg_dictionary['name'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_logical_interface(self, arg_dictionary, **kwargs):
        uuid = "147e596b-0eae-4a4b-8aba-8c30f685ede9"
        cmd = "no logical-intf isis {0}".format(arg_dictionary['isis_id'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_circuit_on_logical_interface(self, arg_dictionary, **kwargs):
        uuid = "d59abe65-4e7d-4fdf-9dc7-60aeba11b38f"
        cmd = "logical-intf isis {0}||isis||exit".format(arg_dictionary['isis_id'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_circuit_on_logical_interface(self, arg_dictionary, **kwargs):
        uuid = "fdf2b144-ed15-4231-8bb6-e936d4051830"
        cmd = "logical-intf isis {0}||isis enable||exit".format(arg_dictionary['isis_id'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_circuit_on_logical_interface(self, arg_dictionary, **kwargs):
        uuid = "2f340493-ed7f-4743-bd1b-014006864256"
        cmd = "logical-intf isis {0}||no isis enable||exit".format(arg_dictionary['isis_id'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_circuit_on_logical_interface(self, arg_dictionary, **kwargs):
        uuid = "5f0e7037-a1c3-46ca-8bfc-fd0ec2841299"
        cmd = "logical-intf isis {0}||no isis||exit".format(arg_dictionary['isis_id'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_auth_on_logical_interface(self, arg_dictionary, **kwargs):
        uuid = "6dbef1fc-ea72-4854-9594-52ccc0109429"
        cmd = "logical-intf isis {0}||isis hello-auth type {1} key {2} key-id {3}||exit".format(arg_dictionary['isis_id'],
                                                                                                arg_dictionary['auth_type'],
                                                                                                arg_dictionary['auth_key'],
                                                                                                arg_dictionary['key_id'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_auth_on_logical_interface(self, arg_dictionary, **kwargs):
        uuid = "69035712-e13e-4b00-af19-c0e77699aee9"
        cmd = "logical-intf isis {0}||no isis hello-auth||exit".format(arg_dictionary['isis_id'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_l1_dr_priority_on_logical_interface(self, arg_dictionary, **kwargs):
        uuid = "4938f0c5-c7ba-47f4-8891-31d58293f376"
        cmd = "logical-intf isis {0}||isis l1-dr-priority {1}||exit".format(arg_dictionary['isis_id'],
                                                                            arg_dictionary['priority'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_l1_hello_interval_on_logical_interface(self, arg_dictionary, **kwargs):
        uuid = "b9be7b04-0cbb-4d58-a6e5-36d3dd3ac3e1"
        cmd = "logical-intf isis {0}||isis l1-hello-interval {1}||exit".format(arg_dictionary['isis_id'],
                                                                               arg_dictionary['interval'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_l1_hello_multiplier_on_logical_interface(self, arg_dictionary, **kwargs):
        uuid = "28ca259c-6215-4fbc-9311-f3863b53e501"
        cmd = "logical-intf isis {0}||isis l1-hello-multiplier {1}||exit".format(arg_dictionary['isis_id'],
                                                                                 arg_dictionary['multiplier'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_circuit(self, arg_dictionary, **kwargs):
        uuid = "fa0140f5-6c5c-496f-af68-3630be0f284e"
        cmd = "show isis"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_circuit_interfaces(self, arg_dictionary, **kwargs):
        uuid = "ec8e2aef-a43d-46f8-b78c-819f227e30f0"
        cmd = "show isis int-ckt-level"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_info(self, arg_dictionary, **kwargs):
        uuid = "1826c2f3-c01c-4da5-8c56-c21538da2331"
        cmd = "show isis"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_interface(self, arg_dictionary, **kwargs):
        uuid = "c777e704-4043-4a2c-9b9d-4afb8d796f73"
        cmd = "show isis interface"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_interface_l1(self, arg_dictionary, **kwargs):
        uuid = "3270ac3e-7cd1-4ecc-948a-0342954e2d7f"
        cmd = "show isis interface l1"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_interface_l2(self, arg_dictionary, **kwargs):
        uuid = "cdd357c7-9811-4a73-8e48-4626efc720de"
        cmd = "show isis interface l2"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_interface_l12(self, arg_dictionary, **kwargs):
        uuid = "70c576f5-4160-4f6e-868e-d481e14504ce"
        cmd = "show isis interface l12"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_area(self, arg_dictionary, **kwargs):
        uuid = "9f7194d9-1204-43b3-80f8-34c7e1d7960a"
        cmd = "show isis area"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_lsdb(self, arg_dictionary, **kwargs):
        uuid = "f0ef2ee5-4617-4d8d-b767-2fbaf1a576b1"
        cmd = "show isis lsdb"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_manual_area(self, arg_dictionary, **kwargs):
        uuid = "587dbeea-5f2c-448f-b305-31d4429f7afd"
        cmd = "show isis manual-area"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_net(self, arg_dictionary, **kwargs):
        uuid = "15e262ad-c217-41cb-ac39-469e95afb303"
        cmd = "show isis net"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_spb_mcast_summary(self, arg_dictionary, **kwargs):
        uuid = "fa374b1a-c8b9-4a51-ad46-01a5332dfe28"
        cmd = "show isis spb-mcast-summary"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_statistics(self, arg_dictionary, **kwargs):
        uuid = "ad804fc6-b117-45c2-afd6-2bf8eed49c9a"
        cmd = "show isis statistics"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_sys_id(self, arg_dictionary, **kwargs):
        uuid = "a7366f3d-a071-4250-9bad-75e339c290a8"
        cmd = "show isis system-id"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_adjacencies(self, arg_dictionary, **kwargs):
        uuid = "6a1f17f2-f7bf-47c1-b0a8-91f887bc7448"
        cmd = "show isis adjacencies"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_interface_auth(self, arg_dictionary, **kwargs):
        uuid = "cd9d0273-3446-46b2-ae13-24fef1351b00"
        cmd = "show isis int-auth"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_interface_timers(self, arg_dictionary, **kwargs):
        uuid = "571b9c9e-0ef6-479f-bd01-92f201db29ab"
        cmd = "show isis int-timers"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_lsdb_ip_unicast(self, arg_dictionary, **kwargs):
        uuid = "1015aaee-1c15-4f93-8227-cb2a46b70620"
        cmd = "show isis lsdb ip-unicast"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_system_stats(self, arg_dictionary, **kwargs):
        uuid = "f50ea600-252c-4654-aa21-403f27015b68"
        cmd = "show isis statistics"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_logical_interface(self, arg_dictionary, **kwargs):
        uuid = "d5433420-d9b3-4d4b-884f-3029de321fa5"
        cmd = "show isis logical-interface"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_logical_interface_name(self, arg_dictionary, **kwargs):
        uuid = "66e013fd-54e2-4b0c-b13f-62e93c7b50ff"
        cmd = "show isis logical-interface name"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_interface_stats(self, arg_dictionary, **kwargs):
        uuid = "6aa9eeb8-a02d-45ab-8da8-1c0f63568b02"
        cmd = "show isis int-counters"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_interface_l1_packet_stats(self, arg_dictionary, **kwargs):
        uuid = "f9500aff-4ba2-4d02-899a-c40aa15b9250"
        cmd = "show isis int-l1-cntl-pkts"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_interface_l2_packet_stats(self, arg_dictionary, **kwargs):
        uuid = "42dd923e-ebff-4ca2-9325-9ffd25aff56c"
        cmd = "show isis int-l2-cntl-pkts"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_ip_redistribute(self, arg_dictionary, **kwargs):
        uuid = "403df57b-93f9-4239-bf4f-5acacada817e"
        cmd = "show ip isis redistribute"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_ipv6_redistribute(self, arg_dictionary, **kwargs):
        uuid = "ec788ef5-15d9-4ddb-ab3e-ea02bc9c0b71"
        cmd = "show ipv6 isis redistribute"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
