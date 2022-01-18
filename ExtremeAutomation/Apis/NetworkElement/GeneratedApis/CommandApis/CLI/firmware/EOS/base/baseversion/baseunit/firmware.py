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
        cmd = "dir images"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def download_firmware(self, arg_dictionary, **kwargs):
        uuid = "67ffac3f-89d6-4c00-9bb8-a5a7862a6916"
        cmd = "copy tftp://{0}/{1} {2}".format(arg_dictionary['server'],
                                               arg_dictionary['filename'],
                                               arg_dictionary['version'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def select_firmware(self, arg_dictionary, **kwargs):
        uuid = "db08d60b-d00c-4c50-acf9-b6a9c3edffb5"
        cmd = "set boot system {0}".format(arg_dictionary['filename'])
        prompt = "userPrompt"
        conf = "(y/n)"
        conf_args = "{0}".format(arg_dictionary['answer'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf, conf_args=conf_args)

    def delete_firmware(self, arg_dictionary, **kwargs):
        uuid = "1633561d-c592-4b8a-a614-5cae5413d383"
        cmd = "delete {0}".format(arg_dictionary['filename'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_firmware_info(self, arg_dictionary, **kwargs):
        uuid = "c7400809-980c-453b-b64c-083e8b9b9721"
        cmd = "dir images"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
