"""
Keyword class for all lldp cli commands.
"""
from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import NetworkElementKeywordBaseClass
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.Constants.LldpConstants import \
    LldpConstants as ParseConstants
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.Constants.LldpConstants import \
    LldpConstants as CommandConstants
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.ListUtils import ListUtils


class NetworkElementLldpGenKeywords(NetworkElementKeywordBaseClass):
    def __init__(self):
        super(NetworkElementLldpGenKeywords, self).__init__()
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()
        self.api_const = "lldp"

    def lldp_enable(self, device_name, **kwargs):
        """
        Description: Globally enables LLDP on the device.

        Supported Agents and OS:
            CLI: SLX
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE,
                                    **kwargs)

    def lldp_disable(self, device_name, **kwargs):
        """
        Description: Globally disables LLDP on the device.

        Supported Agents and OS:
            CLI: SLX
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE,
                                    **kwargs)

    def lldp_enable_tx(self, device_name, **kwargs):
        """
        Description: Globally enables transmission of LLDP packets only.

        Supported Agents and OS:
            CLI: SLX
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_TX,
                                    **kwargs)

    def lldp_enable_rx(self, device_name, **kwargs):
        """
        Description: Globally enables reception of LLDP packets only.

        Supported Agents and OS:
            CLI: SLX
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_RX,
                                    **kwargs)

    def lldp_enable_port_both(self, device_name, port='', **kwargs):
        """
        Description: Enables transmission and reception of LLDP packets on the specified port.

        Supported Agents and OS:
            CLI: SLX, EOS, EXOS
            REST: EXOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_PORT_BOTH,
                                    **kwargs)

    def lldp_disable_port(self, device_name, port='', **kwargs):
        """
        Description: Disables transmission and reception of LLDP packets on the specified port.

        Supported Agents and OS:
            CLI: SLX, EOS, EXOS
            REST: EXOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_PORT,
                                    **kwargs)

    def lldp_set_tx_interval(self, device_name, interval='', **kwargs):
        """
        Description: Configures the LLDP tx interval on a given device.

        Supported Agents and OS:
            CLI: SLX, EOS, EXOS, VOSS
            SNMP: EOS, EXOS, VOSS
        """
        args = {
            "interval": interval
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_TX_INTERVAL,
                                    **kwargs)

    def lldp_set_sys_name(self, device_name, **kwargs):
        """
        Description: Configures the LLDP System Name.

        Supported Agents and OS:
            CLI: SLX
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_SYS_NAME,
                                    **kwargs)

    def lldp_clear_sys_name(self, device_name, name='', **kwargs):
        """
        Description: Clears the LLDP System Name.

        Supported Agents and OS:
            CLI: SLX
        """
        args = {
            "name": name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_SYS_NAME,
                                    **kwargs)

    def lldp_set_profile(self, device_name, profile='', **kwargs):
        """
        Description: Configures an LLDP profile.

        Supported Agents and OS:
            CLI: SLX
        """
        args = {
            "profile": profile
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PROFILE,
                                    **kwargs)

    def lldp_set_profile_interface(self, device_name, port='', profile='', **kwargs):
        """
        Description: Configures an LLDP profile on the specified interface.

        Supported Agents and OS:
            CLI: SLX
        """
        args = {
            "port": port,
            "profile": profile
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PROFILE_INTERFACE,
                                    **kwargs)

    def lldp_set_tx_hold_multiplier(self, device_name, multiplier='', **kwargs):
        """
        Description: Configures the LLDP tx interval on a given device.

        Supported Agents and OS:
            CLI: SLX, VOSS
            SNMP: EOS, EXOS, VOSS
        """
        args = {
            "multiplier": multiplier
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_TX_HOLD_MULTIPLIER,
                                    **kwargs)

    def lldp_enable_port_tx(self, device_name, port='', **kwargs):
        """
        Description: Enables transmission of LLDP packets on the specified port.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_PORT_TX,
                                    **kwargs)

    def lldp_enable_port_rx(self, device_name, port='', **kwargs):
        """
        Description: Enables reception of LLDP packets on the specified port.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_PORT_RX,
                                    **kwargs)

    def lldp_enable_tlv_all(self, device_name, port='', **kwargs):
        """
        Description: Enables all TLVs on a given port.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_TLV_ALL,
                                    **kwargs)

    def lldp_disable_tlv_all(self, device_name, port='', **kwargs):
        """
        Description: Disables all TLVs on a given port.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_TLV_ALL,
                                    **kwargs)

    def lldp_enable_tlv_port_desc(self, device_name, port='', **kwargs):
        """
        Description: Enables the port-desc TLV on a given port.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_TLV_PORT_DESC,
                                    **kwargs)

    def lldp_disable_tlv_port_desc(self, device_name, port='', **kwargs):
        """
        Description: Disables the port-desc TLV on a given port.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_TLV_PORT_DESC,
                                    **kwargs)

    def lldp_enable_tlv_sys_name(self, device_name, port='', **kwargs):
        """
        Description: Enables the sys-name TLV on a given port.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_TLV_SYS_NAME,
                                    **kwargs)

    def lldp_disable_tlv_sys_name(self, device_name, port='', **kwargs):
        """
        Description: Disables the sys-name TLV on a given port.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_TLV_SYS_NAME,
                                    **kwargs)

    def lldp_enable_tlv_sys_desc(self, device_name, port='', **kwargs):
        """
        Description: Enables the sys-desc TLV on a given port.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_TLV_SYS_DESC,
                                    **kwargs)

    def lldp_disable_tlv_sys_desc(self, device_name, port='', **kwargs):
        """
        Description: Disables the sys-desc TLV on a given port.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_TLV_SYS_DESC,
                                    **kwargs)

    def lldp_enable_tlv_sys_cap(self, device_name, port='', **kwargs):
        """
        Description: Enables the sys-cap TLV on a given port.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_TLV_SYS_CAP,
                                    **kwargs)

    def lldp_disable_tlv_sys_cap(self, device_name, port='', **kwargs):
        """
        Description: Disables the sys-cap TLV on a given port.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_TLV_SYS_CAP,
                                    **kwargs)

    def lldp_enable_tlv_mgmt_addr(self, device_name, port='', **kwargs):
        """
        Description: Enables the mgmt-addr TLV on a given port.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_TLV_MGMT_ADDR,
                                    **kwargs)

    def lldp_disable_tlv_mgmt_addr(self, device_name, port='', **kwargs):
        """
        Description: Disables the mgmt-addr TLV on a given port.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_TLV_MGMT_ADDR,
                                    **kwargs)

    def lldp_enable_tlv_vlan_id(self, device_name, port='', **kwargs):
        """
        Description: Enables the vlan-id TLV on a given port.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_TLV_VLAN_ID,
                                    **kwargs)

    def lldp_disable_tlv_vlan_id(self, device_name, port='', **kwargs):
        """
        Description: Disables the vlan-id TLV on a given port.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_TLV_VLAN_ID,
                                    **kwargs)

    def lldp_enable_tlv_stp(self, device_name, port='', **kwargs):
        """
        Description: Enables the stp TLV on a given port.

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_TLV_STP,
                                    **kwargs)

    def lldp_disable_tlv_stp(self, device_name, port='', **kwargs):
        """
        Description: Disables the stp TLV on a given port.

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_TLV_STP,
                                    **kwargs)

    def lldp_enable_tlv_lacp(self, device_name, port='', **kwargs):
        """
        Description: Enables the lacp TLV on a given port.

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_TLV_LACP,
                                    **kwargs)

    def lldp_disable_tlv_lacp(self, device_name, port='', **kwargs):
        """
        Description: Disables the lacp TLV on a given port.

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_TLV_LACP,
                                    **kwargs)

    def lldp_enable_tlv_gvrp(self, device_name, port='', **kwargs):
        """
        Description: Enables the gvrp TLV on a given port.

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_TLV_GVRP,
                                    **kwargs)

    def lldp_disable_tlv_gvrp(self, device_name, port='', **kwargs):
        """
        Description: Disables the gvrp TLV on a given port.

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_TLV_GVRP,
                                    **kwargs)

    def lldp_enable_tlv_mac_phy(self, device_name, port='', **kwargs):
        """
        Description: Enables the mac-phy TLV on a given port.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_TLV_MAC_PHY,
                                    **kwargs)

    def lldp_disable_tlv_mac_phy(self, device_name, port='', **kwargs):
        """
        Description: Disables the mac-phy TLV on a given port.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_TLV_MAC_PHY,
                                    **kwargs)

    def lldp_enable_tlv_poe(self, device_name, port='', **kwargs):
        """
        Description: Enables the poe TLV on a given port.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_TLV_POE,
                                    **kwargs)

    def lldp_disable_tlv_poe(self, device_name, port='', **kwargs):
        """
        Description: Disables the poe TLV on a given port.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_TLV_POE,
                                    **kwargs)

    def lldp_enable_tlv_link_aggr(self, device_name, port='', **kwargs):
        """
        Description: Enables the link-aggr TLV on a given port.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_TLV_LINK_AGGR,
                                    **kwargs)

    def lldp_disable_tlv_link_aggr(self, device_name, port='', **kwargs):
        """
        Description: Disables the link-aggr TLV on a given port.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_TLV_LINK_AGGR,
                                    **kwargs)

    def lldp_enable_tlv_max_frame(self, device_name, port='', **kwargs):
        """
        Description: Enables the max-frame TLV on a given port.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_TLV_MAX_FRAME,
                                    **kwargs)

    def lldp_disable_tlv_max_frame(self, device_name, port='', **kwargs):
        """
        Description: Disables the max-frame TLV on a given port.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_TLV_MAX_FRAME,
                                    **kwargs)

    def lldp_enable_tlv_med_cap(self, device_name, port='', **kwargs):
        """
        Description: Enables the med-cap TLV on a given port.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_TLV_MED_CAP,
                                    **kwargs)

    def lldp_disable_tlv_med_cap(self, device_name, port='', **kwargs):
        """
        Description: Disables the med-cap TLV on a given port.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_TLV_MED_CAP,
                                    **kwargs)

    def lldp_enable_tlv_med_pol(self, device_name, port='', **kwargs):
        """
        Description: Enables the med-pol TLV on a given port.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_TLV_MED_POL,
                                    **kwargs)

    def lldp_disable_tlv_med_pol(self, device_name, port='', **kwargs):
        """
        Description: Disables the med-pol TLV on a given port.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_TLV_MED_POL,
                                    **kwargs)

    def lldp_enable_tlv_med_loc(self, device_name, port='', _type='', value='', **kwargs):
        """
        Description: Enables the med-loc TLV on a given port.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "port": port,
            "type": _type,
            "value": value
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_TLV_MED_LOC,
                                    **kwargs)

    def lldp_disable_tlv_med_loc(self, device_name, port='', _type='', value='', **kwargs):
        """
        Description: Disables the med-loc TLV on a given port.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "port": port,
            "type": _type,
            "value": value
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_TLV_MED_LOC,
                                    **kwargs)

    def lldp_enable_tlv_med_poe(self, device_name, port='', **kwargs):
        """
        Description: Enables the med-poe TLV on a given port.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_TLV_MED_POE,
                                    **kwargs)

    def lldp_disable_tlv_med_poe(self, device_name, port='', **kwargs):
        """
        Description: Disables the med-poe TLV on a given port.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_TLV_MED_POE,
                                    **kwargs)

    def lldp_enable_tlv_enhanced_trans_config(self, device_name, port='', **kwargs):
        """
        Description: Enables the enhanced-trans-config TLV on a given port.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_TLV_ENHANCED_TRANS_CONFIG,
                                    **kwargs)

    def lldp_disable_tlv_enhanced_trans_config(self, device_name, port='', **kwargs):
        """
        Description: Disables the enhanced-trans-config TLV on a given port.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_TLV_ENHANCED_TRANS_CONFIG,
                                    **kwargs)

    def lldp_enable_tlv_enhanced_trans_rec(self, device_name, port='', **kwargs):
        """
        Description: Enables the enhanced-trans-rec TLV on a given port.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_TLV_ENHANCED_TRANS_REC,
                                    **kwargs)

    def lldp_disable_tlv_enhanced_trans_rec(self, device_name, port='', **kwargs):
        """
        Description: Disables the enhanced-trans-rec TLV on a given port.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_TLV_ENHANCED_TRANS_REC,
                                    **kwargs)

    def lldp_enable_tlv_priority_flowctrl(self, device_name, port='', **kwargs):
        """
        Description: Enables the priority-flowctrl TLV on a given port.

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_TLV_PRIORITY_FLOWCTRL,
                                    **kwargs)

    def lldp_disable_tlv_priority_flowctrl(self, device_name, port='', **kwargs):
        """
        Description: Disables the priority-flowctrl TLV on a given port.

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_TLV_PRIORITY_FLOWCTRL,
                                    **kwargs)

    def lldp_enable_tlv_application_pri(self, device_name, port='', **kwargs):
        """
        Description: Enables the application-pri TLV on a given port.

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_TLV_APPLICATION_PRI,
                                    **kwargs)

    def lldp_disable_tlv_application_pri(self, device_name, port='', **kwargs):
        """
        Description: Disables the application-pri TLV on a given port.

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_TLV_APPLICATION_PRI,
                                    **kwargs)

    def lldp_enable_tlv_congestion_notif(self, device_name, port='', **kwargs):
        """
        Description: Enables the congestion-notif TLV on a given port.

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_TLV_CONGESTION_NOTIF,
                                    **kwargs)

    def lldp_disable_tlv_congestion_notif(self, device_name, port='', **kwargs):
        """
        Description: Disables the congestion-notif TLV on a given port.

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_TLV_CONGESTION_NOTIF,
                                    **kwargs)

    def lldp_enable_tlv_energy_eff_eth(self, device_name, port='', **kwargs):
        """
        Description: Enables the energy-eff-eth TLV on a given port.

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_TLV_ENERGY_EFF_ETH,
                                    **kwargs)

    def lldp_disable_tlv_energy_eff_eth(self, device_name, port='', **kwargs):
        """
        Description: Disables the energy-eff-eth TLV on a given port.

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_TLV_ENERGY_EFF_ETH,
                                    **kwargs)

    # ##################################################################################################################
    #   Inspection Keywords   ##########################################################################################
    # ##################################################################################################################

    def lldp_verify_tx_interval(self, device_name, interval='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [interval] - The interval that should be configured.

        IEEE 802.1AB-2005 10.5.3.3
        The interval at which LLDP frames are transmitted on behalf of this LLDP agent.
        The default value is 30.

        Verifies the interval configured on the given device.
        """
        args = {"interval": interval}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO,
                                           self.parse_const.CHECK_LLDP_TX_INTERVAL, True,
                                           "LLDP transmit interval is set to {interval} on {device_name}.",
                                           "LLDP transmit interval is NOT set to {interval} on {device_name}.",
                                           **kwargs)

    def lldp_verify_tx_hold_multiplier(self, device_name, multiplier='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [multiplier] - The tx hold multiplier that should be configured.

        IEEE 802.1AB-2005 10.5.3.3
        The time-to-live value expressed as a multiple of the lldpMessageTxInterval.  The actual time-to-live value
        used in LLDP frames, transmitted on behalf of this LLDP agent, can be expressed by the following formula:
        TTL = min(65535, (lldpMessageTxInterval * lldpMessageTxHoldMultiplier)) For example, if the value
        of lldpMessageTxInterval is '30', and the value of lldpMessageTxHoldMultiplier is '4', then the
        value '120' is encoded in the TTL field in the LLDP header.
        The default value is 4.

        Verifies the tx hold multiplier configured on the given device.
        """
        args = {"multiplier": multiplier}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO,
                                           self.parse_const.CHECK_LLDP_TX_HOLD_MULTIPLIER, True,
                                           "LLDP tx hold multiplier is set to {multiplier} on {device_name}.",
                                           "LLDP tx hold multiplier is NOT set to {multiplier} on {device_name}.",
                                           **kwargs)

    def lldp_verify_port_desc_tlv_enabled(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [port]        - The port(s) that the port-desc TLV should be enabled on.

        Verifies that the port-desc TLV is enabled on a given port.
        """
        args = {"port": port,
                "tlv": "port-desc"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_TLV_PORT_DESC,
                                           self.parse_const.CHECK_TLV_STATUS, True,
                                           "Port-desc TLV was enabled on {device_name}.",
                                           "Port-desc TLV was DISABLED on {device_name}.",
                                           **kwargs)

    def lldp_verify_port_desc_tlv_disabled(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [port]        - The port(s) that the port-desc TLV should be disabled on.

        Verifies that the port-desc TLV is disabled on a given port.
        """
        args = {"port": port,
                "tlv": "port-desc"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_TLV_PORT_DESC,
                                           self.parse_const.CHECK_TLV_STATUS, False,
                                           "Port-desc TLV was disabled on {device_name}.",
                                           "Port-desc TLV was ENABLED on {device_name}.",
                                           **kwargs)

    def lldp_verify_sys_name_tlv_enabled(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [port]        - The port(s) that the sys-name TLV should be enabled on.

        Verifies that the sys-name TLV is enabled on a given port.
        """
        args = {"port": port,
                "tlv": "sys-name"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_TLV_SYS_NAME,
                                           self.parse_const.CHECK_TLV_STATUS, True,
                                           "Sys-name TLV was enabled on {device_name}.",
                                           "Sys-name TLV was DISABLED on {device_name}.",
                                           **kwargs)

    def lldp_verify_sys_name_tlv_disabled(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [port]        - The port(s) that the sys-name TLV should be disabled on.

        Verifies that the sys-name TLV is disabled on a given port.
        """
        args = {"port": port,
                "tlv": "sys-name"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_TLV_SYS_NAME,
                                           self.parse_const.CHECK_TLV_STATUS, False,
                                           "Sys-name TLV was disabled on {device_name}.",
                                           "Sys-name TLV was ENABLED on {device_name}.",
                                           **kwargs)

    def lldp_verify_sys_desc_tlv_enabled(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [port]        - The port(s) that the sys-desc TLV should be enabled on.

        Verifies that the sys-desc TLV is enabled on a given port.
        """
        args = {"port": port,
                "tlv": "sys-desc"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_TLV_SYS_DESC,
                                           self.parse_const.CHECK_TLV_STATUS, True,
                                           "Sys-desc TLV was enabled on {device_name}.",
                                           "Sys-desc TLV was DISABLED on {device_name}.",
                                           **kwargs)

    def lldp_verify_sys_desc_tlv_disabled(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [port]        - The port(s) that the sys-desc TLV should be disabled on.

        Verifies that the sys-desc TLV is disabled on a given port.
        """
        args = {"port": port,
                "tlv": "sys-desc"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_TLV_SYS_DESC,
                                           self.parse_const.CHECK_TLV_STATUS, False,
                                           "Sys-desc TLV was disabled on {device_name}.",
                                           "Sys-desc TLV was ENABLED on {device_name}.",
                                           **kwargs)

    def lldp_verify_sys_cap_tlv_enabled(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [port]        - The port(s) that the sys-cap TLV should be enabled on.

        Verifies that the sys-cap TLV is enabled on a given port.
        """
        args = {"port": port,
                "tlv": "sys-cap"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_TLV_SYS_CAP,
                                           self.parse_const.CHECK_TLV_STATUS, True,
                                           "Sys-cap TLV was enabled on {device_name}.",
                                           "Sys-cap TLV was DISABLED on {device_name}.",
                                           **kwargs)

    def lldp_verify_sys_cap_tlv_disabled(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [port]        - The port(s) that the sys-cap TLV should be disabled on.

        Verifies that the sys-cap TLV is disabled on a given port.
        """
        args = {"port": port,
                "tlv": "sys-cap"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_TLV_SYS_CAP,
                                           self.parse_const.CHECK_TLV_STATUS, False,
                                           "Sys-cap TLV was disabled on {device_name}.",
                                           "Sys-cap TLV was ENABLEDon {device_name}.",
                                           **kwargs)

    def lldp_verify_mgmt_addr_tlv_enabled(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [port]        - The port(s) that the mgmt-addr TLV should be enabled on.

        Verifies that the mgmt-addr TLV is enabled on a given port.
        """
        args = {"port": port,
                "tlv": "mgmt-addr"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_TLV_MGMT_ADDR,
                                           self.parse_const.CHECK_TLV_STATUS, True,
                                           "Mgmt-addr TLV was enabled on {device_name}.",
                                           "Mgmt-addr TLV was DISABLED on {device_name}.",
                                           **kwargs)

    def lldp_verify_mgmt_addr_tlv_disabled(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [port]        - The port(s) that the mgmt-addr TLV should be disabled on.

        Verifies that the mgmt-addr TLV is disabled on a given port.
        """
        args = {"port": port,
                "tlv": "mgmt-addr"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_TLV_MGMT_ADDR,
                                           self.parse_const.CHECK_TLV_STATUS, False,
                                           "Mgmt-addr TLV was disabled on {device_name}.",
                                           "Mgmt-addr TLV was ENABLED on {device_name}.",
                                           **kwargs)

    def lldp_verify_vlan_id_tlv_enabled(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [port]        - The port(s) that the vlan-id TLV should be enabled on.

        Verifies that the vlan-id TLV is enabled on a given port.
        """
        args = {"port": port,
                "tlv": "vlan-id"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_TLV_VLAN_ID,
                                           self.parse_const.CHECK_TLV_STATUS, True,
                                           "Vlan-id TLV was enabled on {device_name}.",
                                           "Vlan-id TLV was DISABLED on {device_name}.",
                                           **kwargs)

    def lldp_verify_vlan_id_tlv_disabled(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [port]        - The port(s) that the vlan-id TLV should be disabled on.

        Verifies that the vlan-id TLV is disabled on a given port.
        """
        args = {"port": port,
                "tlv": "vlan-id"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_TLV_VLAN_ID,
                                           self.parse_const.CHECK_TLV_STATUS, False,
                                           "Vlan-id TLV was disabled on {device_name}.",
                                           "Vlan-id TLV was ENABLED on {device_name}.",
                                           **kwargs)

    def lldp_verify_stp_tlv_enabled(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [port]        - The port(s) that the stp TLV should be enabled on.

        Verifies that the stp TLV is enabled on a given port.
        """
        args = {"port": port,
                "tlv": "stp"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_TLV_STP,
                                           self.parse_const.CHECK_TLV_STATUS, True,
                                           "STP TLV was enabled on {device_name}.",
                                           "STP TLV was DISABLED on {device_name}.",
                                           **kwargs)

    def lldp_verify_stp_tlv_disabled(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [port]        - The port(s) that the stp TLV should be disabled on.

        Verifies that the stp TLV is disabled on a given port.
        """
        args = {"port": port,
                "tlv": "stp"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_TLV_STP,
                                           self.parse_const.CHECK_TLV_STATUS, False,
                                           "STP TLV was disabled on {device_name}.",
                                           "STP TLV was ENABLED on {device_name}.",
                                           **kwargs)

    def lldp_verify_lacp_tlv_enabled(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [port]        - The port(s) that the lacp TLV should be enabled on.

        Verifies that the lacp TLV is enabled on a given port.
        """
        args = {"port": port,
                "tlv": "lacp"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_TLV_LACP,
                                           self.parse_const.CHECK_TLV_STATUS, True,
                                           "LACP TLV was enabled on {device_name}.",
                                           "LACP TLV was DISABLED on {device_name}.",
                                           **kwargs)

    def lldp_verify_lacp_tlv_disabled(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [port]        - The port(s) that the lacp TLV should be disabled on.

        Verifies that the lacp TLV is disabled on a given port.
        """
        args = {"port": port,
                "tlv": "lacp"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_TLV_LACP,
                                           self.parse_const.CHECK_TLV_STATUS, False,
                                           "LACP TLV was disabled on {device_name}.",
                                           "LACP TLV was ENABLED on {device_name}.",
                                           **kwargs)

    def lldp_verify_gvrp_tlv_enabled(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [port]        - The port(s) that the gvrp TLV should be enabled on.

        Verifies that the gvrp TLV is enabled on a given port.
        """
        args = {"port": port,
                "tlv": "gvrp"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_TLV_GVRP,
                                           self.parse_const.CHECK_TLV_STATUS, True,
                                           "GVRP TLV was enabled on {device_name}.",
                                           "GVRP TLV was DISABLED on {device_name}.",
                                           **kwargs)

    def lldp_verify_gvrp_tlv_disabled(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [port]        - The port(s) that the gvrp TLV should be disabled on.

        Verifies that the gvrp TLV is disabled on a given port.
        """
        args = {"port": port,
                "tlv": "gvrp"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_TLV_GVRP,
                                           self.parse_const.CHECK_TLV_STATUS, False,
                                           "GVRP TLV was disabled on {device_name}.",
                                           "GVRP TLV was ENABLED on {device_name}.",
                                           **kwargs)

    def lldp_verify_mac_phy_tlv_enabled(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [port]        - The port(s) that the mac-phy TLV should be enabled on.

        Verifies that the mac-phy TLV is enabled on a given port.
        """
        args = {"port": port,
                "tlv": "mac-phy"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_TLV_MAC_PHY,
                                           self.parse_const.CHECK_TLV_STATUS, True,
                                           "Mac-phy TLV was enabled on {device_name}.",
                                           "Mac-phy TLV was DISABLED on {device_name}.",
                                           **kwargs)

    def lldp_verify_mac_phy_tlv_disabled(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [port]        - The port(s) that the mac-phy TLV should be disabled on.

        Verifies that the mac-phy TLV is disabled on a given port.
        """
        args = {"port": port,
                "tlv": "mac-phy"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_TLV_MAC_PHY,
                                           self.parse_const.CHECK_TLV_STATUS, False,
                                           "Mac-phy TLV was disabled on {device_name}.",
                                           "Mac-phy TLV was ENABLED on {device_name}.",
                                           **kwargs)

    def lldp_verify_poe_tlv_enabled(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [port]        - The port(s) that the poe TLV should be enabled on.

        Verifies that the poe TLV is enabled on a given port.
        """
        args = {"port": port,
                "tlv": "poe"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_TLV_POE,
                                           self.parse_const.CHECK_TLV_STATUS, True,
                                           "POE TLV was enabled on {device_name}.",
                                           "POE TLV was DISABLED on {device_name}.",
                                           **kwargs)

    def lldp_verify_poe_tlv_disabled(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [port]        - The port(s) that the poe TLV should be disabled on.

        Verifies that the poe TLV is disabled on a given port.
        """
        args = {"port": port,
                "tlv": "poe"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_TLV_POE,
                                           self.parse_const.CHECK_TLV_STATUS, False,
                                           "POE TLV was disabled on {device_name}.",
                                           "POE TLV was ENABLED on {device_name}.",
                                           **kwargs)

    def lldp_verify_link_aggr_tlv_enabled(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [port]        - The port(s) that the link-aggr TLV should be enabled on.

        Verifies that the link-aggr TLV is enabled on a given port.
        """
        args = {"port": port,
                "tlv": "link-aggr"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_TLV_LINK_AGGR,
                                           self.parse_const.CHECK_TLV_STATUS, True,
                                           "Link-aggr TLV was enabled on {device_name}.",
                                           "Link-aggr TLV was DISABLED on {device_name}.",
                                           **kwargs)

    def lldp_verify_link_aggr_tlv_disabled(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [port]        - The port(s) that the link-aggr TLV should be disabled on.

        Verifies that the link-aggr TLV is disabled on a given port.
        """
        args = {"port": port,
                "tlv": "link-aggr"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_TLV_LINK_AGGR,
                                           self.parse_const.CHECK_TLV_STATUS, False,
                                           "Link-aggr TLV was disabled on {device_name}.",
                                           "Link-aggr TLV was ENABLED on {device_name}.",
                                           **kwargs)

    def lldp_verify_max_frame_tlv_enabled(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [port]        - The port(s) that the max-frame TLV should be enabled on.

        Verifies that the max-frame TLV is enabled on a given port.
        """
        args = {"port": port,
                "tlv": "max-frame"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_TLV_MAX_FRAME,
                                           self.parse_const.CHECK_TLV_STATUS, True,
                                           "Max-frame TLV was enabled on {device_name}.",
                                           "Max-frame TLV was DISABLED on {device_name}.",
                                           **kwargs)

    def lldp_verify_max_frame_tlv_disabled(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [port]        - The port(s) that the max-frame TLV should be disabled on.

        Verifies that the max-frame TLV is disabled on a given port.
        """
        args = {"port": port,
                "tlv": "max-frame"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_TLV_MAX_FRAME,
                                           self.parse_const.CHECK_TLV_STATUS, False,
                                           "Max-frame TLV was disabled on {device_name}.",
                                           "Max-frame TLV was ENABLED on {device_name}.",
                                           **kwargs)

    def lldp_verify_med_cap_tlv_enabled(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [port]        - The port(s) that the med-cap TLV should be enabled on.

        Verifies that the med-cap TLV is enabled on a given port.
        """
        args = {"port": port,
                "tlv": "med-cap"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_TLV_MED_CAP,
                                           self.parse_const.CHECK_TLV_STATUS, True,
                                           "Med-cap TLV was enabled on {device_name}.",
                                           "Med-cap TLV was DISABLED on {device_name}.",
                                           **kwargs)

    def lldp_verify_med_cap_tlv_disabled(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [port]        - The port(s) that the med-cap TLV should be disabled on.

        Verifies that the med-cap TLV is disabled on a given port.
        """
        args = {"port": port,
                "tlv": "med-cap"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_TLV_MED_CAP,
                                           self.parse_const.CHECK_TLV_STATUS, False,
                                           "Med-cap TLV was disabled on {device_name}.",
                                           "Med-cap TLV was ENABLED on {device_name}.",
                                           **kwargs)

    def lldp_verify_med_pol_tlv_enabled(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [port]        - The port(s) that the med-pol TLV should be enabled on.

        Verifies that the med-pol TLV is enabled on a given port.
        """
        args = {"port": port,
                "tlv": "med-pol"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_TLV_MED_POL,
                                           self.parse_const.CHECK_TLV_STATUS, True,
                                           "Med-pol TLV was enabled on {device_name}.",
                                           "Med-pol TLV was DISABLED on {device_name}.",
                                           **kwargs)

    def lldp_verify_med_pol_tlv_disabled(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [port]        - The port(s) that the med-pol TLV should be disabled on.

        Verifies that the med-pol TLV is disabled on a given port.
        """
        args = {"port": port,
                "tlv": "med-pol"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_TLV_MED_POL,
                                           self.parse_const.CHECK_TLV_STATUS, False,
                                           "Med-pol TLV was disabled on {device_name}.",
                                           "Med-pol TLV was ENABLED on {device_name}.",
                                           **kwargs)

    def lldp_verify_med_loc_tlv_enabled(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [port]        - The port(s) that the med-loc TLV should be enabled on.

        Verifies that the med-loc TLV is enabled on a given port.
        """
        args = {"port": port,
                "tlv": "med-loc"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_TLV_MED_LOC,
                                           self.parse_const.CHECK_TLV_STATUS, True,
                                           "Med-loc TLV was enabled on {device_name}.",
                                           "Med-loc TLV was DISABLED on {device_name}.",
                                           **kwargs)

    def lldp_verify_med_loc_tlv_disabled(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [port]        - The port(s) that the med-loc TLV should be disabled on.

        Verifies that the med-loc TLV is disabled on a given port.
        """
        args = {"port": port,
                "tlv": "med-loc"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_TLV_MED_LOC,
                                           self.parse_const.CHECK_TLV_STATUS, False,
                                           "Med-loc TLV was disabled on {device_name}.",
                                           "Med-loc TLV was ENABLED on {device_name}.",
                                           **kwargs)

    def lldp_verify_med_poe_tlv_enabled(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [port]        - The port(s) that the med-poe TLV should be enabled on.

        Verifies that the med-poe TLV is enabled on a given port.
        """
        args = {"port": port,
                "tlv": "med-poe"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_TLV_MED_POE,
                                           self.parse_const.CHECK_TLV_STATUS, True,
                                           "Med-poe TLV was enabled on {device_name}.",
                                           "Med-poe TLV was DISABLED on {device_name}.",
                                           **kwargs)

    def lldp_verify_med_poe_tlv_disabled(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [port]        - The port(s) that the med-poe TLV should be disabled on.

        Verifies that the med-poe TLV is disabled on a given port.
        """
        args = {"port": port,
                "tlv": "med-poe"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_TLV_MED_POE,
                                           self.parse_const.CHECK_TLV_STATUS, False,
                                           "Med-poe TLV was disabled on {device_name}.",
                                           "Med-poe TLV was ENABLED on {device_name}.",
                                           **kwargs)

    def lldp_verify_enhanced_trans_config_tlv_enabled(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [port]        - The port(s) that the enhanced-trans-config TLV should be enabled on.

        Verifies that the enhanced-trans-config TLV is enabled on a given port.
        """
        args = {"port": port,
                "tlv": "enhanced-trans-config"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_TLV_ENHANCED_TRANS_CONFIG,
                                           self.parse_const.CHECK_TLV_STATUS, True,
                                           "Enhanced-trans-config TLV was enabled on {device_name}.",
                                           "Enhanced-trans-config TLV was DISABLED on {device_name}.",
                                           **kwargs)

    def lldp_verify_enhanced_trans_config_tlv_disabled(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [port]        - The port(s) that the enhanced-trans-config TLV should be disabled on.

        Verifies that the enhanced-trans-config TLV is disabled on a given port.
        """
        args = {"port": port,
                "tlv": "enhanced-trans-config"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_TLV_ENHANCED_TRANS_CONFIG,
                                           self.parse_const.CHECK_TLV_STATUS, False,
                                           "Enhanced-trans-config TLV was disabled on {device_name}.",
                                           "Enhanced-trans-config TLV was ENABLED on {device_name}.",
                                           **kwargs)

    def lldp_verify_enhanced_trans_rec_tlv_enabled(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [port]        - The port(s) that the enhanced-trans-rec TLV should be enabled on.

        Verifies that the enhanced-trans-rec TLV is enabled on a given port.
        """
        args = {"port": port,
                "tlv": "enhanced-trans-rec"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_TLV_ENHANCED_TRANS_REC,
                                           self.parse_const.CHECK_TLV_STATUS, True,
                                           "Enhanced-trans-rec TLV was enabled on {device_name}.",
                                           "Enhanced-trans-rec TLV was DISABLED on {device_name}.",
                                           **kwargs)

    def lldp_verify_enhanced_trans_rec_tlv_disabled(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [port]        - The port(s) that the enhanced-trans-rec TLV should be disabled on.

        Verifies that the enhanced-trans-rec TLV is disabled on a given port.
        """
        args = {"port": port,
                "tlv": "enhanced-trans-rec"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_TLV_ENHANCED_TRANS_REC,
                                           self.parse_const.CHECK_TLV_STATUS, False,
                                           "Enhanced-trans-rec TLV was enabled on {device_name}.",
                                           "Enhanced-trans-rec TLV was DISABLED on {device_name}.",
                                           **kwargs)

    def lldp_verify_priority_flowctrl_tlv_enabled(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [port]        - The port(s) that the priority-flowctrl TLV should be enabled on.

        Verifies that the priority-flowctrl TLV is enabled on a given port.
        """
        args = {"port": port,
                "tlv": "priority-flowctrl"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_TLV_PRIORITY_FLOWCTRL,
                                           self.parse_const.CHECK_TLV_STATUS, True,
                                           "Priority-flowctrl TLV was enabled on {device_name}.",
                                           "Priority-flowctrl TLV was DISABLED on {device_name}.",
                                           **kwargs)

    def lldp_verify_priority_flowctrl_tlv_disabled(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [port]        - The port(s) that the priority-flowctrl TLV should be disabled on.

        Verifies that the priority-flowctrl TLV is disabled on a given port.
        """
        args = {"port": port,
                "tlv": "priority-flowctrl"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_TLV_PRIORITY_FLOWCTRL,
                                           self.parse_const.CHECK_TLV_STATUS, False,
                                           "Priority-flowctrl TLV was disabled on {device_name}.",
                                           "Priority-flowctrl TLV was ENABLED on {device_name}.",
                                           **kwargs)

    def lldp_verify_application_pri_tlv_enabled(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [port]        - The port(s) that the application-pri TLV should be enabled on.

        Verifies that the application-pri TLV is enabled on a given port.
        """
        args = {"port": port,
                "tlv": "application-pri"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_TLV_APPLICATION_PRI,
                                           self.parse_const.CHECK_TLV_STATUS, True,
                                           "Application-pri TLV was enabled on {device_name}.",
                                           "Application-pri TLV was DISABLED on {device_name}.",
                                           **kwargs)

    def lldp_verify_application_pri_tlv_disabled(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [port]        - The port(s) that the application-pri TLV should be disabled on.

        Verifies that the application-pri TLV is disabled on a given port.
        """
        args = {"port": port,
                "tlv": "application-pri"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_TLV_APPLICATION_PRI,
                                           self.parse_const.CHECK_TLV_STATUS, False,
                                           "Application-pri TLV was disabled on {device_name}.",
                                           "Application-pri TLV was ENABLED on {device_name}.",
                                           **kwargs)

    def lldp_verify_congestion_notif_tlv_enabled(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [port]        - The port(s) that the congestion-notif TLV should be enabled on.

        Verifies that the congestion-notif TLV is enabled on a given port.
        """
        args = {"port": port,
                "tlv": "congestion-notif"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_TLV_CONGESTION_NOTIF,
                                           self.parse_const.CHECK_TLV_STATUS, True,
                                           "Congestion-notif TLV was enabled on {device_name}.",
                                           "Congestion-notif TLV was DISABLED on {device_name}.",
                                           **kwargs)

    def lldp_verify_congestion_notif_tlv_disabled(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [port]        - The port(s) that the congestion-notif TLV should be disabled on.

        Verifies that the congestion-notif TLV is disabled on a given port.
        """
        args = {"port": port,
                "tlv": "congestion-notif"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_TLV_CONGESTION_NOTIF,
                                           self.parse_const.CHECK_TLV_STATUS, False,
                                           "Congestion-notif TLV was disabled on {device_name}.",
                                           "Congestion-notif TLV was ENABLED on {device_name}.",
                                           **kwargs)

    def lldp_verify_energy_eff_eth_tlv_enabled(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [port]        - The port(s) that the energy-eff-eth TLV should be enabled on.

        Verifies that the energy-eff-eth TLV is enabled on a given port.
        """
        args = {"port": port,
                "tlv": "energy-eff-eth"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_TLV_ENERGY_EFF_ETH,
                                           self.parse_const.CHECK_TLV_STATUS, True,
                                           "Energy-eff-eth TLV was enabled on {device_name}.",
                                           "Energy-eff-eth TLV was DISABLED on {device_name}.",
                                           **kwargs)

    def lldp_verify_energy_eff_eth_tlv_disabled(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [port]        - The port(s) that the energy-eff-eth TLV should be disabled on.

        Verifies that the energy-eff-eth TLV is disabled on a given port.
        """
        args = {"port": port,
                "tlv": "energy-eff-eth"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_TLV_ENERGY_EFF_ETH,
                                           self.parse_const.CHECK_TLV_STATUS, False,
                                           "Energy-eff-eth TLV was disabled on {device_name}.",
                                           "Energy-eff-eth TLV was ENABLED on {device_name}.",
                                           **kwargs)

    def lldp_verify_transmit_enabled_on_port(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [port]        - The port on which LLDP packet transmission should be disabled.

        Verifies that the specified port IS configured to transmit LLDP packets.
        """
        args = {"port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_STATUS,
                                           self.parse_const.DETERMINE_LLDP_PORT_TRANSMIT_STATE, True,
                                           "LLDP Transmission is ENABLED on {device_name} port {port}.",
                                           "LLDP Transmission is DISABLED on {device_name} port {port}.",
                                           **kwargs)

    def lldp_verify_transmit_disabled_on_port(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [port]        - The port on which LLDP packet transmission should be disabled.

        Verifies that the specified port IS NOT configured to transmit LLDP packets.
        """
        args = {"port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_STATUS,
                                           self.parse_const.DETERMINE_LLDP_PORT_TRANSMIT_STATE, False,
                                           "LLDP Transmission is DISABLED on {device_name} port {port}.",
                                           "LLDP Transmission is ENABLED on {device_name} port {port}.",
                                           **kwargs)

    def lldp_verify_receive_enabled_on_port(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [port]        - The port on which LLDP packet transmission should be disabled.

        Verifies that the specified port IS configured to transmit LLDP packets.
        """
        args = {"port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_STATUS,
                                           self.parse_const.DETERMINE_LLDP_PORT_RECEIVE_STATE, True,
                                           "LLDP Reception is ENABLED on {device_name} port {port}.",
                                           "LLDP Reception is DISABLED on {device_name} port {port}.",
                                           **kwargs)

    def lldp_verify_receive_disabled_on_port(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [port]        - The port on which LLDP packet transmission should be disabled.

        Verifies that the specified port IS NOT configured to transmit LLDP packets.
        """
        args = {"port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_STATUS,
                                           self.parse_const.DETERMINE_LLDP_PORT_RECEIVE_STATE, False,
                                           "LLDP Reception is DISABLED on {device_name} port {port}.",
                                           "LLDP Reception is ENABLED on {device_name} port {port}.",
                                           **kwargs)

    def lldp_verify_remote_port(self, device_name, port='', remote_port='', **kwargs):
        """
        Keyword Arguments:
        ***Ports list and Remote_Ports list must be the same length!***
        [device_name] - The device or devices the keyword will be run against.
        [port]        - The ports on which LLDP remote port ID will be verified.
        [remote_port] - The remote port IDs of the respective local Network Element ports.

        Verifies the remote port(s) are correct for the specified local port(s).
        """
        port = ListUtils.convert_to_list(port)
        remote_port = ListUtils.convert_to_list(remote_port)

        args = {"port": port,
                "remote_port": remote_port}

        if len(port) > len(remote_port):
            self._determine_result(False, True, "", "Local port list has more ports than remote_port list")
        elif len(port) < len(remote_port):
            self._determine_result(False, True, "", "Local port list has fewer ports than remote_port list")
        else:
            return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_REMOTE_INFO,
                                               self.parse_const.CHECK_LLDP_REMOTE_PORT, True,
                                               "LLDP Neighbor on port {port} is {remote_port}.",
                                               "LLDP Neighbor on port {port} is NOT {remote_port}.",
                                               **kwargs)

    def lldp_verify_neighbor_sysname(self, device_name, port='', neighbor_sysname='', **kwargs):
        """
        Keyword Arguments:
        ***Ports list and Neighbor System Name list must be the same length!***
        [device_name]      - The device or devices the keyword will be run against.
        [port]             - The ports on which LLDP Neighbor System Name will be verified.
        [neighbor_sysname] - The Neighbor System Name of the respective local Network Element ports.

        Waits for the Neighbor System Name to be true for the specified local port(s).
        """
        port = ListUtils.convert_to_list(port)
        neighbor_sysname = ListUtils.convert_to_list(neighbor_sysname)

        args = {"port": port,
                "neighbor_sysname": neighbor_sysname}

        if len(port) > len(neighbor_sysname):
            self._determine_result(False, True, "", "Local port list has more ports than neighbor_sysname list")
        elif len(port) < len(neighbor_sysname):
            self._determine_result(False, True, "", "Local port list has fewer ports than neighbor_sysname list")
        else:
            return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_REMOTE_INFO,
                                               self.parse_const.CHECK_LLDP_NEIGHBOR_SYSNAME, True,
                                               "LLDP Sysname Neighbor on port {port} is {neighbor_sysname}.",
                                               "LLDP Sysname Neighbor on port {port} is NOT {neighbor_sysname}.",
                                               **kwargs)
