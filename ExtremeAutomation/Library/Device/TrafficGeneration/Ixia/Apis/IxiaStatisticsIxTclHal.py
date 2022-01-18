from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.Apis.IxiaIxTclHalApi import IxiaIxTclHalApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.TrafficGenerationUtils import TrafficGenerationUtils


class IxiaStatisticsIxTclHal(IxiaIxTclHalApi):
    def __init__(self, device):
        super(IxiaStatisticsIxTclHal, self).__init__(device)

    def get_capture_filter_statistic(self, port_string):
        port_string = TrafficGenerationUtils.convert_port_string_to_ixtclhal_port(port_string)
        dev = self.get_device()
        dev.send_command("stat get statAllStats " + str(port_string))
        count = dev.send_command("stat cget -captureFilter")
        count = count.replace("%", "")
        return count.strip()

    def get_capture_trigger_statistic(self, port_string):
        port_string = TrafficGenerationUtils.convert_port_string_to_ixtclhal_port(port_string)
        dev = self.get_device()
        dev.send_command("stat get statAllStats " + str(port_string))
        count = dev.send_command("stat cget -captureTrigger")
        count = count.replace("%", "")
        return count.strip()

    def get_capture_filter_rate(self, port_string):
        port_string = TrafficGenerationUtils.convert_port_string_to_ixtclhal_port(port_string)
        dev = self.get_device()
        dev.send_command("stat getRate allStats " + str(port_string))
        rate = dev.send_command("stat cget -captureFilter")
        rate = rate.replace("%", "")
        return rate.strip()

    def get_capture_trigger_rate(self, port_string):
        port_string = TrafficGenerationUtils.convert_port_string_to_ixtclhal_port(port_string)
        dev = self.get_device()
        dev.send_command("stat getRate allStats " + str(port_string))
        rate = dev.send_command("stat cget -captureTrigger")
        rate = rate.replace("%", "")
        return rate.strip()
