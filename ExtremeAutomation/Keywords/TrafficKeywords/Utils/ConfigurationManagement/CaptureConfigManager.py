from ExtremeAutomation.Keywords.TrafficKeywords.Utils.ConfigurationManagement.TrafficPortConfigManager \
    import TrafficPortConfigManager


class CaptureConfigManager(TrafficPortConfigManager):
    def __init__(self):
        super(CaptureConfigManager, self).__init__()

        # There should only be one CaptureInfo object per port, so index is always 0.
        self._index = "0"

    def add_capture_config(self, name_port_list):
        """
        Adds the capture config to the Traffic Generator port.
        """
        return super(CaptureConfigManager, self)._add_config(name_port_list, self._index, self._config_type_capture)

    def get_capture_config(self, name_port_list):
        """
        Returns the capture config applied on the Traffic Generator port.
        """
        return super(CaptureConfigManager, self)._get_config(name_port_list, self._index, self._config_type_capture)

    def clear_capture_config(self, name_port_list):
        """
        Clears the capture config on the Traffic Generator port to defaults.
        """
        super(CaptureConfigManager, self)._clear_port_config_index(name_port_list, self._index,
                                                                   self._config_type_capture)
