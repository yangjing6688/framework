"""
Keyword class for all upm cli commands.
"""
from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import NetworkElementKeywordBaseClass
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.Constants.UpmConstants import \
    UpmConstants as ParseConstants
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.Constants.UpmConstants import \
    UpmConstants as CommandConstants
# All imports above this line will be removed after generation.
# User imports must be added below.


class NetworkElementUpmGenKeywords(NetworkElementKeywordBaseClass):
    def __init__(self):
        super(NetworkElementUpmGenKeywords, self).__init__()
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()
        self.api_const = "upm"

    def upm_set_auth(self, device_name, auth_profile='', ports='', **kwargs):
        """
        Description: Configures an authenticated UPM event on specified profile and ports.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "auth_profile": auth_profile,
            "ports": ports
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_AUTH,
                                    **kwargs)

    def upm_set_unauth(self, device_name, auth_profile='', ports='', **kwargs):
        """
        Description: Configures an unauthenticated UPM event on specified profile and ports.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "auth_profile": auth_profile,
            "ports": ports
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_UNAUTH,
                                    **kwargs)

    def upm_set_profile(self, device_name, profile='', lines='', **kwargs):
        """
        Description: Creates a upm profile with desired name and command lines.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "lines": lines,
            "profile": profile
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PROFILE,
                                    list_value_arg=True,
                                    wait_for_prompt=False,
                                    **kwargs)

    def upm_clear_auth(self, device_name, auth_profile='', ports='', **kwargs):
        """
        Description: UnConfigures an authenticated UPM event on specified profile and ports.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "auth_profile": auth_profile,
            "ports": ports
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_AUTH,
                                    **kwargs)

    def upm_clear_unauth(self, device_name, auth_profile='', ports='', **kwargs):
        """
        Description: all.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "auth_profile": auth_profile,
            "ports": ports
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_UNAUTH,
                                    **kwargs)

    def upm_clear_auth_all_ports(self, device_name, auth_profile='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "auth_profile": auth_profile
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_AUTH_ALL_PORTS,
                                    **kwargs)

    def upm_clear_unauth_all_ports(self, device_name, auth_profile='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "auth_profile": auth_profile
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_UNAUTH_ALL_PORTS,
                                    **kwargs)

    def upm_clear_profile(self, device_name, profile='', **kwargs):
        """
        Description: Deletes a specified upm profile.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "profile": profile
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_PROFILE,
                                    **kwargs)

    # ##################################################################################################################
    #   Inspection Keywords   ##########################################################################################
    # ##################################################################################################################

    def upm_verify_authenticate_event_exists(self, device_name, auth_profile='', ports='', **kwargs):
        """
        Keyword Arguments:
        [device_name]  - The device the keyword should be run against.
        [auth_profile] - The name of the auth profile to configure upm on.
        [ports]        - The port(s) to enable upm on.

        Verifies that a upm event exists.
        """
        args = {"auth_profile": auth_profile,
                "ports": ports}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_EVENT_AUTHENTICATE,
                                           self.parse_const.CHECK_UPM_AUTHENTICATE_PROFILE_PORTS, True,
                                           "Upm authenticate event {auth_profile} exists on {ports}.",
                                           "Upm authenticate event {auth_profile} DOES NOT exist on {ports}!",
                                           **kwargs)

    def upm_verify_authenticate_event_does_not_exist(self, device_name, auth_profile='', ports='', **kwargs):
        """
        Keyword Arguments:
        [device_name]  - The device the keyword should be run against.
        [auth_profile] - The name of the auth profile to configure upm on.
        [ports]        - The port(s) to enable upm on.

        Verifies that a upm event does not exist.
        """
        args = {"auth_profile": auth_profile,
                "ports": ports}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_EVENT_AUTHENTICATE,
                                           self.parse_const.CHECK_UPM_AUTHENTICATE_PROFILE_PORTS, False,
                                           "Upm authenticate event {auth_profile} does not exist on {ports}.",
                                           "Upm authenticate event {auth_profile} EXISTS on {ports}!",
                                           **kwargs)

    def upm_verify_unauthenticated_event_exists(self, device_name, auth_profile='', ports='', **kwargs):
        """
        Keyword Arguments:
        [device_name]  - The device the keyword should be run against.
        [auth_profile] - The name of the auth profile to configure upm on.
        [ports]        - The port(s) to enable upm on.

        Verifies that a upm unauthenticated event exists.
        """
        args = {"auth_profile": auth_profile,
                "ports": ports}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_EVENT_UNAUTHENTICATED,
                                           self.parse_const.CHECK_UPM_UNAUTHENTICATED_PROFILE_PORTS, True,
                                           "Upm unauthenticated event {auth_profile} exists on {ports}.",
                                           "Upm unauthenticated event {auth_profile} DOES NOT exist on {ports}!",
                                           **kwargs)

    def upm_verify_unauthenticated_event_does_not_exist(self, device_name, auth_profile='', ports='', **kwargs):
        """
        Keyword Arguments:
        [device_name]  - The device the keyword should be run against.
        [auth_profile] - The name of the auth profile to configure upm on.
        [ports]        - The port(s) to enable upm on.

        Verifies that a upm unauthenticated event does not exist.
        """
        args = {"auth_profile": auth_profile,
                "ports": ports}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_EVENT_UNAUTHENTICATED,
                                           self.parse_const.CHECK_UPM_UNAUTHENTICATED_PROFILE_PORTS, False,
                                           "Upm unauthenticated event {auth_profile} does not exist on {ports}.",
                                           "Upm unauthenticated event {auth_profile} EXISTS on {ports}!",
                                           **kwargs)
