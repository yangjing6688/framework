"""
All cos supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.cos.base.cosbase import CosBase


class Cos(DeviceApi, CosBase):
    def __init__(self, device_input):
        super(Cos, self).__init__(device_input)

    def create_qos_profile(self, arg_dictionary, **kwargs):
        uuid = "66687146-d2d8-4032-9ce3-e462bce8ff76"
        cmd = "create qosprofile {0}".format(self.api_utils.exos_qos_profile(arg_dictionary['name']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def delete_qos_profile(self, arg_dictionary, **kwargs):
        uuid = "3fd8faed-e141-4950-9052-0d39b43477ec"
        cmd = "delete qosprofile {0}".format(self.api_utils.exos_qos_profile(arg_dictionary['name']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def create_port_group(self, arg_dictionary, **kwargs):
        uuid = "2b23f6de-6c28-4e8a-9d66-d10ea7062a2e"
        cmd = "create ports group {0}".format(arg_dictionary['group'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def delete_port_group(self, arg_dictionary, **kwargs):
        uuid = "59ce8d59-ddf9-4693-a2f2-383238ca76d8"
        cmd = "delete ports group {0}".format(arg_dictionary['group'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_port_group_port(self, arg_dictionary, **kwargs):
        uuid = "e2408845-64d2-4a97-88ea-40bfc874b99a"
        cmd = "configure ports group {0} add {1}".format(arg_dictionary['group'],
                                                         arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_txq_settings(self, arg_dictionary, **kwargs):
        uuid = "534ab29f-1519-4d51-8219-919c7a794f1f"
        cmd = "configure dot1p type {0} qosprofile {1} ingress-meter ingmeter{2}".format(arg_dictionary['cos_index'],
                                                                                         arg_dictionary['qos_profile'],
                                                                                         arg_dictionary['txq_index'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_txq_settings_cos_under_seven(self, arg_dictionary, **kwargs):
        uuid = "26cf69ba-cd93-423c-b0a3-adafc1da5763"
        cmd = "configure cos-index {0} qosprofile {1} ingress-meter ingmeter{2}".format(arg_dictionary['cos_index'],
                                                                                        arg_dictionary['qos_profile'],
                                                                                        arg_dictionary['txq_index'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_irl_settings(self, arg_dictionary, **kwargs):
        uuid = "3a0dda6f-e090-4863-a844-40dc73f84732"
        cmd = "configure cos-index {0} qosprofile {1} ingress-meter ingmeter{2}".format(arg_dictionary['cos_index'],
                                                                                        arg_dictionary['qos_profile'],
                                                                                        arg_dictionary['irl_index'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_irl_settings_cos_under_seven(self, arg_dictionary, **kwargs):
        uuid = "ee82d3f5-dfe9-40ab-a217-6e1c6df5dbbd"
        cmd = "configure dot1p type {0} qosprofile {1} ingress-meter ingmeter{2}".format(arg_dictionary['cos_index'],
                                                                                         arg_dictionary['qos_profile'],
                                                                                         arg_dictionary['irl_index'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_port_resource_irl(self, arg_dictionary, **kwargs):
        uuid = "40d8cbfa-559d-4d14-bab3-d3e693d98be0"
        cmd = "configure meter ingmeter{0} committed-rate {1} {2} ports {3}".format(arg_dictionary['irl_index'],
                                                                                    arg_dictionary['rate'],
                                                                                    arg_dictionary['unit'],
                                                                                    arg_dictionary['group'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_orl_settings(self, arg_dictionary, **kwargs):
        uuid = "d597935e-f0d1-4e50-8a57-bf681bedb113"
        cmd = "configure cos-index {0} qosprofile {1} ingress-meter ingmeter{2}".format(arg_dictionary['cos_index'],
                                                                                        arg_dictionary['qos_profile'],
                                                                                        arg_dictionary['orl_index'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_orl_settings_cos_under_seven(self, arg_dictionary, **kwargs):
        uuid = "47b5a9d7-ecd3-45c9-b34d-1e13f39ede5f"
        cmd = "configure dot1p type {0} qosprofile {1} ingress-meter ingmeter{2}".format(arg_dictionary['cos_index'],
                                                                                         arg_dictionary['qos_profile'],
                                                                                         arg_dictionary['orl_index'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_dot1p_type(self, arg_dictionary, **kwargs):
        uuid = "4fff49d4-25c8-44ac-99b0-25861d7e056c"
        cmd = "configure dot1p type {0} qosprofile {1} ingress-meter ingmeter{2}".format(arg_dictionary['cos_index'],
                                                                                         arg_dictionary['qos_profile'],
                                                                                         arg_dictionary['cos_index'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_dot1p_type_only(self, arg_dictionary, **kwargs):
        uuid = "c32e7b5e-ef21-4cf1-bce9-8eef31d090aa"
        cmd = "configure dot1p type {0} qosprofile {1}".format(arg_dictionary['cos_index'],
                                                               arg_dictionary['qos_profile'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_dot1p_port_type(self, arg_dictionary, **kwargs):
        uuid = "5eac757b-854e-49e8-8118-78200de11b1c"
        cmd = "configure ports {0} qosprofile {1}".format(arg_dictionary['port'],
                                                          arg_dictionary['qos_profile'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_qos_scheduler(self, arg_dictionary, **kwargs):
        uuid = "6f5e0812-c128-4952-a8a0-f86e5ae28f39"
        cmd = "configure qosscheduler {0} ports {1}".format(arg_dictionary['mode'],
                                                            arg_dictionary['group'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_txq_weights(self, arg_dictionary, **kwargs):
        uuid = "81961638-5dc2-4530-b986-10032653612e"
        cmd = "configure qosprofile {0} weight {1} ports {2}".format(arg_dictionary['txq'],
                                                                     arg_dictionary['weight'],
                                                                     arg_dictionary['group'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_tos_settings(self, arg_dictionary, **kwargs):
        uuid = "9d20361c-ec50-46f6-bdc0-8c1d9b467fb2"
        cmd = "configure cos-index {0} replace-tos {1}".format(arg_dictionary['cos_index'],
                                                               arg_dictionary['tos'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_tos_settings_cos_under_seven(self, arg_dictionary, **kwargs):
        uuid = "762aa767-837e-48a3-b9e3-677d64accb3e"
        cmd = "configure diffserv replacement {0} code-point {1}".format(arg_dictionary['qos_profile'],
                                                                         arg_dictionary['tos'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_priority_settings(self, arg_dictionary, **kwargs):
        uuid = "5b6beb6b-8a63-497d-8f32-75cd3b799a3d"
        cmd = "configure cos-index {0} qosprofile {1}".format(arg_dictionary['cos_index'],
                                                              arg_dictionary['qos_profile'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_priority_settings_cos_under_seven(self, arg_dictionary, **kwargs):
        uuid = "e5139fe0-4335-413c-b3a1-b379e81b0b01"
        cmd = "configure dot1p type {0} qosprofile {1}".format(arg_dictionary['cos_index'],
                                                               arg_dictionary['qos_profile'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_diff_serve_replacement(self, arg_dictionary, **kwargs):
        uuid = "f335362a-746b-49f6-8944-943f068d9d16"
        cmd = "configure diffserv replacement {0} code-point {1}".format(arg_dictionary['qos_profile'],
                                                                         arg_dictionary['tos'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_index(self, arg_dictionary, **kwargs):
        uuid = "4f88f1b6-0f76-4b46-a667-7b90779bf59e"
        cmd = "unconfigure cos-index {0}".format(arg_dictionary['cos_index'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_irl(self, arg_dictionary, **kwargs):
        uuid = "5e036414-f9be-4117-ac5e-be78c1127afc"
        cmd = "unconfigure meter ingmeter{0} ports {1}".format(arg_dictionary['irl_index'],
                                                               arg_dictionary['group'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_txq_shaping(self, arg_dictionary, **kwargs):
        uuid = "2edc366b-6292-45e5-8a28-e89348077eae"
        cmd = "configure qosprofile {0} peak_rate {1} {2} ports {3}".format(arg_dictionary['qos_profile'],
                                                                            arg_dictionary['rate'],
                                                                            arg_dictionary['unit'],
                                                                            arg_dictionary['group'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_txq_shaping(self, arg_dictionary, **kwargs):
        uuid = "72640ec5-c0dc-487b-87ef-f249f84cc05c"
        cmd = "unconfigure qosprofile ports {0}".format(arg_dictionary['group'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_port_priority(self, arg_dictionary, **kwargs):
        uuid = "aedcb0dc-f957-4b87-b815-65721c906e9a"
        cmd = "configure ports {0} dot1p {1}".format(arg_dictionary['port'],
                                                     arg_dictionary['pri'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_port_qos_profile(self, arg_dictionary, **kwargs):
        uuid = "61d087d3-4505-4a89-bd0b-ecc413d463ce"
        cmd = "configure port {0} qosprofile {1}".format(arg_dictionary['port'],
                                                         self.api_utils.exos_qos_profile(arg_dictionary['qos_profile']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_qos_profile(self, arg_dictionary, **kwargs):
        uuid = "8af5466a-74af-4c37-a0ed-8837a12ede2a"
        cmd = "show qosprofile"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port_qos_profile(self, arg_dictionary, **kwargs):
        uuid = "2d27c8a2-9489-42c0-874f-09be75f4790f"
        cmd = "show port {0} information detail".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_txq_port_group(self, arg_dictionary, **kwargs):
        uuid = "23c637da-2dc2-4ca0-804f-0ac6cfa139fa"
        cmd = "show ports group"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_irl_port_group(self, arg_dictionary, **kwargs):
        uuid = "2ca4b67d-e4bc-488c-abfd-e1297c797c7b"
        cmd = "show ports group"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_txq_port_group_specific(self, arg_dictionary, **kwargs):
        uuid = "cbe6c744-9dc1-4426-8988-fea7ac6f8f8b"
        cmd = "show ports group {0}".format(arg_dictionary['group'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_irl_port_group_specific(self, arg_dictionary, **kwargs):
        uuid = "e7689244-5e18-4dd2-b976-b1f1f5971fec"
        cmd = "show ports group {0}".format(arg_dictionary['group'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_txq_wfq_weights(self, arg_dictionary, **kwargs):
        uuid = "6604b740-d30e-4fa5-b90e-3a3bcbda1fe2"
        cmd = "show qosprofile ports {0}".format(arg_dictionary['group'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_irl_wfq_weights(self, arg_dictionary, **kwargs):
        uuid = "107298bb-d6ae-46c5-b305-1bed401515d0"
        cmd = "show qosprofile ports {0}".format(arg_dictionary['group'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_txq_port_resource_specific(self, arg_dictionary, **kwargs):
        uuid = "c1317888-e5c9-4782-99b3-8030f254ced6"
        cmd = "show meter ingmeter{0}".format(arg_dictionary['cos_index'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_irl_port_resource_specific(self, arg_dictionary, **kwargs):
        uuid = "0889d392-49f0-493a-ab67-400f65d5308b"
        cmd = "show meter ingmeter{0}".format(arg_dictionary['cos_index'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_qos_scheduler(self, arg_dictionary, **kwargs):
        uuid = "09e8faf0-586f-448b-93fa-66d33f4ef28e"
        cmd = "show qosscheduler ports {0}".format(arg_dictionary['group'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_settings(self, arg_dictionary, **kwargs):
        uuid = "8b13448c-1ef0-4618-a60e-c211f1e18dfc"
        cmd = "show cos-index"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port_priority(self, arg_dictionary, **kwargs):
        uuid = "97c2d9be-0104-4fee-9377-67980e562501"
        cmd = "show port {0} information detail".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port_info_detail(self, arg_dictionary, **kwargs):
        uuid = "4b41b6b8-9790-490a-b66d-2e1b742d5cf2"
        cmd = "show ports {0} information detail".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
