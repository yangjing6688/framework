"""
All dns supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.dns.base.dnsbase import DnsBase


class Dns(DeviceApi, DnsBase):
    def __init__(self, device_input):
        super(Dns, self).__init__(device_input)

    def create_domain_name(self, arg_dictionary, **kwargs):
        uuid = "e52ebe68-5a1e-4318-b7eb-01f0165887db"
        cmd = "ip domain-name {0}".format(arg_dictionary['domain_name'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def delete_domain_name(self, arg_dictionary, **kwargs):
        uuid = "24f37769-0d47-4a87-b6de-7ba2735d7daf"
        cmd = "no ip domain-name"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_primary_server_ip(self, arg_dictionary, **kwargs):
        uuid = "1a4f6daf-b175-4fd8-826b-87f0ad9d8ef5"
        cmd = "ip name-server primary {0}".format(arg_dictionary['ip_addr'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_secondary_server_ip(self, arg_dictionary, **kwargs):
        uuid = "e309545c-f045-4ff1-b3b5-df236f6960bf"
        cmd = "ip name-server secondary {0}".format(arg_dictionary['ip_addr'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_tertiary_server_ip(self, arg_dictionary, **kwargs):
        uuid = "a7cfe8b1-4a4e-4c98-a4ee-00ccaaed6d61"
        cmd = "ip name-server tertiary {0}".format(arg_dictionary['ip_addr'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_primary_server_ip(self, arg_dictionary, **kwargs):
        uuid = "ff9d10d1-2200-492f-a0bc-ef9a9aaa1b9d"
        cmd = "no ip name-server primary"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_secondary_server_ip(self, arg_dictionary, **kwargs):
        uuid = "efd8b04c-9820-463e-a4e1-1b90aa0cedc4"
        cmd = "no ip name-server secondary"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_tertiary_server_ip(self, arg_dictionary, **kwargs):
        uuid = "44ad3310-2381-4b0f-87a9-0831a6b47c79"
        cmd = "no ip name-server tertiary"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_domain_name(self, arg_dictionary, **kwargs):
        uuid = "1e06dc66-ec69-44c8-9676-76fe265614e0"
        cmd = "show ip dns"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_servers(self, arg_dictionary, **kwargs):
        uuid = "3f478d14-8e1b-4411-93c9-73b85fe57ea2"
        cmd = "show ip dns"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_host_by_name(self, arg_dictionary, **kwargs):
        uuid = "4cac61fc-ac22-4d80-86d1-7b9c04e84d32"
        cmd = "show hosts {0}".format(arg_dictionary['host_name'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_host_by_ip(self, arg_dictionary, **kwargs):
        uuid = "9513a6d8-fea3-405c-a3d9-1a4971678132"
        cmd = "show hosts {0}".format(arg_dictionary['host_ip'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
