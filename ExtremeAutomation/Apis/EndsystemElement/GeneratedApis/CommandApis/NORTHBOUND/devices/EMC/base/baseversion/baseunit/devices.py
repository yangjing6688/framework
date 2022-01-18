"""
All devices supported northbound commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Library.Device.Common.CommandObjects.RestCommandObject import RestCommandObject
from ExtremeAutomation.Apis.EndsystemElement.GeneratedApis.CommandApis.NORTHBOUND.devices.base.devicesbase import \
    DevicesBase


class Devices(DeviceApi, DevicesBase):
    def __init__(self, device):
        super(Devices, self).__init__(device)

    def show_all_device_assettags(self, arg_dict):
        rest_request = RestCommandObject()
        rest_request.uri = "/nbi/graphql/"
        rest_request.data = '{network{devices{assetTag}}}'
        rest_request.request_type = "post"

        return self.device.send_command_object(rest_request)

    def show_all_device_basemacs(self, arg_dict):
        rest_request = RestCommandObject()
        rest_request.uri = "/nbi/graphql/"
        rest_request.data = '{network{devices{baseMac}}}'
        rest_request.request_type = "post"

        return self.device.send_command_object(rest_request)

    def show_all_device_sysnames(self, arg_dict):
        rest_request = RestCommandObject()
        rest_request.uri = "/nbi/graphql/"
        rest_request.data = '{network{devices{sysName}}}'
        rest_request.request_type = "post"

        return self.device.send_command_object(rest_request)

    def show_all_device_nicknames(self, arg_dict):
        rest_request = RestCommandObject()
        rest_request.uri = "/nbi/graphql/"
        rest_request.data = '{network{devices{nickName}}}'
        rest_request.request_type = "post"

        return self.device.send_command_object(rest_request)

    def show_all_device_ips(self, arg_dict):
        rest_request = RestCommandObject()
        rest_request.uri = "/nbi/graphql/"
        rest_request.data = '{network{devices{ip}}}'
        rest_request.request_type = "post"

        return self.device.send_command_object(rest_request)

    def show_device_assettag(self, arg_dict):
        rest_request = RestCommandObject()
        rest_request.uri = "/nbi/graphql/"
        rest_request.data = '{network{device(ip:"' + arg_dict["ip"] + '"){assetTag}}}'
        rest_request.request_type = "post"

        return self.device.send_command_object(rest_request)

    def show_device_basemac(self, arg_dict):
        rest_request = RestCommandObject()
        rest_request.uri = "/nbi/graphql/"
        rest_request.data = '{network{device(ip:"' + arg_dict["ip"] + '"){baseMac}}}'
        rest_request.request_type = "post"

        return self.device.send_command_object(rest_request)

    def show_device_bootprom(self, arg_dict):
        rest_request = RestCommandObject()
        rest_request.uri = "/nbi/graphql/"
        rest_request.data = '{network{device(ip:"' + arg_dict["ip"] + '"){bootProm}}}'
        rest_request.request_type = "post"

        return self.device.send_command_object(rest_request)

    def show_device_chassisid(self, arg_dict):
        rest_request = RestCommandObject()
        rest_request.uri = "/nbi/graphql/"
        rest_request.data = '{network{device(ip:"' + arg_dict["ip"] + '"){chassisId}}}'
        rest_request.request_type = "post"

        return self.device.send_command_object(rest_request)

    def show_device_chassis_type(self, arg_dict):
        rest_request = RestCommandObject()
        rest_request.uri = "/nbi/graphql/"
        rest_request.data = '{network{device(ip:"' + arg_dict["ip"] + '"){chassisType}}}'
        rest_request.request_type = "post"

        return self.device.send_command_object(rest_request)

    def show_device_devicedisplayfamily(self, arg_dict):
        rest_request = RestCommandObject()
        rest_request.uri = "/nbi/graphql/"
        rest_request.data = '{network{device(ip:"' + arg_dict["ip"] + '"){deviceDisplayFamily}}}'
        rest_request.request_type = "post"

        return self.device.send_command_object(rest_request)

    def show_device_deviceid(self, arg_dict):
        rest_request = RestCommandObject()
        rest_request.uri = "/nbi/graphql/"
        rest_request.data = '{network{device(ip:"' + arg_dict["ip"] + '"){deviceId}}}'
        rest_request.request_type = "post"

        return self.device.send_command_object(rest_request)

    def show_device_devicename(self, arg_dict):
        rest_request = RestCommandObject()
        rest_request.uri = "/nbi/graphql/"
        rest_request.data = '{network{device(ip:"' + arg_dict["ip"] + '"){deviceName}}}'
        rest_request.request_type = "post"

        return self.device.send_command_object(rest_request)

    def show_device_firmware(self, arg_dict):
        rest_request = RestCommandObject()
        rest_request.uri = "/nbi/graphql/"
        rest_request.data = '{network{device(ip:"' + arg_dict["ip"] + '"){firmware}}}'
        rest_request.request_type = "post"

        return self.device.send_command_object(rest_request)

    def show_device_id(self, arg_dict):
        rest_request = RestCommandObject()
        rest_request.uri = "/nbi/graphql/"
        rest_request.data = '{network{device(ip:"' + arg_dict["ip"] + '"){id}}}'
        rest_request.request_type = "post"

        return self.device.send_command_object(rest_request)

    def show_device_ip(self, arg_dict):
        rest_request = RestCommandObject()
        rest_request.uri = "/nbi/graphql/"
        rest_request.data = '{network{device(ip:"' + arg_dict["ip"] + '"){ip}}}'
        rest_request.request_type = "post"

        return self.device.send_command_object(rest_request)

    def show_device_name(self, arg_dict):
        rest_request = RestCommandObject()
        rest_request.uri = "/nbi/graphql/"
        rest_request.data = '{network{device(ip:"' + arg_dict["ip"] + '"){name}}}'
        rest_request.request_type = "post"

        return self.device.send_command_object(rest_request)

    def show_device_nickname(self, arg_dict):
        rest_request = RestCommandObject()
        rest_request.uri = "/nbi/graphql/"
        rest_request.data = '{network{device(ip:"' + arg_dict["ip"] + '"){nickName}}}'
        rest_request.request_type = "post"

        return self.device.send_command_object(rest_request)

    def show_device_sysname(self, arg_dict):
        rest_request = RestCommandObject()
        rest_request.uri = "/nbi/graphql/"
        rest_request.data = '{network{device(ip:"' + arg_dict["ip"] + '"){sysName}}}'
        rest_request.request_type = "post"

        return self.device.send_command_object(rest_request)
