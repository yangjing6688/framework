"""
All fabricattach supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.fabricattach.base.fabricattachbase import \
    FabricattachBase


class Fabricattach(DeviceApi, FabricattachBase):
    def __init__(self, device_input):
        super(Fabricattach, self).__init__(device_input)

    def enable_global(self, arg_dictionary, **kwargs):
        uuid = "2fadd54c-c514-4dd7-adc4-e14f861ecfe7"
        cmd = "fa enable"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_global(self, arg_dictionary, **kwargs):
        uuid = "d44d2d2d-b35f-4bb6-87ea-69e45259f1f4"
        cmd = "no fa enable"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_port(self, arg_dictionary, **kwargs):
        uuid = "014943bb-3d2c-4642-8369-8f4eda5db253"
        cmd = "fa enable"
        prompt = "intfPrompt"
        prompt_args = "GigabitEthernet {0}".format(arg_dictionary['port'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def disable_port(self, arg_dictionary, **kwargs):
        uuid = "84ca75ea-abca-40b9-859e-a2e0334e760a"
        cmd = "no fa enable"
        prompt = "intfPrompt"
        prompt_args = "GigabitEthernet {0}".format(arg_dictionary['port'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def delete_port(self, arg_dictionary, **kwargs):
        uuid = "fb9747d5-cc8a-4aec-bc0f-292609bf07ae"
        cmd = "no fa"
        prompt = "intfPrompt"
        prompt_args = "GigabitEthernet {0}".format(arg_dictionary['port'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def enable_mlt(self, arg_dictionary, **kwargs):
        uuid = "b56fce5c-2794-43b5-9402-ba257afa7fc2"
        cmd = "fa enable"
        prompt = "intfPrompt"
        prompt_args = "mlt {0}".format(arg_dictionary['mlt_id'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def disable_mlt(self, arg_dictionary, **kwargs):
        uuid = "e1ff075d-a674-4319-8cad-c2027b1b42d6"
        cmd = "no fa enable"
        prompt = "intfPrompt"
        prompt_args = "mlt {0}".format(arg_dictionary['mlt_id'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def delete_mlt(self, arg_dictionary, **kwargs):
        uuid = "1b87c519-cb3d-42f8-90fa-4702f613bac4"
        cmd = "no fa"
        prompt = "intfPrompt"
        prompt_args = "mlt {0}".format(arg_dictionary['mlt_id'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def enable_port_auth(self, arg_dictionary, **kwargs):
        uuid = "ee77b7d6-1c80-4a45-8918-1d9f97420fbf"
        cmd = "fa message-authentication"
        prompt = "intfPrompt"
        prompt_args = "GigabitEthernet {0}".format(arg_dictionary['port'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def disable_port_auth(self, arg_dictionary, **kwargs):
        uuid = "b29e33ba-e609-46fc-a013-dbf0530d5cdd"
        cmd = "no fa message-authentication"
        prompt = "intfPrompt"
        prompt_args = "GigabitEthernet {0}".format(arg_dictionary['port'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def enable_mlt_auth(self, arg_dictionary, **kwargs):
        uuid = "d9cf0399-b7d8-4b9c-89eb-aacfd59f7111"
        cmd = "fa message-authentication"
        prompt = "intfPrompt"
        prompt_args = "mlt {0}".format(arg_dictionary['mlt_id'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def disable_mlt_auth(self, arg_dictionary, **kwargs):
        uuid = "d3cb51c9-090b-4f79-b107-8c7cbc7de45d"
        cmd = "no fa message-authentication"
        prompt = "intfPrompt"
        prompt_args = "mlt {0}".format(arg_dictionary['mlt_id'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_assignment_timeout(self, arg_dictionary, **kwargs):
        uuid = "6e7549b9-7fbf-44fd-963f-ca316c7e6ab2"
        cmd = "fa assignment-timeout {0}".format(arg_dictionary['timeout'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_discovery_timeout(self, arg_dictionary, **kwargs):
        uuid = "4970b994-e328-4c88-8282-81b0af6b3219"
        cmd = "fa discovery-timeout {0}".format(arg_dictionary['timeout'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_port_auth_key(self, arg_dictionary, **kwargs):
        uuid = "967ecb22-20cc-4bc9-ab7a-f570616cfcb4"
        cmd = "fa authentication-key {0}".format(arg_dictionary['auth_key'])
        prompt = "intfPrompt"
        prompt_args = "GigabitEthernet {0}".format(arg_dictionary['port'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_mlt_auth_key(self, arg_dictionary, **kwargs):
        uuid = "982e301b-0505-4832-8f3d-d09432fe3b9a"
        cmd = "fa authentication-key {0}".format(arg_dictionary['auth_key'])
        prompt = "intfPrompt"
        prompt_args = "mlt {0}".format(arg_dictionary['mlt_id'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_port_mgmt_isid(self, arg_dictionary, **kwargs):
        uuid = "5d41fe78-26f5-417d-97f8-0218d063f5b0"
        cmd = "fa management i-sid {0}".format(arg_dictionary['i_sid'])
        prompt = "intfPrompt"
        prompt_args = "GigabitEthernet {0}".format(arg_dictionary['port'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_mlt_mgmt_isid(self, arg_dictionary, **kwargs):
        uuid = "86cc40a1-774c-4175-8019-98c3051fe105"
        cmd = "fa management i-sid {0}".format(arg_dictionary['i_sid'])
        prompt = "intfPrompt"
        prompt_args = "mlt {0}".format(arg_dictionary['mlt_id'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_port_mgmt_isid_and_cvid(self, arg_dictionary, **kwargs):
        uuid = "5609738c-9095-4e98-b168-6ef46b060ba0"
        cmd = "fa management i-sid {0} c-vid {1}".format(arg_dictionary['i_sid'],
                                                         arg_dictionary['c_vid'])
        prompt = "intfPrompt"
        prompt_args = "GigabitEthernet {0}".format(arg_dictionary['port'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_mlt_mgmt_isid_and_cvid(self, arg_dictionary, **kwargs):
        uuid = "6ccb9ec6-f2d7-4d11-8031-54cf3a5130bc"
        cmd = "fa management i-sid {0} c-vid {1}".format(arg_dictionary['i_sid'],
                                                         arg_dictionary['c_vid'])
        prompt = "intfPrompt"
        prompt_args = "mlt {0}".format(arg_dictionary['mlt_id'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def clear_port_mgmt_isid(self, arg_dictionary, **kwargs):
        uuid = "a3fd6b4e-cf1b-498f-8cc5-08d1c8491a80"
        cmd = "no fa management i-sid"
        prompt = "intfPrompt"
        prompt_args = "GigabitEthernet {0}".format(arg_dictionary['port'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def clear_mlt_mgmt_isid(self, arg_dictionary, **kwargs):
        uuid = "980e1662-394f-4fea-b058-02fdfc152dae"
        cmd = "no fa management i-sid"
        prompt = "intfPrompt"
        prompt_args = "mlt {0}".format(arg_dictionary['mlt_id'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_zero_touch_client_isid(self, arg_dictionary, **kwargs):
        uuid = "fbb9689a-0c10-4f0d-b6ab-57179f88581c"
        cmd = "fa zero-touch-client standard {0} i-sid {1}".format(arg_dictionary['name'],
                                                                   arg_dictionary['i_sid'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_zero_touch_client(self, arg_dictionary, **kwargs):
        uuid = "d666bda8-c763-4b2d-8e9e-c077b37cbba8"
        cmd = "no fa zero-touch-client standard {0}".format(arg_dictionary['name'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_agent(self, arg_dictionary, **kwargs):
        uuid = "4567a871-654b-4bef-9539-7e221e1e7537"
        cmd = "show fa agent"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_service_state(self, arg_dictionary, **kwargs):
        uuid = "a51e7285-3506-49dd-a482-045cd766d3a4"
        cmd = "show fa"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_element_type(self, arg_dictionary, **kwargs):
        uuid = "67ea1813-fdc0-45a3-8496-2ff556f71576"
        cmd = "show fa"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_provision_mode(self, arg_dictionary, **kwargs):
        uuid = "3075c202-b569-42d7-aada-e89093b62c81"
        cmd = "show fa"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_global_timeouts(self, arg_dictionary, **kwargs):
        uuid = "3e9b00a0-978e-4d30-94f4-3b2c0a402d71"
        cmd = "show fa"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port(self, arg_dictionary, **kwargs):
        uuid = "73db387e-a995-4b8d-bf52-ea999d1608fb"
        cmd = "show fa interface port {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_mlt(self, arg_dictionary, **kwargs):
        uuid = "38d80307-ef51-4c67-afa2-33f7b80a7389"
        cmd = "show fa interface mlt {0}".format(arg_dictionary['mlt_id'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_elements_port(self, arg_dictionary, **kwargs):
        uuid = "d5cace34-fbdb-4b18-a6a9-3a4de157a722"
        cmd = "show fa elements {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        self.device.error_checker.add_error_to_ignore_list(*["Invalid"])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_assignment_port(self, arg_dictionary, **kwargs):
        uuid = "27d91f59-0ab0-4510-9dcc-7eeff2580340"
        cmd = "show fa assignment {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_stats_global(self, arg_dictionary, **kwargs):
        uuid = "fb8262da-696a-49d5-a3ec-e9e502880476"
        cmd = "show fa statistics summary"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_stats_port(self, arg_dictionary, **kwargs):
        uuid = "cfb8d976-77a3-429b-8da6-e22c44e79b50"
        cmd = "show fa statistics {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_zero_touch_client(self, arg_dictionary, **kwargs):
        uuid = "07576a33-7963-499a-b59b-f648c20e13f5"
        cmd = "show fa zero-touch-client"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_isid(self, arg_dictionary, **kwargs):
        uuid = "430c3207-54ff-4e1b-a60e-0d1f766d17d0"
        cmd = "show i-sid {0}".format(arg_dictionary['isid'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
