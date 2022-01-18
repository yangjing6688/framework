"""
All hostutils supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.hostutils.base.hostutilsbase import \
    HostutilsBase


class Hostutils(DeviceApi, HostutilsBase):
    def __init__(self, device_input):
        super(Hostutils, self).__init__(device_input)

    def ping_host(self, arg_dictionary, **kwargs):
        uuid = "57c52793-0d02-4f7f-b5b2-53bcd3024df4"
        cmd = "ping {0} count {1} -t {2}".format(arg_dictionary['host_address'],
                                                 arg_dictionary['count'],
                                                 arg_dictionary['timeout'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def l2_ping_ipaddr(self, arg_dictionary, **kwargs):
        uuid = "b865ec88-e01c-47da-b928-d8cacd8278fb"
        cmd = "l2 ping ip-address {0}".format(arg_dictionary['ip_address'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def l2_ping_ipaddr_burst(self, arg_dictionary, **kwargs):
        uuid = "e826a9f3-d167-4d9a-b4b2-e24b370bf180"
        cmd = "l2 ping {0} burst-count {1}".format(arg_dictionary['ip_address'],
                                                   arg_dictionary['burst_count'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def l2_ping_ipaddr_data_tlv_size(self, arg_dictionary, **kwargs):
        uuid = "c03217f7-8d02-4761-82e7-3b34bac7f745"
        cmd = "l2 ping {0} data-tlv-size {1}".format(arg_dictionary['ip_address'],
                                                     arg_dictionary['tlv_size'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def l2_ping_ipaddr_frame_size(self, arg_dictionary, **kwargs):
        uuid = "623c47a7-9076-4190-adb5-81f2fbf456d9"
        cmd = "l2 ping {0} frame-size {1}".format(arg_dictionary['ip_address'],
                                                  arg_dictionary['frame_size'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def l2_ping_ipaddr_time_out(self, arg_dictionary, **kwargs):
        uuid = "e1f7fe5f-bcef-48f2-be42-169b60e75f74"
        cmd = "l2 ping {0} time-out {1}".format(arg_dictionary['ip_address'],
                                                arg_dictionary['time_out'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def l2_ping_ipaddr_vrf(self, arg_dictionary, **kwargs):
        uuid = "84b7d926-79ed-4786-a361-cf64e19e291d"
        cmd = "l2 ping ip-address {0} vrf {1}".format(arg_dictionary['ip_address'],
                                                      arg_dictionary['vrf_name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def l2_ping_vlan_mac(self, arg_dictionary, **kwargs):
        uuid = "e5e1cf1f-1bc4-429b-90e5-3e5b97f180f7"
        cmd = "l2 ping vlan {0} mac {1}".format(arg_dictionary['vlan'],
                                                arg_dictionary['mac_address'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def l2_ping_vlan_routernodename(self, arg_dictionary, **kwargs):
        uuid = "876087e1-0ccd-4062-9b8a-eafd8b806609"
        cmd = "l2 ping {0} routernodename {1}".format(arg_dictionary['vlan'],
                                                      arg_dictionary['node_name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def l2_ping_vlan_routernodename_burst(self, arg_dictionary, **kwargs):
        uuid = "2f5e3a17-79c6-45dd-a236-464eb043f19c"
        cmd = "l2 ping {0} routernodename {1} burst-count {2}".format(arg_dictionary['vlan'],
                                                                      arg_dictionary['node_name'],
                                                                      arg_dictionary['burst_count'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def l2_ping_vlan_routernodename_data_tlv_size(self, arg_dictionary, **kwargs):
        uuid = "3317ad1e-b519-441e-a82b-1fe05a4f4624"
        cmd = "l2 ping {0} routernodename {1} data-tlv-size {2}".format(arg_dictionary['vlan'],
                                                                        arg_dictionary['node_name'],
                                                                        arg_dictionary['tlv_size'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def l2_ping_vlan_routernodename_frame_size(self, arg_dictionary, **kwargs):
        uuid = "03afaf76-43a1-4599-97e9-5122edaee6e5"
        cmd = "l2 ping {0} routernodename {1} frame_size {2}".format(arg_dictionary['vlan'],
                                                                     arg_dictionary['node_name'],
                                                                     arg_dictionary['frame_size'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def l2_ping_vlan_routernodename_priority(self, arg_dictionary, **kwargs):
        uuid = "a1e82a3d-52f1-418a-bda1-2ba2d7a063d0"
        cmd = "l2 ping {0} routernodename {1} priority {2}".format(arg_dictionary['vlan'],
                                                                   arg_dictionary['node_name'],
                                                                   arg_dictionary['priority'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def l2_ping_vlan_routernodename_source_mode_nodal(self, arg_dictionary, **kwargs):
        uuid = "dd8b8868-c9e0-46e7-948b-666d60ac7683"
        cmd = "l2 ping {0} routernodename {1} source-mode nodal".format(arg_dictionary['vlan'],
                                                                        arg_dictionary['node_name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def l2_ping_vlan_routernodename_source_mode_novlanmac(self, arg_dictionary, **kwargs):
        uuid = "1bf7c148-23fd-4220-9961-7894422c0806"
        cmd = "l2 ping {0} routernodename {1} source-mode novlanmac".format(arg_dictionary['vlan'],
                                                                            arg_dictionary['node_name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def l2_ping_vlan_routernodename_testfill_pattern_all_zero(self, arg_dictionary, **kwargs):
        uuid = "66d4d1b0-9b11-4e0e-9c56-c6c35b5e96e6"
        cmd = "l2 ping {0} routernodename {1} testfill-pattern all-zero".format(arg_dictionary['vlan'],
                                                                                arg_dictionary['node_name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def l2_ping_vlan_routernodename_testfill_pattern_all_zero_crc(self, arg_dictionary, **kwargs):
        uuid = "21bc24ec-1323-492a-a818-900f6fcc87ef"
        cmd = "l2 ping {0} routernodename {1} testfill-pattern all-zero-crc".format(arg_dictionary['vlan'],
                                                                                    arg_dictionary['node_name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def l2_ping_vlan_routernodename_testfill_pattern_pseudo_rand_bit_seq(self, arg_dictionary, **kwargs):
        uuid = "93f96795-4070-4447-b3c1-e3d58ce27937"
        cmd = "l2 ping {0} routernodename {1} testfill-pattern pseudo-random-bit-sequence".format(arg_dictionary['vlan'],
                                                                                                  arg_dictionary['node_name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def l2_ping_vlan_routernodename_testfill_pattern_pseudo_rand_bit_seq_crc(self, arg_dictionary, **kwargs):
        uuid = "09e13a76-cb60-4905-82f8-3b3687353048"
        cmd = "l2 ping {0} routernodename {1} testfill-pattern pseudo-random-bit-sequence-crc".format(arg_dictionary['vlan'],
                                                                                                      arg_dictionary['node_name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def l2_ping_vlan_routernodename_timeout(self, arg_dictionary, **kwargs):
        uuid = "71efee42-56ee-4485-915b-e9dc4bd99bb6"
        cmd = "l2 ping {0} routernodename {1} time-out {2}".format(arg_dictionary['vlan'],
                                                                   arg_dictionary['node_name'],
                                                                   arg_dictionary['timeout'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def l2_traceroute_ipaddr(self, arg_dictionary, **kwargs):
        uuid = "b5249415-798c-409e-8847-f9ea9572540c"
        cmd = "l2 traceroute ip-address {0}".format(arg_dictionary['ip_address'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def l2_traceroute_ipaddr_ttl(self, arg_dictionary, **kwargs):
        uuid = "f0854239-db80-4193-9184-792ac5c1527f"
        cmd = "l2 traceroute ip-address {0} ttl-value {1}".format(arg_dictionary['ip_address'],
                                                                  arg_dictionary['ttl'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def l2_traceroute_ipaddr_vrf(self, arg_dictionary, **kwargs):
        uuid = "206ff912-49f4-433d-93a0-93959427859d"
        cmd = "l2 traceroute ip-address {0} vrf {1}".format(arg_dictionary['ip_address'],
                                                            arg_dictionary['vrf_name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def l2_traceroute_vlan_mac(self, arg_dictionary, **kwargs):
        uuid = "4609e598-4735-4f4d-93ed-93c2c645ba6f"
        cmd = "l2 traceroute vlan {0} mac {1}".format(arg_dictionary['vlan'],
                                                      arg_dictionary['mac'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def l2_traceroute_vlan_routernodename_priority(self, arg_dictionary, **kwargs):
        uuid = "0587bdf3-05d3-4686-b780-0640a76a0fd1"
        cmd = "l2 traceroute vlan {0} routernodename {1} priority {2}".format(arg_dictionary['vlan'],
                                                                              arg_dictionary['name'],
                                                                              arg_dictionary['priority'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def l2_traceroute_vlan_routernodename_source_mode_nodal(self, arg_dictionary, **kwargs):
        uuid = "786dcc02-9baf-429f-99f5-c3202b4e8865"
        cmd = "l2 traceroute vlan {0} routernodename {1} source-mode nodal".format(arg_dictionary['vlan'],
                                                                                   arg_dictionary['name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def l2_traceroute_vlan_routernodename_source_mode_novlanmac(self, arg_dictionary, **kwargs):
        uuid = "9dd77c84-6cc7-4673-aafa-4fdcd64ae983"
        cmd = "l2 traceroute vlan {0} routernodename {1} source-mode novlanmac".format(arg_dictionary['vlan'],
                                                                                       arg_dictionary['name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def l2_traceroute_vlan_routernodename_ttl(self, arg_dictionary, **kwargs):
        uuid = "5dd27024-5a9a-4bec-9876-62490a39ea72"
        cmd = "l2 traceroute vlan {0} routernodename {1} ttl-value {2}".format(arg_dictionary['vlan'],
                                                                               arg_dictionary['name'],
                                                                               arg_dictionary['ttl'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def l2_tracetree_vlan_isid(self, arg_dictionary, **kwargs):
        uuid = "81053d9a-5b3b-46a4-93b4-1de3c8954c87"
        cmd = "l2 tracetree vlan {0} isid {1}".format(arg_dictionary['vlan'],
                                                      arg_dictionary['isid'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def l2_tracetree_vlan_isid_mac(self, arg_dictionary, **kwargs):
        uuid = "04cb12b5-4318-4a6c-8828-82cd43cfd723"
        cmd = "l2 tracetree vlan {0} isid mac {1}".format(arg_dictionary['vlan'],
                                                          arg_dictionary['mac'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def l2_tracetree_vlan_isid_priority(self, arg_dictionary, **kwargs):
        uuid = "44b28541-b559-4f40-b9ca-3175235e92eb"
        cmd = "l2 tracetree vlan {0} isid priority {1}".format(arg_dictionary['vlan'],
                                                               arg_dictionary['priority'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def l2_tracetree_vlan_isid_routernodename(self, arg_dictionary, **kwargs):
        uuid = "f67bb98f-1f9c-4107-ac78-495ddc15b4cf"
        cmd = "l2 tracetree vlan {0} isid {1} routernodename {2}".format(arg_dictionary['vlan'],
                                                                         arg_dictionary['isid'],
                                                                         arg_dictionary['name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def l2_tracetree_vlan_isid_routernodename_priority(self, arg_dictionary, **kwargs):
        uuid = "170b5bf4-9943-4328-84a8-b0e2a9b46099"
        cmd = "l2 tracetree vlan {0} isid {1} routernodename {2} priority {3}".format(arg_dictionary['vlan'],
                                                                                      arg_dictionary['isid'],
                                                                                      arg_dictionary['name'],
                                                                                      arg_dictionary['priority'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def l2_tracetree_vlan_isid_routernodename_source_mode_nodal(self, arg_dictionary, **kwargs):
        uuid = "e8f8e6bb-867f-4ce6-a0db-ac446df1dd52"
        cmd = "l2 tracetree vlan {0} isid {1} routernodename {2} source-mode nodal".format(arg_dictionary['vlan'],
                                                                                           arg_dictionary['isid'],
                                                                                           arg_dictionary['name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def l2_tracetree_vlan_isid_routernodename_ttl(self, arg_dictionary, **kwargs):
        uuid = "4eba03ce-76c2-46ee-bd04-415e3d2b93be"
        cmd = "l2 tracetree vlan {0} isid {1} routernodename {2} ttl-value {3}".format(arg_dictionary['vlan'],
                                                                                       arg_dictionary['isid'],
                                                                                       arg_dictionary['name'],
                                                                                       arg_dictionary['ttl'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def l2_tracetree_vlan_isid_source_mode_nodal(self, arg_dictionary, **kwargs):
        uuid = "ecbd065a-1d3b-4dbd-a56f-146a2e29ce7e"
        cmd = "l2 tracetree vlan {0} isid {1} source-mode nodal".format(arg_dictionary['vlan'],
                                                                        arg_dictionary['isid'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def l2_tracetree_vlan_isid_ttl(self, arg_dictionary, **kwargs):
        uuid = "cbb445d9-b372-4fc2-9a8c-8eea9233bb38"
        cmd = "l2 tracetree vlan {0} isid {1} ttl-value {2}".format(arg_dictionary['vlan'],
                                                                    arg_dictionary['isid'],
                                                                    arg_dictionary['ttl'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def l2_tracemroute(self, arg_dictionary, **kwargs):
        uuid = "9ba90ce9-3030-4298-9a31-f35f7d39f872"
        cmd = "l2 tracemroute source {0} group {1}".format(arg_dictionary['source_address'],
                                                           arg_dictionary['group_address'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def l2_tracemroute_priority(self, arg_dictionary, **kwargs):
        uuid = "fd70b7d6-72c3-4d62-bbb2-1ccc2b32d135"
        cmd = "l2 tracemroute source {0} group {1} priority {2}".format(arg_dictionary['source_address'],
                                                                        arg_dictionary['group_address'],
                                                                        arg_dictionary['priority'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def l2_tracemroute_ttl(self, arg_dictionary, **kwargs):
        uuid = "6a382043-bb0d-4def-bc3c-a51cb96632e3"
        cmd = "l2 tracemroute source {0} group {1} ttl-value {2}".format(arg_dictionary['source_address'],
                                                                         arg_dictionary['group_address'],
                                                                         arg_dictionary['ttl'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def l2_tracemroute_vlan(self, arg_dictionary, **kwargs):
        uuid = "7df24a03-94a9-4190-81ed-cd6e0154f12e"
        cmd = "l2 tracemroute source {0} group {1} vlan {2}".format(arg_dictionary['source_address'],
                                                                    arg_dictionary['group_address'],
                                                                    arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def l2_tracemroute_vrf(self, arg_dictionary, **kwargs):
        uuid = "b5a1808c-2079-4ac7-a3b3-685d4fd4a0ec"
        cmd = "l2 tracemroute source {0} group {1} vrf {2}".format(arg_dictionary['source_address'],
                                                                   arg_dictionary['group_address'],
                                                                   arg_dictionary['vrf_name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
