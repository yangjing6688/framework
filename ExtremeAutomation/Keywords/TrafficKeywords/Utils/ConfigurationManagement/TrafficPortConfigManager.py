from ExtremeAutomation.Library.Logger.Logger import Logger
from ExtremeAutomation.Keywords.TrafficKeywords.Utils.ConfigurationManagement.StreamConfig import StreamConfig
from ExtremeAutomation.Keywords.TrafficKeywords.Utils.ConfigurationManagement.CaptureConfig import CaptureConfig


class TrafficPortConfigManager(object):
    _config_type_stream = "stream"
    _config_type_capture = "capture"

    _all_configs = {_config_type_stream: dict(),
                    _config_type_capture: dict()}

    def __init__(self):
        self.logger = Logger()
        self.current_tgen = None
        self.current_port = None

    def _create_config_object(self, tgen, port, index, config_type):
        if config_type == "stream":
            config = StreamConfig(tgen, port, index)
        elif config_type == "capture":
            config = CaptureConfig(tgen, port, index)
        else:
            self.logger.log_info("Invalid config type passed.")
            return None

        return config

    def _get_config_dict(self, config_type):
        if config_type in self._all_configs:
            return self._all_configs[config_type]
        else:
            self.logger.log_info("Invalid config type passed.")
            return None

    def _add_config(self, name_port_list, index, config_type):
        self.__get_current_tgen_name_and_port(name_port_list)

        config = self._create_config_object(self.current_tgen, self.current_port, index, config_type)
        config_dict = self._get_config_dict(config_type)

        if self.current_tgen in config_dict:
            if self.current_port in config_dict[self.current_tgen]:
                config_dict[self.current_tgen][self.current_port].append(config)
            else:
                config_dict[self.current_tgen][self.current_port] = [config]
        else:
            config_dict[self.current_tgen] = {self.current_port: [config]}

        return config

    def _get_config(self, name_port_list, index, config_type):
        self.__get_current_tgen_name_and_port(name_port_list)

        config_dict = self._get_config_dict(config_type)

        if self.current_tgen in config_dict:
            if self.current_port in config_dict[self.current_tgen]:
                for config in config_dict[self.current_tgen][self.current_port]:
                    if config.index == index:
                        return config
        # return None
        return self._add_config(name_port_list, index, config_type)

    def _get_all_configs_for_port(self, name_port_list, config_type):
        self.__get_current_tgen_name_and_port(name_port_list)

        config_dict = self._get_config_dict(config_type)

        if self.current_tgen in config_dict:
            if self.current_port in config_dict[self.current_tgen]:
                return config_dict[self.current_tgen][self.current_port]

        return None

    def _clear_port_config_all(self, name_port_list, config_type):
        self.__get_current_tgen_name_and_port(name_port_list)

        config_dict = self._get_config_dict(config_type)

        if self.current_tgen in config_dict:
            if self.current_port in config_dict[self.current_tgen]:
                config_dict[self.current_tgen][self.current_port] = list()

    def _clear_port_config_index(self, name_port_list, index, config_type):
        self.__get_current_tgen_name_and_port(name_port_list)

        config_dict = self._get_config_dict(config_type)

        if self.current_tgen in config_dict:
            if self.current_port in config_dict[self.current_tgen]:
                for i in range(len(config_dict[self.current_tgen][self.current_port])):
                    if config_dict[self.current_tgen][self.current_port][i].index == index:
                        config_dict[self.current_tgen][self.current_port].pop(i)
                        break

    def __get_current_tgen_name_and_port(self, name_port_list):
        self.current_tgen = name_port_list["tgen_name"]
        self.current_port = name_port_list["ifname"]
