"""
This class outlines all the constants for the webauth API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(WebauthConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class WebauthConstants(ApiConstants):
    def __init__(self):
        super(WebauthConstants, self).__init__()
        self.CHECK_WEBAUTH_ALLOWED_REFRESH_FAILURES = {"constant": "check_webauth_allowed_refresh_failures",
                                                       "tags": ["PARSE_CLI"],
                                                       "link": self.link.check_webauth_allowed_refresh_failures}
        self.CHECK_WEBAUTH_ALLOWED_REFRESH_FAILURES_DEFAULT = {"constant": "check_webauth_allowed_refresh_failures_default",
                                                               "tags": ["PARSE_CLI"],
                                                               "link": self.link.check_webauth_allowed_refresh_failures_default}
        self.CHECK_WEBAUTH_BASE_URL_DEFAULT = {"constant": "check_webauth_base_url_default",
                                               "tags": ["PARSE_CLI"],
                                               "link": self.link.check_webauth_base_url_default}
        self.CHECK_WEBAUTH_BASE_URL_EXISTS = {"constant": "check_webauth_base_url_exists",
                                              "tags": ["PARSE_CLI"],
                                              "link": self.link.check_webauth_base_url_exists}
        self.CHECK_WEBAUTH_DATABASE_ORDER_LOCAL = {"constant": "check_webauth_database_order_local",
                                                   "tags": ["PARSE_CLI"],
                                                   "link": self.link.check_webauth_database_order_local}
        self.CHECK_WEBAUTH_DATABASE_ORDER_LOCAL_RADIUS = {"constant": "check_webauth_database_order_local_radius",
                                                          "tags": ["PARSE_CLI"],
                                                          "link": self.link.check_webauth_database_order_local_radius}
        self.CHECK_WEBAUTH_DATABASE_ORDER_RADIUS = {"constant": "check_webauth_database_order_radius",
                                                    "tags": ["PARSE_CLI"],
                                                    "link": self.link.check_webauth_database_order_radius}
        self.CHECK_WEBAUTH_DATABASE_ORDER_RADIUS_LOCAL = {"constant": "check_webauth_database_order_radius_local",
                                                          "tags": ["PARSE_CLI"],
                                                          "link": self.link.check_webauth_database_order_radius_local}
        self.CHECK_WEBAUTH_ENABLED = {"constant": "check_webauth_enabled",
                                      "tags": ["PARSE_CLI"],
                                      "link": self.link.check_webauth_enabled}
        self.CHECK_WEBAUTH_ENABLED_ON_PORT = {"constant": "check_webauth_enabled_on_port",
                                              "tags": ["PARSE_CLI"],
                                              "link": self.link.check_webauth_enabled_on_port}
        self.CHECK_WEBAUTH_IDLE_TIMEOUT = {"constant": "check_webauth_idle_timeout",
                                           "tags": ["PARSE_CLI"],
                                           "link": self.link.check_webauth_idle_timeout}
        self.CHECK_WEBAUTH_IDLE_TIMEOUT_DEFAULT = {"constant": "check_webauth_idle_timeout_default",
                                                   "tags": ["PARSE_CLI"],
                                                   "link": self.link.check_webauth_idle_timeout_default}
        self.CHECK_WEBAUTH_LEASE_TIME = {"constant": "check_webauth_lease_time",
                                         "tags": ["PARSE_CLI"],
                                         "link": self.link.check_webauth_lease_time}
        self.CHECK_WEBAUTH_PROTOCOL_ORDER = {"constant": "check_webauth_protocol_order",
                                             "tags": ["PARSE_CLI"],
                                             "link": self.link.check_webauth_protocol_order}
        self.CHECK_WEBAUTH_REAUTHENTICATE_ON_REFRESH_DISABLED = {"constant": "check_webauth_reauthenticate_on_refresh_disabled",
                                                                 "tags": ["PARSE_CLI"],
                                                                 "link": self.link.check_webauth_reauthenticate_on_refresh_disabled}
        self.CHECK_WEBAUTH_REAUTHENTICATE_ON_REFRESH_ENABLED = {"constant": "check_webauth_reauthenticate_on_refresh_enabled",
                                                                "tags": ["PARSE_CLI"],
                                                                "link": self.link.check_webauth_reauthenticate_on_refresh_enabled}
        self.CHECK_WEBAUTH_REDIRECT_ENABLED = {"constant": "check_webauth_redirect_enabled",
                                               "tags": ["PARSE_CLI"],
                                               "link": self.link.check_webauth_redirect_enabled}
        self.CHECK_WEBAUTH_REDIRECT_PAGE = {"constant": "check_webauth_redirect_page",
                                            "tags": ["PARSE_CLI"],
                                            "link": self.link.check_webauth_redirect_page}
        self.CHECK_WEBAUTH_REDIRECT_PAGE_DEFAULT = {"constant": "check_webauth_redirect_page_default",
                                                    "tags": ["PARSE_CLI"],
                                                    "link": self.link.check_webauth_redirect_page_default}
        self.CHECK_WEBAUTH_REDIRECT_PAGE_DISABLED = {"constant": "check_webauth_redirect_page_disabled",
                                                     "tags": ["PARSE_CLI"],
                                                     "link": self.link.check_webauth_redirect_page_disabled}
        self.CHECK_WEBAUTH_REDIRECT_PAGE_ENABLED = {"constant": "check_webauth_redirect_page_enabled",
                                                    "tags": ["PARSE_CLI"],
                                                    "link": self.link.check_webauth_redirect_page_enabled}
        self.CHECK_WEBAUTH_SESSION_REFRESH_DEFAULT = {"constant": "check_webauth_session_refresh_default",
                                                      "tags": ["PARSE_CLI"],
                                                      "link": self.link.check_webauth_session_refresh_default}
        self.CHECK_WEBAUTH_SESSION_REFRESH_DISABLED = {"constant": "check_webauth_session_refresh_disabled",
                                                       "tags": ["PARSE_CLI"],
                                                       "link": self.link.check_webauth_session_refresh_disabled}
        self.CHECK_WEBAUTH_SESSION_REFRESH_ENABLED = {"constant": "check_webauth_session_refresh_enabled",
                                                      "tags": ["PARSE_CLI"],
                                                      "link": self.link.check_webauth_session_refresh_enabled}
        self.CHECK_WEBAUTH_SESSION_REFRESH_INTERVAL = {"constant": "check_webauth_session_refresh_interval",
                                                       "tags": ["PARSE_CLI"],
                                                       "link": self.link.check_webauth_session_refresh_interval}
        self.CHECK_WEBAUTH_SESSION_TIMEOUT = {"constant": "check_webauth_session_timeout",
                                              "tags": ["PARSE_CLI"],
                                              "link": self.link.check_webauth_session_timeout}
        self.CHECK_WEBAUTH_SESSION_TIMEOUT_DEFAULT = {"constant": "check_webauth_session_timeout_default",
                                                      "tags": ["PARSE_CLI"],
                                                      "link": self.link.check_webauth_session_timeout_default}
        self.CHECK_WEBAUTH_USER_AUTHENTICATED = {"constant": "check_webauth_user_authenticated",
                                                 "tags": ["PARSE_CLI"],
                                                 "link": self.link.check_webauth_user_authenticated}
        self.CHECK_WEBAUTH_USER_AUTHENTICATED_AUTH_TYPE = {"constant": "check_webauth_user_authenticated_auth_type",
                                                           "tags": ["PARSE_CLI"],
                                                           "link": self.link.check_webauth_user_authenticated_auth_type}
        self.CHECK_WEBAUTH_USER_AUTHENTICATED_RADIUS = {"constant": "check_webauth_user_authenticated_radius",
                                                        "tags": ["PARSE_CLI"],
                                                        "link": self.link.check_webauth_user_authenticated_radius}
        self.CHECK_WEBAUTH_USER_IP = {"constant": "check_webauth_user_ip",
                                      "tags": ["PARSE_CLI"],
                                      "link": self.link.check_webauth_user_ip}
        self.CHECK_WEBAUTH_USER_LOGIN_NAME = {"constant": "check_webauth_user_login_name",
                                              "tags": ["PARSE_CLI"],
                                              "link": self.link.check_webauth_user_login_name}
        self.CHECK_WEBAUTH_USER_UNAUTHENTICATED = {"constant": "check_webauth_user_unauthenticated",
                                                   "tags": ["PARSE_CLI"],
                                                   "link": self.link.check_webauth_user_unauthenticated}
        self.VERIFY_WEBAUTH_PORT_STATE = {"constant": "verify_webauth_port_state",
                                          "tags": ["PARSE_CLI"],
                                          "link": self.link.verify_webauth_port_state}
