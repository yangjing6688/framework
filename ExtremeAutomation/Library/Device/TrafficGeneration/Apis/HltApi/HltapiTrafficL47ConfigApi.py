from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.TrafficGenerationApi import TrafficGenerationApi
from ExtremeAutomation.Library.Utils.Singleton import Singleton

"""
    This is the API class for the command: traffic_l47_config

    Class is auto-generated. If you update anything here,
        it will be over written.
"""


class TrafficL47ConfigApi(TrafficGenerationApi):

    """
    init function
    """
    def __init__(self, device):
        super(TrafficL47ConfigApi, self).__init__(device)

    """
    This is the "One Large Method" for the command: traffic_l47_config
    use this by passing in a dict() of all the commands
        dummyDict = dict()
        dummyDict[TrafficL47ConfigConstants.CIRCUIT_ENDPOINT_TYPE_CMD] = TrafficL47ConfigConstants.CIRCUIT_ENDPOINT_TYPE_IPV4_APPLICATION_TRAFFIC # constant value
        dummyDict[TrafficL47ConfigConstants.CONNECTION_ID_CMD] = "dummyValue2" # static value
        dummyDict[TrafficL47ConfigConstants.EMULATION_DST_HANDLE_CMD] = "dummyValue3" # static value
        dummyDict[TrafficL47ConfigConstants.EMULATION_SCALABLE_DST_HANDLE_CMD] = "dummyValue4" # static value
        dummyDict[TrafficL47ConfigConstants.EMULATION_SCALABLE_DST_INTF_COUNT_CMD] = "dummyValue5" # static value
        dummyDict[TrafficL47ConfigConstants.EMULATION_SCALABLE_DST_INTF_START_CMD] = "dummyValue6" # static value
        dummyDict[TrafficL47ConfigConstants.EMULATION_SCALABLE_DST_PORT_COUNT_CMD] = "dummyValue7" # static value
        dummyDict[TrafficL47ConfigConstants.EMULATION_SCALABLE_DST_PORT_START_CMD] = "dummyValue8" # static value
        dummyDict[TrafficL47ConfigConstants.EMULATION_SCALABLE_SRC_HANDLE_CMD] = "dummyValue9" # static value
        dummyDict[TrafficL47ConfigConstants.EMULATION_SCALABLE_SRC_INTF_COUNT_CMD] = "dummyValue10" # static value
        dummyDict[TrafficL47ConfigConstants.EMULATION_SCALABLE_SRC_INTF_START_CMD] = "dummyValue11" # static value
        dummyDict[TrafficL47ConfigConstants.EMULATION_SCALABLE_SRC_PORT_COUNT_CMD] = "dummyValue12" # static value
        dummyDict[TrafficL47ConfigConstants.EMULATION_SCALABLE_SRC_PORT_START_CMD] = "dummyValue13" # static value
        dummyDict[TrafficL47ConfigConstants.EMULATION_SRC_HANDLE_CMD] = "dummyValue14" # static value
        dummyDict[TrafficL47ConfigConstants.ENABLE_PER_IP_STATS_CMD] = "dummyValue15" # static value
        dummyDict[TrafficL47ConfigConstants.FLOW_ID_CMD] = "dummyValue16" # static value
        dummyDict[TrafficL47ConfigConstants.FLOW_PERCENTAGE_CMD] = "dummyValue17" # static value
        dummyDict[TrafficL47ConfigConstants.FLOWS_CMD] = "dummyValue18" # static value
        dummyDict[TrafficL47ConfigConstants.L47_CONFIGURATION_CMD] = TrafficL47ConfigConstants.L47_CONFIGURATION_APPEND_FLOW # constant value
        dummyDict[TrafficL47ConfigConstants.NAME_CMD] = "dummyValue20" # static value
        dummyDict[TrafficL47ConfigConstants.OBJECTIVE_DISTRIBUTION_CMD] = TrafficL47ConfigConstants.OBJECTIVE_DISTRIBUTION_APPLY_FULL_OBJECTIVE_TO_EACH_PORT # constant value
        dummyDict[TrafficL47ConfigConstants.OBJECTIVE_TYPE_CMD] = TrafficL47ConfigConstants.OBJECTIVE_TYPE_TPUTGB # constant value
        dummyDict[TrafficL47ConfigConstants.OBJECTIVE_VALUE_CMD] = "dummyValue23" # static value
        dummyDict[TrafficL47ConfigConstants.PARAMETER_ID_CMD] = "dummyValue24" # static value
        dummyDict[TrafficL47ConfigConstants.PARAMETER_OPTION_CMD] = TrafficL47ConfigConstants.PARAMETER_OPTION_CHOICE # constant value
        dummyDict[TrafficL47ConfigConstants.PARAMETER_VALUE_CMD] = TrafficL47ConfigConstants.PARAMETER_VALUE_BOOL # constant value
        dummyDict[TrafficL47ConfigConstants.STREAM_ID_CMD] = "dummyValue27" # static value

        api = device.getApi(TrafficL47ConfigConstants.TRAFFIC_L47_CONFIG_API)
        api.traffic_l47_config(dummyDict)
    """
    def traffic_l47_config(self, argdictionary, supported = None):
        self.process_supported_hltapi_commands(argdictionary, supported)
        return self.send_command_args(self._nameSpace +"::traffic_l47_config", argdictionary)

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


"""
    This is the Constants class for the command: traffic_l47_config
    Commands end with _CMD and constants for a command start with the beginning
    with the command's constant name minus the _CMD
"""


class TrafficL47ConfigConstants(object, metaclass=Singleton):
    # api reference constant for this api to get it from the device
    TRAFFIC_L47_CONFIG_API = "TRAFFIC_L47_CONFIG_API"

    CIRCUIT_ENDPOINT_TYPE_CMD = "circuit_endpoint_type"
    # Constant values for CIRCUIT_ENDPOINT_TYPE_CMD
    CIRCUIT_ENDPOINT_TYPE_IPV4_APPLICATION_TRAFFIC = "ipv4_application_traffic"
    CIRCUIT_ENDPOINT_TYPE_IPV6_APPLICATION_TRAFFIC = "ipv6_application_traffic"

    CONNECTION_ID_CMD = "connection_id"

    EMULATION_DST_HANDLE_CMD = "emulation_dst_handle"

    EMULATION_SCALABLE_DST_HANDLE_CMD = "emulation_scalable_dst_handle"

    EMULATION_SCALABLE_DST_INTF_COUNT_CMD = "emulation_scalable_dst_intf_count"

    EMULATION_SCALABLE_DST_INTF_START_CMD = "emulation_scalable_dst_intf_start"

    EMULATION_SCALABLE_DST_PORT_COUNT_CMD = "emulation_scalable_dst_port_count"

    EMULATION_SCALABLE_DST_PORT_START_CMD = "emulation_scalable_dst_port_start"

    EMULATION_SCALABLE_SRC_HANDLE_CMD = "emulation_scalable_src_handle"

    EMULATION_SCALABLE_SRC_INTF_COUNT_CMD = "emulation_scalable_src_intf_count"

    EMULATION_SCALABLE_SRC_INTF_START_CMD = "emulation_scalable_src_intf_start"

    EMULATION_SCALABLE_SRC_PORT_COUNT_CMD = "emulation_scalable_src_port_count"

    EMULATION_SCALABLE_SRC_PORT_START_CMD = "emulation_scalable_src_port_start"

    EMULATION_SRC_HANDLE_CMD = "emulation_src_handle"

    ENABLE_PER_IP_STATS_CMD = "enable_per_ip_stats"

    FLOW_ID_CMD = "flow_id"

    FLOW_PERCENTAGE_CMD = "flow_percentage"

    FLOWS_CMD = "flows"

    L47_CONFIGURATION_CMD = "l47_configuration"
    # Constant values for L47_CONFIGURATION_CMD
    L47_CONFIGURATION_APPEND_FLOW = "append_flow"
    L47_CONFIGURATION_DISTRIBUTE_FLOWS_PERCENTAGE_EVENLY = "distribute_flows_percentage_evenly"
    L47_CONFIGURATION_GET_AVAILABLE_FLOWS = "get_available_flows"
    L47_CONFIGURATION_MODIFY_FLOW_CONNECTION_PARAMETER = "modify_flow_connection_parameter"
    L47_CONFIGURATION_MODIFY_FLOW_PARAMETER = "modify_flow_parameter"
    L47_CONFIGURATION_MODIFY_FLOW_PERCENTAGE = "modify_flow_percentage"
    L47_CONFIGURATION_MODIFY_PROFILE_PARAMETERS = "modify_profile_parameters"
    L47_CONFIGURATION_OVERRIDE_FLOWS = "override_flows"
    L47_CONFIGURATION_REMOVE_FLOW = "remove_flow"

    NAME_CMD = "name"

    OBJECTIVE_DISTRIBUTION_CMD = "objective_distribution"
    # Constant values for OBJECTIVE_DISTRIBUTION_CMD
    OBJECTIVE_DISTRIBUTION_APPLY_FULL_OBJECTIVE_TO_EACH_PORT = "apply_full_objective_to_each_port"
    OBJECTIVE_DISTRIBUTION_SPLIT_OBJECTIVE_EVENLY_AMONG_PORTS = "split_objective_evenly_among_ports"

    OBJECTIVE_TYPE_CMD = "objective_type"
    # Constant values for OBJECTIVE_TYPE_CMD
    OBJECTIVE_TYPE_TPUTGB = "tputgb"
    OBJECTIVE_TYPE_TPUTKB = "tputkb"
    OBJECTIVE_TYPE_TPUTMB = "tputmb"
    OBJECTIVE_TYPE_USERS = "users"

    OBJECTIVE_VALUE_CMD = "objective_value"

    PARAMETER_ID_CMD = "parameter_id"

    PARAMETER_OPTION_CMD = "parameter_option"
    # Constant values for PARAMETER_OPTION_CMD
    PARAMETER_OPTION_CHOICE = "choice"
    PARAMETER_OPTION_RANGE = "range"
    PARAMETER_OPTION_VALUE = "value"

    PARAMETER_VALUE_CMD = "parameter_value"
    # Constant values for PARAMETER_VALUE_CMD
    PARAMETER_VALUE_BOOL = "bool"
    PARAMETER_VALUE_CHOICE = "choice"
    PARAMETER_VALUE_HEX = "hex"
    PARAMETER_VALUE_NUMERIC = "numeric"
    PARAMETER_VALUE_RANGE = "range"
    PARAMETER_VALUE_STRING = "string"

    STREAM_ID_CMD = "stream_id"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass

"""
Implemented Commands (Alphabetical)
    -circuit_endpoint_type
    -connection_id
    -emulation_dst_handle
    -emulation_scalable_dst_handle
    -emulation_scalable_dst_intf_count
    -emulation_scalable_dst_intf_start
    -emulation_scalable_dst_port_count
    -emulation_scalable_dst_port_start
    -emulation_scalable_src_handle
    -emulation_scalable_src_intf_count
    -emulation_scalable_src_intf_start
    -emulation_scalable_src_port_count
    -emulation_scalable_src_port_start
    -emulation_src_handle
    -enable_per_ip_stats
    -flow_id
    -flow_percentage
    -flows
    -l47_configuration
    -name
    -objective_distribution
    -objective_type
    -objective_value
    -parameter_id
    -parameter_option
    -parameter_value
    -stream_id
If you want to update this file, look in the CSV
"""
