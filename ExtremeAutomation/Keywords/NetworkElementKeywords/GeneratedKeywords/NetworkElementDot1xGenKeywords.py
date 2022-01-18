"""
Keyword class for all dot1x cli commands.
"""
from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import NetworkElementKeywordBaseClass
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.Constants.Dot1xConstants import \
    Dot1xConstants as ParseConstants
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.Constants.Dot1xConstants import \
    Dot1xConstants as CommandConstants
# All imports above this line will be removed after generation.
# User imports must be added below.


class NetworkElementDot1xGenKeywords(NetworkElementKeywordBaseClass):
    def __init__(self):
        super(NetworkElementDot1xGenKeywords, self).__init__()
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()
        self.api_const = "dot1x"

    def dot1x_enable_global(self, device_name, **kwargs):
        """
        Description: Globally Enables Dot1x on the device.

        Supported Agents and OS:
            CLI: EXOS, EOS, SLX
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_GLOBAL,
                                    **kwargs)

    def dot1x_disable_global(self, device_name, **kwargs):
        """
        Description: Globally Disables Dot1x on the device.

        Supported Agents and OS:
            CLI: EXOS, EOS, SLX
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_GLOBAL,
                                    **kwargs)

    def dot1x_enable_port(self, device_name, port='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: EXOS, EOS, SLX
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_PORT,
                                    **kwargs)

    def dot1x_disable_port(self, device_name, port='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: EXOS, EOS, SLX
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_PORT,
                                    **kwargs)

    def dot1x_enable_accounting(self, device_name, **kwargs):
        """
        Description: Globally Enables Dot1x Accounting on the device.

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_ACCOUNTING,
                                    **kwargs)

    def dot1x_disable_accounting(self, device_name, **kwargs):
        """
        Description: Globally Disables Dot1x Accounting on the device.

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_ACCOUNTING,
                                    **kwargs)

    def dot1x_enable_port_reauth(self, device_name, port='', **kwargs):
        """
        Description: Enables Dot1x re-auth on the given port(s).

        Supported Agents and OS:
            CLI: EXOS, SLX
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_PORT_REAUTH,
                                    **kwargs)

    def dot1x_disable_port_reauth(self, device_name, port='', **kwargs):
        """
        Description: Disables Dot1x re-auth on a given port.

        Supported Agents and OS:
            CLI: EXOS, SLX
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_PORT_REAUTH,
                                    **kwargs)

    def dot1x_set_global_idle_timeout(self, device_name, idle_timeout='', **kwargs):
        """
        Description: Sets the Dot1x Global idle timeout value in seconds.

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "idle_timeout": idle_timeout
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_GLOBAL_IDLE_TIMEOUT,
                                    **kwargs)

    def dot1x_set_global_session_timeout(self, device_name, session_timeout='', **kwargs):
        """
        Description: Sets the Dot1x Global session-timeout value in seconds.

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "session_timeout": session_timeout
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_GLOBAL_SESSION_TIMEOUT,
                                    **kwargs)

    def dot1x_set_port_quietperiod(self, device_name, quiet_period='', port='', **kwargs):
        """
        Description: Sets the port Dot1x quiet period timer value in seconds.

        Supported Agents and OS:
            CLI: EXOS, EOS, SLX
        """
        args = {
            "port": port,
            "quiet_period": quiet_period
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PORT_QUIETPERIOD,
                                    **kwargs)

    def dot1x_set_port_reauthperiod(self, device_name, reauth_period='', port='', **kwargs):
        """
        Description: Sets the port Dot1x timer for reauth period in seconds.

        Supported Agents and OS:
            CLI: EXOS, EOS, SLX
        """
        args = {
            "port": port,
            "reauth_period": reauth_period
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PORT_REAUTHPERIOD,
                                    **kwargs)

    def dot1x_set_port_servertimeout(self, device_name, server_timeout='', port='', **kwargs):
        """
        Description: Sets the port Dot1x timer for the Server timeout in seconds.

        Supported Agents and OS:
            CLI: EXOS, EOS, SLX
        """
        args = {
            "port": port,
            "server_timeout": server_timeout
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PORT_SERVERTIMEOUT,
                                    **kwargs)

    def dot1x_set_port_supp_resptimeout(self, device_name, supp_resp_timeout='', port='', **kwargs):
        """
        Description: Sets the port Dot1x timer value for supp_resp_timeout in seconds.

        Supported Agents and OS:
            CLI: EXOS, EOS, SLX
        """
        args = {
            "port": port,
            "supp_resp_timeout": supp_resp_timeout
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PORT_SUPP_RESPTIMEOUT,
                                    **kwargs)

    def dot1x_clear_global_idle_timeout(self, device_name, **kwargs):
        """
        Description: Sets the dot1x Idle Timeout value back to the default setting (Zero for EXOS).

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_GLOBAL_IDLE_TIMEOUT,
                                    **kwargs)

    def dot1x_clear_global_session_timeout(self, device_name, **kwargs):
        """
        Description: Sets the dot1x Session Timeout value back to the default setting (Zero for EXOS).

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_GLOBAL_SESSION_TIMEOUT,
                                    **kwargs)

    def dot1x_clear_state_mac(self, device_name, dot1x_mac='', **kwargs):
        """
        Description: Clears and initializes the network login session for a particular mac address.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "dot1x_mac": dot1x_mac
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_STATE_MAC,
                                    **kwargs)

    def dot1x_clear_port_state(self, device_name, port='', **kwargs):
        """
        Description: Clears and initializes the network login sessions on a VLAN port.

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_PORT_STATE,
                                    **kwargs)

    def dot1x_clear_port_state_mac(self, device_name, dot1x_mac='', port='', **kwargs):
        """
        Description: Clears and initializes the dot1x sessions on a VLAN port and mac.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "dot1x_mac": dot1x_mac,
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_PORT_STATE_MAC,
                                    **kwargs)

    def dot1x_clear_port_reauthperiod(self, device_name, port='', **kwargs):
        """
        Description: Clears the configured Dot1x re-auth period on a given port.

        Supported Agents and OS:
            CLI: EXOS, EOS, SLX
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_PORT_REAUTHPERIOD,
                                    **kwargs)

    # ##################################################################################################################
    #   Inspection Keywords   ##########################################################################################
    # ##################################################################################################################

    def dot1x_verify_enabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.

        Verifies that dot1x is enabled on the given device.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_AUTH_CFG,
                                           self.parse_const.VERIFY_DOT1X_STATE, True,
                                           "Dot1x Authentication is enabled on {device_name}.",
                                           "Dot1x Authentication is NOT enabled on {device_name}!",
                                           **kwargs)

    def dot1x_verify_disabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should run against.

        Verifies that Dot1x is disabled on the device.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_AUTH_CFG,
                                           self.parse_const.VERIFY_DOT1X_STATE, False,
                                           "Dot1x Authentication is disabled on {device_name}.",
                                           "Dot1x Authentication is NOT disabled on {device_name}!",
                                           **kwargs)

    def dot1x_verify_port_enabled(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [port]        - The port(s) or interface of the device.

        Verifies that Dot1x is enabled on a given port.
        """
        args = {"port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_AUTH_CFG_PORT,
                                           self.parse_const.VERIFY_DOT1X_IS_ENABLED_ON_PORT, True,
                                           "Dot1x is Enabled on {device_name} port {port}.",
                                           "Dot1x is NOT Enabled on {device_name} port {port}!",
                                           **kwargs)

    def dot1x_verify_port_disabled(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [port]        - The port(s) or interface(s) of the device.

        Verifies that Dot1x is disabled on a given port.
        """
        args = {"port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_AUTH_CFG_PORT,
                                           self.parse_const.VERIFY_DOT1X_IS_ENABLED_ON_PORT, True,
                                           "Dot1x is Disabled on {device_name} port {port}.",
                                           "Dot1x is NOT Disabled on {device_name} port {port}!",
                                           **kwargs)

    def dot1x_verify_accounting_enabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should run against.

        Verifies that Dot1x accounting is enabled on a given device.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_AUTH_CFG,
                                           self.parse_const.VERIFY_DOT1X_ACCOUNTING_STATE, True,
                                           "Dot1x Accounting is enabled on {device_name}.",
                                           "Dot1x Accounting is NOT enabled on {device_name}!",
                                           **kwargs)

    def dot1x_verify_accounting_disabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_names] - The device the keyword should be run against.

        Verifies that Dot1x accounting is disabled on a given device.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_AUTH_CFG,
                                           self.parse_const.VERIFY_DOT1X_ACCOUNTING_STATE, False,
                                           "Dot1x Accounting is disabled on {device_name}.",
                                           "Dot1x Accounting is NOT disabled on {device_name}!",
                                           **kwargs)

    def dot1x_verify_user_authenticated(self, device_name, mac_or_ip_or_user='', **kwargs):
        """
        Keyword Arguments:
        [device_name]       - The device the keyword will be run against.
        [mac_or_ip_or_user] - The user MAC, IP, or username in either of the following forms:
                              08:00:27:ab:16:c3  192.168.1.201  pwapap.

        Verifies that a dot1x user is authenticated.
        """
        args = {"mac_or_ip_or_user": mac_or_ip_or_user}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SESSION,
                                           self.parse_const.CHECK_IF_DOT1X_USER_IS_AUTHENTICATED, True,
                                           "Dot1x User {mac_or_ip_or_user} is authenticated.",
                                           "Dot1x User {mac_or_ip_or_user} is NOT authenticated!",
                                           **kwargs)

    def dot1x_verify_session_timeout(self, device_name, session_timeout='', **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will be run against.
        [session_timeout] - The session timeout value (in seconds).

        Verifies the Session Timeout duration for Dot1x Auth type.
        """
        args = {"session_timeout": session_timeout}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SESSION,
                                           self.parse_const.VERIFY_DOT1X_SESSION_TIMEOUT, True,
                                           "Dot1x Session Timeout is correctly set to {session_timeout}.",
                                           "Dot1x Session Timeout is NOT set to {session_timeout}!",
                                           **kwargs)

    def dot1x_verify_global_session_timeout(self, device_name, seconds='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [seconds]     - The expected session timeout value in seconds.

        Verifies the Global Session Timeout duration for Dot1x Auth type.
        """
        args = {"seconds": seconds}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_GLOBAL_SESSION_TIMEOUT,
                                           self.parse_const.VERIFY_GLOBAL_DOT1X_SESSION_TIMEOUT, True,
                                           "Dot1x Global Session Timeout is correctly set to {seconds}.",
                                           "Dot1x Global Session Timeout is NOT set to {seconds}!",
                                           **kwargs)

    def dot1x_verify_idle_timeout(self, device_name, idle_timeout='', **kwargs):
        """
        Keyword Arguments:
        [device_name]  - The device the keyword will be run against.
        [idle_timeout] - The idle timeout value. (in seconds)

        Verifies the Idle Timeout value for Dot1x Auth type.
        """
        args = {"idle_timeout": idle_timeout}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SESSION,
                                           self.parse_const.VERIFY_DOT1X_IDLE_TIMEOUT, True,
                                           "The Dot1x Idle Timeout is correctly set to {idle_timeout}.",
                                           "The Dot1x Idle Timeout is NOT set to {idle_timeout}!",
                                           **kwargs)

    def dot1x_verify_global_idle_timeout(self, device_name, seconds='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [seconds]     - The expected idle timeout value in seconds.

        Verifies the Global Idle Timeout duration for Dot1x Auth type.
        """
        args = {"idle_timeout": seconds}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SESSION,
                                           self.parse_const.VERIFY_GLOBAL_DOT1X_IDLE_TIMEOUT, True,
                                           "The Dot1x Global Idle Timeout is correctly set to {idle_timeout}.",
                                           "The Dot1x Global Idle Timeout is NOT set to {idle_timeout}!",
                                           **kwargs)

    def dot1x_verify_port_reauth_period(self, device_name, port='', interval='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [port]        - The port or interface of the device.
        [interval]    - The interval that the re-auth period should be set to.

        Verifies that a port's re-auth period is configured with the specified interval.
        """
        args = {"port": port,
                "interval": interval}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_AUTH_CFG_PORT,
                                           self.parse_const.VERIFY_DOT1X_PORT_REAUTH_PERIOD, True,
                                           "Dot1x Authentication reauth-period is {interval} for port {port}.",
                                           "Dot1x Authentication reauth-period is NOT {interval} for port {port}!",
                                           **kwargs)

    def dot1x_verify_port_reauth_enabled(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [port]        - The port or interface on the device.

        Verifies that a port's re-auth state is enabled.
        """
        args = {"port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_AUTH_CFG_PORT,
                                           self.parse_const.VERIFY_DOT1X_PORT_REAUTH_STATE, True,
                                           "Dot1x reauthentication for port {port} is enabled.",
                                           "Dot1x reauthentication for port {port} is DISABLED!",
                                           **kwargs)

    def dot1x_verify_port_reauth_disabled(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [port]        - The port or interface of the device.

        Verifies that a port's re-auth state is disabled.
        """
        args = {"port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_AUTH_CFG_PORT,
                                           self.parse_const.VERIFY_DOT1X_PORT_REAUTH_STATE, False,
                                           "Dot1x reauthentication for port {port} is disabled.",
                                           "Dot1x reauthentication for port {port} is ENABLED!",
                                           **kwargs)
