"""
All mlt supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.mlt.base.mltbase import MltBase


class Mlt(DeviceApi, MltBase):
    def __init__(self, device_input):
        super(Mlt, self).__init__(device_input)

    def create_id(self, arg_dictionary, **kwargs):
        uuid = "61c7cf26-44c8-47eb-b0b1-344baf998f46"
        cmd = "mlt {0}".format(arg_dictionary['mlt_id'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def delete_id(self, arg_dictionary, **kwargs):
        uuid = "10cf289a-a38f-40ab-985a-e1edab663ebd"
        cmd = "no mlt {0}".format(arg_dictionary['mlt_id'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_flex_uni(self, arg_dictionary, **kwargs):
        uuid = "97c17a90-02d4-4b74-af4e-80bc48f5fa95"
        cmd = "flex-uni enable"
        prompt = "intfPrompt"
        prompt_args = "mlt {0}".format(arg_dictionary['mlt_id'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def disable_flex_uni(self, arg_dictionary, **kwargs):
        uuid = "a9841ef0-3767-404f-84b5-a4125aa299a2"
        cmd = "no flex-uni enable"
        prompt = "intfPrompt"
        prompt_args = "mlt {0}".format(arg_dictionary['mlt_id'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def enable_lacp(self, arg_dictionary, **kwargs):
        uuid = "1e1368d4-55d7-4507-a051-2b8a7752f43b"
        cmd = "lacp enable"
        prompt = "intfPrompt"
        prompt_args = "mlt {0}".format(arg_dictionary['mlt_id'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def disable_lacp(self, arg_dictionary, **kwargs):
        uuid = "68d147b8-0e4e-4ca6-9fb1-51cc995252ef"
        cmd = "no lacp enable"
        prompt = "intfPrompt"
        prompt_args = "mlt {0}".format(arg_dictionary['mlt_id'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_port_member(self, arg_dictionary, **kwargs):
        uuid = "5932c3c8-ee1e-497e-84a9-0d359a20fb79"
        cmd = "mlt {0} member {1}".format(arg_dictionary['mlt_id'],
                                          arg_dictionary['port'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_port_member(self, arg_dictionary, **kwargs):
        uuid = "7e1bb41b-e957-4855-b711-a7165922d877"
        cmd = "no mlt {0} member {1}".format(arg_dictionary['mlt_id'],
                                             arg_dictionary['port'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_type_split_mlt(self, arg_dictionary, **kwargs):
        uuid = "1b4685fe-bb79-40d1-9e07-52a4309e564c"
        cmd = "smlt"
        prompt = "intfPrompt"
        prompt_args = "mlt {0}".format(arg_dictionary['mlt_id'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_type_normal_mlt(self, arg_dictionary, **kwargs):
        uuid = "42dad7ab-c2b1-47eb-968a-4770a759368e"
        cmd = "no smlt"
        prompt = "intfPrompt"
        prompt_args = "mlt {0}".format(arg_dictionary['mlt_id'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_encapsulation_dot1q(self, arg_dictionary, **kwargs):
        uuid = "4ce20ab9-ec4a-4726-8051-5afdb7c4d86c"
        cmd = "mlt {0} encapsulation dot1q".format(arg_dictionary['mlt_id'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_encapsulation_dot1q(self, arg_dictionary, **kwargs):
        uuid = "29d08a66-c90a-4bbb-8e85-0393f2e372d9"
        cmd = "no mlt {0} encapsulation dot1q".format(arg_dictionary['mlt_id'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_logical_index(self, arg_dictionary, **kwargs):
        uuid = "f9e61724-4bd5-41ba-8b2d-55c509385e19"
        cmd = "show mlt {0}".format(arg_dictionary['mlt_id'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_id(self, arg_dictionary, **kwargs):
        uuid = "807b2755-0104-46a2-870b-4da5acd5c071"
        cmd = "show mlt {0}".format(arg_dictionary['mlt_id'])
        prompt = "userPrompt"

        self.device.error_checker.add_error_to_ignore_list(*["Error"])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_admin_type(self, arg_dictionary, **kwargs):
        uuid = "bb540ad3-2e42-42af-8aeb-3ec6dd029160"
        cmd = "show mlt {0}".format(arg_dictionary['mlt_id'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_running_type(self, arg_dictionary, **kwargs):
        uuid = "5e58916a-129a-4991-b96c-740c57282f27"
        cmd = "show mlt {0}".format(arg_dictionary['mlt_id'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_flex_uni_status(self, arg_dictionary, **kwargs):
        uuid = "2ea5876e-eb29-440c-94ff-a0987f93c6b1"
        cmd = "show mlt {0}".format(arg_dictionary['mlt_id'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_lacp_admin_status(self, arg_dictionary, **kwargs):
        uuid = "ace34c52-0b00-4837-813a-6d628aad74ec"
        cmd = "show mlt {0}".format(arg_dictionary['mlt_id'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_lacp_oper_status(self, arg_dictionary, **kwargs):
        uuid = "b88d9f44-5711-4553-a26c-42a96642a18a"
        cmd = "show mlt {0}".format(arg_dictionary['mlt_id'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_ports(self, arg_dictionary, **kwargs):
        uuid = "d7f2ad07-8835-4d66-8a93-2d9ea6eaeb31"
        cmd = "show mlt {0}".format(arg_dictionary['mlt_id'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_encapsulation(self, arg_dictionary, **kwargs):
        uuid = "d2230dff-7053-440b-998d-7fcf101d6134"
        cmd = "show mlt {0}".format(arg_dictionary['mlt_id'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
