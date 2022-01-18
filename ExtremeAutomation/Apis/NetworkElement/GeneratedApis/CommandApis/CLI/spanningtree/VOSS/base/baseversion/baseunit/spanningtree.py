"""
All spanningtree supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.spanningtree.base.spanningtreebase import \
    SpanningtreeBase


class Spanningtree(DeviceApi, SpanningtreeBase):
    def __init__(self, device_input):
        super(Spanningtree, self).__init__(device_input)

    def enable_port_admin(self, arg_dictionary, **kwargs):
        uuid = "fb42dbbb-4759-410a-9810-bca7e9bd89ad"
        cmd = "interface GigabitEthernet {0}||spanning-tree rstp".format(arg_dictionary['port'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_port_admin(self, arg_dictionary, **kwargs):
        uuid = "4da238d6-8dda-4685-803c-44926e305ea6"
        cmd = "interface GigabitEthernet {0}||no spanning-tree rstp {1}".format(arg_dictionary['port'],
                                                                                arg_dictionary['port'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_stp_mode(self, arg_dictionary, **kwargs):
        uuid = "92b4464f-52bb-4af1-898b-d56fd39c4191"
        cmd = "spanning-tree mstp version {0}".format(self.api_utils.voss_stp_mode(arg_dictionary['mode']))
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_stp_mode(self, arg_dictionary, **kwargs):
        uuid = "2f7f1071-e451-4727-8844-66e25ea247a5"
        cmd = "spanning-tree rstp version mstp"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_priority(self, arg_dictionary, **kwargs):
        uuid = "deda1330-9d1e-4073-9f84-c83b776f751a"
        cmd = "spanning-tree rstp priority {0}".format(arg_dictionary['priority'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_msti_vlan_mapping(self, arg_dictionary, **kwargs):
        uuid = "6017e09a-4a1a-40c1-9ddf-d115e9493d53"
        cmd = "vlan create {0} type port-mstprstp s{1}".format(arg_dictionary['vlan'],
                                                               arg_dictionary['sid'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_msti_vlan_mapping(self, arg_dictionary, **kwargs):
        uuid = "4866041a-6d89-40db-b595-48c9c2590edb"
        cmd = "vlan delete {0}".format(arg_dictionary['vlan'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_mst_region_name(self, arg_dictionary, **kwargs):
        uuid = "b5a10760-b5ab-47c4-a493-431a4a594df0"
        cmd = "spanning-tree mstp region region-name {0}".format(arg_dictionary['region'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_mst_revision_level(self, arg_dictionary, **kwargs):
        uuid = "625db2cb-e475-4068-bfba-1f10033d7312"
        cmd = "spanning-tree mstp region region-version {0}".format(arg_dictionary['revision'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_hello_time(self, arg_dictionary, **kwargs):
        uuid = "7238ca1e-0519-418e-8768-7c2fbcd5ccb1"
        cmd = "spanning-tree rstp hello-time {0}".format(arg_dictionary['hello'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_fwd_delay(self, arg_dictionary, **kwargs):
        uuid = "07dc6524-f57c-40df-a452-3b035f6a3a35"
        cmd = "spanning-tree rstp forward-time {0}".format(arg_dictionary['fwd_delay'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_max_age(self, arg_dictionary, **kwargs):
        uuid = "c8504eba-6791-4455-8d32-43e80b6a518d"
        cmd = "spanning-tree rstp max-age {max_age"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_mst_instance(self, arg_dictionary, **kwargs):
        uuid = "e39955cf-086f-4833-b817-99f2460a48d2"
        cmd = "spanning-tree mstp msti s{0}".format(arg_dictionary['sid'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_mst_instance(self, arg_dictionary, **kwargs):
        uuid = "85d46362-9f42-4ec1-872b-578ca0a7e904"
        cmd = "no spanning-tree mstp msti s{0}".format(arg_dictionary['sid'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_mst_instance_tag(self, arg_dictionary, **kwargs):
        uuid = "ca2243c4-4118-4c63-92c3-c2dc906603ff"
        cmd = "spanning-tree mstp region config-id-sel {0}".format(arg_dictionary['tag'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_port_link_type_point_to_point(self, arg_dictionary, **kwargs):
        uuid = "11ab7305-fd4a-48f0-ad0c-510934db0493"
        cmd = "interface GigabitEthernet {0}||spanning-tree rstp edge-port false".format(arg_dictionary['port'])
        prompt = "routerConfigPrompt"
        conf = "Warning:"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf)

    def set_port_link_type_edge(self, arg_dictionary, **kwargs):
        uuid = "88bc889e-d8f7-4723-8476-203e246d7669"
        cmd = "interface GigabitEthernet {0}||spanning-tree rstp edge-port true".format(arg_dictionary['port'])
        prompt = "routerConfigPrompt"
        conf = "Warning:"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf)

    def create_mst_vlan_instance(self, arg_dictionary, **kwargs):
        uuid = "41a178a7-fd2f-4842-963f-c19a351727c3"
        cmd = "vlan create {0} type port-mstprstp s{1}".format(arg_dictionary['vlan'],
                                                               arg_dictionary['sid'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def delete_mst_vlan_instance(self, arg_dictionary, **kwargs):
        uuid = "934d9114-29cc-4f39-af75-33d5d1c5dc6f"
        cmd = "vlan delete {0}".format(arg_dictionary['vlan'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_mstp_on_port(self, arg_dictionary, **kwargs):
        uuid = "297a76aa-f908-41a3-ab44-d12772fe91c6"
        cmd = "spanning-tree mstp force-port-state enable"
        prompt = "intfPrompt"
        prompt_args = "GigabitEthernet {0}".format(arg_dictionary['port'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def disable_mstp_on_port(self, arg_dictionary, **kwargs):
        uuid = "19af32a6-2617-4a02-9f03-4fe8064bf8b5"
        cmd = "no spanning-tree mstp force-port-state enable"
        prompt = "intfPrompt"
        prompt_args = "GigabitEthernet {0}".format(arg_dictionary['port'])
        conf = "(y/n)"
        conf_args = "y"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args, conf=conf, conf_args=conf_args)

    def enable_bpduguard(self, arg_dictionary, **kwargs):
        uuid = "21bc4f3f-57ec-488a-b6a4-d00266a74697"
        cmd = "interface GigabitEthernet {0}||spanning-tree bpduguard enable".format(arg_dictionary['port'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_bpduguard(self, arg_dictionary, **kwargs):
        uuid = "cc77f789-2c8d-4286-8fd5-7070f8c761fd"
        cmd = "interface GigabitEthernet {0}||spanning-tree bpduguard enable".format(arg_dictionary['port'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_boot_flag_rstp(self, arg_dictionary, **kwargs):
        uuid = "6fb3cfae-7b6c-4d5b-86e0-b6c4363cdba0"
        cmd = "boot config flags spanning-tree-mode rstp"
        prompt = "routerConfigPrompt"
        conf = "Warning:"
        conf_args = "save configuration||reset -y"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf, conf_args=conf_args)

    def set_boot_flag_mstp(self, arg_dictionary, **kwargs):
        uuid = "57c6dfb5-9d58-43be-8e43-fb92d6903488"
        cmd = "boot config flags spanning-tree-mode mstp"
        prompt = "routerConfigPrompt"
        conf = "Warning:"
        conf_args = "save configuration||reset -y"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf, conf_args=conf_args)

    def set_bpduguard_timeout(self, arg_dictionary, **kwargs):
        uuid = "eb8e550b-5d1a-4534-bab6-ce3b68d857b3"
        cmd = "interface GigabitEthernet {0}||spanning-tree bpduguard timeout {1}".format(arg_dictionary['port'],
                                                                                          arg_dictionary['timeout'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_bpduguard_timeout(self, arg_dictionary, **kwargs):
        uuid = "4a4c61e4-ace5-43fd-ab08-88c0ea57092a"
        cmd = "interface GigabitEthernet {0}||spanning-tree bpduguard timeout 120".format(arg_dictionary['port'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_info_detail(self, arg_dictionary, **kwargs):
        uuid = "c1bd6514-2f30-4b28-af6b-795c8bcdf237"
        cmd = "show spanning-tree rstp status"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_info_summary(self, arg_dictionary, **kwargs):
        uuid = "636c4458-6a76-413b-b9d1-a08a2de9ed2a"
        cmd = "show spanning-tree rstp config"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port_info(self, arg_dictionary, **kwargs):
        uuid = "d84bd022-69d9-4eee-b18f-3b23b8a5d0a2"
        cmd = "show spanning-tree rstp port config {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port_info_detail(self, arg_dictionary, **kwargs):
        uuid = "bc473c5d-6e99-42b2-bf7d-c83b0d04e9f0"
        cmd = "show spanning-tree rstp port config {0}||show spanning-tree rstp port status {1}".format(arg_dictionary['port'],
                                                                                                        arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_version(self, arg_dictionary, **kwargs):
        uuid = "538adba9-e73c-4fe7-994e-750762b8c5ee"
        cmd = "show spanning-tree config"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port_admin(self, arg_dictionary, **kwargs):
        uuid = "9d55386e-ad6d-4a74-b207-d3bface7d346"
        cmd = "show spanning-tree rstp port role {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port_edge(self, arg_dictionary, **kwargs):
        uuid = "ecfe168e-155e-45ea-b3db-f9780afe7254"
        cmd = "show spanning-tree rstp port config {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port_role(self, arg_dictionary, **kwargs):
        uuid = "441cd158-f7b5-44c7-9e1b-48d36742e844"
        cmd = "show spanning-tree rstp port role {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_boot_flag(self, arg_dictionary, **kwargs):
        uuid = "2ccba41f-a300-4d78-95ea-205ebae46b32"
        cmd = "show boot config flags"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_bpduguard(self, arg_dictionary, **kwargs):
        uuid = "c76489fd-79cb-40c4-91a5-44ed96f62912"
        cmd = "show spanning-tree bpduguard {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_mstp_info_detail(self, arg_dictionary, **kwargs):
        uuid = "e1fc0d55-1412-4da7-a85c-f30a8bd7c63a"
        cmd = "show spanning-tree mstp status"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_mstp_info_summary(self, arg_dictionary, **kwargs):
        uuid = "3a0e0848-5bd4-4dfc-9a21-8b4f5bd6ceb2"
        cmd = "show spanning-tree mstp config"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_mstp_instance_info(self, arg_dictionary, **kwargs):
        uuid = "23ef58df-efd7-426e-aa93-61a777a2ca29"
        cmd = "show spanning-tree mstp msti config s{0}".format(arg_dictionary['sid'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_mstp_port_info(self, arg_dictionary, **kwargs):
        uuid = "4af92ed0-14f1-4dfc-87f7-c856b79bdc82"
        cmd = "show spanning-tree mstp port config {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_mstp_port_info_detail(self, arg_dictionary, **kwargs):
        uuid = "98236257-3284-4425-8f58-e743d339939c"
        cmd = "show spanning-tree mstp port config {0}||show spanning-tree mstp port status {1}".format(arg_dictionary['port'],
                                                                                                        arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_mstp_port_role(self, arg_dictionary, **kwargs):
        uuid = "18c73d6a-7c48-47e3-b814-2049062a62d4"
        cmd = "show spanning-tree mstp port role {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_mstp_port_admin(self, arg_dictionary, **kwargs):
        uuid = "36d8cdc9-c6b3-4f8b-82de-e5398c54528c"
        cmd = "show spanning-tree mstp port role {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_mstp_edge(self, arg_dictionary, **kwargs):
        uuid = "3445779c-cbf5-44ee-9cd6-8b7e6aff2e01"
        cmd = "show spanning-tree mstp port config {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_stp_port_role(self, arg_dictionary, **kwargs):
        uuid = "ce22c661-e033-461a-a7a5-2019d548ed04"
        cmd = "show spanning-tree {0} port role {1}".format(arg_dictionary['stp_type'],
                                                            arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
