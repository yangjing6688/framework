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
        conf = "The system has unsaved changes||Are you sure you would like to reset the system?"
        conf_args = "{0}||{1}".format(arg_dictionary['reboot_exos'],
                                      arg_dictionary['reboot_answer'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf, conf_args=conf_args)

    def reset_factory_default(self, arg_dictionary, **kwargs):
        uuid = "bd80cb95-1f4d-4789-bc9a-c8022e99bc5c"
        cmd = "clear config"
        prompt = "userPrompt"
        conf = "Are you sure you want to clear the configuration? (y/n)"
        conf_args = "{0}".format(arg_dictionary['reboot_answer'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf, conf_args=conf_args)
