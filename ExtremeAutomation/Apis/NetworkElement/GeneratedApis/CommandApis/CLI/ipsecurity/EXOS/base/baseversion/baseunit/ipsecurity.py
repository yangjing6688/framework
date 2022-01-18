"""
All ipsecurity supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.ipsecurity.base.ipsecuritybase import \
    IpsecurityBase


class Ipsecurity(DeviceApi, IpsecurityBase):
    def __init__(self, device_input):
        super(Ipsecurity, self).__init__(device_input)

    def set_trusted_port(self, arg_dictionary, **kwargs):
        uuid = "b9ac8cef-938a-42b2-9f7c-89f05e973036"
        cmd = "configure trusted-port {0} trust-for dhcp-server".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_dhcp_snooping(self, arg_dictionary, **kwargs):
        uuid = "47d790b4-9278-4c6b-840b-cc492b777005"
        cmd = "enable ip-security dhcp-snooping vlan {0} ports {1} violation-action {2} {3} {4} {5}".format(arg_dictionary['vlan'],
                                                                                                            arg_dictionary['ports'],
                                                                                                            arg_dictionary['violation_action'],
                                                                                                            self.api_utils.exos_ipsec_trap(arg_dictionary['snmp_trap']),
                                                                                                            arg_dictionary['block'],
                                                                                                            self.api_utils.exos_ipsec_duration(arg_dictionary['duration'], arg_dictionary['snmp_trap'], arg_dictionary['block']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_dhcp_snooping(self, arg_dictionary, **kwargs):
        uuid = "57f8930a-0e61-4148-a03c-10a9c233593c"
        cmd = "disable ip-security dhcp-snooping vlan {0} ports {1}".format(arg_dictionary['vlan'],
                                                                            arg_dictionary['ports'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_snooping_vlan(self, arg_dictionary, **kwargs):
        uuid = "78dac202-30b3-4926-80fd-86573120adb6"
        cmd = "show ip-security dhcp-snooping vlan {0}".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_snooping_vlan_entries(self, arg_dictionary, **kwargs):
        uuid = "222cc1ba-091a-4eb0-8f5b-6e7d7521ad38"
        cmd = "show ip-security dhcp-snooping entries vlan {0}".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_snooping_vlan_violations(self, arg_dictionary, **kwargs):
        uuid = "4e7517f1-29e4-4f7d-9803-de48ecc02914"
        cmd = "show ip-security dhcp-snooping violations vlan {0}".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_trusted_ports(self, arg_dictionary, **kwargs):
        uuid = "c6308292-b9f3-4434-99fe-ed7d362d246d"
        cmd = "show config | grep trusted"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
