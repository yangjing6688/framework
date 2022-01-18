"""
All vlan supported commands
"""
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.vlan.EXOS.base.baseversion.baseunit.vlan \
    import Vlan as VlanBase


class Vlan(VlanBase):
    def __init__(self, device_input):
        super(Vlan, self).__init__(device_input)

    def show_nsi(self, arg_dictionary, **kwargs):
        uuid = "27ad3b81-b4a6-4daf-a3f1-76ed5ff2ed36"
        cmd = "show vlan {0} fabric attach assignments".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
