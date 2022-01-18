from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiInterfaceConfigApi import InterfaceConfigApi, InterfaceConfigConstants

"""
    This is the API class for the command: interface_config

    Class is auto-generated. If you update anything here,
        it will be over written.
"""


class IxiaInterfaceConfigApi(InterfaceConfigApi):

    """
    init function
    """
    def __init__(self, device):
        super(IxiaInterfaceConfigApi, self).__init__(device)

    """
    This is the "One Large Method" for the command: interface_config
    use this by passing in a dict() of all the commands

        api = device.getApi(InterfaceConfigConstants.INTERFACE_CONFIG_API)
        api.interface_config(dummyDict)
    """
    def interface_config(self, argdictionary):
        return super(IxiaInterfaceConfigApi, self).interface_config(argdictionary, self.supportedIxiaHltapiCommands)

    """
    Individual commands for each option. Typically, the "One Large Method"
    is the one that you want to be using so look at that example above
    """
    def interface_config_additional_fcoe_stat_1(self, opt):
        """
        This is the method the command: interface_config option additional_fcoe_stat_1
        Description:Valid only with ixnetwork api and when enable_data_center_shared_stats is 1.
            Valid options are:
            Not defined
            fcoe_invalid_frames: FCoE invalid frames
            fcoe_invalid_size: FCoE invalid size
            fcoe_normal_size_bad_fc_crc: FCoE normal size, bad FC-CRC
            fcoe_normal_size_good_fc_crc: FCoE normal size, good FC-CRC
            fcoe_undersize_bad_fc_crc: FCoE undersize, bad FC-CRC
            fcoe_undersize_good_fc_crc: FCoE undersize, good FC-CRC
            fcoe_valid_frames: FCoE valid frames
        Constants Available: ADDITIONAL_FCOE_STAT_1_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.ADDITIONAL_FCOE_STAT_1_CMD : opt})

    def interface_config_additional_fcoe_stat_2(self, opt):
        """
        This is the method the command: interface_config option additional_fcoe_stat_2
        Description:Valid only with ixnetwork api and when enable_data_center_shared_stats is 1.
            Valid options are:
            Not defined
            fcoe_invalid_frames: FCoE invalid frames
            fcoe_invalid_size: FCoE invalid size
            fcoe_normal_size_bad_fc_crc: FCoE normal size, bad FC-CRC
            fcoe_normal_size_good_fc_crc: FCoE normal size, good FC-CRC
            fcoe_undersize_bad_fc_crc: FCoE undersize, bad FC-CRC
            fcoe_undersize_good_fc_crc: FCoE undersize, good FC-CRC
            fcoe_valid_frames: FCoE valid frames
        Constants Available: ADDITIONAL_FCOE_STAT_2_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.ADDITIONAL_FCOE_STAT_2_CMD : opt})

    def interface_config_addresses_per_svlan(self, range):
        """
        This is the method the command: interface_config option addresses_per_svlan
        Description:How often a new outer VLAN ID is generated. For stacked vlans this parameter accepts a list of elements, each element being represented by numbers separated through comma(,). This parameter is valid only when l23_config_type is static_endpoint (new API).
        Constants Available: ADDRESSES_PER_SVLAN_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.ADDRESSES_PER_SVLAN_CMD : range})

    def interface_config_addresses_per_vci(self, range):
        """
        This is the method the command: interface_config option addresses_per_vci
        Description:How often a new VCI value is generated. This parameter is valid only when l23_config_type is static_endpoint (new API).
        Constants Available: ADDRESSES_PER_VCI_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.ADDRESSES_PER_VCI_CMD : range})

    def interface_config_addresses_per_vlan(self, range):
        """
        This is the method the command: interface_config option addresses_per_vlan
        Description:How often a new VLAN ID/inner VLAN ID is generated. For stacked vlans this parameter accepts a list of elements, each element being represented by numbers separated through comma(,). This parameter is valid only when l23_config_type is static_endpoint (new API).
        Constants Available: ADDRESSES_PER_VLAN_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.ADDRESSES_PER_VLAN_CMD : range})

    def interface_config_addresses_per_vpi(self, range):
        """
        This is the method the command: interface_config option addresses_per_vpi
        Description:How often a new VPI value is generated. This parameter is valid only when l23_config_type is static_endpoint (new API).
        Constants Available: ADDRESSES_PER_VPI_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.ADDRESSES_PER_VPI_CMD : range})

    def interface_config_arp(self, bool_opt):
        """
        This is the method the command: interface_config option arp
        Description:Enables or disables the -arp_send_req parameter. If this is 0 -arp_send_req will be ignored.
        Constants Available: ARP_CMD
        Supported:IxOS/IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.ARP_CMD : bool_opt})

    def interface_config_arp_on_linkup(self, bool_opt):
        """
        This is the method the command: interface_config option arp_on_linkup
        Description:Send ARP for the IPv4 interfaces when the port link becomes up. The option is global, for all ports and interfaces. This is valid only for the new API.
        Constants Available: ARP_ON_LINKUP_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.ARP_ON_LINKUP_CMD : bool_opt})

    def interface_config_arp_refresh_interval(self, range):
        """
        This is the method the command: interface_config option arp_refresh_interval
        Description:A user configurable ARP refresh timer
        Constants Available: ARP_REFRESH_INTERVAL_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.ARP_REFRESH_INTERVAL_CMD : range})

    def interface_config_arp_req_retries(self, numeric):
        """
        This is the method the command: interface_config option arp_req_retries
        Description:The number of times the arp request will be attempted.This option takes a list of values when -port_handle is a list of port handles. This option is valid for the old and the new APIs.
        Constants Available: ARP_REQ_RETRIES_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.ARP_REQ_RETRIES_CMD : numeric})

    def interface_config_arp_req_timer(self, range):
        """
        This is the method the command: interface_config option arp_req_timer
        Description:(deprecated) The value has no effect on the code. It was left in so as not to break existing scripts that attempt to use it.This option takes a list of values when -port_handle is a list of port handles. This option is valid for the old and the new APIs.
        Constants Available: ARP_REQ_TIMER_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.ARP_REQ_TIMER_CMD : range})

    def interface_config_atm_enable_coset(self, bool_opt):
        """
        This is the method the command: interface_config option atm_enable_coset
        Description:If 1, enables the Coset algorithm to be used with the Header Error Control (HEC) byte. This option takes a list of values when -port_handle is a list of port handles.
        Constants Available: ATM_ENABLE_COSET_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.ATM_ENABLE_COSET_CMD : bool_opt})

    def interface_config_atm_enable_pattern_matching(self, bool_opt):
        """
        This is the method the command: interface_config option atm_enable_pattern_matching
        Description:If 1, then the use of capture and filter based on ATM patterns is enabled and the maximum number of VCCs is reduced to 12,288. This option takes a list of values when -port_handle is a list of port handles. This option is valid for the old and the new APIs.
        Constants Available: ATM_ENABLE_PATTERN_MATCHING_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.ATM_ENABLE_PATTERN_MATCHING_CMD : bool_opt})

    def interface_config_atm_encapsulation(self, opt):
        """
        This is the method the command: interface_config option atm_encapsulation
        Description:Sets atm encapsulation type for ports that support ATM feature. This option takes a list of values when -port_handle is a list of port handles. This option is valid for the old and the new APIs.
        Constants Available: ATM_ENCAPSULATION_CMD
        Supported:IxNetwork
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.ATM_ENCAPSULATION_CMD : opt})

    def interface_config_atm_filler_cell(self, opt):
        """
        This is the method the command: interface_config option atm_filler_cell
        Description:SONET frame transmission is continuous even when data or control messages are not being transmitted. This option allows the cell type that is transmitted during these intervals. This option takes a list of values when -port_handle is a list of port handles.
            Valid options are:
            idle: (default) idle cells are transmitted with VPI/VCI = 0/0 and CLP = 0.
            unassigned: unassigned cells are transmitted with VPI/VCI = 0/0 and CLP = 0.
        Constants Available: ATM_FILLER_CELL_CMD
        Supported:IxOS/IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.ATM_FILLER_CELL_CMD : opt})

    def interface_config_atm_interface_type(self, opt):
        """
        This is the method the command: interface_config option atm_interface_type
        Description:The type of interface to emulate. This option takes a list of values when -port_handle is a list of port handles. Valid choices are: uni - (default) user to network interface nni - network to network interface
        Constants Available: ATM_INTERFACE_TYPE_CMD
        Supported:IxOS/IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.ATM_INTERFACE_TYPE_CMD : opt})

    def interface_config_atm_packet_decode_mode(self, opt):
        """
        This is the method the command: interface_config option atm_packet_decode_mode
        Description:This setting controls the interpretation of received packets when they are decoded. This option takes a list of values when -port_handle is a list of port handles.
            Valid options are:
            frame: (default) Decode the packet as a frame.
            cell: Decode the packet as an ATM cell.
        Constants Available: ATM_PACKET_DECODE_MODE_CMD
        Supported:IxOS/IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.ATM_PACKET_DECODE_MODE_CMD : opt})

    def interface_config_atm_reassembly_timeout(self, numeric):
        """
        This is the method the command: interface_config option atm_reassembly_timeout
        Description:Sets the value for the Reassembly Timeout, which is the period of time (expressed in seconds) that the receive side will wait for another cell on that channel - for reassembly of cells into a CPCS PDU (packet). If no cell is received within that period, the timer will expire.This option takes a list of values when -port_handle is a list of port handles. This option is valid for the old and the new APIs.
        Constants Available: ATM_REASSEMBLY_TIMEOUT_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.ATM_REASSEMBLY_TIMEOUT_CMD : numeric})

    def interface_config_auto_detect_instrumentation_type(self, opt):
        """
        This is the method the command: interface_config option auto_detect_instrumentation_type
        Description:How to insert the instrumentation signature. Valid only is port_rx_mode is auto_detect_instrumentation. Valid only for the new API (IxTclNetwork).
            Valid options are:
            end_of_frame: the timestamp and data integrity CRC will be inserted at the end of the frame before the CRC
            floating: (default) the timestamp is part of an automatic instrumentation header. This mode should be used when the packet may get truncated or has padding. This is the IxTclProtocol equivalent.
            DEFAULT: floating
            DEPENDENCIES: Valid in combination with parameter(s)
            'port_rx_mode' | value= 'auto_detect_instrumentation' |
        Constants Available: AUTO_DETECT_INSTRUMENTATION_TYPE_CMD
        Supported:IxOS/IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.AUTO_DETECT_INSTRUMENTATION_TYPE_CMD : opt})

    def interface_config_bad_blocks_number(self, numeric):
        """
        This is the method the command: interface_config option bad_blocks_number
        Description:The number of contiguous 66-bit blocks with errors to insert between bad blocks. Valid only for Multis cards.
        Constants Available: BAD_BLOCKS_NUMBER_CMD
        Supported:IxOS
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.BAD_BLOCKS_NUMBER_CMD : numeric})

    def interface_config_bert_configuration(self, opt):
        """
        This is the method the command: interface_config option bert_configuration
        Description:This option takes a list of physical lanes . This parameter is valid only with IxTclHal api.It has the following structure::,,,,|....phy_lane - physical lane, it can take values from 0A-9A,0B-9B for 100Gig ports, and 0A-3A for 40Gig ports.tx_pattern - If set, indicates that the transmitted pattern is to be inverted. Valid options are:PRBS-31 - the 2^31 pattern as specified in ITU-T0151 is expectedPRBS-23 - the 2^23 pattern as specified in ITU-T0151 is expectedPRBS-20 - the 2^20 pattern as specified in ITU-T0151 is expectedPRBS-15 - the 2^15 pattern as specified in ITU-T0151 is expectedPRBS-11 - the 2^11 pattern as specified in ITU-T0151 is expectedPRBS-9 - the 2^9 pattern as specified in ITU-T0151 is expectedPRBS-7 - the 2^7 pattern as specified in ITU-T0151 is expectedlane_detection - used to detect the lane pattern and how the lanes are connected between portsalternating - alternating ones and zeroes are expectedall1 - all ones are expectedtx_invert - If set, indicates that the transmitted pattern is to be inverted. Valid options are:0 - disable1- enable(default = disable)rx_pattern - If set, indicates the expected receive pattern. Valid options are:PRBS-31 - the 2^31 pattern as specified in ITU-T0151 is expectedPRBS-23 - the 2^23 pattern as specified in ITU-T0151 is expectedPRBS-20 - the 2^20 pattern as specified in ITU-T0151 is expectedPRBS-15 - the 2^15 pattern as specified in ITU-T0151 is expectedPRBS-11 - the 2^11 pattern as specified in ITU-T0151 is expectedPRBS-9 - the 2^9 pattern as specified in ITU-T0151 is expectedPRBS-7 - the 2^7 pattern as specified in ITU-T0151 is expectedauto_detect - the pattern is automatically detected by the receiver.alternating - alternating ones and zeroes are expected.all1 - all ones are expected.rx_invert -If txRxPatternMode is set to independent, this indicates that the expected receivepattern is to be inverted. Valid options are:0 - disable1 - enable(default = disable)enable_stats - Only applicable when bert mode is active. If set, enables BERT lanestatistics to be collected. Valid options are:0 - disable1 - enable(default = disable)
        Constants Available: BERT_CONFIGURATION_CMD
        Supported:IxOS, IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.BERT_CONFIGURATION_CMD : opt})

    def interface_config_bert_error_insertion(self, opt):
        """
        This is the method the command: interface_config option bert_error_insertion
        Description:This command is used to configure the insertion of deliberate errors on a port. It takes a list of physical lanes for the error insertion. This parameter is valid only with IxTclHal api. It has the following structure: :,,,|.... phy_lane - physical lane, it can take values from 0A-9A,0B-9B for 100Gig ports, and 0A-3A for 40Gig ports. single_error - insert single error value error_bit_rate - a 32-bit mask, expressed as a list of four one-byte elements, which indicates which bit in a 32-bit word is to be errored. (default = 1) error_bit_rate_unit - During continuous burst rate situations, this is the error rate. Valid options are: e-2 - An error is inserted every 2^2 (4) bits. e-3 - An error is inserted every 2^3 (8) bits. e-4 - An error is inserted every 2^4 (16) bits. e-5 - An error is inserted every 2^5 (32) bits. e-6 - An error is inserted every 2^6 (64) bits. e-7 - An error is inserted every 2^7 (128) bits. e-8 - An error is inserted every 2^8 (256) bits. e-9 - An error is inserted every 2^9 (512) bits. e-10 - An error is inserted every 2^10 (1024) bits. e-11 - An error is inserted every 2^11 (2048) bits. insert - choose whether to insert the error or not
        Constants Available: BERT_ERROR_INSERTION_CMD
        Supported:IxOS, IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.BERT_ERROR_INSERTION_CMD : opt})

    def interface_config_check_gateway_exists(self, bool_opt):
        """
        This is the method the command: interface_config option check_gateway_exists
        Description:If 0, this check offers the possibility of creating routed/unconnected interfaces as connected interfaces.If 1, the command will check if the provided gateway address can be found on an existing interface. If an interface with the gateway IP address exists, the interface required will be configured as unconnected.
        Constants Available: CHECK_GATEWAY_EXISTS_CMD
        Supported:IxOS/IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.CHECK_GATEWAY_EXISTS_CMD : bool_opt})

    def interface_config_connected_count(self, numeric):
        """
        This is the method the command: interface_config option connected_count
        Description:The number of connected interfaces to be created, when trying to create multiple interfaces with a single interface_config call. This option takes a list of values when -port_handle is a list of port handles. This option is valid only when static_enable is 0 and l23_config_type is static_endpoint or protocol_interface(new API).
            DEFAULT: 1
            DEPENDENCIES: Valid in combination with parameter(s)
            'static_enable' | value= '0' |
        Constants Available: CONNECTED_COUNT_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.CONNECTED_COUNT_CMD : numeric})

    def interface_config_connected_to_handle(self, bool_opt):
        """
        This is the method the command: interface_config option connected_to_handle
        Description:A handle to another ethernet or loopback stack through which the current protocol stack will be connected. This argument will be ignored if the current protocol stack does not support connectors.
        Constants Available: CONNECTED_TO_HANDLE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.CONNECTED_TO_HANDLE_CMD : bool_opt})

    def interface_config_data_integrity(self, bool_opt):
        """
        This is the method the command: interface_config option data_integrity
        Description:Whether to enable the data integrity checking capability on the port. This option takes a list of values when -port_handle is a list of port handles. Valid options are: 0 - Disable (DEFAULT) 1 - Enable
        Constants Available: DATA_INTEGRITY_CMD
        Supported:IxOS/IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.DATA_INTEGRITY_CMD : bool_opt})

    def interface_config_enable_data_center_shared_stats(self, bool_opt):
        """
        This is the method the command: interface_config option enable_data_center_shared_stats
        Description:Valid only with ixnetwork api. Globally enable Data Center Shared Statistics. Valid choices are: 0 (default) - disabled 1 - enabled
        Constants Available: ENABLE_DATA_CENTER_SHARED_STATS_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.ENABLE_DATA_CENTER_SHARED_STATS_CMD : bool_opt})

    def interface_config_enable_flow_control(self, bool_opt):
        """
        This is the method the command: interface_config option enable_flow_control
        Description:If 1, enables the port's MAC flow control and mechanisms to listen for a directed address pause message. Valid only with ixnetwork api.
            Valid options are:
            0: disable
            1: enable
        Constants Available: ENABLE_FLOW_CONTROL_CMD
        Supported:IxOS/IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.ENABLE_FLOW_CONTROL_CMD : bool_opt})

    def interface_config_enable_loopback(self, opt):
        """
        This is the method the command: interface_config option enable_loopback
        Description:This argument can be used to trigger the addition of loopback IPv4 or IPv6 protocols instead of the usual ones.
        Constants Available: ENABLE_LOOPBACK_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.ENABLE_LOOPBACK_CMD : opt})

    def interface_config_enable_ndp(self, bool_opt):
        """
        This is the method the command: interface_config option enable_ndp
        Description:Enables or disables the -send_router_solicitation and -ndp_send_req parameters. If this is 0 both -send_router_solicitation and -ndp_send_req will be ignored.
        Constants Available: ENABLE_NDP_CMD
        Supported:IxOS/IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.ENABLE_NDP_CMD : bool_opt})

    def interface_config_enable_rs_fec(self, bool_opt):
        """
        This is the method the command: interface_config option enable_rs_fec
        Description:Enable RS-FEC (Reed Solomon - Forward Error Correction). RS-FEC is a encoding mechanism to improve Bit Error Rate across a channel.
        Constants Available: ENABLE_RS_FEC_CMD
        Supported:IxNetwork-FT
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.ENABLE_RS_FEC_CMD : bool_opt})

    def interface_config_enable_rs_fec_statistics(self, bool_opt):
        """
        This is the method the command: interface_config option enable_rs_fec_statistics
        Description:Enable RS-FEC Statistics
        Constants Available: ENABLE_RS_FEC_STATISTICS_CMD
        Supported:IxNetwork-FT
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.ENABLE_RS_FEC_STATISTICS_CMD : bool_opt})

    def interface_config_ethernet_attempt_enabled(self, bool_opt):
        """
        This is the method the command: interface_config option ethernet_attempt_enabled
        Constants Available: ETHERNET_ATTEMPT_ENABLED_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.ETHERNET_ATTEMPT_ENABLED_CMD : bool_opt})

    def interface_config_ethernet_attempt_interval(self, numeric):
        """
        This is the method the command: interface_config option ethernet_attempt_interval
        Description:Time interval used to calculate the rate for triggering an action(rate = count/interval)
        Constants Available: ETHERNET_ATTEMPT_INTERVAL_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.ETHERNET_ATTEMPT_INTERVAL_CMD : numeric})

    def interface_config_ethernet_attempt_rate(self, range):
        """
        This is the method the command: interface_config option ethernet_attempt_rate
        Description:Specifies the rate in attempts/second at which attempts are made to bring up sessions. When using IxNetwork this parameter can take values from the 1-1000 range.
        Constants Available: ETHERNET_ATTEMPT_RATE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.ETHERNET_ATTEMPT_RATE_CMD : range})

    def interface_config_ethernet_attempt_scale_mode(self, opt):
        """
        This is the method the command: interface_config option ethernet_attempt_scale_mode
        Description:Indicates whether the control is specified per port or per device group. This setting is global for all the ethernet protocols configured in the ixncfg and can be configured just when handle is /globals meaning that the user wants to configure only global protocol settings.
        Constants Available: ETHERNET_ATTEMPT_SCALE_MODE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.ETHERNET_ATTEMPT_SCALE_MODE_CMD : opt})

    def interface_config_ethernet_diconnect_enabled(self, bool_opt):
        """
        This is the method the command: interface_config option ethernet_diconnect_enabled
        Constants Available: ETHERNET_DICONNECT_ENABLED_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.ETHERNET_DICONNECT_ENABLED_CMD : bool_opt})

    def interface_config_ethernet_disconnect_interval(self, numeric):
        """
        This is the method the command: interface_config option ethernet_disconnect_interval
        Description:Time interval used to calculate the rate for triggering an action(rate = count/interval)
        Constants Available: ETHERNET_DISCONNECT_INTERVAL_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.ETHERNET_DISCONNECT_INTERVAL_CMD : numeric})

    def interface_config_ethernet_disconnect_rate(self, range):
        """
        This is the method the command: interface_config option ethernet_disconnect_rate
        Description:Specifies the rate in attempts/second at which attempts are made to disconnect sessions. When using IxNetwork this parameter can take values from the 1-1000 range.
        Constants Available: ETHERNET_DISCONNECT_RATE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.ETHERNET_DISCONNECT_RATE_CMD : range})

    def interface_config_ethernet_disconnect_scale_mode(self, opt):
        """
        This is the method the command: interface_config option ethernet_disconnect_scale_mode
        Description:Indicates whether the control is specified per port or per device group. This setting is global for all the ethernet protocols configured in the ixncfg and can be configured just when handle is /globals meaning that the user wants to configure only global protocol settings.
        Constants Available: ETHERNET_DISCONNECT_SCALE_MODE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.ETHERNET_DISCONNECT_SCALE_MODE_CMD : opt})

    def interface_config_fc_credit_starvation_value(self, numeric):
        """
        This is the method the command: interface_config option fc_credit_starvation_value
        Description:Valid only with ixnetwork api. If selected, the programs encounter a delay valuespecified in the Hold R_RDY field. The counter starts counting down after it receives the first frame. The port holds R_RDY for all frames received until counterreaches to 0.Valid only when intf_mode is fc.
        Constants Available: FC_CREDIT_STARVATION_VALUE_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.FC_CREDIT_STARVATION_VALUE_CMD : numeric})

    def interface_config_fc_fixed_delay_value(self, range):
        """
        This is the method the command: interface_config option fc_fixed_delay_value
        Description:Valid only with ixnetwork api. Internal delays the R_RDY primitive signals.Valid only when intf_mode is fc.
        Constants Available: FC_FIXED_DELAY_VALUE_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.FC_FIXED_DELAY_VALUE_CMD : range})

    def interface_config_fc_force_errors(self, opt):
        """
        This is the method the command: interface_config option fc_force_errors
        Description:Valid only with ixnetwork api. Configure the port to introduce errors in the transmission of R_RDYPrimitives Signals. Valid only when intf_mode is fc. Valid choices are: no_errors (default) no_rrdy no_rrdy_every
        Constants Available: FC_FORCE_ERRORS_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.FC_FORCE_ERRORS_CMD : opt})

    def interface_config_fc_max_delay_for_random_value(self, range):
        """
        This is the method the command: interface_config option fc_max_delay_for_random_value
        Description:Valid only with ixnetwork api. The maximum random delay value for the R_RDY primitives. Valid only when intf_mode is fc.
        Constants Available: FC_MAX_DELAY_FOR_RANDOM_VALUE_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.FC_MAX_DELAY_FOR_RANDOM_VALUE_CMD : range})

    def interface_config_fc_min_delay_for_random_value(self, numeric):
        """
        This is the method the command: interface_config option fc_min_delay_for_random_value
        Description:Valid only with ixnetwork api. The minimum random delay value for the R_RDY primitives.Valid only when intf_mode is fc.
        Constants Available: FC_MIN_DELAY_FOR_RANDOM_VALUE_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.FC_MIN_DELAY_FOR_RANDOM_VALUE_CMD : numeric})

    def interface_config_fc_no_rrdy_after(self, numeric):
        """
        This is the method the command: interface_config option fc_no_rrdy_after
        Description:Valid only with ixnetwork api. Send R_RDY signals without any delay.Valid only when intf_mode is fc.
        Constants Available: FC_NO_RRDY_AFTER_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.FC_NO_RRDY_AFTER_CMD : numeric})

    def interface_config_fc_rrdy_response_delays(self, opt):
        """
        This is the method the command: interface_config option fc_rrdy_response_delays
        Description:Valid only with ixnetwork api. The internal delays for the transmission of R_RDY Primitive Signal Valid only when intf_mode is fc. Valid choices are: credit_starvation fixed_delay no_delay (default) random_delay
        Constants Available: FC_RRDY_RESPONSE_DELAYS_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.FC_RRDY_RESPONSE_DELAYS_CMD : opt})

    def interface_config_fc_tx_ignore_available_credits(self, bool_opt):
        """
        This is the method the command: interface_config option fc_tx_ignore_available_credits
        Description:Valid only with ixnetwork api. Valid only when intf_mode is fc. Valid choices are: 0 (default) - disable 1 - enable
        Constants Available: FC_TX_IGNORE_AVAILABLE_CREDITS_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.FC_TX_IGNORE_AVAILABLE_CREDITS_CMD : bool_opt})

    def interface_config_fc_tx_ignore_rx_link_faults(self, opt):
        """
        This is the method the command: interface_config option fc_tx_ignore_rx_link_faults
        Description:DEPRECATED - Please use tx_ignore_rx_link_faults instead.
        Constants Available: FC_TX_IGNORE_RX_LINK_FAULTS_CMD
        Supported:IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.FC_TX_IGNORE_RX_LINK_FAULTS_CMD : opt})

    def interface_config_fcoe_flow_control_type(self, opt):
        """
        This is the method the command: interface_config option fcoe_flow_control_type
        Description:Valid only with ixnetwork api. Selects and configures a flow control protocol for the FCoE Client port. Valid only when intf_mode is ethernet_fcoe and speed is ether10000wan or ether10000lan. Valid choices are: ieee802.3x - ieee802.3x ieee802.1Qbb (default) - ieee802.1Qbb
            DEPENDENCIESValid in combination with parameter(s)
            'intf_mode' | value= 'ethernet_fcoe' |
            'speed' | value= 'ether10000wan' |
            'speed' | value= 'ether10000lan' |
        Constants Available: FCOE_FLOW_CONTROL_TYPE_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.FCOE_FLOW_CONTROL_TYPE_CMD : opt})

    def interface_config_fcoe_priority_group_size(self, opt):
        """
        This is the method the command: interface_config option fcoe_priority_group_size
        Description:Valid only with ixnetwork api and when intf_mode is ethernet_fcoe and speed is ether10000wan or ether10000lan. Configure the size of a priority group. Valid choices are: 4 - 4 8 (default) - 8
        Constants Available: FCOE_PRIORITY_GROUP_SIZE_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.FCOE_PRIORITY_GROUP_SIZE_CMD : opt})

    def interface_config_fcoe_priority_groups(self, opt):
        """
        This is the method the command: interface_config option fcoe_priority_groups
        Description:Valid only with ixnetwork api and when intf_mode is ethernet_fcoe and speed is ether10000wan or ether10000lan. If 802.3Qbb is selected as the fcoe_flow_control_type, the PFC/Priority settings is used to map each of the eight PFC priorities to one of the four Priority Groups (or to none). The Priority Groups are numbered 0 through 3. This parameter takes a list of values, with a length of maximum 8 elements 0,1,2,3 or none. Example: {0 3 1 2 none 3} will configure:PFC 0 - Priority Group 0PFC 1 - Priority Group 3PFC 2 - Priority Group 1PFC 3 - Priority Group 2PFC 4 - Priority Group NonePFC 5 - Priority Group 3PFC 6 - Priority Group NonePFC 7 - Priority Group None
        Constants Available: FCOE_PRIORITY_GROUPS_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.FCOE_PRIORITY_GROUPS_CMD : opt})

    def interface_config_flow_control_directed_addr(self, opt):
        """
        This is the method the command: interface_config option flow_control_directed_addr
        Description:The 48-bit MAC address that the port listens on for a directed pause.Valid only with ixnetwork api.
        Constants Available: FLOW_CONTROL_DIRECTED_ADDR_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.FLOW_CONTROL_DIRECTED_ADDR_CMD : opt})

    def interface_config_gateway_incr_mode(self, opt):
        """
        This is the method the command: interface_config option gateway_incr_mode
        Description:Determines when the gateway addresses are incremented. This option is valid only when l23_config_type is static_endpoint (new API).
            Valid options are:
            every_subnet: (default) - A new gateway address is created for each subnet defined in the port group. With this mode, the increment operation is triggered when a range IP increment operation creates an IP address that is in a new subnet.
            every_interface: A new gateway address is created for each interface, whether or not the next address is from the same subnet.
            DEFAULT: every_subnet
            DEPENDENCIES: Valid in combination with parameter(s)
            'l23_config_type' | value= 'static_endpoint' |
        Constants Available: GATEWAY_INCR_MODE_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.GATEWAY_INCR_MODE_CMD : opt})

    def interface_config_gateway_step(self, ipv4):
        """
        This is the method the command: interface_config option gateway_step
        Description:The incrementing step for the gateway address of the interface, when connected_count is greater than 1. This option takes a list of values when -port_handle is a list of port handles. This option is valid only when l23_config_type is static_endpoint.
            DEFAULT: 0.0.0.1
            DEPENDENCIES: Valid in combination with parameter(s)
            'l23_config_type' | value= 'static_endpoint' |
        Constants Available: GATEWAY_STEP_CMD
        Supported:IxOS/IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        ipv4 --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.GATEWAY_STEP_CMD : ipv4})

    def interface_config_good_blocks_number(self, numeric):
        """
        This is the method the command: interface_config option good_blocks_number
        Description:The number of contiguous 66-bit blocks without errors to insert between bad blocks. Valid only for Multis cards.
        Constants Available: GOOD_BLOCKS_NUMBER_CMD
        Supported:IxNetwork-FT
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.GOOD_BLOCKS_NUMBER_CMD : numeric})

    def interface_config_gre_checksum_enable(self, bool_opt):
        """
        This is the method the command: interface_config option gre_checksum_enable
        Description:Enable/disable checksum on a GRE interface.This option takes a list of values when -port_handle is a list of port handles. This option is valid only when l23_config_type is protocol_interface (old and new API).
        Constants Available: GRE_CHECKSUM_ENABLE_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.GRE_CHECKSUM_ENABLE_CMD : bool_opt})

    def interface_config_gre_count(self, numeric):
        """
        This is the method the command: interface_config option gre_count
        Description:The number of GRE interfaces to be created for each connected interface. This option takes a list of values when -port_handle is a list of port handles.This option is valid only when l23_config_type is protocol_interface (old and new API).
        Constants Available: GRE_COUNT_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.GRE_COUNT_CMD : numeric})

    def interface_config_gre_dst_ip_addr(self, ip):
        """
        This is the method the command: interface_config option gre_dst_ip_addr
        Description:GRE tunnel destination IP address.This option takes a list of values when -port_handle is a list of port handles.This option is valid only when l23_config_type is protocol_interface (old and new API).
        Constants Available: GRE_DST_IP_ADDR_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.GRE_DST_IP_ADDR_CMD : ip})

    def interface_config_gre_dst_ip_addr_step(self, ip):
        """
        This is the method the command: interface_config option gre_dst_ip_addr_step
        Description:The incrementing step for the GRE Destination IP address of the interface, when connected_count is greater than 1.This option takes a list of values when -port_handle is a list of port handles.This option is valid only when l23_config_type is protocol_interface (old and new API). (DEFAULT = 0.0.0.1 | 0::1)
        Constants Available: GRE_DST_IP_ADDR_STEP_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.GRE_DST_IP_ADDR_STEP_CMD : ip})

    def interface_config_gre_ip_addr(self, ipv4):
        """
        This is the method the command: interface_config option gre_ip_addr
        Description:GRE tunnel IPv4 address. This option takes a list of values when -port_handle is a list of port handles.This option is valid only when l23_config_type is protocol_interface (old and new API).
        Constants Available: GRE_IP_ADDR_CMD
        Supported:IxNetwork-FT
        Keyword arguments:
        ipv4 --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.GRE_IP_ADDR_CMD : ipv4})

    def interface_config_gre_ip_addr_step(self, ipv4):
        """
        This is the method the command: interface_config option gre_ip_addr_step
        Description:The incrementing step for the GRE IPv4 address of the interface, when connected_count is greater than 1. This option takes a list of values when -port_handle is a list of port handles.This option is valid only when l23_config_type is protocol_interface (old and new API).
        Constants Available: GRE_IP_ADDR_STEP_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        ipv4 --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.GRE_IP_ADDR_STEP_CMD : ipv4})

    def interface_config_gre_ip_prefix_length(self, range):
        """
        This is the method the command: interface_config option gre_ip_prefix_length
        Description:The IPv4 prefix length for the GRE interface that needs to be created. This option takes a list of values when -port_handle is a list of port handles.This option is valid only when l23_config_type is protocol_interface (old and new API).
        Constants Available: GRE_IP_PREFIX_LENGTH_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.GRE_IP_PREFIX_LENGTH_CMD : range})

    def interface_config_gre_ipv6_addr(self, ipv6):
        """
        This is the method the command: interface_config option gre_ipv6_addr
        Description:GRE tunnel IPv6 address. This option takes a list of values when -port_handle is a list of port handles.This option is valid only when l23_config_type is protocol_interface (old and new API).
        Constants Available: GRE_IPV6_ADDR_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        ipv6 --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.GRE_IPV6_ADDR_CMD : ipv6})

    def interface_config_gre_ipv6_addr_step(self, ipv6):
        """
        This is the method the command: interface_config option gre_ipv6_addr_step
        Description:The incrementing step for the GRE IPv6 address of the interface, when connected_count is greater than 1. This option takes a list of values when -port_handle is a list of port handles.This option is valid only when l23_config_type is protocol_interface (old and new API).
        Constants Available: GRE_IPV6_ADDR_STEP_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        ipv6 --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.GRE_IPV6_ADDR_STEP_CMD : ipv6})

    def interface_config_gre_ipv6_prefix_length(self, range):
        """
        This is the method the command: interface_config option gre_ipv6_prefix_length
        Description:The IPv6 prefix length for the GRE interface that needs to be created. This option takes a list of values when -port_handle is a list of port handles.This option is valid only when l23_config_type is protocol_interface (old and new API).
        Constants Available: GRE_IPV6_PREFIX_LENGTH_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.GRE_IPV6_PREFIX_LENGTH_CMD : range})

    def interface_config_gre_key_enable(self, bool_opt):
        """
        This is the method the command: interface_config option gre_key_enable
        Description:Enable/disable key on a GRE interface. This option takes a list of values when -port_handle is a list of port handles.This option is valid only when l23_config_type is protocol_interface (old and new API).
        Constants Available: GRE_KEY_ENABLE_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.GRE_KEY_ENABLE_CMD : bool_opt})

    def interface_config_gre_key_in(self, range):
        """
        This is the method the command: interface_config option gre_key_in
        Description:Value of the IN key on a GRE interface. This option takes a list of values when -port_handle is a list of port handles. This option is valid only when l23_config_type is protocol_interface.
            DEPENDENCIES: Valid in combination with parameter(s)
            'l23_config_type' | value= 'protocol_interface' |
            'gre_key_enable' | value= '1' |
        Constants Available: GRE_KEY_IN_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.GRE_KEY_IN_CMD : range})

    def interface_config_gre_key_out(self, range):
        """
        This is the method the command: interface_config option gre_key_out
        Description:Value of the OUT key on a GRE interface. This option takes a list of values when -port_handle is a list of port handles. This option is valid only when l23_config_type is protocol_interface.
            DEPENDENCIES: Valid in combination with parameter(s)
            'l23_config_type' | value= 'protocol_interface' |
            'gre_key_enable' | value= '1' |
        Constants Available: GRE_KEY_OUT_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.GRE_KEY_OUT_CMD : range})

    def interface_config_gre_seq_enable(self, bool_opt):
        """
        This is the method the command: interface_config option gre_seq_enable
        Description:Enable/disable sequencing on a GRE interface. This option takes a list of values when -port_handle is a list of port handles.This option is valid only when l23_config_type is protocol_interface (old and new API).
        Constants Available: GRE_SEQ_ENABLE_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.GRE_SEQ_ENABLE_CMD : bool_opt})

    def interface_config_ieee_media_defaults(self, bool_opt):
        """
        This is the method the command: interface_config option ieee_media_defaults
        Description:ieee l1 media defaults
        Constants Available: IEEE_MEDIA_DEFAULTS_CMD
        Supported:IxNetwork-FT
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.IEEE_MEDIA_DEFAULTS_CMD : bool_opt})

    def interface_config_integrity_signature(self, opt):
        """
        This is the method the command: interface_config option integrity_signature
        Description:Signature used in the packet for data integrity checking. When the Receive Mode for a port is configured to check for data integrity, received packets are matched for the data integrity signature value. This signature is a 4-byte value. This option takes a list of values when -port_handle is a list of port handles. This is valid only for the old API (IxTclProtocol).(DEFAULT = 08 71 18 05)
        Constants Available: INTEGRITY_SIGNATURE_CMD
        Supported:IxOS, IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.INTEGRITY_SIGNATURE_CMD : opt})

    def interface_config_integrity_signature_offset(self, range):
        """
        This is the method the command: interface_config option integrity_signature_offset
        Description:The offset of the data integrity signature in the packet. If -port_rx_mode is set to auto_detect_instrumentation then this offset will be ignored, only the -integrity_signature is needed. This option takes a list of values when -port_handle is a list of port handles. This is valid only for the old API (IxTclProtocol).(DEFAULT = 40 bytes)
        Constants Available: INTEGRITY_SIGNATURE_OFFSET_CMD
        Supported:IxOS, IxNetwork-NGPF
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.INTEGRITY_SIGNATURE_OFFSET_CMD : range})

    def interface_config_intf_ip_addr_step(self, ipv4):
        """
        This is the method the command: interface_config option intf_ip_addr_step
        Description:The incrementing step for the IPv4 address of the interface, when connected_count is greater than 1. This option takes a list of values when -port_handle is a list of port handles. This is valid only for the new API. DEFAULT: 0.0.0.1
        Constants Available: INTF_IP_ADDR_STEP_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        ipv4 --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.INTF_IP_ADDR_STEP_CMD : ipv4})

    def interface_config_ipv4_attempt_enabled(self, bool_opt):
        """
        This is the method the command: interface_config option ipv4_attempt_enabled
        Constants Available: IPV4_ATTEMPT_ENABLED_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.IPV4_ATTEMPT_ENABLED_CMD : bool_opt})

    def interface_config_ipv4_attempt_interval(self, numeric):
        """
        This is the method the command: interface_config option ipv4_attempt_interval
        Description:Time interval used to calculate the rate for triggering an action(rate = count/interval)
        Constants Available: IPV4_ATTEMPT_INTERVAL_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.IPV4_ATTEMPT_INTERVAL_CMD : numeric})

    def interface_config_ipv4_attempt_rate(self, range):
        """
        This is the method the command: interface_config option ipv4_attempt_rate
        Description:Specifies the rate in attempts/second at which attempts are made to bring up sessions. When using IxNetwork this parameter can take values from the 1-1000 range.
        Constants Available: IPV4_ATTEMPT_RATE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.IPV4_ATTEMPT_RATE_CMD : range})

    def interface_config_ipv4_attempt_scale_mode(self, opt):
        """
        This is the method the command: interface_config option ipv4_attempt_scale_mode
        Description:Indicates whether the control is specified per port or per device group. This setting is global for all the IPv4 protocols configured in the ixncfg and can be configured just when handle is /globals meaning that the user wants to configure only global protocol settings.
            Valid options are:
            port
            device_group
        Constants Available: IPV4_ATTEMPT_SCALE_MODE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.IPV4_ATTEMPT_SCALE_MODE_CMD : opt})

    def interface_config_ipv4_diconnect_enabled(self, bool_opt):
        """
        This is the method the command: interface_config option ipv4_diconnect_enabled
        Constants Available: IPV4_DICONNECT_ENABLED_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.IPV4_DICONNECT_ENABLED_CMD : bool_opt})

    def interface_config_ipv4_disconnect_interval(self, numeric):
        """
        This is the method the command: interface_config option ipv4_disconnect_interval
        Description:Time interval used to calculate the rate for triggering an action(rate = count/interval)
        Constants Available: IPV4_DISCONNECT_INTERVAL_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.IPV4_DISCONNECT_INTERVAL_CMD : numeric})

    def interface_config_ipv4_disconnect_rate(self, range):
        """
        This is the method the command: interface_config option ipv4_disconnect_rate
        Description:Specifies the rate in attempts/second at which attempts are made to disconnect sessions. When using IxNetwork this parameter can take values from the 1-1000 range.
        Constants Available: IPV4_DISCONNECT_RATE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.IPV4_DISCONNECT_RATE_CMD : range})

    def interface_config_ipv4_disconnect_scale_mode(self, opt):
        """
        This is the method the command: interface_config option ipv4_disconnect_scale_mode
        Description:Indicates whether the control is specified per port or per device group. This setting is global for all the IPv4 protocols configured in the ixncfg and can be configured just when handle is /globals meaning that the user wants to configure only global protocol settings.
            Valid options are:
            port
            device_group
        Constants Available: IPV4_DISCONNECT_SCALE_MODE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.IPV4_DISCONNECT_SCALE_MODE_CMD : opt})

    def interface_config_ipv4_manual_gateway_mac(self, mac):
        """
        This is the method the command: interface_config option ipv4_manual_gateway_mac
        Description:The manual gateway MAC addresses. This option has no effect unless ipv4_autoresolve_gateway_mac is set to 0.
            DEFAULT:0000.0000.0001
            DEPENDENCIES Valid in combination with parameter(s)
            'ipv4_autoresolve_gateway_mac' | value= '0' |
        Constants Available: IPV4_MANUAL_GATEWAY_MAC_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        mac --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.IPV4_MANUAL_GATEWAY_MAC_CMD : mac})

    def interface_config_ipv4_manual_gateway_mac_step(self, mac):
        """
        This is the method the command: interface_config option ipv4_manual_gateway_mac_step
        Description:The step of the manual gateway MAC addresses. This option has no effect unless ipv4_autoresolve_gateway_mac is set to 0.
            DEFAULT: 0000.0000.0001
            DEPENDENCIES: Valid in combination with parameter(s)
            'ipv4_autoresolve_gateway_mac' | value= '0' |
        Constants Available: IPV4_MANUAL_GATEWAY_MAC_STEP_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        mac --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.IPV4_MANUAL_GATEWAY_MAC_STEP_CMD : mac})

    def interface_config_ipv4_re_send_arp_on_link_up(self, opt):
        """
        This is the method the command: interface_config option ipv4_re_send_arp_on_link_up
        Description:Resends ARP after link up.
        Constants Available: IPV4_RE_SEND_ARP_ON_LINK_UP_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.IPV4_RE_SEND_ARP_ON_LINK_UP_CMD : opt})

    def interface_config_ipv4_resolve_gateway(self, bool_opt):
        """
        This is the method the command: interface_config option ipv4_resolve_gateway
        Description:Autoresolve gateway MAC addresses.
        Constants Available: IPV4_RESOLVE_GATEWAY_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.IPV4_RESOLVE_GATEWAY_CMD : bool_opt})

    def interface_config_ipv4_send_arp_interval(self, numeric):
        """
        This is the method the command: interface_config option ipv4_send_arp_interval
        Description:Time interval used to calculate the rate for triggering an action(rate = count/interval)
        Constants Available: IPV4_SEND_ARP_INTERVAL_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.IPV4_SEND_ARP_INTERVAL_CMD : numeric})

    def interface_config_ipv4_send_arp_max_outstanding(self, range):
        """
        This is the method the command: interface_config option ipv4_send_arp_max_outstanding
        Description:The maximum number of triggered instances of an action that is still awaiting a response or completion
        Constants Available: IPV4_SEND_ARP_MAX_OUTSTANDING_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.IPV4_SEND_ARP_MAX_OUTSTANDING_CMD : range})

    def interface_config_ipv4_send_arp_rate(self, range):
        """
        This is the method the command: interface_config option ipv4_send_arp_rate
        Description:Specifies the rate in attempts/second at which attempts are made to send ARP requests on sessions. When using IxNetwork this parameter can take values from the 1-1000 range.
        Constants Available: IPV4_SEND_ARP_RATE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.IPV4_SEND_ARP_RATE_CMD : range})

    def interface_config_ipv4_send_arp_scale_mode(self, opt):
        """
        This is the method the command: interface_config option ipv4_send_arp_scale_mode
        Description:Indicates whether the control is specified per port or per device group. This setting is global for all the IPv4 protocols configured in the ixncfg and can be configured just when handle is /globals meaning that the user wants to configure only global protocol settings.
            Valid options are:
            port
            device_group
        Constants Available: IPV4_SEND_ARP_SCALE_MODE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.IPV4_SEND_ARP_SCALE_MODE_CMD : opt})

    def interface_config_ipv6_addr_mode(self, opt):
        """
        This is the method the command: interface_config option ipv6_addr_mode
        Description:The address mode for Static ipv6 endpoints. May be static or autoconfig. This option is valid only when l23_config_type is static_endpoint.
            Valid options are:
            static
            autoconfig
            DEPENDENCIES: Valid in combination with parameter(s)
            'l23_config_type' | value= 'static_endpoint' |
        Constants Available: IPV6_ADDR_MODE_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.IPV6_ADDR_MODE_CMD : opt})

    def interface_config_ipv6_attempt_enabled(self, bool_opt):
        """
        This is the method the command: interface_config option ipv6_attempt_enabled
        Constants Available: IPV6_ATTEMPT_ENABLED_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.IPV6_ATTEMPT_ENABLED_CMD : bool_opt})

    def interface_config_ipv6_attempt_interval(self, numeric):
        """
        This is the method the command: interface_config option ipv6_attempt_interval
        Description:Time interval used to calculate the rate for triggering an action(rate = count/interval)
        Constants Available: IPV6_ATTEMPT_INTERVAL_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.IPV6_ATTEMPT_INTERVAL_CMD : numeric})

    def interface_config_ipv6_attempt_rate(self, range):
        """
        This is the method the command: interface_config option ipv6_attempt_rate
        Description:Specifies the rate in attempts/second at which attempts are made to bring up sessions. When using IxNetwork this parameter can take values from the 1-1000 range.
        Constants Available: IPV6_ATTEMPT_RATE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.IPV6_ATTEMPT_RATE_CMD : range})

    def interface_config_ipv6_attempt_scale_mode(self, opt):
        """
        This is the method the command: interface_config option ipv6_attempt_scale_mode
        Description:Indicates whether the control is specified per port or per device group. This setting is global for all the IPv6 protocols configured in the ixncfg and can be configured just when handle is /globals meaning that the user wants to configure only global protocol settings.
            Valid options are:
            port
            device_group
        Constants Available: IPV6_ATTEMPT_SCALE_MODE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.IPV6_ATTEMPT_SCALE_MODE_CMD : opt})

    def interface_config_ipv6_autoconfiguration_attempt_enabled(self, bool_opt):
        """
        This is the method the command: interface_config option ipv6_autoconfiguration_attempt_enabled
        Constants Available: IPV6_AUTOCONFIGURATION_ATTEMPT_ENABLED_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.IPV6_AUTOCONFIGURATION_ATTEMPT_ENABLED_CMD : bool_opt})

    def interface_config_ipv6_autoconfiguration_attempt_interval(self, numeric):
        """
        This is the method the command: interface_config option ipv6_autoconfiguration_attempt_interval
        Description:Time interval used to calculate the rate for triggering an action(rate = count/interval)
        Constants Available: IPV6_AUTOCONFIGURATION_ATTEMPT_INTERVAL_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.IPV6_AUTOCONFIGURATION_ATTEMPT_INTERVAL_CMD : numeric})

    def interface_config_ipv6_autoconfiguration_attempt_max_outstanding(self, range):
        """
        This is the method the command: interface_config option ipv6_autoconfiguration_attempt_max_outstanding
        Description:The maximum number of triggered instances of an action that is still awaiting a response or completion
        Constants Available: IPV6_AUTOCONFIGURATION_ATTEMPT_MAX_OUTSTANDING_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.IPV6_AUTOCONFIGURATION_ATTEMPT_MAX_OUTSTANDING_CMD : range})

    def interface_config_ipv6_autoconfiguration_attempt_rate(self, range):
        """
        This is the method the command: interface_config option ipv6_autoconfiguration_attempt_rate
        Description:Specifies the rate in attempts/second at which attempts are made to bring up sessions. When using IxNetwork this parameter can take values from the 1-1000 range.
        Constants Available: IPV6_AUTOCONFIGURATION_ATTEMPT_RATE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.IPV6_AUTOCONFIGURATION_ATTEMPT_RATE_CMD : range})

    def interface_config_ipv6_autoconfiguration_attempt_scale_mode(self, opt):
        """
        This is the method the command: interface_config option ipv6_autoconfiguration_attempt_scale_mode
        Description:Indicates whether the control is specified per port or per device group. This setting is global for all the IPv6 Autoconfiguration protocols configured in the ixncfg and can be configured just when handle is /globals meaning that the user wants to configure only global protocol settings.
            Valid options are:
            port
            device_group
        Constants Available: IPV6_AUTOCONFIGURATION_ATTEMPT_SCALE_MODE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.IPV6_AUTOCONFIGURATION_ATTEMPT_SCALE_MODE_CMD : opt})

    def interface_config_ipv6_autoconfiguration_disconnect_enabled(self, bool_opt):
        """
        This is the method the command: interface_config option ipv6_autoconfiguration_disconnect_enabled
        Constants Available: IPV6_AUTOCONFIGURATION_DISCONNECT_ENABLED_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.IPV6_AUTOCONFIGURATION_DISCONNECT_ENABLED_CMD : bool_opt})

    def interface_config_ipv6_autoconfiguration_disconnect_interval(self, numeric):
        """
        This is the method the command: interface_config option ipv6_autoconfiguration_disconnect_interval
        Description:Time interval used to calculate the rate for triggering an action(rate = count/interval)
        Constants Available: IPV6_AUTOCONFIGURATION_DISCONNECT_INTERVAL_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.IPV6_AUTOCONFIGURATION_DISCONNECT_INTERVAL_CMD : numeric})

    def interface_config_ipv6_autoconfiguration_disconnect_max_outstanding(self, range):
        """
        This is the method the command: interface_config option ipv6_autoconfiguration_disconnect_max_outstanding
        Description:The maximum number of triggered instances of an action that is still awaiting a response or completion
        Constants Available: IPV6_AUTOCONFIGURATION_DISCONNECT_MAX_OUTSTANDING_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.IPV6_AUTOCONFIGURATION_DISCONNECT_MAX_OUTSTANDING_CMD : range})

    def interface_config_ipv6_autoconfiguration_disconnect_rate(self, range):
        """
        This is the method the command: interface_config option ipv6_autoconfiguration_disconnect_rate
        Description:Specifies the rate in attempts/second at which attempts are made to disconnect sessions. When using IxNetwork this parameter can take values from the 1-1000 range.
        Constants Available: IPV6_AUTOCONFIGURATION_DISCONNECT_RATE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.IPV6_AUTOCONFIGURATION_DISCONNECT_RATE_CMD : range})

    def interface_config_ipv6_autoconfiguration_disconnect_scale_mode(self, opt):
        """
        This is the method the command: interface_config option ipv6_autoconfiguration_disconnect_scale_mode
        Description:Indicates whether the control is specified per port or per device group. This setting is global for all the IPv6 Autoconfiguration protocols configured in the ixncfg and can be configured just when handle is /globals meaning that the user wants to configure only global protocol settings.
            Valid options are:
            port
            device_group
        Constants Available: IPV6_AUTOCONFIGURATION_DISCONNECT_SCALE_MODE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.IPV6_AUTOCONFIGURATION_DISCONNECT_SCALE_MODE_CMD : opt})

    def interface_config_ipv6_autoconfiguration_send_ns_enabled(self, bool_opt):
        """
        This is the method the command: interface_config option ipv6_autoconfiguration_send_ns_enabled
        Constants Available: IPV6_AUTOCONFIGURATION_SEND_NS_ENABLED_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.IPV6_AUTOCONFIGURATION_SEND_NS_ENABLED_CMD : bool_opt})

    def interface_config_ipv6_autoconfiguration_send_ns_max_outstanding(self, range):
        """
        This is the method the command: interface_config option ipv6_autoconfiguration_send_ns_max_outstanding
        Description:The maximum number of triggered instances of an action that is still awaiting a response or completion
        Constants Available: IPV6_AUTOCONFIGURATION_SEND_NS_MAX_OUTSTANDING_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.IPV6_AUTOCONFIGURATION_SEND_NS_MAX_OUTSTANDING_CMD : range})

    def interface_config_ipv6_autoconfiguration_send_ns_rate(self, range):
        """
        This is the method the command: interface_config option ipv6_autoconfiguration_send_ns_rate
        Description:Specifies the rate in attempts/second at which attempts are made to send NS requests on sessions. When using IxNetwork this parameter can take values from the 1-1000 range.
        Constants Available: IPV6_AUTOCONFIGURATION_SEND_NS_RATE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.IPV6_AUTOCONFIGURATION_SEND_NS_RATE_CMD : range})

    def interface_config_ipv6_autoconfiguration_send_ns_scale_mode(self, opt):
        """
        This is the method the command: interface_config option ipv6_autoconfiguration_send_ns_scale_mode
        Description:Indicates whether the control is specified per port or per device group. This setting is global for all the IPv6 Autoconfiguration protocols configured in the ixncfg and can be configured just when handle is /globals meaning that the user wants to configure only global protocol settings.
            Valid options are:
            port
            device_group
        Constants Available: IPV6_AUTOCONFIGURATION_SEND_NS_SCALE_MODE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.IPV6_AUTOCONFIGURATION_SEND_NS_SCALE_MODE_CMD : opt})

    def interface_config_ipv6_autoconfiguration_send_rs_enabled(self, bool_opt):
        """
        This is the method the command: interface_config option ipv6_autoconfiguration_send_rs_enabled
        Constants Available: IPV6_AUTOCONFIGURATION_SEND_RS_ENABLED_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.IPV6_AUTOCONFIGURATION_SEND_RS_ENABLED_CMD : bool_opt})

    def interface_config_ipv6_autoconfiguration_send_rs_interval(self, numeric):
        """
        This is the method the command: interface_config option ipv6_autoconfiguration_send_rs_interval
        Description:Time interval used to calculate the rate for triggering an action(rate = count/interval)
        Constants Available: IPV6_AUTOCONFIGURATION_SEND_RS_INTERVAL_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.IPV6_AUTOCONFIGURATION_SEND_RS_INTERVAL_CMD : numeric})

    def interface_config_ipv6_autoconfiguration_send_rs_max_outstanding(self, range):
        """
        This is the method the command: interface_config option ipv6_autoconfiguration_send_rs_max_outstanding
        Description:The maximum number of triggered instances of an action that is still awaiting a response or completion
        Constants Available: IPV6_AUTOCONFIGURATION_SEND_RS_MAX_OUTSTANDING_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.IPV6_AUTOCONFIGURATION_SEND_RS_MAX_OUTSTANDING_CMD : range})

    def interface_config_ipv6_autoconfiguration_send_rs_rate(self, range):
        """
        This is the method the command: interface_config option ipv6_autoconfiguration_send_rs_rate
        Description:Specifies the rate in attempts/second at which attempts are made to send RS requests on sessions. When using IxNetwork this parameter can take values from the 1-1000 range.
        Constants Available: IPV6_AUTOCONFIGURATION_SEND_RS_RATE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.IPV6_AUTOCONFIGURATION_SEND_RS_RATE_CMD : range})

    def interface_config_ipv6_autoconfiguration_send_rs_scale_mode(self, opt):
        """
        This is the method the command: interface_config option ipv6_autoconfiguration_send_rs_scale_mode
        Description:Indicates whether the control is specified per port or per device group. This setting is global for all the IPv6 Autoconfiguration protocols configured in the ixncfg and can be configured just when handle is /globals meaning that the user wants to configure only global protocol settings.
            Valid options are:
            port
            device_group
        Constants Available: IPV6_AUTOCONFIGURATION_SEND_RS_SCALE_MODE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.IPV6_AUTOCONFIGURATION_SEND_RS_SCALE_MODE_CMD : opt})

    def interface_config_ipv6_diconnect_enabled(self, bool_opt):
        """
        This is the method the command: interface_config option ipv6_diconnect_enabled
        Constants Available: IPV6_DICONNECT_ENABLED_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.IPV6_DICONNECT_ENABLED_CMD : bool_opt})

    def interface_config_ipv6_disconnect_interval(self, numeric):
        """
        This is the method the command: interface_config option ipv6_disconnect_interval
        Description:Time interval used to calculate the rate for triggering an action(rate = count/interval)
        Constants Available: IPV6_DISCONNECT_INTERVAL_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.IPV6_DISCONNECT_INTERVAL_CMD : numeric})

    def interface_config_ipv6_disconnect_rate(self, range):
        """
        This is the method the command: interface_config option ipv6_disconnect_rate
        Description:Specifies the rate in attempts/second at which attempts are made to disconnect sessions. When using IxNetwork this parameter can take values from the 1-1000 range.
        Constants Available: IPV6_DISCONNECT_RATE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.IPV6_DISCONNECT_RATE_CMD : range})

    def interface_config_ipv6_disconnect_scale_mode(self, opt):
        """
        This is the method the command: interface_config option ipv6_disconnect_scale_mode
        Description:Indicates whether the control is specified per port or per device group. This setting is global for all the IPv6 protocols configured in the ixncfg and can be configured just when handle is /globals meaning that the user wants to configure only global protocol settings.
            Valid options are:
            port
            device_group
        Constants Available: IPV6_DISCONNECT_SCALE_MODE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.IPV6_DISCONNECT_SCALE_MODE_CMD : opt})

    def interface_config_ipv6_gateway_step(self, ipv6):
        """
        This is the method the command: interface_config option ipv6_gateway_step
        Description:The incrementing step for the IPv6 gateway of the interface, when connected_count is greater than 1. This option takes a list of values when -port_handle is a list of port handles.
        Constants Available: IPV6_GATEWAY_STEP_CMD
        Supported:IxOS/IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        ipv6 --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.IPV6_GATEWAY_STEP_CMD : ipv6})

    def interface_config_ipv6_intf_addr_step(self, ipv6):
        """
        This is the method the command: interface_config option ipv6_intf_addr_step
        Description:The incrementing step for the IPv6 address of the interface, when connected_count is greater than 1. This option takes a list of values when -port_handle is a list of port handles.This option is valid only when l23_config_type is static_endpoint (new API).
            DEFAULT: 0::1
        Constants Available: IPV6_INTF_ADDR_STEP_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        ipv6 --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.IPV6_INTF_ADDR_STEP_CMD : ipv6})

    def interface_config_ipv6_loopback_multiplier(self, numeric):
        """
        This is the method the command: interface_config option ipv6_loopback_multiplier
        Description:This is the multiplier for the IPv6 loopback stack as its used in the custom ratios.
        Constants Available: IPV6_LOOPBACK_MULTIPLIER_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.IPV6_LOOPBACK_MULTIPLIER_CMD : numeric})

    def interface_config_ipv6_manual_gateway_mac(self, mac):
        """
        This is the method the command: interface_config option ipv6_manual_gateway_mac
        Description:The manual gateway MAC addresses. This option has no effect unless ipv6_resolve_gateway is set to 0.
            DEPENDENCIES: Valid in combination with parameter(s)
            'ipv6_resolve_gateway' | value= '0' |
        Constants Available: IPV6_MANUAL_GATEWAY_MAC_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        mac --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.IPV6_MANUAL_GATEWAY_MAC_CMD : mac})

    def interface_config_ipv6_manual_gateway_mac_step(self, mac):
        """
        This is the method the command: interface_config option ipv6_manual_gateway_mac_step
        Description:The step of the manual gateway MAC addresses. This option has no effect unless ipv6_resolve_gateway is set to 0.
            DEFAULT: 0000.0000.0001
            DEPENDENCIES: Valid in combination with parameter(s)
            'ipv6_resolve_gateway' | value= '0' |
        Constants Available: IPV6_MANUAL_GATEWAY_MAC_STEP_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        mac --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.IPV6_MANUAL_GATEWAY_MAC_STEP_CMD : mac})

    def interface_config_ipv6_multiplier(self, numeric):
        """
        This is the method the command: interface_config option ipv6_multiplier
        Description:This is the multiplier for the IPv6 stack as its used in the custom ratios.
        Constants Available: IPV6_MULTIPLIER_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.IPV6_MULTIPLIER_CMD : numeric})

    def interface_config_ipv6_re_send_ns_on_link_up(self, opt):
        """
        This is the method the command: interface_config option ipv6_re_send_ns_on_link_up
        Description:Resends neighbor solicitation after link up.
        Constants Available: IPV6_RE_SEND_NS_ON_LINK_UP_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.IPV6_RE_SEND_NS_ON_LINK_UP_CMD : opt})

    def interface_config_ipv6_resolve_gateway(self, bool_opt):
        """
        This is the method the command: interface_config option ipv6_resolve_gateway
        Description:Autoresolve gateway MAC addresses.
        Constants Available: IPV6_RESOLVE_GATEWAY_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.IPV6_RESOLVE_GATEWAY_CMD : bool_opt})

    def interface_config_ipv6_send_ns_interval(self, numeric):
        """
        This is the method the command: interface_config option ipv6_send_ns_interval
        Description:Time interval used to calculate the rate for triggering an action(rate = count/interval)
        Constants Available: IPV6_SEND_NS_INTERVAL_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.IPV6_SEND_NS_INTERVAL_CMD : numeric})

    def interface_config_ipv6_send_ns_max_outstanding(self, range):
        """
        This is the method the command: interface_config option ipv6_send_ns_max_outstanding
        Description:The maximum number of triggered instances of an action that is still awaiting a response or completion
        Constants Available: IPV6_SEND_NS_MAX_OUTSTANDING_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.IPV6_SEND_NS_MAX_OUTSTANDING_CMD : range})

    def interface_config_ipv6_send_ns_rate(self, range):
        """
        This is the method the command: interface_config option ipv6_send_ns_rate
        Description:Specifies the rate in attempts/second at which attempts are made to send NS requests on sessions. When using IxNetwork this parameter can take values from the 1-1000 range.
        Constants Available: IPV6_SEND_NS_RATE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.IPV6_SEND_NS_RATE_CMD : range})

    def interface_config_ipv6_send_ns_scale_mode(self, opt):
        """
        This is the method the command: interface_config option ipv6_send_ns_scale_mode
        Description:Indicates whether the control is specified per port or per device group. This setting is global for all the IPv6 protocols configured in the ixncfg and can be configured just when handle is /globals meaning that the user wants to configure only global protocol settings.
            Valid options are:
            port
            device_group
        Constants Available: IPV6_SEND_NS_SCALE_MODE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.IPV6_SEND_NS_SCALE_MODE_CMD : opt})

    def interface_config_l23_config_type(self, opt):
        """
        This is the method the command: interface_config option l23_config_type
        Description:The type of IP interface that will be configured. protocol_interface (default) - the interface will be configured in the Routing/Switching/Interfaces section (valid for IxTclProtocol and IxTclNetwork)static_endpoint - the interface will be configured as an IP endpoint in the Auth/Access Hosts/DCB section (valid only for IxTclNetwork)
            The type of IP interface that will be configured. This argument is only supported for legacy compatibility with the ixia namespace.
            Valid options are:
            protocol_interface: (default) - the interface will be configured in the Routing/Switching/Interfaces section
            static_endpoint:the interface will be configured as an IP endpoint in the Auth/Access Hosts/DCB section
            DEFAULT: protocol_interface
        Constants Available: L23_CONFIG_TYPE_CMD
        Supported:IxOS/IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.L23_CONFIG_TYPE_CMD : opt})

    def interface_config_laser_on(self, bool_opt):
        """
        This is the method the command: interface_config option laser_on
        Description:Enable 'laser on' option for Multis cards.
            This option is valid when intf_mode is multis and only for IxNetwork new api.
        Constants Available: LASER_ON_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.LASER_ON_CMD : bool_opt})

    def interface_config_link_training(self, bool_opt):
        """
        This is the method the command: interface_config option link_training
        Description:Link training
        Constants Available: LINK_TRAINING_CMD
        Supported:IxNetwork-FT
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.LINK_TRAINING_CMD : bool_opt})

    def interface_config_loop_continuously(self, bool_opt):
        """
        This is the method the command: interface_config option loop_continuously
        Description:L1 config parameter that enables continuous looping. Valid only for Multis cards.
        Constants Available: LOOP_CONTINUOUSLY_CMD
        Supported:IxOS/IxNetwork-FT
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.LOOP_CONTINUOUSLY_CMD : bool_opt})

    def interface_config_loop_count_number(self, numeric):
        """
        This is the method the command: interface_config option loop_count_number
        Description:L1 config parameter that counts the number of times the series will loop. Valid only for Multis cards.
        Constants Available: LOOP_COUNT_NUMBER_CMD
        Supported:IxOS/IxNetwork-FT
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.LOOP_COUNT_NUMBER_CMD : numeric})

    def interface_config_master_slave_mode(self, opt):
        """
        This is the method the command: interface_config option master_slave_mode
        Description:Valid only for IxNetwork for interfaces that support media-independent master/slave negotiation. Valid options are: auto master slave
        Constants Available: MASTER_SLAVE_MODE_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.MASTER_SLAVE_MODE_CMD : opt})

    def interface_config_mss(self, range):
        """
        This is the method the command: interface_config option mss
        Description:The Maximum Segment Size. The MSS is the largest amount of data, specified in bytes, that the IP device can transmit as a single, unfragmented unit. The TCP MSS equals the MTU minus the TCP header size, minus the IP header size. Stack Manager supports jumbo frames. Therefore the maximum value is 9460. This option is valid only when l23_config_type is static_endpoint (new API). This option takes a list of values when -port_handle is a list of port handles.
            DEFAULT: 1460
        Constants Available: MSS_CMD
        Supported:IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.MSS_CMD : range})

    def interface_config_mtu(self, range):
        """
        This is the method the command: interface_config option mtu
        Description:This option configure Maximum Trasmision Unit for created interfaces. This parameter can be an interfaces - one MTU value for each interface to be created. This option takes a list of values when -port_handle is a list of port handles. This is valid for the old and new APIs.
        Constants Available: MTU_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.MTU_CMD : range})

    def interface_config_ndp_send_req(self, bool_opt):
        """
        This is the method the command: interface_config option ndp_send_req
        Description:See -send_router_solicitation parameter.If both -ndp_send_req and -send_router_solicitation are present, -ndp_send_req takes precedence.
        Constants Available: NDP_SEND_REQ_CMD
        Supported:IxOS/IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.NDP_SEND_REQ_CMD : bool_opt})

    def interface_config_no_write(self, flag):
        """
        This is the method the command: interface_config option no_write
        Description:If this option is present, the configuration is not written to the hardware. This option can be used to queue up multiple configurations before writing to the hardware.This is valid for the old API (IxTclProtocol).
        Constants Available: NO_WRITE_CMD
        Supported:IxOS/IxNetwork-NGPF
        Keyword arguments:
        flag --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.NO_WRITE_CMD : flag})

    def interface_config_notify_mac_move(self, bool_opt):
        """
        This is the method the command: interface_config option notify_mac_move
        Description:Flag to determine if MAC move notifications should be sent
        Constants Available: NOTIFY_MAC_MOVE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.NOTIFY_MAC_MOVE_CMD : bool_opt})

    def interface_config_ns_on_linkup(self, bool_opt):
        """
        This is the method the command: interface_config option ns_on_linkup
        Description:Send Neighbor Solicitation for the IPv6 interfaces when the port link becomes up. The option is global, for all ports and interfaces. This is valid only for the new API.
        Constants Available: NS_ON_LINKUP_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.NS_ON_LINKUP_CMD : bool_opt})

    def interface_config_override_existence_check(self, bool_opt):
        """
        This is the method the command: interface_config option override_existence_check
        Description:If this option is enabled, the interface existence check is skipped but the list of interfaces is still created and maintained in order to keep track of existing interfaces if required. Using this option will speed up the interfaces' creation. Valid only for -l23_config_type protocol_interface.
        Constants Available: OVERRIDE_EXISTENCE_CHECK_CMD
        Supported:IxOS/IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.OVERRIDE_EXISTENCE_CHECK_CMD : bool_opt})

    def interface_config_override_tracking(self, bool_opt):
        """
        This is the method the command: interface_config option override_tracking
        Description:If this option is enabled, the list of interfaces won't be created and maintained anymore, thus, speeding up the interfaces' creation even more. Also, it will enable -override_existence_check in case it wasn't already enabled because checking for interface existence becomes impossible if the the list of interfaces doesn't exist anymore. Valid only for -l23_config_type protocol_interface.
        Constants Available: OVERRIDE_TRACKING_CMD
        Supported:IxOS/IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.OVERRIDE_TRACKING_CMD : bool_opt})

    def interface_config_pcs_count(self, numeric):
        """
        This is the method the command: interface_config option pcs_count
        Description:Consecutive errors to transmit.
        Constants Available: PCS_COUNT_CMD
        Supported:IxOS/IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.PCS_COUNT_CMD : numeric})

    def interface_config_pcs_enabled_continuous(self, bool_opt):
        """
        This is the method the command: interface_config option pcs_enabled_continuous
        Description:If set to true, will transmit errors continuously at the given period and count. If false, see repeat, below. Valid choices are: 0 - false 1 - true
        Constants Available: PCS_ENABLED_CONTINUOUS_CMD
        Supported:IxOS/IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.PCS_ENABLED_CONTINUOUS_CMD : bool_opt})

    def interface_config_pcs_lane(self, numeric):
        """
        This is the method the command: interface_config option pcs_lane
        Description:Specifies which lane to insert errors into. This parameter is valid only with IxTclHal api. Valid values range:0 - 19 for 100G load modules;0 - 3 for 40G load modules.
        Constants Available: PCS_LANE_CMD
        Supported:IxOS/IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.PCS_LANE_CMD : numeric})

    def interface_config_pcs_marker_fields(self, opt):
        """
        This is the method the command: interface_config option pcs_marker_fields
        Description:Hex field for entering the lane marker fields. Valid formats are: 00.00.00.00.00.00.00.02 , 00:00:00:00:00:00:00:02
        Constants Available: PCS_MARKER_FIELDS_CMD
        Supported:IxOS/IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.PCS_MARKER_FIELDS_CMD : opt})

    def interface_config_pcs_period(self, numeric):
        """
        This is the method the command: interface_config option pcs_period
        Description:Periodicity of transmitted errors. The unit of period differs based on the type of error (pcs_period_type) selected. This parameter is valid only with IxTclHal api.Type = lane markers, period = lane markersType = lane markers and payload, period = 64/66 bit words
        Constants Available: PCS_PERIOD_CMD
        Supported:IxOS/IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.PCS_PERIOD_CMD : numeric})

    def interface_config_pcs_period_type(self, numeric):
        """
        This is the method the command: interface_config option pcs_period_type
        Description:Use to configure the PCS Error Period Type. This parameter is valid only with IxTclHal api. Valid values are:0 - pcsLaneErrorPeriodTypeLaneMarkers - Lane Markers period type (only)1 - pcsLaneErrorPeriodTypeLaneMarkersAndPayload - both Lane Markers and Payload period types
        Constants Available: PCS_PERIOD_TYPE_CMD
        Supported:IxOS/IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.PCS_PERIOD_TYPE_CMD : numeric})

    def interface_config_pcs_repeat(self, numeric):
        """
        This is the method the command: interface_config option pcs_repeat
        Description:Total number of errors to transmit. This is value ignored if pcs_enabled_continuous is set to 1 (true).This parameter is valid only with IxTclHal api.
        Constants Available: PCS_REPEAT_CMD
        Supported:IxOS/IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.PCS_REPEAT_CMD : numeric})

    def interface_config_pcs_sync_bits(self, opt):
        """
        This is the method the command: interface_config option pcs_sync_bits
        Description:Hex field for entering the error bits for the sync field.
        Constants Available: PCS_SYNC_BITS_CMD
        Supported:IxOS/IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.PCS_SYNC_BITS_CMD : opt})

    def interface_config_pgid_128k_bin_enable(self, bool_opt):
        """
        This is the method the command: interface_config option pgid_128k_bin_enable
        Description:Enables the 128k bin mode so that the wide packet group receive mode will be larger. This option takes a list of values when -port_handle is a list of port handles.
        Constants Available: PGID_128K_BIN_ENABLE_CMD
        Supported:IxOS/IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.PGID_128K_BIN_ENABLE_CMD : bool_opt})

    def interface_config_pgid_encap(self, opt):
        """
        This is the method the command: interface_config option pgid_encap
        Description:Available only with IxNetwork TCL API. When -pgid_mode is configured to 'ipv6TC', 'dscp', 'mplsExp', 'tos_precedence', 'ipv6TC_bits_0_2' or 'ipv6TC_bits_0_2' and the port is ATM, this option configures the encapsulation used for egress tracking. Valid options are:LLCRoutedCLIP - defaultLLCPPPoALLCBridgedEthernetFCSLLCBridgedEthernetNoFCSVccMuxPPPoAVccMuxIPV4RoutedVccMuxBridgedEthernetFCSVccMuxBridgedEthernetNoFCS
        Constants Available: PGID_ENCAP_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.PGID_ENCAP_CMD : opt})

    def interface_config_pgid_mask(self, opt):
        """
        This is the method the command: interface_config option pgid_mask
        Description:The mask value to use when the -port_rx_mode is set to wide_packet_group. Value is by default a two byte value, in hex form, without any spaces (e.g., AAAA). This option takes a list of values when -port_handle is a list of port handles.
        Constants Available: PGID_MASK_CMD
        Supported:IxOS/IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.PGID_MASK_CMD : opt})

    def interface_config_pgid_mode(self, opt):
        """
        This is the method the command: interface_config option pgid_mode
        Description:This option can be used to specify the PGID mode in the filter section, on specified RX port. This option takes a list of values when -port_handle is a list of port handles. The predifined split pgid offsets used for egress tracking with IxNetwork TCL API are fixed. They do not adjust if the offsets monitored in the received packets are shifted.
            Valid options are:
            custom: this option is not available with IxNetwork TclAPI
            dscp: When IxNetwork Tcl API is used, this option enables egress tracking on this port using split pgids. The egress tracking offset will configured to the predefined IPv4 DSCP (6 bits) offset.
            ipv6TCWhen IxNetwork Tcl API is used, this option enables egress tracking on this port using split pgids. The egress tracking offset will configured to the predifined IPv6 Traffic Class (8 bits) offset.
            mplsExp: When IxNetwork Tcl API is used, this option enables egress tracking on this port using split pgids. The egress tracking offset will configured to the predifined MPLS Exp (3 bits) offset.
            split: When IxNetwork Tcl API is used, this option enables egress tracking on this port using split pgids. The egress tracking offset and width will be configured manually with the parameters -pgid_split1_offset and pgid_split1_width.
            outer_vlan_priority: Available only with IxNetwork TCL API, this option enables egress tracking on this port using split pgids. The egress tracking offset will configured to the predifined Outer VLAN Priority (3 bits) offset. This choice is supported only on Ethernet, 10 gig lan and 10 gig wan cards.
            outer_vlan_id_4: Available only with IxNetwork TCL API, this option enables egress tracking on this port using split pgids. The egress tracking offset will configured to the predifined Outer VLAN ID (4 bits) offset. This choice is supported only on Ethernet, 10 gig lan and 10 gig wan cards.
            outer_vlan_id_6: Available only with IxNetwork TCL API, this option enables egress tracking on this port using split pgids. The egress tracking offset will configured to the predifined Outer VLAN ID (6 bits) offset. This choice is supported only on Ethernet, 10 gig lan and 10 gig wan cards.
            outer_vlan_id_8: Available only with IxNetwork TCL API, this option enables egress tracking on this port using split pgids. The egress tracking offset will configured to the predifined Outer VLAN ID (8 bits) offset. This choice is supported only on Ethernet, 10 gig lan and 10 gig wan cards.
            outer_vlan_id_10: Available only with IxNetwork TCL API, this option enables egress tracking on this port using split pgids. The egress tracking offset will configured to the predifined Outer VLAN ID (10 bits) offset. This choice is supported only on Ethernet, 10 gig lan and 10 gig wan cards.
            outer_vlan_id_12: Available only with IxNetwork TCL API, this option enables egress tracking on this port using split pgids. The egress tracking offset will configured to the predifined Outer VLAN ID (12 bits) offset. This choice is supported only on Ethernet, 10 gig lan and 10 gig wan cards.
            inner_vlan_priority: Available only with IxNetwork TCL API, this option enables egress tracking on this port using split pgids. The egress tracking offset will configured to the predifined Inner VLAN Priority (3 bits) offset. This choice is supported only on Ethernet, 10 gig lan and 10 gig wan cards.
            inner_vlan_id_4: Available only with IxNetwork TCL API, this option enables egress tracking on this port using split pgids. The egress tracking offset will configured to the predifined Inner VLAN ID (4 bits) offset. This choice is supported only on Ethernet, 10 gig lan and 10 gig wan cards.
            inner_vlan_id_6: Available only with IxNetwork TCL API, this option enables egress tracking on this port using split pgids. The egress tracking offset will configured to the predifined Inner VLAN ID (6 bits) offset. This choice is supported only on Ethernet, 10 gig lan and 10 gig wan cards.
            inner_vlan_id_8: Available only with IxNetwork TCL API, this option enables egress tracking on this port using split pgids. The egress tracking offset will configured to the predifined Inner VLAN ID (8 bits) offset. This choice is supported only on Ethernet, 10 gig lan and 10 gig wan cards.
            inner_vlan_id_10: Available only with IxNetwork TCL API, this option enables egress tracking on this port using split pgids. The egress tracking offset will configured to the predifined Inner VLAN ID (10 bits) offset. This choice is supported only on Ethernet, 10 gig lan and 10 gig wan cards.
            inner_vlan_id_12: Available only with IxNetwork TCL API, this option enables egress tracking on this port using split pgids. The egress tracking offset will configured to the predifined Inner VLAN ID (12 bits) offset. This choice is supported only on Ethernet, 10 gig lan and 10 gig wan cards.
            tos_precedence: Available only with IxNetwork TCL API, this option enables egress tracking on this port using split pgids. The egress tracking offset will configured to the predifined IPv4 TOS Precedence (3 bits) offset.
            ipv6TC_bits_0_2: Available only with IxNetwork TCL API, this option enables egress tracking on this port using split pgids. The egress tracking offset will configured to the predifined IPv6 Traffic Class Bits 0-2 (3 bits) offset.
            ipv6TC_bits_0_5: Available only with IxNetwork TCL API, this option enables egress tracking on this port using split pgids. The egress tracking offset will configured to the predifined IPv6 Traffic Class Bits 0-5 (6 bits) offset.
        Constants Available: PGID_MODE_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.PGID_MODE_CMD : opt})

    def interface_config_pgid_offset(self, range):
        """
        This is the method the command: interface_config option pgid_offset
        Description:The group ID offset value. If -port_rx_mode is set to auto_detect_instrumentation then this offset will be ignored, only the pgid value is needed. This option takes a list of values when -port_handle is a list of port handles.
        Constants Available: PGID_OFFSET_CMD
        Supported:IxOS/IxNetwork-NGPF
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.PGID_OFFSET_CMD : range})

    def interface_config_pgid_split1_mask(self, opt):
        """
        This is the method the command: interface_config option pgid_split1_mask
        Description:The PGID mask bits for the first split PGID. It is a hexadecimal value in the 0x format. This option is available only for traffic_generator ixos. This option has any meaning only if the -pgid_mode option is set to split. This option takes a list of values when -port_handle is a list of port handles.
        Constants Available: PGID_SPLIT1_MASK_CMD
        Supported:IxOS/IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.PGID_SPLIT1_MASK_CMD : opt})

    def interface_config_pgid_split1_offset(self, numeric):
        """
        This is the method the command: interface_config option pgid_split1_offset
        Description:The offset in bytes from pgid_split1_offset_from. This option has any meaning only if the -pgid_mode option is set to split. This option takes a list of values when -port_handle is a list of port handles.
        Constants Available: PGID_SPLIT1_OFFSET_CMD
        Supported:IxOS/IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.PGID_SPLIT1_OFFSET_CMD : numeric})

    def interface_config_pgid_split1_offset_from(self, opt):
        """
        This is the method the command: interface_config option pgid_split1_offset_from
        Description:The frame location from which the pgid_split1_offset value is computed. This option is available only for traffic_generator ixos. This option has any meaning only if the -pgid_mode option is set to split. This option takes a list of values when -port_handle is a list of port handles.
        Constants Available: PGID_SPLIT1_OFFSET_FROM_CMD
        Supported:IxOS/IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.PGID_SPLIT1_OFFSET_FROM_CMD : opt})

    def interface_config_pgid_split1_width(self, range):
        """
        This is the method the command: interface_config option pgid_split1_width
        Description:The width, in bytes/bits, of the split PGID for IxOs/IxNetwork. This option has any meaning only if the -pgid_mode option is set to split. This option takes a list of values when -port_handle is a list of port handles. For IxOS the range accepted is 0-4 bytes. When IxNetwork TclAPI is used the range accepted is 0-12 bits.
        Constants Available: PGID_SPLIT1_WIDTH_CMD
        Supported:IxOS/IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.PGID_SPLIT1_WIDTH_CMD : range})

    def interface_config_pgid_split2_mask(self, opt):
        """
        This is the method the command: interface_config option pgid_split2_mask
        Description:The PGID mask bits for the second split PGID. It is a hexadecimal value in the 0x format. This option is available only for traffic_generator ixos. This option has any meaning only if the -pgid_mode option is set to split. This option takes a list of values when -port_handle is a list of port handles.
        Constants Available: PGID_SPLIT2_MASK_CMD
        Supported:IxOS/IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.PGID_SPLIT2_MASK_CMD : opt})

    def interface_config_pgid_split2_offset(self, numeric):
        """
        This is the method the command: interface_config option pgid_split2_offset
        Description:The offset in bytes from pgid_split2_offset_from. This option is available only for traffic_generator ixos. This option has any meaning only if the -pgid_mode option is set to split. This option takes a list of values when -port_handle is a list of port handles.
        Constants Available: PGID_SPLIT2_OFFSET_CMD
        Supported:IxOS/IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.PGID_SPLIT2_OFFSET_CMD : numeric})

    def interface_config_pgid_split2_offset_from(self, opt):
        """
        This is the method the command: interface_config option pgid_split2_offset_from
        Description:The frame location from which the pgid_split2_offset value is computed. This option is available only for traffic_generator ixos. This option has any meaning only if the -pgid_mode option is set to split. This option takes a list of values when -port_handle is a list of port handles
        Constants Available: PGID_SPLIT2_OFFSET_FROM_CMD
        Supported:IxOS/IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.PGID_SPLIT2_OFFSET_FROM_CMD : opt})

    def interface_config_pgid_split2_width(self, range):
        """
        This is the method the command: interface_config option pgid_split2_width
        Description:The width, in bytes, of the split PGID. This option is available only for traffic_generator ixos. This option has any meaning only if the -pgid_mode option is set to split.
        Constants Available: PGID_SPLIT2_WIDTH_CMD
        Supported:IxOS/IxNetwork-NGPF
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.PGID_SPLIT2_WIDTH_CMD : range})

    def interface_config_pgid_split3_mask(self, opt):
        """
        This is the method the command: interface_config option pgid_split3_mask
        Description:The PGID mask bits for the third split PGID. It is a hexadecimal value in the 0x format. This option is available only for traffic_generator ixos. This option has any meaning only if the -pgid_mode option is set to split. This option takes a list of values when -port_handle is a list of port handles.
        Constants Available: PGID_SPLIT3_MASK_CMD
        Supported:IxOS/IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.PGID_SPLIT3_MASK_CMD : opt})

    def interface_config_pgid_split3_offset(self, numeric):
        """
        This is the method the command: interface_config option pgid_split3_offset
        Description:The offset in bytes from pgid_split_offsetX_from. This option is available only for traffic_generator ixos. This option has any meaning only if the -pgid_mode option is set to split. This option takes a list of values when -port_handle is a list of port handles.
        Constants Available: PGID_SPLIT3_OFFSET_CMD
        Supported:IxOS/IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.PGID_SPLIT3_OFFSET_CMD : numeric})

    def interface_config_pgid_split3_offset_from(self, opt):
        """
        This is the method the command: interface_config option pgid_split3_offset_from
        Description:The frame location from which the pgid_split3_offset value is computed. This option is available only for traffic_generator ixos. This option has any meaning only if the -pgid_mode option is set to split. This option takes a list of values when -port_handle is a list of port handles.
        Constants Available: PGID_SPLIT3_OFFSET_FROM_CMD
        Supported:IxOS/IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.PGID_SPLIT3_OFFSET_FROM_CMD : opt})

    def interface_config_pgid_split3_width(self, range):
        """
        This is the method the command: interface_config option pgid_split3_width
        Description:The width, in bytes, of the split PGID. This option is available only for traffic_generator ixos. This option has any meaning only if the -pgid_mode option is set to split. This option takes a list of values when -port_handle is a list of port handles.
        Constants Available: PGID_SPLIT3_WIDTH_CMD
        Supported:IxOS/IxNetwork-NGPF
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.PGID_SPLIT3_WIDTH_CMD : range})

    def interface_config_ping_dst(self, opt):
        """
        This is the method the command: interface_config option ping_dst
        Description:Specifies what destination to ping.
        Constants Available: PING_DST_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.PING_DST_CMD : opt})

    def interface_config_port_rx_mode(self, opt):
        """
        This is the method the command: interface_config option port_rx_mode
        Description:Configure the Receive Engine of the Ixia port. This option takes a list of values when -port_handle is a list of capture - Capture packets. This is valid for the old and new API (IxTclProcol and IxTclNetwork).latency - Calculate latency. This is valid for the old API (IxTclProcol).data_integrity - Check data integrity. This is valid for the old API (IxTclProcol).sequence_checking - Check data sequencing. This is valid for the old API (IxTclProcol).packet_group - Compile statistics for specified packet group. PGID is 2 bytes. This is valid for the old and new API (IxTclProcol and IxTclNetwork).wide_packet_group - Compile statistics for specified packet group. PGID is 4 bytes, but only the low order 17 bits are active. This is valid for the old and new API (IxTclProcol and IxTclNetwork).auto_detect_instrumentation - Automatic instrumentation detection This option includes wide_packet_group mode also. If this option is set then, for PGID, data integrity checking and sequence checking there will be no need for specifying signature offset, only signature value will be provided. This is valid for old and new API (IxTclProcol and IxTclNetwork).echo - Gigabit echo mode. This is valid for the old API (IxTclProcol).capture_and_measure - This is valid only for new API (IxTclNetwork).
            Configure the Receive Engine of the Ixia port. This option takes a list of values when -port_handle is a list of port handles.
            Valid options are:
            capture: Capture packets.
            packet_group: Compile statistics for specified packet group. PGID is 2 bytes.
            data_integrity: Check data integrity.
            sequence_checking: Check data sequencing.
            wide_packet_group: Compile statistics for specified packet group. PGID is 4 bytes,but only the low order 17 bits are active.
            echo: Gigabit echo mode.
            auto_detect_instrumentation: Automatic instrumentation detection. This option includes wide_packet_group mode also. If this option is set then, for PGID, data integrity checking and sequence checking there will be no need for specifying signature offset, only signature value will be provided.
            capture_and_measure: This is valid only for new API (IxTclNetwork)
        Constants Available: PORT_RX_MODE_CMD
        Supported:IxOS/IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.PORT_RX_MODE_CMD : opt})

    def interface_config_ppp_ipv4_address(self, ip):
        """
        This is the method the command: interface_config option ppp_ipv4_address
        Description:IPv4 address for which to enable or disable PPP IPv4 negotiation. This option takes a list of values when -port_handle is a list of port handles.This is valid for the old and new API.
        Constants Available: PPP_IPV4_ADDRESS_CMD
        Supported:IxOS/IxNetwork-NGPF
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.PPP_IPV4_ADDRESS_CMD : ip})

    def interface_config_ppp_ipv4_negotiation(self, bool_opt):
        """
        This is the method the command: interface_config option ppp_ipv4_negotiation
        Description:Whether to enable PPP IPv4 negotiation on this port. This option takes a list of values when -port_handle is a list of port handles. Valid options are: 0 - Disable 1 - (default) Enable
        Constants Available: PPP_IPV4_NEGOTIATION_CMD
        Supported:IxOS/IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.PPP_IPV4_NEGOTIATION_CMD : bool_opt})

    def interface_config_ppp_ipv6_negotiation(self, bool_opt):
        """
        This is the method the command: interface_config option ppp_ipv6_negotiation
        Description:Whether to enable PPP IPv6 negotiation on this port. This option takes a list of values when -port_handle is a list of port handles. Valid options are: 0 - Disable 1 - (default) Enable
        Constants Available: PPP_IPV6_NEGOTIATION_CMD
        Supported:IxOS/IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.PPP_IPV6_NEGOTIATION_CMD : bool_opt})

    def interface_config_ppp_mpls_negotiation(self, bool_opt):
        """
        This is the method the command: interface_config option ppp_mpls_negotiation
        Description:Whether to enable PPP MPLS negotiation on this port. Valid options are: 0 - Disable 1 - (default) Enable
        Constants Available: PPP_MPLS_NEGOTIATION_CMD
        Supported:IxOS/IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.PPP_MPLS_NEGOTIATION_CMD : bool_opt})

    def interface_config_ppp_osi_negotiation(self, opt):
        """
        This is the method the command: interface_config option ppp_osi_negotiation
        Description:Whether to enable OSI Network Control protocol on the Ixia PoS port. This option takes a list of values when -port_handle is a list of port handles.This is valid for the old and new API.Valid options are:0 - Disable1 - (default) Enable
        Constants Available: PPP_OSI_NEGOTIATION_CMD
        Supported:IxOS/IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.PPP_OSI_NEGOTIATION_CMD : opt})

    def interface_config_protocol_handle(self, opt):
        """
        This is the method the command: interface_config option protocol_handle
        Description:Handle for the stack that the user wants to modify or delete.
        Constants Available: PROTOCOL_HANDLE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.PROTOCOL_HANDLE_CMD : opt})

    def interface_config_protocol_name(self, name):
        """
        This is the method the command: interface_config option protocol_name
        Description:This is the name of the protocol stack as it appears in the GUI.
        Constants Available: PROTOCOL_NAME_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        name --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.PROTOCOL_NAME_CMD : name})

    def interface_config_pvc_incr_mode(self, opt):
        """
        This is the method the command: interface_config option pvc_incr_mode
        Description:The Method used to increment PVCs. This parameter is valid only vci - The VCI is incremented first. When the Unique Count (vci_count) is reached the number of times specified by the addresses_per_vpi parameter, the VPI is incremented.vpi - The VPI is incremented first. When the Unique Count (vpi_count) is reached the number of times specified by the addresses_per_vci parameter, the VCI is incremented.both (default) - Both VCI and VPI are incremented at the same time.
        Constants Available: PVC_INCR_MODE_CMD
        Supported:IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.PVC_INCR_MODE_CMD : opt})

    def interface_config_qinq_incr_mode(self, opt):
        """
        This is the method the command: interface_config option qinq_incr_mode
        Description:The Method used to increment VLAN IDs. This parameter is valid only outer - The outer VLAN ID is incremented first. When the Unique Count (vlan_id_count) is reached the number of times specified by the addresses_per_vlan parameter, the inner VLAN ID is incremented.inner - The inner VLAN ID is incremented first. When the Unique Count (vlan_id_count) is reached the number of times specified by the addresses_per_svlan parameter, the outer VLAN ID is incremented.both (default) - Both VLAN IDs are incremented at the same time.
            The Method used to increment VLAN IDs. This parameter is valid only when l23_config_type is static_endpoint (new API).
            Valid options are:
            inner: The inner VLAN ID is incremented first. When the Unique Count (vlan_id_count) is reached the number of times specified by the addresses_per_svlan parameter, the outer VLAN ID is incremented.
            outer: The outer VLAN ID is incremented first. When the Unique Count (vlan_id_count) is reached the number of times specified by the addresses_per_vlan parameter, the inner VLAN ID is incremented.
            both: Both VLAN IDs are incremented at the same time.
            DEFAULT: both
            DEPENDENCIES: Valid in combination with parameter(s)
            'l23_config_type' | value= 'static_endpoint' |
        Constants Available: QINQ_INCR_MODE_CMD
        Supported:IxOS/IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.QINQ_INCR_MODE_CMD : opt})

    def interface_config_qos_byte_offset(self, range):
        """
        This is the method the command: interface_config option qos_byte_offset
        Description:The byte offset from the beginning of the packet for the byte which contains the QoS level for the packet.
        Constants Available: QOS_BYTE_OFFSET_CMD
        Supported:IxOS/IxNetwork-NGPF
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.QOS_BYTE_OFFSET_CMD : range})

    def interface_config_qos_packet_type(self, opt):
        """
        This is the method the command: interface_config option qos_packet_type
        Description:The type of packet that the QoS counters are looking for priority bits within. Choices are: ethernet, ip_snap, vlan, custom, ip_ppp, ip_cisco_hdlc, ip_atm. This option takes a list of values when -port_handle is a list of port handles.
            Valid options are:
            ethernet
            ip_snap
            vlan
            custom
            ip_ppp
            ip_cisco_hdlc
            ip_atm
        Constants Available: QOS_PACKET_TYPE_CMD
        Supported:IxOS/IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.QOS_PACKET_TYPE_CMD : opt})

    def interface_config_qos_pattern_mask(self, opt):
        """
        This is the method the command: interface_config option qos_pattern_mask
        Description:The mask to be applied to the pattern match. Value of 1 indicate that the corresponding bit is not to be matched.
        Constants Available: QOS_PATTERN_MASK_CMD
        Supported:IxOS/IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.QOS_PATTERN_MASK_CMD : opt})

    def interface_config_qos_pattern_match(self, opt):
        """
        This is the method the command: interface_config option qos_pattern_match
        Description:The value to be matched for at the Pattern Match Offset, subject to the Pattern Match Mask. The value is in hex. This option takes a list of values when -port_handle is a list of port handles.
        Constants Available: QOS_PATTERN_MATCH_CMD
        Supported:IxOS/IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.QOS_PATTERN_MATCH_CMD : opt})

    def interface_config_qos_pattern_offset(self, range):
        """
        This is the method the command: interface_config option qos_pattern_offset
        Description:The byte offset from the beginning of the packet for the byte(s) that contains a value to be matched. If the pattern is matched, then the packet is deemed to contain a QoS level. This option takes a list of values when -port_handle is a list of port handles.
        Constants Available: QOS_PATTERN_OFFSET_CMD
        Supported:IxOS/IxNetwork-NGPF
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.QOS_PATTERN_OFFSET_CMD : range})

    def interface_config_qos_stats(self, bool_opt):
        """
        This is the method the command: interface_config option qos_stats
        Description:Whether to have access to the QOS (IP TOS PRECEDENCE) statistics on this port. This option takes a list of values when -port_handle is a list of port handles. Valid options are: 0 - Disable 1 - (default) Enable
        Constants Available: QOS_STATS_CMD
        Supported:IxOS/IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.QOS_STATS_CMD : bool_opt})

    def interface_config_router_solicitation_retries(self, range):
        """
        This is the method the command: interface_config option router_solicitation_retries
        Description:The number of times the router solicitation request will be attempted. This option takes a list of values when -port_handle is a list of port handles.
        Constants Available: ROUTER_SOLICITATION_RETRIES_CMD
        Supported:IxOS/IxNetwork-NGPF
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.ROUTER_SOLICITATION_RETRIES_CMD : range})

    def interface_config_rpr_hec_seed(self, bool_opt):
        """
        This is the method the command: interface_config option rpr_hec_seed
        Description:The initial setting of the CRC for the 16 byte header. This option is used only when intf_mode is set to rpr. This option takes a list of values when -port_handle is a list of port handles. Valid options are: 0 - (default) 0x0000 1 - 0xFFFF
        Constants Available: RPR_HEC_SEED_CMD
        Supported:IxOS/IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.RPR_HEC_SEED_CMD : bool_opt})

    def interface_config_send_ping(self, bool_opt):
        """
        This is the method the command: interface_config option send_ping
        Description:Sends ping from the specified interfaces or protocol handles to the destination specified in ping_dst. This argument will have no effect if no ping_dst is specified.
            DEFAULT: 0
            DEPENDENCIES: Valid in combination with parameter(s)
            'ping_dst' | value= '' |
        Constants Available: SEND_PING_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.SEND_PING_CMD : bool_opt})

    def interface_config_send_router_solicitation(self, bool_opt):
        """
        This is the method the command: interface_config option send_router_solicitation
        Description:If is option is present and has value 1 then interfaces on specifiedport will sent IPv6 router solicitation ICMP message to the DUT. This option takes a list of values when -port_handle is a list of port handles.
        Constants Available: SEND_ROUTER_SOLICITATION_CMD
        Supported:IxOS/IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.SEND_ROUTER_SOLICITATION_CMD : bool_opt})

    def interface_config_send_sets_mode(self, opt):
        """
        This is the method the command: interface_config option send_sets_mode
        Description:Specifies whether ordered set A and/or B is used in the error insertion.
        Constants Available: SEND_SETS_MODE_CMD
        Supported:IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.SEND_SETS_MODE_CMD : opt})

    def interface_config_sequence_checking(self, bool_opt):
        """
        This is the method the command: interface_config option sequence_checking
        Description:Whether to enable the frame sequence capability on this port. This option takes a list of values when -port_handle is a list of port handles. Valid options are: 0 - (default) Disable 1 - Enable
        Constants Available: SEQUENCE_CHECKING_CMD
        Supported:IxOS/IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.SEQUENCE_CHECKING_CMD : bool_opt})

    def interface_config_sequence_num_offset(self, range):
        """
        This is the method the command: interface_config option sequence_num_offset
        Description:The offset of the sequence number in the packet. If -port_rx_mode is set to auto_detect_instrumentation then this offset will be ignored. This option takes a list of values when -port_handle is a list of port handles.
        Constants Available: SEQUENCE_NUM_OFFSET_CMD
        Supported:IxOS/IxNetwork-NGPF
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.SEQUENCE_NUM_OFFSET_CMD : range})

    def interface_config_signature(self, opt):
        """
        This is the method the command: interface_config option signature
        Description:Signature used in the packet for Packet Group Statistics when packet groups or wide packet groups are enable. This signature will be searched into the received packets at offset represented by -signature_offset. If -port_rx_mode is set to auto_detect_instrumentation then this option will represent the a signature value of 12 hex bytes. This signature will be searched into the received packets starting with offset -signature_start_offset. This option takes a list of values when -port_handle is a list of port handles.
        Constants Available: SIGNATURE_CMD
        Supported:IxOS/IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.SIGNATURE_CMD : opt})

    def interface_config_signature_mask(self, opt):
        """
        This is the method the command: interface_config option signature_mask
        Description:Sets the signature mask when -port_rx_mode is set to auto_detect_instrumentation. Value 1 means don't care and value 0 means that that bit should correspond to the signature. If -signature is 00 00 00 00 00 00 00 00 23 45 67 89 and the -signature_mask is FF FF FF FF FF FF FF FF 00 00 00 00, then only last 4 bytes will be searched in the packet. This option takes a list of values when -port_handle is a list of port handles.
        Constants Available: SIGNATURE_MASK_CMD
        Supported:IxOS/IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.SIGNATURE_MASK_CMD : opt})

    def interface_config_signature_offset(self, range):
        """
        This is the method the command: interface_config option signature_offset
        Description:The offset of the signature in the packet. You can configure a fully customized signature in the packet for advanced testing. The signature of the packet is a 4-byte value, DE AD BE EF. This signature is used for ease of readability when capturing packets. If -port_rx_mode is set to auto_detect_instrumentation then this offset will be ignored. This option takes a list of values when -port_handle is a list of port handles.
        Constants Available: SIGNATURE_OFFSET_CMD
        Supported:IxOS/IxNetwork-NGPF
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.SIGNATURE_OFFSET_CMD : range})

    def interface_config_signature_start_offset(self, range):
        """
        This is the method the command: interface_config option signature_start_offset
        Description:If -port_rx_mode is set to auto_detect_instrumentation then this will be the offset start to search into the received packets for -signature option. This option takes a list of values when -port_handle is a list of port handles.
        Constants Available: SIGNATURE_START_OFFSET_CMD
        Supported:IxOS/IxNetwork-NGPF
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.SIGNATURE_START_OFFSET_CMD : range})

    def interface_config_single_arp_per_gateway(self, bool_opt):
        """
        This is the method the command: interface_config option single_arp_per_gateway
        Description:Send single ARP per gateway for the IPv4 interfaces when the port link becomes up. The option is global, for all ports and interfaces. This is valid only for the new API.
        Constants Available: SINGLE_ARP_PER_GATEWAY_CMD
        Supported:IxOS/IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.SINGLE_ARP_PER_GATEWAY_CMD : bool_opt})

    def interface_config_single_ns_per_gateway(self, bool_opt):
        """
        This is the method the command: interface_config option single_ns_per_gateway
        Description:Send single Neighbor Solicitation per gateway for the IPv6 interfaces when the port link becomes up. The option is global, for all ports and interfaces. This is valid only for the new API.
        Constants Available: SINGLE_NS_PER_GATEWAY_CMD
        Supported:IxOS/IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.SINGLE_NS_PER_GATEWAY_CMD : bool_opt})

    def interface_config_site_id(self, numeric):
        """
        This is the method the command: interface_config option site_id
        Description:VPN Site Identifier
        Constants Available: SITE_ID_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.SITE_ID_CMD : numeric})

    def interface_config_src_mac_addr_step(self, mac):
        """
        This is the method the command: interface_config option src_mac_addr_step
        Description:The incrementing step for the MAC address of the connected interface, when connected_count is greater than 1.This option takes a list of values when -port_handle is a list of port handles. This is valid for the new API. DEFAULT: 0000.0000.0001
        Constants Available: SRC_MAC_ADDR_STEP_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        mac --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.SRC_MAC_ADDR_STEP_CMD : mac})

    def interface_config_start_error_insertion(self, numeric):
        """
        This is the method the command: interface_config option start_error_insertion
        Description:L1 config parameter that starts/stops the error insertion for the contiguous 66-bit blocks. Valid only for Multis cards.
        Constants Available: START_ERROR_INSERTION_CMD
        Supported:IxOS/IxNetwork-FT
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.START_ERROR_INSERTION_CMD : numeric})

    def interface_config_static_ig_atm_encap(self, opt):
        """
        This is the method the command: interface_config option static_ig_atm_encap
        Description:Parameter valid only for IxNetwork static endpoints when -static_enable 1 and -static_ig_range_count > 0. The type of ATM encapsulation used for
        Constants Available: STATIC_IG_ATM_ENCAP_CMD
        Supported:IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.STATIC_IG_ATM_ENCAP_CMD : opt})

    def interface_config_static_ig_interface_enable_list(self, opt):
        """
        This is the method the command: interface_config option static_ig_interface_enable_list
        Description:Parameter valid only for IxNetwork static endpoints when -static_enable 1 and -static_ig_range_count > 0. Specify whether to enable the corresponding protocol interface entry. This parameter must be a list of values separated by semicolons having the same length as -static_ig_interface_handle_list.
        Constants Available: STATIC_IG_INTERFACE_ENABLE_LIST_CMD
        Supported:IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.STATIC_IG_INTERFACE_ENABLE_LIST_CMD : opt})

    def interface_config_static_ig_interface_handle_list(self, opt):
        """
        This is the method the command: interface_config option static_ig_interface_handle_list
        Description:Parameter valid only for IxNetwork static endpoints when -static_enable 1 and -static_ig_range_count > 0. A list of protocol interface handles (returned by interface_config with -l23_config_type protocol_interface) separated by semicolons :. Only protocol interfaces with matching IP version and VLAN setting must be used.
        Constants Available: STATIC_IG_INTERFACE_HANDLE_LIST_CMD
        Supported:IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.STATIC_IG_INTERFACE_HANDLE_LIST_CMD : opt})

    def interface_config_static_ig_ip_type(self, opt):
        """
        This is the method the command: interface_config option static_ig_ip_type
        Description:Parameter valid only for IxNetwork static endpoints when -static_enable 1 and -static_ig_range_count > 0. The IP version being used for the Protocol
        Constants Available: STATIC_IG_IP_TYPE_CMD
        Supported:IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.STATIC_IG_IP_TYPE_CMD : opt})

    def interface_config_static_ig_range_count(self, numeric):
        """
        This is the method the command: interface_config option static_ig_range_count
        Description:Parameter valid only for IxNetwork static endpoints when -static_enable 1. Specify the number of Interface Groups static endpoints to configure.
        Constants Available: STATIC_IG_RANGE_COUNT_CMD
        Supported:IxNetwork-FT
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.STATIC_IG_RANGE_COUNT_CMD : numeric})

    def interface_config_static_ig_vlan_enable(self, bool_opt):
        """
        This is the method the command: interface_config option static_ig_vlan_enable
        Description:Parameter valid only for IxNetwork static endpoints when -static_enable 1 and -static_ig_range_count > 0. Associate VLANs with the protocol interfaces. Vlan must already be enabled on the interfaces that will be specified with -static_ig_interface_handle_list.
        Constants Available: STATIC_IG_VLAN_ENABLE_CMD
        Supported:IxNetwork-FT
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.STATIC_IG_VLAN_ENABLE_CMD : bool_opt})

    def interface_config_static_lan_count_per_vc(self, numeric):
        """
        This is the method the command: interface_config option static_lan_count_per_vc
        Description:Parameter valid only for IxNetwork static endpoints when -static_enable 1 and -static_lan_range_count > 0 and -static_lan_mac_range_mode bundled. The total count per VC in this bundled mode.
        Constants Available: STATIC_LAN_COUNT_PER_VC_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.STATIC_LAN_COUNT_PER_VC_CMD : numeric})

    def interface_config_static_lan_incr_per_vc_vlan_mode(self, opt):
        """
        This is the method the command: interface_config option static_lan_incr_per_vc_vlan_mode
        Description:Parameter valid only for IxNetwork static endpoints when -static_enable 1 and -static_lan_range_count > 0 and -static_lan_mac_range_mode bundled. Enable the use of multiple VLANs, which are incremented for each additional VLAN per VC. Valid choices are: fixed (DEFAULT) increment inner outer
        Constants Available: STATIC_LAN_INCR_PER_VC_VLAN_MODE_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.STATIC_LAN_INCR_PER_VC_VLAN_MODE_CMD : opt})

    def interface_config_static_lan_intermediate_objref(self, opt):
        """
        This is the method the command: interface_config option static_lan_intermediate_objref
        Description:Parameter valid only for IxNetwork static endpoints when -static_enable 1 and -static_lan_range_count > 0. It is used to create a LAN object on ATM/POS interface related to a specific ATM/FR object. This parameter accepts static ATM/FR range handles (returned by interface_config with -static_enabled 1 and -static_atm_range_count/static_fr_range_count >=1). This parameter will be a list of elements separated by commas (,) that must be >= $static_lan_range_count divided by $static_range_per_spoke. ATM static endpoints can be used to create LAN objects only when -static_atm_header_encapsulation is one of: LLCBridgedEthernetFCS, LLCBridgedEthernetNoFCS, VccMuxBridgedEthernetFCS, VccMuxBridgedEthernetNoFCS. FR static endpoints can be used to create LAN objects only if layer 1 configuration of the port is Frame Relay (interface_config -intf_mode frame_relay2427).
        Constants Available: STATIC_LAN_INTERMEDIATE_OBJREF_CMD
        Supported:IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.STATIC_LAN_INTERMEDIATE_OBJREF_CMD : opt})

    def interface_config_static_lan_mac_range_mode(self, opt):
        """
        This is the method the command: interface_config option static_lan_mac_range_mode
        Description:Parameter valid only for IxNetwork static endpoints when -static_enable 1 and -static_lan_range_count > 0. Configure available MAC Range Mode. Valid choices are: normal - bundled -
            Valid options are:
            normal: This mode supports only a single MAC Id for all the VCs. Existing Static MAC Range fields are exposed in this mode. Parameters -static_lan_count_per_vc and -static_lan_number_of_vcs are ignored in this case.
            bundled: This mode supports Multiple MAC ids for each VC. Bundled mode is also useful to create MAC ranges for testing L2 devices when L2/VPN is not being used. This is intended for L2VPN/VPLS application where there is a need to simulate many MAC hosts behind each VC. The number of MAC Ids are dependent on the Number of VCs and Count Per VC that is configured.
        Constants Available: STATIC_LAN_MAC_RANGE_MODE_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.STATIC_LAN_MAC_RANGE_MODE_CMD : opt})

    def interface_config_static_lan_number_of_vcs(self, numeric):
        """
        This is the method the command: interface_config option static_lan_number_of_vcs
        Description:Parameter valid only for IxNetwork static endpoints when -static_enable 1 and -static_lan_range_count > 0 and -static_lan_mac_range_mode bundled. The total number of VCs.
        Constants Available: STATIC_LAN_NUMBER_OF_VCS_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.STATIC_LAN_NUMBER_OF_VCS_CMD : numeric})

    def interface_config_static_lan_skip_vlan_id_zero(self, bool_opt):
        """
        This is the method the command: interface_config option static_lan_skip_vlan_id_zero
        Description:Parameter valid only for IxNetwork static endpoints when -static_enable 1 and -static_lan_range_count > 0. Enable skip vlan id 0.
        Constants Available: STATIC_LAN_SKIP_VLAN_ID_ZERO_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.STATIC_LAN_SKIP_VLAN_ID_ZERO_CMD : bool_opt})

    def interface_config_static_lan_tpid(self, opt):
        """
        This is the method the command: interface_config option static_lan_tpid
        Description:Parameter valid only for IxNetwork static endpoints when -static_enable 1 and -static_lan_range_count > 0 and -static_vlan_enable 1. Tag Protocol Identifier // TPID (hex). The EtherType that identifies the protocol header that follows the VLAN header (tag). If stacked vlans need to be created, a list of values separated by the colon(:) character must be provided to this parameter. Valid choices are: 0x8100 (DEFAULT) 0x88a8 0x9100 0x9200
        Constants Available: STATIC_LAN_TPID_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.STATIC_LAN_TPID_CMD : opt})

    def interface_config_static_lan_vlan_priority(self, range):
        """
        This is the method the command: interface_config option static_lan_vlan_priority
        Description:Parameter valid only for IxNetwork static endpoints when -static_enable 1 and -static_lan_range_count > 0 and -static_vlan_enable 1. The user priority of the VLAN tag: a value from 0 through 7. The use and interpretation of this field is defined in ISO/IEC 15802-3. If stacked vlans need to be created, a list of values separated by the colon(:) character must be provided to this parameter.
        Constants Available: STATIC_LAN_VLAN_PRIORITY_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.STATIC_LAN_VLAN_PRIORITY_CMD : range})

    def interface_config_static_lan_vlan_stack_count(self, numeric):
        """
        This is the method the command: interface_config option static_lan_vlan_stack_count
        Description:Parameter valid only for IxNetwork static endpoints when -static_enable 1 and -static_lan_range_count > 0 and -static_vlan_enable 1. The number of VLANs configured for stacked VLANs/QinQ.
        Constants Available: STATIC_LAN_VLAN_STACK_COUNT_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.STATIC_LAN_VLAN_STACK_COUNT_CMD : numeric})

    def interface_config_target_link_layer_address(self, bool_opt):
        """
        This is the method the command: interface_config option target_link_layer_address
        Description:Enable target the link layer address for an IPv6 interface.This is valid when l23_config_type is protocol_interface (new API).
        Constants Available: TARGET_LINK_LAYER_ADDRESS_CMD
        Supported:IxNetwork-FT
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.TARGET_LINK_LAYER_ADDRESS_CMD : bool_opt})

    def interface_config_transmit_mode(self, opt):
        """
        This is the method the command: interface_config option transmit_mode
        Description:Type of stream for this port. This option takes a list of values when -port_handle is a list of port handles.
            Valid options are:
            advanced: Sets up the hardware to use the advanced stream scheduler, which involves the ability to interleave differing streams within one stream definition. Valid for the old and new API.
            stream: Sets up the hardware to use normal streams. Valid for the old and new API.
            advanced_coarse: Sets up the hardware to use the advanced stream scheduler, but with less precision and CPU utilization. This option is specific to virtual ports and is valid only for intf_mode = ethernet_vm.
            stream_coarse: Sets up the hardware to use less precision and CPU utilization with normal streams. This option is specific to virtual ports and is valid only for intf_mode = ethernet_vm.
            flow: Sets up the hardware to use flows. Valid only for the old API(IxTclProtocol).
            echo: Sets up port to echo received packets (for gigabit cards only). Valid only for the old API(IxTclProtocol).
        Constants Available: TRANSMIT_MODE_CMD
        Supported:IxOS/IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.TRANSMIT_MODE_CMD : opt})

    def interface_config_tx_gap_control_mode(self, opt):
        """
        This is the method the command: interface_config option tx_gap_control_mode
        Description:Valid only for new API when speed is ether10000wan or ether10000lan and intf_mode is ethernet | ethernet_fcoe.
            Valid options are:
            fixed: Sets gap control to fixed mode
            average: Sets gap control to average mode
            DEPENDENCIES: Valid in combination with parameter(s)
            'speed' | value= 'ether10000wan' |
            'speed' | value= 'ether10000lan' |
            'intf_mode' | value= 'ethernet' |
            'intf_mode' | value= 'ethernet_fcoe' |
        Constants Available: TX_GAP_CONTROL_MODE_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.TX_GAP_CONTROL_MODE_CMD : opt})

    def interface_config_tx_ignore_rx_link_faults(self, bool_opt):
        """
        This is the method the command: interface_config option tx_ignore_rx_link_faults
        Description:Valid only with ixnetwork new api. Enable to send trafic even if the receive link is down.
        Constants Available: TX_IGNORE_RX_LINK_FAULTS_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.TX_IGNORE_RX_LINK_FAULTS_CMD : bool_opt})

    def interface_config_tx_lanes(self, opt):
        """
        This is the method the command: interface_config option tx_lanes
        Description:This option takes a list of txLanes. This parameter is valid only with IxTclHal api.:,|:,|....
        Constants Available: TX_LANES_CMD
        Supported:IxOS/IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.TX_LANES_CMD : opt})

    def interface_config_type_a_ordered_sets(self, opt):
        """
        This is the method the command: interface_config option type_a_ordered_sets
        Description:L1 config parameter that indicates whether the type should insert a local error, a remote error or a custom ordered set. Valid only for Multis cards.
        Constants Available: TYPE_A_ORDERED_SETS_CMD
        Supported:IxOs/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.TYPE_A_ORDERED_SETS_CMD : opt})

    def interface_config_type_b_ordered_sets(self, opt):
        """
        This is the method the command: interface_config option type_b_ordered_sets
        Description:L1 config parameter that indicates whether the type should insert a local error, a remote error or a custom ordered set. Valid only for Multis cards.
        Constants Available: TYPE_B_ORDERED_SETS_CMD
        Supported:IxOs/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.TYPE_B_ORDERED_SETS_CMD : opt})

    def interface_config_use_vpn_parameters(self, bool_opt):
        """
        This is the method the command: interface_config option use_vpn_parameters
        Description:Flag to determine whether optional VPN parameters are provided.
        Constants Available: USE_VPN_PARAMETERS_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.USE_VPN_PARAMETERS_CMD : bool_opt})

    def interface_config_vci(self, range):
        """
        This is the method the command: interface_config option vci
        Description:The VCI value when configuring ATM interfaces. This option takes a list of values when -port_handle is a list of port handles. This is valid for the old and new API.
        Constants Available: VCI_CMD
        Supported:IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.VCI_CMD : range})

    def interface_config_vci_count(self, range):
        """
        This is the method the command: interface_config option vci_count
        Description:The number of unique VCI values. This parameter is valid when l23_config_type is static_endpoint (new API).
        Constants Available: VCI_COUNT_CMD
        Supported:IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.VCI_COUNT_CMD : range})

    def interface_config_vci_step(self, range):
        """
        This is the method the command: interface_config option vci_step
        Description:The incrementing step for the VCI of the interface, when connected_count is greater than 1. The vci will be incremented modulo 65536, when the maximum value is reached, the counting starts again from 32. This option is valid only when l23_config_type is static_endpoint (new API). This option takes a list of values when -port_handle is a list of port handles.
        Constants Available: VCI_STEP_CMD
        Supported:IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.VCI_STEP_CMD : range})

    def interface_config_vlan_id(self, range):
        """
        This is the method the command: interface_config option vlan_id
        Description:VLAN ID of each interface where VLAN is enabled. This parameter accepts a list of numbers separated by ',' - the vlan id for each encapsulation 802.1q. This is how stacked vlan is configured. Each value should be between 0 and 4095, inclusive, for l23_config_type protocol_interfaces. Each value should be between 0 and 4094, inclusive, for l23_config_type static_endpoint. This option takes a list of values when -port_handle is a list of port handles. This is valid for the old and new API.
        Constants Available: VLAN_ID_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.VLAN_ID_CMD : range})

    def interface_config_vlan_id_count(self, range):
        """
        This is the method the command: interface_config option vlan_id_count
        Description:The number of unique outer VLAN IDs that will be created. This parameter accepts a list of numbers separated by ',' - the vlan id count for each encapsulation 802.1q. This is how stacked vlan is configured. This option is valid only when l23_config_type is static_endpoint. This option takes a list of values when -port_handle is a list of port handles. For stacked vlans this parameter accepts a list of elements, each element being represented by numbers separated through comma(,). This option is valid only when l23_config_type is static_endpoint (new API).
        Constants Available: VLAN_ID_COUNT_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.VLAN_ID_COUNT_CMD : range})

    def interface_config_vlan_id_inner(self, range):
        """
        This is the method the command: interface_config option vlan_id_inner
        Description:Set the VLAN ID 2 associated with the address pool. Only works is VLAN is enabled and vlan_id provided.Each value should be between 0 and 4095, inclusive. For stacked vlans this parameter accepts a list of elements, each element being represented by numbers separated through comma(,).This is valid for the old and new API.
        Constants Available: VLAN_ID_INNER_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.VLAN_ID_INNER_CMD : range})

    def interface_config_vlan_id_inner_count(self, range):
        """
        This is the method the command: interface_config option vlan_id_inner_count
        Description:Count value of inner VLAN ID per outer VLAN. Depending on this value outer and inner VLANs are incremented in QinQ. If not specified outer and inner VLANs are incremented independently. For stacked vlans this parameter accepts a list of elements, each element being represented by numbers separated through comma(,). This parameter is ignored if -vlan_id_inner is not specified in the same command. This option is valid only when l23_config_type is static_endpoint (new API).
        Constants Available: VLAN_ID_INNER_COUNT_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.VLAN_ID_INNER_COUNT_CMD : range})

    def interface_config_vlan_id_inner_mode(self, opt):
        """
        This is the method the command: interface_config option vlan_id_inner_mode
        Description:Used to specify whether VLAN ID is the same, or incremented, for multiple addresses. This parameter is ignored if -vlan_id_inner is not specified in the same command. This option is valid only when l23_config_type is static_endpoint (new API).
        Constants Available: VLAN_ID_INNER_MODE_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.VLAN_ID_INNER_MODE_CMD : opt})

    def interface_config_vlan_id_inner_step(self, range):
        """
        This is the method the command: interface_config option vlan_id_inner_step
        Description:Used to specify how much the VLAN ID 2 is incremented when vlan_id_inner_mode is increment. For stacked vlans this parameter accepts a list of elements, each element being represented by numbers separated through comma(,). This parameter is ignored if -vlan_id_inner is not specified in the same command. This option is valid only when l23_config_type is static_endpoint (new API).
        Constants Available: VLAN_ID_INNER_STEP_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.VLAN_ID_INNER_STEP_CMD : range})

    def interface_config_vlan_id_list(self, range):
        """
        This is the method the command: interface_config option vlan_id_list
        Description:See description for -vlan_id parameter. If both vlan_id and vlan_id_list are present, vlan_id_list takes precedence. If vlan_id_list is present vlan_id_inner will be ignored. This is valid for the old and new API.
        Constants Available: VLAN_ID_LIST_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.VLAN_ID_LIST_CMD : range})

    def interface_config_vlan_id_mode(self, opt):
        """
        This is the method the command: interface_config option vlan_id_mode
        Description:Used to specify whether VLAN ID is the same, or incremented, for multiple addresses.This is valid for the old and new API.
            Valid options are:
            fixed
            increment
        Constants Available: VLAN_ID_MODE_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.VLAN_ID_MODE_CMD : opt})

    def interface_config_vlan_id_step(self, range):
        """
        This is the method the command: interface_config option vlan_id_step
        Description:The incrementing step for the VLAN ID of the interface, when connected_count is greater than 1. The vlan_id will be incremented modulo 4096, when the maximum value is reached, the counting starts again from 0. The vlan_id will be incremented modulo 4094 (by default), when the maximum value is reached, the counting starts again from 0, for l23_config_type static_endpoint, but the number of unique values can be modified by using vlan_id_count.This option takes a list of values when -port_handle is a list of port handles. For stacked vlans this parameter accepts a list of elements, each element being represented by numbers separated through comma(,).This is valid for the old and new API.
        Constants Available: VLAN_ID_STEP_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.VLAN_ID_STEP_CMD : range})

    def interface_config_vlan_protocol_id(self, opt):
        """
        This is the method the command: interface_config option vlan_protocol_id
        Description:See -vlan_tpid parameter
        Constants Available: VLAN_PROTOCOL_ID_CMD
        Supported:IxOS/IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.VLAN_PROTOCOL_ID_CMD : opt})

    def interface_config_vlan_tpid(self, opt):
        """
        This is the method the command: interface_config option vlan_tpid
        Description:Tag Protocol Identifier // TPID (hex). The EtherType that identifies the protocol header that follows the VLAN header (tag).Available TPIDs: 0x8100 (the default), 0x88a8, 0x9100, 0x9200.If the VLAN Count is greater than 1 (for stacked VLANs), this field also accepts comma-separated values so that different TPID values can be assigned to different VLANs. For example, to assign TPID 0x8100, 0x9100, 0x9200, and 0x9200 to the first four created VLANs, enter: 0x8100,0x9100,0x9200,0x9200.This option takes a list of values when -port_handle is a list of port handles. This option is valid only when l23_config_type is protocol_interface. This is valid for the old and new API. DEFAULT: 0x8100
        Constants Available: VLAN_TPID_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.VLAN_TPID_CMD : opt})

    def interface_config_vlan_user_priority(self, range):
        """
        This is the method the command: interface_config option vlan_user_priority
        Description:If VLAN is enabled on the interface, the priority of the VLAN. For each interface, the user priority list should be given as a list of integers separated by commas. This parameter accepts a list of user priority for each 802.1 encapsulation used. Valid choices for each element in the list are between 0 and 7, inclusive. This option takes a list of values when -port_handle is a list of port handles. For example, if we have 2 interfaces with 3 vlans each, the user priority could be: [list 1,2,7 1,3,4]
        Constants Available: VLAN_USER_PRIORITY_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.VLAN_USER_PRIORITY_CMD : range})

    def interface_config_vlan_user_priority_step(self, range):
        """
        This is the method the command: interface_config option vlan_user_priority_step
        Description:The incrementing step for the VLAN user priority of the interface, when connected_count is greater than 1. The vlan_user_priority will be incremented modulo 8, when the maximum value is reached, the counting starts again from 0. This option is valid only when l23_config_type is static_endpoint. This option takes a list of values when -port_handle is a list of port handles. This is valid for the old and new API.
        Constants Available: VLAN_USER_PRIORITY_STEP_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.VLAN_USER_PRIORITY_STEP_CMD : range})

    def interface_config_vpi(self, range):
        """
        This is the method the command: interface_config option vpi
        Description:The VPI value when configuring ATM interfaces. This option takes a list of values when -port_handle is a list of port handles. This is valid for the old and new API.
        Constants Available: VPI_CMD
        Supported:IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.VPI_CMD : range})

    def interface_config_vpi_count(self, range):
        """
        This is the method the command: interface_config option vpi_count
        Description:The number of unique VPI values. This parameter is valid when l23_config_type is static_endpoint (new API).
        Constants Available: VPI_COUNT_CMD
        Supported:IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.VPI_COUNT_CMD : range})

    def interface_config_vpi_step(self, range):
        """
        This is the method the command: interface_config option vpi_step
        Description:The incrementing step for the VPI of the interface, when connected_count is greater than 1. The vpi will be incremented modulo 256, when the maximum value is reached, the counting starts again from 0. This option is valid only when l23_config_type is static_endpoint (new API). This option takes a list of values when -port_handle is a list of port handles.
        Constants Available: VPI_STEP_CMD
        Supported:IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.VPI_STEP_CMD : range})

    supportedIxiaHltapiCommands = {InterfaceConfigConstants.ADDITIONAL_FCOE_STAT_1_CMD,
                                   InterfaceConfigConstants.ADDITIONAL_FCOE_STAT_2_CMD,
                                   InterfaceConfigConstants.ADDRESSES_PER_SVLAN_CMD,
                                   InterfaceConfigConstants.ADDRESSES_PER_VCI_CMD,
                                   InterfaceConfigConstants.ADDRESSES_PER_VLAN_CMD,
                                   InterfaceConfigConstants.ADDRESSES_PER_VPI_CMD,
                                   InterfaceConfigConstants.ARP_CMD,
                                   InterfaceConfigConstants.ARP_ON_LINKUP_CMD,
                                   InterfaceConfigConstants.ARP_REFRESH_INTERVAL_CMD,
                                   InterfaceConfigConstants.ARP_REQ_RETRIES_CMD,
                                   InterfaceConfigConstants.ARP_REQ_TIMER_CMD,
                                   InterfaceConfigConstants.ARP_SEND_REQ_CMD, InterfaceConfigConstants.ATM_ENABLE_COSET_CMD, InterfaceConfigConstants.ATM_ENABLE_PATTERN_MATCHING_CMD, InterfaceConfigConstants.ATM_ENCAPSULATION_CMD, InterfaceConfigConstants.ATM_FILLER_CELL_CMD, InterfaceConfigConstants.ATM_INTERFACE_TYPE_CMD, InterfaceConfigConstants.ATM_PACKET_DECODE_MODE_CMD, InterfaceConfigConstants.ATM_REASSEMBLY_TIMEOUT_CMD, InterfaceConfigConstants.AUTO_DETECT_INSTRUMENTATION_TYPE_CMD, InterfaceConfigConstants.AUTONEGOTIATION_CMD, InterfaceConfigConstants.BAD_BLOCKS_NUMBER_CMD, InterfaceConfigConstants.BERT_CONFIGURATION_CMD,
                                   InterfaceConfigConstants.BERT_ERROR_INSERTION_CMD,
                                   InterfaceConfigConstants.CHECK_GATEWAY_EXISTS_CMD, InterfaceConfigConstants.CHECK_OPPOSITE_IP_VERSION_CMD, InterfaceConfigConstants.CLOCKSOURCE_CMD, InterfaceConfigConstants.CONNECTED_COUNT_CMD, InterfaceConfigConstants.CONNECTED_TO_HANDLE_CMD, InterfaceConfigConstants.DATA_INTEGRITY_CMD,
                                   InterfaceConfigConstants.DUPLEX_CMD,
                                   InterfaceConfigConstants.ENABLE_DATA_CENTER_SHARED_STATS_CMD, InterfaceConfigConstants.ENABLE_FLOW_CONTROL_CMD, InterfaceConfigConstants.ENABLE_LOOPBACK_CMD, InterfaceConfigConstants.ENABLE_NDP_CMD, InterfaceConfigConstants.ENABLE_RS_FEC_CMD, InterfaceConfigConstants.ENABLE_RS_FEC_STATISTICS_CMD, InterfaceConfigConstants.ETHERNET_ATTEMPT_ENABLED_CMD, InterfaceConfigConstants.ETHERNET_ATTEMPT_INTERVAL_CMD, InterfaceConfigConstants.ETHERNET_ATTEMPT_RATE_CMD, InterfaceConfigConstants.ETHERNET_ATTEMPT_SCALE_MODE_CMD, InterfaceConfigConstants.ETHERNET_DICONNECT_ENABLED_CMD, InterfaceConfigConstants.ETHERNET_DISCONNECT_INTERVAL_CMD, InterfaceConfigConstants.ETHERNET_DISCONNECT_RATE_CMD, InterfaceConfigConstants.ETHERNET_DISCONNECT_SCALE_MODE_CMD, InterfaceConfigConstants.FC_CREDIT_STARVATION_VALUE_CMD, InterfaceConfigConstants.FC_FIXED_DELAY_VALUE_CMD, InterfaceConfigConstants.FC_FORCE_ERRORS_CMD, InterfaceConfigConstants.FC_MAX_DELAY_FOR_RANDOM_VALUE_CMD, InterfaceConfigConstants.FC_MIN_DELAY_FOR_RANDOM_VALUE_CMD, InterfaceConfigConstants.FC_NO_RRDY_AFTER_CMD, InterfaceConfigConstants.FC_RRDY_RESPONSE_DELAYS_CMD, InterfaceConfigConstants.FC_TX_IGNORE_AVAILABLE_CREDITS_CMD, InterfaceConfigConstants.FC_TX_IGNORE_RX_LINK_FAULTS_CMD, InterfaceConfigConstants.FCOE_FLOW_CONTROL_TYPE_CMD, InterfaceConfigConstants.FCOE_PRIORITY_GROUP_SIZE_CMD, InterfaceConfigConstants.FCOE_PRIORITY_GROUPS_CMD, InterfaceConfigConstants.FCOE_SUPPORT_DATA_CENTER_MODE_CMD, InterfaceConfigConstants.FLOW_CONTROL_DIRECTED_ADDR_CMD, InterfaceConfigConstants.FRAMING_CMD, InterfaceConfigConstants.GATEWAY_CMD, InterfaceConfigConstants.GATEWAY_INCR_MODE_CMD, InterfaceConfigConstants.GATEWAY_STEP_CMD, InterfaceConfigConstants.GOOD_BLOCKS_NUMBER_CMD, InterfaceConfigConstants.GRE_CHECKSUM_ENABLE_CMD, InterfaceConfigConstants.GRE_COUNT_CMD, InterfaceConfigConstants.GRE_DST_IP_ADDR_CMD, InterfaceConfigConstants.GRE_DST_IP_ADDR_STEP_CMD, InterfaceConfigConstants.GRE_IP_ADDR_CMD, InterfaceConfigConstants.GRE_IP_ADDR_STEP_CMD, InterfaceConfigConstants.GRE_IP_PREFIX_LENGTH_CMD, InterfaceConfigConstants.GRE_IPV6_ADDR_CMD, InterfaceConfigConstants.GRE_IPV6_ADDR_STEP_CMD, InterfaceConfigConstants.GRE_IPV6_PREFIX_LENGTH_CMD, InterfaceConfigConstants.GRE_KEY_ENABLE_CMD, InterfaceConfigConstants.GRE_KEY_IN_CMD, InterfaceConfigConstants.GRE_KEY_OUT_CMD, InterfaceConfigConstants.GRE_SEQ_ENABLE_CMD, InterfaceConfigConstants.IEEE_MEDIA_DEFAULTS_CMD, InterfaceConfigConstants.IGNORE_LINK_CMD, InterfaceConfigConstants.INTEGRITY_SIGNATURE_CMD, InterfaceConfigConstants.INTEGRITY_SIGNATURE_OFFSET_CMD, InterfaceConfigConstants.INTERFACE_HANDLE_CMD, InterfaceConfigConstants.INTERNAL_PPM_ADJUST_CMD, InterfaceConfigConstants.INTF_IP_ADDR_CMD, InterfaceConfigConstants.INTF_IP_ADDR_STEP_CMD, InterfaceConfigConstants.INTF_MODE_CMD, InterfaceConfigConstants.INTRINSIC_LATENCY_ADJUSTMENT_CMD, InterfaceConfigConstants.IPV4_ATTEMPT_ENABLED_CMD, InterfaceConfigConstants.IPV4_ATTEMPT_INTERVAL_CMD, InterfaceConfigConstants.IPV4_ATTEMPT_RATE_CMD, InterfaceConfigConstants.IPV4_ATTEMPT_SCALE_MODE_CMD, InterfaceConfigConstants.IPV4_DICONNECT_ENABLED_CMD, InterfaceConfigConstants.IPV4_DISCONNECT_INTERVAL_CMD, InterfaceConfigConstants.IPV4_DISCONNECT_RATE_CMD, InterfaceConfigConstants.IPV4_DISCONNECT_SCALE_MODE_CMD, InterfaceConfigConstants.IPV4_MANUAL_GATEWAY_MAC_CMD, InterfaceConfigConstants.IPV4_MANUAL_GATEWAY_MAC_STEP_CMD, InterfaceConfigConstants.IPV4_RE_SEND_ARP_ON_LINK_UP_CMD, InterfaceConfigConstants.IPV4_RESOLVE_GATEWAY_CMD, InterfaceConfigConstants.IPV4_SEND_ARP_INTERVAL_CMD, InterfaceConfigConstants.IPV4_SEND_ARP_MAX_OUTSTANDING_CMD, InterfaceConfigConstants.IPV4_SEND_ARP_RATE_CMD, InterfaceConfigConstants.IPV4_SEND_ARP_SCALE_MODE_CMD, InterfaceConfigConstants.IPV6_ADDR_MODE_CMD, InterfaceConfigConstants.IPV6_ATTEMPT_ENABLED_CMD, InterfaceConfigConstants.IPV6_ATTEMPT_INTERVAL_CMD, InterfaceConfigConstants.IPV6_ATTEMPT_RATE_CMD, InterfaceConfigConstants.IPV6_ATTEMPT_SCALE_MODE_CMD, InterfaceConfigConstants.IPV6_AUTOCONFIGURATION_ATTEMPT_ENABLED_CMD, InterfaceConfigConstants.IPV6_AUTOCONFIGURATION_ATTEMPT_INTERVAL_CMD, InterfaceConfigConstants.IPV6_AUTOCONFIGURATION_ATTEMPT_MAX_OUTSTANDING_CMD, InterfaceConfigConstants.IPV6_AUTOCONFIGURATION_ATTEMPT_RATE_CMD, InterfaceConfigConstants.IPV6_AUTOCONFIGURATION_ATTEMPT_SCALE_MODE_CMD, InterfaceConfigConstants.IPV6_AUTOCONFIGURATION_DISCONNECT_ENABLED_CMD, InterfaceConfigConstants.IPV6_AUTOCONFIGURATION_DISCONNECT_INTERVAL_CMD, InterfaceConfigConstants.IPV6_AUTOCONFIGURATION_DISCONNECT_MAX_OUTSTANDING_CMD, InterfaceConfigConstants.IPV6_AUTOCONFIGURATION_DISCONNECT_RATE_CMD, InterfaceConfigConstants.IPV6_AUTOCONFIGURATION_DISCONNECT_SCALE_MODE_CMD, InterfaceConfigConstants.IPV6_AUTOCONFIGURATION_SEND_NS_ENABLED_CMD, InterfaceConfigConstants.IPV6_AUTOCONFIGURATION_SEND_NS_MAX_OUTSTANDING_CMD, InterfaceConfigConstants.IPV6_AUTOCONFIGURATION_SEND_NS_RATE_CMD, InterfaceConfigConstants.IPV6_AUTOCONFIGURATION_SEND_NS_SCALE_MODE_CMD, InterfaceConfigConstants.IPV6_AUTOCONFIGURATION_SEND_RS_ENABLED_CMD, InterfaceConfigConstants.IPV6_AUTOCONFIGURATION_SEND_RS_INTERVAL_CMD, InterfaceConfigConstants.IPV6_AUTOCONFIGURATION_SEND_RS_MAX_OUTSTANDING_CMD, InterfaceConfigConstants.IPV6_AUTOCONFIGURATION_SEND_RS_RATE_CMD, InterfaceConfigConstants.IPV6_AUTOCONFIGURATION_SEND_RS_SCALE_MODE_CMD, InterfaceConfigConstants.IPV6_DICONNECT_ENABLED_CMD, InterfaceConfigConstants.IPV6_DISCONNECT_INTERVAL_CMD, InterfaceConfigConstants.IPV6_DISCONNECT_RATE_CMD, InterfaceConfigConstants.IPV6_DISCONNECT_SCALE_MODE_CMD, InterfaceConfigConstants.IPV6_GATEWAY_CMD, InterfaceConfigConstants.IPV6_GATEWAY_STEP_CMD, InterfaceConfigConstants.IPV6_INTF_ADDR_CMD, InterfaceConfigConstants.IPV6_INTF_ADDR_STEP_CMD, InterfaceConfigConstants.IPV6_LOOPBACK_MULTIPLIER_CMD, InterfaceConfigConstants.IPV6_MANUAL_GATEWAY_MAC_CMD, InterfaceConfigConstants.IPV6_MANUAL_GATEWAY_MAC_STEP_CMD, InterfaceConfigConstants.IPV6_MULTIPLIER_CMD, InterfaceConfigConstants.IPV6_PREFIX_LENGTH_CMD, InterfaceConfigConstants.IPV6_RE_SEND_NS_ON_LINK_UP_CMD, InterfaceConfigConstants.IPV6_RESOLVE_GATEWAY_CMD, InterfaceConfigConstants.IPV6_SEND_NS_INTERVAL_CMD, InterfaceConfigConstants.IPV6_SEND_NS_MAX_OUTSTANDING_CMD, InterfaceConfigConstants.IPV6_SEND_NS_RATE_CMD, InterfaceConfigConstants.IPV6_SEND_NS_SCALE_MODE_CMD, InterfaceConfigConstants.L23_CONFIG_TYPE_CMD, InterfaceConfigConstants.LASER_ON_CMD, InterfaceConfigConstants.LINK_TRAINING_CMD, InterfaceConfigConstants.LOOP_CONTINUOUSLY_CMD, InterfaceConfigConstants.LOOP_COUNT_NUMBER_CMD, InterfaceConfigConstants.MASTER_SLAVE_MODE_CMD, InterfaceConfigConstants.MODE_CMD, InterfaceConfigConstants.MSS_CMD, InterfaceConfigConstants.MTU_CMD, InterfaceConfigConstants.NDP_SEND_REQ_CMD, InterfaceConfigConstants.NETMASK_CMD, InterfaceConfigConstants.NO_WRITE_CMD, InterfaceConfigConstants.NOTIFY_MAC_MOVE_CMD, InterfaceConfigConstants.NS_ON_LINKUP_CMD, InterfaceConfigConstants.OP_MODE_CMD, InterfaceConfigConstants.OVERRIDE_EXISTENCE_CHECK_CMD, InterfaceConfigConstants.OVERRIDE_TRACKING_CMD, InterfaceConfigConstants.PCS_COUNT_CMD, InterfaceConfigConstants.PCS_ENABLED_CONTINUOUS_CMD, InterfaceConfigConstants.PCS_LANE_CMD, InterfaceConfigConstants.PCS_MARKER_FIELDS_CMD, InterfaceConfigConstants.PCS_PERIOD_CMD, InterfaceConfigConstants.PCS_PERIOD_TYPE_CMD, InterfaceConfigConstants.PCS_REPEAT_CMD, InterfaceConfigConstants.PCS_SYNC_BITS_CMD, InterfaceConfigConstants.PGID_128K_BIN_ENABLE_CMD, InterfaceConfigConstants.PGID_ENCAP_CMD, InterfaceConfigConstants.PGID_MASK_CMD, InterfaceConfigConstants.PGID_MODE_CMD, InterfaceConfigConstants.PGID_OFFSET_CMD, InterfaceConfigConstants.PGID_SPLIT1_MASK_CMD, InterfaceConfigConstants.PGID_SPLIT1_OFFSET_CMD, InterfaceConfigConstants.PGID_SPLIT1_OFFSET_FROM_CMD, InterfaceConfigConstants.PGID_SPLIT1_WIDTH_CMD, InterfaceConfigConstants.PGID_SPLIT2_MASK_CMD, InterfaceConfigConstants.PGID_SPLIT2_OFFSET_CMD, InterfaceConfigConstants.PGID_SPLIT2_OFFSET_FROM_CMD, InterfaceConfigConstants.PGID_SPLIT2_WIDTH_CMD, InterfaceConfigConstants.PGID_SPLIT3_MASK_CMD, InterfaceConfigConstants.PGID_SPLIT3_OFFSET_CMD, InterfaceConfigConstants.PGID_SPLIT3_OFFSET_FROM_CMD, InterfaceConfigConstants.PGID_SPLIT3_WIDTH_CMD, InterfaceConfigConstants.PHY_MODE_CMD, InterfaceConfigConstants.PING_DST_CMD, InterfaceConfigConstants.PORT_HANDLE_CMD, InterfaceConfigConstants.PORT_RX_MODE_CMD, InterfaceConfigConstants.PPP_IPV4_ADDRESS_CMD, InterfaceConfigConstants.PPP_IPV4_NEGOTIATION_CMD, InterfaceConfigConstants.PPP_IPV6_NEGOTIATION_CMD, InterfaceConfigConstants.PPP_MPLS_NEGOTIATION_CMD, InterfaceConfigConstants.PPP_OSI_NEGOTIATION_CMD, InterfaceConfigConstants.PROTOCOL_HANDLE_CMD, InterfaceConfigConstants.PROTOCOL_NAME_CMD, InterfaceConfigConstants.PVC_INCR_MODE_CMD, InterfaceConfigConstants.QINQ_INCR_MODE_CMD, InterfaceConfigConstants.QOS_BYTE_OFFSET_CMD, InterfaceConfigConstants.QOS_PACKET_TYPE_CMD, InterfaceConfigConstants.QOS_PATTERN_MASK_CMD, InterfaceConfigConstants.QOS_PATTERN_MATCH_CMD, InterfaceConfigConstants.QOS_PATTERN_OFFSET_CMD, InterfaceConfigConstants.QOS_STATS_CMD, InterfaceConfigConstants.ROUTER_SOLICITATION_RETRIES_CMD, InterfaceConfigConstants.RPR_HEC_SEED_CMD, InterfaceConfigConstants.RX_C2_CMD, InterfaceConfigConstants.RX_FCS_CMD, InterfaceConfigConstants.RX_SCRAMBLING_CMD, InterfaceConfigConstants.SEND_PING_CMD, InterfaceConfigConstants.SEND_ROUTER_SOLICITATION_CMD, InterfaceConfigConstants.SEND_SETS_MODE_CMD, InterfaceConfigConstants.SEQUENCE_CHECKING_CMD, InterfaceConfigConstants.SEQUENCE_NUM_OFFSET_CMD, InterfaceConfigConstants.SIGNATURE_CMD, InterfaceConfigConstants.SIGNATURE_MASK_CMD, InterfaceConfigConstants.SIGNATURE_OFFSET_CMD, InterfaceConfigConstants.SIGNATURE_START_OFFSET_CMD, InterfaceConfigConstants.SINGLE_ARP_PER_GATEWAY_CMD, InterfaceConfigConstants.SINGLE_NS_PER_GATEWAY_CMD, InterfaceConfigConstants.SITE_ID_CMD, InterfaceConfigConstants.SPEED_CMD, InterfaceConfigConstants.SRC_MAC_ADDR_CMD, InterfaceConfigConstants.SRC_MAC_ADDR_STEP_CMD, InterfaceConfigConstants.START_ERROR_INSERTION_CMD, InterfaceConfigConstants.STATIC_ATM_HEADER_ENCAPSULATION_CMD, InterfaceConfigConstants.STATIC_ATM_RANGE_COUNT_CMD, InterfaceConfigConstants.STATIC_DLCI_COUNT_MODE_CMD, InterfaceConfigConstants.STATIC_DLCI_REPEAT_COUNT_CMD, InterfaceConfigConstants.STATIC_DLCI_VALUE_CMD, InterfaceConfigConstants.STATIC_DLCI_VALUE_STEP_CMD, InterfaceConfigConstants.STATIC_ENABLE_CMD, InterfaceConfigConstants.STATIC_FR_RANGE_COUNT_CMD, InterfaceConfigConstants.STATIC_IG_ATM_ENCAP_CMD, InterfaceConfigConstants.STATIC_IG_INTERFACE_ENABLE_LIST_CMD, InterfaceConfigConstants.STATIC_IG_INTERFACE_HANDLE_LIST_CMD, InterfaceConfigConstants.STATIC_IG_IP_TYPE_CMD, InterfaceConfigConstants.STATIC_IG_RANGE_COUNT_CMD, InterfaceConfigConstants.STATIC_IG_VLAN_ENABLE_CMD, InterfaceConfigConstants.STATIC_INDIRECT_CMD, InterfaceConfigConstants.STATIC_INTF_HANDLE_CMD, InterfaceConfigConstants.STATIC_IP_DST_ADDR_CMD, InterfaceConfigConstants.STATIC_IP_DST_COUNT_CMD, InterfaceConfigConstants.STATIC_IP_DST_COUNT_STEP_CMD, InterfaceConfigConstants.STATIC_IP_DST_INCREMENT_CMD, InterfaceConfigConstants.STATIC_IP_DST_INCREMENT_STEP_CMD, InterfaceConfigConstants.STATIC_IP_DST_PREFIX_LEN_CMD, InterfaceConfigConstants.STATIC_IP_DST_PREFIX_LEN_STEP_CMD, InterfaceConfigConstants.STATIC_IP_DST_RANGE_STEP_CMD, InterfaceConfigConstants.STATIC_IP_RANGE_COUNT_CMD, InterfaceConfigConstants.STATIC_L3_PROTOCOL_CMD, InterfaceConfigConstants.STATIC_LAN_COUNT_PER_VC_CMD, InterfaceConfigConstants.STATIC_LAN_INCR_PER_VC_VLAN_MODE_CMD, InterfaceConfigConstants.STATIC_LAN_INTERMEDIATE_OBJREF_CMD, InterfaceConfigConstants.STATIC_LAN_MAC_RANGE_MODE_CMD, InterfaceConfigConstants.STATIC_LAN_NUMBER_OF_VCS_CMD, InterfaceConfigConstants.STATIC_LAN_RANGE_COUNT_CMD, InterfaceConfigConstants.STATIC_LAN_SKIP_VLAN_ID_ZERO_CMD, InterfaceConfigConstants.STATIC_LAN_TPID_CMD, InterfaceConfigConstants.STATIC_LAN_VLAN_PRIORITY_CMD, InterfaceConfigConstants.STATIC_LAN_VLAN_STACK_COUNT_CMD, InterfaceConfigConstants.STATIC_MAC_DST_CMD, InterfaceConfigConstants.STATIC_MAC_DST_COUNT_CMD, InterfaceConfigConstants.STATIC_MAC_DST_COUNT_STEP_CMD, InterfaceConfigConstants.STATIC_MAC_DST_MODE_CMD, InterfaceConfigConstants.STATIC_MAC_DST_STEP_CMD, InterfaceConfigConstants.STATIC_PVC_COUNT_CMD, InterfaceConfigConstants.STATIC_PVC_COUNT_STEP_CMD, InterfaceConfigConstants.STATIC_RANGE_PER_SPOKE_CMD, InterfaceConfigConstants.STATIC_SITE_ID_CMD, InterfaceConfigConstants.STATIC_SITE_ID_ENABLE_CMD, InterfaceConfigConstants.STATIC_SITE_ID_STEP_CMD, InterfaceConfigConstants.STATIC_VCI_CMD, InterfaceConfigConstants.STATIC_VCI_INCREMENT_CMD, InterfaceConfigConstants.STATIC_VCI_INCREMENT_STEP_CMD, InterfaceConfigConstants.STATIC_VCI_STEP_CMD, InterfaceConfigConstants.STATIC_VLAN_ENABLE_CMD, InterfaceConfigConstants.STATIC_VLAN_ID_CMD, InterfaceConfigConstants.STATIC_VLAN_ID_MODE_CMD, InterfaceConfigConstants.STATIC_VLAN_ID_STEP_CMD, InterfaceConfigConstants.STATIC_VPI_CMD, InterfaceConfigConstants.STATIC_VPI_INCREMENT_CMD, InterfaceConfigConstants.STATIC_VPI_INCREMENT_STEP_CMD, InterfaceConfigConstants.STATIC_VPI_STEP_CMD, InterfaceConfigConstants.TARGET_LINK_LAYER_ADDRESS_CMD, InterfaceConfigConstants.TRANSMIT_CLOCK_SOURCE_CMD, InterfaceConfigConstants.TRANSMIT_MODE_CMD, InterfaceConfigConstants.TX_C2_CMD, InterfaceConfigConstants.TX_FCS_CMD, InterfaceConfigConstants.TX_GAP_CONTROL_MODE_CMD, InterfaceConfigConstants.TX_IGNORE_RX_LINK_FAULTS_CMD, InterfaceConfigConstants.TX_LANES_CMD, InterfaceConfigConstants.TX_RX_SYNC_STATS_ENABLE_CMD, InterfaceConfigConstants.TX_RX_SYNC_STATS_INTERVAL_CMD, InterfaceConfigConstants.TX_SCRAMBLING_CMD, InterfaceConfigConstants.TYPE_A_ORDERED_SETS_CMD, InterfaceConfigConstants.TYPE_B_ORDERED_SETS_CMD, InterfaceConfigConstants.USE_VPN_PARAMETERS_CMD, InterfaceConfigConstants.VCI_CMD, InterfaceConfigConstants.VCI_COUNT_CMD, InterfaceConfigConstants.VCI_STEP_CMD, InterfaceConfigConstants.VLAN_CMD, InterfaceConfigConstants.VLAN_ID_CMD, InterfaceConfigConstants.VLAN_ID_COUNT_CMD, InterfaceConfigConstants.VLAN_ID_INNER_CMD, InterfaceConfigConstants.VLAN_ID_INNER_COUNT_CMD, InterfaceConfigConstants.VLAN_ID_INNER_MODE_CMD, InterfaceConfigConstants.VLAN_ID_INNER_STEP_CMD, InterfaceConfigConstants.VLAN_ID_LIST_CMD, InterfaceConfigConstants.VLAN_ID_MODE_CMD, InterfaceConfigConstants.VLAN_ID_STEP_CMD, InterfaceConfigConstants.VLAN_PROTOCOL_ID_CMD, InterfaceConfigConstants.VLAN_TPID_CMD, InterfaceConfigConstants.VLAN_USER_PRIORITY_CMD, InterfaceConfigConstants.VLAN_USER_PRIORITY_STEP_CMD, InterfaceConfigConstants.VPI_CMD, InterfaceConfigConstants.VPI_COUNT_CMD, InterfaceConfigConstants.VPI_STEP_CMD}
