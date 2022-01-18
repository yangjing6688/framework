from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiConnectApi import ConnectApi, \
    ConnectConstants

"""
    This is the API class for the command: connect

    Class is auto-generated. If you update anything here,
        it will be over written.
"""


class IxiaConnectApi(ConnectApi):
    """
    init function
    """

    def __init__(self, device):
        super(IxiaConnectApi, self).__init__(device)

    """
    This is the "One Large Method" for the command: connect
    use this by passing in a dict() of all the commands

        api = device.getApi(ConnectConstants.CONNECT_API)
        assert isinstance(api, ConnectApi)
        api.connect(dummyDict)
    """

    def connect(self, argdictionary):
        return super(IxiaConnectApi, self).connect(argdictionary, self.supportedIxiaHltapiCommands)

    """
    Individual commands for each option. Typically, the "One Large Method"
    is the one that you want to be using so look at that example above
    """

    def connect_aggregation_mode(self, param_string):
        """
        This is the method the command: connect option aggregation_mode
        Description:This parameter represents the aggregation mode that can be set on the card.
            Valid options are:
            normal: default (all the ports can be used, except the 40Gig ones)
            mixed: using this mode, you can set different aggregation modes on each aggregation group
            not_supported: the card does not support aggregation
            ten_gig_aggregation: 10Gig aggregation mode
            ten_gig_fan_out: 10Gig aggregation mode for Multis cards (aka 1X10G in IxNetwork GUI).
            three_by_ten_gig_fan_out: 10Gig aggregation mode for Multis cards (aka 3X10G in IxNetwork GUI).
            four_by_ten_gig_fan_out: 10Gig aggregation mode for Multis cards (aka 4X10G in IxNetwork GUI).
            eight_by_ten_gig_fan_out: 10Gig aggregation mode for Multis cards (aka 8X10G in IxNetwork GUI).
            four_by_twenty_five_gig_non_fan_out: 25Gig aggregation mode for Multis cards (aka 4X25G in IxNetwork GUI).
            forty_gig_aggregation: 40Gig aggregation mode
            forty_gig_fan_out: 40Gig aggregation for Multis cards with FAN out (aka 3x40G in IxNetwork GUI).
            forty_gig_normal_mode: 40Gig aggregation for Multis cards with FAN out (aka 1x40G mode in IxNetwork GUI).
            hundred_gig_non_fan_out: 100Gig aggregation mode for cards with no FAN out.
            single_mode_aggregation: Single Mode aggregation (supported both with IxNetwork and IxTclProtocol)
            dual_mode_aggregation: Dual Mode aggregation (supported both with IxNetwork and IxTclProtocol)
        Constants Available: AGGREGATION_MODE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT,IxNetwork-NGPF
        Keyword arguments:
        param_string --
        return -- pass/fail
        """
        return self.connect({ConnectConstants.AGGREGATION_MODE_CMD: param_string})

    def connect_aggregation_resource_mode(self, param_string):
        """
        This is the method the command: connect option aggregation_resource_mode
        Description:This parameter represents the aggregation mode on each resource group on the card.
            Valid options are:
            normal: default (all the ports can be used, except the 40Gig ones)
            ten_gig_aggregation: 10Gig aggregation mode
            ten_gig_fan_out: 10Gig aggregation mode for Multis cards (aka 1X10G in IxNetwork GUI).
            three_by_ten_gig_fan_out: 10Gig aggregation mode for Multis cards (aka 3X10G in IxNetwork GUI).
            four_by_ten_gig_fan_out: 10Gig aggregation mode for Multis cards (aka 4X10G in IxNetwork GUI).
            eight_by_ten_gig_fan_out: 10Gig aggregation mode for Multis cards (aka 8X10G in IxNetwork GUI).
            four_by_twenty_five_gig_non_fan_out: 25Gig aggregation mode for Multis cards (aka 4X25G in IxNetwork GUI).
            forty_gig_aggregation: 40Gig aggregation mode
            forty_gig_fan_out: 40Gig aggregation for Multis cards with FAN out (aka 3x40G in IxNetwork GUI).
            forty_gig_normal_mode: 40Gig aggregation for Multis cards with FAN out (aka 1x40G mode in IxNetwork GUI).
            hundred_gig_non_fan_out: 100Gig aggregation mode for cards with no FAN out.
            single_mode_aggregation: Single Mode aggregation (supported both with IxNetwork and IxTclProtocol)
            dual_mode_aggregation: Dual Mode aggregation (supported both with IxNetwork and IxTclProtocol)
        Constants Available: AGGREGATION_RESOURCE_MODE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT,IxNetwork-NGPF
        Keyword arguments:
        param_string --
        return -- pass/fail
        """
        return self.connect({ConnectConstants.AGGREGATION_RESOURCE_MODE_CMD: param_string})

    def connect_chain_cables_length(self, any):
        """
        This is the method the command: connect option chain_cables_length
        Description:Cable length in ft used for the chassis chain. This can be a value of a
            list of values for each slave chassis.Valid values are: '0' (not
            applicabale), '3' (3 ft) or '6' (6 ft). Only valid for slave chassis
            when master_device parameter is used. If not specified it will default
            to 3 for each slave chassis.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            Cable length in ft used for the chassis chain. This can be a value of a
            list of values for each slave chassis. Valid values are: '0' (not
            applicabale), '3' (3 ft) or '6' (6 ft). Only valid for slave chassis
            when master_device parameter is used. If not specified it will default
            to 3 for each slave chassis.
            DEFAULT
                None
        Constants Available: CHAIN_CABLES_LENGTH_CMD
        Supported:IxNetwork
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.connect({ConnectConstants.CHAIN_CABLES_LENGTH_CMD: any})

    def connect_chain_sequence(self, any):
        """
        This is the method the command: connect option chain_sequence
        Description:SequenceID for chassis chain. Only valid for slave chassis when
            master_device parameter is used. For more info please consult Ixia
            chassis chaining user guide from IxOS or IxNetwork products.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            SequenceID for chassis chain. Only valid for slave chassis when
            master_device parameter is used. For more info please consult Ixia
            chassis chaining user guide from IxOS or IxNetwork products.
            DEFAULT
                None
        Constants Available: CHAIN_SEQUENCE_CMD
        Supported:IxNetwork
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.connect({ConnectConstants.CHAIN_SEQUENCE_CMD: any})

    def connect_chain_type(self, opt):
        """
        This is the method the command: connect option chain_type
        Description:This optional parameter specifices the chassis chain type used by IxNetwork.
            Valid options are:
            none

            No chassis chain is used. The chain type present in IxNetwork will not
            be changed in this case.
            daisy

            Daisy chain. This is the default option when master_device argument is
            present. This refers to a set of Ixia chassis that have been cabled
            together through their Sync In/Sync Out ports.
            star

            This refers to a set of Ixia chassis that have been cabled together
            using a star topology. In this mode all slave chassis will have a cable
            connected directly in the master chassis.
            DEFAULT

            none
            IxNetwork-NGPF

            DESCRIPTION

            This optional parameter specifices the chassis chain type used by IxNetwork.
            Valid options are:
            none

            No chassis chain is used. The chain type present in IxNetwork will not
            be changed in this case.
            daisy

            Daisy chain. This is the default option when master_device argument is
            present. This refers to a set of Ixia chassis that have been cabled
            together through their Sync In/Sync Out ports.
            star

            This refers to a set of Ixia chassis that have been cabled together
            using a star topology. In this mode all slave chassis will have a cable
            connected directly in the master chassis.
            DEFAULT

            none
        Constants Available: CHAIN_TYPE_CMD
        Supported:IxNetwork
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.connect({ConnectConstants.CHAIN_TYPE_CMD: opt})

    def connect_config_file(self, any):
        """
        This is the method the command: connect option config_file
        Description:Name of a file containing Ixia configuration information. Must be a .chs
            file of an exported chassis from IxExplorer. When ixnetwork is used this
            must be an ixncfg file and will be loaded only for the session resume
            feature (when the -reset flag is missing). When using Unix, this
            parameter works only if HLT commands are executed locally, on the Unix
            client machine.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            and/or the hlt configuration to the file specified with -config_file_hlt.
            DEFAULT
                None
        Constants Available: CONFIG_FILE_CMD
        Supported:IxNetwork
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.connect({ConnectConstants.CONFIG_FILE_CMD: any})

    def connect_connect_timeout(self, numeric):
        """
        This is the method the command: connect option connect_timeout
        Description:Timeout in seconds to wait before failing connection to chassis when
            using IxNetwork TCL API is used.
            From IxNetwork the connection to chassis is performed when
            ::<namespace>::interface_config procedure is called. The timeout will
            not apply to the chassis connection performed in ::<namespace>::connect
            procedure by IxTclHal.
            DEFAULT

            10
            IxNetwork-NGPF

            DESCRIPTION

            Timeout in seconds to wait before failing connection to chassis when
            using IxNetwork TCL API is used.
            From IxNetwork the connection to chassis is performed when
            ::::interface_config procedure is called. The timeout will not apply to
            the chassis connection performed in ::::connect procedure by IxTclHal.
            DEFAULT

            10
        Constants Available: CONNECT_TIMEOUT_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.connect({ConnectConstants.CONNECT_TIMEOUT_CMD: numeric})

    def connect_enable_win_tcl_server(self, bool_opt):
        """
        This is the method the command: connect option enable_win_tcl_server
        Description:Enables running entire HLT API commands on Tcl Server's machine. Valid
            only on Windows platforms.
            DEFAULT

            0
            IxNetwork-NGPF

            DESCRIPTION

            Enables running entire HLT API commands on Tcl Server's machine. Valid
            only on Windows platforms.
            DEFAULT

            0
        Constants Available: ENABLE_WIN_TCL_SERVER_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.connect({ConnectConstants.ENABLE_WIN_TCL_SERVER_CMD: bool_opt})

    def connect_execution_timeout(self, numeric):
        """
        This is the method the command: connect option execution_timeout
        Description:This is the timeout for each individual HLT command. Applies to all HLT
            commands. The setting is in seconds. Setting this setting to 60 it will
            mean that each command (ex: interface_config) must complete in under 60
            seconds. If the command will last more than 60 seconds the command will
            be terminated by force. This flag can be used to guard against dead
            locks occurring in IxNetwork. Default is 0, meaning no execution timeout.
            DEFAULT

            0
        Constants Available: EXECUTION_TIMEOUT_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.connect({ConnectConstants.EXECUTION_TIMEOUT_CMD: numeric})

    def connect_guard_rail(self, opt):
        """
        This is the method the command: connect option guard_rail
        Description:This parameter will protect the application from exceeding the memory
            limits and by limiting the maximum number of views and statistics
            provided to the user.
            Valid options are:
            statistics

            limit the maximum number of views and statistics
            none

            no guard rail
            DEFAULT

            none
            IxNetwork-NGPF

            DESCRIPTION

            This parameter will protect the application from exceeding the memory
            limits and by limiting the maximum number of views and statistics
            provided to the user.
            Valid options are:
            statistics

            limit the maximum number of views and statistics
            none

            no guard rail
            DEFAULT

            none
        Constants Available: GUARD_RAIL_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.connect({ConnectConstants.GUARD_RAIL_CMD: opt})

    def connect_interactive(self, bool_opt):
        """
        This is the method the command: connect option interactive
        Description:This argument is used to specify whether the console in which the script
            is run will work in the interactive mode or not.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            This argument is used to specify whether the console in which the script
            is run will work in the interactive mode or not.
            DEFAULT
                None
        Constants Available: INTERACTIVE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.connect({ConnectConstants.INTERACTIVE_CMD: bool_opt})

    def connect_ixnetwork_license_servers(self, any):
        """
        This is the method the command: connect option ixnetwork_license_servers
        Description:If set this will set the central license server from where you can
            request a license. Any computer where Ixia Licensing Utility is
            installed can act as a License Server. Multiple servers can be provided
            as a list.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            If set this will set the central license server from where you can
            request a license. Any computer where Ixia Licensing Utility is
            installed can act as a License Server. Multiple servers can be provided
            as a list.
            DEFAULT
                None
        Constants Available: IXNETWORK_LICENSE_SERVERS_CMD
        Supported:IxNetwork
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.connect({ConnectConstants.IXNETWORK_LICENSE_SERVERS_CMD: any})

    def connect_ixnetwork_license_type(self, opt):
        """
        This is the method the command: connect option ixnetwork_license_type
        Description:Valid if ixnetwork_license_servers argument is used. This argument is
            used to specify which type of license is used.
            Valid options are:
            perpetual

            In this mode licenses are checked out from the individual chassis. You
            cannot install perpetual licenses for a chassis on a different license
            server. You can use any number of ports on the given chassis as the
            license is node locked (locked to a specific chassis) and unlimited.
            Here the core license is checked when the chassis is connected. If there
            are no core licenses, the port fails to connect and an error is
            displayed. Perpetual mode is available for <b>Hardware ports
            only.</b><br/> Perpetual Mode is the legacy licensing mode.<br/>
            Changing modes between Subscription and Perpetual can only be done when
            all the ports are released.<br/> This is the default option if
            ixnetwork_license_servers is specified without ixnetwork_license_type.
            subscription_tier0

            Interfaces only support. For details on the limitations, please refer to
            IxNetwork User Guide.
            subscription_tier1

            It is the most restrictive, with only a few protocols and sessions
            support available per protocol. For details on the limitations, please
            refer to IxNetwork User Guide.
            subscription_tier2

            It provides unlimited protocol and session support for Hardware ports
            and limited protocol and session support for VM ports. For details on
            the limitations, please refer to IxNetwork User Guide.
            subscription_tier3

            It provides unlimited protocol and session support and also the premium
            features.
            mixed

            Mixed mode refers to mixed HW/VM licensing model. For details on the
            limitations, please refer to IxNetwork User Guide.
            DEFAULT

            perpetual
            IxNetwork-NGPF

            DESCRIPTION

            Valid if ixnetwork_license_servers argument is used. This argument is
            used to specify which type of license is used.
            Valid options are:
            perpetual

            In this mode licenses are checked out from the individual chassis. You
            cannot install perpetual licenses for a chassis on a different license
            server. You can use any number of ports on the given chassis as the
            license is node locked (locked to a specific chassis) and unlimited.
            Here the core license is checked when the chassis is connected. If there
            are no core licenses, the port fails to connect and an error is
            displayed. Perpetual mode is available for <b>Hardware ports
            only.</b><br/> Perpetual Mode is the legacy licensing mode.<br/>
            Changing modes between Subscription and Perpetual can only be done when
            all the ports are released.<br/> This is the default option if
            ixnetwork_license_servers is specified without ixnetwork_license_type.
            subscription_tier0

            Interfaces only support. For details on the limitations, please refer to
            IxNetwork User Guide.
            subscription_tier1

            It is the most restrictive, with only a few protocols and sessions
            support available per protocol. For details on the limitations, please
            refer to IxNetwork User Guide.
            subscription_tier2

            It provides unlimited protocol and session support for Hardware ports
            and limited protocol and session support for VM ports. For details on
            the limitations, please refer to IxNetwork User Guide.
            subscription_tier3

            It provides unlimited protocol and session support and also the premium
            features.
            mixed

            Mixed mode reffers to mixed HW/VM licensing model. For details on the
            limitations, please refer to IxNetwork User Guide.
            DEFAULT
                None
        Constants Available: IXNETWORK_LICENSE_TYPE_CMD
        Supported:IxNetwork
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.connect({ConnectConstants.IXNETWORK_LICENSE_TYPE_CMD: opt})

    def connect_ixnetwork_tcl_proxy(self, any):
        """
        This is the method the command: connect option ixnetwork_tcl_proxy
        Description:This flag is deprecated and ignored. The IxNetwork proxy server is
            detected automatically. To configure specific proxy server parameters
            please check the -tcl_proxy_username and -close_server_on_disconnect
            arguments.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            The presence of this flag loads the IxTclNetworkConnector package and
            enables connection to the IxNetwork TCL Proxy Server. This parameter is
            valid only when using IxTclNetwork (new API).The address for the TCL
            proxy will be the value specified by the ixnetwork_tcl_server parameter.
            DEFAULT
                None
        Constants Available: IXNETWORK_TCL_PROXY_CMD
        Supported:IxNetwork
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.connect({ConnectConstants.IXNETWORK_TCL_PROXY_CMD: any})

    def connect_ixnetwork_tcl_server(self, any):
        """
        This is the method the command: connect option ixnetwork_tcl_server
        Description:IP address or name of the IxNetwork TCL server, followed optionally by
            :port number;
            When using IxTclProtocol (old API), this parameter is ignored on both
            Windows and Unix platforms.
            When using IxTclNetwork (new API), on Windows platform, if both
            ixnetwork_tcl_server and tcl_server are not specified, the default value
            for ixnetwork_tcl_server is 127.0.0.1:8009. Otherwise, if tcl_server
            option is present and in use, the default value is equal to tcl_server:8009.
            When using IxTclNetwork (new API), on Unix platform, if
            ixnetwork_tcl_server is not specified, the default value is equal to
            tcl_server:8009. This means that, on Unix, if ixnetwork_tcl_server is
            not specified, then tcl_server must be specified.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            IP address or name of the IxNetwork TCL server, followed optionally by :.
            When using IxTclProtocol (old API), this parameter is ignored on both
            Windows and Unix platforms.
            When using IxTclNetwork (new API), on Windows platform, if both
            ixnetwork_tcl_server and tcl_server are not specified, the default value
            for ixnetwork_tcl_server is 127.0.0.1:8009.
            Otherwise, if tcl_server option is present and in use, the default value
            is equal to tcl_server:8009.
            When using IxTclNetwork (new API), on Unix platform, if
            ixnetwork_tcl_server is not specified, the default value is equal to
            tcl_server:8009. This means that, on Unix, if ixnetwork_tcl_server is
            not specified, then tcl_server must be specified.
            DEFAULT
                None
        Constants Available: IXNETWORK_TCL_SERVER_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.connect({ConnectConstants.IXNETWORK_TCL_SERVER_CMD: any})

    def connect_log_path(self, any):
        """
        This is the method the command: connect option log_path
        Description:Sets the path for hltapi logs, when parameter -logging is used.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            Sets the path for hltapi logs, when parameter -logging is used.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'logging' | value= 'hltapi_calls' |
        Constants Available: LOG_PATH_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.connect({ConnectConstants.LOG_PATH_CMD: any})

    def connect_logging(self, opt):
        """
        This is the method the command: connect option logging
        Description:This parameter enables logging HLTAPI commands.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            This parameter enables logging HLTAPI commands.
            Valid options are:
            hltapi_calls

            DEFAULT
                None
        Constants Available: LOGGING_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.connect({ConnectConstants.LOGGING_CMD: opt})

    def connect_master_device(self, any):
        """
        This is the method the command: connect option master_device
        Description:IP address or name of the master chassis, if -device is a slave chassis.
            May contain a list of devices. In this case, the string 'none' can be
            added when the master chassis IP is not applicable.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            IP address or name of the master chassis, if -device is a slave chassis.
            May contain a list of devices. In this case, the string 'none' can be
            added when the master chassis IP is not applicable.
            DEFAULT
                None
        Constants Available: MASTER_DEVICE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.connect({ConnectConstants.MASTER_DEVICE_CMD: any})

    def connect_mode(self, opt):
        """
        This is the method the command: connect option mode
        Description:This parameter depends on 'vport_list' and 'vport_count' parameters.
            More details are available in the description for parameter 'device'.
            This parameter is valid only when IxNetwork Tcl API is used.
            Valid options are:
            connect

            (DEFAULT) connect virtual ports specified with 'vport_list' parameter to
            reconnect_ports

            This mode will force reloading the port configuration on all used
            chassis ports by releasing all ports curently assigned and then connect
            them back with the same vport assignment.<br/> This mode accepts no
            other aguments (any other argument in this mode will be ignored).<br/>
            Valid only for IxTclNetwork. This mode is required when connecting to an
            IxNetwork configuration that uses PCPU traffic configuration for HL
            compatibility. <br/> <b>NOTE: <i>When this reload happens all the port
            configurations that are not present in IxNetwork will be lost (eg.:
            IxTclHal low level commands, HL commands using P HLTSET, HL commands
            using IxTclHal implementation). </i></b>
            disconnect

            disconnect virtual ports specified with 'vport_list' parameter
            save

            save the current ixnetwork configuration (ixncfg) to the file specified
            with at least one of the parameters file_name or file_ixncfg.
            DEFAULT

            connect
            IxNetwork-NGPF

            DESCRIPTION

            This parameter depends on 'vport_list' and 'vport_count' parameters.
            More details are available in the description for parameter 'device'.
            This parameter is valid only when IxNetwork Tcl API is used.
            Valid options are:
            connect

            (DEFAULT) connect virtual ports specified with 'vport_list' parameter to
            the real ports specified with 'port_list' parameter.
            disconnect

            disconnect virtual ports specified with 'vport_list' parameter from the
            real ports they are currently connected to.
            reconnect_ports

            This mode will force reloading the port configuration on all used
            chassis ports by releasing all ports curently assigned and then connect
            them back with the same vport assignment.<br/> This mode accepts no
            other arguments (any other argument in this mode will be ignored).<br/>
            Valid only for IxTclNetwork. This mode is required when connecting to an
            IxNetwork configuration that uses PCPU traffic configuration for HL
            compatibility. <br/> <b>NOTE: <i>When this reload happens all the port
            configurations that are not present in IxNetwork will be lost (eg.:
            IxTclHal low level commands, HL commands using P HLTSET, HL commands
            using IxTclHal implementation). </i></b>
            save

            save the current ixnetwork configuration (ixncfg) to the file specified
            with at least one of the parameters file_name or file_ixncfg.
            DEFAULT

            connect
        Constants Available: MODE_CMD
        Supported:IxNetwork
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.connect({ConnectConstants.MODE_CMD: opt})

    def connect_protocol_stacking_mode(self, opt):
        """
        This is the method the command: connect option protocol_stacking_mode
        Description:This parameter enables the parallel/sequential start/stop of protocol
            layers when multiple protocols are stacked together.
            Valid options are:
            parallel

            The operation on one layer of a device is triggered as soon as the
            operation on the previous layer of this device is completed. This
            behavior provides a more realistic emulation of real world scenarios and
            it is currently supported only for NGPF access protocols.
            sequential

            The operation on one layer must complete on all devices before the same
            operation is triggered on the next layer. This is the default behavior
            of NGPF protocols.
            DEFAULT
                None
        Constants Available: PROTOCOL_STACKING_MODE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.connect({ConnectConstants.PROTOCOL_STACKING_MODE_CMD: opt})

    def connect_return_detailed_handles(self, bool_opt):
        """
        This is the method the command: connect option return_detailed_handles
        Description:This argument determines if individual interface, session or router
            handles are returned by ixiangpf commands. This applies to all HLT
            commands from the current session. Setting this to 0 means that only
            NGPF-specific protocol stack handles will be returned. This will
            significantly decrease the size of command results and speed up script
            execution. Individual item handles can still be retrieved using the
            protocol_info command with -mode handles. The default is 1, meaning all
            possible handles will be returned.
            DEFAULT

            1
        Constants Available: RETURN_DETAILED_HANDLES_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.connect({ConnectConstants.RETURN_DETAILED_HANDLES_CMD: bool_opt})

    def connect_session_resume_include_filter(self, any):
        """
        This is the method the command: connect option session_resume_include_filter
        Description:May contains a list of value that specify an inclusion filter for the
            returned session resume dictionary keys when -session_resume_keys is 1.
            The keys that have items in are dependent on the command that generated
            that kind of typepath. Generally the procedure that generated those
            objects has the same name as the first part in the key. Eg. in
            emulation_bgp_route_config.bgp_sites.objects of type
            vport/protocols/bgp/neighborRange/l2Site are generated by the
            emulation_bgp_route_config command. Valid values are:
            Valid options are:
            connect

            connect.vport_list
            interface_config

            interface_config.interface_handle
            interface_config.routed_interface_handle

            interface_config.gre_interface_handle
            interface_config.atm_endpoints

            interface_config.fr_endpoints
            interface_config.ip_endpoints

            interface_config.lan_endpoints
            interface_config.ig_endpoints

            emulation_bfd_config
            emulation_bfd_config.router_handles

            emulation_bfd_config.router_interface_handles
            emulation_bfd_config.router_interface_handles.<vport/protocols/bfd/router>

            emulation_bfd_config.interface_handles
            emulation_bfd_config.interface_handles.<vport/protocols/bfd/router>

            emulation_bfd_session_config.session_handles
            emulation_bgp_config

            emulation_bgp_config.handles
            emulation_bgp_route_config

            emulation_bgp_route_config.bgp_routes
            emulation_bgp_route_config.bgp_sites

            emulation_bgp_route_config.bgp_sites.<vport/protocols/bgp/neighborRange/l2Site>
            emulation_bgp_route_config.bgp_sites.<vport/protocols/bgp/neighborRange/l3Site>

            emulation_cfm_config
            emulation_cfm_config.handle

            emulation_cfm_config.interface_handles
            emulation_cfm_custom_tlv_config

            emulation_cfm_custom_tlv_config.handle
            emulation_cfm_links_config

            emulation_cfm_links_config.handle
            emulation_cfm_md_meg_config

            emulation_cfm_md_meg_config.handle
            emulation_cfm_mip_mep_config

            emulation_cfm_mip_mep_config.handle
            emulation_cfm_vlan_config

            emulation_cfm_vlan_config.handle
            emulation_cfm_vlan_config.mac_range_handles

            emulation_cfm_vlan_config.mac_range_handles.<vport/protocols/cfm/bridge/vlans>
            emulation_dhcp_config

            emulation_dhcp_config.handle
            emulation_dhcp_group_config

            emulation_dhcp_group_config.handle
            emulation_dhcp_server_config

            emulation_dhcp_server_config.handle
            emulation_dhcp_server_config.handle

            dhcp_client_extension_configdhcp_client_extension_config.handledhcp_server_extension_configdhcp_server_extension_config.handle
            emulation_efm_config

            emulation_efm_config.information_oampdu_id
            emulation_efm_config.event_notification_oampdu_id

            emulation_efm_org_var_config
            emulation_efm_org_var_config.handle

            emulation_eigrp_config
            emulation_eigrp_config.router_handles

            emulation_eigrp_config.interface_handles
            emulation_eigrp_route_config

            emulation_eigrp_route_config.session_handles
            emulation_elmi_configemulation_elmi_config.interface_handlesemulation_elmi_config.uni_handlesemulation_elmi_config.uni_status_handlesemulation_elmi_config.bw_profile_handlesemulation_elmi_config.evc_handlesemulation_elmi_config.ce_vlan_id_range_handles

            emulation_igmp_config
            emulation_igmp_config.handle

            emulation_igmp_group_config
            emulation_igmp_group_config.handle

            emulation_igmp_group_config.source_handle
            emulation_igmp_group_config.group_pool_handle

            emulation_igmp_group_config.source_pool_handle
            emulation_isis_config

            emulation_isis_config.handle
            emulation_isis_topology_route_config

            emulation_isis_topology_route_config.elem_handle
            emulation_isis_topology_route_config.stub

            emulation_isis_topology_route_config.external
            emulation_isis_topology_route_config.grid

            emulation_isis_topology_route_config.grid.connected_session.<vport/protocols/isis/router>.rowemulation_isis_topology_route_config.grid.connected_session.<vport/protocols/isis/router>.col
            l2tp_config l2tp_config.handles
            emulation_lacp_link_config emulation_lacp_link_config.handle

            emulation_ldp_config emulation_ldp_config.handle emulation_ldp_route_config
            emulation_ldp_route_config.lsp_handle emulation_ldp_route_config.lsp_intf

            emulation_ldp_route_config.lsp_vc_range_handles
            emulation_ldp_route_config.lsp_vc_ip_range_handles

            emulation_ldp_route_config.lsp_vc_mac_range_handles
            emulation_mld_config emulation_mld_config.handle

            emulation_mld_group_config
            emulation_mld_group_config.handle

            emulation_mld_group_config.group_pool_handle
            emulation_mld_group_config.source_pool_handles

            emulation_oam_config_msg
            emulation_oam_config_msg.handle

            emulation_oam_config_topology
            emulation_oam_config_topology.handle

            emulation_oam_config_topology.traffic_handles
            emulation_ospf_config

            emulation_ospf_config.handle
            emulation_ospf_topology_route_config

            emulation_ospf_topology_route_config.elem_handle
            emulation_pbb_config

            emulation_pbb_config.handle
            emulation_pbb_config.interface_handles

            emulation_pbb_trunk_config
            emulation_pbb_trunk_config.trunk_handle

            emulation_pbb_trunk_config.mr_handle
            emulation_pim_config

            emulation_pim_config.handle
            emulation_pim_config.interfaces

            emulation_pim_group_config emulation_pim_group_config.handle
            emulation_pim_group_config.group_pool_handle

            emulation_pim_group_config.source_pool_handles
            pppox_config pppox_config.handles

            emulation_rip_config
            emulation_rip_config.handle

            emulation_rip_route_config
            emulation_rip_route_config.route_handle

            emulation_rsvp_config
            emulation_rsvp_config.handles

            emulation_rsvp_config.router_interface_handle
            emulation_rsvp_tunnel_config

            emulation_rsvp_tunnel_config.tunnel_handle
            emulation_rsvp_tunnel_config.tunnel_leaves_handle

            emulation_rsvp_tunnel_config.tunnel_leaves_handle.<vport/protocols/rsvp/neighborPair/destinationRange>
            emulation_rsvp_tunnel_config.tunnel_leaves_handle.<vport/protocols/rsvp/neighborPair/destinationRange>/ingress

            emulation_rsvp_tunnel_config.routed_interfaces
            emulation_stp_msti_config

            emulation_stp_msti_config.handle
            emulation_stp_bridge_config

            emulation_stp_bridge_config.bridge_handle
            emulation_stp_bridge_config.bridge_interface_handles

            emulation_stp_bridge_config.bridge_interface_handles.<vport/protocols/stp/bridge>
            emulation_stp_bridge_config.interface_handles

            emulation_stp_bridge_config.interface_handles.<vport/protocols/stp/bridge>
            emulation_twamp_config

            emulation_twamp_config.handle
            emulation_twamp_control_range_config

            emulation_twamp_control_range_config.handle
            emulation_twamp_test_range_config

            emulation_twamp_test_range_config.handle
            emulation_twamp_server_range_config

            emulation_twamp_server_range_config.handle
            emulation_ancp_config

            emulation_ancp_config.handle
            emulation_ancp_subscriber_lines_config

            emulation_ancp_subscriber_lines_config.handle
            fc_client_config

            fc_client_config.handle
            fc_fport_config

            fc_fport_config.handle
            fc_fport_vnport_config

            fc_fport_vnport_config.handle
            traffic_config traffic_config.stream_id

            traffic_config.traffic_item
            emulation_multicast_group_config

            emulation_multicast_source_config (DEFAULT = {})
            traffic_l47_config

            list of traffic item handles of the existing L47 AppLib traffic items.
            traffic_l47_config.traffic_l47_handle.applib_profile

            to return a list of all the applib profiles under the
            <traffic_l47_handle>. Where the <traffic_l47_handle> is an object of
            type /traffic/trafficItem.
            traffic_l47_config.traffic_l47_handle.applib_profile.applib_flow

            to return a list of flows existing under the <applib_profile>. Where the
            <applib_profile> is an object of type /traffic/trafficItem/appLibProfile.
            traffic_l47_config.traffic_l47_handle.applib_profile.applib_flow.parameter

            to return a list of parameters existing under the <applib_flow>. Where
            the <applib_flow> is an object of type
            /traffic/trafficItem/appLibProfile/appLibFlow.
            traffic_l47_config.traffic_l47_handle.applib_profile.applib_flow.connection

            to return a list of connections existing under the <applib_flow>. Where
            the <applib_flow> is an object of type
            /traffic/trafficItem/appLibProfile/appLibFlow.
            traffic_l47_config.traffic_l47_handle.applib_profile.applib_flow.connection.parameter

            to return a list of parameters existing under the <connection>. Where
            the <connection> is an object of type
            /traffic/trafficItem/appLibProfile/appLibFlow/connection.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            May contains a list of value that specify an inclusion filter for the
            returned session resume dictionary keys when -session_resume_keys is 1.
            The keys that have items in are dependent on the command that generated
            that kind of typepath. Generally the procedure that generated those
            objects has the same name as the first part in the key.
            Eg. in emulation_bgp_route_config.bgp_sites.objects of type
            vport/protocols/bgp/neighborRange/l2Site are generated by the
            emulation_bgp_route_config command.
            Valid values are:
              * connect
              * connect.vport_list
              * interface_config
              * interface_config.interface_handle
              * interface_config.routed_interface_handle
              * interface_config.gre_interface_handle
              * interface_config.atm_endpoints
              * interface_config.fr_endpoints
              * interface_config.ip_endpoints
              * interface_config.lan_endpoints
              * interface_config.ig_endpoints
              * emulation_bfd_config
              * emulation_bfd_config.router_handles
              * emulation_bfd_config.router_interface_handles
              * emulation_bfd_config.router_interface_handles.
              * emulation_bfd_config.interface_handles
              * emulation_bfd_config.interface_handles.
              * emulation_bfd_session_config.session_handles
              * emulation_bgp_config
              * emulation_bgp_config.handles
              * emulation_bgp_route_config
              * emulation_bgp_route_config.bgp_routes
              * emulation_bgp_route_config.bgp_sites
              * emulation_bgp_route_config.bgp_sites.
              * emulation_bgp_route_config.bgp_sites.
              * emulation_cfm_config
              * emulation_cfm_config.handle
              * emulation_cfm_config.interface_handles
              * emulation_cfm_custom_tlv_config
              * emulation_cfm_custom_tlv_config.handle
              * emulation_cfm_links_config
              * emulation_cfm_links_config.handle
              * emulation_cfm_md_meg_config
              * emulation_cfm_md_meg_config.handle
              * emulation_cfm_mip_mep_config
              * emulation_cfm_mip_mep_config.handle
              * emulation_cfm_vlan_config
              * emulation_cfm_vlan_config.handle
              * emulation_cfm_vlan_config.mac_range_handles
              * emulation_cfm_vlan_config.mac_range_handles.
              * emulation_dhcp_config
              * emulation_dhcp_config.handle
              * emulation_dhcp_group_config
              * emulation_dhcp_group_config.handle
              * emulation_dhcp_server_config
              * emulation_dhcp_server_config.handle
              * emulation_dhcp_server_config.handle
              * dhcp_client_extension_config
              * dhcp_client_extension_config.handle
              * dhcp_server_extension_config
              * dhcp_server_extension_config.handle
              * emulation_efm_config
              * emulation_efm_config.information_oampdu_id
              * emulation_efm_config.event_notification_oampdu_id
              * emulation_efm_org_var_config
              * emulation_efm_org_var_config.handle
              * emulation_eigrp_config
              * emulation_eigrp_config.router_handles
              * emulation_eigrp_config.interface_handles
              * emulation_eigrp_route_config
              * emulation_eigrp_route_config.session_handles
              * emulation_igmp_config
              * emulation_igmp_config.handle
              * emulation_igmp_group_config
              * emulation_igmp_group_config.handle
              * emulation_igmp_group_config.source_handle
              * emulation_igmp_group_config.group_pool_handle
              * emulation_igmp_group_config.source_pool_handle
              * emulation_isis_config
              * emulation_isis_config.handle
              * emulation_isis_topology_route_config
              * emulation_isis_topology_route_config.elem_handle
              * emulation_isis_topology_route_config.stub
              * emulation_isis_topology_route_config.external
              * emulation_isis_topology_route_config.grid
              * emulation_isis_topology_route_config.grid.connected_session..row
              * emulation_isis_topology_route_config.grid.connected_session..col
              * l2tp_config
              * l2tp_config.handles
              * emulation_lacp_link_config
              * emulation_lacp_link_config.handle
              * emulation_ldp_config
              * emulation_ldp_config.handle
              * emulation_ldp_route_config
              * emulation_ldp_route_config.lsp_handle
              * emulation_ldp_route_config.lsp_intf
              * emulation_ldp_route_config.lsp_vc_range_handles
              * emulation_ldp_route_config.lsp_vc_ip_range_handles
              * emulation_ldp_route_config.lsp_vc_mac_range_handles
              * emulation_mld_config
              * emulation_mld_config.handle
              * emulation_mld_group_config
              * emulation_mld_group_config.handle
              * emulation_mld_group_config.group_pool_handle
              * emulation_mld_group_config.source_pool_handles
              * emulation_oam_config_msg
              * emulation_oam_config_msg.handle
              * emulation_oam_config_topology
              * emulation_oam_config_topology.handle
              * emulation_oam_config_topology.traffic_handles
              * emulation_ospf_config
              * emulation_ospf_config.handle
              * emulation_ospf_topology_route_config
              * emulation_ospf_topology_route_config.elem_handle
              * emulation_pbb_config
              * emulation_pbb_config.handle
              * emulation_pbb_config.interface_handles
              * emulation_pbb_trunk_config
              * emulation_pbb_trunk_config.trunk_handle
              * emulation_pbb_trunk_config.mr_handle
              * emulation_pim_config
              * emulation_pim_config.handle
              * emulation_pim_config.interfaces
              * emulation_pim_group_config
              * emulation_pim_group_config.handle
              * emulation_pim_group_config.group_pool_handle
              * emulation_pim_group_config.source_pool_handles
              * pppox_config
              * pppox_config.handles
              * emulation_rip_config
              * emulation_rip_config.handle
              * emulation_rip_route_config
              * emulation_rip_route_config.route_handle
              * emulation_rsvp_config
              * emulation_rsvp_config.handles
              * emulation_rsvp_config.router_interface_handle
              * emulation_rsvp_tunnel_config
              * emulation_rsvp_tunnel_config.tunnel_handle
              * emulation_rsvp_tunnel_config.tunnel_leaves_handle
              * emulation_rsvp_tunnel_config.tunnel_leaves_handle.
              * emulation_rsvp_tunnel_config.tunnel_leaves_handle./ingress
              * emulation_rsvp_tunnel_config.routed_interfaces
              * emulation_stp_msti_config
              * emulation_stp_msti_config.handle
              * emulation_stp_bridge_config
              * emulation_stp_bridge_config.bridge_handle
              * emulation_stp_bridge_config.bridge_interface_handles
              * emulation_stp_bridge_config.bridge_interface_handles.
              * emulation_stp_bridge_config.interface_handles
              * emulation_stp_bridge_config.interface_handles.
              * emulation_twamp_config
              * emulation_twamp_config.handle
              * emulation_twamp_control_range_config
              * emulation_twamp_control_range_config.handle
              * emulation_twamp_test_range_config
              * emulation_twamp_test_range_config.handle
              * emulation_twamp_server_range_config
              * emulation_twamp_server_range_config.handle
              * emulation_ancp_config
              * emulation_ancp_config.handle
              * emulation_ancp_subscriber_lines_config
              * emulation_ancp_subscriber_lines_config.handle
              * fc_client_config
              * fc_client_config.handle
              * fc_fport_config
              * fc_fport_config.handle
              * fc_fport_vnport_config
              * fc_fport_vnport_config.handle
              * traffic_config
              * traffic_config.stream_id
              * traffic_config.traffic_item
              * emulation_multicast_group_config
              * emulation_multicast_source_config
            DEFAULT

            {}
        Constants Available: SESSION_RESUME_INCLUDE_FILTER_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.connect({ConnectConstants.SESSION_RESUME_INCLUDE_FILTER_CMD: any})

    def connect_session_resume_keys(self, bool_opt):
        """
        This is the method the command: connect option session_resume_keys
        Description:Using this parameter when loading an ixncfg file allows you to choose
            whether to show the session resume keys or not. This parameter is valid
            only when using IxTclNetwork. If global parameter
            ::::session_resume_keys does not exist, it will be overwritten by
            ::::connect local parameter -session_resume_keys.
            Valid options are:
            0

            do not show the session resume keys
            1

            show the session resume keys
            DEFAULT

            1
            IxNetwork-NGPF

            DESCRIPTION

            Using this parameter when loading an ixncfg file allows you to choose
            whether to show the session resume keys or not. This parameter is valid
            only when using IxTclNetwork. If global parameter
            ::::session_resume_keys does not exist, it will be overwritten by
            ::::connect local parameter -session_resume_keys. Valid choices are:
            Valid options are:
            0

            do not show the session resume keys
            1

            show the session resume keys
            DEFAULT

            1
        Constants Available: SESSION_RESUME_KEYS_CMD
        Supported:IxNetwork
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.connect({ConnectConstants.SESSION_RESUME_KEYS_CMD: bool_opt})

    def connect_tcl_server(self, any):
        """
        This is the method the command: connect option tcl_server
        Description:IP address or name of the ixTclServer. When using IxTclProtocol (old
            API), this parameter is ignored on Windows platforms. On Unix platforms,
            the default value is the first item in option 'device' list.
            When using IxTclNetwork (new API) on Windows platform, if both
            tcl_server and ixnetwork_tcl_server are not specified, the default value
            is 127.0.0.1. If ixnetwork_tcl_server is present, the default value is
            equal to ixnetwork_tcl_server and if this fails it will fallback to the
            value of the first item in option 'device' list. When using IxTclNetwork
            (new API) on Unix platform, if tcl_server is not specified, the default
            value is equal to ixnetwork_tcl_server. This means that, on Unix, if
            tcl_server is not specified, then ixnetwork_tcl_server must be specified.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            IP address or name of the ixTclServer. When using IxTclProtocol (old
            API), this parameter is ignored on Windows platforms. On Unix platforms,
            the default value is the first item in option 'device' list.
            When using IxTclNetwork (new API) on Windows platform, if both
            tcl_server and ixnetwork_tcl_server are not specified, the default value
            is 127.0.0.1. If ixnetwork_tcl_server is present, the default value is
            equal to ixnetwork_tcl_server and if this fails it will fallback to the
            value of the first item in option 'device' list. When using IxTclNetwork
            (new API) on Unix platform, if tcl_server is not specified, the default
            value is equal to ixnetwork_tcl_server. This means that, on Unix, if
            tcl_server is not specified, then ixnetwork_tcl_server must be specified.
            DEFAULT
                None
        Constants Available: TCL_SERVER_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.connect({ConnectConstants.TCL_SERVER_CMD: any})

    def connect_vport_count(self, range):
        """
        This is the method the command: connect option vport_count
        Description:More details are available in the description for parameter 'device'.
            This parameter is valid only when IxNetwork Tcl API is used and it
            configures the number of virtual ports to be created. When this
            parameter is specified the parameters 'device' , 'port_list',
            'vport_list', 'mode' are ignored. The virtual port handles created are
            returned with 'vport_handle' key.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            More details are available in the description for parameter 'device'.
            This parameter is valid only when IxNetwork Tcl API is used and it
            configures the number of virtual ports to be created. When this
            parameter is specified the parameters 'device' , 'port_list',
            'vport_list', 'mode' are ignored. The virtual port handles created are
            returned with 'vport_handle' key.
            DEFAULT
                None
        Constants Available: VPORT_COUNT_CMD
        Supported:IxNetwork
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.connect({ConnectConstants.VPORT_COUNT_CMD: range})

    def connect_vport_list(self, any):
        """
        This is the method the command: connect option vport_list
        Description:More details are available in the description for parameter 'device'.
            This parameter is valid only when IxNetwork Tcl API is used. When
            parameter 'mode' is 'disconnect', the virtual ports specified will be
            disconnected from the real ports they are connected to. Parameters
            'device' and 'port_list' are ignored. When parameter 'mode' is 'connect'
            parameters 'device' and 'port_list' are mandatory. The virtual ports
            specified with 'vport_list' will be connected to the real ports
            specified with 'port_list' and 'device'.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            More details are available in the description for parameter 'device'.
            This parameter is valid only when IxNetwork Tcl API is used. When
            parameter 'mode' is 'disconnect', the virtual ports specified will be
            disconnected from the real ports they are connected to. Parameters
            'device' and 'port_list' are ignored. When parameter 'mode' is 'connect'
            parameters 'device' and 'port_list' are mandatory. The virtual ports
            specified with 'vport_list' will be connected to the real ports
            specified with 'port_list' and 'device'.
            DEFAULT
                None
        Constants Available: VPORT_LIST_CMD
        Supported:IxNetwork
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.connect({ConnectConstants.VPORT_LIST_CMD: any})

    supportedIxiaHltapiCommands = {ConnectConstants.AGGREGATION_MODE_CMD,
                                   ConnectConstants.AGGREGATION_RESOURCE_MODE_CMD, ConnectConstants.BREAK_LOCKS_CMD,
                                   ConnectConstants.CHAIN_CABLES_LENGTH_CMD, ConnectConstants.CHAIN_SEQUENCE_CMD,
                                   ConnectConstants.CHAIN_TYPE_CMD, ConnectConstants.CLOSE_SERVER_ON_DISCONNECT_CMD,
                                   ConnectConstants.CONFIG_FILE_CMD, ConnectConstants.CONFIG_FILE_HLT_CMD,
                                   ConnectConstants.CONNECT_TIMEOUT_CMD, ConnectConstants.DEVICE_CMD,
                                   ConnectConstants.ENABLE_WIN_TCL_SERVER_CMD, ConnectConstants.EXECUTION_TIMEOUT_CMD,
                                   ConnectConstants.FORCELOAD_CMD, ConnectConstants.GUARD_RAIL_CMD,
                                   ConnectConstants.HELPER_CMD, ConnectConstants.INTERACTIVE_CMD,
                                   ConnectConstants.IXNETWORK_LICENSE_SERVERS_CMD,
                                   ConnectConstants.IXNETWORK_LICENSE_TYPE_CMD,
                                   ConnectConstants.IXNETWORK_TCL_PROXY_CMD, ConnectConstants.IXNETWORK_TCL_SERVER_CMD,
                                   ConnectConstants.LOG_PATH_CMD, ConnectConstants.LOGGING_CMD,
                                   ConnectConstants.MASTER_DEVICE_CMD, ConnectConstants.MODE_CMD,
                                   ConnectConstants.NOBIOS_CMD, ConnectConstants.PORT_LIST_CMD,
                                   ConnectConstants.PROTOCOL_STACKING_MODE_CMD, ConnectConstants.RESET_CMD,
                                   ConnectConstants.RETURN_DETAILED_HANDLES_CMD,
                                   ConnectConstants.SESSION_RESUME_INCLUDE_FILTER_CMD,
                                   ConnectConstants.SESSION_RESUME_KEYS_CMD, ConnectConstants.SYNC_CMD,
                                   ConnectConstants.TCL_PROXY_USERNAME_CMD, ConnectConstants.TCL_SERVER_CMD,
                                   ConnectConstants.TIMEOUT_CMD, ConnectConstants.USERNAME_CMD,
                                   ConnectConstants.VPORT_COUNT_CMD, ConnectConstants.VPORT_LIST_CMD}
    # supportedIxiaHltapiCommands = {ConnectConstants.AGGREGATION_MODE_CMD: "IxTclNetwork:7.40.929.15,IxTclHal:6.80"}
