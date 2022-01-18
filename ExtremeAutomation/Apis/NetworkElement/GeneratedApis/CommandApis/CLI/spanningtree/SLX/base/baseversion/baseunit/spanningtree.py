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
        cmd = "protocol spanning-tree stp"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_global(self, arg_dictionary, **kwargs):
        uuid = "bcdfcb77-c269-4562-a0ec-597bbac5214c"
        cmd = "protocol spanning-tree stp||shutdown"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_mstp_global(self, arg_dictionary, **kwargs):
        uuid = "42f1f766-feb0-45c6-b64d-cebe1d91dcff"
        cmd = "protocol spanning-tree mstp"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_mstp_global(self, arg_dictionary, **kwargs):
        uuid = "b7afd649-658a-4a5c-81d8-235684d33470"
        cmd = "protocol spanning-tree mstp||shutdown"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_rstp_global(self, arg_dictionary, **kwargs):
        uuid = "76376f63-5b96-4e54-8c9b-1d06241f78fe"
        cmd = "protocol spanning-tree rstp"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_rstp_global(self, arg_dictionary, **kwargs):
        uuid = "7f13a4ce-84cd-414d-9f92-892cb2705088"
        cmd = "protocol spanning-tree rstp||shutdown"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_auto_edge(self, arg_dictionary, **kwargs):
        uuid = "c7c9f88e-ef19-491f-a9fe-ca577375b7f4"
        cmd = "interface ethernet {0}||spanning-tree autoedge".format(arg_dictionary['port'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_auto_edge(self, arg_dictionary, **kwargs):
        uuid = "096ef5df-1a36-4387-8082-7d441782c70b"
        cmd = "interface ethernet {0}||no spanning-tree autoedge".format(arg_dictionary['port'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_restricted_role(self, arg_dictionary, **kwargs):
        uuid = "cae234b7-a797-43f4-8530-553aaa45d037"
        cmd = "interface ethernet {0}||spanning-tree restricted-role".format(arg_dictionary['port'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_restricted_tcn(self, arg_dictionary, **kwargs):
        uuid = "ececba25-0636-48d9-a542-eaa1c1721291"
        cmd = "interface ethernet {0}||spanning-tree restricted-tcn".format(arg_dictionary['port'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_priority(self, arg_dictionary, **kwargs):
        uuid = "deda1330-9d1e-4073-9f84-c83b776f751a"
        cmd = "interface ethernet {0}||spanning-tree priority {1}".format(arg_dictionary['port'],
                                                                          arg_dictionary['priority'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_mst_region_name(self, arg_dictionary, **kwargs):
        uuid = "b5a10760-b5ab-47c4-a493-431a4a594df0"
        cmd = "protocol spanning-tree mstp||region {0}".format(arg_dictionary['region'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_mst_revision_level(self, arg_dictionary, **kwargs):
        uuid = "625db2cb-e475-4068-bfba-1f10033d7312"
        cmd = "protocol spanning-tree mstp||revision {0}".format(arg_dictionary['revision'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_port_link_type_point_to_point(self, arg_dictionary, **kwargs):
        uuid = "11ab7305-fd4a-48f0-ad0c-510934db0493"
        cmd = "interface ethernet {0}||spanning-tree link-type point-to-point".format(arg_dictionary['port'])
        prompt = "routerConfigPrompt"
        conf = "Warning:"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf)

    def set_port_link_type_edge(self, arg_dictionary, **kwargs):
        uuid = "88bc889e-d8f7-4723-8476-203e246d7669"
        cmd = "interface ethernet {0}||spanning-tree edgeport".format(arg_dictionary['port'])
        prompt = "routerConfigPrompt"
        conf = "Warning:"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf)

    def enable_bpduguard(self, arg_dictionary, **kwargs):
        uuid = "21bc4f3f-57ec-488a-b6a4-d00266a74697"
        cmd = "interface ethernet {0}||spanning-tree edgeport bpdu-guard".format(arg_dictionary['port'])
        prompt = "routerConfigPrompt"
        conf = "Warning:"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf)

    def disable_bpduguard(self, arg_dictionary, **kwargs):
        uuid = "cc77f789-2c8d-4286-8fd5-7070f8c761fd"
        cmd = "interface ethernet {0}||no spanning-tree edgeport bpdu-guard".format(arg_dictionary['port'])
        prompt = "routerConfigPrompt"
        conf = "Warning:"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf)

    def show_info_detail(self, arg_dictionary, **kwargs):
        uuid = "c1bd6514-2f30-4b28-af6b-795c8bcdf237"
        cmd = "show spanning-tree"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_info_summary(self, arg_dictionary, **kwargs):
        uuid = "636c4458-6a76-413b-b9d1-a08a2de9ed2a"
        cmd = "show spanning-tree"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_mstp_info_summary(self, arg_dictionary, **kwargs):
        uuid = "3a0e0848-5bd4-4dfc-9a21-8b4f5bd6ceb2"
        cmd = "show spanning-tree mst"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
