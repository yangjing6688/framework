from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.Ospf.HltapiEmulationOspfLsaConfigApi import EmulationOspfLsaConfigApi, EmulationOspfLsaConfigConstants

"""
    This is the API class for the command: emulation_ospf_lsa_config

    Class is auto-generated. If you update anything here,
        it will be over written.
"""


class SpirentEmulationOspfLsaConfigApi(EmulationOspfLsaConfigApi):

    """
    init function
    """
    def __init__(self, device):
        super(SpirentEmulationOspfLsaConfigApi, self).__init__(device)

    """
    This is the "One Large Method" for the command: emulation_ospf_lsa_config
    use this by passing in a dict() of all the commands

        api = device.getApi(EmulationOspfLsaConfigConstants.EMULATION_OSPF_LSA_CONFIG_API)
        assert isinstance(api, EmulationOspfLsaConfigApi)
        api.emulation_ospf_lsa_config(dummyDict)
    """
    def emulation_ospf_lsa_config(self, argdictionary):
        return super(SpirentEmulationOspfLsaConfigApi, self).emulation_ospf_lsa_config(argdictionary, self.supportedSpirentHltapiCommands)

    """
    Individual commands for each option. Typically, the "One Large Method"
    is the one that you want to be using so look at that example above
    """
    def emulation_ospf_lsa_config_area_id(self, ip):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_lsa_config_external_metric_ebit(self, opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_lsa_config_external_metric_fbit(self, opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_lsa_config_external_metric_tbit(self, opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_lsa_config_lsa_group_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_lsa_config_no_write(self, flag):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_lsa_config_opaque_link_other_subtlvs(self, any):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_lsa_config_prefix_options(self, any):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_lsa_config_router_wildcard(self, bool_opt):
        return self.logger.log_unimplemented_method()


    supportedSpirentHltapiCommands = {EmulationOspfLsaConfigConstants.ADV_ROUTER_ID_CMD, EmulationOspfLsaConfigConstants.ATTACHED_ROUTER_ID_CMD, EmulationOspfLsaConfigConstants.AUTO_LS_AGE_CMD, EmulationOspfLsaConfigConstants.AUTO_LS_CHECKSUM_CMD, EmulationOspfLsaConfigConstants.AUTO_LS_SEQ_CMD, EmulationOspfLsaConfigConstants.AUTO_UPDATE_CMD, EmulationOspfLsaConfigConstants.EXTERNAL_NUMBER_OF_PREFIX_CMD, EmulationOspfLsaConfigConstants.EXTERNAL_PREFIX_FORWARD_ADDR_CMD, EmulationOspfLsaConfigConstants.EXTERNAL_PREFIX_LENGTH_CMD, EmulationOspfLsaConfigConstants.EXTERNAL_PREFIX_METRIC_CMD, EmulationOspfLsaConfigConstants.EXTERNAL_PREFIX_START_CMD, EmulationOspfLsaConfigConstants.EXTERNAL_PREFIX_STEP_CMD, EmulationOspfLsaConfigConstants.EXTERNAL_PREFIX_TYPE_CMD, EmulationOspfLsaConfigConstants.EXTERNAL_ROUTE_TAG_CMD, EmulationOspfLsaConfigConstants.HANDLE_CMD, EmulationOspfLsaConfigConstants.LINK_STATE_ID_CMD, EmulationOspfLsaConfigConstants.LINK_STATE_ID_STEP_CMD, EmulationOspfLsaConfigConstants.LS_AGE_CMD, EmulationOspfLsaConfigConstants.LS_CHECKSUM_CMD, EmulationOspfLsaConfigConstants.LS_SEQ_CMD, EmulationOspfLsaConfigConstants.LS_TYPE_FUNCTION_CODE_CMD, EmulationOspfLsaConfigConstants.LS_TYPE_S_BITS_CMD, EmulationOspfLsaConfigConstants.LS_TYPE_U_BIT_CMD, EmulationOspfLsaConfigConstants.LSA_HANDLE_CMD, EmulationOspfLsaConfigConstants.MODE_CMD, EmulationOspfLsaConfigConstants.NET_ATTACHED_ROUTER_CMD, EmulationOspfLsaConfigConstants.NET_PREFIX_LENGTH_CMD, EmulationOspfLsaConfigConstants.NSSA_NUMBER_OF_PREFIX_CMD, EmulationOspfLsaConfigConstants.NSSA_PREFIX_FORWARD_ADDR_CMD, EmulationOspfLsaConfigConstants.NSSA_PREFIX_LENGTH_CMD, EmulationOspfLsaConfigConstants.NSSA_PREFIX_METRIC_CMD, EmulationOspfLsaConfigConstants.NSSA_PREFIX_START_CMD, EmulationOspfLsaConfigConstants.NSSA_PREFIX_STEP_CMD, EmulationOspfLsaConfigConstants.NSSA_PREFIX_TYPE_CMD, EmulationOspfLsaConfigConstants.OPAQUE_ENABLE_LINK_ID_CMD, EmulationOspfLsaConfigConstants.OPAQUE_ENABLE_LINK_LOCAL_IP_ADDR_CMD, EmulationOspfLsaConfigConstants.OPAQUE_ENABLE_LINK_MAX_BW_CMD, EmulationOspfLsaConfigConstants.OPAQUE_ENABLE_LINK_MAX_RESV_BW_CMD, EmulationOspfLsaConfigConstants.OPAQUE_ENABLE_LINK_METRIC_CMD, EmulationOspfLsaConfigConstants.OPAQUE_ENABLE_LINK_REMOTE_IP_ADDR_CMD, EmulationOspfLsaConfigConstants.OPAQUE_ENABLE_LINK_RESOURCE_CLASS_CMD, EmulationOspfLsaConfigConstants.OPAQUE_ENABLE_LINK_TYPE_CMD, EmulationOspfLsaConfigConstants.OPAQUE_ENABLE_LINK_UNRESV_BW_CMD, EmulationOspfLsaConfigConstants.OPAQUE_LINK_ID_CMD, EmulationOspfLsaConfigConstants.OPAQUE_LINK_LOCAL_IP_ADDR_CMD, EmulationOspfLsaConfigConstants.OPAQUE_LINK_MAX_BW_CMD, EmulationOspfLsaConfigConstants.OPAQUE_LINK_MAX_RESV_BW_CMD, EmulationOspfLsaConfigConstants.OPAQUE_LINK_METRIC_CMD, EmulationOspfLsaConfigConstants.OPAQUE_LINK_REMOTE_IP_ADDR_CMD, EmulationOspfLsaConfigConstants.OPAQUE_LINK_RESOURCE_CLASS_CMD, EmulationOspfLsaConfigConstants.OPAQUE_LINK_SUBTLVS_CMD, EmulationOspfLsaConfigConstants.OPAQUE_LINK_TYPE_CMD, EmulationOspfLsaConfigConstants.OPAQUE_LINK_UNRESV_BW_PRIORITY_CMD, EmulationOspfLsaConfigConstants.OPAQUE_ROUTER_ADDR_CMD, EmulationOspfLsaConfigConstants.OPAQUE_TLV_TYPE_CMD, EmulationOspfLsaConfigConstants.OPTIONS_CMD, EmulationOspfLsaConfigConstants.ROUTER_ABR_CMD, EmulationOspfLsaConfigConstants.ROUTER_ASBR_CMD, EmulationOspfLsaConfigConstants.ROUTER_LINK_DATA_CMD, EmulationOspfLsaConfigConstants.ROUTER_LINK_ID_CMD, EmulationOspfLsaConfigConstants.ROUTER_LINK_IDX_CMD, EmulationOspfLsaConfigConstants.ROUTER_LINK_METRIC_CMD, EmulationOspfLsaConfigConstants.ROUTER_LINK_MODE_CMD, EmulationOspfLsaConfigConstants.ROUTER_LINK_TYPE_CMD, EmulationOspfLsaConfigConstants.ROUTER_VIRTUAL_LINK_ENDPT_CMD, EmulationOspfLsaConfigConstants.SESSION_TYPE_CMD, EmulationOspfLsaConfigConstants.SUMMARY_NUMBER_OF_PREFIX_CMD, EmulationOspfLsaConfigConstants.SUMMARY_PREFIX_LENGTH_CMD, EmulationOspfLsaConfigConstants.SUMMARY_PREFIX_METRIC_CMD, EmulationOspfLsaConfigConstants.SUMMARY_PREFIX_START_CMD, EmulationOspfLsaConfigConstants.SUMMARY_PREFIX_STEP_CMD, EmulationOspfLsaConfigConstants.TE_ADMIN_GROUP_CMD, EmulationOspfLsaConfigConstants.TE_INSTANCE_ID_CMD, EmulationOspfLsaConfigConstants.TE_LINK_ID_CMD, EmulationOspfLsaConfigConstants.TE_LINK_TYPE_CMD, EmulationOspfLsaConfigConstants.TE_LOCAL_IP_CMD, EmulationOspfLsaConfigConstants.TE_MAX_BW_CMD, EmulationOspfLsaConfigConstants.TE_MAX_RESV_BW_CMD, EmulationOspfLsaConfigConstants.TE_MAX_RESV_PRIORITY0_CMD, EmulationOspfLsaConfigConstants.TE_MAX_RESV_PRIORITY1_CMD, EmulationOspfLsaConfigConstants.TE_MAX_RESV_PRIORITY2_CMD, EmulationOspfLsaConfigConstants.TE_MAX_RESV_PRIORITY3_CMD, EmulationOspfLsaConfigConstants.TE_MAX_RESV_PRIORITY4_CMD, EmulationOspfLsaConfigConstants.TE_MAX_RESV_PRIORITY5_CMD, EmulationOspfLsaConfigConstants.TE_MAX_RESV_PRIORITY6_CMD, EmulationOspfLsaConfigConstants.TE_MAX_RESV_PRIORITY7_CMD, EmulationOspfLsaConfigConstants.TE_METRIC_CMD, EmulationOspfLsaConfigConstants.TE_REMOTE_IP_CMD, EmulationOspfLsaConfigConstants.TE_ROUTER_ADDRESS_CMD, EmulationOspfLsaConfigConstants.TE_TLV_TYPE_CMD, EmulationOspfLsaConfigConstants.TYPE_CMD}
