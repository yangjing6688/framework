"""
All snmp supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.snmp.base.snmpbase import SnmpBase


class Snmp(DeviceApi, SnmpBase):
    def __init__(self, device_input):
        super(Snmp, self).__init__(device_input)

    def create_readonly_community(self, arg_dictionary, **kwargs):
        uuid = "3a7cc49b-7100-4584-9f62-ad1646c91afe"
        cmd = "snmp-server community {0} index {1} secname {2} context {3}".format(arg_dictionary['community_name'],
                                                                                   arg_dictionary['community_index'],
                                                                                   arg_dictionary['security_name'],
                                                                                   arg_dictionary['context'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def create_readwrite_community(self, arg_dictionary, **kwargs):
        uuid = "967de9e7-3ced-40a1-ad0d-c89ab4b5177d"
        cmd = "snmp-server community {0} index {1} secname {2} context {3}".format(arg_dictionary['community_name'],
                                                                                   arg_dictionary['community_index'],
                                                                                   arg_dictionary['security_name'],
                                                                                   arg_dictionary['context'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def delete_community(self, arg_dictionary, **kwargs):
        uuid = "c8579c62-a6a4-4e03-9bea-89fd8b50c5b3"
        cmd = "no snmp-server community {0}".format(arg_dictionary['community_name'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def delete_user(self, arg_dictionary, **kwargs):
        uuid = "282ee4e9-601d-4c42-b69a-1965fe2a66e7"
        cmd = "no snmp-server user {0}".format(arg_dictionary['user_name'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_user_no_authentication(self, arg_dictionary, **kwargs):
        uuid = "86b262b8-fc15-4c68-be86-1ca3ef0bc457"
        cmd = "snmp-server user {0} group {1}".format(arg_dictionary['user_name'],
                                                      arg_dictionary['group'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_user_authentication(self, arg_dictionary, **kwargs):
        uuid = "83cad0e6-f50c-4897-a587-7fdb393dc513"
        cmd = "snmp-server user {0}  group {1} {2} {3}".format(arg_dictionary['user_name'],
                                                               arg_dictionary['group'],
                                                               arg_dictionary['auth_proto'],
                                                               arg_dictionary['auth_password'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_user_privacy(self, arg_dictionary, **kwargs):
        uuid = "2715b88c-a9de-41c0-8605-2900d2be9f33"
        cmd = "snmp-server user {0} group {1} {2} {3} {4} {5}".format(arg_dictionary['user_name'],
                                                                      arg_dictionary['group'],
                                                                      arg_dictionary['auth_proto'],
                                                                      arg_dictionary['auth_password'],
                                                                      arg_dictionary['priv_proto'],
                                                                      arg_dictionary['priv_password'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_user_no_authentication_engine_id(self, arg_dictionary, **kwargs):
        uuid = "5351d630-450c-4fa4-9a26-8c685b6ac119"
        cmd = "snmp-server user engine-id {0} {1} group {2}".format(arg_dictionary['engine_id'],
                                                                    arg_dictionary['user_name'],
                                                                    arg_dictionary['group'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_user_authentication_engine_id(self, arg_dictionary, **kwargs):
        uuid = "f75c5703-adac-4c4e-9885-5d73a91fbae9"
        cmd = "snmp-server user engine-id {0} {1} group {2} {3} {4}".format(arg_dictionary['engine_id'],
                                                                            arg_dictionary['user_name'],
                                                                            arg_dictionary['group'],
                                                                            arg_dictionary['auth_proto'],
                                                                            arg_dictionary['auth_password'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_user_privacy_engine_id(self, arg_dictionary, **kwargs):
        uuid = "9d182ff5-016a-42e3-a16a-e1fbbd96c461"
        cmd = "snmp-server user engine-id {0} {1} group {2} {3} {4} {5} {6}".format(arg_dictionary['engine_id'],
                                                                                    arg_dictionary['user_name'],
                                                                                    arg_dictionary['group'],
                                                                                    arg_dictionary['auth_proto'],
                                                                                    arg_dictionary['auth_password'],
                                                                                    arg_dictionary['priv_proto'],
                                                                                    arg_dictionary['priv_password'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_authentication_trap(self, arg_dictionary, **kwargs):
        uuid = "82570981-b4ba-4d40-8fe9-3868f9a706c7"
        cmd = "snmp-server authentication-trap enable"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_authentication_trap(self, arg_dictionary, **kwargs):
        uuid = "1af11b3a-7b17-4173-80ee-8b0075ee8a6f"
        cmd = "no snmp-server authentication-trap"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_same_snmp_and_ip_sender_flag(self, arg_dictionary, **kwargs):
        uuid = "5a069297-79af-4ce3-b42a-057f33874574"
        cmd = "snmp-server force-iphdr-sender enable"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_same_snmp_and_ip_sender_flag(self, arg_dictionary, **kwargs):
        uuid = "b22d72e2-458b-4f59-a4ad-484bb7d29ad0"
        cmd = "no snmp-server force-iphdr-sender"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_same_snmp_trap_sender_ip(self, arg_dictionary, **kwargs):
        uuid = "103819d3-297a-4504-b03e-ae75b124b56b"
        cmd = "snmp-server force-trap-sender enable"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_same_snmp_trap_sender_ip(self, arg_dictionary, **kwargs):
        uuid = "82f99f99-a12a-4765-b0c4-ef5a14932855"
        cmd = "no snmp-server force-trap-sender"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def create_v1_trap_server(self, arg_dictionary, **kwargs):
        uuid = "65155113-aca6-401f-9523-d24e265742af"
        cmd = "snmp-server host {0} port {1} v1 {2}".format(arg_dictionary['ip_addr'],
                                                            arg_dictionary['port'],
                                                            arg_dictionary['security_name'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def delete_v1_trap_server(self, arg_dictionary, **kwargs):
        uuid = "a2fc0df6-ba11-4600-aaa7-2b310e3137fd"
        cmd = "no snmp-server host {0} port {1} v1 {2}".format(arg_dictionary['ip_addr'],
                                                               arg_dictionary['port'],
                                                               arg_dictionary['security_name'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def create_v2c_trap_server(self, arg_dictionary, **kwargs):
        uuid = "ab9bc27d-48a7-49e8-8060-a2d05523c403"
        cmd = "snmp-server host {0} port {1} v2c {2}".format(arg_dictionary['ip_addr'],
                                                             arg_dictionary['port'],
                                                             arg_dictionary['security_name'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def delete_v2c_trap_server(self, arg_dictionary, **kwargs):
        uuid = "32c795f8-1d58-49fc-8546-175dea332fde"
        cmd = "no snmp-server host {0} port {1} v2c {2}".format(arg_dictionary['ip_addr'],
                                                                arg_dictionary['port'],
                                                                arg_dictionary['security_name'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def create_v2c_inform_server(self, arg_dictionary, **kwargs):
        uuid = "262425cb-ecba-4def-ab78-92bef8d53265"
        cmd = "snmp-server host {0} port {1} v2c {2} inform timeout {3} retries {4} mms {5}".format(arg_dictionary['ip_addr'],
                                                                                                    arg_dictionary['port'],
                                                                                                    arg_dictionary['security_name'],
                                                                                                    arg_dictionary['timeout'],
                                                                                                    arg_dictionary['retries'],
                                                                                                    arg_dictionary['mms'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def delete_v2c_inform_server(self, arg_dictionary, **kwargs):
        uuid = "7b190c70-f885-4be0-afa8-7d02a752781e"
        cmd = "no snmp-server host {0} v2c {1}".format(arg_dictionary['ip_addr'],
                                                       arg_dictionary['security_name'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def create_v3_trap_server(self, arg_dictionary, **kwargs):
        uuid = "5c45efe6-41f2-4aca-bbc5-c2c58a4aa086"
        cmd = "snmp-server host {0} port {1} v3 {2} {3}".format(arg_dictionary['ip_addr'],
                                                                arg_dictionary['port'],
                                                                arg_dictionary['security_level'],
                                                                arg_dictionary['security_name'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def delete_v3_trap_server(self, arg_dictionary, **kwargs):
        uuid = "27309891-ea40-41ce-8f00-63492aa8db80"
        cmd = "no snmp-server host {0} port {1} v3 {2}".format(arg_dictionary['ip_addr'],
                                                               arg_dictionary['port'],
                                                               arg_dictionary['security_name'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def create_v3_inform_server(self, arg_dictionary, **kwargs):
        uuid = "60d292ee-8aa6-420e-8f61-9e5d94cf3c4b"
        cmd = "snmp-server host {0} port {1} v3 {2} {3} inform timeout {4} retries {5}".format(arg_dictionary['ip_addr'],
                                                                                               arg_dictionary['port'],
                                                                                               arg_dictionary['security_level'],
                                                                                               arg_dictionary['security_name'],
                                                                                               arg_dictionary['timeout'],
                                                                                               arg_dictionary['retries'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def delete_v3_inform_server(self, arg_dictionary, **kwargs):
        uuid = "8410645f-c725-4937-8f93-ed97ec5c6d72"
        cmd = "no snmp-server host {0} v3 {1}".format(arg_dictionary['ip_addr'],
                                                      arg_dictionary['security_name'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_notify_filter(self, arg_dictionary, **kwargs):
        uuid = "dc2296ba-a156-49a2-9584-59b971ca9756"
        cmd = "snmp-server notify-filter {0} {1}".format(arg_dictionary['profile_name'],
                                                         arg_dictionary['oid_tree'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_notify_filter(self, arg_dictionary, **kwargs):
        uuid = "50c0c14a-8374-4114-859c-c7ffb10cb66c"
        cmd = "no snmp-server notify-filter {0} {1}".format(arg_dictionary['profile_name'],
                                                            arg_dictionary['oid_tree'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def delete_user_engine_id(self, arg_dictionary, **kwargs):
        uuid = "e3dd38d3-79c0-4829-9a51-da0a58af052b"
        cmd = "no snmp-server user engine-id {0} {1}".format(arg_dictionary['engine_id'],
                                                             arg_dictionary['user_name'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def create_group_and_access(self, arg_dictionary, **kwargs):
        uuid = "8d68eddb-86bc-4b21-85a7-40ce75c3815d"
        cmd = "snmp-server group {0} {1} {2} read-view {3} write-view {4} notify-view {5}".format(arg_dictionary['group'],
                                                                                                  arg_dictionary['context'],
                                                                                                  arg_dictionary['security_level'],
                                                                                                  arg_dictionary['read_view'],
                                                                                                  arg_dictionary['write_view'],
                                                                                                  arg_dictionary['notify_view'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def delete_group_and_access(self, arg_dictionary, **kwargs):
        uuid = "453baa15-3319-46ad-8851-3b75ea6dab78"
        cmd = "no snmp-server group {0} {1}".format(arg_dictionary['group'],
                                                    arg_dictionary['context'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def create_view(self, arg_dictionary, **kwargs):
        uuid = "e714befc-dc0d-4293-8ab7-108d34aee8ef"
        cmd = "snmp-server view {0} {1}".format(arg_dictionary['view_name'],
                                                arg_dictionary['oid_tree'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def delete_view(self, arg_dictionary, **kwargs):
        uuid = "47f6342b-af6f-4346-b3cf-83e093410bbf"
        cmd = "no snmp-server view {0} {1}".format(arg_dictionary['view_name'],
                                                   arg_dictionary['oid_tree'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_globals(self, arg_dictionary, **kwargs):
        uuid = "188d9c0c-a329-4842-90c9-5d7758d9d4f7"
        cmd = "show snmp-server"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_community(self, arg_dictionary, **kwargs):
        uuid = "8cf2de00-0a2c-440a-b8ff-7a27be04b189"
        cmd = "show snmp-server community"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_context(self, arg_dictionary, **kwargs):
        uuid = "a2262541-9629-4502-8a7b-b5ba27b204cf"
        cmd = "show snmp-server context"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_group(self, arg_dictionary, **kwargs):
        uuid = "df37671c-b286-4eb7-afcf-8db270b76c9d"
        cmd = "show snmp-server group"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_access(self, arg_dictionary, **kwargs):
        uuid = "77c7a6e6-f281-48d8-b21b-aad5fff0e7f5"
        cmd = "show snmp-server group"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_host(self, arg_dictionary, **kwargs):
        uuid = "14bd2f4c-d351-40a9-add6-5ec45b20d689"
        cmd = "show snmp-server host"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_notify_filter(self, arg_dictionary, **kwargs):
        uuid = "5810ac9d-ea35-4792-ad32-3b843495c8cb"
        cmd = "show snmp-server notify-filter"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_user(self, arg_dictionary, **kwargs):
        uuid = "b6de9c13-0c3a-4764-861a-2354e2d245c3"
        cmd = "show snmp-server user"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_view(self, arg_dictionary, **kwargs):
        uuid = "ac04eb58-4784-4705-8831-1e1d8196a25f"
        cmd = "show snmp-server view"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
