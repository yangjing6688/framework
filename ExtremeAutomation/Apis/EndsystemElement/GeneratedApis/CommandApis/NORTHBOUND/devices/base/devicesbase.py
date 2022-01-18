"""
Base class for all devices northbound commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.BaseApi import BaseApi
from ExtremeAutomation.Library.Device.Common.CommandObjects.RestCommandObject import RestCommandObject


class DevicesBase(BaseApi):
    def __init__(self, device):
        self.device = device

        def show_all_device_assettags(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request

        def show_all_device_basemacs(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request

        def show_all_device_sysnames(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request

        def show_all_device_nicknames(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request

        def show_all_device_ips(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request

        def show_device_assettag(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request

        def show_device_basemac(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request

        def show_device_bootprom(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request

        def show_device_chassisid(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request

        def show_device_chassis_type(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request

        def show_device_devicedisplayfamily(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request

        def show_device_deviceid(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request

        def show_device_devicename(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request

        def show_device_firmware(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request

        def show_device_id(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request

        def show_device_ip(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request

        def show_device_name(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request

        def show_device_nickname(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request

        def show_device_sysname(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request
