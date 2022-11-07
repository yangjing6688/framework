from ExtremeAutomation.Library.Utils.Constants.LicenseServerConstants import LicenseServerConstants
from ExtremeAutomation.Library.Device.Common.Agents.RestAgent import RestAgent
from ExtremeAutomation.Library.Device.Common.CommandObjects.CliCommandObject import CliCommandObject
from ExtremeAutomation.Library.Device.Common.CommandObjects.RestCommandObject import RestCommandObject
from ExtremeAutomation.Library.Device.EndsystemElement.EndsystemElement import EndsystemElement
from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import \
    NetworkElementKeywordBaseClass
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.Constants.HostutilsConstants \
    import HostutilsConstants as CommandConstants
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.Constants.HostutilsConstants \
    import HostutilsConstants as ParseConstants


class NetworkElementHostUtilsKeywords(NetworkElementKeywordBaseClass):
    def __init__(self):
        super(NetworkElementHostUtilsKeywords, self).__init__()
        self.api_const = self.constants.API_HOSTUTILS
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()

    # ##################################################################################################################
    #   Inspection Keywords   ##########################################################################################
    # ##################################################################################################################

    def host_address_should_be_reachable(self, device_names, host_address, count="1", timeout="1", **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [host_address] - The host address to be pinged.
        [count] - The number of pings to send.  Setting the default to 1 if not specified.
        [timeout] - The timeout to wait for a ping reply from the host, per ping.

        Pings a host once by default.  The number of pings to be sent can be changed.
        """
        args = {"host_address": host_address,
                "timeout": timeout,
                "count": count}

        self.execute_verify_keyword(device_names, args, self.cmd_const.PING_HOST,
                                    self.parse_const.CHECK_PING_RESULT, True,
                                    "Host address {host_address} is reachable.",
                                    "Host address {host_address} is NOT reachable!",
                                    **kwargs)

    def host_address_should_not_be_reachable(self, device_names, host_address, count="1", timeout="1", **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [host_address] - The host address to be pinged.
        [count] - The number of pings to send.  Setting the default to 1 if not specified.
        [timeout] - The timeout to wait for a ping reply from the host, per ping.

        Pings a host once by default.  The number of pings to be sent can be changed. Negative case.
        """
        args = {"host_address": host_address,
                "timeout": timeout,
                "count": count}

        self.execute_verify_keyword(device_names, args, self.cmd_const.PING_HOST,
                                    self.parse_const.CHECK_PING_RESULT, False,
                                    "Host address {host_address} is not reachable.",
                                    "Host address {host_address} is STILL reachable!",
                                    **kwargs)

    def l2_ping_host_address_should_be_reachable(self, device_names, ip_address, **kwargs):
        """
        Keyword Arguments:
        [device_name]         - The device the keyword will be run against.
        [ip_address]          - The ip address to be pinged.

        Performs an L2 Ping for a specified ip address.
        """
        args = {"ip_address": ip_address}

        self.execute_verify_keyword(device_names, args, self.cmd_const.L2_PING_IPADDR,
                                    self.parse_const.CHECK_L2PING_IPADDR_RESULT, True,
                                    "IP Address {ip_address} is reachable using L2 Ping.",
                                    "IP Address {ip_address} is NOT reachable using L2 Ping!",
                                    **kwargs)

    def l2_ping_host_address_should_not_be_reachable(self, device_names, ip_address, **kwargs):
        """
        Keyword Arguments:
        [device_name]         - The device the keyword will be run against.
        [ip_address]          - The ip address to be pinged.

        Performs an L2 Ping for a specified ip address.
        """
        args = {"ip_address": ip_address}

        self.execute_verify_keyword(device_names, args, self.cmd_const.L2_PING_IPADDR,
                                    self.parse_const.CHECK_L2PING_IPADDR_RESULT, False,
                                    "IP Address {ip_address} is not reachable using L2 Ping.",
                                    "IP Address {ip_address} IS reachable using L2 Ping!",
                                    **kwargs)

    def l2_ping_host_address_vrf_should_be_reachable(self, device_names, ip_address, vrf_name, **kwargs):
        """
        Keyword Arguments:
        [device_name]         - The device the keyword will be run against.
        [ip_address]          - The ip address to be pinged.
        [vrf_name]            - The name of the vrf.

        Performs an L2 Ping for a specified ip address and Vrf.
        """
        args = {"ip_address": ip_address,
                "vrf_name": vrf_name}

        self.execute_verify_keyword(device_names, args, self.cmd_const.L2_PING_IPADDR_VRF,
                                    self.parse_const.CHECK_L2PING_IPADDR_RESULT, True,
                                    "IP Address {ip_address} using Vrf {vrf_name} is reachable.",
                                    "IP Address {ip_address} using Vrf {vrf_name} is NOT reachable!",
                                    **kwargs)

    def l2_ping_host_address_vrf_should_not_be_reachable(self, device_names, ip_address, vrf_name, **kwargs):
        """
        Keyword Arguments:
        [device_name]         - The device the keyword will be run against.
        [ip_address]          - The ip address to be pinged.
        [vrf_name]            - The name of the vrf.

        Performs an L2 Ping for a specified ip address and Vrf.
        """
        args = {"ip_address": ip_address,
                "vrf_name": vrf_name}

        self.execute_verify_keyword(device_names, args, self.cmd_const.L2_PING_IPADDR_VRF,
                                    self.parse_const.CHECK_L2PING_IPADDR_RESULT, False,
                                    "IP Address {ip_address} using Vrf {vrf_name} is not reachable.",
                                    "IP Address {ip_address} using Vrf {vrf_name} IS reachable!",
                                    **kwargs)

    def verify_failed_login_attempts_on_login(self, device_names, ip_address, username, password, login_attempts,
                                              connection_type="telnet", **kwargs):
        """
        Keyword Arguments:
        [device_name]         - The device the keyword will be run against.
        [ip_address]          - The ip address to connect to.
        [username]            - The username to login.
        [password]            - The password to login.
        [login_attempts]      - The number of expected failed login attempts.
        [connection_type]     - Optional arg.  Can be ssh or telnet.

        Connects to the device and verifies the number of failed login attempts since the last successful login.
        """
        args = {"ip_address": ip_address,
                "username": username,
                "password": password,
                "login_attempts": login_attempts}
        if connection_type == "telnet":
            self.execute_verify_keyword(device_names, args, self.cmd_const.TELNET_TO_IP,
                                        self.parse_const.CHECK_FAILED_LOGIN_ATTEMPTS, True,
                                        "The device correctly indicates {login_attempts} failed login attempts.",
                                        "The device DOES NOT indicate {login_attempts} failed login attempts!",
                                        **kwargs)
        else:
            self.execute_verify_keyword(device_names, args, self.cmd_const.SSH_TO_IP,
                                        self.parse_const.CHECK_FAILED_LOGIN_ATTEMPTS, True,
                                        "The device correctly indicates {login_attempts} failed login attempts.",
                                        "The device DOES NOT indicate {login_attempts} failed login attempts!",
                                        **kwargs)

    def verify_last_login_date_exists(self, device_names, ip_address, username, password,
                                      connection_type="telnet", **kwargs):
        """
        Keyword Arguments:
        [device_name]         - The device the keyword will be run against.
        [ip_address]          - The ip address to connect to.
        [username]            - The username to login.
        [password]            - The password to login.
        [connection_type]     - Optional arg.  Can be ssh or telnet.

        Connects to the device and verifies the data of last successful login is displayed.
        """
        args = {"ip_address": ip_address,
                "username": username,
                "password": password}
        if connection_type == "telnet":
            self.execute_verify_keyword(device_names, args, self.cmd_const.TELNET_TO_IP,
                                        self.parse_const.CHECK_LAST_LOGIN_DATE, True,
                                        "The device correctly displays a last login date.",
                                        "The device DOES NOT display a correct last login date!",
                                        **kwargs)
        else:
            self.execute_verify_keyword(device_names, args, self.cmd_const.SSH_TO_IP,
                                        self.parse_const.CHECK_LAST_LOGIN_DATE, True,
                                        "The device correctly displays a last login date.",
                                        "The device DOES NOT display a correct last login date!",
                                        **kwargs)

    def verify_logout_message_exists(self, device_names, ip_address, username, password,
                                     connection_type="telnet", **kwargs):
        """
        Keyword Arguments:
        [device_name]         - The device the keyword will be run against.
        [ip_address]          - The ip address to connect to.
        [username]            - The username to login.
        [password]            - The password to login.
        [connection_type]     - Optional arg.  Can be ssh or telnet.

        Connects to the device, then quits the session and verifies a logout message was displayed.
        """
        args = {"ip_address": ip_address,
                "username": username,
                "password": password}
        if connection_type == "telnet":
            self.execute_verify_keyword(device_names, args, self.cmd_const.TELNET_TO_IP,
                                        self.parse_const.CHECK_LOGOUT_MESSAGE_EXISTS, True,
                                        "The device correctly displays a logout message.",
                                        "The device DOES NOT display a correct logout message!",
                                        **kwargs)
        else:
            self.execute_verify_keyword(device_names, args, self.cmd_const.SSH_TO_IP,
                                        self.parse_const.CHECK_LOGOUT_MESSAGE_EXISTS, True,
                                        "The device correctly displays a logout message.",
                                        "The device DOES NOT display a correct logout message!",
                                        **kwargs)

    def verify_successful_login_attempts_on_login(self, device_names, ip_address, username, password, login_attempts,
                                                  connection_type="telnet", **kwargs):
        """
        Keyword Arguments:
        [device_name]         - The device the keyword will be run against.
        [ip_address]          - The ip address to connect to.
        [username]            - The username to login.
        [password]            - The password to login.
        [login_attempts]      - The number of expected failed login attempts.
        [connection_type]     - Optional arg.  Can be ssh or telnet.

        Connects to the device and verifies the number of successful login attempts since the last successful login.
        The login_attempts provided by the user will need to be 1 more than expected, as the keyword itself logs in to
        the device to verify this value, adding 1 additional successful login.
        """
        args = {"ip_address": ip_address,
                "username": username,
                "password": password,
                "login_attempts": login_attempts}
        if connection_type == "telnet":
            self.execute_verify_keyword(device_names, args, self.cmd_const.TELNET_TO_IP,
                                        self.parse_const.CHECK_SUCCESSFUL_LOGIN_ATTEMPTS, True,
                                        "The device correctly indicates {login_attempts} successful login attempts.",
                                        "The device DOES NOT indicate {login_attempts} successful login attempts!",
                                        **kwargs)
        else:
            self.execute_verify_keyword(device_names, args, self.cmd_const.SSH_TO_IP,
                                        self.parse_const.CHECK_SUCCESSFUL_LOGIN_ATTEMPTS, True,
                                        "The device correctly indicates {login_attempts} successful login attempts.",
                                        "The device DOES NOT indicate {login_attempts} successful login attempts!",
                                        **kwargs)

    # ##################################################################################################################
    #   Debug Keywords   ###############################################################################################
    # ##################################################################################################################
    def enable_debug_mode(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.

        Attempts to enable the debug prompt in the device, auto-filling any password or challenge-response.
        """
        dev, cmd_api, parse_api = self._init_keyword(device_name, self.constants.API_HOSTUTILS,
                                                     self.constants.API_HOSTUTILS, wait_for_prompt=False, **kwargs)

        kw_results = []
        # Get debug login and any password or challenge.
        cmd_obj = dev.send_command_object(cmd_api.enable_debug_mode(None))
        output = cmd_obj.return_text
        parse_result, response = parse_api.check_debug_login(output, None, **kwargs)

        kw_results.append(self._determine_result(dev, cmd_obj, parse_result, True,
                                                 "Debug challenge received, sending response to " + device_name + ".",
                                                 "Debug challenge was not received, aborting!"))
        if not parse_result:
            return self._keyword_cleanup(kw_results)

        # Return the password or challenge response
        args = {"response": response}
        cmd_obj = dev.send_command_object(cmd_api.return_debug_creds(args))
        output = cmd_obj.return_text
        parse_result = parse_api.check_debug_login_enabled(output, args, **kwargs)
        kw_results.append(self._determine_result(dev, cmd_obj, parse_result[0], True,
                                                 "Debug mode has been enabled on " + device_name + ".",
                                                 "Debug mode COULD NOT be enabled on " + device_name + "!"))

        return self._keyword_cleanup(kw_results)

    def enable_feature_license(self, device_name, feature, serial_number, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [feature]     - The feature key to enable.

        Valid features:
        macsec
        mpls
        bgp
        dev
        advancededge_core
        unknown_core
        advancedcore_edge
        advancededge_advancedcore
        core_advancedcore
        edge_advancededge
        edge_core
        highspeed
        nettiming
        trill
        40_100_optics
        avb
        x440quad
        x440dual
        openflow
        ssh
        direct_attach
        flowvsr

        Attempts to retrieve the feature license key from value_storage, or sends a REST request to get all licenses,
        and activate it for the given device.
        Note: Currently only supported on EXOS Network Elements.
        """
        dev, cmd_api, parse_api = self._init_keyword(device_name, self.constants.API_HOSTSERVICES,
                                                     self.constants.API_HOSTSERVICES, **kwargs)

        kw_results = []
        if not self.value_storage.get_value(device_name, "feature_licenses"):
            challenge_dict = {"serial": serial_number,
                              "username": LicenseServerConstants.LICENSE_USERNAME,
                              "password": LicenseServerConstants.LICENSE_PASSWORD}

            rest_server = EndsystemElement(self.constants.OS_LINUX, self.constants.PLATFORM_BASE,
                                           self.constants.UNIT_BASE, self.constants.VERSION_BASE)
            rest_server.hostname = LicenseServerConstants.CHALLENGE_SERVER
            rest_server.port = LicenseServerConstants.CHALLENGE_SERVER_PORT
            rest = RestAgent(rest_server)
            rest_cmd = RestCommandObject()
            rest_cmd.request_type = "post"
            rest_cmd.uri = LicenseServerConstants.LICENSE_URI
            rest_cmd.data = challenge_dict
            rest_response = rest.send_command_object(rest_cmd)

            self.value_storage.add_value(device_name, "feature_licenses", rest_response.return_text)

            kw_results.append(self._determine_result(dev, rest_cmd, True, True, "License was received from server."))
        feature_key = None
        for feature_dict in self.value_storage.get_value(device_name, "feature_licenses"):
            if feature_dict["name"] == feature:
                feature_key = feature_dict["key"]

        if feature_key is not None:
            args = {"key": feature_key}
            cmd_obj = dev.send_command_object(cmd_api.enable_feature_license(args))
            result = True
        else:
            self.logger.log_info("License key for feature " + feature + " could not be found!")
            cmd_obj = CliCommandObject()
            result = False

        kw_results.append(self._determine_result(dev, cmd_obj, result, True,
                                                 "License for " + feature + " has been enabled on " + device_name + ".",
                                                 "License for " + feature + " WAS NOT enabled on " + device_name + "!"))
        return self._keyword_cleanup(kw_results)
