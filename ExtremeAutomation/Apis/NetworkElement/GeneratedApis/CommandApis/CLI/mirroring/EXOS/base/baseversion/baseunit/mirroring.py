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
        cmd = "create mirror {0} to port {1}||configure mirror {2} add port {3} ingress-and-egress".format(arg_dictionary['name'],
                                                                                                           arg_dictionary['dst_port'],
                                                                                                           arg_dictionary['name'],
                                                                                                           arg_dictionary['src_port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def create_ingress(self, arg_dictionary, **kwargs):
        uuid = "9c4fca35-e2b6-4795-9575-3dd9ff15beef"
        cmd = "create mirror {0} to port {1}||configure mirror {2} add port {3} ingress".format(arg_dictionary['name'],
                                                                                                arg_dictionary['dst_port'],
                                                                                                arg_dictionary['name'],
                                                                                                arg_dictionary['src_port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def create_egress(self, arg_dictionary, **kwargs):
        uuid = "e599fd8a-8124-4614-9442-34b1ed04b425"
        cmd = "create mirror {0} to port {1}||configure mirror {2} add port {3} egress".format(arg_dictionary['name'],
                                                                                               arg_dictionary['dst_port'],
                                                                                               arg_dictionary['name'],
                                                                                               arg_dictionary['src_port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def delete_port_mirror(self, arg_dictionary, **kwargs):
        uuid = "8318eb28-5773-4485-a296-4e58fd750979"
        cmd = "delete mirror {0}".format(arg_dictionary['name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_port(self, arg_dictionary, **kwargs):
        uuid = "11727cab-c503-416e-bb6c-bbdc34b8df48"
        cmd = "enable mirror {0}".format(arg_dictionary['name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_port(self, arg_dictionary, **kwargs):
        uuid = "76c15bfb-dbac-4f97-88e2-303b7e1400e7"
        cmd = "disable mirror {0}".format(arg_dictionary['name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def create_remote_both(self, arg_dictionary, **kwargs):
        uuid = "86f6074b-6927-4104-86bb-8c0f6a32ae7b"
        cmd = "create mirror {0} to remote-ip {1}".format(arg_dictionary['name'],
                                                          arg_dictionary['ip'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def create_portlist(self, arg_dictionary, **kwargs):
        uuid = "67f7a017-2424-4570-9fb4-2072b7a3cae3"
        cmd = "create mirror {0} to port-list {1}".format(arg_dictionary['name'],
                                                          arg_dictionary['port_list'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_source_port_both(self, arg_dictionary, **kwargs):
        uuid = "36706790-6717-4eba-bff7-ab50276d95fb"
        cmd = "configure mirror {0} add port {1} ingress-and-egress".format(arg_dictionary['name'],
                                                                            arg_dictionary['src_port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_source_port_vlan(self, arg_dictionary, **kwargs):
        uuid = "4c7b5043-1eb9-46dc-aefe-f3546e24a662"
        cmd = "configure mirror {0} add port {1} vlan {2}".format(arg_dictionary['name'],
                                                                  arg_dictionary['src_port'],
                                                                  arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_source_port_ingress(self, arg_dictionary, **kwargs):
        uuid = "056f8301-40d8-4252-b9a9-843000e960f4"
        cmd = "configure mirror {0} add port {1} ingress".format(arg_dictionary['name'],
                                                                 arg_dictionary['src_port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_source_port_egress(self, arg_dictionary, **kwargs):
        uuid = "77e707e2-1dc1-4a94-afd7-dc289bdaafa1"
        cmd = "configure mirror {0} add port {1} egress".format(arg_dictionary['name'],
                                                                arg_dictionary['src_port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_source_port(self, arg_dictionary, **kwargs):
        uuid = "8dd4f447-ca67-4415-857f-35d5bb131055"
        cmd = "configure mirror {0} delete port {1}".format(arg_dictionary['name'],
                                                            arg_dictionary['src_port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_remote_ping_check(self, arg_dictionary, **kwargs):
        uuid = "f2319f16-18ea-4819-bddc-60d9501568b6"
        cmd = "configure mirror {0} ping-check on from {1} to remote-ip {2}".format(arg_dictionary['name'],
                                                                                    arg_dictionary['src_ip'],
                                                                                    arg_dictionary['dst_ip'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_remote_ping_check(self, arg_dictionary, **kwargs):
        uuid = "04077770-3b9f-4abf-88e0-2b7a2124a5dd"
        cmd = "configure mirror {0} ping-check off from {1} to remote-ip {2}".format(arg_dictionary['name'],
                                                                                     arg_dictionary['src_ip'],
                                                                                     arg_dictionary['dst_ip'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port_mirror(self, arg_dictionary, **kwargs):
        uuid = "2eea68a2-d875-4922-ba4e-190f13a1fc14"
        cmd = "show mirror {0}".format(arg_dictionary['name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port_mirror_all(self, arg_dictionary, **kwargs):
        uuid = "32dfd4e2-3f84-4991-be7b-cc91db8fbc3d"
        cmd = "show mirror"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
