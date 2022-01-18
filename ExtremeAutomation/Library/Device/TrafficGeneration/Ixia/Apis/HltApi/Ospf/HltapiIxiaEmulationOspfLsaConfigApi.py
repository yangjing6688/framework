from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.Ospf.HltapiEmulationOspfLsaConfigApi import EmulationOspfLsaConfigApi, EmulationOspfLsaConfigConstants

"""
    This is the API class for the command: emulation_ospf_lsa_config

    Class is auto-generated. If you update anything here,
        it will be over written.
"""


class IxiaEmulationOspfLsaConfigApi(EmulationOspfLsaConfigApi):

    """
    init function
    """
    def __init__(self, device):
        super(IxiaEmulationOspfLsaConfigApi, self).__init__(device)

    """
    This is the "One Large Method" for the command: emulation_ospf_lsa_config
    use this by passing in a dict() of all the commands

        api = device.getApi(EmulationOspfLsaConfigConstants.EMULATION_OSPF_LSA_CONFIG_API)
        assert isinstance(api, EmulationOspfLsaConfigApi)
        api.emulation_ospf_lsa_config(dummyDict)
    """
    def emulation_ospf_lsa_config(self, argdictionary):
        return super(IxiaEmulationOspfLsaConfigApi, self).emulation_ospf_lsa_config(argdictionary, self.supportedIxiaHltapiCommands)

    """
    Individual commands for each option. Typically, the "One Large Method"
    is the one that you want to be using so look at that example above
    """
    def emulation_ospf_lsa_config_area_id(self, ip):
        """
        This is the method the command: emulation_ospf_lsa_config option area_id
        Description:The area ID of the User LSA Group.This option is valid only for
            IxTclNetwork API.
            DEFAULT

            0.0.0.0
            IxNetwork-NGPF

            DESCRIPTION

            The area ID of the User LSA Group. This option is valid only for
            IxTclNetwork API.
            DEFAULT

            0.0.0.0
        Constants Available: AREA_ID_CMD
        Supported:IxNetwork
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.AREA_ID_CMD : ip})

    def emulation_ospf_lsa_config_external_metric_ebit(self, opt):
        """
        This is the method the command: emulation_ospf_lsa_config option external_metric_ebit
        Description:The value of the external metric's E-bit.
            DEFAULT

            0
            IxNetwork-NGPF

            DESCRIPTION

            The value of the external metric's E-bit.
            Valid options are:
            1

            0

            DEFAULT

            0
        Constants Available: EXTERNAL_METRIC_EBIT_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.EXTERNAL_METRIC_EBIT_CMD : opt})

    def emulation_ospf_lsa_config_external_metric_fbit(self, opt):
        """
        This is the method the command: emulation_ospf_lsa_config option external_metric_fbit
        Description:The value of the external metric's F-bit. If true, then the
            forwardingAddress field is to be included in the LSA.
            DEFAULT

            1
            IxNetwork-NGPF

            DESCRIPTION

            The value of the external metric's F-bit. If true, then the
            forwardingAddress field is to be included in the LSA.
            Valid options are:
            1

            0

            DEFAULT

            1
        Constants Available: EXTERNAL_METRIC_FBIT_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.EXTERNAL_METRIC_FBIT_CMD : opt})

    def emulation_ospf_lsa_config_external_metric_tbit(self, opt):
        """
        This is the method the command: emulation_ospf_lsa_config option external_metric_tbit
        Description:The value of the external metric's T-bit. If true, then the
            externalRouteTag field will be included in the LSA.
            DEFAULT

            1
            IxNetwork-NGPF

            DESCRIPTION

            The value of the external metric's T-bit. If true, then the
            externalRouteTag field will be included in the LSA.
            Valid options are:
            1

            0

            DEFAULT

            1
        Constants Available: EXTERNAL_METRIC_TBIT_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.EXTERNAL_METRIC_TBIT_CMD : opt})

    def emulation_ospf_lsa_config_lsa_group_mode(self, opt):
        """
        This is the method the command: emulation_ospf_lsa_config option lsa_group_mode
        Description:The two modes are append or create. Append means appending the new LSA
            to the last LSA group created. Create means creating a new LSA group for
            the newly added LSA. This option is valid only for -mode create. This
            option is valid only for IxTclNetwork API.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            The two modes are append or create. Append means appending the new LSA
            to the last LSA group created. Create means creating a new LSA group for
            the newly added LSA. This option is valid only for -mode create. This
            option is valid only for IxTclNetwork API.
            Valid options are:
            append

            create

            DEFAULT

            append
        Constants Available: LSA_GROUP_MODE_CMD
        Supported:IxNetwork
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.LSA_GROUP_MODE_CMD : opt})

    def emulation_ospf_lsa_config_no_write(self, flag):
        """
        This is the method the command: emulation_ospf_lsa_config option no_write
        Description:If this option is present, the protocol configuration will not be
            written to the server.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            If this option is present, the protocol configuration will not be
            written to the server.
            DEFAULT
                None
        Constants Available: NO_WRITE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        flag --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.NO_WRITE_CMD : flag})

    def emulation_ospf_lsa_config_opaque_link_other_subtlvs(self, any):
        """
        This is the method the command: emulation_ospf_lsa_config option opaque_link_other_subtlvs
        Description:Allows the user to create custom Sub-TLVs - for Traffic Engineering. To
            be provided with a list of parameters in the following format:::, where
            type is from 0 to 65535, length is a value from 0 to 65535 and value is
            a hex number preceeded by 0x with the length specified by parameter.When
            both -opaque_link_subtlvs and -opaque_link_other_subtlvs are provided
            then -opaque_link_subtlvs has a greater priority. This option is valid
            only when -type is opaque and -opaque_tlv_type is link. This option is
            valid only for IxTclNetwork API.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            Allows the user to create custom Sub-TLVs - for Traffic Engineering. To
            be provided with a list of parameters in the following format: ::, where
            type is from 0 to 65535, length is a value from 0 to 65535 and value is
            a hex number preceeded by 0x with the length specified by parameter.
            When both -opaque_link_subtlvs and -opaque_link_other_subtlvs are
            provided then -opaque_link_subtlvs has a greater priority. This option
            is valid only when type is opaque and opaque_tlv_type is link. This
            option is valid only for IxTclNetwork API.
            DEFAULT
                None
        Constants Available: OPAQUE_LINK_OTHER_SUBTLVS_CMD
        Supported:IxNetwork
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.OPAQUE_LINK_OTHER_SUBTLVS_CMD : any})

    def emulation_ospf_lsa_config_prefix_options(self, any):
        """
        This is the method the command: emulation_ospf_lsa_config option prefix_options
        Description:An 8-bit quantity with options related to the prefixAddress. Multiple
            bits may be combined using a logical or. If both options and
            prefix_options are provided, the options value takes priority.
            Valid options are:
            ospfV3PrefixOptionPBit

            0x08--The propagate bit, which is set on
            x

            0x08--The propagate bit, which is set on
            ospfV3PrefixOptionMCBit

            0x04--The multicast capability bit, which
            ospfV3PrefixOptionLABit

            0x02--The local address capability bit,
            ospfV3PrefixOptionNUBit

            0x01--The no unicast bit, which should be
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            An 8-bit quantity with options related to the prefixAddress. Multiple
            bits may be combined using a logical or. If both options and
            prefix_options are provided, the options value takes priority. Valid
            choices are: ospfV3PrefixOptionPBit - 0x08--The propagate bit, which is
            set on NSSA area prefixes that should be re-advertised at the NSSA area
            border. ospfV3PrefixOptionMCBit - 0x04--The multicast capability bit,
            which should be set if the prefix should be included in IPv6 multicast
            routing calculations. ospfV3PrefixOptionLABit - 0x02--The local address
            capability bit, which should be set if the prefix is actually an IPv6
            interface address of the advertising router. ospfV3PrefixOptionNUBit -
            0x01--The no unicast bit, which should be set if the prefix should be
            excluded from IPv6 unicast calculations.
            DEFAULT
                None
        Constants Available: PREFIX_OPTIONS_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.PREFIX_OPTIONS_CMD : any})

    def emulation_ospf_lsa_config_router_wildcard(self, bool_opt):
        """
        This is the method the command: emulation_ospf_lsa_config option router_wildcard
        Description:Indicates that the router is a wild-card multicast receiver and will
            receive multicast datagrams regardless of destination.
            DEFAULT

            0
            IxNetwork-NGPF

            DESCRIPTION

            Indicates that the router is a wild-card multicast receiver and will
            receive multicast datagrams regardless of destination.
            DEFAULT

            0
        Constants Available: ROUTER_WILDCARD_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.ROUTER_WILDCARD_CMD : bool_opt})


    supportedIxiaHltapiCommands = {EmulationOspfLsaConfigConstants.ADV_ROUTER_ID_CMD, EmulationOspfLsaConfigConstants.AREA_ID_CMD, EmulationOspfLsaConfigConstants.ATTACHED_ROUTER_ID_CMD, EmulationOspfLsaConfigConstants.AUTO_LS_AGE_CMD, EmulationOspfLsaConfigConstants.AUTO_LS_CHECKSUM_CMD, EmulationOspfLsaConfigConstants.AUTO_LS_SEQ_CMD, EmulationOspfLsaConfigConstants.AUTO_UPDATE_CMD, EmulationOspfLsaConfigConstants.EXTERNAL_METRIC_EBIT_CMD, EmulationOspfLsaConfigConstants.EXTERNAL_METRIC_FBIT_CMD, EmulationOspfLsaConfigConstants.EXTERNAL_METRIC_TBIT_CMD, EmulationOspfLsaConfigConstants.EXTERNAL_NUMBER_OF_PREFIX_CMD, EmulationOspfLsaConfigConstants.EXTERNAL_PREFIX_FORWARD_ADDR_CMD, EmulationOspfLsaConfigConstants.EXTERNAL_PREFIX_LENGTH_CMD, EmulationOspfLsaConfigConstants.EXTERNAL_PREFIX_METRIC_CMD, EmulationOspfLsaConfigConstants.EXTERNAL_PREFIX_START_CMD, EmulationOspfLsaConfigConstants.EXTERNAL_PREFIX_STEP_CMD, EmulationOspfLsaConfigConstants.EXTERNAL_PREFIX_TYPE_CMD, EmulationOspfLsaConfigConstants.EXTERNAL_ROUTE_TAG_CMD, EmulationOspfLsaConfigConstants.HANDLE_CMD, EmulationOspfLsaConfigConstants.LINK_STATE_ID_CMD, EmulationOspfLsaConfigConstants.LINK_STATE_ID_STEP_CMD, EmulationOspfLsaConfigConstants.LS_AGE_CMD, EmulationOspfLsaConfigConstants.LS_CHECKSUM_CMD, EmulationOspfLsaConfigConstants.LS_SEQ_CMD, EmulationOspfLsaConfigConstants.LS_TYPE_FUNCTION_CODE_CMD, EmulationOspfLsaConfigConstants.LS_TYPE_S_BITS_CMD, EmulationOspfLsaConfigConstants.LS_TYPE_U_BIT_CMD, EmulationOspfLsaConfigConstants.LSA_GROUP_MODE_CMD, EmulationOspfLsaConfigConstants.LSA_HANDLE_CMD, EmulationOspfLsaConfigConstants.MODE_CMD, EmulationOspfLsaConfigConstants.NET_ATTACHED_ROUTER_CMD, EmulationOspfLsaConfigConstants.NET_PREFIX_LENGTH_CMD, EmulationOspfLsaConfigConstants.NO_WRITE_CMD, EmulationOspfLsaConfigConstants.NSSA_NUMBER_OF_PREFIX_CMD, EmulationOspfLsaConfigConstants.NSSA_PREFIX_FORWARD_ADDR_CMD, EmulationOspfLsaConfigConstants.NSSA_PREFIX_LENGTH_CMD, EmulationOspfLsaConfigConstants.NSSA_PREFIX_METRIC_CMD, EmulationOspfLsaConfigConstants.NSSA_PREFIX_START_CMD, EmulationOspfLsaConfigConstants.NSSA_PREFIX_STEP_CMD, EmulationOspfLsaConfigConstants.NSSA_PREFIX_TYPE_CMD, EmulationOspfLsaConfigConstants.OPAQUE_ENABLE_LINK_ID_CMD, EmulationOspfLsaConfigConstants.OPAQUE_ENABLE_LINK_LOCAL_IP_ADDR_CMD, EmulationOspfLsaConfigConstants.OPAQUE_ENABLE_LINK_MAX_BW_CMD, EmulationOspfLsaConfigConstants.OPAQUE_ENABLE_LINK_MAX_RESV_BW_CMD, EmulationOspfLsaConfigConstants.OPAQUE_ENABLE_LINK_METRIC_CMD, EmulationOspfLsaConfigConstants.OPAQUE_ENABLE_LINK_REMOTE_IP_ADDR_CMD, EmulationOspfLsaConfigConstants.OPAQUE_ENABLE_LINK_RESOURCE_CLASS_CMD, EmulationOspfLsaConfigConstants.OPAQUE_ENABLE_LINK_TYPE_CMD, EmulationOspfLsaConfigConstants.OPAQUE_ENABLE_LINK_UNRESV_BW_CMD, EmulationOspfLsaConfigConstants.OPAQUE_LINK_ID_CMD, EmulationOspfLsaConfigConstants.OPAQUE_LINK_LOCAL_IP_ADDR_CMD, EmulationOspfLsaConfigConstants.OPAQUE_LINK_MAX_BW_CMD, EmulationOspfLsaConfigConstants.OPAQUE_LINK_MAX_RESV_BW_CMD, EmulationOspfLsaConfigConstants.OPAQUE_LINK_METRIC_CMD, EmulationOspfLsaConfigConstants.OPAQUE_LINK_OTHER_SUBTLVS_CMD, EmulationOspfLsaConfigConstants.OPAQUE_LINK_REMOTE_IP_ADDR_CMD, EmulationOspfLsaConfigConstants.OPAQUE_LINK_RESOURCE_CLASS_CMD, EmulationOspfLsaConfigConstants.OPAQUE_LINK_SUBTLVS_CMD, EmulationOspfLsaConfigConstants.OPAQUE_LINK_TYPE_CMD, EmulationOspfLsaConfigConstants.OPAQUE_LINK_UNRESV_BW_PRIORITY_CMD, EmulationOspfLsaConfigConstants.OPAQUE_ROUTER_ADDR_CMD, EmulationOspfLsaConfigConstants.OPAQUE_TLV_TYPE_CMD, EmulationOspfLsaConfigConstants.OPTIONS_CMD, EmulationOspfLsaConfigConstants.PREFIX_OPTIONS_CMD, EmulationOspfLsaConfigConstants.ROUTER_ABR_CMD, EmulationOspfLsaConfigConstants.ROUTER_ASBR_CMD, EmulationOspfLsaConfigConstants.ROUTER_LINK_DATA_CMD, EmulationOspfLsaConfigConstants.ROUTER_LINK_ID_CMD, EmulationOspfLsaConfigConstants.ROUTER_LINK_IDX_CMD, EmulationOspfLsaConfigConstants.ROUTER_LINK_METRIC_CMD, EmulationOspfLsaConfigConstants.ROUTER_LINK_MODE_CMD, EmulationOspfLsaConfigConstants.ROUTER_LINK_TYPE_CMD, EmulationOspfLsaConfigConstants.ROUTER_VIRTUAL_LINK_ENDPT_CMD, EmulationOspfLsaConfigConstants.ROUTER_WILDCARD_CMD, EmulationOspfLsaConfigConstants.SESSION_TYPE_CMD, EmulationOspfLsaConfigConstants.SUMMARY_NUMBER_OF_PREFIX_CMD, EmulationOspfLsaConfigConstants.SUMMARY_PREFIX_LENGTH_CMD, EmulationOspfLsaConfigConstants.SUMMARY_PREFIX_METRIC_CMD, EmulationOspfLsaConfigConstants.SUMMARY_PREFIX_START_CMD, EmulationOspfLsaConfigConstants.SUMMARY_PREFIX_STEP_CMD, EmulationOspfLsaConfigConstants.TE_ADMIN_GROUP_CMD, EmulationOspfLsaConfigConstants.TE_INSTANCE_ID_CMD, EmulationOspfLsaConfigConstants.TE_LINK_ID_CMD, EmulationOspfLsaConfigConstants.TE_LINK_TYPE_CMD, EmulationOspfLsaConfigConstants.TE_LOCAL_IP_CMD, EmulationOspfLsaConfigConstants.TE_MAX_BW_CMD, EmulationOspfLsaConfigConstants.TE_MAX_RESV_BW_CMD, EmulationOspfLsaConfigConstants.TE_MAX_RESV_PRIORITY0_CMD, EmulationOspfLsaConfigConstants.TE_MAX_RESV_PRIORITY1_CMD, EmulationOspfLsaConfigConstants.TE_MAX_RESV_PRIORITY2_CMD, EmulationOspfLsaConfigConstants.TE_MAX_RESV_PRIORITY3_CMD, EmulationOspfLsaConfigConstants.TE_MAX_RESV_PRIORITY4_CMD, EmulationOspfLsaConfigConstants.TE_MAX_RESV_PRIORITY5_CMD, EmulationOspfLsaConfigConstants.TE_MAX_RESV_PRIORITY6_CMD, EmulationOspfLsaConfigConstants.TE_MAX_RESV_PRIORITY7_CMD, EmulationOspfLsaConfigConstants.TE_METRIC_CMD, EmulationOspfLsaConfigConstants.TE_REMOTE_IP_CMD, EmulationOspfLsaConfigConstants.TE_ROUTER_ADDRESS_CMD, EmulationOspfLsaConfigConstants.TE_TLV_TYPE_CMD, EmulationOspfLsaConfigConstants.TYPE_CMD}
