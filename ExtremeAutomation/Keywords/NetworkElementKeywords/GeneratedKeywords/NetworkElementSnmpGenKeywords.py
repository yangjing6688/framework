"""
Keyword class for all snmp cli commands.
"""
from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import NetworkElementKeywordBaseClass
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.Constants.SnmpConstants import \
    SnmpConstants as ParseConstants
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.Constants.SnmpConstants import \
    SnmpConstants as CommandConstants
# All imports above this line will be removed after generation.
# User imports must be added below.


class NetworkElementSnmpGenKeywords(NetworkElementKeywordBaseClass):
    def __init__(self):
        super(NetworkElementSnmpGenKeywords, self).__init__()
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()
        self.api_const = "snmp"

    def snmp_create_all_trap_server(self, device_name, ip_address='', server_name='', param_name='', tag_list='',
                                    community='', **kwargs):
        """
        Description: Configures the specified SNMP trap server.

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "community": community,
            "ip_address": ip_address,
            "param_name": param_name,
            "server_name": server_name,
            "tag_list": tag_list
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CREATE_ALL_TRAP_SERVER,
                                    **kwargs)

    def snmp_delete_trap_servers(self, device_name, ip_address='', server_name='', **kwargs):
        """
        Description: Removes the specified SNMP trap server.

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "ip_address": ip_address,
            "server_name": server_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DELETE_TRAP_SERVERS,
                                    **kwargs)

    def snmp_create_readonly_community(self, device_name, community_index='', community_name='', security_name='',
                                       context='', **kwargs):
        """
        Description: Creates a read only SNMP community name.

        Supported Agents and OS:
            CLI: EXOS, VOSS
        """
        args = {
            "community_index": community_index,
            "community_name": community_name,
            "context": context,
            "security_name": security_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CREATE_READONLY_COMMUNITY,
                                    **kwargs)

    def snmp_create_readwrite_community(self, device_name, community_index='', community_name='', security_name='',
                                        context='', **kwargs):
        """
        Description: Creates a read write SNMP community name.

        Supported Agents and OS:
            CLI: EXOS, VOSS
        """
        args = {
            "community_index": community_index,
            "community_name": community_name,
            "context": context,
            "security_name": security_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CREATE_READWRITE_COMMUNITY,
                                    **kwargs)

    def snmp_delete_community(self, device_name, community_name='', **kwargs):
        """
        Description: Removes an SNMP community entry.

        Supported Agents and OS:
            CLI: EXOS, VOSS
        """
        args = {
            "community_name": community_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DELETE_COMMUNITY,
                                    **kwargs)

    def snmp_delete_user(self, device_name, user_name='', **kwargs):
        """
        Description: Removes an SNMP user.

        Supported Agents and OS:
            CLI: EXOS, VOSS
        """
        args = {
            "user_name": user_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DELETE_USER,
                                    **kwargs)

    def snmp_set_user_no_authentication(self, device_name, user_name='', group='', **kwargs):
        """
        Description: Creates an SNMP user without authentication and without privacy.

        Supported Agents and OS:
            CLI: EXOS, VOSS
        """
        args = {
            "group": group,
            "user_name": user_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_USER_NO_AUTHENTICATION,
                                    **kwargs)

    def snmp_set_user_authentication(self, device_name, user_name='', auth_proto='', auth_password='', group='',
                                     **kwargs):
        """
        Description: Creates an SNMP user with authentication only.

        Supported Agents and OS:
            CLI: EXOS, VOSS
        """
        args = {
            "auth_password": auth_password,
            "auth_proto": auth_proto,
            "group": group,
            "user_name": user_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_USER_AUTHENTICATION,
                                    **kwargs)

    def snmp_set_user_privacy(self, device_name, user_name='', auth_proto='', auth_password='', priv_proto='',
                              priv_password='', group='', **kwargs):
        """
        Description: Creates an SNMP user with authentication and privacy.

        Supported Agents and OS:
            CLI: EXOS, VOSS
        """
        args = {
            "auth_password": auth_password,
            "auth_proto": auth_proto,
            "group": group,
            "priv_password": priv_password,
            "priv_proto": priv_proto,
            "user_name": user_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_USER_PRIVACY,
                                    **kwargs)

    def snmp_set_user_no_authentication_engine_id(self, device_name, engine_id='', user_name='', group='', **kwargs):
        """
        Description: Set user with no auth and engine id.

        Supported Agents and OS:
            CLI: EXOS, VOSS
        """
        args = {
            "engine_id": engine_id,
            "group": group,
            "user_name": user_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_USER_NO_AUTHENTICATION_ENGINE_ID,
                                    **kwargs)

    def snmp_set_user_authentication_engine_id(self, device_name, auth_password='', auth_proto='', engine_id='',
                                               user_name='', group='', **kwargs):
        """
        Description: Set user with auth and engine id.

        Supported Agents and OS:
            CLI: EXOS, VOSS
        """
        args = {
            "auth_password": auth_password,
            "auth_proto": auth_proto,
            "engine_id": engine_id,
            "group": group,
            "user_name": user_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_USER_AUTHENTICATION_ENGINE_ID,
                                    **kwargs)

    def snmp_set_user_privacy_engine_id(self, device_name, auth_password='', auth_proto='', engine_id='',
                                        priv_password='', priv_proto='', user_name='', group='', **kwargs):
        """
        Description: Set user privacy with engine id.

        Supported Agents and OS:
            CLI: EXOS, VOSS
        """
        args = {
            "auth_password": auth_password,
            "auth_proto": auth_proto,
            "engine_id": engine_id,
            "group": group,
            "priv_password": priv_password,
            "priv_proto": priv_proto,
            "user_name": user_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_USER_PRIVACY_ENGINE_ID,
                                    **kwargs)

    def snmp_enable_access_global(self, device_name, **kwargs):
        """
        Description: Globally enables SNMP for v1 v2c and v3..

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_ACCESS_GLOBAL,
                                    **kwargs)

    def snmp_disable_access_global(self, device_name, **kwargs):
        """
        Description: Globally disables SNMP for v1 v2c and v3..

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_ACCESS_GLOBAL,
                                    **kwargs)

    def snmp_set_trap_param(self, device_name, param_name='', community='', version='', **kwargs):
        """
        Description: Set snmp trap param.

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "community": community,
            "param_name": param_name,
            "version": version
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_TRAP_PARAM,
                                    **kwargs)

    def snmp_clear_trap_param(self, device_name, param_name='', **kwargs):
        """
        Description: Removes the specified SNMP target parameters.

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "param_name": param_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_TRAP_PARAM,
                                    **kwargs)

    def snmp_set_notify(self, device_name, notify_name='', _type='', **kwargs):
        """
        Description: Creates a notify entry.

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "notify_name": notify_name,
            "type": _type
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_NOTIFY,
                                    **kwargs)

    def snmp_clear_notify(self, device_name, notify_name='', **kwargs):
        """
        Description: Removes the specified SNMP notify.

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "notify_name": notify_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_NOTIFY,
                                    **kwargs)

    def snmp_enable_authentication_trap(self, device_name, **kwargs):
        """
        Description: Enables the sending of SNMP authentication traps.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_AUTHENTICATION_TRAP,
                                    **kwargs)

    def snmp_disable_authentication_trap(self, device_name, **kwargs):
        """
        Description: Disables the sending of SNMP authentication traps.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_AUTHENTICATION_TRAP,
                                    **kwargs)

    def snmp_enable_same_snmp_and_ip_sender_flag(self, device_name, **kwargs):
        """
        Description: Enables using the same IP for SNMP as the IP sender..

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_SAME_SNMP_AND_IP_SENDER_FLAG,
                                    **kwargs)

    def snmp_disable_same_snmp_and_ip_sender_flag(self, device_name, **kwargs):
        """
        Description: Disables using the same IP for SNMP as the IP sender..

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_SAME_SNMP_AND_IP_SENDER_FLAG,
                                    **kwargs)

    def snmp_enable_same_snmp_trap_sender_ip(self, device_name, **kwargs):
        """
        Description: Enables using the same IP for SNMP traps as the IP sender..

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_SAME_SNMP_TRAP_SENDER_IP,
                                    **kwargs)

    def snmp_disable_same_snmp_trap_sender_ip(self, device_name, **kwargs):
        """
        Description: Disables using the same IP for SNMP traps as the IP sender..

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_SAME_SNMP_TRAP_SENDER_IP,
                                    **kwargs)

    def snmp_create_v1_trap_server(self, device_name, ip_addr='', security_name='', port='', **kwargs):
        """
        Description: Configures the specified SNMP v1 trap server that the device will send v1 traps to.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "ip_addr": ip_addr,
            "port": port,
            "security_name": security_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CREATE_V1_TRAP_SERVER,
                                    **kwargs)

    def snmp_delete_v1_trap_server(self, device_name, ip_addr='', security_name='', port='', **kwargs):
        """
        Description: Deletes the specified v1 trap server.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "ip_addr": ip_addr,
            "port": port,
            "security_name": security_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DELETE_V1_TRAP_SERVER,
                                    **kwargs)

    def snmp_create_v2c_trap_server(self, device_name, ip_addr='', security_name='', port='', **kwargs):
        """
        Description: Configures the specified SNMP v2c trap server where the device will send v2c traps to.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "ip_addr": ip_addr,
            "port": port,
            "security_name": security_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CREATE_V2C_TRAP_SERVER,
                                    **kwargs)

    def snmp_delete_v2c_trap_server(self, device_name, ip_addr='', security_name='', port='', **kwargs):
        """
        Description: Deletes the specified v2c trap server.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "ip_addr": ip_addr,
            "port": port,
            "security_name": security_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DELETE_V2C_TRAP_SERVER,
                                    **kwargs)

    def snmp_create_v2c_inform_server(self, device_name, ip_addr='', security_name='', port='', timeout='', retries='',
                                      mms='', **kwargs):
        """
        Description: Configures the specified SNMP v2c inform server where the device will send v2c informs to.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "ip_addr": ip_addr,
            "mms": mms,
            "port": port,
            "retries": retries,
            "security_name": security_name,
            "timeout": timeout
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CREATE_V2C_INFORM_SERVER,
                                    **kwargs)

    def snmp_delete_v2c_inform_server(self, device_name, ip_addr='', security_name='', **kwargs):
        """
        Description: Deletes the specified v2c inform server.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "ip_addr": ip_addr,
            "security_name": security_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DELETE_V2C_INFORM_SERVER,
                                    **kwargs)

    def snmp_create_v3_trap_server(self, device_name, ip_addr='', security_name='', security_level='', port='',
                                   **kwargs):
        """
        Description: Configures the specified SNMP 3 trap server where the device will send v3 traps to.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "ip_addr": ip_addr,
            "port": port,
            "security_level": security_level,
            "security_name": security_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CREATE_V3_TRAP_SERVER,
                                    **kwargs)

    def snmp_delete_v3_trap_server(self, device_name, ip_addr='', security_name='', port='', **kwargs):
        """
        Description: Deletes the specified v3 trap server.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "ip_addr": ip_addr,
            "port": port,
            "security_name": security_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DELETE_V3_TRAP_SERVER,
                                    **kwargs)

    def snmp_create_v3_inform_server(self, device_name, ip_addr='', security_name='', security_level='', port='',
                                     timeout='', retries='', **kwargs):
        """
        Description: Configures the specified SNMP v3 inform server where the device will send v3 informs to.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "ip_addr": ip_addr,
            "port": port,
            "retries": retries,
            "security_level": security_level,
            "security_name": security_name,
            "timeout": timeout
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CREATE_V3_INFORM_SERVER,
                                    **kwargs)

    def snmp_delete_v3_inform_server(self, device_name, ip_addr='', security_name='', **kwargs):
        """
        Description: Deletes the specified v3 inform server.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "ip_addr": ip_addr,
            "security_name": security_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DELETE_V3_INFORM_SERVER,
                                    **kwargs)

    def snmp_set_notify_filter(self, device_name, profile_name='', oid_tree='', **kwargs):
        """
        Description: Creates a notify filter entry.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "oid_tree": oid_tree,
            "profile_name": profile_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_NOTIFY_FILTER,
                                    **kwargs)

    def snmp_clear_notify_filter(self, device_name, profile_name='', oid_tree='', **kwargs):
        """
        Description: Deletes a notify filter entry.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "oid_tree": oid_tree,
            "profile_name": profile_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_NOTIFY_FILTER,
                                    **kwargs)

    def snmp_delete_user_engine_id(self, device_name, engine_id='', user_name='', **kwargs):
        """
        Description: Delete user engine id.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "engine_id": engine_id,
            "user_name": user_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DELETE_USER_ENGINE_ID,
                                    **kwargs)

    def snmp_create_group_and_access(self, device_name, group='', security_level='', read_view='', write_view='',
                                     notify_view='', context='', **kwargs):
        """
        Description: Creates an SNMP group and access table. VOSS creates both group and access entries in one
                     command.VOSS also does not include the security_name in the group table as this is handled in the
                     user table..

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "context": context,
            "group": group,
            "notify_view": notify_view,
            "read_view": read_view,
            "security_level": security_level,
            "write_view": write_view
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CREATE_GROUP_AND_ACCESS,
                                    **kwargs)

    def snmp_delete_group_and_access(self, device_name, group='', context='', **kwargs):
        """
        Description: Removes an SNMP group and access table. VOSS creates and deletes both group and access entries in
                     one command..

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "context": context,
            "group": group
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DELETE_GROUP_AND_ACCESS,
                                    **kwargs)

    def snmp_create_view(self, device_name, view_name='', oid_tree='', **kwargs):
        """
        Description: Creates a view entry for access to the tree.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "oid_tree": oid_tree,
            "view_name": view_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CREATE_VIEW,
                                    **kwargs)

    def snmp_delete_view(self, device_name, view_name='', oid_tree='', **kwargs):
        """
        Description: Deletes a view entry.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "oid_tree": oid_tree,
            "view_name": view_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DELETE_VIEW,
                                    **kwargs)

    # ##################################################################################################################
    #   Inspection Keywords   ##########################################################################################
    # ##################################################################################################################

    def snmp_verify_enabled(self, device_name, vr="VR-Default", **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vr]          - The VR that is being checked if snmp is enabled. Set to VR-Default by default.

        Verifies that SNMP is enabled on the provided VR.
        """
        args = {"vr": vr}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SNMP,
                                           self.parse_const.VERIFY_SNMP_ENABLED, True,
                                           "SNMP is enabled.", "SNMP is disabled.",
                                           **kwargs)

    def snmp_verify_disabled(self, device_name, vr="VR-Default", **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vr] -          The VR that is being checked if snmp is enabled. Set to VR-Default by default.

        Verifies that SNMP is disabled on the provided VR.
        """
        args = {"vr": vr}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SNMP,
                                           self.parse_const.VERIFY_SNMP_ENABLED, False,
                                           "SNMP is disabled.", "SNMP is enabled.",
                                           **kwargs)

    def snmp_verify_notify_filter(self, device_name, profile_name='', oid_tree='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [profile_name] - The name of the filter profile to be used when generating notifications.
        [oid_tree]     - The MIB subtree which defines a subtree to be included or excluded.
                         Example:  +1.3.6.1.6.3.1.1.4.1 to include and -1.3.6.1.6.3.1.1.4.1 to exclude.

        Verifies the presence of a notify filter entry with the correct OID tree.
        """
        args = {"profile_name": profile_name,
                "oid_tree": oid_tree}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SNMP_NOTIFY_FILTER,
                                           self.parse_const.CHECK_SNMP_NOTIFY_FILTER, True,
                                           "SNMP notify filter {profile_name} has the correct oid_tree.",
                                           "SNMP notify filter {profile_name} does NOT have the correct "
                                           "OID tree!",
                                           **kwargs)

    def snmp_verify_authentication_trap_enabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.

        Verifies that SNMP authentication traps is enabled.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SNMP_GLOBALS,
                                           self.parse_const.CHECK_SNMP_ENABLE_AUTHENTICATION_TRAP, True,
                                           "SNMP authentication trap is enabled.",
                                           "SNMP authentication trap is NOT enabled!",
                                           **kwargs)

    def snmp_verify_authentication_trap_disabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.

        Verifies that SNMP authentication traps is disabled.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SNMP_GLOBALS,
                                           self.parse_const.CHECK_SNMP_ENABLE_AUTHENTICATION_TRAP, False,
                                           "SNMP authentication trap is disabled.",
                                           "SNMP authentication trap is NOT disabled!",
                                           **kwargs)

    def snmp_verify_same_ip_as_ip_sender_enabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.

        Verifies that the flag for SNMP using the same IP as the IP sender is enabled.
        VOSS only.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SNMP_GLOBALS,
                                           self.parse_const.CHECK_SNMP_ENABLE_SAME_SNMP_AND_IP_SENDER_FLAG, True,
                                           "Flag for SNMP to use the same IP as the IP sender is enabled.",
                                           "Flag for SNMP to use the same IP as the IP sender NOT enabled!",
                                           **kwargs)

    def snmp_verify_same_ip_as_ip_sender_disabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.

        Verifies that the flag for SNMP using the same IP as the IP sender is disabled.
        VOSS only.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SNMP_GLOBALS,
                                           self.parse_const.CHECK_SNMP_ENABLE_SAME_SNMP_AND_IP_SENDER_FLAG, False,
                                           "Flag for SNMP to use the same IP as the IP sender is disabled.",
                                           "Flag for SNMP to use the same IP as the IP sender NOT disabled!",

                                           **kwargs)

    def snmp_verify_same_trap_ip_as_ip_sender_enabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.

        Verifies that the flag for SNMP traps using the same IP as the IP sender is enabled.
        VOSS only.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SNMP_GLOBALS,
                                           self.parse_const.CHECK_SNMP_ENABLE_SAME_SNMP_TRAP_SENDER_IP, True,
                                           "Flag for SNMP traps to use the same IP as the IP sender is enabled.",
                                           "Flag for SNMP traps to use the same IP as the IP sender NOT enabled!",
                                           **kwargs)

    def snmp_verify_same_trap_ip_as_ip_sender_disabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.

        Verifies that the flag for SNMP traps using the same IP as the IP sender is disabled.
        VOSS only.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SNMP_GLOBALS,
                                           self.parse_const.CHECK_SNMP_ENABLE_SAME_SNMP_TRAP_SENDER_IP, False,
                                           "Flag for SNMP traps to use the same IP as the IP sender "
                                           "is disabled.",
                                           "Flag for SNMP traps to use the same IP as the IP sender "
                                           "NOT disabled!",
                                           **kwargs)

    def snmp_verify_v1_trap_server_exists(self, device_name, ip_addr='', security_name="initialview", port="162",
                                          **kwargs):
        """
        [device_name]     - The device the keyword will be run against.
        [ip_addr]         - The IP Address of the trap server.
        [security_name]   - The SNMP security name that maps to the community name. It is not necessarily
                            the same as the community name.  For SNMP v1 and v2 it can be "readview" or "initialview".
                            For SNMP V3 USM it is the user name.  Default is initialview.
        [port]            - The transport layer port number.  Default is 162.

        Verifies that the specified SNMP v1 trap server exists.
        """
        args = {"ip_addr": ip_addr,
                "security_name": security_name,
                "port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SNMP_HOST,
                                           self.parse_const.CHECK_SNMP_V1_TRAP_SERVER, True,
                                           "SNMP v1 trap server {ip_addr} exists.",
                                           "SNMP v1 trap server {ip_addr} does NOT exist!",
                                           **kwargs)

    def snmp_verify_v1_trap_server_does_not_exist(self, device_name, ip_addr='', security_name="initialview",
                                                  port="162", **kwargs):
        """
        [device_name]     - The device the keyword will be run against.
        [ip_addr]         - The IP Address of the trap server.
        [security_name]   - The SNMP security name that maps to the community name. It is not necessarily
                            the same as the community name.  For SNMP v1 and v2 it can be "readview" or "initialview".
                            For SNMP V3 USM it is the user name.  Default is initialview.
        [port]            - The transport layer port number.  Default is 162.

        Verifies that the specified SNMP v1 trap server does not exist.
        """
        args = {"ip_addr": ip_addr,
                "security_name": security_name,
                "port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SNMP_HOST,
                                           self.parse_const.CHECK_SNMP_V1_TRAP_SERVER, False,
                                           "SNMP v1 trap server {ip_addr} does not exist.",
                                           "SNMP v1 trap server {ip_addr} exists!",
                                           **kwargs)

    def snmp_verify_v2c_trap_server_exists(self, device_name, ip_addr='', security_name="initialview", port="162",
                                           **kwargs):
        """
        [device_name]     - The device the keyword will be run against.
        [ip_addr]         - The IP Address of the trap server.
        [security_name]   - The SNMP security name that maps to the community name. It is not necessarily
                            the same as the community name.  For SNMP v1 and v2 it can be "readview" or "initialview".
                            For SNMP V3 USM it is the user name.  Default is initialview.
        [port]            - The transport layer port number.  Default is 162.

        Verifies that the specified SNMP v2c trap server exists.
        """
        args = {"ip_addr": ip_addr,
                "security_name": security_name,
                "port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SNMP_HOST,
                                           self.parse_const.CHECK_SNMP_V2C_TRAP_SERVER, True,
                                           "SNMP v2c trap server {ip_addr} exists.",
                                           "SNMP v2c trap server {ip_addr} does NOT exist!",
                                           **kwargs)

    def snmp_verify_v2c_trap_server_does_not_exist(self, device_name, ip_addr='', security_name="initialview",
                                                   port="162", **kwargs):
        """
        [device_name]     - The device the keyword will be run against.
        [ip_addr]         - The IP Address of the trap server.
        [security_name]   - The SNMP security name that maps to the community name. It is not necessarily
                            the same as the community name.  For SNMP v1 and v2 it can be "readview" or "initialview".
                            For SNMP V3 USM it is the user name.  Default is initialview.
        [port]            - The transport layer port number.  Default is 162.

        Verifies that the specified SNMP v2c trap server does not exist.
        """
        args = {"ip_addr": ip_addr,
                "security_name": security_name,
                "port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SNMP_HOST,
                                           self.parse_const.CHECK_SNMP_V2C_TRAP_SERVER, False,
                                           "SNMP v2c trap server {ip_addr} does not exist.",
                                           "SNMP v2c trap server {ip_addr} exists!",
                                           **kwargs)

    def snmp_verify_v2c_inform_server_exists(self, device_name, ip_addr='', security_name="initialview", timeout="1500",
                                             port="162", **kwargs):
        """
        [device_name]     - The device the keyword will be run against.
        [ip_addr]         - The IP Address of the trap server.
        [security_name]   - The SNMP security name that maps to the community name. It is not necessarily
                            the same as the community name.  For SNMP v1 and v2 it can be "readview" or "initialview".
                            For SNMP V3 USM it is the user name.  Default is initialview.
        [timeout]         - Timeout between retransmission.
        [port]            - The transport layer port number.  Default is 162.

        Verifies that the specified SNMP v2c inform server exists.
        """
        args = {"ip_addr": ip_addr,
                "security_name": security_name,
                "timeout": timeout,
                "port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SNMP_HOST,
                                           self.parse_const.CHECK_SNMP_V2C_INFORM_SERVER, True,
                                           "SNMP v2c inform server {ip_addr} exists.",
                                           "SNMP v2c inform server {ip_addr} does NOT exist!",
                                           **kwargs)

    def snmp_verify_v2c_inform_server_does_not_exist(self, device_name, ip_addr='', security_name="initialview",
                                                     timeout="1500", port="162", **kwargs):
        """
        [device_name]     - The device the keyword will be run against.
        [ip_addr]         - The IP Address of the trap server.
        [security_name]   - The SNMP security name that maps to the community name. It is not necessarily
                            the same as the community name.  For SNMP v1 and v2 it can be "readview" or "initialview".
                            For SNMP V3 USM it is the user name.  Default is initialview.
        [timeout]         - Timeout between retransmission.
        [port]            - The transport layer port number.  Default is 162.

        Verifies that the specified SNMP v2c inform server does not exist.
        """
        args = {"ip_addr": ip_addr,
                "security_name": security_name,
                "timeout": timeout,
                "port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SNMP_HOST,
                                           self.parse_const.CHECK_SNMP_V2C_INFORM_SERVER, False,
                                           "SNMP v2c inform server {ip_addr} does not exist.",
                                           "SNMP v2c inform server {ip_addr} exists!",
                                           **kwargs)

    def snmp_verify_v3_trap_server_exists(self, device_name, ip_addr='', security_name='', security_level='',
                                          port="162", **kwargs):
        """
        [device_name]     - The device the keyword will be run against.
        [ip_addr]         - The IP Address of the trap server.
        [security_name]   - The  SNMP V3 USM  user name.
        [security_level]  - The security level in which the message is sent.
                            Valid values are:   noAuthNoPriv, authNoPriv, or authPriv
        [port]            - The transport layer port number.  Default is 162.

        Verifies that the specified SNMP v3 trap server exists.
        """
        args = {"ip_addr": ip_addr,
                "security_name": security_name,
                "security_level": security_level,
                "port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SNMP_HOST,
                                           self.parse_const.CHECK_SNMP_V3_TRAP_SERVER, True,
                                           "SNMP v3 trap server {ip_addr} exists.",
                                           "SNMP v3 trap server {ip_addr} does NOT exist!",
                                           **kwargs)

    def snmp_verify_v3_trap_server_does_not_exist(self, device_name, ip_addr='', security_name='', security_level='',
                                                  port="162", **kwargs):
        """
        [device_name]     - The device the keyword will be run against.
        [ip_addr]         - The IP Address of the trap server.
        [security_name]   - The  SNMP V3 USM  user name.
        [security_level]  - The security level in which the message is sent.
                            Valid values are:   noAuthNoPriv, authNoPriv, or authPriv
        [port]            - The transport layer port number.  Default is 162.

        Verifies that the specified SNMP v3 trap server does not exist.
        """
        args = {"ip_addr": ip_addr,
                "security_name": security_name,
                "security_level": security_level,
                "port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SNMP_HOST,
                                           self.parse_const.CHECK_SNMP_V3_TRAP_SERVER, False,
                                           "SNMP v3 trap server {ip_addr} does not exist.",
                                           "SNMP v3 trap server {ip_addr} exists!",
                                           **kwargs)

    def snmp_verify_v3_inform_server_exists(self, device_name, ip_addr='', security_name='', security_level='',
                                            timeout="1500", port="162", **kwargs):
        """
        [device_name]     - The device the keyword will be run against.
        [ip_addr]         - The IP Address of the trap server.
        [security_name]   - The  SNMP V3 USM  user name.
        [security_level]  - The security level in which the message is sent.
                            Valid values are:   noAuthNoPriv, authNoPriv, or authPriv
        [timeout]         - Timeout between retransmission.
        [port]            - The transport layer port number.  Default is 162.

        Verifies that the specified SNMP v3 trap server exists.
        """
        args = {"ip_addr": ip_addr,
                "security_name": security_name,
                "security_level": security_level,
                "timeout": timeout,
                "port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SNMP_HOST,
                                           self.parse_const.CHECK_SNMP_V3_INFORM_SERVER, True,
                                           "SNMP v3 inform server {ip_addr} exists.",
                                           "SNMP v3 inform server {ip_addr} does NOT exist!",
                                           **kwargs)

    def snmp_verify_v3_inform_server_does_not_exist(self, device_name, ip_addr='', security_name='', security_level='',
                                                    timeout="1500", port="162", **kwargs):
        """
        [device_name]     - The device the keyword will be run against.
        [ip_addr]         - The IP Address of the trap server.
        [security_name]   - The  SNMP V3 USM  user name.
        [security_level]  - The security level in which the message is sent.
                            Valid values are:   noAuthNoPriv, authNoPriv, or authPriv
        [timeout]         - Timeout between retransmission.
        [port]            - The transport layer port number.  Default is 162.

        Verifies that the specified SNMP v3 trap server does not exist.
        """
        args = {"ip_addr": ip_addr,
                "security_name": security_name,
                "security_level": security_level,
                "timeout": timeout,
                "port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SNMP_HOST,
                                           self.parse_const.CHECK_SNMP_V3_INFORM_SERVER, False,
                                           "SNMP v3 trap server {ip_addr} does not exist.",
                                           "SNMP v3 trap server {ip_addr} exists!",
                                           **kwargs)

    def snmp_verify_community_exists(self, device_name, community_index='', security_name="", community_name="",
                                     **kwargs):
        """
        [device_name]           - The device the keyword will be run against.
        [community_index]       - The SNMP community index which is a text string representing the entry.
        [community_name]        - The actual community name that is used in SNMP messages.
        [security_name]         - The security name that maps to the community name for read only.
                                  For VOSS use: readview
                                  For EXOS use: v1v2c_ro

        Verifies that the specified SNMP community entry exists.
        Note:  In most applications the community name is encrypted for security reasons
               but it is present here in the keyword for reporting purposes.
        """
        args = {"community_index": community_index,
                "security_name": security_name,
                "community_name": community_name}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SNMP_COMMUNITY,
                                           self.parse_const.CHECK_SNMP_COMMUNITY, True,
                                           "SNMP community name {community_name} exists.",
                                           "SNMP community name {community_name} does NOT exist!",
                                           **kwargs)

    def snmp_verify_community_does_not_exist(self, device_name, community_index='', security_name="", community_name="",
                                             **kwargs):
        """
        [device_name]           - The device the keyword will be run against.
        [community_index]       - The SNMP community index which is a text string representing the entry.
        [community_name]        - The actual community name that is used in SNMP messages.
        [security_name]         - The security name that maps to the community name for read only.
                                  For VOSS use: readview
                                  For EXOS use: v1v2c_ro

        Verifies that the specified SNMP community entry does not exist.
        Note:  In most applications the community name is encrypted for security reasons
               but it is present here in the keyword for reporting purposes.
        """
        args = {"community_index": community_index,
                "security_name": security_name,
                "community_name": community_name}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SNMP_COMMUNITY,
                                           self.parse_const.CHECK_SNMP_COMMUNITY, False,
                                           "SNMP community name {community_name} does not exist.",
                                           "SNMP community name {community_name} exists!",
                                           **kwargs)

    def snmp_verify_user_exists(self, device_name, user_name='', **kwargs):
        """
        [device_name]   - The device the keyword will be run against.
        [user_name]     - The SNMP user name that has authentication parameters. It is the same as security_name.

        Verifies that the specified SNMP v3 USM user entry exists.
        """
        args = {"user_name": user_name}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SNMP_USER,
                                           self.parse_const.CHECK_SNMP_USER, True,
                                           "SNMP user {user_name} exists.",
                                           "SNMP user {user_name} does NOT exist!",
                                           **kwargs)

    def snmp_verify_user_does_not_exist(self, device_name, user_name='', **kwargs):
        """
        [device_name]   - The device the keyword will be run against.
        [user_name]     - The SNMP user name that has authentication parameters. It is the same as security_name.

        Verifies that the specified SNMP v3 USM user entry does not exist.
        """
        args = {"user_name": user_name}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SNMP_USER,
                                           self.parse_const.CHECK_SNMP_USER, False,
                                           "SNMP user {user_name} does not exist.",
                                           "SNMP user {user_name} exists!",
                                           **kwargs)

    def snmp_verify_group_exists(self, device_name, group='', **kwargs):
        """
        [device_name]   - The device the keyword will be run against.
        [group]         - The group in which which the users belong to.

        Verifies that the specified SNMP group entry exists.
        """
        args = {"group": group}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SNMP_GROUP,
                                           self.parse_const.CHECK_SNMP_GROUP, True,
                                           "SNMP group {group} exists.",
                                           "SNMP group {group} does NOT exist!",
                                           **kwargs)

    def snmp_verify_group_does_not_exist(self, device_name, group='', **kwargs):
        """
        [device_name]   - The device the keyword will be run against.
        [group]         - The group in which which the users belong to.

        Verifies that the specified SNMP group exists.
        """
        args = {"group": group}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SNMP_GROUP,
                                           self.parse_const.CHECK_SNMP_GROUP, False,
                                           "SNMP group {group} does not exist.",
                                           "SNMP group {group} exists!",
                                           **kwargs)

    def snmp_verify_access_for_group_exists(self, device_name, group='', security_level='', **kwargs):
        """
        [device_name]   - The device the keyword will be run against.
        [group]         - The group in which which the users belong to.
        [security_level]  - The security level in which the message is sent for users in the group.
                            Valid values are:   noAuthNoPriv, authNoPriv, or authPriv

        Verifies that the specified SNMP access entry for the group entry exists.
        """
        args = {"group": group,
                "security_level": security_level}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SNMP_ACCESS,
                                           self.parse_const.CHECK_SNMP_ACCESS, True,
                                           "SNMP group {group} exists with level {security_level}.",
                                           "SNMP group {group} does NOT exist with level {security_level}!",
                                           **kwargs)

    def snmp_verify_access_for_group_does_not_exist(self, device_name, group='', security_level='', **kwargs):
        """
        [device_name]   - The device the keyword will be run against.
        [group]         - The group in which which the users belong to.
        [security_level]  - The security level in which the message is sent for users in the group.
                            Valid values are:   noAuthNoPriv, authNoPriv, or authPriv

        Verifies that the specified SNMP access entry for the group entry exists.
        """
        args = {"group": group,
                "security_level": security_level}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SNMP_ACCESS,
                                           self.parse_const.CHECK_SNMP_ACCESS, False,
                                           "SNMP group {group} does not exist with level {security_level}.",
                                           "SNMP group {group} does exists with level {security_level}!",
                                           **kwargs)

    def snmp_verify_view_exists(self, device_name, view_name='', oid_tree='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [view_name]    - The name of the view.
        [oid_tree]     - The MIB subtree which defines a subtree to be included or excluded.
                         Example:  +1.3.6.1.6.3.1.1.4.1 to include and -1.3.6.1.6.3.1.1.4.1 to exclude.

        Verifies that a view entry exists.
        """
        args = {"view_name": view_name,
                "oid_tree": oid_tree}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SNMP_VIEW,
                                           self.parse_const.CHECK_SNMP_VIEW, True,
                                           "SNMP view {view_name} exists with tree{oid_tree}.",
                                           "SNMP view {view_name} does NOT exist with tree {oid_tree}!",
                                           **kwargs)

    def snmp_verify_view_does_not_exist(self, device_name, view_name='', oid_tree='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [view_name]    - The name of the view.
        [oid_tree]     - The MIB subtree which defines a subtree to be included or excluded.
                         Example:  +1.3.6.1.6.3.1.1.4.1 to include and -1.3.6.1.6.3.1.1.4.1 to exclude.

        Verifies that a view entry does not exist.
        """
        args = {"view_name": view_name,
                "oid_tree": oid_tree}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SNMP_VIEW,
                                           self.parse_const.CHECK_SNMP_VIEW, False,
                                           "SNMP {view_name} exists with tree{oid_tree}.",
                                           "SNMP {view_name} does NOT exist with tree {oid_tree}!",
                                           **kwargs)
