from ExtremeAutomation.Keywords.BaseClasses.EndsystemKeywordBaseClass import EndsystemKeywordBaseClass
from ExtremeAutomation.Apis.EndsystemElement.GeneratedApis.ParseApis.Constants.CommonConstants \
    import CommonConstants as ParseConstants
from ExtremeAutomation.Apis.EndsystemElement.GeneratedApis.CommandApis.Constants.CommonConstants \
    import CommonConstants as CommandConstants


class CommonEndsystemKeywords(EndsystemKeywordBaseClass):
    def __init__(self):
        super(CommonEndsystemKeywords, self).__init__()
        self.api_const = self.constants.API_COMMON
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()

    def get_dir(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.

        Valid **kwargs:
        [ignore_cli_feedback] - If set to True CLI feedback is ignored.
        [expect_error] - Used for negative testing. Enable if you expect the command
                         sent to cause an error.

        Dictionary Arguments:

        """
        return self.execute_keyword(device_name, {}, self.cmd_const.GET_DIR, **kwargs)

    def remove_file(self, device_name, file_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device that the keyword should be run against.
        [file_name] - The name of the file that should be removed.

        Removes the given file from a device.
        """
        args = {"file_name": file_name}

        return self.execute_keyword(device_name, args, self.cmd_const.REMOVE_FILE, **kwargs)

    def verify_file_exists(self, device_name, file_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [file_name] - The name of the file that should exist on the device.

        Verifies that a file with name <file_name> exists on the device.
        """
        args = {"file_name": file_name}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.GET_DIR,
                                           self.parse_const.CHECK_FILE_EXISTS, True,
                                           "File {file_name} exists on {device_name}.",
                                           "File {file_name} DOES NOT exist on {device_name}.",
                                           **kwargs)

    def verify_file_does_not_exist(self, device_name, file_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [file_name] - The name of the file that should not exist on the device.

        Verifies that a file with name <file_name> does not exist on the device.
        """
        args = {"file_name": file_name}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.GET_DIR,
                                           self.parse_const.CHECK_FILE_EXISTS, False,
                                           "File {file_name} does not exist on {device_name}.",
                                           "File {file_name} EXISTS on {device_name}.",
                                           **kwargs)
