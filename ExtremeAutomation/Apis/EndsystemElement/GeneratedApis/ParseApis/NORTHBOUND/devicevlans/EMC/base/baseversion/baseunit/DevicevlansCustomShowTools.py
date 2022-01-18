from ExtremeAutomation.Library.Device.Common.Apis.BaseShowApi import NorthboundResults
from ExtremeAutomation.Apis.EndsystemElement.GeneratedApis.ParseApis.NORTHBOUND.devicevlans.base.\
    DevicevlansBaseCustomShowTools import DevicevlansBaseCustomShowTools


class DevicevlansCustomShowTools(DevicevlansBaseCustomShowTools):
    def placeholder(self, output, args, **kwargs):
        try:
            result = NorthboundResults()
            result.add_result(output['dataplaceholder'], args['dataplaceholder'])
            return result.return_result()
        except KeyError:
            self.logger.log_info("KEY ERROR")
            return False
