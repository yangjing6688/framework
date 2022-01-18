"""
All macsec supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.macsec.base.macsecbase import MacsecBase


class Macsec(DeviceApi, MacsecBase):
    def __init__(self, device_input):
        super(Macsec, self).__init__(device_input)

    def enable_ca_port(self, arg_dictionary, **kwargs):
        uuid = "233d8332-a5cf-4fa2-837c-410dd31e62f2"
        cmd = "configure macsec connectivity-association {0} ports {1} enable".format(arg_dictionary['ca_name'],
                                                                                      arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_ca_port(self, arg_dictionary, **kwargs):
        uuid = "cd3c1607-b1dc-4495-832f-a2f20b2977c7"
        cmd = "configure macsec connectivity-association {0} ports {1} disable".format(arg_dictionary['ca_name'],
                                                                                       arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def create_ca(self, arg_dictionary, **kwargs):
        uuid = "a04e7d1e-b39d-4cad-a245-60db991ba1b7"
        cmd = "create macsec connectivity-association {0} pre-shared-key ckn {1} cak {2}".format(arg_dictionary['ca_name'],
                                                                                                 arg_dictionary['key_name'],
                                                                                                 arg_dictionary['key'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def create_ca_encrypted(self, arg_dictionary, **kwargs):
        uuid = "a0ca20f4-aea0-49a2-a8fd-00a39e56ad49"
        cmd = "create macsec connectivity-association {0} pre-shared-key ckn {1} cak encrypted {2}".format(arg_dictionary['ca_name'],
                                                                                                           arg_dictionary['key_name'],
                                                                                                           arg_dictionary['key'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_cipher_suite_128(self, arg_dictionary, **kwargs):
        uuid = "bbd3da5f-92d3-4afe-8b25-607855ae6440"
        cmd = "configure macsec cipher-suite gcm-aes-128 ports {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_cipher_suite_256(self, arg_dictionary, **kwargs):
        uuid = "a7b9178d-d85a-4693-b99f-5a6b1f8d3782"
        cmd = "configure macsec cipher-suite gcm-aes-256 ports {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_confidentiality_offset_0(self, arg_dictionary, **kwargs):
        uuid = "5304635f-dfcf-41a7-b3db-f1d493fd572b"
        cmd = "configure macsec confidentiality-offset 0 ports {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_confidentiality_offset_30(self, arg_dictionary, **kwargs):
        uuid = "e9182628-08d6-4e6a-820f-70858c15b917"
        cmd = "configure macsec confidentiality-offset 30 ports {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_confidentiality_offset_50(self, arg_dictionary, **kwargs):
        uuid = "34499cc9-cf80-446a-88fd-083d70d7b8ab"
        cmd = "configure macsec confidentiality-offset 50 ports {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_hw_mode_half_duplex_mode(self, arg_dictionary, **kwargs):
        uuid = "7b9b0748-794e-441b-9c97-886179b8f54e"
        cmd = "configure macsec hw-mode half-duplex-mode ports {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_hw_mode_macsec_mode(self, arg_dictionary, **kwargs):
        uuid = "749d5636-1cdd-4d82-abaf-58a3968aa4e6"
        cmd = "configure macsec hw-mode macsec-mode ports {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_include_sci_enable(self, arg_dictionary, **kwargs):
        uuid = "4475d65a-3621-40d9-bb60-c2157f344669"
        cmd = "configure macsec include-sci enable ports {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_include_sci_disable(self, arg_dictionary, **kwargs):
        uuid = "c1d00df9-5e3b-4fef-b8c7-df599f5b3c7d"
        cmd = "configure macsec include-sci disable ports {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_initialize_ports(self, arg_dictionary, **kwargs):
        uuid = "3676756d-e07b-4357-b6f9-c5cbb106a208"
        cmd = "configure macsec initialize ports {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_mka_actor_priority(self, arg_dictionary, **kwargs):
        uuid = "3db645df-a1a1-40ab-bb40-6549a7f6c324"
        cmd = "configure macsec mka actor-priority {0} ports {1}".format(arg_dictionary['priority'],
                                                                         arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_replay_protect(self, arg_dictionary, **kwargs):
        uuid = "b63cf63e-1884-4b26-a7b0-ddcf0626f629"
        cmd = "configure macsec replay-protect {0} ports {1}".format(arg_dictionary['window_size'],
                                                                     arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_replay_protect_disable(self, arg_dictionary, **kwargs):
        uuid = "0a11905d-a90b-4604-ab23-7bdcd0a7aabd"
        cmd = "configure macsec replay-protect disable ports {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_counters_all(self, arg_dictionary, **kwargs):
        uuid = "ba7a6602-7e7d-4f3f-801a-1062113d739e"
        cmd = "clear macsec counters"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_counters_on_port(self, arg_dictionary, **kwargs):
        uuid = "e6e8de1d-81b2-4c87-8679-a69b4f4dc48e"
        cmd = "clear macsec counters ports {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def delete_ca(self, arg_dictionary, **kwargs):
        uuid = "ae4bf96e-121f-4c57-a716-a7eede466818"
        cmd = "delete macsec connectivity-association {0}".format(arg_dictionary['ca_name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show(self, arg_dictionary, **kwargs):
        uuid = "74b4a151-0750-4a8a-a517-2d38020705c9"
        cmd = "show macsec"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port(self, arg_dictionary, **kwargs):
        uuid = "37d44773-2324-41d4-8f0b-f9598032bb1f"
        cmd = "show macsec ports {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port_configuration(self, arg_dictionary, **kwargs):
        uuid = "226173dd-ee7b-400a-bef1-b0596a0e1f43"
        cmd = "show macsec ports {0} configuration".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port_detail(self, arg_dictionary, **kwargs):
        uuid = "b71624f5-cf44-4ada-b5fb-30d9db0fb416"
        cmd = "show macsec ports {0} detail".format(arg_dictionary['port'])
        prompt = "userPrompt"

        self.device.error_checker.add_error_to_ignore_list(*["SecY Hardware Error Count"])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port_counters(self, arg_dictionary, **kwargs):
        uuid = "84da5599-b18b-408e-9e94-d6851a2f5989"
        cmd = "show macsec ports {0} detail | begin \"SecY Interface Statistics\"".format(arg_dictionary['port'])
        prompt = "userPrompt"

        self.device.error_checker.add_error_to_ignore_list(*["SecY Hardware Error Count"])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port_all(self, arg_dictionary, **kwargs):
        uuid = "98724d26-bf74-4ac8-a968-2464089fe8c9"
        cmd = "show macsec ports all"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port_all_config(self, arg_dictionary, **kwargs):
        uuid = "2da424eb-8975-4468-b929-52aa754c9948"
        cmd = "show macsec ports all configuration"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port_all_detail(self, arg_dictionary, **kwargs):
        uuid = "a81825d5-5fff-48ca-9e60-2ba8d00b3ee7"
        cmd = "show macsec ports all detail"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_connectivity_association(self, arg_dictionary, **kwargs):
        uuid = "d9de53c4-5be3-43cd-b8d4-33052a211c74"
        cmd = "show macsec connectivity-association {0}".format(arg_dictionary['ca_name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_connectivity_association_all(self, arg_dictionary, **kwargs):
        uuid = "3a2df81f-d76c-49e1-9d88-d2256b6b26cf"
        cmd = "show macsec connectivity-association"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
