"""
Keyword class for all mlt cli commands.
"""
from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import NetworkElementKeywordBaseClass
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.Constants.MltConstants import \
    MltConstants as ParseConstants
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.Constants.MltConstants import \
    MltConstants as CommandConstants
# All imports above this line will be removed after generation.
# User imports must be added below.


class NetworkElementMltGenKeywords(NetworkElementKeywordBaseClass):
    def __init__(self):
        super(NetworkElementMltGenKeywords, self).__init__()
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()
        self.api_const = "mlt"

    def mlt_create_id(self, device_name, mlt_id='', **kwargs):
        """
        Description: Creates the MLT instance and enables it.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "mlt_id": mlt_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CREATE_ID,
                                    **kwargs)

    def mlt_delete_id(self, device_name, mlt_id='', **kwargs):
        """
        Description: Removes the MLT instance.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "mlt_id": mlt_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DELETE_ID,
                                    **kwargs)

    def mlt_enable_flex_uni(self, device_name, mlt_id='', **kwargs):
        """
        Description: Enables flex-uni on the MLT instanceEnables flex-uni on the MLT instance.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "mlt_id": mlt_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_FLEX_UNI,
                                    **kwargs)

    def mlt_disable_flex_uni(self, device_name, mlt_id='', **kwargs):
        """
        Description: Disables flex-uni on the MLT instance.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "mlt_id": mlt_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_FLEX_UNI,
                                    **kwargs)

    def mlt_enable_lacp(self, device_name, mlt_id='', **kwargs):
        """
        Description: Enables LACP on the MLT instance.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "mlt_id": mlt_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_LACP,
                                    **kwargs)

    def mlt_disable_lacp(self, device_name, mlt_id='', **kwargs):
        """
        Description: Disables LACP on the MLT instance.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "mlt_id": mlt_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_LACP,
                                    **kwargs)

    def mlt_set_port_member(self, device_name, mlt_id='', port='', **kwargs):
        """
        Description: Adds a port to the MLT.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "mlt_id": mlt_id,
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PORT_MEMBER,
                                    **kwargs)

    def mlt_clear_port_member(self, device_name, mlt_id='', port='', **kwargs):
        """
        Description: Removes a port from the MLT.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "mlt_id": mlt_id,
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_PORT_MEMBER,
                                    **kwargs)

    def mlt_set_type_split_mlt(self, device_name, mlt_id='', **kwargs):
        """
        Description: Configures the MLT instance to a split MLT.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "mlt_id": mlt_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_TYPE_SPLIT_MLT,
                                    **kwargs)

    def mlt_set_type_normal_mlt(self, device_name, mlt_id='', **kwargs):
        """
        Description: Configures the MLT instance to a normal MLT.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "mlt_id": mlt_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_TYPE_NORMAL_MLT,
                                    **kwargs)

    def mlt_set_encapsulation_dot1q(self, device_name, mlt_id='', **kwargs):
        """
        Description: Enables trunking on the MLT instance.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "mlt_id": mlt_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_ENCAPSULATION_DOT1Q,
                                    **kwargs)

    def mlt_clear_encapsulation_dot1q(self, device_name, mlt_id='', **kwargs):
        """
        Description: Disables trunking on the MLT instance.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "mlt_id": mlt_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_ENCAPSULATION_DOT1Q,
                                    **kwargs)

    # ##################################################################################################################
    #   Inspection Keywords   ##########################################################################################
    # ##################################################################################################################

    def mlt_verify_id_exists(self, device_name, mlt_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will run against.
        [mlt_id]      - The value that uniquely identifies the Multi-Link Trunk
                        Values:  1..512

        Verifies the MLT instance exists.
        """
        args = {"mlt_id": mlt_id,
                "oid_index": mlt_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ID,
                                           self.parse_const.CHECK_MLT_EXISTS, True,
                                           "MLT {mlt_id} exists on {device_name}.",
                                           "MLT {mlt_id} does not exist on {device_name}!",
                                           **kwargs)

    def mlt_verify_id_does_not_exist(self, device_name, mlt_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will run against.
        [mlt_id]      - The value that uniquely identifies the Multi-Link Trunk
                        Values:  1..512

        Verifies the MLT instance does not exist.
        """
        args = {"mlt_id": mlt_id,
                "oid_index": mlt_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ID,
                                           self.parse_const.CHECK_MLT_EXISTS, False,
                                           "MLT {mlt_id} does not exist on {device_name}.",
                                           "MLT {mlt_id} exists on {device_name}!",

                                           **kwargs)

    def mlt_verify_admin_mode_split(self, device_name, mlt_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will run against.
        [mlt_id]      - The value that uniquely identifies the Multi-Link Trunk
                        Values:  1..512

        Verifies the MLT instance is configured as a split MLT.
        """
        args = {"mlt_id": mlt_id,
                "oid_index": mlt_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ADMIN_TYPE,
                                           self.parse_const.CHECK_MLT_ADMIN_TYPE_SPLIT, True,
                                           "MLT {mlt_id} is configured as a split MLT on {device_name}.",
                                           "MLT {mlt_id} is NOT configured as a split MLT on {device_name}!",
                                           **kwargs)

    def mlt_verify_admin_mode_normal(self, device_name, mlt_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will run against.
        [mlt_id]      - The value that uniquely identifies the Multi-Link Trunk
                        Values:  1..512

        Verifies the MLT instance is configured as a normal MLT.
        """
        args = {"mlt_id": mlt_id,
                "oid_index": mlt_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ADMIN_TYPE,
                                           self.parse_const.CHECK_MLT_ADMIN_TYPE_NORMAL, True,
                                           "MLT {mlt_id} is configured as a normal MLT on {device_name}.",
                                           "MLT {mlt_id} is NOT configured as a normal MLT on {device_name}!",
                                           **kwargs)

    def mlt_verify_oper_mode_split(self, device_name, mlt_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will run against.
        [mlt_id]      - The value that uniquely identifies the Multi-Link Trunk
                        Values:  1..512

        Verifies the MLT instance is operating as a split MLT.
        """
        args = {"mlt_id": mlt_id,
                "oid_index": mlt_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RUNNING_TYPE,
                                           self.parse_const.CHECK_MLT_RUNNING_TYPE_SPLIT, True,
                                           "MLT {mlt_id} is running as a split MLT on {device_name}.",
                                           "MLT {mlt_id} is NOT running as a split MLT on {device_name}!",
                                           **kwargs)

    def mlt_verify_oper_mode_normal(self, device_name, mlt_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will run against.
        [mlt_id]      - The value that uniquely identifies the Multi-Link Trunk
                        Values:  1..512

        Verifies the MLT instance is operating as a normal MLT.
        """
        args = {"mlt_id": mlt_id,
                "oid_index": mlt_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RUNNING_TYPE,
                                           self.parse_const.CHECK_MLT_RUNNING_TYPE_NORMAL, True,
                                           "MLT {mlt_id} is running as a normal MLT on {device_name}.",
                                           "MLT {mlt_id} is NOT running as a normal MLT on {device_name}!",
                                           **kwargs)

    def mlt_verify_flex_uni_enabled(self, device_name, mlt_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will run against.
        [mlt_id]      - The value that uniquely identifies the Multi-Link Trunk
                        Values:  1..512

        Verifies the MLT instance is enabled for flex-uni.
        """
        args = {"mlt_id": mlt_id,
                "oid_index": mlt_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_FLEX_UNI_STATUS,
                                           self.parse_const.CHECK_MLT_FLEX_UNI_STATUS, True,
                                           "MLT {mlt_id} FLEX-UNI is enabled on {device_name}.",
                                           "MLT {mlt_id} FLEX-UNI is NOT enabled on {device_name}!",
                                           **kwargs)

    def mlt_verify_flex_uni_disabled(self, device_name, mlt_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will run against.
        [mlt_id]      - The value that uniquely identifies the Multi-Link Trunk
                        Values:  1..512

        Verifies the MLT instance is disabled for flex-uni.
        """
        args = {"mlt_id": mlt_id,
                "oid_index": mlt_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_FLEX_UNI_STATUS,
                                           self.parse_const.CHECK_MLT_FLEX_UNI_STATUS, False,
                                           "MLT {mlt_id} FLEX-UNI is disabled on {device_name}.",
                                           "MLT {mlt_id} FLEX-UNI is NOT disabled on {device_name}!",
                                           **kwargs)

    def mlt_verify_lacp_enabled(self, device_name, mlt_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will run against.
        [mlt_id]      - The value that uniquely identifies the Multi-Link Trunk
                        Values:  1..512

        Verifies the MLT instance is administratively enabled for LACP.
        """
        args = {"mlt_id": mlt_id,
                "oid_index": mlt_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_LACP_ADMIN_STATUS,
                                           self.parse_const.CHECK_MLT_LACP_ADMIN_STATUS, True,
                                           "MLT {mlt_id} LACP is configured as enabled on {device_name}.",
                                           "MLT {mlt_id} LACP is NOT configured as enabled on {device_name}!",
                                           **kwargs)

    def mlt_verify_lacp_disabled(self, device_name, mlt_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will run against.
        [mlt_id]      - The value that uniquely identifies the Multi-Link Trunk
                        Values:  1..512

        Verifies the MLT instance is administratively disabled for LACP.
        """
        args = {"mlt_id": mlt_id,
                "oid_index": mlt_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_LACP_ADMIN_STATUS,
                                           self.parse_const.CHECK_MLT_LACP_ADMIN_STATUS, False,
                                           "MLT {mlt_id} LACP is configured as disabled on {device_name}.",
                                           "MLT {mlt_id} LACP is NOT configured as disabled on {device_name}!",
                                           **kwargs)

    def mlt_verify_lacp_oper_up(self, device_name, mlt_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will run against.
        [mlt_id]      - The value that uniquely identifies the Multi-Link Trunk
                        Values:  1..512

        Verifies the MLT instance is operationally up for LACP.
        """
        args = {"mlt_id": mlt_id,
                "oid_index": mlt_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_LACP_OPER_STATUS,
                                           self.parse_const.CHECK_MLT_LACP_OPER_STATUS, True,
                                           "MLT {mlt_id} LACP is operationally UP on {device_name}.",
                                           "MLT {mlt_id} LACP is operationally DOWN on {device_name}!",
                                           **kwargs)

    def mlt_verify_lacp_oper_down(self, device_name, mlt_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will run against.
        [mlt_id]      - The value that uniquely identifies the Multi-Link Trunk
                        Values:  1..512

        Verifies the MLT instance is operationally down for LACP.
        """
        args = {"mlt_id": mlt_id,
                "oid_index": mlt_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_LACP_OPER_STATUS,
                                           self.parse_const.CHECK_MLT_LACP_OPER_STATUS, False,
                                           "MLT {mlt_id} LACP is operationally DOWN on {device_name}.",
                                           "MLT {mlt_id} LACP is operationally UP on {device_name}!",
                                           **kwargs)

    def mlt_verify_port_exists(self, device_name, mlt_id='', ports='', **kwargs):
        """
        Keyword Arguments:
        [device_name]   - The device the keyword should be run against.
        [mlt_id]        - The unique numeric identifier representing the MLT.
        [ports]         - The port(s) to be checked on the MLT.

        Verifies ports on the designated MLT exist.
        """
        args = {"mlt_id": mlt_id,
                "port": ports}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORTS,
                                           self.parse_const.CHECK_MLT_PORT, True,
                                           "Port {port} is assigned on MLT {mlt_id}.",
                                           "Port {port} is NOT assigned on MLT {mlt_id}!",
                                           **kwargs)

    def mlt_verify_port_does_not_exist(self, device_name, mlt_id='', ports='', **kwargs):
        """
        Keyword Arguments:
        [device_name]   - The device the keyword should be run against.
        [mlt_id]        - The unique numeric identifier representing the MLT.
        [ports]         - The port(s) to be checked on the MLT.

        Verifies ports on the designated MLT do not exist.
        """
        args = {"mlt_id": mlt_id,
                "port": ports}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORTS,
                                           self.parse_const.CHECK_MLT_PORT, False,
                                           "Port {port} is not assigned on MLT {mlt_id}.",
                                           "Port {port} is assigned on MLT {mlt_id}!",
                                           **kwargs)

    def mlt_verify_encapsulation_dot1q(self, device_name, mlt_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will run against.
        [mlt_id]      - The value that uniquely identifies the Multi-Link Trunk
                        Values:  1..512

        Verifies the MLT instance is is enabled for trunking.
        """
        args = {"mlt_id": mlt_id,
                "oid_index": mlt_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ENCAPSULATION,
                                           self.parse_const.CHECK_MLT_TRUNKING, True,
                                           "MLT {mlt_id} encapsulation is enabled on {device_name}.",
                                           "MLT {mlt_id} encapsulation is disabled on {device_name}!",
                                           **kwargs)

    def mlt_verify_encapsulation_not_dot1q(self, device_name, mlt_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will run against.
        [mlt_id]      - The value that uniquely identifies the Multi-Link Trunk
                        Values:  1..512

        Verifies the MLT instance is is disabled for trunking.
        """
        args = {"mlt_id": mlt_id,
                "oid_index": mlt_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ENCAPSULATION,
                                           self.parse_const.CHECK_MLT_TRUNKING, False,
                                           "MLT {mlt_id} encapsulation is disabled on {device_name}.",
                                           "MLT {mlt_id} encapsulation is enabled on {device_name}!",
                                           **kwargs)
