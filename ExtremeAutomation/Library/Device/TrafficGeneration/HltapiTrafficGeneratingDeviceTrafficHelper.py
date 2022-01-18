import abc
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficConfigApi import TrafficConfigApi, \
    TrafficConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.TrafficGeneratingDeviceTrafficHelper import \
    TrafficGeneratingDeviceTrafficHelper


class HltapiTrafficGeneratingDeviceTrafficHelper(TrafficGeneratingDeviceTrafficHelper, metaclass=abc.ABCMeta):
    def __init__(self, ixia_device):
        super(HltapiTrafficGeneratingDeviceTrafficHelper, self).__init__(ixia_device)

    def configure_stream_mac_dst_options(self, port_string, stream_id, addr, mode, count, step, seed, options=None):
        if options is None:
            options = {}
        port_string = self.convert_port_to_port_handle(port_string)
        options[TrafficConfigConstants.PORT_HANDLE_CMD] = port_string
        if stream_id:
            options[TrafficConfigConstants.STREAM_ID_CMD] = stream_id
        if addr:
            options[TrafficConfigConstants.MAC_DST_CMD] = addr
        if mode:
            options[TrafficConfigConstants.MAC_DST_MODE_CMD] = mode
        if count:
            options[TrafficConfigConstants.MAC_DST_COUNT_CMD] = count
        if step:
            options[TrafficConfigConstants.MAC_DST_STEP_CMD] = step
        if seed and 'Not Set' not in seed:
            options[TrafficConfigConstants.MAC_DST_SEED_CMD] = seed
        options[TrafficConfigConstants.MODE_CMD] = TrafficConfigConstants.MODE_MODIFY
        api = self.dev.get_api(TrafficConfigConstants.TRAFFIC_CONFIG_API)
        assert isinstance(api, TrafficConfigApi)
        ret_string = api.traffic_config(options)
        if 'no such element' in str(ret_string) or 'ERROR' in str(ret_string):
            options[TrafficConfigConstants.MODE_CMD] = TrafficConfigConstants.MODE_CREATE
            ret_string = api.traffic_config(options)

    def configure_stream_mac_src_options(self, port_string, stream_id, addr, mode, count, step, seed, options=None):
        if options is None:
            options = {}
        port_string = self.convert_port_to_port_handle(port_string)
        options[TrafficConfigConstants.PORT_HANDLE_CMD] = port_string
        if stream_id:
            options[TrafficConfigConstants.STREAM_ID_CMD] = stream_id
        if addr:
            options[TrafficConfigConstants.MAC_SRC_CMD] = addr
        if mode:
            options[TrafficConfigConstants.MAC_SRC_MODE_CMD] = mode
        if count:
            options[TrafficConfigConstants.MAC_SRC_COUNT_CMD] = count
        if step:
            options[TrafficConfigConstants.MAC_SRC_STEP_CMD] = step
        if seed and 'Not Set' not in seed:
            options[TrafficConfigConstants.MAC_SRC_SEED_CMD] = seed
        options[TrafficConfigConstants.MODE_CMD] = TrafficConfigConstants.MODE_MODIFY
        api = self.dev.get_api(TrafficConfigConstants.TRAFFIC_CONFIG_API)
        assert isinstance(api, TrafficConfigApi)
        ret_string = api.traffic_config(options)
        if 'no such element' in str(ret_string) or 'ERROR' in str(ret_string):
            options[TrafficConfigConstants.MODE_CMD] = TrafficConfigConstants.MODE_CREATE
            ret_string = api.traffic_config(options)

    def configure_stream_ip_dst_options(self, port_string, stream_id, addr, mode, count, step, options=None):
        if options is None:
            options = {}
        port_string = self.convert_port_to_port_handle(port_string)
        options[TrafficConfigConstants.PORT_HANDLE_CMD] = port_string
        if stream_id:
            options[TrafficConfigConstants.STREAM_ID_CMD] = stream_id
        if addr:
            options[TrafficConfigConstants.IP_DST_ADDR_CMD] = addr
        if mode:
            options[TrafficConfigConstants.IP_DST_MODE_CMD] = mode
        if count:
            options[TrafficConfigConstants.IP_DST_COUNT_CMD] = count
        if step:
            options[TrafficConfigConstants.IP_DST_STEP_CMD] = step
        options[TrafficConfigConstants.MODE_CMD] = TrafficConfigConstants.MODE_MODIFY
        api = self.dev.get_api(TrafficConfigConstants.TRAFFIC_CONFIG_API)
        assert isinstance(api, TrafficConfigApi)
        ret_string = api.traffic_config(options)
        if 'no such element' in str(ret_string) or 'ERROR' in str(ret_string):
            options[TrafficConfigConstants.MODE_CMD] = TrafficConfigConstants.MODE_CREATE
            ret_string = api.traffic_config(options)

    def configure_stream_ip_src_options(self, port_string, stream_id, addr, mode, count, step, options=None):
        if options is None:
            options = {}
        port_string = self.convert_port_to_port_handle(port_string)
        options[TrafficConfigConstants.PORT_HANDLE_CMD] = port_string
        if stream_id:
            options[TrafficConfigConstants.STREAM_ID_CMD] = stream_id
        if addr:
            options[TrafficConfigConstants.IP_SRC_ADDR_CMD] = addr
        if mode:
            options[TrafficConfigConstants.IP_SRC_MODE_CMD] = mode
        if count:
            options[TrafficConfigConstants.IP_SRC_COUNT_CMD] = count
        if step:
            options[TrafficConfigConstants.IP_SRC_STEP_CMD] = step
        options[TrafficConfigConstants.MODE_CMD] = TrafficConfigConstants.MODE_MODIFY
        api = self.dev.get_api(TrafficConfigConstants.TRAFFIC_CONFIG_API)
        assert isinstance(api, TrafficConfigApi)
        ret_string = api.traffic_config(options)
        if 'no such element' in str(ret_string) or 'ERROR' in str(ret_string):
            options[TrafficConfigConstants.MODE_CMD] = TrafficConfigConstants.MODE_CREATE
            ret_string = api.traffic_config(options)

    def configure_stream_ipv6_dst_options(self, port_string, stream_id, addr, mode, count, step, options=None):
        if options is None:
            options = {}
        port_string = self.convert_port_to_port_handle(port_string)
        options[TrafficConfigConstants.PORT_HANDLE_CMD] = port_string
        if stream_id:
            options[TrafficConfigConstants.STREAM_ID_CMD] = stream_id
        if addr:
            options[TrafficConfigConstants.IPV6_DST_ADDR_CMD] = addr
        if mode:
            options[TrafficConfigConstants.IPV6_DST_MODE_CMD] = mode
        if count:
            options[TrafficConfigConstants.IPV6_DST_COUNT_CMD] = count
        if step:
            options[TrafficConfigConstants.IPV6_DST_STEP_CMD] = step
        options[TrafficConfigConstants.MODE_CMD] = TrafficConfigConstants.MODE_MODIFY
        api = self.dev.get_api(TrafficConfigConstants.TRAFFIC_CONFIG_API)
        assert isinstance(api, TrafficConfigApi)
        ret_string = api.traffic_config(options)
        if 'no such element' in str(ret_string) or 'ERROR' in str(ret_string):
            options[TrafficConfigConstants.MODE_CMD] = TrafficConfigConstants.MODE_CREATE
            ret_string = api.traffic_config(options)

    def configure_stream_ipv6_src_options(self, port_string, stream_id, addr, mode, count, step, options=None):
        if options is None:
            options = {}
        port_string = self.convert_port_to_port_handle(port_string)
        options[TrafficConfigConstants.PORT_HANDLE_CMD] = port_string
        if stream_id:
            options[TrafficConfigConstants.STREAM_ID_CMD] = stream_id
        if addr:
            options[TrafficConfigConstants.IPV6_SRC_ADDR_CMD] = addr
        if mode:
            options[TrafficConfigConstants.IPV6_SRC_MODE_CMD] = mode
        if count:
            options[TrafficConfigConstants.IPV6_SRC_COUNT_CMD] = count
        if step:
            options[TrafficConfigConstants.IPV6_SRC_STEP_CMD] = step
        options[TrafficConfigConstants.MODE_CMD] = TrafficConfigConstants.MODE_MODIFY
        api = self.dev.get_api(TrafficConfigConstants.TRAFFIC_CONFIG_API)
        assert isinstance(api, TrafficConfigApi)
        ret_string = api.traffic_config(options)
        if 'no such element' in str(ret_string) or 'ERROR' in str(ret_string):
            options[TrafficConfigConstants.MODE_CMD] = TrafficConfigConstants.MODE_CREATE
            ret_string = api.traffic_config(options)

    def configure_stream_arp_sender_hardware_options(self, port_string, stream_id, addr, mode, count, options=None):
        if options is None:
            options = {}
        port_string = self.convert_port_to_port_handle(port_string)
        options[TrafficConfigConstants.PORT_HANDLE_CMD] = port_string
        if stream_id:
            options[TrafficConfigConstants.STREAM_ID_CMD] = stream_id
        if addr:
            options[TrafficConfigConstants.ARP_SRC_HW_ADDR_CMD] = addr
        if mode:
            options[TrafficConfigConstants.ARP_SRC_HW_MODE_CMD] = mode
        if count:
            options[TrafficConfigConstants.ARP_SRC_HW_COUNT_CMD] = count
        # if step:
        #     options[TrafficConfigConstants.ARP_SRC_HW_STEP_CMD] = step
        options[TrafficConfigConstants.MODE_CMD] = TrafficConfigConstants.MODE_MODIFY
        api = self.dev.get_api(TrafficConfigConstants.TRAFFIC_CONFIG_API)
        assert isinstance(api, TrafficConfigApi)
        ret_string = api.traffic_config(options)
        if 'no such element' in str(ret_string) or 'ERROR' in str(ret_string):
            options[TrafficConfigConstants.MODE_CMD] = TrafficConfigConstants.MODE_CREATE
            ret_string = api.traffic_config(options)

    def configure_stream_arp_target_hardware_options(self, port_string, stream_id, addr, mode, count, options=None):
        if options is None:
            options = {}
        port_string = self.convert_port_to_port_handle(port_string)
        options[TrafficConfigConstants.PORT_HANDLE_CMD] = port_string
        if stream_id:
            options[TrafficConfigConstants.STREAM_ID_CMD] = stream_id
        if addr:
            options[TrafficConfigConstants.ARP_DST_HW_ADDR_CMD] = addr
        if mode:
            options[TrafficConfigConstants.ARP_DST_HW_MODE_CMD] = mode
        if count:
            options[TrafficConfigConstants.ARP_DST_HW_COUNT_CMD] = count
        # if step:
        #     options[TrafficConfigConstants.ARP_DST_HW_STEP_CMD] = step
        options[TrafficConfigConstants.MODE_CMD] = TrafficConfigConstants.MODE_MODIFY
        api = self.dev.get_api(TrafficConfigConstants.TRAFFIC_CONFIG_API)
        assert isinstance(api, TrafficConfigApi)
        ret_string = api.traffic_config(options)
        if 'no such element' in str(ret_string) or 'ERROR' in str(ret_string):
            options[TrafficConfigConstants.MODE_CMD] = TrafficConfigConstants.MODE_CREATE
            ret_string = api.traffic_config(options)

    def configure_stream_fcs_dribble(self, port_string, stream_id, options=None):
        if options is None:
            options = {}
        options[TrafficConfigConstants.FCS_CMD] = 1
        options[TrafficConfigConstants.FCS_TYPE_CMD] = TrafficConfigConstants.FCS_TYPE_DRIBBLE
        self.__modify_hltapi_stream(port_string, stream_id, options)

    def configure_stream_fcs_alignment(self, port_string, stream_id, options=None):
        if options is None:
            options = {}
        options[TrafficConfigConstants.FCS_CMD] = 1
        options[TrafficConfigConstants.FCS_TYPE_CMD] = TrafficConfigConstants.FCS_TYPE_ALIGNMENT
        self.__modify_hltapi_stream(port_string, stream_id, options)

    def configure_stream_fcs_jabber(self, port_string, stream_id, options=None):
        if options is None:
            options = {}
        # options[TrafficConfigConstants.FCS_CMD] = 1
        # options[TrafficConfigConstants.FCS_TYPE_CMD] = TrafficConfigConstants.FCS_TYPE_
        # self.__modify_hltapi_stream(port_string, stream_id, options)
        return self.logger.log_unimplemented_method()

    def configure_stream_fcs_none(self, port_string, stream_id, options=None):
        if options is None:
            options = {}
        options[TrafficConfigConstants.FCS_CMD] = 1
        options[TrafficConfigConstants.FCS_TYPE_CMD] = TrafficConfigConstants.FCS_TYPE_NO_CRC
        self.__modify_hltapi_stream(port_string, stream_id, options)

    def configure_stream_fcs_bad_packet(self, port_string, stream_id, options=None):
        if options is None:
            options = {}
        options[TrafficConfigConstants.FCS_CMD] = 1
        options[TrafficConfigConstants.FCS_TYPE_CMD] = TrafficConfigConstants.FCS_TYPE_BAD_CRC
        self.__modify_hltapi_stream(port_string, stream_id, options)

    def configure_stream_fcs_good_packet(self, port_string, stream_id, options=None):
        if options is None:
            options = {}
        options[TrafficConfigConstants.FCS_CMD] = 0
        self.__modify_hltapi_stream(port_string, stream_id, options)

    def __modify_hltapi_stream(self, port_string, stream_id, options=None):
        if options is None:
            options = {}
        api = self.dev.get_api(TrafficConfigConstants.TRAFFIC_CONFIG_API)
        assert isinstance(api, TrafficConfigApi)
        options[TrafficConfigConstants.STREAM_ID_CMD] = stream_id
        options[TrafficConfigConstants.MODE_CMD] = TrafficConfigConstants.MODE_MODIFY
        ret_string = api.traffic_config(options)
        if 'no such element' in str(ret_string) or 'ERROR' in str(ret_string):
            options[TrafficConfigConstants.MODE_CMD] = TrafficConfigConstants.MODE_CREATE
            ret_string = api.traffic_config(options)
