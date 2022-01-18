"""
All mld supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.mld.base.mldbase import MldBase


class Mld(DeviceApi, MldBase):
    def __init__(self, device_input):
        super(Mld, self).__init__(device_input)

    def enable_vlan(self, arg_dictionary, **kwargs):
        uuid = "fdf9ef13-b6e0-4e40-9778-b37009e57b73"
        cmd = "vlan {0}||ipv6 mld snooping enable".format(arg_dictionary['vlan'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_vlan(self, arg_dictionary, **kwargs):
        uuid = "ac01e9f9-216e-4148-b8d9-9c814f561fca"
        cmd = "vlan {0}||no ipv6 mld snooping enable".format(arg_dictionary['vlan'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_snooping(self, arg_dictionary, **kwargs):
        uuid = "2dbb6f6e-5680-4f48-b9e2-0c1f898c96a4"
        cmd = "vlan {0}||ipv6 mld snooping enable".format(arg_dictionary['vlan'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_snooping(self, arg_dictionary, **kwargs):
        uuid = "2b2e306b-3c94-498b-b9c2-13b8c0ae10b0"
        cmd = "vlan {0}||no ipv6 mld snooping enable".format(arg_dictionary['vlan'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_snooping_querier(self, arg_dictionary, **kwargs):
        uuid = "65b02f61-2516-4d37-9afa-13a16a609a97"
        cmd = "vlan {0}||ipv6 mld snooping querier enable".format(arg_dictionary['vlan'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_snooping_querier(self, arg_dictionary, **kwargs):
        uuid = "3a36fffa-9295-490b-80bf-e000d805714a"
        cmd = "vlan {0}||no ipv6 mld snooping querier enable".format(arg_dictionary['vlan'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_snooping_fast_leave(self, arg_dictionary, **kwargs):
        uuid = "f9b1733d-6159-4597-826d-dff13ad888da"
        cmd = "vlan {0}||ipv6 mld snooping fast-leave".format(arg_dictionary['vlan'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_snooping_fast_leave(self, arg_dictionary, **kwargs):
        uuid = "b732ffd3-870e-40fe-87cb-572820e35061"
        cmd = "vlan {0}||no ipv6 mld snooping fast-leave".format(arg_dictionary['vlan'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_snooping_last_member_query_count(self, arg_dictionary, **kwargs):
        uuid = "30168a49-720f-488b-add4-79faa0e1ec88"
        cmd = "vlan {0}||ipv6 mld snooping last-member-query-count {1}".format(arg_dictionary['vlan'],
                                                                               arg_dictionary['value'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_snooping_last_member_query_count(self, arg_dictionary, **kwargs):
        uuid = "01ea4117-bcb2-4926-a0f9-157ff3ed1142"
        cmd = "vlan {0}||no ipv6 mld snooping last-member-query-count".format(arg_dictionary['vlan'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_snooping_last_member_query_interval(self, arg_dictionary, **kwargs):
        uuid = "058cc38d-7123-4aa2-8967-17944d9f34f5"
        cmd = "vlan {0}||ipv6 mld snooping last-member-query-interval {1}".format(arg_dictionary['vlan'],
                                                                                  arg_dictionary['value'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_snooping_last_member_query_interval(self, arg_dictionary, **kwargs):
        uuid = "40827e1e-d06b-47f3-909e-e50b18aa9f1b"
        cmd = "vlan {0}||no ipv6 mld snooping last-member-query-interval".format(arg_dictionary['vlan'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_snooping_robustness_variable(self, arg_dictionary, **kwargs):
        uuid = "2144237d-6c46-4bbc-9948-e4bb1b274f7a"
        cmd = "vlan {0}||ipv6 mld snooping robustness-variable {1}".format(arg_dictionary['vlan'],
                                                                           arg_dictionary['value'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_snooping_robustness_variable(self, arg_dictionary, **kwargs):
        uuid = "e2caa83e-dcfc-4081-acfc-c2528eddc8aa"
        cmd = "vlan {0}||no ipv6 mld snooping robustness-variable".format(arg_dictionary['vlan'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_snooping_startup_query_count(self, arg_dictionary, **kwargs):
        uuid = "d9564fc5-60cc-44b0-8cfe-840bc9a4ec63"
        cmd = "vlan {0}||ipv6 mld snooping startup-query-count {1}".format(arg_dictionary['vlan'],
                                                                           arg_dictionary['value'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_snooping_startup_query_count(self, arg_dictionary, **kwargs):
        uuid = "379c3a65-3448-4bc5-be33-c6d03c954d2a"
        cmd = "vlan {0}||no ipv6 mld snooping startup-query-count".format(arg_dictionary['vlan'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_snooping_startup_query_interval(self, arg_dictionary, **kwargs):
        uuid = "92e59bff-c3f0-40a2-ac3b-2d7380251cbf"
        cmd = "vlan {0}||ipv6 mld snooping startup-query-interval {1}".format(arg_dictionary['vlan'],
                                                                              arg_dictionary['value'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_snooping_startup_query_interval(self, arg_dictionary, **kwargs):
        uuid = "c2051e4c-d158-4d14-9ba3-a0564a05a79c"
        cmd = "vlan {0}||no ipv6 mld snooping startup-query-interval".format(arg_dictionary['vlan'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_snooping_mrouter(self, arg_dictionary, **kwargs):
        uuid = "2ced3098-8888-4ef5-8cc9-783664497def"
        cmd = "vlan {0}||ipv6 mld snooping mrouter interface ethernet {1}".format(arg_dictionary['vlan'],
                                                                                  arg_dictionary['port'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_snooping_mrouter(self, arg_dictionary, **kwargs):
        uuid = "0bbca321-7d96-4f9e-a96a-2a0256e5ee8e"
        cmd = "vlan {0}||no ipv6 mld snooping mrouter interface ethernet".format(arg_dictionary['vlan'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_vlan(self, arg_dictionary, **kwargs):
        uuid = "5a011cd7-4ac2-4c80-83a3-77739dfe7063"
        cmd = "show ipv6 mld snooping vlan {0}".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_version(self, arg_dictionary, **kwargs):
        uuid = "f2376d5c-ee82-4fb3-83a4-00b9492c2c03"
        cmd = "show ipv6 mld snooping vlan {0}".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_statistics(self, arg_dictionary, **kwargs):
        uuid = "2f96ab47-c496-4ac7-b953-b2f65d27ed32"
        cmd = "show ipv6 mld statistics vlan {0}".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
