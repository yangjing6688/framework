"""
All spanningtree supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.spanningtree.base.spanningtreebase import \
    SpanningtreeBase


class Spanningtree(DeviceApi, SpanningtreeBase):
    def __init__(self, device_input):
        super(Spanningtree, self).__init__(device_input)

    def enable_global(self, arg_dictionary, **kwargs):
        uuid = "3b6f55e6-7a02-4ec3-8e6b-4791fe167449"
        cmd = "set spantree stpmode ieee8021"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_global(self, arg_dictionary, **kwargs):
        uuid = "bcdfcb77-c269-4562-a0ec-597bbac5214c"
        cmd = "set spantree stpmode none"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def create_mst_instance(self, arg_dictionary, **kwargs):
        uuid = "60227c17-8db3-4021-a178-49179d250d27"
        cmd = "set spantree msti sid {0} create".format(arg_dictionary['sid'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def delete_mst_instance(self, arg_dictionary, **kwargs):
        uuid = "f899a4c0-e5a6-488b-8735-4634c023f36f"
        cmd = "set spantree msti sid {0} delete".format(arg_dictionary['sid'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_port_admin(self, arg_dictionary, **kwargs):
        uuid = "fb42dbbb-4759-410a-9810-bca7e9bd89ad"
        cmd = "set span portadmin {0} enable".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_port_admin(self, arg_dictionary, **kwargs):
        uuid = "4da238d6-8dda-4685-803c-44926e305ea6"
        cmd = "set span portadmin {0} disable".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_auto_edge(self, arg_dictionary, **kwargs):
        uuid = "c7c9f88e-ef19-491f-a9fe-ca577375b7f4"
        cmd = "set spantree autoedge enable"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_auto_edge(self, arg_dictionary, **kwargs):
        uuid = "096ef5df-1a36-4387-8082-7d441782c70b"
        cmd = "set spantree autoedge disable"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_stp_mode(self, arg_dictionary, **kwargs):
        uuid = "92b4464f-52bb-4af1-898b-d56fd39c4191"
        cmd = "set spantree version {0}".format(self.api_utils.eos_stp_mode(arg_dictionary['mode']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_stp_mode(self, arg_dictionary, **kwargs):
        uuid = "2f7f1071-e451-4727-8844-66e25ea247a5"
        cmd = "clear spantree version"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_restricted_role(self, arg_dictionary, **kwargs):
        uuid = "cae234b7-a797-43f4-8530-553aaa45d037"
        cmd = "set spantree restrictedrole {0} {1}".format(arg_dictionary['port'],
                                                           self.api_utils.state_true_false(arg_dictionary['state']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_restricted_tcn(self, arg_dictionary, **kwargs):
        uuid = "ececba25-0636-48d9-a542-eaa1c1721291"
        cmd = "set spantree restrictedtcn {0} {1}".format(arg_dictionary['port'],
                                                          self.api_utils.state_true_false(arg_dictionary['state']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_priority(self, arg_dictionary, **kwargs):
        uuid = "deda1330-9d1e-4073-9f84-c83b776f751a"
        cmd = "set spantree priority {0} {1}".format(arg_dictionary['priority'],
                                                     arg_dictionary['sid'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_priority_mode(self, arg_dictionary, **kwargs):
        uuid = "7fd87379-ff3a-4ec0-bae3-644aa2afbd0f"
        cmd = "set spantree bridgeprioritymode {0}".format(self.api_utils.eos_prio_mode(arg_dictionary['mode']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_tc_trap(self, arg_dictionary, **kwargs):
        uuid = "e86d6ff5-508c-4873-a93c-b41392c95c61"
        cmd = "set spantree tctrapsuppress {0}".format(arg_dictionary['state'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_tc_trap(self, arg_dictionary, **kwargs):
        uuid = "443f3f6c-eac4-4155-8a1f-5be96078a32d"
        cmd = "clear spantree tctrapsuppress"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_msti_vlan_mapping(self, arg_dictionary, **kwargs):
        uuid = "6017e09a-4a1a-40c1-9ddf-d115e9493d53"
        cmd = "set spantree mstmap {0} sid {1}".format(arg_dictionary['vlan'],
                                                       arg_dictionary['sid'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_msti_vlan_mapping(self, arg_dictionary, **kwargs):
        uuid = "4866041a-6d89-40db-b595-48c9c2590edb"
        cmd = "clear spantree mstmap {0}".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_mst_region_name(self, arg_dictionary, **kwargs):
        uuid = "b5a10760-b5ab-47c4-a493-431a4a594df0"
        cmd = "set spantree mstcfgid cfgname {0}".format(arg_dictionary['region'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_mst_revision_level(self, arg_dictionary, **kwargs):
        uuid = "625db2cb-e475-4068-bfba-1f10033d7312"
        cmd = "set spantree mstcfgid rev {0}".format(arg_dictionary['revision'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_hello_time(self, arg_dictionary, **kwargs):
        uuid = "7238ca1e-0519-418e-8768-7c2fbcd5ccb1"
        cmd = "set spantree hello {0}".format(arg_dictionary['hello'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_fwd_delay(self, arg_dictionary, **kwargs):
        uuid = "07dc6524-f57c-40df-a452-3b035f6a3a35"
        cmd = "set spantree fwddelay {0}".format(arg_dictionary['fwd_delay'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_max_age(self, arg_dictionary, **kwargs):
        uuid = "c8504eba-6791-4455-8d32-43e80b6a518d"
        cmd = "set spantree maxage {0}".format(arg_dictionary['max_age'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_info_detail(self, arg_dictionary, **kwargs):
        uuid = "c1bd6514-2f30-4b28-af6b-795c8bcdf237"
        cmd = "show spantree debug"
        prompt = "userPrompt"

        self.device.error_checker.add_error_to_ignore_list(*["Invalid"])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_info_summary(self, arg_dictionary, **kwargs):
        uuid = "636c4458-6a76-413b-b9d1-a08a2de9ed2a"
        cmd = "show spantree stats sid {0}".format(arg_dictionary['sid'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_instance_info(self, arg_dictionary, **kwargs):
        uuid = "e5c3591a-7330-4a93-8805-a16067e5057c"
        cmd = "show spantree stats sid {0}".format(arg_dictionary['sid'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_instance_info_detail(self, arg_dictionary, **kwargs):
        uuid = "70c662b8-4659-4805-b66e-6c755bde121b"
        cmd = "show spantree debug sid {0}".format(arg_dictionary['sid'])
        prompt = "userPrompt"

        self.device.error_checker.add_error_to_ignore_list(*["Invalid"])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port_info(self, arg_dictionary, **kwargs):
        uuid = "d84bd022-69d9-4eee-b18f-3b23b8a5d0a2"
        cmd = "show spantree stats port {0} sid {1}".format(arg_dictionary['port'],
                                                            arg_dictionary['sid'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port_info_detail(self, arg_dictionary, **kwargs):
        uuid = "bc473c5d-6e99-42b2-bf7d-c83b0d04e9f0"
        cmd = "show spantree debug port {0} sid {1}".format(arg_dictionary['port'],
                                                            arg_dictionary['sid'])
        prompt = "userPrompt"

        self.device.error_checker.add_error_to_ignore_list(*["Invalid"])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_version(self, arg_dictionary, **kwargs):
        uuid = "538adba9-e73c-4fe7-994e-750762b8c5ee"
        cmd = "show spantree version"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port_admin(self, arg_dictionary, **kwargs):
        uuid = "9d55386e-ad6d-4a74-b207-d3bface7d346"
        cmd = "show span portadmin port {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_autoedge(self, arg_dictionary, **kwargs):
        uuid = "073792ca-203a-40eb-8d98-01d3e79b5492"
        cmd = "show spantree autoedge"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_mst_digest(self, arg_dictionary, **kwargs):
        uuid = "261d5955-a611-421d-85cf-7f6842a0a70a"
        cmd = "show spantree mstcfg"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
