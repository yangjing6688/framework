from ExtremeAutomation.Library.Device.Common.Apis.BaseShowApi import BaseShowApi
from ExtremeAutomation.Library.Device.EndsystemElement.Constants.EndsystemElementConstants import EndsystemElementConstants


class DevicesBaseCustomShowTools(BaseShowApi):
    def __init__(self, device):
        super(DevicesBaseCustomShowTools, self).__init__()
        self.device = device

    def show_all_device_assettags(self, *args):
        return EndsystemElementConstants.METHOD_NOT_SUPPORTED

    def show_all_device_basemacs(self, *args):
        return EndsystemElementConstants.METHOD_NOT_SUPPORTED

    def show_all_device_sysnames(self, *args):
        return EndsystemElementConstants.METHOD_NOT_SUPPORTED

    def show_all_device_nicknames(self, *args):
        return EndsystemElementConstants.METHOD_NOT_SUPPORTED

    def show_all_device_ips(self, *args):
        return EndsystemElementConstants.METHOD_NOT_SUPPORTED

    def show_device_assettag(self, *args):
        return EndsystemElementConstants.METHOD_NOT_SUPPORTED

    def show_device_basemac(self, *args):
        return EndsystemElementConstants.METHOD_NOT_SUPPORTED

    def show_device_bootprom(self, *args):
        return EndsystemElementConstants.METHOD_NOT_SUPPORTED

    def show_device_chassisid(self, *args):
        return EndsystemElementConstants.METHOD_NOT_SUPPORTED

    def show_device_chassis_type(self, *args):
        return EndsystemElementConstants.METHOD_NOT_SUPPORTED

    def show_device_devicedisplayfamily(self, *args):
        return EndsystemElementConstants.METHOD_NOT_SUPPORTED

    def show_device_deviceid(self, *args):
        return EndsystemElementConstants.METHOD_NOT_SUPPORTED

    def show_device_devicename(self, *args):
        return EndsystemElementConstants.METHOD_NOT_SUPPORTED

    def show_device_firmware(self, *args):
        return EndsystemElementConstants.METHOD_NOT_SUPPORTED

    def show_device_id(self, *args):
        return EndsystemElementConstants.METHOD_NOT_SUPPORTED

    def show_device_ip(self, *args):
        return EndsystemElementConstants.METHOD_NOT_SUPPORTED

    def show_device_name(self, *args):
        return EndsystemElementConstants.METHOD_NOT_SUPPORTED

    def show_device_nickname(self, *args):
        return EndsystemElementConstants.METHOD_NOT_SUPPORTED

    def show_device_sysname(self, *args):
        return EndsystemElementConstants.METHOD_NOT_SUPPORTED
