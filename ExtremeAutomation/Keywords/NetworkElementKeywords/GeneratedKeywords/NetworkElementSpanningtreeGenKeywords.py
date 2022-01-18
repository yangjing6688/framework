"""
Keyword class for all spanningtree cli commands.
"""
from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import NetworkElementKeywordBaseClass
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.Constants.SpanningtreeConstants import \
    SpanningtreeConstants as ParseConstants
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.Constants.SpanningtreeConstants import \
    SpanningtreeConstants as CommandConstants
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Keywords.NetworkElementKeywords.Utils.NetworkElementSnmpUtils \
    import NetworkElementSnmpUtils as SnmpUtils


class NetworkElementSpanningtreeGenKeywords(NetworkElementKeywordBaseClass):
    def __init__(self):
        super(NetworkElementSpanningtreeGenKeywords, self).__init__()
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()
        self.api_const = "spanningtree"

    def spanningtree_enable_global(self, device_name, **kwargs):
        """
        Description: Globally enables Spanning Tree.

        Supported Agents and OS:
            CLI: EOS, EXOS, SLX
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_GLOBAL,
                                    **kwargs)

    def spanningtree_disable_global(self, device_name, **kwargs):
        """
        Description: Globally disables Spanning Tree.

        Supported Agents and OS:
            CLI: EOS, EXOS, SLX
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_GLOBAL,
                                    **kwargs)

    def spanningtree_create_mst_instance(self, device_name, sid='', **kwargs):
        """
        Description: Creates a new MST instance with the provided SID.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "sid": sid
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CREATE_MST_INSTANCE,
                                    **kwargs)

    def spanningtree_delete_mst_instance(self, device_name, sid='', **kwargs):
        """
        Description: Deletes the MST instance with the provided SID.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "sid": sid
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DELETE_MST_INSTANCE,
                                    **kwargs)

    def spanningtree_enable_port_admin(self, device_name, port='', sid='', **kwargs):
        """
        Description: Enables STP Port Admin on the specified port(s).

        Supported Agents and OS:
            CLI: EOS, EXOS, VOSS
        """
        args = {
            "port": port,
            "sid": sid
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_PORT_ADMIN,
                                    **kwargs)

    def spanningtree_disable_port_admin(self, device_name, port='', sid='', **kwargs):
        """
        Description: Disables STP Port Admin on the specified port(s).

        Supported Agents and OS:
            CLI: EOS, EXOS, VOSS
        """
        args = {
            "port": port,
            "sid": sid
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_PORT_ADMIN,
                                    **kwargs)

    def spanningtree_enable_auto_edge(self, device_name, port='', sid='', **kwargs):
        """
        Description: Enables STP auto-edge on the specified port(s).

        Supported Agents and OS:
            CLI: EOS, EXOS, SLX
        """
        args = {
            "port": port,
            "sid": sid
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_AUTO_EDGE,
                                    **kwargs)

    def spanningtree_disable_auto_edge(self, device_name, port='', sid='', **kwargs):
        """
        Description: Disables STP auto-edge on the specified port(s).

        Supported Agents and OS:
            CLI: EOS, EXOS, SLX
        """
        args = {
            "port": port,
            "sid": sid
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_AUTO_EDGE,
                                    **kwargs)

    def spanningtree_set_stp_mode(self, device_name, mode='', sid='', msti='', **kwargs):
        """
        Description: Configures Spanning Tree to use the given mode.

        Supported Agents and OS:
            CLI: EOS, EXOS, VOSS
        """
        args = {
            "mode": mode,
            "msti": msti,
            "sid": sid
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_STP_MODE,
                                    **kwargs)

    def spanningtree_clear_stp_mode(self, device_name, msti='', sid='', **kwargs):
        """
        Description: Configures Spanning Tree to use the MSTP mode.

        Supported Agents and OS:
            CLI: EOS, EXOS, VOSS
        """
        args = {
            "msti": msti,
            "sid": sid
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_STP_MODE,
                                    **kwargs)

    def spanningtree_set_restricted_role(self, device_name, port='', sid='', state='', **kwargs):
        """
        Description: Configures the Restricted Role for the specified port.

        Supported Agents and OS:
            CLI: EOS, EXOS, SLX
        """
        args = {
            "port": port,
            "sid": sid,
            "state": state
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_RESTRICTED_ROLE,
                                    **kwargs)

    def spanningtree_set_restricted_tcn(self, device_name, port='', sid='', state='', **kwargs):
        """
        Description: Configures the Restricted TCN for the specified port.

        Supported Agents and OS:
            CLI: EOS, EXOS, SLX
        """
        args = {
            "port": port,
            "sid": sid,
            "state": state
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_RESTRICTED_TCN,
                                    **kwargs)

    def spanningtree_set_priority(self, device_name, priority='', port='', sid='', **kwargs):
        """
        Description: Configures the spanning tree priority to the provided value.

        Supported Agents and OS:
            CLI: EOS, EXOS, SLX, VOSS
        """
        args = {
            "port": port,
            "priority": priority,
            "sid": sid
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PRIORITY,
                                    **kwargs)

    def spanningtree_set_priority_mode(self, device_name, mode='', sid='', **kwargs):
        """
        Description: Configures the Spanning Tree bridge priority mode.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "mode": mode,
            "sid": sid
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PRIORITY_MODE,
                                    **kwargs)

    def spanningtree_set_tc_trap(self, device_name, state='', sid='', **kwargs):
        """
        Description: Enables sending of STP Topology Change Traps.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "sid": sid,
            "state": state
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_TC_TRAP,
                                    **kwargs)

    def spanningtree_clear_tc_trap(self, device_name, sid='', state='', **kwargs):
        """
        Description: Disables sending of STP Topology Change Traps.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "sid": sid,
            "state": state
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_TC_TRAP,
                                    **kwargs)

    def spanningtree_set_msti_vlan_mapping(self, device_name, vlan='', sid='', **kwargs):
        """
        Description: Maps the specified VLANs to the MSTIs.

        Supported Agents and OS:
            CLI: EOS, EXOS, VOSS
        """
        args = {
            "sid": sid,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_MSTI_VLAN_MAPPING,
                                    **kwargs)

    def spanningtree_clear_msti_vlan_mapping(self, device_name, vlan='', sid='', **kwargs):
        """
        Description: Deletes the Mapping for the specified VLANs and MSTIs.

        Supported Agents and OS:
            CLI: EOS, EXOS, VOSS
        """
        args = {
            "sid": sid,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_MSTI_VLAN_MAPPING,
                                    **kwargs)

    def spanningtree_set_mst_region_name(self, device_name, region='', **kwargs):
        """
        Description: Configures the MST Region Name.

        Supported Agents and OS:
            CLI: EOS, EXOS, SLX, VOSS
        """
        args = {
            "region": region
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_MST_REGION_NAME,
                                    **kwargs)

    def spanningtree_set_mst_revision_level(self, device_name, revision='', **kwargs):
        """
        Description: Configures the MST Revision Level.

        Supported Agents and OS:
            CLI: EOS, EXOS, SLX, VOSS
        """
        args = {
            "revision": revision
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_MST_REVISION_LEVEL,
                                    **kwargs)

    def spanningtree_set_hello_time(self, device_name, hello='', sid='', **kwargs):
        """
        Description: Configures the spanning tree hello timer to the provided value.

        Supported Agents and OS:
            CLI: EOS, EXOS, VOSS
        """
        args = {
            "hello": hello,
            "sid": sid
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_HELLO_TIME,
                                    **kwargs)

    def spanningtree_set_fwd_delay(self, device_name, fwd_delay='', sid='', **kwargs):
        """
        Description: Configures the spanning tree forward delay timer to the provided value.

        Supported Agents and OS:
            CLI: EOS, EXOS, VOSS
        """
        args = {
            "fwd_delay": fwd_delay,
            "sid": sid
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_FWD_DELAY,
                                    **kwargs)

    def spanningtree_set_max_age(self, device_name, max_age='', sid='', **kwargs):
        """
        Description: Configures the spanning tree BPDU max age to the provided value.

        Supported Agents and OS:
            CLI: EOS, EXOS, VOSS
        """
        args = {
            "max_age": max_age,
            "sid": sid
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_MAX_AGE,
                                    **kwargs)

    def spanningtree_enable_mst_instance(self, device_name, sid='', **kwargs):
        """
        Description: Enables a Multiple Spanning Tree instance.

        Supported Agents and OS:
            CLI: EXOS, VOSS
        """
        args = {
            "sid": sid
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_MST_INSTANCE,
                                    **kwargs)

    def spanningtree_disable_mst_instance(self, device_name, sid='', **kwargs):
        """
        Description: Disables a Multiple Spanning Tree instance.

        Supported Agents and OS:
            CLI: EXOS, VOSS
        """
        args = {
            "sid": sid
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_MST_INSTANCE,
                                    **kwargs)

    def spanningtree_enable_vlan_autobind(self, device_name, vlan='', sid='', **kwargs):
        """
        Description: Enables vlan auto-bind for the specified VLAN and Instance.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "sid": sid,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_VLAN_AUTOBIND,
                                    **kwargs)

    def spanningtree_disable_vlan_autobind(self, device_name, vlan='', sid='', **kwargs):
        """
        Description: Disables vlan auto-bind for the specified VLAN and Instance.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "sid": sid,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_VLAN_AUTOBIND,
                                    **kwargs)

    def spanningtree_set_mst_instance_tag(self, device_name, tag='', sid='', **kwargs):
        """
        Description: Configures the EXOS MST instance ID.

        Supported Agents and OS:
            CLI: EXOS, VOSS
        """
        args = {
            "sid": sid,
            "tag": tag
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_MST_INSTANCE_TAG,
                                    **kwargs)

    def spanningtree_set_port_link_type_point_to_point(self, device_name, port='', sid='', **kwargs):
        """
        Description: Configures the Spanning Tree port link type to point-to-point.

        Supported Agents and OS:
            CLI: EXOS, SLX, VOSS
        """
        args = {
            "port": port,
            "sid": sid
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PORT_LINK_TYPE_POINT_TO_POINT,
                                    **kwargs)

    def spanningtree_set_port_link_type_edge(self, device_name, port='', sid='', **kwargs):
        """
        Description: Configures the Spanning Tree port link type to edge.

        Supported Agents and OS:
            CLI: EXOS, SLX, VOSS
        """
        args = {
            "port": port,
            "sid": sid
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PORT_LINK_TYPE_EDGE,
                                    **kwargs)

    def spanningtree_set_instance_msti(self, device_name, sid='', **kwargs):
        """
        Description: Configures the specified instance as an MSTI.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "sid": sid
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_INSTANCE_MSTI,
                                    **kwargs)

    def spanningtree_set_instance_cist(self, device_name, sid='', **kwargs):
        """
        Description: Configures the specified instance as the CIST.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "sid": sid
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_INSTANCE_CIST,
                                    **kwargs)

    def spanningtree_enable_mstp_global(self, device_name, **kwargs):
        """
        Description: Globally enables Multi Spanning Tree.

        Supported Agents and OS:
            CLI: SLX
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_MSTP_GLOBAL,
                                    **kwargs)

    def spanningtree_disable_mstp_global(self, device_name, **kwargs):
        """
        Description: Globally disables Multi Spanning Tree.

        Supported Agents and OS:
            CLI: SLX
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_MSTP_GLOBAL,
                                    **kwargs)

    def spanningtree_enable_rstp_global(self, device_name, **kwargs):
        """
        Description: Globally enables Rapid Spanning Tree.

        Supported Agents and OS:
            CLI: SLX
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_RSTP_GLOBAL,
                                    **kwargs)

    def spanningtree_disable_rstp_global(self, device_name, **kwargs):
        """
        Description: Globally disables Rapid Spanning Tree.

        Supported Agents and OS:
            CLI: SLX
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_RSTP_GLOBAL,
                                    **kwargs)

    def spanningtree_enable_bpduguard(self, device_name, port='', **kwargs):
        """
        Description: Enables bpdu guard on a port.

        Supported Agents and OS:
            CLI: SLX, VOSS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_BPDUGUARD,
                                    **kwargs)

    def spanningtree_disable_bpduguard(self, device_name, port='', **kwargs):
        """
        Description: Disables bpdu guard on a port.

        Supported Agents and OS:
            CLI: SLX, VOSS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_BPDUGUARD,
                                    **kwargs)

    def spanningtree_create_mst_vlan_instance(self, device_name, sid='', vlan='', **kwargs):
        """
        Description: Creates a new VLAN and an MST instance.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "sid": sid,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CREATE_MST_VLAN_INSTANCE,
                                    **kwargs)

    def spanningtree_delete_mst_vlan_instance(self, device_name, vlan='', **kwargs):
        """
        Description: Deletes the MST instance and associated VLAN.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DELETE_MST_VLAN_INSTANCE,
                                    **kwargs)

    def spanningtree_enable_mstp_on_port(self, device_name, port='', **kwargs):
        """
        Description: Enables MSTP on a port.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_MSTP_ON_PORT,
                                    **kwargs)

    def spanningtree_disable_mstp_on_port(self, device_name, port='', **kwargs):
        """
        Description: Disables MSTP on a port.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_MSTP_ON_PORT,
                                    **kwargs)

    def spanningtree_set_boot_flag_rstp(self, device_name, **kwargs):
        """
        Description: Sets the Spanning Tree boot flag to RSTP.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_BOOT_FLAG_RSTP,
                                    **kwargs)

    def spanningtree_set_boot_flag_mstp(self, device_name, **kwargs):
        """
        Description: Sets the Spanning Tree boot flag to MSTP.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_BOOT_FLAG_MSTP,
                                    **kwargs)

    def spanningtree_set_bpduguard_timeout(self, device_name, port='', timeout='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "port": port,
            "timeout": timeout
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_BPDUGUARD_TIMEOUT,
                                    **kwargs)

    def spanningtree_clear_bpduguard_timeout(self, device_name, port='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_BPDUGUARD_TIMEOUT,
                                    **kwargs)

    # ##################################################################################################################
    #   Inspection Keywords   ##########################################################################################
    # ##################################################################################################################

    def spanningtree_verify_enabled(self, device_name, sid="0", **kwargs):
        """
        Keyword Arguments
        [device_name]  - The device, or list of devices, the keyword will be run against.
        [sid]          - The instance, or list of instances, to be enabled.

        Verifies that Spanning Tree is enabled.
        """
        args = {"sid": sid}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INSTANCE_INFO,
                                           self.parse_const.CHECK_SPANNING_TREE_ENABLED, True,
                                           "Spanning Tree is enabled.",
                                           "Spanning Tree is disabled.",
                                           **kwargs)

    def spanningtree_verify_disabled(self, device_name, sid="0", **kwargs):
        """
        Keyword Arguments
        [device_name]  - The device, or list of devices, the keyword will be run against.
        [sid]          - The instance to be disabled.

        Verifies that spanning tree is disabled.
        """
        args = {"sid": sid}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INSTANCE_INFO,
                                           self.parse_const.CHECK_SPANNING_TREE_ENABLED, False,
                                           "Spanning Tree is disabled.",
                                           "Spanning Tree is enabled.",
                                           **kwargs)

    def spanningtree_verify_boot_flag_rstp(self, device_name, **kwargs):
        """
        Keyword Arguments
        [device_name]  - The device, or list of devices, the keyword will be run against.

        Verifies that the Spanning Tree boot config flag is set to rstp
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_BOOT_FLAG,
                                           self.parse_const.CHECK_STP_BOOT_FLAG_IS_RSTP, True,
                                           "The Spanning Tree Boot Config Flag is set to RSTP.",
                                           "The Spanning Tree Boot Config Flag IS NOT set to RSTP!",
                                           **kwargs)

    def spanningtree_verify_boot_flag_mstp(self, device_name, **kwargs):
        """
        Keyword Arguments
        [device_name]  - The device, or list of devices, the keyword will be run against.

        Verifies that the Spanning Tree boot config flag is set to mstp
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_BOOT_FLAG,
                                           self.parse_const.CHECK_STP_BOOT_FLAG_IS_MSTP, True,
                                           "The Spanning Tree Boot Config Flag is set to MSTP.",
                                           "The Spanning Tree Boot Config Flag IS NOT set to MSTP!",
                                           **kwargs)

    def spanningtree_verify_mode_stp(self, device_name, sid="0", **kwargs):
        """
        Keyword Arguments
        [device_name]  - The device, or list of devices, the keyword will be run against.
        [sid]          - The instance to be configured.

        Verifies that spanning tree is configured to version 802.1D.
        """
        args = {"sid": sid,
                "version": "802.1D"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_VERSION,
                                           self.parse_const.CHECK_SPANNING_TREE_VERSION, True,
                                           "Spanning tree version is dot1d.",
                                           "Spanning tree version is not dot1d.",
                                           **kwargs)

    def spanningtree_verify_mode_rstp(self, device_name, sid="0", **kwargs):
        """
        Keyword Arguments
        [device_name]  - The device, or list of devices, the keyword will be run against.
        [sid]          - The instance to be configured.

        Verifies that spanning tree is configured to version 802.1w.
        """
        args = {"sid": sid,
                "version": "802.1W"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_VERSION,
                                           self.parse_const.CHECK_SPANNING_TREE_VERSION, True,
                                           "Spanning tree version is dot1w.",
                                           "Spanning tree version is not dot1w.",
                                           **kwargs)

    def spanningtree_verify_mode_mstp(self, device_name, sid="0", **kwargs):
        """
        Keyword Arguments
        [device_name]  - The device, or list of devices, the keyword will be run against.
        [sid]          - The instance to be configured.

        Verifies that spanning tree is configured to version MSTP.
        """
        args = {"sid": sid,
                "version": "MSTP"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_VERSION,
                                           self.parse_const.CHECK_SPANNING_TREE_VERSION, True,
                                           "Spanning tree version is mstp.",
                                           "Spanning tree version is not mstp.",
                                           **kwargs)

    def spanningtree_verify_bridge_priority(self, device_name, bridge_priority='', sid="0", **kwargs):
        """
        Keyword Arguments
        [device_name]     - The device the keyword will be run against.
        [bridge_priority] - The bridge priority to be configured.
        [sid]             - The instance to be configured.

        Verifies that spanning tree priority is set to the provided value.
        """
        args = {"sid": sid,
                "priority": bridge_priority}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_VERSION,
                                           self.parse_const.CHECK_SPANNING_TREE_BRIDGE_PRIORITY, True,
                                           "Spanning tree priority is set to {priority}.",
                                           "Spanning tree priority is not set to {priority}.",
                                           **kwargs)

    def spanningtree_verify_loop_protect_enabled_on_port(self, device_name, port='', sid="0", **kwargs):
        """
        Keyword Arguments
        [device_name]   - The device the keyword will be run against.
        [port]          - The port, or list of ports, on which loop protect should be enabled.
        [sid]           - The instance to be configured.

        Verifies that spanning tree loop protect is enabled on user specified port.
        """
        args = {"port": port,
                "sid": sid}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_INFO_DETAIL,
                                           self.parse_const.CHECK_SPANNING_TREE_LOOP_PROTECT_ENABLED, True,
                                           "Spanning tree loop protect is enabled on port {port}.",
                                           "Spanning tree loop protect is disabled on port {port}.",
                                           **kwargs)

    def spanningtree_verify_loop_protect_disabled_on_port(self, device_name, port='', sid="0", **kwargs):
        """
        Keyword Arguments
        [device_name]  - The device the keyword will be run against.
        [port]         - The port, or list of ports, on which loop protect should be enabled.
        [sid]          - The instance to be configured.

        Verifies that spanning tree loop protect is disabled on user specified port.
        """
        args = {"port": port,
                "sid": sid}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_INFO_DETAIL,
                                           self.parse_const.CHECK_SPANNING_TREE_LOOP_PROTECT_ENABLED, False,
                                           "Spanning tree loop protect is disabled on port {port}.",
                                           "Spanning tree loop protect is enabled on port {port}.",
                                           **kwargs)

    def spanningtree_verify_spanguard_enabled_on_port(self, device_name, port='', sid="0", **kwargs):
        """
        Keyword Arguments
        [device_name]  - The device the keyword will be run against.
        [port]         - The port, or list of ports, on which loop protect should be enabled.
        [sid]          - The instance to be configured.

        Verifies that spanning tree SpanGuard is enabled on user specified port.
        """
        args = {"port": port,
                "sid": sid}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_INFO_DETAIL,
                                           self.parse_const.CHECK_SPANNING_TREE_SPAN_GUARD_ENABLED, True,
                                           "Spanning tree span guard protect is enabled on port {port}.",
                                           "Spanning tree span guard is disabled on port {port}.",
                                           **kwargs)

    def spanningtree_verify_spanguard_disabled_on_port(self, device_name, port='', sid="0", **kwargs):
        """
        Keyword Arguments
        [device_name]   - The device the keyword will be run against.
        [port]          - The port, or list of ports, on which loop protect should be enabled.
        [sid]           - The instance to be configured.

        Verifies that spanning SpanGuard is disabled on user specified port.
        """
        args = {"port": port,
                "sid": sid}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_INFO_DETAIL,
                                           self.parse_const.CHECK_SPANNING_TREE_SPAN_GUARD_ENABLED, False,
                                           "Spanning tree span guard protect is disabled on port {port}.",
                                           "Spanning tree span guard is enabled on port {port}.",
                                           **kwargs)

    def spanningtree_verify_tc_counter_incremented(self, device_name, increment='', sid="0", **kwargs):
        """
        Keyword Arguments
        [device_name]  - The device the keyword will be run against.
        [increment]    - The amount that the TC counter should increment.
        [sid]          - The instance to be configured.

        Verifies that the Topology Change counter incremented by the specified amount.
        """
        args = {"sid": sid,
                "increment": increment}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INSTANCE_INFO_DETAIL,
                                           self.parse_const.CHECK_SPANNING_TREE_TC_INCREMENTED, True,
                                           "The Spanning Tree TC count incremented by {increment}.",
                                           "The Spanning Tree TC count did not increment by the expected value.",
                                           **kwargs)

    def spanningtree_verify_tc_counter_did_not_increment(self, device_name, sid="0", **kwargs):
        """
        Keyword Arguments
        [device_name]  - The device the keyword will be run against.
        [sid]          - The instance to be configured.

        Verifies that the Topology Change counter did not incremented.
        """
        args = {"sid": sid}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INSTANCE_INFO_DETAIL,
                                           self.parse_const.CHECK_SPANNING_TREE_TC_SAME, True,
                                           "The Spanning Tree TC count did not increment.",
                                           "The Spanning Tree TC count incremented when it shouldn't have.",
                                           **kwargs)

    def spanningtree_verify_root_bridge(self, device_name, root_id='', sid="0", **kwargs):
        """
        Keyword Arguments
        [device_name]  - The device the keyword will be run against.
        [root_id]      - The MAC Address expected to be the Root Bridge.
        [sid]          - The instance to be configured.

        Verifies that the specified MAC address is the Root Bridge.
        """
        args = {"sid": sid,
                "root_id": root_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO_SUMMARY,
                                           self.parse_const.CHECK_SPANNING_TREE_ROOT, True,
                                           "The Root Bridge is {root_id}.",
                                           "The Root Bridge is NOT {root_id}.",
                                           **kwargs)

    def spanningtree_verify_cist_root(self, device_name, root_id='', sid="0", **kwargs):
        """
        Keyword Arguments
        [device_name]  - The device the keyword will be run against.
        [root_id]      - The MAC Address expected to be the CIST Root Bridge.
        [sid]          - The instance to be configured.

        Verifies that the specified MAC address is the CIST Root Bridge.
        """
        args = {"sid": sid,
                "root_id": root_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO_DETAIL,
                                           self.parse_const.CHECK_SPANNING_TREE_CIST_ROOT, True,
                                           "The Root Bridge is {root_id}.",
                                           "The Root Bridge is NOT {root_id}.",
                                           **kwargs)

    def spanningtree_verify_mstp_cist_regional_root(self, device_name, root_id='', sid="0", **kwargs):
        """
        Keyword Arguments
        [device_name]  - The device the keyword will be run against.
        [root_id]      - The MAC Address expected to be the CIST Regional Root Bridge.
        [sid]          - The instance to be configured.

        Verifies that the specified MAC address is the CIST Regional Root Bridge.
        """
        args = {"sid": sid,
                "root_id": root_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INSTANCE_INFO_DETAIL,
                                           self.parse_const.CHECK_CIST_REGIONAL_ROOT, True,
                                           "The CIST Regional Root Bridge is {root_id}.",
                                           "The CIST Regional Root Bridge is NOT {root_id}.",
                                           **kwargs)

    def spanningtree_verify_mstp_regional_root(self, device_name, sid='', reg_root='', **kwargs):
        """
        Keyword Arguments
        [device_name]  - The device the keyword will be run against.
        [root_id]      - The MAC Address expected to be the MSTI Regional Root Bridge.
        [sid]          - The instance to be configured.

        Verifies that the specified MAC address is the MSTI Regional Root Bridge.
        """
        args = {"sid": sid,
                "reg_root": reg_root}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INSTANCE_INFO_DETAIL,
                                           self.parse_const.CHECK_INSTANCE_REGIONAL_ROOT, True,
                                           "The regional root for MSTI {sid} was {reg_root}.",
                                           "The regional root for MSTI {sid} was NOT {reg_root}.",
                                           **kwargs)

    def spanningtree_verify_mstp_region_name(self, device_name, region_name='', sid="0", **kwargs):
        """
        Keyword Arguments
        [device_name]   - The device the keyword will be run against.
        [region_name]   - The MSTP region name that should be configured.

        Verifies that the specified MSTP region name is configured.
        """
        args = {"region_name": region_name,
                "sid": sid}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO_SUMMARY,
                                           self.parse_const.CHECK_REGIONAL_NAME, True,
                                           "The MSTP Region Name is {region_name}.",
                                           "The MSTP Region Name is NOT {region_name}!",
                                           **kwargs)

    def spanningtree_verify_mstp_revision_level(self, device_name, revision_level='', sid="0", **kwargs):
        """
        Keyword Arguments
        [device_name]    - The device the keyword will be run against.
        [revision_level] - The MSTP revision level that should be configured.

        Verifies that the specified MSTP revision level is configured.
        """
        args = {"revision_level": revision_level,
                "sid": sid}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO_SUMMARY,
                                           self.parse_const.CHECK_REVISION_LEVEL, True,
                                           "The MSTP Revision Level is {revision_level}.",
                                           "The MSTP Revision Level is NOT {revision_level}!",
                                           **kwargs)

    def spanningtree_verify_root_port(self, device_name, port='', sid="0", **kwargs):
        """
        Keyword Arguments
        [device_name]  - The device the keyword will be run against.
        [port]         - The expected Root Port.
        [sid]          - The instance to be configured.

        Verifies that the specified port is the Root Port.
        """
        args = {"port": port,
                "sid": sid}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INSTANCE_INFO,
                                           self.parse_const.CHECK_INSTANCE_ROOT_PORT, True,
                                           "Port {port} is the current Root port.",
                                           "Port {port} WAS NOT the current Root port.",
                                           **kwargs)

    def spanningtree_verify_port_role_designated(self, device_name, port='', sid="0", **kwargs):
        """
        Keyword Arguments
        [device_name]  - The device the keyword will be run against.
        [port]         - The port, or list of ports, to configure.
        [sid]          - The instance to be configured.

        Verifies the specified port has a role of Designated.
        """
        args = {"port": port,
                "sid": sid,
                "state": "DESIGNATED"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_INFO,
                                           self.parse_const.CHECK_STP_PORT_ROLE, True,
                                           "Port {port} had a port role of DESIGNATED.",
                                           "Port {port} DID NOT have a port role of DESIGNATED.",
                                           **kwargs)

    def spanningtree_verify_port_role_root(self, device_name, port='', sid="0", **kwargs):
        """
        Keyword Arguments
        [device_name]  - The device the keyword will be run against.
        [port]         - The port, or list of ports, to configure.
        [sid]          - The instance to be configured.

        Verifies the specified port has a role of Root.
        """
        args = {"port": port,
                "sid": sid,
                "state": "ROOT"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_INFO,
                                           self.parse_const.CHECK_STP_PORT_ROLE, True,
                                           "Port {port} had a port role of ROOT.",
                                           "Port {port} DID NOT have a port role of ROOT.",
                                           **kwargs)

    def spanningtree_verify_port_role_backup(self, device_name, port='', sid="0", **kwargs):
        """
        Keyword Arguments
        [device_name]  - The device the keyword will be run against.
        [port]         - The port, or list of ports, to configure.
        [sid]          - The instance to be configured.

        Verifies the specified port has a role of Backup.
        """
        args = {"port": port,
                "sid": sid,
                "state": "BACKUP"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_INFO,
                                           self.parse_const.CHECK_STP_PORT_ROLE, True,
                                           "Port {port} had a port role of BACKUP.",
                                           "Port {port} DID NOT have a port role of BACKUP.",
                                           **kwargs)

    def spanningtree_verify_port_role_alternate(self, device_name, port='', sid="0", **kwargs):
        """
        Keyword Arguments
        [device_name]  - The device the keyword will be run against.
        [port]         - The port, or list of ports, to configure.
        [sid]          - The instance to be configured.

        Verifies the specified port has a role of Alternate.
        """
        args = {"port": port,
                "sid": sid,
                "state": "ALTERNATE"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_INFO,
                                           self.parse_const.CHECK_STP_PORT_ROLE, True,
                                           "Port {port} had a port role of ALTERNATE.",
                                           "Port {port} DID NOT have a port role of ALTERNATE.",
                                           **kwargs)

    def spanningtree_verify_port_role_forwarding(self, device_name, port='', sid="0", stp_type='rstp', **kwargs):
        """
        Keyword Arguments
        [device_name]  - The device the keyword will be run against.
        [port]         - The port, or list of ports, to configure.
        [sid]          - The instance to be configured.
        [stp_type]     - The stp type (rstp default, mstp)

        Verifies the specified port has a role of Alternate.
        """
        args = {"port": port,
                "sid": sid,
                "state": "FORWARDING",
                "stp_type":stp_type.lower()}
        
       
        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_STP_PORT_ROLE,
                                           self.parse_const.CHECK_STP_PORT_ROLE, True,
                                           "Port {port} had a port role of ALTERNATE.",
                                           "Port {port} DID NOT have a port role of ALTERNATE.",
                                           **kwargs)
      

    def spanningtree_verify_port_role_restricted(self, device_name, port='', sid="0", **kwargs):
        """
        Keyword Arguments
        [device_name]  - The device the keyword will be run against.
        [port]         - The port, or list of ports, to configure.
        [sid]          - The instance to be configured.

        Verifies the specified port has a role of Alternate or Backup.
        """
        args = {"port": port,
                "sid": sid}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_INFO,
                                           self.parse_const.CHECK_STP_PORT_RESTRICTED, True,
                                           "Port {port} had a restricted port role of BACKUP or ALTERNATE.",
                                           "Port {port} DID NOT have a port role of BACKUP or ALTERNATE.",
                                           **kwargs)

    def spanningtree_verify_port_autoedge_enable(self, device_name, port='', sid="0", **kwargs):
        """
        Keyword Arguments
        [device_name]  - The device the keyword will be run against.
        [port]         - The port, or list of ports, on which auto-edge should be enabled.
        [sid]          - The instance to be configured.

        Verifies that STP auto-edge is enabled on the specified port(s).
        """
        args = {"port": port,
                "sid": sid}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_AUTOEDGE,
                                           self.parse_const.CHECK_STP_PORT_AUTOEDGE, True,
                                           "Port {port} is auto-edge enabled.",
                                           "Port {port} is auto-edge disabled.",
                                           **kwargs)

    def spanningtree_verify_port_autoedge_disable(self, device_name, port='', sid="0", **kwargs):
        """
        Keyword Arguments
        [device_name]  - The device the keyword will be run against.
        [port]         - The port, or list of ports, on which auto-edge should be disabled.
        [sid]          - The instance to be configured.

        Verifies that STP auto-edge is disabled on the specified port(s).
        """
        args = {"port": port,
                "sid": sid}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_AUTOEDGE,
                                           self.parse_const.CHECK_STP_PORT_AUTOEDGE, False,
                                           "Port {port} is auto-edge disabled.",
                                           "Port {port} is auto-edge enabled.",
                                           **kwargs)

    def spanningtree_verify_port_edge_enabled(self, device_name, port='', **kwargs):
        """
        Keyword Arguments
        [device_name]  - The device the keyword will be run against.
        [port]         - The port, or list of ports, on which edge should be enabled.

        Verifies that STP edge is enabled on the specified port(s).
        """
        args = {"port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_EDGE,
                                           self.parse_const.CHECK_STP_PORTS_LINK_TYPE_IS_EDGE, True,
                                           "Port {port} is set as an edge port.",
                                           "Port {port} IS NOT set as an edge port!",
                                           **kwargs)

    def spanningtree_verify_port_edge_disabled(self, device_name, port='', **kwargs):
        """
        Keyword Arguments
        [device_name]  - The device the keyword will be run against.
        [port]         - The port, or list of ports, on which edge should be disabled.

        Verifies that STP edge is disabled on the specified port(s).
        """
        args = {"port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_EDGE,
                                           self.parse_const.CHECK_STP_PORTS_LINK_TYPE_IS_EDGE, False,
                                           "Port {port} is not set as an edge port.",
                                           "Port {port} IS set as an edge port!",
                                           **kwargs)

    def spanningtree_verify_portadmin_enabled(self, device_name, port='', sid="0", **kwargs):
        """
        Keyword Arguments
        [device_name]  - The device the keyword will be run against.
        [port]         - The port, or list of ports, on which STP Port Admin should be enabled.
        [sid]          - The instance to be inspected.

        Verifies STP Port Admin is enabled on the specified port(s).
        """
        args = {"port": port,
                "sid": sid}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_ADMIN,
                                           self.parse_const.CHECK_STP_PORTADMIN, True,
                                           "Port {port} is PortAdmin enabled.",
                                           "Port {port} is PortAdmin disabled.",
                                           **kwargs)

    def spanningtree_verify_portadmin_disabled(self, device_name, port='', sid="0", **kwargs):
        """
        Keyword Arguments
        [device_name]  - The device the keyword will be run against.
        [port]         - The port, or list of ports, on which STP Port Admin should be disabled.
        [sid]          - The instance to be inspected.

        Verifies STP Port Admin is disabled on the specified port(s).
        """
        args = {"port": port,
                "sid": sid}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_ADMIN,
                                           self.parse_const.CHECK_STP_PORTADMIN, False,
                                           "Port {port} is PortAdmin disabled.",
                                           "Port {port} is PortAdmin enabled.",
                                           **kwargs)

    def spanningtree_verify_portadmin_oper_up(self, device_name, port='', sid="0", **kwargs):
        """
        Keyword Arguments
        [device_name]  - The device the keyword will be run against.
        [port]         - The port, or list of ports, on which STP Port Admin oper should be up.
        [sid]          - The instance to be inspected.

        Verifies STP Port Admin is operationally up on the specified port(s).
        """
        args = {"port": port,
                "sid": sid}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_INFO_DETAIL,
                                           self.parse_const.CHECK_STP_PORTADMIN_OPER, True,
                                           "Port {port} is PortAdmin operationally enabled.",
                                           "Port {port} is PortAdmin operationally disabled.",
                                           **kwargs)

    def spanningtree_verify_portadmin_oper_down(self, device_name, port='', sid="0", **kwargs):
        """
        Keyword Arguments
        [device_name]  - The device the keyword will be run against.
        [port]         - The port, or list of ports, on which STP Port Admin oper should be down.
        [sid]          - The instance to be inspected.

        Verifies STP Port Admin is operationally down on the specified port(s).
        """
        args = {"port": port,
                "sid": sid}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_INFO_DETAIL,
                                           self.parse_const.CHECK_STP_PORTADMIN_OPER, False,
                                           "Port {port} is PortAdmin operationally disabled.",
                                           "Port {port} is PortAdmin operationally enabled.",
                                           **kwargs)

    def spanningtree_verify_bridge_hello_time(self, device_name, hello_time='', sid="0", **kwargs):
        """
        Keyword Arguments
        [device_name]  - The device the keyword will be run against.
        [hello_time]   - The bridge hello interval to be inspected.
        [sid]          - The instance to be inspected.

        Verifies the spanning tree hello timer to be provided value.
        """
        args = {"sid": sid,
                "hello_time": hello_time}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO_SUMMARY,
                                           self.parse_const.CHECK_STP_BRIDGE_HELLO_TIME, True,
                                           "The Bridge Hello Time is {hello_time}.",
                                           "The Bridge Hello Time is NOT {hello_time}!",
                                           **kwargs)

    def spanningtree_verify_bridge_forward_delay(self, device_name, fwd_delay='', sid="0", **kwargs):
        """
        Keyword Arguments
        [device_name]  - The device the keyword will be run against.
        [fwd_delay]    - The bridge forward delay to be inspected.
        [sid]          - The instance to be inspected.

        Verifies the spanning tree forward delay timer to be provided value.
        """
        args = {"sid": sid,
                "fwd_delay": fwd_delay}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO_SUMMARY,
                                           self.parse_const.CHECK_STP_BRIDGE_FWD_DELAY, True,
                                           "The Bridge Forward Delay is {fwd_delay}.",
                                           "The Bridge Forward Delay is NOT {fwd_delay}.",
                                           **kwargs)

    def spanningtree_verify_bridge_max_age(self, device_name, max_age='', sid="0", **kwargs):
        """
        Keyword Arguments
        [device_name]  - The device the keyword will be run against.
        [max_age]      - The bridge max age to be inspected.
        [sid]          - The instance to be inspected.

        Verifies the spanning tree BPDU max age to be provided value.
        """
        args = {"sid": sid,
                "max_age": max_age}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO_SUMMARY,
                                           self.parse_const.CHECK_STP_BRIDGE_MAX_AGE, True,
                                           "The Bridge BPDU Max Age is {max_age}.",
                                           "The Bridge BPDU Max Age is NOT {max_age}.",
                                           **kwargs)

    def spanningtree_verify_root_hello_time(self, device_name, hello_time='', sid="0", **kwargs):
        """
        Keyword Arguments
        [device_name]  - The device the keyword will be run against.
        [hello_time]   - The bridge hello interval to be inspected.
        [sid]          - The instance to be inspected.

        Verifies the spanning tree Root hello timer to be provided value.
        """
        args = {"sid": sid,
                "hello_time": hello_time}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO_SUMMARY,
                                           self.parse_const.CHECK_STP_ROOT_HELLO_TIME, True,
                                           "The Root Hello Time is {hello_time}.",
                                           "The Root Hello Time is NOT {hello_time}.",
                                           **kwargs)

    def spanningtree_verify_root_forward_delay(self, device_name, fwd_delay='', sid="0", **kwargs):
        """
        Keyword Arguments
        [device_name]  - The device the keyword will be run against.
        [fwd_delay]    - The bridge forward delay to be inspected.
        [sid]          - The instance to be inspected.

        Verifies the spanning tree Root forward delay timer to be provided value.
        """
        args = {"sid": sid,
                "fwd_delay": fwd_delay}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO_SUMMARY,
                                           self.parse_const.CHECK_STP_ROOT_FWD_DELAY, True,
                                           "The Root Forward Delay is {fwd_delay}.",
                                           "The Root Forward Delay is NOT {fwd_delay}.",
                                           **kwargs)

    def spanningtree_verify_root_max_age(self, device_name, max_age='', sid="0", **kwargs):
        """
        Keyword Arguments
        [device_name]  - The device the keyword will be run against.
        [max_age]      - The bridge max age to be inspected.
        [sid]          - The instance to be inspected.

        Verifies the spanning tree Root BPDU max age to be provided value.
        """
        args = {"sid": sid,
                "max_age": max_age}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO_SUMMARY,
                                           self.parse_const.CHECK_STP_ROOT_MAX_AGE, True,
                                           "The Root BPDU Max Age is {max_age}.",
                                           "The Root BPDU Max Age is NOT {max_age}.",
                                           **kwargs)

    def spanningtree_verify_port_link_type_point_to_point(self, device_name, port='', sid="0", **kwargs):
        """
        Keyword Arguments
        [device_name]  - The device the keyword will be run against.
        [port]         - The port, or list of ports, to configure.
        [sid]          - The instance to be configured.

        Verifies the specified port is set to point-to-point (EXOS only).
        """
        args = {"port": port,
                "sid": sid,
                "config_type": "POINT-TO-POINT"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_INFO,
                                           self.parse_const.CHECK_STP_PORT_CONFIG_TYPE, True,
                                           "Port {port} is correctly set to point-to-point.",
                                           "Port {port} is NOT set to point-to-point!",
                                           **kwargs)

    def spanningtree_verify_port_link_type_edge(self, device_name, port='', sid="0", **kwargs):
        """
        Keyword Arguments
        [device_name]  - The device the keyword will be run against.
        [port]         - The port, or list of ports, to configure.
        [sid]          - The instance to be configured.

        Verifies the specified port is set to edge (EXOS only).
        """
        args = {"port": port,
                "sid": sid,
                "config_type": "EDGE"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_INFO,
                                           self.parse_const.CHECK_STP_PORT_CONFIG_TYPE, True,
                                           "Port {port} is correctly set to edge.",
                                           "Port {port} is NOT set to edge!",
                                           **kwargs)

    def spanningtree_verify_bpduguard_enabled(self, device_name, port='', **kwargs):
        """
        Keyword Arguments
        [device_name]  - The device, or list of devices, the keyword will be run against.
        [port]         - The port to check.

        Verifies that Spanning Tree BPDU guard is enabled on a port.
        """
        args = {"port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_BPDUGUARD,
                                           self.parse_const.CHECK_STP_BPDUGUARD, True,
                                           "Spanning Tree BPDU-guard is enabled on {port}.",
                                           "Spanning Tree BPDU-guard is NOT enabled on {port}!",
                                           **kwargs)

    def spanningtree_verify_bpduguard_disabled(self, device_name, port='', **kwargs):
        """
        Keyword Arguments
        [device_name]  - The device, or list of devices, the keyword will be run against.
        [port]        - The port to check.

        Verifies that Spanning Tree BPDU guard is disabled on a port.
        """
        args = {"port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_BPDUGUARD,
                                           self.parse_const.CHECK_STP_BPDUGUARD, False,
                                           "Spanning Tree BPDU-guard is disabled on {port}.",
                                           "Spanning Tree BPDU-guard is NOT disabled on {port}!",
                                           **kwargs)

    def spanningtree_verify_mstp_enabled_on_port(self, device_name, port='', **kwargs):
        """
        Keyword Arguments
        [device_name]  - The device, or list of devices, the keyword will be run against.
        [port]         - The port(s) to check that MSTP is enabled on.

        Verifies that MSTP is enabled on a given interface.
        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port)}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_MSTP_PORT_INFO,
                                           self.parse_const.CHECK_MSTP_ENABLED_ON_INTERFACE, True,
                                           "MSTP is enabled on interface {port}.",
                                           "MSTP IS NOT enabled on interface {port}!",
                                           **kwargs)

    def spanningtree_verify_mstp_disabled_on_port(self, device_name, port='', **kwargs):
        """
        Keyword Arguments
        [device_name]  - The device, or list of devices, the keyword will be run against.
        [port]         - The port(s) to check that MSTP is disabled on.

        Verifies that MSTP is disabled on a given interface.
        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port)}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_MSTP_PORT_INFO,
                                           self.parse_const.CHECK_MSTP_ENABLED_ON_INTERFACE, False,
                                           "MSTP is disabled on interface {port}.",
                                           "MSTP is NOT disabled on interface {port}!",
                                           **kwargs)

    def spanningtree_verify_mst_config_digest(self, device_name, sid="0", **kwargs):
        """
        Keyword Arguments
        [device_name]  - The device the keyword will be run against.
        [sid]          - The instance to be inspected.

        Returns the current MST Configuration Digest hash.
        """
        args = {"sid": sid}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_MST_DIGEST,
                                           self.parse_const.RETURN_SPANNING_TREE_CONFIG_DIGEST, None,
                                           "The MST config digest was equal to the expected value.",
                                           "The MST config digest value was incorrect!",
                                           **kwargs)

    def spanningtree_verify_and_store_current_tc_counter(self, device_name, sid="0", **kwargs):
        """
        Keyword Arguments
        [device_name]  - The device the keyword will be run against.
        [sid]          - The instance to be configured.

        Stores the current Topology Change count.
        """
        args = {"sid": sid}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INSTANCE_INFO_DETAIL,
                                           self.parse_const.STORE_SPANNING_TREE_TC_COUNTER, True,
                                           "Spanning Tree TC Count Stored.",
                                           "Could not resolve Spanning Tree TC Count.",
                                           **kwargs)
