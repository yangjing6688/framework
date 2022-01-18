"""
All ospf supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.ospf.base.ospfbase import OspfBase


class Ospf(DeviceApi, OspfBase):
    def __init__(self, device_input):
        super(Ospf, self).__init__(device_input)

    def enable_global(self, arg_dictionary, **kwargs):
        uuid = "aad90010-4be0-4857-b591-ff4a17af18be"
        cmd = "enable ospf"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_global(self, arg_dictionary, **kwargs):
        uuid = "f38e1877-724f-4c29-a5c7-1a2dfc41aa2b"
        cmd = "disable ospf"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_router_id(self, arg_dictionary, **kwargs):
        uuid = "6548157c-4534-476f-89fb-ae4539384372"
        cmd = "configure ospf routerid {0}".format(arg_dictionary['router_id'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_router_id(self, arg_dictionary, **kwargs):
        uuid = "43074a74-1bf6-4d37-af45-3339a6a9228f"
        cmd = "configure ospf routerid automatic"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_metric_table_100g(self, arg_dictionary, **kwargs):
        uuid = "d65e2476-bf53-49a7-ae91-d492a7bdd2e1"
        cmd = "configure ospf metric-table 100G {0}".format(arg_dictionary['cost'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_metric_table_100m(self, arg_dictionary, **kwargs):
        uuid = "7d219512-6c32-4b3d-a3a8-fcd70d354a57"
        cmd = "configure ospf metric-table 100M {0}".format(arg_dictionary['cost'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_metric_table_10g(self, arg_dictionary, **kwargs):
        uuid = "66bfeeeb-5c41-4209-9a40-cef2695ac762"
        cmd = "configure ospf metric-table 10G {0}".format(arg_dictionary['cost'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_metric_table_10m(self, arg_dictionary, **kwargs):
        uuid = "c247c47f-1bd7-4d41-bb4a-b568130b07ce"
        cmd = "configure ospf metric-table 10M {0}".format(arg_dictionary['cost'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_metric_table_1g(self, arg_dictionary, **kwargs):
        uuid = "d3ef5e25-1c48-4e15-8cdc-fd1c894c514b"
        cmd = "configure ospf metric-table 1G {0}".format(arg_dictionary['cost'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_metric_table_2dot5g(self, arg_dictionary, **kwargs):
        uuid = "a201e959-4f32-422f-8b89-950556527194"
        cmd = "configure ospf metric-table 2.5G {0}".format(arg_dictionary['cost'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_metric_table_25g(self, arg_dictionary, **kwargs):
        uuid = "0c46e7a3-6018-49c5-bee2-d8197400aca8"
        cmd = "configure ospf metric-table 25G {0}".format(arg_dictionary['cost'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_metric_table_40g(self, arg_dictionary, **kwargs):
        uuid = "008f679a-851b-4c9b-93cb-5c63daf1c7b0"
        cmd = "configure ospf metric-table 40G {0}".format(arg_dictionary['cost'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_metric_table_50g(self, arg_dictionary, **kwargs):
        uuid = "9d28b706-bba7-4c62-8269-d8676a6e18cd"
        cmd = "configure ospf metric-table 50G {0}".format(arg_dictionary['cost'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_metric_table_5g(self, arg_dictionary, **kwargs):
        uuid = "07edcb0d-d8db-4067-bb7d-e607b2ab80b5"
        cmd = "configure ospf metric-table 5G {0}".format(arg_dictionary['cost'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_vlan_auth_md5(self, arg_dictionary, **kwargs):
        uuid = "9b280edc-6252-47e9-ad38-da7bb7b83a4a"
        cmd = "configure ospf vlan {0} authentication md5 {1} {2}".format(arg_dictionary['vlan'],
                                                                          arg_dictionary['key_id'],
                                                                          arg_dictionary['key'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_vlan_auth_none(self, arg_dictionary, **kwargs):
        uuid = "439fdd96-8672-45df-be44-5326a03d5739"
        cmd = "configure ospf vlan {0} authentication none".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_add_vlan(self, arg_dictionary, **kwargs):
        uuid = "fc1dd197-214f-4192-bafd-06b3278c0067"
        cmd = "configure ospf add vlan {0} area {1}".format(arg_dictionary['vlan'],
                                                            arg_dictionary['area'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_del_vlan(self, arg_dictionary, **kwargs):
        uuid = "1303aa7a-4736-41ea-bd9a-7d447edfc640"
        cmd = "configure ospf delete vlan {0}".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_info(self, arg_dictionary, **kwargs):
        uuid = "7cb9490c-58e2-4982-a677-dffd12962348"
        cmd = "show ospf"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_neighbor(self, arg_dictionary, **kwargs):
        uuid = "713eab98-b780-42f0-af6b-ddc205be6cec"
        cmd = "show ospf neighbor"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_vlan_interface(self, arg_dictionary, **kwargs):
        uuid = "35b16b05-2cb2-42d9-bcff-849392b7a49b"
        cmd = "show ospf interface vlan {0}".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
