"""
All cos supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.cos.base.cosbase import CosBase


class Cos(DeviceApi, CosBase):
    def __init__(self, device_input):
        super(Cos, self).__init__(device_input)

    def create_port_group(self, arg_dictionary, **kwargs):
        uuid = "2b23f6de-6c28-4e8a-9d66-d10ea7062a2e"
        cmd = "set cos port-config {0} {1}".format(arg_dictionary['cos_type'],
                                                   arg_dictionary['group'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def delete_port_group(self, arg_dictionary, **kwargs):
        uuid = "59ce8d59-ddf9-4693-a2f2-383238ca76d8"
        cmd = "clear cos port-config {0} {1} entry".format(arg_dictionary['cos_type'],
                                                           arg_dictionary['group'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_port_group_port(self, arg_dictionary, **kwargs):
        uuid = "e2408845-64d2-4a97-88ea-40bfc874b99a"
        cmd = "set cos port-config {0} {1} append ports {2}".format(arg_dictionary['cos_type'],
                                                                    arg_dictionary['group'],
                                                                    arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_txq_settings(self, arg_dictionary, **kwargs):
        uuid = "534ab29f-1519-4d51-8219-919c7a794f1f"
        cmd = "set cos settings {0} txq-reference {1}".format(arg_dictionary['cos_index'],
                                                              arg_dictionary['txq_index'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_txq_settings_cos_under_seven(self, arg_dictionary, **kwargs):
        uuid = "26cf69ba-cd93-423c-b0a3-adafc1da5763"
        cmd = "set cos settings {0} txq-reference {1}".format(arg_dictionary['cos_index'],
                                                              arg_dictionary['txq_index'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_irl_settings(self, arg_dictionary, **kwargs):
        uuid = "3a0dda6f-e090-4863-a844-40dc73f84732"
        cmd = "set cos settings {0} priority {1} irl-reference {2}".format(arg_dictionary['cos_index'],
                                                                           arg_dictionary['priority'],
                                                                           arg_dictionary['irl_index'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_irl_settings_cos_under_seven(self, arg_dictionary, **kwargs):
        uuid = "ee82d3f5-dfe9-40ab-a217-6e1c6df5dbbd"
        cmd = "set cos settings {0} irl-reference {1}".format(arg_dictionary['cos_index'],
                                                              arg_dictionary['irl_index'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_port_resource_irl(self, arg_dictionary, **kwargs):
        uuid = "40d8cbfa-559d-4d14-bab3-d3e693d98be0"
        cmd = "set cos port-resource irl {0} {1} unit {2} rate {3}|| set cos reference irl {4} {5} rate-limit {6}".format(arg_dictionary['group'],
                                                                                                                          arg_dictionary['irl_index'],
                                                                                                                          arg_dictionary['unit'],
                                                                                                                          arg_dictionary['rate'],
                                                                                                                          arg_dictionary['group'],
                                                                                                                          arg_dictionary['irl_index'],
                                                                                                                          arg_dictionary['irl_index'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_orl_settings(self, arg_dictionary, **kwargs):
        uuid = "d597935e-f0d1-4e50-8a57-bf681bedb113"
        cmd = "set cos settings {0} priority {1} orl-reference {2}".format(arg_dictionary['cos_index'],
                                                                           arg_dictionary['priority'],
                                                                           arg_dictionary['orl_index'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_orl_settings_cos_under_seven(self, arg_dictionary, **kwargs):
        uuid = "47b5a9d7-ecd3-45c9-b34d-1e13f39ede5f"
        cmd = "set cos settings {0} orl-reference {1}".format(arg_dictionary['cos_index'],
                                                              arg_dictionary['orl_index'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_txq_weights(self, arg_dictionary, **kwargs):
        uuid = "81961638-5dc2-4530-b986-10032653612e"
        cmd = "set cos port-config txq {0} arb-percentage {1}".format(arg_dictionary['group'],
                                                                      arg_dictionary['weights'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_tos_settings(self, arg_dictionary, **kwargs):
        uuid = "9d20361c-ec50-46f6-bdc0-8c1d9b467fb2"
        cmd = "set cos settings {0} tos-value {1}".format(arg_dictionary['cos_index'],
                                                          arg_dictionary['tos'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_tos_settings_cos_under_seven(self, arg_dictionary, **kwargs):
        uuid = "762aa767-837e-48a3-b9e3-677d64accb3e"
        cmd = "set cos settings {0} tos-value {1}".format(arg_dictionary['cos_index'],
                                                          arg_dictionary['tos'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_priority_settings(self, arg_dictionary, **kwargs):
        uuid = "5b6beb6b-8a63-497d-8f32-75cd3b799a3d"
        cmd = "set cos settings {0} priority {1}".format(arg_dictionary['cos_index'],
                                                         arg_dictionary['priority'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_priority_settings_cos_under_seven(self, arg_dictionary, **kwargs):
        uuid = "e5139fe0-4335-413c-b3a1-b379e81b0b01"
        cmd = "set cos settings {0} priority {1}".format(arg_dictionary['cos_index'],
                                                         arg_dictionary['priority'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_index(self, arg_dictionary, **kwargs):
        uuid = "4f88f1b6-0f76-4b46-a667-7b90779bf59e"
        cmd = "clear cos settings {0} all".format(arg_dictionary['cos_index'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_irl(self, arg_dictionary, **kwargs):
        uuid = "5e036414-f9be-4117-ac5e-be78c1127afc"
        cmd = "clear cos irl {0} {1}".format(arg_dictionary['group'],
                                             arg_dictionary['irl_index'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_txq_shaping(self, arg_dictionary, **kwargs):
        uuid = "2edc366b-6292-45e5-8a28-e89348077eae"
        cmd = "set cos port-resource txq {0} {1} rate {2} unit {3}".format(arg_dictionary['group'],
                                                                           arg_dictionary['txq'],
                                                                           arg_dictionary['rate'],
                                                                           arg_dictionary['unit'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_txq_shaping(self, arg_dictionary, **kwargs):
        uuid = "72640ec5-c0dc-487b-87ef-f249f84cc05c"
        cmd = "clear cos port-resource txq {0} {1}".format(arg_dictionary['group'],
                                                           arg_dictionary['txq'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_port_priority(self, arg_dictionary, **kwargs):
        uuid = "aedcb0dc-f957-4b87-b815-65721c906e9a"
        cmd = "set port priority {0} {1}".format(arg_dictionary['port'],
                                                 arg_dictionary['pri'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_state(self, arg_dictionary, **kwargs):
        uuid = "a4405432-6e50-48a2-ae3f-7188264bac9b"
        cmd = "set cos state enable"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_state(self, arg_dictionary, **kwargs):
        uuid = "18a6c301-b0ad-4e01-b6bc-9c7c090a3b6d"
        cmd = "set cos state disable"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_txq_reference(self, arg_dictionary, **kwargs):
        uuid = "f72a808d-5200-4422-8364-3bf5d683b12b"
        cmd = "set cos reference txq {0} {1} queue {2}".format(arg_dictionary['group'],
                                                               arg_dictionary['reference'],
                                                               arg_dictionary['queue'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_txq_settings(self, arg_dictionary, **kwargs):
        uuid = "f0586b7e-8d8c-4b21-a818-d9beace3192d"
        cmd = "clear cos settings {0} txq-reference".format(arg_dictionary['cos_index'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_irl_reference(self, arg_dictionary, **kwargs):
        uuid = "340f5bfb-6f5e-4969-af93-38327ff4b428"
        cmd = "set cos reference irl {0} {1} rate-limit {2}".format(arg_dictionary['group'],
                                                                    arg_dictionary['reference'],
                                                                    arg_dictionary['number'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_irl_settings(self, arg_dictionary, **kwargs):
        uuid = "43b138cd-a7ed-48f4-af24-fe092573d725"
        cmd = "clear cos settings {0} irl-reference".format(arg_dictionary['cos_index'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_orl_reference(self, arg_dictionary, **kwargs):
        uuid = "89cc3486-532c-4aaa-a7bb-29f0f59b9d8a"
        cmd = "set cos reference orl {0} {1} rate-limit {2}".format(arg_dictionary['group'],
                                                                    arg_dictionary['reference'],
                                                                    arg_dictionary['number'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_port_resource_orl(self, arg_dictionary, **kwargs):
        uuid = "c612d698-6767-4b14-b06a-479d69987aa5"
        cmd = "set cos port-resource orl {0} {1} unit {2} rate {3}|| set cos reference orl {4} {5} rate-limit {6}".format(arg_dictionary['group'],
                                                                                                                          arg_dictionary['orl_index'],
                                                                                                                          arg_dictionary['unit'],
                                                                                                                          arg_dictionary['rate'],
                                                                                                                          arg_dictionary['group'],
                                                                                                                          arg_dictionary['orl_index'],
                                                                                                                          arg_dictionary['orl_index'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_orl_settings(self, arg_dictionary, **kwargs):
        uuid = "9313c590-f148-4abe-87d0-fe5ffb2202b6"
        cmd = "clear cos settings {0} orl-reference".format(arg_dictionary['cos_index'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_tos_settings(self, arg_dictionary, **kwargs):
        uuid = "557f1555-5501-4215-a868-ee04fd7841d9"
        cmd = "clear cos settings {0} tos-value".format(arg_dictionary['cos_index'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_flood_ctrl_settings(self, arg_dictionary, **kwargs):
        uuid = "c4ffb22d-4229-44f7-ab5e-1402bced0123"
        cmd = "clear cos settings {0} flood-ctrl".format(arg_dictionary['cos_index'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_all_config(self, arg_dictionary, **kwargs):
        uuid = "6eb8182a-3f4e-4297-bdcb-91cf976a3b10"
        cmd = "clear cos all-entries"
        prompt = "userPrompt"
        conf = "(y/n)"
        conf_args = "y"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf, conf_args=conf_args)

    def show_txq_port_group(self, arg_dictionary, **kwargs):
        uuid = "23c637da-2dc2-4ca0-804f-0ac6cfa139fa"
        cmd = "show cos port-config txq"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_irl_port_group(self, arg_dictionary, **kwargs):
        uuid = "2ca4b67d-e4bc-488c-abfd-e1297c797c7b"
        cmd = "show cos port-config irl"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_txq_port_group_specific(self, arg_dictionary, **kwargs):
        uuid = "cbe6c744-9dc1-4426-8988-fea7ac6f8f8b"
        cmd = "show cos port-config txq {0}".format(arg_dictionary['group'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_irl_port_group_specific(self, arg_dictionary, **kwargs):
        uuid = "e7689244-5e18-4dd2-b976-b1f1f5971fec"
        cmd = "show cos port-config irl {0}".format(arg_dictionary['group'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_txq_wfq_weights(self, arg_dictionary, **kwargs):
        uuid = "6604b740-d30e-4fa5-b90e-3a3bcbda1fe2"
        cmd = "show cos port-config txq {0}".format(arg_dictionary['group'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_irl_wfq_weights(self, arg_dictionary, **kwargs):
        uuid = "107298bb-d6ae-46c5-b305-1bed401515d0"
        cmd = "show cos port-config irl {0}".format(arg_dictionary['group'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_txq_port_resource_specific(self, arg_dictionary, **kwargs):
        uuid = "c1317888-e5c9-4782-99b3-8030f254ced6"
        cmd = "show cos port-resource txq {0} {1}".format(arg_dictionary['group'],
                                                          arg_dictionary['cos_index'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_irl_port_resource_specific(self, arg_dictionary, **kwargs):
        uuid = "0889d392-49f0-493a-ab67-400f65d5308b"
        cmd = "show cos port-resource irl {0} {1}".format(arg_dictionary['group'],
                                                          arg_dictionary['cos_index'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_settings(self, arg_dictionary, **kwargs):
        uuid = "8b13448c-1ef0-4618-a60e-c211f1e18dfc"
        cmd = "show cos settings"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port_priority(self, arg_dictionary, **kwargs):
        uuid = "97c2d9be-0104-4fee-9377-67980e562501"
        cmd = "show port priority {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port_info_detail(self, arg_dictionary, **kwargs):
        uuid = "4b41b6b8-9790-490a-b66d-2e1b742d5cf2"
        cmd = "show port status {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_txq_port_resource(self, arg_dictionary, **kwargs):
        uuid = "b5dbeeb0-7ff4-409e-89f9-06442ed4fa1b"
        cmd = "show cos port-resource txq {0}".format(arg_dictionary['group'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_irl_port_resource(self, arg_dictionary, **kwargs):
        uuid = "a2e90dc9-f2f3-4619-a838-6db6e6725216"
        cmd = "show cos port-resource irl {0}".format(arg_dictionary['group'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_orl_port_resource(self, arg_dictionary, **kwargs):
        uuid = "87e83d8c-bf1b-4dd9-8937-57a759acd060"
        cmd = "show cos port-resource orl {0}".format(arg_dictionary['group'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_txq_reference(self, arg_dictionary, **kwargs):
        uuid = "fa0aa14d-7015-4b3a-9416-82cd84226498"
        cmd = "show cos reference txq {0}".format(arg_dictionary['group'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_irl_reference(self, arg_dictionary, **kwargs):
        uuid = "68aed0bb-747f-4bf0-a8a3-710c0d7ba107"
        cmd = "show cos reference irl {0}".format(arg_dictionary['group'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_orl_reference(self, arg_dictionary, **kwargs):
        uuid = "24d8c23d-249a-42d6-8b3e-672f57764661"
        cmd = "show cos reference orl {0}".format(arg_dictionary['group'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_state(self, arg_dictionary, **kwargs):
        uuid = "0ccbb8d4-5ae5-4e01-84dc-8fbd9e868808"
        cmd = "show cos state"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
