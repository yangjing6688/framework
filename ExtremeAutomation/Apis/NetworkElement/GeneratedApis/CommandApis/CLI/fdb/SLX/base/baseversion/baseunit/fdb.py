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
        cmd = "mac-address-table aging-time {0}".format(arg_dictionary['agetime'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_agetime_conversational(self, arg_dictionary, **kwargs):
        uuid = "a492eead-986d-4e65-aa59-412dcc2f963e"
        cmd = "mac-address-table aging-time conversational {0}".format(arg_dictionary['agetime'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_agetime(self, arg_dictionary, **kwargs):
        uuid = "66f14371-91fd-4033-8f27-ff150c64064f"
        cmd = "no mac-address-table aging-time"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_agetime_conversational(self, arg_dictionary, **kwargs):
        uuid = "efbe4303-7299-4609-933e-e3cba7f5eff2"
        cmd = "no mac-address-table aging-time conversational"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_fdb_learn_mode_conversational(self, arg_dictionary, **kwargs):
        uuid = "0051f0b5-6ee6-4192-be05-c9f983a7921c"
        cmd = "mac-address-table learning-mode conversational"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_fdb_learn_mode(self, arg_dictionary, **kwargs):
        uuid = "d8621faf-21ea-4ad5-9920-1258bdcf1701"
        cmd = "no mac-address-table learning-mode"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_all(self, arg_dictionary, **kwargs):
        uuid = "254dbcd8-83ed-4264-8cc8-2a3f9861e262"
        cmd = "clear mac-address-table dynamic"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_all_vlan(self, arg_dictionary, **kwargs):
        uuid = "102b660f-4c7f-4da0-9428-df884f789080"
        cmd = "clear mac-address-table dynamic vlan {0}".format(arg_dictionary['vlan'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_all_port(self, arg_dictionary, **kwargs):
        uuid = "f8a712ed-edd6-402f-8f72-233e9db3b554"
        cmd = "clear mac-address-table dynamic interface {0}".format(arg_dictionary['port'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_all_linecard(self, arg_dictionary, **kwargs):
        uuid = "8858fcda-16c3-4834-9354-166ec6639f2c"
        cmd = "clear mac-address-table dynamic linecard {0}".format(arg_dictionary['linecard'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_all_linecard_rbid(self, arg_dictionary, **kwargs):
        uuid = "759183ec-93e6-428f-930f-ee5c6492a562"
        cmd = "clear mac-address-table dynamic linecard {0} rbridge-id {1}".format(arg_dictionary['linecard'],
                                                                                   arg_dictionary['rbid'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def create_entry(self, arg_dictionary, **kwargs):
        uuid = "ab3fbbd4-53b0-4e10-811e-a1e5a6177ffe"
        cmd = "mac-address-table static {0} forward ethernet {1} vlan {2}".format(self.str_utils.normalize_mac(arg_dictionary['mac']),
                                                                                  arg_dictionary['port'],
                                                                                  arg_dictionary['vlan'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def delete_entry(self, arg_dictionary, **kwargs):
        uuid = "a7ffbe28-bdad-435e-8cc1-a8cd70494d91"
        cmd = "clear mac-address-table dynamic address {0}".format(self.str_utils.normalize_mac(arg_dictionary['mac']))
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_learning(self, arg_dictionary, **kwargs):
        uuid = "1b7c9c68-7fb4-4ac9-bf13-672a4ccafc27"
        cmd = "no mac-learning disable"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_learning_vlan(self, arg_dictionary, **kwargs):
        uuid = "e0863cc7-fd58-463e-9152-c041ab212648"
        cmd = "mac-learning disable vlan remove {0}".format(arg_dictionary['vlan'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_learning(self, arg_dictionary, **kwargs):
        uuid = "4be32eb9-a507-4cbb-89f3-a1161120e7e5"
        cmd = "mac-learning disable"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_learning_vlan(self, arg_dictionary, **kwargs):
        uuid = "7a410a50-052d-4560-bd7d-974fb0e45cfb"
        cmd = "mac-learning disable vlan add {0}".format(arg_dictionary['vlan'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
