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
        cmd = "no shutdown"
        prompt = "intfPrompt"
        prompt_args = "GigabitEthernet {0}".format(arg_dictionary['port'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def disable_state(self, arg_dictionary, **kwargs):
        uuid = "62c8985e-e0eb-46fc-aaa1-409eaab3d702"
        cmd = "shutdown"
        prompt = "intfPrompt"
        prompt_args = "GigabitEthernet {0}".format(arg_dictionary['port'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def enable_flex_uni(self, arg_dictionary, **kwargs):
        uuid = "2b1c6baf-48a0-41b9-94a8-037e4dfd8d81"
        cmd = "flex-uni enable"
        prompt = "intfPrompt"
        prompt_args = "GigabitEthernet {0}".format(arg_dictionary['port'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def disable_flex_uni(self, arg_dictionary, **kwargs):
        uuid = "b5a2fb20-a78c-4321-a3d3-e9d362a54665"
        cmd = "no flex-uni enable"
        prompt = "intfPrompt"
        prompt_args = "GigabitEthernet {0}".format(arg_dictionary['port'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_alias(self, arg_dictionary, **kwargs):
        uuid = "26939b7a-06a4-4759-99fa-76dc9caf1515"
        cmd = "name {0}".format(arg_dictionary['name'])
        prompt = "intfPrompt"
        prompt_args = "GigabitEthernet {0}".format(arg_dictionary['port'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def show_alias(self, arg_dictionary, **kwargs):
        uuid = "f8cfdc6c-0c9c-42f7-a581-ca70dd23eb75"
        cmd = "show interface GigabitEthernet name {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_admin_status(self, arg_dictionary, **kwargs):
        uuid = "aff4e031-7493-4728-9ed5-dd640c8ee2b0"
        cmd = "show interface GigabitEthernet state {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_oper_status(self, arg_dictionary, **kwargs):
        uuid = "75ffd61b-7b99-47dc-8deb-b96577bcf6e8"
        cmd = "show interface GigabitEthernet state {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_mtu(self, arg_dictionary, **kwargs):
        uuid = "1439a54f-38a7-465e-8454-e22ea92fbd99"
        cmd = "show interface GigabitEthernet interface {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_mac_address(self, arg_dictionary, **kwargs):
        uuid = "59ecc15f-826e-4e0a-a021-0d2cd792ff4e"
        cmd = "show interface GigabitEthernet interface {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_high_speed(self, arg_dictionary, **kwargs):
        uuid = "5047b112-5de9-4ab0-96e9-9620c4a69d7f"
        cmd = "show interface GigabitEthernet l1-config {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_in_octets(self, arg_dictionary, **kwargs):
        uuid = "c97a2828-cbb8-412f-a9dc-c80850707c4e"
        cmd = "show interface GigabitEthernet statistics {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_in_unicast_packets(self, arg_dictionary, **kwargs):
        uuid = "c4fa7bf2-eccd-4429-8b56-65330536c009"
        cmd = "show interface GigabitEthernet statistics verbose {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_in_discard_packets(self, arg_dictionary, **kwargs):
        uuid = "8c0bf5fb-5640-433a-a881-c756634ff522"
        cmd = "show interface GigabitEthernet statistics verbose {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_in_error_packets(self, arg_dictionary, **kwargs):
        uuid = "1d564800-6b86-47a9-839d-ec55341e0cf7"
        cmd = "show interface GigabitEthernet statistics verbose {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_out_octets(self, arg_dictionary, **kwargs):
        uuid = "b316b446-81fc-416b-97f4-c0e2fcf4ce92"
        cmd = "show interface GigabitEthernet statistics {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_out_unicast_packets(self, arg_dictionary, **kwargs):
        uuid = "ee8c50ae-7a0e-4ea3-afb5-335c9a2deb62"
        cmd = "show interface GigabitEthernet statistics verbose {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_out_discard_packets(self, arg_dictionary, **kwargs):
        uuid = "29555c1c-b7f5-40b3-b1e1-607044c7c3ba"
        cmd = "show interface GigabitEthernet statistics {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_out_error_packets(self, arg_dictionary, **kwargs):
        uuid = "f2aeac12-dcba-447d-834d-64bb54cb8663"
        cmd = "show interface GigabitEthernet statistics verbose {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_in_multicast_packets(self, arg_dictionary, **kwargs):
        uuid = "f531cc1c-a829-4d10-9ab9-e6cead126d86"
        cmd = "show interface GigabitEthernet statistics verbose {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_in_broadcast_packets(self, arg_dictionary, **kwargs):
        uuid = "06201eb5-eaca-4f97-8f06-c3e33e9145e4"
        cmd = "show interface GigabitEthernet statistics verbose {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_out_multicast_packets(self, arg_dictionary, **kwargs):
        uuid = "fd5f8d0a-de0a-4b0a-b057-e6ace49a50a5"
        cmd = "show interface GigabitEthernet statistics verbose {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_out_broadcast_packets(self, arg_dictionary, **kwargs):
        uuid = "ec4979b9-2cec-4435-9230-7151450950a2"
        cmd = "show interface GigabitEthernet statistics verbose {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_64_bit_in_octets(self, arg_dictionary, **kwargs):
        uuid = "8b0b5333-d713-4031-b03a-bc33f2fd3851"
        cmd = "show interface GigabitEthernet statistics {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_64_bit_in_unicast_packets(self, arg_dictionary, **kwargs):
        uuid = "6c0ae132-a890-4b1b-a768-81b84718642e"
        cmd = "show interface GigabitEthernet statistics verbose {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_64_bit_in_multicast_packets(self, arg_dictionary, **kwargs):
        uuid = "6f1f06a6-23b6-429d-a35d-fdaadf610a6a"
        cmd = "show interface GigabitEthernet statistics verbose {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_64_bit_in_broadcast_packets(self, arg_dictionary, **kwargs):
        uuid = "522c2b65-b2fc-414d-88a1-ffac3b0667bf"
        cmd = "show interface GigabitEthernet statistics verbose {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_64_bit_out_octets(self, arg_dictionary, **kwargs):
        uuid = "45e50d85-560f-4b1f-ba2d-8d6d3738bbe3"
        cmd = "show interface GigabitEthernet statistics {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_64_bit_out_unicast_packets(self, arg_dictionary, **kwargs):
        uuid = "10f79368-469e-4404-981a-f0fdd73c6217"
        cmd = "show interface GigabitEthernet statistics verbose {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_64_bit_out_multicast_packets(self, arg_dictionary, **kwargs):
        uuid = "0f38c025-d773-4826-af6e-d2cb9b9e5d7d"
        cmd = "show interface GigabitEthernet statistics verbose {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_64_bit_out_broadcast_packets(self, arg_dictionary, **kwargs):
        uuid = "b470bad8-9ba7-40ca-9777-2ee7836b4806"
        cmd = "show interface GigabitEthernet statistics verbose {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_flex_uni_status(self, arg_dictionary, **kwargs):
        uuid = "79c31e05-fa7a-4053-a537-91a3c0888096"
        cmd = "show interface GigabitEthernet config {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
