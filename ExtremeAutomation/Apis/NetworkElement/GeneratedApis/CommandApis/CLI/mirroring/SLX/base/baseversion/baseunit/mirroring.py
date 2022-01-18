"""
All mirroring supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.mirroring.base.mirroringbase import \
    MirroringBase


class Mirroring(DeviceApi, MirroringBase):
    def __init__(self, device_input):
        super(Mirroring, self).__init__(device_input)

    def create_both(self, arg_dictionary, **kwargs):
        uuid = "35ff8622-050d-45d8-bdcd-cb2d0f1d0b00"
        cmd = "monitor session {0}|| source ethernet {1} destination ethernet {2} direction both".format(arg_dictionary['name'],
                                                                                                         arg_dictionary['src_port'],
                                                                                                         arg_dictionary['dst_port'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def create_ingress(self, arg_dictionary, **kwargs):
        uuid = "9c4fca35-e2b6-4795-9575-3dd9ff15beef"
        cmd = "monitor session {0}|| source ethernet {1} destination ethernet {2} direction rx".format(arg_dictionary['name'],
                                                                                                       arg_dictionary['src_port'],
                                                                                                       arg_dictionary['dst_port'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def create_egress(self, arg_dictionary, **kwargs):
        uuid = "e599fd8a-8124-4614-9442-34b1ed04b425"
        cmd = "monitor session {0}|| source ethernet {1} destination ethernet {2} direction tx".format(arg_dictionary['name'],
                                                                                                       arg_dictionary['src_port'],
                                                                                                       arg_dictionary['dst_port'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def delete_port_mirror(self, arg_dictionary, **kwargs):
        uuid = "8318eb28-5773-4485-a296-4e58fd750979"
        cmd = "no monitor session {0}".format(arg_dictionary['name'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_description(self, arg_dictionary, **kwargs):
        uuid = "a85983a3-446c-4086-86c1-56881347b937"
        cmd = "monitor session {0}||description {1}".format(arg_dictionary['name'],
                                                            arg_dictionary['description'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port_mirror(self, arg_dictionary, **kwargs):
        uuid = "2eea68a2-d875-4922-ba4e-190f13a1fc14"
        cmd = "show monitor session {0}".format(arg_dictionary['name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
