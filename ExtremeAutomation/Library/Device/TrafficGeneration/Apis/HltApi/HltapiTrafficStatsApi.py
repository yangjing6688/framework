from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.TrafficGenerationApi import TrafficGenerationApi
from ExtremeAutomation.Library.Utils.Singleton import Singleton

"""
    This is the API class for the command: traffic_stats

    Class is auto-generated. If you update anything here,
        it will be over written.
"""


class TrafficStatsApi(TrafficGenerationApi):

    """
    init function
    """
    def __init__(self, device):
        super(TrafficStatsApi, self).__init__(device)

    """
    This is the "One Large Method" for the command: traffic_stats
    use this by passing in a dict() of all the commands
        dummyDict = dict()
        dummyDict[TrafficStatsConstants.ATM_COUNTER_VCI_DATA_ITEM_LIST_CMD] = "dummyValue1" # static value
        dummyDict[TrafficStatsConstants.ATM_COUNTER_VCI_MODE_CMD] = TrafficStatsConstants.ATM_COUNTER_VCI_MODE_INCR # constant value
        dummyDict[TrafficStatsConstants.ATM_COUNTER_VCI_TYPE_CMD] = TrafficStatsConstants.ATM_COUNTER_VCI_TYPE_FIXED # constant value
        dummyDict[TrafficStatsConstants.ATM_COUNTER_VPI_DATA_ITEM_LIST_CMD] = "dummyValue4" # static value
        dummyDict[TrafficStatsConstants.ATM_COUNTER_VPI_MODE_CMD] = TrafficStatsConstants.ATM_COUNTER_VPI_MODE_INCR # constant value
        dummyDict[TrafficStatsConstants.ATM_COUNTER_VPI_TYPE_CMD] = TrafficStatsConstants.ATM_COUNTER_VPI_TYPE_FIXED # constant value
        dummyDict[TrafficStatsConstants.ATM_REASSEMBLY_ENABLE_IP_QOS_CMD] = "dummyValue7" # static value
        dummyDict[TrafficStatsConstants.ATM_REASSEMBLY_ENABLE_IPTCPUDP_CHECKSUM_CMD] = "dummyValue8" # static value
        dummyDict[TrafficStatsConstants.ATM_REASSEMBLY_ENCAPSULATION_CMD] = TrafficStatsConstants.ATM_REASSEMBLY_ENCAPSULATION_VCC_MUX_IPV4_ROUTED # constant value
        dummyDict[TrafficStatsConstants.CSV_PATH_CMD] = "dummyValue10" # static value
        dummyDict[TrafficStatsConstants.DRILL_DOWN_FLOW_CMD] = "dummyValue11" # static value
        dummyDict[TrafficStatsConstants.DRILL_DOWN_LISTENING_PORT_CMD] = "dummyValue12" # static value
        dummyDict[TrafficStatsConstants.DRILL_DOWN_PORT_CMD] = "dummyValue13" # static value
        dummyDict[TrafficStatsConstants.DRILL_DOWN_TRAFFIC_ITEM_CMD] = "dummyValue14" # static value
        dummyDict[TrafficStatsConstants.DRILL_DOWN_TYPE_CMD] = TrafficStatsConstants.DRILL_DOWN_TYPE_PER_IPS # constant value
        dummyDict[TrafficStatsConstants.EGRESS_MODE_CMD] = TrafficStatsConstants.EGRESS_MODE_CONDITIONAL # constant value
        dummyDict[TrafficStatsConstants.EGRESS_STATS_LIST_CMD] = "dummyValue17" # static value
        dummyDict[TrafficStatsConstants.IGNORE_RATE_CMD] = "dummyValue18" # static value
        dummyDict[TrafficStatsConstants.MEASURE_MODE_CMD] = TrafficStatsConstants.MEASURE_MODE_CUMULATIVE # constant value
        dummyDict[TrafficStatsConstants.MODE_CMD] = TrafficStatsConstants.MODE_ADD_ATM_STATS # constant value
        dummyDict[TrafficStatsConstants.PACKET_GROUP_ID_CMD] = "dummyValue21" # static value
        dummyDict[TrafficStatsConstants.PORT_HANDLE_CMD] = "dummyValue22" # static value
        dummyDict[TrafficStatsConstants.PREVIOUS_DATA_CMD] = TrafficStatsConstants.PREVIOUS_DATA_KEEP # constant value
        dummyDict[TrafficStatsConstants.QOS_STATS_CMD] = "dummyValue24" # static value
        dummyDict[TrafficStatsConstants.RETURN_METHOD_CMD] = TrafficStatsConstants.RETURN_METHOD_KEYED_LIST # constant value
        dummyDict[TrafficStatsConstants.STREAM_CMD] = "dummyValue26" # static value
        dummyDict[TrafficStatsConstants.STREAMS_CMD] = "dummyValue27" # static value
        dummyDict[TrafficStatsConstants.TRAFFIC_GENERATOR_CMD] = TrafficStatsConstants.TRAFFIC_GENERATOR_IXOS # constant value
        dummyDict[TrafficStatsConstants.UDS_ACTION_CMD] = TrafficStatsConstants.UDS_ACTION_GET_AVAILABLE_PORT_FILTERS # constant value
        dummyDict[TrafficStatsConstants.UDS_L23PS_DRILLDOWN_CMD] = TrafficStatsConstants.UDS_L23PS_DRILLDOWN_PER_SESSION # constant value
        dummyDict[TrafficStatsConstants.UDS_L23PS_NUM_RESULTS_CMD] = "dummyValue31" # static value
        dummyDict[TrafficStatsConstants.UDS_L23PS_SORTING_STATISTIC_CMD] = "dummyValue32" # static value
        dummyDict[TrafficStatsConstants.UDS_L23PS_SORTING_TYPE_CMD] = TrafficStatsConstants.UDS_L23PS_SORTING_TYPE_ASCENDING # constant value
        dummyDict[TrafficStatsConstants.UDS_L23TF_AGGREGATED_ACROSS_PORTS_CMD] = "dummyValue34" # static value
        dummyDict[TrafficStatsConstants.UDS_L23TF_EGRESS_LATENCY_BIN_DISPLAY_CMD] = TrafficStatsConstants.UDS_L23TF_EGRESS_LATENCY_BIN_DISPLAY_NONE # constant value
        dummyDict[TrafficStatsConstants.UDS_L23TF_ENUMERATION_SORTING_TYPE_CMD] = TrafficStatsConstants.UDS_L23TF_ENUMERATION_SORTING_TYPE_ASCENDING # constant value
        dummyDict[TrafficStatsConstants.UDS_L23TF_FILTER_TYPE_CMD] = TrafficStatsConstants.UDS_L23TF_FILTER_TYPE_ENUMERATION # constant value
        dummyDict[TrafficStatsConstants.UDS_L23TF_TRACKING_OPERATOR_CMD] = TrafficStatsConstants.UDS_L23TF_TRACKING_OPERATOR_IS_DIFFERENT # constant value
        dummyDict[TrafficStatsConstants.UDS_L23TF_TRACKING_VALUE_CMD] = "dummyValue39" # static value
        dummyDict[TrafficStatsConstants.UDS_L23TFD_DEAD_FLOWS_TRESHOLD_CMD] = "dummyValue40" # static value
        dummyDict[TrafficStatsConstants.UDS_L23TFD_FLOW_TYPE_CMD] = TrafficStatsConstants.UDS_L23TFD_FLOW_TYPE_ALL_FLOWS # constant value
        dummyDict[TrafficStatsConstants.UDS_L23TFD_SHOW_EGRESS_FLOWS_CMD] = "dummyValue42" # static value
        dummyDict[TrafficStatsConstants.UDS_L23TFD_STATISTIC_ALL_FLOWS_NUM_RESULTS_CMD] = "dummyValue43" # static value
        dummyDict[TrafficStatsConstants.UDS_L23TFD_STATISTIC_ALL_FLOWS_SORT_BY_CMD] = "dummyValue44" # static value
        dummyDict[TrafficStatsConstants.UDS_L23TFD_STATISTIC_ALL_FLOWS_SORTING_TYPE_CMD] = TrafficStatsConstants.UDS_L23TFD_STATISTIC_ALL_FLOWS_SORTING_TYPE_ASCENDING # constant value
        dummyDict[TrafficStatsConstants.UDS_L23TFD_STATISTIC_DEAD_FLOWS_NUM_RESULTS_CMD] = "dummyValue46" # static value
        dummyDict[TrafficStatsConstants.UDS_L23TFD_STATISTIC_DEAD_FLOWS_SORT_BY_CMD] = "dummyValue47" # static value
        dummyDict[TrafficStatsConstants.UDS_L23TFD_STATISTIC_DEAD_FLOWS_SORTING_TYPE_CMD] = TrafficStatsConstants.UDS_L23TFD_STATISTIC_DEAD_FLOWS_SORTING_TYPE_ASCENDING # constant value
        dummyDict[TrafficStatsConstants.UDS_L23TFD_STATISTIC_LIVE_FLOWS_NUM_RESULTS_CMD] = "dummyValue49" # static value
        dummyDict[TrafficStatsConstants.UDS_L23TFD_STATISTIC_LIVE_FLOWS_SORT_BY_CMD] = "dummyValue50" # static value
        dummyDict[TrafficStatsConstants.UDS_L23TFD_STATISTIC_LIVE_FLOWS_SORTING_TYPE_CMD] = TrafficStatsConstants.UDS_L23TFD_STATISTIC_LIVE_FLOWS_SORTING_TYPE_ASCENDING # constant value
        dummyDict[TrafficStatsConstants.UDS_L23TFD_STATISTIC_OPERATOR_CMD] = TrafficStatsConstants.UDS_L23TFD_STATISTIC_OPERATOR_IS_DIFFERENT # constant value
        dummyDict[TrafficStatsConstants.UDS_L23TFD_STATISTIC_VALUE_CMD] = "dummyValue53" # static value
        dummyDict[TrafficStatsConstants.UDS_L23TFD_TRACKING_OPERATOR_CMD] = TrafficStatsConstants.UDS_L23TFD_TRACKING_OPERATOR_IS_DIFFERENT # constant value
        dummyDict[TrafficStatsConstants.UDS_L23TFD_TRACKING_VALUE_CMD] = "dummyValue55" # static value
        dummyDict[TrafficStatsConstants.UDS_PORT_FILTER_CMD] = "dummyValue56" # static value
        dummyDict[TrafficStatsConstants.UDS_PORT_FILTER_COUNT_CMD] = "dummyValue57" # static value
        dummyDict[TrafficStatsConstants.UDS_PROTOCOL_STACK_FILTER_CMD] = "dummyValue58" # static value
        dummyDict[TrafficStatsConstants.UDS_PROTOCOL_STACK_FILTER_COUNT_CMD] = "dummyValue59" # static value
        dummyDict[TrafficStatsConstants.UDS_STATISTIC_FILTER_CMD] = "dummyValue60" # static value
        dummyDict[TrafficStatsConstants.UDS_STATISTIC_FILTER_COUNT_CMD] = "dummyValue61" # static value
        dummyDict[TrafficStatsConstants.UDS_TRACKING_FILTER_CMD] = "dummyValue62" # static value
        dummyDict[TrafficStatsConstants.UDS_TRACKING_FILTER_COUNT_CMD] = "dummyValue63" # static value
        dummyDict[TrafficStatsConstants.UDS_TRAFFIC_ITEM_FILTER_CMD] = "dummyValue64" # static value
        dummyDict[TrafficStatsConstants.UDS_TRAFFIC_ITEM_FILTER_COUNT_CMD] = "dummyValue65" # static value
        dummyDict[TrafficStatsConstants.UDS_TYPE_CMD] = TrafficStatsConstants.UDS_TYPE_L23_PROTOCOL_PORT # constant value
        dummyDict[TrafficStatsConstants.VCI_CMD] = "dummyValue67" # static value
        dummyDict[TrafficStatsConstants.VCI_COUNT_CMD] = "dummyValue68" # static value
        dummyDict[TrafficStatsConstants.VCI_STEP_CMD] = "dummyValue69" # static value
        dummyDict[TrafficStatsConstants.VPI_CMD] = "dummyValue70" # static value
        dummyDict[TrafficStatsConstants.VPI_STEP_CMD] = "dummyValue71" # static value

        api = device.getApi(TrafficStatsConstants.TRAFFIC_STATS_API)
        api.traffic_stats(dummyDict)
    """
    def traffic_stats(self, argdictionary, supported = None):
        self.process_supported_hltapi_commands(argdictionary, supported)
        return self.send_command_args(self._nameSpace +"::traffic_stats", argdictionary)

    """
    Individual commands for each option. Typically, the "One Large Method"
    is the one that you want to be using so look at that example above
    """
    def traffic_stats_atm_counter_vci_data_item_list(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_stats_atm_counter_vci_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_stats_atm_counter_vci_type(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_stats_atm_counter_vpi_data_item_list(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_stats_atm_counter_vpi_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_stats_atm_counter_vpi_type(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_stats_atm_reassembly_enable_ip_qos(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_stats_atm_reassembly_enable_iptcpudp_checksum(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_stats_atm_reassembly_encapsulation(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_stats_csv_path(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_stats_drill_down_flow(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_stats_drill_down_listening_port(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_stats_drill_down_port(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_stats_drill_down_traffic_item(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_stats_drill_down_type(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_stats_egress_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_stats_egress_stats_list(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_stats_ignore_rate(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_stats_measure_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_stats_mode(self, opt):
        """
        This is the method the command: traffic_stats option mode
        Description:Type of statistics to collect. Valid choices are:
            Valid options are:
            add_atm_stats: Adds the vpi/vci pair to gather both rx and tx statistics. The number of tx stats that can be tracked is less than the number of rx stats that can be tracked. This option is valid only if -traffic_generator is set to ixos.
            add_atm_stats_rx: Adds the vpi/vci pair to gather rx statistics. The number of tx stats that can be tracked is less than the number of rx stats that can be tracked. This option is valid only if -traffic_generator is set to ixos.
            add_atm_stats_tx: Adds the vpi/vci pair to gather tx statistics. The number of tx stats that can be tracked is less than the number of rx stats that can be tracked. This option is valid only if -traffic_generator is set to ixos.
            aggregate: Gathers per port aggregated stats. This option is valid only if -traffic_generator is set to ixos or ixnetwork or ixnetwork_540 and streams where generated either with IxOS/IxNetwork.
            all: Gathers all the statistics available for the specific -traffic_generator option.Note: This mode is applicable only for L2/L3 Traffic.
            faststream: Not implemented.
            flow: Gathers per flow stats. This option is valid only if -traffic_generator is set to ixnetwork or ixnetwork_540 and streams were generated with IxNetwork.
            igmp_over_ppp: Not supported.
            l23_test_summary: Available only for IxNetwork TCL API. This mode retrieves layer 2-3 statistics agreagated across all ports (parameter port_handle is ignored in this mode). The equivalent from IxNetwork GUI is ""L2-L3 Test Summary Statistics"" view. This option is valid only if -traffic_generator is set to ixnetwork_540.
            multicast: Not supported.
            out_of_filter: Not implemented.
            per_port_flows: Ability to retrieve per flow information using HLTAPI. Valid only for traffic generator ixnetwork or ixnetwork_540.session - Not supported.
            stream: Gathers per stream stats. This option is valid only if -traffic_generator is set to ixos and streams were generated with IxOS or parameter -traffic_generator is set to ixnetwork or ixnetwork_540 and streams were generated with IxNetwork.
            streams: This is the same as stream option. Deprecated.
            egress_by_port: Available only for IxNetwork TCL API. Parameter port_handle is mandatory for this mode. If egress tracking was configured on the port_handle port this mode retrieves egress tracking statistics for this port. This is available with -traffic_generator ixnetwork and ixnetwork_540.
            egress_by_flow: Available only for IxNetwork TCL API. Parameter port_handle is mandatory for this mode. If egress tracking was configured on the port_handle port this mode retrieves egress tracking statistics for the flows on port_handle port. This is available with -traffic_generator ixnetwork and ixnetwork_540.
            data_plane_port: Available only for IxNetwork TCL API with traffic_generator ixnetwork_540. Retrieve per port data plane statistics.
            traffic_item: Available only for IxNetwork TCL API with traffic_generator ixnetwork_540. Retrieve statistics per traffic item. The statistics can be filtered using parameter -stream with one or a list of values. The values must be traffic_items returned by procedure ::<namespace>::traffic_config.
            user_defined_stats: Available only for IxNetwork TCL API with traffic_generator ixnetwork_540. Retrieve user defined statitics. The statistics can be filtered using parameters starting with -uds_... with one or a list of values. Available starting with HLT API 3.80.
            application_FTP: Deprecated value, previously used for AppLib Legacy Traffic
            application_HTTP: Deprecated value, previously used for AppLib Legacy Traffic
            application_TELNET: Deprecated value, previously used for AppLib Legacy Traffic
            application_SMTP: Deprecated value, previously used for AppLib Legacy Traffic
            application_IMAP: Deprecated value, previously used for AppLib Legacy Traffic
            application_POP3: Deprecated value, previously used for AppLib Legacy Traffic
            application_TriplePlay: Deprecated value, previously used for AppLib Legacy Traffic
            application_SIP: Deprecated value, previously used for AppLib Legacy Traffic
            application_Video: Deprecated value, previously used for AppLib Legacy Traffic
            application_RTSP: Deprecated value, previously used for AppLib Legacy Traffic

            Type of statistics to collect. Valid choices are:
            Valid options are:
            add_atm_stats"" Adds the vpi/vci pair to gather both rx and tx statistics. The number of tx stats that can be tracked is less than the number of rx stats that can be tracked. This option is valid only if -traffic_generator is set to ixos.
            add_atm_stats_rx: Adds the vpi/vci pair to gather rx statistics. The number of tx stats that can be tracked is less than the number of rx stats that can be tracked. This option is valid only if -traffic_generator is set to ixos.
            add_atm_stats_tx: Adds the vpi/vci pair to gather tx statistics. The number of tx stats that can be tracked is less than the number of rx stats that can be tracked. This option is valid only if -traffic_generator is set to ixos.
            aggregate: Gathers per port aggregated stats. This option is valid only if -traffic_generator is set to ixos or ixnetwork or ixnetwork_540 and streams where generated either with IxOS/IxNetwork.
            all: Gathers all the statistics available for the specific -traffic_generator option.Note: This mode is applicable only for L2/L3 Traffic.
            faststream: Not implemented.
            flow: Gathers per flow stats. This option is valid only if -traffic_generator is set to ixnetwork or ixnetwork_540 and streams were generated with IxNetwork.
            igmp_over_ppp: Not supported.
            l23_test_summary: Available only for IxNetwork TCL API. This mode retrieves layer 2-3 statistics agreagated across all ports (parameter port_handle is ignored in this mode). The equivalent from IxNetwork GUI is ""L2-L3 Test Summary Statistics"" view. This option is valid only if -traffic_generator is set to ixnetwork_540.
            multicast: Not supported.
            out_of_filter: Not implemented.
            per_port_flows: Ability to retrieve per flow information using HLTAPI. Valid only for traffic generator ixnetwork or ixnetwork_540.session - Not supported.
            stream: Gathers per stream stats. This option is valid only if -traffic_generator is set to ixos and streams were generated with IxOS or parameter -traffic_generator is set to ixnetwork or ixnetwork_540 and streams were generated with IxNetwork.
            streams: This is the same as stream option. Deprecated.
            egress_by_port: Available only for IxNetwork TCL API. Parameter port_handle is mandatory for this mode. If egress tracking was configured on the port_handle port this mode retrieves egress tracking statistics for this port. This is available with -traffic_generator ixnetwork and ixnetwork_540.
            egress_by_flow: Available only for IxNetwork TCL API. Parameter port_handle is mandatory for this mode. If egress tracking was configured on the port_handle port this mode retrieves egress tracking statistics for the flows on port_handle port. This is available with -traffic_generator ixnetwork and ixnetwork_540.
            data_plane_port: Available only for IxNetwork TCL API with traffic_generator ixnetwork_540. Retrieve per port data plane statistics.
            traffic_item: Available only for IxNetwork TCL API with traffic_generator ixnetwork_540. Retrieve statistics per traffic item. The statistics can be filtered using parameter -stream with one or a list of values. The values must be traffic_items returned by procedure ::<namespace>::traffic_config.
            user_defined_stats: Available only for IxNetwork TCL API with traffic_generator ixnetwork_540. Retrieve user defined statitics. The statistics can be filtered using parameters starting with -uds_... with one or a list of values. Available starting with HLT API 3.80.
            application_FTP: Available only for IxNetwork TCL API with traffic_generator ixnetwork_540. Retrieves FTP statitics for L4/L7 traffic. The statistics are retrieved from the following stat views. Available starting with HLT API 4.70. csv is the only supported return method for this mode.Retrieved Stat Views: FTP Client - ObjectivesFTP Client - Throughput ObjectiveFTP Client - Connection RatesFTP Client - ConnectionsFTP Client - LatenciesFTP Client - File Upload Download RatesFTP Client - TCP ConnectionsFTP Client - TCP FailuresFTP Server - Connection RatesFTP Server - ConnectionsFTP Server - Connection LatencyFTP Server - Data RatesFTP Server - File Upload Download RatesFTP Server - TCP ConnectionsFTP Server - TCP Failures
            application_HTTP: Available only for IxNetwork TCL API with traffic_generator ixnetwork_540. Retrieves HTTP statitics for L4/L7 traffic. The statistics are retrieved from the following stat views. Available starting with HLT API 4.70. csv is the only supported return method for this mode.Retrieved Stat Views: HTTP Client - TCP ConnectionsHTTP Client - TCP FailuresHTTP Client - Per URLHTTP Client - SSL Handshake statsHTTP Client - SSL ThroughputHTTP Client - SSL Warning AlertsHTTP Client - SSL Fatal AlertsHTTP Client - SSLv2 ErrorsHTTP Server - Transaction RatesHTTP Server - TransactionsHTTP Server - Data RatesHTTP Server - Responses SentHTTP Server - HTTP FailuresHTTP Server - TCP ConnectionsHTTP Server - TCP FailuresHTTP Server - Per IPv4 Per URLHTTP Server - SSL Handshake StatsHTTP Server - SSL ThroughputHTTP Server - SSL Warning AlertsHTTP Server - SSL Fatal AlertsHTTP Server - SSLv2 Errors
            application_TELNET: Available only for IxNetwork TCL API with traffic_generator ixnetwork_540. Retrieves TELNET statitics for L4/L7 traffic. The statistics are retrieved from the following stat views. Available starting with HLT API 4.70. csv is the only supported return method for this mode. Retrieved Stat Views: Telnet Client - ObjectivesTelnet Client - Throughput ObjectiveTelnet Client - Echo OptionTelnet Client - Suppress Go Ahead OptionTelnet Client - Line Mode OptionTelnet Client - SessionsTelnet Client - TCP ConnectionsTelnet Client - TCP FailuresTelnet Server - ThroughputTelnet Server - Echo OptionTelnet Server - Suppress Go Ahead OptionTelnet Server - SessionsTelnet Server - Line Mode OptionTelnet Server - TCP ConnectionsTelnet Server - TCP Failures
            application_SMTP: Available only for IxNetwork TCL API with traffic_generator ixnetwork_540. Retrieves SMTP statitics for L4/L7 traffic. The statistics are retrieved from the following stat views. Available starting with HLT API 4.70. csv is the only supported return method for this mode. Retrieved Stat Views: SMTP Client - ObjectivesSMTP Client - Throughput ObjectiveSMTP Client - Session RatesSMTP Client - SessionsSMTP Client - Mail RatesSMTP Client - MailsSMTP Client - TCP ConnectionsSMTP Client - TCP FailuresSMTP Server - Session RatesSMTP Server - SessionsSMTP Server - Data RatesSMTP Server - Mail RatesSMTP Server - MailsSMTP Server - TCP ConnectionsSMTP Server - TCP Failures
            application_IMAP: Available only for IxNetwork TCL API with traffic_generator ixnetwork_540. Retrieves IMAP statitics for L4/L7 traffic. The statistics are retrieved from the following stat views. Available starting with HLT API 4.70. csv is the only supported return method for this mode. Retrieved Stat Views: IMAP Client - ObjectivesIMAP Client - Throughput ObjectiveIMAP Client - Session RatesIMAP Client - Commands SentIMAP Client - Commands SuccessfullIMAP Client - Commands FailedIMAP Client - Commands AbortedIMAP Client - Total Mails ReceivedIMAP Server - Commands ReceivedIMAP Server - Responses SentIMAP Server - FailuresIMAP Server - ThroughputIMAP Server - Session RatesIMAP Server - Total Mails and Attachments Sent
            application_POP3: Available only for IxNetwork TCL API with traffic_generator ixnetwork_540. Retrieves POP3 statitics for L4/L7 traffic. The statistics are retrieved from the following stat views. Available starting with HLT API 4.70. csv is the only supported return method for this mode. Retrieved Stat Views: POP3 Client - Mail RatesPOP3 Client - MailsPOP3 Client - ObjectivesPOP3 Client - Session RatesPOP3 Client - SessionsPOP3 Client - TCP ConnectionsPOP3 Client - TCP FailuresPOP3 Client - Throughput ObjectivePOP3 Server - Data RatesPOP3 Server - Mail RatesPOP3 Server - MailsPOP3 Server - Session RatesPOP3 Server - SessionsPOP3 Server - TCP ConnectionsPOP3 Server - TCP Failures
            application_TriplePlay: Available only for IxNetwork TCL API with traffic_generator ixnetwork_540. Retrieves TriplePlay statitics for L4/L7 traffic. The statistics are retrieved from the following stat views. Available starting with HLT API 4.70. csv is the only supported return method for this mode. Retrieved Stat Views: FTP Client - ObjectivesFTP Client - Throughput ObjectiveFTP Client - Connection RatesFTP Client - ConnectionsFTP Client - LatenciesFTP Client - File Upload Download RatesFTP Client - TCP ConnectionsFTP Client - TCP FailuresFTP Server - Connection RatesFTP Server - ConnectionsFTP Server - Connection LatencyFTP Server - Data RatesFTP Server - File Upload Download RatesFTP Server - TCP ConnectionsFTP Server - TCP FailuresHTTP Client - ObjectivesHTTP Client - Throughput ObjectiveHTTP Client - Transaction RatesHTTP Client - TransactionsHTTP Client - LatenciesHTTP Client - 1xx, 2xx and 3xx ResponsesHTTP Client - HTTP FailuresHTTP Client - TCP ConnectionsHTTP Client - TCP FailuresHTTP Client - Per URLHTTP Client - SSL Handshake statsHTTP Client - SSL ThroughputHTTP Client - SSL Warning AlertsHTTP Client - SSL Fatal AlertsHTTP Client - SSLv2 ErrorsHTTP Server - Transaction RatesHTTP Server - TransactionsHTTP Server - Data RatesHTTP Server - Responses SentHTTP Server - HTTP FailuresHTTP Server - TCP ConnectionsHTTP Server - TCP FailuresHTTP Server - Per IPv4 Per URLHTTP Server - SSL Handshake StatsHTTP Server - SSL ThroughputHTTP Server - SSL Warning AlertsHTTP Server - SSL Fatal AlertsHTTP Server - SSLv2 ErrorsSIP Client - ObjectivesSIP Client - Busy Hour Call AttemptsSIP Client - TransactionsSIP Client - Sent MessagesSIP Client - Received MessagesSIP Client - TCPSIP Client - RTPSIP Client - RTP JitterSIP Client - RTP Per CallSIP Server - CallsSIP Server - TransactionsSIP Server - Sent MessagesSIP Server - Received MessagesSIP Server - TCPSIP Server - RTPSIP Server - RTP JitterSIP Server - RTP Per CallVideo Client - ObjectivesVideo Client - Active ChannelsVideo Client - Multicast Channel RequestsVideo Client - VoD Channel RequestsVideo Client - Report SummaryVideo Client - Jitter DistributionVideo Client - Inter Packet Arrival Time DistributionVideo Client - Packet Latency DistributionVideo Client - Per StreamVideo Client - RTSP CommandsVideo Client - Data RatesVideo Client - LatencyVideo Client - Data ErrorsVideo Client - Error MessagesVideo Client - Packet Size DistributionVideo Server - Active StreamsVideo Server - RTSP TotalsVideo Server - Stream Bit RatesVideo Server - Data RatesVideo Server - Error Stats
            application_SIP: Available only for IxNetwork TCL API with traffic_generator ixnetwork_540. Retrieves SIP statitics for L4/L7 traffic. The statistics are retrieved from the following stat views. Available starting with HLT API 4.70. csv is the only supported return method for this mode. Retrieved Stat Views: SIP Client - ObjectivesSIP Client - Busy Hour Call AttemptsSIP Client - TransactionsSIP Client - Sent MessagesSIP Client - Received MessagesSIP Client - TCPSIP Client - RTPSIP Client - RTP JitterSIP Client - RTP Per CallSIP Server - CallsSIP Server - TransactionsSIP Server - Sent MessagesSIP Server - Received MessagesSIP Server - TCPSIP Server - RTPSIP Server - RTP JitterSIP Server - RTP Per Call
            application_Video: Available only for IxNetwork TCL API with traffic_generator ixnetwork_540. Retrieves video statitics for L4/L7 traffic. The statistics are retrieved from the following stat views. Available starting with HLT API 4.70. csv is the only supported return method for this mode. Retrieved Stat Views: Video Client - ObjectivesVideo Client - Active ChannelsVideo Client - Multicast Channel RequestsVideo Client - VoD Channel RequestsVideo Client - Report SummaryVideo Client - Jitter DistributionVideo Client - Inter Packet Arrival Time DistributionVideo Client - Packet Latency DistributionVideo Client - Per StreamVideo Client - RTSP CommandsVideo Client - Data RatesVideo Client - LatencyVideo Client - Data ErrorsVideo Client - Error MessagesVideo Client - Packet Size DistributionVideo Server - Active StreamsVideo Server - RTSP TotalsVideo Server - Stream Bit RatesVideo Server - Data RatesVideo Server - Error Stats
            application_RTSP: Available only for IxNetwork TCL API with traffic_generator ixnetwork_540. Retrieves RTSP statitics for L4/L7 traffic. The statistics are retrieved from the following stat views. Available starting with HLT API 4.70. csv is the only supported return method for this mode. Retrieved Stat Views: RTSP Client - ObjectivesRTSP Client - Presentation RatesRTSP Client - PresentationsRTSP Client - LatenciesRTSP Client - Play Latency DistributionRTSP Client - RTP Jitter DistributionRTSP Client - RTP Packet Loss DistributionRTSP Client - Data RatesRTSP Client - TCP ConnectionsRTSP Client - TCP FailuresRTSP Server - Presentation RatesRTSP Server - PresentationsRTSP Server - Play latencyRTSP Server - Data RatesRTSP Server - Response CodesRTSP Server - TCP ConnectionsRTSP Server - TCP Failures
            L47_traffic_item: Available only for IxNetwork TCL API with traffic_generator ixnetwork_540. Retrieves L4-7 Applibrary traffic item statistics. The statistics are retrieved from the following stat views. Available starting with HLT API 4.80. Retrieved Stat Views: Application Traffic Item Statistics
            L47_flow_initiator: Available only for IxNetwork TCL API with traffic_generator ixnetwork_540. Retrieves L4-7 Applibrary traffic flow initiator statistics. The statistics are retrieved from the following stat views. Available starting with HLT API 4.80. Retrieved Stat Views: Application Flow Initiator Statistics
            L47_flow_responder: Available only for IxNetwork TCL API with traffic_generator ixnetwork_540. Retrieves L4-7 Applibrary traffic flow responder statistics. The statistics are retrieved from the following stat views. Available starting with HLT API 4.80. Retrieved Stat Views: Application Flow Responder Statistics
            L47_traffic_item_tcp: Available only for IxNetwork TCL API with traffic_generator ixnetwork_540. Retrieves L4-7 Applibrary traffic item TCP statistics. The statistics are retrieved from the following stat views. Available starting with HLT API 4.80. Retrieved Stat Views: Application Traffic Item TCP Statistics
            L47_flow_initiator_tcp: Available only for IxNetwork TCL API with traffic_generator ixnetwork_540. Retrieves L4-7 Applibrary traffic flow TCP initiator statistics. The statistics are retrieved from the following stat views. Available starting with HLT API 4.80. Retrieved Stat Views: Application Flow Initiator TCP Statistics
            L47_listening_port_tcp: Available only for IxNetwork TCL API with traffic_generator ixnetwork_540. Retrieves L4-7 Applibrary traffic flow TCP responder statistics. The statistics are retrieved from the following stat views. Available starting with HLT API 4.80. Retrieved Stat Views: Application Flow Responder TCP Statistics
        Constants Available: MODE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.traffic_stats({TrafficStatsConstants.MODE_CMD : opt})

    def traffic_stats_packet_group_id(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_stats_port_handle(self, port):
        """
        This is the method the command: traffic_stats option port_handle
        Description:Depending on the traffic_generator value, this option has different meanings. If traffic_generator ixnetwork_540 is used this parameter is used ixos/ixnetwork_540 - The port for which to configure traffic. Mandatory for -mode create/reset when -traffic_generator is set to ixos. For traffic_generator ixnetwork_540 this is mandatory on mode create only if parameter -emulation_src_handle is missing.ixnetwork/ixnetwork_540 - The port_handle parameter is not necessary anymore. When using IxNetwork, traffic configurations will be done using previously created handles (IP interfaces, PPP ranges, L2TP ranges, Protocol Route Ranges etc.) as sources (parameter -emulation_src_handle) and destinations (-emulation_dst_handle).
        Constants Available: PORT_HANDLE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        port --
        return -- pass/fail
        """
        return self.traffic_stats({TrafficStatsConstants.PORT_HANDLE_CMD : port})

    def traffic_stats_previous_data(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_stats_qos_stats(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_stats_return_method(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_stats_stream(self, stream_id):
        """
        This is the method the command: traffic_stats option stream
        Description:Stream ID on which to gather statistics (deprecated).Valid for traffic_generator ixos/ixnetwork/ixnetwork_540 and -mode set to stream/all. If traffic_generator is ixos, then the stream ID is a numeric value. If traffic_generator is ixnetwork/ixnetwork_540, then the stream ID is a string with the following regular expression: ^TI[0-9]+\-(.)*$.
        Constants Available: STREAM_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        stream_id --
        return -- pass/fail
        """
        return self.traffic_stats({TrafficStatsConstants.STREAM_CMD : stream_id})

    def traffic_stats_streams(self, streams_id):
        """
        This is the method the command: traffic_stats option streams
        Description:Stream ID on which to gather statistics.Valid for traffic_generator ixos/ixnetwork/ixnetwork_540 and -mode set to stream/all. The stream_id is the stream_id returned by traffic_config command. If traffic_generator is ixos, then the stream ID is a numeric value. If traffic_generator is ixnetwork/ixnetwork_540, then the stream ID is a string with the following regular expression: ^TI[0-9]+\-(.)*$.
        Constants Available: STREAMS_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        streams_id --
        return -- pass/fail
        """
        return self.traffic_stats({TrafficStatsConstants.STREAMS_CMD : streams_id})

    def traffic_stats_traffic_generator(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_action(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_l23ps_drilldown(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_l23ps_num_results(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_l23ps_sorting_statistic(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_l23ps_sorting_type(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_l23tf_aggregated_across_ports(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_l23tf_egress_latency_bin_display(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_l23tf_enumeration_sorting_type(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_l23tf_filter_type(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_l23tf_tracking_operator(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_l23tf_tracking_value(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_l23tfd_dead_flows_treshold(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_l23tfd_flow_type(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_l23tfd_show_egress_flows(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_l23tfd_statistic_all_flows_num_results(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_l23tfd_statistic_all_flows_sort_by(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_l23tfd_statistic_all_flows_sorting_type(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_l23tfd_statistic_dead_flows_num_results(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_l23tfd_statistic_dead_flows_sort_by(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_l23tfd_statistic_dead_flows_sorting_type(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_l23tfd_statistic_live_flows_num_results(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_l23tfd_statistic_live_flows_sort_by(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_l23tfd_statistic_live_flows_sorting_type(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_l23tfd_statistic_operator(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_l23tfd_statistic_value(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_l23tfd_tracking_operator(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_l23tfd_tracking_value(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_port_filter(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_port_filter_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_protocol_stack_filter(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_protocol_stack_filter_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_statistic_filter(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_statistic_filter_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_tracking_filter(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_tracking_filter_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_traffic_item_filter(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_traffic_item_filter_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_type(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_stats_vci(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_stats_vci_count(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_stats_vci_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_stats_vpi(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_stats_vpi_step(self, range):
        return self.logger.log_unimplemented_method()


"""
    This is the Constants class for the command: traffic_stats
    Commands end with _CMD and constants for a command start with the beginning
    with the command's constant name minus the _CMD
"""


class TrafficStatsConstants(object, metaclass=Singleton):
    # api reference constant for this api to get it from the device
    TRAFFIC_STATS_API = "TRAFFIC_STATS_API"

    ATM_COUNTER_VCI_DATA_ITEM_LIST_CMD = "atm_counter_vci_data_item_list"

    ATM_COUNTER_VCI_MODE_CMD = "atm_counter_vci_mode"
    # Constant values for ATM_COUNTER_VCI_MODE_CMD
    ATM_COUNTER_VCI_MODE_INCR = "incr"
    ATM_COUNTER_VCI_MODE_DECR = "decr"

    ATM_COUNTER_VCI_TYPE_CMD = "atm_counter_vci_type"
    # Constant values for ATM_COUNTER_VCI_TYPE_CMD
    ATM_COUNTER_VCI_TYPE_FIXED = "fixed"
    ATM_COUNTER_VCI_TYPE_COUNTER = "counter"
    ATM_COUNTER_VCI_TYPE_TABLE = "table"

    ATM_COUNTER_VPI_DATA_ITEM_LIST_CMD = "atm_counter_vpi_data_item_list"

    ATM_COUNTER_VPI_MODE_CMD = "atm_counter_vpi_mode"
    # Constant values for ATM_COUNTER_VPI_MODE_CMD
    ATM_COUNTER_VPI_MODE_INCR = "incr"
    ATM_COUNTER_VPI_MODE_DECR = "decr"

    ATM_COUNTER_VPI_TYPE_CMD = "atm_counter_vpi_type"
    # Constant values for ATM_COUNTER_VPI_TYPE_CMD
    ATM_COUNTER_VPI_TYPE_FIXED = "fixed"
    ATM_COUNTER_VPI_TYPE_COUNTER = "counter"
    ATM_COUNTER_VPI_TYPE_TABLE = "table"

    ATM_REASSEMBLY_ENABLE_IP_QOS_CMD = "atm_reassembly_enable_ip_qos"

    ATM_REASSEMBLY_ENABLE_IPTCPUDP_CHECKSUM_CMD = "atm_reassembly_enable_iptcpudp_checksum"

    ATM_REASSEMBLY_ENCAPSULATION_CMD = "atm_reassembly_encapsulation"
    # Constant values for ATM_REASSEMBLY_ENCAPSULATION_CMD
    ATM_REASSEMBLY_ENCAPSULATION_VCC_MUX_IPV4_ROUTED = "vcc_mux_ipv4_routed"
    ATM_REASSEMBLY_ENCAPSULATION_VCC_MUX_BRIDGED_ETH_FCS = "vcc_mux_bridged_eth_fcs"
    ATM_REASSEMBLY_ENCAPSULATION_VCC_MUX_BRIDGED_ETH_NO_FCS = "vcc_mux_bridged_eth_no_fcs"
    ATM_REASSEMBLY_ENCAPSULATION_VCC_MUX_IPV6_ROUTED = "vcc_mux_ipv6_routed"
    ATM_REASSEMBLY_ENCAPSULATION_VCC_MUX_MPLS_ROUTED = "vcc_mux_mpls_routed"
    ATM_REASSEMBLY_ENCAPSULATION_LLC_ROUTED_CLIP = "llc_routed_clip"
    ATM_REASSEMBLY_ENCAPSULATION_LLC_BRIDGED_ETH_FCS = "llc_bridged_eth_fcs"
    ATM_REASSEMBLY_ENCAPSULATION_LLC_BRIDGED_ETH_NO_FCS = "llc_bridged_eth_no_fcs"
    ATM_REASSEMBLY_ENCAPSULATION_LLC_PPPOA = "llc_pppoa"
    ATM_REASSEMBLY_ENCAPSULATION_VCC_MUX_PPOA = "vcc_mux_ppoa"
    ATM_REASSEMBLY_ENCAPSULATION_LLC_NLPID_ROUTED = "llc_nlpid_routed"

    CSV_PATH_CMD = "csv_path"

    DRILL_DOWN_FLOW_CMD = "drill_down_flow"

    DRILL_DOWN_LISTENING_PORT_CMD = "drill_down_listening_port"

    DRILL_DOWN_PORT_CMD = "drill_down_port"

    DRILL_DOWN_TRAFFIC_ITEM_CMD = "drill_down_traffic_item"

    DRILL_DOWN_TYPE_CMD = "drill_down_type"
    # Constant values for DRILL_DOWN_TYPE_CMD
    DRILL_DOWN_TYPE_PER_IPS = "per_ips"
    DRILL_DOWN_TYPE_PER_PORTS = "per_ports"
    DRILL_DOWN_TYPE_PER_INITIATOR_FLOWS = "per_initiator_flows"
    DRILL_DOWN_TYPE_PER_RESPONDER_FLOWS = "per_responder_flows"
    DRILL_DOWN_TYPE_PER_PORTS_PER_INITIATOR_FLOWS = "per_ports_per_initiator_flows"
    DRILL_DOWN_TYPE_PER_PORTS_PER_RESPONDER_FLOWS = "per_ports_per_responder_flows"
    DRILL_DOWN_TYPE_PER_PORTS_PER_INITIATOR_IPS = "per_ports_per_initiator_ips"
    DRILL_DOWN_TYPE_PER_PORTS_PER_RESPONDER_IPS = "per_ports_per_responder_ips"
    DRILL_DOWN_TYPE_PER_INITIATOR_FLOWS_PER_INITIATOR_PORTS = "per_initiator_flows_per_initiator_ports"
    DRILL_DOWN_TYPE_PER_RESPONDER_FLOWS_PER_RESPONDER_PORTS = "per_responder_flows_per_responder_ports"
    DRILL_DOWN_TYPE_PER_INITIATOR_FLOWS_PER_INITIATOR_IPS = "per_initiator_flows_per_initiator_ips"
    DRILL_DOWN_TYPE_PER_RESPONDER_FLOWS_PER_RESPONDER_IPS = "per_responder_flows_per_responder_ips"
    DRILL_DOWN_TYPE_PER_PORTS_PER_INITIATOR_FLOWS_PER_INITIATOR_IPS = "per_ports_per_initiator_flows_per_initiator_ips"
    DRILL_DOWN_TYPE_PER_PORTS_PER_RESPONDER_FLOWS_PER_RESPONDER_IPS = "per_ports_per_responder_flows_per_responder_ips"
    DRILL_DOWN_TYPE_PER_INITIATOR_FLOWS_PER_INITIATOR_PORTS_PER_INITIATOR_IPS = "per_initiator_flows_per_initiator_ports_per_initiator_ips"
    DRILL_DOWN_TYPE_PER_RESPONDER_FLOWS_PER_RESPONDER_PORTS_PER_RESPONDER_IPS = "per_responder_flows_per_responder_ports_per_responder_ips"
    DRILL_DOWN_TYPE_PER_INITIATOR_PORTS = "per_initiator_ports"
    DRILL_DOWN_TYPE_PER_INITIATOR_IPS = "per_initiator_ips"
    DRILL_DOWN_TYPE_PER_INITIATOR_PORTS_PER_INITIATOR_IPS = "per_initiator_ports_per_initiator_ips"
    DRILL_DOWN_TYPE_PER_RESPONDER_PORTS = "per_responder_ports"
    DRILL_DOWN_TYPE_PER_RESPONDER_IPS = "per_responder_ips"
    DRILL_DOWN_TYPE_PER_RESPONDER_PORTS_PER_RESPONDER_IPS = "per_responder_ports_per_responder_ips"
    DRILL_DOWN_TYPE_PER_LISTENING_PORTS = "per_listening_ports"
    DRILL_DOWN_TYPE_PER_LISTENING_PORTS_PER_RESPONDER_PORT = "per_listening_ports_per_responder_port"
    DRILL_DOWN_TYPE_PER_RESPONDER_PORT = "per_responder_port"
    DRILL_DOWN_TYPE_NONE = "none"

    EGRESS_MODE_CMD = "egress_mode"
    # Constant values for EGRESS_MODE_CMD
    EGRESS_MODE_CONDITIONAL = "conditional"
    EGRESS_MODE_PAGED = "paged"

    EGRESS_STATS_LIST_CMD = "egress_stats_list"

    IGNORE_RATE_CMD = "ignore_rate"

    MEASURE_MODE_CMD = "measure_mode"
    # Constant values for MEASURE_MODE_CMD
    MEASURE_MODE_CUMULATIVE = "cumulative"
    MEASURE_MODE_INSTANTANEOUS = "instantaneous"
    MEASURE_MODE_MIXED = "mixed"

    MODE_CMD = "mode"
    # Constant values for MODE_CMD
    MODE_ADD_ATM_STATS = "add_atm_stats"
    MODE_ADD_ATM_STATS_TX = "add_atm_stats_tx"
    MODE_ADD_ATM_STATS_RX = "add_atm_stats_rx"
    MODE_AGGREGATE = "aggregate"
    MODE_APPLICATION_FTP = "application_FTP"
    MODE_APPLICATION_HTTP = "application_HTTP"
    MODE_APPLICATION_IMAP = "application_IMAP"
    MODE_APPLICATION_POP3 = "application_POP3"
    MODE_APPLICATION_RTSP = "application_RTSP"
    MODE_APPLICATION_SIP = "application_SIP"
    MODE_APPLICATION_SMTP = "application_SMTP"
    MODE_APPLICATION_TELNET = "application_TELNET"
    MODE_APPLICATION_TRIPLEPLAY = "application_TriplePlay"
    MODE_APPLICATION_VIDEO = "application_Video"
    MODE_DATA_PLANE_PORT = "data_plane_port"
    MODE_EGRESS_BY_FLOW = "egress_by_flow"
    MODE_EGRESS_BY_PORT = "egress_by_port"
    MODE_FASTSTREAM = "faststream"
    MODE_FLOW = "flow"
    MODE_IGMP_OVER_PPP = "igmp_over_ppp"
    MODE_L23_TEST_SUMMARY = "l23_test_summary"
    MODE_MULTICAST = "multicast"
    MODE_OUT_OF_FILTER = "out_of_filter"
    MODE_PER_PORT_FLOWS = "per_port_flows"
    MODE_SESSION = "session"
    MODE_STREAM = "stream"
    MODE_STREAMS = "streams"
    MODE_TRAFFIC_ITEM = "traffic_item"
    MODE_USER_DEFINED_STATS = "user_defined_stats"
    MODE_ADD_ATM_STATS = "add_atm_stats"
    MODE_ADD_ATM_STATS_TX = "add_atm_stats_tx"
    MODE_ADD_ATM_STATS_RX = "add_atm_stats_rx"
    MODE_AGGREGATE = "aggregate"
    MODE_APPLICATION_FTP = "application_FTP"
    MODE_APPLICATION_HTTP = "application_HTTP"
    MODE_APPLICATION_IMAP = "application_IMAP"
    MODE_APPLICATION_POP3 = "application_POP3"
    MODE_APPLICATION_RTSP = "application_RTSP"
    MODE_APPLICATION_SIP = "application_SIP"
    MODE_APPLICATION_SMTP = "application_SMTP"
    MODE_APPLICATION_TELNET = "application_TELNET"
    MODE_APPLICATION_TRIPLEPLAY = "application_TriplePlay"
    MODE_APPLICATION_VIDEO = "application_Video"
    MODE_DATA_PLANE_PORT = "data_plane_port"
    MODE_EGRESS_BY_FLOW = "egress_by_flow"
    MODE_EGRESS_BY_PORT = "egress_by_port"
    MODE_FASTSTREAM = "faststream"
    MODE_FLOW = "flow"
    MODE_IGMP_OVER_PPP = "igmp_over_ppp"
    MODE_L23_TEST_SUMMARY = "l23_test_summary"
    MODE_MULTICAST = "multicast"
    MODE_OUT_OF_FILTER = "out_of_filter"
    MODE_PER_PORT_FLOWS = "per_port_flows"
    MODE_SESSION = "session"
    MODE_STREAM = "stream"
    MODE_STREAMS = "streams"
    MODE_TRAFFIC_ITEM = "traffic_item"
    MODE_USER_DEFINED_STATS = "user_defined_stats"
    MODE_ALL = "all"
    MODE_ADD_ATM_STATS = "add_atm_stats"
    MODE_ADD_ATM_STATS_TX = "add_atm_stats_tx"
    MODE_ADD_ATM_STATS_RX = "add_atm_stats_rx"
    MODE_AGGREGATE = "aggregate"
    MODE_APPLICATION_FTP = "application_FTP"
    MODE_APPLICATION_HTTP = "application_HTTP"
    MODE_APPLICATION_IMAP = "application_IMAP"
    MODE_APPLICATION_POP3 = "application_POP3"
    MODE_APPLICATION_RTSP = "application_RTSP"
    MODE_APPLICATION_SIP = "application_SIP"
    MODE_APPLICATION_SMTP = "application_SMTP"
    MODE_APPLICATION_TELNET = "application_TELNET"
    MODE_APPLICATION_TRIPLEPLAY = "application_TriplePlay"
    MODE_APPLICATION_VIDEO = "application_Video"
    MODE_DATA_PLANE_PORT = "data_plane_port"
    MODE_EGRESS_BY_FLOW = "egress_by_flow"
    MODE_EGRESS_BY_PORT = "egress_by_port"
    MODE_FASTSTREAM = "faststream"
    MODE_FLOW = "flow"
    MODE_IGMP_OVER_PPP = "igmp_over_ppp"
    MODE_L23_TEST_SUMMARY = "l23_test_summary"
    MODE_MULTICAST = "multicast"
    MODE_OUT_OF_FILTER = "out_of_filter"
    MODE_PER_PORT_FLOWS = "per_port_flows"
    MODE_SESSION = "session"
    MODE_STREAM = "stream"
    MODE_STREAMS = "streams"
    MODE_TRAFFIC_ITEM = "traffic_item"
    MODE_USER_DEFINED_STATS = "user_defined_stats"
    MODE_L47_TRAFFIC_ITEM = "L47_traffic_item"
    MODE_L47_FLOW_INITIATOR = "L47_flow_initiator"
    MODE_L47_FLOW_RESPONDER = "L47_flow_responder"
    MODE_L47_TRAFFIC_ITEM_TCP = "L47_traffic_item_tcp"
    MODE_L47_FLOW_INITIATOR_TCP = "L47_flow_initiator_tcp"
    MODE_L47_LISTENING_PORT_TCP = "L47_listening_port_tcp"

    PACKET_GROUP_ID_CMD = "packet_group_id"

    PORT_HANDLE_CMD = "port_handle"

    PREVIOUS_DATA_CMD = "previous_data"
    # Constant values for PREVIOUS_DATA_CMD
    PREVIOUS_DATA_KEEP = "keep"
    PREVIOUS_DATA_RESET = "reset"

    QOS_STATS_CMD = "qos_stats"

    RETURN_METHOD_CMD = "return_method"
    # Constant values for RETURN_METHOD_CMD
    RETURN_METHOD_KEYED_LIST = "keyed_list"
    RETURN_METHOD_KEYED_LIST_OR_ARRAY = "keyed_list_or_array"
    RETURN_METHOD_ARRAY = "array"
    RETURN_METHOD_CSV = "csv"

    STREAM_CMD = "stream"

    STREAMS_CMD = "streams"

    TRAFFIC_GENERATOR_CMD = "traffic_generator"
    # Constant values for TRAFFIC_GENERATOR_CMD
    TRAFFIC_GENERATOR_IXOS = "ixos"
    TRAFFIC_GENERATOR_IXNETWORK = "ixnetwork"

    UDS_ACTION_CMD = "uds_action"
    # Constant values for UDS_ACTION_CMD
    UDS_ACTION_GET_AVAILABLE_PORT_FILTERS = "get_available_port_filters"
    UDS_ACTION_GET_AVAILABLE_PROTOCOL_STACK_FILTERS = "get_available_protocol_stack_filters"
    UDS_ACTION_GET_AVAILABLE_TRAFFIC_ITEM_FILTERS = "get_available_traffic_item_filters"
    UDS_ACTION_GET_AVAILABLE_TRACKING_FILTERS = "get_available_tracking_filters"
    UDS_ACTION_GET_AVAILABLE_STATISTIC_FILTERS = "get_available_statistic_filters"
    UDS_ACTION_GET_AVAILABLE_STATS = "get_available_stats"
    UDS_ACTION_GET_STATS = "get_stats"

    UDS_L23PS_DRILLDOWN_CMD = "uds_l23ps_drilldown"
    # Constant values for UDS_L23PS_DRILLDOWN_CMD
    UDS_L23PS_DRILLDOWN_PER_SESSION = "per_session"
    UDS_L23PS_DRILLDOWN_PER_RANGE = "per_range"

    UDS_L23PS_NUM_RESULTS_CMD = "uds_l23ps_num_results"

    UDS_L23PS_SORTING_STATISTIC_CMD = "uds_l23ps_sorting_statistic"

    UDS_L23PS_SORTING_TYPE_CMD = "uds_l23ps_sorting_type"
    # Constant values for UDS_L23PS_SORTING_TYPE_CMD
    UDS_L23PS_SORTING_TYPE_ASCENDING = "ascending"
    UDS_L23PS_SORTING_TYPE_DESCENDING = "descending"

    UDS_L23TF_AGGREGATED_ACROSS_PORTS_CMD = "uds_l23tf_aggregated_across_ports"

    UDS_L23TF_EGRESS_LATENCY_BIN_DISPLAY_CMD = "uds_l23tf_egress_latency_bin_display"
    # Constant values for UDS_L23TF_EGRESS_LATENCY_BIN_DISPLAY_CMD
    UDS_L23TF_EGRESS_LATENCY_BIN_DISPLAY_NONE = "none"
    UDS_L23TF_EGRESS_LATENCY_BIN_DISPLAY_SHOW_EGRESS_FLAT_VIEW = "show_egress_flat_view"
    UDS_L23TF_EGRESS_LATENCY_BIN_DISPLAY_SHOW_EGRESS_ROWS = "show_egress_rows"
    UDS_L23TF_EGRESS_LATENCY_BIN_DISPLAY_SHOW_LATENCY_BIN_STATS = "show_latency_bin_stats"

    UDS_L23TF_ENUMERATION_SORTING_TYPE_CMD = "uds_l23tf_enumeration_sorting_type"
    # Constant values for UDS_L23TF_ENUMERATION_SORTING_TYPE_CMD
    UDS_L23TF_ENUMERATION_SORTING_TYPE_ASCENDING = "ascending"
    UDS_L23TF_ENUMERATION_SORTING_TYPE_DESCENDING = "descending"

    UDS_L23TF_FILTER_TYPE_CMD = "uds_l23tf_filter_type"
    # Constant values for UDS_L23TF_FILTER_TYPE_CMD
    UDS_L23TF_FILTER_TYPE_ENUMERATION = "enumeration"
    UDS_L23TF_FILTER_TYPE_TRACKING = "tracking"

    UDS_L23TF_TRACKING_OPERATOR_CMD = "uds_l23tf_tracking_operator"
    # Constant values for UDS_L23TF_TRACKING_OPERATOR_CMD
    UDS_L23TF_TRACKING_OPERATOR_IS_DIFFERENT = "is_different"
    UDS_L23TF_TRACKING_OPERATOR_IS_EQUAL = "is_equal"
    UDS_L23TF_TRACKING_OPERATOR_IS_EQUAL_OR_GREATER = "is_equal_or_greater"
    UDS_L23TF_TRACKING_OPERATOR_IS_EQUAL_OR_SMALLER = "is_equal_or_smaller"
    UDS_L23TF_TRACKING_OPERATOR_IS_GREATER = "is_greater"
    UDS_L23TF_TRACKING_OPERATOR_IS_SMALLER = "is_smaller"
    UDS_L23TF_TRACKING_OPERATOR_NULL = "null"

    UDS_L23TF_TRACKING_VALUE_CMD = "uds_l23tf_tracking_value"

    UDS_L23TFD_DEAD_FLOWS_TRESHOLD_CMD = "uds_l23tfd_dead_flows_treshold"

    UDS_L23TFD_FLOW_TYPE_CMD = "uds_l23tfd_flow_type"
    # Constant values for UDS_L23TFD_FLOW_TYPE_CMD
    UDS_L23TFD_FLOW_TYPE_ALL_FLOWS = "all_flows"
    UDS_L23TFD_FLOW_TYPE_LIVE_FLOWS = "live_flows"
    UDS_L23TFD_FLOW_TYPE_DEAD_FLOWS = "dead_flows"

    UDS_L23TFD_SHOW_EGRESS_FLOWS_CMD = "uds_l23tfd_show_egress_flows"

    UDS_L23TFD_STATISTIC_ALL_FLOWS_NUM_RESULTS_CMD = "uds_l23tfd_statistic_all_flows_num_results"

    UDS_L23TFD_STATISTIC_ALL_FLOWS_SORT_BY_CMD = "uds_l23tfd_statistic_all_flows_sort_by"

    UDS_L23TFD_STATISTIC_ALL_FLOWS_SORTING_TYPE_CMD = "uds_l23tfd_statistic_all_flows_sorting_type"
    # Constant values for UDS_L23TFD_STATISTIC_ALL_FLOWS_SORTING_TYPE_CMD
    UDS_L23TFD_STATISTIC_ALL_FLOWS_SORTING_TYPE_ASCENDING = "ascending"
    UDS_L23TFD_STATISTIC_ALL_FLOWS_SORTING_TYPE_DESCENDING = "descending"
    UDS_L23TFD_STATISTIC_ALL_FLOWS_SORTING_TYPE_NULL = "null"
    UDS_L23TFD_STATISTIC_ALL_FLOWS_SORTING_TYPE_WORST_PERFORMERS = "worst_performers"
    UDS_L23TFD_STATISTIC_ALL_FLOWS_SORTING_TYPE_BEST_PERFORMERS = "best_performers"

    UDS_L23TFD_STATISTIC_DEAD_FLOWS_NUM_RESULTS_CMD = "uds_l23tfd_statistic_dead_flows_num_results"

    UDS_L23TFD_STATISTIC_DEAD_FLOWS_SORT_BY_CMD = "uds_l23tfd_statistic_dead_flows_sort_by"

    UDS_L23TFD_STATISTIC_DEAD_FLOWS_SORTING_TYPE_CMD = "uds_l23tfd_statistic_dead_flows_sorting_type"
    # Constant values for UDS_L23TFD_STATISTIC_DEAD_FLOWS_SORTING_TYPE_CMD
    UDS_L23TFD_STATISTIC_DEAD_FLOWS_SORTING_TYPE_ASCENDING = "ascending"
    UDS_L23TFD_STATISTIC_DEAD_FLOWS_SORTING_TYPE_DESCENDING = "descending"
    UDS_L23TFD_STATISTIC_DEAD_FLOWS_SORTING_TYPE_NULL = "null"
    UDS_L23TFD_STATISTIC_DEAD_FLOWS_SORTING_TYPE_WORST_PERFORMERS = "worst_performers"
    UDS_L23TFD_STATISTIC_DEAD_FLOWS_SORTING_TYPE_BEST_PERFORMERS = "best_performers"

    UDS_L23TFD_STATISTIC_LIVE_FLOWS_NUM_RESULTS_CMD = "uds_l23tfd_statistic_live_flows_num_results"

    UDS_L23TFD_STATISTIC_LIVE_FLOWS_SORT_BY_CMD = "uds_l23tfd_statistic_live_flows_sort_by"

    UDS_L23TFD_STATISTIC_LIVE_FLOWS_SORTING_TYPE_CMD = "uds_l23tfd_statistic_live_flows_sorting_type"
    # Constant values for UDS_L23TFD_STATISTIC_LIVE_FLOWS_SORTING_TYPE_CMD
    UDS_L23TFD_STATISTIC_LIVE_FLOWS_SORTING_TYPE_ASCENDING = "ascending"
    UDS_L23TFD_STATISTIC_LIVE_FLOWS_SORTING_TYPE_DESCENDING = "descending"
    UDS_L23TFD_STATISTIC_LIVE_FLOWS_SORTING_TYPE_NULL = "null"
    UDS_L23TFD_STATISTIC_LIVE_FLOWS_SORTING_TYPE_WORST_PERFORMERS = "worst_performers"
    UDS_L23TFD_STATISTIC_LIVE_FLOWS_SORTING_TYPE_BEST_PERFORMERS = "best_performers"

    UDS_L23TFD_STATISTIC_OPERATOR_CMD = "uds_l23tfd_statistic_operator"
    # Constant values for UDS_L23TFD_STATISTIC_OPERATOR_CMD
    UDS_L23TFD_STATISTIC_OPERATOR_IS_DIFFERENT = "is_different"
    UDS_L23TFD_STATISTIC_OPERATOR_IS_EQUAL = "is_equal"
    UDS_L23TFD_STATISTIC_OPERATOR_IS_EQUAL_OR_GREATER = "is_equal_or_greater"
    UDS_L23TFD_STATISTIC_OPERATOR_IS_EQUAL_OR_SMALLER = "is_equal_or_smaller"
    UDS_L23TFD_STATISTIC_OPERATOR_IS_GREATER = "is_greater"
    UDS_L23TFD_STATISTIC_OPERATOR_IS_SMALLER = "is_smaller"
    UDS_L23TFD_STATISTIC_OPERATOR_NULL = "null"

    UDS_L23TFD_STATISTIC_VALUE_CMD = "uds_l23tfd_statistic_value"

    UDS_L23TFD_TRACKING_OPERATOR_CMD = "uds_l23tfd_tracking_operator"
    # Constant values for UDS_L23TFD_TRACKING_OPERATOR_CMD
    UDS_L23TFD_TRACKING_OPERATOR_IS_DIFFERENT = "is_different"
    UDS_L23TFD_TRACKING_OPERATOR_IS_EQUAL = "is_equal"
    UDS_L23TFD_TRACKING_OPERATOR_IS_EQUAL_OR_GREATER = "is_equal_or_greater"
    UDS_L23TFD_TRACKING_OPERATOR_IS_EQUAL_OR_SMALLER = "is_equal_or_smaller"
    UDS_L23TFD_TRACKING_OPERATOR_IS_GREATER = "is_greater"
    UDS_L23TFD_TRACKING_OPERATOR_IS_SMALLER = "is_smaller"
    UDS_L23TFD_TRACKING_OPERATOR_NULL = "null"

    UDS_L23TFD_TRACKING_VALUE_CMD = "uds_l23tfd_tracking_value"

    UDS_PORT_FILTER_CMD = "uds_port_filter"

    UDS_PORT_FILTER_COUNT_CMD = "uds_port_filter_count"

    UDS_PROTOCOL_STACK_FILTER_CMD = "uds_protocol_stack_filter"

    UDS_PROTOCOL_STACK_FILTER_COUNT_CMD = "uds_protocol_stack_filter_count"

    UDS_STATISTIC_FILTER_CMD = "uds_statistic_filter"

    UDS_STATISTIC_FILTER_COUNT_CMD = "uds_statistic_filter_count"

    UDS_TRACKING_FILTER_CMD = "uds_tracking_filter"

    UDS_TRACKING_FILTER_COUNT_CMD = "uds_tracking_filter_count"

    UDS_TRAFFIC_ITEM_FILTER_CMD = "uds_traffic_item_filter"

    UDS_TRAFFIC_ITEM_FILTER_COUNT_CMD = "uds_traffic_item_filter_count"

    UDS_TYPE_CMD = "uds_type"
    # Constant values for UDS_TYPE_CMD
    UDS_TYPE_L23_PROTOCOL_PORT = "l23_protocol_port"
    UDS_TYPE_L23_PROTOCOL_STACK = "l23_protocol_stack"
    UDS_TYPE_L23_TRAFFIC_FLOW = "l23_traffic_flow"
    UDS_TYPE_L23_TRAFFIC_FLOW_DETECTIVE = "l23_traffic_flow_detective"
    UDS_TYPE_L23_TRAFFIC_ITEM = "l23_traffic_item"
    UDS_TYPE_L23_TRAFFIC_PORT = "l23_traffic_port"

    VCI_CMD = "vci"

    VCI_COUNT_CMD = "vci_count"

    VCI_STEP_CMD = "vci_step"

    VPI_CMD = "vpi"

    VPI_STEP_CMD = "vpi_step"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass

"""
Implemented Commands (Alphabetical)
    -atm_counter_vci_data_item_list
    -atm_counter_vci_mode
    -atm_counter_vci_type
    -atm_counter_vpi_data_item_list
    -atm_counter_vpi_mode
    -atm_counter_vpi_type
    -atm_reassembly_enable_ip_qos
    -atm_reassembly_enable_iptcpudp_checksum
    -atm_reassembly_encapsulation
    -csv_path
    -drill_down_flow
    -drill_down_listening_port
    -drill_down_port
    -drill_down_traffic_item
    -drill_down_type
    -egress_mode
    -egress_stats_list
    -ignore_rate
    -measure_mode
    -mode
    -packet_group_id
    -port_handle
    -previous_data
    -qos_stats
    -return_method
    -stream
    -streams
    -traffic_generator
    -uds_action
    -uds_l23ps_drilldown
    -uds_l23ps_num_results
    -uds_l23ps_sorting_statistic
    -uds_l23ps_sorting_type
    -uds_l23tf_aggregated_across_ports
    -uds_l23tf_egress_latency_bin_display
    -uds_l23tf_enumeration_sorting_type
    -uds_l23tf_filter_type
    -uds_l23tf_tracking_operator
    -uds_l23tf_tracking_value
    -uds_l23tfd_dead_flows_treshold
    -uds_l23tfd_flow_type
    -uds_l23tfd_show_egress_flows
    -uds_l23tfd_statistic_all_flows_num_results
    -uds_l23tfd_statistic_all_flows_sort_by
    -uds_l23tfd_statistic_all_flows_sorting_type
    -uds_l23tfd_statistic_dead_flows_num_results
    -uds_l23tfd_statistic_dead_flows_sort_by
    -uds_l23tfd_statistic_dead_flows_sorting_type
    -uds_l23tfd_statistic_live_flows_num_results
    -uds_l23tfd_statistic_live_flows_sort_by
    -uds_l23tfd_statistic_live_flows_sorting_type
    -uds_l23tfd_statistic_operator
    -uds_l23tfd_statistic_value
    -uds_l23tfd_tracking_operator
    -uds_l23tfd_tracking_value
    -uds_port_filter
    -uds_port_filter_count
    -uds_protocol_stack_filter
    -uds_protocol_stack_filter_count
    -uds_statistic_filter
    -uds_statistic_filter_count
    -uds_tracking_filter
    -uds_tracking_filter_count
    -uds_traffic_item_filter
    -uds_traffic_item_filter_count
    -uds_type
    -vci
    -vci_count
    -vci_step
    -vpi
    -vpi_step
If you want to update this file, look in the CSV
"""
