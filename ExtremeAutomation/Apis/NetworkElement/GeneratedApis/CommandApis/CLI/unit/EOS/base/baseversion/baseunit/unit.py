"""
All unit supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.unit.base.unitbase import UnitBase


class Unit(DeviceApi, UnitBase):
    def __init__(self, device_input):
        super(Unit, self).__init__(device_input)

    def change_current_slot(self, arg_dictionary, **kwargs):
        uuid = "d0470a79-e039-4743-afbc-b00867b0c018"
        cmd = "telnet {0}".format(arg_dictionary['slot'])
        prompt = "debugPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def exit_current_slot(self, arg_dictionary, **kwargs):
        uuid = "3045df80-28a3-4efe-8eb3-a1729fba9c9d"
        cmd = "exit"
        prompt = "debugPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
