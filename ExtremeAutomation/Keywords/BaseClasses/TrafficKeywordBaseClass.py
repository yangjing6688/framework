from ExtremeAutomation.Library.Utils.StringUtils import StringUtils
from ExtremeAutomation.Keywords.FailureException import FailureException
from ExtremeAutomation.Keywords.BaseClasses.KeywordResult import KeywordResult
from ExtremeAutomation.Keywords.BaseClasses.CompareResults import CompareResults
from ExtremeAutomation.Keywords.BaseClasses.KeywordBaseClass import KeywordBaseClass
from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.TrafficGenConstants import TrafficGenConstants
from ExtremeAutomation.Keywords.TrafficKeywords.Utils.PacketUtils.PacketDictionary import PacketDictionary
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficConfigApi \
    import TrafficConfigConstants
from ExtremeAutomation.Keywords.TrafficKeywords.Utils.Constants.PacketDefaultConstants \
    import PacketDefaultConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiPacketConfigFilterApi \
    import PacketConfigFilterConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiPacketConfigTriggersApi \
    import PacketConfigTriggersConstants


class TrafficKeywordBaseClass(KeywordBaseClass):
    def __init__(self):
        super(TrafficKeywordBaseClass, self).__init__()

        self.debug_packet = False
        self.traffic_gen_constants = TrafficGenConstants()
        self.config_constants = TrafficConfigConstants()
        self.filter_constants = PacketConfigFilterConstants()
        self.trigger_consts = PacketConfigTriggersConstants()
        self.pkt_defaults = PacketDefaultConstants()
        self.pkt_dict = PacketDictionary()
        self.packet = None
        self.current_port = None
        self.phy_mode = None
        self.kw_results = []

    def _init_keyword(self, device_name=None, emulation_api_const=None, **kwargs):
        if device_name is not None:
            self.traffic_gen = super(TrafficKeywordBaseClass, self)._init_keyword(device_name=device_name, **kwargs)
        elif hasattr(self, 'device_name') and self.device_name is not None:
            self.traffic_gen = super(TrafficKeywordBaseClass, self)._init_keyword(device_name=self.device_name,
                                                                                  **kwargs)
        else:
            self.traffic_gen = super(TrafficKeywordBaseClass, self)._init_keyword(device_name=device_name, **kwargs)

        if self.traffic_gen and "jetsdevice" in type(self.traffic_gen).__name__.lower():
            if "view_tag" in kwargs:
                self.traffic_gen.set_view_tag(kwargs["view_tag"])
            if "jets_dir" in kwargs:
                self.traffic_gen.set_jets_directory(kwargs["jets_dir"])

        if emulation_api_const is not None:
            try:
                self.emulation_api = self.traffic_gen.get_api(emulation_api_const)
            except AttributeError:
                self.logger.log_info("No Traffic Generator " + self.device_name + " found.")

        if self.traffic_gen is not None:
            self.capture_helper = self.traffic_gen.get_capture_helper()
            self.stats_helper = self.traffic_gen.get_statistic_helper()
            self.traffic_helper = self.traffic_gen.get_traffic_helper()
        return self

    def _get_traffic_generator_info(self, tgen_port_dict):
        """
        Arguments:
        [name_and_port_list] - This must be a list which contains the name of the traffic generator and the
                  traffic generator port. Example ["tgen_1", "1/1/11"].
        """
        if isinstance(tgen_port_dict, dict):
            try:
                self.device_name = tgen_port_dict["tgen_name"]
                self.current_port = tgen_port_dict["ifname"]
                self.phy_mode = tgen_port_dict.get("phy_mode", None)
                self.traffic_gen = self.device_collection.get_device(self.device_name)
            except KeyError:
                self.logger.log_error("Traffic generator port dictionary should follow template.")

            if self.traffic_gen is not None:
                self.capture_helper = self.traffic_gen.get_capture_helper()
                self.stats_helper = self.traffic_gen.get_statistic_helper()
                self.traffic_helper = self.traffic_gen.get_traffic_helper()
        else:
            raise Exception("name_and_port_list must be dictionary, received type " + str(type(tgen_port_dict)) +
                            " instead.")

    def _determine_result(self, result, expected_result, pass_string=None, fail_string=None, **kwargs):
        compare_results = CompareResults()

        if pass_string is None:
            pass_string = "Keyword Passed"
        if fail_string is None:
            fail_string = "Keyword Failed"
            
        expect_error = self.get_kwarg_bool(kwargs, "expect_error", False)

        test_result = compare_results.compare_results(result, expected_result)
        
        if expect_error and not test_result:
            test_result = True
        elif expect_error and test_result:
            test_result = False
    
        kw_result = KeywordResult(self.device_name, test_result, pass_string, fail_string, None)
        self.kw_results.append(kw_result)

    def _keyword_cleanup(self):
        keyword_failed = False
        self.expect_error = False
        self.capture_length = None
        self.current_port = None

        for kw_result in self.kw_results:
            if not isinstance(kw_result, KeywordResult):
                self.logger.log_error("Keyword Result class KeywordResult:" + str(self.kw_results))
            kw_result.print_kw_result()
            if not kw_result.test_result and not keyword_failed:
                keyword_failed = True

        self.kw_results = list()

        if keyword_failed:
            if self.DEBUG:
                self._pause()
            raise FailureException("!!! Keyword Failed !!!")

        super(TrafficKeywordBaseClass, self).log_keyword_result(keyword_failed)

    def _parse_kwargs(self, dev, **kwargs):
        super(TrafficKeywordBaseClass, self)._parse_kwargs(kwargs)

        self.debug_packet = StringUtils.string_to_boolean(kwargs.get("debug_packet", False))

        if "jets_dir" in kwargs:
            dev.jets_dir = kwargs.get("jets_dir", None)
            dev.view_tag = kwargs.get("view_tag", None)

    @staticmethod
    def _validate_tgen_name_port_list(name_port_list):
        if not isinstance(name_port_list, list):
            return [name_port_list]
        else:
            return name_port_list
