from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficL47ConfigApi import \
    TrafficL47ConfigApi

"""
    This is the API class for the command: traffic_l47_config

    Class is auto-generated. If you update anything here,
        it will be over written.
"""


class SpirentTrafficL47ConfigApi(TrafficL47ConfigApi):

    """
    init function
    """
    def __init__(self, device):
        super(SpirentTrafficL47ConfigApi, self).__init__(device)

    """
    This is the "One Large Method" for the command: traffic_l47_config
    use this by passing in a dict() of all the commands

        api = device.getApi(TrafficL47ConfigConstants.TRAFFIC_L47_CONFIG_API)
        api.traffic_l47_config(dummyDict)
    """
    def traffic_l47_config(self, argdictionary):
        return super(SpirentTrafficL47ConfigApi, self).traffic_l47_config(argdictionary, self.supportedSpirentHltapiCommands)

    """
    Individual commands for each option. Typically, the "One Large Method"
    is the one that you want to be using so look at that example above
    """
    def traffic_l47_config_circuit_endpoint_type(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_l47_config_connection_id(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_l47_config_emulation_dst_handle(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_l47_config_emulation_scalable_dst_handle(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_l47_config_emulation_scalable_dst_intf_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_l47_config_emulation_scalable_dst_intf_start(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_l47_config_emulation_scalable_dst_port_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_l47_config_emulation_scalable_dst_port_start(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_l47_config_emulation_scalable_src_handle(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_l47_config_emulation_scalable_src_intf_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_l47_config_emulation_scalable_src_intf_start(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_l47_config_emulation_scalable_src_port_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_l47_config_emulation_scalable_src_port_start(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_l47_config_emulation_src_handle(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_l47_config_enable_per_ip_stats(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_l47_config_flow_id(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_l47_config_flow_percentage(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_l47_config_flows(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_l47_config_l47_configuration(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_l47_config_name(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_l47_config_objective_distribution(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_l47_config_objective_type(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_l47_config_objective_value(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_l47_config_parameter_id(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_l47_config_parameter_option(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_l47_config_parameter_value(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_l47_config_stream_id(self, any):
        return self.logger.log_unimplemented_method()


    supportedSpirentHltapiCommands = {}
