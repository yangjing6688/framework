from ExtremeAutomation.Library.Device.Common.CommandObjects.CommandObjectConstants import CommandObjectConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.TrafficGenerationApi import TrafficGenerationApi
from ExtremeAutomation.Library.Utils.Singleton import Singleton

"""
    This is the API class for the command: packet_config_triggers

    Class is auto-generated. If you update anything here,
        it will be over written.
"""


class PacketConfigTriggersApi(TrafficGenerationApi):

    """
    init function
    """
    def __init__(self, device):
        super(PacketConfigTriggersApi, self).__init__(device)

    """
    This is the "One Large Method" for the command: packet_config_triggers
    use this by passing in a dict() of all the commands
        dummyDict = dict()
        dummyDict[PacketConfigTriggersConstants.ASYNC_TRIGGER1_CMD] = "dummyValue1" # static value
        dummyDict[PacketConfigTriggersConstants.ASYNC_TRIGGER1_DA_CMD] = PacketConfigTriggersConstants.ASYNC_TRIGGER1_DA_ANY # constant value
        dummyDict[PacketConfigTriggersConstants.ASYNC_TRIGGER1_SA_CMD] = PacketConfigTriggersConstants.ASYNC_TRIGGER1_SA_ANY # constant value
        dummyDict[PacketConfigTriggersConstants.ASYNC_TRIGGER1_ERROR_CMD] = "dummyValue4" # static value
        dummyDict[PacketConfigTriggersConstants.ASYNC_TRIGGER1_FRAMESIZE_CMD] = PacketConfigTriggersConstants.ASYNC_TRIGGER1_FRAMESIZE_0 # constant value
        dummyDict[PacketConfigTriggersConstants.ASYNC_TRIGGER1_FRAMESIZE_FROM_CMD] = "dummyValue6" # static value
        dummyDict[PacketConfigTriggersConstants.ASYNC_TRIGGER1_FRAMESIZE_TO_CMD] = "dummyValue7" # static value
        dummyDict[PacketConfigTriggersConstants.ASYNC_TRIGGER1_PATTERN_CMD] = PacketConfigTriggersConstants.ASYNC_TRIGGER1_PATTERN_ANY # constant value
        dummyDict[PacketConfigTriggersConstants.ASYNC_TRIGGER2_CMD] = "dummyValue9" # static value
        dummyDict[PacketConfigTriggersConstants.ASYNC_TRIGGER2_DA_CMD] = PacketConfigTriggersConstants.ASYNC_TRIGGER2_DA_ANY # constant value
        dummyDict[PacketConfigTriggersConstants.ASYNC_TRIGGER2_SA_CMD] = PacketConfigTriggersConstants.ASYNC_TRIGGER2_SA_ANY # constant value
        dummyDict[PacketConfigTriggersConstants.ASYNC_TRIGGER2_ERROR_CMD] = "dummyValue12" # static value
        dummyDict[PacketConfigTriggersConstants.ASYNC_TRIGGER2_FRAMESIZE_CMD] = PacketConfigTriggersConstants.ASYNC_TRIGGER2_FRAMESIZE_0 # constant value
        dummyDict[PacketConfigTriggersConstants.ASYNC_TRIGGER2_FRAMESIZE_FROM_CMD] = "dummyValue14" # static value
        dummyDict[PacketConfigTriggersConstants.ASYNC_TRIGGER2_FRAMESIZE_TO_CMD] = "dummyValue15" # static value
        dummyDict[PacketConfigTriggersConstants.ASYNC_TRIGGER2_PATTERN_CMD] = PacketConfigTriggersConstants.ASYNC_TRIGGER2_PATTERN_ANY # constant value
        dummyDict[PacketConfigTriggersConstants.CAPTURE_FILTER_CMD] = "dummyValue17" # static value
        dummyDict[PacketConfigTriggersConstants.CAPTURE_FILTER_DA_CMD] = PacketConfigTriggersConstants.CAPTURE_FILTER_DA_ANY # constant value
        dummyDict[PacketConfigTriggersConstants.CAPTURE_FILTER_SA_CMD] = PacketConfigTriggersConstants.CAPTURE_FILTER_SA_ANY # constant value
        dummyDict[PacketConfigTriggersConstants.CAPTURE_FILTER_ERROR_CMD] = "dummyValue20" # static value
        dummyDict[PacketConfigTriggersConstants.CAPTURE_FILTER_EXPRESSION_STRING_CMD] = "dummyValue21" # static value
        dummyDict[PacketConfigTriggersConstants.CAPTURE_FILTER_FRAMESIZE_CMD] = PacketConfigTriggersConstants.CAPTURE_FILTER_FRAMESIZE_0 # constant value
        dummyDict[PacketConfigTriggersConstants.CAPTURE_FILTER_FRAMESIZE_FROM_CMD] = "dummyValue23" # static value
        dummyDict[PacketConfigTriggersConstants.CAPTURE_FILTER_FRAMESIZE_TO_CMD] = "dummyValue24" # static value
        dummyDict[PacketConfigTriggersConstants.CAPTURE_FILTER_PATTERN_CMD] = PacketConfigTriggersConstants.CAPTURE_FILTER_PATTERN_ANY # constant value
        dummyDict[PacketConfigTriggersConstants.CAPTURE_TRIGGER_CMD] = "dummyValue26" # static value
        dummyDict[PacketConfigTriggersConstants.CAPTURE_TRIGGER_DA_CMD] = PacketConfigTriggersConstants.CAPTURE_TRIGGER_DA_ANY # constant value
        dummyDict[PacketConfigTriggersConstants.CAPTURE_TRIGGER_SA_CMD] = PacketConfigTriggersConstants.CAPTURE_TRIGGER_SA_ANY # constant value
        dummyDict[PacketConfigTriggersConstants.CAPTURE_TRIGGER_ERROR_CMD] = "dummyValue29" # static value
        dummyDict[PacketConfigTriggersConstants.CAPTURE_TRIGGER_EXPRESSION_STRING_CMD] = "dummyValue30" # static value
        dummyDict[PacketConfigTriggersConstants.CAPTURE_TRIGGER_FRAMESIZE_CMD] = PacketConfigTriggersConstants.CAPTURE_TRIGGER_FRAMESIZE_0 # constant value
        dummyDict[PacketConfigTriggersConstants.CAPTURE_TRIGGER_FRAMESIZE_FROM_CMD] = "dummyValue32" # static value
        dummyDict[PacketConfigTriggersConstants.CAPTURE_TRIGGER_FRAMESIZE_TO_CMD] = "dummyValue33" # static value
        dummyDict[PacketConfigTriggersConstants.CAPTURE_TRIGGER_PATTERN_CMD] = PacketConfigTriggersConstants.CAPTURE_TRIGGER_PATTERN_ANY # constant value
        dummyDict[PacketConfigTriggersConstants.HANDLE_CMD] = "dummyValue35" # static value
        dummyDict[PacketConfigTriggersConstants.MODE_CMD] = PacketConfigTriggersConstants.MODE_CREATE # constant value
        dummyDict[PacketConfigTriggersConstants.PORT_HANDLE_CMD] = "dummyValue37" # static value
        dummyDict[PacketConfigTriggersConstants.UDS1_CMD] = "dummyValue38" # static value
        dummyDict[PacketConfigTriggersConstants.UDS1_DA_CMD] = PacketConfigTriggersConstants.UDS1_DA_ANY # constant value
        dummyDict[PacketConfigTriggersConstants.UDS1_SA_CMD] = PacketConfigTriggersConstants.UDS1_SA_ANY # constant value
        dummyDict[PacketConfigTriggersConstants.UDS1_ERROR_CMD] = "dummyValue41" # static value
        dummyDict[PacketConfigTriggersConstants.UDS1_FRAMESIZE_CMD] = PacketConfigTriggersConstants.UDS1_FRAMESIZE_0 # constant value
        dummyDict[PacketConfigTriggersConstants.UDS1_FRAMESIZE_FROM_CMD] = "dummyValue43" # static value
        dummyDict[PacketConfigTriggersConstants.UDS1_FRAMESIZE_TO_CMD] = "dummyValue44" # static value
        dummyDict[PacketConfigTriggersConstants.UDS1_PATTERN_CMD] = PacketConfigTriggersConstants.UDS1_PATTERN_ANY # constant value
        dummyDict[PacketConfigTriggersConstants.UDS2_CMD] = "dummyValue46" # static value
        dummyDict[PacketConfigTriggersConstants.UDS2_DA_CMD] = PacketConfigTriggersConstants.UDS2_DA_ANY # constant value
        dummyDict[PacketConfigTriggersConstants.UDS2_SA_CMD] = PacketConfigTriggersConstants.UDS2_SA_ANY # constant value
        dummyDict[PacketConfigTriggersConstants.UDS2_ERROR_CMD] = "dummyValue49" # static value
        dummyDict[PacketConfigTriggersConstants.UDS2_FRAMESIZE_CMD] = PacketConfigTriggersConstants.UDS2_FRAMESIZE_0 # constant value
        dummyDict[PacketConfigTriggersConstants.UDS2_FRAMESIZE_FROM_CMD] = "dummyValue51" # static value
        dummyDict[PacketConfigTriggersConstants.UDS2_FRAMESIZE_TO_CMD] = "dummyValue52" # static value
        dummyDict[PacketConfigTriggersConstants.UDS2_PATTERN_CMD] = PacketConfigTriggersConstants.UDS2_PATTERN_ANY # constant value

        api = device.getApi(PacketConfigTriggersConstants.PACKET_CONFIG_TRIGGERS_API)
        api.packet_config_triggers(dummyDict)
    """
    def packet_config_triggers(self, argdictionary, supported = None):
        self.process_supported_hltapi_commands(argdictionary, supported)
        return self.send_command_args(self._nameSpace +"::packet_config_triggers", argdictionary)

    """
    Individual commands for each option. Typically, the "One Large Method"
    is the one that you want to be using so look at that example above
    """
    def packet_config_triggers_async_trigger1(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_async_trigger1_DA(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_async_trigger1_SA(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_async_trigger1_error(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_async_trigger1_framesize(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_async_trigger1_framesize_from(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_async_trigger1_framesize_to(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_async_trigger1_pattern(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_async_trigger2(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_async_trigger2_DA(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_async_trigger2_SA(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_async_trigger2_error(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_async_trigger2_framesize(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_async_trigger2_framesize_from(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_async_trigger2_framesize_to(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_async_trigger2_pattern(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_capture_filter(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_capture_filter_DA(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_capture_filter_SA(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_capture_filter_error(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_capture_filter_expression_string(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_capture_filter_framesize(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_capture_filter_framesize_from(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_capture_filter_framesize_to(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_capture_filter_pattern(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_capture_trigger(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_capture_trigger_DA(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_capture_trigger_SA(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_capture_trigger_error(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_capture_trigger_expression_string(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_capture_trigger_framesize(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_capture_trigger_framesize_from(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_capture_trigger_framesize_to(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_capture_trigger_pattern(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_handle(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_mode(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_port_handle(self, port):
        """
        This is the method the command: packet_config_triggers option port_handle
        Description:Depending on the traffic_generator value, this option has different meanings. If traffic_generator ixnetwork_540 is used this parameter is used ixos/ixnetwork_540 - The port for which to configure traffic. Mandatory for -mode create/reset when -traffic_generator is set to ixos. For traffic_generator ixnetwork_540 this is mandatory on mode create only if parameter -emulation_src_handle is missing.ixnetwork/ixnetwork_540 - The port_handle parameter is not necessary anymore. When using IxNetwork, traffic configurations will be done using previously created handles (IP interfaces, PPP ranges, L2TP ranges, Protocol Route Ranges etc.) as sources (parameter -emulation_src_handle) and destinations (-emulation_dst_handle).
        Constants Available: PORT_HANDLE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        port --
        return -- pass/fail
        """
        return self.packet_config_triggers({PacketConfigTriggersConstants.PORT_HANDLE_CMD : port})

    def packet_config_triggers_uds1(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_uds1_DA(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_uds1_SA(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_uds1_error(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_uds1_framesize(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_uds1_framesize_from(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_uds1_framesize_to(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_uds1_pattern(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_uds2(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_uds2_DA(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_uds2_SA(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_uds2_error(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_uds2_framesize(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_uds2_framesize_from(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_uds2_framesize_to(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_uds2_pattern(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED


"""
    This is the Constants class for the command: packet_config_triggers
    Commands end with _CMD and constants for a command start with the beginning
    with the command's constant name minus the _CMD
"""


class PacketConfigTriggersConstants(object, metaclass=Singleton):
    # api reference constant for this api to get it from the device
    PACKET_CONFIG_TRIGGERS_API = "PACKET_CONFIG_TRIGGERS_API"

    ASYNC_TRIGGER1_CMD = "async_trigger1"

    ASYNC_TRIGGER1_DA_CMD = "async_trigger1_DA"
    # Constant values for ASYNC_TRIGGER1_DA_CMD
    ASYNC_TRIGGER1_DA_ANY = "any"
    ASYNC_TRIGGER1_DA_DA1 = "DA1"
    ASYNC_TRIGGER1_DA_NOTDA1 = "notDA1"
    ASYNC_TRIGGER1_DA_DA2 = "DA2"
    ASYNC_TRIGGER1_DA_NOTDA2 = "notDA2"

    ASYNC_TRIGGER1_SA_CMD = "async_trigger1_SA"
    # Constant values for ASYNC_TRIGGER1_SA_CMD
    ASYNC_TRIGGER1_SA_ANY = "any"
    ASYNC_TRIGGER1_SA_SA1 = "SA1"
    ASYNC_TRIGGER1_SA_NOTSA1 = "notSA1"
    ASYNC_TRIGGER1_SA_SA2 = "SA2"
    ASYNC_TRIGGER1_SA_NOTSA2 = "notSA2"

    ASYNC_TRIGGER1_ERROR_CMD = "async_trigger1_error"

    ASYNC_TRIGGER1_FRAMESIZE_CMD = "async_trigger1_framesize"
    # Constant values for ASYNC_TRIGGER1_FRAMESIZE_CMD
    ASYNC_TRIGGER1_FRAMESIZE_0 = "0"
    ASYNC_TRIGGER1_FRAMESIZE_1 = "1"
    ASYNC_TRIGGER1_FRAMESIZE_JUMBO = "jumbo"
    ASYNC_TRIGGER1_FRAMESIZE_OVERSIZED = "oversized"
    ASYNC_TRIGGER1_FRAMESIZE_UNDERSIZED = "undersized"

    ASYNC_TRIGGER1_FRAMESIZE_FROM_CMD = "async_trigger1_framesize_from"

    ASYNC_TRIGGER1_FRAMESIZE_TO_CMD = "async_trigger1_framesize_to"

    ASYNC_TRIGGER1_PATTERN_CMD = "async_trigger1_pattern"
    # Constant values for ASYNC_TRIGGER1_PATTERN_CMD
    ASYNC_TRIGGER1_PATTERN_ANY = "any"
    ASYNC_TRIGGER1_PATTERN_PATTERN1 = "pattern1"
    ASYNC_TRIGGER1_PATTERN_NOTPATTERN1 = "notPattern1"
    ASYNC_TRIGGER1_PATTERN_PATTERN2 = "pattern2"
    ASYNC_TRIGGER1_PATTERN_NOTPATTERN2 = "notPattern2"
    ASYNC_TRIGGER1_PATTERN_PATTERN1AND2 = "pattern1and2"

    ASYNC_TRIGGER2_CMD = "async_trigger2"

    ASYNC_TRIGGER2_DA_CMD = "async_trigger2_DA"
    # Constant values for ASYNC_TRIGGER2_DA_CMD
    ASYNC_TRIGGER2_DA_ANY = "any"
    ASYNC_TRIGGER2_DA_DA1 = "DA1"
    ASYNC_TRIGGER2_DA_NOTDA1 = "notDA1"
    ASYNC_TRIGGER2_DA_DA2 = "DA2"
    ASYNC_TRIGGER2_DA_NOTDA2 = "notDA2"

    ASYNC_TRIGGER2_SA_CMD = "async_trigger2_SA"
    # Constant values for ASYNC_TRIGGER2_SA_CMD
    ASYNC_TRIGGER2_SA_ANY = "any"
    ASYNC_TRIGGER2_SA_SA1 = "SA1"
    ASYNC_TRIGGER2_SA_NOTSA1 = "notSA1"
    ASYNC_TRIGGER2_SA_SA2 = "SA2"
    ASYNC_TRIGGER2_SA_NOTSA2 = "notSA2"

    ASYNC_TRIGGER2_ERROR_CMD = "async_trigger2_error"

    ASYNC_TRIGGER2_FRAMESIZE_CMD = "async_trigger2_framesize"
    # Constant values for ASYNC_TRIGGER2_FRAMESIZE_CMD
    ASYNC_TRIGGER2_FRAMESIZE_0 = "0"
    ASYNC_TRIGGER2_FRAMESIZE_1 = "1"
    ASYNC_TRIGGER2_FRAMESIZE_JUMBO = "jumbo"
    ASYNC_TRIGGER2_FRAMESIZE_OVERSIZED = "oversized"
    ASYNC_TRIGGER2_FRAMESIZE_UNDERSIZED = "undersized"

    ASYNC_TRIGGER2_FRAMESIZE_FROM_CMD = "async_trigger2_framesize_from"

    ASYNC_TRIGGER2_FRAMESIZE_TO_CMD = "async_trigger2_framesize_to"

    ASYNC_TRIGGER2_PATTERN_CMD = "async_trigger2_pattern"
    # Constant values for ASYNC_TRIGGER2_PATTERN_CMD
    ASYNC_TRIGGER2_PATTERN_ANY = "any"
    ASYNC_TRIGGER2_PATTERN_PATTERN1 = "pattern1"
    ASYNC_TRIGGER2_PATTERN_NOTPATTERN1 = "notPattern1"
    ASYNC_TRIGGER2_PATTERN_PATTERN2 = "pattern2"
    ASYNC_TRIGGER2_PATTERN_NOTPATTERN2 = "notPattern2"
    ASYNC_TRIGGER2_PATTERN_PATTERN1AND2 = "pattern1and2"

    CAPTURE_FILTER_CMD = "capture_filter"

    CAPTURE_FILTER_DA_CMD = "capture_filter_DA"
    # Constant values for CAPTURE_FILTER_DA_CMD
    CAPTURE_FILTER_DA_ANY = "any"
    CAPTURE_FILTER_DA_DA1 = "DA1"
    CAPTURE_FILTER_DA_NOTDA1 = "notDA1"
    CAPTURE_FILTER_DA_DA2 = "DA2"
    CAPTURE_FILTER_DA_NOTDA2 = "notDA2"

    CAPTURE_FILTER_SA_CMD = "capture_filter_SA"
    # Constant values for CAPTURE_FILTER_SA_CMD
    CAPTURE_FILTER_SA_ANY = "any"
    CAPTURE_FILTER_SA_SA1 = "SA1"
    CAPTURE_FILTER_SA_NOTSA1 = "notSA1"
    CAPTURE_FILTER_SA_SA2 = "SA2"
    CAPTURE_FILTER_SA_NOTSA2 = "notSA2"

    CAPTURE_FILTER_ERROR_CMD = "capture_filter_error"

    CAPTURE_FILTER_EXPRESSION_STRING_CMD = "capture_filter_expression_string"

    CAPTURE_FILTER_FRAMESIZE_CMD = "capture_filter_framesize"
    # Constant values for CAPTURE_FILTER_FRAMESIZE_CMD
    CAPTURE_FILTER_FRAMESIZE_0 = "0"
    CAPTURE_FILTER_FRAMESIZE_1 = "1"
    CAPTURE_FILTER_FRAMESIZE_JUMBO = "jumbo"
    CAPTURE_FILTER_FRAMESIZE_OVERSIZED = "oversized"
    CAPTURE_FILTER_FRAMESIZE_UNDERSIZED = "undersized"

    CAPTURE_FILTER_FRAMESIZE_FROM_CMD = "capture_filter_framesize_from"

    CAPTURE_FILTER_FRAMESIZE_TO_CMD = "capture_filter_framesize_to"

    CAPTURE_FILTER_PATTERN_CMD = "capture_filter_pattern"
    # Constant values for CAPTURE_FILTER_PATTERN_CMD
    CAPTURE_FILTER_PATTERN_ANY = "any"
    CAPTURE_FILTER_PATTERN_PATTERN1 = "pattern1"
    CAPTURE_FILTER_PATTERN_NOTPATTERN1 = "notPattern1"
    CAPTURE_FILTER_PATTERN_PATTERN2 = "pattern2"
    CAPTURE_FILTER_PATTERN_NOTPATTERN2 = "notPattern2"
    CAPTURE_FILTER_PATTERN_PATTERN1AND2 = "pattern1and2"

    CAPTURE_TRIGGER_CMD = "capture_trigger"

    CAPTURE_TRIGGER_DA_CMD = "capture_trigger_DA"
    # Constant values for CAPTURE_TRIGGER_DA_CMD
    CAPTURE_TRIGGER_DA_ANY = "any"
    CAPTURE_TRIGGER_DA_DA1 = "DA1"
    CAPTURE_TRIGGER_DA_NOTDA1 = "notDA1"
    CAPTURE_TRIGGER_DA_DA2 = "DA2"
    CAPTURE_TRIGGER_DA_NOTDA2 = "notDA2"

    CAPTURE_TRIGGER_SA_CMD = "capture_trigger_SA"
    # Constant values for CAPTURE_TRIGGER_SA_CMD
    CAPTURE_TRIGGER_SA_ANY = "any"
    CAPTURE_TRIGGER_SA_SA1 = "SA1"
    CAPTURE_TRIGGER_SA_NOTSA1 = "notSA1"
    CAPTURE_TRIGGER_SA_SA2 = "SA2"
    CAPTURE_TRIGGER_SA_NOTSA2 = "notSA2"

    CAPTURE_TRIGGER_ERROR_CMD = "capture_trigger_error"

    CAPTURE_TRIGGER_EXPRESSION_STRING_CMD = "capture_trigger_expression_string"

    CAPTURE_TRIGGER_FRAMESIZE_CMD = "capture_trigger_framesize"
    # Constant values for CAPTURE_TRIGGER_FRAMESIZE_CMD
    CAPTURE_TRIGGER_FRAMESIZE_0 = "0"
    CAPTURE_TRIGGER_FRAMESIZE_1 = "1"
    CAPTURE_TRIGGER_FRAMESIZE_JUMBO = "jumbo"
    CAPTURE_TRIGGER_FRAMESIZE_OVERSIZED = "oversized"
    CAPTURE_TRIGGER_FRAMESIZE_UNDERSIZED = "undersized"

    CAPTURE_TRIGGER_FRAMESIZE_FROM_CMD = "capture_trigger_framesize_from"

    CAPTURE_TRIGGER_FRAMESIZE_TO_CMD = "capture_trigger_framesize_to"

    CAPTURE_TRIGGER_PATTERN_CMD = "capture_trigger_pattern"
    # Constant values for CAPTURE_TRIGGER_PATTERN_CMD
    CAPTURE_TRIGGER_PATTERN_ANY = "any"
    CAPTURE_TRIGGER_PATTERN_PATTERN1 = "pattern1"
    CAPTURE_TRIGGER_PATTERN_NOTPATTERN1 = "notPattern1"
    CAPTURE_TRIGGER_PATTERN_PATTERN2 = "pattern2"
    CAPTURE_TRIGGER_PATTERN_NOTPATTERN2 = "notPattern2"
    CAPTURE_TRIGGER_PATTERN_PATTERN1AND2 = "pattern1and2"

    HANDLE_CMD = "handle"

    MODE_CMD = "mode"
    # Constant values for MODE_CMD
    MODE_CREATE = "create"
    MODE_ADDATMTRIGGER = "addAtmTrigger"

    PORT_HANDLE_CMD = "port_handle"

    UDS1_CMD = "uds1"

    UDS1_DA_CMD = "uds1_DA"
    # Constant values for UDS1_DA_CMD
    UDS1_DA_ANY = "any"
    UDS1_DA_DA1 = "DA1"
    UDS1_DA_NOTDA1 = "notDA1"
    UDS1_DA_DA2 = "DA2"
    UDS1_DA_NOTDA2 = "notDA2"

    UDS1_SA_CMD = "uds1_SA"
    # Constant values for UDS1_SA_CMD
    UDS1_SA_ANY = "any"
    UDS1_SA_SA1 = "SA1"
    UDS1_SA_NOTSA1 = "notSA1"
    UDS1_SA_SA2 = "SA2"
    UDS1_SA_NOTSA2 = "notSA2"

    UDS1_ERROR_CMD = "uds1_error"

    UDS1_FRAMESIZE_CMD = "uds1_framesize"
    # Constant values for UDS1_FRAMESIZE_CMD
    UDS1_FRAMESIZE_0 = "0"
    UDS1_FRAMESIZE_1 = "1"
    UDS1_FRAMESIZE_JUMBO = "jumbo"
    UDS1_FRAMESIZE_OVERSIZED = "oversized"
    UDS1_FRAMESIZE_UNDERSIZED = "undersized"

    UDS1_FRAMESIZE_FROM_CMD = "uds1_framesize_from"

    UDS1_FRAMESIZE_TO_CMD = "uds1_framesize_to"

    UDS1_PATTERN_CMD = "uds1_pattern"
    # Constant values for UDS1_PATTERN_CMD
    UDS1_PATTERN_ANY = "any"
    UDS1_PATTERN_PATTERN1 = "pattern1"
    UDS1_PATTERN_NOTPATTERN1 = "notPattern1"
    UDS1_PATTERN_PATTERN2 = "pattern2"
    UDS1_PATTERN_NOTPATTERN2 = "notPattern2"
    UDS1_PATTERN_PATTERN1AND2 = "pattern1and2"

    UDS2_CMD = "uds2"

    UDS2_DA_CMD = "uds2_DA"
    # Constant values for UDS2_DA_CMD
    UDS2_DA_ANY = "any"
    UDS2_DA_DA1 = "DA1"
    UDS2_DA_NOTDA1 = "notDA1"
    UDS2_DA_DA2 = "DA2"
    UDS2_DA_NOTDA2 = "notDA2"

    UDS2_SA_CMD = "uds2_SA"
    # Constant values for UDS2_SA_CMD
    UDS2_SA_ANY = "any"
    UDS2_SA_SA1 = "SA1"
    UDS2_SA_NOTSA1 = "notSA1"
    UDS2_SA_SA2 = "SA2"
    UDS2_SA_NOTSA2 = "notSA2"

    UDS2_ERROR_CMD = "uds2_error"

    UDS2_FRAMESIZE_CMD = "uds2_framesize"
    # Constant values for UDS2_FRAMESIZE_CMD
    UDS2_FRAMESIZE_0 = "0"
    UDS2_FRAMESIZE_1 = "1"
    UDS2_FRAMESIZE_JUMBO = "jumbo"
    UDS2_FRAMESIZE_OVERSIZED = "oversized"
    UDS2_FRAMESIZE_UNDERSIZED = "undersized"

    UDS2_FRAMESIZE_FROM_CMD = "uds2_framesize_from"

    UDS2_FRAMESIZE_TO_CMD = "uds2_framesize_to"

    UDS2_PATTERN_CMD = "uds2_pattern"
    # Constant values for UDS2_PATTERN_CMD
    UDS2_PATTERN_ANY = "any"
    UDS2_PATTERN_PATTERN1 = "pattern1"
    UDS2_PATTERN_NOTPATTERN1 = "notPattern1"
    UDS2_PATTERN_PATTERN2 = "pattern2"
    UDS2_PATTERN_NOTPATTERN2 = "notPattern2"
    UDS2_PATTERN_PATTERN1AND2 = "pattern1and2"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass

"""
Implemented Commands (Alphabetical)
    -async_trigger1
    -async_trigger1_DA
    -async_trigger1_SA
    -async_trigger1_error
    -async_trigger1_framesize
    -async_trigger1_framesize_from
    -async_trigger1_framesize_to
    -async_trigger1_pattern
    -async_trigger2
    -async_trigger2_DA
    -async_trigger2_SA
    -async_trigger2_error
    -async_trigger2_framesize
    -async_trigger2_framesize_from
    -async_trigger2_framesize_to
    -async_trigger2_pattern
    -capture_filter
    -capture_filter_DA
    -capture_filter_SA
    -capture_filter_error
    -capture_filter_expression_string
    -capture_filter_framesize
    -capture_filter_framesize_from
    -capture_filter_framesize_to
    -capture_filter_pattern
    -capture_trigger
    -capture_trigger_DA
    -capture_trigger_SA
    -capture_trigger_error
    -capture_trigger_expression_string
    -capture_trigger_framesize
    -capture_trigger_framesize_from
    -capture_trigger_framesize_to
    -capture_trigger_pattern
    -handle
    -mode
    -port_handle
    -uds1
    -uds1_DA
    -uds1_SA
    -uds1_error
    -uds1_framesize
    -uds1_framesize_from
    -uds1_framesize_to
    -uds1_pattern
    -uds2
    -uds2_DA
    -uds2_SA
    -uds2_error
    -uds2_framesize
    -uds2_framesize_from
    -uds2_framesize_to
    -uds2_pattern
If you want to update this file, look in the CSV
"""
