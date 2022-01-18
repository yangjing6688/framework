from ExtremeAutomation.Keywords.BaseClasses.TrafficKeywordBaseClass import TrafficKeywordBaseClass


class TrafficProtocolConfigurationKeywords(TrafficKeywordBaseClass):

    def execute_tgen_protocol_config(self, tgen_name, file_path, test_name=None, user_name=None, **kwargs):
        """
        Keyword Arguments:
        tgen_name - The name of the Traffic Generation Device.
        file_path - The path to the configuration file on the Robot Engine.
        """
        self._init_keyword(tgen_name, **kwargs)

        test_name = test_name if not None else "Test Name"
        user_name = user_name if not None else "Test Engineer"

        dev = self.device_collection.get_device(tgen_name)
        dev.run_config_file(file_path, test_name, user_name)

        return self._keyword_cleanup()
