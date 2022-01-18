from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficL47ConfigApi import TrafficL47ConfigApi, TrafficL47ConfigConstants

"""
    This is the API class for the command: traffic_l47_config

    Class is auto-generated. If you update anything here,
        it will be over written.
"""


class IxiaTrafficL47ConfigApi(TrafficL47ConfigApi):

    """
    init function
    """
    def __init__(self, device):
        super(IxiaTrafficL47ConfigApi, self).__init__(device)

    """
    This is the "One Large Method" for the command: traffic_l47_config
    use this by passing in a dict() of all the commands

        api = device.getApi(TrafficL47ConfigConstants.TRAFFIC_L47_CONFIG_API)
        api.traffic_l47_config(dummyDict)
    """
    def traffic_l47_config(self, argdictionary):
        return super(IxiaTrafficL47ConfigApi, self).traffic_l47_config(argdictionary, self.supportedIxiaHltapiCommands)

    """
    Individual commands for each option. Typically, the "One Large Method"
    is the one that you want to be using so look at that example above
    """
    def traffic_l47_config_circuit_endpoint_type(self, opt):
        """
        This is the method the command: traffic_l47_config option circuit_endpoint_type
        Description:This argument can be used to specify the endpoint type that will be used
            to generate traffic.
            Valid options are:
            ipv4_application_traffic

            Select this option if the endpoint supports IPv4 application traffic
            generation.
            ipv6_application_traffic

            Select this option if the endpoint supports IPv6 application traffic
            generation.
            DEFAULT

            ipv4_application_traffic
        Constants Available: CIRCUIT_ENDPOINT_TYPE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.traffic_l47_config({TrafficL47ConfigConstants.CIRCUIT_ENDPOINT_TYPE_CMD : opt})

    def traffic_l47_config_connection_id(self, numeric):
        """
        This is the method the command: traffic_l47_config option connection_id
        Description:Application library flow connection identifier ( e.g. 1).
            DEFAULT
                None
        Constants Available: CONNECTION_ID_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.traffic_l47_config({TrafficL47ConfigConstants.CONNECTION_ID_CMD : numeric})

    def traffic_l47_config_emulation_dst_handle(self, any):
        """
        This is the method the command: traffic_l47_config option emulation_dst_handle
        Description:The handle used to retrieve information for L2 or L3 source addresses
            and use them to configure the destinations for traffic. This should be
            the emulation handle that was obtained after configuring NGPF protocols.
            This parameter can be provided with a list or with a list of lists elements.
            DEFAULT
                None
        Constants Available: EMULATION_DST_HANDLE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.traffic_l47_config({TrafficL47ConfigConstants.EMULATION_DST_HANDLE_CMD : any})

    def traffic_l47_config_emulation_scalable_dst_handle(self, any):
        """
        This is the method the command: traffic_l47_config option emulation_scalable_dst_handle
        Description:An array which contains lists of handles used to retrieve information
            for L3 dst addresses, indexed by the endpointset to which they
            correspond. This should be a handle that was obtained after configuring
            protocols with commands from the ::ixia_hlapi_framework:: namespace.
            This parameter can be used in conjunction with emulation_dst_handle.
            DEFAULT
                None
        Constants Available: EMULATION_SCALABLE_DST_HANDLE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.traffic_l47_config({TrafficL47ConfigConstants.EMULATION_SCALABLE_DST_HANDLE_CMD : any})

    def traffic_l47_config_emulation_scalable_dst_intf_count(self, numeric):
        """
        This is the method the command: traffic_l47_config option emulation_scalable_dst_intf_count
        Description:An array which contains lists of numbers that encode the number of
            interfaces on which the corresponding endpointset will be configured.
            This parameter will be ignored if no corresponding value is specified
            for emulation_scalable_dst_handle.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'emulation_scalable_dst_handle' | value= '1' |
        Constants Available: EMULATION_SCALABLE_DST_INTF_COUNT_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.traffic_l47_config({TrafficL47ConfigConstants.EMULATION_SCALABLE_DST_INTF_COUNT_CMD : numeric})

    def traffic_l47_config_emulation_scalable_dst_intf_start(self, numeric):
        """
        This is the method the command: traffic_l47_config option emulation_scalable_dst_intf_start
        Description:An array which contains lists of numbers that encode the index of the
            first interface on which the corresponding endpointset will be
            configured. This parameter will be ignored if no corresponding value is
            specified for emulation_scalable_dst_handle.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'emulation_scalable_dst_handle' | value= '1' |
        Constants Available: EMULATION_SCALABLE_DST_INTF_START_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.traffic_l47_config({TrafficL47ConfigConstants.EMULATION_SCALABLE_DST_INTF_START_CMD : numeric})

    def traffic_l47_config_emulation_scalable_dst_port_count(self, numeric):
        """
        This is the method the command: traffic_l47_config option emulation_scalable_dst_port_count
        Description:An array which contains lists of numbers that encode the number of ports
            on which the corresponding endpointset will be configured. This
            parameter will be ignored if no corresponding value is specified for
            emulation_scalable_dst_handle.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'emulation_scalable_dst_handle' | value= '1' |
        Constants Available: EMULATION_SCALABLE_DST_PORT_COUNT_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.traffic_l47_config({TrafficL47ConfigConstants.EMULATION_SCALABLE_DST_PORT_COUNT_CMD : numeric})

    def traffic_l47_config_emulation_scalable_dst_port_start(self, numeric):
        """
        This is the method the command: traffic_l47_config option emulation_scalable_dst_port_start
        Description:An array which contains lists of numbers that encode the index of the
            first port on which the corresponding endpointset will be configured.
            This parameter will be ignored if no corresponding value is specified
            for emulation_scalable_dst_handle.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'emulation_scalable_dst_handle' | value= '1' |
        Constants Available: EMULATION_SCALABLE_DST_PORT_START_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.traffic_l47_config({TrafficL47ConfigConstants.EMULATION_SCALABLE_DST_PORT_START_CMD : numeric})

    def traffic_l47_config_emulation_scalable_src_handle(self, any):
        """
        This is the method the command: traffic_l47_config option emulation_scalable_src_handle
        Description:An array which contains lists of handles used to retrieve information
            for L3 src addresses, indexed by the endpointset to which they
            correspond. This should be a handle that was obtained after configuring
            protocols with commands from the ::ixia_hlapi_framework:: namespace.
            This parameter can be used in conjunction with emulation_src_handle.
            DEFAULT
                None
        Constants Available: EMULATION_SCALABLE_SRC_HANDLE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.traffic_l47_config({TrafficL47ConfigConstants.EMULATION_SCALABLE_SRC_HANDLE_CMD : any})

    def traffic_l47_config_emulation_scalable_src_intf_count(self, numeric):
        """
        This is the method the command: traffic_l47_config option emulation_scalable_src_intf_count
        Description:An array which contains lists of numbers that encode the number of
            interfaces on which the corresponding endpointset will be configured.
            This parameter will be ignored if no corresponding value is specified
            for emulation_scalable_src_handle.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'emulation_scalable_src_handle' | value= '1' |
        Constants Available: EMULATION_SCALABLE_SRC_INTF_COUNT_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.traffic_l47_config({TrafficL47ConfigConstants.EMULATION_SCALABLE_SRC_INTF_COUNT_CMD : numeric})

    def traffic_l47_config_emulation_scalable_src_intf_start(self, numeric):
        """
        This is the method the command: traffic_l47_config option emulation_scalable_src_intf_start
        Description:An array which contains lists of numbers that encode the index of the
            first interface on which the corresponding endpointset will be
            configured. This parameter will be ignored if no corresponding value is
            specified for emulation_scalable_src_handle.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'emulation_scalable_src_handle' | value= '1' |
        Constants Available: EMULATION_SCALABLE_SRC_INTF_START_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.traffic_l47_config({TrafficL47ConfigConstants.EMULATION_SCALABLE_SRC_INTF_START_CMD : numeric})

    def traffic_l47_config_emulation_scalable_src_port_count(self, numeric):
        """
        This is the method the command: traffic_l47_config option emulation_scalable_src_port_count
        Description:An array which contains lists of numbers that encode the number of ports
            on which the corresponding endpointset will be configured. This
            parameter will be ignored if no corresponding value is specified for
            emulation_scalable_src_handle.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'emulation_scalable_src_handle' | value= '1' |
        Constants Available: EMULATION_SCALABLE_SRC_PORT_COUNT_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.traffic_l47_config({TrafficL47ConfigConstants.EMULATION_SCALABLE_SRC_PORT_COUNT_CMD : numeric})

    def traffic_l47_config_emulation_scalable_src_port_start(self, numeric):
        """
        This is the method the command: traffic_l47_config option emulation_scalable_src_port_start
        Description:An array which contains lists of numbers that encode the index of the
            first port on which the corresponding endpointset will be configured.
            This parameter will be ignored if no corresponding value is specified
            for emulation_scalable_src_handle.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'emulation_scalable_src_handle' | value= '1' |
        Constants Available: EMULATION_SCALABLE_SRC_PORT_START_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.traffic_l47_config({TrafficL47ConfigConstants.EMULATION_SCALABLE_SRC_PORT_START_CMD : numeric})

    def traffic_l47_config_emulation_src_handle(self, any):
        """
        This is the method the command: traffic_l47_config option emulation_src_handle
        Description:The handle used to retrieve information for L2 or L3 source addresses
            and use them to configure the sources for traffic. This should be the
            emulation handle that was obtained after configuring NGPF protocols.
            This parameter can be provided with a list or with a list of lists elements.
            DEFAULT
                None
        Constants Available: EMULATION_SRC_HANDLE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.traffic_l47_config({TrafficL47ConfigConstants.EMULATION_SRC_HANDLE_CMD : any})

    def traffic_l47_config_enable_per_ip_stats(self, bool_opt):
        """
        This is the method the command: traffic_l47_config option enable_per_ip_stats
        Description:enables/disables per IP statistics.
            DEFAULT
                None
        Constants Available: ENABLE_PER_IP_STATS_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.traffic_l47_config({TrafficL47ConfigConstants.ENABLE_PER_IP_STATS_CMD : bool_opt})

    def traffic_l47_config_flow_id(self, any):
        """
        This is the method the command: traffic_l47_config option flow_id
        Description:Name of the Application Library flow ( e.g. HTTP_Request).
            DEFAULT
                None
        Constants Available: FLOW_ID_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.traffic_l47_config({TrafficL47ConfigConstants.FLOW_ID_CMD : any})

    def traffic_l47_config_flow_percentage(self, any):
        """
        This is the method the command: traffic_l47_config option flow_percentage
        Description:Amount of traffic to be generated for this flow in percentage.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'flow_id' | value= '1' |
        Constants Available: FLOW_PERCENTAGE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.traffic_l47_config({TrafficL47ConfigConstants.FLOW_PERCENTAGE_CMD : any})

    def traffic_l47_config_flows(self, any):
        """
        This is the method the command: traffic_l47_config option flows
        Description:sets flows to be configured when create a traffic application profile.
            DEFAULT
                None
        Constants Available: FLOWS_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.traffic_l47_config({TrafficL47ConfigConstants.FLOWS_CMD : any})

    def traffic_l47_config_l47_configuration(self, opt):
        """
        This is the method the command: traffic_l47_config option l47_configuration
        Description:Required for -mode modify and -stream_id traffic_item_handler calls
            Valid for Application Library Traffic.
            Valid options are:
            modify_profile_parameters

            Modify the profile parameter for stream/traffic item.
            modify_flow_percentage

            Modify the flow percentage for a given flow.
            modify_flow_parameter

            Modify the flow parameters for a given flow.
            modify_flow_connection_parameter

            Modify the flow connection parameter for a given flow.
            override_flows

            Override flow from existing stream/traffic item.
            append_flow

            Add a new flow to existing stream/traffic item.
            remove_flow

            Remove flow from existing stream/traffic item.
            distribute_flows_percentage_evenly

            Distribute flow percentage equally among the configured flows in given
            stream/traffic item.
            get_available_flows

            Get all the configured flows in a given stream/traffic item.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'for -l47_configuration 'modify_profile_parameters': 'objective_type' |
            'objective_value' | 'objective_distribution' | 'stream_id' for
            -l47_configuration 'modify_flow_percentage': 'flow_percentage' |
            'stream_id' for -l47_configuration 'modify_flow_parameter':
            'parameter_id ' | 'parameter_option' | 'parameter_value' | 'stream_id'
            for -l47_configuration 'modify_flow_connection_parameter':
            'connection_id ' | 'stream_id' for -l47_configuration 'override_flows':
            'stream_id ' | 'flow_id' for -l47_configuration 'append_flow':
            'stream_id ' | 'flow_id' for -l47_configuration 'remove_flow':
            'stream_id' | 'flow_id' for -l47_configuration
            'distribute_flows_percentage_evenly': 'stream_id ' for
            -l47_configuration 'get_available_flows': 'stream_id'' | value= '1' |
        Constants Available: L47_CONFIGURATION_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.traffic_l47_config({TrafficL47ConfigConstants.L47_CONFIGURATION_CMD : opt})

    def traffic_l47_config_name(self, any):
        """
        This is the method the command: traffic_l47_config option name
        Description:Stream string identifier/name. If this name contains spaces, the spaces
            will be translated to underscores and a warning will be displayed. The
            string name must not contain commas.
            DEFAULT
                None
        Constants Available: NAME_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.traffic_l47_config({TrafficL47ConfigConstants.NAME_CMD : any})

    def traffic_l47_config_objective_distribution(self, opt):
        """
        This is the method the command: traffic_l47_config option objective_distribution
        Description:sets objective distribution.
            Valid options are:
            apply_full_objective_to_each_port

            split_objective_evenly_among_ports

            DEFAULT

            apply_full_objective_to_each_port
        Constants Available: OBJECTIVE_DISTRIBUTION_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.traffic_l47_config({TrafficL47ConfigConstants.OBJECTIVE_DISTRIBUTION_CMD : opt})

    def traffic_l47_config_objective_type(self, opt):
        """
        This is the method the command: traffic_l47_config option objective_type
        Description:sets objective type.
            Valid options are:
            users

            tputkb

            tputmb

            tputgb

            DEFAULT

            users
        Constants Available: OBJECTIVE_TYPE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.traffic_l47_config({TrafficL47ConfigConstants.OBJECTIVE_TYPE_CMD : opt})

    def traffic_l47_config_objective_value(self, numeric):
        """
        This is the method the command: traffic_l47_config option objective_value
        Description:sets objective value.
            DEFAULT
                None
        Constants Available: OBJECTIVE_VALUE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.traffic_l47_config({TrafficL47ConfigConstants.OBJECTIVE_VALUE_CMD : numeric})

    def traffic_l47_config_parameter_id(self, any):
        """
        This is the method the command: traffic_l47_config option parameter_id
        Description:Application library flow parameter identifier ( e.g. enableProxyPort).
            DEFAULT
                None
        Constants Available: PARAMETER_ID_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.traffic_l47_config({TrafficL47ConfigConstants.PARAMETER_ID_CMD : any})

    def traffic_l47_config_parameter_option(self, opt):
        """
        This is the method the command: traffic_l47_config option parameter_option
        Description:Each parameter has one or multiple options. This options are: value,
            choice and range.
            Valid options are:
            value

            single value. To be used when parameter takes a single value.
            choice

            choice of values. To be used when parameter takes a value from choice of
            values.
            range

            range of value. To be used when parameter takes a value between range of
            values.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'parameter_id' | value= '1' |
        Constants Available: PARAMETER_OPTION_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.traffic_l47_config({TrafficL47ConfigConstants.PARAMETER_OPTION_CMD : opt})

    def traffic_l47_config_parameter_value(self, opt):
        """
        This is the method the command: traffic_l47_config option parameter_value
        Description:For each parameter a value can be assigned. The parameters are runtime
            specific and can accommodate the following types:
            Valid options are:
            numeric

            when the value is in number format
            bool

            when the value is a boolean value, true or false
            string

            when the value is a word
            hex

            when the value is in hex format
            choice

            when the value is selected from a list of available options
            range

            when specifying a range value, this value must be in format min-max,
            where min and max are numeric values
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'parameter_option' | value= '1' |
        Constants Available: PARAMETER_VALUE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.traffic_l47_config({TrafficL47ConfigConstants.PARAMETER_VALUE_CMD : opt})

    def traffic_l47_config_stream_id(self, any):
        """
        This is the method the command: traffic_l47_config option stream_id
        Description:Required for -mode modify/remove/enable/disable/get calls. Stream ID
            returned from the traffic_l47_config handles. Stream ID is not required
            for configuring a stream for the first time. In this case, the stream ID
            is returned by the call.. Valid for Application Library Traffic.
            DEFAULT

            none
            DEPENDENCIES

            Valid in combination with parameter(s)
            ''mode' | value= 'modify' | 'mode' | value= 'delete' | 'mode' | value=
            'enable' | 'mode' | value= 'disable' | 'mode' | value= 'get'' | value= '1' |
        Constants Available: STREAM_ID_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.traffic_l47_config({TrafficL47ConfigConstants.STREAM_ID_CMD : any})


    supportedIxiaHltapiCommands = {TrafficL47ConfigConstants.CIRCUIT_ENDPOINT_TYPE_CMD, TrafficL47ConfigConstants.CONNECTION_ID_CMD, TrafficL47ConfigConstants.EMULATION_DST_HANDLE_CMD, TrafficL47ConfigConstants.EMULATION_SCALABLE_DST_HANDLE_CMD, TrafficL47ConfigConstants.EMULATION_SCALABLE_DST_INTF_COUNT_CMD, TrafficL47ConfigConstants.EMULATION_SCALABLE_DST_INTF_START_CMD, TrafficL47ConfigConstants.EMULATION_SCALABLE_DST_PORT_COUNT_CMD, TrafficL47ConfigConstants.EMULATION_SCALABLE_DST_PORT_START_CMD, TrafficL47ConfigConstants.EMULATION_SCALABLE_SRC_HANDLE_CMD, TrafficL47ConfigConstants.EMULATION_SCALABLE_SRC_INTF_COUNT_CMD, TrafficL47ConfigConstants.EMULATION_SCALABLE_SRC_INTF_START_CMD, TrafficL47ConfigConstants.EMULATION_SCALABLE_SRC_PORT_COUNT_CMD, TrafficL47ConfigConstants.EMULATION_SCALABLE_SRC_PORT_START_CMD, TrafficL47ConfigConstants.EMULATION_SRC_HANDLE_CMD, TrafficL47ConfigConstants.ENABLE_PER_IP_STATS_CMD, TrafficL47ConfigConstants.FLOW_ID_CMD, TrafficL47ConfigConstants.FLOW_PERCENTAGE_CMD, TrafficL47ConfigConstants.FLOWS_CMD, TrafficL47ConfigConstants.L47_CONFIGURATION_CMD, TrafficL47ConfigConstants.NAME_CMD, TrafficL47ConfigConstants.OBJECTIVE_DISTRIBUTION_CMD, TrafficL47ConfigConstants.OBJECTIVE_TYPE_CMD, TrafficL47ConfigConstants.OBJECTIVE_VALUE_CMD, TrafficL47ConfigConstants.PARAMETER_ID_CMD, TrafficL47ConfigConstants.PARAMETER_OPTION_CMD, TrafficL47ConfigConstants.PARAMETER_VALUE_CMD, TrafficL47ConfigConstants.STREAM_ID_CMD}
