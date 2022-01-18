"""
All hostmonitor supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.hostmonitor.base.hostmonitorbase import \
    HostmonitorBase


class Hostmonitor(DeviceApi, HostmonitorBase):
    def __init__(self, device_input):
        super(Hostmonitor, self).__init__(device_input)

    def show_cpu_current_total_utilization(self, arg_dictionary, **kwargs):
        uuid = "4b715aa5-36a8-4a89-ba3f-f1b61104d5d9"
        cmd = "show khi performance cpu {0}".format(arg_dictionary['slot'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_cpu_5_minute_total_utilization(self, arg_dictionary, **kwargs):
        uuid = "7baccf20-2ed6-43af-a954-1cb80f45ae16"
        cmd = "show khi performance cpu {0}".format(arg_dictionary['slot'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_cpu_highest_5_minute_total_utilization(self, arg_dictionary, **kwargs):
        uuid = "2c70c83d-fb44-4203-b48e-11a9f8c7b56a"
        cmd = "show khi performance cpu {0}".format(arg_dictionary['slot'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_cpu_5_minute_hi_time_total_utilization(self, arg_dictionary, **kwargs):
        uuid = "a0bb0f40-a260-4da1-b8f2-da0a8f2a28ed"
        cmd = "show khi performance cpu {0}".format(arg_dictionary['slot'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_used_total_memory(self, arg_dictionary, **kwargs):
        uuid = "0d11e377-6503-4359-878c-7e5b6fb72195"
        cmd = "show khi performance memory {0}".format(arg_dictionary['slot'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_free_total_memory(self, arg_dictionary, **kwargs):
        uuid = "30d88f0c-761d-45cb-95f1-6bdc0c1687c2"
        cmd = "show khi performance memory {0}".format(arg_dictionary['slot'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_memory_total_utilization(self, arg_dictionary, **kwargs):
        uuid = "65c4b178-768a-47ae-8317-0e684c08f301"
        cmd = "show khi performance memory {0}".format(arg_dictionary['slot'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_memory_5_minute_total_utilization(self, arg_dictionary, **kwargs):
        uuid = "4168d780-8d0b-4fce-aa3b-c5ca5e0997c9"
        cmd = "show khi performance memory {0}".format(arg_dictionary['slot'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_memory_highest_5_minute_total_utilization(self, arg_dictionary, **kwargs):
        uuid = "38c5fcae-0a2c-4a48-97da-25a49960dd7c"
        cmd = "show khi performance memory {0}".format(arg_dictionary['slot'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_memory_5_minute_hi_time_total_utilization(self, arg_dictionary, **kwargs):
        uuid = "d90814b2-9a48-4302-8ead-cbf3ff6f4386"
        cmd = "show khi performance memory {0}".format(arg_dictionary['slot'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_used_fbuf(self, arg_dictionary, **kwargs):
        uuid = "b55c1af8-4739-4f06-b7f4-9e0d57f49dd6"
        cmd = "show khi performance buffer-pool {0}".format(arg_dictionary['slot'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_free_fbuf(self, arg_dictionary, **kwargs):
        uuid = "90fa9474-462f-4d83-be64-5f14c83dd3f1"
        cmd = "show khi performance buffer-pool {0}".format(arg_dictionary['slot'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_exhausted_fbufs(self, arg_dictionary, **kwargs):
        uuid = "0ad339c7-4cba-49af-b049-646a67b13cd2"
        cmd = "show khi performance buffer-pool {0}".format(arg_dictionary['slot'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_net_stack_system_free_mbuf(self, arg_dictionary, **kwargs):
        uuid = "7f29e0c2-f6fc-4c26-9d0d-a5b1d5ac676c"
        cmd = "show khi performance buffer-pool {0}".format(arg_dictionary['slot'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_net_stack_data_free_mbuf(self, arg_dictionary, **kwargs):
        uuid = "5a89ebf9-b5ba-4a80-ae48-dbfd22b5692c"
        cmd = "show khi performance buffer-pool {0}".format(arg_dictionary['slot'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_net_stack_system_used_mbuf(self, arg_dictionary, **kwargs):
        uuid = "83509ac7-a75c-466c-9208-2c30222ec012"
        cmd = "show khi performance buffer-pool {0}".format(arg_dictionary['slot'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_net_stack_data_used_mbuf(self, arg_dictionary, **kwargs):
        uuid = "81811985-1562-4818-a333-d0275fd30025"
        cmd = "show khi performance buffer-pool {0}".format(arg_dictionary['slot'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_net_stack_system_socket_mbuf(self, arg_dictionary, **kwargs):
        uuid = "59566cc4-9a43-434c-8c67-362597a5b2d6"
        cmd = "show khi performance buffer-pool {0}".format(arg_dictionary['slot'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_highest_queue_entries_consumed(self, arg_dictionary, **kwargs):
        uuid = "8ef38433-92db-4f8b-977f-b0d006f1c9c7"
        cmd = "show khi performance buffer-pool {0}".format(arg_dictionary['slot'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_current_queue_entries_consumed(self, arg_dictionary, **kwargs):
        uuid = "67571eb2-7e02-4ebf-8c0d-1d29ef4fbf5c"
        cmd = "show khi performance buffer-pool {0}".format(arg_dictionary['slot'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_free_queue_entries(self, arg_dictionary, **kwargs):
        uuid = "a4768ae6-debc-455b-a240-0123f7d91f59"
        cmd = "show khi performance buffer-pool {0}".format(arg_dictionary['slot'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
