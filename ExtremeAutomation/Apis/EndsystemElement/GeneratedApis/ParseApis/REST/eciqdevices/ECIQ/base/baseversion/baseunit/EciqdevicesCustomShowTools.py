from ExtremeAutomation.Apis.EndsystemElement.GeneratedApis.ParseApis.REST.eciqdevices.base.\
    EciqdevicesBaseCustomShowTools import EciqdevicesBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Keywords.Utils.DeviceValueStorage import DeviceValueStorage


class EciqdevicesCustomShowTools(EciqdevicesBaseCustomShowTools):
    def __init__(self, device):
        super(EciqdevicesCustomShowTools, self).__init__(device)

    def store_device_id_for_serial_number(self, output, args, **kwargs):
        ret_output = output['data']
        for item in ret_output:
            if item['serialId'] == args['serial_number']:
                DeviceValueStorage().add_value(self.device.name, args["var_name"], item['deviceId'])
                return True, {"ret_device_id": item['deviceId']}
        self.logger.log_info("The serial number of the DUT was not found!")
        return False, {"ret_serial_number": None}

    def verify_device_firmware(self, output, args, **kwargs):
        ret_output = output['data']
        for item in ret_output:
            if item['serialId'] == args['serial_number'] and item['osVersion'] == args['firmware_version']:
                return True, item['osVersion']
        return False, args['firmware_version']

    def verify_device_ip(self, output, args, **kwargs):
        ret_output = output['data']
        for item in ret_output:
            if item['serialId'] == args['serial_number'] and item['ip'] == args['mgmt_ip']:
                return True, item['ip']
        return False, args['mgmt_ip']

    def verify_device_mac(self, output, args, **kwargs):
        ret_output = output['data']
        for item in ret_output:
            if item['serialId'] == args['serial_number'] and item['macAddress'] == args['mac_addr']:
                return True, item['macAddress']
        return False, args['mac_addr']

    def verify_device_model(self, output, args, **kwargs):
        ret_output = output['data']
        for item in ret_output:
            if item['serialId'] == args['serial_number'] and item['model'] == args['model']:
                return True, item['model']
        return False, args['model']

    def verify_device_serial_number(self, output, args, **kwargs):
        ret_output = output['data']
        for item in ret_output:
            if item['serialId'] == args['serial_number']:
                return True, item['serialId']
        return False, args['serial_number']
