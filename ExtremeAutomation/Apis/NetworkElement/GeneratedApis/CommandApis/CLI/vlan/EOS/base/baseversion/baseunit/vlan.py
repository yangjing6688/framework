"""
All vlan supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.vlan.base.vlanbase import VlanBase


class Vlan(DeviceApi, VlanBase):
    def __init__(self, device_input):
        super(Vlan, self).__init__(device_input)

    def create_vlan(self, arg_dictionary, **kwargs):
        uuid = "2e07dc6a-2f52-4bdd-b814-6a3fd6afc666"
        cmd = "set vlan create {0}".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def delete_vlan(self, arg_dictionary, **kwargs):
        uuid = "eaccd886-b51c-409d-9daa-703133a964e5"
        cmd = "clear vlan {0}".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def create_vman(self, arg_dictionary, **kwargs):
        uuid = "88e93a18-aa67-42a4-920c-03d4b57d43a5"
        cmd = "set vlan create {0}".format(arg_dictionary['vman'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def delete_vman(self, arg_dictionary, **kwargs):
        uuid = "c1034622-3df6-43ac-bfa9-4cd8a7d15073"
        cmd = "clear vlan {0}".format(arg_dictionary['vman'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_vlan(self, arg_dictionary, **kwargs):
        uuid = "8f1d1665-b71b-45ee-bcb3-062106d5c14e"
        cmd = "set vlan enable {0}".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_vlan(self, arg_dictionary, **kwargs):
        uuid = "0e76a4c3-41d3-4405-a5c2-040c75793e40"
        cmd = "set vlan disable {0}".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_dynamic_egress(self, arg_dictionary, **kwargs):
        uuid = "25943c13-2b66-42fb-9a65-21c384ecdd57"
        cmd = "set vlan dynamicegress {0} enable".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_dynamic_egress(self, arg_dictionary, **kwargs):
        uuid = "688ba73b-d326-4b4e-8dea-ebd4fb7a260f"
        cmd = "set vlan dynamicegress {0} disable".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_egress_untagged(self, arg_dictionary, **kwargs):
        uuid = "1455236d-3899-476e-a333-93fcff7ed6ad"
        cmd = "set vlan egress {0} {1} untagged".format(arg_dictionary['vlan'],
                                                        arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_egress_tagged(self, arg_dictionary, **kwargs):
        uuid = "8fb45945-51d5-43b8-b469-84d4cfc3f546"
        cmd = "set vlan egress {0} {1} tagged".format(arg_dictionary['vlan'],
                                                      arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_egress_forbidden(self, arg_dictionary, **kwargs):
        uuid = "b75aade1-939c-4c43-b73d-c14250537fed"
        cmd = "set vlan egress {0} {1} forbidden".format(arg_dictionary['vlan'],
                                                         arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_egress(self, arg_dictionary, **kwargs):
        uuid = "aaca0f2c-01a7-48d1-8b68-f113d9711a23"
        cmd = "clear vlan egress {0} {1}".format(arg_dictionary['vlan'],
                                                 arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_egress_type(self, arg_dictionary, **kwargs):
        uuid = "51de2778-983c-462e-b205-29d1b6454bc6"
        cmd = "clear vlan egress {0} {1} {2}".format(arg_dictionary['vlan'],
                                                     arg_dictionary['port'],
                                                     arg_dictionary['egress_type'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_description(self, arg_dictionary, **kwargs):
        uuid = "5e31f606-0a42-473b-906e-651b1fdabebc"
        cmd = "set vlan name {0} \"{1}\"".format(arg_dictionary['vlan'],
                                                 arg_dictionary['name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_description(self, arg_dictionary, **kwargs):
        uuid = "c5b9a551-a137-41af-aa7b-c283c9f9f12e"
        cmd = "clear vlan name {0}".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_name(self, arg_dictionary, **kwargs):
        uuid = "b5132db1-ed57-4b19-a129-13bf3cf6efbe"
        cmd = "set vlan name {0} \"{1}\"".format(arg_dictionary['vlan'],
                                                 arg_dictionary['name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_name(self, arg_dictionary, **kwargs):
        uuid = "a435b6bd-7aec-4705-81b0-af0bc59ffaeb"
        cmd = "clear vlan name {0}".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_pvid(self, arg_dictionary, **kwargs):
        uuid = "b4477fa8-5f9e-449e-bc9f-c88a87add7b6"
        cmd = "set port vlan {0} {1} {2}".format(arg_dictionary['port'],
                                                 arg_dictionary['vlan'],
                                                 arg_dictionary['modify_egress'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_pvid(self, arg_dictionary, **kwargs):
        uuid = "04479df7-6ad7-4db6-8410-9bda5e8458d9"
        cmd = "clear port vlan {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_all_info(self, arg_dictionary, **kwargs):
        uuid = "665c60ed-ab31-4ccd-9b85-7946db3c01a3"
        cmd = "show vlan"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_info(self, arg_dictionary, **kwargs):
        uuid = "62cb48f8-848b-4604-a67b-5e135a96d45a"
        cmd = "show vlan {0}".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_name(self, arg_dictionary, **kwargs):
        uuid = "48cf27a1-71fd-4212-85a3-12db4d2f899d"
        cmd = "show vlan {0}".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_description(self, arg_dictionary, **kwargs):
        uuid = "eecd4686-9ec0-483b-99ca-2d7c45bd5036"
        cmd = "show vlan {0}".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_status(self, arg_dictionary, **kwargs):
        uuid = "d487d4f0-befa-4034-9882-80fa3f609e21"
        cmd = "show vlan {0}".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_pvid(self, arg_dictionary, **kwargs):
        uuid = "49369c19-a5c0-4518-bd93-317d7ff99061"
        cmd = "show port vlan {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_static(self, arg_dictionary, **kwargs):
        uuid = "61b9b7fc-add0-405d-ac77-30694a708e62"
        cmd = "show vlan static {0}".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port_egress(self, arg_dictionary, **kwargs):
        uuid = "5129a33b-95c8-4b61-a2b9-f18d94db9f53"
        cmd = "show port egress {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_all_vman_info(self, arg_dictionary, **kwargs):
        uuid = "970b28f4-48a1-44ca-8fb6-db655fd6e5dc"
        cmd = "show vlan"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
