from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.TrafficGenerationApi import TrafficGenerationApi
from ExtremeAutomation.Library.Utils.Singleton import Singleton

"""
    This is the API class for the command: emulation_ospf_lsa_config

    Class is auto-generated. If you update anything here,
        it will be over written.
"""


class EmulationOspfLsaConfigApi(TrafficGenerationApi):

    """
    init function
    """
    def __init__(self, device):
        super(EmulationOspfLsaConfigApi, self).__init__(device)

    """
    This is the "One Large Method" for the command: emulation_ospf_lsa_config
    use this by passing in a dict() of all the commands
        dummyDict = dict()
        dummyDict[EmulationOspfLsaConfigConstants.ADV_ROUTER_ID_CMD] = "dummyValue1" # static value
        dummyDict[EmulationOspfLsaConfigConstants.AREA_ID_CMD] = "dummyValue2" # static value
        dummyDict[EmulationOspfLsaConfigConstants.ATTACHED_ROUTER_ID_CMD] = "dummyValue3" # static value
        dummyDict[EmulationOspfLsaConfigConstants.AUTO_LS_AGE_CMD] = "dummyValue4" # static value
        dummyDict[EmulationOspfLsaConfigConstants.AUTO_LS_CHECKSUM_CMD] = "dummyValue5" # static value
        dummyDict[EmulationOspfLsaConfigConstants.AUTO_LS_SEQ_CMD] = "dummyValue6" # static value
        dummyDict[EmulationOspfLsaConfigConstants.AUTO_UPDATE_CMD] = "dummyValue7" # static value
        dummyDict[EmulationOspfLsaConfigConstants.EXTERNAL_METRIC_EBIT_CMD] = EmulationOspfLsaConfigConstants.EXTERNAL_METRIC_EBIT_0 # constant value
        dummyDict[EmulationOspfLsaConfigConstants.EXTERNAL_METRIC_FBIT_CMD] = EmulationOspfLsaConfigConstants.EXTERNAL_METRIC_FBIT_0 # constant value
        dummyDict[EmulationOspfLsaConfigConstants.EXTERNAL_METRIC_TBIT_CMD] = EmulationOspfLsaConfigConstants.EXTERNAL_METRIC_TBIT_0 # constant value
        dummyDict[EmulationOspfLsaConfigConstants.EXTERNAL_NUMBER_OF_PREFIX_CMD] = "dummyValue11" # static value
        dummyDict[EmulationOspfLsaConfigConstants.EXTERNAL_PREFIX_FORWARD_ADDR_CMD] = "dummyValue12" # static value
        dummyDict[EmulationOspfLsaConfigConstants.EXTERNAL_PREFIX_LENGTH_CMD] = "dummyValue13" # static value
        dummyDict[EmulationOspfLsaConfigConstants.EXTERNAL_PREFIX_METRIC_CMD] = "dummyValue14" # static value
        dummyDict[EmulationOspfLsaConfigConstants.EXTERNAL_PREFIX_START_CMD] = "dummyValue15" # static value
        dummyDict[EmulationOspfLsaConfigConstants.EXTERNAL_PREFIX_STEP_CMD] = "dummyValue16" # static value
        dummyDict[EmulationOspfLsaConfigConstants.EXTERNAL_PREFIX_TYPE_CMD] = EmulationOspfLsaConfigConstants.EXTERNAL_PREFIX_TYPE_1 # constant value
        dummyDict[EmulationOspfLsaConfigConstants.EXTERNAL_ROUTE_TAG_CMD] = "dummyValue18" # static value
        dummyDict[EmulationOspfLsaConfigConstants.HANDLE_CMD] = "dummyValue19" # static value
        dummyDict[EmulationOspfLsaConfigConstants.LINK_STATE_ID_CMD] = "dummyValue20" # static value
        dummyDict[EmulationOspfLsaConfigConstants.LINK_STATE_ID_STEP_CMD] = "dummyValue21" # static value
        dummyDict[EmulationOspfLsaConfigConstants.LS_AGE_CMD] = "dummyValue22" # static value
        dummyDict[EmulationOspfLsaConfigConstants.LS_CHECKSUM_CMD] = "dummyValue23" # static value
        dummyDict[EmulationOspfLsaConfigConstants.LS_SEQ_CMD] = "dummyValue24" # static value
        dummyDict[EmulationOspfLsaConfigConstants.LS_TYPE_FUNCTION_CODE_CMD] = "dummyValue25" # static value
        dummyDict[EmulationOspfLsaConfigConstants.LS_TYPE_S_BITS_CMD] = "dummyValue26" # static value
        dummyDict[EmulationOspfLsaConfigConstants.LS_TYPE_U_BIT_CMD] = "dummyValue27" # static value
        dummyDict[EmulationOspfLsaConfigConstants.LSA_GROUP_MODE_CMD] = EmulationOspfLsaConfigConstants.LSA_GROUP_MODE_ANY # constant value
        dummyDict[EmulationOspfLsaConfigConstants.LSA_HANDLE_CMD] = "dummyValue29" # static value
        dummyDict[EmulationOspfLsaConfigConstants.MODE_CMD] = EmulationOspfLsaConfigConstants.MODE_CREATE # constant value
        dummyDict[EmulationOspfLsaConfigConstants.NET_ATTACHED_ROUTER_CMD] = EmulationOspfLsaConfigConstants.NET_ATTACHED_ROUTER_CREATE # constant value
        dummyDict[EmulationOspfLsaConfigConstants.NET_PREFIX_LENGTH_CMD] = "dummyValue32" # static value
        dummyDict[EmulationOspfLsaConfigConstants.NO_WRITE_CMD] = "dummyValue33" # static value
        dummyDict[EmulationOspfLsaConfigConstants.NSSA_NUMBER_OF_PREFIX_CMD] = "dummyValue34" # static value
        dummyDict[EmulationOspfLsaConfigConstants.NSSA_PREFIX_FORWARD_ADDR_CMD] = "dummyValue35" # static value
        dummyDict[EmulationOspfLsaConfigConstants.NSSA_PREFIX_LENGTH_CMD] = "dummyValue36" # static value
        dummyDict[EmulationOspfLsaConfigConstants.NSSA_PREFIX_METRIC_CMD] = "dummyValue37" # static value
        dummyDict[EmulationOspfLsaConfigConstants.NSSA_PREFIX_START_CMD] = "dummyValue38" # static value
        dummyDict[EmulationOspfLsaConfigConstants.NSSA_PREFIX_STEP_CMD] = "dummyValue39" # static value
        dummyDict[EmulationOspfLsaConfigConstants.NSSA_PREFIX_TYPE_CMD] = "dummyValue40" # static value
        dummyDict[EmulationOspfLsaConfigConstants.OPAQUE_ENABLE_LINK_ID_CMD] = "dummyValue41" # static value
        dummyDict[EmulationOspfLsaConfigConstants.OPAQUE_ENABLE_LINK_LOCAL_IP_ADDR_CMD] = "dummyValue42" # static value
        dummyDict[EmulationOspfLsaConfigConstants.OPAQUE_ENABLE_LINK_MAX_BW_CMD] = "dummyValue43" # static value
        dummyDict[EmulationOspfLsaConfigConstants.OPAQUE_ENABLE_LINK_MAX_RESV_BW_CMD] = "dummyValue44" # static value
        dummyDict[EmulationOspfLsaConfigConstants.OPAQUE_ENABLE_LINK_METRIC_CMD] = "dummyValue45" # static value
        dummyDict[EmulationOspfLsaConfigConstants.OPAQUE_ENABLE_LINK_REMOTE_IP_ADDR_CMD] = "dummyValue46" # static value
        dummyDict[EmulationOspfLsaConfigConstants.OPAQUE_ENABLE_LINK_RESOURCE_CLASS_CMD] = "dummyValue47" # static value
        dummyDict[EmulationOspfLsaConfigConstants.OPAQUE_ENABLE_LINK_TYPE_CMD] = "dummyValue48" # static value
        dummyDict[EmulationOspfLsaConfigConstants.OPAQUE_ENABLE_LINK_UNRESV_BW_CMD] = "dummyValue49" # static value
        dummyDict[EmulationOspfLsaConfigConstants.OPAQUE_LINK_ID_CMD] = "dummyValue50" # static value
        dummyDict[EmulationOspfLsaConfigConstants.OPAQUE_LINK_LOCAL_IP_ADDR_CMD] = "dummyValue51" # static value
        dummyDict[EmulationOspfLsaConfigConstants.OPAQUE_LINK_MAX_BW_CMD] = "dummyValue52" # static value
        dummyDict[EmulationOspfLsaConfigConstants.OPAQUE_LINK_MAX_RESV_BW_CMD] = "dummyValue53" # static value
        dummyDict[EmulationOspfLsaConfigConstants.OPAQUE_LINK_METRIC_CMD] = "dummyValue54" # static value
        dummyDict[EmulationOspfLsaConfigConstants.OPAQUE_LINK_OTHER_SUBTLVS_CMD] = "dummyValue55" # static value
        dummyDict[EmulationOspfLsaConfigConstants.OPAQUE_LINK_REMOTE_IP_ADDR_CMD] = "dummyValue56" # static value
        dummyDict[EmulationOspfLsaConfigConstants.OPAQUE_LINK_RESOURCE_CLASS_CMD] = "dummyValue57" # static value
        dummyDict[EmulationOspfLsaConfigConstants.OPAQUE_LINK_SUBTLVS_CMD] = "dummyValue58" # static value
        dummyDict[EmulationOspfLsaConfigConstants.OPAQUE_LINK_TYPE_CMD] = EmulationOspfLsaConfigConstants.OPAQUE_LINK_TYPE_DEAULT # constant value
        dummyDict[EmulationOspfLsaConfigConstants.OPAQUE_LINK_UNRESV_BW_PRIORITY_CMD] = "dummyValue60" # static value
        dummyDict[EmulationOspfLsaConfigConstants.OPAQUE_ROUTER_ADDR_CMD] = "dummyValue61" # static value
        dummyDict[EmulationOspfLsaConfigConstants.OPAQUE_TLV_TYPE_CMD] = EmulationOspfLsaConfigConstants.OPAQUE_TLV_TYPE_LINK # constant value
        dummyDict[EmulationOspfLsaConfigConstants.OPTIONS_CMD] = "dummyValue63" # static value
        dummyDict[EmulationOspfLsaConfigConstants.PREFIX_OPTIONS_CMD] = "dummyValue64" # static value
        dummyDict[EmulationOspfLsaConfigConstants.ROUTER_ABR_CMD] = "dummyValue65" # static value
        dummyDict[EmulationOspfLsaConfigConstants.ROUTER_ASBR_CMD] = "dummyValue66" # static value
        dummyDict[EmulationOspfLsaConfigConstants.ROUTER_LINK_DATA_CMD] = "dummyValue67" # static value
        dummyDict[EmulationOspfLsaConfigConstants.ROUTER_LINK_ID_CMD] = "dummyValue68" # static value
        dummyDict[EmulationOspfLsaConfigConstants.ROUTER_LINK_IDX_CMD] = "dummyValue69" # static value
        dummyDict[EmulationOspfLsaConfigConstants.ROUTER_LINK_METRIC_CMD] = "dummyValue70" # static value
        dummyDict[EmulationOspfLsaConfigConstants.ROUTER_LINK_MODE_CMD] = EmulationOspfLsaConfigConstants.ROUTER_LINK_MODE_CREATE # constant value
        dummyDict[EmulationOspfLsaConfigConstants.ROUTER_LINK_TYPE_CMD] = EmulationOspfLsaConfigConstants.ROUTER_LINK_TYPE_PTOP # constant value
        dummyDict[EmulationOspfLsaConfigConstants.ROUTER_VIRTUAL_LINK_ENDPT_CMD] = "dummyValue73" # static value
        dummyDict[EmulationOspfLsaConfigConstants.ROUTER_WILDCARD_CMD] = "dummyValue74" # static value
        dummyDict[EmulationOspfLsaConfigConstants.SESSION_TYPE_CMD] = EmulationOspfLsaConfigConstants.SESSION_TYPE_OSPFV2 # constant value
        dummyDict[EmulationOspfLsaConfigConstants.SUMMARY_NUMBER_OF_PREFIX_CMD] = "dummyValue76" # static value
        dummyDict[EmulationOspfLsaConfigConstants.SUMMARY_PREFIX_LENGTH_CMD] = "dummyValue77" # static value
        dummyDict[EmulationOspfLsaConfigConstants.SUMMARY_PREFIX_METRIC_CMD] = "dummyValue78" # static value
        dummyDict[EmulationOspfLsaConfigConstants.SUMMARY_PREFIX_START_CMD] = "dummyValue79" # static value
        dummyDict[EmulationOspfLsaConfigConstants.SUMMARY_PREFIX_STEP_CMD] = "dummyValue80" # static value
        dummyDict[EmulationOspfLsaConfigConstants.TE_ADMIN_GROUP_CMD] = "dummyValue81" # static value
        dummyDict[EmulationOspfLsaConfigConstants.TE_INSTANCE_ID_CMD] = "dummyValue82" # static value
        dummyDict[EmulationOspfLsaConfigConstants.TE_LINK_ID_CMD] = "dummyValue83" # static value
        dummyDict[EmulationOspfLsaConfigConstants.TE_LINK_TYPE_CMD] = "dummyValue84" # static value
        dummyDict[EmulationOspfLsaConfigConstants.TE_LOCAL_IP_CMD] = "dummyValue85" # static value
        dummyDict[EmulationOspfLsaConfigConstants.TE_MAX_BW_CMD] = "dummyValue86" # static value
        dummyDict[EmulationOspfLsaConfigConstants.TE_MAX_RESV_BW_CMD] = "dummyValue87" # static value
        dummyDict[EmulationOspfLsaConfigConstants.TE_MAX_RESV_PRIORITY0_CMD] = "dummyValue88" # static value
        dummyDict[EmulationOspfLsaConfigConstants.TE_MAX_RESV_PRIORITY1_CMD] = "dummyValue89" # static value
        dummyDict[EmulationOspfLsaConfigConstants.TE_MAX_RESV_PRIORITY2_CMD] = "dummyValue90" # static value
        dummyDict[EmulationOspfLsaConfigConstants.TE_MAX_RESV_PRIORITY3_CMD] = "dummyValue91" # static value
        dummyDict[EmulationOspfLsaConfigConstants.TE_MAX_RESV_PRIORITY4_CMD] = "dummyValue92" # static value
        dummyDict[EmulationOspfLsaConfigConstants.TE_MAX_RESV_PRIORITY5_CMD] = "dummyValue93" # static value
        dummyDict[EmulationOspfLsaConfigConstants.TE_MAX_RESV_PRIORITY6_CMD] = "dummyValue94" # static value
        dummyDict[EmulationOspfLsaConfigConstants.TE_MAX_RESV_PRIORITY7_CMD] = "dummyValue95" # static value
        dummyDict[EmulationOspfLsaConfigConstants.TE_METRIC_CMD] = "dummyValue96" # static value
        dummyDict[EmulationOspfLsaConfigConstants.TE_REMOTE_IP_CMD] = "dummyValue97" # static value
        dummyDict[EmulationOspfLsaConfigConstants.TE_ROUTER_ADDRESS_CMD] = "dummyValue98" # static value
        dummyDict[EmulationOspfLsaConfigConstants.TE_TLV_TYPE_CMD] = "dummyValue99" # static value
        dummyDict[EmulationOspfLsaConfigConstants.TYPE_CMD] = EmulationOspfLsaConfigConstants.TYPE_ASBR_SUMMARY # constant value

        api = device.getApi(EmulationOspfLsaConfigConstants.EMULATION_OSPF_LSA_CONFIG_API)
        assert isinstance(api, EmulationOspfLsaConfigApi)
        api.emulation_ospf_lsa_config(dummyDict)
    """
    def emulation_ospf_lsa_config(self, argdictionary, supported = None):
        self.process_supported_hltapi_commands(argdictionary, supported)
        return self.send_command_args(self._nameSpace +"::emulation_ospf_lsa_config", argdictionary)

    """
    Individual commands for each option. Typically, the "One Large Method"
    is the one that you want to be using so look at that example above
    """
    def emulation_ospf_lsa_config_adv_router_id(self, ip):
        """
        This is the method the command: emulation_ospf_lsa_config option adv_router_id
        Description:The router ID of the router that is originating the LSA.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            The router ID of the router that is originating the LSA.
            DEFAULT

            198.18.1.1
        Constants Available: ADV_ROUTER_ID_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.ADV_ROUTER_ID_CMD : ip})

    def emulation_ospf_lsa_config_area_id(self, ip):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_lsa_config_attached_router_id(self, ip):
        """
        This is the method the command: emulation_ospf_lsa_config option attached_router_id
        Description:A list of router IDs in the area, in IP address format separated by spaces.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            A list of router IDs in the area, in IP address format separated by spaces.
            DEFAULT

            14.0.0.1
        Constants Available: ATTACHED_ROUTER_ID_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.ATTACHED_ROUTER_ID_CMD : ip})

    def emulation_ospf_lsa_config_auto_ls_age(self, any):
        """
        This is the method the command: emulation_ospf_lsa_config option auto_ls_age
        Description:Not supported
            DEFAULT
                Not supported
        Constants Available: AUTO_LS_AGE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.AUTO_LS_AGE_CMD : any})

    def emulation_ospf_lsa_config_auto_ls_checksum(self, any):
        """
        This is the method the command: emulation_ospf_lsa_config option auto_ls_checksum
        Description:Not supported
            DEFAULT
                Not supported
        Constants Available: AUTO_LS_CHECKSUM_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.AUTO_LS_CHECKSUM_CMD : any})

    def emulation_ospf_lsa_config_auto_ls_seq(self, any):
        """
        This is the method the command: emulation_ospf_lsa_config option auto_ls_seq
        Description:Not supported
            DEFAULT
                Not supported
        Constants Available: AUTO_LS_SEQ_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.AUTO_LS_SEQ_CMD : any})

    def emulation_ospf_lsa_config_auto_update(self, any):
        """
        This is the method the command: emulation_ospf_lsa_config option auto_update
        Description:Not supported
            DEFAULT
                Not supported
        Constants Available: AUTO_UPDATE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.AUTO_UPDATE_CMD : any})

    def emulation_ospf_lsa_config_external_metric_ebit(self, opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_lsa_config_external_metric_fbit(self, opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_lsa_config_external_metric_tbit(self, opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_lsa_config_external_number_of_prefix(self, any):
        """
        This is the method the command: emulation_ospf_lsa_config option external_number_of_prefix
        Description:The number of External IP LSAs to generate.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            The number of External IP LSAs to generate.
            DEFAULT

            16
        Constants Available: EXTERNAL_NUMBER_OF_PREFIX_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.EXTERNAL_NUMBER_OF_PREFIX_CMD : any})

    def emulation_ospf_lsa_config_external_prefix_forward_addr(self, ip):
        """
        This is the method the command: emulation_ospf_lsa_config option external_prefix_forward_addr
        Description:If the external_metric_fbit is true, data traffic for the advertised
            destination will be forwarded to this fully qualified IPv6 address.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            If the external_metric_fbit is true, data traffic for the advertised
            destination will be forwarded to this fully qualified IPv6 address.
            DEFAULT
                None
        Constants Available: EXTERNAL_PREFIX_FORWARD_ADDR_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.EXTERNAL_PREFIX_FORWARD_ADDR_CMD : ip})

    def emulation_ospf_lsa_config_external_prefix_length(self, any):
        """
        This is the method the command: emulation_ospf_lsa_config option external_prefix_length
        Description:The number of high-order bits of prefixAddress that are significant.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            The number of high-order bits of prefixAddress that are significant.
            DEFAULT

            16
        Constants Available: EXTERNAL_PREFIX_LENGTH_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.EXTERNAL_PREFIX_LENGTH_CMD : any})

    def emulation_ospf_lsa_config_external_prefix_metric(self, range):
        """
        This is the method the command: emulation_ospf_lsa_config option external_prefix_metric
        Description:The cost of the route for all TOS levels.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            The cost of the route for all TOS levels.
            DEFAULT

            1
        Constants Available: EXTERNAL_PREFIX_METRIC_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.EXTERNAL_PREFIX_METRIC_CMD : range})

    def emulation_ospf_lsa_config_external_prefix_start(self, ip):
        """
        This is the method the command: emulation_ospf_lsa_config option external_prefix_start
        Description:This option is valid for OSPFv3 external route type. The prefix address
            to be advertised in the LSA. Although only prefixLength bits of the IPv6
            address are meaningful, a full IPv6 address should be specified.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            This option is valid for OSPFv3 external route type. The prefix address
            to be advertised in the LSA. Although only prefixLength bits of the IPv6
            address are meaningful, a full IPv6 address should be specified.
            DEFAULT
                None
        Constants Available: EXTERNAL_PREFIX_START_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.EXTERNAL_PREFIX_START_CMD : ip})

    def emulation_ospf_lsa_config_external_prefix_step(self, ip):
        """
        This is the method the command: emulation_ospf_lsa_config option external_prefix_step
        Description:If external_number_of_prefix is greater than 1,this is the value that
            will be added to the most significant external_prefix_length bits of
            external_prefix_start between generated LSAs. This is also the value to
            increment the link_state_id.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            If external_number_of_prefix is greater than 1,this is the value that
            will be added to the most significant external_prefix_length bits of
            external_prefix_start between generated LSAs. This is also the value to
            increment the link_state_id.
            DEFAULT

            0.0.0.1
        Constants Available: EXTERNAL_PREFIX_STEP_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.EXTERNAL_PREFIX_STEP_CMD : ip})

    def emulation_ospf_lsa_config_external_prefix_type(self, opt):
        """
        This is the method the command: emulation_ospf_lsa_config option external_prefix_type
        Description:The type of external metric. A value of 1 implies type 2 metric. A value
            of 0 implies type 1.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            The type of external metric. A value of 1 implies type 2 metric. A value
            of 0 implies type 1.
            Valid options are:
            1

            2

            DEFAULT

            1
        Constants Available: EXTERNAL_PREFIX_TYPE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.EXTERNAL_PREFIX_TYPE_CMD : opt})

    def emulation_ospf_lsa_config_external_route_tag(self, ip):
        """
        This is the method the command: emulation_ospf_lsa_config option external_route_tag
        Description:If the external_metric_tbit is true, an additional value to be used for
            external routes between AS boundary routers. This field is not used
            within OSPF.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            If the external_metric_tbit is true, an additional value to be used for
            external routes between AS boundary routers. This field is not used
            within OSPF.
            DEFAULT

            17.0.0.1
        Constants Available: EXTERNAL_ROUTE_TAG_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.EXTERNAL_ROUTE_TAG_CMD : ip})

    def emulation_ospf_lsa_config_handle(self, any):
        """
        This is the method the command: emulation_ospf_lsa_config option handle
        Description:This option represents the handle the user *must* pass to the
            'emulation_ospf_lsa_config' procedure. This option specifies on which
            OSPF router to configure the OSPF User LSA. The OSPF router handle(s)
            are returned by the procedure 'emulation_ospf_config' when configuring
            OSPF routers on the Ixia interface.
            DEFAULT
                None
            IxNetwork-NGPF[M]

            DESCRIPTION

            This option represents the handle the user *must* pass to the
            'emulation_ospf_lsa_config' procedure. This option specifies on which
            OSPF router to configure the OSPF User LSA. The OSPF router handle(s)
            are returned by the procedure 'emulation_ospf_config' when configuring
            OSPF routers on the Ixia interface.
            DEFAULT
                None
        Constants Available: HANDLE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.HANDLE_CMD : any})

    def emulation_ospf_lsa_config_link_state_id(self, ip):
        """
        This is the method the command: emulation_ospf_lsa_config option link_state_id
        Description:The router ID of the originating router. This field uniquely identified
            the LSA in the link-state database.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            The router ID of the originating router. This field uniquely identified
            the LSA in the link-state database.
            DEFAULT

            199.18.1.1
        Constants Available: LINK_STATE_ID_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.LINK_STATE_ID_CMD : ip})

    def emulation_ospf_lsa_config_link_state_id_step(self, ipv4):
        """
        This is the method the command: emulation_ospf_lsa_config option link_state_id_step
        Description:If summary_number_of_prefix is greater than 1, the value to increment
            the link_state_id by for each LSA. The value is expressed in IPv4 format.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            If summary_number_of_prefix is greater than 1, the value to increment
            the link_state_id by for each LSA. The value is expressed in IPv4 format.
            DEFAULT
                None
        Constants Available: LINK_STATE_ID_STEP_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        ipv4 --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.LINK_STATE_ID_STEP_CMD : ipv4})

    def emulation_ospf_lsa_config_ls_age(self, any):
        """
        This is the method the command: emulation_ospf_lsa_config option ls_age
        Description:Not supported
            DEFAULT
                Not supported
        Constants Available: LS_AGE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.LS_AGE_CMD : any})

    def emulation_ospf_lsa_config_ls_checksum(self, any):
        """
        This is the method the command: emulation_ospf_lsa_config option ls_checksum
        Description:Not supported
            DEFAULT
                Not supported
        Constants Available: LS_CHECKSUM_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.LS_CHECKSUM_CMD : any})

    def emulation_ospf_lsa_config_ls_seq(self, any):
        """
        This is the method the command: emulation_ospf_lsa_config option ls_seq
        Description:Not supported
            DEFAULT
                Not supported
        Constants Available: LS_SEQ_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.LS_SEQ_CMD : any})

    def emulation_ospf_lsa_config_ls_type_function_code(self, range):
        """
        This is the method the command: emulation_ospf_lsa_config option ls_type_function_code
        Description:Not defined
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            Not defined
            DEFAULT

            0
        Constants Available: LS_TYPE_FUNCTION_CODE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.LS_TYPE_FUNCTION_CODE_CMD : range})

    def emulation_ospf_lsa_config_ls_type_s_bits(self, any):
        """
        This is the method the command: emulation_ospf_lsa_config option ls_type_s_bits
        Description:Not supported
            DEFAULT
                Not supported
        Constants Available: LS_TYPE_S_BITS_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.LS_TYPE_S_BITS_CMD : any})

    def emulation_ospf_lsa_config_ls_type_u_bit(self, any):
        """
        This is the method the command: emulation_ospf_lsa_config option ls_type_u_bit
        Description:Not supported
            DEFAULT
                Not supported
        Constants Available: LS_TYPE_U_BIT_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.LS_TYPE_U_BIT_CMD : any})

    def emulation_ospf_lsa_config_lsa_group_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_lsa_config_lsa_handle(self, any):
        """
        This is the method the command: emulation_ospf_lsa_config option lsa_handle
        Description:This option specifies on which OSPF User LSA to configure. This option
            *must* be passed if the -mode option is modify or delete. The OSPF LSA
            handle(s) are returned by the procedure 'emulation_ospf_lsa_config' when
            creating OSPF user LSA(s) on the Ixia interface.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            This option specifies on which OSPF User LSA to configure. This option
            *must* be passed if the -mode option is modify or delete. The OSPF LSA
            handle(s) are returned by the procedure 'emulation_ospf_lsa_config' when
            creating OSPF user LSA(s) on the Ixia interface.
            DEFAULT
                None
        Constants Available: LSA_HANDLE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.LSA_HANDLE_CMD : any})

    def emulation_ospf_lsa_config_mode(self, opt):
        """
        This is the method the command: emulation_ospf_lsa_config option mode
        Description:Mode of the procedure call. Valid options are:createmodifydelete
            DEFAULT
                None
            IxNetwork-NGPF[M]

            DESCRIPTION

            Mode of the procedure call. Valid options are: create modify delete
            Valid options are:
            create

            modify

            delete

            reset

            DEFAULT

            create
        Constants Available: MODE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.MODE_CMD : opt})

    def emulation_ospf_lsa_config_net_attached_router(self, opt):
        """
        This is the method the command: emulation_ospf_lsa_config option net_attached_router
        Description:The option specifies the mode in configuring router IDs in the area.
            Note that delete and reset does not work. Valid options
            are:createdeletereset
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            The option specifies the mode in configuring router IDs in the area.
            Note that delete and reset does not work. Valid options are: create
            delete reset
            Valid options are:
            create

            delete

            reset

            DEFAULT

            create
        Constants Available: NET_ATTACHED_ROUTER_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.NET_ATTACHED_ROUTER_CMD : opt})

    def emulation_ospf_lsa_config_net_prefix_length(self, any):
        """
        This is the method the command: emulation_ospf_lsa_config option net_prefix_length
        Description:The length in bits of the IP address mask for the network.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            The length in bits of the IP address mask for the network.
            DEFAULT

            16
        Constants Available: NET_PREFIX_LENGTH_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.NET_PREFIX_LENGTH_CMD : any})

    def emulation_ospf_lsa_config_no_write(self, flag):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_lsa_config_nssa_number_of_prefix(self, any):
        """
        This is the method the command: emulation_ospf_lsa_config option nssa_number_of_prefix
        Description:Not supported
            DEFAULT
                Not supported
        Constants Available: NSSA_NUMBER_OF_PREFIX_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.NSSA_NUMBER_OF_PREFIX_CMD : any})

    def emulation_ospf_lsa_config_nssa_prefix_forward_addr(self, any):
        """
        This is the method the command: emulation_ospf_lsa_config option nssa_prefix_forward_addr
        Description:Not supported
            DEFAULT
                Not supported
        Constants Available: NSSA_PREFIX_FORWARD_ADDR_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.NSSA_PREFIX_FORWARD_ADDR_CMD : any})

    def emulation_ospf_lsa_config_nssa_prefix_length(self, any):
        """
        This is the method the command: emulation_ospf_lsa_config option nssa_prefix_length
        Description:Not supported
            DEFAULT
                Not supported
        Constants Available: NSSA_PREFIX_LENGTH_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.NSSA_PREFIX_LENGTH_CMD : any})

    def emulation_ospf_lsa_config_nssa_prefix_metric(self, any):
        """
        This is the method the command: emulation_ospf_lsa_config option nssa_prefix_metric
        Description:Not supported
            DEFAULT
                Not supported
        Constants Available: NSSA_PREFIX_METRIC_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.NSSA_PREFIX_METRIC_CMD : any})

    def emulation_ospf_lsa_config_nssa_prefix_start(self, any):
        """
        This is the method the command: emulation_ospf_lsa_config option nssa_prefix_start
        Description:Not supported
            DEFAULT
                Not supported
        Constants Available: NSSA_PREFIX_START_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.NSSA_PREFIX_START_CMD : any})

    def emulation_ospf_lsa_config_nssa_prefix_step(self, any):
        """
        This is the method the command: emulation_ospf_lsa_config option nssa_prefix_step
        Description:Not supported
            DEFAULT
                Not supported
        Constants Available: NSSA_PREFIX_STEP_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.NSSA_PREFIX_STEP_CMD : any})

    def emulation_ospf_lsa_config_nssa_prefix_type(self, any):
        """
        This is the method the command: emulation_ospf_lsa_config option nssa_prefix_type
        Description:Not supported
            DEFAULT
                Not supported
        Constants Available: NSSA_PREFIX_TYPE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.NSSA_PREFIX_TYPE_CMD : any})

    def emulation_ospf_lsa_config_opaque_enable_link_id(self, bool_opt):
        """
        This is the method the command: emulation_ospf_lsa_config option opaque_enable_link_id
        Description:This will enable usage of link id. TLV Type 2. If checked, this will be
            the 4-octet IP address which identifies the other end of the link. For
            Point to Point, the Neighbor's Router ID. For Multi-access, the
            interface of the DR.This option is valid only when -type is opaque and
            -opaque_tlv_type is link. This option is valid only for IxTclNetwork API.
            DEFAULT

            0
            IxNetwork-NGPF

            DESCRIPTION

            This will enable usage of link id. TLV Type 2. If checked, this will be
            the 4-octet IP address which identifies the other end of the link. For
            Point to Point, the Neighbor's Router ID. For Multi-access, the
            interface of the DR. This option is valid only when type is opaque and
            opaque_tlv_type is link. This option is valid only for IxTclNetwork API.
            DEFAULT

            0
        Constants Available: OPAQUE_ENABLE_LINK_ID_CMD
        Supported:IxNetwork
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.OPAQUE_ENABLE_LINK_ID_CMD : bool_opt})

    def emulation_ospf_lsa_config_opaque_enable_link_local_ip_addr(self, bool_opt):
        """
        This is the method the command: emulation_ospf_lsa_config option opaque_enable_link_local_ip_addr
        Description:This will enable the usage of local IP address. TLV Type 3. The IP
            address of the local interface for this link. Each address is a 4-octet
            value. The total length is N times 4 octets, where N is the number of
            addresses. This option is valid only when -type is opaque and
            -opaque_tlv_type is link. This option is valid only for IxTclNetwork API.
            DEFAULT

            0
            IxNetwork-NGPF

            DESCRIPTION

            This will enable the usage of local IP address. TLV Type 3. The IP
            address of the local interface for this link. Each address is a 4-octet
            value. The total length is N times 4 octets, where N is the number of
            addresses. This option is valid only when type is opaque and
            opaque_tlv_type is link. This option is valid only for IxTclNetwork API.
            DEFAULT

            0
        Constants Available: OPAQUE_ENABLE_LINK_LOCAL_IP_ADDR_CMD
        Supported:IxNetwork
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.OPAQUE_ENABLE_LINK_LOCAL_IP_ADDR_CMD : bool_opt})

    def emulation_ospf_lsa_config_opaque_enable_link_max_bw(self, bool_opt):
        """
        This is the method the command: emulation_ospf_lsa_config option opaque_enable_link_max_bw
        Description:This will enable the usage of max bandwidth. TLV Type 6. Units are in
            bytes per second. The maximum bandwidth that can be used on this link in
            this direction (from originator to the neighbor). Four octets in length,
            expressed in IEEE floating point format. This option is valid only when
            -type is opaque and -opaque_tlv_type is link. This option is valid only
            for IxTclNetwork API.
            DEFAULT

            0
            IxNetwork-NGPF

            DESCRIPTION

            This will enable the usage of max bandwidth. TLV Type 6. Units are in
            bytes per second. The maximum bandwidth that can be used on this link in
            this direction (from originator to the neighbor). Four octets in length,
            expressed in IEEE floating point format. This option is valid only when
            type is opaque and opaque_tlv_type is link. This option is valid only
            for IxTclNetwork API.
            DEFAULT

            0
        Constants Available: OPAQUE_ENABLE_LINK_MAX_BW_CMD
        Supported:IxNetwork
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.OPAQUE_ENABLE_LINK_MAX_BW_CMD : bool_opt})

    def emulation_ospf_lsa_config_opaque_enable_link_max_resv_bw(self, bool_opt):
        """
        This is the method the command: emulation_ospf_lsa_config option opaque_enable_link_max_resv_bw
        Description:This will enable the usage of max reservable bandwidth. TLV Type 7.
            Units in bytes per second. The maximum bandwidth that can be reserved on
            this link in this direction (from originator to the neighbor). Four
            octets in length, expressed in IEEE floating point format. This may be
            greater than the maximum bandwidth. This option is valid only when -type
            is opaque and -opaque_tlv_type is link. This option is valid only for
            IxTclNetwork API.
            DEFAULT

            0
            IxNetwork-NGPF

            DESCRIPTION

            This will enable the usage of max reservable bandwidth. TLV Type 7.
            Units in bytes per second. The maximum bandwidth that can be reserved on
            this link in this direction (from originator to the neighbor). Four
            octets in length, expressed in IEEE floating point format. This may be
            greater than the maximum bandwidth. This option is valid only when type
            is opaque and opaque_tlv_type is link. This option is valid only for
            IxTclNetwork API.
            DEFAULT

            0
        Constants Available: OPAQUE_ENABLE_LINK_MAX_RESV_BW_CMD
        Supported:IxNetwork
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.OPAQUE_ENABLE_LINK_MAX_RESV_BW_CMD : bool_opt})

    def emulation_ospf_lsa_config_opaque_enable_link_metric(self, bool_opt):
        """
        This is the method the command: emulation_ospf_lsa_config option opaque_enable_link_metric
        Description:This will enable the usage of link metric. TLV Type 5. The Traffic
            Engineering Metric. This option is valid only when -type is opaque and
            -opaque_tlv_type is link. This option is valid only for IxTclNetwork API.
            DEFAULT

            0
            IxNetwork-NGPF

            DESCRIPTION

            This will enable the usage of link metric. TLV Type 5. The Traffic
            Engineering Metric. This option is valid only when type is opaque and
            opaque_tlv_type is link. This option is valid only for IxTclNetwork API.
            DEFAULT

            0
        Constants Available: OPAQUE_ENABLE_LINK_METRIC_CMD
        Supported:IxNetwork
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.OPAQUE_ENABLE_LINK_METRIC_CMD : bool_opt})

    def emulation_ospf_lsa_config_opaque_enable_link_remote_ip_addr(self, bool_opt):
        """
        This is the method the command: emulation_ospf_lsa_config option opaque_enable_link_remote_ip_addr
        Description:This will enable the usage of the remote IP address. TLV Type 4. The IP
            address of the neighbor's interface for this link. The total length is N
            times four octets, where N is the number of addresses. This option is
            valid only when -type is opaque and -opaque_tlv_type is link. This
            option is valid only for IxTclNetwork API.
            DEFAULT

            0
            IxNetwork-NGPF

            DESCRIPTION

            This will enable the usage of the remote IP address. TLV Type 4. The IP
            address of the neighbor's interface for this link. The total length is N
            times four octets, where N is the number of addresses. This option is
            valid only when type is opaque and opaque_tlv_type is link. This option
            is valid only for IxTclNetwork API.
            DEFAULT

            0
        Constants Available: OPAQUE_ENABLE_LINK_REMOTE_IP_ADDR_CMD
        Supported:IxNetwork
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.OPAQUE_ENABLE_LINK_REMOTE_IP_ADDR_CMD : bool_opt})

    def emulation_ospf_lsa_config_opaque_enable_link_resource_class(self, bool_opt):
        """
        This is the method the command: emulation_ospf_lsa_config option opaque_enable_link_resource_class
        Description:This will enable the usage of link resource class. TLV Type 9. A bit
            mask value, four octets in length, which specifies administrative group
            membership for this link. This option is valid only when -type is opaque
            and -opaque_tlv_type is link. This option is valid only for IxTclNetwork
            API.
            DEFAULT

            0
            IxNetwork-NGPF

            DESCRIPTION

            This will enable the usage of link resource class. TLV Type 9. A bit
            mask value, four octets in length, which specifies administrative group
            membership for this link. This option is valid only when type is opaque
            and opaque_tlv_type is link. This option is valid only for IxTclNetwork API.
            DEFAULT

            0
        Constants Available: OPAQUE_ENABLE_LINK_RESOURCE_CLASS_CMD
        Supported:IxNetwork
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.OPAQUE_ENABLE_LINK_RESOURCE_CLASS_CMD : bool_opt})

    def emulation_ospf_lsa_config_opaque_enable_link_type(self, bool_opt):
        """
        This is the method the command: emulation_ospf_lsa_config option opaque_enable_link_type
        Description:This will enable the usage of link type. TLV Type 1. Defines the type of
            link and is one octet in length. This option is valid only when -type is
            opaque and -opaque_tlv_type is link. This option is valid only for
            IxTclNetwork API.
            DEFAULT

            0
            IxNetwork-NGPF

            DESCRIPTION

            This will enable the usage of link type. TLV Type 1. Defines the type of
            link and is one octet in length. This option is valid only when type is
            opaque and opaque_tlv_type is link. This option is valid only for
            IxTclNetwork API.
            DEFAULT

            0
        Constants Available: OPAQUE_ENABLE_LINK_TYPE_CMD
        Supported:IxNetwork
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.OPAQUE_ENABLE_LINK_TYPE_CMD : bool_opt})

    def emulation_ospf_lsa_config_opaque_enable_link_unresv_bw(self, bool_opt):
        """
        This is the method the command: emulation_ospf_lsa_config option opaque_enable_link_unresv_bw
        Description:This will enable the usage of the unreserved bandwidth. TLV Type 8. The
            amount of bandwidth not yet reserved at each of the eight priority
            levels. This value will be less than or equal to the maximum reservable
            bandwidth. 32 octets in length, expressed in IEEE floating point format.
            If checked, unreserved bandwidth may be assigned to each of the 8
            priority levels (0 through 7). This option is valid only when -type is
            opaque and -opaque_tlv_type is link. This option is valid only for
            IxTclNetwork API.
            DEFAULT

            0
            IxNetwork-NGPF

            DESCRIPTION

            This will enable the usage of the unreserved bandwidth. TLV Type 8. The
            amount of bandwidth not yet reserved at each of the eight priority
            levels. This value will be less than or equal to the maximum reservable
            bandwidth. 32 octets in length, expressed in IEEE floating point format.
            If checked, unreserved bandwidth may be assigned to each of the 8
            priority levels (0 through 7). This option is valid only when type is
            opaque and opaque_tlv_type is link. This option is valid only for
            IxTclNetwork API.
            DEFAULT

            0
        Constants Available: OPAQUE_ENABLE_LINK_UNRESV_BW_CMD
        Supported:IxNetwork
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.OPAQUE_ENABLE_LINK_UNRESV_BW_CMD : bool_opt})

    def emulation_ospf_lsa_config_opaque_link_id(self, ip):
        """
        This is the method the command: emulation_ospf_lsa_config option opaque_link_id
        Description:TLV Type 2. If checked, this will be the 4-octet IP address which
            identifies the other end of the link. For Point to Point, the Neighbor's
            Router ID. For Multiaccess, the interface of the DR. This option is
            valid only when -type is opaque and -opaque_tlv_type is link. This
            option is valid only for IxTclNetwork API.
            DEFAULT

            0.0.0.0
            IxNetwork-NGPF

            DESCRIPTION

            TLV Type 2. If checked, this will be the 4-octet IP address which
            identifies the other end of the link. For Point to Point, the Neighbor's
            Router ID. For Multiaccess, the interface of the DR. This option is
            valid only when type is opaque and opaque_tlv_type is link. This option
            is valid only for IxTclNetwork API.
            DEFAULT

            0.0.0.0
        Constants Available: OPAQUE_LINK_ID_CMD
        Supported:IxNetwork
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.OPAQUE_LINK_ID_CMD : ip})

    def emulation_ospf_lsa_config_opaque_link_local_ip_addr(self, ip):
        """
        This is the method the command: emulation_ospf_lsa_config option opaque_link_local_ip_addr
        Description:TLV Type 3. The IP address of the local interface for this link. Each
            address is a 4-octet value. The total length is N times 4 octets, where
            N is the number of addresses. This option is valid only when -type is
            opaque and -opaque_tlv_type is link. This option is valid only for
            IxTclNetwork API.
            DEFAULT

            0.0.0.0
            IxNetwork-NGPF

            DESCRIPTION

            TLV Type 3. The IP address of the local interface for this link. Each
            address is a 4-octet value. The total length is N times 4 octets, where
            N is the number of addresses. This option is valid only when type is
            opaque and opaque_tlv_type is link. This option is valid only for
            IxTclNetwork API.
            DEFAULT

            0.0.0.0
        Constants Available: OPAQUE_LINK_LOCAL_IP_ADDR_CMD
        Supported:IxNetwork
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.OPAQUE_LINK_LOCAL_IP_ADDR_CMD : ip})

    def emulation_ospf_lsa_config_opaque_link_max_bw(self, any):
        """
        This is the method the command: emulation_ospf_lsa_config option opaque_link_max_bw
        Description:TLV Type 6. Units are in bytes per second. The maximum bandwidth that
            can be used on this link in this direction (from originator to the
            neighbor). Four octets in length, expressed in IEEE floating point
            format. This option is valid only when -type is opaque and
            -opaque_tlv_type is link. This option is valid only for IxTclNetwork API.
            DEFAULT

            0
            IxNetwork-NGPF

            DESCRIPTION

            TLV Type 6. Units are in bytes per second. The maximum bandwidth that
            can be used on this link in this direction (from originator to the
            neighbor). Four octets in length, expressed in IEEE floating point
            format. This option is valid only when type is opaque and
            opaque_tlv_type is link. This option is valid only for IxTclNetwork API.
            DEFAULT

            0
        Constants Available: OPAQUE_LINK_MAX_BW_CMD
        Supported:IxNetwork
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.OPAQUE_LINK_MAX_BW_CMD : any})

    def emulation_ospf_lsa_config_opaque_link_max_resv_bw(self, any):
        """
        This is the method the command: emulation_ospf_lsa_config option opaque_link_max_resv_bw
        Description:TLV Type 7. Units in bytes per second. The maximum bandwidth that can be
            reserved on this link in this direction (from originator to the
            neighbor). Four octets in length, expressed in IEEE floating point
            format. This may be greater than the maximum bandwidth. This option is
            valid only when -type is opaque and -opaque_tlv_type is link. This
            option is valid only for IxTclNetwork API.
            DEFAULT

            0
            IxNetwork-NGPF

            DESCRIPTION

            TLV Type 7. Units in bytes per second. The maximum bandwidth that can be
            reserved on this link in this direction (from originator to the
            neighbor). Four octets in length, expressed in IEEE floating point
            format. This may be greater than the maximum bandwidth. This option is
            valid only when type is opaque and opaque_tlv_type is link. This option
            is valid only for IxTclNetwork API.
            DEFAULT

            0
        Constants Available: OPAQUE_LINK_MAX_RESV_BW_CMD
        Supported:IxNetwork
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.OPAQUE_LINK_MAX_RESV_BW_CMD : any})

    def emulation_ospf_lsa_config_opaque_link_metric(self, numeric):
        """
        This is the method the command: emulation_ospf_lsa_config option opaque_link_metric
        Description:TLV Type 5. The Traffic Engineering Metric. Four octets in length. This
            option is valid only when -type is opaque and -opaque_tlv_type is link.
            This option is valid only for IxTclNetwork API.
            DEFAULT

            0
            IxNetwork-NGPF

            DESCRIPTION

            TLV Type 5. The Traffic Engineering Metric. Four octets in length. This
            option is valid only when type is opaque and opaque_tlv_type is link.
            This option is valid only for IxTclNetwork API.
            DEFAULT

            0
        Constants Available: OPAQUE_LINK_METRIC_CMD
        Supported:IxNetwork
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.OPAQUE_LINK_METRIC_CMD : numeric})

    def emulation_ospf_lsa_config_opaque_link_other_subtlvs(self, any):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_lsa_config_opaque_link_remote_ip_addr(self, ip):
        """
        This is the method the command: emulation_ospf_lsa_config option opaque_link_remote_ip_addr
        Description:TLV Type 4. The IP address of the neighbor's interface for this link.
            The total length is N times four octets, where N is the number of
            addresses. This option is valid only when -type is opaque and
            -opaque_tlv_type is link. This option is valid only for IxTclNetwork API.
            DEFAULT

            0.0.0.0
            IxNetwork-NGPF

            DESCRIPTION

            TLV Type 4. The IP address of the neighbor's interface for this link.
            The total length is N times four octets, where N is the number of
            addresses. This option is valid only when type is opaque and
            opaque_tlv_type is link. This option is valid only for IxTclNetwork API.
            DEFAULT

            0.0.0.0
        Constants Available: OPAQUE_LINK_REMOTE_IP_ADDR_CMD
        Supported:IxNetwork
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.OPAQUE_LINK_REMOTE_IP_ADDR_CMD : ip})

    def emulation_ospf_lsa_config_opaque_link_resource_class(self, hexhex):
        """
        This is the method the command: emulation_ospf_lsa_config option opaque_link_resource_class
        Description:TLV Type 9. A bit mask value, four octets in length, which specifies
            administrative group membership for this link. This option is valid only
            when -type is opaque and -opaque_tlv_type is link. This option is valid
            only for IxTclNetwork API.
            DEFAULT

            0x00000000
            IxNetwork-NGPF

            DESCRIPTION

            TLV Type 9. A bit mask value, four octets in length, which specifies
            administrative group membership for this link. This option is valid only
            when type is opaque and opaque_tlv_type is link. This option is valid
            only for IxTclNetwork API.
            DEFAULT

            0x00000000
        Constants Available: OPAQUE_LINK_RESOURCE_CLASS_CMD
        Supported:IxNetwork
        Keyword arguments:
        hexhex --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.OPAQUE_LINK_RESOURCE_CLASS_CMD : hexhex})

    def emulation_ospf_lsa_config_opaque_link_subtlvs(self, ip):
        """
        This is the method the command: emulation_ospf_lsa_config option opaque_link_subtlvs
        Description:Allows the user to create custom type 10 Sub-TLVs with length 4 - for
            Traffic Engineering. When both -opaque_link_subtlvs and
            -opaque_link_other_subtlvs are provided then -opaque_link_subtlvs has a
            greater priority. This option is valid only when -type is opaque and
            -opaque_tlv_type is link. This option is valid only for IxTclNetwork API.
            DEFAULT

            0.0.0.0
            IxNetwork-NGPF

            DESCRIPTION

            Allows the user to create custom type 10 Sub-TLVs with length 4 - for
            Traffic Engineering. When both -opaque_link_subtlvs and
            -opaque_link_other_subtlvs are provided then -opaque_link_subtlvs has a
            greater priority. This option is valid only when type is opaque and
            opaque_tlv_type is link. This option is valid only for IxTclNetwork API.
            DEFAULT

            0.0.0.0
        Constants Available: OPAQUE_LINK_SUBTLVS_CMD
        Supported:IxNetwork
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.OPAQUE_LINK_SUBTLVS_CMD : ip})

    def emulation_ospf_lsa_config_opaque_link_type(self, opt):
        """
        This is the method the command: emulation_ospf_lsa_config option opaque_link_type
        Description:TLV Type 1. Defines the type of link and is one octet in length. This
            option is valid only when -type is opaque and -opaque_tlv_type is link.
            This option is valid only for IxTclNetwork API.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            TLV Type 1. Defines the type of link and is one octet in length. This
            option is valid only when type is opaque and opaque_tlv_type is link.
            This option is valid only for IxTclNetwork API.
            Valid options are:
            ptop

            multiaccess

            DEFAULT

            ptop
        Constants Available: OPAQUE_LINK_TYPE_CMD
        Supported:IxNetwork
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.OPAQUE_LINK_TYPE_CMD : opt})

    def emulation_ospf_lsa_config_opaque_link_unresv_bw_priority(self, any):
        """
        This is the method the command: emulation_ospf_lsa_config option opaque_link_unresv_bw_priority
        Description:Unreserved Bandwidth in bytes per second per priority level. This option
            is valid only when -type is opaque and -opaque_tlv_type is link. This
            option is valid only for IxTclNetwork API.
            DEFAULT

            0
            IxNetwork-NGPF

            DESCRIPTION

            Unreserved Bandwidth in bytes per second per priority level. This option
            is valid only when type is opaque and opaque_tlv_type is link. This
            option is valid only for IxTclNetwork API.
            DEFAULT

            0
        Constants Available: OPAQUE_LINK_UNRESV_BW_PRIORITY_CMD
        Supported:IxNetwork
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.OPAQUE_LINK_UNRESV_BW_PRIORITY_CMD : any})

    def emulation_ospf_lsa_config_opaque_router_addr(self, ip):
        """
        This is the method the command: emulation_ospf_lsa_config option opaque_router_addr
        Description:TLVs are Type/Length/Value field combinations that make up part of the
            LSA payload and enable OSPF Traffic Engineering (OSPF-TE). If
            -opaque_tlv_type is router, the field is for the four-octet IP address
            of the advertising router. This option is valid only when -type is
            opaque and -opaque_tlv_type is router. This option is valid only for
            IxTclNetwork API.
            DEFAULT

            0.0.0.0
            IxNetwork-NGPF

            DESCRIPTION

            TLVs are Type/Length/Value field combinations that make up part of the
            LSA payload and enable OSPF Traffic Engineering (OSPF-TE). If
            opaque_tlv_type is router, the field is for the four-octet IP address of
            the advertising router. This option is valid only when type is opaque
            and opaque_tlv_type is router. This option is valid only for
            IxTclNetwork API.
            DEFAULT

            0.0.0.0
        Constants Available: OPAQUE_ROUTER_ADDR_CMD
        Supported:IxNetwork
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.OPAQUE_ROUTER_ADDR_CMD : ip})

    def emulation_ospf_lsa_config_opaque_tlv_type(self, opt):
        """
        This is the method the command: emulation_ospf_lsa_config option opaque_tlv_type
        Description:TLVs are Type/Length/Value field combinations that make up part of the
            LSA payload and enable OSPF Traffic Engineering (OSPF-TE). If
            -opaque_tlv_type is router, the field is for the four-octet IP address
            of the advertising router. Otherwise, if opaque_tlv_type is link, all
            the other TLVs from 1-9 can be enabled and used. This option is valid
            only when -type is opaque. This option is valid only for IxTclNetwork API.
            DEFAULT

            router
            IxNetwork-NGPF

            DESCRIPTION

            TLVs are Type/Length/Value field combinations that make up part of the
            LSA payload and enable OSPF Traffic Engineering (OSPF-TE). If
            opaque_tlv_type is router, the field is for the four-octet IP address of
            the advertising router. Otherwise, if opaque_tlv_type is link, all the
            other TLVs from 1-9 can be enabled and used. This option is valid only
            when type is opaque. This option is valid only for IxTclNetwork API.
            Valid options are:
            link

            router

            DEFAULT

            router
        Constants Available: OPAQUE_TLV_TYPE_CMD
        Supported:IxNetwork
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.OPAQUE_TLV_TYPE_CMD : opt})

    def emulation_ospf_lsa_config_options(self, range):
        """
        This is the method the command: emulation_ospf_lsa_config option options
        Description:The optional capabilities supported by the OSPFv2 router. For OSPFv3,
            use OSPFv3 specific options. Multiple options may be combined using a
            logical 'or'.
            Valid options are:
            ospfOptionBitTypeOfService

            0x01
            ospfOptionBitExternalRouting

            0x02
            ospfOptionBitMulticast

            0x04
            ospfOptionBitNSSACapability

            0x08
            ospfOptionBitExternalAttributes

            0x10
            ospfOptionBitDemandCircuit

            0x20
            ospfOptionBitLSANoForward

            0x40
            ospfOptionBitUnused

            0x80
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            The optional capabilities supported by the OSPFv2 router. For OSPFv3,
            use OSPFv3 specific options. Multiple options may be combined using a
            logical 'or'. Valid choices are: ospfOptionBitTypeOfService - 0x01
            ospfOptionBitExternalRouting - 0x02 ospfOptionBitMulticast - 0x04
            ospfOptionBitNSSACapability - 0x08 ospfOptionBitExternalAttributes -
            0x10 ospfOptionBitDemandCircuit - 0x20 ospfOptionBitLSANoForward - 0x40
            ospfOptionBitUnused - 0x80
            DEFAULT
                None
        Constants Available: OPTIONS_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.OPTIONS_CMD : range})

    def emulation_ospf_lsa_config_prefix_options(self, any):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_lsa_config_router_abr(self, bool_opt):
        """
        This is the method the command: emulation_ospf_lsa_config option router_abr
        Description:Set router to be an area boundary router (ABR). Correspond to E
            (external) bit in router LSA.
            DEFAULT

            0
            IxNetwork-NGPF

            DESCRIPTION

            Set router to be an area boundary router (ABR). Correspond to E
            (external) bit in router LSA.
            DEFAULT

            0
        Constants Available: ROUTER_ABR_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.ROUTER_ABR_CMD : bool_opt})

    def emulation_ospf_lsa_config_router_asbr(self, bool_opt):
        """
        This is the method the command: emulation_ospf_lsa_config option router_asbr
        Description:Set router to be an AS boundary router (ASBR). Correspond to B (border)
            bit in router LSA.
            DEFAULT

            0
            IxNetwork-NGPF

            DESCRIPTION

            Set router to be an AS boundary router (ASBR). Correspond to B (border)
            bit in router LSA.
            DEFAULT

            0
        Constants Available: ROUTER_ASBR_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.ROUTER_ASBR_CMD : bool_opt})

    def emulation_ospf_lsa_config_router_link_data(self, ip):
        """
        This is the method the command: emulation_ospf_lsa_config option router_link_data
        Description:The meaning of this option depends on the router_link_type option.
            Valid options are:
            ptop

            The interface's MIB-II.
            transit

            The router interface's IP address.
            stub

            The network's IP address mask.
            virtual

            The router interface's IP address.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            The meaning of this option depends on the router_link_type option. Valid
            choices are: ptop - The interfaces MIB-II. transit - The router
            interfaces IP address. stub - The networks IP address mask. virtual -
            The router interfaces IP address.
            DEFAULT

            13.0.0.1
        Constants Available: ROUTER_LINK_DATA_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.ROUTER_LINK_DATA_CMD : ip})

    def emulation_ospf_lsa_config_router_link_id(self, ip):
        """
        This is the method the command: emulation_ospf_lsa_config option router_link_id
        Description:Identifies the object that this router link connects to, depending on
            Valid options are:
            ptop

            The neighboring router's router ID.
            transit

            The IP address of the Designated Router.
            stub

            The IP network/subnet number.
            virtual

            The neighboring router's router ID.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            Identifies the object that this router link connects to, depending on
            the router_link_type option. Valid choices are: ptop - The neighboring
            routers router ID. transit - The IP address of the Designated Router.
            stub - The IP network/subnet number. virtual - The neighboring routers
            router ID.
            DEFAULT

            12.0.0.1
        Constants Available: ROUTER_LINK_ID_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.ROUTER_LINK_ID_CMD : ip})

    def emulation_ospf_lsa_config_router_link_idx(self, any):
        """
        This is the method the command: emulation_ospf_lsa_config option router_link_idx
        Description:Not supported
            DEFAULT
                Not supported
        Constants Available: ROUTER_LINK_IDX_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.ROUTER_LINK_IDX_CMD : any})

    def emulation_ospf_lsa_config_router_link_metric(self, range):
        """
        This is the method the command: emulation_ospf_lsa_config option router_link_metric
        Description:The cost of using the router link, applied to all TOS values.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            The cost of using the router link, applied to all TOS values.
            DEFAULT

            1
        Constants Available: ROUTER_LINK_METRIC_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.ROUTER_LINK_METRIC_CMD : range})

    def emulation_ospf_lsa_config_router_link_mode(self, opt):
        """
        This is the method the command: emulation_ospf_lsa_config option router_link_mode
        Description:This option specifies the mode for configuring router links in a router
            LSA. Note that the modify and delete mode do not work. Valid options
            are:createmodifydelete
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            This option specifies the mode for configuring router links in a router
            LSA. Note that the modify and delete mode do not work. Valid options
            are: create modify delete
            Valid options are:
            create

            modify

            delete

            DEFAULT

            create
        Constants Available: ROUTER_LINK_MODE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.ROUTER_LINK_MODE_CMD : opt})

    def emulation_ospf_lsa_config_router_link_type(self, opt):
        """
        This is the method the command: emulation_ospf_lsa_config option router_link_type
        Description:Not defined
            Valid options are:
            ptop

            A point-to-point connection to another router.
            transit

            (default) A connection to a transit network.
            stub

            A connection a stub network.
            virtual

            A virtual link.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            The type of the router link. Valid choices are: ptop - A point-to-point
            connection to another router. transit - (default) A connection to a
            transit network. stub - A connection a stub network. virtual - A virtual
            link.
            Valid options are:
            ptop

            transit

            stub

            virtual

            DEFAULT

            ptop
        Constants Available: ROUTER_LINK_TYPE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.ROUTER_LINK_TYPE_CMD : opt})

    def emulation_ospf_lsa_config_router_virtual_link_endpt(self, bool_opt):
        """
        This is the method the command: emulation_ospf_lsa_config option router_virtual_link_endpt
        Description:Set router to be an endpoint of an active virtual link. Correspond to V
            (virtual link endpoint) bit in router LSA.
            DEFAULT

            0
            IxNetwork-NGPF

            DESCRIPTION

            Set router to be an endpoint of an active virtual link. Correspond to V
            (virtual link endpoint) bit in router LSA.
            DEFAULT

            0
        Constants Available: ROUTER_VIRTUAL_LINK_ENDPT_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.ROUTER_VIRTUAL_LINK_ENDPT_CMD : bool_opt})

    def emulation_ospf_lsa_config_router_wildcard(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_lsa_config_session_type(self, opt):
        """
        This is the method the command: emulation_ospf_lsa_config option session_type
        Description:Not defined
            Valid options are:
            ospfv2

            ospfv3

            DEFAULT

            ospfv2
        Constants Available: SESSION_TYPE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.SESSION_TYPE_CMD : opt})

    def emulation_ospf_lsa_config_summary_number_of_prefix(self, any):
        """
        This is the method the command: emulation_ospf_lsa_config option summary_number_of_prefix
        Description:The number of Summary IP LSAs to generate.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            The number of Summary IP LSAs to generate.
            DEFAULT

            16
        Constants Available: SUMMARY_NUMBER_OF_PREFIX_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.SUMMARY_NUMBER_OF_PREFIX_CMD : any})

    def emulation_ospf_lsa_config_summary_prefix_length(self, any):
        """
        This is the method the command: emulation_ospf_lsa_config option summary_prefix_length
        Description:The number of high-order bits of prefixAddress that are significant.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            The number of high-order bits of prefixAddress that are significant.
            DEFAULT

            16
        Constants Available: SUMMARY_PREFIX_LENGTH_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.SUMMARY_PREFIX_LENGTH_CMD : any})

    def emulation_ospf_lsa_config_summary_prefix_metric(self, range):
        """
        This is the method the command: emulation_ospf_lsa_config option summary_prefix_metric
        Description:The cost of the route for all TOS levels.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            The cost of the route for all TOS levels.
            DEFAULT

            1
        Constants Available: SUMMARY_PREFIX_METRIC_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.SUMMARY_PREFIX_METRIC_CMD : range})

    def emulation_ospf_lsa_config_summary_prefix_start(self, ip):
        """
        This is the method the command: emulation_ospf_lsa_config option summary_prefix_start
        Description:This option is valid for OSPFv3 summary_pool route type. The prefix
            address to be advertised in the LSA. Although only prefixLength bits of
            the IPv6 address are meaningful, a full IPv6 address should be specified.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            This option is valid for OSPFv3 summary_pool route type. The prefix
            address to be advertised in the LSA. Although only prefixLength bits of
            the IPv6 address are meaningful, a full IPv6 address should be specified.
            DEFAULT

            15.0.0.1
        Constants Available: SUMMARY_PREFIX_START_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.SUMMARY_PREFIX_START_CMD : ip})

    def emulation_ospf_lsa_config_summary_prefix_step(self, ip):
        """
        This is the method the command: emulation_ospf_lsa_config option summary_prefix_step
        Description:If summary_number_of_prefix is greater than 1, this is the value that
            will be added to the most significant summary_prefix_length bits of
            summary_prefix_start between generated LSAs. This is also the value to
            increment the link_state_id, if link_state_id_step is not present.This
            parameter can be provided as an IPv4/IPv6 address, depending on the
            prefix type, but the corresponding number of the IP address provided
            should not be greater than 4,294,967,295.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            If summary_number_of_prefix is greater than 1, this is the value that
            will be added to the most significant summary_prefix_length bits of
            summary_prefix_start between generated LSAs. This is also the value to
            increment the link_state_id, if link_state_id_step is not present. This
            parameter can be provided as an IPv4/IPv6 address, depending on the
            prefix type, but the corresponding number of the IP address provided
            should not be greater than 4,294,967,295.
            DEFAULT

            0.0.0.1
        Constants Available: SUMMARY_PREFIX_STEP_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.SUMMARY_PREFIX_STEP_CMD : ip})

    def emulation_ospf_lsa_config_te_admin_group(self):
        """
        This is the method the command: emulation_ospf_lsa_config option te_admin_group
        Constants Available: TE_ADMIN_GROUP_CMD
        Supported:Supported platforms     Details
        Keyword arguments:
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.TE_ADMIN_GROUP_CMD : ""})

    def emulation_ospf_lsa_config_te_instance_id(self):
        """
        This is the method the command: emulation_ospf_lsa_config option te_instance_id
        Constants Available: TE_INSTANCE_ID_CMD
        Supported:Supported platforms     Details
        Keyword arguments:
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.TE_INSTANCE_ID_CMD : ""})

    def emulation_ospf_lsa_config_te_link_id(self):
        """
        This is the method the command: emulation_ospf_lsa_config option te_link_id
        Constants Available: TE_LINK_ID_CMD
        Supported:Supported platforms     Details
        Keyword arguments:
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.TE_LINK_ID_CMD : ""})

    def emulation_ospf_lsa_config_te_link_type(self):
        """
        This is the method the command: emulation_ospf_lsa_config option te_link_type
        Constants Available: TE_LINK_TYPE_CMD
        Supported:Supported platforms     Details
        Keyword arguments:
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.TE_LINK_TYPE_CMD : ""})

    def emulation_ospf_lsa_config_te_local_ip(self):
        """
        This is the method the command: emulation_ospf_lsa_config option te_local_ip
        Constants Available: TE_LOCAL_IP_CMD
        Supported:Supported platforms     Details
        Keyword arguments:
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.TE_LOCAL_IP_CMD : ""})

    def emulation_ospf_lsa_config_te_max_bw(self):
        """
        This is the method the command: emulation_ospf_lsa_config option te_max_bw
        Constants Available: TE_MAX_BW_CMD
        Supported:Supported platforms     Details
        Keyword arguments:
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.TE_MAX_BW_CMD : ""})

    def emulation_ospf_lsa_config_te_max_resv_bw(self):
        """
        This is the method the command: emulation_ospf_lsa_config option te_max_resv_bw
        Constants Available: TE_MAX_RESV_BW_CMD
        Supported:Supported platforms     Details
        Keyword arguments:
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.TE_MAX_RESV_BW_CMD : ""})

    def emulation_ospf_lsa_config_te_max_resv_priority0(self):
        """
        This is the method the command: emulation_ospf_lsa_config option te_max_resv_priority0
        Constants Available: TE_MAX_RESV_PRIORITY0_CMD
        Supported:Supported platforms     Details
        Keyword arguments:
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.TE_MAX_RESV_PRIORITY0_CMD : ""})

    def emulation_ospf_lsa_config_te_max_resv_priority1(self):
        """
        This is the method the command: emulation_ospf_lsa_config option te_max_resv_priority1
        Constants Available: TE_MAX_RESV_PRIORITY1_CMD
        Supported:Supported platforms     Details
        Keyword arguments:
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.TE_MAX_RESV_PRIORITY1_CMD : ""})

    def emulation_ospf_lsa_config_te_max_resv_priority2(self):
        """
        This is the method the command: emulation_ospf_lsa_config option te_max_resv_priority2
        Constants Available: TE_MAX_RESV_PRIORITY2_CMD
        Supported:Supported platforms     Details
        Keyword arguments:
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.TE_MAX_RESV_PRIORITY2_CMD : ""})

    def emulation_ospf_lsa_config_te_max_resv_priority3(self):
        """
        This is the method the command: emulation_ospf_lsa_config option te_max_resv_priority3
        Constants Available: TE_MAX_RESV_PRIORITY3_CMD
        Supported:Supported platforms     Details
        Keyword arguments:
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.TE_MAX_RESV_PRIORITY3_CMD : ""})

    def emulation_ospf_lsa_config_te_max_resv_priority4(self):
        """
        This is the method the command: emulation_ospf_lsa_config option te_max_resv_priority4
        Constants Available: TE_MAX_RESV_PRIORITY4_CMD
        Supported:Supported platforms     Details
        Keyword arguments:
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.TE_MAX_RESV_PRIORITY4_CMD : ""})

    def emulation_ospf_lsa_config_te_max_resv_priority5(self):
        """
        This is the method the command: emulation_ospf_lsa_config option te_max_resv_priority5
        Constants Available: TE_MAX_RESV_PRIORITY5_CMD
        Supported:Supported platforms     Details
        Keyword arguments:
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.TE_MAX_RESV_PRIORITY5_CMD : ""})

    def emulation_ospf_lsa_config_te_max_resv_priority6(self):
        """
        This is the method the command: emulation_ospf_lsa_config option te_max_resv_priority6
        Constants Available: TE_MAX_RESV_PRIORITY6_CMD
        Supported:Supported platforms     Details
        Keyword arguments:
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.TE_MAX_RESV_PRIORITY6_CMD : ""})

    def emulation_ospf_lsa_config_te_max_resv_priority7(self):
        """
        This is the method the command: emulation_ospf_lsa_config option te_max_resv_priority7
        Constants Available: TE_MAX_RESV_PRIORITY7_CMD
        Supported:Supported platforms     Details
        Keyword arguments:
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.TE_MAX_RESV_PRIORITY7_CMD : ""})

    def emulation_ospf_lsa_config_te_metric(self):
        """
        This is the method the command: emulation_ospf_lsa_config option te_metric
        Constants Available: TE_METRIC_CMD
        Supported:Supported platforms     Details
        Keyword arguments:
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.TE_METRIC_CMD : ""})

    def emulation_ospf_lsa_config_te_remote_ip(self):
        """
        This is the method the command: emulation_ospf_lsa_config option te_remote_ip
        Constants Available: TE_REMOTE_IP_CMD
        Supported:Supported platforms     Details
        Keyword arguments:
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.TE_REMOTE_IP_CMD : ""})

    def emulation_ospf_lsa_config_te_router_address(self):
        """
        This is the method the command: emulation_ospf_lsa_config option te_router_address
        Constants Available: TE_ROUTER_ADDRESS_CMD
        Supported:Supported platforms     Details
        Keyword arguments:
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.TE_ROUTER_ADDRESS_CMD : ""})

    def emulation_ospf_lsa_config_te_tlv_type(self):
        """
        This is the method the command: emulation_ospf_lsa_config option te_tlv_type
        Constants Available: TE_TLV_TYPE_CMD
        Supported:Supported platforms     Details
        Keyword arguments:
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.TE_TLV_TYPE_CMD : ""})

    def emulation_ospf_lsa_config_type(self, opt):
        """
        This is the method the command: emulation_ospf_lsa_config option type
        Description:This option specified the type of the LSA. The user *must* pass this
            option when creating a LSA. The choices are: router - ospfv2, ospfv3
            network - ospfv2, ospfv3 summary_pool - ospfv2, ospfv3 asbr_summary -
            ospfv2, ospfv3 ext_pool - ospfv2, ospfv3 opaque_type_9 - ospfv2
            opaque_type_10 - ospfv2 opaque_type_11 - ospfv2
            DEFAULT

            router
        Constants Available: TYPE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_ospf_lsa_config({EmulationOspfLsaConfigConstants.TYPE_CMD : opt})


"""
    This is the Constants class for the command: emulation_ospf_lsa_config
    Commands end with _CMD and constants for a command start with the beginning
    with the command's constant name minus the _CMD
"""


class EmulationOspfLsaConfigConstants(object, metaclass=Singleton):
    # api reference constant for this api to get it from the device
    EMULATION_OSPF_LSA_CONFIG_API = "EMULATION_OSPF_LSA_CONFIG_API"

    ADV_ROUTER_ID_CMD = "adv_router_id"

    AREA_ID_CMD = "area_id"

    ATTACHED_ROUTER_ID_CMD = "attached_router_id"

    AUTO_LS_AGE_CMD = "auto_ls_age"

    AUTO_LS_CHECKSUM_CMD = "auto_ls_checksum"

    AUTO_LS_SEQ_CMD = "auto_ls_seq"

    AUTO_UPDATE_CMD = "auto_update"

    EXTERNAL_METRIC_EBIT_CMD = "external_metric_ebit"
    # Constant values for EXTERNAL_METRIC_EBIT_CMD
    EXTERNAL_METRIC_EBIT_0 = "0"
    EXTERNAL_METRIC_EBIT_1 = "1"

    EXTERNAL_METRIC_FBIT_CMD = "external_metric_fbit"
    # Constant values for EXTERNAL_METRIC_FBIT_CMD
    EXTERNAL_METRIC_FBIT_0 = "0"
    EXTERNAL_METRIC_FBIT_1 = "1"

    EXTERNAL_METRIC_TBIT_CMD = "external_metric_tbit"
    # Constant values for EXTERNAL_METRIC_TBIT_CMD
    EXTERNAL_METRIC_TBIT_0 = "0"
    EXTERNAL_METRIC_TBIT_1 = "1"

    EXTERNAL_NUMBER_OF_PREFIX_CMD = "external_number_of_prefix"

    EXTERNAL_PREFIX_FORWARD_ADDR_CMD = "external_prefix_forward_addr"

    EXTERNAL_PREFIX_LENGTH_CMD = "external_prefix_length"

    EXTERNAL_PREFIX_METRIC_CMD = "external_prefix_metric"

    EXTERNAL_PREFIX_START_CMD = "external_prefix_start"

    EXTERNAL_PREFIX_STEP_CMD = "external_prefix_step"

    EXTERNAL_PREFIX_TYPE_CMD = "external_prefix_type"
    # Constant values for EXTERNAL_PREFIX_TYPE_CMD
    EXTERNAL_PREFIX_TYPE_1 = "1"
    EXTERNAL_PREFIX_TYPE_2 = "2"

    EXTERNAL_ROUTE_TAG_CMD = "external_route_tag"

    HANDLE_CMD = "handle"

    LINK_STATE_ID_CMD = "link_state_id"

    LINK_STATE_ID_STEP_CMD = "link_state_id_step"

    LS_AGE_CMD = "ls_age"

    LS_CHECKSUM_CMD = "ls_checksum"

    LS_SEQ_CMD = "ls_seq"

    LS_TYPE_FUNCTION_CODE_CMD = "ls_type_function_code"

    LS_TYPE_S_BITS_CMD = "ls_type_s_bits"

    LS_TYPE_U_BIT_CMD = "ls_type_u_bit"

    LSA_GROUP_MODE_CMD = "lsa_group_mode"
    # Constant values for LSA_GROUP_MODE_CMD
    LSA_GROUP_MODE_ANY = "ANY"
    LSA_GROUP_MODE_APPEND = "append"
    LSA_GROUP_MODE_CREATE = "create"

    LSA_HANDLE_CMD = "lsa_handle"

    MODE_CMD = "mode"
    # Constant values for MODE_CMD
    MODE_CREATE = "create"
    MODE_DELETE = "delete"
    MODE_MODIFY = "modify"
    MODE_RESET = "reset"

    NET_ATTACHED_ROUTER_CMD = "net_attached_router"
    # Constant values for NET_ATTACHED_ROUTER_CMD
    NET_ATTACHED_ROUTER_CREATE = "create"
    NET_ATTACHED_ROUTER_DELETE = "delete"
    NET_ATTACHED_ROUTER_RESET = "reset"

    NET_PREFIX_LENGTH_CMD = "net_prefix_length"

    NO_WRITE_CMD = "no_write"

    NSSA_NUMBER_OF_PREFIX_CMD = "nssa_number_of_prefix"

    NSSA_PREFIX_FORWARD_ADDR_CMD = "nssa_prefix_forward_addr"

    NSSA_PREFIX_LENGTH_CMD = "nssa_prefix_length"

    NSSA_PREFIX_METRIC_CMD = "nssa_prefix_metric"

    NSSA_PREFIX_START_CMD = "nssa_prefix_start"

    NSSA_PREFIX_STEP_CMD = "nssa_prefix_step"

    NSSA_PREFIX_TYPE_CMD = "nssa_prefix_type"

    OPAQUE_ENABLE_LINK_ID_CMD = "opaque_enable_link_id"

    OPAQUE_ENABLE_LINK_LOCAL_IP_ADDR_CMD = "opaque_enable_link_local_ip_addr"

    OPAQUE_ENABLE_LINK_MAX_BW_CMD = "opaque_enable_link_max_bw"

    OPAQUE_ENABLE_LINK_MAX_RESV_BW_CMD = "opaque_enable_link_max_resv_bw"

    OPAQUE_ENABLE_LINK_METRIC_CMD = "opaque_enable_link_metric"

    OPAQUE_ENABLE_LINK_REMOTE_IP_ADDR_CMD = "opaque_enable_link_remote_ip_addr"

    OPAQUE_ENABLE_LINK_RESOURCE_CLASS_CMD = "opaque_enable_link_resource_class"

    OPAQUE_ENABLE_LINK_TYPE_CMD = "opaque_enable_link_type"

    OPAQUE_ENABLE_LINK_UNRESV_BW_CMD = "opaque_enable_link_unresv_bw"

    OPAQUE_LINK_ID_CMD = "opaque_link_id"

    OPAQUE_LINK_LOCAL_IP_ADDR_CMD = "opaque_link_local_ip_addr"

    OPAQUE_LINK_MAX_BW_CMD = "opaque_link_max_bw"

    OPAQUE_LINK_MAX_RESV_BW_CMD = "opaque_link_max_resv_bw"

    OPAQUE_LINK_METRIC_CMD = "opaque_link_metric"

    OPAQUE_LINK_OTHER_SUBTLVS_CMD = "opaque_link_other_subtlvs"

    OPAQUE_LINK_REMOTE_IP_ADDR_CMD = "opaque_link_remote_ip_addr"

    OPAQUE_LINK_RESOURCE_CLASS_CMD = "opaque_link_resource_class"

    OPAQUE_LINK_SUBTLVS_CMD = "opaque_link_subtlvs"

    OPAQUE_LINK_TYPE_CMD = "opaque_link_type"
    # Constant values for OPAQUE_LINK_TYPE_CMD
    OPAQUE_LINK_TYPE_DEAULT = "DEAULT"
    OPAQUE_LINK_TYPE_MULTIACCESS = "multiaccess"
    OPAQUE_LINK_TYPE_PTOP = "ptop"

    OPAQUE_LINK_UNRESV_BW_PRIORITY_CMD = "opaque_link_unresv_bw_priority"

    OPAQUE_ROUTER_ADDR_CMD = "opaque_router_addr"

    OPAQUE_TLV_TYPE_CMD = "opaque_tlv_type"
    # Constant values for OPAQUE_TLV_TYPE_CMD
    OPAQUE_TLV_TYPE_LINK = "link"
    OPAQUE_TLV_TYPE_ROUTER = "router"

    OPTIONS_CMD = "options"

    PREFIX_OPTIONS_CMD = "prefix_options"

    ROUTER_ABR_CMD = "router_abr"

    ROUTER_ASBR_CMD = "router_asbr"

    ROUTER_LINK_DATA_CMD = "router_link_data"

    ROUTER_LINK_ID_CMD = "router_link_id"

    ROUTER_LINK_IDX_CMD = "router_link_idx"

    ROUTER_LINK_METRIC_CMD = "router_link_metric"

    ROUTER_LINK_MODE_CMD = "router_link_mode"
    # Constant values for ROUTER_LINK_MODE_CMD
    ROUTER_LINK_MODE_CREATE = "create"
    ROUTER_LINK_MODE_DELETE = "delete"
    ROUTER_LINK_MODE_MODIFY = "modify"

    ROUTER_LINK_TYPE_CMD = "router_link_type"
    # Constant values for ROUTER_LINK_TYPE_CMD
    ROUTER_LINK_TYPE_PTOP = "ptop"
    ROUTER_LINK_TYPE_STUB = "stub"
    ROUTER_LINK_TYPE_TRANSIT = "transit"
    ROUTER_LINK_TYPE_VIRTUAL = "virtual"

    ROUTER_VIRTUAL_LINK_ENDPT_CMD = "router_virtual_link_endpt"

    ROUTER_WILDCARD_CMD = "router_wildcard"

    SESSION_TYPE_CMD = "session_type"
    # Constant values for SESSION_TYPE_CMD
    SESSION_TYPE_OSPFV2 = "ospfv2"
    SESSION_TYPE_OSPFV3 = "ospfv3"

    SUMMARY_NUMBER_OF_PREFIX_CMD = "summary_number_of_prefix"

    SUMMARY_PREFIX_LENGTH_CMD = "summary_prefix_length"

    SUMMARY_PREFIX_METRIC_CMD = "summary_prefix_metric"

    SUMMARY_PREFIX_START_CMD = "summary_prefix_start"

    SUMMARY_PREFIX_STEP_CMD = "summary_prefix_step"

    TE_ADMIN_GROUP_CMD = "te_admin_group"

    TE_INSTANCE_ID_CMD = "te_instance_id"

    TE_LINK_ID_CMD = "te_link_id"

    TE_LINK_TYPE_CMD = "te_link_type"

    TE_LOCAL_IP_CMD = "te_local_ip"

    TE_MAX_BW_CMD = "te_max_bw"

    TE_MAX_RESV_BW_CMD = "te_max_resv_bw"

    TE_MAX_RESV_PRIORITY0_CMD = "te_max_resv_priority0"

    TE_MAX_RESV_PRIORITY1_CMD = "te_max_resv_priority1"

    TE_MAX_RESV_PRIORITY2_CMD = "te_max_resv_priority2"

    TE_MAX_RESV_PRIORITY3_CMD = "te_max_resv_priority3"

    TE_MAX_RESV_PRIORITY4_CMD = "te_max_resv_priority4"

    TE_MAX_RESV_PRIORITY5_CMD = "te_max_resv_priority5"

    TE_MAX_RESV_PRIORITY6_CMD = "te_max_resv_priority6"

    TE_MAX_RESV_PRIORITY7_CMD = "te_max_resv_priority7"

    TE_METRIC_CMD = "te_metric"

    TE_REMOTE_IP_CMD = "te_remote_ip"

    TE_ROUTER_ADDRESS_CMD = "te_router_address"

    TE_TLV_TYPE_CMD = "te_tlv_type"

    TYPE_CMD = "type"
    # Constant values for TYPE_CMD
    TYPE_ASBR_SUMMARY = "asbr_summary"
    TYPE_EXT_POOL = "ext_pool"
    TYPE_NETWORK = "network"
    TYPE_OPAQUE_TYPE_10 = "opaque_type_10"
    TYPE_OPAQUE_TYPE_11 = "opaque_type_11"
    TYPE_OPAQUE_TYPE_9 = "opaque_type_9"
    TYPE_ROUTER = "router"
    TYPE_SUMMARY_POOL = "summary_pool"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass

"""
Implemented Commands (Alphabetical)
    -adv_router_id
    -area_id
    -attached_router_id
    -auto_ls_age
    -auto_ls_checksum
    -auto_ls_seq
    -auto_update
    -external_metric_ebit
    -external_metric_fbit
    -external_metric_tbit
    -external_number_of_prefix
    -external_prefix_forward_addr
    -external_prefix_length
    -external_prefix_metric
    -external_prefix_start
    -external_prefix_step
    -external_prefix_type
    -external_route_tag
    -handle
    -link_state_id
    -link_state_id_step
    -ls_age
    -ls_checksum
    -ls_seq
    -ls_type_function_code
    -ls_type_s_bits
    -ls_type_u_bit
    -lsa_group_mode
    -lsa_handle
    -mode
    -net_attached_router
    -net_prefix_length
    -no_write
    -nssa_number_of_prefix
    -nssa_prefix_forward_addr
    -nssa_prefix_length
    -nssa_prefix_metric
    -nssa_prefix_start
    -nssa_prefix_step
    -nssa_prefix_type
    -opaque_enable_link_id
    -opaque_enable_link_local_ip_addr
    -opaque_enable_link_max_bw
    -opaque_enable_link_max_resv_bw
    -opaque_enable_link_metric
    -opaque_enable_link_remote_ip_addr
    -opaque_enable_link_resource_class
    -opaque_enable_link_type
    -opaque_enable_link_unresv_bw
    -opaque_link_id
    -opaque_link_local_ip_addr
    -opaque_link_max_bw
    -opaque_link_max_resv_bw
    -opaque_link_metric
    -opaque_link_other_subtlvs
    -opaque_link_remote_ip_addr
    -opaque_link_resource_class
    -opaque_link_subtlvs
    -opaque_link_type
    -opaque_link_unresv_bw_priority
    -opaque_router_addr
    -opaque_tlv_type
    -options
    -prefix_options
    -router_abr
    -router_asbr
    -router_link_data
    -router_link_id
    -router_link_idx
    -router_link_metric
    -router_link_mode
    -router_link_type
    -router_virtual_link_endpt
    -router_wildcard
    -session_type
    -summary_number_of_prefix
    -summary_prefix_length
    -summary_prefix_metric
    -summary_prefix_start
    -summary_prefix_step
    -te_admin_group
    -te_instance_id
    -te_link_id
    -te_link_type
    -te_local_ip
    -te_max_bw
    -te_max_resv_bw
    -te_max_resv_priority0
    -te_max_resv_priority1
    -te_max_resv_priority2
    -te_max_resv_priority3
    -te_max_resv_priority4
    -te_max_resv_priority5
    -te_max_resv_priority6
    -te_max_resv_priority7
    -te_metric
    -te_remote_ip
    -te_router_address
    -te_tlv_type
    -type
If you want to update this file, look in the CSV
"""
