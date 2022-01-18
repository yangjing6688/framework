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
        cmd = "create vlan {0}".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def delete_vlan(self, arg_dictionary, **kwargs):
        uuid = "eaccd886-b51c-409d-9daa-703133a964e5"
        cmd = "delete vlan {0}".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        self.device.error_checker.add_error_to_ignore_list(*["Error: The specified VLAN"])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def create_vman(self, arg_dictionary, **kwargs):
        uuid = "88e93a18-aa67-42a4-920c-03d4b57d43a5"
        cmd = "create vman {0}".format(arg_dictionary['vman'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def delete_vman(self, arg_dictionary, **kwargs):
        uuid = "c1034622-3df6-43ac-bfa9-4cd8a7d15073"
        cmd = "delete vman {0}".format(arg_dictionary['vman'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_vlan(self, arg_dictionary, **kwargs):
        uuid = "8f1d1665-b71b-45ee-bcb3-062106d5c14e"
        cmd = "enable vlan {0}".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_vlan(self, arg_dictionary, **kwargs):
        uuid = "0e76a4c3-41d3-4405-a5c2-040c75793e40"
        cmd = "disable vlan {0}".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_egress_untagged(self, arg_dictionary, **kwargs):
        uuid = "1455236d-3899-476e-a333-93fcff7ed6ad"
        cmd = "configure vlan {0} add ports {1} untagged".format(arg_dictionary['vlan'],
                                                                 arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_egress_tagged(self, arg_dictionary, **kwargs):
        uuid = "8fb45945-51d5-43b8-b469-84d4cfc3f546"
        cmd = "configure vlan {0} add ports {1} tagged".format(arg_dictionary['vlan'],
                                                               arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_egress(self, arg_dictionary, **kwargs):
        uuid = "aaca0f2c-01a7-48d1-8b68-f113d9711a23"
        cmd = "configure vlan {0} delete ports {1}".format(arg_dictionary['vlan'],
                                                           arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_description(self, arg_dictionary, **kwargs):
        uuid = "5e31f606-0a42-473b-906e-651b1fdabebc"
        cmd = "configure vlan {0} description \"{1}\"".format(arg_dictionary['vlan'],
                                                              arg_dictionary['name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_description(self, arg_dictionary, **kwargs):
        uuid = "c5b9a551-a137-41af-aa7b-c283c9f9f12e"
        cmd = "unconfigure vlan {0} description".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_name(self, arg_dictionary, **kwargs):
        uuid = "b5132db1-ed57-4b19-a129-13bf3cf6efbe"
        cmd = "configure vlan {0} name \"{1}\"".format(arg_dictionary['vlan'],
                                                       arg_dictionary['name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def create_vlan_with_name(self, arg_dictionary, **kwargs):
        uuid = "b86d2d18-f68a-4a9a-8ad1-1cdb08fe5b12"
        cmd = "create vlan {0} tag {1}".format(arg_dictionary['vlan'],
                                               arg_dictionary['tag'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_vman_egress_untagged(self, arg_dictionary, **kwargs):
        uuid = "04fbd352-383e-4c39-893e-dda530bd3503"
        cmd = "configure vman {0} add ports {1} untagged".format(arg_dictionary['vman'],
                                                                 arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_vman_egress_tagged(self, arg_dictionary, **kwargs):
        uuid = "407229d5-b7f8-4000-b3df-d72b175b5ff5"
        cmd = "configure vman {0} add ports {1} tagged".format(arg_dictionary['vman'],
                                                               arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_vman_egress(self, arg_dictionary, **kwargs):
        uuid = "6a69ee23-2396-4360-84a1-a6e1ba89800a"
        cmd = "configure vman {0} delete ports {1}".format(arg_dictionary['vman'],
                                                           arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_nsi(self, arg_dictionary, **kwargs):
        uuid = "610c3185-468f-4904-8271-907e501cf8cb"
        cmd = "configure vlan {0} add nsi {1}".format(arg_dictionary['vlan'],
                                                      arg_dictionary['nsi'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_nsi(self, arg_dictionary, **kwargs):
        uuid = "f0948db0-40b0-401c-ae27-1ec4f2b41dc1"
        cmd = "configure vlan {0} delete nsi {1}".format(arg_dictionary['vlan'],
                                                         arg_dictionary['nsi'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_isid(self, arg_dictionary, **kwargs):
        uuid = "294d7f0f-df09-4d6e-9270-7c0828f55389"
        cmd = "configure vlan {0} add isid {1}".format(arg_dictionary['vlan'],
                                                       arg_dictionary['i_sid'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_isid(self, arg_dictionary, **kwargs):
        uuid = "46694b6b-a900-4efa-a601-ee598aa753ec"
        cmd = "configure vlan {0} delete isid {1}".format(arg_dictionary['vlan'],
                                                          arg_dictionary['i_sid'])
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

    def show_static(self, arg_dictionary, **kwargs):
        uuid = "61b9b7fc-add0-405d-ac77-30694a708e62"
        cmd = "show vlan {0}".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_all_vman_info(self, arg_dictionary, **kwargs):
        uuid = "970b28f4-48a1-44ca-8fb6-db655fd6e5dc"
        cmd = "show vman"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_vman_info(self, arg_dictionary, **kwargs):
        uuid = "0232c1ae-d430-4d55-a131-f2d3f7b14710"
        cmd = "show vman {0}".format(arg_dictionary['vman'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_fabric_attach_assignments(self, arg_dictionary, **kwargs):
        uuid = "7c45c869-ca15-45f3-b775-70972371f537"
        cmd = "show vlan fabric attach assignments"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_nsi(self, arg_dictionary, **kwargs):
        uuid = "27ad3b81-b4a6-4daf-a3f1-76ed5ff2ed36"
        cmd = "show vlan {0} fabric attach mappings".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_isid(self, arg_dictionary, **kwargs):
        uuid = "d693505e-bd3f-4930-b12e-b46a62309c08"
        cmd = "show vlan {0} fabric attach mappings".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
