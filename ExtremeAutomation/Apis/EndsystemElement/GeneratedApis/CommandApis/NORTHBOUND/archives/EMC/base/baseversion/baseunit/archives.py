"""
All archives supported northbound commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Library.Device.Common.CommandObjects.RestCommandObject import RestCommandObject
from ExtremeAutomation.Apis.EndsystemElement.GeneratedApis.CommandApis.NORTHBOUND.archives.base.archivesbase import \
    ArchivesBase


class Archives(DeviceApi, ArchivesBase):
    def __init__(self, device):
        super(Archives, self).__init__(device)

    def show_archives(self, arg_dict):
        rest_request = RestCommandObject()
        rest_request.uri = "/nbi/graphql/"
        rest_request.data = '{network{archives{alertStatus archiveId archiveName dateCreated getConfigFile getCustomAttributes getPortAttributes maxVersions memoAsString numberOfDevices}}}'
        rest_request.request_type = "post"

        return self.device.send_command_object(rest_request)
