"""
All firmware supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.firmware.base.firmwarebase import FirmwareBase


class Firmware(DeviceApi, FirmwareBase):
    def __init__(self, device_input):
        super(Firmware, self).__init__(device_input)

    def determine_firmware(self, arg_dictionary, **kwargs):
        uuid = "ba85b548-bf68-4a74-8b3b-4c3fa9504581"
        cmd = "show bootvar"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def select_firmware(self, arg_dictionary, **kwargs):
        uuid = "db08d60b-d00c-4c50-acf9-b6a9c3edffb5"
        cmd = "boot system {0}".format(arg_dictionary['filename'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_firmware_info(self, arg_dictionary, **kwargs):
        uuid = "c7400809-980c-453b-b64c-083e8b9b9721"
        cmd = "show version"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_installed_images(self, arg_dictionary, **kwargs):
        uuid = "915a5c65-84e5-426b-a322-48bdbda9f462"
        cmd = "show bootvar"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
