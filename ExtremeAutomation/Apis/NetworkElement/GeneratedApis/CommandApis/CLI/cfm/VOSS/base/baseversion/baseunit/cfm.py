"""
All cfm supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.cfm.base.cfmbase import CfmBase


class Cfm(DeviceApi, CfmBase):
    def __init__(self, device_input):
        super(Cfm, self).__init__(device_input)

    def enable_spbm(self, arg_dictionary, **kwargs):
        uuid = "8f60226a-aad9-4e26-82ce-3d38ef7f5114"
        cmd = "cfm spbm enable"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_spbm(self, arg_dictionary, **kwargs):
        uuid = "59e45f05-83fe-4fe1-9ec9-13bf8c8c86b1"
        cmd = "no cfm spbm enable"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_maintenance_endpoint(self, arg_dictionary, **kwargs):
        uuid = "456725b9-99ed-4f6e-a09b-f8d95f7516fe"
        cmd = "cfm maintenance-endpoint {0} {1} {2} enable".format(arg_dictionary['md_name'],
                                                                   arg_dictionary['ma_name'],
                                                                   arg_dictionary['mep_id'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_maintenance_endpoint(self, arg_dictionary, **kwargs):
        uuid = "470e0bea-8107-4a05-9809-7b9f0cf1dcd4"
        cmd = "no cfm maintenance-endpoint {0} {1} {2} enable".format(arg_dictionary['md_name'],
                                                                      arg_dictionary['ma_name'],
                                                                      arg_dictionary['mep_id'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_spbm_mepid(self, arg_dictionary, **kwargs):
        uuid = "c0b7c2f3-d0eb-4cba-9343-572403bd1418"
        cmd = "cfm spbm mepid {0}".format(arg_dictionary['mep_id'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_spbm_level(self, arg_dictionary, **kwargs):
        uuid = "77e98ce5-147f-4ef3-a17e-344d6d5f109d"
        cmd = "cfm spbm level {0}".format(arg_dictionary['spbm_level'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_maintenance_domain(self, arg_dictionary, **kwargs):
        uuid = "4c5bcd94-1569-4c2c-a7e8-f3e81994c441"
        cmd = "cfm maintenance-domain {0} index {1} maintenance-level {2}".format(arg_dictionary['md_name'],
                                                                                  arg_dictionary['md_index'],
                                                                                  arg_dictionary['md_level'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_maintenance_domain_name(self, arg_dictionary, **kwargs):
        uuid = "a3c647d2-6ab7-495f-b746-9168baec8557"
        cmd = "cfm maintenance-domain {0}".format(arg_dictionary['md_name'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_maintenance_domain_index(self, arg_dictionary, **kwargs):
        uuid = "897ddb76-a82b-4bf9-b272-c3760286dd68"
        cmd = "cfm maintenance-domain {0} index {1}".format(arg_dictionary['md_name'],
                                                            arg_dictionary['md_index'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_maintenance_domain_level(self, arg_dictionary, **kwargs):
        uuid = "d17b5590-19b5-401e-81e9-cb83a5759828"
        cmd = "cfm maintenance-domain {0} level {1}".format(arg_dictionary['md_name'],
                                                            arg_dictionary['md_level'])
        prompt = "routerConfigPrompt"

        self.device.error_checker.add_error_to_ignore_list(*["Error"])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_spbm_mepid(self, arg_dictionary, **kwargs):
        uuid = "8b63fbe9-b7ac-475f-b6fd-eb3a97d17be8"
        cmd = "cfm spbm mepid 1"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_spbm_level(self, arg_dictionary, **kwargs):
        uuid = "3025081e-cc13-4f6c-9c66-525d310a9447"
        cmd = "cfm spbm level 4"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_maintenance_domain(self, arg_dictionary, **kwargs):
        uuid = "1c620dbd-f86b-4928-9d60-967d1f2e3660"
        cmd = "no cfm maintenance-domain {0}".format(arg_dictionary['md_name'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_cmac(self, arg_dictionary, **kwargs):
        uuid = "5173ced0-99dc-495f-acdf-20472e39d547"
        cmd = "show cfm cmac"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_spbm(self, arg_dictionary, **kwargs):
        uuid = "c8cfba3f-68dc-48b0-9cf0-36abedb1c93a"
        cmd = "show cfm spbm"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_maintenance_endpoint(self, arg_dictionary, **kwargs):
        uuid = "3bc56ed5-76fc-4683-b72c-2c5862a502e2"
        cmd = "show cfm maintenance-endpoint"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_maintenance_association(self, arg_dictionary, **kwargs):
        uuid = "6037e58d-02b2-4e93-ae76-32e28d89845a"
        cmd = "show cfm maintenance-association"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_maintenance_domain(self, arg_dictionary, **kwargs):
        uuid = "2927d7eb-8576-4c8b-9af5-015a2a39fc2f"
        cmd = "show cfm maintenance-domain"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_association_name(self, arg_dictionary, **kwargs):
        uuid = "672c0a91-5e52-4a98-a48c-0465860acf50"
        cmd = "show cfm maintenance-association"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_domain_name(self, arg_dictionary, **kwargs):
        uuid = "24ec9c2f-94b7-4cea-80ec-6c04250cf980"
        cmd = "show cfm maintenance-domain"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
