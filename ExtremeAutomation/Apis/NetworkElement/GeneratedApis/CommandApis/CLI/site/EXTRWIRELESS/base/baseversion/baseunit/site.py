"""
All site supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.site.base.sitebase import SiteBase


class Site(DeviceApi, SiteBase):
    def __init__(self, device_input):
        super(Site, self).__init__(device_input)

    def show_all(self, arg_dictionary, **kwargs):
        uuid = "66054fea-36d6-49b3-a59a-c64727a94ad6"
        cmd = "show site"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_detail(self, arg_dictionary, **kwargs):
        uuid = "cb810be3-6e9d-48c1-878e-915722ddbf33"
        cmd = "show site \"{0}\"".format(arg_dictionary['site_name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
