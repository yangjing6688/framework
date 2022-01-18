from ExtremeAutomation.Keywords.BaseClasses.EndsystemKeywordBaseClass import EndsystemKeywordBaseClass


class EndsystemMultiAuthMethodClientKeywords(EndsystemKeywordBaseClass):
    def execute_multiuser_config(self, device_name, config_filename, adapter, pwa_server_ip="1.1.1.1", **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [config_filename] - The name of the configuration file that will be used.
        [adapter] - The number of the adapter that will be used.
        [pwa_server] - IP of the pwa server if needed in test.

        Valid **kwargs:
        [ignore_cli_feedback] - If set to True CLI feedback is ignored.
        [expect_error] - Used for negative testing. Enable if you expect the command
                         sent to cause an error.

        """
        dev, cmd_api, _ = self._init_keyword(device_name, self.constants.API_MULTIAUTHMETHODCLIENT, **kwargs)

        arg_dict = {"config_filename": config_filename,
                    "adapter": adapter,
                    "pwa_server_ip": pwa_server_ip,
                    "password": dev.password}

        cmd_obj = cmd_api.switch_to_root(arg_dict)
        dev.send_command_object(cmd_obj)
        dev.wait_for_prompt = False
        cmd_obj = cmd_api.change_to_atgapps_dir(arg_dict)
        dev.send_command_object(cmd_obj)
        dev.wait_for_prompt = True
        cmd_obj = cmd_api.run_multiuser_config(arg_dict)
        dev.send_command_object(cmd_obj)
        kw_results = self._determine_result(dev, cmd_obj)

        return self._keyword_cleanup(kw_results)

    def execute_multiuser_config_no_logoff(self, device_name, config_filename, adapter, pwa_server_ip="1.1.1.1",
                                           **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [config_filename] - The name of the configuration file that will be used.
        [adapter] - The number of the adapter that will be used.
        [pwa_server] - IP of the pwa server if needed in test.

        Valid **kwargs:
        [ignore_cli_feedback] - If set to True CLI feedback is ignored.
        [expect_error] - Used for negative testing. Enable if you expect the command
                         sent to cause an error.

        """
        dev, cmd_api, _ = self._init_keyword(device_name, self.constants.API_MULTIAUTHMETHODCLIENT, **kwargs)

        arg_dict = {"config_filename": config_filename,
                    "adapter": adapter,
                    "pwa_server_ip": pwa_server_ip,
                    "password": dev.password}

        cmd_obj = cmd_api.switch_to_root(arg_dict)
        dev.send_command_object(cmd_obj)
        dev.wait_for_prompt = False
        cmd_obj = cmd_api.change_to_atgapps_dir(arg_dict)
        dev.send_command_object(cmd_obj)
        dev.wait_for_prompt = True
        cmd_obj = cmd_api.run_multiuser_config_no_logoff(arg_dict)
        dev.send_command_object(cmd_obj)
        kw_results = self._determine_result(dev, cmd_obj)
        self._keyword_cleanup(kw_results)
