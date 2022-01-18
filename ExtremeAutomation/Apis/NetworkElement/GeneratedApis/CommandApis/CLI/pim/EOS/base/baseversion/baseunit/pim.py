"""
All pim supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.pim.base.pimbase import PimBase


class Pim(DeviceApi, PimBase):
    def __init__(self, device_input):
        super(Pim, self).__init__(device_input)

    def enable_sparse(self, arg_dictionary, **kwargs):
        uuid = "9aa86d46-68cf-4c13-a466-a93068dbbeb6"
        cmd = "{0} pim {1}".format(arg_dictionary['ip_ver'],
                                   arg_dictionary['mode'])
        prompt = "intfPrompt"
        prompt_args = "{0}".format(arg_dictionary['interface'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def disable_sparse(self, arg_dictionary, **kwargs):
        uuid = "0df06e63-809b-41ee-a689-9c4a00ae4998"
        cmd = "no {0} pim {1}".format(arg_dictionary['ip_ver'],
                                      arg_dictionary['mode'])
        prompt = "intfPrompt"
        prompt_args = "{0}".format(arg_dictionary['interface'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_rp(self, arg_dictionary, **kwargs):
        uuid = "dde6ad18-c92d-4adf-ae33-bcc41017c9c2"
        cmd = "ip pim rp-candidate {0} group-list {1}".format(arg_dictionary['ip'],
                                                              arg_dictionary['acl'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_bsr_priority(self, arg_dictionary, **kwargs):
        uuid = "1f90fadf-b3df-4e1e-930e-4fb774b9a74e"
        cmd = "ip pim bsr-candidate {0} priority {1}".format(arg_dictionary['ip'],
                                                             arg_dictionary['priority'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_bsr(self, arg_dictionary, **kwargs):
        uuid = "70d5b5ee-5137-428b-a309-594642ec432b"
        cmd = "show ip pim bsr"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_rp(self, arg_dictionary, **kwargs):
        uuid = "455651e9-8084-4043-9781-28474afd9a31"
        cmd = "show run pim"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
