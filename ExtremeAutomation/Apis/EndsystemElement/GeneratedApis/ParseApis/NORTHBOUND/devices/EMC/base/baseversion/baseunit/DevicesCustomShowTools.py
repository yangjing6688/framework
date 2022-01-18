from ExtremeAutomation.Library.Device.Common.Apis.BaseShowApi import NorthboundResults
from ExtremeAutomation.Apis.EndsystemElement.GeneratedApis.ParseApis.NORTHBOUND.devices.base.\
    DevicesBaseCustomShowTools import DevicesBaseCustomShowTools


class DevicesCustomShowTools(DevicesBaseCustomShowTools):
    def show_all_device_assettags(self, output, args, **kwargs):
        try:
            result = NorthboundResults()
            result.add_result(output['data']['network']['devices']['assetTag'], args['assettag'])
            return result.return_result()
        except KeyError:
            self.logger.log_info("KEY ERROR")
            return False

    def show_all_device_basemacs(self, output, args, **kwargs):
        try:
            result = NorthboundResults()
            result.add_result(output['data']['network']['devices']['baseMac'], args['basemac'])
            return result.return_result()
        except KeyError:
            self.logger.log_info("KEY ERROR")
            return False

    def show_all_device_sysnames(self, output, args, **kwargs):
        try:
            result = NorthboundResults()
            result.add_result(output['data']['network']['devices']['sysName'], args['sysname'])
            return result.return_result()
        except KeyError:
            self.logger.log_info("KEY ERROR")
            return False

    def show_all_device_nicknames(self, output, args, **kwargs):
        try:
            result = NorthboundResults()
            result.add_result(output['data']['network']['devices']['nickName'], args['nickname'])
            return result.return_result()
        except KeyError:
            self.logger.log_info("KEY ERROR")
            return False

    def show_all_device_ips(self, output, args, **kwargs):
        try:
            result = NorthboundResults()
            result.add_result(output['data']['network']['devices']['ip'], args['ip'])
            return result.return_result()
        except KeyError:
            self.logger.log_info("KEY ERROR")
            return False

    def show_device_assettag(self, output, args, **kwargs):
        try:
            result = NorthboundResults()
            result.add_result(output['data']['network']['device']['assetTag'], args['assettag'])
            return result.return_result()
        except KeyError:
            self.logger.log_info("KEY ERROR")
            return False

    def show_device_basemac(self, output, args, **kwargs):
        try:
            result = NorthboundResults()
            result.add_result(output['data']['network']['device']['baseMac'], args['basemac'])
            return result.return_result()
        except KeyError:
            self.logger.log_info("KEY ERROR")
            return False

    def show_device_bootprom(self, output, args, **kwargs):
        try:
            result = NorthboundResults()
            result.add_result(output['data']['network']['device']['bootProm'], args['bootprom'])
            return result.return_result()
        except KeyError:
            self.logger.log_info("KEY ERROR")
            return False

    def show_device_chassisid(self, output, args, **kwargs):
        try:
            result = NorthboundResults()
            result.add_result(output['data']['network']['device']['chassisId'], args['chassisid'])
            return result.return_result()
        except KeyError:
            self.logger.log_info("KEY ERROR")
            return False

    def show_device_chassis_type(self, output, args, **kwargs):
        try:
            result = NorthboundResults()
            result.add_result(output['data']['network']['device']['chassisType'], args['chassistype'])
            return result.return_result()
        except KeyError:
            self.logger.log_info("KEY ERROR")
            return False

    def show_device_devicedisplayfamily(self, output, args, **kwargs):
        try:
            result = NorthboundResults()
            result.add_result(output['data']['network']['device']['deviceDisplayFamily'], args['devicedisplayfamily'])
            return result.return_result()
        except KeyError:
            self.logger.log_info("KEY ERROR")
            return False

    def show_device_deviceid(self, output, args, **kwargs):
        try:
            result = NorthboundResults()
            result.add_result(output['data']['network']['device']['deviceId'], args['deviceid'])
            return result.return_result()
        except KeyError:
            self.logger.log_info("KEY ERROR")
            return False

    def show_device_devicename(self, output, args, **kwargs):
        try:
            result = NorthboundResults()
            result.add_result(output['data']['network']['device']['deviceName'], args['devicename'])
            return result.return_result()
        except KeyError:
            self.logger.log_info("KEY ERROR")
            return False

    def show_device_firmware(self, output, args, **kwargs):
        try:
            result = NorthboundResults()
            result.add_result(output['data']['network']['device']['firmware'], args['firmware'])
            return result.return_result()
        except KeyError:
            self.logger.log_info("KEY ERROR")
            return False

    def show_device_id(self, output, args, **kwargs):
        try:
            result = NorthboundResults()
            result.add_result(output['data']['network']['device']['id'], args['id'])
            return result.return_result()
        except KeyError:
            self.logger.log_info("KEY ERROR")
            return False

    def show_device_ip(self, output, args, **kwargs):
        try:
            result = NorthboundResults()
            result.add_result(output['data']['network']['device']['ip'], args['ip'])
            return result.return_result()
        except KeyError:
            self.logger.log_info("KEY ERROR")
            return False

    def show_device_name(self, output, args, **kwargs):
        try:
            result = NorthboundResults()
            result.add_result(output['data']['network']['device']['name'], args['name'])
            return result.return_result()
        except KeyError:
            self.logger.log_info("KEY ERROR")
            return False

    def show_device_nickname(self, output, args, **kwargs):
        try:
            result = NorthboundResults()
            result.add_result(output['data']['network']['device']['nickName'], args['nickname'])
            return result.return_result()
        except KeyError:
            self.logger.log_info("KEY ERROR")
            return False

    def show_device_sysname(self, output, args, **kwargs):
        try:
            result = NorthboundResults()
            result.add_result(output['data']['network']['device']['sysName'], args['sysname'])
            return result.return_result()
        except KeyError:
            self.logger.log_info("KEY ERROR")
            return False
