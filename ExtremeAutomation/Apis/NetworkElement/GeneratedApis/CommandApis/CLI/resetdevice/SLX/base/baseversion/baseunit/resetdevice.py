"""
All resetdevice supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.resetdevice.base.resetdevicebase import \
    ResetdeviceBase


class Resetdevice(DeviceApi, ResetdeviceBase):
    def __init__(self, device_input):
        super(Resetdevice, self).__init__(device_input)

    def reset_now(self, arg_dictionary, **kwargs):
        uuid = "2d811556-db6d-4a05-876b-546a65abf61a"
        cmd = "reload"
        prompt = "userPrompt"
        conf = "Are you sure you want to reload the switch?"
        conf_args = "{0}".format(arg_dictionary['reboot_answer'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf, conf_args=conf_args)

    def reset_system(self, arg_dictionary, **kwargs):
        uuid = "5f0f8465-9d88-4cdb-9cae-3f9dd55b940c"
        cmd = "reload system"
        prompt = "userPrompt"
        conf = "Are you sure you want to reboot the chassis [y/n]?"
        conf_args = "{0}".format(arg_dictionary['reboot_answer'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf, conf_args=conf_args)
