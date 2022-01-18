"""
All bgp supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.bgp.base.bgpbase import BgpBase


class Bgp(DeviceApi, BgpBase):
    def __init__(self, device_input):
        super(Bgp, self).__init__(device_input)

    def enable_global(self, arg_dictionary, **kwargs):
        uuid = "864baf6b-abcf-47ba-920d-856bb640e79c"
        cmd = "router bgp {0} enable".format(arg_dictionary['asnum'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_global(self, arg_dictionary, **kwargs):
        uuid = "fe9d5af9-a437-4627-9fd1-df444da0f44e"
        cmd = "no router bgp enable"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def create_as(self, arg_dictionary, **kwargs):
        uuid = "5cb85d69-e9d2-4cf9-a87f-ad9173289ac6"
        cmd = "router bgp {0}".format(arg_dictionary['asnum'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def delete_as(self, arg_dictionary, **kwargs):
        uuid = "2844c681-6679-4646-a94e-570082c8b85e"
        cmd = "router bgp 0"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_router_id(self, arg_dictionary, **kwargs):
        uuid = "0cd0af1c-15cd-4a39-bc11-154744a4f502"
        cmd = "router bgp||router-id {0}".format(arg_dictionary['rtrid'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_router_id(self, arg_dictionary, **kwargs):
        uuid = "45788698-c46e-40e7-804f-221a7536bf93"
        cmd = "router bgp||no router-id"
        prompt = "routerConfigPrompt"
        conf = "Are you sure you want to continue? (y/n) ?"
        conf_args = "{0}".format(arg_dictionary['answer'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf, conf_args=conf_args)

    def create_neighbor(self, arg_dictionary, **kwargs):
        uuid = "157a36a7-b911-4e1b-a16b-04bb52abf727"
        cmd = "router bgp||neighbor {0}||neighbor {1} remote-as {2}".format(arg_dictionary['ip'],
                                                                            arg_dictionary['ip'],
                                                                            arg_dictionary['remoteas'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def delete_neighbor(self, arg_dictionary, **kwargs):
        uuid = "be1c7911-d5ae-4de3-940f-639373cad108"
        cmd = "router bgp||no neighbor {0}".format(arg_dictionary['ip'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_neighbor(self, arg_dictionary, **kwargs):
        uuid = "5af49855-d323-4e88-aafa-25023a8541b8"
        cmd = "router bgp||neighbor {0} enable".format(arg_dictionary['ip'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_neighbor(self, arg_dictionary, **kwargs):
        uuid = "402dd380-b0c2-48c8-87af-77d1b99d617c"
        cmd = "router bgp||no neighbor {0} enable".format(arg_dictionary['ip'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_redistribute(self, arg_dictionary, **kwargs):
        uuid = "fd5a6676-3d4c-491e-a842-3234fd0d3154"
        cmd = "router bgp||redistribute {0}".format(arg_dictionary['protocol'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_redistribute(self, arg_dictionary, **kwargs):
        uuid = "314c6f26-9895-43e9-be5e-17615b1f3175"
        cmd = "router bgp||no redistribute {0}".format(arg_dictionary['protocol'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_neighbor_password(self, arg_dictionary, **kwargs):
        uuid = "e48b6513-3b98-4cef-b33a-b5d6ca8d9987"
        cmd = "router bgp||neighbor password {0} {1}".format(arg_dictionary['ip'],
                                                             arg_dictionary['password'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_neighbor_capability(self, arg_dictionary, **kwargs):
        uuid = "e813f686-694b-49ca-8f0e-9da4531f2500"
        cmd = "router bgp||neighbor {0} {1}".format(arg_dictionary['ip'],
                                                    arg_dictionary['capability'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_neighbor_capability(self, arg_dictionary, **kwargs):
        uuid = "69328593-da48-4fe0-8c82-2c2d9f5d5576"
        cmd = "router bgp||no neighbor {0} {1}".format(arg_dictionary['ip'],
                                                       arg_dictionary['capability'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_all_routes(self, arg_dictionary, **kwargs):
        uuid = "8b16d3d7-c625-41bc-8383-cac30cee3fa3"
        cmd = "show ip bgp route"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_neighbors(self, arg_dictionary, **kwargs):
        uuid = "1909e224-5174-4515-9adf-6576c2c4e2a6"
        cmd = "show ip bgp neighbor"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_status(self, arg_dictionary, **kwargs):
        uuid = "41a0b4f3-4260-40e2-8f9d-7b9cbad07fd4"
        cmd = "show ip bgp conf"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_route_ip(self, arg_dictionary, **kwargs):
        uuid = "5819fa87-9a46-4fa3-8e05-bab1c8706b8a"
        cmd = "show ip bgp route ip {0}".format(arg_dictionary['ip'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_redistributed_routes(self, arg_dictionary, **kwargs):
        uuid = "7625e7d8-4a49-4a50-8f8a-d4454cc10e9b"
        cmd = "show ip bgp redistributed-routes"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_networks(self, arg_dictionary, **kwargs):
        uuid = "ea4608a6-3755-48a5-b4a8-24d63a169206"
        cmd = "show ip bgp networks"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_peer_group(self, arg_dictionary, **kwargs):
        uuid = "1318cdee-ef72-43a3-9f59-565e2ee6c063"
        cmd = "show ip bgp peer-group"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_stats(self, arg_dictionary, **kwargs):
        uuid = "513d37b3-784d-4d0a-85be-0d2cedc0758a"
        cmd = "show ip bgp stats"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_summary(self, arg_dictionary, **kwargs):
        uuid = "9dc5582d-e992-44a9-be29-489e98d79d5e"
        cmd = "show ip bgp summary"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
