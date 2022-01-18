"""
This class outlines all the constants for the firmware API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(FirmwareConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class FirmwareConstants(ApiConstants):
    def __init__(self):
        super(FirmwareConstants, self).__init__()
        self.COMMIT_FIRMWARE = {"constant": "commit_firmware",
                                "tags": ["COMMAND_CLI"],
                                "link": self.link.commit_firmware}
        self.DELETE_FIRMWARE = {"constant": "delete_firmware",
                                "tags": ["COMMAND_CLI"],
                                "link": self.link.delete_firmware}
        self.DETERMINE_FIRMWARE = {"constant": "determine_firmware",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.determine_firmware}
        self.DOWNLOAD_FIRMWARE = {"constant": "download_firmware",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.download_firmware}
        self.DOWNLOAD_FIRMWARE_HTTPS = {"constant": "download_firmware_https",
                                        "tags": ["COMMAND_CLI"],
                                        "link": self.link.download_firmware_https}
        self.DOWNLOAD_FIRMWARE_SCP = {"constant": "download_firmware_scp",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.download_firmware_scp}
        self.DOWNLOAD_FIRMWARE_SFTP = {"constant": "download_firmware_sftp",
                                       "tags": ["COMMAND_CLI"],
                                       "link": self.link.download_firmware_sftp}
        self.SELECT_FIRMWARE = {"constant": "select_firmware",
                                "tags": ["COMMAND_CLI"],
                                "link": self.link.select_firmware}
        self.SHOW_FIRMWARE_INFO = {"constant": "show_firmware_info",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.show_firmware_info}
        self.SHOW_FIRMWARE_VERSION = {"constant": "show_firmware_version",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.show_firmware_version}
        self.SHOW_INSTALLED_IMAGES = {"constant": "show_installed_images",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.show_installed_images}
        self.UNINSTALL_XMOD = {"constant": "uninstall_xmod",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.uninstall_xmod}
