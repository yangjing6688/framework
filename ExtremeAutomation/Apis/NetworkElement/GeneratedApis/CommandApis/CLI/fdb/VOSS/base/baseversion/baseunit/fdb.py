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

    def clear_agetime(self, arg_dictionary, **kwargs):
        uuid = "66f14371-91fd-4033-8f27-ff150c64064f"
        cmd = "default mac-address-table aging-time"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_all_vlan(self, arg_dictionary, **kwargs):
        uuid = "102b660f-4c7f-4da0-9428-df884f789080"
        cmd = "vlan mac-address-entry {0} flush".format(arg_dictionary['vlan'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_all_port(self, arg_dictionary, **kwargs):
        uuid = "f8a712ed-edd6-402f-8f72-233e9db3b554"
        cmd = "action flushMacFdb"
        prompt = "intfPrompt"
        prompt_args = "GigabitEthernet {0}".format(arg_dictionary['port'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def create_entry(self, arg_dictionary, **kwargs):
        uuid = "ab3fbbd4-53b0-4e10-811e-a1e5a6177ffe"
        cmd = "vlan mac-address-static {0} {1} {2}".format(arg_dictionary['vlan'],
                                                           self.str_utils.normalize_mac(arg_dictionary['mac']),
                                                           arg_dictionary['port'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def delete_entry(self, arg_dictionary, **kwargs):
        uuid = "a7ffbe28-bdad-435e-8cc1-a8cd70494d91"
        cmd = "no vlan mac-address-static {0} {1}".format(arg_dictionary['vlan'],
                                                          self.str_utils.normalize_mac(arg_dictionary['mac']))
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_mac_port(self, arg_dictionary, **kwargs):
        uuid = "6e6956b8-7388-499d-9ad4-011889173bab"
        cmd = "clear mac-address-table port {0} address {1}".format(arg_dictionary['port'],
                                                                    self.str_utils.normalize_mac(arg_dictionary['mac']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_mac_port_vlan(self, arg_dictionary, **kwargs):
        uuid = "5a282653-5135-4c64-bce5-872b907725c0"
        cmd = "clear mac-address-table port {0} address {1} interface vlan {2}".format(arg_dictionary['port'],
                                                                                       self.str_utils.normalize_mac(arg_dictionary['mac']),
                                                                                       arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_dynamic_entry(self, arg_dictionary, **kwargs):
        uuid = "8fa25d83-1e10-4208-8bb4-681351ac937e"
        cmd = "clear mac-address-table dynamic {0} {1}".format(self.str_utils.normalize_mac(arg_dictionary['mac']),
                                                               arg_dictionary['vlan'])
        prompt = "intfPrompt"
        prompt_args = "GigabitEthernet {0}".format(arg_dictionary['port'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def show_agetime(self, arg_dictionary, **kwargs):
        uuid = "1ed8be08-313f-4598-b926-59ef7dccdfd3"
        cmd = "show mac-address-table aging-time"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_all_entries(self, arg_dictionary, **kwargs):
        uuid = "d4a7b29a-1b98-4d7f-9ae5-854280b9839a"
        cmd = "show interfaces gigabitethernet fdb-entry"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_entry(self, arg_dictionary, **kwargs):
        uuid = "ccaf6147-a3a7-4abc-8363-e820e491b0a9"
        cmd = "show vlan mac-address-entry mac {0}".format(arg_dictionary['mac'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_entries_vlan(self, arg_dictionary, **kwargs):
        uuid = "4ac951b9-8be2-4cc4-af98-76d7a6fdca2e"
        cmd = "show vlan mac-address-entry {0}".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_entries_port(self, arg_dictionary, **kwargs):
        uuid = "c5eb792d-6d07-4bae-9e10-7f5b6df91522"
        cmd = "show interfaces gigabitethernet fdb-entry {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
