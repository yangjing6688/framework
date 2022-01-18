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
        cmd = "configure snmp add trapreceiver {0} community {1}".format(arg_dictionary['ip_address'],
                                                                         arg_dictionary['community'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def delete_trap_servers(self, arg_dictionary, **kwargs):
        uuid = "380d633f-5653-4917-bafb-2bed364f74eb"
        cmd = "configure snmp delete trapreceiver {0}".format(arg_dictionary['ip_address'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def create_readonly_community(self, arg_dictionary, **kwargs):
        uuid = "3a7cc49b-7100-4584-9f62-ad1646c91afe"
        cmd = "configure snmpv3 add community {0} name {1} user {2}".format(arg_dictionary['community_index'],
                                                                            arg_dictionary['community_name'],
                                                                            arg_dictionary['security_name'])
        prompt = "userPrompt"
        conf = "Warning: Entry exists. Are you sure you want to modify it? (y/N)"
        conf_args = "y"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf, conf_args=conf_args)

    def create_readwrite_community(self, arg_dictionary, **kwargs):
        uuid = "967de9e7-3ced-40a1-ad0d-c89ab4b5177d"
        cmd = "configure snmpv3 add community {0} name {1} user {2}".format(arg_dictionary['community_index'],
                                                                            arg_dictionary['community_name'],
                                                                            arg_dictionary['security_name'])
        prompt = "userPrompt"
        conf = "Warning: Entry exists. Are you sure you want to modify it? (y/N)"
        conf_args = "y"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf, conf_args=conf_args)

    def delete_community(self, arg_dictionary, **kwargs):
        uuid = "c8579c62-a6a4-4e03-9bea-89fd8b50c5b3"
        cmd = "configure snmpv3 del community {0}".format(arg_dictionary['community_name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def delete_user(self, arg_dictionary, **kwargs):
        uuid = "282ee4e9-601d-4c42-b69a-1965fe2a66e7"
        cmd = "configure snmpv3 delete user {0}".format(arg_dictionary['user_name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_user_no_authentication(self, arg_dictionary, **kwargs):
        uuid = "86b262b8-fc15-4c68-be86-1ca3ef0bc457"
        cmd = "configure snmpv3 add user {0}".format(arg_dictionary['user_name'])
        prompt = "userPrompt"
        conf = "Warning: Entry exists. Are you sure you want to modify it? (y/N)"
        conf_args = "y"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf, conf_args=conf_args)

    def set_user_authentication(self, arg_dictionary, **kwargs):
        uuid = "83cad0e6-f50c-4897-a587-7fdb393dc513"
        cmd = "configure snmpv3 add user {0} authentication {1} {2}".format(arg_dictionary['user_name'],
                                                                            arg_dictionary['auth_proto'],
                                                                            arg_dictionary['auth_password'])
        prompt = "userPrompt"
        conf = "Warning: Entry exists. Are you sure you want to modify it? (y/N)"
        conf_args = "y"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf, conf_args=conf_args)

    def set_user_privacy(self, arg_dictionary, **kwargs):
        uuid = "2715b88c-a9de-41c0-8605-2900d2be9f33"
        cmd = "configure snmpv3 add user {0} authentication {1} {2} privacy {3} {4}".format(arg_dictionary['user_name'],
                                                                                            arg_dictionary['auth_proto'],
                                                                                            arg_dictionary['auth_password'],
                                                                                            arg_dictionary['priv_proto'],
                                                                                            arg_dictionary['priv_password'])
        prompt = "userPrompt"
        conf = "Warning: Entry exists. Are you sure you want to modify it? (y/N)"
        conf_args = "y"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf, conf_args=conf_args)

    def set_user_no_authentication_engine_id(self, arg_dictionary, **kwargs):
        uuid = "5351d630-450c-4fa4-9a26-8c685b6ac119"
        cmd = "configure snmpv3 add user {0} engine-id {1}".format(arg_dictionary['user_name'],
                                                                   arg_dictionary['engine_id'])
        prompt = "userPrompt"
        conf = "Warning: Entry exists. Are you sure you want to modify it? (y/N)"
        conf_args = "y"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf, conf_args=conf_args)

    def set_user_authentication_engine_id(self, arg_dictionary, **kwargs):
        uuid = "f75c5703-adac-4c4e-9885-5d73a91fbae9"
        cmd = "configure snmpv3 add user {0} authentication {1} {2} engine-id {3}".format(arg_dictionary['user_name'],
                                                                                          arg_dictionary['auth_proto'],
                                                                                          arg_dictionary['auth_password'],
                                                                                          arg_dictionary['engine_id'])
        prompt = "userPrompt"
        conf = "Warning: Entry exists. Are you sure you want to modify it? (y/N)"
        conf_args = "y"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf, conf_args=conf_args)

    def set_user_privacy_engine_id(self, arg_dictionary, **kwargs):
        uuid = "9d182ff5-016a-42e3-a16a-e1fbbd96c461"
        cmd = "configure snmpv3 add user {0} authentication {1} {2} privacy {3} {4} engine-id {5}".format(arg_dictionary['user_name'],
                                                                                                          arg_dictionary['auth_proto'],
                                                                                                          arg_dictionary['auth_password'],
                                                                                                          arg_dictionary['priv_proto'],
                                                                                                          arg_dictionary['priv_password'],
                                                                                                          arg_dictionary['engine_id'])
        prompt = "userPrompt"
        conf = "Warning: Entry exists. Are you sure you want to modify it? (y/N)"
        conf_args = "y"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf, conf_args=conf_args)

    def enable_access_global(self, arg_dictionary, **kwargs):
        uuid = "acd52df8-7550-404d-8cd9-e757fabab7c2"
        cmd = "enable snmp access"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_access_global(self, arg_dictionary, **kwargs):
        uuid = "4ae2e419-faec-4a79-8d5b-c5475ea946a8"
        cmd = "disable snmp access"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_vr(self, arg_dictionary, **kwargs):
        uuid = "f93f38f1-df1a-47e2-a8b4-033f7b330ae3"
        cmd = "show snmp {0}".format(arg_dictionary['vr'])
        prompt = "userPrompt"

        self.device.error_checker.add_error_to_ignore_list(*["Error"])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
