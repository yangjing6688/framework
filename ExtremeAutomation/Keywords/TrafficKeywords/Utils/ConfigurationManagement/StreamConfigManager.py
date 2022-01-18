from ExtremeAutomation.Keywords.TrafficKeywords.Utils.ConfigurationManagement.TrafficPortConfigManager \
    import TrafficPortConfigManager


class StreamConfigManager(TrafficPortConfigManager):
    def __init__(self):
        super(StreamConfigManager, self).__init__()

    def add_stream_config(self, name_port_list, stream_number):
        """
        Adds the stream config to the Traffic Generator port, as the given stream number.
        """
        return super(StreamConfigManager, self)._add_config(name_port_list, stream_number, self._config_type_stream)

    def get_stream_config(self, name_port_list, stream_number):
        """
        Returns the stream config on the Traffic Generator port, for the given stream number.
        """
        return super(StreamConfigManager, self)._get_config(name_port_list, stream_number, self._config_type_stream)

    def get_all_streams_for_port(self, name_port_list):
        """
        Returns the stream config for all streams on the Traffic Generator port.
        """
        return super(StreamConfigManager, self)._get_all_configs_for_port(name_port_list, self._config_type_stream)

    def clear_port_streams(self, name_port_list):
        """
        Removes all streams from the Traffic Generator port.
        """
        super(StreamConfigManager, self)._clear_port_config_all(name_port_list, self._config_type_stream)

    def clear_stream(self, name_port_list, stream_number):
        """
        Removes only the given stream number from the Traffic Generator port.
        """
        super(StreamConfigManager, self)._clear_port_config_index(name_port_list, stream_number,
                                                                  self._config_type_stream)
