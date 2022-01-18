"""
All fdb supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.fdb.base.fdbbase import FdbBase


class Fdb(DeviceApi, FdbBase):
    def __init__(self, device_input):
        super(Fdb, self).__init__(device_input)

    def set_agetime(self, arg_dictionary, **kwargs):
        uuid = "736ac064-ce1f-4dee-afca-fb6a4319bac4"
        cmd = "configure fdb agingtime {0}".format(arg_dictionary['agetime'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_agetime_min(self, arg_dictionary, **kwargs):
        uuid = "b19aed04-3660-4ec2-a109-b0f1c570666e"
        cmd = "configure fdb agingtime {0}".format(arg_dictionary['agetime'])
        prompt = "userPrompt"
        conf = "WARNING: Agingtime values below 15"
        conf_args = "y"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf, conf_args=conf_args)

    def clear_agetime(self, arg_dictionary, **kwargs):
        uuid = "66f14371-91fd-4033-8f27-ff150c64064f"
        cmd = "configure fdb agingtime 300"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_all(self, arg_dictionary, **kwargs):
        uuid = "254dbcd8-83ed-4264-8cc8-2a3f9861e262"
        cmd = "clear fdb"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_all_vlan(self, arg_dictionary, **kwargs):
        uuid = "102b660f-4c7f-4da0-9428-df884f789080"
        cmd = "clear fdb vlan {0}".format(arg_dictionary['vlan_name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_all_port(self, arg_dictionary, **kwargs):
        uuid = "f8a712ed-edd6-402f-8f72-233e9db3b554"
        cmd = "clear fdb ports {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def create_entry(self, arg_dictionary, **kwargs):
        uuid = "ab3fbbd4-53b0-4e10-811e-a1e5a6177ffe"
        cmd = "create fdb {0} vlan {1} ports {2}".format(self.str_utils.normalize_mac(arg_dictionary['mac']),
                                                         arg_dictionary['vlan_name'],
                                                         arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def create_multicast_entry(self, arg_dictionary, **kwargs):
        uuid = "fe3435c2-b44b-45fa-9ceb-ffc249c6b962"
        cmd = "create fdb {0} vlan {1} ports {2}".format(self.str_utils.normalize_mac(arg_dictionary['mac']),
                                                         arg_dictionary['vlan_name'],
                                                         self.api_utils.exos_fdb_portlist(arg_dictionary['port']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def delete_entry(self, arg_dictionary, **kwargs):
        uuid = "a7ffbe28-bdad-435e-8cc1-a8cd70494d91"
        cmd = "delete fdb {0} vlan {1}".format(self.str_utils.normalize_mac(arg_dictionary['mac']),
                                               arg_dictionary['vlan_name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def create_blackhole_entry(self, arg_dictionary, **kwargs):
        uuid = "d2e810e2-d4a5-4775-b7b2-dc087479edc7"
        cmd = "create fdb {0} vlan {1} blackhole".format(self.str_utils.normalize_mac(arg_dictionary['mac']),
                                                         arg_dictionary['vlan_name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_learning_vlan(self, arg_dictionary, **kwargs):
        uuid = "e0863cc7-fd58-463e-9152-c041ab212648"
        cmd = "enable learning vlan {0}".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_learning_port(self, arg_dictionary, **kwargs):
        uuid = "8040411f-9a0b-4627-97a4-30145a1625f0"
        cmd = "disable learning port {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_learning_vlan(self, arg_dictionary, **kwargs):
        uuid = "7a410a50-052d-4560-bd7d-974fb0e45cfb"
        cmd = "enable learning vlan {0}".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_learning_port(self, arg_dictionary, **kwargs):
        uuid = "d49dc04a-9fcb-4e05-ac51-1a4107d6123f"
        cmd = "disable learning port {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_agetime(self, arg_dictionary, **kwargs):
        uuid = "1ed8be08-313f-4598-b926-59ef7dccdfd3"
        cmd = "show fdb"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_all_entries(self, arg_dictionary, **kwargs):
        uuid = "d4a7b29a-1b98-4d7f-9ae5-854280b9839a"
        cmd = "show fdb"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_entry(self, arg_dictionary, **kwargs):
        uuid = "ccaf6147-a3a7-4abc-8363-e820e491b0a9"
        cmd = "show fdb {0}".format(arg_dictionary['mac'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_stats(self, arg_dictionary, **kwargs):
        uuid = "580e73cc-3bb3-4969-bf36-9693e774e881"
        cmd = "show fdb stats"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_stats_port(self, arg_dictionary, **kwargs):
        uuid = "b66bd965-8cd4-4d34-b33c-253da38d49aa"
        cmd = "show fdb stats ports {0} no-refresh".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_stats_vlan(self, arg_dictionary, **kwargs):
        uuid = "7b06a937-6471-4e42-b07b-2682ff7a7dca"
        cmd = "show fdb stats {0} no-refresh".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_stats_vlan_name(self, arg_dictionary, **kwargs):
        uuid = "8482d37f-363b-4e4e-ba50-6eba757ef79a"
        cmd = "show fdb stats vlan {0} no-refresh".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_vlan(self, arg_dictionary, **kwargs):
        uuid = "d68b2ec4-ae4b-47b5-a9a6-860d8bedc72b"
        cmd = "show fdb {0} ".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_vlan_name(self, arg_dictionary, **kwargs):
        uuid = "eb426da0-ea1d-4ef3-8b00-c1a1065205c7"
        cmd = "show fdb vlan {0} ".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port(self, arg_dictionary, **kwargs):
        uuid = "2381d26e-3903-4d9f-89a3-0feb18f1bb6e"
        cmd = "show fdb port {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
