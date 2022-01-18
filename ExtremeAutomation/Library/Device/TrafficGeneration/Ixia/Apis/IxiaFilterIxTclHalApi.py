from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.Apis.IxiaIxTclHalApi import IxiaIxTclHalApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.TrafficGenerationUtils import TrafficGenerationUtils


class IxiaFilterIxTclHalApi (IxiaIxTclHalApi):
    def __init__(self, device):
        super(IxiaFilterIxTclHalApi, self).__init__(device)

    def get_capture_filter_settings(self, port_string):
        port_string = TrafficGenerationUtils.convert_port_string_to_ixtclhal_port(port_string)
        dev = self.get_device()
        ret_string = ""
        ret_string += "\t:" + self.strip_return(dev.send_command("filter get " + str(port_string))) + "\n"
        ret_string += "\tuserDefinedStat1Enable:" + \
                      self.strip_return(dev.send_command("filter cget -userDefinedStat1Enable")) + "\n"
        ret_string += "\tuserDefinedStat1DA:" + \
                      self.strip_return(dev.send_command("filter cget -userDefinedStat1DA")) + "\n"
        ret_string += "\tuserDefinedStat1SA:" + \
                      self.strip_return(dev.send_command("filter cget -userDefinedStat1SA")) + "\n"
        ret_string += "\tuserDefinedStat1Pattern:" + \
                      self.strip_return(dev.send_command("filter cget -userDefinedStat1Pattern")) + "\n"
        ret_string += "\tuserDefinedStat1Error:" + \
                      self.strip_return(dev.send_command("filter cget -userDefinedStat1Error")) + "\n"
        ret_string += "\tuserDefinedStat1FrameSizeEnable:" + \
                      self.strip_return(dev.send_command("filter cget -userDefinedStat1FrameSizeEnable")) + "\n"
        ret_string += "\tuserDefinedStat1FrameSizeFrom:" + \
                      self.strip_return(dev.send_command("filter cget -userDefinedStat1FrameSizeFrom")) + "\n"
        ret_string += "\tuserDefinedStat1FrameSizeTo:" + \
                      self.strip_return(dev.send_command("filter cget -userDefinedStat1FrameSizeTo")) + "\n"
        ret_string += "\tuserDefinedStat2Enable:" + \
                      self.strip_return(dev.send_command("filter cget -userDefinedStat2Enable")) + "\n"
        ret_string += "\tuserDefinedStat2DA:" + \
                      self.strip_return(dev.send_command("filter cget -userDefinedStat2DA")) + "\n"
        ret_string += "\tuserDefinedStat2SA:" + \
                      self.strip_return(dev.send_command("filter cget -userDefinedStat2SA")) + "\n"
        ret_string += "\tuserDefinedStat2Pattern:" + \
                      self.strip_return(dev.send_command("filter cget -userDefinedStat2Pattern")) + "\n"
        ret_string += "\tuserDefinedStat2Error:" + \
                      self.strip_return(dev.send_command("filter cget -userDefinedStat2Error")) + "\n"
        ret_string += "\tuserDefinedStat2FrameSizeEnable:" + \
                      self.strip_return(dev.send_command("filter cget -userDefinedStat2FrameSizeEnable")) + "\n"
        ret_string += "\tuserDefinedStat2FrameSizeFrom:" + \
                      self.strip_return(dev.send_command("filter cget -userDefinedStat2FrameSizeFrom")) + "\n"
        ret_string += "\tuserDefinedStat2FrameSizeTo:" + \
                      self.strip_return(dev.send_command("filter cget -userDefinedStat2FrameSizeTo")) + "\n"
        ret_string += "\tcaptureTriggerEnable:" + \
                      self.strip_return(dev.send_command("filter cget -captureTriggerEnable")) + "\n"
        ret_string += "\tcaptureTriggerDA:" + \
                      self.strip_return(dev.send_command("filter cget -captureTriggerDA")) + "\n"
        ret_string += "\tcaptureTriggerSA:" + \
                      self.strip_return(dev.send_command("filter cget -captureTriggerSA")) + "\n"
        ret_string += "\tcaptureTriggerPattern:" + \
                      self.strip_return(dev.send_command("filter cget -captureTriggerPattern")) + "\n"
        ret_string += "\tcaptureTriggerError:" + \
                      self.strip_return(dev.send_command("filter cget -captureTriggerError")) + "\n"
        ret_string += "\tcaptureTriggerFrameSizeEnable:" + \
                      self.strip_return(dev.send_command("filter cget -captureTriggerFrameSizeEnable")) + "\n"
        ret_string += "\tcaptureTriggerFrameSizeFrom:" + \
                      self.strip_return(dev.send_command("filter cget -captureTriggerFrameSizeFrom")) + "\n"
        ret_string += "\tcaptureTriggerFrameSizeTo:" + \
                      self.strip_return(dev.send_command("filter cget -captureTriggerFrameSizeTo")) + "\n"
        ret_string += "\tcaptureFilterEnable:" + \
                      self.strip_return(dev.send_command("filter cget -captureFilterEnable")) + "\n"
        ret_string += "\tcaptureFilterDA:" + \
                      self.strip_return(dev.send_command("filter cget -captureFilterDA")) + "\n"
        ret_string += "\tcaptureFilterSA:" + \
                      self.strip_return(dev.send_command("filter cget -captureFilterSA")) + "\n"
        ret_string += "\tcaptureFilterPattern:" + \
                      self.strip_return(dev.send_command("filter cget -captureFilterPattern")) + "\n"
        ret_string += "\tcaptureFilterError:" + \
                      self.strip_return(dev.send_command("filter cget -captureFilterError")) + "\n"
        ret_string += "\tcaptureFilterFrameSizeEnable:" + \
                      self.strip_return(dev.send_command("filter cget -captureFilterFrameSizeEnable")) + "\n"
        ret_string += "\tcaptureFilterFrameSizeFrom:" + \
                      self.strip_return(dev.send_command("filter cget -captureFilterFrameSizeFrom")) + "\n"
        ret_string += "\tcaptureFilterFrameSizeTo:" + \
                      self.strip_return(dev.send_command("filter cget -captureFilterFrameSizeTo")) + "\n"
        return ret_string
