"""
All vpex supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.vpex.base.vpexbase import VpexBase


class Vpex(DeviceApi, VpexBase):
    def __init__(self, device_input):
        super(Vpex, self).__init__(device_input)

    def enable_global(self, arg_dictionary, **kwargs):
        uuid = "ad5e8fd5-07f8-4894-a55a-66207c4141ad"
        cmd = "enable vpex"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_global(self, arg_dictionary, **kwargs):
        uuid = "3a292f45-5876-478a-b74d-d77acdbb1899"
        cmd = "disable vpex"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_auto_configuration(self, arg_dictionary, **kwargs):
        uuid = "457451ee-6dfc-4c54-8188-a8dd65cab4aa"
        cmd = "enable vpex auto-configuration"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_auto_configuration(self, arg_dictionary, **kwargs):
        uuid = "ac3de84b-ca95-4ade-ad84-d0a5ccce75ed"
        cmd = "disable vpex auto-configuration"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_ports(self, arg_dictionary, **kwargs):
        uuid = "fcd6f07b-9815-49cd-902c-8037df898def"
        cmd = "configure vpex ports {0} slot {1}".format(arg_dictionary['port'],
                                                         arg_dictionary['slot'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_ports(self, arg_dictionary, **kwargs):
        uuid = "c93965cf-c7c6-4699-a240-fb69d14c0e72"
        cmd = "unconfigure vpex ports {0} slot".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_ring_rebalancing_auto(self, arg_dictionary, **kwargs):
        uuid = "38d8b33b-d2d7-4551-a008-af9dbcc390c4"
        cmd = "configure vpex ring rebalancing auto"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_ring_rebalancing_off(self, arg_dictionary, **kwargs):
        uuid = "e86cc601-ec3c-4e0e-b84e-be7957d7bb7b"
        cmd = "configure vpex ring rebalancing off"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_info(self, arg_dictionary, **kwargs):
        uuid = "ecdf3468-4f27-458b-a3d8-6991cc1058a3"
        cmd = "show vpex"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_bpe(self, arg_dictionary, **kwargs):
        uuid = "81e59da1-f439-484c-9eb6-1c0d87ef8f8c"
        cmd = "show vpex bpe"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_bpe_cpu_utilization(self, arg_dictionary, **kwargs):
        uuid = "947ebd0f-f016-409c-8335-0ddf1a9c29ca"
        cmd = "show vpex bpe cpu-utilization"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_bpe_environment(self, arg_dictionary, **kwargs):
        uuid = "ff52a45c-fc43-4278-b1a8-40e0ea6930d5"
        cmd = "show vpex bpe environment"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_bpe_version_detail(self, arg_dictionary, **kwargs):
        uuid = "25b07336-d377-4829-9af7-2a99708cd7d3"
        cmd = "show vpex bpe version detail"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_bpe_slot(self, arg_dictionary, **kwargs):
        uuid = "0d74db1c-fb40-4f02-a0b1-0b50c710c1c9"
        cmd = "show vpex bpe slot {0}".format(arg_dictionary['slot'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_bpe_slot_cpu_utilization(self, arg_dictionary, **kwargs):
        uuid = "c54304ee-306a-4eab-a4c8-de90af1cfb05"
        cmd = "show vpex bpe slot {0} cpu-utilization".format(arg_dictionary['slot'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_bpe_slot_environment(self, arg_dictionary, **kwargs):
        uuid = "732ab290-1c9d-49fe-b914-636100d7a955"
        cmd = "show vpex bpe slot {0} environment".format(arg_dictionary['slot'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_bpe_slot_statistics(self, arg_dictionary, **kwargs):
        uuid = "af6062d7-c305-4906-a534-dfb50525f3c1"
        cmd = "show vpex bpe slot {0} statistics".format(arg_dictionary['slot'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_bpe_slot_statistics_detail(self, arg_dictionary, **kwargs):
        uuid = "962d7438-5b93-43f5-acc4-94207b5fc057"
        cmd = "show vpex bpe slot {0} statistics detail".format(arg_dictionary['slot'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_bpe_slot_version_detail(self, arg_dictionary, **kwargs):
        uuid = "67b838a9-c612-442a-b6d0-894430f3b7ba"
        cmd = "show vpex bpe slot {0} version detail".format(arg_dictionary['slot'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_bpe_statistics(self, arg_dictionary, **kwargs):
        uuid = "eacb83c3-d0df-4e4a-8870-bc10aeddf7c3"
        cmd = "show vpex bpe statistics"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_bpe_statistics_detail(self, arg_dictionary, **kwargs):
        uuid = "7b0432d1-3248-4741-9e22-0d41ce332e66"
        cmd = "show vpex bpe statistics detail"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_bpe_statistics_detail_slot(self, arg_dictionary, **kwargs):
        uuid = "8e7e3dc3-9ae6-41d4-a52e-dd5dd6c542d7"
        cmd = "show vpex bpe statistics detail slot {0}".format(arg_dictionary['slot'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_ports(self, arg_dictionary, **kwargs):
        uuid = "13c1c7fe-de4a-4ce6-931b-43fa7a982ab5"
        cmd = "show vpex ports"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_ports_ecp_statistics(self, arg_dictionary, **kwargs):
        uuid = "9e1ce645-6cef-4936-8f9d-866c02141a27"
        cmd = "show vpex ports ecp statistics"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_ports_statistics(self, arg_dictionary, **kwargs):
        uuid = "14b44ec3-2c7e-418f-bd6b-a8badc78487e"
        cmd = "show vpex ports statistics"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_ports_statistics_detail(self, arg_dictionary, **kwargs):
        uuid = "ac0b9010-0ff0-4832-b87e-c85270bc1328"
        cmd = "show vpex ports statistics detail"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_topology(self, arg_dictionary, **kwargs):
        uuid = "65347b7e-7b26-42a5-9ac2-deee0ca4b633"
        cmd = "show vpex topology"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_topology_detail(self, arg_dictionary, **kwargs):
        uuid = "7409021b-1d64-48ba-9686-b41a0778ec59"
        cmd = "show vpex topology detail"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_topology_detail_port(self, arg_dictionary, **kwargs):
        uuid = "a232b920-dddc-4fe0-bb3c-0538dee1b353"
        cmd = "show vpex topology detail port {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_topology_port(self, arg_dictionary, **kwargs):
        uuid = "00c5c177-da18-4803-8685-d8812613fa6f"
        cmd = "show vpex topology port {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_topology_port_detail(self, arg_dictionary, **kwargs):
        uuid = "07630d62-e451-4c60-ada5-46f6cdcfa80e"
        cmd = "show vpex topology port {0} detail".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_topology_port_summary(self, arg_dictionary, **kwargs):
        uuid = "df64854b-5837-4bd0-81e2-98b0864c4704"
        cmd = "show vpex topology port {0} summary".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_topology_summary(self, arg_dictionary, **kwargs):
        uuid = "359e087e-ae2c-439e-9382-69f0ab9ec8a4"
        cmd = "show vpex topology summary"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_topology_summary_port(self, arg_dictionary, **kwargs):
        uuid = "24b2b1b3-3f53-40f3-a272-f63dd7e9c45a"
        cmd = "show vpex topology summary port {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
