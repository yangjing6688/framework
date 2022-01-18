"""
All hostservices supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.hostservices.base.hostservicesbase import \
    HostservicesBase


class Hostservices(DeviceApi, HostservicesBase):
    def __init__(self, device_input):
        super(Hostservices, self).__init__(device_input)

    def enable_sys_force_topology_ip_flag(self, arg_dictionary, **kwargs):
        uuid = "44ae2093-7a32-4200-9f6b-c76d9048a8a8"
        cmd = "sys force-topology-ip-flag"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_sys_force_topology_ip_flag(self, arg_dictionary, **kwargs):
        uuid = "0ed942d2-10cd-489d-804e-4e0ff39a37e7"
        cmd = "no sys force-topology-ip-flag"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_sys_clipid_topology_ip(self, arg_dictionary, **kwargs):
        uuid = "7dafa48c-20c4-4179-9a54-b6f6cc54e735"
        cmd = "sys clipId-topology-ip {0}".format(arg_dictionary['clip_id'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_sys_clipid_topology_ip(self, arg_dictionary, **kwargs):
        uuid = "ee66147e-6a71-43b9-b73a-4cd7defa0dc7"
        cmd = "no sys clipId-topology-ip"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_sys_setting(self, arg_dictionary, **kwargs):
        uuid = "f60ea537-ad29-4c8a-96bf-bfaa679d2433"
        cmd = "show sys setting"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_autotopology_nmm_table(self, arg_dictionary, **kwargs):
        uuid = "99b9efa8-9d29-4288-80d3-d56a2cf16193"
        cmd = "show autotopology nmm-table"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
