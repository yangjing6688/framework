import time
from ExtremeAutomation.Keywords.BaseClasses.TrafficKeywordBaseClass import TrafficKeywordBaseClass


class TrafficStatisticsKeywords(TrafficKeywordBaseClass):
    def __init__(self):
        super(TrafficStatisticsKeywords, self).__init__()

        self.current_stats = {}
        self.current_stat_types = {}
        self.stat_constants = TrafficStatisticConstants()

    def get_rx_count(self, ports, **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.

        Stores a given traffic generator port's current receive count.
        Returns the stat values in a dictionary.
            Example: {'tgen1': {'1/2/10': 100,
                               {'1/2/11': 100},
                      'tgen2': {'1/2/10': 100)}
        """
        self._init_keyword(**kwargs)
        ports = self._validate_tgen_name_port_list(ports)
        port_stats = dict()

        for name_port_list in ports:
            self._get_traffic_generator_info(name_port_list)
            port_stats.setdefault(name_port_list['tgen_name'], {})[name_port_list['ifname']] = \
                self.__get_stat(self.stat_constants.rx_count, self.current_port)

        self._keyword_cleanup()
        return port_stats

    def get_rx_rate(self, ports, **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.

        Stores a given traffic generator port's current receive rate.
        Returns the stat values in a dictionary.
            Example: {'tgen1': {'1/2/10': 100,
                               {'1/2/11': 100},
                      'tgen2': {'1/2/10': 100)}
        """
        self._init_keyword(**kwargs)
        ports = self._validate_tgen_name_port_list(ports)
        port_stats = dict()

        for name_port_list in ports:
            self._get_traffic_generator_info(name_port_list)
            port_stats.setdefault(name_port_list['tgen_name'], {})[name_port_list['ifname']] = \
                self.__get_stat(self.stat_constants.rx_rate, self.current_port)

        self._keyword_cleanup()
        return port_stats

    def get_tx_count(self, ports, **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.

        Stores a given traffic generator port's current transmit count.
        Returns the stat values in a dictionary.
            Example: {'tgen1': {'1/2/10': 100,
                               {'1/2/11': 100},
                      'tgen2': {'1/2/10': 100)}
        """
        self._init_keyword(**kwargs)
        ports = self._validate_tgen_name_port_list(ports)
        port_stats = dict()

        for name_port_list in ports:
            self._get_traffic_generator_info(name_port_list)
            port_stats.setdefault(name_port_list['tgen_name'], {})[name_port_list['ifname']] = \
                self.__get_stat(self.stat_constants.tx_count, self.current_port)

        self._keyword_cleanup()
        return port_stats

    def get_tx_rate(self, ports, **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.

        Stores a given traffic generator port's current transmit rate.
        Returns the stat values in a dictionary.
            Example: {'tgen1': {'1/2/10': 100,
                               {'1/2/11': 100},
                      'tgen2': {'1/2/10': 100)}
        """
        self._init_keyword(**kwargs)
        ports = self._validate_tgen_name_port_list(ports)
        port_stats = dict()

        for name_port_list in ports:
            self._get_traffic_generator_info(name_port_list)
            port_stats.setdefault(name_port_list['tgen_name'], {})[name_port_list['ifname']] = \
                self.__get_stat(self.stat_constants.tx_rate, self.current_port)

        self._keyword_cleanup()
        return port_stats

    def get_captured_count(self, ports, **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.

        Stores a given traffic generator port's current captured packet count.
        Returns the stat values in a dictionary.
            Example: {'tgen1': {'1/2/10': 100,
                               {'1/2/11': 100},
                      'tgen2': {'1/2/10': 100)}
        """
        self._init_keyword(**kwargs)
        ports = self._validate_tgen_name_port_list(ports)
        port_stats = dict()

        for name_port_list in ports:
            self._get_traffic_generator_info(name_port_list)
            port_stats.setdefault(name_port_list['tgen_name'], {})[name_port_list['ifname']] = \
                self.__get_stat(self.stat_constants.capture_count, self.current_port)

        self._keyword_cleanup()
        return port_stats

    def get_captured_rate(self, ports, **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.

        Stores a given traffic generator port's current captured packet rate.
        Returns the stat values in a dictionary.
            Example: {'tgen1': {'1/2/10': 100,
                               {'1/2/11': 100},
                      'tgen2': {'1/2/10': 100)}
        """
        self._init_keyword(**kwargs)
        ports = self._validate_tgen_name_port_list(ports)
        port_stats = dict()

        for name_port_list in ports:
            self._get_traffic_generator_info(name_port_list)
            port_stats.setdefault(name_port_list['tgen_name'], {})[name_port_list['ifname']] = \
                self.__get_stat(self.stat_constants.capture_rate, self.current_port)

        self._keyword_cleanup()
        return port_stats

    def get_qos_count(self, ports, qos_index="0", **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [qos_index] - The QOS index that should be inspected. Valid indexes are 0-7.

        Stores QOS index N's packet count for a given traffic generator port.
        Returns the stat values in a dictionary.
            Example: {'tgen1': {'1/2/10': 100,
                               {'1/2/11': 100},
                      'tgen2': {'1/2/10': 100)}
        """
        self._init_keyword(**kwargs)
        ports = self._validate_tgen_name_port_list(ports)
        port_stats = dict()

        if qos_index.isdigit():
            if not 0 <= int(qos_index) <= 7:
                raise Exception("QOS index must be between 0-7.")
        else:
            raise Exception("QOS index must be a digit (0-7).")

        for name_port_list in ports:
            self._get_traffic_generator_info(name_port_list)
            qos_stat_constant = getattr(self.stat_constants, "qos_" + qos_index + "_count")
            port_stats.setdefault(name_port_list['tgen_name'], {})[name_port_list['ifname']] = \
                self.__get_stat(qos_stat_constant, self.current_port)

        self._keyword_cleanup()
        return port_stats

    def get_qos_rate(self, ports, qos_index="0", **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [qos_index] - The QOS index that should be inspected. Valid indexes are 0-7.

        Stores QOS index N's packet rate for a given traffic generator port.
        Returns the stat values in a dictionary.
            Example: {'tgen1': {'1/2/10': 100,
                               {'1/2/11': 100},
                      'tgen2': {'1/2/10': 100)}
        """
        self._init_keyword(**kwargs)
        ports = self._validate_tgen_name_port_list(ports)
        port_stats = dict()

        if qos_index.isdigit():
            if not 0 <= int(qos_index) <= 7:
                raise Exception("QOS index must be between 0-7.")
        else:
            raise Exception("QOS index must be a digit (0-7).")

        for name_port_list in ports:
            self._get_traffic_generator_info(name_port_list)
            qos_stat_constant = getattr(self.stat_constants, "qos_" + qos_index + "_rate")
            port_stats.setdefault(name_port_list['tgen_name'], {})[name_port_list['ifname']] = \
                self.__get_stat(qos_stat_constant, self.current_port)

        self._keyword_cleanup()
        return port_stats

    def get_uds1_count(self, ports, **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [qos_index] - The QOS index that should be inspected. Valid indexes are 0-7.

        Stores QOS index N's packet count for a given traffic generator port.
        Returns the stat values in a dictionary.
            Example: {'tgen1': {'1/2/10': 100,
                               {'1/2/11': 100},
                      'tgen2': {'1/2/10': 100)}
        """
        self._init_keyword(**kwargs)
        ports = self._validate_tgen_name_port_list(ports)
        port_stats = dict()

        for name_port_list in ports:
            self._get_traffic_generator_info(name_port_list)
            qos_stat_constant = getattr(self.stat_constants, "uds1_count")
            port_stats.setdefault(name_port_list['tgen_name'], {})[name_port_list['ifname']] = \
                self.__get_stat(qos_stat_constant, self.current_port)

        self._keyword_cleanup()
        return port_stats

    def get_uds2_count(self, ports, **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [qos_index] - The QOS index that should be inspected. Valid indexes are 0-7.

        Stores QOS index N's packet count for a given traffic generator port.
        Returns the stat values in a dictionary.
            Example: {'tgen1': {'1/2/10': 100,
                               {'1/2/11': 100},
                      'tgen2': {'1/2/10': 100)}
        """
        self._init_keyword(**kwargs)
        ports = self._validate_tgen_name_port_list(ports)
        port_stats = dict()

        for name_port_list in ports:
            self._get_traffic_generator_info(name_port_list)
            qos_stat_constant = getattr(self.stat_constants, "uds2_count")
            port_stats.setdefault(name_port_list['tgen_name'], {})[name_port_list['ifname']] = \
                self.__get_stat(qos_stat_constant, self.current_port)

        self._keyword_cleanup()
        return port_stats

    def get_current_stat(self, port, **kwargs):
        """
        Return the value of the currently stored stat value
        """
        self._init_keyword(**kwargs)
        self._get_traffic_generator_info(port)
        stat = self.current_stats[self.current_port]
        self._keyword_cleanup()

        return stat

    def stat_value_should_be_equal(self, ports, expected_value, **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [expected_value] - The value to compare against the stored value.

        Verifies that the stored statistic value is equal to the expected value.
        """
        self._init_keyword(**kwargs)
        ports = self._validate_tgen_name_port_list(ports)

        for name_port_list in ports:
            self._get_traffic_generator_info(name_port_list)

            result = (self.current_stats[self.current_port] == int(expected_value))

            self._determine_result(result, True,
                                   "Statistic value was " + str(self.current_stats[self.current_port]) +
                                   " which was equal to the expected value " + str(expected_value) + ".",
                                   "Statistic value was " + str(self.current_stats[self.current_port]) +
                                   " which was NOT equal to the expected value " + str(expected_value) + ".",**kwargs)

        return self._keyword_cleanup()

    def stat_value_should_be_less_than(self, ports, expected_value, **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [expected_value] - The value to compare against the stored value.

        Verifies that the stored statistic value is less than the expected value.
        """
        self._init_keyword(**kwargs)
        ports = self._validate_tgen_name_port_list(ports)

        for name_port_list in ports:
            self._get_traffic_generator_info(name_port_list)

            result = (self.current_stats[self.current_port] < int(expected_value))

            self._determine_result(result, True,
                                   "Statistic value was " + str(self.current_stats[self.current_port]) +
                                   " which was less than the expected value " + str(expected_value) + ".",
                                   "Statistic value was " + str(self.current_stats[self.current_port]) +
                                   " which was NOT less than the expected value " + str(expected_value) + ".",**kwargs)

        return self._keyword_cleanup()

    def stat_value_should_be_greater_than(self, ports, expected_value, **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [expected_value] - The value to compare against the stored value.

        Verifies that the stored statistic value is greater than the expected value.
        """
        self._init_keyword(**kwargs)
        ports = self._validate_tgen_name_port_list(ports)

        for name_port_list in ports:
            self._get_traffic_generator_info(name_port_list)

            result = (self.current_stats[self.current_port] > int(expected_value))

            self._determine_result(result, True,
                                   "Statistic value was " + str(self.current_stats[self.current_port]) +
                                   " which was greater than the expected value " + str(expected_value) + ".",
                                   "Statistic value was " + str(self.current_stats[self.current_port]) +
                                   " which was NOT greater than the expected value " + str(expected_value) + ".",**kwargs)

        return self._keyword_cleanup()

    def stat_value_should_be_greater_than_or_equal(self, ports, expected_value, **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [expected_value] - The value to compare against the stored value.

        Verifies that the stored statistic value is greater than or equal to the expected value.
        """
        self._init_keyword(**kwargs)
        ports = self._validate_tgen_name_port_list(ports)

        for name_port_list in ports:
            self._get_traffic_generator_info(name_port_list)

            result = (self.current_stats[self.current_port] >= int(expected_value))

            self._determine_result(result, True,
                                   "Statistic value was " + str(self.current_stats[self.current_port]) +
                                   " which was greater or equal to the expected value " +
                                   str(expected_value) + ".",
                                   "Statistic value was " + str(self.current_stats[self.current_port]) +
                                   " which was NOT greater or equal to the expected value " +
                                   str(expected_value) + ".",**kwargs)

        return self._keyword_cleanup()

    def stat_value_should_be_in_range(self, ports, expected_value_min, expected_value_max, **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [expected_value_min] - The minimum acceptable statistic value.
        [expected_value_max] - The maximum acceptable statistic value.

        Verifies that the stored statistic value is within the range of <expected_value_min>-<expected_value_max>.
        """
        self._init_keyword(**kwargs)
        ports = self._validate_tgen_name_port_list(ports)

        if int(expected_value_min) > int(expected_value_max):
            raise Exception("Minimum value must be less than maximum value.")

        for name_port_list in ports:
            self._get_traffic_generator_info(name_port_list)

            result = (int(expected_value_min) <= self.current_stats[self.current_port] <= int(expected_value_max))

            self._determine_result(result, True,
                                   "Statistic value was " + str(self.current_stats[self.current_port]) + " which was" +
                                   " within the range " + str(expected_value_min) + "-" +
                                   str(expected_value_max) + ".",
                                   "Statistic value was " + str(self.current_stats[self.current_port]) + " which was" +
                                   " NOT within the range " + str(expected_value_min) + "-" +
                                   str(expected_value_max) + ".",**kwargs)

        return self._keyword_cleanup()

    def stat_value_should_be_plus_or_minus(self, ports, expected_value, threshold, **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [expected_value] - The value to compare against the stored value.
        [threshold] - The number of packets the stored value must be within.
                      Example: (expected_value = 100, threshold = 5)
                               Stored value must be between 95-105 packets.

        Verifies that the stored statistic value is within +|- <threshold> packets of <expected_value>.
        """
        self._init_keyword(**kwargs)
        ports = self._validate_tgen_name_port_list(ports)

        expected_value_min = int(expected_value) - int(threshold)
        expected_value_max = int(expected_value) + int(threshold)

        for name_port_list in ports:
            self._get_traffic_generator_info(name_port_list)

            result = (expected_value_min <= self.current_stats[self.current_port] <= expected_value_max)

            self._determine_result(result, True,
                                   "Statistic value was " + str(self.current_stats[self.current_port]) + " which was" +
                                   " within +/- " + str(threshold) + " packets of expected value " +
                                   str(expected_value) + ".",
                                   "Statistic value was " + str(self.current_stats[self.current_port]) + " which was" +
                                   " NOT within +/- " + str(threshold) + " packets of expected value " +
                                   str(expected_value) + ".",**kwargs)

        return self._keyword_cleanup()

    def stat_value_should_be_plus_or_minus_percent(self, ports, expected_value, threshold, **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [expected_value] - The value to compare against the stored value.
        [threshold] - What percentage the stored value must be within in order to be considered a pass.
                      Example: (expected_value = 200, threshold = 10)
                               Stored value must be between 180-220 packets.

        Verifies that the stored statistic value is within +|- <threshold> percent of <expected_value>.
        """
        self._init_keyword(**kwargs)
        ports = self._validate_tgen_name_port_list(ports)

        expected_value_min = int(expected_value) - ((int(threshold) / 100.0) * int(expected_value))
        expected_value_max = int(expected_value) + ((int(threshold) / 100.0) * int(expected_value))

        for name_port_list in ports:
            self._get_traffic_generator_info(name_port_list)

            result = (expected_value_min <= self.current_stats[self.current_port] <= expected_value_max)

            self._determine_result(result, True,
                                   "Statistic value was " + str(self.current_stats[self.current_port]) + " which was" +
                                   " within +/- " + str(threshold) + "% of expected value " +
                                   str(expected_value) + ".",
                                   "Statistic value was " + str(self.current_stats[self.current_port]) + " which was" +
                                   " NOT within +/- " + str(threshold) + "% of expected value " +
                                   str(expected_value) + ".",**kwargs)

        return self._keyword_cleanup()

    def wait_for_stat_value_to_be_equal(self, ports, expected_value, max_wait="60", interval="5", **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [expected_value] - The value to compare against the stored value.
        [max_wait] - How long the keyword should run before being considered a fail.
        [interval] - How often the statistic value should be polled.

        Waits for a stored statistic value to be equal to the expected_value.
        """
        self._init_keyword(**kwargs)
        ports = self._validate_tgen_name_port_list(ports)
        result = False

        for name_port_list in ports:
            self._get_traffic_generator_info(name_port_list)

            start_time = time.time()
            current_time = time.time()

            while not result and (current_time - start_time) < int(max_wait):
                result = (self.current_stats[self.current_port] == int(expected_value))

                if not result:
                    self.logger.log_info("Statistic value was " + str(self.current_stats[self.current_port]) +
                                         " which did not equal " + str(expected_value) + "." +
                                         " Elapsed time: " + str(int(current_time - start_time)) + " seconds.")

                    self.__get_stat(self.current_stat_types[self.current_port], self.current_port)
                    time.sleep(int(interval))
                    current_time = time.time()

            self._determine_result(result, True,
                                   "Statistic value was " + str(self.current_stats[self.current_port]) +
                                   " which was equal to the expected value " + str(expected_value) + ".",
                                   "Statistic value was " + str(self.current_stats[self.current_port]) +
                                   " which was NOT equal to the expected value " + str(expected_value) + ".",**kwargs)

        return self._keyword_cleanup()

    def wait_for_stat_value_to_be_less_than(self, ports, expected_value, max_wait="60", interval="5", **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [expected_value] - The value to compare against the stored value.
        [max_wait] - How long the keyword should run before being considered a fail.
        [interval] - How often the statistic value should be polled.

        Waits for a stored statistic value to be less than the expected_value.
        """
        self._init_keyword(**kwargs)
        ports = self._validate_tgen_name_port_list(ports)
        result = False

        for name_port_list in ports:
            self._get_traffic_generator_info(name_port_list)

            start_time = time.time()
            current_time = time.time()

            while not result and (current_time - start_time) < int(max_wait):
                result = (self.current_stats[self.current_port] < int(expected_value))

                if not result:
                    self.logger.log_info("Statistic value was " + str(self.current_stats[self.current_port]) +
                                         " which was not less than " + str(expected_value) + "." +
                                         " Elapsed time: " + str(int(current_time - start_time)) + " seconds.")

                    self.__get_stat(self.current_stat_types[self.current_port], self.current_port)
                    time.sleep(int(interval))
                    current_time = time.time()

            self._determine_result(result, True,
                                   "Statistic value was " + str(self.current_stats[self.current_port]) +
                                   " which was less than the expected value " + str(expected_value) + ".",
                                   "Statistic value was " + str(self.current_stats[self.current_port]) +
                                   " which was NOT less than the expected value " + str(expected_value) + ".",**kwargs)

        return self._keyword_cleanup()

    def wait_for_stat_value_to_be_greater_than(self, ports, expected_value, max_wait="60", interval="5", **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [expected_value] - The value to compare against the stored value.
        [max_wait] - How long the keyword should run before being considered a fail.
        [interval] - How often the statistic value should be polled.

        Waits for a stored statistic value to be greater than the expected_value.
        """
        self._init_keyword(**kwargs)
        ports = self._validate_tgen_name_port_list(ports)
        result = False

        for name_port_list in ports:
            self._get_traffic_generator_info(name_port_list)

            start_time = time.time()
            current_time = time.time()

            while not result and (current_time - start_time) < int(max_wait):
                result = (self.current_stats[self.current_port] > int(expected_value))

                if not result:
                    self.logger.log_info("Statistic value was " + str(self.current_stats[self.current_port]) +
                                         " which was not greater than " + str(expected_value) + "." +
                                         " Elapsed time: " + str(int(current_time - start_time)) + " seconds.")

                    self.__get_stat(self.current_stat_types[self.current_port], self.current_port)
                    time.sleep(int(interval))
                    current_time = time.time()

            self._determine_result(result, True,
                                   "Statistic value was " + str(self.current_stats[self.current_port]) +
                                   " which was greater than the expected value " + str(expected_value) + ".",
                                   "Statistic value was " + str(self.current_stats[self.current_port]) +
                                   " which was NOT greater than the expected value " + str(expected_value) + ".",**kwargs)

        return self._keyword_cleanup()

    def wait_for_stat_value_to_be_greater_than_or_equal(self, ports, expected_value, max_wait="60", interval="5",
                                                        **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [expected_value] - The value to compare against the stored value.
        [max_wait] - How long the keyword should run before being considered a fail.
        [interval] - How often the statistic value should be polled.

        Waits for a stored statistic value to be greater than or equal to the expected_value.
        """
        self._init_keyword(**kwargs)
        ports = self._validate_tgen_name_port_list(ports)
        result = False

        for name_port_list in ports:
            self._get_traffic_generator_info(name_port_list)

            start_time = time.time()
            current_time = time.time()

            while not result and (current_time - start_time) < int(max_wait):
                result = (self.current_stats[self.current_port] >= int(expected_value))

                if not result:
                    self.logger.log_info("Statistic value was " + str(self.current_stats[self.current_port]) +
                                         " which was not greater or equal to " + str(expected_value) + "." +
                                         " Elapsed time: " + str(int(current_time - start_time)) + " seconds.")

                    self.__get_stat(self.current_stat_types[self.current_port], self.current_port)
                    time.sleep(int(interval))
                    current_time = time.time()

            self._determine_result(result, True,
                                   "Statistic value was " + str(self.current_stats[self.current_port]) +
                                   " which was greater or equal to the expected value " +
                                   str(expected_value) + ".",
                                   "Statistic value was " + str(self.current_stats[self.current_port]) +
                                   " which was NOT greater or equal to the expected value " +
                                   str(expected_value) + ".",**kwargs)

        return self._keyword_cleanup()

    def wait_for_stat_value_to_be_in_range(self, ports, expected_value_min, expected_value_max, max_wait="60",
                                           interval="1", **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [expected_value_min] - The minimum acceptable statistic value.
        [expected_value_max] - The maximum acceptable statistic value.
        [max_wait] - How long the keyword should run before being considered a fail.
        [interval] - How often the statistic value should be polled.

        Waits for the stored statistic value to be within the range of <expected_value_min>-<expected_value_max>.
        """
        self._init_keyword(**kwargs)
        ports = self._validate_tgen_name_port_list(ports)
        result = False

        if int(expected_value_min) > int(expected_value_max):
            raise Exception("Minimum value must be less than maximum value.")

        for name_port_list in ports:
            self._get_traffic_generator_info(name_port_list)

            start_time = time.time()
            current_time = time.time()

            while not result and (current_time - start_time) < int(max_wait):
                result = (int(expected_value_min) <= self.current_stats[self.current_port] <= int(expected_value_max))

                if not result:
                    self.logger.log_info("Statistic value was " + str(self.current_stats[self.current_port]) +
                                         " which was not in the range " + str(expected_value_min) + "-" +
                                         expected_value_max + "." + " Elapsed time: " +
                                         str(int(current_time - start_time)) + " seconds.")

                    self.__get_stat(self.current_stat_types[self.current_port], self.current_port)
                    time.sleep(int(interval))
                    current_time = time.time()

            self._determine_result(result, True,
                                   "Statistic value was " + str(self.current_stats[self.current_port]) + " which was" +
                                   " within the range " + str(expected_value_min) + "-" +
                                   str(expected_value_max) + ".",
                                   "Statistic value was " + str(self.current_stats[self.current_port]) + " which was" +
                                   " NOT within the range " + str(expected_value_min) + "-" +
                                   str(expected_value_max) + ".",**kwargs)

        return self._keyword_cleanup()

    def wait_for_stat_value_to_be_plus_or_minus(self, ports, expected_value, threshold, max_wait="60", interval="1",
                                                **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [expected_value] - The value to compare against the stored value.
        [threshold] - The number of packets the stored value must be within.
                      Example: (expected_value = 100, threshold = 5)
                               Stored value must be between 95-105 packets.
        [max_wait] - How long the keyword should run before being considered a fail.
        [interval] - How often the statistic value should be polled.

        Waits for the stored statistic value to be within +|- <threshold> packets of <expected_value>.
        """
        self._init_keyword(**kwargs)
        ports = self._validate_tgen_name_port_list(ports)
        result = False

        expected_value_min = int(expected_value) - int(threshold)
        expected_value_max = int(expected_value) + int(threshold)

        for name_port_list in ports:
            self._get_traffic_generator_info(name_port_list)

            start_time = time.time()
            current_time = time.time()

            while not result and (current_time - start_time) < int(max_wait):
                result = (int(expected_value_min) <= self.current_stats[self.current_port] <= int(expected_value_max))

                if not result:
                    self.logger.log_info("Statistic value was " + str(self.current_stats[self.current_port]) +
                                         " which was not within +/- " + str(threshold) + " packets of expected value " +
                                         expected_value + "." + " Elapsed time: " +
                                         str(int(current_time - start_time)) + " seconds.")

                    self.__get_stat(self.current_stat_types[self.current_port], self.current_port)
                    time.sleep(int(interval))
                    current_time = time.time()

            self._determine_result(result, True,
                                   "Statistic value was " + str(self.current_stats[self.current_port]) + " which was" +
                                   " within +/- " + str(threshold) + " packets of expected value " +
                                   expected_value + ".",
                                   "Statistic value was " + str(self.current_stats[self.current_port]) + " which was" +
                                   " NOT within +/- " + str(threshold) + " packets of expected value " +
                                   expected_value + ".",**kwargs)

        return self._keyword_cleanup()

    def wait_for_stat_value_to_be_plus_or_minus_percent(self, ports, expected_value, threshold, max_wait="60",
                                                        interval="1", **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [expected_value] - The value to compare against the stored value.
        [threshold] - What percentage the stored value must be within in order to be considered a pass.
                      Example: (expected_value = 200, threshold = 10)
                               Stored value must be between 180-220 packets.
        [max_wait] - How long the keyword should run before being considered a fail.
        [interval] - How often the statistic value should be polled.

        Waits for the stored statistic value to be within +|- <threshold> percent of <expected_value>.
        """
        self._init_keyword(**kwargs)
        ports = self._validate_tgen_name_port_list(ports)
        result = False

        expected_value_min = int(expected_value) - ((int(threshold) / 100.0) * int(expected_value))
        expected_value_max = int(expected_value) + ((int(threshold) / 100.0) * int(expected_value))

        for name_port_list in ports:
            self._get_traffic_generator_info(name_port_list)

            start_time = time.time()
            current_time = time.time()

            while not result and (current_time - start_time) < int(max_wait):
                result = (int(expected_value_min) <= self.current_stats[self.current_port] <= int(expected_value_max))

                if not result:
                    self.logger.log_info("Statistic value was " + str(self.current_stats[self.current_port]) +
                                         " which was not within +/- " + str(threshold) + " packets of expected value " +
                                         expected_value + "." + " Elapsed time: " +
                                         str(int(current_time - start_time)) + " seconds.")

                    self.__get_stat(self.current_stat_types[self.current_port], self.current_port)
                    time.sleep(int(interval))
                    current_time = time.time()

            self._determine_result(result, True,
                                   "Statistic value was " + str(self.current_stats[self.current_port]) + " which was" +
                                   " within +/- " + str(threshold) + "% of expected value " +
                                   expected_value + ".",
                                   "Statistic value was " + str(self.current_stats[self.current_port]) + " which was" +
                                   " NOT within +/- " + str(threshold) + "% of expected value " +
                                   expected_value + ".",**kwargs)

        return self._keyword_cleanup()

    def __get_stat(self, stat_constant, port):
        if stat_constant == self.stat_constants.rx_count:
            self.current_stats[port] = int(self.stats_helper.get_port_statistic_rx_raw_pkt_count(port))
            self.current_stat_types[port] = self.stat_constants.rx_count
        elif stat_constant == self.stat_constants.rx_rate:
            self.current_stats[port] = int(self.stats_helper.get_port_statistic_rx_raw_pkt_rate(port))
            self.current_stat_types[port] = self.stat_constants.rx_rate
        elif stat_constant == self.stat_constants.tx_count:
            self.current_stats[port] = int(self.stats_helper.get_port_statistic_tx_raw_pkt_count(port))
            self.current_stat_types[port] = self.stat_constants.tx_count
        elif stat_constant == self.stat_constants.tx_rate:
            self.current_stats[port] = int(self.stats_helper.get_port_statistic_tx_raw_pkt_rate(port))
            self.current_stat_types[port] = self.stat_constants.tx_rate
        elif stat_constant == self.stat_constants.capture_count:
            self.current_stats[port] = int(self.stats_helper.get_port_statistic_capture_filter_count(port))
            self.current_stat_types[port] = self.stat_constants.capture_count
        elif stat_constant == self.stat_constants.capture_rate:
            self.current_stats[port] = int(self.stats_helper.get_port_statistic_capture_filter_rate(port))
            self.current_stat_types[port] = self.stat_constants.capture_rate
        elif stat_constant == self.stat_constants.qos_0_count:
            self.current_stats[port] = int(self.stats_helper.get_port_statistic_rx_qos0_count(port))
            self.current_stat_types[port] = self.stat_constants.qos_0_count
        elif stat_constant == self.stat_constants.qos_0_rate:
            self.current_stats[port] = int(self.stats_helper.get_port_statistic_rx_qos0_rate(port))
            self.current_stat_types[port] = self.stat_constants.qos_0_rate
        elif stat_constant == self.stat_constants.qos_1_count:
            self.current_stats[port] = int(self.stats_helper.get_port_statistic_rx_qos1_count(port))
            self.current_stat_types[port] = self.stat_constants.qos_1_count
        elif stat_constant == self.stat_constants.qos_1_rate:
            self.current_stats[port] = int(self.stats_helper.get_port_statistic_rx_qos1_rate(port))
            self.current_stat_types[port] = self.stat_constants.qos_1_rate
        elif stat_constant == self.stat_constants.qos_2_count:
            self.current_stats[port] = int(self.stats_helper.get_port_statistic_rx_qos2_count(port))
            self.current_stat_types[port] = self.stat_constants.qos_2_count
        elif stat_constant == self.stat_constants.qos_2_rate:
            self.current_stats[port] = int(self.stats_helper.get_port_statistic_rx_qos2_rate(port))
            self.current_stat_types[port] = self.stat_constants.qos_2_rate
        elif stat_constant == self.stat_constants.qos_3_count:
            self.current_stats[port] = int(self.stats_helper.get_port_statistic_rx_qos3_count(port))
            self.current_stat_types[port] = self.stat_constants.qos_3_count
        elif stat_constant == self.stat_constants.qos_3_rate:
            self.current_stats[port] = int(self.stats_helper.get_port_statistic_rx_qos3_rate(port))
            self.current_stat_types[port] = self.stat_constants.qos_3_rate
        elif stat_constant == self.stat_constants.qos_4_count:
            self.current_stats[port] = int(self.stats_helper.get_port_statistic_rx_qos4_count(port))
            self.current_stat_types[port] = self.stat_constants.qos_4_count
        elif stat_constant == self.stat_constants.qos_4_rate:
            self.current_stats[port] = int(self.stats_helper.get_port_statistic_rx_qos4_rate(port))
            self.current_stat_types[port] = self.stat_constants.qos_4_rate
        elif stat_constant == self.stat_constants.qos_5_count:
            self.current_stats[port] = int(self.stats_helper.get_port_statistic_rx_qos5_count(port))
            self.current_stat_types[port] = self.stat_constants.qos_5_count
        elif stat_constant == self.stat_constants.qos_5_rate:
            self.current_stats[port] = int(self.stats_helper.get_port_statistic_rx_qos5_rate(port))
            self.current_stat_types[port] = self.stat_constants.qos_5_rate
        elif stat_constant == self.stat_constants.qos_6_count:
            self.current_stats[port] = int(self.stats_helper.get_port_statistic_rx_qos6_count(port))
            self.current_stat_types[port] = self.stat_constants.qos_6_count
        elif stat_constant == self.stat_constants.qos_6_rate:
            self.current_stats[port] = int(self.stats_helper.get_port_statistic_rx_qos6_rate(port))
            self.current_stat_types[port] = self.stat_constants.qos_6_rate
        elif stat_constant == self.stat_constants.qos_7_count:
            self.current_stats[port] = int(self.stats_helper.get_port_statistic_rx_qos7_count(port))
            self.current_stat_types[port] = self.stat_constants.qos_7_count
        elif stat_constant == self.stat_constants.qos_7_rate:
            self.current_stats[port] = int(self.stats_helper.get_port_statistic_rx_qos7_rate(port))
            self.current_stat_types[port] = self.stat_constants.qos_7_rate
        elif stat_constant == self.stat_constants.uds1_count:
            self.current_stats[port] = int(self.stats_helper.get_port_statistic_rx_uds1_count(port))
            self.current_stat_types[port] = self.stat_constants.uds1_count
        elif stat_constant == self.stat_constants.uds1_rate:
            self.current_stats[port] = int(self.stats_helper.get_port_statistic_rx_uds1_rate(port))
            self.current_stat_types[port] = self.stat_constants.uds1_rate
        elif stat_constant == self.stat_constants.uds2_count:
            self.current_stats[port] = int(self.stats_helper.get_port_statistic_rx_uds2_count(port))
            self.current_stat_types[port] = self.stat_constants.uds2_count
        elif stat_constant == self.stat_constants.uds1_rate:
            self.current_stats[port] = int(self.stats_helper.get_port_statistic_rx_uds2_rate(port))
            self.current_stat_types[port] = self.stat_constants.uds2_rate
        else:
            raise Exception(stat_constant + " is not a valid constant.\n" +
                            "Refer to TrafficStatisticConstants for valid constants.")
        return self.current_stats[port]


class TrafficStatisticConstants(object):
    rx_count = "rx_count"
    rx_rate = "rx_rate"
    tx_count = "tx_count"
    tx_rate = "tx_rate"
    capture_count = "capture_count"
    capture_rate = "capture_rate"
    qos_0_count = "qos_0_count"
    qos_0_rate = "qos_0_rate"
    qos_1_count = "qos_1_count"
    qos_1_rate = "qos_1_rate"
    qos_2_count = "qos_2_count"
    qos_2_rate = "qos_2_rate"
    qos_3_count = "qos_3_count"
    qos_3_rate = "qos_3_rate"
    qos_4_count = "qos_4_count"
    qos_4_rate = "qos_4_rate"
    qos_5_count = "qos_5_count"
    qos_5_rate = "qos_5_rate"
    qos_6_count = "qos_6_count"
    qos_6_rate = "qos_6_rate"
    qos_7_count = "qos_7_count"
    qos_7_rate = "qos_7_rate"
    uds1_count = "uds1_count"
    uds1_rate = "uds1_rate"
    uds2_count = "uds2_count"
    uds2_rate = "uds2_rate"

    # Don't allow values to be updated
    def __setattr__(self, *_):
        """Do NOT allow variables to be changed."""
        pass
