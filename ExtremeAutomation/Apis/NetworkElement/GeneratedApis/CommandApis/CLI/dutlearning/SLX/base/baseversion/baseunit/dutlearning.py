"""
All dutlearning supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.dutlearning.base.dutlearningbase import \
    DutlearningBase


class Dutlearning(DeviceApi, DutlearningBase):
    def __init__(self, device_input):
        super(Dutlearning, self).__init__(device_input)

    def show_system_info(self, arg_dictionary, **kwargs):
        uuid = "2bc7a245-b0ec-4659-9315-8db8aec9e95c"
        cmd = "show system||show system monitor"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_chassis_info(self, arg_dictionary, **kwargs):
        uuid = "4a297236-fcd2-441a-8491-be0d69a87558"
        cmd = "show chassis"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_unit_info(self, arg_dictionary, **kwargs):
        uuid = "7e8d8470-e156-42ef-aff1-d8a42cbf9c8c"
        cmd = "show hardware profile"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port_info(self, arg_dictionary, **kwargs):
        uuid = "d906bb8c-043e-4625-98d6-cbe8d10c4c4a"
        cmd = "show interface||show interface status"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_license_info(self, arg_dictionary, **kwargs):
        uuid = "a3fc6b30-bcfd-4472-96b0-be93acca95da"
        cmd = "show license"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
