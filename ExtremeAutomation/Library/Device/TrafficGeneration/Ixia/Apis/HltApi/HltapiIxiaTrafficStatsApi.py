from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficStatsApi import TrafficStatsApi, TrafficStatsConstants

"""
    This is the API class for the command: traffic_stats

    Class is auto-generated. If you update anything here,
        it will be over written.
"""


class IxiaTrafficStatsApi(TrafficStatsApi):

    """
    init function
    """
    def __init__(self, device):
        super(IxiaTrafficStatsApi, self).__init__(device)

    """
    This is the "One Large Method" for the command: traffic_stats
    use this by passing in a dict() of all the commands

        api = device.getApi(TrafficStatsConstants.TRAFFIC_STATS_API)
        api.traffic_stats(dummyDict)
    """
    def traffic_stats(self, argdictionary):
        return super(IxiaTrafficStatsApi, self).traffic_stats(argdictionary, self.supportedIxiaHltapiCommands)

    """
    Individual commands for each option. Typically, the "One Large Method"
    is the one that you want to be using so look at that example above
    """
    def traffic_stats_atm_counter_vci_data_item_list(self, any):
        """
        This is the method the command: traffic_stats option atm_counter_vci_data_item_list
        Description:If the -atm_counter_vci_type option is set to table, this list is used for the set of values (default ''). Valid only for traffic_generator ixos.
        Constants Available: ATM_COUNTER_VCI_DATA_ITEM_LIST_CMD
        Supported:IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.traffic_stats({TrafficStatsConstants.ATM_COUNTER_VCI_DATA_ITEM_LIST_CMD : any})

    def traffic_stats_atm_counter_vci_mode(self, opt):
        """
        This is the method the command: traffic_stats option atm_counter_vci_mode
        Description:If the -atm_counter_vpi_type option is set to counter, this indicates what counter mode should be used (default incr). Valid only for traffic_generator ixos.
        Constants Available: ATM_COUNTER_VCI_MODE_CMD
        Supported:IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.traffic_stats({TrafficStatsConstants.ATM_COUNTER_VCI_MODE_CMD : opt})

    def traffic_stats_atm_counter_vci_type(self, opt):
        """
        This is the method the command: traffic_stats option atm_counter_vci_type
        Description:The type of counter to use on the vci (default fixed). Currently only fixed, counter, and table are supported. Valid only for traffic_generator ixos.
        Constants Available: ATM_COUNTER_VCI_TYPE_CMD
        Supported:IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.traffic_stats({TrafficStatsConstants.ATM_COUNTER_VCI_TYPE_CMD : opt})

    def traffic_stats_atm_counter_vpi_data_item_list(self, any):
        """
        This is the method the command: traffic_stats option atm_counter_vpi_data_item_list
        Description:If the -atm_counter_vpi_type option is set to table, this list is used for the set of values (default ''). Valid only for traffic_generator ixos.
        Constants Available: ATM_COUNTER_VPI_DATA_ITEM_LIST_CMD
        Supported:IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.traffic_stats({TrafficStatsConstants.ATM_COUNTER_VPI_DATA_ITEM_LIST_CMD : any})

    def traffic_stats_atm_counter_vpi_mode(self, opt):
        """
        This is the method the command: traffic_stats option atm_counter_vpi_mode
        Description:If the -atm_counter_vci_type option is set to counter, this indicates what counter mode should be used (default incr). Currently only the incr and decr mode are supported. Valid only for traffic_generator ixos.
        Constants Available: ATM_COUNTER_VPI_MODE_CMD
        Supported:IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.traffic_stats({TrafficStatsConstants.ATM_COUNTER_VPI_MODE_CMD : opt})

    def traffic_stats_atm_counter_vpi_type(self, opt):
        """
        This is the method the command: traffic_stats option atm_counter_vpi_type
        Description:The type of counter to use on the vpi (default fixed). Currently only fixed, counter, and table are supported. Valid only for traffic_generator ixos.
        Constants Available: ATM_COUNTER_VPI_TYPE_CMD
        Supported:IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.traffic_stats({TrafficStatsConstants.ATM_COUNTER_VPI_TYPE_CMD : opt})

    def traffic_stats_atm_reassembly_enable_ip_qos(self, bool_opt):
        """
        This is the method the command: traffic_stats option atm_reassembly_enable_ip_qos
        Description:Enables the collection of QoS statistics for packets that match this vpi/vci (default 1). Valid only for traffic_generator ixos.
        Constants Available: ATM_REASSEMBLY_ENABLE_IP_QOS_CMD
        Supported:IxOS/IxNetwork-FT
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.traffic_stats({TrafficStatsConstants.ATM_REASSEMBLY_ENABLE_IP_QOS_CMD : bool_opt})

    def traffic_stats_atm_reassembly_enable_iptcpudp_checksum(self, opt):
        """
        This is the method the command: traffic_stats option atm_reassembly_enable_iptcpudp_checksum
        Description:Enables the collection of TCP and UDP checksum statistics for packets that match this vpi/vci (default 1). Valid only for traffic_generator ixos.
        Constants Available: ATM_REASSEMBLY_ENABLE_IPTCPUDP_CHECKSUM_CMD
        Supported:IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.traffic_stats({TrafficStatsConstants.ATM_REASSEMBLY_ENABLE_IPTCPUDP_CHECKSUM_CMD : opt})

    def traffic_stats_atm_reassembly_encapsulation(self, opt):
        """
        This is the method the command: traffic_stats option atm_reassembly_encapsulation
        Description:The decode encapsulation to be used on received data when the port is in packet group mode. This is the only means by which the encapsulation may be set (default llc_routed_clip). Valid only for traffic_generator ixos.
        Constants Available: ATM_REASSEMBLY_ENCAPSULATION_CMD
        Supported:IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.traffic_stats({TrafficStatsConstants.ATM_REASSEMBLY_ENCAPSULATION_CMD : opt})

    def traffic_stats_csv_path(self, any):
        """
        This is the method the command: traffic_stats option csv_path
        Description:This parameter represents the path for the generated CSV files. This parameter is used for Unix environments only, and the path to the directory should be absolute (eg. /home/user/folder). If -return_method is different from csv, the csv files are created temporarily, for parsing the statistics. After the parsing, these csv files are deleted. In case the csv_path is omitted or the user doesn't havewriting permission on the directory, the csv files will be created in the currentdirectory if possible, otherwise the /tmp directory will be used.
        Constants Available: CSV_PATH_CMD
        Supported:IxNetwork
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.traffic_stats({TrafficStatsConstants.CSV_PATH_CMD : any})

    def traffic_stats_drill_down_flow(self, any):
        """
        This is the method the command: traffic_stats option drill_down_flow
        Description:The Application flow for which the drill down stats have to retreived.
        Constants Available: DRILL_DOWN_FLOW_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.traffic_stats({TrafficStatsConstants.DRILL_DOWN_FLOW_CMD : any})

    def traffic_stats_drill_down_listening_port(self, numeric):
        """
        This is the method the command: traffic_stats option drill_down_listening_port
        Description:Drill down listening port. Needed only when drill_down_type is per_responder_port or per_listening_ports_per_responder_port
        Constants Available: DRILL_DOWN_LISTENING_PORT_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.traffic_stats({TrafficStatsConstants.DRILL_DOWN_LISTENING_PORT_CMD : numeric})

    def traffic_stats_drill_down_port(self, any):
        """
        This is the method the command: traffic_stats option drill_down_port
        Description:The port for which the drill down stats have to retreived.
        Constants Available: DRILL_DOWN_PORT_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.traffic_stats({TrafficStatsConstants.DRILL_DOWN_PORT_CMD : any})

    def traffic_stats_drill_down_traffic_item(self, any):
        """
        This is the method the command: traffic_stats option drill_down_traffic_item
        Description:The traffic item for which the drill down stats have to retreived..
        Constants Available: DRILL_DOWN_TRAFFIC_ITEM_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.traffic_stats({TrafficStatsConstants.DRILL_DOWN_TRAFFIC_ITEM_CMD : any})

    def traffic_stats_drill_down_type(self, opt):
        """
        This is the method the command: traffic_stats option drill_down_type
        Description:Type of drill down statistics to be collected for AppLib traffic.
            Valid choices are:
            Valid option     Description     Required Handle(s)     Supported in combination with -mode
            per_ips     Retrieve per ip stats.     drill_down_traffic_item     L47_traffic_item, L47_traffic_item_tcp
            per_ports     Retrieve per port stats.     drill_down_traffic_item     L47_traffic_item, L47_traffic_item_tcp
            per_initiator_flows     Retrieve per initiator flow stats.     drill_down_traffic_item     L47_traffic_item, L47_traffic_item_tcp
            per_responder_flows     Retrieve per responder flow stats.     drill_down_traffic_item     L47_traffic_item, L47_traffic_item_tcp
            per_initiator_ports     Retrieve per initiator port stats.     drill_down_traffic_item     L47_flow_initiator, L47_flow_initiator_tcp
            per_responder_ports     Retrieve per responder port stats.     drill_down_traffic_item     L47_flow_responder, L47_listening_port_tcp
            per_initiator_ips     Retrieve per initiator ip stats.     drill_down_flow, drill_down_traffic_item     L47_flow_initiator, L47_flow_initiator_tcp
            per_responder_ips     Retrieve per responder ip stats.     drill_down_flow, drill_down_traffic_item     L47_flow_responder, L47_listening_port_tcp
            per_ports_per_initiator_flows     Retrieve per initiator flow stats of the given port.     drill_down_port, drill_down_traffic_item     L47_traffic_item, L47_traffic_item_tcp
            per_ports_per_responder_flows     Retrieve per responder flow stats of the given port.     drill_down_port, drill_down_traffic_item     L47_traffic_item, L47_traffic_item_tcp
            per_ports_per_initiator_ips     Retrieve per initiator ip stats of the given port.     drill_down_port, drill_down_traffic_item     L47_traffic_item, L47_traffic_item_tcp
            per_ports_per_responder_ips     Retrieve per responder ip stats of the given port.     drill_down_port, drill_down_traffic_item     L47_traffic_item, L47_traffic_item_tcp
            per_initiator_flows_per_initiator_ports     Retrieve per initiator port stats of given initiator flow.     drill_down_flow, drill_down_traffic_item     L47_traffic_item, L47_traffic_item_tcp
            per_responder_flows_per_responder_ports     Retrieve per responder port stats of given responder flow.     drill_down_flow, drill_down_traffic_item     L47_traffic_item, L47_traffic_item_tcp
            per_initiator_flows_per_initiator_ips     per initiator ip stats of given initiator flow.     drill_down_flow, drill_down_traffic_item     L47_traffic_item, L47_traffic_item_tcp
            per_responder_flows_per_responder_ips     Retrieve per responder ip stats of given responder flow.     drill_down_flow, drill_down_traffic_item     L47_traffic_item, L47_traffic_item_tcp
            per_initiator_ports_per_initiator_ips     Retrieve per initiator ip stats of the given initiator port.     drill_down_flow, drill_down_port, drill_down_traffic_item     L47_flow_initiator, L47_flow_initiator_tcp
            per_responder_ports_per_responder_ips     Retrieve per responder ip stats of the given responder port.     drill_down_flow, drill_down_port, drill_down_traffic_item     L47_flow_responder, L47_listening_port_tcp
            per_ports_per_initiator_flows_per_initiator_ips     Retrieve per initiator ip stats of given initiator flow of given port..     drill_down_flow, drill_down_port, drill_down_traffic_item     L47_traffic_item, L47_traffic_item_tcp
            per_ports_per_responder_flows_per_responder_ips     Retrieve per responder ip stats of given responder flow of given port.     drill_down_flow, drill_down_port, drill_down_traffic_item     L47_traffic_item, L47_traffic_item_tcp
            per_initiator_flows_per_initiator_ports_per_initiator_ips     Retrieve per initiator ip stats of given initiator flow and initiator port.     drill_down_flow, drill_down_port, drill_down_traffic_item     L47_traffic_item, L47_traffic_item_tcp
            per_responder_flows_per_responder_ports_per_responder_ips     Retrieve per responder ip stats of given responder flow and responder port.     drill_down_flow, drill_down_port, drill_down_traffic_item     L47_traffic_item, L47_traffic_item_tcp
            DEPENDENCIESValid in combination with parameter(s)
            'mode = L47_traffic_item, L47_flow_initiator, L47_flow_responder, L47_traffic_item_tcp, L47_flow_initiator_tcp or L47_listening_port_tcp. 'drill_down_flow' with valid options 'drill_down_port' with valid options 'drill_down_traffic_item' with valid option' | value= '1' |
        Constants Available: DRILL_DOWN_TYPE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.traffic_stats({TrafficStatsConstants.DRILL_DOWN_TYPE_CMD : opt})

    def traffic_stats_egress_mode(self, opt):
        """
        This is the method the command: traffic_stats option egress_mode
        Description:When -mode is egress_by_flow or egress_by_port the statistics can be collected in two ways: conditional or paged. When using conditional, the advantage is that it will return egress statistics only for the rows for which it received values, the disadvantage is that retrieving conditional stats is slower. When using paged mode the advantage is that it's faster (an optimal number of rows per page will be auto configured) but the disadvantage is that it will retrieve statistics for all the egress values that are expected even if nothing was received for a certain egress value. For example: if egress tracking was configured to outer_vlan_id_4 but only 2 values were received, the conditional mode will return 2 separate egress values while the paged mode will return 15 values.When to use egress_mode conditional: when the number of possible egress tracking values is very big but the actual number of egress values is small (e.g. outer_vlan_id_12 and the values received are 1, 10 and 4000).When to use egress_mode paged:Scalability, when the number of expected egress values is big (many ingress flows each having multiple egress flows)When the number of possible egress values is small (inner_vlan_priority has a total number of 7 flows)Valid only for traffic_generator ixnetwork_540.
        Constants Available: EGRESS_MODE_CMD
        Supported:IxNetwork
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.traffic_stats({TrafficStatsConstants.EGRESS_MODE_CMD : opt})

    def traffic_stats_egress_stats_list(self, any):
        """
        This is the method the command: traffic_stats option egress_stats_list
        Description:This parameter is valid only for custom egress views only. Using this parameter, the user can select a list. Valid only for traffic_generator ixnetwork_540.
            Valid options are:
            tx.total_pkts: Tx Frames
            rx.expected_pkts: Rx Expected Frames
            rx.total_pkts: Rx Frames
            rx.loss_pkts: Frames Delta
            rx.loss_percent: Loss %
            rx.pkt_loss_duration: Packet Loss Duration (ms)
            tx.total_pkt_rate: Tx Frame Rate
            rx.total_pkt_rate: Rx Frame Rate
            rx.total_pkts_bytes: Rx Bytes
            tx.total_pkt_byte_rate: Tx Rate (Bps)
            rx.total_pkt_byte_rate: Rx Rate (Bps)
            tx.total_pkt_bit_rate: Tx Rate (bps)
            rx.total_pkt_bit_rate: Rx Rate (bps)
            tx.total_pkt_kbit_rate: Tx Rate (Kbps)
            rx.total_pkt_kbit_rate: Rx Rate (Kbps)
            tx.total_pkt_mbit_rate: Tx Rate (Mbps)
            rx.total_pkt_mbit_rate: Rx Rate (Mbps)
            rx.avg_delay: Store-Forward Avg Latency (ns)
            rx.min_delay: Store-Forward Min Latency (ns)
            rx.max_delay: Store-Forward Max Latency (ns)
            rx.first_tstamp: First Timestamp
            rx.last_tstamp: Last Timestamp
        Constants Available: EGRESS_STATS_LIST_CMD
        Supported:IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.traffic_stats({TrafficStatsConstants.EGRESS_STATS_LIST_CMD : any})

    def traffic_stats_ignore_rate(self, bool_opt):
        """
        This is the method the command: traffic_stats option ignore_rate
        Description:When getting aggregate statistics and this is set to 1, the rate values will not be returned. This will save time on the call as gathering rate stats requires a 700 ms wait in the call. Valid only for traffic_generator ixos.
        Constants Available: IGNORE_RATE_CMD
        Supported:IxOS/IxNetwork-FT
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.traffic_stats({TrafficStatsConstants.IGNORE_RATE_CMD : bool_opt})

    def traffic_stats_measure_mode(self, opt):
        """
        This is the method the command: traffic_stats option measure_mode
        Description:This sets the measuring mode for traffic stats in IxNetwork. The returned statistics will be in accord with this value. If this parameter is not present, the measure mode is not changed from the current value in IxNetwork. Valid only for traffic_generator ixnetwork_540
        Constants Available: MEASURE_MODE_CMD
        Supported:IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.traffic_stats({TrafficStatsConstants.MEASURE_MODE_CMD : opt})

    def traffic_stats_packet_group_id(self, any):
        """
        This is the method the command: traffic_stats option packet_group_id
        Description:Given a packet group ID, returns the statistics for all packet group ids from 0 to this value. It also support a range. For example 7-9 means that return statistics for groups 7, 8 and 9. Valid only for traffic_generator ixos.
        Constants Available: PACKET_GROUP_ID_CMD
        Supported:IxNetwork
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.traffic_stats({TrafficStatsConstants.PACKET_GROUP_ID_CMD : any})

    def traffic_stats_previous_data(self, opt):
        """
        This is the method the command: traffic_stats option previous_data
        Description:If this parameter is given with the reset value allthe arrays that were previously allocated will be erased.Valid only for traffic_generator ixnetwork_540.
        Constants Available: PREVIOUS_DATA_CMD
        Supported:IxNetwork
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.traffic_stats({TrafficStatsConstants.PREVIOUS_DATA_CMD : opt})

    def traffic_stats_qos_stats(self, any):
        """
        This is the method the command: traffic_stats option qos_stats
        Description:and Count, inclusive. Valid only for traffic_generator ixos.
        Constants Available: QOS_STATS_CMD
        Supported:IxNetwork
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.traffic_stats({TrafficStatsConstants.QOS_STATS_CMD : any})

    def traffic_stats_return_method(self, opt):
        """
        This is the method the command: traffic_stats option return_method
        Description:Valid options are:
            keyed_list (default): always return the stat values as a keyed list, no matter how long it takes.
            keyed_list_or_array: when more than 2000 statistics values need to be retrieved, the key handle will be returned instead of all the keyed list items specified in the section dedicated for returned values. This key, handle, represents the name of the array to be used for reading the stats. This key is returned when more than 2000 statistics values need to be retrieved. The indices of this array are the keys that you'll find explained in the returned values section, and the values are the statistics values. This method has been introduced to increase performance when returning and reading stats. Returning a huge list in the tcl console can make the console hang.
            array: the key handle will be returned instead of all the keyed list items specified in the section dedicated for returned values. This key, handle, represents the name of the array to be used for reading the stats. The indices of this array are the keys that you'll find explained in the returned values section, and the values are the statistics values. This method has been introduced to increase performance when returning and reading stats. Returning a huge list in the tcl console can make the console hang.
            csv: only returns a path to the csv file containing the statsOnly valid if $::<namespace>::snapshot_stats == 1 (Ixia.tcl), otherwise -return_method defaults to keyed_list. Parameter -mode must be different than all, otherwise it defaults on aggregate. This option is available only when mode is aggregate, all, data_plane_port, flow,per_port_flows, stream, streams, traffic_item, l23_test_summary, egress_by_flow, egress_by_port, user_defined_stats and for L47 Application Traffic (application_FTP, application_HTTP, etc).Valid for traffic_generator ixos/ixnetwork/ixnetwork_540.
        Constants Available: RETURN_METHOD_CMD
        Supported:IxNetwork
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.traffic_stats({TrafficStatsConstants.RETURN_METHOD_CMD : opt})

    def traffic_stats_traffic_generator(self, opt):
        """
        This is the method the command: traffic_stats option traffic_generator
        Description:The Ixia product that was used for configuring traffic.ixos - The traffic was generated using IxOS and will be used further also with IxOS.ixnetwork - The traffic was generated using IxNetwork and will be used further also with IxNetwork. This option is valid only IxTclNetwork 5.30 or greater is loaded.ixnetwork_540 - The traffic was generated using IxNetwork and will be used further also with IxNetwork. This option is valid only IxTclNetwork 5.40 or greater is loaded.
        Constants Available: TRAFFIC_GENERATOR_CMD
        Supported:IxOs/IxNetwork-FT, IxNetwork
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.traffic_stats({TrafficStatsConstants.TRAFFIC_GENERATOR_CMD : opt})

    def traffic_stats_uds_action(self, opt):
        """
        This is the method the command: traffic_stats option uds_action
        Description:This parameter is valid for traffic_generator ixnetwork_540, mode user_defined_stats. This parameter is valid for IxTclNetwork 5.40+ API. Available starting with HLT API 3.80.
            Valid options are:
            get_available_port_filters: returns the available port filters that can be applied for filtering traffic
            statisticsget_available_protocol_stack_filters: returns the available protocol stack filters (PPP ranges, L2TP ranges etc) that can be applied for filtering traffic
            statisticsget_available_statistic_filters: returns the available statistic filters (Tx Frames, Rx Frames etc) that can be applied for filtering traffic
            statisticsget_available_stats: returns the available statistic names (Tx Frames, Rx Frames etc) that can be retrieved for a specified user defined statistic
            typeget_available_traffic_item_filters: returns the available traffic item filters that can be applied for filtering traffic
            statisticsget_available_tracking_filters:  returns the available tracking filters that can be applied for filtering traffic statistics. The list of tracking filters should contain the tracked fields when configuring traffic.
            get_stats: (DEFAULT), returns the statistics values. When retrieving stats, filters can be applied depending on the uds_type parameter. If no filter is provided by the user, then all possible and available filters are applied.
        Constants Available: UDS_ACTION_CMD
        Supported:IxNetwork
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.traffic_stats({TrafficStatsConstants.UDS_ACTION_CMD : opt})

    def traffic_stats_uds_l23ps_drilldown(self, opt):
        """
        This is the method the command: traffic_stats option uds_l23ps_drilldown
        Description:This parameter is valid for traffic_generator ixnetwork_540, mode user_defined_stats, uds_type l23_protocol_stack. This parameter is valid for IxTclNetwork 5.40+ API. Available starting with HLT API 3.80. per_session - (DEFAULT), retrieves per session protocol stack statisticsper_range - retrieves per range protocol stack statistics
        Constants Available: UDS_L23PS_DRILLDOWN_CMD
        Supported:IxNetwork
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.traffic_stats({TrafficStatsConstants.UDS_L23PS_DRILLDOWN_CMD : opt})

    def traffic_stats_uds_l23ps_num_results(self, numeric):
        """
        This is the method the command: traffic_stats option uds_l23ps_num_results
        Description:This parameter is valid for traffic_generator ixnetwork_540, mode user_defined_stats, uds_type l23_protocol_stack. This parameter is valid for IxTclNetwork 5.40+ API. Available starting with HLT API 3.80. This parameter indicates the number of results per page to be retrieved in teh corresponding user defined statistics view.
        Constants Available: UDS_L23PS_NUM_RESULTS_CMD
        Supported:IxNetwork
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.traffic_stats({TrafficStatsConstants.UDS_L23PS_NUM_RESULTS_CMD : numeric})

    def traffic_stats_uds_l23ps_sorting_statistic(self, any):
        """
        This is the method the command: traffic_stats option uds_l23ps_sorting_statistic
        Description:This parameter is valid for traffic_generator ixnetwork_540, mode user_defined_stats, uds_type l23_protocol_stack. This parameter is valid for IxTclNetwork 5.40+ API. Available starting with HLT API 3.80. This parameter indicates the statistic to use for sorting the results.
        Constants Available: UDS_L23PS_SORTING_STATISTIC_CMD
        Supported:IxNetwork
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.traffic_stats({TrafficStatsConstants.UDS_L23PS_SORTING_STATISTIC_CMD : any})

    def traffic_stats_uds_l23ps_sorting_type(self, opt):
        """
        This is the method the command: traffic_stats option uds_l23ps_sorting_type
        Description:This parameter is valid for traffic_generator ixnetwork_540, mode user_defined_stats, uds_type l23_protocol_stack. This parameter is valid for IxTclNetwork 5.40+ API. Available starting with HLT API 3.80. This parameter indicates the sorting type: ascending or decending, for the uds_l23ps_sorting_statistic parameter.
        Constants Available: UDS_L23PS_SORTING_TYPE_CMD
        Supported:IxNetwork
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.traffic_stats({TrafficStatsConstants.UDS_L23PS_SORTING_TYPE_CMD : opt})

    def traffic_stats_uds_l23tf_aggregated_across_ports(self, bool_opt):
        """
        This is the method the command: traffic_stats option uds_l23tf_aggregated_across_ports
        Description:This parameter is valid for traffic_generator ixnetwork_540, mode user_defined_stats, uds_type l23_traffic_flow. This parameter is valid for IxTclNetwork 5.40+ API. Available starting with HLT API 3.80. When retrieving traffic flow statistics, this parameter indicates whether the flows should be aggregated across ports or not.
        Constants Available: UDS_L23TF_AGGREGATED_ACROSS_PORTS_CMD
        Supported:IxNetwork
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.traffic_stats({TrafficStatsConstants.UDS_L23TF_AGGREGATED_ACROSS_PORTS_CMD : bool_opt})

    def traffic_stats_uds_l23tf_egress_latency_bin_display(self, opt):
        """
        This is the method the command: traffic_stats option uds_l23tf_egress_latency_bin_display
        Description:This parameter is valid for traffic_generator ixnetwork_540, mode user_defined_stats, uds_type l23_traffic_flow. This parameter is valid for IxTclNetwork 5.40+ API. Available starting with HLT API 3.80. Determines what type of latency statistics should be inluded in the list of retrieved statistics. none - no latency statistics are includedshow_egress_flat_view - egress flat view statistics are includedshow_egress_rows - egress statistics are includedshow_latency_bin_stats - latency bin statistics are included
        Constants Available: UDS_L23TF_EGRESS_LATENCY_BIN_DISPLAY_CMD
        Supported:IxNetwork
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.traffic_stats({TrafficStatsConstants.UDS_L23TF_EGRESS_LATENCY_BIN_DISPLAY_CMD : opt})

    def traffic_stats_uds_l23tf_enumeration_sorting_type(self, opt):
        """
        This is the method the command: traffic_stats option uds_l23tf_enumeration_sorting_type
        Description:This parameter is valid for traffic_generator ixnetwork_540, mode user_defined_stats, uds_type l23_traffic_flow, uds_l23tf_filter_type enumeration, uds_tracking_filter should be present. This parameter is valid for IxTclNetwork 5.40+ API. Available starting with HLT API 3.80. This parameter accepts a list of values, exactly like uds_l23tf_filter_type parameter. If the corresponding index of uds_l23tf_filter_type has the value tracking, then this parameter's value should be null. ascending - the sorting for the enumeration filter is ascendingdescending - the sorting for the enumeration filter is descendingnull - used when uds_l23tf_filter_type is tracking
        Constants Available: UDS_L23TF_ENUMERATION_SORTING_TYPE_CMD
        Supported:IxNetwork
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.traffic_stats({TrafficStatsConstants.UDS_L23TF_ENUMERATION_SORTING_TYPE_CMD : opt})

    def traffic_stats_uds_l23tf_filter_type(self, opt):
        """
        This is the method the command: traffic_stats option uds_l23tf_filter_type
        Description:This parameter is valid for traffic_generator ixnetwork_540, mode user_defined_stats, uds_type l23_traffic_flow, uds_tracking_filter should be present. This parameter is valid for IxTclNetwork 5.40+ API. Available starting with HLT API 3.80. The traffic flow filter type: enumeration or tracking.
        Constants Available: UDS_L23TF_FILTER_TYPE_CMD
        Supported:IxNetwork
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.traffic_stats({TrafficStatsConstants.UDS_L23TF_FILTER_TYPE_CMD : opt})

    def traffic_stats_uds_l23tf_tracking_operator(self, opt):
        """
        This is the method the command: traffic_stats option uds_l23tf_tracking_operator
        Description:This parameter is valid for traffic_generator ixnetwork_540, mode user_defined_stats, uds_type l23_traffic_flow, uds_tracking_filter should be present. This parameter is valid for IxTclNetwork 5.40+ API. Available starting with HLT API 3.80. The uds_tracking_filter parameter is provided with a list of fields that are used for filtering. An operator and a value are applied on the specified field. This parameter specifies the operator that is applied: is_any_of is_different is_equal is_equal_or_greater is_equal_or_smaller is_greater is_in_any_range is_none_of is_smaller null.
        Constants Available: UDS_L23TF_TRACKING_OPERATOR_CMD
        Supported:IxNetwork
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.traffic_stats({TrafficStatsConstants.UDS_L23TF_TRACKING_OPERATOR_CMD : opt})

    def traffic_stats_uds_l23tf_tracking_value(self, any):
        """
        This is the method the command: traffic_stats option uds_l23tf_tracking_value
        Description:This parameter is valid for traffic_generator ixnetwork_540, mode user_defined_stats, uds_type l23_traffic_flow, uds_tracking_filter should be present. This parameter is valid for IxTclNetwork 5.40+ API. Available starting with HLT API 3.80. The uds_tracking_filter parameter is provided with a list of fields that are used for filtering. An operator and a value are applied on the specified field. This parameter specifies the value that is used for comparison.
        Constants Available: UDS_L23TF_TRACKING_VALUE_CMD
        Supported:IxNetwork
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.traffic_stats({TrafficStatsConstants.UDS_L23TF_TRACKING_VALUE_CMD : any})

    def traffic_stats_uds_l23tfd_dead_flows_treshold(self, numeric):
        """
        This is the method the command: traffic_stats option uds_l23tfd_dead_flows_treshold
        Description:This parameter is valid for traffic_generator ixnetwork_540, mode user_defined_stats, uds_type l23_traffic_flow_detective. This parameter is valid for IxTclNetwork 5.40+ API. Available starting with HLT API 3.80.
        Constants Available: UDS_L23TFD_DEAD_FLOWS_TRESHOLD_CMD
        Supported:IxNetwork
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.traffic_stats({TrafficStatsConstants.UDS_L23TFD_DEAD_FLOWS_TRESHOLD_CMD : numeric})

    def traffic_stats_uds_l23tfd_flow_type(self, opt):
        """
        This is the method the command: traffic_stats option uds_l23tfd_flow_type
        Description:This parameter is valid for traffic_generator ixnetwork_540, mode user_defined_stats, uds_type l23_traffic_flow_detective. This parameter is valid for IxTclNetwork 5.40+ API. all_flows - retrieved stats are for all flowslive_flows - retrieved stats are for live flowsdead_flows - retrieved stats are for dead flows
        Constants Available: UDS_L23TFD_FLOW_TYPE_CMD
        Supported:IxNetwork
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.traffic_stats({TrafficStatsConstants.UDS_L23TFD_FLOW_TYPE_CMD : opt})

    def traffic_stats_uds_l23tfd_show_egress_flows(self, bool_opt):
        """
        This is the method the command: traffic_stats option uds_l23tfd_show_egress_flows
        Description:Display the egress flows similar to a Flat Egress view. Using this option will ease the visualisation of failed flows.Valid only for traffic_generator ixnetwork_540.
        Constants Available: UDS_L23TFD_SHOW_EGRESS_FLOWS_CMD
        Supported:IxNetwork
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.traffic_stats({TrafficStatsConstants.UDS_L23TFD_SHOW_EGRESS_FLOWS_CMD : bool_opt})

    def traffic_stats_uds_l23tfd_statistic_all_flows_num_results(self, numeric):
        """
        This is the method the command: traffic_stats option uds_l23tfd_statistic_all_flows_num_results
        Description:This parameter is valid for traffic_generator ixnetwork_540, mode user_defined_stats, uds_type l23_traffic_flow_detective, uds_statistic_filter should be present. This parameter is valid for IxTclNetwork 5.40+ API. Available starting with HLT API 3.80. This parameter specifies the number of results to be displayed per page in the statistic view that is created.
        Constants Available: UDS_L23TFD_STATISTIC_ALL_FLOWS_NUM_RESULTS_CMD
        Supported:IxNetwork
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.traffic_stats({TrafficStatsConstants.UDS_L23TFD_STATISTIC_ALL_FLOWS_NUM_RESULTS_CMD : numeric})

    def traffic_stats_uds_l23tfd_statistic_all_flows_sort_by(self, any):
        """
        This is the method the command: traffic_stats option uds_l23tfd_statistic_all_flows_sort_by
        Description:This parameter is valid for traffic_generator ixnetwork_540, mode user_defined_stats, uds_type l23_traffic_flow_detective, uds_statistic_filter should be present. This parameter is valid for IxTclNetwork 5.40+ API. Available starting with HLT API 3.80. This parameter specifies the field by which the statistics are sorted.
        Constants Available: UDS_L23TFD_STATISTIC_ALL_FLOWS_SORT_BY_CMD
        Supported:IxNetwork
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.traffic_stats({TrafficStatsConstants.UDS_L23TFD_STATISTIC_ALL_FLOWS_SORT_BY_CMD : any})

    def traffic_stats_uds_l23tfd_statistic_all_flows_sorting_type(self, opt):
        """
        This is the method the command: traffic_stats option uds_l23tfd_statistic_all_flows_sorting_type
        Description:This parameter is valid for traffic_generator ixnetwork_540, mode user_defined_stats, uds_type l23_traffic_flow_detective, uds_statistic_filter should be present. This parameter is valid for IxTclNetwork 5.40+ API. Available starting with HLT API 3.80. This parameter specifies the type of sorting for the statistics. ascending - sort statistics in ascending orderdescending - sort statistics in descending orderworst_performers - sort statistics by worst performersbest_performers - sort statistics by best performers
        Constants Available: UDS_L23TFD_STATISTIC_ALL_FLOWS_SORTING_TYPE_CMD
        Supported:IxNetwork
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.traffic_stats({TrafficStatsConstants.UDS_L23TFD_STATISTIC_ALL_FLOWS_SORTING_TYPE_CMD : opt})

    def traffic_stats_uds_l23tfd_statistic_dead_flows_num_results(self, numeric):
        """
        This is the method the command: traffic_stats option uds_l23tfd_statistic_dead_flows_num_results
        Description:This parameter is valid for traffic_generator ixnetwork_540, mode user_defined_stats, uds_type l23_traffic_flow_detective, uds_statistic_filter should be present. This parameter is valid for IxTclNetwork 5.40+ API. Available starting with HLT API 3.80. This parameter specifies the number of results to be displayed per page in the statistic view that is created.
        Constants Available: UDS_L23TFD_STATISTIC_DEAD_FLOWS_NUM_RESULTS_CMD
        Supported:IxNetwork
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.traffic_stats({TrafficStatsConstants.UDS_L23TFD_STATISTIC_DEAD_FLOWS_NUM_RESULTS_CMD : numeric})

    def traffic_stats_uds_l23tfd_statistic_dead_flows_sort_by(self, any):
        """
        This is the method the command: traffic_stats option uds_l23tfd_statistic_dead_flows_sort_by
        Description:This parameter is valid for traffic_generator ixnetwork_540, mode user_defined_stats, uds_type l23_traffic_flow_detective, uds_statistic_filter should be present. This parameter is valid for IxTclNetwork 5.40+ API. Available starting with HLT API 3.80. This parameter specifies the field by which the statistics are sorted.
        Constants Available: UDS_L23TFD_STATISTIC_DEAD_FLOWS_SORT_BY_CMD
        Supported:IxNetwork
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.traffic_stats({TrafficStatsConstants.UDS_L23TFD_STATISTIC_DEAD_FLOWS_SORT_BY_CMD : any})

    def traffic_stats_uds_l23tfd_statistic_dead_flows_sorting_type(self, opt):
        """
        This is the method the command: traffic_stats option uds_l23tfd_statistic_dead_flows_sorting_type
        Description:This parameter is valid for traffic_generator ixnetwork_540, mode user_defined_stats, uds_type l23_traffic_flow_detective, uds_statistic_filter should be present. This parameter is valid for IxTclNetwork 5.40+ API. Available starting with HLT API 3.80. This parameter specifies the type of sorting for the statistics. ascending - sort statistics in ascending orderdescending - sort statistics in descending orderworst_performers - sort statistics by worst performersbest_performers - sort statistics by best performers
        Constants Available: UDS_L23TFD_STATISTIC_DEAD_FLOWS_SORTING_TYPE_CMD
        Supported:IxNetwork
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.traffic_stats({TrafficStatsConstants.UDS_L23TFD_STATISTIC_DEAD_FLOWS_SORTING_TYPE_CMD : opt})

    def traffic_stats_uds_l23tfd_statistic_live_flows_num_results(self, numeric):
        """
        This is the method the command: traffic_stats option uds_l23tfd_statistic_live_flows_num_results
        Description:This parameter is valid for traffic_generator ixnetwork_540, mode user_defined_stats, uds_type l23_traffic_flow_detective, uds_statistic_filter should be present. This parameter is valid for IxTclNetwork 5.40+ API. Available starting with HLT API 3.80. This parameter specifies the number of results to be displayed per page in the statistic view that is created.
        Constants Available: UDS_L23TFD_STATISTIC_LIVE_FLOWS_NUM_RESULTS_CMD
        Supported:IxNetwork
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.traffic_stats({TrafficStatsConstants.UDS_L23TFD_STATISTIC_LIVE_FLOWS_NUM_RESULTS_CMD : numeric})

    def traffic_stats_uds_l23tfd_statistic_live_flows_sort_by(self, any):
        """
        This is the method the command: traffic_stats option uds_l23tfd_statistic_live_flows_sort_by
        Description:This parameter is valid for traffic_generator ixnetwork_540, mode user_defined_stats, uds_type l23_traffic_flow_detective, uds_statistic_filter should be present. This parameter is valid for IxTclNetwork 5.40+ API. Available starting with HLT API 3.80. This parameter specifies the field by which the statistics are sorted.
        Constants Available: UDS_L23TFD_STATISTIC_LIVE_FLOWS_SORT_BY_CMD
        Supported:IxNetwork
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.traffic_stats({TrafficStatsConstants.UDS_L23TFD_STATISTIC_LIVE_FLOWS_SORT_BY_CMD : any})

    def traffic_stats_uds_l23tfd_statistic_live_flows_sorting_type(self, opt):
        """
        This is the method the command: traffic_stats option uds_l23tfd_statistic_live_flows_sorting_type
        Description:This parameter is valid for traffic_generator ixnetwork_540, mode user_defined_stats, uds_type l23_traffic_flow_detective, uds_statistic_filter should be present. This parameter is valid for IxTclNetwork 5.40+ API. Available starting with HLT API 3.80. This parameter specifies the type of sorting for the statistics. ascending - sort statistics in ascending orderdescending - sort statistics in descending orderworst_performers - sort statistics by worst performersbest_performers - sort statistics by best performers
        Constants Available: UDS_L23TFD_STATISTIC_LIVE_FLOWS_SORTING_TYPE_CMD
        Supported:IxNetwork
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.traffic_stats({TrafficStatsConstants.UDS_L23TFD_STATISTIC_LIVE_FLOWS_SORTING_TYPE_CMD : opt})

    def traffic_stats_uds_l23tfd_statistic_operator(self, opt):
        """
        This is the method the command: traffic_stats option uds_l23tfd_statistic_operator
        Description:This parameter is valid for traffic_generator ixnetwork_540, mode user_defined_stats, uds_type l23_traffic_flow_detective, uds_statistic_filter should be present. This parameter is valid for IxTclNetwork 5.40+ API. Available starting with HLT API 3.80. The uds_statistic_filter parameter is provided with a list of fields that are used for filtering. An operator and a value are applied on the specified field. This parameter specifies the operator that is applied: is_different is_equal is_equal_or_greater is_equal_or_smaller is_greater is_smaller null.
        Constants Available: UDS_L23TFD_STATISTIC_OPERATOR_CMD
        Supported:IxNetwork
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.traffic_stats({TrafficStatsConstants.UDS_L23TFD_STATISTIC_OPERATOR_CMD : opt})

    def traffic_stats_uds_l23tfd_statistic_value(self, any):
        """
        This is the method the command: traffic_stats option uds_l23tfd_statistic_value
        Description:This parameter is valid for traffic_generator ixnetwork_540, mode user_defined_stats, uds_type l23_traffic_flow_detective, uds_statistic_filter should be present. This parameter is valid for IxTclNetwork 5.40+ API. Available starting with HLT API 3.80. The uds_statistic_filter parameter is provided with a list of fields that are used for filtering. An operator and a value are applied on the specified field. This parameter specifies the value that is used for comparison.
        Constants Available: UDS_L23TFD_STATISTIC_VALUE_CMD
        Supported:IxNetwork
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.traffic_stats({TrafficStatsConstants.UDS_L23TFD_STATISTIC_VALUE_CMD : any})

    def traffic_stats_uds_l23tfd_tracking_operator(self, opt):
        """
        This is the method the command: traffic_stats option uds_l23tfd_tracking_operator
        Description:mode user_defined_stats, uds_type l23_traffic_flow_detective, uds_tracking_filter should be present. This parameter is valid for traffic_generator ixnetwork_540. Available starting with HLT API 3.80. The uds_tracking_filter parameter is provided with a list of fields that are used for filtering. An operator and a value are applied on the specified field. This parameter specifies the operator that is applied: is_different is_equal is_equal_or_greater is_equal_or_smaller is_greater is_smaller null.
        Constants Available: UDS_L23TFD_TRACKING_OPERATOR_CMD
        Supported:IxNetwork
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.traffic_stats({TrafficStatsConstants.UDS_L23TFD_TRACKING_OPERATOR_CMD : opt})

    def traffic_stats_uds_l23tfd_tracking_value(self, any):
        """
        This is the method the command: traffic_stats option uds_l23tfd_tracking_value
        Description:This parameter is valid for traffic_generator ixnetwork_540, mode user_defined_stats, uds_type l23_traffic_flow_detective, uds_tracking_filter should be present. This parameter is valid for IxTclNetwork 5.40+ API. Available starting with HLT API 3.80. The uds_tracking_filter parameter is provided with a list of fields that are used for filtering. An operator and a value are applied on the specified field. This parameter specifies the value that is used for comparison.
        Constants Available: UDS_L23TFD_TRACKING_VALUE_CMD
        Supported:IxNetwork
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.traffic_stats({TrafficStatsConstants.UDS_L23TFD_TRACKING_VALUE_CMD : any})

    def traffic_stats_uds_port_filter(self, any):
        """
        This is the method the command: traffic_stats option uds_port_filter
        Description:This parameter is valid for traffic_generator ixnetwork_540, mode user_defined_stats, uds_type: l23_protocol_port, l23_traffic_flow, l23_traffic_flow_detective, l23_traffic_port. This parameter is valid for IxTclNetwork 5.40+ API. Available starting with HLT API 3.80. Represents the port filters that should be applied when retrieving statistics.
        Constants Available: UDS_PORT_FILTER_CMD
        Supported:IxNetwork
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.traffic_stats({TrafficStatsConstants.UDS_PORT_FILTER_CMD : any})

    def traffic_stats_uds_port_filter_count(self, numeric):
        """
        This is the method the command: traffic_stats option uds_port_filter_count
        Description:This parameter is valid for traffic_generator ixnetwork_540, mode user_defined_stats, uds_type: l23_protocol_port, l23_traffic_flow, l23_traffic_flow_detective, l23_traffic_port. This parameter is valid for IxTclNetwork 5.40+ API. Available starting with HLT API 3.80. Represents the number of port filters that should be applied when retrieving statistics (the length of the list provided to uds_port_filter). This parameter is extremely useful when the names of the filters contain spaces.
        Constants Available: UDS_PORT_FILTER_COUNT_CMD
        Supported:IxNetwork
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.traffic_stats({TrafficStatsConstants.UDS_PORT_FILTER_COUNT_CMD : numeric})

    def traffic_stats_uds_protocol_stack_filter(self, any):
        """
        This is the method the command: traffic_stats option uds_protocol_stack_filter
        Description:This parameter is valid for traffic_generator ixnetwork_540, mode user_defined_stats, uds_type: l23_protocol_stack. This parameter is valid for IxTclNetwork 5.40+ API. Available starting with HLT API 3.80. Represents the protocol stack filters that should be applied when retrieving statistics.
        Constants Available: UDS_PROTOCOL_STACK_FILTER_CMD
        Supported:IxNetwork
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.traffic_stats({TrafficStatsConstants.UDS_PROTOCOL_STACK_FILTER_CMD : any})

    def traffic_stats_uds_protocol_stack_filter_count(self, numeric):
        """
        This is the method the command: traffic_stats option uds_protocol_stack_filter_count
        Description:This parameter is valid for traffic_generator ixnetwork_540, mode user_defined_stats, uds_type: l23_protocol_stack. This parameter is valid for IxTclNetwork 5.40+ API. Available starting with HLT API 3.80. Represents the number of protocol stack filters that should be applied when retrieving statistics (the length of the list provided to uds_protocol_stack_filter). This parameter is extremely useful when the names of the filters contain spaces.
        Constants Available: UDS_PROTOCOL_STACK_FILTER_COUNT_CMD
        Supported:IxNetwork
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.traffic_stats({TrafficStatsConstants.UDS_PROTOCOL_STACK_FILTER_COUNT_CMD : numeric})

    def traffic_stats_uds_statistic_filter(self, any):
        """
        This is the method the command: traffic_stats option uds_statistic_filter
        Description:This parameter is valid for traffic_generator ixnetwork_540, mode user_defined_stats, uds_type: l23_traffic_flow_detective. This parameter is valid for IxTclNetwork 5.40+ API. Available starting with HLT API 3.80. Represents the statistic filters that should be applied when retrieving statistics.
        Constants Available: UDS_STATISTIC_FILTER_CMD
        Supported:IxNetwork
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.traffic_stats({TrafficStatsConstants.UDS_STATISTIC_FILTER_CMD : any})

    def traffic_stats_uds_statistic_filter_count(self, numeric):
        """
        This is the method the command: traffic_stats option uds_statistic_filter_count
        Description:This parameter is valid for traffic_generator ixnetwork_540, mode user_defined_stats, uds_type: l23_traffic_flow_detective. This parameter is valid for IxTclNetwork 5.40+ API. Available starting with HLT API 3.80. Represents the number of statistic filters that should be applied when retrieving statistics (the length of the list provided to uds_statistic_filter). This parameter is extremely useful when the names of the filters contain spaces.
        Constants Available: UDS_STATISTIC_FILTER_COUNT_CMD
        Supported:IxNetwork
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.traffic_stats({TrafficStatsConstants.UDS_STATISTIC_FILTER_COUNT_CMD : numeric})

    def traffic_stats_uds_tracking_filter(self, any):
        """
        This is the method the command: traffic_stats option uds_tracking_filter
        Description:This parameter is valid for traffic_generator ixnetwork_540, mode user_defined_stats, uds_type: l23_traffic_flow, l23_traffic_flow_detective. This parameter is valid for IxTclNetwork 5.40+ API. Available starting with HLT API 3.80. Represents the tracking filters that should be applied when retrieving statistics.If uds_type is l23_traffic_flow, parameters uds_l23tf_tracking_operator and uds_l23tf_tracking_value must be provided. If uds_type is l23_traffic_flow_detective, parameters uds_l23tfd_tracking_operator and uds_l23tfd_tracking_value must be provided.
        Constants Available: UDS_TRACKING_FILTER_CMD
        Supported:IxNetwork
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.traffic_stats({TrafficStatsConstants.UDS_TRACKING_FILTER_CMD : any})

    def traffic_stats_uds_tracking_filter_count(self, numeric):
        """
        This is the method the command: traffic_stats option uds_tracking_filter_count
        Description:This parameter is valid for traffic_generator ixnetwork_540, mode user_defined_stats, uds_type: l23_traffic_flow, l23_traffic_flow_detective. This parameter is valid for IxTclNetwork 5.40+ API. Represents the number of tracking filters that should be applied when retrieving statistics (the length of the list provided to uds_tracking_filter). This parameter is extremely useful when the names of the filters contain spaces.
        Constants Available: UDS_TRACKING_FILTER_COUNT_CMD
        Supported:IxNetwork
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.traffic_stats({TrafficStatsConstants.UDS_TRACKING_FILTER_COUNT_CMD : numeric})

    def traffic_stats_uds_traffic_item_filter(self, opt):
        """
        This is the method the command: traffic_stats option uds_traffic_item_filter
        Description:This parameter is valid for traffic_generator ixnetwork_540, mode user_defined_stats, uds_type: l23_traffic_flow, l23_traffic_flow_detective, l23_traffic_item. When uds_type is l23_traffic_flow, l23_traffic_flow_detective, only one filter can be applied at a time. This parameter is valid for IxTclNetwork 5.40+ API. Available starting with HLT API 3.80. Represents the traffic item filters that should be applied when retrieving statistics.
        Constants Available: UDS_TRAFFIC_ITEM_FILTER_CMD
        Supported:IxNetwork
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.traffic_stats({TrafficStatsConstants.UDS_TRAFFIC_ITEM_FILTER_CMD : opt})

    def traffic_stats_uds_traffic_item_filter_count(self, numeric):
        """
        This is the method the command: traffic_stats option uds_traffic_item_filter_count
        Description:This parameter is valid for traffic_generator ixnetwork_540, mode user_defined_stats, uds_type: l23_traffic_flow, l23_traffic_flow_detective, l23_traffic_item. This parameter is valid for IxTclNetwork 5.40+ API. Represents the number of traffic item filters that should be applied when retrieving statistics (the length of the list provided to uds_traffic_item_filter). This parameter is extremely useful when the names of the filters contain spaces.
        Constants Available: UDS_TRAFFIC_ITEM_FILTER_COUNT_CMD
        Supported:IxNetwork
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.traffic_stats({TrafficStatsConstants.UDS_TRAFFIC_ITEM_FILTER_COUNT_CMD : numeric})

    def traffic_stats_uds_type(self, opt):
        """
        This is the method the command: traffic_stats option uds_type
        Description:This parameter is valid for traffic_generator ixnetwork_540, mode user_defined_stats. This parameter is valid for IxTclNetwork 5.40+ API. Available starting with HLT API 3.80. l23_protocol_port - (DEFAULT) retrieve per port protocol statistics.l23_protocol_stack - retrieve per session or per range protocol statisticsl23_traffic_flow - retrieve per flow statisticsl23_traffic_flow_detective - retrieve flow detective statisticsl23_traffic_item - retrieve per traffic item statisticsl23_traffic_port - retrieve per port traffic statistics
        Constants Available: UDS_TYPE_CMD
        Supported:IxNetwork
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.traffic_stats({TrafficStatsConstants.UDS_TYPE_CMD : opt})

    def traffic_stats_vci(self, range):
        """
        This is the method the command: traffic_stats option vci
        Description:The virtual path identifier (default 0). Valid only for traffic_generator ixos.
        Constants Available: VCI_CMD
        Supported:IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.traffic_stats({TrafficStatsConstants.VCI_CMD : range})

    def traffic_stats_vci_count(self, range):
        """
        This is the method the command: traffic_stats option vci_count
        Description:If -atm_counter_vci_type is set to counter and atm_counter_vci_mode is set to incr or decr, then this is the number of times to increment the VCI value before repeating from the start value (default 1). Valid only for traffic_generator ixos.
        Constants Available: VCI_COUNT_CMD
        Supported:IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.traffic_stats({TrafficStatsConstants.VCI_COUNT_CMD : range})

    def traffic_stats_vci_step(self, range):
        """
        This is the method the command: traffic_stats option vci_step
        Description:If -atm_counter_vci_type is set to counter, then this is the value added/substracted between successive vci values (default 1). Valid only for traffic_generator ixos.
        Constants Available: VCI_STEP_CMD
        Supported:IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.traffic_stats({TrafficStatsConstants.VCI_STEP_CMD : range})

    def traffic_stats_vpi(self, range):
        """
        This is the method the command: traffic_stats option vpi
        Description:The virtual circuit identifier (default 32). Valid only for traffic_generator ixos.
        Constants Available: VPI_CMD
        Supported:IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.traffic_stats({TrafficStatsConstants.VPI_CMD : range})

    def traffic_stats_vpi_step(self, range):
        """
        This is the method the command: traffic_stats option vpi_step
        Description:If -atm_counter_vpi_type is set to counter, then this is the value added/substracted between successive vpi values (default 1). Valid only for traffic_generator ixos.
        Constants Available: VPI_STEP_CMD
        Supported:IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.traffic_stats({TrafficStatsConstants.VPI_STEP_CMD : range})


    supportedIxiaHltapiCommands = {TrafficStatsConstants.ATM_COUNTER_VCI_DATA_ITEM_LIST_CMD, TrafficStatsConstants.ATM_COUNTER_VCI_MODE_CMD, TrafficStatsConstants.ATM_COUNTER_VCI_TYPE_CMD, TrafficStatsConstants.ATM_COUNTER_VPI_DATA_ITEM_LIST_CMD, TrafficStatsConstants.ATM_COUNTER_VPI_MODE_CMD, TrafficStatsConstants.ATM_COUNTER_VPI_TYPE_CMD, TrafficStatsConstants.ATM_REASSEMBLY_ENABLE_IP_QOS_CMD, TrafficStatsConstants.ATM_REASSEMBLY_ENABLE_IPTCPUDP_CHECKSUM_CMD, TrafficStatsConstants.ATM_REASSEMBLY_ENCAPSULATION_CMD, TrafficStatsConstants.CSV_PATH_CMD, TrafficStatsConstants.DRILL_DOWN_FLOW_CMD, TrafficStatsConstants.DRILL_DOWN_LISTENING_PORT_CMD, TrafficStatsConstants.DRILL_DOWN_PORT_CMD, TrafficStatsConstants.DRILL_DOWN_TRAFFIC_ITEM_CMD, TrafficStatsConstants.DRILL_DOWN_TYPE_CMD, TrafficStatsConstants.EGRESS_MODE_CMD, TrafficStatsConstants.EGRESS_STATS_LIST_CMD, TrafficStatsConstants.IGNORE_RATE_CMD, TrafficStatsConstants.MEASURE_MODE_CMD, TrafficStatsConstants.MODE_CMD, TrafficStatsConstants.PACKET_GROUP_ID_CMD, TrafficStatsConstants.PORT_HANDLE_CMD, TrafficStatsConstants.PREVIOUS_DATA_CMD, TrafficStatsConstants.QOS_STATS_CMD, TrafficStatsConstants.RETURN_METHOD_CMD, TrafficStatsConstants.STREAM_CMD, TrafficStatsConstants.STREAMS_CMD, TrafficStatsConstants.TRAFFIC_GENERATOR_CMD, TrafficStatsConstants.UDS_ACTION_CMD, TrafficStatsConstants.UDS_L23PS_DRILLDOWN_CMD, TrafficStatsConstants.UDS_L23PS_NUM_RESULTS_CMD, TrafficStatsConstants.UDS_L23PS_SORTING_STATISTIC_CMD, TrafficStatsConstants.UDS_L23PS_SORTING_TYPE_CMD, TrafficStatsConstants.UDS_L23TF_AGGREGATED_ACROSS_PORTS_CMD, TrafficStatsConstants.UDS_L23TF_EGRESS_LATENCY_BIN_DISPLAY_CMD, TrafficStatsConstants.UDS_L23TF_ENUMERATION_SORTING_TYPE_CMD, TrafficStatsConstants.UDS_L23TF_FILTER_TYPE_CMD, TrafficStatsConstants.UDS_L23TF_TRACKING_OPERATOR_CMD, TrafficStatsConstants.UDS_L23TF_TRACKING_VALUE_CMD, TrafficStatsConstants.UDS_L23TFD_DEAD_FLOWS_TRESHOLD_CMD, TrafficStatsConstants.UDS_L23TFD_FLOW_TYPE_CMD, TrafficStatsConstants.UDS_L23TFD_SHOW_EGRESS_FLOWS_CMD, TrafficStatsConstants.UDS_L23TFD_STATISTIC_ALL_FLOWS_NUM_RESULTS_CMD, TrafficStatsConstants.UDS_L23TFD_STATISTIC_ALL_FLOWS_SORT_BY_CMD, TrafficStatsConstants.UDS_L23TFD_STATISTIC_ALL_FLOWS_SORTING_TYPE_CMD, TrafficStatsConstants.UDS_L23TFD_STATISTIC_DEAD_FLOWS_NUM_RESULTS_CMD, TrafficStatsConstants.UDS_L23TFD_STATISTIC_DEAD_FLOWS_SORT_BY_CMD, TrafficStatsConstants.UDS_L23TFD_STATISTIC_DEAD_FLOWS_SORTING_TYPE_CMD, TrafficStatsConstants.UDS_L23TFD_STATISTIC_LIVE_FLOWS_NUM_RESULTS_CMD, TrafficStatsConstants.UDS_L23TFD_STATISTIC_LIVE_FLOWS_SORT_BY_CMD, TrafficStatsConstants.UDS_L23TFD_STATISTIC_LIVE_FLOWS_SORTING_TYPE_CMD, TrafficStatsConstants.UDS_L23TFD_STATISTIC_OPERATOR_CMD, TrafficStatsConstants.UDS_L23TFD_STATISTIC_VALUE_CMD, TrafficStatsConstants.UDS_L23TFD_TRACKING_OPERATOR_CMD, TrafficStatsConstants.UDS_L23TFD_TRACKING_VALUE_CMD, TrafficStatsConstants.UDS_PORT_FILTER_CMD, TrafficStatsConstants.UDS_PORT_FILTER_COUNT_CMD, TrafficStatsConstants.UDS_PROTOCOL_STACK_FILTER_CMD, TrafficStatsConstants.UDS_PROTOCOL_STACK_FILTER_COUNT_CMD, TrafficStatsConstants.UDS_STATISTIC_FILTER_CMD, TrafficStatsConstants.UDS_STATISTIC_FILTER_COUNT_CMD, TrafficStatsConstants.UDS_TRACKING_FILTER_CMD, TrafficStatsConstants.UDS_TRACKING_FILTER_COUNT_CMD, TrafficStatsConstants.UDS_TRAFFIC_ITEM_FILTER_CMD, TrafficStatsConstants.UDS_TRAFFIC_ITEM_FILTER_COUNT_CMD, TrafficStatsConstants.UDS_TYPE_CMD, TrafficStatsConstants.VCI_CMD, TrafficStatsConstants.VCI_COUNT_CMD, TrafficStatsConstants.VCI_STEP_CMD, TrafficStatsConstants.VPI_CMD, TrafficStatsConstants.VPI_STEP_CMD}
