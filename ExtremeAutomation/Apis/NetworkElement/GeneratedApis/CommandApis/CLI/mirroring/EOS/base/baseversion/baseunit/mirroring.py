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
        cmd = "set port mirroring create {0} {1}".format(arg_dictionary['src_port'],
                                                         arg_dictionary['dst_port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def create_ingress(self, arg_dictionary, **kwargs):
        uuid = "9c4fca35-e2b6-4795-9575-3dd9ff15beef"
        cmd = "set port mirroring create {0} {1} rx".format(arg_dictionary['src_port'],
                                                            arg_dictionary['dst_port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def create_egress(self, arg_dictionary, **kwargs):
        uuid = "e599fd8a-8124-4614-9442-34b1ed04b425"
        cmd = "set port mirroring create {0} {1} tx".format(arg_dictionary['src_port'],
                                                            arg_dictionary['dst_port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def delete_port_mirror(self, arg_dictionary, **kwargs):
        uuid = "8318eb28-5773-4485-a296-4e58fd750979"
        cmd = "clear port mirroring {0} {1}".format(arg_dictionary['src_port'],
                                                    arg_dictionary['dst_port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_port(self, arg_dictionary, **kwargs):
        uuid = "11727cab-c503-416e-bb6c-bbdc34b8df48"
        cmd = "set port mirroring enable {0} {1}".format(arg_dictionary['src_port'],
                                                         arg_dictionary['dst_port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_port(self, arg_dictionary, **kwargs):
        uuid = "76c15bfb-dbac-4f97-88e2-303b7e1400e7"
        cmd = "set port mirroring disable {0} {1}".format(arg_dictionary['src_port'],
                                                          arg_dictionary['dst_port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port_mirror(self, arg_dictionary, **kwargs):
        uuid = "2eea68a2-d875-4922-ba4e-190f13a1fc14"
        cmd = "show port mirroring"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port_mirror_all(self, arg_dictionary, **kwargs):
        uuid = "32dfd4e2-3f84-4991-be7b-cc91db8fbc3d"
        cmd = "show port mirroring"
        prompt = "userPrompt"

        self.device.error_checker.add_error_to_ignore_list(*["No Port"])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
