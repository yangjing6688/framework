from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.TrafficGenerationApi import TrafficGenerationApi
from ExtremeAutomation.Library.Device.TrafficGeneration.TrafficGeneratingCommandObject import \
    TrafficGeneratingCommandObject

from collections import deque


class IxiaIxTclHalApi(TrafficGenerationApi):
    def __init__(self, device):
        TrafficGenerationApi.__init__(self, device)

    def send_commands(self, commands_list):
        ret_string = deque()
        for cmd in commands_list:
            ret_string.append(self.send_command(cmd))
        return ret_string

    def strip_return(self, mess):
        if isinstance(mess, TrafficGeneratingCommandObject):
            if len(mess.return_text) > 0:
                ret_string = str(mess.return_text[0])
            else:
                ret_string = ""
        else:
            ret_string = str(mess)
        ret_string = ret_string.replace('%', '')
        return ret_string.strip()
