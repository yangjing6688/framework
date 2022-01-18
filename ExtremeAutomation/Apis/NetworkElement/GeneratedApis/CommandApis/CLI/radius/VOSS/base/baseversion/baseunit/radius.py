"""
All radius supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.radius.base.radiusbase import RadiusBase


class Radius(DeviceApi, RadiusBase):
    def __init__(self, device_input):
        super(Radius, self).__init__(device_input)

    def enable_global(self, arg_dictionary, **kwargs):
        uuid = "6a794411-17ce-44a1-b80f-5f467d25a8d6"
        cmd = "radius enable"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_acct(self, arg_dictionary, **kwargs):
        uuid = "d2154d3e-5129-4551-8e84-21fe67976ba5"
        cmd = "radius enable||radius accounting enable"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_global(self, arg_dictionary, **kwargs):
        uuid = "9f41adce-7e97-45c2-addc-1b3b23dcdd4c"
        cmd = "no radius enable"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_acct(self, arg_dictionary, **kwargs):
        uuid = "55596503-345c-4584-9438-65aff18f58ea"
        cmd = "no radius accounting enable"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_server(self, arg_dictionary, **kwargs):
        uuid = "714d2b1e-d4bc-436a-8691-dbd3ac8209b6"
        cmd = "radius server host {0} key {1} source-ip {2}".format(arg_dictionary['client_ip'],
                                                                    arg_dictionary['secret'],
                                                                    arg_dictionary['addr'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_server(self, arg_dictionary, **kwargs):
        uuid = "51c0947e-5037-40a8-b4da-20d97ff27f12"
        cmd = "no radius server host {0} used-by cli".format(arg_dictionary['client_ip'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_include_cli_cmds(self, arg_dictionary, **kwargs):
        uuid = "47365281-4cf9-4edc-a300-c605dba1b82b"
        cmd = "radius accounting include-cli-commands"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_cli_profile(self, arg_dictionary, **kwargs):
        uuid = "174bcffc-fd8c-44e0-8819-b6467e53fcca"
        cmd = "radius cli-profile"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_src_ip_flag(self, arg_dictionary, **kwargs):
        uuid = "65f9bf8e-afc4-4ba9-9524-2f6cba1014e4"
        cmd = "radius sourceip-flag"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_include_cli_cmds(self, arg_dictionary, **kwargs):
        uuid = "cdf8d306-4ecc-46a2-bb3c-c54e9e7e4bde"
        cmd = "no radius accounting include-cli-commands"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_cli_profile(self, arg_dictionary, **kwargs):
        uuid = "d9ca9238-85ed-485a-a939-7687362b38d4"
        cmd = "no radius cli-profile"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_src_ip_flag(self, arg_dictionary, **kwargs):
        uuid = "057b5f5e-0951-4e7d-8753-4bc8c689994d"
        cmd = "no radius sourceip-flag"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_max_servers(self, arg_dictionary, **kwargs):
        uuid = "165af531-1f1e-4519-9f91-6c59f50e0cb5"
        cmd = "radius maxserver {0}".format(arg_dictionary['max_servers'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_access_priority(self, arg_dictionary, **kwargs):
        uuid = "69907b5f-f591-4374-830f-9db39180b440"
        cmd = "radius access-priority-attribute {0}".format(arg_dictionary['attr_value'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_acct_attr(self, arg_dictionary, **kwargs):
        uuid = "ff4888ac-a8c7-4635-97e9-c714020980d9"
        cmd = "radius accounting attribute-value {0}".format(arg_dictionary['attr_value'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_mcast_addr_attr(self, arg_dictionary, **kwargs):
        uuid = "3d1d1fbe-ba8d-4b2d-841f-5cc71b44a6ec"
        cmd = "radius mcast-addr-attr-value {0}".format(arg_dictionary['attr_value'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_auth_info_attr(self, arg_dictionary, **kwargs):
        uuid = "2acf12a1-fa88-431e-ae57-05a286cbf7e4"
        cmd = "radius auth-info-attr-value {0}".format(arg_dictionary['attr_value'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_cmd_access_attr(self, arg_dictionary, **kwargs):
        uuid = "475ba50d-f042-41a2-a03f-e24928eb9aef"
        cmd = "radius command-access-attribute {0}".format(arg_dictionary['attr_value'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_cli_cmd_attr(self, arg_dictionary, **kwargs):
        uuid = "f2d03fd9-f2ac-4668-a737-26e2448a57fc"
        cmd = "radius cli-commands-attribute {0}".format(arg_dictionary['attr_value'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_cli_cmd_count(self, arg_dictionary, **kwargs):
        uuid = "3a3728fc-4684-4532-87b3-7290b2a51fe0"
        cmd = "radius cli-cmd-count {0}".format(arg_dictionary['value'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_server_for_cli(self, arg_dictionary, **kwargs):
        uuid = "80b929b7-de43-4258-a2ac-e1276374cc12"
        cmd = "radius server host {0} key {1} port {2} priority {3} retry {4} timeout {5} acct-port {6} source-ip {7}".format(arg_dictionary['addr'],
                                                                                                                              arg_dictionary['secret'],
                                                                                                                              arg_dictionary['auth_port'],
                                                                                                                              arg_dictionary['priority'],
                                                                                                                              arg_dictionary['max_retries'],
                                                                                                                              arg_dictionary['timeout'],
                                                                                                                              arg_dictionary['acct_port'],
                                                                                                                              arg_dictionary['source_ip'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_server_for_cli(self, arg_dictionary, **kwargs):
        uuid = "93acf6fd-8d47-4be8-90fb-ca762a0da238"
        cmd = "no radius server host {0} used-by cli".format(arg_dictionary['addr'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_stats_global(self, arg_dictionary, **kwargs):
        uuid = "d5301bc9-f275-4b44-904d-62d24a4da49e"
        cmd = "radius clear-stat"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_global(self, arg_dictionary, **kwargs):
        uuid = "dc7a3e85-b914-4749-9bf6-145d7123d568"
        cmd = "show radius||show radius snmp||show radius-server"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_state(self, arg_dictionary, **kwargs):
        uuid = "e4f281eb-c13f-4aaa-a1d7-a1e9a7295195"
        cmd = "show radius"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_acct_state(self, arg_dictionary, **kwargs):
        uuid = "0c4f711c-7595-43eb-921d-9d1864619ac6"
        cmd = "show radius"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_servers(self, arg_dictionary, **kwargs):
        uuid = "b0fd163c-1b3e-479e-9f7c-350cdfbfaed8"
        cmd = "show radius-server"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_global_scalars(self, arg_dictionary, **kwargs):
        uuid = "2d66e027-471a-414e-b120-72958acb1e79"
        cmd = "show radius"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_global_snmp_scalars(self, arg_dictionary, **kwargs):
        uuid = "05528f95-bf92-4607-a656-841611cf718c"
        cmd = "show radius snmp"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
