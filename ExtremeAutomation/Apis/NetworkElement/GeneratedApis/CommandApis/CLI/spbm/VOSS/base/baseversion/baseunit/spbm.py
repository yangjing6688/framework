"""
All spbm supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.spbm.base.spbmbase import SpbmBase


class Spbm(DeviceApi, SpbmBase):
    def __init__(self, device_input):
        super(Spbm, self).__init__(device_input)

    def set_ethertype(self, arg_dictionary, **kwargs):
        uuid = "c136f8ab-cc0c-4550-b157-14943892b971"
        cmd = "spbm ethertype {0}".format(arg_dictionary['ethertype'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_ethertype(self, arg_dictionary, **kwargs):
        uuid = "a3ccaba0-b9f5-4a61-9069-77da2ffd4ce7"
        cmd = "spbm ethertype 0x8100"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_global(self, arg_dictionary, **kwargs):
        uuid = "78fe268a-16fd-4bb1-8364-18e2d22d09c0"
        cmd = "spbm"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_global(self, arg_dictionary, **kwargs):
        uuid = "39d9011e-4241-496a-959d-34ffb37fd6af"
        cmd = "no spbm"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_ip_shortcut(self, arg_dictionary, **kwargs):
        uuid = "5a85377b-4858-4507-a4d8-60aa9bf085f8"
        cmd = "router isis||spbm {0} ip enable||exit".format(arg_dictionary['spbm_id'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_ip_shortcut(self, arg_dictionary, **kwargs):
        uuid = "a11b78c4-42a0-4a47-a525-952db7cb3108"
        cmd = "router isis||no spbm {0} ip enable||exit".format(arg_dictionary['spbm_id'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_ipv6_shortcut(self, arg_dictionary, **kwargs):
        uuid = "c6574c76-301b-41f9-8c33-a098e8756360"
        cmd = "router isis||spbm {0} ipv6 enable||exit".format(arg_dictionary['spbm_id'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_ipv6_shortcut(self, arg_dictionary, **kwargs):
        uuid = "90574270-cc2f-4bdd-b312-cbea48df779f"
        cmd = "router isis||no spbm {0} ipv6 enable||exit".format(arg_dictionary['spbm_id'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_lsdb_trap(self, arg_dictionary, **kwargs):
        uuid = "8ca085e9-24b2-4751-a584-e6a399327607"
        cmd = "router isis||spbm {0} lsdb-trap enable||exit".format(arg_dictionary['spbm_id'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_lsdb_trap(self, arg_dictionary, **kwargs):
        uuid = "01e46e45-6aaa-40e1-9fb1-d450ab581c9d"
        cmd = "router isis||no spbm {0} lsdb-trap enable||exit".format(arg_dictionary['spbm_id'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_isis_instance_id(self, arg_dictionary, **kwargs):
        uuid = "ce70f188-0c68-4c9e-a499-cc09aad52c3f"
        cmd = "router isis||spbm {0}||exit".format(arg_dictionary['spbm_id'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_isis_instance_id(self, arg_dictionary, **kwargs):
        uuid = "81819efc-1e95-4272-a8ad-a69cc382a529"
        cmd = "router isis||no spbm {0}||exit".format(arg_dictionary['spbm_id'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_isis_nickname(self, arg_dictionary, **kwargs):
        uuid = "5825a7d7-957a-4ef1-9dfe-4f68e69e5f57"
        cmd = "router isis||spbm {0} nick-name {1}||exit".format(arg_dictionary['spbm_id'],
                                                                 arg_dictionary['nickname'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_isis_nickname(self, arg_dictionary, **kwargs):
        uuid = "8389ed74-dbb8-4d6d-8e10-6ffdd4e0ad4d"
        cmd = "router isis||no spbm {0} nick-name||exit".format(arg_dictionary['spbm_id'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_isis_bvid(self, arg_dictionary, **kwargs):
        uuid = "9033b7a0-92fb-4a58-b047-2c5c3bccec6c"
        cmd = "router isis||spbm {0} b-vid {1},{2} primary {3}||exit".format(arg_dictionary['spbm_id'],
                                                                             arg_dictionary['pri_vlan'],
                                                                             arg_dictionary['sec_vlan'],
                                                                             arg_dictionary['pri_vlan'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_isis_bvid(self, arg_dictionary, **kwargs):
        uuid = "64c86061-df56-4766-bf61-a9a130e2394f"
        cmd = "router isis||no spbm {0} b-vid {1},{2}||exit".format(arg_dictionary['spbm_id'],
                                                                    arg_dictionary['pri_vlan'],
                                                                    arg_dictionary['sec_vlan'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_isis_multicast(self, arg_dictionary, **kwargs):
        uuid = "43378da1-621e-4a13-9373-b74a0cb3ee28"
        cmd = "router isis||spbm {0} multicast enable||exit".format(arg_dictionary['spbm_id'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_isis_multicast(self, arg_dictionary, **kwargs):
        uuid = "f8f6903f-34c3-4496-bcda-9c940f3ebf6a"
        cmd = "router isis||no spbm {0} multicast enable||exit".format(arg_dictionary['spbm_id'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_isis_multicast_fwd_cache_timeout(self, arg_dictionary, **kwargs):
        uuid = "03473550-1e69-4362-a42e-3310392d4c36"
        cmd = "router isis||spbm {0} multicast fwd-cache-timeout {1}||exit".format(arg_dictionary['spbm_id'],
                                                                                   arg_dictionary['timeout'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_isis_multicast_fwd_cache_timeout(self, arg_dictionary, **kwargs):
        uuid = "de7738f1-f145-421e-97f6-3889870c4e08"
        cmd = "router isis||no spbm {0} multicast fwd-cache-timeout||exit".format(arg_dictionary['spbm_id'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_isis_smlt_virtual_bmac(self, arg_dictionary, **kwargs):
        uuid = "0875014c-78b5-40ec-a015-4a6419985d1b"
        cmd = "router isis||spbm {0} smlt-virtual-bmac {1}||exit".format(arg_dictionary['spbm_id'],
                                                                         arg_dictionary['bmac'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_isis_smlt_virtual_bmac(self, arg_dictionary, **kwargs):
        uuid = "8e860b4d-187f-4b1a-8624-10cf14f75845"
        cmd = "router isis||no spbm {0} smlt-virtual-bmac||exit".format(arg_dictionary['spbm_id'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_isis_smlt_peer_system_id(self, arg_dictionary, **kwargs):
        uuid = "c2730f12-5a57-4b2c-a89c-918a93ff7b96"
        cmd = "router isis||spbm {0} smlt-peer-system-id {1}||exit".format(arg_dictionary['spbm_id'],
                                                                           arg_dictionary['peer_id'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_isis_smlt_peer_system_id(self, arg_dictionary, **kwargs):
        uuid = "0eb30dfe-5354-42dc-b17c-e8fa8edeff30"
        cmd = "router isis||no spbm {0} smlt-peer-system-id||exit".format(arg_dictionary['spbm_id'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_port_isis_instance_id(self, arg_dictionary, **kwargs):
        uuid = "a0337bcb-f440-43ff-862a-4472a9992f3b"
        cmd = "isis spbm {0}".format(arg_dictionary['spbm_id'])
        prompt = "intfPrompt"
        prompt_args = "GigabitEthernet {0}".format(arg_dictionary['port'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def clear_port_isis_instance_id(self, arg_dictionary, **kwargs):
        uuid = "a0478d48-a84c-4783-b92a-f8292ccd0d15"
        cmd = "no isis spbm {0}".format(arg_dictionary['spbm_id'])
        prompt = "intfPrompt"
        prompt_args = "GigabitEthernet {0}".format(arg_dictionary['port'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_mlt_isis_instance_id(self, arg_dictionary, **kwargs):
        uuid = "ce782566-ba3a-4dfb-b2e5-1c7664d58888"
        cmd = "isis spbm {0}".format(arg_dictionary['spbm_id'])
        prompt = "intfPrompt"
        prompt_args = "mlt {0}".format(arg_dictionary['mlt_id'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def clear_mlt_isis_instance_id(self, arg_dictionary, **kwargs):
        uuid = "5eda73f9-ee72-41a8-8570-d35c7040a610"
        cmd = "no isis spbm {0}".format(arg_dictionary['spbm_id'])
        prompt = "intfPrompt"
        prompt_args = " mlt {0}".format(arg_dictionary['mlt_id'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_port_isis_interface_type_broadcast(self, arg_dictionary, **kwargs):
        uuid = "c7d6f404-b060-4a5e-ba12-57c44106aad3"
        cmd = "isis spbm {0} interface-type broadcast".format(arg_dictionary['spbm_id'])
        prompt = "intfPrompt"
        prompt_args = "GigabitEthernet {0}".format(arg_dictionary['port'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_port_isis_interface_type_p2p(self, arg_dictionary, **kwargs):
        uuid = "2e8a85c0-0b45-434b-bd73-8cf9f34661cc"
        cmd = "isis spbm {0} interface-type pt-pt".format(arg_dictionary['spbm_id'])
        prompt = "intfPrompt"
        prompt_args = "GigabitEthernet {0}".format(arg_dictionary['port'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def clear_port_isis_interface_type(self, arg_dictionary, **kwargs):
        uuid = "44c01d4f-a214-42b8-9e90-c9ec26bdf4a4"
        cmd = "isis spbm {0} interface-type pt-pt".format(arg_dictionary['spbm_id'])
        prompt = "intfPrompt"
        prompt_args = "GigabitEthernet {0}".format(arg_dictionary['port'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_mlt_isis_interface_type_broadcast(self, arg_dictionary, **kwargs):
        uuid = "78613ac3-c70b-4ef7-a63f-9f0d232ff9f0"
        cmd = "isis spbm {0} interface-type broadcast".format(arg_dictionary['spbm_id'])
        prompt = "intfPrompt"
        prompt_args = "mlt {0}".format(arg_dictionary['mlt_id'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_mlt_isis_interface_type_p2p(self, arg_dictionary, **kwargs):
        uuid = "491b2ef5-3da5-47fd-ba16-03c7b7a46e74"
        cmd = "isis spbm {0} interface-type pt-pt".format(arg_dictionary['spbm_id'])
        prompt = "intfPrompt"
        prompt_args = "mlt {0}".format(arg_dictionary['mlt_id'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def clear_mlt_isis_interface_type(self, arg_dictionary, **kwargs):
        uuid = "8db6ac4d-ccde-4888-8a0c-f87fb988d674"
        cmd = "isis spbm {0} interface-type pt-pt".format(arg_dictionary['spbm_id'])
        prompt = "intfPrompt"
        prompt_args = "mlt {0}".format(arg_dictionary['mlt_id'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_port_isis_l1_metric(self, arg_dictionary, **kwargs):
        uuid = "192c93b3-a9c6-437a-ad7c-a394db290ecf"
        cmd = "isis spbm {0} l1-metric {1}".format(arg_dictionary['spbm_id'],
                                                   arg_dictionary['metric'])
        prompt = "intfPrompt"
        prompt_args = "GigabitEthernet {0}".format(arg_dictionary['port'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def clear_port_isis_l1_metric(self, arg_dictionary, **kwargs):
        uuid = "118919a5-184c-48f3-b968-01263df60f94"
        cmd = "isis spbm {0} l1-metric 10".format(arg_dictionary['spbm_id'])
        prompt = "intfPrompt"
        prompt_args = "GigabitEthernet {0}".format(arg_dictionary['port'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_mlt_isis_l1_metric(self, arg_dictionary, **kwargs):
        uuid = "4fe99065-df6e-47e4-b341-e3149e3a90d5"
        cmd = "isis spbm {0} l1-metric {1}".format(arg_dictionary['spbm_id'],
                                                   arg_dictionary['metric'])
        prompt = "intfPrompt"
        prompt_args = "mlt {0}".format(arg_dictionary['mlt_id'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def clear_mlt_isis_l1_metric(self, arg_dictionary, **kwargs):
        uuid = "db58c4ab-d6d5-488c-a445-f3bdd4ac9994"
        cmd = "isis spbm {0} l1-metric 10".format(arg_dictionary['spbm_id'])
        prompt = "intfPrompt"
        prompt_args = "mlt {0}".format(arg_dictionary['mlt_id'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_logical_interface_isis_instance_id(self, arg_dictionary, **kwargs):
        uuid = "102d76c8-b7ef-46d2-8676-02e680dd5b3e"
        cmd = "logical-intf isis {0}||isis spbm {1}||exit".format(arg_dictionary['isis_id'],
                                                                  arg_dictionary['spbm_id'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_logical_interface_isis_instance_id(self, arg_dictionary, **kwargs):
        uuid = "fc371754-1f33-49e2-ba2a-1b8e99285a86"
        cmd = "logical-intf isis {0}||no isis spbm {1}||exit".format(arg_dictionary['isis_id'],
                                                                     arg_dictionary['spbm_id'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_logical_interface_isis_interface_type_broadcast(self, arg_dictionary, **kwargs):
        uuid = "7499a7ff-6e7a-4fd2-8016-c316b08543e6"
        cmd = "logical-intf isis {0}||isis spbm {1} interface-type broadcast||exit".format(arg_dictionary['isis_id'],
                                                                                           arg_dictionary['spbm_id'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_logical_interface_isis_interface_type_p2p(self, arg_dictionary, **kwargs):
        uuid = "2e674775-61f4-4e42-a16e-2abd9233bbc9"
        cmd = "logical-intf isis {0}||isis spbm {1} interface-type pt-pt||exit".format(arg_dictionary['isis_id'],
                                                                                       arg_dictionary['spbm_id'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_logical_interface_isis_interface_type(self, arg_dictionary, **kwargs):
        uuid = "e69ab934-b0f6-4d59-b73a-8f0618030cdb"
        cmd = "logical-intf isis {0}||isis spbm {1} interface-type pt-pt||exit".format(arg_dictionary['isis_id'],
                                                                                       arg_dictionary['spbm_id'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_logical_interface_isis_l1_metric(self, arg_dictionary, **kwargs):
        uuid = "cf049f1e-8540-4415-9bc9-655b87514d9a"
        cmd = "logical-intf isis {0}||isis spbm {1} l1-metric {2}||exit".format(arg_dictionary['isis_id'],
                                                                                arg_dictionary['spbm_id'],
                                                                                arg_dictionary['metric'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_logical_interface_isis_l1_metric(self, arg_dictionary, **kwargs):
        uuid = "efb270e6-bc64-48c7-a852-70bb9ad3941e"
        cmd = "logical-intf isis {0}||isis spbm {1} l1-metric 1000||exit".format(arg_dictionary['isis_id'],
                                                                                 arg_dictionary['spbm_id'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_virtual_ist_peer_ip(self, arg_dictionary, **kwargs):
        uuid = "be8d1e54-361c-42a8-a27a-4785671cdd5d"
        cmd = "virtual-ist peer-ip {0} vlan {1}".format(arg_dictionary['ip'],
                                                        arg_dictionary['vlan'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_virtual_ist_peer_ip(self, arg_dictionary, **kwargs):
        uuid = "d2d8ead0-8751-4d2b-9eba-b46ef94de674"
        cmd = "no virtual-ist peer-ip"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_virtual_ist(self, arg_dictionary, **kwargs):
        uuid = "85f347a1-7907-402c-800c-31d34824ff74"
        cmd = "show virtual-ist"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_virtual_ist_stat(self, arg_dictionary, **kwargs):
        uuid = "ddd852a4-e745-49c6-97fb-89dc8c3580e2"
        cmd = "show virtual-ist stat"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_info(self, arg_dictionary, **kwargs):
        uuid = "20304340-d70a-41d6-9b92-b3605cca7ce1"
        cmd = "show spbm"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_isis_info(self, arg_dictionary, **kwargs):
        uuid = "f38a8fa5-adea-49fc-9e5a-d9d6888ba7a8"
        cmd = "show isis spbm"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_isis_interface(self, arg_dictionary, **kwargs):
        uuid = "cda4da94-7df5-480e-b115-0e20fec130d0"
        cmd = "show isis interface"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_isis_isid_all(self, arg_dictionary, **kwargs):
        uuid = "6aaff610-ed87-4cb8-86db-48f2415a152b"
        cmd = "show isis spbm i-sid all"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_isis_isid_all_id(self, arg_dictionary, **kwargs):
        uuid = "84ba13a6-f186-4072-9051-68d54d3868f4"
        cmd = "show isis spbm i-sid all id {0}".format(arg_dictionary['isid'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_isis_isid_all_nickname(self, arg_dictionary, **kwargs):
        uuid = "ca4cd2d9-8234-4d14-8561-52040825bbb9"
        cmd = "show isis spbm i-sid all nick-name {0}".format(arg_dictionary['nickname'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_isis_isid_all_vlan(self, arg_dictionary, **kwargs):
        uuid = "4a199aa8-de33-436a-bfe3-934e12312a5e"
        cmd = "show isis spbm i-sid all vlan {0}".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_isis_isid_config(self, arg_dictionary, **kwargs):
        uuid = "546c48b6-3aa9-4d21-b202-d7e68e45d879"
        cmd = "show isis spbm i-sid config"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_isis_isid_config_id(self, arg_dictionary, **kwargs):
        uuid = "a813f307-4ee7-47f0-8224-0e88062d5a75"
        cmd = "show isis spbm i-sid config id {0}".format(arg_dictionary['isid'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_isis_isid_config_nickname(self, arg_dictionary, **kwargs):
        uuid = "aa02b940-4107-41c1-83fb-a6408b6f7b0b"
        cmd = "show isis spbm i-sid config nick_name {0}".format(arg_dictionary['nickname'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_isis_isid_config_vlan(self, arg_dictionary, **kwargs):
        uuid = "f98ff251-fb5e-4bf5-8855-0b8612e4b49a"
        cmd = "show isis spbm i-sid config vlan {0}".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_isis_isid_discover(self, arg_dictionary, **kwargs):
        uuid = "7ba509bd-1c56-4426-a02e-08a62e309e58"
        cmd = "show isis spbm i-sid discover"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_isis_isid_discover_id(self, arg_dictionary, **kwargs):
        uuid = "3d46862a-521f-4823-9ff2-2dd5f6013538"
        cmd = "show isis spbm i-sid discover id {0}".format(arg_dictionary['isid'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_isis_isid_discover_nickname(self, arg_dictionary, **kwargs):
        uuid = "f03943bc-66c5-4d1e-b8a8-dfb039e4afee"
        cmd = "show isis spbm i-sid discover nick_name {0}".format(arg_dictionary['nickname'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_isis_isid_discover_vlan(self, arg_dictionary, **kwargs):
        uuid = "9fb77ae6-311e-46ef-840f-f9a1f44a332c"
        cmd = "show isis spbm i-sid discover vlan {0}".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_isis_ip_multicast_route(self, arg_dictionary, **kwargs):
        uuid = "b1e56535-cb34-4439-8906-6a8c787c669d"
        cmd = "show isis spbm ip-multicast-route"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_isis_ip_multicast_route_all(self, arg_dictionary, **kwargs):
        uuid = "25a8be76-e467-4adc-b670-85e569849602"
        cmd = "show isis spbm ip-multicast-route all"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_isis_ip_multicast_route_detail(self, arg_dictionary, **kwargs):
        uuid = "d47d1372-a1bd-41c7-8469-2d7b39b2c40e"
        cmd = "show isis spbm ip-multicast-route detail"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_isis_ip_multicast_route_group(self, arg_dictionary, **kwargs):
        uuid = "e255b177-0af9-423c-97ce-7cf7bbbb7657"
        cmd = "show isis spbm ip-multicast-route group {0}".format(arg_dictionary['ip'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_isis_ip_multicast_route_group_detail(self, arg_dictionary, **kwargs):
        uuid = "09df1e63-0560-4fd1-b2eb-6580a1027d62"
        cmd = "show isis spbm ip-multicast-route group {0} detail".format(arg_dictionary['ip'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_isis_ip_multicast_route_group_source(self, arg_dictionary, **kwargs):
        uuid = "97285fd3-343c-4298-919d-3c9a38cfa5bd"
        cmd = "show isis spbm ip-multicast-route group {0} source {1}".format(arg_dictionary['ip'],
                                                                              arg_dictionary['sip'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_isis_ip_multicast_route_group_source_detail(self, arg_dictionary, **kwargs):
        uuid = "2f1f1cee-b388-4787-a1b9-859ab2a97d62"
        cmd = "show isis spbm ip-multicast-route group {0} source {1} detail".format(arg_dictionary['ip'],
                                                                                     arg_dictionary['sip'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_isis_ip_multicast_route_group_source_beb(self, arg_dictionary, **kwargs):
        uuid = "28c0a5e2-8a50-4b15-ab3a-7285412eed48"
        cmd = "show isis spbm ip-multicast-route group {0} source {1} source-beb {2}".format(arg_dictionary['ip'],
                                                                                             arg_dictionary['sip'],
                                                                                             arg_dictionary['name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_isis_ip_multicast_route_vlan(self, arg_dictionary, **kwargs):
        uuid = "ed61f828-c8e0-4ab9-b3b6-96353a285041"
        cmd = "show isis spbm ip-multicast-route vlan {0}".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_isis_ip_multicast_route_vlan_detail(self, arg_dictionary, **kwargs):
        uuid = "9a1cfa34-00d0-43cf-8dfd-001b48f391e9"
        cmd = "show isis spbm ip-multicast-route vlan {0} detail".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_isis_ip_multicast_route_vlan_group(self, arg_dictionary, **kwargs):
        uuid = "6e571d88-0455-4f55-9f2e-8ba41ecbbdca"
        cmd = "show isis spbm ip-multicast-route vlan {0} group {1}".format(arg_dictionary['vlan'],
                                                                            arg_dictionary['ip'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_isis_ip_multicast_route_vlan_group_detail(self, arg_dictionary, **kwargs):
        uuid = "75e5d20c-3889-47ce-b796-e6299cebd287"
        cmd = "show isis spbm ip-multicast-route vlan {0} group {1} detail".format(arg_dictionary['vlan'],
                                                                                   arg_dictionary['ip'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_isis_ip_multicast_route_vlan_group_source(self, arg_dictionary, **kwargs):
        uuid = "d7401950-0ee9-4729-aa87-2a5eccd91a60"
        cmd = "show isis spbm ip-multicast-route vlan {0} group {1} source {2}".format(arg_dictionary['vlan'],
                                                                                       arg_dictionary['ip'],
                                                                                       arg_dictionary['sip'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_isis_ip_multicast_route_vlan_group_source_detail(self, arg_dictionary, **kwargs):
        uuid = "6a9efcb3-93f6-4f6a-911b-4c4d0a1bdb10"
        cmd = "show isis spbm ip-multicast-route vlan {0} group {1} source {2} detail".format(arg_dictionary['vlan'],
                                                                                              arg_dictionary['ip'],
                                                                                              arg_dictionary['sip'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_isis_ip_multicast_route_vlan_group_source_beb(self, arg_dictionary, **kwargs):
        uuid = "36bb3f43-08d5-4962-8f59-2b3d40e8b348"
        cmd = "show isis spbm ip-multicast-route vlan {0} group {1} source {2} source-beb {3}".format(arg_dictionary['vlan'],
                                                                                                      arg_dictionary['ip'],
                                                                                                      arg_dictionary['sip'],
                                                                                                      arg_dictionary['name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_isis_ip_multicast_route_vrf(self, arg_dictionary, **kwargs):
        uuid = "500c4a72-076b-47d9-b016-e68d5649aef6"
        cmd = "show isis spbm ip-multicast-route vrf {0}".format(arg_dictionary['vrf_name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_isis_ip_multicast_route_vrf_detail(self, arg_dictionary, **kwargs):
        uuid = "c79a9a5c-bb12-4d1a-8250-8594604fcb7a"
        cmd = "show isis spbm ip-multicast-route vrf {0} detail".format(arg_dictionary['vrf'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_isis_ip_multicast_route_vrf_group(self, arg_dictionary, **kwargs):
        uuid = "2ea4ba67-33e5-4ffa-bfd3-ccf0e2d37353"
        cmd = "show isis spbm ip-multicast-route vrf {0} group {1}".format(arg_dictionary['vrf'],
                                                                           arg_dictionary['ip'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_isis_ip_multicast_route_vsn_isid(self, arg_dictionary, **kwargs):
        uuid = "45dee8c1-2d37-4080-bd8c-222f660260ac"
        cmd = "show isis spbm ip-multicast-route vsn-isid {0}".format(arg_dictionary['isid'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_isis_ip_multicast_route_vsn_isid_etail(self, arg_dictionary, **kwargs):
        uuid = "fc40c6f8-b252-495a-98bb-204740ea3965"
        cmd = "show isis spbm ip-multicast-route vsn-isid {0} detail".format(arg_dictionary['isid'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_isis_ip_multicast_route_vsn_isid_group(self, arg_dictionary, **kwargs):
        uuid = "021e1b78-cda4-4711-af84-f9e83a17c3c7"
        cmd = "show isis spbm ip-multicast-route vsn-isid {0} group {1}".format(arg_dictionary['isid'],
                                                                                arg_dictionary['ip'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_isis_ip_unicast_fib(self, arg_dictionary, **kwargs):
        uuid = "74b7ecbf-7afc-4886-9020-21d6dd2717bf"
        cmd = "show isis spbm ip-unicast-fib"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_isis_ipv6_unicast_fib(self, arg_dictionary, **kwargs):
        uuid = "86c0e7c0-4cb7-4b8f-9bca-8f38b18a79dc"
        cmd = "show isis spbm ipv6-unicast-fib"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_isis_ipv6_unicast_fib_id(self, arg_dictionary, **kwargs):
        uuid = "974e07ad-f503-4eaa-afe9-d465c40bb535"
        cmd = "show isis spbm ipv6-unicast-fib id {0}".format(arg_dictionary['isid'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_isis_ip_unicast_fib_id(self, arg_dictionary, **kwargs):
        uuid = "2aacd9a0-b2ef-47f1-b2b3-0be284497eee"
        cmd = "show isis spbm ip-unicast-fib id {0}".format(arg_dictionary['isid'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_isis_ip_unicast_fib_spbm_nh_as_mac(self, arg_dictionary, **kwargs):
        uuid = "6abe888e-0778-4441-92ad-8b73a3f565e4"
        cmd = "show isis spbm ip-unicast-fib spbm-nh-as-mac"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_isis_multicast(self, arg_dictionary, **kwargs):
        uuid = "700ffaea-223f-4e77-947e-15cb876d70e5"
        cmd = "show isis spbm multicast"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_isis_multicast_fib(self, arg_dictionary, **kwargs):
        uuid = "f380acb6-ea96-4678-962b-534b49184b25"
        cmd = "show isis spbm multicast-fib"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_isis_multicast_fib_detail(self, arg_dictionary, **kwargs):
        uuid = "94a0acb9-7f92-4a90-bb02-2bec71405305"
        cmd = "show isis spbm multicast-fib detail"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_isis_multicast_fib_isid(self, arg_dictionary, **kwargs):
        uuid = "8f7e88a9-8577-4d18-b334-befd18aec1ef"
        cmd = "show isis spbm multicast-fib i-sid {0}".format(arg_dictionary['isid'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_isis_multicast_fib_nickname(self, arg_dictionary, **kwargs):
        uuid = "01897b97-ee9f-44f6-b8a1-bc97966343eb"
        cmd = "show isis spbm multicast-fib nick-name {0}".format(arg_dictionary['nickname'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_isis_multicast_fib_summary(self, arg_dictionary, **kwargs):
        uuid = "58279390-2ac9-43c0-b937-369e4924ff90"
        cmd = "show isis spbm multicast-fib summary"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_isis_multicast_fib_vlan(self, arg_dictionary, **kwargs):
        uuid = "dc0b4750-adc6-42a6-a353-4acbc4e52f66"
        cmd = "show isis spbm multicast-fib vlan {0}".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_isis_nickname(self, arg_dictionary, **kwargs):
        uuid = "c5bae896-780c-4af7-bccb-d92d4eca20c2"
        cmd = "show isis spbm nick-name {0}".format(arg_dictionary['nickname'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_isis_nickname_smlt_virtual_bmac(self, arg_dictionary, **kwargs):
        uuid = "484ce639-0c92-438a-8b32-e54d2688911e"
        cmd = "show isis spbm nick-name smlt-virtual-bmac {0}".format(arg_dictionary['bmac'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_isis_nickname_sysid(self, arg_dictionary, **kwargs):
        uuid = "efcaaa77-8512-4d3b-9ed2-2fc46f736d38"
        cmd = "show isis spbm nick-name sysid {0}".format(arg_dictionary['sysid'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_isis_unicast_fib(self, arg_dictionary, **kwargs):
        uuid = "d81f45ec-39a7-47fb-a6a5-f75eeadf0e8b"
        cmd = "show isis spbm unicast-fib"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_isis_unicast_fib_bmac(self, arg_dictionary, **kwargs):
        uuid = "6905d0f9-1a1c-4d1c-bdac-c36e78b53744"
        cmd = "show isis spbm unicast-fib b-mac {0}".format(arg_dictionary['bmac'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_isis_unicast_fib_summary(self, arg_dictionary, **kwargs):
        uuid = "aebace63-c304-4635-9050-e2200854284e"
        cmd = "show isis spbm unicast-fib summary"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_isis_unicast_fib_vlan(self, arg_dictionary, **kwargs):
        uuid = "9afe47bf-98e0-409e-80a5-66e25e7d50f4"
        cmd = "show isis spbm unicast-fib vlan {0}".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_isis_unicast_tree(self, arg_dictionary, **kwargs):
        uuid = "f199dac4-9c45-4f7b-8ccd-798b2d0b576f"
        cmd = "show isis spbm unicast-tree {0}".format(arg_dictionary['bvlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_isis_unicast_tree_destination(self, arg_dictionary, **kwargs):
        uuid = "1b724108-2b98-4356-a79b-bf1af8befb8a"
        cmd = "show isis spbm unicast-tree {0} destination {1}".format(arg_dictionary['bvlan'],
                                                                       arg_dictionary['sysid'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_isid(self, arg_dictionary, **kwargs):
        uuid = "8227f5c7-3bc4-48d9-b7cc-fa40f3cf4b79"
        cmd = "show i-sid {0}".format(arg_dictionary['isid'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_isid_all(self, arg_dictionary, **kwargs):
        uuid = "7881482f-6e66-44b6-85e3-da76313cb7f2"
        cmd = "show i-sid"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_isid_elan(self, arg_dictionary, **kwargs):
        uuid = "a7f6dbcb-c532-4317-965d-7bf6b78383f7"
        cmd = "show i-sid elan"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_isid_elan_transparent(self, arg_dictionary, **kwargs):
        uuid = "9e150c48-0151-4e77-b17c-988475c44bf4"
        cmd = "show i-sid elan-transparent"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_isid_mac_address_entry(self, arg_dictionary, **kwargs):
        uuid = "be027d23-b56f-48a3-8f69-455f18b892d9"
        cmd = "show i-sid mac-address-entry {0}".format(arg_dictionary['isid'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_isid_mac_address_entry_all(self, arg_dictionary, **kwargs):
        uuid = "6f2ea73f-b0cd-48b5-bad9-bc4cf20d9244"
        cmd = "show i-sid mac-address-entry"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_isid_mac_address_entry_mac(self, arg_dictionary, **kwargs):
        uuid = "81993a78-2287-40a1-81ec-675a3338cff3"
        cmd = "show i-sid mac-address-entry mac {0}".format(arg_dictionary['mac'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_isid_mac_address_entry_port(self, arg_dictionary, **kwargs):
        uuid = "ef151f57-2e54-4593-a9b3-96706e8d3a42"
        cmd = "show i-sid mac-address-entry port {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_isid_mac_address_entry_remote(self, arg_dictionary, **kwargs):
        uuid = "dc0bfd0a-155a-4a07-b3d0-fc59676c4210"
        cmd = "show i-sid mac-address-entry remote"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
