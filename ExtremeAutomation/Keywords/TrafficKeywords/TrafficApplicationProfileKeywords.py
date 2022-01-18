import time
from ExtremeAutomation.Keywords.BaseClasses.TrafficKeywordBaseClass import TrafficKeywordBaseClass


class TrafficApplicationProfileKeywords(TrafficKeywordBaseClass):
    def upload_and_run_application_profile(self, tgen_name, config_path, delay_after=None, **kwargs):
        """
        [ports]       - This must be a dictionary which contains the name of the traffic generator and the
                        traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [config_path] - The path to the config file, including filename, from the Robot Engine.
        [delay_after] - The amount of time to wait after starting the transmit. The default
                        value is 0 seconds.

        Uploads and starts the application config on the selected ports.
        """
        # ports = self._validate_tgen_name_port_list(ports)
        self._init_keyword(tgen_name, **kwargs)
        # TBD at a later date: Changing the ports in the app config.
        # port_list = []
        # for name_port_list in ports:
        #     self._get_traffic_generator_info(name_port_list)
        #     port_list.append(self.current_port)
        # self.traffic_gen.update_ports()
        self.traffic_gen.run_config_file(config_path)

        if delay_after is not None:
            if delay_after.isdigit():
                time.sleep(int(delay_after))

        return self._keyword_cleanup()

    def verify_expected_results(self, tgen_name, location, search_string="failed", max_count=0, delay_after=None,
                                **kwargs):
        """
        [tgen_name] - The name of the tgen running the application traffic.
        [location]  - The location to download the results file.

        Downloads the application run's results and parses for failures.
        """
        self._init_keyword(tgen_name, **kwargs)

        self.traffic_gen.copy_results_file(location)
        self.traffic_gen.clean_up()

        result = self.traffic_gen.check_all_parsed_results_column_containing_value_greater_than(search_string,
                                                                                                max_count)

        if delay_after is not None:
            if delay_after.isdigit():
                time.sleep(int(delay_after))

        self._determine_result(result, False,**kwargs)

        return self._keyword_cleanup()
