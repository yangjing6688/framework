"""
All administration supported northbound commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Library.Device.Common.CommandObjects.RestCommandObject import RestCommandObject
from ExtremeAutomation.Apis.EndsystemElement.GeneratedApis.CommandApis.NORTHBOUND.administration.base.\
    administrationbase import AdministrationBase


class Administration(DeviceApi, AdministrationBase):
    def __init__(self, device):
        super(Administration, self).__init__(device)

    def show_administration_server_info(self, arg_dict):
        rest_request = RestCommandObject()
        rest_request.uri = "/nbi/graphql/"
        rest_request.data = '{administration{serverInfo{freePhysicalMemory heapMemoryCommitted heapMemoryInit heapMemoryMax heapMemoryUsed peakThreadCount serverJVMStartTime startTime threadCount totalPhysicalMemory totalStartedThreadCount upTime version}}}'
        rest_request.request_type = "post"

        return self.device.send_command_object(rest_request)
