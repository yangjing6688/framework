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
        cmd = "interface vlan {0}||ip igmp version {1}".format(arg_dictionary['vlan'],
                                                               arg_dictionary['igmp_ver'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_snooping_vlan(self, arg_dictionary, **kwargs):
        uuid = "60d3ecc1-10ff-48e2-ae92-69fa5da82b0c"
        cmd = "interface vlan {0}||ip igmp snooping".format(arg_dictionary['vlan'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_snooping_vlan(self, arg_dictionary, **kwargs):
        uuid = "1631f48a-be31-4588-974f-c24c337c12f5"
        cmd = "interface vlan {0}||no ip igmp snooping".format(arg_dictionary['vlan'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_snooping_proxy(self, arg_dictionary, **kwargs):
        uuid = "0196a404-68d8-4b0f-83f1-433fc6432474"
        cmd = "interface vlan {0}||ip igmp proxy".format(arg_dictionary['vlan'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_snooping_proxy(self, arg_dictionary, **kwargs):
        uuid = "76d57f2c-571e-45b2-b5c0-0a207ba0d9dc"
        cmd = "interface vlan {0}||no ip igmp proxy".format(arg_dictionary['vlan'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_snooping_querier(self, arg_dictionary, **kwargs):
        uuid = "e1aa66d9-a6f6-4b0a-8a7e-0fac3b8ce11a"
        cmd = "interface vlan {0}||ip igmp snoop-querier".format(arg_dictionary['vlan'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_snooping_querier(self, arg_dictionary, **kwargs):
        uuid = "3d678401-0b11-4825-b3c8-ed3f8a17ea08"
        cmd = "interface vlan {0}||no ip igmp snoop-querier".format(arg_dictionary['vlan'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_snooping_querier_address(self, arg_dictionary, **kwargs):
        uuid = "da64ed04-80dd-4d0c-bf3a-7800e85e490f"
        cmd = "interface vlan {0}||ip igmp snoop-querier-addr {1}".format(arg_dictionary['vlan'],
                                                                          arg_dictionary['ip'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_snooping_querier_address(self, arg_dictionary, **kwargs):
        uuid = "eb8d99c4-0eff-4747-8e35-ef20436b8dc0"
        cmd = "interface vlan {0}||no ip igmp snoop-querier-addr".format(arg_dictionary['vlan'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_snooping_compatibility_mode_vlan(self, arg_dictionary, **kwargs):
        uuid = "9e528319-5811-48ba-8ef8-7c28815237da"
        cmd = "interface vlan {0}||ip igmp compatibility-mode".format(arg_dictionary['vlan'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_snooping_compatibility_mode_vlan(self, arg_dictionary, **kwargs):
        uuid = "cbe934fa-704e-4d48-a21a-3f0d8b15d30e"
        cmd = "interface vlan {0}||no ip igmp compatibility-mode".format(arg_dictionary['vlan'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_snooping_dynamic_downgrade_vlan(self, arg_dictionary, **kwargs):
        uuid = "eda8b88f-e4a8-469e-b265-106c467192f8"
        cmd = "interface vlan {0}||ip igmp dynamic-downgrade-version".format(arg_dictionary['vlan'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_snooping_dynamic_downgrade_vlan(self, arg_dictionary, **kwargs):
        uuid = "a1a8ff37-78c9-403d-8037-aab70629a7da"
        cmd = "interface vlan {0}||no ip igmp dynamic-downgrade-version".format(arg_dictionary['vlan'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_snooping_explicit_host_tracking_vlan(self, arg_dictionary, **kwargs):
        uuid = "54ce7d01-39b1-42e6-b7e0-b5d4b39e93b1"
        cmd = "interface vlan {0}||ip igmp igmpv3-explicit-host-tracking".format(arg_dictionary['vlan'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_snooping_explicit_host_tracking_vlan(self, arg_dictionary, **kwargs):
        uuid = "9b6b1d1e-ce7a-4d65-a79e-0bf5d2e7d566"
        cmd = "interface vlan {0}no ip igmp igmpv3-explicit-host-tracking".format(arg_dictionary['vlan'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_version(self, arg_dictionary, **kwargs):
        uuid = "b4ec33ba-8bd1-4b3c-91c8-9d60afeb97ba"
        cmd = "show ip igmp interface vlan {0}".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_state(self, arg_dictionary, **kwargs):
        uuid = "7b779ef2-9d5c-4543-ac6d-dfb5b7740cd9"
        cmd = "show ip igmp interface vlan"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_vlan(self, arg_dictionary, **kwargs):
        uuid = "cba4b245-18c5-44fe-ab3c-28a8cdd281bf"
        cmd = "show ip igmp interface vlan {0}".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_group(self, arg_dictionary, **kwargs):
        uuid = "7f377619-0c96-4bad-b335-662383a5e945"
        cmd = "show ip igmp group"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port(self, arg_dictionary, **kwargs):
        uuid = "ab9fddf2-0215-4878-8f5f-583539cb3a72"
        cmd = "show ip igmp interface gigabitethernet {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_snooping(self, arg_dictionary, **kwargs):
        uuid = "df44a792-0235-41f4-986e-fac40d8dfc66"
        cmd = "show ip igmp snooping"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_snooping_querier_address(self, arg_dictionary, **kwargs):
        uuid = "0f0d4e7a-7780-47d3-9759-e967b5747a02"
        cmd = "show ip igmp interface vlan {0}".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_sender(self, arg_dictionary, **kwargs):
        uuid = "7ecd4539-b6c9-49c1-9a6f-ca8e1c02bee2"
        cmd = "show ip igmp sender"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_snoop_trace(self, arg_dictionary, **kwargs):
        uuid = "964a8781-a06b-45dd-9a78-8658ec2aa204"
        cmd = "show ip igmp snoop-trace"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_router_alert(self, arg_dictionary, **kwargs):
        uuid = "9196a77e-31f8-4a09-836e-31265609e84f"
        cmd = "show ip igmp router-alert"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
