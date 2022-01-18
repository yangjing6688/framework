from ExtremeAutomation.Keywords.EndsystemKeywords.CloudConnect.EndsystemCloudConnectConfigKeywords import \
    EndsystemCloudConnectConfigKeywords
from ExtremeAutomation.Keywords.BaseClasses.EndsystemKeywordBaseClass import EndsystemKeywordBaseClass
from ExtremeAutomation.Apis.EndsystemElement.GeneratedApis.ParseApis.Constants.CloudconnectfsmConstants import \
    CloudconnectfsmConstants as ParseConstants
from ExtremeAutomation.Apis.EndsystemElement.GeneratedApis.CommandApis.Constants.CloudconnectfsmConstants import \
    CloudconnectfsmConstants as CommandConstants


class EndsystemCloudConnectFsmKeywords(EndsystemKeywordBaseClass):
    def __init__(self):
        super(EndsystemCloudConnectFsmKeywords, self).__init__()
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()
        self.api_const = "cloudconnectfsm"
        self.ccs_config = EndsystemCloudConnectConfigKeywords()

########################################################################################################################
#   Configuration Keywords   ###########################################################################################
########################################################################################################################
    def add_connect_entry_for_serial(self, server_name, serial, action, standby_timeout, login, password,
                                     redirect_type=None, redirect_uri=None, **kwargs):
        """
        Keyword Arguments:
        server_name     - The name of the Cloud Connect server Endsystem Element.
        serial          - The serial number of the DUT being added.
        action          - The Connect response action.
        standby_timeout - The standby_timeout to return to the DUT.
        login           - The username to return to the DUT.
        password        - The password to return to the DUT.
        redirect_type   - The redirect type, when adding a REDIRECT connect response.
        redirect_uri    - The URL that the DUT will be redirected to, when adding a REDIRECT connect response.
        """
        arg_dict = {"serial": serial,
                    "action": action,
                    "standby_timeout": standby_timeout,
                    "login": login,
                    "password": password,
                    "redirect_type": redirect_type,
                    "redirect_uri": redirect_uri}

        return self.execute_keyword(server_name, arg_dict, self.cmd_const.ADD_CONNECT_ENTRY_FOR_SERIAL, **kwargs)

    def remove_connect_entry_for_serial(self, server_name, serial, **kwargs):
        """
        Keyword Arguments:
        server_name     - The name of the Cloud Connect server Endsystem Element.
        serial          - The serial number of the DUT being removed.
        """
        arg_dict = {"remove": serial}

        return self.execute_keyword(server_name, arg_dict, self.cmd_const.REMOVE_CONNECT_ENTRY_FOR_SERIAL,
                                    **kwargs)

    def add_upgrade_entry_for_serial(self, server_name, serial, upgrade=False, uri=None, timeout=10,
                                     asset_name=None, asset_version=None, asset_type="other", asset_size=0, **kwargs):
        """
        Keyword Arguments:
        server_name     - The name of the Cloud Connect server Endsystem Element.
        serial          - The serial number of the DUT being added.
        upgrade         - A boolean, denoting whether the DUT should attempt an upgrade.
        image_uri       - The path to the image file.
        timeout         - The timeout to use when attempting the image upgrade.
        image_name      - The filename of the image.
        image_version   - The image version being upgraded to.
        image_type      - The type of image file being downloaded.
        image_size      - The size of the new image file.
        """
        arg_dict = {"serial": serial,
                    "upgrade": upgrade,
                    "uri": uri,
                    "timeout": timeout,
                    "asset_name": asset_name,
                    "asset_version": asset_version,
                    "asset_type": asset_type,
                    "asset_size": asset_size if isinstance(asset_size, int) else int(asset_size)}

        return self.execute_keyword(server_name, arg_dict, self.cmd_const.ADD_UPGRADE_ENTRY_FOR_SERIAL, **kwargs)

    def remove_upgrade_entry_for_serial(self, server_name, serial, **kwargs):
        """
        Keyword Arguments:
        server_name     - The name of the Cloud Connect server Endsystem Element.
        serial          - The serial number of the DUT being removed.
        """
        arg_dict = {"remove": serial}

        return self.execute_keyword(server_name, arg_dict, self.cmd_const.REMOVE_UPGRADE_ENTRY_FOR_SERIAL,
                                    **kwargs)

    def add_config_entry_for_serial(self, server_name, serial, merge=True, **kwargs):
        """
        Keyword Arguments:
        server_name     - The name of the Cloud Connect server Endsystem Element.
        serial          - The serial number of the DUT being added.
        merge           - Whether or not to merge the supplied config with the current Device config.
        """
        arg_dict = {"serial": serial,
                    "merge": False if not merge else True,
                    serial: self.ccs_config.build_config_response(serial)}

        return self.execute_keyword(server_name, arg_dict, self.cmd_const.ADD_CONFIG_ENTRY_FOR_SERIAL, **kwargs)

    def add_full_config_entry_for_serial(self, server_name, serial, config_block, merge=True, **kwargs):
        """
        Keyword Arguments:
        server_name     - The name of the Cloud Connect server Endsystem Element.
        serial          - The serial number of the DUT being added.
        config_block    - The full {configBlock: dictionary} config for the DUT.
        merge           - Whether or not to merge the supplied config with the current Device config.
        """
        arg_dict = {"serial": serial,
                    "merge": False if not merge else True,
                    serial: config_block}

        return self.execute_keyword(server_name, arg_dict, self.cmd_const.ADD_CONFIG_ENTRY_FOR_SERIAL, **kwargs)

    def add_manual_config_entry_for_serial(self, server_name, serial, config_dict, merge=True, **kwargs):
        """
        Keyword Arguments:
        server_name     - The name of the Cloud Connect server Endsystem Element.
        serial          - The serial number of the DUT being added.
        """
        arg_dict = {"serial": serial,
                    "merge": False if not merge else True,
                    serial: config_dict}

        return self.execute_keyword(server_name, arg_dict, self.cmd_const.ADD_CONFIG_ENTRY_FOR_SERIAL, **kwargs)

    def remove_config_entry_for_serial(self, server_name, serial, **kwargs):
        """
        Keyword Arguments:
        server_name     - The name of the Cloud Connect server Endsystem Element.
        serial          - The serial number of the DUT being removed.
        """
        arg_dict = {"remove": serial}

        return self.execute_keyword(server_name, arg_dict, self.cmd_const.REMOVE_CONFIG_ENTRY_FOR_SERIAL,
                                    **kwargs)

    def add_stats_reply_for_serial(self, server_name, serial, action="NONE", checkin_timer=None, stats_interval=None,
                                   trace_uri=None, trace_del=False, stat_type=None, **kwargs):
        """
        Keyword Arguments:
        server_name     - The name of the Cloud Connect server Endsystem Element.
        serial          - The serial number(s) of the DUT being added.
        action          - The Stats response action. Valid actions are:
                          ["REBOOT", "RESET", "IMAGE_UPGRADE", "CONFIGURATION", "TRACES", "STATS", "NONE"]
        """
        allowed_actions = ["REBOOT", "RESET", "IMAGE_UPGRADE", "CONFIGURATION", "TRACES", "STATS", "NONE"]
        arg_dict = {"serials": serial}

        if action.upper() in allowed_actions:
            arg_dict["action"] = action.upper()
            if action.upper() == "TRACES":
                arg_dict["uri"] = trace_uri
                arg_dict["delete"] = trace_del if trace_del else False
            if action.upper() == "STATS":
                arg_dict["type"] = stat_type if isinstance(stat_type, list) else [stat_type]
        else:
            self.logger.log_error("Received invalid action: " + action + ". Must be one of the following:\n" +
                                  str(allowed_actions))

        if checkin_timer is not None:
            arg_dict["checkin_timer"] = checkin_timer

        if stats_interval is not None:
            arg_dict["stats_interval"] = stats_interval

        return self.execute_keyword(server_name, arg_dict, self.cmd_const.ADD_STATS_REPLY_FOR_SERIAL, **kwargs)

    def remove_stats_reply_for_serial(self, server_name, serial, **kwargs):
        """
        Keyword Arguments:
        server_name     - The name of the Cloud Connect server Endsystem Element.
        serial          - The serial number(s) of the DUT being added.
        """
        arg_dict = {"serials": serial,
                    "remove": True}

        return self.execute_keyword(server_name, arg_dict, self.cmd_const.ADD_STATS_REPLY_FOR_SERIAL, **kwargs)

    def allow_connect_state_timeout(self, server_name, serial, **kwargs):
        """
        Keyword Arguments:
        server_name     - The name of the Cloud Connect server Endsystem Element.
        serial          - The serial number of the DUT being added to allow_timeout.
        """
        arg_dict = {"allow_timeout": {serial: ["connect_timeout"]}}

        return self.execute_keyword(server_name, arg_dict, self.cmd_const.ALLOW_CONNECT_STATE_TIMEOUT, **kwargs)

    def allow_upgrade_state_timeout(self, server_name, serial, **kwargs):
        """
        Keyword Arguments:
        server_name     - The name of the Cloud Connect server Endsystem Element.
        serial          - The serial number of the DUT being added to allow_timeout.
        """
        arg_dict = {"allow_timeout": {serial: ["upgrade_timeout"]}}

        return self.execute_keyword(server_name, arg_dict, self.cmd_const.ALLOW_CONNECT_STATE_TIMEOUT, **kwargs)

    def allow_config_state_timeout(self, server_name, serial, **kwargs):
        """
        Keyword Arguments:
        server_name     - The name of the Cloud Connect server Endsystem Element.
        serial          - The serial number of the DUT being added to allow_timeout.
        """
        arg_dict = {"allow_timeout": {serial: ["config_timeout"]}}

        return self.execute_keyword(server_name, arg_dict, self.cmd_const.ALLOW_CONNECT_STATE_TIMEOUT, **kwargs)

    def clear_fsm_state_list(self, server_name, serial, **kwargs):
        """
        Keyword Arguments:
        server_name     - The name of the Cloud Connect server Endsystem Element.
        serial          - The serial number of the device state list being cleared.
        """
        arg_dict = {"serial": serial}

        return self.execute_keyword(server_name, arg_dict, self.cmd_const.CLEAR_FSM_STATES_BY_SERIAL, **kwargs)

########################################################################################################################
#   Verification Keywords   ############################################################################################
########################################################################################################################
    def verify_device_states(self, server_name, serial, state_list, **kwargs):
        """
        Keyword Arguments:
        server_name     - The name of the Cloud Connect server Endsystem Element.
        serial          - The serial number of the DUT being added.
        state_list      - A comma separated list, as a string, of the expected states the device has gone through.
        """
        # Convert state_list to a string, for execute_verification_keyword looping.
        if isinstance(state_list, list):
            arg_dict = {"serial": serial,
                        "states": ",".join(state_list)}
        else:
            arg_dict = {"serial": serial,
                        "states": state_list}

        return self.execute_verify_keyword(server_name, arg_dict, self.cmd_const.CHECK_DEVICE_STATES,
                                           self.parse_const.CHECK_DEVICE_STATES, True,
                                           "The device progressed through the expected state list.",
                                           "The device DID NOT progress through the expected state list!",
                                           **kwargs)

    def verify_device_asset_version(self, server_name, serial, asset_name, asset_version, **kwargs):
        """
        Keyword Arguments:
        server_name     - The name of the Cloud Connect server Endsystem Element.
        serial          - The serial number of the DUT being added.
        asset_name      - The assetName field to search on, in the assets dictionary.
        asset_version   - The expected version of the specified asset.
        """
        arg_dict = {"serial": serial,
                    "asset_name": asset_name,
                    "asset_version": asset_version}

        return self.execute_verify_keyword(server_name, arg_dict, self.cmd_const.SHOW_DEVICE_VERSION,
                                           self.parse_const.CHECK_DEVICE_VERSION, True,
                                           "The device had the correct {asset_name} version of {asset_version}.",
                                           "The device DID NOT have the correct {asset_name} version of "
                                           "{asset_version}!",
                                           **kwargs)

    def store_mgmt_ip_for_serial(self, server_name, serial, var_name="dut_mgmt_ip", **kwargs):
        """
        Keyword Arguments:
        server_name     - The name of the Cloud Connect server Endsystem Element.
        serial          - The serial number of the DUT.
        device_name     - The name to store the 'mgmt_ip' variable under.

        Resulting variable in Robot:
        ${<yaml_server_index>.value_storage.<device_name>.<var_name>}
        Ex:
        ${endsys1.value_storage.dut1_mgmt_ip}
        """
        arg_dict = {"serial": serial,
                    "var_name": var_name}

        return self.execute_verify_keyword(server_name, arg_dict, self.cmd_const.SHOW_MGMT_IP,
                                           self.parse_const.STORE_MGMT_IP, True,
                                           "The device's Mgmt IP has been stored as ${<yaml_index>.value_storage." +
                                           var_name + "}.",
                                           "The device's Mgmt IP was not found!",
                                           **kwargs)
