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
        cmd = "ip pim enable"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable(self, arg_dictionary, **kwargs):
        uuid = "1d82492c-8d8b-42bc-abe6-7e5a4577c68c"
        cmd = "no ip pim enable"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_sparse(self, arg_dictionary, **kwargs):
        uuid = "9aa86d46-68cf-4c13-a466-a93068dbbeb6"
        cmd = "ip pim mode sparse"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_rp(self, arg_dictionary, **kwargs):
        uuid = "dde6ad18-c92d-4adf-ae33-bcc41017c9c2"
        cmd = "ip pim rp-candidate group {0} {1} rp {2}".format(arg_dictionary['mcast_group_address'],
                                                                arg_dictionary['mask'],
                                                                arg_dictionary['ip'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_bsr_priority(self, arg_dictionary, **kwargs):
        uuid = "1f90fadf-b3df-4e1e-930e-4fb774b9a74e"
        cmd = "ip pim bsr-candidate preference {0}".format(arg_dictionary['priority'])
        prompt = "intfPrompt"
        prompt_args = "GigabitEthernet {0}".format(arg_dictionary['interface'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def enable_interface(self, arg_dictionary, **kwargs):
        uuid = "2f125372-eb07-4026-ac07-d8496c900dcb"
        cmd = "ip pim enable"
        prompt = "intfPrompt"
        prompt_args = "GigabitEthernet {0}".format(arg_dictionary['port'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def enable_interface_vlan(self, arg_dictionary, **kwargs):
        uuid = "a29ab14c-4118-4b89-8db4-050389320a90"
        cmd = "ip pim enable"
        prompt = "intfPrompt"
        prompt_args = "vlan {0}".format(arg_dictionary['vlan'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def enable_ssm(self, arg_dictionary, **kwargs):
        uuid = "dbd29b01-730a-4f46-a94d-be979c9bd715"
        cmd = "ip pim mode ssm||yes"
        prompt = "routerConfigPrompt"
        conf = "Do you wish to continue? (y/n) ?"
        conf_args = "{0}".format(arg_dictionary['answer'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf, conf_args=conf_args)

    def disable_interface(self, arg_dictionary, **kwargs):
        uuid = "e0c7f6f0-1156-4df5-99a3-b6485fe02ac3"
        cmd = "no ip pim enable"
        prompt = "intfPrompt"
        prompt_args = "GigabitEthernet {0}".format(arg_dictionary['port'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def disable_interface_vlan(self, arg_dictionary, **kwargs):
        uuid = "f732d752-dd26-4ff5-8b4e-0572215066a0"
        cmd = "no ip pim enable"
        prompt = "intfPrompt"
        prompt_args = "vlan {0}".format(arg_dictionary['vlan'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_bsr_priority_vlan(self, arg_dictionary, **kwargs):
        uuid = "49b462e7-2600-49af-b40a-4ea6e2553b01"
        cmd = "ip pim bsr-candidate preference {0}".format(arg_dictionary['priority'])
        prompt = "intfPrompt"
        prompt_args = "vlan {0}".format(arg_dictionary['vlan'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_rp_static(self, arg_dictionary, **kwargs):
        uuid = "a079226c-fb18-47e9-bead-fb4118ddcdf8"
        cmd = "ip pim static-rp"
        prompt = "routerConfigPrompt"
        conf = "Do you wish to enable Static RP? (y/n) ?"
        conf_args = "{0}".format(arg_dictionary['answer'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf, conf_args=conf_args)

    def set_interface_active(self, arg_dictionary, **kwargs):
        uuid = "522a379f-6419-453e-b276-7b22065b4040"
        cmd = "ip pim active"
        prompt = "intfPrompt"
        prompt_args = "GigabitEthernet {0}".format(arg_dictionary['port'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_interface_passive(self, arg_dictionary, **kwargs):
        uuid = "d45d3028-1eda-492e-ada7-07139874005b"
        cmd = "ip pim passive"
        prompt = "intfPrompt"
        prompt_args = "GigabitEthernet {0}".format(arg_dictionary['port'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_vlan_active(self, arg_dictionary, **kwargs):
        uuid = "cb7046f0-a67b-4bd5-97a9-081a45a6c458"
        cmd = "ip pim active"
        prompt = "intfPrompt"
        prompt_args = "vlan {0}".format(arg_dictionary['vlan'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_vlan_passive(self, arg_dictionary, **kwargs):
        uuid = "b2f50332-3266-4d74-b2dd-bbe57560c93a"
        cmd = "ip pim passive"
        prompt = "intfPrompt"
        prompt_args = "vlan {0}".format(arg_dictionary['vlan'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def clear_rp(self, arg_dictionary, **kwargs):
        uuid = "f70f48d0-844b-4692-b68a-1e334d3b369f"
        cmd = "no ip pim rp-candidate group {0} {1}".format(arg_dictionary['ip'],
                                                            arg_dictionary['mask'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_info(self, arg_dictionary, **kwargs):
        uuid = "7d7c7c2f-adbf-4f15-9f0f-9d0c94a68eb2"
        cmd = "show ip pim"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_bsr(self, arg_dictionary, **kwargs):
        uuid = "70d5b5ee-5137-428b-a309-594642ec432b"
        cmd = "show ip pim bsr"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_rp(self, arg_dictionary, **kwargs):
        uuid = "455651e9-8084-4043-9781-28474afd9a31"
        cmd = "show ip pim rp-candidate"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_vlan(self, arg_dictionary, **kwargs):
        uuid = "2ef3a781-aac3-4dd7-b069-6850ac2b63c9"
        cmd = "show ip pim interface vlan {0}".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_interface(self, arg_dictionary, **kwargs):
        uuid = "9b49883a-3c46-4389-b8c8-dda5c0fffdb2"
        cmd = "show ip pim interface GigabitEthernet {0}".format(arg_dictionary['interface'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
