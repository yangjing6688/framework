"""
All rsmlt supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.rsmlt.base.rsmltbase import RsmltBase


class Rsmlt(DeviceApi, RsmltBase):
    def __init__(self, device_input):
        super(Rsmlt, self).__init__(device_input)

    def enable_edge_support(self, arg_dictionary, **kwargs):
        uuid = "1cd191b8-4663-4daf-a172-43367ef3f08a"
        cmd = "ip rsmlt edge-support"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_edge_support(self, arg_dictionary, **kwargs):
        uuid = "55d26d95-87cf-4f12-a0ad-ba272e1ba705"
        cmd = "no ip rsmlt edge-support"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_vlan_interface(self, arg_dictionary, **kwargs):
        uuid = "9a19e49e-ff41-4d35-bb56-b9af088a99e2"
        cmd = "ip rsmlt"
        prompt = "intfPrompt"
        prompt_args = "vlan {0}".format(arg_dictionary['interface'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def disable_vlan_interface(self, arg_dictionary, **kwargs):
        uuid = "ccff1e1c-83e4-4033-a8e2-02920585166c"
        cmd = "no ip rsmlt"
        prompt = "intfPrompt"
        prompt_args = "vlan {0}".format(arg_dictionary['interface'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_interface_holddown_timer(self, arg_dictionary, **kwargs):
        uuid = "0096a4a2-a456-4713-8e24-8b0c353a3126"
        cmd = "ip rsmlt holddown-timer {0}".format(arg_dictionary['timer'])
        prompt = "intfPrompt"
        prompt_args = "vlan {0}".format(arg_dictionary['interface'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_interface_holdup_timer(self, arg_dictionary, **kwargs):
        uuid = "1c71b9f6-7d6e-411a-bbed-3fbd81e8de87"
        cmd = "ip rsmlt holdup-timer {0}".format(arg_dictionary['timer'])
        prompt = "intfPrompt"
        prompt_args = "vlan {0}".format(arg_dictionary['interface'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def show_info(self, arg_dictionary, **kwargs):
        uuid = "2aeb7133-d9d9-4070-8ea5-fd4605f98726"
        cmd = "show ip rsmlt"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_edge_support(self, arg_dictionary, **kwargs):
        uuid = "076ea85d-774c-45f5-a63b-aad5dcfc44c6"
        cmd = "show ip rsmlt edge-support"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_vrf(self, arg_dictionary, **kwargs):
        uuid = "5a775e8e-20a2-4a07-a5c4-156f29e1ae73"
        cmd = "show ip rsmlt vrf {0}".format(arg_dictionary['vrf_name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_vrfid(self, arg_dictionary, **kwargs):
        uuid = "072e67f6-98ef-449c-b01a-dd3b178db6be"
        cmd = "show ip rsmlt vrf {0}".format(arg_dictionary['vrfid'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_local(self, arg_dictionary, **kwargs):
        uuid = "85b5667a-1dce-4d62-856f-378f1709a30f"
        cmd = "show ip rsmlt local"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_local_vrf(self, arg_dictionary, **kwargs):
        uuid = "b278e204-9ba8-4dac-a04a-ef509f21038b"
        cmd = "show ip rsmlt local vrf {0}".format(arg_dictionary['vrf_name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_local_vrfid(self, arg_dictionary, **kwargs):
        uuid = "6849ddec-4e93-4ff3-9b80-fc7eaa1cba3b"
        cmd = "show ip rsmlt local vrf {0}".format(arg_dictionary['vrfid'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_peer(self, arg_dictionary, **kwargs):
        uuid = "dff6e248-9921-4c5f-b0c6-5e76535dac46"
        cmd = "show ip rsmlt peer"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_peer_vrf(self, arg_dictionary, **kwargs):
        uuid = "ce5720d7-6383-4aa6-bafe-231c3d764097"
        cmd = "show ip rsmlt peer vrf {0}".format(arg_dictionary['vrf_name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_peer_vrfid(self, arg_dictionary, **kwargs):
        uuid = "e2ff2584-90fa-4814-b1b5-8559155efd61"
        cmd = "show ip rsmlt peer vrf {0}".format(arg_dictionary['vrfid'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
