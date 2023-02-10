"""
All hostinformation supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.hostinformation.base.hostinformationbase \
    import HostinformationBase


class Hostinformation(DeviceApi, HostinformationBase):
    def __init__(self, device_input):
        super(Hostinformation, self).__init__(device_input)

    def set_prompt(self, arg_dictionary, **kwargs):
        uuid = "8570be79-7439-4139-bd18-5a986b3389bd"
        cmd = "prompt {0}".format(arg_dictionary['prompt_name'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_host_contact(self, arg_dictionary, **kwargs):
        uuid = "783d173e-6609-4b01-a7c5-2030c6c54b0a"
        cmd = "snmp-server contact {0}".format(arg_dictionary['contact'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_host_name(self, arg_dictionary, **kwargs):
        uuid = "c7f45f88-cc06-4a62-981d-275f6fa8983f"
        cmd = "snmp-server name {0}".format(arg_dictionary['name'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_host_location(self, arg_dictionary, **kwargs):
        uuid = "162acbb4-0e6f-43c9-8211-9b83e34bfc6b"
        cmd = "snmp-server location {0}".format(arg_dictionary['location'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_prompt(self, arg_dictionary, **kwargs):
        uuid = "2ff11f67-fb26-45a2-bfda-0afbd69fcae9"
        cmd = "no prompt"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_system_name(self, arg_dictionary, **kwargs):
        uuid = "d8dc0a12-021d-4f17-947d-f275443dca07"
        cmd = "show sys-info"
        prompt = "userPrompt"

        self.device.error_checker.add_error_to_ignore_list(*["Error"])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_host_contact(self, arg_dictionary, **kwargs):
        uuid = "1c4a1acc-30cd-438b-ae00-ff635a4dc656"
        cmd = "show snmp-server"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_host_name(self, arg_dictionary, **kwargs):
        uuid = "64689dd6-98ef-4b8e-8be4-6a7928ca6699"
        cmd = "show snmp-server"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_host_location(self, arg_dictionary, **kwargs):
        uuid = "9d709f83-dae7-4210-ae2d-4de62a70fa59"
        cmd = "show snmp-server"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_app_iqagent(self, arg_dictionary, **kwargs):
        uuid = "d8dc0a12-021d-4f17-947d-f275443dca07"
        cmd = "show application iqagent"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
