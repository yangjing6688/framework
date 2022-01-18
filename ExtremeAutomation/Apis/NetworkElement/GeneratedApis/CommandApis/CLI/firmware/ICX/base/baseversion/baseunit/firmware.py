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
        cmd = "show flash"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def select_firmware(self, arg_dictionary, **kwargs):
        uuid = "db08d60b-d00c-4c50-acf9-b6a9c3edffb5"
        cmd = "write memory||boot system flash {0}".format(arg_dictionary['filename'])
        prompt = "userPrompt"
        conf = "Are you sure? (enter 'y' or 'n'):"
        conf_args = "{0}".format(arg_dictionary['answer'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf, conf_args=conf_args)

    def show_firmware_info(self, arg_dictionary, **kwargs):
        uuid = "c7400809-980c-453b-b64c-083e8b9b9721"
        cmd = "show version"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
