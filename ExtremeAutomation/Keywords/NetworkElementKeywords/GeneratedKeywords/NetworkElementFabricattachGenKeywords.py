"""
Keyword class for all fabricattach cli commands.
"""
from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import NetworkElementKeywordBaseClass
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.Constants.FabricattachConstants import \
    FabricattachConstants as ParseConstants
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.Constants.FabricattachConstants import \
    FabricattachConstants as CommandConstants
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Keywords.NetworkElementKeywords.Utils.NetworkElementSnmpUtils import \
    NetworkElementSnmpUtils as SnmpUtils


class NetworkElementFabricattachGenKeywords(NetworkElementKeywordBaseClass):
    def __init__(self):
        super(NetworkElementFabricattachGenKeywords, self).__init__()
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()
        self.api_const = "fabricattach"

    def fabricattach_enable_global(self, device_name, **kwargs):
        """
        Description: Enables the Fabric Attach service.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_GLOBAL,
                                    **kwargs)

    def fabricattach_disable_global(self, device_name, **kwargs):
        """
        Description: Disables the Fabric Attach service.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_GLOBAL,
                                    **kwargs)

    def fabricattach_enable_port(self, device_name, port='', **kwargs):
        """
        Description: Adds a port in the Fabric Attach table as enabled. i.e. FA TLVs will be included in LLDPDUs
                     generated on the port.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_PORT,
                                    **kwargs)

    def fabricattach_disable_port(self, device_name, port='', **kwargs):
        """
        Description: Adds a port in the Fabric Attach table as disabled i.e. FA TLVs will not be included in LLDPDUs
                     generated on the port.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_PORT,
                                    **kwargs)

    def fabricattach_delete_port(self, device_name, port='', **kwargs):
        """
        Description: Removes the port instance in the Fabric Attach interface table.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DELETE_PORT,
                                    **kwargs)

    def fabricattach_enable_mlt(self, device_name, mlt_id='', **kwargs):
        """
        Description: Adds an MLT in the Fabric Attach table as enabled. i.e. FA TLVs will be included in LLDPDUs
                     generated on the MLT.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "mlt_id": mlt_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_MLT,
                                    **kwargs)

    def fabricattach_disable_mlt(self, device_name, mlt_id='', **kwargs):
        """
        Description: Adds an MLT in the Fabric Attach table as disabled. i.e. FA TLVs will be included in LLDPDUs
                     generated on the MLT.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "mlt_id": mlt_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_MLT,
                                    **kwargs)

    def fabricattach_delete_mlt(self, device_name, mlt_id='', **kwargs):
        """
        Description: Removes MLT instance on the Fabric Attach interface table.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "mlt_id": mlt_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DELETE_MLT,
                                    **kwargs)

    def fabricattach_enable_port_auth(self, device_name, port='', **kwargs):
        """
        Description: Enables Fabric Attach authentication for a port.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_PORT_AUTH,
                                    **kwargs)

    def fabricattach_disable_port_auth(self, device_name, port='', **kwargs):
        """
        Description: Disables Fabric Attach authentication for a port.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_PORT_AUTH,
                                    **kwargs)

    def fabricattach_enable_mlt_auth(self, device_name, mlt_id='', **kwargs):
        """
        Description: Enables a Multi-Link Trunk for Fabric Attach authentication.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "mlt_id": mlt_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_MLT_AUTH,
                                    **kwargs)

    def fabricattach_disable_mlt_auth(self, device_name, mlt_id='', **kwargs):
        """
        Description: Disables Fabric Attach authentication for a Multi-Link Trunk.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "mlt_id": mlt_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_MLT_AUTH,
                                    **kwargs)

    def fabricattach_set_assignment_timeout(self, device_name, timeout='', **kwargs):
        """
        Description: Configures the Fabric Attach assignment timeout.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "timeout": timeout
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_ASSIGNMENT_TIMEOUT,
                                    **kwargs)

    def fabricattach_set_discovery_timeout(self, device_name, timeout='', **kwargs):
        """
        Description: Configures the Fabric Attach discovery timeout.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "timeout": timeout
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_DISCOVERY_TIMEOUT,
                                    **kwargs)

    def fabricattach_set_port_auth_key(self, device_name, port='', auth_key='', **kwargs):
        """
        Description: Provides access to the Fabric Attach message authentication key for the associated port.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "auth_key": auth_key,
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PORT_AUTH_KEY,
                                    **kwargs)

    def fabricattach_set_mlt_auth_key(self, device_name, mlt_id='', auth_key='', **kwargs):
        """
        Description: Provides access to the Fabric Attach message authentication key for the associated Multi-Link
                     Trunk.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "auth_key": auth_key,
            "mlt_id": mlt_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_MLT_AUTH_KEY,
                                    **kwargs)

    def fabricattach_set_port_mgmt_isid(self, device_name, port='', i_sid='', **kwargs):
        """
        Description: Configures the Fabric Attach management i-sid for the associated port.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "i_sid": i_sid,
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PORT_MGMT_ISID,
                                    **kwargs)

    def fabricattach_set_mlt_mgmt_isid(self, device_name, mlt_id='', i_sid='', **kwargs):
        """
        Description: Configures the Fabric Attach management i-sid for the associated Multi-Link Trunk.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "i_sid": i_sid,
            "mlt_id": mlt_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_MLT_MGMT_ISID,
                                    **kwargs)

    def fabricattach_set_port_mgmt_isid_and_cvid(self, device_name, port='', i_sid='', c_vid='', **kwargs):
        """
        Description: Configures the Fabric Attach management i-sid for the associated port.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "c_vid": c_vid,
            "i_sid": i_sid,
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PORT_MGMT_ISID_AND_CVID,
                                    **kwargs)

    def fabricattach_set_mlt_mgmt_isid_and_cvid(self, device_name, mlt_id='', i_sid='', c_vid='', **kwargs):
        """
        Description: Configures the Fabric Attach management i-sid for the associated Multi-Link Trunk.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "c_vid": c_vid,
            "i_sid": i_sid,
            "mlt_id": mlt_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_MLT_MGMT_ISID_AND_CVID,
                                    **kwargs)

    def fabricattach_clear_port_mgmt_isid(self, device_name, port='', **kwargs):
        """
        Description: Removes the Fabric Attach management i-sid for the associated port.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_PORT_MGMT_ISID,
                                    **kwargs)

    def fabricattach_clear_mlt_mgmt_isid(self, device_name, mlt_id='', **kwargs):
        """
        Description: Removes the Fabric Attach management i-sid for the associated Multi-Link Trunk.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "mlt_id": mlt_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_MLT_MGMT_ISID,
                                    **kwargs)

    def fabricattach_set_zero_touch_client_isid(self, device_name, name='', i_sid='', **kwargs):
        """
        Description: Creates the auto-attach mapping of the Fabric Attach I-SID component to the Zero Touch Client
                     standard name.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "i_sid": i_sid,
            "name": name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_ZERO_TOUCH_CLIENT_ISID,
                                    **kwargs)

    def fabricattach_clear_zero_touch_client(self, device_name, name='', **kwargs):
        """
        Description: Removes the auto-attach mapping of the Fabric Attach I-SID component to the Zero Touch Client
                     standard name.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "name": name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_ZERO_TOUCH_CLIENT,
                                    **kwargs)

    # ##################################################################################################################
    #   Inspection Keywords   ##########################################################################################
    # ##################################################################################################################

    def fabricattach_verify_enabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.

        Verifies that the Fabric Attach service is enabled.
        """
        args = {"oid_index": "0"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SERVICE_STATE,
                                           self.parse_const.CHECK_FA_SERVICE_STATE, True,
                                           "Fabric Attach service on {device_name} is enabled.",
                                           "Fabric Attach service on {device_name} is NOT enabled!",
                                           **kwargs)

    def fabricattach_verify_disabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.

        Verifies that the Fabric Attach service is disabled.
        """
        args = {"oid_index": "0"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SERVICE_STATE,
                                           self.parse_const.CHECK_FA_SERVICE_STATE, False,
                                           "Fabric Attach service on {device_name} is disabled.",
                                           "Fabric Attach service on {device_name} is NOT disabled!",
                                           **kwargs)

    def fabricattach_verify_element_is_server(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.

        Verifies that the device is a fabric attach server.
        """
        args = {"oid_index": "0"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ELEMENT_TYPE,
                                           self.parse_const.CHECK_FA_ELEMENT_TYPE, True,
                                           "{device_name} is a Fabric Attach Server.",
                                           "{device_name} is NOT a Fabric Attach Server!",
                                           **kwargs)

    def fabricattach_verify_element_is_proxy(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.

        Verifies that the device is a fabric attach proxy.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_AGENT,
                                           self.parse_const.CHECK_FA_ELEMENT_TYPE, True,
                                           "{device_name} is a Fabric Attach Proxy.",
                                           "{device_name} is NOT a Fabric Attach Proxy!",
                                           **kwargs)

    def fabricattach_verify_client_proxy_enabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.

        Verifies that the client proxy status is enabled.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_AGENT,
                                           self.parse_const.CHECK_FA_CLIENT_PROXY_STATUS, True,
                                           "{device_name} is a Fabric Attach Proxy.",
                                           "{device_name} is NOT a Fabric Attach Proxy!",
                                           **kwargs)

    def fabricattach_verify_mode_spbm(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.

        Verifies that fabric attach is using SPBM mode.
        """
        args = {"oid_index": "0"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PROVISION_MODE,
                                           self.parse_const.CHECK_FA_PROVISION_MODE, True,
                                           "Fabric Attach provisioning mode is SPBM on {device_name}.",
                                           "Fabric Attach provisioning mode is NOT SPBM on {device_name}!",
                                           **kwargs)

    def fabricattach_verify_assignment_timeout(self, device_name, timeout='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [timeout]     - The Fabric Attach assignment timeout.  Values: 45..480 Default: 240

        Verifies the Fabric Attach assignment timeout.
        """
        args = {"oid_index": "0",
                "timeout": timeout}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_GLOBAL_TIMEOUTS,
                                           self.parse_const.CHECK_FA_ASSIGNMENT_TIMEOUT, True,
                                           "Fabric Attach assignment timeout on {device_name} is {timeout}.",
                                           "Fabric Attach assignment timeout on {device_name} is NOT {timeout}!",
                                           **kwargs)

    def fabricattach_verify_agent_timeout(self, device_name, timeout='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [timeout]     - The Fabric Attach assignment timeout to verify.

        Verifies the Fabric Attach agent timeout value.
        """
        args = {"timeout": timeout}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_GLOBAL_TIMEOUTS,
                                           self.parse_const.CHECK_FA_AGENT_TIMEOUT, True,
                                           "Fabric Attach agent timeout on {device_name} is {timeout}.",
                                           "Fabric Attach agent timeout on {device_name} is NOT {timeout}!",
                                           **kwargs)

    def fabricattach_verify_discovery_timeout(self, device_name, timeout='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [timeout]     - The Fabric Attach discovery timeout.  Values: 45..480 Default: 240

        Verifies the Fabric Attach discovery timeout.
        """
        args = {"oid_index": "0",
                "timeout": timeout}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_GLOBAL_TIMEOUTS,
                                           self.parse_const.CHECK_FA_DISCOVERY_TIMEOUT, True,
                                           "Fabric Attach discovery timeout on {device_name} is {timeout}.",
                                           "Fabric Attach discovery timeout on {device_name} is NOT {timeout}!",
                                           **kwargs)

    def fabricattach_verify_attach_agent_service_enabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.

        Verifies the Fabric Attach Agent's Service Status is Enabled.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_AGENT,
                                           self.parse_const.CHECK_FA_SERVICE_STATE, True,
                                           "The Fabric Attach Agent's service status on {device_name} is enabled.",
                                           "The Fabric Attach Agent's service status on {device_name} is NOT enabled!",
                                           **kwargs)

    def fabricattach_verify_removed_on_port(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [port]        - The port(s) to check.

        Verifies Fabric Attach does not have the port instance.
        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port)}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT,
                                           self.parse_const.CHECK_FA_PORT_EXISTS, False,
                                           "Fabric Attach server is removed on {port}.",
                                           "Fabric Attach server is NOT removed on {port}!",
                                           **kwargs)

    def fabricattach_verify_enabled_on_port(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [port]        - The port(s) to check.

        Verifies FA TLVs will be included in LLDPDUs generated on the port.
        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port)}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT,
                                           self.parse_const.CHECK_FA_PORT_SERVER_STATUS, True,
                                           "Fabric Attach server status is enabled on {port}.",
                                           "Fabric Attach server status is NOT enabled on {port}!",
                                           **kwargs)

    def fabricattach_verify_disabled_on_port(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [port]        - The port(s) to check.

        Verifies FA TLVs will not be included in LLDPDUs generated on the port.
        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port)}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT,
                                           self.parse_const.CHECK_FA_PORT_SERVER_STATUS, False,
                                           "Fabric Attach server status is disabled on {port}.",
                                           "Fabric Attach server status is NOT disabled on {port}!",
                                           **kwargs)

    def fabricattach_verify_removed_on_mlt(self, device_name, mlt_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [mlt_id]      - The Multi-Link Trunk(s) to remove on Fabric Attach.

        Verifies Fabric Attach does not have the Multi-Link Trunk instance.
        """
        args = {"mlt_id": mlt_id,
                "oid_index": SnmpUtils().get_mlt_logical_index(device_name, mlt_id)}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_MLT,
                                           self.parse_const.CHECK_FA_MLT_EXISTS, False,
                                           "Fabric Attach server exists on MLT {mlt_id}.",
                                           "Fabric Attach server does NOT exist on MLT {mlt_id}!",
                                           **kwargs)

    def fabricattach_verify_enabled_on_mlt(self, device_name, mlt_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [mlt_id]      - The Multi-Link Trunk(s) to enable Fabric Attach.

        Verifies FA TLVs will be included in LLDPDUs generated on the Multi-Link Trunk.
        """
        args = {"mlt_id": mlt_id,
                "oid_index": SnmpUtils().get_mlt_logical_index(device_name, mlt_id)}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_MLT,
                                           self.parse_const.CHECK_FA_MLT_SERVER_STATUS, True,
                                           "Fabric Attach server status is enabled on MLT {mlt_id}.",
                                           "Fabric Attach server status is NOT enabled on MLT {mlt_id}!",
                                           **kwargs)

    def fabricattach_verify_disabled_on_mlt(self, device_name, mlt_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [mlt_id]      - The Multi-Link Trunk(s) to disable Fabric Attach.

        Verifies FA TLVs will not be included in LLDPDUs generated on the Multi-Link Trunk.
        """
        args = {"mlt_id": mlt_id,
                "oid_index": SnmpUtils().get_mlt_logical_index(device_name, mlt_id)}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_MLT,
                                           self.parse_const.CHECK_FA_MLT_SERVER_STATUS, False,
                                           "Fabric Attach server status is disabled on MLT {mlt_id}.",
                                           "Fabric Attach server status is NOT disabled on MLT {mlt_id}!",
                                           **kwargs)

    def fabricattach_verify_auth_enabled_on_port(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [port]        - The port(s) to check.

        Verifies Fabric Attach authentication is enabled on a port.
        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port)}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT,
                                           self.parse_const.CHECK_FA_PORT_AUTHENTICATION_STATUS, True,
                                           "Fabric Attach authentication is enabled on {port}.",
                                           "Fabric Attach authentication is NOT enabled on {port}!",
                                           **kwargs)

    def fabricattach_verify_auth_disabled_on_port(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [port]        - The port(s) to check.

        Verifies Fabric Attach authentication is disabled on a port.
        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port)}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT,
                                           self.parse_const.CHECK_FA_PORT_AUTHENTICATION_STATUS, False,
                                           "Fabric Attach authentication is disabled on {port}.",
                                           "Fabric Attach authentication is NOT disabled on {port}!",
                                           **kwargs)

    def fabricattach_verify_auth_enabled_on_mlt(self, device_name, mlt_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name]   - The device the keyword should be run against.
        [mlt_id]       - The Multi-Link Trunk(s) to check.

        Verifies Fabric Attach authentication is enabled on a Multi-Link Trunk.
        """
        args = {"mlt_id": mlt_id,
                "oid_index": SnmpUtils().get_mlt_logical_index(device_name, mlt_id)}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_MLT,
                                           self.parse_const.CHECK_FA_MLT_AUTHENTICATION_STATUS, True,
                                           "Fabric Attach authentication is enabled on MLT {mlt_id}.",
                                           "Fabric Attach authentication is NOT enabled on MLT {mlt_id}!",
                                           **kwargs)

    def fabricattach_verify_auth_disabled_on_mlt(self, device_name, mlt_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name]   - The device the keyword should be run against.
        [mlt_id]       - The Multi-Link Trunk(s) to check.

        Verifies Fabric Attach authentication is disabled on a Multi-Link Trunk.
        """
        args = {"mlt_id": mlt_id,
                "oid_index": SnmpUtils().get_mlt_logical_index(device_name, mlt_id)}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_MLT,
                                           self.parse_const.CHECK_FA_MLT_AUTHENTICATION_STATUS, False,
                                           "Fabric Attach authentication is disabled on MLT {mlt_id}.",
                                           "Fabric Attach authentication is NOT disabled on MLT {mlt_id}!",
                                           **kwargs)

    def fabricattach_verify_mgmt_isid_on_port(self, device_name, port='', i_sid='', **kwargs):
        """
        Keyword Arguments:
        [device_name]   - The device the keyword should be run against.
        [port]          - The port to check.
        [i_sid]         - The Service Identifier instance.

        Verifies the Fabric Attach management i-sid is on the port.
        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port),
                "i_sid": i_sid}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT,
                                           self.parse_const.CHECK_FA_MANAGEMENT_ISID_ON_PORT, True,
                                           "Fabric Attach management i-sid {i_sid} is on port {port}.",
                                           "Fabric Attach management i-sid {i_sid} is NOT on port {port}!",
                                           **kwargs)

    def fabricattach_verify_mgmt_isid_on_mlt(self, device_name, mlt_id='', i_sid='', **kwargs):
        """
        Keyword Arguments:
        [device_name]   - The device the keyword should be run against.
        [mlt-id]        - The Multi-Link trunk to check.
        [i_sid]         - The Service Identifier instance.

        Verifies the Fabric Attach management i-sid is on the MLT.
        """
        args = {"mlt_id": mlt_id,
                "oid_index": SnmpUtils().get_mlt_logical_index(device_name, mlt_id),
                "i_sid": i_sid}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_MLT,
                                           self.parse_const.CHECK_FA_MANAGEMENT_ISID_ON_MLT, True,
                                           "Fabric Attach management i-sid {i_sid} is on MLT {mlt_id}.",
                                           "Fabric Attach management i-sid {i_sid} is NOT on MLT {mlt_id}!",
                                           **kwargs)

    def fabricattach_verify_mgmt_isid_and_cvid_on_port(self, device_name, port='', i_sid='', c_vid='', **kwargs):
        """
        Keyword Arguments:
        [device_name]   - The device the keyword should be run against.
        [port]          - The port to check.
        [i_sid]         - The Fabric Attach management i-sid. Values: 0..16777215
        [c_vid]         - The Fabric Attach management customer vid. Values: 0..4096

        Configures the Fabric Attach management i-sid for the associated interface.
        Zero means the management i-sid feature is not enabled.
        It Also configures the Fabric Attach management customer vid for the associated interface.
        Zero means the management i-sid feature is not enabled. 4096 means it is untagged.

        Verifies the Fabric Attach management i-sid and c-vid is on the port.
        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port),
                "i_sid": i_sid,
                "c_vid": c_vid}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT,
                                           self.parse_const.CHECK_FA_MANAGEMENT_ISID_AND_CVID_ON_PORT, True,
                                           "Fabric Attach i-sid {i_sid} and c-vid {c_vid} is on port {port}.",
                                           "Fabric Attach i-sid {i_sid} and c-vid {c_vid} is NOT on port {port}!",
                                           **kwargs)

    def fabricattach_verify_mgmt_isid_and_cvid_on_mlt(self, device_name, mlt_id='', i_sid='', c_vid='', **kwargs):
        """
        Keyword Arguments:
        [device_name]   - The device the keyword should be run against.
        [mlt-id]        - The Multi-Link trunk to check.
        [i_sid]         - The Fabric Attach management i-sid. Values: 0..16777215
        [c_vid]         - The Fabric Attach management customer vid. Values: 0..4096

        Configures the Fabric Attach management i-sid for the associated interface.
        Zero means the management i-sid feature is not enabled.
        It Also configures the Fabric Attach management customer vid for the associated interface.
        Zero means the management i-sid feature is not enabled. 4096 means it is untagged.
        Verifies the Fabric Attach management i-sid and c-vid is on the MLT.
        """
        args = {"mlt_id": mlt_id,
                "oid_index": SnmpUtils().get_mlt_logical_index(device_name, mlt_id),
                "i_sid": i_sid,
                "c_vid": c_vid}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_MLT,
                                           self.parse_const.CHECK_FA_MANAGEMENT_ISID_AND_CVID_ON_MLT, True,
                                           "Fabric Attach i-sid {i_sid} and c-vid {c_vid} is on MLT {mlt_id}.",
                                           "Fabric Attach i-sid {i_sid} and c-vid {c_vid} is NOT on "
                                           "MLT {mlt_id}!",
                                           **kwargs)

    def fabricattach_verify_mgmt_isid_disabled_on_port(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [port]        - The port(s) to check.

        Verifies Fabric Attach management i-sid is disabled on a port.
        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port),
                "i_sid": "0"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT,
                                           self.parse_const.CHECK_FA_MANAGEMENT_ISID_ON_PORT, False,
                                           "Fabric Attach management i-sid is disabled on {port}.",
                                           "Fabric Attach management i-sid is NOT disabled on {port}!",
                                           **kwargs)

    def fabricattach_verify_mgmt_isid_disabled_on_mlt(self, device_name, mlt_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [port]        - The port(s) to check.

        Verifies Fabric Attach management i-sid is disabled on a Multi-Link trunk.
        """
        args = {"mlt_id": mlt_id,
                "oid_index": SnmpUtils().get_mlt_logical_index(device_name, mlt_id),
                "i_sid": "0"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_MLT,
                                           self.parse_const.CHECK_FA_MANAGEMENT_ISID_ON_MLT, False,
                                           "Fabric Attach management i-sid is disabled on {mlt_id}.",
                                           "Fabric Attach management i-sid is NOT disabled on {mlt_id}!",
                                           **kwargs)

    def fabricattach_verify_neighbor_exists(self, device_name, neighbor='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [neighbor]    - The Fabric Attach neighbor to verify.

        Verifies that a specified Fabric Attach neighbor is present on the device.
        """
        args = {"neighbor": neighbor}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_NEIGHBORS,
                                           self.parse_const.CHECK_FA_NEIGHBORS, True,
                                           "Fabric Attach neighbor {neighbor} is present on {device_name}.",
                                           "Fabric Attach neighbor {neighbor} is NOT present on {device_name}!",
                                           **kwargs)

    def fabricattach_verify_neighbor_does_not_exist(self, device_name, neighbor='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [neighbor]    - The Fabric Attach neighbor to verify.

        Verifies that a specified Fabric Attach neighbor is not present on the device.
        """
        args = {"neighbor": neighbor}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_NEIGHBORS,
                                           self.parse_const.CHECK_FA_NEIGHBORS, False,
                                           "Fabric Attach neighbor {neighbor} is not present on {device_name}.",
                                           "Fabric Attach neighbor {neighbor} IS present on {device_name}!",
                                           **kwargs)

    def fabricattach_verify_element_type(self, device_name, port='', element_type='', **kwargs):
        """
        Keyword Arguments:
        [device_name]   - The device the keyword should be run against.
        [port]          - The port(s) to check.
        [element_type]  - The Fabric Attach discovered element type to verify.
        Value list for element_type:

        other
        Server
        Proxy
        ServerNoAuth
        ProxyNoAuth
        ClientWapType1
        ClientWapType2
        ClientSwitch
        ClientRouter
        ClientIpPhone
        ClientIpCamera
        ClientIpVideo
        ClientSecurityDev
        ClientVirtSwitch
        ClientSrvrEndpt

        Verifies the Fabric Attach discovered element type on the port.
        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port),
                "element_type": element_type,
                "enum_element_type": SnmpUtils().fa_element_type(element_type)}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ELEMENTS_PORT,
                                           self.parse_const.CHECK_FA_DISC_ELEMENT_TYPE, True,
                                           "Fabric Attach element type is {element_type} on {port}.",
                                           "Fabric Attach element type is NOT {element_type} on {port}!",
                                           **kwargs)

    def fabricattach_verify_element_vlan(self, device_name, port='', vlan='', **kwargs):
        """
        Keyword Arguments:
        [device_name]   - The device the keyword should be run against.
        [port]          - The port(s) to check.
        [vlan]          - The Fabric Attach element VLAN ID as advertised through LLDP.

        Verifies the Fabric Attach discovered VLAN ID.
        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port),
                "vlan": vlan}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ELEMENTS_PORT,
                                           self.parse_const.CHECK_FA_DISC_ELEMENT_VLAN, True,
                                           "Fabric Attach element VLAN is {vlan} on {port}.",
                                           "Fabric Attach element VLAN is NOT {vlan} on {port}!",
                                           **kwargs)

    def fabricattach_verify_element_system_id(self, device_name, port='', system_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name]  - The device the keyword should be run against.
        [port]         - The port(s) to check.
        [system_id]    - The Chassis ID associated with the discovered Fabric Attach element as advertised through LLDP.

        Verifies the Fabric Attach discovered System ID.
        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port),
                "system_id": system_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ELEMENTS_PORT,
                                           self.parse_const.CHECK_FA_DISC_ELEMENT_SYSTEM_ID, True,
                                           "Fabric Attach element system id is {system_id} on {port}.",
                                           "Fabric Attach element system id is NOT {system_id} on {port}!",
                                           **kwargs)

    def fabricattach_verify_primary_server_id(self, device_name, server_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name]  - The device the keyword should be run against.
        [server id]    - The Primary Server ID to verify.
        (NOTE:  On EXOS, the Server ID is the same as the System ID on VOSS).

        Verifies the Fabric Attach Primary Server ID.
        """
        args = {"server_id": server_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_AGENT,
                                           self.parse_const.CHECK_FA_PRIMARY_SERVER_ID, True,
                                           "Fabric Attach Server ID {server_id} exists on {device_name}.",
                                           "Fabric Attach Server ID {server_id} does NOT exist on {device_name}!",
                                           **kwargs)

    def fabricattach_verify_element_state(self, device_name, port='', state='', **kwargs):
        """
        Keyword Arguments:
        [device_name]   - The device the keyword should be run against.
        [port]          - The port(s) to check.
        [state]         - The Fabric Attach discovered state to verify.
        Value list for state: T, U, D, S, and V.

                              T = trafficTagged
                              U = trafficUntagged
                              D = provisionModeDisabled
                              S = provisionModeSpbm
                              V = provisionModeVlan

        Verifies the Fabric Attach discovered element state on the port.
        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port),
                "state": state}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ELEMENTS_PORT,
                                           self.parse_const.CHECK_FA_DISC_ELEMENT_STATE, True,
                                           "Fabric Attach element state is {state} on {port}.",
                                           "Fabric Attach element state is NOT {state} on {port}!",
                                           **kwargs)

    def fabricattach_verify_element_assigned_auth_status(self, device_name, port='', element_assign_auth='', **kwargs):
        """
        Keyword Arguments:
        [device_name]   - The device the keyword should be run against.
        [port]          - The port(s) to check.
        [element_assign_auth]  - The Fabric Attach discovered element assignment authentication status to verify.
        Value list for element_assign_auth:  AP, AF, NA, or N

                 AP = authenticationPass
                 AF = authenticationFail
                 NA = notAuthenticated
                 N = none

        Verifies the Fabric Attach discovered element assignment authentication status on the port.
        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port),
                "element_assign_auth": element_assign_auth,
                "enum_element_assign_auth": SnmpUtils().fa_element_assign_auth_status(element_assign_auth)}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ELEMENTS_PORT,
                                           self.parse_const.CHECK_FA_DISC_ELEMENT_ASSIGN_AUTH, True,
                                           "Fabric Attach element assigned auth is {element_assign_auth} "
                                           "on {port}.",
                                           "Fabric Attach element assigned auth is NOT {element_assign_auth} "
                                           "on {port}!",
                                           **kwargs)

    def fabricattach_verify_element_auth_status(self, device_name, port='', element_auth='', **kwargs):
        """
        Keyword Arguments:
        [device_name]   - The device the keyword should be run against.
        [port]          - The port(s) to check.
        [element_auth]  - The Fabric Attach discovered element authentication status to verify.
        Value list for element_assign_auth:  AP, AF, NA, or N

                 AP = authenticationPass
                 AF = authenticationFail
                 NA = notAuthenticated
                 N = none

        Verifies the Fabric Attach discovered element assignment authentication status on the port.
        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port),
                "element_auth": element_auth,
                "enum_element_auth": SnmpUtils().fa_element_auth_status(element_auth)}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ELEMENTS_PORT,
                                           self.parse_const.CHECK_FA_DISC_ELEMENT_AUTH, True,
                                           "Fabric Attach element auth is {element_auth} on {port}.",
                                           "Fabric Attach element assigned auth is NOT {element_auth} on {port}!",
                                           **kwargs)

    def fabricattach_verify_element_assigned_oper_auth_status(self, device_name, port='', element_assigned_oper_auth='',
                                                              **kwargs):
        """
        Keyword Arguments:
        [device_name]                 - The device the keyword should be run against.
        [port]                        - The port(s) to check.
        [element_assigned_oper_auth]  - The Fabric Attach discovered element assigned operational authentication status
                                        to verify.
        Value list for element_assign_oper_auth:

                none
                successNoAuth
                successAuth
                failMismatchedKeys
                failLocalAuthRemoteNoAuth
                failLocalNoAuthRemoteAuth

        Verifies the Fabric Attach discovered element assignment operational authentication status on the port.
        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port),
                "element_assigned_oper_auth": element_assigned_oper_auth,
                "enum_element_assigned_oper_auth": SnmpUtils().fa_element_assign_oper_auth_status(
                    element_assigned_oper_auth)}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ELEMENTS_PORT,
                                           self.parse_const.CHECK_FA_DISC_ELEMENT_ASSIGNED_OPER_AUTH, True,
                                           "Fabric Attach assigned oper auth is {element_assigned_oper_auth} "
                                           "on {port}.",
                                           "Fabric Attach assigned oper auth is NOT {element_assigned_oper_auth} "
                                           "on {port}!",
                                           **kwargs)

    def fabricattach_verify_element_oper_auth_status(self, device_name, port='', element_oper_auth='', **kwargs):
        """
        Keyword Arguments:
        [device_name]        - The device the keyword should be run against.
        [port]               - The port(s) to check.
        [element_oper_auth]  - The Fabric Attach discovered element operational authentication status to verify.
        Value list for element_oper_auth:

                none
                successNoAuth
                successAuth
                failMismatchedKeys
                failLocalAuthRemoteNoAuth
                failLocalNoAuthRemoteAuth

        Verifies the Fabric Attach discovered element operational authentication status on the port.
        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port),
                "element_oper_auth": element_oper_auth,
                "enum_element_oper_auth": SnmpUtils().fa_element_oper_auth_status(element_oper_auth)}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ELEMENTS_PORT,
                                           self.parse_const.CHECK_FA_DISC_ELEMENT_OPER_AUTH, True,
                                           "Fabric Attach oper auth is {element_oper_auth} on {port}.",
                                           "Fabric Attach oper auth is NOT {element_oper_auth} on {port}!",
                                           **kwargs)

    def fabricattach_verify_assigned_isid_to_vlan_map_on_port(self, device_name, port='', isid='', vlan='', **kwargs):
        """
        Keyword Arguments:
        [device_name]        - The device the keyword should be run against.
        [port]               - The port to check.
        [isid]               - The I-SID component of the I-SID <-> VLAN  assignment.
        [vlan]               - The VLAN ID component of the I-SID <-> VLAN assignment.

        Verifies the Fabric Attach assignment mapping between an ISID and VLAN is on a port.
        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port),
                "isid": isid,
                "vlan": vlan}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ASSIGNMENT_PORT,
                                           self.parse_const.CHECK_FA_ASSIGN_ISID_TO_VLAN, True,
                                           "Fabric Attach assignment isid {isid} to vlan {vlan}"
                                           " is on port {port}.",
                                           "Fabric Attach assignment isid {isid} to vlan {vlan}"
                                           " is NOT on port {port}!",
                                           **kwargs)

    def fabricattach_verify_assigned_isid_to_vlan_map_not_on_port(self, device_name, port='', isid='', vlan='',
                                                                  **kwargs):
        """
        Keyword Arguments:
        [device_name]        - The device the keyword should be run against.
        [port]               - The port to check.
        [isid]               - The I-SID component of the I-SID <-> VLAN  assignment.
        [vlan]               - The VLAN ID component of the I-SID <-> VLAN assignment.

        Verifies the Fabric Attach assignment mapping between an ISID and VLAN is not on a port.
        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port),
                "isid": isid,
                "vlan": vlan}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ASSIGNMENT_PORT,
                                           self.parse_const.CHECK_FA_ASSIGN_ISID_TO_VLAN, False,
                                           "Fabric Attach assignment isid {isid} to vlan {vlan}"
                                           " is not on port {port}.",
                                           "Fabric Attach assignment isid {isid} to vlan {vlan}"
                                           " EXISTS on port {port}!",
                                           **kwargs)

    def fabricattach_verify_assigned_isid_to_vlan_map_state_on_port(self, device_name, port='', isid='', vlan='',
                                                                    state='', **kwargs):
        """
        Keyword Arguments:
        [device_name]        - The device the keyword should be run against.
        [port]               - The port to check.
        [isid]               - The I-SID component of the I-SID <-> VLAN  assignment.
        [vlan]               - The VLAN ID component of the I-SID <-> VLAN assignment.
        [state]              - The current state of the Fabric Attach I-SID <-> VLAN assignment.
                                - State Values:

                                    other
                                    pending
                                    active
                                    rejected

        Verifies the state of the Fabric Attach assignment mapping between an ISID and VLAN on a port.
        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port),
                "isid": isid,
                "vlan": vlan,
                "state": state}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ASSIGNMENT_PORT,
                                           self.parse_const.CHECK_FA_ASSIGN_ISID_TO_VLAN_STATE, True,
                                           "Fabric Attach assignment isid {isid} to vlan {vlan}"
                                           " state on port {port} is {state}.",
                                           "Fabric Attach assignment isid {isid} to vlan {vlan}"
                                           " state on port {port} is NOT {state}!",
                                           **kwargs)

    def fabricattach_verify_assigned_isid_to_vlan_map_origin_on_port(self, device_name, port='', isid='', vlan='',
                                                                     origin='', **kwargs):
        """
        Keyword Arguments:
        [device_name]        - The device the keyword should be run against.
        [port]               - The port to check.
        [isid]               - The I-SID component of the I-SID <-> VLAN  assignment.
        [vlan]               - The VLAN ID component of the I-SID <-> VLAN assignment.
        [origin]              - The origin information for the Fabric Attach I-SID <-> VLAN assignment.
                                - Origin Values:

                                    Other
                                    Proxy
                                    Client
                                    RadiusClient
                                    ZeroTouchClient

        Verifies the origin of the Fabric Attach assignment mapping between an ISID and VLAN on a port.
        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port),
                "isid": isid,
                "vlan": vlan,
                "origin": origin}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ASSIGNMENT_PORT,
                                           self.parse_const.CHECK_FA_ASSIGN_ISID_TO_VLAN_ORIGIN, True,
                                           "Fabric Attach assignment isid {isid} to vlan {vlan}"
                                           " origin on port {port} is {origin}.",
                                           "Fabric Attach assignment isid {isid} to vlan {vlan}"
                                           " origin on port {port} is NOT {origin}!",
                                           **kwargs)

    def fabricattach_verify_global_stats_discovered_elements_received(self, device_name, count='', count_operator="=",
                                                                      **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will be run against.
        [count]           - The value to compare against.
        [count_operator]  - The operator (>, <, or =) to be used along with the count argument.
                            If nothing is specified (=) will be used.

        Verifies the number of FA Element TLVs received on all device ports since the
        most recent epoch (e.g., device reset, global statistics reset).
        """
        args = {"oid_index": "0",
                "count_operator": count_operator,
                "count": count}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_STATS_GLOBAL,
                                           self.parse_const.CHECK_FA_GLOBAL_STATS_DISC_ELEM_RECEIVED, True,
                                           "Fabric Attach global stats discovered elements received is"
                                           " {count_operator} {count}.",
                                           "Fabric Attach global stats discovered elements received is NOT"
                                           " {count_operator} {count}!",
                                           **kwargs)

    def fabricattach_verify_global_stats_assignments_received(self, device_name, count='', count_operator="=",
                                                              **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will be run against.
        [count]           - The value to compare against.
        [count_operator]  - The operator (>, <, or =) to be used along with the count argument.
                            If nothing is specified (=) will be used.

        Verifies the number of I-SID/VLAN bindings received in FA I-SID/VLAN Assignment TLVs on
        all device ports since the most recent epoch (e.g., device reset, global statistics reset).
        """
        args = {"oid_index": "0",
                "count_operator": count_operator,
                "count": count}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_STATS_GLOBAL,
                                           self.parse_const.CHECK_FA_GLOBAL_STATS_ASGN_RECEIVED, True,
                                           "Fabric Attach global stats assignments received is"
                                           " {count_operator} {count}.",
                                           "Fabric Attach global stats assignments received is NOT"
                                           " {count_operator} {count}!",
                                           **kwargs)

    def fabricattach_verify_global_stats_assignments_accepted(self, device_name, count='', count_operator="=",
                                                              **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will be run against.
        [count]           - The value to compare against.
        [count_operator]  - The operator (>, <, or =) to be used along with the count argument.
                            If nothing is specified (=) will be used.

        Verifies the number of I-SID/VLAN bindings from received FA I-SID/VLAN Assignment TLVs that are accepted
        (activated) on all device ports since the most recent epoch (e.g., device reset, global statistics reset).
        """
        args = {"oid_index": "0",
                "count_operator": count_operator,
                "count": count}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_STATS_GLOBAL,
                                           self.parse_const.CHECK_FA_GLOBAL_STATS_ASGN_ACCEPTED, True,
                                           "Fabric Attach global stats assignments accepted is"
                                           " {count_operator} {count}.",
                                           "Fabric Attach global stats assignments accepted is NOT"
                                           " {count_operator} {count}!",
                                           **kwargs)

    def fabricattach_verify_global_stats_assignments_rejected(self, device_name, count='', count_operator="=",
                                                              **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will be run against.
        [count]           - The value to compare against.
        [count_operator]  - The operator (>, <, or =) to be used along with the count argument.
                            If nothing is specified (=) will be used.

        Verifies the number of I-SID/VLAN bindings from received FA I-SID/VLAN Assignment TLVs that are rejected
        on all device ports since the most recent epoch (e.g., device reset, global statistics reset).
        """
        args = {"oid_index": "0",
                "count_operator": count_operator,
                "count": count}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_STATS_GLOBAL,
                                           self.parse_const.CHECK_FA_GLOBAL_STATS_ASGN_REJECTED, True,
                                           "Fabric Attach global stats assignments rejected is"
                                           " {count_operator} {count}.",
                                           "Fabric Attach global stats assignments rejected is NOT"
                                           " {count_operator} {count}!",
                                           **kwargs)

    def fabricattach_verify_global_stats_assignments_expired(self, device_name, count='', count_operator="=", **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will be run against.
        [count]           - The value to compare against.
        [count_operator]  - The operator (>, <, or =) to be used along with the count argument.
                            If nothing is specified (=) will be used.

        Verifies the number of I-SID/VLAN bindings from received FA I-SID/VLAN Assignment TLVs that have expired
        on all device ports since the most recent epoch (e.g., device reset, global statistics reset).
        """
        args = {"oid_index": "0",
                "count_operator": count_operator,
                "count": count}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_STATS_GLOBAL,
                                           self.parse_const.CHECK_FA_GLOBAL_STATS_ASGN_EXPIRED, True,
                                           "Fabric Attach global stats assignments expired is"
                                           " {count_operator} {count}.",
                                           "Fabric Attach global stats assignments expired is NOT"
                                           " {count_operator} {count}!",
                                           **kwargs)

    def fabricattach_verify_global_stats_discovered_auth_failed(self, device_name, count='', count_operator="=",
                                                                **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will be run against.
        [count]           - The value to compare against.
        [count_operator]  - The operator (>, <, or =) to be used along with the count argument.
                            If nothing is specified (=) will be used.

        Verifies the number of received FA Element TLVs from which authentication was attempted and failed on all device
        ports since the most recent epoch (e.g., device reset, global statistics reset).
        """
        args = {"oid_index": "0",
                "count_operator": count_operator,
                "count": count}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_STATS_GLOBAL,
                                           self.parse_const.CHECK_FA_GLOBAL_STATS_DISC_AUTH_FAILED, True,
                                           "Fabric Attach global stats discovered authentications failed is"
                                           " {count_operator} {count}.",
                                           "Fabric Attach global stats discovered authentications failed is NOT"
                                           " {count_operator} {count}!",
                                           **kwargs)

    def fabricattach_verify_global_stats_discovered_elements_expired(self, device_name, count='', count_operator="=",
                                                                     **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will be run against.
        [count]           - The value to compare against.
        [count_operator]  - The operator (>, <, or =) to be used along with the count argument.
                            If nothing is specified (=) will be used.

        Verifies the number of received FA Element TLVs from received FA Element TLVs that were expired on all device
        ports since the most recent epoch (e.g., device reset, global statistics reset).
        """
        args = {"oid_index": "0",
                "count_operator": count_operator,
                "count": count}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_STATS_GLOBAL,
                                           self.parse_const.CHECK_FA_GLOBAL_STATS_DISC_ELEM_EXPIRED, True,
                                           "Fabric Attach global stats discovered elements expired is"
                                           " {count_operator} {count}.",
                                           "Fabric Attach global stats discovered elements expired is NOT"
                                           " {count_operator} {count}!",
                                           **kwargs)

    def fabricattach_verify_global_stats_discovered_elements_deleted(self, device_name, count='', count_operator="=",
                                                                     **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will be run against.
        [count]           - The value to compare against.
        [count_operator]  - The operator (>, <, or =) to be used along with the count argument.
                            If nothing is specified (=) will be used.

        Verifies the number of received FA Element TLVs from received FA Element TLVs that have been deleted
        on all device ports since the most recent epoch (e.g., device reset, global statistics reset).
        """
        args = {"oid_index": "0",
                "count_operator": count_operator,
                "count": count}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_STATS_GLOBAL,
                                           self.parse_const.CHECK_FA_GLOBAL_STATS_DISC_ELEM_DELETED, True,
                                           "Fabric Attach global stats discovered elements deleted is"
                                           " {count_operator} {count}.",
                                           "Fabric Attach global stats discovered elements deleted is NOT"
                                           " {count_operator} {count}!",
                                           **kwargs)

    def fabricattach_verify_global_stats_assignments_deleted(self, device_name, count='', count_operator="=", **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will be run against.
        [count]           - The value to compare against.
        [count_operator]  - The operator (>, <, or =) to be used along with the count argument.
                            If nothing is specified (=) will be used.

        Verifies the number of I-SID/VLAN bindings from received FA I-SID/VLAN Assignment TLVs that have been
        deleted on all device ports since the most recent epoch (e.g., device reset, global statistics reset).

        """
        args = {"oid_index": "0",
                "count_operator": count_operator,
                "count": count}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_STATS_GLOBAL,
                                           self.parse_const.CHECK_FA_GLOBAL_STATS_ASGN_DELETED, True,
                                           "Fabric Attach global stats assignments deleted is"
                                           " {count_operator} {count}.",
                                           "Fabric Attach global stats assignments deleted is NOT"
                                           " {count_operator} {count}!",
                                           **kwargs)

    def fabricattach_verify_global_stats_assignment_auth_failed(self, device_name, count='', count_operator="=",
                                                                **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will be run against.
        [count]           - The value to compare against.
        [count_operator]  - The operator (>, <, or =) to be used along with the count argument.
                            If nothing is specified (=) will be used.

        Verifies the number of received FA I-SID/VLAN Assignment TLVs for which authentication was attempted and failed
        on all device ports since the most recent epoch (e.g., device reset, global statistics reset).
        """
        args = {"oid_index": "0",
                "count_operator": count_operator,
                "count": count}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_STATS_GLOBAL,
                                           self.parse_const.CHECK_FA_GLOBAL_STATS_ASGN_AUTH_FAILED, True,
                                           "Fabric Attach global stats assignment authentications failed is"
                                           " {count_operator} {count}.",
                                           "Fabric Attach global stats assignment authentications failed is NOT"
                                           " {count_operator} {count}!",
                                           **kwargs)

    def fabricattach_verify_port_stats_discovered_elements_received(self, device_name, port='', count='',
                                                                    count_operator="=", **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will be run against.
        [port]            - The port(s) in which is being verified.
        [count]           - The value to compare against.
        [count_operator]  - The operator (>, <, or =) to be used along with the count argument.
                            If nothing is specified (=) will be used.

        Verifies the number of FA Element TLVs received on the identified port.
        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port),
                "count_operator": count_operator,
                "count": count}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_STATS_PORT,
                                           self.parse_const.CHECK_FA_PORT_STATS_DISC_ELEM_RECEIVED, True,
                                           "Fabric Attach port stats discovered elements received is"
                                           " {count_operator} {count} on port {port}.",
                                           "Fabric Attach port stats discovered elements received is NOT"
                                           " {count_operator} {count} on port {port}!",
                                           **kwargs)

    def fabricattach_verify_port_stats_assignments_received(self, device_name, port='', count='', count_operator="=",
                                                            **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will be run against.
        [port]            - The port(s) in which is being verified.
        [count]           - The value to compare against.
        [count_operator]  - The operator (>, <, or =) to be used along with the count argument.
                            If nothing is specified (=) will be used.

        Verifies the number of I-SID/VLAN bindings received in FA I-SID/VLAN Assignment TLVs on the identified port.
        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port),
                "count_operator": count_operator,
                "count": count}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_STATS_PORT,
                                           self.parse_const.CHECK_FA_PORT_STATS_ASGN_RECEIVED, True,
                                           "Fabric Attach port stats assignments received is"
                                           " {count_operator} {count} on port {port}.",
                                           "Fabric Attach port stats assignments received is NOT"
                                           " {count_operator} {count} on port {port}!",
                                           **kwargs)

    def fabricattach_verify_port_stats_assignments_accepted(self, device_name, port='', count='', count_operator="=",
                                                            **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will be run against.
        [port]            - The port(s) in which is being verified.
        [count]           - The value to compare against.
        [count_operator]  - The operator (>, <, or =) to be used along with the count argument.
                            If nothing is specified (=) will be used.

        Verifies  the number of I-SID/VLAN bindings from received FA I-SID/VLAN Assignment TLVs that are accepted
        (activated) on the identified port. The counter is incremented when the binding transitions from a
        non-accepted state (e.g.,'pending', 'rejected') to the accepted state.
        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port),
                "count_operator": count_operator,
                "count": count}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_STATS_PORT,
                                           self.parse_const.CHECK_FA_PORT_STATS_ASGN_ACCEPTED, True,
                                           "Fabric Attach port stats assignments accepted is"
                                           " {count_operator} {count} on port {port}.",
                                           "Fabric Attach port stats assignments accepted is NOT"
                                           " {count_operator} {count} on port {port}!",
                                           **kwargs)

    def fabricattach_verify_port_stats_assignments_rejected(self, device_name, port='', count='', count_operator="=",
                                                            **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will be run against.
        [port]            - The port(s) in which is being verified.
        [count]           - The value to compare against.
        [count_operator]  - The operator (>, <, or =) to be used along with the count argument.
                            If nothing is specified (=) will be used.

        Verifies the number of I-SID/VLAN bindings from received FA I-SID/VLAN Assignment TLVs that are rejected on
        the identified port.  The counter is incremented when the binding transitions from a non-rejected state
         (e.g., 'pending', 'accepted') to the rejected state.

        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port),
                "count_operator": count_operator,
                "count": count}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_STATS_PORT,
                                           self.parse_const.CHECK_FA_PORT_STATS_ASGN_REJECTED, True,
                                           "Fabric Attach port stats assignments rejected is"
                                           " {count_operator} {count} on port {port}.",
                                           "Fabric Attach port stats assignments rejected is NOT"
                                           " {count_operator} {count} on port {port}!",
                                           **kwargs)

    def fabricattach_verify_port_stats_assignments_expired(self, device_name, port='', count='', count_operator="=",
                                                           **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will be run against.
        [port]            - The port(s) in which is being verified.
        [count]           - The value to compare against.
        [count_operator]  - The operator (>, <, or =) to be used along with the count argument.
                            If nothing is specified (=) will be used.

        Verifies the number of I-SID/VLAN bindings from received FA I-SID/VLAN Assignment TLVs that have expired on the
        identified port.  The counter is not incremented when bindings are deleted for reasons other than expiration.

        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port),
                "count_operator": count_operator,
                "count": count}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_STATS_PORT,
                                           self.parse_const.CHECK_FA_PORT_STATS_ASGN_EXPIRED, True,
                                           "Fabric Attach port stats assignments expired is"
                                           " {count_operator} {count} on port {port}.",
                                           "Fabric Attach port stats assignments expired is NOT"
                                           " {count_operator} {count} on port {port}!",
                                           **kwargs)

    def fabricattach_verify_port_stats_discovered_auth_failed(self, device_name, port='', count='', count_operator="=",
                                                              **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will be run against.
        [port]            - The port(s) in which is being verified.
        [count]           - The value to compare against.
        [count_operator]  - The operator (>, <, or =) to be used along with the count argument.
                            If nothing is specified (=) will be used.

        Verifies the number of received FA Element TLVs for which authentication
        was attempted and failed on the identified port.
        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port),
                "count_operator": count_operator,
                "count": count}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_STATS_PORT,
                                           self.parse_const.CHECK_FA_PORT_STATS_DISC_AUTH_FAILED, True,
                                           "Fabric Attach port stats discovered authentications failed is"
                                           " {count_operator} {count} on port {port}.",
                                           "Fabric Attach port stats discovered authentications failed is NOT"
                                           " {count_operator} {count} on port {port}!",
                                           **kwargs)

    def fabricattach_verify_port_stats_discovered_elements_expired(self, device_name, port='', count='',
                                                                   count_operator="=", **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will be run against.
        [port]            - The port(s) in which is being verified.
        [count]           - The value to compare against.
        [count_operator]  - The operator (>, <, or =) to be used along with the count argument.
                            If nothing is specified (=) will be used.

        Verifies the number of discovered FA elements from received FA Element TLVs that have expired  on the
        identified port.  The counter is not incremented when elements are deleted for reasons other than expiration.

        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port),
                "count_operator": count_operator,
                "count": count}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_STATS_PORT,
                                           self.parse_const.CHECK_FA_PORT_STATS_DISC_ELEM_EXPIRED, True,
                                           "Fabric Attach port stats discovered elements expired is"
                                           " {count_operator} {count} on port {port}.",
                                           "Fabric Attach port stats discovered elements expired is NOT"
                                           " {count_operator} {count} on port {port}!",
                                           **kwargs)

    def fabricattach_verify_port_stats_discovered_elements_deleted(self, device_name, port='', count='',
                                                                   count_operator="=", **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will be run against.
        [port]            - The port(s) in which is being verified.
        [count]           - The value to compare against.
        [count_operator]  - The operator (>, <, or =) to be used along with the count argument.
                            If nothing is specified (=) will be used.

        Verifies  the number of discovered FA elements from received FA Element TLVs that have been deleted on the
        identified port. The counter is only incremented when elements are deleted for reasons other than expiration.
        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port),
                "count_operator": count_operator,
                "count": count}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_STATS_PORT,
                                           self.parse_const.CHECK_FA_PORT_STATS_DISC_ELEM_DELETED, True,
                                           "Fabric Attach port stats discovered elements deleted is"
                                           " {count_operator} {count} on port {port}.",
                                           "Fabric Attach port stats discovered elements deleted is NOT"
                                           " {count_operator} {count} on port {port}!",
                                           **kwargs)

    def fabricattach_verify_port_stats_assignments_deleted(self, device_name, port='', count='', count_operator="=",
                                                           **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will be run against.
        [port]            - The port(s) in which is being verified.
        [count]           - The value to compare against.
        [count_operator]  - The operator (>, <, or =) to be used along with the count argument.
                            If nothing is specified (=) will be used.

        Verifies  the number of I-SID/VLAN bindings from received FA I-SID/VLAN Assignment TLVs
        that have been deleted on the identified port.
        The counter is only incremented when bindings are deleted for reasons other than expiration.
        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port),
                "count_operator": count_operator,
                "count": count}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_STATS_PORT,
                                           self.parse_const.CHECK_FA_PORT_STATS_ASGN_DELETED, True,
                                           "Fabric Attach port stats assignments deleted is"
                                           " {count_operator} {count} on port {port}.",
                                           "Fabric Attach port stats assignments deleted is NOT"
                                           " {count_operator} {count} on port {port}!",
                                           **kwargs)

    def fabricattach_verify_port_stats_assignment_auth_failed(self, device_name, port='', count='', count_operator="=",
                                                              **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will be run against.
        [port]            - The port(s) in which is being verified.
        [count]           - The value to compare against.
        [count_operator]  - The operator (>, <, or =) to be used along with the count argument.
                            If nothing is specified (=) will be used.

        Verifies the number of received FA I-SID/VLAN Assignment TLVs for which authentication was
        attempted and failed on the identified port.
        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port),
                "count_operator": count_operator,
                "count": count}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_STATS_PORT,
                                           self.parse_const.CHECK_FA_PORT_STATS_ASGN_AUTH_FAILED, True,
                                           "Fabric Attach port stats assignment authentications failed is"
                                           " {count_operator} {count} on port {port}.",
                                           "Fabric Attach port stats assignment authentications failed is NOT"
                                           " {count_operator} {count} on port {port}!",
                                           **kwargs)

    def fabricattach_verify_zero_touch_client_to_isid_auto_attach_map(self, device_name, client_name='', i_sid='',
                                                                      **kwargs):
        """
        Keyword Arguments:
        [device_name]   - The device the keyword should be run against.
        [i_sid]         - The Fabric Attach management i-sid. Values: 0..16777215
        [client_name]   - The Fabric Attach standard client name.
                          Valid values:

                          wap-type1
                          wap-type2
                          switch
                          router
                          phone
                          camera
                          video
                          security-device
                          virtual-switch
                          srvr-endpt
                          ona-sdn
                          ona-spb-over-ip

        Verifies the auto-attach mapping of the Fabric Attach I-SID component to the Zero Touch Client standard name.
        """
        args = {"name": client_name,
                "oid_index": SnmpUtils().fa_zero_touch_client(client_name),
                "i_sid": i_sid}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_ZERO_TOUCH_CLIENT,
                                           self.parse_const.CHECK_FA_ZERO_TOUCH_CLIENT_AUTO_ATTACH_ISID, True,
                                           "Fabric Attach zero-touch-client name {name} is auto-attached"
                                           " to i-sid {i_sid}.",
                                           "Fabric Attach zero-touch-client name {name} is NOT auto-attached"
                                           " to i-sid {i_sid}!",
                                           **kwargs)

    def fabricattach_verify_zero_touch_client_to_vlan_auto_attach_map(self, device_name, client_name='',
                                                                      vlan_or_untagged='', **kwargs):
        """
        Keyword Arguments:
        [device_name]         - The device the keyword should be run against.
        [vlan_or_untagged]    - The Fabric Attach numeric VLAN ID component of the Zero Touch Client auto-attach
                                specification.
                                A value of "untagged" indicates that a VLAN has not been specified
                                (e.g., an untagged traffic environment).
        [client_name]         - The Fabric Attach standard client name.
                                Valid values:

                                wap-type1
                                wap-type2
                                switch
                                router
                                phone
                                camera
                                video
                                security-device
                                virtual-switch
                                srvr-endpt
                                ona-sdn
                                ona-spb-over-ip

        Verifies the auto-attach mapping of the Fabric Attach VLAN component to the Zero Touch Client standard name.
        """
        args = {"name": client_name,
                "oid_index": SnmpUtils().fa_zero_touch_client(client_name),
                "vlan_or_untagged": vlan_or_untagged}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_ZERO_TOUCH_CLIENT,
                                           self.parse_const.CHECK_FA_ZERO_TOUCH_CLIENT_AUTO_ATTACH_VLAN, True,
                                           "Fabric Attach zero-touch-client name {name} is auto-attached"
                                           " to vlan {vlan_or_untagged}.",
                                           "Fabric Attach zero-touch-client name {name} is NOT auto-attached"
                                           " to vlan {vlan_or_untagged}!",
                                           **kwargs)

    def fabricattach_verify_zero_touch_client_name_exists(self, device_name, client_name='', **kwargs):
        """
        Keyword Arguments:
        [device_name]  - The device the keyword should be run against.
        [client_name]   - The Fabric Attach standard client name.
                          Valid values:

                          wap-type1
                          wap-type2
                          switch
                          router
                          phone
                          camera
                          video
                          security-device
                          virtual-switch
                          srvr-endpt
                          ona-sdn
                          ona-spb-over-ip

        Verifies that an auto-attach mapping of the Fabric Attach the Zero Touch Client standard name exists.
        """
        args = {"name": client_name,
                "oid_index": SnmpUtils().fa_zero_touch_client(client_name)}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_ZERO_TOUCH_CLIENT,
                                           self.parse_const.CHECK_FA_ZERO_TOUCH_CLIENT_AUTO_ATTACH_NAME, True,
                                           "Fabric Attach zero-touch-client name {name} exists.",
                                           "Fabric Attach zero-touch-client name {name} does NOT exist!",
                                           **kwargs)

    def fabricattach_verify_zero_touch_client_name_does_not_exist(self, device_name, client_name='', **kwargs):
        """
        Keyword Arguments:
        [device_name]  - The device the keyword should be run against.
        [client_name]   - The Fabric Attach standard client name.
                          Valid values:

                          wap-type1
                          wap-type2
                          switch
                          router
                          phone
                          camera
                          video
                          security-device
                          virtual-switch
                          srvr-endpt
                          ona-sdn
                          ona-spb-over-ip

        Verifies that an auto-attach mapping of the Fabric Attach the Zero Touch Client standard name does not exist.
        """
        args = {"name": client_name,
                "oid_index": SnmpUtils().fa_zero_touch_client(client_name)}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_ZERO_TOUCH_CLIENT,
                                           self.parse_const.CHECK_FA_ZERO_TOUCH_CLIENT_AUTO_ATTACH_NAME, False,
                                           "Fabric Attach zero-touch-client name {name} does not exist.",
                                           "Fabric Attach zero-touch-client name {name} exists!",
                                           **kwargs)

    def fabricattach_verify_isid_port_platform_vlan(self, device_name, port='', isid='', vlan='', **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will be run against.
        [port]            - The port which is being verified.
        [isid]            - A numeric value that uniquely identifies the i-sid of the isid interface.
        [vlan]            - A numeric value that uniquely identifies the platform VLAN of the I-SID interface.

        Verifies the port and platform VLAN of the I-SID.
        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port) + "." + isid,
                "isid": isid,
                "vlan": vlan}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISID,
                                           self.parse_const.CHECK_FA_ISID_PORT_PLAT_VLAN, True,
                                           "Fabric Attach I-SID {isid} platform VLAN {vlan}"
                                           " exists on port {port}.",
                                           "Fabric Attach I-SID {isid} platform VLAN {vlan}"
                                           " does NOT exist on port {port}!",
                                           **kwargs)

    def fabricattach_verify_isid_port_isid_cvid(self, device_name, port='', isid='', cvid='', **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will be run against.
        [port]            - The port which is being verified.
        [isid]            - A numeric value that uniquely identifies the i-sid of the I-SID interface.
        [cvid]            - The A value that uniquely identifies the customer vid of this isid interface.
                            4095 is not used.
                            Use 'u' for the untagged case.

        Verifies the port and I-SID along with the CVID portion of the I-SID.
        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port) + "." + isid,
                "isid": isid,
                "cvid": cvid}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISID,
                                           self.parse_const.CHECK_FA_ISID_PORT_CVID, True,
                                           "Fabric Attach I-SID {isid} CVID {cvid}"
                                           " exists on port {port}.",
                                           "Fabric Attach I-SID {isid} CVID {cvid}"
                                           " does NOT exist on port {port}!",
                                           **kwargs)

    def fabricattach_verify_isid_port_isid_type(self, device_name, port='', isid='', i_type='', **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will be run against.
        [port]            - The port which is being verified.
        [isid]            - A numveric value that uniquely identifies the i-sid of the I-SID interface.
        [i_type]          - The I-SID type of service on an interface.
                            Values:
                              ELAN_TRANS
                              ELAN
                              ETREE
                              L2VSN

        Verifies the port and I-SID service type of the I-SID.
        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port) + "." + isid,
                "isid": isid,
                "i_type": i_type}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISID,
                                           self.parse_const.CHECK_FA_ISID_PORT_ISID_TYPE, True,
                                           "Fabric Attach I-SID {isid} I-SID type {i_type}"
                                           " exists on port {port}.",
                                           "Fabric Attach I-SID {isid} I-SID type {i_type}"
                                           " does NOT exist on port {port}!",
                                           **kwargs)

    def fabricattach_verify_isid_port_isid_origin(self, device_name, port='', isid='', i_origin='', **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will be run against.
        [port]            - The port which is being verified.
        [isid]            - A numeric value that uniquely identifies the i-sid of the isid interface.
        [i_origin]        - The origin of service associated with the I-SID interface.
                            Values:
                              CONFIG
                              DISC_LOCAL
                              DISC_REMOTE
                              MANAGEMENT
                              DISC_BOTH
                              SPBM
                              MGMT_DISC_LOCAL
                              MGMT_DISC_REMOTE
                              MGMT_DISC_BOTH

        Verifies the port and origin of service associated with the I-SID interface.
        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port) + "." + isid,
                "isid": isid,
                "i_origin": i_origin}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISID,
                                           self.parse_const.CHECK_FA_ISID_PORT_ORIGIN, True,
                                           "Fabric Attach I-SID {isid} I-SID origin {i_origin}"
                                           " exists on port {port}.",
                                           "Fabric Attach I-SID {isid} I-SID origin {i_origin}"
                                           " does NOT exist on port {port}!",
                                           **kwargs)

    def fabricattach_verify_isid_mlt_platform_vlan(self, device_name, mlt_id='', isid='', vlan='', **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will be run against.
        [mlt_id]          - The MLT which is being verified.
        [isid]            - A numeric value that uniquely identifies the i-sid of the isid interface.
        [vlan]            - A numeric value that uniquely identifies the platform VLAN of the I-SID interface.

        Verifies the MLT and platform VLAN of the I-SID.
        """
        args = {"mlt_id": mlt_id,
                "oid_index": SnmpUtils().get_mlt_logical_index(device_name, mlt_id) + "." + isid,
                "isid": isid,
                "vlan": vlan}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISID,
                                           self.parse_const.CHECK_FA_ISID_MLT_PLAT_VLAN, True,
                                           "Fabric Attach I-SID {isid} platform VLAN {vlan}"
                                           " exists on MLT {mlt_id}.",
                                           "Fabric Attach I-SID {isid} platform VLAN {vlan}"
                                           " does NOT exist on MLT {mlt_id}!",
                                           **kwargs)

    def fabricattach_verify_isid_mlt_isid_cvid(self, device_name, mlt_id='', isid='', cvid='', **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will be run against.
        [mlt_id]          - The MLT which is being verified.
        [isid]            - A numeric value that uniquely identifies the i-sid of the I-SID interface.
        [cvid]            - The A value that uniquely identifies the customer vid of this isid interface.
                            4095 is not used.
                            Use 'u' for the untagged case.

        Verifies the MLT and ISID along with the CVID portion of the I-SID.
        """
        args = {"mlt_id": mlt_id,
                "oid_index": SnmpUtils().get_mlt_logical_index(device_name, mlt_id) + "." + isid,
                "isid": isid,
                "cvid": cvid}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISID,
                                           self.parse_const.CHECK_FA_ISID_MLT_CVID, True,
                                           "Fabric Attach I-SID {isid} CVID {cvid}"
                                           " exists on MLT {mlt_id}.",
                                           "Fabric Attach I-SID {isid} CVID {cvid}"
                                           " does NOT exist on MLT {mlt_id}!",
                                           **kwargs)

    def fabricattach_verify_isid_mlt_isid_type(self, device_name, mlt_id='', isid='', i_type='', **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will be run against.
        [mlt_id]          - The MLT which is being verified.
        [isid]            - A numveric value that uniquely identifies the i-sid of the I-SID interface.
        [i_type]          - The I-SID type of service on an interface.
                            Values:
                              ELAN_TRANS
                              ELAN
                              ETREE
                              L2VSN

        Verifies the MLT and I-SID service type of the I-SID.
        """
        args = {"mlt_id": mlt_id,
                "oid_index": SnmpUtils().get_mlt_logical_index(device_name, mlt_id) + "." + isid,
                "isid": isid,
                "i_type": i_type}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISID,
                                           self.parse_const.CHECK_FA_ISID_MLT_ISID_TYPE, True,
                                           "Fabric Attach I-SID {isid} I-SID type {i_type}"
                                           " exists on MLT {mlt_id}.",
                                           "Fabric Attach I-SID {isid} I-SID type {i_type}"
                                           " does NOT exist on MLT {mlt_id}!",
                                           **kwargs)

    def fabricattach_verify_isid_mlt_isid_origin(self, device_name, mlt_id='', isid='', i_origin='', **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will be run against.
        [mlt_id]          - The MLT which is being verified.
        [isid]            - A numeric value that uniquely identifies the i-sid of the isid interface.
        [i_origin]        - The origin of service associated with the I-SID interface.
                            Values:
                              CONFIG
                              DISC_LOCAL
                              DISC_REMOTE
                              MANAGEMENT
                              DISC_BOTH
                              SPBM
                              MGMT_DISC_LOCAL
                              MGMT_DISC_REMOTE
                              MGMT_DISC_BOTH

        Verifies the MLT and origin of service associated with the I-SID interface.
        """
        args = {"mlt_id": mlt_id,
                "oid_index": SnmpUtils().get_mlt_logical_index(device_name, mlt_id) + "." + isid,
                "isid": isid,
                "i_origin": i_origin}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISID,
                                           self.parse_const.CHECK_FA_ISID_MLT_ORIGIN, True,
                                           "Fabric Attach I-SID {isid} I-SID origin {i_origin}"
                                           " exists on mlt {mlt_id}.",
                                           "Fabric Attach I-SID {isid} I-SID origin {i_origin}"
                                           " does NOT exist on MLT {mlt_id}!",
                                           **kwargs)
