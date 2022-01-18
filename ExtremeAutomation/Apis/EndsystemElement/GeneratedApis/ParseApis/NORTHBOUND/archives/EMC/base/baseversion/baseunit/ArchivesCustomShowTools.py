from ExtremeAutomation.Library.Device.Common.Apis.BaseShowApi import NorthboundResults
from ExtremeAutomation.Apis.EndsystemElement.GeneratedApis.ParseApis.NORTHBOUND.archives.base.\
    ArchivesBaseCustomShowTools import ArchivesBaseCustomShowTools


class ArchivesCustomShowTools(ArchivesBaseCustomShowTools):
    def show_archives(self, output, args, **kwargs):
        try:
            result = NorthboundResults()
            result.add_result(output['data']['network']['archives']['alertStatus'], args['alertstatus'])
            result.add_result(output['data']['network']['archives']['archiveId'], args['archiveid'])
            result.add_result(output['data']['network']['archives']['archiveName'], args['archivename'])
            result.add_result(output['data']['network']['archives']['dateCreated'], args['datecreated'])
            result.add_result(output['data']['network']['archives']['getConfigFile'], args['getconfigfile'])
            result.add_result(output['data']['network']['archives']['getCustomAttributes'], args['getcustomattributes'])
            result.add_result(output['data']['network']['archives']['getPortAttributes'], args['getportattributes'])
            result.add_result(output['data']['network']['archives']['maxVersions'], args['maxversions'])
            result.add_result(output['data']['network']['archives']['memoAsString'], args['memoasstring'])
            result.add_result(output['data']['network']['archives']['numberOfDevices'], args['numberofdevices'])
            return result.return_result()
        except KeyError:
            self.logger.log_info("KEY ERROR")
            return False
