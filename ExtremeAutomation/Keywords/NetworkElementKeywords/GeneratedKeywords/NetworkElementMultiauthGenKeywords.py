"""
Keyword class for all multiauth cli commands.
"""
from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import NetworkElementKeywordBaseClass
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.Constants.MultiauthConstants import \
    MultiauthConstants as ParseConstants
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.Constants.MultiauthConstants import \
    MultiauthConstants as CommandConstants
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Keywords.NetworkElementKeywords.Utils.NetworkElementMultiauthSession \
    import NetworkElementMultiauthSession as MultiauthSession


class NetworkElementMultiauthGenKeywords(NetworkElementKeywordBaseClass):
    def __init__(self):
        super(NetworkElementMultiauthGenKeywords, self).__init__()
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()
        self.api_const = "multiauth"

    def multiauth_enable_session_refresh(self, device_name, **kwargs):
        """
        Description: Enables MultiAuth session refresh.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_SESSION_REFRESH,
                                    **kwargs)

    def multiauth_disable_session_refresh(self, device_name, **kwargs):
        """
        Description: Disables MultiAuth session refresh.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_SESSION_REFRESH,
                                    **kwargs)

    def multiauth_set_session_timeout(self, device_name, timeout='', **kwargs):
        """
        Description: Configures the session timeout duration for all auth types.

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "timeout": timeout
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_SESSION_TIMEOUT,
                                    **kwargs)

    def multiauth_set_session_type_timeout(self, device_name, mode='', timeout='', **kwargs):
        """
        Description: Configures the session timeout duration for auth sessions of the given type.

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "mode": mode,
            "timeout": timeout
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_SESSION_TYPE_TIMEOUT,
                                    **kwargs)

    def multiauth_clear_session_type_timeout(self, device_name, mode='', **kwargs):
        """
        Description: Clears the session timeout duration for auth sessions of the given type to default.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "mode": mode
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_SESSION_TYPE_TIMEOUT,
                                    **kwargs)

    def multiauth_set_session_refresh(self, device_name, seconds='', **kwargs):
        """
        Description: Configures the MultiAuth session refresh interval.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "seconds": seconds
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_SESSION_REFRESH,
                                    **kwargs)

    def multiauth_clear_session_refresh(self, device_name, **kwargs):
        """
        Description: Clears the MultiAuth session reauth interval to default.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_SESSION_REFRESH,
                                    **kwargs)

    def multiauth_set_vlan(self, device_name, multiauth_vlan_name='', **kwargs):
        """
        Description: Enables the MultiAuth/Netlogin VLAN on the given device.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "multiauth_vlan_name": multiauth_vlan_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_VLAN,
                                    **kwargs)

    def multiauth_clear_vlan(self, device_name, **kwargs):
        """
        Description: Disables the MultiAuth/Netlogin VLAN on the given device.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_VLAN,
                                    **kwargs)

    def multiauth_set_idle_timeout(self, device_name, timeout='', **kwargs):
        """
        Description: Configures the idle timeout duration for all auth types.

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "timeout": timeout
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_IDLE_TIMEOUT,
                                    **kwargs)

    def multiauth_set_idle_type_timeout(self, device_name, mode='', timeout='', **kwargs):
        """
        Description: Configures the idle timeout duration for the given type.

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "mode": mode,
            "timeout": timeout
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_IDLE_TYPE_TIMEOUT,
                                    **kwargs)

    def multiauth_clear_idle_type_timeout(self, device_name, mode='', **kwargs):
        """
        Description: Clears the idle timeout for the given type to default.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "mode": mode
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_IDLE_TYPE_TIMEOUT,
                                    **kwargs)

    def multiauth_set_port_mode(self, device_name, mode='', port='', **kwargs):
        """
        Description: This Method will set MultiAuth port mode.

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "mode": mode,
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PORT_MODE,
                                    **kwargs)

    def multiauth_set_port_numusers(self, device_name, port='', num_users='', **kwargs):
        """
        Description: This method will set the max number of allowed users.

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "num_users": num_users,
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PORT_NUMUSERS,
                                    **kwargs)

    def multiauth_clear_station_mac_port(self, device_name, mac='', port='', **kwargs):
        """
        Description: Clears and initializes the network login sessions on a VLAN port and mac.

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "mac": mac,
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_STATION_MAC_PORT,
                                    **kwargs)

    def multiauth_clear_station_port(self, device_name, port='', **kwargs):
        """
        Description: Clears and initializes the network login sessions on a VLAN port.

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_STATION_PORT,
                                    **kwargs)

    def multiauth_clear_station_mac(self, device_name, mac='', **kwargs):
        """
        Description: Clears and initializes the network login session for a particular mac address.

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "mac": mac
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_STATION_MAC,
                                    **kwargs)

    def multiauth_clear_station_agent(self, device_name, agent='', mac='', **kwargs):
        """
        Description: Clears and initializes the network login session for a particular mac address.

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "agent": agent,
            "mac": mac
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_STATION_AGENT,
                                    **kwargs)

    def multiauth_set_mode(self, device_name, mode='', **kwargs):
        """
        Description: This Method will set MultiAuth mode.

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "mode": mode
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_MODE,
                                    **kwargs)

    def multiauth_set_port_force_auth(self, device_name, port='', **kwargs):
        """
        Description: This Method will set MultiAuth port mode to forced auth.

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PORT_FORCE_AUTH,
                                    **kwargs)

    # ##################################################################################################################
    #   Inspection Keywords   ##########################################################################################
    # ##################################################################################################################

    def multiauth_verify_enabled(self, device_name, **kwargs):
        """
        [device_name] - The device the keyword will be run against.

        This Method will set MultiAuth mode to multi.
        """
        args = {"type": "multi"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO,
                                           self.parse_const.CHECK_MULTIAUTH_STATE, True,
                                           "MultiAuth is enabled.",
                                           "MultiAuth is NOT enabled!",
                                           **kwargs)

    def multiauth_verify_session_exists(self, device_name, station_address='', port='', auth_status='',
                                        last_attempt='', agent_type='',
                                        session_applied='', server_type='',
                                        vlan_tun_attr='', policy_index='', policy_name='',
                                        session_timeout='', session_duration='',
                                        idle_timeout='', idle_time='',
                                        termination_time='', auth_server_ip='', session_duration_operator='',
                                        idle_time_operator='', **kwargs):
        """
        Keyword Arguments:
        [device_name]               - The Network Element to run the keyword against.
        [station_address]           - The station address of the multiauth session.
        [port]                      - The authentication port of the session.
        [auth_status]               - The session's authentication status.
        [last_attempt]              - The status of the previous authentication attempt.
        [agent_type]                - The session's authentication agent.
        [session_applied]           - Whether the session is applied or not.
        [server_type]               - The authentication server type.
        [vlan_tun_attr]             - The VLAN ID associated with the auth session.
        [policy_index]              - The applied policy's index.
        [policy_name]               - The applied policy's name.
        [session_timeout]           - The timeout value for the session duration.
        [session_duration]          - The current session duration.
        [idle_timeout]              - The maximum idle time before terminating the session.
        [idle_time]                 - The current session idle time.
        [termination_time]          - The time at which the session was terminated.
        [auth_server_ip]            - The IP Address of the authentication server.
        [session_duration_operator] - Defines the comparison type for the session duration.
        [idle_time_operator]        - Defines the comparison type for the idle time.

        This method will check to see if a session exist on the given device. When searching for a specific session
        you will need to give this command the fields of the session you want as variable. If no variable is set then
        that session field will not be checked.

        When checking session duration, Idle time, and last attempt you can set the comparison operator for that
        variable to >,<, or =. eg. If you set session_duration=0 and the session_duration_operator=> then it will
        check to see if there is a session that has a session duration > 0
        """
        checksession = MultiauthSession().create_session_object(port, station_address, auth_status, last_attempt,
                                                                agent_type, session_applied, server_type, vlan_tun_attr,
                                                                policy_index, policy_name, session_timeout,
                                                                session_duration, idle_timeout, idle_time,
                                                                termination_time, auth_server_ip)

        args = {"checksession": checksession,
                "session_duration_operator": session_duration_operator,
                "idle_time_operator": idle_time_operator,
                "type": "not defined"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SESSION_ALL,
                                           self.parse_const.CHECK_MULTIAUTH_SESSION_EXISTS, True,
                                           "MultiAuth session exists.",
                                           "MultiAuth session DOES NOT exist!",
                                           **kwargs)

    def multiauth_verify_session_exists_by_port(self, device_name, station_address='', port='', auth_status='',
                                                last_attempt='', agent_type='',
                                                session_applied='', server_type='',
                                                vlan_tun_attr='', policy_index='', policy_name='',
                                                session_timeout='', session_duration='',
                                                idle_timeout='', idle_time='',
                                                termination_time='', auth_server_ip='',
                                                session_duration_operator='', idle_time_operator='', **kwargs):
        """
        Keyword Arguments:
        [device_name]               - The Network Element to run the keyword against.
        [station_address]           - The station address of the multiauth session.
        [port]                      - The authentication port of the session.
        [auth_status]               - The session's authentication status.
        [last_attempt]              - The status of the previous authentication attempt.
        [agent_type]                - The session's authentication agent.
        [session_applied]           - Whether the session is applied or not.
        [server_type]               - The authentication server type.
        [vlan_tun_attr]             - The VLAN ID associated with the auth session.
        [policy_index]              - The applied policy's index.
        [policy_name]               - The applied policy's name.
        [session_timeout]           - The timeout value for the session duration.
        [session_duration]          - The current session duration.
        [idle_timeout]              - The maximum idle time before terminating the session.
        [idle_time]                 - The current session idle time.
        [termination_time]          - The time at which the session was terminated.
        [auth_server_ip]            - The IP Address of the authentication server.
        [session_duration_operator] - Defines the comparison type for the session duration.
        [idle_time_operator]        - Defines the comparison type for the idle time.

        This method will check to see if a session exist on the given device. When searching for a specific session
        you will need to give this command the fields of the session you want as variable. If no variable is set then
        that session field will not be checked.

        When checking session duration, Idle time, and last attempt you can set the comparison operator for that
        variable to >,<, or =. eg. If you set session_duration=0 and the session_duration_operator=> then it will
        check to see if there is a session that has a session duration > 0
        """
        checksession = MultiauthSession().create_session_object(port, station_address, auth_status, last_attempt,
                                                                agent_type, session_applied, server_type, vlan_tun_attr,
                                                                policy_index, policy_name, session_timeout,
                                                                session_duration, idle_timeout, idle_time,
                                                                termination_time, auth_server_ip)

        args = {"checksession": checksession,
                "session_duration_operator": session_duration_operator,
                "idle_time_operator": idle_time_operator,
                "type": "not defined",
                "port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SESSION_PORT,
                                           self.parse_const.CHECK_MULTIAUTH_SESSION_EXISTS, True,
                                           "MultiAuth session exists.",
                                           "MultiAuth session DOES NOT exist!",
                                           **kwargs)

    def multiauth_verify_session_exists_by_mac(self, device_name, station_address='', port='', auth_status='',
                                               last_attempt='', agent_type='',
                                               session_applied='', server_type='',
                                               vlan_tun_attr='', policy_index='', policy_name='',
                                               session_timeout='', session_duration='',
                                               idle_timeout='', idle_time='',
                                               termination_time='', auth_server_ip='',
                                               session_duration_operator='', idle_time_operator='', **kwargs):
        """
        Keyword Arguments:
        [device_name]               - The Network Element to run the keyword against.
        [station_address]           - The station address of the multiauth session.
        [port]                      - The authentication port of the session.
        [auth_status]               - The session's authentication status.
        [last_attempt]              - The status of the previous authentication attempt.
        [agent_type]                - The session's authentication agent.
        [session_applied]           - Whether the session is applied or not.
        [server_type]               - The authentication server type.
        [vlan_tun_attr]             - The VLAN ID associated with the auth session.
        [policy_index]              - The applied policy's index.
        [policy_name]               - The applied policy's name.
        [session_timeout]           - The timeout value for the session duration.
        [session_duration]          - The current session duration.
        [idle_timeout]              - The maximum idle time before terminating the session.
        [idle_time]                 - The current session idle time.
        [termination_time]          - The time at which the session was terminated.
        [auth_server_ip]            - The IP Address of the authentication server.
        [session_duration_operator] - Defines the comparison type for the session duration.
        [idle_time_operator]        - Defines the comparison type for the idle time.
        [last_attempt_operator]     - Defines the comparison type for the last attempt.

        This method will check to see if a session exist on the given device. When searching for a specific session
        you will need to give this command the fields of the session you want as variable. If no variable is set then
        that session field will not be checked.

        When checking session duration, Idle time, and last attempt you can set the comparison operator for that
        variable to >,<, or =. eg. If you set session_duration=0 and the session_duration_operator=> then it will
        check to see if there is a session that has a session duration > 0
        """
        checksession = MultiauthSession().create_session_object(port, station_address, auth_status, last_attempt,
                                                                agent_type, session_applied, server_type, vlan_tun_attr,
                                                                policy_index, policy_name, session_timeout,
                                                                session_duration, idle_timeout, idle_time,
                                                                termination_time, auth_server_ip)

        args = {"checksession": checksession,
                "session_duration_operator": session_duration_operator,
                "idle_time_operator": idle_time_operator,
                "station_address": station_address}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SESSION_MAC,
                                           self.parse_const.CHECK_MULTIAUTH_SESSION_EXISTS, True,
                                           "MultiAuth session exists.",
                                           "MultiAuth session DOES NOT exist!",
                                           **kwargs)

    def multiauth_verify_session_does_not_exist(self, device_name, station_address='', port='', auth_status='',
                                                last_attempt='', agent_type='',
                                                session_applied='', server_type='',
                                                vlan_tun_attr='', policy_index='', policy_name='',
                                                session_timeout='', session_duration='',
                                                idle_timeout='', idle_time='',
                                                termination_time='', auth_server_ip='',
                                                session_duration_operator='', idle_time_operator='', **kwargs):
        """
        Keyword Arguments:
        [device_name]               - The Network Element to run the keyword against.
        [station_address]           - The station address of the multiauth session.
        [port]                      - The authentication port of the session.
        [auth_status]               - The session's authentication status.
        [last_attempt]              - The status of the previous authentication attempt.
        [agent_type]                - The session's authentication agent.
        [session_applied]           - Whether the session is applied or not.
        [server_type]               - The authentication server type.
        [vlan_tun_attr]             - The VLAN ID associated with the auth session.
        [policy_index]              - The applied policy's index.
        [policy_name]               - The applied policy's name.
        [session_timeout]           - The timeout value for the session duration.
        [session_duration]          - The current session duration.
        [idle_timeout]              - The maximum idle time before terminating the session.
        [idle_time]                 - The current session idle time.
        [termination_time]          - The time at which the session was terminated.
        [auth_server_ip]            - The IP Address of the authentication server.
        [session_duration_operator] - Defines the comparison type for the session duration.
        [idle_time_operator]        - Defines the comparison type for the idle time.
        [last_attempt_operator]     - Defines the comparison type for the last attempt.

        This method will check to see if a session exist on the given device. When searching for a specific session
        you will need to give this command the fields of the session you want as variable. If no variable is set then
        that session field will not be checked.

        When checking session duration, Idle time, and last attempt you can set the comparison operator for that
        variable to >,<, or =. eg. If you set session_duration=0 and the session_duration_operator=> then it will
        check to see if there is a session that has a session duration > 0
        """
        checksession = MultiauthSession().create_session_object(port, station_address, auth_status, last_attempt,
                                                                agent_type, session_applied, server_type, vlan_tun_attr,
                                                                policy_index, policy_name, session_timeout,
                                                                session_duration, idle_timeout, idle_time,
                                                                termination_time, auth_server_ip)

        args = {"checksession": checksession,
                "session_duration_operator": session_duration_operator,
                "idle_time_operator": idle_time_operator,
                "type": "not defined"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SESSION_ALL,
                                           self.parse_const.CHECK_MULTIAUTH_SESSION_EXISTS, False,
                                           "MultiAuth session does not exist.",
                                           "MultiAuth session DOES exist!",
                                           **kwargs)

    def multiauth_verify_session_expired(self, device_name, station_address='', port='', auth_status='',
                                         last_attempt='', agent_type='',
                                         session_applied='', server_type='',
                                         vlan_tun_attr='', policy_index='', policy_name='',
                                         session_timeout='', session_duration='',
                                         idle_timeout='', idle_time='',
                                         termination_time='', auth_server_ip='', session_duration_operator='',
                                         idle_time_operator='', **kwargs):
        """
        Keyword Arguments:
        [device_name]               - The Network Element to run the keyword against.
        [station_address]           - The station address of the multiauth session.
        [port]                      - The authentication port of the session.
        [auth_status]               - The session's authentication status.
        [last_attempt]              - The status of the previous authentication attempt.
        [agent_type]                - The session's authentication agent.
        [session_applied]           - Whether the session is applied or not.
        [server_type]               - The authentication server type.
        [vlan_tun_attr]             - The VLAN ID associated with the auth session.
        [policy_index]              - The applied policy's index.
        [policy_name]               - The applied policy's name.
        [session_timeout]           - The timeout value for the session duration.
        [session_duration]          - The current session duration.
        [idle_timeout]              - The maximum idle time before terminating the session.
        [idle_time]                 - The current session idle time.
        [termination_time]          - The time at which the session was terminated.
        [auth_server_ip]            - The IP Address of the authentication server.
        [session_duration_operator] - Defines the comparison type for the session duration.
        [idle_time_operator]        - Defines the comparison type for the idle time.
        [last_attempt_operator]     - Defines the comparison type for the last attempt.

        This method will check to see if a session exist on the given device. When searching for a specific session
        you will need to give this command the fields of the session you want as variable. If no variable is set then
        that session field will not be checked.

        When checking session duration, Idle time, and last attempt you can set the comparison operator for that
        variable to >,<, or =. eg. If you set session_duration=0 and the session_duration_operator=> then it will
        check to see if there is a session that has a session duration > 0

        """
        if auth_status is not None or auth_status.lower() != "terminated":
            self.logger.log_info("Auth_Status will be set to \'terminated\' for verifying an expired session.")

        checksession = MultiauthSession().create_session_object(port, station_address, "terminated", last_attempt,
                                                                agent_type, session_applied, server_type, vlan_tun_attr,
                                                                policy_index, policy_name, session_timeout,
                                                                session_duration, idle_timeout, idle_time,
                                                                termination_time, auth_server_ip)

        args = {"checksession": checksession,
                "session_duration_operator": session_duration_operator,
                "idle_time_operator": idle_time_operator,
                "type": "not defined"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SESSION_ALL,
                                           self.parse_const.CHECK_MULTIAUTH_SESSION_EXPIRED, True,
                                           "MultiAuth session is expired.",
                                           "MultiAuth session is NOT expired!",
                                           **kwargs)

    def multiauth_verify_vlan_exist(self, device_name, multiauth_vlan_name='', **kwargs):
        """
        Keyword Arguments:
        [device_names] - The device the keyword will run against.
        [vlan]         - The VLAN name.

        Verifies that the MultiAuth/netlogin vlan exists.
        """
        args = {"multiauth_vlan_name": multiauth_vlan_name}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO,
                                           self.parse_const.CHECK_MULTIAUTH_VLAN_EXISTS, True,
                                           "FOUND MultiAuth VLAN {multiauth_vlan_name}.",
                                           "WARNING: DID NOT FIND MultiAuth VLAN {multiauth_vlan_name}!",
                                           **kwargs)

    def multiauth_verify_vlan_does_not_exist(self, device_name, multiauth_vlan_name='', **kwargs):
        """
        Keyword Arguments:
        [device_names] - The device the keyword will run against.
        [vlan]         - The VLAN name.

        Verifies that the MultiAuth/netlogin vlan does not exist
        """
        args = {"multiauth_vlan_name": multiauth_vlan_name}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO,
                                           self.parse_const.CHECK_MULTIAUTH_VLAN_EXISTS, False,
                                           "Did Not Find MultiAuth {multiauth_vlan_name}.",
                                           "ERROR: FOUND MultiAuth VLAN {multiauth_vlan_name}!",
                                           **kwargs)

    def multiauth_verify_session_timeout(self, device_name, timeout='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [timeout]     - The idle timeout value. (in seconds)

        Verifies the Session Timeout duration for all auth types.
        """
        args = {"timeout": timeout}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SESSION_TIMEOUT,
                                           self.parse_const.CHECK_MULTIAUTH_SESSION_TIMEOUT, True,
                                           "MultiAuth session timeout is {timeout} for all types.",
                                           "MultiAuth session timeout is NOT {timeout} for all types!",
                                           **kwargs)

    def multiauth_verify_mac_session_timeout(self, device_name, timeout='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [timeout]     - The idle timeout value. (in seconds)

        Verifies the session timeout duration for all the MAC Auth type.
        """
        args = {"timeout": timeout}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SESSION_TIMEOUT,
                                           self.parse_const.CHECK_MULTIAUTH_SESSION_TIMEOUT_MAC, True,
                                           "MultiAuth session timeout is {timeout} for MAC Auth.",
                                           "MultiAuth session timeout is NOT {timeout} for MAC Auth!",
                                           **kwargs)

    def multiauth_verify_dot1x_session_timeout(self, device_name, timeout='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [timeout]     - The idle timeout value. (in seconds)

        Verifies the session timeout duration for the 802.1X auth type.
        """
        args = {"timeout": timeout}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SESSION_TIMEOUT,
                                           self.parse_const.CHECK_MULTIAUTH_SESSION_TIMEOUT_DOT1X, True,
                                           "MultiAuth session timeout is {timeout} for 802.1X.",
                                           "MultiAuth session timeout is NOT {timeout} for 802.1X!",
                                           **kwargs)

    def multiauth_verify_web_session_timeout(self, device_name, timeout='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [timeout]     - The idle timeout value. (in seconds)

        Verifies the session timeout duration for the Web Auth type.
        """
        args = {"timeout": timeout}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SESSION_TIMEOUT,
                                           self.parse_const.CHECK_MULTIAUTH_SESSION_TIMEOUT_WEB, True,
                                           "MultiAuth session timeout is {timeout} for Web Auth.",
                                           "MultiAuth session timeout is NOT {timeout} for Web Auth!",
                                           **kwargs)

    def multiauth_verify_idle_timeout(self, device_name, timeout='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [timeout]     - The idle timeout value. (in seconds)

        Verifies the idle timeout duration for all auth types.
        """
        args = {"timeout": timeout}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_IDLE_TIMEOUT,
                                           self.parse_const.CHECK_MULTIAUTH_IDLE_TIMEOUT, True,
                                           "MultiAuth idle timeout is {timeout} for all types.",
                                           "MultiAuth idle timeout is NOT {timeout} for all types!",
                                           **kwargs)

    def multiauth_verify_mac_idle_timeout(self, device_name, timeout='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [timeout]     - The idle timeout value. (in seconds)

        Verifies the idle timeout duration for all auth types.
        """
        args = {"timeout": timeout}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_IDLE_TIMEOUT,
                                           self.parse_const.CHECK_MULTIAUTH_IDLE_TIMEOUT_MAC, True,
                                           "MultiAuth idle timeout is {timeout} for MAC Auth.",
                                           "MultiAuth idle timeout is NOT {timeout} for MAC Auth!",
                                           **kwargs)

    def multiauth_verify_dot1x_idle_timeout(self, device_name, timeout='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [timeout]     - The idle timeout value. (in seconds)

        Verifies the idle timeout duration for all auth types.
        """
        args = {"timeout": timeout}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_IDLE_TIMEOUT,
                                           self.parse_const.CHECK_MULTIAUTH_IDLE_TIMEOUT_DOT1X, True,
                                           "MultiAuth idle timeout is {timeout} for 802.1X.",
                                           "MultiAuth idle timeout is NOT {timeout} for 802.1X!",
                                           **kwargs)

    def multiauth_verify_web_idle_timeout(self, device_name, timeout='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [timeout]     - The idle timeout value. (in seconds)

        Verifies the idle timeout duration for all auth types.
        """
        args = {"timeout": timeout}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_IDLE_TIMEOUT,
                                           self.parse_const.CHECK_MULTIAUTH_IDLE_TIMEOUT_WEB, True,
                                           "MultiAuth idle timeout is {timeout} for Web Auth.",
                                           "MultiAuth idle timeout is NOT {timeout} for Web Auth!",
                                           **kwargs)

    def multiauth_verify_session_refresh_enabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.

        Verifies the idle timeout duration for all auth types.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO,
                                           self.parse_const.CHECK_MULTIAUTH_SESSION_REFRESH, True,
                                           "MultiAuth session-refresh is enabled on {device_name}.",
                                           "MultiAuth session-refresh is NOT enabled on {device_name}!",
                                           **kwargs)

    def multiauth_verify_session_refresh_interval(self, device_name, interval='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [interval]    - The session-refresh interval. (in seconds)

        Verifies the idle timeout duration for all auth types.
        """
        args = {"interval": interval}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO,
                                           self.parse_const.CHECK_MULTIAUTH_SESSION_REFRESH_INTERVAL, True,
                                           "MultiAuth session-refresh time is {interval} on {device_name}.",
                                           "MultiAuth session-refresh time is NOT {interval} on {device_name}!",
                                           **kwargs)

    def multiauth_verify_session_idle_time(self, device_name, station_address='', timer='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [timer]       - The idle-time to verify against. (in seconds)

        Verifies the idle time is greater than the supplied value.
        """
        args = {"station_address": station_address,
                "timer": timer}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SESSION,
                                           self.parse_const.CHECK_MULTIAUTH_IDLE_TIME, True,
                                           "MultiAuth idle-time for {station_address} was {timer}.",
                                           "MultiAuth idle-time for {station_address} was NOT {timer}!",
                                           **kwargs)

    def multiauth_verify_session_idle_time_greater_than(self, device_name, station_address='', timer='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [timer]       - The idle-time to verify against. (in seconds)

        Verifies the idle time is greater than the supplied value.
        """
        args = {"station_address": station_address,
                "timer": timer}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SESSION,
                                           self.parse_const.CHECK_MULTIAUTH_IDLE_TIME_GREATER, True,
                                           "MultiAuth idle-time for {station_address} was > {timer}.",
                                           "MultiAuth idle-time for {station_address} was NOT > {timer}!",
                                           **kwargs)

    def multiauth_verify_session_idle_time_less_than(self, device_name, station_address='', timer='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [timer]       - The idle-time to verify against. (in seconds)

        Verifies the idle time is greater than the supplied value.
        """
        args = {"station_address": station_address,
                "timer": timer}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SESSION,
                                           self.parse_const.CHECK_MULTIAUTH_IDLE_TIME_LESS, True,
                                           "MultiAuth idle-time for {station_address} was < {timer}.",
                                           "MultiAuth idle-time for {station_address} was NOT < {timer}!",
                                           **kwargs)

    def multiauth_verify_session_duration_greater_than(self, device_name, station_address='', timer='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [timer]       - The idle-time to verify against. (in seconds)

        Verifies the idle time is greater than the supplied value.
        """
        args = {"station_address": station_address,
                "timer": timer}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SESSION,
                                           self.parse_const.CHECK_MULTIAUTH_SESSION_DURATION_GREATER, True,
                                           "MultiAuth session duration for {station_address} was > {timer}.",
                                           "MultiAuth session duration for {station_address} was NOT > {timer}!",
                                           **kwargs)

    def multiauth_verify_session_duration_less_than(self, device_name, station_address='', timer='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [timer] - The idle-time to verify against. (in seconds)

        Verifies the idle time is greater than the supplied value.
        """
        args = {"station_address": station_address,
                "timer": timer}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SESSION,
                                           self.parse_const.CHECK_MULTIAUTH_SESSION_DURATION_LESS, True,
                                           "MultiAuth session duration for {station_address} was < {timer}.",
                                           "MultiAuth session duration for {station_address} was NOT < {timer}!",
                                           **kwargs)
