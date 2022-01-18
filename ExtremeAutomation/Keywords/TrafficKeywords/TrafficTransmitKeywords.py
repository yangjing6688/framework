import time
from ExtremeAutomation.Keywords.BaseClasses.TrafficKeywordBaseClass import TrafficKeywordBaseClass


class TrafficTransmitKeywords(TrafficKeywordBaseClass):
    def start_transmit_on_port(self, ports, delay_after=None, **kwargs):
        """
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [delay_after] - The amount of time to wait after starting the transmit. The default
                        value is 0 seconds.

        Starts transmitting streams on a given <tx_port>.
        """
        ports = self._validate_tgen_name_port_list(ports)

        self._init_keyword(**kwargs)

        for name_port_list in ports:
            self._get_traffic_generator_info(name_port_list)

            self.traffic_gen.start_traffic(self.current_port)

        if delay_after is not None:
            if delay_after.isdigit():
                time.sleep(int(delay_after))

        return self._keyword_cleanup()

    def start_transmit_on_port_and_wait(self, ports, max_wait="60", **kwargs):
        """
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [max_wait] - The maximum length the keyword should wait for the stream to complete.

        Starts transmitting streams on a given <tx_port> and waits for them to complete. This keyword should
        not be used if continuous streams have been configured.
        """
        ports = self._validate_tgen_name_port_list(ports)

        max_wait = int(max_wait) if str(max_wait).isdigit() else 600

        self._init_keyword(**kwargs)

        for name_port_list in ports:
            self._get_traffic_generator_info(name_port_list)
            self.traffic_gen.start_traffic_and_wait(self.current_port, max_wait * 1000)

        return self._keyword_cleanup()

    def stop_transmit_on_port(self, ports, **kwargs):
        """
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.

        Stops the transmitting streams on <tx_port>.
        """
        ports = self._validate_tgen_name_port_list(ports)

        self._init_keyword(**kwargs)

        for name_port_list in ports:
            self._get_traffic_generator_info(name_port_list)
            self.traffic_gen.stop_traffic(self.current_port)

        return self._keyword_cleanup()

    def stop_transmit_on_port_and_wait(self, ports, wait="1", **kwargs):
        """
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [wait] - How long to wait after stopping the transmit. The default value is 1 second.

        Stops the transmitting streams on <tx_port>.
        """
        ports = self._validate_tgen_name_port_list(ports)

        self._init_keyword(**kwargs)

        if wait.isdigit():
            wait = int(wait)
        else:
            self.logger.log_info("Invalid wait specified, defaulting to 1 second.")
            wait = 1

        for name_port_list in ports:
            self._get_traffic_generator_info(name_port_list)
            self.traffic_gen.stop_traffic(self.current_port)
            time.sleep(wait)

        return self._keyword_cleanup()
