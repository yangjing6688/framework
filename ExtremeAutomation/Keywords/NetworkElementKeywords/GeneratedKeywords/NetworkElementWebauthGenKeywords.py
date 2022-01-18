"""
Keyword class for all webauth cli commands.
"""
from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import NetworkElementKeywordBaseClass
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.Constants.WebauthConstants import \
    WebauthConstants as ParseConstants
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.Constants.WebauthConstants import \
    WebauthConstants as CommandConstants
# All imports above this line will be removed after generation.
# User imports must be added below.


class NetworkElementWebauthGenKeywords(NetworkElementKeywordBaseClass):
    def __init__(self):
        super(NetworkElementWebauthGenKeywords, self).__init__()
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()
        self.api_const = "webauth"

    def webauth_enable_global(self, device_name, **kwargs):
        """
        Description: Enables the web authentication feature.

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_GLOBAL,
                                    **kwargs)

    def webauth_disable_global(self, device_name, **kwargs):
        """
        Description: Disables the web authentication feature.

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_GLOBAL,
                                    **kwargs)

    def webauth_enable_control_port(self, device_name, port='', **kwargs):
        """
        Description: Enables the specified ports for web authentication.

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_CONTROL_PORT,
                                    **kwargs)

    def webauth_disable_control_port(self, device_name, port='', **kwargs):
        """
        Description: Disables the specified ports for web authentication.

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_CONTROL_PORT,
                                    **kwargs)

    def webauth_enable_redirect_page(self, device_name, **kwargs):
        """
        Description: This command enables the network login redirect page so that the client is sent to the redirect
                     page rather than the original page.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_REDIRECT_PAGE,
                                    **kwargs)

    def webauth_disable_redirect_page(self, device_name, **kwargs):
        """
        Description: This command disables the network login redirect page so that the client is sent to the the
                     original page rather than the redirect page.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_REDIRECT_PAGE,
                                    **kwargs)

    def webauth_enable_logout_page(self, device_name, **kwargs):
        """
        Description: This command controls the logout window pop-up on the web-based network client.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_LOGOUT_PAGE,
                                    **kwargs)

    def webauth_disable_logout_page(self, device_name, **kwargs):
        """
        Description: This command controls the logout window pop-up on the web-based network client.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_LOGOUT_PAGE,
                                    **kwargs)

    def webauth_enable_session_refresh(self, device_name, **kwargs):
        """
        Description: Sessions can refresh themselves after a configured timeout.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_SESSION_REFRESH,
                                    **kwargs)

    def webauth_disable_session_refresh(self, device_name, **kwargs):
        """
        Description: Sessions cannot refresh themselves.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_SESSION_REFRESH,
                                    **kwargs)

    def webauth_enable_reauthentication_on_refresh(self, device_name, **kwargs):
        """
        Description: Enables re-authentication to occur with the session refresh.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_REAUTHENTICATION_ON_REFRESH,
                                    **kwargs)

    def webauth_disable_reauthentication_on_refresh(self, device_name, **kwargs):
        """
        Description: Disables re-authentication to occur with the session refresh.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_REAUTHENTICATION_ON_REFRESH,
                                    **kwargs)

    def webauth_set_hostname(self, device_name, url_name='', **kwargs):
        """
        Description: Configures base address/URL for the webauth users.

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "url_name": url_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_HOSTNAME,
                                    **kwargs)

    def webauth_set_init_mac_port(self, device_name, mac='', port='', **kwargs):
        """
        Description: Clears and initializes the web-auth sessions on a VLAN port and mac.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "mac": mac,
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_INIT_MAC_PORT,
                                    **kwargs)

    def webauth_set_init_port(self, device_name, port='', **kwargs):
        """
        Description: Clears and initializes the webauth network login sessions on a VLAN port.

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_INIT_PORT,
                                    **kwargs)

    def webauth_set_init_mac(self, device_name, mac='', **kwargs):
        """
        Description: Clears and initializes the webauth network login session for a particular mac address.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "mac": mac
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_INIT_MAC,
                                    **kwargs)

    def webauth_set_init_all(self, device_name, **kwargs):
        """
        Description: Clears and initializes all webauth sessions.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_INIT_ALL,
                                    **kwargs)

    def webauth_set_redirect_page(self, device_name, redirect_page='', **kwargs):
        """
        Description: Configures destination address/URL for the netlogin users.

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "redirect_page": redirect_page
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_REDIRECT_PAGE,
                                    **kwargs)

    def webauth_set_session_timeout(self, device_name, session_timeout='', **kwargs):
        """
        Description: Use this command to set the maximum number of seconds an authenticated session may last before
                     termination of the session.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "session_timeout": session_timeout
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_SESSION_TIMEOUT,
                                    **kwargs)

    def webauth_set_idle_timeout(self, device_name, idle_timeout='', **kwargs):
        """
        Description: Use this command to set the maximum number of seconds an idle authenticated session lasts before
                     termination of the session.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "idle_timeout": idle_timeout
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_IDLE_TIMEOUT,
                                    **kwargs)

    def webauth_set_lease_time(self, device_name, vlan_name='', lease_time='', **kwargs):
        """
        Description: Configures the lease timer in seconds for the users coming in on the vlan.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "lease_time": lease_time,
            "vlan_name": vlan_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_LEASE_TIME,
                                    **kwargs)

    def webauth_set_session_refresh(self, device_name, session_refresh='', **kwargs):
        """
        Description: Configures the value of the session refresh timeout.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "session_refresh": session_refresh
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_SESSION_REFRESH,
                                    **kwargs)

    def webauth_set_allowed_refresh_failures(self, device_name, num_failures='', **kwargs):
        """
        Description: This command allows you to set the number of refresh failures allowed. You can set the number of
                     failures to be from between 0 to 5.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "num_failures": num_failures
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_ALLOWED_REFRESH_FAILURES,
                                    **kwargs)

    def webauth_set_protocol_order(self, device_name, order='', **kwargs):
        """
        Description: Sets the protocol precedence as desired.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "order": order
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PROTOCOL_ORDER,
                                    **kwargs)

    def webauth_set_protocol_order_web_dot1x_mac(self, device_name, **kwargs):
        """
        Description: Sets the protocol precedence to web-based first followed by dot1x and then mac.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PROTOCOL_ORDER_WEB_DOT1X_MAC,
                                    **kwargs)

    def webauth_set_protocol_order_web_mac_dot1x(self, device_name, **kwargs):
        """
        Description: Sets the protocol precedence to web-based first followed by mac and then dot1x.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PROTOCOL_ORDER_WEB_MAC_DOT1X,
                                    **kwargs)

    def webauth_set_db_order_local(self, device_name, **kwargs):
        """
        Description: Configures the order of database authentication protocols for webauth to use local only.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_DB_ORDER_LOCAL,
                                    **kwargs)

    def webauth_set_db_order_local_radius(self, device_name, **kwargs):
        """
        Description: Configures the order of database authentication protocols for webauth to use local and then RADIUS.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_DB_ORDER_LOCAL_RADIUS,
                                    **kwargs)

    def webauth_set_db_order_radius(self, device_name, **kwargs):
        """
        Description: Configures the order of database authentication protocols for webauth to use RADIUS only.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_DB_ORDER_RADIUS,
                                    **kwargs)

    def webauth_set_db_order_radius_local(self, device_name, **kwargs):
        """
        Description: Configures the order of database authentication protocols for webauth to use RADIUS and then local.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_DB_ORDER_RADIUS_LOCAL,
                                    **kwargs)

    def webauth_clear_hostname(self, device_name, **kwargs):
        """
        Description: Removes the base address/URL for the webauth users.

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_HOSTNAME,
                                    **kwargs)

    def webauth_clear_redirect_page(self, device_name, **kwargs):
        """
        Description: Configures destination address/URL for the netlogin users back to default.

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_REDIRECT_PAGE,
                                    **kwargs)

    def webauth_clear_session_timeout(self, device_name, **kwargs):
        """
        Description: Use this command to set the session timeout for webauth to default.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_SESSION_TIMEOUT,
                                    **kwargs)

    def webauth_clear_idle_timeout(self, device_name, **kwargs):
        """
        Description: Use this command to set the idle session timeout for webauth to default.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_IDLE_TIMEOUT,
                                    **kwargs)

    def webauth_clear_lease_time(self, device_name, vlan_name='', **kwargs):
        """
        Description: Sets the lease timer for the users coming in on the vlan to the default of 10 seconds.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "vlan_name": vlan_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_LEASE_TIME,
                                    **kwargs)

    def webauth_clear_session_refresh(self, device_name, **kwargs):
        """
        Description: Unconfigures the session refresh timeout.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_SESSION_REFRESH,
                                    **kwargs)

    def webauth_clear_allowed_refresh_failures(self, device_name, **kwargs):
        """
        Description: This command allows you to restore the number of refresh failures allowed to the default value of
                     0.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_ALLOWED_REFRESH_FAILURES,
                                    **kwargs)

    def webauth_clear_protocol_order(self, device_name, **kwargs):
        """
        Description: Sets the protocol precedence to the default setting of dot1x.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_PROTOCOL_ORDER,
                                    **kwargs)

    def webauth_clear_db_order(self, device_name, **kwargs):
        """
        Description: Sets the database authentication order for webauth to the default of RADIUS and then local.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_DB_ORDER,
                                    **kwargs)

    # ##################################################################################################################
    #   Inspection Keywords   ##########################################################################################
    # ##################################################################################################################

    def webauth_verify_enabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.

        Verifies that webauth is enabled.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SUMMARY_SNAPSHOT,
                                           self.parse_const.CHECK_WEBAUTH_ENABLED, True,
                                           "Web-Auth is correctly enabled.",
                                           "WARNING: Web-Auth IS NOT enabled!",
                                           **kwargs)

    def webauth_verify_disabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.

        Verifies that webauth is disabled.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SUMMARY_SNAPSHOT,
                                           self.parse_const.CHECK_WEBAUTH_ENABLED, False,
                                           "Web-Auth is correctly disabled.",
                                           "WARNING: Web-Auth IS NOT disabled!",
                                           **kwargs)

    def webauth_verify_port_enabled(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [port]        - The port(s) to check for webauth being enabled.

        Verifies that webauth is enabled on the given port(s).
        """
        args = {"port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT,
                                           self.parse_const.VERIFY_WEBAUTH_PORT_STATE, True,
                                           "Web-Auth is enabled on port {port}.",
                                           "WARNING: Web-Auth IS NOT enabled on port {port}!",
                                           **kwargs)

    def webauth_verify_port_disabled(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [port]        - The port(s) to check for webauth being disabled.

        Verifies that webauth is enabled on the given port(s).
        """
        args = {"port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT,
                                           self.parse_const.VERIFY_WEBAUTH_PORT_STATE, False,
                                           "Web-Auth is disabled on port {port}.",
                                           "WARNING: Web-Auth IS NOT disabled on port {port}!",
                                           **kwargs)

    def webauth_verify_url_name(self, device_name, base_url='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [base_url]    - The base URL address to check for.

        Verifies that the webauth url exists.
        """
        args = {"base_url": base_url}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SUMMARY_SNAPSHOT,
                                           self.parse_const.CHECK_WEBAUTH_BASE_URL_EXISTS, True,
                                           "Web-Auth base URL is {base_url}.",
                                           "WARNING: Web-Auth base URL IS NOT {base_url}!",
                                           **kwargs)

    def webauth_verify_url_name_default(self, device_name, base_url="network-access.com", **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [base_url]    - The base URL to check for.

        Verifies that the webauth url is the default value.
        """
        args = {"base_url": base_url}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SUMMARY_SNAPSHOT,
                                           self.parse_const.CHECK_WEBAUTH_BASE_URL_DEFAULT, True,
                                           "Web-Auth base URL is the default, {base_url}.",
                                           "WARNING: Web-Auth base URL IS NOT the default, {base_url}!",
                                           **kwargs)

    def webauth_verify_lease_time(self, device_name, vlan_name='', lease_time='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vlan]        - The vlan that the lease time is set on.
        [lease_time]  - The expected value of the netlogin lease time

        Verifies that the lease time for the netlogin vlan is correct.
        """
        args = {"vlan_name": vlan_name,
                "lease_time": lease_time}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_VLAN_DHCP_NETLOGIN_LEASE_TIME,
                                           self.parse_const.CHECK_WEBAUTH_LEASE_TIME, True,
                                           "Web-Auth lease time is {lease_time}.",
                                           "WARNING: Web-Auth lease time IS NOT {lease_time}!",
                                           **kwargs)

    def webauth_verify_redirect_enabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.

        Verifies that webauth redirect is enabled.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SUMMARY_SNAPSHOT,
                                           self.parse_const.CHECK_WEBAUTH_REDIRECT_ENABLED, True,
                                           "Web-Auth redirect is enabled.",
                                           "WARNING: Web-Auth redirect IS NOT enabled!",
                                           **kwargs)

    def webauth_verify_redirect_disabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.

        Verifies that webauth redirect is disabled.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SUMMARY_SNAPSHOT,
                                           self.parse_const.CHECK_WEBAUTH_REDIRECT_ENABLED, False,
                                           "Web-Auth redirect is disabled.",
                                           "WARNING: Web-Auth redirect IS NOT disabled!",
                                           **kwargs)

    def webauth_verify_session_timeout(self, device_name, session_timeout='', **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will be run against.
        [session_timeout] - The expected session timeout value in seconds.

        Verifies that webauth session timeout configuration is shown as expected.
        """
        args = {"session_timeout": session_timeout}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_TIMEOUT_VALUES,
                                           self.parse_const.CHECK_WEBAUTH_SESSION_TIMEOUT, True,
                                           "Web-Auth session timeout is {session_timeout}.",
                                           "WARNING: Web-Auth session timeout IS NOT {session_timeout}!",
                                           **kwargs)

    def webauth_verify_session_timeout_default(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.

        Verifies that webauth session timeout is set to default.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_TIMEOUT_VALUES,
                                           self.parse_const.CHECK_WEBAUTH_SESSION_TIMEOUT_DEFAULT, True,
                                           "Web-Auth session timeout is set to default.",
                                           "WARNING: Web-Auth session timeout IS NOT set to default!",
                                           **kwargs)

    def webauth_verify_idle_timeout(self, device_name, idle_timeout='', **kwargs):
        """
        Keyword Arguments:
        [device_name]  - The device the keyword will be run against.
        [idle_timeout] - The expected session idle timeout value in seconds.

        Verifies that webauth session idle timeout configuration is shown as expected.
        """
        args = {"idle_timeout": idle_timeout}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_TIMEOUT_VALUES,
                                           self.parse_const.CHECK_WEBAUTH_IDLE_TIMEOUT, True,
                                           "Web-Auth session idle timeout is {idle_timeout}.",
                                           "WARNING: Web-Auth session idle timeout IS NOT {idle_timeout}!",
                                           **kwargs)

    def webauth_verify_idle_timeout_default(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.

        Verifies that webauth session idle timeout is set to default.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_TIMEOUT_VALUES,
                                           self.parse_const.CHECK_WEBAUTH_IDLE_TIMEOUT_DEFAULT, True,
                                           "Web-Auth session idle timeout is set to default.",
                                           "WARNING: Web-Auth session idle timeout IS NOT set to default!",
                                           **kwargs)

    def webauth_verify_user_authenticated(self, device_name, mac_or_ip_or_user='', **kwargs):
        """
        Keyword Arguments:
        [device_name]       - The device the keyword will be run against.
        [mac_or_ip_or_user] - The user MAC, IP, or username in either of the following forms:
                              "08:00:27:ab:16:c3" or "192.168.1.201" or "pwapap"

        Verifies that a webauth user is authenticated.
        """
        args = {"mac_or_ip_or_user": mac_or_ip_or_user}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SUMMARY_SNAPSHOT,
                                           self.parse_const.CHECK_WEBAUTH_USER_AUTHENTICATED, True,
                                           "Web-Auth user {mac_or_ip_or_user} is authenticated.",
                                           "WARNING: Web-Auth user {mac_or_ip_or_user} IS NOT authenticated!",
                                           **kwargs)

    def webauth_verify_user_unauthenticated(self, device_name, mac_or_ip_or_user='', **kwargs):
        """
        Keyword Arguments:
        [device_name]       - The device the keyword will be run against.
        [mac_or_ip_or_user] - The user MAC, IP, or username in either of the following forms:
                              "08:00:27:ab:16:c3" or "192.168.1.201" or "pwapap"

        Verifies that a webauth user is unauthenticated.
        """
        args = {"mac_or_ip_or_user": mac_or_ip_or_user}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SUMMARY_SNAPSHOT,
                                           self.parse_const.CHECK_WEBAUTH_USER_UNAUTHENTICATED, True,
                                           "Web-Auth user {mac_or_ip_or_user} is unauthenticated.",
                                           "WARNING: Web-Auth user {mac_or_ip_or_user} IS NOT unauthenticated!",
                                           **kwargs)

    def webauth_verify_user_authenticated_by_radius(self, device_name, mac_or_ip_or_user='', **kwargs):
        """
        Keyword Arguments:
        [device_name]       - The device the keyword will be run against.
        [mac_or_ip_or_user] - The user MAC, IP, or username in either of the following forms:
                              "08:00:27:ab:16:c3" or "192.168.1.201" or "pwapap"

        Verifies that a webauth user is authenticated by RADIUS.
        """
        args = {"mac_or_ip_or_user": mac_or_ip_or_user}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SUMMARY_SNAPSHOT,
                                           self.parse_const.CHECK_WEBAUTH_USER_AUTHENTICATED_RADIUS, True,
                                           "Web-Auth user {mac_or_ip_or_user} is authenticated by RADIUS.",
                                           "Web-Auth user {mac_or_ip_or_user} IS NOT authenticated by RADIUS!",
                                           **kwargs)

    def webauth_verify_user_login_name(self, device_name, mac_or_ip_or_user='', login_name='', **kwargs):
        """
        Keyword Arguments:
        [device_name]       - The device the keyword will be run against.
        [mac_or_ip_or_user] - The user MAC, IP, or username in either of the following forms:
                              "08:00:27:ab:16:c3" or "192.168.1.201" or "pwapap"
        [login_name]        - The expected login name.

        Verifies that a webath user login name is correct.
        """
        args = {"mac_or_ip_or_user": mac_or_ip_or_user,
                "login_name": login_name}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SUMMARY_SNAPSHOT,
                                           self.parse_const.CHECK_WEBAUTH_USER_LOGIN_NAME, True,
                                           "Web-Auth user {mac_or_ip_or_user} login name is {login_name}.",
                                           "Web-Auth user {mac_or_ip_or_user} login name IS NOT {login_name}!",
                                           **kwargs)

    def webauth_verify_user_ip(self, device_name, mac_or_ip_or_user='', ip='', **kwargs):
        """
        Keyword Arguments:
        [device_name]       - The device the keyword will be run against.
        [mac_or_ip_or_user] - The user MAC, IP, or username in either of the following forms:
                              "08:00:27:ab:16:c3" or "192.168.1.201" or "pwapap"
        [ip]                - The expected ip address

        Verifies that a webauth user IP address is correct.
        """
        args = {"mac_or_ip_or_user": mac_or_ip_or_user,
                "ip": ip}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SUMMARY_SNAPSHOT,
                                           self.parse_const.CHECK_WEBAUTH_USER_IP, True,
                                           "Web-Auth user {mac_or_ip_or_user} IP address is {ip}.",
                                           "Web-Auth user {mac_or_ip_or_user} IP address IS NOT {ip}!",
                                           **kwargs)

    def webauth_verify_user_auth_type(self, device_name, mac_or_ip_or_user='', auth_type='', **kwargs):
        """
        Keyword Arguments:
        [device_name]       - The device the keyword will be run against.
        [mac_or_ip_or_user] - The user MAC, IP, or username in either of the following forms:
                              "08:00:27:ab:16:c3" or "192.168.1.201" or "pwapap"
        [auth_type]         - The expected auth type such as Web Mac or Dot1x.

        Verifies that a webauth user IP address is correct.
        """
        args = {"mac_or_ip_or_user": mac_or_ip_or_user,
                "auth_type": auth_type}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SUMMARY_SNAPSHOT,
                                           self.parse_const.CHECK_WEBAUTH_USER_AUTHENTICATED_AUTH_TYPE, True,
                                           "Web-Auth user {mac_or_ip_or_user} protocol type is {auth_type}.",
                                           "Web-Auth user {mac_or_ip_or_user} protocol type IS NOT {auth_type}!",
                                           **kwargs)

    def webauth_verify_database_order_radius(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.

        Verifies that the webauth database order is RADIUS only.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SUMMARY_SNAPSHOT,
                                           self.parse_const.CHECK_WEBAUTH_DATABASE_ORDER_RADIUS, True,
                                           "Web-Auth database order showing RADIUS only is correct.",
                                           "Web-Auth database order is not showing RADIUS only!",
                                           **kwargs)

    def webauth_verify_database_order_radius_local(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.

        Verifies that the webauth database order is first RADIUS and local as 2nd.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SUMMARY_SNAPSHOT,
                                           self.parse_const.CHECK_WEBAUTH_DATABASE_ORDER_RADIUS_LOCAL, True,
                                           "Web-Auth database order showing RADIUS and local is correct.",
                                           "Web-Auth database order is not showing RADIUS and local!",
                                           **kwargs)

    def webauth_verify_database_order_local(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.

        Verifies that the webauth database order is local only.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SUMMARY_SNAPSHOT,
                                           self.parse_const.CHECK_WEBAUTH_DATABASE_ORDER_LOCAL, True,
                                           "Web-Auth database order showing local only is correct.",
                                           "Web-Auth database order is not showing local only!",
                                           **kwargs)

    def webauth_verify_database_order_local_radius(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.

        Verifies that the webauth database order is first local and RADIUS as 2nd.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SUMMARY_SNAPSHOT,
                                           self.parse_const.CHECK_WEBAUTH_DATABASE_ORDER_LOCAL_RADIUS, True,
                                           "Web-Auth database order showing local and RADIUS is correct.",
                                           "Web-Auth database order is not showing local and RADIUS!",
                                           **kwargs)

    def webauth_verify_protocol_order(self, device_name, order='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [order]       - The protocol order separated by spaces or commas.
                        Protocols are web-based, 802.1x, mac-based.

        Verifies that the netlogin protocol order is correct.
        """
        args = {"order": order}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SUMMARY_SNAPSHOT,
                                           self.parse_const.CHECK_WEBAUTH_PROTOCOL_ORDER, True,
                                           "Web-Auth protocol order is {order}.",
                                           "WARNING: Web-Auth protocol order IS NOT {order}!",
                                           **kwargs)

    def webauth_verify_redirect_page_enabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.

        Verifies that the webauth redirect page is enabled.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SUMMARY_SNAPSHOT,
                                           self.parse_const.CHECK_WEBAUTH_REDIRECT_PAGE_ENABLED, True,
                                           "Web-Auth redirect page is enabled.",
                                           "WARNING: Web-Auth redirect page IS NOT enabled!",
                                           **kwargs)

    def webauth_verify_redirect_page_disabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.

        Verifies that the webauth redirect page is disabled.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SUMMARY_SNAPSHOT,
                                           self.parse_const.CHECK_WEBAUTH_REDIRECT_PAGE_DISABLED, True,
                                           "Web-Auth redirect page is disabled.",
                                           "WARNING: Web-Auth redirect page IS NOT disabled!",
                                           **kwargs)

    def webauth_verify_redirect_page(self, device_name, address='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [address]     - The HTTP URL address.
                        It can be something like http://192.168.10.11 or http://www.extremenetworks.com

        Verifies that the webauth redirect page is correct.
        """
        args = {"address": address}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SUMMARY_SNAPSHOT,
                                           self.parse_const.CHECK_WEBAUTH_REDIRECT_PAGE, True,
                                           "Web-Auth redirect page is {address}.",
                                           "Web-Auth redirect page IS NOT {address}!",
                                           **kwargs)

    def webauth_verify_redirect_page_default(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.

        Verifies that the webauth redirect page is default of http://www.extremenetworks.com.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SUMMARY_SNAPSHOT,
                                           self.parse_const.CHECK_WEBAUTH_REDIRECT_PAGE_DEFAULT, True,
                                           "Web-Auth redirect page is the default.",
                                           "WARNING: Web-Auth redirect page IS NOT the default!",
                                           **kwargs)

    def webauth_verify_reauthenticate_on_refresh_enabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.

        Verifies that the webauth reauthenticate on refresh is enabled.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SUMMARY_SNAPSHOT,
                                           self.parse_const.CHECK_WEBAUTH_REAUTHENTICATE_ON_REFRESH_ENABLED, True,
                                           "Web-Auth reauthenticate on refresh is enabled.",
                                           "WARNING: Web-Auth reauthenticate on refresh IS NOT enabled!",
                                           **kwargs)

    def webauth_verify_reauthenticate_on_refresh_disabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.

        Verifies that the webauth reauthenticate on refresh is disabled.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SUMMARY_SNAPSHOT,
                                           self.parse_const.CHECK_WEBAUTH_REAUTHENTICATE_ON_REFRESH_DISABLED,
                                           True, "Web-Auth reauthenticate on refresh is disabled.",
                                           "WARNING: Web-Auth reauthenticate on refresh IS NOT disabled!",
                                           **kwargs)

    def webauth_verify_session_refresh_enabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.

        Verifies that the webauth session refresh is enabled.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SUMMARY_SNAPSHOT,
                                           self.parse_const.CHECK_WEBAUTH_SESSION_REFRESH_ENABLED, True,
                                           "Web-Auth session refresh is enabled.",
                                           "WARNING: Web-Auth session refresh IS NOT enabled!",
                                           **kwargs)

    def webauth_verify_session_refresh_disabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.

        Verifies that the webauth session refresh is disabled.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SUMMARY_SNAPSHOT,
                                           self.parse_const.CHECK_WEBAUTH_SESSION_REFRESH_DISABLED, True,
                                           "Web-Auth session refresh is disabled.",
                                           "WARNING: Web-Auth session refresh IS NOT disabled!",
                                           **kwargs)

    def webauth_verify_session_refresh_interval(self, device_name, refresh_interval='', **kwargs):
        """
        Keyword Arguments:
        [device_name]      - The device the keyword will be run against.
        [refresh_interval] - The session refresh interval to be verified in minutes:seconds.

        Verifies that the webauth session refresh interval is correct.
        """
        args = {"refresh_interval": refresh_interval}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SUMMARY_SNAPSHOT,
                                           self.parse_const.CHECK_WEBAUTH_SESSION_REFRESH_INTERVAL, True,
                                           "Web-Auth session refresh interval is {refresh_interval}.",
                                           "Web-Auth session refresh interval IS NOT {refresh_interval}!",
                                           **kwargs)

    def webauth_verify_allowed_refresh_failures(self, device_name, num_failures='', **kwargs):
        """
        Keyword Arguments:
        [device_name]  - The device the keyword will be run against.
        [num_failures] - The expected number of allowed refresh failures.

        Verifies that webauth allowed session refresh failures is correct.
        """
        args = {"num_failures": num_failures}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SUMMARY_SNAPSHOT,
                                           self.parse_const.CHECK_WEBAUTH_ALLOWED_REFRESH_FAILURES, True,
                                           "Web-Auth allowed session refresh failures is {num_failures}.",
                                           "Web-Auth allowed session refresh failures IS NOT {num_failures}!",
                                           **kwargs)

    def webauth_verify_allowed_refresh_failures_default(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.

        Verifies that webauth allowed session refresh failures is set to the default of zero.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SUMMARY_SNAPSHOT,
                                           self.parse_const.CHECK_WEBAUTH_ALLOWED_REFRESH_FAILURES_DEFAULT, True,
                                           "Web-Auth allowed session refresh failures is the default.",
                                           "Web-Auth allowed session refresh failures IS NOT the default!",
                                           **kwargs)

    def webauth_verify_session_refresh_default(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.

        Verifies that webauth session refresh is set to the default value of 3 minutes.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SUMMARY_SNAPSHOT,
                                           self.parse_const.CHECK_WEBAUTH_SESSION_REFRESH_DEFAULT, True,
                                           "Web-Auth session refresh is the default value.",
                                           "Web-Auth session refresh IS NOT the default value!",
                                           **kwargs)
