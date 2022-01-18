"""
All policy supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.policy.base.policybase import PolicyBase


class Policy(DeviceApi, PolicyBase):
    def __init__(self, device_input):
        super(Policy, self).__init__(device_input)

    def set_profile(self, arg_dictionary, **kwargs):
        uuid = "186cd3f0-1c59-4c01-8d30-3469e618861d"
        cmd = "create {0}".format(arg_dictionary['profile_id'])
        prompt = "ewBaseRolePrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_profile(self, arg_dictionary, **kwargs):
        uuid = "1b24bfee-47d4-4044-9312-3a5f8306faf2"
        cmd = "delete {0}".format(arg_dictionary['profile_id'])
        prompt = "ewBaseRolePrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_profile_cos(self, arg_dictionary, **kwargs):
        uuid = "7ed1047d-4e70-4bf1-b876-8a528ae2d8ff"
        cmd = "default-cos {0}".format(arg_dictionary['cos_name'])
        prompt = "ewRolePrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_profile_egress_vlan(self, arg_dictionary, **kwargs):
        uuid = "2df5030d-a802-4114-afd5-9a8438b02dc5"
        cmd = "egress-vlans enable {0}".format(arg_dictionary['vlan'])
        prompt = "ewRolePrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_profile_access_control(self, arg_dictionary, **kwargs):
        uuid = "58b7c94e-e02e-4ce8-be2a-34d987ec0667"
        cmd = "access-control {0}".format(arg_dictionary['state'])
        prompt = "ewRolePrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_profile_traffic_mirror(self, arg_dictionary, **kwargs):
        uuid = "3444cb7b-7790-40a5-a7fa-bf6baeb90a70"
        cmd = "traffic-mirror {0}".format(arg_dictionary['mirror_state'])
        prompt = "ewRolePrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_rule_l7(self, arg_dictionary, **kwargs):
        uuid = "ce7cf52e-bbfa-4d6f-90bc-28ca12a83bbe"
        cmd = "create {0} app-signature group {1} name {2} in {3} out {4} {5} cos {6} traffic-mirror {7}||apply {8}".format(arg_dictionary['rule_id'],
                                                                                                                            arg_dictionary['group_name'],
                                                                                                                            arg_dictionary['app_name'],
                                                                                                                            arg_dictionary['in_filter_action'],
                                                                                                                            arg_dictionary['out_filter_action'],
                                                                                                                            arg_dictionary['access_control'],
                                                                                                                            arg_dictionary['cos_name'],
                                                                                                                            arg_dictionary['mirror_state'],
                                                                                                                            arg_dictionary['profile_name'])
        prompt = "ewAcFiltersPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_rule_l7(self, arg_dictionary, **kwargs):
        uuid = "274f530c-7715-418e-932f-7482ad7cbf91"
        cmd = "delete {0}||apply {1}".format(arg_dictionary['rule_id'],
                                             arg_dictionary['profile_name'])
        prompt = "ewAcFiltersPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_rule_l7_configure(self, arg_dictionary, **kwargs):
        uuid = "967f6656-1398-48ea-bcb6-c4e2e8c7186b"
        cmd = "config {0} app-signature group {1} name {2} in {3} out {4} {5} cos {6} traffic-mirror {7}".format(arg_dictionary['rule_id'],
                                                                                                                 arg_dictionary['group_name'],
                                                                                                                 arg_dictionary['app_name'],
                                                                                                                 arg_dictionary['in_filter_action'],
                                                                                                                 arg_dictionary['out_filter_action'],
                                                                                                                 arg_dictionary['access_control'],
                                                                                                                 arg_dictionary['cos_name'],
                                                                                                                 arg_dictionary['mirror_state'])
        prompt = "ewAcFiltersPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_rule_apply(self, arg_dictionary, **kwargs):
        uuid = "2f33e730-926b-4585-b011-2fa6537d21a6"
        cmd = "apply {0}".format(arg_dictionary['profile_name'])
        prompt = "ewAcFiltersPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_all_profiles(self, arg_dictionary, **kwargs):
        uuid = "4cc7973d-623a-4ba9-a48a-3963adc44854"
        cmd = "role show"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_rules_profile(self, arg_dictionary, **kwargs):
        uuid = "5e757112-dbf2-46f6-98d3-c97d3966fcbe"
        cmd = "role {0} acfilters show".format(arg_dictionary['profile_id'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_profile_detail(self, arg_dictionary, **kwargs):
        uuid = "49398e02-08d0-4cb0-997c-e333ac188cba"
        cmd = "role {0} show".format(arg_dictionary['profile_name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
