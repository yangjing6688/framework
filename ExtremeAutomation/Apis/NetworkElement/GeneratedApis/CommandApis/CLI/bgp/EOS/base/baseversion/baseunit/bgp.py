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
        cmd = "enable"
        prompt = "routerProtoPrompt"
        prompt_args = "bgp||{0}".format(arg_dictionary['asnum'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def disable_global(self, arg_dictionary, **kwargs):
        uuid = "fe9d5af9-a437-4627-9fd1-df444da0f44e"
        cmd = "no enable"
        prompt = "routerProtoPrompt"
        prompt_args = "bgp||{0}".format(arg_dictionary['asnum'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def create_as(self, arg_dictionary, **kwargs):
        uuid = "5cb85d69-e9d2-4cf9-a87f-ad9173289ac6"
        cmd = ""
        prompt = "routerProtoPrompt"
        prompt_args = "bgp||{0}".format(arg_dictionary['asnum'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def delete_as(self, arg_dictionary, **kwargs):
        uuid = "2844c681-6679-4646-a94e-570082c8b85e"
        cmd = "no router bgp {0}".format(arg_dictionary['asnum'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_router_id(self, arg_dictionary, **kwargs):
        uuid = "0cd0af1c-15cd-4a39-bc11-154744a4f502"
        cmd = "bgp router-id {0}".format(arg_dictionary['rtrid'])
        prompt = "routerProtoPrompt"
        prompt_args = "bgp||{0}".format(arg_dictionary['asnum'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def clear_router_id(self, arg_dictionary, **kwargs):
        uuid = "45788698-c46e-40e7-804f-221a7536bf93"
        cmd = "no bgp router-id"
        prompt = "routerProtoPrompt"
        prompt_args = "bgp||{0}".format(arg_dictionary['asnum'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def create_neighbor(self, arg_dictionary, **kwargs):
        uuid = "157a36a7-b911-4e1b-a16b-04bb52abf727"
        cmd = "neighbor {0} remote-as {1}".format(arg_dictionary['ip'],
                                                  arg_dictionary['remoteas'])
        prompt = "routerProtoPrompt"
        prompt_args = "bgp||{0}".format(arg_dictionary['asnum'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def create_neighbor_link_local(self, arg_dictionary, **kwargs):
        uuid = "7123f5e3-13e7-435d-b9dd-eb43664b7af2"
        cmd = "neighbor {0}%{1} remote-as {2}".format(arg_dictionary['ip'],
                                                      arg_dictionary['vlan_eos'],
                                                      arg_dictionary['remoteas'])
        prompt = "routerProtoPrompt"
        prompt_args = "bgp||{0}".format(arg_dictionary['asnum'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def delete_neighbor(self, arg_dictionary, **kwargs):
        uuid = "be1c7911-d5ae-4de3-940f-639373cad108"
        cmd = "no neighbor {0} remote-as {1}".format(arg_dictionary['ip'],
                                                     arg_dictionary['remoteas'])
        prompt = "routerProtoPrompt"
        prompt_args = "bgp||{0}".format(arg_dictionary['asnum'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def delete_neighbor_link_local(self, arg_dictionary, **kwargs):
        uuid = "b4e67dba-f36a-4a65-b973-3eb7e1f02739"
        cmd = "no neighbor {0}%{1} remote-as {2}".format(arg_dictionary['ip'],
                                                         arg_dictionary['vlan_eos'],
                                                         arg_dictionary['remoteas'])
        prompt = "routerProtoPrompt"
        prompt_args = "bgp||{0}".format(arg_dictionary['asnum'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def enable_neighbor(self, arg_dictionary, **kwargs):
        uuid = "5af49855-d323-4e88-aafa-25023a8541b8"
        cmd = "neighbor {0} enable".format(arg_dictionary['ip'])
        prompt = "routerProtoPrompt"
        prompt_args = "bgp||{0}".format(arg_dictionary['asnum'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def enable_neighbor_link_local(self, arg_dictionary, **kwargs):
        uuid = "37fc30fe-c52f-49f3-8b4a-aea3c076c403"
        cmd = "neighbor {0}%{1} enable".format(arg_dictionary['ip'],
                                               arg_dictionary['vlan_eos'])
        prompt = "routerProtoPrompt"
        prompt_args = "bgp||{0}".format(arg_dictionary['asnum'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def disable_neighbor(self, arg_dictionary, **kwargs):
        uuid = "402dd380-b0c2-48c8-87af-77d1b99d617c"
        cmd = "no neighbor {0} enable".format(arg_dictionary['ip'])
        prompt = "routerProtoPrompt"
        prompt_args = "bgp||{0}".format(arg_dictionary['asnum'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def disable_neighbor_link_local(self, arg_dictionary, **kwargs):
        uuid = "1fcb4eba-f5fd-4d60-aeb0-32781e3e5b3e"
        cmd = "no neighbor {0}%{1} enable".format(arg_dictionary['ip'],
                                                  arg_dictionary['vlan_eos'])
        prompt = "routerProtoPrompt"
        prompt_args = "bgp||{0}".format(arg_dictionary['asnum'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_redistribute(self, arg_dictionary, **kwargs):
        uuid = "fd5a6676-3d4c-491e-a842-3234fd0d3154"
        cmd = "redistribute {0}".format(arg_dictionary['protocol'])
        prompt = "routerProtoPrompt"
        prompt_args = "bgp||{0}".format(arg_dictionary['asnum'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def clear_redistribute(self, arg_dictionary, **kwargs):
        uuid = "314c6f26-9895-43e9-be5e-17615b1f3175"
        cmd = "no redistribute {0}".format(arg_dictionary['protocol'])
        prompt = "routerProtoPrompt"
        prompt_args = "bgp||{0}".format(arg_dictionary['asnum'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_neighbor_password(self, arg_dictionary, **kwargs):
        uuid = "e48b6513-3b98-4cef-b33a-b5d6ca8d9987"
        cmd = "neighbor {0} remote-as {1} password {2}".format(arg_dictionary['ip'],
                                                               arg_dictionary['asnum'],
                                                               arg_dictionary['password'])
        prompt = "routerProtoPrompt"
        prompt_args = "bgp||{0}".format(arg_dictionary['asnum'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def show_all_routes(self, arg_dictionary, **kwargs):
        uuid = "8b16d3d7-c625-41bc-8383-cac30cee3fa3"
        cmd = "show ip bgp"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_neighbors(self, arg_dictionary, **kwargs):
        uuid = "1909e224-5174-4515-9adf-6576c2c4e2a6"
        cmd = "show ip bgp neighbors"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_status(self, arg_dictionary, **kwargs):
        uuid = "41a0b4f3-4260-40e2-8f9d-7b9cbad07fd4"
        cmd = "show ip bgp"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
