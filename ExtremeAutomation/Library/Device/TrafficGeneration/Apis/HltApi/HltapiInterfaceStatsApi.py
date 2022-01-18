from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.TrafficGenerationApi import TrafficGenerationApi
from ExtremeAutomation.Library.Utils.Singleton import Singleton

"""
    This is the API class for the command: interface_stats

    Class is auto-generated. If you update anything here,
        it will be over written.
"""


class InterfaceStatsApi(TrafficGenerationApi):

    """
    init function
    """
    def __init__(self, device):
        super(InterfaceStatsApi, self).__init__(device)

    """
    This is the "One Large Method" for the command: interface_stats
    use this by passing in a dict() of all the commands
        dummyDict = dict()
        dummyDict[InterfaceStatsConstants.PORT_HANDLE_CMD] = "dummyValue1" # static value

        api = device.getApi(InterfaceStatsConstants.INTERFACE_STATS_API)
        api.interface_stats(dummyDict)
    """
    def interface_stats(self, argdictionary, supported = None):
        self.process_supported_hltapi_commands(argdictionary, supported)
        return self.send_command_args(self._nameSpace +"::interface_stats", argdictionary)

    """
    Individual commands for each option. Typically, the "One Large Method"
    is the one that you want to be using so look at that example above
    """
    def interface_stats_port_handle(self, port):
        """
        This is the method the command: interface_stats option port_handle
        Description:<port_handle>.<status>: $::SUCCESS | $::FAILURE
            <port_handle>.<log>: On status of failure, gives detailed information.
            <port_handle>.<intf_type>: same info as intf_mode of interface_config
            <port_handle>.<framing>: SONET or SDH, if applicable
            <port_handle>.<card_name>: official card name
            <port_handle>.<port_name>: official port name
            <port_handle>.<intf_speed>: same info as speed in interface_config
            <port_handle>.<tx_frames>: frames sent
            <port_handle>.<rx_frames>: frames received
            <port_handle>.<elapsed_time>: transmit duration
            <port_handle>.<rx_collisions>: collision frames received
            <port_handle>.<total_collisions>: total collisions
            <port_handle>.<duplex>: duplex value, full or half
            <port_handle>.<fcs_errors>: number of fcs errors
            <port_handle>.<late_collisions>: number of late collisions
            <port_handle>.<link>: link value representative of an IxTclHal enum
            <port_handle>.<phy_lane>.sync_header_lock: Indicates if the received PCS lane achieved sync-bit lock, where phy_lane is 0A-3A for ether40Gig ports or 0A-9A,0B-9B for ether100Gig ports
            <port_handle>.<phy_lane>.pcs_lane_marker_lock: Indicates if the received PCS lane has achieved alignment marker lock, where phy_lane is 0A-3A for ether40Gig ports or 0A-9A,0B-9B for ether100Gig ports
            <port_handle>.<phy_lane>.pcs_lane_marker_map: The PCS lane number identified by the alignment marker, where phy_lane is 0A-3A for ether40Gig ports or 0A-9A,0B-9B for ether100Gig ports
            <port_handle>.<phy_lane>.relative_lane_skew: Shows the actual skew in nanoseconds, where phy_lane is 0A-3A for ether40Gig ports or 0A-9A,0B-9B for ether100Gig ports
            <port_handle>.<phy_lane>.synk_header_error_count: The number of synchronization bit errors received, where phy_lane is 0A-3A for ether40Gig ports or 0A-9A,0B-9B for ether100Gig ports
            <port_handle>.<phy_lane>.pcs_lane_error_marker_count: The number of incorrect PCS lane markers received while in PCS lane lock state, where phy_lane is 0A-3A for ether40Gig ports or 0A-9A,0B-9B for ether100Gig ports
            <port_handle>.<phy_lane>.bip8_error_count: The number of BIP-8 errors for a PCS lane, where phy_lane is 0A-3A for ether40Gig ports or 0A-9A,0B-9B for ether100Gig ports
            <port_handle>.<phy_lane>.lost_sync_header_lock: Indicates the loss of sync header lock since the last statistic was read, where phy_lane is 0A-3A for ether40Gig ports or 0A-9A,0B-9B for ether100Gig ports
            <port_handle>.<phy_lane>.lost_pcs_lane_marker_lock: Indicates the loss of PCS lane marker lock since the last statistic was read, where phy_lane is 0A-3A for ether40Gig ports or 0A-9A,0B-9B for ether100Gig ports
            <port_handle>.pcs_sync_errors_received: For 40/100Gig PCS error generation.
            <port_handle>.pcs_illegal_codes_received: For 40/100Gig PCS error generation.
            <port_handle>.pcs_remote_faults_received: For 40/100Gig PCS error generation.
            <port_handle>.pcs_local_faults_received: For 40/100Gig PCS error generation.
            <port_handle>.pcs_illegal_ordered_set_received: For 40/100Gig PCS error generation.
            <port_handle>.pcs_illegal_idle_received: For 40/100Gig PCS error generation.
            <port_handle>.pcs_illegal_sof_received: For 40/100Gig PCS error generation.
            <port_handle>.pcs_out_of_order_sof_received: For 40/100Gig PCS error generation.
            <port_handle>.pcs_out_of_order_eof_received: For 40/100Gig PCS error generation.
            <port_handle>.pcs_out_of_order_data_received: For 40/100Gig PCS error generation.
            <port_handle>.pcs_out_of_order_ordered: For 40/100Gig PCS error generation.
            <port_handle>.<phy_lane>.bert_bits_sent: For BERT, indicates the total number of bits sent, where phy_lane is 0A-3A for ether40Gig ports or 0A-9A,0B-9B for ether100Gig ports
            <port_handle>.<phy_lane>.bert_bits_received: IFor BERT, indicates the total number of bits received, where phy_lane is 0A-3A for ether40Gig ports or 0A-9A,0B-9B for ether100Gig ports
            <port_handle>.<phy_lane>.bert_bit_errors_sent: For BERT, indicates the total number of bit errors sent., where phy_lane is 0A-3A for ether40Gig ports or 0A-9A,0B-9B for ether100Gig ports
            <port_handle>.<phy_lane>.bert_bit_error_received: For BERT,indicates the total number of bit errors received, where phy_lane is 0A-3A for ether40Gig ports or 0A-9A,0B-9B for ether100Gig ports
            <port_handle>.<phy_lane>.bert_pattern_lock: Indicates if the pattern is locked where phy_lane is 0A-3A for ether40Gig ports or 0A-9A,0B-9B for ether100Gig ports
            <port_handle>.<phy_lane>.bert_pattern_lock_lost: Indicates the Pattern Lock Lost value, where phy_lane is 0A-3A for ether40Gig ports or 0A-9A,0B-9B for ether100Gig ports
            <port_handle>.<phy_lane>.bert_bit_error_ratio: Indicates if the received PCS lane achieved sync-bit lock, where phy_lane is 0A-3A for ether40Gig ports or 0A-9A,0B-9B for ether100Gig ports
            <port_handle>.<phy_lane>.bert_number_mismatched_ones: For BERT, indicates the ratio of the number of errored bits compared to the total number of bits transmitted, where phy_lane is 0A-3A for ether40Gig ports or 0A-9A,0B-9B for ether100Gig ports
            <port_handle>.<phy_lane>.bert_mismatched_ones_ratio: Indicates the number of expected ones that where received as zeroes, where phy_lane is 0A-3A for ether40Gig ports or 0A-9A,0B-9B for ether100Gig ports
            <port_handle>.<phy_lane>.bert_number_mismatched_zeros: Indicates the ratio of mismatched zeroes to the total number of bits, where phy_lane is 0A-3A for ether40Gig ports or 0A-9A,0B-9B for ether100Gig ports
            <port_handle>.<phy_lane>.bert_mismatched_zeros_ratio: Indicates the ratio of mismatched ones to the total number of bits, where phy_lane is 0A-3A for ether40Gig ports or 0A-9A,0B-9B for ether100Gig ports
        Constants Available: PORT_HANDLE_CMD
        Supported:IxOS/IxNetwork-FT
        Keyword arguments:
        port --
        return -- pass/fail
        """
        return self.interface_stats({InterfaceStatsConstants.PORT_HANDLE_CMD : port})


"""
    This is the Constants class for the command: interface_stats
    Commands end with _CMD and constants for a command start with the beginning
    with the command's constant name minus the _CMD
"""


class InterfaceStatsConstants(object, metaclass=Singleton):
    # api reference constant for this api to get it from the device
    INTERFACE_STATS_API = "INTERFACE_STATS_API"

    PORT_HANDLE_CMD = "port_handle"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass


"""
Implemented Commands (Alphabetical)
    -port_handle
If you want to update this file, look in the CSV
"""
