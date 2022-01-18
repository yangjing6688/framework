"""
Keyword class for all macauth cli commands.
"""
from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import NetworkElementKeywordBaseClass
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.Constants.MacauthConstants import \
    MacauthConstants as ParseConstants
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.Constants.MacauthConstants import \
    MacauthConstants as CommandConstants
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils as StringUtils


class NetworkElementMacauthGenKeywords(NetworkElementKeywordBaseClass):
    def __init__(self):
        super(NetworkElementMacauthGenKeywords, self).__init__()
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()
        self.api_const = "macauth"

    def macauth_enable(self, device_name, **kwargs):
        """
        Description: Enables the MAC Authentication feature.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE,
                                    **kwargs)

    def macauth_disable(self, device_name, **kwargs):
        """
        Description: Disables the MAC Authentication feature.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE,
                                    **kwargs)

    def macauth_enable_port_reauthentication(self, device_name, port='', **kwargs):
        """
        Description: Enables MAC Authentication reauthentication on the specified port(s).

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_PORT_REAUTHENTICATION,
                                    **kwargs)

    def macauth_disable_port_reauthentication(self, device_name, port='', **kwargs):
        """
        Description: Disables MAC Authentication reauthentication on the specified port(s).

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_PORT_REAUTHENTICATION,
                                    **kwargs)

    def macauth_set_password(self, device_name, password='', **kwargs):
        """
        Description: Configures the default MAC Authentication password for all MAC users.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "password": password
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PASSWORD,
                                    **kwargs)

    def macauth_set_port_state(self, device_name, port='', state='', **kwargs):
        """
        Description: Configures the MAC Authentication feature on the specified port(s).

        Supported Agents and OS:
            CLI: EOS, EXOS, SLX
        """
        args = {
            "port": port,
            "state": state
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PORT_STATE,
                                    **kwargs)

    def macauth_set_port_reauthperiod(self, device_name, port='', interval='', **kwargs):
        """
        Description: Configures the MAC Authentication re-authentication period on the specified port(s).

        Supported Agents and OS:
            CLI: EOS, EXOS, SLX
        """
        args = {
            "interval": interval,
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PORT_REAUTHPERIOD,
                                    **kwargs)

    def macauth_set_port_quietperiod(self, device_name, port='', sec='', **kwargs):
        """
        Description: Configures the MAC Authentication port-delay on the specified port(s).

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "port": port,
            "sec": sec
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PORT_QUIETPERIOD,
                                    **kwargs)

    def macauth_clear_password(self, device_name, **kwargs):
        """
        Description: Removes the default MAC Authentication password for all MAC users. (On EOS this will revert to
                     thedefault password.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_PASSWORD,
                                    **kwargs)

    def macauth_clear_port_reauthperiod(self, device_name, port='', **kwargs):
        """
        Description: Clears the MAC Authentication re-authentication period to the default value.

        Supported Agents and OS:
            CLI: EOS, EXOS, SLX
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_PORT_REAUTHPERIOD,
                                    **kwargs)

    def macauth_clear_port_quietperiod(self, device_name, port='', **kwargs):
        """
        Description: Removes the MAC Authentication port-delay on the specified port(s).

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_PORT_QUIETPERIOD,
                                    **kwargs)

    def macauth_set_mac_format_type(self, device_name, format_type='', **kwargs):
        """
        Description: Configures the MAC Authentication octet separator for usernames to hyphen.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "format_type": format_type
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_MAC_FORMAT_TYPE,
                                    **kwargs)

    def macauth_set_mac_user(self, device_name, mac_addr='', password='', mask='', **kwargs):
        """
        Description: Adds the MAC address to the MacAuth mac-list.  This is an EXOS-only keyword..

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "mac_addr": mac_addr,
            "mask": mask,
            "password": password
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_MAC_USER,
                                    **kwargs)

    def macauth_set_mac_user_nopass(self, device_name, mac_addr='', mask='', **kwargs):
        """
        Description: Adds the MAC address to the MacAuth mac-list without configuring a password. This is an EXOS-only
                     keyword..

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "mac_addr": mac_addr,
            "mask": mask
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_MAC_USER_NOPASS,
                                    **kwargs)

    def macauth_set_reauthperiod(self, device_name, interval='', **kwargs):
        """
        Description: Configures the MAC Authentication re-authentication period.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "interval": interval
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_REAUTHPERIOD,
                                    **kwargs)

    def macauth_clear_mac_user(self, device_name, mac_addr='', mask='', **kwargs):
        """
        Description: Removes the MAC address from the MacAuth mac-list.  This is an EXOS-only keyword.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "mac_addr": mac_addr,
            "mask": mask
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_MAC_USER,
                                    **kwargs)

    # ##################################################################################################################
    #   Inspection Keywords   ##########################################################################################
    # ##################################################################################################################

    def macauth_verify_enabled(self, device_name, **kwargs):
        """
        Keyword arguments:
        [device_name] - The device the keyword will be run against.

        Verifies that the MAC Authentication feature is enabled.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW,
                                           self.parse_const.VERIFY_MACAUTH_STATE, True,
                                           "MAC Authentication is enabled on {device_name}.",
                                           "MAC Authentication is NOT enabled on {device_name}!",
                                           **kwargs)

    def macauth_verify_disabled(self, device_name, **kwargs):
        """
        Keyword arguments:
        [device_name] - The device the keyword will be run against.

        Verifies that the MAC Authentication feature is disabled.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW,
                                           self.parse_const.VERIFY_MACAUTH_STATE, False,
                                           "MAC Authentication is disabled on {device_name}.",
                                           "MAC Authentication is NOT disabled on {device_name}!",
                                           **kwargs)

    def macauth_verify_enabled_on_port(self, device_name, port='', **kwargs):
        """
        Keyword arguments:
        [device_name] - The device the keyword will be run against.
        [port]        - The port(s) to verify macauth on.

        Verifies that the MAC Authentication feature is enabled on the specified port(s).
        """
        args = {"port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT,
                                           self.parse_const.VERIFY_MACAUTH_PORT_STATE, True,
                                           "MAC Authentication is enabled on {device_name} port {port}.",
                                           "MAC Authentication is NOT enabled on {device_name} port {port}!",
                                           **kwargs)

    def macauth_verify_disabled_on_port(self, device_name, port='', **kwargs):
        """
        Keyword arguments:
        [device_name] - The device the keyword will be run against.
        [port]        - The port(s) to verify macauth on.

        Verifies that the MAC Authentication feature is disabled on the specified port(s).
        """
        args = {"port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT,
                                           self.parse_const.VERIFY_MACAUTH_PORT_STATE, False,
                                           "MAC Authentication is disabled on {device_name} port {port}.",
                                           "MAC Authentication is NOT disabled on {device_name} port {port}!",
                                           **kwargs)

    def macauth_verify_reauth_period(self, device_name, interval='', **kwargs):
        """
        Keyword arguments:
        [device_name] - The device the keyword will be run against.
        [interval]    - The reauth period interval to configure.

        Verifies the MAC Authentication re-authentication period.
        """
        args = {"interval": interval}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW,
                                           self.parse_const.VERIFY_MACAUTH_REAUTH_PERIOD, True,
                                           "MAC Authentication reauth-period is {interval} on {device_name}.",
                                           "MAC Authentication reauth-period is NOT {interval} on {device_name}!",
                                           **kwargs)

    def macauth_verify_port_reauth_period(self, device_name, port='', interval='', **kwargs):
        """
        Keyword arguments:
        [device_name] - The device the keyword will be run against.
        [port]        - The port to be verified for reauth-period.
        [interval]    - The reauth-period interval to verify.

        Verifies the MAC Authentication reauth-period for the specified port(s).
        """
        args = {"interval": interval,
                "port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT,
                                           self.parse_const.VERIFY_MACAUTH_PORT_REAUTH_PERIOD, True,
                                           "MAC Authentication reauth-period is {interval} for port {port}.",
                                           "MAC Authentication reauth-period is NOT {interval} for port {port}!",
                                           **kwargs)

    def macauth_verify_port_reauth_period_default(self, device_name, port='', interval='', **kwargs):
        """
        Keyword arguments:
        [device_name] - The device the keyword will be run against.
        [port]        - The port to be verified for reauth-period.
        [interval]    - The reauth-period interval to verify.

        Verifies the MAC Authentication reauth-period for the specified port(s) is the default value.
        """
        args = {"interval": interval,
                "port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT,
                                           self.parse_const.VERIFY_MACAUTH_PORT_REAUTH_PERIOD, True,
                                           "MAC Authentication reauth-period is the default of {interval} "
                                           "for port {port}.",
                                           "MAC Authentication reauth-period is NOT the default of {interval} "
                                           "for port {port}!",
                                           **kwargs)

    def macauth_verify_reauth_state_enabled(self, device_name, port='', **kwargs):
        """
        Keyword arguments:
        [device_name] - The device the keyword will be run against.
        [port]        - The port(s) to verify reauth on.

        Verifies MAC Authentication reauthentication is enabled on the specified port(s).
        """
        args = {"port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT,
                                           self.parse_const.VERIFY_MACAUTH_PORT_REAUTH_STATE, True,
                                           "MAC Authentication reauthentication for port {port} is on.",
                                           "MAC Authentication reauthentication for port {port} is NOT on!",
                                           **kwargs)

    def macauth_verify_reauth_state_disabled(self, device_name, port='', **kwargs):
        """
        Keyword arguments:
        [device_name] - The device the keyword will be run against.
        [port]        - The port(s) to verify reauth on.

        Verifies MAC Authentication reauthentication is disabled on the specified port(s).
        """
        args = {"port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT,
                                           self.parse_const.VERIFY_MACAUTH_PORT_REAUTH_STATE, False,
                                           "MAC Authentication reauthentication for port {port} is off.",
                                           "MAC Authentication reauthentication for port {port} is NOT off!",
                                           **kwargs)

    def macauth_verify_port_reauth_delay(self, device_name, port='', interval='', **kwargs):
        """
        Keyword arguments:
        [device_name] - The device the keyword will be run against.
        [port]        - The port(s) to verify reauth on.
        [interval]    - The reauth-delay value, in seconds.

        Verifies the MAC Authentication reauth-delay for the specified port(s).
        """
        args = {"port": port,
                "interval": interval}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT,
                                           self.parse_const.VERIFY_MACAUTH_PORT_REAUTH_DELAY, True,
                                           "MAC Authentication reauth delay is {interval} for {port}.",
                                           "MAC Authentication reauth delay is NOT {interval} for {port}!",
                                           **kwargs)

    def macauth_verify_mac_list_exists(self, device_name, mac_addrs='', mask="48", **kwargs):
        """
        Keyword arguments:
        [device_name] - The device the keyword will be run against.
        [mac_addrs]   - The MAC address(es) to check for in the mac-list.
        [mask]        - The mask value for the MAC address.

        Verifies the MAC Authentication reauth-delay for the specified port(s).
        """
        args = {"mac_addr": StringUtils.normalize_mac(mac_addrs),
                "mask": mask}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_MAC_LIST,
                                           self.parse_const.VERIFY_MACAUTH_MAC_LIST_MEMBERS, True,
                                           "MAC Authentication mac-list contains mac user {mac_addr}.",
                                           "MAC Authentication mac-list DOES NOT contain mac user {mac_addr}!",
                                           **kwargs)

    def macauth_verify_mac_list_does_not_exist(self, device_name, mac_addrs='', mask="48", **kwargs):
        """
        Keyword arguments:
        [device_name] - The device the keyword will be run against.
        [mac_addrs]   - The MAC address(es) to check for in the mac-list.
        [mask]        - The mask value for the MAC address.

        Verifies the MAC Authentication reauth-delay for the specified port(s).
        """
        args = {"mac_addr": StringUtils.normalize_mac(mac_addrs),
                "mask": mask}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_MAC_LIST,
                                           self.parse_const.VERIFY_MACAUTH_MAC_LIST_MEMBERS, False,
                                           "MAC Authentication mac-list does not contain mac user {mac_addr}.",
                                           "MAC Authentication mac-list contains mac user {mac_addr}!",
                                           **kwargs)

    def macauth_verify_session_exists_by_port(self, device_name, port='', mac_addr='', vlanid='', mac_type='',
                                              state='', **kwargs):
        """
        Keyword arguments:
        [device_name] - The device the keyword will be run against.
        [port]        - The port on which to verify the macauth session.
        [mac_addr]    - The MAC address to check for in the output.
        [vlanid]      - The vlan id of the macauth session.
        [mac_type]    - The type of macauth session (dynamic or static).
        [state]       - The state of the macauth session.

        Verifies the MAC Authentication session exists on the specified port.
        """
        args = {"port": port,
                "mac_addr": StringUtils.normalize_mac(mac_addr),
                "vlanid": vlanid,
                "mac_type": mac_type,
                "state": state}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_PORT_AUTHENTICATION,
                                           self.parse_const.VERIFY_MACAUTH_PORT_AUTHENTICATION, True,
                                           "MAC authentication session with MAC address {mac_addr}, vlan ID {vlanid}, "
                                           "type {mac_type}, and state {state} exists on port {port}.",
                                           "MAC authentication session with MAC address {mac_addr}, vlan ID {vlanid}, "
                                           "type {mac_type}, and state {state} DOES NOT exist on port {port}!",
                                           **kwargs)

    def macauth_verify_session_does_not_exist_by_port(self, device_name, port='', mac_addr='', vlanid='', mac_type='',
                                                      state='', **kwargs):
        """
        Keyword arguments:
        [device_name] - The device the keyword will be run against.
        [port]        - The port on which to verify the macauth session.
        [mac_addr]    - The MAC address to check for in the output.
        [vlanid]      - The vlan id of the macauth session.
        [mac_type]    - The type of macauth session (dynamic or static).
        [state]       - The state of the macauth session.

        Verifies the MAC Authentication session does not exist on the specified port.
        """
        args = {"port": port,
                "mac_addr": StringUtils.normalize_mac(mac_addr),
                "vlanid": vlanid,
                "mac_type": mac_type,
                "state": state}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_PORT_AUTHENTICATION,
                                           self.parse_const.VERIFY_MACAUTH_PORT_AUTHENTICATION, False,
                                           "MAC authentication session with MAC address {mac_addr}, vlan ID {vlanid}, "
                                           "type {mac_type}, and state {state} does not exist on port {port}.",
                                           "MAC authentication session with MAC address {mac_addr}, vlan ID {vlanid}, "
                                           "type {mac_type}, and state {state} EXISTS on port {port}!", **kwargs)
