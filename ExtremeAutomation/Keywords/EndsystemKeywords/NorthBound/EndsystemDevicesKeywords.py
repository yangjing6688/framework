"""
Keyword class for all devices northbound commands.
"""
from ExtremeAutomation.Keywords.BaseClasses.EndsystemKeywordBaseClass import EndsystemKeywordBaseClass
from ExtremeAutomation.Apis.EndsystemElement.GeneratedApis.ParseApis.Constants.DevicesConstants import \
    DevicesConstants as ParseConstants
from ExtremeAutomation.Apis.EndsystemElement.GeneratedApis.CommandApis.Constants.DevicesConstants import \
    DevicesConstants as CommandConstants


class EndsystemDevicesKeywords(EndsystemKeywordBaseClass):
    def __init__(self):
        super(EndsystemDevicesKeywords, self).__init__()
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()
        self.api_const = "devices"

    def verify_show_all_device_assettags(self, device_name, **kwargs):
        """Verifies the output from show_all_device_assettags."""
        return self.execute_verify_keyword(device_name, kwargs,
                                           self.cmd_const.SHOW_ALL_DEVICE_ASSETTAGS,
                                           self.parse_const.SHOW_ALL_DEVICE_ASSETTAGS,
                                           True, "PASSED", "FAILED", **kwargs)

    def verify_show_all_device_basemacs(self, device_name, **kwargs):
        """Verifies the output from show_all_device_basemacs."""
        return self.execute_verify_keyword(device_name, kwargs,
                                           self.cmd_const.SHOW_ALL_DEVICE_BASEMACS,
                                           self.parse_const.SHOW_ALL_DEVICE_BASEMACS,
                                           True, "PASSED", "FAILED", **kwargs)

    def verify_show_all_device_sysnames(self, device_name, **kwargs):
        """Verifies the output from show_all_device_sysnames."""
        return self.execute_verify_keyword(device_name, kwargs,
                                           self.cmd_const.SHOW_ALL_DEVICE_SYSNAMES,
                                           self.parse_const.SHOW_ALL_DEVICE_SYSNAMES,
                                           True, "PASSED", "FAILED", **kwargs)

    def verify_show_all_device_nicknames(self, device_name, **kwargs):
        """Verifies the output from show_all_device_nicknames."""
        return self.execute_verify_keyword(device_name, kwargs,
                                           self.cmd_const.SHOW_ALL_DEVICE_NICKNAMES,
                                           self.parse_const.SHOW_ALL_DEVICE_NICKNAMES,
                                           True, "PASSED", "FAILED", **kwargs)

    def verify_show_all_device_ips(self, device_name, **kwargs):
        """Verifies the output from show_all_device_ips."""
        return self.execute_verify_keyword(device_name, kwargs,
                                           self.cmd_const.SHOW_ALL_DEVICE_IPS,
                                           self.parse_const.SHOW_ALL_DEVICE_IPS,
                                           True, "PASSED", "FAILED", **kwargs)

    def verify_show_device_assettag(self, device_name, **kwargs):
        """Verifies the output from show_device_assettag."""
        return self.execute_verify_keyword(device_name, kwargs,
                                           self.cmd_const.SHOW_DEVICE_ASSETTAG,
                                           self.parse_const.SHOW_DEVICE_ASSETTAG,
                                           True, "PASSED", "FAILED", **kwargs)

    def verify_show_device_basemac(self, device_name, **kwargs):
        """Verifies the output from show_device_basemac."""
        return self.execute_verify_keyword(device_name, kwargs,
                                           self.cmd_const.SHOW_DEVICE_BASEMAC,
                                           self.parse_const.SHOW_DEVICE_BASEMAC,
                                           True, "PASSED", "FAILED", **kwargs)

    def verify_show_device_bootprom(self, device_name, **kwargs):
        """Verifies the output from show_device_bootprom."""
        return self.execute_verify_keyword(device_name, kwargs,
                                           self.cmd_const.SHOW_DEVICE_BOOTPROM,
                                           self.parse_const.SHOW_DEVICE_BOOTPROM,
                                           True, "PASSED", "FAILED", **kwargs)

    def verify_show_device_chassisid(self, device_name, **kwargs):
        """Verifies the output from show_device_chassisid."""
        return self.execute_verify_keyword(device_name, kwargs,
                                           self.cmd_const.SHOW_DEVICE_CHASSISID,
                                           self.parse_const.SHOW_DEVICE_CHASSISID,
                                           True, "PASSED", "FAILED", **kwargs)

    def verify_show_device_chassis_type(self, device_name, **kwargs):
        """Verifies the output from show_device_chassis_type."""
        return self.execute_verify_keyword(device_name, kwargs,
                                           self.cmd_const.SHOW_DEVICE_CHASSIS_TYPE,
                                           self.parse_const.SHOW_DEVICE_CHASSIS_TYPE,
                                           True, "PASSED", "FAILED", **kwargs)

    def verify_show_device_devicedisplayfamily(self, device_name, **kwargs):
        """Verifies the output from show_device_devicedisplayfamily."""
        return self.execute_verify_keyword(device_name, kwargs,
                                           self.cmd_const.SHOW_DEVICE_DEVICEDISPLAYFAMILY,
                                           self.parse_const.SHOW_DEVICE_DEVICEDISPLAYFAMILY,
                                           True, "PASSED", "FAILED", **kwargs)

    def verify_show_device_deviceid(self, device_name, **kwargs):
        """Verifies the output from show_device_deviceid."""
        return self.execute_verify_keyword(device_name, kwargs,
                                           self.cmd_const.SHOW_DEVICE_DEVICEID,
                                           self.parse_const.SHOW_DEVICE_DEVICEID,
                                           True, "PASSED", "FAILED", **kwargs)

    def verify_show_device_devicename(self, device_name, **kwargs):
        """Verifies the output from show_device_devicename."""
        return self.execute_verify_keyword(device_name, kwargs,
                                           self.cmd_const.SHOW_DEVICE_DEVICENAME,
                                           self.parse_const.SHOW_DEVICE_DEVICENAME,
                                           True, "PASSED", "FAILED", **kwargs)

    def verify_show_device_firmware(self, device_name, **kwargs):
        """Verifies the output from show_device_firmware."""
        return self.execute_verify_keyword(device_name, kwargs,
                                           self.cmd_const.SHOW_DEVICE_FIRMWARE,
                                           self.parse_const.SHOW_DEVICE_FIRMWARE,
                                           True, "PASSED", "FAILED", **kwargs)

    def verify_show_device_id(self, device_name, **kwargs):
        """Verifies the output from show_device_id."""
        return self.execute_verify_keyword(device_name, kwargs,
                                           self.cmd_const.SHOW_DEVICE_ID,
                                           self.parse_const.SHOW_DEVICE_ID,
                                           True, "PASSED", "FAILED", **kwargs)

    def verify_show_device_ip(self, device_name, **kwargs):
        """Verifies the output from show_device_ip."""
        return self.execute_verify_keyword(device_name, kwargs,
                                           self.cmd_const.SHOW_DEVICE_IP,
                                           self.parse_const.SHOW_DEVICE_IP,
                                           True, "PASSED", "FAILED", **kwargs)

    def verify_show_device_name(self, device_name, **kwargs):
        """Verifies the output from show_device_name."""
        return self.execute_verify_keyword(device_name, kwargs,
                                           self.cmd_const.SHOW_DEVICE_NAME,
                                           self.parse_const.SHOW_DEVICE_NAME,
                                           True, "PASSED", "FAILED", **kwargs)

    def verify_show_device_nickname(self, device_name, **kwargs):
        """Verifies the output from show_device_nickname."""
        return self.execute_verify_keyword(device_name, kwargs,
                                           self.cmd_const.SHOW_DEVICE_NICKNAME,
                                           self.parse_const.SHOW_DEVICE_NICKNAME,
                                           True, "PASSED", "FAILED", **kwargs)

    def verify_show_device_sysname(self, device_name, **kwargs):
        """Verifies the output from show_device_sysname."""
        return self.execute_verify_keyword(device_name, kwargs,
                                           self.cmd_const.SHOW_DEVICE_SYSNAME,
                                           self.parse_const.SHOW_DEVICE_SYSNAME,
                                           True, "PASSED", "FAILED", **kwargs)
