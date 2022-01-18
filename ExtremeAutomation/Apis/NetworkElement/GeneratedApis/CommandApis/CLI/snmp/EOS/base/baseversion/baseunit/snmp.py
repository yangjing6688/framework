"""
All snmp supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.snmp.base.snmpbase import SnmpBase


class Snmp(DeviceApi, SnmpBase):
    def __init__(self, device_input):
        super(Snmp, self).__init__(device_input)

    def create_all_trap_server(self, arg_dictionary, **kwargs):
        uuid = "937890fb-dc59-4f13-a87c-c4e718fc9990"
        cmd = "set snmp targetaddr {0} {1} param {2} taglist {3}".format(arg_dictionary['server_name'],
                                                                         arg_dictionary['ip_address'],
                                                                         arg_dictionary['param_name'],
                                                                         arg_dictionary['tag_list'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def delete_trap_servers(self, arg_dictionary, **kwargs):
        uuid = "380d633f-5653-4917-bafb-2bed364f74eb"
        cmd = "clear snmp targetaddr {0}".format(arg_dictionary['server_name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_trap_param(self, arg_dictionary, **kwargs):
        uuid = "9911ac50-36b0-46eb-95c3-9e128d042a82"
        cmd = "set snmp targetparams {0} user {1} security {2} message {3}".format(arg_dictionary['param_name'],
                                                                                   arg_dictionary['community'],
                                                                                   arg_dictionary['version'],
                                                                                   arg_dictionary['version'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_trap_param(self, arg_dictionary, **kwargs):
        uuid = "502a9f4e-4cee-42a8-9689-5da899ad1bb8"
        cmd = "clear snmp targetparams {0}".format(arg_dictionary['param_name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_notify(self, arg_dictionary, **kwargs):
        uuid = "fa526bb7-d1fc-4196-8a0c-80dcf7cd84f7"
        cmd = "set snmp notify {0} tag {1} {2}".format(arg_dictionary['notify_name'],
                                                       arg_dictionary['notify_name'],
                                                       arg_dictionary['type'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_notify(self, arg_dictionary, **kwargs):
        uuid = "d945dbb4-92ab-4f69-b810-97fbdd8d9a2b"
        cmd = "clear snmp notify {0}".format(arg_dictionary['notify_name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
