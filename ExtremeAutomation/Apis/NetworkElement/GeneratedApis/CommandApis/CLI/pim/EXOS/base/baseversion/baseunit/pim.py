"""
All pim supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.pim.base.pimbase import PimBase


class Pim(DeviceApi, PimBase):
    def __init__(self, device_input):
        super(Pim, self).__init__(device_input)

    def enable(self, arg_dictionary, **kwargs):
        uuid = "2ea0a641-0c71-44f1-b414-f118bda2b214"
        cmd = "enable pim"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable(self, arg_dictionary, **kwargs):
        uuid = "1d82492c-8d8b-42bc-abe6-7e5a4577c68c"
        cmd = "disable pim"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_sparse(self, arg_dictionary, **kwargs):
        uuid = "9aa86d46-68cf-4c13-a466-a93068dbbeb6"
        cmd = "configure pim add {0} {1}".format(arg_dictionary['vlan'],
                                                 arg_dictionary['exos_mode'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_sparse(self, arg_dictionary, **kwargs):
        uuid = "0df06e63-809b-41ee-a689-9c4a00ae4998"
        cmd = "configure pim delete {0}".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_rp(self, arg_dictionary, **kwargs):
        uuid = "dde6ad18-c92d-4adf-ae33-bcc41017c9c2"
        cmd = "configure pim crp {0} {1}".format(arg_dictionary['interface'],
                                                 arg_dictionary['acl'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_bsr_priority(self, arg_dictionary, **kwargs):
        uuid = "1f90fadf-b3df-4e1e-930e-4fb774b9a74e"
        cmd = "configure pim cbsr {0} {1}".format(arg_dictionary['interface'],
                                                  arg_dictionary['priority'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_cache(self, arg_dictionary, **kwargs):
        uuid = "bda40a90-b5f8-4229-a94d-bfef85b44422"
        cmd = "clear pim cache {0}".format(arg_dictionary['mcast_group_address'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_info(self, arg_dictionary, **kwargs):
        uuid = "7d7c7c2f-adbf-4f15-9f0f-9d0c94a68eb2"
        cmd = "show pim"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_bsr(self, arg_dictionary, **kwargs):
        uuid = "70d5b5ee-5137-428b-a309-594642ec432b"
        cmd = "show pim detail"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_rp(self, arg_dictionary, **kwargs):
        uuid = "455651e9-8084-4043-9781-28474afd9a31"
        cmd = "show configuration pim"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_vlan(self, arg_dictionary, **kwargs):
        uuid = "2ef3a781-aac3-4dd7-b069-6850ac2b63c9"
        cmd = "show pim vlan {0}".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_cache(self, arg_dictionary, **kwargs):
        uuid = "737e512b-ce7c-4a31-99ca-035fd6613083"
        cmd = "show pim cache"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_cache_group(self, arg_dictionary, **kwargs):
        uuid = "297b8551-9f31-47d9-a97e-07f523b89521"
        cmd = "show pim cache {0}".format(arg_dictionary['dest_group'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_rp_set(self, arg_dictionary, **kwargs):
        uuid = "b8661a1d-e91f-4036-8dee-e69a2998cf5d"
        cmd = "show pim rp-set"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_rp_set_group(self, arg_dictionary, **kwargs):
        uuid = "c4d7c570-3988-4fba-8aaa-3fae8467f8b2"
        cmd = "show pim rp-set {0}".format(arg_dictionary['mcast_group_address'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
