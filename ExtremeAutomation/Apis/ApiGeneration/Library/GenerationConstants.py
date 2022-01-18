from ExtremeAutomation.Library.Utils.Constants.Constants import Constants


class GenerationConstants(Constants):
    # Device Type
    DEVICE_TYPE_NET_ELEM = "network_element"
    DEVICE_TYPE_END_SYS_ELEM = "endsystem_element"
    DEVICE_TYPE_UI_ELEM = "ui_element"

    # API Type Constants
    API_TYPE_COMMAND = "COMMAND"
    API_TYPE_PARSE = "PARSE"
    API_TYPE_PLATFORM_VARIABLE = "PLATVAR"

    # Agent Type Constants
    AGENT_TYPE_CLI = "CLI"
    AGENT_TYPE_REST = "REST"
    AGENT_TYPE_SNMP = "SNMP"
    AGENT_TYPE_SIESTA = "SIESTA"
    AGENT_TYPE_SELENIUM = "SELENIUM"
    AGENT_TYPE_NORTHBOUND = "NORTHBOUND"
    AGENT_TYPE_XMC_REST = "XMC_REST"

    # UI App Type Constants
    APPLICATION_TYPE_EMC = "EMC"
    APPLICATION_TYPE_XCA = "XCA"
    APPLICATION_TYPE_XMC = "XMC"
    APPLICATION_TYPE_GIM = "GIM"
    APPLICATION_TYPE_EWC = "EWC"
    APPLICATION_TYPE_ECIQ = "ECIQ"
    APPLICATION_TYPE_DFNDR = "DFNDR"
