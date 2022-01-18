from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiConnectApi import ConnectApi, ConnectConstants

"""
    This is the API class for the command: connect

    Class is auto-generated. If you update anything here,
        it will be over written.
"""


class SpirentConnectApi(ConnectApi):

    """
    init function
    """
    def __init__(self, device):
        super(SpirentConnectApi, self).__init__(device)

    """
    This is the "One Large Method" for the command: connect
    use this by passing in a dict() of all the commands

        api = device.getApi(ConnectConstants.CONNECT_API)
        assert isinstance(api, ConnectApi)
        api.connect(dummyDict)
    """
    def connect(self, argdictionary):
        return super(SpirentConnectApi, self).connect(argdictionary, self.supportedSpirentHltapiCommands)

    """
    Individual commands for each option. Typically, the "One Large Method"
    is the one that you want to be using so look at that example above
    """
    def connect_aggregation_mode(self, param_string):
        return self.logger.log_unimplemented_method()

    def connect_aggregation_resource_mode(self, param_string):
        return self.logger.log_unimplemented_method()

    def connect_chain_cables_length(self, any):
        return self.logger.log_unimplemented_method()

    def connect_chain_sequence(self, any):
        return self.logger.log_unimplemented_method()

    def connect_chain_type(self, opt):
        return self.logger.log_unimplemented_method()

    def connect_config_file(self, any):
        return self.logger.log_unimplemented_method()

    def connect_connect_timeout(self, numeric):
        return self.logger.log_unimplemented_method()

    def connect_enable_win_tcl_server(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def connect_execution_timeout(self, numeric):
        return self.logger.log_unimplemented_method()

    def connect_guard_rail(self, opt):
        return self.logger.log_unimplemented_method()

    # def connect_helper(self, device, _port_list, opt):
    #     return self.logger.log_unimplemented_method()

    def connect_interactive(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def connect_ixnetwork_license_servers(self, any):
        return self.logger.log_unimplemented_method()

    def connect_ixnetwork_license_type(self, opt):
        return self.logger.log_unimplemented_method()

    def connect_ixnetwork_tcl_proxy(self, any):
        return self.logger.log_unimplemented_method()

    def connect_ixnetwork_tcl_server(self, any):
        return self.logger.log_unimplemented_method()

    def connect_log_path(self, any):
        return self.logger.log_unimplemented_method()

    def connect_logging(self, opt):
        return self.logger.log_unimplemented_method()

    def connect_master_device(self, any):
        return self.logger.log_unimplemented_method()

    def connect_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def connect_protocol_stacking_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def connect_return_detailed_handles(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def connect_session_resume_include_filter(self, any):
        return self.logger.log_unimplemented_method()

    def connect_session_resume_keys(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def connect_tcl_server(self, any):
        return self.logger.log_unimplemented_method()

    def connect_vport_count(self, range):
        return self.logger.log_unimplemented_method()

    def connect_vport_list(self, any):
        return self.logger.log_unimplemented_method()


    supportedSpirentHltapiCommands = {ConnectConstants.BREAK_LOCKS_CMD, ConnectConstants.CLOSE_SERVER_ON_DISCONNECT_CMD, ConnectConstants.CONFIG_FILE_HLT_CMD, ConnectConstants.DEVICE_CMD, ConnectConstants.FORCELOAD_CMD, ConnectConstants.NOBIOS_CMD, ConnectConstants.PORT_LIST_CMD, ConnectConstants.RESET_CMD, ConnectConstants.SYNC_CMD, ConnectConstants.TCL_PROXY_USERNAME_CMD, ConnectConstants.TIMEOUT_CMD, ConnectConstants.USERNAME_CMD}
