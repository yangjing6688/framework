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
        cmd = "vlan create {0} type port-mstprstp 0".format(arg_dictionary['vlan'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def delete_vlan(self, arg_dictionary, **kwargs):
        uuid = "eaccd886-b51c-409d-9daa-703133a964e5"
        cmd = "vlan delete {0}".format(arg_dictionary['vlan'])
        prompt = "routerConfigPrompt"

        self.device.error_checker.add_error_to_ignore_list(*["Error: Invalid VLAN ID"])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_egress_untagged(self, arg_dictionary, **kwargs):
        uuid = "1455236d-3899-476e-a333-93fcff7ed6ad"
        cmd = "vlan ports {0} tagging tagAll||vlan members add {1} {2}||interface GigabitEthernet {3}||default-vlan-id {4}||untag-port-default-vlan enable||exit".format(arg_dictionary['port'],
                                                                                                                                                                         arg_dictionary['vlan'],
                                                                                                                                                                         arg_dictionary['port'],
                                                                                                                                                                         arg_dictionary['port'],
                                                                                                                                                                         arg_dictionary['vlan'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_egress_tagged(self, arg_dictionary, **kwargs):
        uuid = "8fb45945-51d5-43b8-b469-84d4cfc3f546"
        cmd = "vlan ports {0} tagging tagAll||vlan members add {1} {2}".format(arg_dictionary['port'],
                                                                               arg_dictionary['vlan'],
                                                                               arg_dictionary['port'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_name(self, arg_dictionary, **kwargs):
        uuid = "b5132db1-ed57-4b19-a129-13bf3cf6efbe"
        cmd = "vlan name {0} {1}".format(arg_dictionary['vlan'],
                                         arg_dictionary['name'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_pvid(self, arg_dictionary, **kwargs):
        uuid = "b4477fa8-5f9e-449e-bc9f-c88a87add7b6"
        cmd = "default-vlan-id {0}".format(arg_dictionary['vlan'])
        prompt = "intfPrompt"
        prompt_args = "GigabitEthernet {0}".format(arg_dictionary['port'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def clear_pvid(self, arg_dictionary, **kwargs):
        uuid = "04479df7-6ad7-4db6-8410-9bda5e8458d9"
        cmd = "default-vlan-id 1"
        prompt = "intfPrompt"
        prompt_args = "GigabitEthernet {0}".format(arg_dictionary['port'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_isid(self, arg_dictionary, **kwargs):
        uuid = "294d7f0f-df09-4d6e-9270-7c0828f55389"
        cmd = "vlan i-sid {0} {1}".format(arg_dictionary['vlan'],
                                          arg_dictionary['i_sid'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_isid(self, arg_dictionary, **kwargs):
        uuid = "46694b6b-a900-4efa-a601-ee598aa753ec"
        cmd = "no vlan i-sid {0}".format(arg_dictionary['vlan'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def create_spbm(self, arg_dictionary, **kwargs):
        uuid = "6b27e129-327c-49c4-aab5-c2867715e0bd"
        cmd = "vlan create {0} type spbm-bvlan".format(arg_dictionary['vlan'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_member(self, arg_dictionary, **kwargs):
        uuid = "c639c0ad-4fce-423f-ace9-15fe887fb325"
        cmd = "vlan members add {0} {1}".format(arg_dictionary['vlan'],
                                                arg_dictionary['port'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_member(self, arg_dictionary, **kwargs):
        uuid = "2d7fb185-5133-4fb8-8d98-19e72eb05776"
        cmd = "vlan members remove {0} {1}".format(arg_dictionary['vlan'],
                                                   arg_dictionary['port'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_port_encapsulation_dot1q(self, arg_dictionary, **kwargs):
        uuid = "345acff8-3752-4fa5-bede-4a40de99cadf"
        cmd = "encapsulation dot1q"
        prompt = "intfPrompt"
        prompt_args = "GigabitEthernet {0}".format(arg_dictionary['port'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def clear_port_encapsulation_dot1q(self, arg_dictionary, **kwargs):
        uuid = "7c4d0acd-43c6-4374-9863-49b5ebaac0a2"
        cmd = "no encapsulation dot1q"
        prompt = "intfPrompt"
        prompt_args = "GigabitEthernet {0}".format(arg_dictionary['port'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def show_all_info(self, arg_dictionary, **kwargs):
        uuid = "665c60ed-ab31-4ccd-9b85-7946db3c01a3"
        cmd = "show vlan basic"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_info(self, arg_dictionary, **kwargs):
        uuid = "62cb48f8-848b-4604-a67b-5e135a96d45a"
        cmd = "show port vlan"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_name(self, arg_dictionary, **kwargs):
        uuid = "48cf27a1-71fd-4212-85a3-12db4d2f899d"
        cmd = "show vlan name {0}".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_status(self, arg_dictionary, **kwargs):
        uuid = "d487d4f0-befa-4034-9882-80fa3f609e21"
        cmd = "show vlan basic {0}".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_pvid(self, arg_dictionary, **kwargs):
        uuid = "49369c19-a5c0-4518-bd93-317d7ff99061"
        cmd = "show port vlan {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_static(self, arg_dictionary, **kwargs):
        uuid = "61b9b7fc-add0-405d-ac77-30694a708e62"
        cmd = "show vlan mac-address-static {0}".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port_egress(self, arg_dictionary, **kwargs):
        uuid = "5129a33b-95c8-4b61-a2b9-f18d94db9f53"
        cmd = "show port vlans"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_isid(self, arg_dictionary, **kwargs):
        uuid = "d693505e-bd3f-4930-b12e-b46a62309c08"
        cmd = "show vlan i-sid {0}".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_members(self, arg_dictionary, **kwargs):
        uuid = "40751f42-ee75-4d5c-91df-31cec8779388"
        cmd = "show vlan members"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_members_port(self, arg_dictionary, **kwargs):
        uuid = "ee7a03f6-be9e-4946-baf0-75d059ca98a6"
        cmd = "show vlan members port {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port(self, arg_dictionary, **kwargs):
        uuid = "f3e6ecae-2e8a-4de3-9cc3-0faede0c623f"
        cmd = "show interfaces gigabitEthernet name {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
