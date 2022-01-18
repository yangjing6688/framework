"""
All igmp supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.igmp.base.igmpbase import IgmpBase


class Igmp(DeviceApi, IgmpBase):
    def __init__(self, device_input):
        super(Igmp, self).__init__(device_input)

    def set_version(self, arg_dictionary, **kwargs):
        uuid = "0aadf5bd-92a0-4eb4-808e-41d4b8cac082"
        cmd = "vlan {0}||ip igmp snooping version {1}".format(arg_dictionary['vlan'],
                                                              arg_dictionary['igmp_ver'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_version_interface(self, arg_dictionary, **kwargs):
        uuid = "8aea0bc5-c952-4e2e-816c-e427b8517071"
        cmd = "ip igmp snooping version {0}".format(arg_dictionary['igmp_ver'])
        prompt = "intfPrompt"
        prompt_args = "interface ethernet {0}".format(arg_dictionary['port'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def enable_vlan(self, arg_dictionary, **kwargs):
        uuid = "641501ff-2725-4c7b-bd1b-d2712089faef"
        cmd = "vlan {0}||ip igmp snooping enable".format(arg_dictionary['vlan'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_vlan(self, arg_dictionary, **kwargs):
        uuid = "8cf98d6c-2531-4707-8e13-610bbbe5b015"
        cmd = "vlan {0}||no ip igmp snooping enable".format(arg_dictionary['vlan'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_snooping_vlan(self, arg_dictionary, **kwargs):
        uuid = "60d3ecc1-10ff-48e2-ae92-69fa5da82b0c"
        cmd = "vlan {0}||ip igmp snooping enable".format(arg_dictionary['vlan'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_snooping_vlan(self, arg_dictionary, **kwargs):
        uuid = "1631f48a-be31-4588-974f-c24c337c12f5"
        cmd = "vlan {0}||no ip igmp snooping enable".format(arg_dictionary['vlan'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_snooping_proxy(self, arg_dictionary, **kwargs):
        uuid = "0196a404-68d8-4b0f-83f1-433fc6432474"
        cmd = "vlan {0}||ip igmp snooping mrouter interface ethernet {1}".format(arg_dictionary['vlan'],
                                                                                 arg_dictionary['port'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_snooping_proxy(self, arg_dictionary, **kwargs):
        uuid = "76d57f2c-571e-45b2-b5c0-0a207ba0d9dc"
        cmd = "vlan {0}||no ip igmp snooping mrouter interface ethernet {1}".format(arg_dictionary['vlan'],
                                                                                    arg_dictionary['port'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_snooping_querier(self, arg_dictionary, **kwargs):
        uuid = "e1aa66d9-a6f6-4b0a-8a7e-0fac3b8ce11a"
        cmd = "vlan {0}||ip igmp snooping querier enable".format(arg_dictionary['vlan'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_snooping_querier(self, arg_dictionary, **kwargs):
        uuid = "3d678401-0b11-4825-b3c8-ed3f8a17ea08"
        cmd = "vlan {0}||no ip igmp snooping querier enable".format(arg_dictionary['vlan'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_snooping_fast_leave(self, arg_dictionary, **kwargs):
        uuid = "d2c72ecd-47e2-4f58-86cf-08f36f55b45b"
        cmd = "vlan {0}||ip igmp snooping fast-leave".format(arg_dictionary['vlan'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_snooping_fast_leave(self, arg_dictionary, **kwargs):
        uuid = "c6f3a98b-4179-4ea1-b7d7-468b79315034"
        cmd = "vlan {0}||no ip igmp snooping fast-leave".format(arg_dictionary['vlan'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_snooping_last_member_query_interval(self, arg_dictionary, **kwargs):
        uuid = "6949f5e5-5f42-4a72-acdf-c24982b417c1"
        cmd = "vlan {0}||ip igmp snooping last-member-query-interval {1}".format(arg_dictionary['vlan'],
                                                                                 arg_dictionary['interval'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_snooping_last_member_query_count(self, arg_dictionary, **kwargs):
        uuid = "1b1f42c4-3cd1-41c8-9be5-5e2adb9b6f29"
        cmd = "vlan {0}||ip igmp snooping last-member-query-count {1}".format(arg_dictionary['vlan'],
                                                                              arg_dictionary['value'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_snooping_query_interval(self, arg_dictionary, **kwargs):
        uuid = "4e09522e-fdf2-4a99-93a9-58ad6ff39773"
        cmd = "vlan {0}||ip igmp snooping query-interval {1}".format(arg_dictionary['vlan'],
                                                                     arg_dictionary['interval'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_snooping_query_max_response_time(self, arg_dictionary, **kwargs):
        uuid = "cd2a3cb1-3e0a-4fd3-adc2-6d23e9e5d52b"
        cmd = "vlan {0}||ip igmp snooping query-max-response-time {1}".format(arg_dictionary['vlan'],
                                                                              arg_dictionary['time'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_version(self, arg_dictionary, **kwargs):
        uuid = "b4ec33ba-8bd1-4b3c-91c8-9d60afeb97ba"
        cmd = "show ip igmp snooping vlan {0}".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_state(self, arg_dictionary, **kwargs):
        uuid = "7b779ef2-9d5c-4543-ac6d-dfb5b7740cd9"
        cmd = "show ip igmp snooping"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_vlan(self, arg_dictionary, **kwargs):
        uuid = "cba4b245-18c5-44fe-ab3c-28a8cdd281bf"
        cmd = "show ip igmp snooping vlan {0}".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_group(self, arg_dictionary, **kwargs):
        uuid = "7f377619-0c96-4bad-b335-662383a5e945"
        cmd = "show ip igmp groups"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_groups_vlan(self, arg_dictionary, **kwargs):
        uuid = "59372db3-f62c-4e4b-a66c-903de6c80db1"
        cmd = "show ip igmp groups vlan {0}".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port(self, arg_dictionary, **kwargs):
        uuid = "ab9fddf2-0215-4878-8f5f-583539cb3a72"
        cmd = "show ip igmp groups interface ethernet {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_snooping(self, arg_dictionary, **kwargs):
        uuid = "df44a792-0235-41f4-986e-fac40d8dfc66"
        cmd = "show ip igmp snooping"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_sender(self, arg_dictionary, **kwargs):
        uuid = "7ecd4539-b6c9-49c1-9a6f-ca8e1c02bee2"
        cmd = "show ip igmp snooping mrouter"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_statistics_vlan(self, arg_dictionary, **kwargs):
        uuid = "b6bef82c-589e-4c85-8f11-fd7aae803b0c"
        cmd = "show ip igmp statistics vlan {0}".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_statistics_port(self, arg_dictionary, **kwargs):
        uuid = "e9a9217a-3e61-4fce-8cd7-2a189a477d52"
        cmd = "show ip igmp statistics interface ethernet {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
