from ExtremeAutomation.Keywords.BaseClasses.EndsystemKeywordBaseClass import EndsystemKeywordBaseClass
from ExtremeAutomation.Apis.EndsystemElement.GeneratedApis.ParseApis.Constants.HostservicesConstants \
    import HostservicesConstants as ParseConstants
from ExtremeAutomation.Apis.EndsystemElement.GeneratedApis.CommandApis.Constants.HostservicesConstants \
    import HostservicesConstants as CommandConstants


class EndsystemHostServiceKeywords(EndsystemKeywordBaseClass):
    def __init__(self):
        super(EndsystemHostServiceKeywords, self).__init__()
        self.api_const = self.constants.API_HOSTSERVICES
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()

    def ping_host_address_from_endsys(self, device_name, host_address, count="1", **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [host_address] - The host address to be pinged.
        [count] - The number of pings to send.  Setting the default to 1 if not specified.

        Pings a host once by default.  The number of pings to be sent can be changed.
        """
        args = {"host_address": host_address,
                "count": count}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.PING_HOST_FROM_ENDSYS,
                                           self.parse_const.CHECK_PING_RESULT_ON_ENDSYS, True,
                                           "Host address {host_address} is reachable.",
                                           "Host address {host_address} is NOT reachable!",
                                           **kwargs)

    def download_file_via_ftp(self, device_name, host, username, password, file_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [host] - The hostname or IP of the FTP server.
        [username] - The FTP username
        [password] - The FTP password
        [file_name] - The name of the file to download.

        Downloads a <file_name> from <host> via FTP.
        """
        args = {"host": host,
                "user": username,
                "password": password,
                "file_name": file_name}

        return self.execute_keyword(device_name, args, self.cmd_const.DOWNLOAD_FILE_VIA_FTP, **kwargs)
