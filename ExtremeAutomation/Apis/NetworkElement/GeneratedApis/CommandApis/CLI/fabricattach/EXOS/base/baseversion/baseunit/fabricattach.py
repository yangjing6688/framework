"""
All fabricattach supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.fabricattach.base.fabricattachbase import \
    FabricattachBase


class Fabricattach(DeviceApi, FabricattachBase):
    def __init__(self, device_input):
        super(Fabricattach, self).__init__(device_input)

    def show_agent(self, arg_dictionary, **kwargs):
        uuid = "4567a871-654b-4bef-9539-7e221e1e7537"
        cmd = "show fabric attach agent"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_service_state(self, arg_dictionary, **kwargs):
        uuid = "a51e7285-3506-49dd-a482-045cd766d3a4"
        cmd = "show fabric attach agent"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_element_type(self, arg_dictionary, **kwargs):
        uuid = "67ea1813-fdc0-45a3-8496-2ff556f71576"
        cmd = "show fabric attach agent"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_provision_mode(self, arg_dictionary, **kwargs):
        uuid = "3075c202-b569-42d7-aada-e89093b62c81"
        cmd = "show fabric attach agent"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_global_timeouts(self, arg_dictionary, **kwargs):
        uuid = "3e9b00a0-978e-4d30-94f4-3b2c0a402d71"
        cmd = "show fabric attach agent"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_stats_global(self, arg_dictionary, **kwargs):
        uuid = "fb8262da-696a-49d5-a3ec-e9e502880476"
        cmd = "show fabric attach statistics"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_client_proxy_status(self, arg_dictionary, **kwargs):
        uuid = "9e5cd2d7-d2be-4d89-aa1a-97531ab5e191"
        cmd = "show fabric attach agent"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_standalone_proxy_status(self, arg_dictionary, **kwargs):
        uuid = "dd69da30-844f-4869-996c-24d1942c1bb2"
        cmd = "show fabric attach agent"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_agent_timeout(self, arg_dictionary, **kwargs):
        uuid = "424a0a0b-e26b-439c-8535-e8d1f969bd01"
        cmd = "show fabric attach agent"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_extended_logging_status(self, arg_dictionary, **kwargs):
        uuid = "d374d76e-30c3-4a14-afd5-8e042cff9e06"
        cmd = "show fabric attach agent"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_primary_server_id(self, arg_dictionary, **kwargs):
        uuid = "35bd30b6-9e4d-4627-9412-dc07baba7377"
        cmd = "show fabric attach agent"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_server_description(self, arg_dictionary, **kwargs):
        uuid = "70c5140c-03c8-4c37-b5cf-efb11a734224"
        cmd = "show fabric attach agent"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_neighbors(self, arg_dictionary, **kwargs):
        uuid = "d4058dbc-aa04-476b-8250-dbd7ed3fa277"
        cmd = "show fabric attach neighbors"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_elements(self, arg_dictionary, **kwargs):
        uuid = "df6dd63e-7c54-48fc-b83e-6a74983e546b"
        cmd = "show fabric attach elements"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_auto_provision_setting(self, arg_dictionary, **kwargs):
        uuid = "2b427864-874f-45ee-84ef-3ce1fa7df180"
        cmd = "show fabric attach agent"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_zero_touch_status(self, arg_dictionary, **kwargs):
        uuid = "e34ddcc6-77d1-4c7a-a5a6-6c68f0a4e313"
        cmd = "show fabric attach agent"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
