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
        cmd = "show switch"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def download_firmware(self, arg_dictionary, **kwargs):
        uuid = "67ffac3f-89d6-4c00-9bb8-a5a7862a6916"
        cmd = "download url tftp://{0}/{1} vr {2}".format(arg_dictionary['server'],
                                                          arg_dictionary['filename'],
                                                          arg_dictionary['vr'])
        prompt = "userPrompt"
        conf = "Debug information files are present||Do you want to install image after downloading"
        conf_args = "{0}||{1}".format(arg_dictionary['answer'],
                                      arg_dictionary['answer'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf, conf_args=conf_args)

    def select_firmware(self, arg_dictionary, **kwargs):
        uuid = "db08d60b-d00c-4c50-acf9-b6a9c3edffb5"
        cmd = "use image {0}".format(arg_dictionary['filename'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def uninstall_xmod(self, arg_dictionary, **kwargs):
        uuid = "19fd14e7-69c5-495f-ab1a-a3e53d1ae378"
        cmd = "uninstall image {0} {1}".format(arg_dictionary['xmod'],
                                               arg_dictionary['partition'])
        prompt = "userPrompt"
        conf = "(y or n)"
        conf_args = "{0}".format(arg_dictionary['save_config'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf, conf_args=conf_args)

    def download_firmware_https(self, arg_dictionary, **kwargs):
        uuid = "a4696382-57e2-40ee-8ebb-8560ac93a96e"
        cmd = "download url https://{0}/{1} vr {2}".format(arg_dictionary['server'],
                                                           arg_dictionary['filename'],
                                                           arg_dictionary['vr'])
        prompt = "userPrompt"
        conf = "Debug information files are present||Do you want to install image after downloading"
        conf_args = "{0}||{1}".format(arg_dictionary['answer'],
                                      arg_dictionary['answer'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf, conf_args=conf_args)

    def show_firmware_info(self, arg_dictionary, **kwargs):
        uuid = "c7400809-980c-453b-b64c-083e8b9b9721"
        cmd = "show version"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_installed_images(self, arg_dictionary, **kwargs):
        uuid = "915a5c65-84e5-426b-a322-48bdbda9f462"
        cmd = "show version images"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_firmware_version(self, arg_dictionary, **kwargs):
        uuid = "b695cdd6-6066-11ec-8607-0242ac1300021"
        cmd = "show version"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
