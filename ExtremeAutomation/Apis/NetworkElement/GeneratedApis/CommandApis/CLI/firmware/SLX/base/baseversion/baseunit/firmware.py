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
        cmd = "show version"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def download_firmware_sftp(self, arg_dictionary, **kwargs):
        uuid = "674229d2-38c1-4f03-81e4-9ae3976b02f0"
        cmd = "firmware download fullinstall sftp host {0} user {1} password {2} directory {3}".format(arg_dictionary['server'],
                                                                                                       arg_dictionary['username'],
                                                                                                       arg_dictionary['password'],
                                                                                                       arg_dictionary['filename'])
        prompt = "userPrompt"
        conf = "Do you want to continue? [y/n]:"
        conf_args = "y"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf, conf_args=conf_args)

    def download_firmware_scp(self, arg_dictionary, **kwargs):
        uuid = "a65dab29-db0d-402e-a12c-4c36d37c4ce8"
        cmd = "firmware download fullinstall scp host {0} user {1} password {2} directory {3}".format(arg_dictionary['server'],
                                                                                                      arg_dictionary['username'],
                                                                                                      arg_dictionary['password'],
                                                                                                      arg_dictionary['filename'])
        prompt = "userPrompt"
        conf = "Do you want to continue? [y/n]:"
        conf_args = "y"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf, conf_args=conf_args)

    def show_firmware_info(self, arg_dictionary, **kwargs):
        uuid = "c7400809-980c-453b-b64c-083e8b9b9721"
        cmd = "show version"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
