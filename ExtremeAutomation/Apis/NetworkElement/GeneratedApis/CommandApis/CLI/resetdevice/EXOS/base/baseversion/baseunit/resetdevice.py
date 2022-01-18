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
        cmd = "reboot"
        prompt = "userPrompt"
        conf = "Do you want to save configuration changes||Are you sure you want to reboot the"
        conf_args = "{0}||{1}".format(arg_dictionary['reboot_exos'],
                                      arg_dictionary['reboot_answer'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf, conf_args=conf_args)

    def reset_system_to_config(self, arg_dictionary, **kwargs):
        uuid = "89c13d08-20a6-44cd-9a60-d97567a64939"
        cmd = "use configuration {0}||reboot".format(arg_dictionary['config'])
        prompt = "userPrompt"
        conf = "Do you want to save configuration changes||Are you sure you want to reboot the"
        conf_args = "{0}||{1}".format(arg_dictionary['reboot_exos'],
                                      arg_dictionary['reboot_answer'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf, conf_args=conf_args)

    def reset_factory_default(self, arg_dictionary, **kwargs):
        uuid = "bd80cb95-1f4d-4789-bc9a-c8022e99bc5c"
        cmd = "unconfigure switch all"
        prompt = "userPrompt"
        conf = "Restore all factory defaults and reboot? (y/N)"
        conf_args = "{0}".format(arg_dictionary['reboot_answer'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf, conf_args=conf_args)

    def bypass_initial_setup(self, arg_dictionary, **kwargs):
        uuid = "464e9b90-2b34-4244-94a6-600b803abfe2"
        cmd = "quit"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def login_after_reset(self, arg_dictionary, **kwargs):
        uuid = "660a18b1-9695-424f-b293-98b150d8d718"
        cmd = "{0}||{1}".format(arg_dictionary['username'],
                                arg_dictionary['password'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def run_failover(self, arg_dictionary, **kwargs):
        uuid = "7ff99091-fcf9-4f22-9308-de3030f378a3"
        cmd = "run failover"
        prompt = "userPrompt"
        conf = "Are you sure you want to failover?"
        conf_args = "{0}".format(arg_dictionary['failover_answer'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf, conf_args=conf_args)

    def run_failover_warm(self, arg_dictionary, **kwargs):
        uuid = "ce4485f8-7f77-4cdb-8a30-44d59ff429d9"
        cmd = "run failover warm"
        prompt = "userPrompt"
        conf = "Are you sure you want to failover?"
        conf_args = "{0}".format(arg_dictionary['failover_answer'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf, conf_args=conf_args)
