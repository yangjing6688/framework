from ExtremeAutomation.Library.Utils.FileUtils import FileUtils
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils
from ExtremeAutomation.Keywords.BaseClasses.TrafficKeywordBaseClass import TrafficKeywordBaseClass
from ExtremeAutomation.Keywords.TrafficKeywords.Utils.ConfigurationManagement.CaptureConfigManager \
    import CaptureConfigManager


class TrafficCaptureKeywords(TrafficKeywordBaseClass):
    _capture_configs = CaptureConfigManager()

    def clear_port_statistics(self, ports, **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.

        Clears all stats on a give <port>.
        """
        ports = self._validate_tgen_name_port_list(ports)

        self._init_keyword(**kwargs)

        for name_port_list in ports:
            self._get_traffic_generator_info(name_port_list)
            self.traffic_gen.clear_statistics(self.current_port)

        return self._keyword_cleanup()

    def clear_port_filters(self, ports, **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.

        Clears all capture filters on a given <port>.
        """
        ports = self._validate_tgen_name_port_list(ports)

        self._init_keyword(**kwargs)

        for name_port_list in ports:
            self._get_traffic_generator_info(name_port_list)
            self.traffic_gen.clear_capture_filters_and_triggers(self.current_port)

        return self._keyword_cleanup()

    def clear_port_stats_and_filters(self, ports, **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.

        Clears all capture filters and statistics on a given <port>.
        """
        self._init_keyword(**kwargs)

        self.clear_port_statistics(ports, log_keyword=False, **kwargs)
        self.clear_port_filters(ports, log_keyword=False, **kwargs)

    def configure_capture_da1(self, ports, da, mask=None, **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [da] - The DA that DA1 should be set to.
        [mask] - The mask to apply to the DA. This should be in the format "00:00:00:FF:FF:FF".

        Configures DA1 on a given traffic gen port.
        """
        ports = self._validate_tgen_name_port_list(ports)

        self._init_keyword(**kwargs)

        for name_port_list in ports:
            capture_config = self._capture_configs.get_capture_config(name_port_list)
            capture_config.da1 = StringUtils.normalize_mac(da)
            capture_config.da1_mask = mask

            if capture_config.da_mode is None:
                capture_config.da_mode = "da1"

        return self._keyword_cleanup()

    def configure_capture_da2(self, ports, da, mask=None, **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [da] - The DA that DA2 should be set to.
        [mask] - The mask to apply to the DA. This should be in the format "00:00:00:FF:FF:FF".

        Configures DA2 on a given traffic gen port.
        """
        ports = self._validate_tgen_name_port_list(ports)

        self._init_keyword(**kwargs)

        for name_port_list in ports:
            capture_config = self._capture_configs.get_capture_config(name_port_list)
            capture_config.da2 = StringUtils.normalize_mac(da)
            capture_config.da2_mask = mask

            if capture_config.da_mode is None:
                capture_config.da_mode = "da2"

        return self._keyword_cleanup()

    def configure_capture_da_mode(self, ports, da_mode, **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [da_mode] - The DA mode to configure. Valid Modes: any, da1, da2, !da1, !da2

        Configures the DA mode on a given traffic gen port.
        """
        ports = self._validate_tgen_name_port_list(ports)

        self._init_keyword(**kwargs)

        for name_port_list in ports:
            capture_config = self._capture_configs.get_capture_config(name_port_list)
            capture_config.da_mode = da_mode

        return self._keyword_cleanup()

    def configure_capture_da_uds1_mode(self, ports, da_mode, **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [da_mode] - The DA mode to configure. Valid Modes: any, da1, da2, !da1, !da2

        Configures the DA mode on a given traffic gen port.
        """
        ports = self._validate_tgen_name_port_list(ports)

        self._init_keyword(**kwargs)

        for name_port_list in ports:
            capture_config = self._capture_configs.get_capture_config(name_port_list)
            capture_config.da_uds1_mode = da_mode

        return self._keyword_cleanup()

    def configure_capture_da_uds2_mode(self, ports, da_mode, **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [da_mode] - The DA mode to configure. Valid Modes: any, da1, da2, !da1, !da2

        Configures the DA mode on a given traffic gen port.
        """
        ports = self._validate_tgen_name_port_list(ports)

        self._init_keyword(**kwargs)

        for name_port_list in ports:
            capture_config = self._capture_configs.get_capture_config(name_port_list)
            capture_config.da_uds2_mode = da_mode

        return self._keyword_cleanup()

    def configure_capture_sa1(self, ports, sa, mask=None, **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [sa] - The SA that SA1 should be set to.
        [mask] - The mask to apply to the SA. This should be in the format "00:00:00:FF:FF:FF".

        Configures SA1 on a given traffic gen port.
        """
        ports = self._validate_tgen_name_port_list(ports)

        self._init_keyword(**kwargs)

        for name_port_list in ports:
            capture_config = self._capture_configs.get_capture_config(name_port_list)
            capture_config.sa1 = StringUtils.normalize_mac(sa)
            capture_config.sa1_mask = mask

            if capture_config.sa_mode is None:
                capture_config.sa_mode = "sa1"

        return self._keyword_cleanup()

    def configure_capture_sa2(self, ports, sa, mask=None, **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [sa] - The SA that SA2 should be set to.
        [mask] - The mask to apply to the SA. This should be in the format "00:00:00:FF:FF:FF".

        Configures SA2 on a given traffic gen port.
        """
        ports = self._validate_tgen_name_port_list(ports)

        self._init_keyword(**kwargs)

        for name_port_list in ports:
            capture_config = self._capture_configs.get_capture_config(name_port_list)
            capture_config.sa2 = StringUtils.normalize_mac(sa)
            capture_config.sa2_mask = mask

            if capture_config.sa_mode is None:
                capture_config.sa_mode = "sa2"

        return self._keyword_cleanup()

    def configure_capture_sa_mode(self, ports, sa_mode, **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [sa_mode] - The SA mode to configure. Valid Modes: any, sa1, sa2, !sa1, !sa2

        Configures the SA mode on a given traffic gen port.
        """
        ports = self._validate_tgen_name_port_list(ports)

        self._init_keyword(**kwargs)

        for name_port_list in ports:
            capture_config = self._capture_configs.get_capture_config(name_port_list)
            capture_config.sa_mode = sa_mode

        return self._keyword_cleanup()

    def configure_capture_sa_uds1_mode(self, ports, sa_mode, **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [sa_mode] - The SA mode to configure. Valid Modes: any, sa1, sa2, !sa1, !sa2

        Configures the SA mode on a given traffic gen port.
        """
        ports = self._validate_tgen_name_port_list(ports)

        self._init_keyword(**kwargs)

        for name_port_list in ports:
            capture_config = self._capture_configs.get_capture_config(name_port_list)
            capture_config.sa_uds1_mode = sa_mode

    def configure_capture_sa_uds2_mode(self, ports, sa_mode, **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [sa_mode] - The SA mode to configure. Valid Modes: any, sa1, sa2, !sa1, !sa2

        Configures the SA mode on a given traffic gen port.
        """
        ports = self._validate_tgen_name_port_list(ports)

        self._init_keyword(**kwargs)

        for name_port_list in ports:
            capture_config = self._capture_configs.get_capture_config(name_port_list)
            capture_config.sa_uds2_mode = sa_mode

        return self._keyword_cleanup()

    def configure_capture_pattern1(self, ports, pattern, pattern_offset, pattern_mask=None, **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [pattern] - The pattern that pattern1 should be set to.
        [pattern_offset] - The value to assign to pattern1 offset.
        [pattern_mask] - The mask to apply to the pattern. This should be in the format "00FF00FF00".

        Configures pattern1 on a given traffic gen port.
        """
        ports = self._validate_tgen_name_port_list(ports)

        self._init_keyword(**kwargs)

        for name_port_list in ports:
            capture_config = self._capture_configs.get_capture_config(name_port_list)
            capture_config.pattern1 = pattern
            capture_config.pattern1_offset = pattern_offset
            capture_config.pattern1_mask = pattern_mask

            if capture_config.pattern_mode is None:
                capture_config.pattern_mode = "pattern1"

        return self._keyword_cleanup()

    def configure_capture_pattern2(self, ports, pattern, pattern_offset, pattern_mask=None, **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [pattern] - The pattern that pattern2 should be set to.
        [pattern_offset] - The value to assign to pattern2 offset.
        [pattern_mask] - The mask to apply to the pattern. This should be in the format "00FF00FF00".

        Configures pattern2 on a given traffic gen port.
        """
        ports = self._validate_tgen_name_port_list(ports)

        self._init_keyword(**kwargs)

        for name_port_list in ports:
            capture_config = self._capture_configs.get_capture_config(name_port_list)
            capture_config.pattern2 = pattern
            capture_config.pattern2_offset = pattern_offset
            capture_config.pattern2_mask = pattern_mask

            if capture_config.pattern_mode is None:
                capture_config.pattern_mode = "pattern2"

        return self._keyword_cleanup()

    def configure_capture_pattern_mode(self, ports, pattern_mode, **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [sa_mode] - The SA mode to configure.
                    Valid Modes: any, pattern1, pattern2, !pattern1, !pattern2, pattern1and2

        Configures the SA mode on a given traffic gen port.
        """
        ports = self._validate_tgen_name_port_list(ports)

        self._init_keyword(**kwargs)

        for name_port_list in ports:
            capture_config = self._capture_configs.get_capture_config(name_port_list)
            capture_config.pattern_mode = pattern_mode

        return self._keyword_cleanup()

    def configure_capture_pattern_uds1_mode(self, ports, pattern_mode, **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [sa_mode] - The SA mode to configure.
                    Valid Modes: any, pattern1, pattern2, !pattern1, !pattern2, pattern1and2

        Configures the SA mode on a given traffic gen port.
        """
        ports = self._validate_tgen_name_port_list(ports)

        self._init_keyword(**kwargs)

        for name_port_list in ports:
            capture_config = self._capture_configs.get_capture_config(name_port_list)
            capture_config.pattern_uds1_mode = pattern_mode

        return self._keyword_cleanup()

    def configure_capture_pattern_uds2_mode(self, ports, pattern_mode, **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [sa_mode] - The SA mode to configure.
                    Valid Modes: any, pattern1, pattern2, !pattern1, !pattern2, pattern1and2

        Configures the SA mode on a given traffic gen port.
        """
        ports = self._validate_tgen_name_port_list(ports)

        self._init_keyword(**kwargs)

        for name_port_list in ports:
            capture_config = self._capture_configs.get_capture_config(name_port_list)
            capture_config.pattern_uds2_mode = pattern_mode

        return self._keyword_cleanup()

    def start_uds1_stats_on_port(self, ports, **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.

        Starts user defined statistics on a given port with the applied configuration. If no configuration was added
        a usd for all DAs, SAs, and Patterns will be started.
        """
        return self.start_uds_stats_on_port(ports, True, False, **kwargs)

    def start_uds2_stats_on_port(self, ports, **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.

        Starts user defined statistics on a given port with the applied configuration. If no configuration was added
        a usd for all DAs, SAs, and Patterns will be started.
        """
        return self.start_uds_stats_on_port(ports, False, True, **kwargs)

    def start_uds_stats_on_port(self, ports, start_one, start_two, **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.

        Starts user defined statistics on a given port with the applied configuration. If no configuration was added
        a usd for all DAs, SAs, and Patterns will be started.
        """
        ports = self._validate_tgen_name_port_list(ports)

        self._init_keyword(**kwargs)

        for name_port_list in ports:
            self._get_traffic_generator_info(name_port_list)
            capture_config = self._capture_configs.get_capture_config(name_port_list)

            if capture_config is not None:
                if FileUtils.is_method_supported(self.capture_helper.get_capture_filter_default):
                    self.capture_helper.get_capture_filter_default()

                    if capture_config.da1 is not None:
                        self.capture_helper.add_capture_filter_da1(capture_config.da1, capture_config.da1_mask)
                    if capture_config.sa1 is not None:
                        self.capture_helper.add_capture_filter_sa1(capture_config.sa1, capture_config.sa1_mask)
                    if capture_config.da2 is not None:
                        self.capture_helper.add_capture_filter_da2(capture_config.da2, capture_config.da2_mask)
                    if capture_config.sa2 is not None:
                        self.capture_helper.add_capture_filter_sa2(capture_config.sa2, capture_config.sa2_mask)

                    if capture_config.pattern1 is not None:
                        self.capture_helper.add_capture_filter_pattern1(capture_config.pattern1,
                                                                        capture_config.pattern1_mask,
                                                                        capture_config.pattern1_offset, None,
                                                                        self.filter_constants.MATCH_TYPE1_USER)
                    if capture_config.pattern2 is not None:
                        self.capture_helper.add_capture_filter_pattern2(capture_config.pattern2,
                                                                        capture_config.pattern2_mask,
                                                                        capture_config.pattern2_offset, None,
                                                                        self.filter_constants.MATCH_TYPE1_USER)
                    self.capture_helper.write_capture_filter(self.current_port)

                    if start_two:
                        da_mode = (capture_config.da_uds2_mode if capture_config.da_uds2_mode is not None
                                   else self.trigger_consts.CAPTURE_TRIGGER_DA_ANY)
                        sa_mode = (capture_config.sa_uds2_mode if capture_config.sa_uds2_mode is not None
                                   else self.trigger_consts.CAPTURE_TRIGGER_SA_ANY)
                        pattern_mode = (capture_config.pattern_uds2_mode if capture_config.pattern_uds2_mode is not None
                                        else self.trigger_consts.CAPTURE_TRIGGER_PATTERN_ANY)
                        self.capture_helper.add_capture_trigger_capture_user_defined_statistics2(True, da_mode, sa_mode,
                                                                                                 pattern_mode,
                                                                                                 None, None, None, None)
                    if start_one:
                        da_mode = (capture_config.da_uds1_mode if capture_config.da_uds1_mode is not None
                                   else self.trigger_consts.CAPTURE_TRIGGER_DA_ANY)
                        sa_mode = (capture_config.sa_uds1_mode if capture_config.sa_uds1_mode is not None
                                   else self.trigger_consts.CAPTURE_TRIGGER_SA_ANY)
                        pattern_mode = (capture_config.pattern_uds1_mode if capture_config.pattern_uds1_mode is not None
                                        else self.trigger_consts.CAPTURE_TRIGGER_PATTERN_ANY)
                        self.capture_helper.add_capture_trigger_capture_user_defined_statistics1(True, da_mode, sa_mode,
                                                                                                 pattern_mode,
                                                                                                 None, None, None, None)
                    self.capture_helper.add_capture_trigger_capture_filter(True, da_mode, sa_mode, pattern_mode,
                                                                           None, None, None, None)
                    self.capture_helper.write_capture_trigger(self.current_port)
                    self._capture_configs.clear_capture_config(name_port_list)
            else:
                # No configuration exists for specified port, start a capture for DA: any, SA: any, Pattern: any.
                self.capture_helper.get_capture_filter_default()
                self.capture_helper.write_capture_filter(self.current_port)
                if start_two:
                    self.capture_helper.add_capture_trigger_capture_user_defined_statistics2(
                        True,
                        self.trigger_consts.CAPTURE_TRIGGER_DA_ANY,
                        self.trigger_consts.CAPTURE_TRIGGER_SA_ANY,
                        self.trigger_consts.CAPTURE_TRIGGER_PATTERN_ANY,
                        None, None, None, None)
                if start_one:
                    self.capture_helper.add_capture_trigger_capture_user_defined_statistics1(
                        True,
                        self.trigger_consts.CAPTURE_TRIGGER_DA_ANY,
                        self.trigger_consts.CAPTURE_TRIGGER_SA_ANY,
                        self.trigger_consts.CAPTURE_TRIGGER_PATTERN_ANY,
                        None, None, None, None)

                self.capture_helper.write_capture_trigger(self.current_port)

            # if self.debug_packet:
            #     self.capture_helper.get_capture_filter_and_trigger_settings(self.current_port)

        return self._keyword_cleanup()

    def start_capture_on_port(self, ports, **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.

        Starts a capture on a given port with the applied configuration. If no configuration was added
        a capture for all DAs, SAs, and Patterns will be started.
        """
        ports = self._validate_tgen_name_port_list(ports)

        self._init_keyword(**kwargs)

        for name_port_list in ports:
            self._get_traffic_generator_info(name_port_list)
            capture_config = self._capture_configs.get_capture_config(name_port_list)

            if capture_config is not None:
                if FileUtils.is_method_supported(self.capture_helper.get_capture_filter_default):
                    self.capture_helper.get_capture_filter_default()

                    if capture_config.da1 is not None:
                        self.capture_helper.add_capture_filter_da1(capture_config.da1, capture_config.da1_mask)
                    if capture_config.sa1 is not None:
                        self.capture_helper.add_capture_filter_sa1(capture_config.sa1, capture_config.sa1_mask)
                    if capture_config.da2 is not None:
                        self.capture_helper.add_capture_filter_da2(capture_config.da2, capture_config.da2_mask)
                    if capture_config.sa2 is not None:
                        self.capture_helper.add_capture_filter_sa2(capture_config.sa2, capture_config.sa2_mask)

                    if capture_config.pattern1 is not None:
                        self.capture_helper.add_capture_filter_pattern1(capture_config.pattern1,
                                                                        capture_config.pattern1_mask,
                                                                        capture_config.pattern1_offset, None,
                                                                        self.filter_constants.MATCH_TYPE1_USER)
                    if capture_config.pattern2 is not None:
                        self.capture_helper.add_capture_filter_pattern2(capture_config.pattern2,
                                                                        capture_config.pattern2_mask,
                                                                        capture_config.pattern2_offset, None,
                                                                        self.filter_constants.MATCH_TYPE1_USER)
                    self.capture_helper.write_capture_filter(self.current_port)

                    da_mode = (capture_config.da_mode if capture_config.da_mode is not None
                               else self.trigger_consts.CAPTURE_TRIGGER_DA_ANY)
                    sa_mode = (capture_config.sa_mode if capture_config.sa_mode is not None
                               else self.trigger_consts.CAPTURE_TRIGGER_SA_ANY)
                    pattern_mode = (capture_config.pattern_mode if capture_config.pattern_mode is not None
                                    else self.trigger_consts.CAPTURE_TRIGGER_PATTERN_ANY)

                    self.capture_helper.add_capture_trigger_capture_filter(True, da_mode, sa_mode, pattern_mode,
                                                                           None, None, None, None)
                    self.capture_helper.add_capture_trigger_capture_trigger(True, da_mode, sa_mode, pattern_mode,
                                                                            None, None, None, None)
                    self.capture_helper.write_capture_trigger(self.current_port)

                    self._capture_configs.clear_capture_config(name_port_list)
            else:
                # No configuration exists for specified port, start a capture for DA: any, SA: any, Pattern: any.
                self.capture_helper.get_capture_filter_default()
                self.capture_helper.write_capture_filter(self.current_port)
                self.capture_helper.add_capture_trigger_capture_filter(True,
                                                                       self.trigger_consts.CAPTURE_TRIGGER_DA_ANY,
                                                                       self.trigger_consts.CAPTURE_TRIGGER_SA_ANY,
                                                                       self.trigger_consts.CAPTURE_TRIGGER_PATTERN_ANY,
                                                                       None, None, None, None)
                self.capture_helper.add_capture_trigger_capture_trigger(True,
                                                                        self.trigger_consts.CAPTURE_TRIGGER_DA_ANY,
                                                                        self.trigger_consts.CAPTURE_TRIGGER_SA_ANY,
                                                                        self.trigger_consts.CAPTURE_TRIGGER_PATTERN_ANY,
                                                                        None, None, None, None)
                self.capture_helper.write_capture_trigger(self.current_port)

            if self.debug_packet:
                self.capture_helper.get_capture_filter_and_trigger_settings(self.current_port)

            self.traffic_gen.start_capture(self.current_port)

        return self._keyword_cleanup()

    def stop_capture_on_port(self, ports, **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.

        Stops the capture on a given traffic generator port.
        """
        ports = self._validate_tgen_name_port_list(ports)

        self._init_keyword(**kwargs)

        for name_port_list in ports:
            self._get_traffic_generator_info(name_port_list)
            self.traffic_gen.stop_capture(self.current_port)

            if self.debug_packet:
                self.logger.log_info(self.capture_helper.get_capture_filter_and_trigger_settings(self.current_port))
                self.logger.log_info(self.traffic_gen.get_filtered_captured_frames_report(self.current_port))

        return self._keyword_cleanup()

    def wait_for_capture_count_on_port(self, ports, expected_count, max_wait="60", **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [max_wait] - The maximum length the keyword should wait for the stream to complete.

        Stops the capture on a given traffic generator port.
        """
        ports = self._validate_tgen_name_port_list(ports)

        max_wait = int(max_wait) if str(max_wait).isdigit() else 600

        self._init_keyword(**kwargs)

        for name_port_list in ports:
            self._get_traffic_generator_info(name_port_list)
            self.traffic_gen.wait_for_capture_count_on_port(self.current_port, expected_count, max_wait * 1000)

        return self._keyword_cleanup()

    @staticmethod
    def __generate_pattern(pattern):
        if pattern is not None:
            pattern = pattern.replace(" ", "")

            if pattern.startswith("0x"):
                pattern = pattern.replace("0x", "")
            else:
                pattern = hex(int(pattern)).replace("0x", "")

            if len(pattern) % 2 != 0:
                pattern = "0" + pattern

            pattern = " ".join(pattern[i:i + 2] for i in range(0, len(pattern), 2))

            return pattern
