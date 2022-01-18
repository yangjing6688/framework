from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.Apis.IxiaIxTclHalApi import IxiaIxTclHalApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.TrafficGenerationUtils import TrafficGenerationUtils


class IxiaFilterPalletteIxTclHalApi (IxiaIxTclHalApi):
    def __init__(self, device):
        super(IxiaFilterPalletteIxTclHalApi, self).__init__(device)

    def get_capture_filter_pallette_settings(self, port_string):
        port_string = TrafficGenerationUtils.convert_port_string_to_ixtclhal_port(port_string)
        dev = self.get_device()
        ret_string = ""
        ret_string += "\t" + self.strip_return(dev.send_command("filterPallette get " + str(port_string))) + "\n"
        ret_string += "\tDA1 da:" + self.strip_return(dev.send_command("filterPallette cget -DA1")) + "\n"
        ret_string += "\tDA1 daMask:" + self.strip_return(dev.send_command("filterPallette cget -DAMask1")) + "\n"
        ret_string += "\tDA2 da:" + self.strip_return(dev.send_command("filterPallette cget -DA2")) + "\n"
        ret_string += "\tDA2 daMask:" + self.strip_return(dev.send_command("filterPallette cget -DAMask2")) + "\n"
        ret_string += "\tSA1 sa:" + self.strip_return(dev.send_command("filterPallette cget -SA1")) + "\n"
        ret_string += "\tSA1 saMask:" + self.strip_return(dev.send_command("filterPallette cget -SAMask1")) + "\n"
        ret_string += "\tSA2 sa:" + self.strip_return(dev.send_command("filterPallette cget -SA2")) + "\n"
        ret_string += "\tSA2 saMask:" + self.strip_return(dev.send_command("filterPallette cget -SAMask2")) + "\n"
        ret_string += "\tpattern 1 pattern:" + \
                      self.strip_return(dev.send_command("filterPallette cget -pattern1")) + "\n"
        ret_string += "\tpattern 1 patternMask:" + \
                      self.strip_return(dev.send_command("filterPallette cget -patternMask1")) + "\n"
        ret_string += "\tpattern 1 pattern Offset:" + \
                      self.strip_return(dev.send_command("filterPallette cget -patternOffset1")) + "\n"
        ret_string += "\tPattern 1 match type:" + \
                      self.strip_return(dev.send_command("filterPallette cget -matchType1")) + "\n"
        ret_string += "\tpattern 2 pattern:" + \
                      self.strip_return(dev.send_command("filterPallette cget -pattern2")) + "\n"
        ret_string += "\tpattern 2 patternMask:" + \
                      self.strip_return(dev.send_command("filterPallette cget -patternMask2")) + "\n"
        ret_string += "\tpattern 2 pattern Offset:" + \
                      self.strip_return(dev.send_command("filterPallette cget -patternOffset2")) + "\n"
        ret_string += "\tPattern 2 match type:" + \
                      self.strip_return(dev.send_command("filterPallette cget -matchType2"))
        return ret_string
