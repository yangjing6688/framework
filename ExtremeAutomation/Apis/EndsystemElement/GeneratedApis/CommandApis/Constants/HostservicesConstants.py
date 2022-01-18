"""
This class outlines all the constants for the hostservices API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(HostservicesConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class HostservicesConstants(ApiConstants):
    def __init__(self):
        super(HostservicesConstants, self).__init__()
        self.DOWNLOAD_FILE_VIA_FTP = {"constant": "download_file_via_ftp",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.download_file_via_ftp}
        self.PING_HOST_FROM_ENDSYS = {"constant": "ping_host_from_endsys",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.ping_host_from_endsys}
