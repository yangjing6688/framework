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
        cmd = "show software"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def select_firmware(self, arg_dictionary, **kwargs):
        uuid = "db08d60b-d00c-4c50-acf9-b6a9c3edffb5"
        cmd = "software activate {0}".format(arg_dictionary['filename'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def delete_firmware(self, arg_dictionary, **kwargs):
        uuid = "1633561d-c592-4b8a-a614-5cae5413d383"
        cmd = "delete {0}".format(arg_dictionary['filename'])
        prompt = "userPrompt"
        conf = "Are you sure (y/n) ?"
        conf_args = "{0}".format(arg_dictionary['answer'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf, conf_args=conf_args)

    def commit_firmware(self, arg_dictionary, **kwargs):
        uuid = "983f1e85-7533-4acc-927f-054bddc1885e"
        cmd = "software commit"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_firmware_info(self, arg_dictionary, **kwargs):
        uuid = "c7400809-980c-453b-b64c-083e8b9b9721"
        cmd = "show software"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_firmware_version(self, arg_dictionary, **kwargs):
        uuid = "b695cdd6-6066-11ec-8607-0242ac1300021"
        cmd = "show software detail"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
