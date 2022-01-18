from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import \
    NetworkElementKeywordBaseClass
from ExtremeAutomation.Library.Utils import RobotUtils
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.Constants.FilemanagementConstants  \
    import FilemanagementConstants as CommandConstants
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.Constants.FilemanagementConstants  \
    import FilemanagementConstants as ParseConstants
from ExtremeAutomation.Library.Utils.NetworkElementUtils import NetworkElementUtils



class NetworkElementFileManagementUtilsKeywords(NetworkElementKeywordBaseClass):
    def __init__(self):
        super(NetworkElementFileManagementUtilsKeywords, self).__init__()
        self.api_const = self.constants.API_FILEMANAGEMENT
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()

    # ##################################################################################################################
    #   Configuration Keywords   #######################################################################################
    # ##################################################################################################################

    def save_current_config(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The name of the device to save the configuration on.

        Saves the current config to the currently loaded config.
        """
        args = {"save_config": "y",
                "oid_index": "0"}

        return self.execute_keyword(device_name, args, self.cmd_const.SAVE_CURRENT_CONFIG, **kwargs)

    def load_config_on_network_element(self, device_name, config_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should run against.
        [config_name] - The name of the configuration that should be loaded.

        Loads the given configuration on the network element. This will not reboot the device if prompted.
        Configures the default boot configuration file.
        """
        args = {"config": config_name,
                "reboot_answer": "n",
                "oid_index": "0"}

        return self.execute_keyword(device_name, args, self.cmd_const.SET_SYSTEM_TO_CONFIG, **kwargs)

    def copy_configuration(self, device_name, server, filename, new_filename="", overwrite="N", vr="vr-default",
                           slot=None, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [server] - The IP address of the server where the configuration is located.
        [filename] - The filename, including tftp path, of the file. Root directory is configured as
                     '/ExtremeAutomation/Resources/TestEnvironments'
        [new_filename] - New filename for the copied file on the destination device.
        [overwrite] - Whether or not to overwrite the file if it exists already. Default is no.
        [vr] - The VR which the server IP resides on.
        [slot] - used for EOS only to specify which slot to use for the configuraion

        Downloads a specified config file onto the device(s).
        """
        args = {"server": server,
                "filename": filename,
                "vr": vr,
                "answer": overwrite,
                "new_filename": new_filename,
                "slot": slot}

        return self.execute_keyword(device_name, args, self.cmd_const.COPY_FILE, **kwargs)

    def copy_configuration_all_netelems(self, server, new_filename="", overwrite="N", vr="vr-default",
                                        slot=None, **kwargs):
        """
        Keyword Arguments:
        [server]       - The remote server the file exists on.
        [new_filename] - The filename to save as on the Network Element.
        [overwrite]    - Overwrite flag, if the filename already exists.
        [vr]           - Which VR to use for the copy operation.
        [slot]         - Which slot to copy the file onto.

        Copies the given config file to all Network Elements in the ENV file.
        """
        variables = RobotUtils.get_variables(no_decoration=True)
        netelems = NetworkElementUtils.get_device_names_from_variables(variables, "netelem")

        for netelem in netelems:
            netelem_name = None
            netelem_base_cfg_location = None

            try:
                netelem_name = variables[netelem]["name"]
                netelem_base_cfg_location = variables[netelem]["base_cfg_location"]

            except KeyError:
                if netelem_base_cfg_location is None:
                    self.logger.log_error("${" + netelem + ".base_cfg_location} variable not present in testbed " +
                                          "resource file.")

            if netelem_name is not None:
                self.copy_configuration(netelem_name, server, netelem_base_cfg_location, new_filename, overwrite, vr,
                                        slot, **kwargs)

    def upload_logging_to_server(self, device_name, local_file, remote_file, server_ip, vr="vr-default", **kwargs):
        """
        Keyword Arguments:
        [device_names] - The device(s) the keyword should be run against.
        [local_file] - The name of the local log file that should be uploaded.
        [remote_file] - The name the log file should given when uploaded to the remote server.
        [server_ip] - The IP of the TFTP server the log file should be uploaded to.
        [vr] - Which VR should be used for the upload.

        Uploads a given log file to a remote TFTP server.
        """
        args = {"local_file": local_file,
                "remote_file": remote_file,
                "server_ip": server_ip,
                "vr": vr}

        return self.execute_keyword(device_name, args, self.cmd_const.UPLOAD_FILE, **kwargs)

    def set_primary_config_on_network_element(self, device_name, config_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should run against.
        [config_name] - The name of the boot choice primary configuration that should be used.

        Sets the boot choice primary configuration file on the network element.
        This feature is supported on VOSS only.
        """
        args = {"config": config_name}

        return self.execute_keyword(device_name, args, self.cmd_const.SET_SYSTEM_TO_PRIMARY_CONFIG, **kwargs)

    def set_backup_config_on_network_element(self, device_name, config_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should run against.
        [config_name] - The name of the Backup configuration that should be loaded for backup.

        Sets the boot choice primary backup configuration file on the network element..
        This feature is supported on VOSS only.
        """
        args = {"config": config_name}

        return self.execute_keyword(device_name, args, self.cmd_const.SET_SYSTEM_TO_BACKUP_CONFIG, **kwargs)

    def save_current_config_to_file(self, device_name, config, overwrite_answer="y", standard_answer="y", replace_default_answer="n",
                                    **kwargs):
        """
        Keyword Arguments:
        [device_name] - The name of the device to save the configuration file on.
        [config]      - The name of the file that the saved configuration will be named.

        Saves the current config on the system to a file name of the user's choice.
        """
        args = {"config": config,
                "overwrite_answer": overwrite_answer,
                "replace_default_answer": replace_default_answer,
                "standard_answer": standard_answer,
                "oid_index": "0"}

        return self.execute_keyword(device_name, args, self.cmd_const.SAVE_CONFIG_TO_FILE, **kwargs)

    def verify_default_boot_config_file(self, device_name, config, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device to check for the default boot configuration file.
        [config]      - The name of the configuration file to check.

        Verifies if the default configuration file is correct.
        VOSS only.
        """
        args = {"config": config,
                "oid_index": "0"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_DEFAULT_BOOT_CONFIG_FILE,
                                           self.parse_const.CHECK_DEFAULT_BOOT_CONFIG_FILE, True,
                                           "Default boot config file is {config}.",
                                           "Default boot config file is NOT {config}!",
                                           **kwargs)

    def verify_config_file_exists(self, device_name, config, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device to check for the default boot configuration file.
        [config]      - The name of the configuration file to check.

        Verifies if the griven configuration file is present.
        """
        args = {"config": config,
                "oid_index": "0"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_CONFIG_FILES,
                                           self.parse_const.CHECK_CONFIG_FILE_EXISTS, True,
                                           "Config file {config} is present on {device_name}.",
                                           "Config file {config} IS NOT present on {device_name}!",
                                           **kwargs)

    def verify_config_file_exists_on_slot(self, device_name, config, slot="1", **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device to check for the default boot configuration file.
        [config]      - The name of the configuration file to check.

        Verifies if the griven configuration file is present.
        """
        args = {"config": config,
                "slot": slot,
                "oid_index": "0"}

        if slot == "0":
            return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_CONFIG_FILES,
                                               self.parse_const.CHECK_CONFIG_FILE_EXISTS, True,
                                               "Config file {config} is present on {device_name}.",
                                               "Config file {config} IS NOT present on {device_name}!",
                                               **kwargs)
        else:
            return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_CONFIG_FILES_PER_SLOT,
                                               self.parse_const.CHECK_CONFIG_FILE_EXISTS_PER_SLOT, True,
                                               "Config file {config} is present on {device_name} slot {slot}.",
                                               "Config file {config} IS NOT present on {device_name} slot "
                                               "{slot}!", **kwargs)

    def delete_file_on_slot(self, device_name, config, slot="1", answer="yes", **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device to check for the default boot configuration file.
        [config]      - The name of the configuration file to check.

        Verifies if the griven configuration file is present.
        """
        args = {"file_name": config,
                "slot": slot,
                "oid_index": "0",
                "answer": answer}

        command_api = self.cmd_const.DELETE_FILE if slot == '0' else self.cmd_const.DELETE_FILE_ON_SLOT
        return self.execute_keyword(device_name, args, command_api, **kwargs)

    def copy_file(self, device_name, filename, new_filename, answer="y", slot_a="1", slot_b="1", **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should run against.
        [filename_a] - The name of the file you want to copy.
        [filename_b] - The name of the file you want to copy to.
        [answer] - Used on EXOS to cofirm or deny overwrite based on "y" or "n".
        [slot_a] - Integer used to specify the "from" slot number for EOS.
        [slot_b] - Integer used to specify the "to" slot number for EOS.

        Copys one file to the other
        """
        args = {"filename": filename,
                "new_filename": new_filename,
                "answer": answer,
                "slot_a": slot_a,
                "slot_b": slot_b}

        return self.execute_keyword(device_name, args, self.cmd_const.COPY_FILE, **kwargs)

    def copy_file_from_server(self, device_name, server, filename, new_filename, vr="vr-default", answer="y", **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should run against.
        [server] - IP address of the server to copy the file from.
        [filename_a] - The name of the file you want to copy.
        [filename_b] - The name of the file you want to copy to.
        [vr] - Virtual router used for transfer. Used by EXOS.

        Copys one file to the other
        """
        args = {"server": server,
                "filename": filename,
                "new_filename": new_filename,
                "vr": vr,
                "answer": answer}

        return self.execute_keyword(device_name, args, self.cmd_const.COPY_FILE_FROM_SERVER, **kwargs)

    def verify_primary_config_on_network_element(self, device_name, config, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device to check for the default boot configuration file.
        [config]      - The name of the primary boot configuration file to verify.

        Verifies if the specified configuration file is set as the primary boot configuration file on the device.
        This command applies to VOSS only.
        """
        args = {"config": config}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_DEFAULT_BOOT_CONFIG_FILE,
                                           self.parse_const.CHECK_PRIMARY_BOOT_CONFIG_FILE, True,
                                           "The primary boot config file is correctly set to {config}.",
                                           "The primary boot config file is NOT correctly set to {config}!",
                                           **kwargs)

    def verify_backup_config_on_network_element(self, device_name, config, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device to check for the default boot configuration file.
        [config]      - The name of the primary backup boot configuration file to verify.

        Verifies if the specified configuration file is set as the primary backup boot configuration file on the device.
        This command applies to VOSS only.
        """
        args = {"config": config}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_DEFAULT_BOOT_CONFIG_FILE,
                                           self.parse_const.CHECK_PRIMARY_BACKUP_BOOT_CONFIG_FILE, True,
                                           "The primary backup boot config file is correctly set to {config}.",
                                           "The primary backup boot config file is NOT correctly set to {config}!",
                                           **kwargs)
