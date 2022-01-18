"""
All firmware supported commands
"""
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.firmware.BOSS.base.baseversion.baseunit.\
    firmware import Firmware as FirmwareBase


class Firmware(FirmwareBase):
    def __init__(self, device_input):
        super(Firmware, self).__init__(device_input)

    def download_firmware_sftp(self, arg_dictionary, **kwargs):
        uuid = "674229d2-38c1-4f03-81e4-9ae3976b02f0"
        cmd = "download {0} address {1} {2} image {3} {4} username {5} password".format(arg_dictionary['server_type'],
                                                                                        arg_dictionary['server'],
                                                                                        arg_dictionary['image_location'],
                                                                                        arg_dictionary['filename'],
                                                                                        arg_dictionary['reset'],
                                                                                        arg_dictionary['username'])
        prompt = "userPrompt"
        conf = "Enter password:||Confirm password:"
        conf_args = "{0}||{1}".format(arg_dictionary['password'],
                                      arg_dictionary['password'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf, conf_args=conf_args)
