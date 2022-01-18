"""
All port supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.port.base.portbase import PortBase


class Port(DeviceApi, PortBase):
    def __init__(self, device_input):
        super(Port, self).__init__(device_input)

    def enable_state(self, arg_dictionary, **kwargs):
        uuid = "97f025f1-a7f6-44b9-a118-33ddff5ef15a"
        cmd = "enable ports {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_state(self, arg_dictionary, **kwargs):
        uuid = "62c8985e-e0eb-46fc-aaa1-409eaab3d702"
        cmd = "disable ports {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_jumbo(self, arg_dictionary, **kwargs):
        uuid = "b7eee19b-7245-4369-8778-1a8f4f3f0b29"
        cmd = "enable jumbo-frame ports {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_jumbo(self, arg_dictionary, **kwargs):
        uuid = "b2215268-4e83-4d0a-ba2d-75e40438e3fd"
        cmd = "disable jumbo-frame ports {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_speed(self, arg_dictionary, **kwargs):
        uuid = "538ae084-d666-4980-ac02-2b6a17f3167c"
        cmd = "configure port {0} auto {1} speed {2} duplex {3}".format(arg_dictionary['port'],
                                                                        arg_dictionary['state'],
                                                                        arg_dictionary['speed'],
                                                                        arg_dictionary['duplex'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_speed(self, arg_dictionary, **kwargs):
        uuid = "9b736e06-72a2-4bdc-bddf-1222c16ac04e"
        cmd = "configure port {0} auto on".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_rate_egress_mbps(self, arg_dictionary, **kwargs):
        uuid = "ee8358af-ab27-416c-83ae-038b6b9d2b60"
        cmd = "configure port {0} rate-limit egress {1} Mbps".format(arg_dictionary['port'],
                                                                     arg_dictionary['rate'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_rate_egress_gbps(self, arg_dictionary, **kwargs):
        uuid = "aece5b75-5a3f-4dd0-9898-ec02174656ff"
        cmd = "configure port {0} rate-limit egress {1} Gbps".format(arg_dictionary['port'],
                                                                     arg_dictionary['rate'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_rate_egress_kbps(self, arg_dictionary, **kwargs):
        uuid = "54127682-0ec3-4a86-8ff2-7e6c9082d60a"
        cmd = "configure port {0} rate-limit egress {1} Kbps".format(arg_dictionary['port'],
                                                                     arg_dictionary['rate'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_rate_egress_no_limit(self, arg_dictionary, **kwargs):
        uuid = "093f13b2-e8a0-46dd-94e2-3abcfa11c450"
        cmd = "configure port {0} rate-limit egress no-limit".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_rate_flood_bcast(self, arg_dictionary, **kwargs):
        uuid = "c64ae3dc-01d2-4808-88b8-c17ba3838a9f"
        cmd = "configure port {0} rate-limit flood broadcast {1}".format(arg_dictionary['port'],
                                                                         arg_dictionary['rate'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_rate_flood_mcast(self, arg_dictionary, **kwargs):
        uuid = "be2c7b98-9550-45e2-9178-34259c288e1c"
        cmd = "configure port {0} rate-limit flood multicast {1}".format(arg_dictionary['port'],
                                                                         arg_dictionary['rate'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_rate_flood_unknown(self, arg_dictionary, **kwargs):
        uuid = "42289171-2ebc-4c10-b618-045961049356"
        cmd = "configure port {0} rate-limit flood unknown-destmac {1}".format(arg_dictionary['port'],
                                                                               arg_dictionary['rate'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_restart(self, arg_dictionary, **kwargs):
        uuid = "ab98d9fa-b817-4b98-8f10-e6c0abd11cb1"
        cmd = "restart ports {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_all_jumbo(self, arg_dictionary, **kwargs):
        uuid = "d2f74ec7-e0cc-471b-8a17-5e4fdda8a9cd"
        cmd = "show ports {0} information ".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_alias(self, arg_dictionary, **kwargs):
        uuid = "f8cfdc6c-0c9c-42f7-a581-ca70dd23eb75"
        cmd = "show ports {0} information detail".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_admin_status(self, arg_dictionary, **kwargs):
        uuid = "aff4e031-7493-4728-9ed5-dd640c8ee2b0"
        cmd = "show ports {0} information detail".format(arg_dictionary['port'])
        prompt = "userPrompt"

        self.device.error_checker.add_error_to_ignore_list(*["Forward-Error-Correction"])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_oper_status(self, arg_dictionary, **kwargs):
        uuid = "75ffd61b-7b99-47dc-8deb-b96577bcf6e8"
        cmd = "show ports {0} information detail".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_mtu(self, arg_dictionary, **kwargs):
        uuid = "1439a54f-38a7-465e-8454-e22ea92fbd99"
        cmd = "show ports {0} information detail".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_mac_address(self, arg_dictionary, **kwargs):
        uuid = "59ecc15f-826e-4e0a-a021-0d2cd792ff4e"
        cmd = "show ports {0} information detail".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_high_speed(self, arg_dictionary, **kwargs):
        uuid = "5047b112-5de9-4ab0-96e9-9620c4a69d7f"
        cmd = "show ports {0} information detail".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_in_octets(self, arg_dictionary, **kwargs):
        uuid = "c97a2828-cbb8-412f-a9dc-c80850707c4e"
        cmd = "show port {0} statistics no-refresh".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_in_unicast_packets(self, arg_dictionary, **kwargs):
        uuid = "c4fa7bf2-eccd-4429-8b56-65330536c009"
        cmd = "show port {0} statistics no-refresh".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_in_discard_packets(self, arg_dictionary, **kwargs):
        uuid = "8c0bf5fb-5640-433a-a881-c756634ff522"
        cmd = "show port {0} statistics no-refresh".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_in_error_packets(self, arg_dictionary, **kwargs):
        uuid = "1d564800-6b86-47a9-839d-ec55341e0cf7"
        cmd = "show port {0} statistics no-refresh".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_out_octets(self, arg_dictionary, **kwargs):
        uuid = "b316b446-81fc-416b-97f4-c0e2fcf4ce92"
        cmd = "show port {0} statistics no-refresh".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_out_unicast_packets(self, arg_dictionary, **kwargs):
        uuid = "ee8c50ae-7a0e-4ea3-afb5-335c9a2deb62"
        cmd = "show port {0} statistics no-refresh".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_out_discard_packets(self, arg_dictionary, **kwargs):
        uuid = "29555c1c-b7f5-40b3-b1e1-607044c7c3ba"
        cmd = "show port {0} statistics no-refresh".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_out_error_packets(self, arg_dictionary, **kwargs):
        uuid = "f2aeac12-dcba-447d-834d-64bb54cb8663"
        cmd = "show port {0} statistics no-refresh".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_in_multicast_packets(self, arg_dictionary, **kwargs):
        uuid = "f531cc1c-a829-4d10-9ab9-e6cead126d86"
        cmd = "show port {0} statistics no-refresh".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_in_broadcast_packets(self, arg_dictionary, **kwargs):
        uuid = "06201eb5-eaca-4f97-8f06-c3e33e9145e4"
        cmd = "show port {0} statistics no-refresh".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_out_multicast_packets(self, arg_dictionary, **kwargs):
        uuid = "fd5f8d0a-de0a-4b0a-b057-e6ace49a50a5"
        cmd = "show port {0} statistics no-refresh".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_out_broadcast_packets(self, arg_dictionary, **kwargs):
        uuid = "ec4979b9-2cec-4435-9230-7151450950a2"
        cmd = "show port {0} statistics no-refresh".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_64_bit_in_octets(self, arg_dictionary, **kwargs):
        uuid = "8b0b5333-d713-4031-b03a-bc33f2fd3851"
        cmd = "show port {0} statistics no-refresh".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_64_bit_in_unicast_packets(self, arg_dictionary, **kwargs):
        uuid = "6c0ae132-a890-4b1b-a768-81b84718642e"
        cmd = "show port {0} statistics no-refresh".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_64_bit_in_multicast_packets(self, arg_dictionary, **kwargs):
        uuid = "6f1f06a6-23b6-429d-a35d-fdaadf610a6a"
        cmd = "show port {0} statistics no-refresh".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_64_bit_in_broadcast_packets(self, arg_dictionary, **kwargs):
        uuid = "522c2b65-b2fc-414d-88a1-ffac3b0667bf"
        cmd = "show port {0} statistics no-refresh".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_64_bit_out_octets(self, arg_dictionary, **kwargs):
        uuid = "45e50d85-560f-4b1f-ba2d-8d6d3738bbe3"
        cmd = "show port {0} statistics no-refresh".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_64_bit_out_unicast_packets(self, arg_dictionary, **kwargs):
        uuid = "10f79368-469e-4404-981a-f0fdd73c6217"
        cmd = "show port {0} statistics no-refresh".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_64_bit_out_multicast_packets(self, arg_dictionary, **kwargs):
        uuid = "0f38c025-d773-4826-af6e-d2cb9b9e5d7d"
        cmd = "show port {0} statistics no-refresh".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_64_bit_out_broadcast_packets(self, arg_dictionary, **kwargs):
        uuid = "b470bad8-9ba7-40ca-9777-2ee7836b4806"
        cmd = "show port {0} statistics no-refresh".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_rate_limit(self, arg_dictionary, **kwargs):
        uuid = "b0b2f661-be78-4551-bcae-62d21baf79d0"
        cmd = "show ports {0} information detail".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_advertised(self, arg_dictionary, **kwargs):
        uuid = "1c2ce739-a568-4ee6-b211-3b8b1217cfb0"
        cmd = "show ports {0} advertised".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
