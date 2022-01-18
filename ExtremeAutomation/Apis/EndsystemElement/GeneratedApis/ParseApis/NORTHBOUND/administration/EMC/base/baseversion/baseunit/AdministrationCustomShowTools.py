from ExtremeAutomation.Library.Device.Common.Apis.BaseShowApi import NorthboundResults
from ExtremeAutomation.Apis.EndsystemElement.GeneratedApis.ParseApis.NORTHBOUND.administration.base.\
    AdministrationBaseCustomShowTools import AdministrationBaseCustomShowTools


class AdministrationCustomShowTools(AdministrationBaseCustomShowTools):
    def show_administration_server_info(self, output, args, **kwargs):
        try:
            result = NorthboundResults()
            result.add_result(output['data']['administration']['serverInfo']['freePhysicalMemory'], args['freephysicalmemory'])
            result.add_result(output['data']['administration']['serverInfo']['heapMemoryCommitted'], args['heapmemorycommitted'])
            result.add_result(output['data']['administration']['serverInfo']['heapMemoryInit'], args['heapmemoryinit'])
            result.add_result(output['data']['administration']['serverInfo']['heapMemoryMax'], args['heapmemorymax'])
            result.add_result(output['data']['administration']['serverInfo']['heapMemoryUsed'], args['heapmemoryused'])
            result.add_result(output['data']['administration']['serverInfo']['peakThreadCount'], args['peakthreadcount'])
            result.add_result(output['data']['administration']['serverInfo']['serverJVMStartTime'], args['serverjvmstarttime'])
            result.add_result(output['data']['administration']['serverInfo']['startTime'], args['starttime'])
            result.add_result(output['data']['administration']['serverInfo']['threadCount'], args['threadcount'])
            result.add_result(output['data']['administration']['serverInfo']['totalPhysicalMemory'], args['totalphysicalmemory'])
            result.add_result(output['data']['administration']['serverInfo']['totalStartedThreadCount'], args['totalstartedthreadcount'])
            result.add_result(output['data']['administration']['serverInfo']['upTime'], args['uptime'])
            result.add_result(output['data']['administration']['serverInfo']['version'], args['version'])
            return result.return_result()
        except KeyError:
            self.logger.log_info("KEY ERROR")
            return False
