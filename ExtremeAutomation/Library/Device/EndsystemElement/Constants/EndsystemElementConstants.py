from ExtremeAutomation.Library.Utils.Constants.Constants import Constants


class EndsystemElementConstants(Constants):
    # Device class returns
    METHOD_RETURN_COMMAND = "command"
    METHOD_RETURN_PROMPT = "prompts"
    METHOD_RETURN_PROMPT_ARGS = "promptargs"
    METHOD_RETURN_CONFIRM_PHRASES = "comfirmphrases"
    METHOD_RETURN_CONFIRM_ARGS = "comfirmargs"
    METHOD_RETURN_TEXT = "returntext"
    METHOD_RETURN_ERROR_TEXT = "returnerrortext"
    METHOD_NOT_SUPPORTED = "method not supported"
    METHOD_RETURN_START_TIME = "methodstarttime"
    METHOD_RETURN_END_TIME = "methodendtime"

    # OS Constants
    OS_CCSERVER = "CCSERVER"
    OS_WINDOWS = "WINDOWS"
    OS_LINUX = "LINUX"
    OS_EMC = "EMC"
    OS_GIM = "GIM"
    OS_ECIQ = "ECIQ"
    OS_WINDOWS_MU = "MU-WINDOWS"
    OS_LINUX_MU = "MU-LINUX"
    OS_MAC_MU =  "MU-MAC"
    OS_A3 = "A3"


    # Unit Constants
    UNIT_BASE = "baseunit"

    # Version Constants
    VERSION_BASE = "baseversion"

    # Platform Constants
    PLATFORM_BASE = "base"
    PLATFORM_LINUX_BASE = "base"
    PLATFORM_WINDOWS_BASE = "base"
    PLATFORM_CCSERVER_BASE = "base"
    PLATFORM_EMC_BASE = "base"
    PLATFORM_GIM_BASE = "base"
    PLATFORM_ECIQ_BASE = "base"
    PLATFORM_MU_WINDOWS_BASE = "base"
    PLATFORM_MU_LINUX_BASE = "base"
    PLATFORM_MU_MAC_BASE = "base"
    PLATFORM_A3_BASE = "base"

    # API Constants
    API_COMMON = "common"
    API_HOSTSERVICES = "hostservices"
    API_NETWORKING = "networking"
    API_MULTIAUTHMETHODCLIENT = "multiauthmethodclient"
    API_DHCP = "dhcp"
    API_DEVICES = "devices"
    API_NETSIGHT_UTILITIES = "netsightutilities"
    API_DATADRIVEN = "datadriven"
    API_DEMO = "demo"
    API_ECIQ_DEVICES = "eciqdevices"

    CLISENDLOGGERNAME = "cli_send_logger_name"
    CLIREADLOGGERNAME = "cli_read_logger_name"
    CLISTREAMLOGGERNAME = "cli_stream_logger)name"
    INFOLOGGERNAME = "info_logger_name"
    VALUE_NOT_PRESENT = "valueNotPresent"

    DEFAULT_SLEEP_BETWEEN_COMMANDS = 500
