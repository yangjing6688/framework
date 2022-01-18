from ExtremeAutomation.Library.Utils.ListUtils import ListUtils
from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import \
    NetworkElementKeywordBaseClass
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.Constants.FirmwareConstants \
    import FirmwareConstants as FirmwareCommandConstants
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.Constants.SysinfoConstants \
    import SysinfoConstants as SysinfoParseConstants
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.Constants.FilemanagementConstants \
    import FilemanagementConstants as FilemanagementCommandConstants
from pytest_testconfig import config
from ExtremeAutomation.Imports.pytestConfigHelper import PytestConfigHelper

class NetworkElementFirmwareUtilsKeywords(NetworkElementKeywordBaseClass):
    def __init__(self):
        super(NetworkElementFirmwareUtilsKeywords, self).__init__()
        self.firmware_cmd_const = FirmwareCommandConstants()
        self.filemgmt_parse_const = FilemanagementCommandConstants()
        self.sysinfo_parse_const = SysinfoParseConstants()

    # ##################################################################################################################
    #   Configuration Keywords   #######################################################################################
    # ##################################################################################################################
    def firmware_version_should_be_equal(self, device_names, expected_version, **kwargs):
        """
        Keyword Arguments:
        [device_names] - The device(s) the keyword should be run against.
        [expected_version] - The FW version that should be loaded on the device.

        Verifies that the given firmware version is loaded on the device.
        """
        device_names = ListUtils.convert_to_list(device_names)
        kw_results = []
        for device_name in device_names:
            dev, cmd_api, parse_api = self._init_keyword(device_name, self.constants.API_FIRMWARE,
                                                         self.constants.API_SYSINFO, **kwargs)
            cmd_obj = getattr(cmd_api, self.firmware_cmd_const.SHOW_FIRMWARE_INFO)(expected_version, **kwargs)
            if not cmd_obj.not_supported:
                cmd_obj = dev.send_command_object(cmd_obj)
                output = cmd_obj.return_text
                parse_result, ret_val = getattr(parse_api, self.sysinfo_parse_const.CHECK_FIRMWARE_VERSION)(
                    output, expected_version, **kwargs)
                kw_results.append(self._determine_result(dev, cmd_obj, parse_result, True,
                                                         "Device " + device_name + " firmware version was equal to " +
                                                         expected_version + ".",
                                                         "Device " + device_name +
                                                         " firmware version was NOT equal to " + expected_version + ".",
                                                         **kwargs))
                return self._keyword_cleanup(kw_results, ret_val), ret_val

    def firmware_version_should_not_be_equal(self, device_names, version, **kwargs):
        """
        Keyword Arguments:
        [device_names] - The device(s) the keyword should be run against.
        [version] - The version of FW that the device should not be running.

        Verifies that the device is not running the version of firmware provided.
        """
        device_names = ListUtils.convert_to_list(device_names)
        kw_results = []
        for device_name in device_names:
            dev, cmd_api, parse_api = self._init_keyword(device_name, self.constants.API_FIRMWARE,
                                                         self.constants.API_SYSINFO, **kwargs)
            cmd_obj = getattr(cmd_api, self.firmware_cmd_const.SHOW_FIRMWARE_INFO)(version, **kwargs)
            if not cmd_obj.not_supported:
                cmd_obj = dev.send_command_object(cmd_obj)
                output = cmd_obj.return_text
                parse_result, ret_val = getattr(parse_api, self.sysinfo_parse_const.CHECK_FIRMWARE_VERSION)(
                    output, version, **kwargs)
                kw_results.append(self._determine_result(dev, cmd_obj, parse_result, False,
                                                         "Device " + device_name + " firmware version was equal to " +
                                                         version + ".",
                                                         "Device " + device_name +
                                                         " firmware version was NOT equal to " + version + ".",
                                                         **kwargs))
                return self._keyword_cleanup(kw_results, ret_val), ret_val

    def delete_firmware_on_network_element(self, device_names, filename=None, version=None, answer="n", **kwargs):
        """
        Keyword Arguments:
        [device_names] - The device(s) the keyword should be run against.
        [filename] - The filename of the firmware to delete.
        [version] - The version number of the firmware to delete.
        [answer] - answer to question if it pertains. Only acceptable values are 'n' or 'y'

        Deletes the given firmware from a network element.
        """
        device_names = ListUtils.convert_to_list(device_names)
        kw_results = []
        for device_name in device_names:
            dev, cmd_api, parse_api = self._init_keyword(device_name, self.constants.API_FIRMWARE,
                                                         self.constants.API_FILEMANAGEMENT, wait_for_prompt=False,
                                                         **kwargs)

            args = {"filename": filename,
                    "version": version,
                    "answer": answer}

            if filename is not None:
                cmd_obj = getattr(cmd_api, self.firmware_cmd_const.DELETE_FIRMWARE)(args,
                                                                                    ignore_cli_feedback=True,
                                                                                    **kwargs)
                if not cmd_obj.not_supported:
                    self.logger.log_info("\nConfirmation answer to delete was:" + args['answer'] + '\n')
                    cmd_obj = dev.send_command_object(cmd_obj)
                    kw_results.append(self._determine_result(dev, cmd_obj,
                                                             pass_string="Firmware version " + args['filename'] +
                                                             " was Deleted on " + device_name + ".",
                                                             fail_string="Firmware version " + args['filename'] +
                                                             " was NOT Deleted on " + device_name + ".",
                                                             **kwargs))
                    return self._keyword_cleanup(kw_results)

            elif version is not None and filename is None:
                cmd_obj = getattr(cmd_api, self.firmware_cmd_const.DETERMINE_FIRMWARE)(args, **kwargs)
                if not cmd_obj.not_supported:
                    cmd_obj = dev.send_command_object(cmd_obj)
                    output = cmd_obj.return_text
                    result, filename = getattr(
                        parse_api, self.filemgmt_parse_const.GET_VERSION_FILENAME)(output, version, **kwargs)

                    kw_results.append(self._determine_result(dev, cmd_obj, result, True,
                                                             "Firmware version " + version + " was installed on " +
                                                             device_name + ".", "Firmware version " + version +
                                                             " was NOT installed on " + device_name + ".", **kwargs))
                    if result is False:
                        return self._keyword_cleanup(kw_results)

                    else:
                        args['filename'] = filename
                        cmd_obj = getattr(
                            cmd_api, self.firmware_cmd_const.DELETE_FIRMWARE)(args, ignore_cli_feedback=True, **kwargs)
                        self.logger.log_info("\nConfirmation answer to boot was:" + args['answer'] + '\n')
                        cmd_obj = dev.send_command_object(cmd_obj)
                        kw_results.append(self._determine_result(dev, cmd_obj,
                                                                 pass_string="Firmware version " + version +
                                                                 " was Deleted on " + device_name + ".",
                                                                 fail_string="Firmware version " + version +
                                                                 " was NOT Deleted on " + device_name + ".",
                                                                 **kwargs))
                        return self._keyword_cleanup(kw_results)
            else:
                cmd_obj = getattr(cmd_api, self.firmware_cmd_const.DELETE_FIRMWARE)(args,
                                                                                    ignore_cli_feedback=True,
                                                                                    **kwargs)
                kw_results.append(self._determine_result(dev, cmd_obj, False, True,
                                                         fail_string="No filename or firmware version provided.",
                                                         **kwargs))
                return self._keyword_cleanup(kw_results)

    def select_firmware_on_network_element(self, device_names, filename=None, version=None, answer='n', **kwargs):
        """
        Keyword Arguments:
        [device_names] - The device(s) the keyword should be run against.
        [filename] - The filename of the firmware to load.
        [version] - The version number of the firmware to load.

        Loads the given firmware on a network element.
        """
        device_names = ListUtils.convert_to_list(device_names)
        kw_results = []
        for device_name in device_names:
            dev, cmd_api, parse_api = self._init_keyword(device_name, self.constants.API_FIRMWARE,
                                                         self.constants.API_FILEMANAGEMENT, wait_for_prompt=False,
                                                         **kwargs)

            args = {"filename": filename,
                    "version": version,
                    "answer": answer}

            if filename is not None:
                cmd_obj = getattr(cmd_api, self.firmware_cmd_const.SELECT_FIRMWARE)(args,
                                                                                    ignore_cli_feedback=True,
                                                                                    **kwargs)
                if not cmd_obj.not_supported:
                    self.logger.log_info("\nConfirmation answer to boot was:" + args['answer'] + '\n')
                    cmd_obj = dev.send_command_object(cmd_obj)
                    kw_results.append(self._determine_result(dev, cmd_obj,
                                                             pass_string="Firmware version " + args['filename'] +
                                                             " was selected to boot on " + device_name + ".",
                                                             fail_string="Firmware version " + args['filename'] +
                                                             " was NOT selected to boot " + device_name + ".",
                                                             **kwargs))
                    return self._keyword_cleanup(kw_results)

            elif version is not None and filename is None:
                cmd_obj = getattr(cmd_api, self.firmware_cmd_const.DETERMINE_FIRMWARE)(args, **kwargs)
                if not cmd_obj.not_supported:
                    cmd_obj = dev.send_command_object(cmd_obj)
                    output = cmd_obj.return_text
                    result, filename = getattr(
                        parse_api, self.filemgmt_parse_const.GET_VERSION_FILENAME)(output, version, **kwargs)

                    kw_results.append(self._determine_result(dev, cmd_obj, result, True,
                                                             "Firmware version " + version + " was installed on " +
                                                             device_name + ".", "Firmware version " + version +
                                                             " was NOT installed on " + device_name + ".", **kwargs))
                    if result is False:
                        return self._keyword_cleanup(kw_results)

                    else:
                        args['filename'] = filename
                        cmd_obj = getattr(cmd_api, self.firmware_cmd_const.SELECT_FIRMWARE)(args,
                                                                                            ignore_cli_feedback=True,
                                                                                            **kwargs)
                        self.logger.log_info("\nConfirmation answer to boot was:" + args['answer'] + '\n')
                        cmd_obj = dev.send_command_object(cmd_obj)
                        kw_results.append(self._determine_result(dev, cmd_obj,
                                                                 pass_string="Firmware version " + version +
                                                                 " was selected to boot on " + device_name + ".",
                                                                 fail_string="Firmware version " + version +
                                                                 " was NOT selected to boot " + device_name + ".",
                                                                 **kwargs))
                        return self._keyword_cleanup(kw_results)
            else:
                cmd_obj = getattr(cmd_api, self.firmware_cmd_const.SELECT_FIRMWARE)(args,
                                                                                    ignore_cli_feedback=True,
                                                                                    **kwargs)
                kw_results.append(self._determine_result(dev, cmd_obj, False, True,
                                                         fail_string="No filename or firmware version provided.",
                                                         **kwargs))
                return self._keyword_cleanup(kw_results)

    def load_firmware_on_network_element(self, device_names, server, filename, version=None, vr="vr-default",
                                         image_location='primary', reset='no-reset', server_type='tftp',
                                         username='sftpuser', password='sftpuser', **kwargs):
        """
        Keyword Arguments:
        [device_names] - The device the keyword should be run against.
        [server] - The IP address of the server where the image is located.
        [filename] - The filename, including tftp path, of the image.
        [version] - The image version being downloaded.
        [vr] - The VR which the server IP resides on.

        Downloads a specified firmware image onto the device(s).
        """
        device_names = ListUtils.convert_to_list(device_names)
        result = False
        kw_results = []
        for device_name in device_names:
            args = {"server": server,
                    "filename": filename,
                    "version": version,
                    "vr": vr,
                    "answer": "y",
                    'image_location': image_location,
                    'reset': reset,
                    'server_type': server_type,
                    'username': username,
                    'password': password}

            wait_for_prompt = True
            if reset != "no-reset":
                wait_for_prompt = False
            dev, cmd_api, parse_api = self._init_keyword(device_name, self.constants.API_FIRMWARE,
                                                         self.constants.API_FILEMANAGEMENT, cmd_delay=120000,
                                                         wait_for_prompt=wait_for_prompt, **kwargs)

            cmd_obj = getattr(cmd_api, self.firmware_cmd_const.DETERMINE_FIRMWARE)(args, **kwargs)
            if dev.oper_sys == self.constants.OS_LINUX:
                self.logger.log_info("Bypassing version check for ezFabric.")
                result = False
            elif version is None:
                version = filename
                result = False
            else:
                cmd_obj = getattr(cmd_api, self.firmware_cmd_const.DETERMINE_FIRMWARE)(args, **kwargs)
                if not cmd_obj.not_supported:
                    cmd_obj = dev.send_command_object(cmd_obj)
                    output = cmd_obj.return_text
                    result, _ = getattr(parse_api, self.sysinfo_parse_const.CHECK_FIRMWARE_VERSION)(output, version,
                                                                                                    **kwargs)

            if result and result != self.cmd_obj_constants.METHOD_NOT_SUPPORTED:
                self.logger.log_info("Firmware version " + version + " is already installed on " + device_name + ".")

                kw_results.append(self._determine_result(dev, cmd_obj, **kwargs))

            else:
                if not dev.oper_sys == self.constants.OS_LINUX:
                    self.logger.log_info("Firmware version " + version + " was not installed on " + device_name +
                                         ". Beginning download.")

                if dev.oper_sys == self.constants.OS_EOS:
                    self.verify_max_images(device_name)

                if server_type.lower() == "tftp":
                    cmd_obj = getattr(cmd_api, self.firmware_cmd_const.DOWNLOAD_FIRMWARE)(args, **kwargs)
                    if not cmd_obj.not_supported:
                        cmd_obj = dev.send_command_object(cmd_obj)
                        kw_results.append(self._determine_result(dev, cmd_obj, pass_string="Downloading using TFTP",
                                                                 **kwargs))
                elif server_type.lower() == "scp":
                    cmd_obj = getattr(cmd_api, self.firmware_cmd_const.DOWNLOAD_FIRMWARE_SCP)(args, **kwargs)
                    if not cmd_obj.not_supported:
                        cmd_obj = dev.send_command_object(cmd_obj)
                        kw_results.append(self._determine_result(dev, cmd_obj, pass_string="Downloading using SCP",
                                                                 **kwargs))
                elif server_type.lower() == "https":
                    cmd_obj = getattr(cmd_api, self.firmware_cmd_const.DOWNLOAD_FIRMWARE_HTTPS)(args, **kwargs)
                    if not cmd_obj.not_supported:
                        cmd_obj = dev.send_command_object(cmd_obj)
                        kw_results.append(self._determine_result(dev, cmd_obj, pass_string="Downloading using HTTPS",
                                                                 **kwargs))
                else:
                    cmd_obj = getattr(cmd_api, self.firmware_cmd_const.DOWNLOAD_FIRMWARE_SFTP)(args, **kwargs)
                    if not cmd_obj.not_supported:
                        cmd_obj = dev.send_command_object(cmd_obj)
                        kw_results.append(self._determine_result(dev, cmd_obj, pass_string="Downloading using SFTP",
                                                                 **kwargs))

        return self._keyword_cleanup(kw_results)

    # # ###############################################################################################################
    # #   Inspection Keywords   #######################################################################################
    # # ###############################################################################################################
    def verify_max_images(self, device_names, **kwargs):
        """
        Keyword Arguments:
        [device_names] - The device the keyword should be run against.

        Check if the device has the maximum images installed and deletes one if necessary.
        """
        device_names = ListUtils.convert_to_list(device_names)
        kw_results = []
        for device_name in device_names:
            args = {}
            dev, cmd_api, parse_api = self._init_keyword(device_name, self.constants.API_FIRMWARE,
                                                         self.constants.API_FILEMANAGEMENT, **kwargs)

            cmd_obj = getattr(cmd_api, self.firmware_cmd_const.DETERMINE_FIRMWARE)(args, **kwargs)
            if not cmd_obj.not_supported:
                cmd_obj = dev.send_command_object(cmd_obj)
                output = cmd_obj.return_text
                result, imagename = getattr(
                    parse_api, self.sysinfo_parse_const.CHECK_FIRMWARE_VERSION)(output, **kwargs)
            else:
                result = False
                imagename = None

            if result:
                self.logger.log_info("Firmware image " + str(imagename) +
                                     " is not in use and will be deleted.")
                args = {"imagename": imagename}

                cmd_obj = getattr(cmd_api, self.firmware_cmd_const.DELETE_FIRMWARE)(args, **kwargs)
                if not cmd_obj.not_supported:
                    cmd_obj = dev.send_command_object(cmd_obj)

                kw_results.append(self._determine_result(dev, cmd_obj, **kwargs))

            else:
                self.logger.log_info("Device " + device_name + " has less than the maximum allowed images.")

        return self._keyword_cleanup(kw_results)

    def commit_firmware(self, device_names, **kwargs):
        """
        Keyword Arguments:
        [device_names] - The device the keyword should be run against.

        Commits the software.
        """
        device_names = ListUtils.convert_to_list(device_names)
        kw_results = []
        for device_name in device_names:
            args = {}
            dev, cmd_api, _ = self._init_keyword(device_name, self.constants.API_FIRMWARE, **kwargs)
            cmd_obj = getattr(cmd_api, self.firmware_cmd_const.COMMIT_FIRMWARE)(args, **kwargs)
            if not cmd_obj.not_supported:
                cmd_obj = dev.send_command_object(cmd_obj)
                kw_results.append(self._determine_result(dev, cmd_obj, **kwargs))
            return self._keyword_cleanup(kw_results)

    def save_running_firmware(self, **kwargs):
        """
        Keyword Arguments:
        Store network element version as dev.running_version  and netelem#.running_version
        """
        hConfig = PytestConfigHelper(config)
        self.logger.log_info(f"hconfig nodecount = {hConfig.node_count}")
        kw_results = []
        i=0
        while i < hConfig.node_count:
            i+=1
            device_name = config[f'netelem{i}']['name']
            args = {}
            dev, cmd_api, parse_api = self._init_keyword(device_name, self.constants.API_FIRMWARE,
                                                         self.constants.API_SYSINFO, **kwargs)
            cmd_obj = getattr(cmd_api, self.firmware_cmd_const.SHOW_FIRMWARE_VERSION)(args, **kwargs)
            if not cmd_obj.not_supported:
                cmd_obj = dev.send_command_object(cmd_obj)
                output = cmd_obj.return_text
                parse_result, ret_val = getattr(parse_api, self.sysinfo_parse_const.GET_FIRMWARE_VERSION)(output, **kwargs)
                dev.running_version = ret_val
                config[f'netelem{i}']['running_version'] = ret_val
                self.logger.log_info(f"Running version: {ret_val}")
                kw_results.append(self._determine_result(dev, cmd_obj, parse_result, None,
                                                         "Firmware version found: " + ret_val,
                                                         "Firmware version not found:" + ret_val,
                                                         get_only=True))
        return self._keyword_cleanup(kw_results)
