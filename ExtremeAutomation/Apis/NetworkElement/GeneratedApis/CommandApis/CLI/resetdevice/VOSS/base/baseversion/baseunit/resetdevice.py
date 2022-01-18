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
        cmd = "boot"
        prompt = "userPrompt"
        conf = "Are you sure you want to re-boot the switch (y/n) ?"
        conf_args = "{0}".format(arg_dictionary['reboot_answer'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf, conf_args=conf_args)

    def reset_system_to_config(self, arg_dictionary, **kwargs):
        uuid = "89c13d08-20a6-44cd-9a60-d97567a64939"
        cmd = "boot config {0}".format(arg_dictionary['config'])
        prompt = "userPrompt"
        conf = "Are you sure you want to re-boot the switch (y/n) ?"
        conf_args = "{0}".format(arg_dictionary['reboot_answer'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf, conf_args=conf_args)
