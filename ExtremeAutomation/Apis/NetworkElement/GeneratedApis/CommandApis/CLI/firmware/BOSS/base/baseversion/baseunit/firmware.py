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

    def download_firmware(self, arg_dictionary, **kwargs):
        uuid = "67ffac3f-89d6-4c00-9bb8-a5a7862a6916"
        cmd = "download address {0} {1} image {2} {3}".format(arg_dictionary['server'],
                                                              arg_dictionary['image_location'],
                                                              arg_dictionary['filename'],
                                                              arg_dictionary['reset'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def download_firmware_sftp(self, arg_dictionary, **kwargs):
        uuid = "674229d2-38c1-4f03-81e4-9ae3976b02f0"
        cmd = "download {0} address {1} {2} image {3} {4} username {5} password".format(arg_dictionary['server_type'],
                                                                                        arg_dictionary['server'],
                                                                                        arg_dictionary['image_location'],
                                                                                        arg_dictionary['filename'],
                                                                                        arg_dictionary['reset'],
                                                                                        arg_dictionary['username'])
        prompt = "userPrompt"
        conf = "Enter password:"
        conf_args = "{0}".format(arg_dictionary['password'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf, conf_args=conf_args)

    def show_firmware_info(self, arg_dictionary, **kwargs):
        uuid = "c7400809-980c-453b-b64c-083e8b9b9721"
        cmd = "show sys-info"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
