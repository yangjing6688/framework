from ExtremeAutomation.Keywords.NetworkElementKeywords.GeneratedKeywords.NetworkElementWebauthGenKeywords import NetworkElementWebauthGenKeywords


class WebAuthUdks():
    def __init__(self) -> None:
        self.networkElementWebauthGenKeywords = NetworkElementWebauthGenKeywords()

    def EnableWebAuthandVerifyitisEnabled(self, netelem_name, **kwargs):
        self.networkElementWebauthGenKeywords.webauth_enable_global(netelem_name, **kwargs)
        self.networkElementWebauthGenKeywords.webauth_verify_enabled(netelem_name, **kwargs)

    def EnableWebAuthPortandVerifyitisEnabled(self, netelem_name, port_list, **kwargs):
        self.networkElementWebauthGenKeywords.webauth_enable_control_port(netelem_name, port_list, **kwargs)
        self.networkElementWebauthGenKeywords.webauth_verify_port_enabled(netelem_name, port_list, **kwargs)

    def SetWebAuthIdleTimeoutandVerify(self, netelem_name, idle_timeout, **kwargs):
        self.networkElementWebauthGenKeywords.webauth_set_idle_timeout(netelem_name, idle_timeout, **kwargs)
        self.networkElementWebauthGenKeywords.webauth_verify_idle_timeout(netelem_name, idle_timeout, **kwargs)

    def SetWebAuthSessionTimeoutandVerify(self, netelem_name, session_timeout, **kwargs):
        self.networkElementWebauthGenKeywords.webauth_set_session_timeout(netelem_name, session_timeout, **kwargs)
        self.networkElementWebauthGenKeywords.webauth_verify_session_timeout(netelem_name, session_timeout, **kwargs)

    def SetWebAuthBaseURLandVerify(self, netelem_name, base_url_addr, **kwargs):
        self.networkElementWebauthGenKeywords.webauth_set_hostname(netelem_name, base_url_addr, **kwargs)
        self.networkElementWebauthGenKeywords.webauth_verify_url_name(netelem_name, base_url_addr, **kwargs)

    def SetWebAuthRedirectPageandVerify(self, netelem_name, redirect_addr, **kwargs):
        self.networkElementWebauthGenKeywords.webauth_set_redirect_page(netelem_name, redirect_addr, **kwargs)
        self.networkElementWebauthGenKeywords.webauth_verify_redirect_page(netelem_name, redirect_addr, **kwargs)

    def EnableWebAuthRedirectPageandVerify(self, netelem_name, **kwargs):
        self.networkElementWebauthGenKeywords.webauth_enable_redirect_page(netelem_name, **kwargs)
        self.networkElementWebauthGenKeywords.webauth_verify_redirect_enabled(netelem_name, **kwargs)

    def DisableWebAuthRedirectPageandVerify(self, netelem_name, **kwargs):
        self.networkElementWebauthGenKeywords.webauth_disable_redirect_page(netelem_name, **kwargs)
        self.networkElementWebauthGenKeywords.webauth_verify_redirect_disabled(netelem_name, **kwargs)

    def EnableWebAuthReauthenticateOnRefreshandVerify(self, netelem_name, **kwargs):
        self.networkElementWebauthGenKeywords.webauth_enable_reauthentication_on_refresh(netelem_name, **kwargs)
        self.networkElementWebauthGenKeywords.webauth_verify_reauthenticate_on_refresh_enabled(netelem_name, **kwargs)

    def DisableWebAuthReauthenticateOnRefreshandVerify(self, netelem_name, **kwargs):
        self.networkElementWebauthGenKeywords.webauth_disable_reauthentication_on_refresh(netelem_name, **kwargs)
        self.networkElementWebauthGenKeywords.webauth_verify_reauthenticate_on_refresh_disabled(netelem_name, **kwargs)

    def EnableWebAuthSessionRefreshandVerify(self, netelem_name, **kwargs):
        self.networkElementWebauthGenKeywords.webauth_enable_session_refresh(netelem_name, **kwargs)
        self.networkElementWebauthGenKeywords.webauth_verify_session_refresh_enabled(netelem_name, **kwargs)

    def DisableWebAuthSessionRefreshandVerify(self, netelem_name, **kwargs):
        self.networkElementWebauthGenKeywords.webauth_disable_session_refresh(netelem_name, **kwargs)
        self.networkElementWebauthGenKeywords.webauth_verify_session_refresh_disabled(netelem_name, **kwargs)

    def SetWebAuthSessionRefreshandVerify(self, netelem_name, session_refresh, minutes_sec_interval, **kwargs):
        self.networkElementWebauthGenKeywords.webauth_set_session_refresh(netelem_name, session_refresh, **kwargs)
        self.networkElementWebauthGenKeywords.webauth_verify_session_refresh_interval(netelem_name, minutes_sec_interval, **kwargs)

    def SetWebAuthAllowedRefreshFailuresandVerify(self,  netelem_name, num_failures, **kwargs):
        self.networkElementWebauthGenKeywords.webauth_set_allowed_refresh_failures(netelem_name, num_failures, **kwargs)
        self.networkElementWebauthGenKeywords.webauth_verify_allowed_refresh_failures(netelem_name, num_failures, **kwargs)

    def SetWebAuthDatatbaseOrdertoRadiusandVerify(self, netelem_name, **kwargs):
        self.networkElementWebauthGenKeywords.webauth_set_db_order_radius(netelem_name, **kwargs)
        self.networkElementWebauthGenKeywords.webauth_verify_database_order_radius(netelem_name, **kwargs)

    def SetWebAuthProtocolOrderandVerify(self, netelem_name, order, **kwargs):
        self.networkElementWebauthGenKeywords.webauth_set_protocol_order(netelem_name, order, **kwargs)
        self.networkElementWebauthGenKeywords.webauth_verify_protocol_order(netelem_name, order, **kwargs)

    #########################################################################
    ########################  CLEANUPKEYWORDS  #############################
    #########################################################################

    def DisableWebAuthandVerifyitisDisabled(self, netelem_name, **kwargs):
        self.networkElementWebauthGenKeywords.webauth_disable_global(netelem_name, **kwargs)
        self.networkElementWebauthGenKeywords.webauth_verify_disabled(netelem_name, **kwargs)

    def DisableWebAuthPortandVerifyitisDisabled(self, netelem_name,  port_list, **kwargs):
        self.networkElementWebauthGenKeywords.webauth_disable_control_port(netelem_name,  port_list, **kwargs)
        self.networkElementWebauthGenKeywords.webauth_verify_port_disabled(netelem_name,  port_list, **kwargs)

    def ClearWebAuthBaseURLandVerify(self, netelem_name, **kwargs):
        self.networkElementWebauthGenKeywords.webauth_clear_hostname(netelem_name, **kwargs)
        self.networkElementWebauthGenKeywords.webauth_verify_url_name_default(netelem_name, **kwargs)

    def ClearWebAuthRedirectPageandVerify(self, netelem_name, **kwargs):
        self.networkElementWebauthGenKeywords.webauth_clear_redirect_page(netelem_name, **kwargs)
        self.networkElementWebauthGenKeywords.webauth_verify_redirect_page_default(netelem_name, **kwargs)

    def ClearWebAuthAllowedRefreshFailuresandVerify(self, netelem_name, **kwargs):
        self.networkElementWebauthGenKeywords.webauth_clear_allowed_refresh_failures(netelem_name, **kwargs)
        self.networkElementWebauthGenKeywords.webauth_verify_allowed_refresh_failures_default(netelem_name, **kwargs)

    def ClearWebAuthSessionRefreshandVerify(self, netelem_name, **kwargs):
        self.networkElementWebauthGenKeywords.webauth_clear_session_refresh(netelem_name, **kwargs)
        self.networkElementWebauthGenKeywords.webauth_verify_session_refresh_default(netelem_name, **kwargs)

    def ClearWebAuthNetloginSessionTimeoutandVerify(self, netelem_name, **kwargs):
        self.networkElementWebauthGenKeywords.webauth_clear_session_timeout(netelem_name, **kwargs)
        self.networkElementWebauthGenKeywords.webauth_verify_session_timeout_default(netelem_name, **kwargs)

    def ClearWebAuthNetloginIdleTimeoutandVerify(self, netelem_name, **kwargs):
        self.networkElementWebauthGenKeywords.webauth_clear_idle_timeout(netelem_name, **kwargs)
        self.networkElementWebauthGenKeywords.webauth_verify_idle_timeout_default(netelem_name, **kwargs)

    def ClearAllWebauthSettings(self, netelem_name, **kwargs):
        self.ClearWebAuthBaseURLandVerify(netelem_name, **kwargs)
        self.ClearWebAuthRedirectPageandVerify(netelem_name, **kwargs)
        self.EnableWebAuthSessionRefreshandVerify(netelem_name, **kwargs)
        self.ClearWebAuthSessionRefreshandVerify(netelem_name, **kwargs)
        self.ClearWebAuthAllowedRefreshFailuresandVerify(netelem_name, **kwargs)
        self.DisableWebAuthReauthenticateOnRefreshandVerify(netelem_name, **kwargs)
        self.EnableWebAuthRedirectPageandVerify(netelem_name, **kwargs)
        self.ClearWebAuthNetloginSessionTimeoutandVerify(netelem_name, **kwargs)
        self.ClearWebAuthNetloginIdleTimeoutandVerify(netelem_name, **kwargs)
