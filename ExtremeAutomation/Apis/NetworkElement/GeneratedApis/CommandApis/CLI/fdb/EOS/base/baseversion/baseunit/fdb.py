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
        cmd = "set mac agetime {0}".format(arg_dictionary['agetime'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_agetime_min(self, arg_dictionary, **kwargs):
        uuid = "b19aed04-3660-4ec2-a109-b0f1c570666e"
        cmd = "set mac agetime {0}".format(arg_dictionary['agetime'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_agetime(self, arg_dictionary, **kwargs):
        uuid = "66f14371-91fd-4033-8f27-ff150c64064f"
        cmd = "clear mac agetime"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_unicast_as_multicast(self, arg_dictionary, **kwargs):
        uuid = "47b3a54d-ba99-476d-8c5d-b49a30be417b"
        cmd = "set mac unicast-as-multicast enable"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_unicast_as_multicast(self, arg_dictionary, **kwargs):
        uuid = "c337fe5a-94e8-4bf2-8936-97395a846603"
        cmd = "set mac unicast-as-multicast disable"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_all(self, arg_dictionary, **kwargs):
        uuid = "254dbcd8-83ed-4264-8cc8-2a3f9861e262"
        cmd = "clear mac all"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_all_vlan(self, arg_dictionary, **kwargs):
        uuid = "102b660f-4c7f-4da0-9428-df884f789080"
        cmd = "clear mac fid {0}".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_all_port(self, arg_dictionary, **kwargs):
        uuid = "f8a712ed-edd6-402f-8f72-233e9db3b554"
        cmd = "clear mac port-string {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def create_entry(self, arg_dictionary, **kwargs):
        uuid = "ab3fbbd4-53b0-4e10-811e-a1e5a6177ffe"
        cmd = "set mac unicast {0} {1} {2}".format(self.str_utils.normalize_mac(arg_dictionary['mac']),
                                                   arg_dictionary['vlan'],
                                                   arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def create_multicast_entry(self, arg_dictionary, **kwargs):
        uuid = "fe3435c2-b44b-45fa-9ceb-ffc249c6b962"
        cmd = "set mac multicast {0} {1} {2}".format(self.str_utils.normalize_mac(arg_dictionary['mac']),
                                                     arg_dictionary['vlan'],
                                                     self.api_utils.eos_fdb_portlist(arg_dictionary['port']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def delete_entry(self, arg_dictionary, **kwargs):
        uuid = "a7ffbe28-bdad-435e-8cc1-a8cd70494d91"
        cmd = "clear mac address {0}".format(self.str_utils.normalize_mac(arg_dictionary['mac']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_agetime(self, arg_dictionary, **kwargs):
        uuid = "1ed8be08-313f-4598-b926-59ef7dccdfd3"
        cmd = "show mac agetime"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_all_entries(self, arg_dictionary, **kwargs):
        uuid = "d4a7b29a-1b98-4d7f-9ae5-854280b9839a"
        cmd = "show mac"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_entry(self, arg_dictionary, **kwargs):
        uuid = "ccaf6147-a3a7-4abc-8363-e820e491b0a9"
        cmd = "show mac address {0}".format(arg_dictionary['mac'])
        prompt = "userPrompt"

        self.device.error_checker.add_error_to_ignore_list(*["No entries found"])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
