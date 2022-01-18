"""
All vrf supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.vrf.base.vrfbase import VrfBase


class Vrf(DeviceApi, VrfBase):
    def __init__(self, device_input):
        super(Vrf, self).__init__(device_input)

    def create_router(self, arg_dictionary, **kwargs):
        uuid = "79ad39b1-ea31-44e0-af58-0c820758655a"
        cmd = "ip vrf {0}".format(arg_dictionary['vrf_name'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def create_router_with_vrfid(self, arg_dictionary, **kwargs):
        uuid = "0aba9a09-f599-42b7-89e2-45dbeec380dd"
        cmd = "ip vrf {0} vrfid {1}".format(arg_dictionary['vrf_name'],
                                            arg_dictionary['vrfid'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def delete_router(self, arg_dictionary, **kwargs):
        uuid = "8fca33fe-1a50-499a-8d9d-fa01eed835e3"
        cmd = "no ip vrf {0}".format(arg_dictionary['vrf_name'])
        prompt = "routerConfigPrompt"
        conf = "(y/n) ?"
        conf_args = "y"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf, conf_args=conf_args)

    def enable_trap(self, arg_dictionary, **kwargs):
        uuid = "57402ee0-6ae0-49d6-ac07-2a907c1f910e"
        cmd = "ip vrf {0} vrf-trap enable".format(arg_dictionary['vrf_name'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_trap(self, arg_dictionary, **kwargs):
        uuid = "1dce067a-6fe7-4069-a18c-8a30d7a9e09f"
        cmd = "no ip vrf {0} vrf-trap enable".format(arg_dictionary['vrf_name'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_max_routes_trap(self, arg_dictionary, **kwargs):
        uuid = "8cfe1a37-1b6f-4df1-a762-3a171b9efa38"
        cmd = "ip vrf {0} max-routes-trap enable".format(arg_dictionary['vrf_name'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_max_routes_trap(self, arg_dictionary, **kwargs):
        uuid = "213b5ab6-963d-49f0-8a32-f9da60698841"
        cmd = "no ip vrf {0} max-routes-trap enable".format(arg_dictionary['vrf_name'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_mvpn(self, arg_dictionary, **kwargs):
        uuid = "e6839ffc-2101-4399-b175-2f976cc4e41c"
        cmd = "router vrf {0} || mvpn enable".format(arg_dictionary['vrf_name'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_mvpn(self, arg_dictionary, **kwargs):
        uuid = "b6a526c3-3b87-4aae-8ebe-08ec636cfb64"
        cmd = "router vrf {0} || no mvpn enable".format(arg_dictionary['vrf_name'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_ipv6_max_routes_trap(self, arg_dictionary, **kwargs):
        uuid = "87b358f0-068b-434f-8a02-910813c8b9c8"
        cmd = "ip vrf {0} ipv6-max-routes-trap enable".format(arg_dictionary['vrf_name'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_ipv6_max_routes_trap(self, arg_dictionary, **kwargs):
        uuid = "6f2d3dee-e0cc-4910-a42c-64c5b17bd684"
        cmd = "no ip vrf {0} ipv6-max-routes-trap enable".format(arg_dictionary['vrf_name'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_ipvpn(self, arg_dictionary, **kwargs):
        uuid = "5c9afa7d-9ea0-4e98-8d38-0952e97c0ec7"
        cmd = "router vrf {0}||ipvpn enable".format(arg_dictionary['vrf_name'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_ipvpn(self, arg_dictionary, **kwargs):
        uuid = "bf2da38d-06f7-4ca1-aebe-d25a1f472ff6"
        cmd = "router vrf {0}||no ipvpn enable".format(arg_dictionary['vrf_name'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_isis_redistribute_direct(self, arg_dictionary, **kwargs):
        uuid = "ebb15783-390a-4eda-a807-68a1faddbbda"
        cmd = "router vrf {0}||isis redistribute direct enable||exit".format(arg_dictionary['vrf_name'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_isis_redistribute_direct(self, arg_dictionary, **kwargs):
        uuid = "9eccfbc2-293c-426a-9814-28749746c015"
        cmd = "router vrf {0}||no isis redistribute direct enable||exit".format(arg_dictionary['vrf_name'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_mvpn_fwd_cache_timeout(self, arg_dictionary, **kwargs):
        uuid = "562e7f2d-955e-4f3c-8804-0166234e9c6e"
        cmd = "router vrf {0}||mvpn fwd-cache-timeout {1}||exit".format(arg_dictionary['vrf_name'],
                                                                        arg_dictionary['timeout'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_max_routes(self, arg_dictionary, **kwargs):
        uuid = "9ccdaf91-17f5-4c9d-b925-0060d97a92af"
        cmd = "ip vrf {0} max-routes {1}".format(arg_dictionary['vrf_name'],
                                                 arg_dictionary['num_max_routes'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_ipv6_max_routes(self, arg_dictionary, **kwargs):
        uuid = "3456a4a9-c719-4988-8814-2bce7ac6f7f5"
        cmd = "ip vrf {0} ipv6-max-routes {1}".format(arg_dictionary['vrf_name'],
                                                      arg_dictionary['num_max_routes'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_name(self, arg_dictionary, **kwargs):
        uuid = "6d3ef614-8bf1-4cd0-8dc2-31c07b418f32"
        cmd = "ip vrf {0} {1}".format(arg_dictionary['vrf_name'],
                                      arg_dictionary['new_vrf_name'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_vrfid(self, arg_dictionary, **kwargs):
        uuid = "cc22e8fa-bc27-4a43-8e9a-d781f04af55b"
        cmd = "ip vrf {0} vrfid {1}".format(arg_dictionary['vrf_name'],
                                            arg_dictionary['vrfid'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_interface_vlan(self, arg_dictionary, **kwargs):
        uuid = "47b48d3e-d7f5-4ac3-aaf1-aeb4d367b985"
        cmd = "vrf {0}".format(arg_dictionary['vrf_name'])
        prompt = "intfPrompt"
        prompt_args = "vlan {0}".format(arg_dictionary['interface'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def clear_interface_vlan(self, arg_dictionary, **kwargs):
        uuid = "814fff13-2c4d-461a-b91e-d6f5aaf1a6b0"
        cmd = "no vrf {0}".format(arg_dictionary['vrf_name'])
        prompt = "intfPrompt"
        prompt_args = "vlan {0}".format(arg_dictionary['interface'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_ipvpn(self, arg_dictionary, **kwargs):
        uuid = "7c72f65d-3b9d-4110-abc0-fb5c12b1e92e"
        cmd = "router vrf {0}||ipvpn".format(arg_dictionary['vrf_name'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_isid(self, arg_dictionary, **kwargs):
        uuid = "eab779d3-226a-4742-9d4f-0997b14350db"
        cmd = "router vrf {0}||i-sid {1}".format(arg_dictionary['vrf_name'],
                                                 arg_dictionary['i_sid'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_isis_redistribute_direct(self, arg_dictionary, **kwargs):
        uuid = "3f53d840-e837-4305-a1e1-fae3a510e5d9"
        cmd = "router vrf {0}||isis redistribute direct||exit".format(arg_dictionary['vrf_name'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_isis_redistribute_direct(self, arg_dictionary, **kwargs):
        uuid = "97f1fb35-755e-444b-8056-65a8c4a6512e"
        cmd = "router vrf {0}||no isis redistribute direct||exit".format(arg_dictionary['vrf_name'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_isis_redistribute_direct_apply(self, arg_dictionary, **kwargs):
        uuid = "64858983-7fc7-496e-a08f-fa9f39c061a3"
        cmd = "isis apply redistribute direct vrf {0}".format(arg_dictionary['vrf_name'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_all(self, arg_dictionary, **kwargs):
        uuid = "122d7f45-c278-4264-b3a2-c2e0eb7c0f5a"
        cmd = "show ip vrf"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_max_routes(self, arg_dictionary, **kwargs):
        uuid = "32ff249b-19de-4d42-9834-920c6d1ad191"
        cmd = "show ip vrf max-routes {0}".format(arg_dictionary['vrfid'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_max_routes_all(self, arg_dictionary, **kwargs):
        uuid = "5926680c-1188-4cc0-91c0-548027d80000"
        cmd = "show ip vrf max-routes"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_max_routes_name(self, arg_dictionary, **kwargs):
        uuid = "9b319b7f-8e92-425b-a437-e9d957cd1ce6"
        cmd = "show ip vrf max-routes {0}".format(arg_dictionary['vrf_name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_ipv6_max_routes(self, arg_dictionary, **kwargs):
        uuid = "d91beefa-3111-46c5-be3d-825b7070cd3b"
        cmd = "show ip vrf ipv6-max-routes {0}".format(arg_dictionary['vrfid'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_ipv6_max_routes_all(self, arg_dictionary, **kwargs):
        uuid = "67513f17-d50b-4bd9-8b7a-b94d38dfc1c6"
        cmd = "show ip vrf ipv6-max-routes"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_ipv6_max_routes_name(self, arg_dictionary, **kwargs):
        uuid = "91068bf4-fcd0-4b54-9fbc-ca3846574916"
        cmd = "show ip vrf ipv6-max-routes {0}".format(arg_dictionary['vrf_name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_mvpn(self, arg_dictionary, **kwargs):
        uuid = "b2d4d2be-c6e7-401d-a7df-7a7db05d178a"
        cmd = "show ip vrf mvpn"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_vrfids(self, arg_dictionary, **kwargs):
        uuid = "035dd6c5-fac6-46d3-b8ea-473996d6da49"
        cmd = "show ip vrf vrfids {0}".format(arg_dictionary['vrfid'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_name(self, arg_dictionary, **kwargs):
        uuid = "e94f578c-29c8-4f0f-abc1-462116671166"
        cmd = "show ip vrf {0}".format(arg_dictionary['vrf_name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_ip_route(self, arg_dictionary, **kwargs):
        uuid = "c900cc3e-a3cf-470e-9488-5a9d23683ef3"
        cmd = "show ip route vrf {0}".format(arg_dictionary['vrf_name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_ip_routing(self, arg_dictionary, **kwargs):
        uuid = "6c0e905c-ed7e-480f-a8a4-aaf3b1f1cc2f"
        cmd = "show ip routing vrf {0}".format(arg_dictionary['vrf_name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_vrfid_ip_routing(self, arg_dictionary, **kwargs):
        uuid = "71c51a81-0912-40a4-b0af-590d4a9d1ad5"
        cmd = "show ip routing vrfids {0}".format(arg_dictionary['vrfid'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_isid_list(self, arg_dictionary, **kwargs):
        uuid = "68709988-4b5f-42ac-89ac-6548d7c7ea2d"
        cmd = "show ip isid-list vrf {0}".format(arg_dictionary['vrfid'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_interface_vlan(self, arg_dictionary, **kwargs):
        uuid = "e7633a10-ae1e-4fc7-994b-ec5a49a2c4da"
        cmd = "show interfaces vlan vrf {0}".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_ipvpn(self, arg_dictionary, **kwargs):
        uuid = "fed38f0c-a323-47f9-afc0-04fe78d4b491"
        cmd = "show ip ipvpn vrf {0}".format(arg_dictionary['vrf_name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_isis_redistribute_direct(self, arg_dictionary, **kwargs):
        uuid = "d84ccd0b-4a21-4b2a-8fc7-0385735e0e68"
        cmd = "show ip isis redistribute vrf {0}".format(arg_dictionary['vrf_name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
