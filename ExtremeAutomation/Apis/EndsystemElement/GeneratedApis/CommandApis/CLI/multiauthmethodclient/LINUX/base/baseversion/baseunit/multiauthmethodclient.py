"""
All multiauthmethodclient supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.EndsystemElement.GeneratedApis.CommandApis.CLI.multiauthmethodclient.base.\
    multiauthmethodclientbase import MultiauthmethodclientBase


class Multiauthmethodclient(DeviceApi, MultiauthmethodclientBase):
    def __init__(self, device_input):
        super(Multiauthmethodclient, self).__init__(device_input)

    def run_multiuser_config(self, arg_dictionary, **kwargs):
        cmd = "/home/administrator/atgapps/bin/multiAuth -cli -adapter {0} -debug -pcapVersion jnetpcap -pwaServer {1} -hostFile /home/administrator/atgapps/bin/multiauth_configs/{2}".format(arg_dictionary['adapater'],
                                                                                                                                                                                               arg_dictionary['pwa_server_ip'],
                                                                                                                                                                                               arg_dictionary['config_filename'])
        prompt = "userPrompt"

        return self.create_cmd_obj(cmd, prompt=prompt)

    def run_multiuser_config_no_logoff(self, arg_dictionary, **kwargs):
        cmd = "/home/administrator/atgapps/bin/multiAuth -cli -adapter {0} -debug -pcapVersion jnetpcap -pwaServer {1} -hostFile /home/administrator/atgapps/bin/multiauth_configs/{2} -cliSkipLogoff".format(arg_dictionary['adapater'],
                                                                                                                                                                                                              arg_dictionary['pwa_server_ip'],
                                                                                                                                                                                                              arg_dictionary['config_filename'])
        prompt = "userPrompt"

        return self.create_cmd_obj(cmd, prompt=prompt)

    def switch_to_root(self, arg_dictionary, **kwargs):
        cmd = "sudo su"
        prompt = "userPrompt"
        conf = "[sudo] password for administrator:"
        conf_args = "{0}".format(arg_dictionary['password'])

        return self.create_cmd_obj(cmd, prompt=prompt, conf=conf, conf_args=conf_args)

    def change_to_atgapps_dir(self, arg_dictionary, **kwargs):
        cmd = "cd /home/administrator/atgapps/bin"
        prompt = "userPrompt"

        return self.create_cmd_obj(cmd, prompt=prompt)
