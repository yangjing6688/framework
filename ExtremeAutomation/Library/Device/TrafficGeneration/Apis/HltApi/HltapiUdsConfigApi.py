from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.TrafficGenerationApi import TrafficGenerationApi
from ExtremeAutomation.Library.Utils.Singleton import Singleton

"""
    This is the API class for the command: uds_config

    Class is auto-generated. If you update anything here,
        it will be over written.
"""


class UdsConfigApi(TrafficGenerationApi):

    """
    init function
    """
    def __init__(self, device):
        super(UdsConfigApi, self).__init__(device)

    """
    This is the "One Large Method" for the command: uds_config
    use this by passing in a dict() of all the commands
        dummyDict = dict()
        dummyDict[UdsConfigConstants.PORT_HANDLE_CMD] = "dummyValue1" # static value
        dummyDict[UdsConfigConstants.UDS1_CMD] = "dummyValue2" # static value
        dummyDict[UdsConfigConstants.UDS1_DA_CMD] = UdsConfigConstants.UDS1_DA_DA1 # constant value
        dummyDict[UdsConfigConstants.UDS1_SA_CMD] = UdsConfigConstants.UDS1_SA_SA1 # constant value
        dummyDict[UdsConfigConstants.UDS1_ERROR_CMD] = UdsConfigConstants.UDS1_ERROR_ERRANYFRAME # constant value
        dummyDict[UdsConfigConstants.UDS1_FRAMESIZE_CMD] = "dummyValue6" # static value
        dummyDict[UdsConfigConstants.UDS1_FRAMESIZE_FROM_CMD] = "dummyValue7" # static value
        dummyDict[UdsConfigConstants.UDS1_FRAMESIZE_TO_CMD] = "dummyValue8" # static value
        dummyDict[UdsConfigConstants.UDS1_PATTERN_CMD] = UdsConfigConstants.UDS1_PATTERN_ANY # constant value
        dummyDict[UdsConfigConstants.UDS2_CMD] = "dummyValue10" # static value
        dummyDict[UdsConfigConstants.UDS2_DA_CMD] = UdsConfigConstants.UDS2_DA_DA1 # constant value
        dummyDict[UdsConfigConstants.UDS2_SA_CMD] = UdsConfigConstants.UDS2_SA_SA1 # constant value
        dummyDict[UdsConfigConstants.UDS2_ERROR_CMD] = UdsConfigConstants.UDS2_ERROR_ERRANYFRAME # constant value
        dummyDict[UdsConfigConstants.UDS2_FRAMESIZE_CMD] = "dummyValue14" # static value
        dummyDict[UdsConfigConstants.UDS2_FRAMESIZE_FROM_CMD] = "dummyValue15" # static value
        dummyDict[UdsConfigConstants.UDS2_FRAMESIZE_TO_CMD] = "dummyValue16" # static value
        dummyDict[UdsConfigConstants.UDS2_PATTERN_CMD] = UdsConfigConstants.UDS2_PATTERN_ANY # constant value
        dummyDict[UdsConfigConstants.UDS3_CMD] = "dummyValue18" # static value
        dummyDict[UdsConfigConstants.UDS3_DA_CMD] = UdsConfigConstants.UDS3_DA_DA1 # constant value
        dummyDict[UdsConfigConstants.UDS3_SA_CMD] = UdsConfigConstants.UDS3_SA_SA1 # constant value
        dummyDict[UdsConfigConstants.UDS3_ERROR_CMD] = UdsConfigConstants.UDS3_ERROR_ERRANYFRAME # constant value
        dummyDict[UdsConfigConstants.UDS3_FRAMESIZE_CMD] = "dummyValue22" # static value
        dummyDict[UdsConfigConstants.UDS3_FRAMESIZE_FROM_CMD] = "dummyValue23" # static value
        dummyDict[UdsConfigConstants.UDS3_FRAMESIZE_TO_CMD] = "dummyValue24" # static value
        dummyDict[UdsConfigConstants.UDS3_PATTERN_CMD] = UdsConfigConstants.UDS3_PATTERN_ANY # constant value
        dummyDict[UdsConfigConstants.UDS4_CMD] = "dummyValue26" # static value
        dummyDict[UdsConfigConstants.UDS4_DA_CMD] = UdsConfigConstants.UDS4_DA_DA1 # constant value
        dummyDict[UdsConfigConstants.UDS4_SA_CMD] = UdsConfigConstants.UDS4_SA_SA1 # constant value
        dummyDict[UdsConfigConstants.UDS4_ERROR_CMD] = UdsConfigConstants.UDS4_ERROR_ERRANYFRAME # constant value
        dummyDict[UdsConfigConstants.UDS4_FRAMESIZE_CMD] = "dummyValue30" # static value
        dummyDict[UdsConfigConstants.UDS4_FRAMESIZE_FROM_CMD] = "dummyValue31" # static value
        dummyDict[UdsConfigConstants.UDS4_FRAMESIZE_TO_CMD] = "dummyValue32" # static value
        dummyDict[UdsConfigConstants.UDS4_PATTERN_CMD] = UdsConfigConstants.UDS4_PATTERN_ANY # constant value
        dummyDict[UdsConfigConstants.UDS5_CMD] = "dummyValue34" # static value
        dummyDict[UdsConfigConstants.UDS5_DA_CMD] = UdsConfigConstants.UDS5_DA_DA1 # constant value
        dummyDict[UdsConfigConstants.UDS5_SA_CMD] = UdsConfigConstants.UDS5_SA_SA1 # constant value
        dummyDict[UdsConfigConstants.UDS5_ERROR_CMD] = UdsConfigConstants.UDS5_ERROR_ERRANYFRAME # constant value
        dummyDict[UdsConfigConstants.UDS5_FRAMESIZE_CMD] = "dummyValue38" # static value
        dummyDict[UdsConfigConstants.UDS5_FRAMESIZE_FROM_CMD] = "dummyValue39" # static value
        dummyDict[UdsConfigConstants.UDS5_FRAMESIZE_TO_CMD] = "dummyValue40" # static value
        dummyDict[UdsConfigConstants.UDS5_PATTERN_CMD] = UdsConfigConstants.UDS5_PATTERN_ANY # constant value
        dummyDict[UdsConfigConstants.UDS6_CMD] = "dummyValue42" # static value
        dummyDict[UdsConfigConstants.UDS6_DA_CMD] = UdsConfigConstants.UDS6_DA_DA1 # constant value
        dummyDict[UdsConfigConstants.UDS6_SA_CMD] = UdsConfigConstants.UDS6_SA_SA1 # constant value
        dummyDict[UdsConfigConstants.UDS6_ERROR_CMD] = UdsConfigConstants.UDS6_ERROR_ERRANYFRAME # constant value
        dummyDict[UdsConfigConstants.UDS6_FRAMESIZE_CMD] = "dummyValue46" # static value
        dummyDict[UdsConfigConstants.UDS6_FRAMESIZE_FROM_CMD] = "dummyValue47" # static value
        dummyDict[UdsConfigConstants.UDS6_FRAMESIZE_TO_CMD] = "dummyValue48" # static value
        dummyDict[UdsConfigConstants.UDS6_PATTERN_CMD] = UdsConfigConstants.UDS6_PATTERN_ANY # constant value

        api = device.getApi(UdsConfigConstants.UDS_CONFIG_API)
        api.uds_config(dummyDict)
    """
    def uds_config(self, argdictionary, supported = None):
        self.process_supported_hltapi_commands(argdictionary, supported)
        return self.send_command_args(self._nameSpace +"::uds_config", argdictionary)

    """
    Individual commands for each option. Typically, the "One Large Method"
    is the one that you want to be using so look at that example above
    """
    def uds_config_port_handle(self, any):
        """
        This is the method the command: uds_config option port_handle
        Description:Port handle or list of port handles on which to configure the user
            defined statistic counters.
            DEFAULT
                None
        Constants Available: PORT_HANDLE_CMD
        Supported:IxNetwork[M]
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.uds_config({UdsConfigConstants.PORT_HANDLE_CMD : any})

    def uds_config_uds1(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def uds_config_uds1_DA(self, opt):
        return self.logger.log_unimplemented_method()

    def uds_config_uds1_SA(self, opt):
        return self.logger.log_unimplemented_method()

    def uds_config_uds1_error(self, opt):
        return self.logger.log_unimplemented_method()

    def uds_config_uds1_framesize(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def uds_config_uds1_framesize_from(self, numeric):
        return self.logger.log_unimplemented_method()

    def uds_config_uds1_framesize_to(self, numeric):
        return self.logger.log_unimplemented_method()

    def uds_config_uds1_pattern(self, opt):
        return self.logger.log_unimplemented_method()

    def uds_config_uds2(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def uds_config_uds2_DA(self, opt):
        return self.logger.log_unimplemented_method()

    def uds_config_uds2_SA(self, opt):
        return self.logger.log_unimplemented_method()

    def uds_config_uds2_error(self, opt):
        return self.logger.log_unimplemented_method()

    def uds_config_uds2_framesize(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def uds_config_uds2_framesize_from(self, numeric):
        return self.logger.log_unimplemented_method()

    def uds_config_uds2_framesize_to(self, numeric):
        return self.logger.log_unimplemented_method()

    def uds_config_uds2_pattern(self, opt):
        return self.logger.log_unimplemented_method()

    def uds_config_uds3(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def uds_config_uds3_DA(self, opt):
        return self.logger.log_unimplemented_method()

    def uds_config_uds3_SA(self, opt):
        return self.logger.log_unimplemented_method()

    def uds_config_uds3_error(self, opt):
        return self.logger.log_unimplemented_method()

    def uds_config_uds3_framesize(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def uds_config_uds3_framesize_from(self, numeric):
        return self.logger.log_unimplemented_method()

    def uds_config_uds3_framesize_to(self, numeric):
        return self.logger.log_unimplemented_method()

    def uds_config_uds3_pattern(self, opt):
        return self.logger.log_unimplemented_method()

    def uds_config_uds4(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def uds_config_uds4_DA(self, opt):
        return self.logger.log_unimplemented_method()

    def uds_config_uds4_SA(self, opt):
        return self.logger.log_unimplemented_method()

    def uds_config_uds4_error(self, opt):
        return self.logger.log_unimplemented_method()

    def uds_config_uds4_framesize(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def uds_config_uds4_framesize_from(self, numeric):
        return self.logger.log_unimplemented_method()

    def uds_config_uds4_framesize_to(self, numeric):
        return self.logger.log_unimplemented_method()

    def uds_config_uds4_pattern(self, opt):
        return self.logger.log_unimplemented_method()

    def uds_config_uds5(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def uds_config_uds5_DA(self, opt):
        return self.logger.log_unimplemented_method()

    def uds_config_uds5_SA(self, opt):
        return self.logger.log_unimplemented_method()

    def uds_config_uds5_error(self, opt):
        return self.logger.log_unimplemented_method()

    def uds_config_uds5_framesize(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def uds_config_uds5_framesize_from(self, numeric):
        return self.logger.log_unimplemented_method()

    def uds_config_uds5_framesize_to(self, numeric):
        return self.logger.log_unimplemented_method()

    def uds_config_uds5_pattern(self, opt):
        return self.logger.log_unimplemented_method()

    def uds_config_uds6(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def uds_config_uds6_DA(self, opt):
        return self.logger.log_unimplemented_method()

    def uds_config_uds6_SA(self, opt):
        return self.logger.log_unimplemented_method()

    def uds_config_uds6_error(self, opt):
        return self.logger.log_unimplemented_method()

    def uds_config_uds6_framesize(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def uds_config_uds6_framesize_from(self, numeric):
        return self.logger.log_unimplemented_method()

    def uds_config_uds6_framesize_to(self, numeric):
        return self.logger.log_unimplemented_method()

    def uds_config_uds6_pattern(self, opt):
        return self.logger.log_unimplemented_method()


"""
    This is the Constants class for the command: uds_config
    Commands end with _CMD and constants for a command start with the beginning
    with the command's constant name minus the _CMD
"""


class UdsConfigConstants(object, metaclass=Singleton):
    # api reference constant for this api to get it from the device
    UDS_CONFIG_API = "UDS_CONFIG_API"

    PORT_HANDLE_CMD = "port_handle"

    UDS1_CMD = "uds1"

    UDS1_DA_CMD = "uds1_DA"
    # Constant values for UDS1_DA_CMD
    UDS1_DA_DA1 = "DA1"
    UDS1_DA_DA2 = "DA2"
    UDS1_DA_ANY = "any"
    UDS1_DA_NOTDA1 = "notDA1"
    UDS1_DA_NOTDA2 = "notDA2"

    UDS1_SA_CMD = "uds1_SA"
    # Constant values for UDS1_SA_CMD
    UDS1_SA_SA1 = "SA1"
    UDS1_SA_SA2 = "SA2"
    UDS1_SA_ANY = "any"
    UDS1_SA_NOTSA1 = "notSA1"
    UDS1_SA_NOTSA2 = "notSA2"

    UDS1_ERROR_CMD = "uds1_error"
    # Constant values for UDS1_ERROR_CMD
    UDS1_ERROR_ERRANYFRAME = "errAnyFrame"

    UDS1_FRAMESIZE_CMD = "uds1_framesize"

    UDS1_FRAMESIZE_FROM_CMD = "uds1_framesize_from"

    UDS1_FRAMESIZE_TO_CMD = "uds1_framesize_to"

    UDS1_PATTERN_CMD = "uds1_pattern"
    # Constant values for UDS1_PATTERN_CMD
    UDS1_PATTERN_ANY = "any"
    UDS1_PATTERN_NOTPATTERN1 = "notPattern1"
    UDS1_PATTERN_PATTERN1 = "pattern1"

    UDS2_CMD = "uds2"

    UDS2_DA_CMD = "uds2_DA"
    # Constant values for UDS2_DA_CMD
    UDS2_DA_DA1 = "DA1"
    UDS2_DA_DA2 = "DA2"
    UDS2_DA_ANY = "any"
    UDS2_DA_NOTDA1 = "notDA1"
    UDS2_DA_NOTDA2 = "notDA2"

    UDS2_SA_CMD = "uds2_SA"
    # Constant values for UDS2_SA_CMD
    UDS2_SA_SA1 = "SA1"
    UDS2_SA_SA2 = "SA2"
    UDS2_SA_ANY = "any"
    UDS2_SA_NOTSA1 = "notSA1"
    UDS2_SA_NOTSA2 = "notSA2"

    UDS2_ERROR_CMD = "uds2_error"
    # Constant values for UDS2_ERROR_CMD
    UDS2_ERROR_ERRANYFRAME = "errAnyFrame"

    UDS2_FRAMESIZE_CMD = "uds2_framesize"

    UDS2_FRAMESIZE_FROM_CMD = "uds2_framesize_from"

    UDS2_FRAMESIZE_TO_CMD = "uds2_framesize_to"

    UDS2_PATTERN_CMD = "uds2_pattern"
    # Constant values for UDS2_PATTERN_CMD
    UDS2_PATTERN_ANY = "any"
    UDS2_PATTERN_NOTPATTERN1 = "notPattern1"
    UDS2_PATTERN_PATTERN1 = "pattern1"

    UDS3_CMD = "uds3"

    UDS3_DA_CMD = "uds3_DA"
    # Constant values for UDS3_DA_CMD
    UDS3_DA_DA1 = "DA1"
    UDS3_DA_DA2 = "DA2"
    UDS3_DA_ANY = "any"
    UDS3_DA_NOTDA1 = "notDA1"
    UDS3_DA_NOTDA2 = "notDA2"

    UDS3_SA_CMD = "uds3_SA"
    # Constant values for UDS3_SA_CMD
    UDS3_SA_SA1 = "SA1"
    UDS3_SA_SA2 = "SA2"
    UDS3_SA_ANY = "any"
    UDS3_SA_NOTSA1 = "notSA1"
    UDS3_SA_NOTSA2 = "notSA2"

    UDS3_ERROR_CMD = "uds3_error"
    # Constant values for UDS3_ERROR_CMD
    UDS3_ERROR_ERRANYFRAME = "errAnyFrame"

    UDS3_FRAMESIZE_CMD = "uds3_framesize"

    UDS3_FRAMESIZE_FROM_CMD = "uds3_framesize_from"

    UDS3_FRAMESIZE_TO_CMD = "uds3_framesize_to"

    UDS3_PATTERN_CMD = "uds3_pattern"
    # Constant values for UDS3_PATTERN_CMD
    UDS3_PATTERN_ANY = "any"
    UDS3_PATTERN_NOTPATTERN1 = "notPattern1"
    UDS3_PATTERN_PATTERN1 = "pattern1"

    UDS4_CMD = "uds4"

    UDS4_DA_CMD = "uds4_DA"
    # Constant values for UDS4_DA_CMD
    UDS4_DA_DA1 = "DA1"
    UDS4_DA_DA2 = "DA2"
    UDS4_DA_ANY = "any"
    UDS4_DA_NOTDA1 = "notDA1"
    UDS4_DA_NOTDA2 = "notDA2"

    UDS4_SA_CMD = "uds4_SA"
    # Constant values for UDS4_SA_CMD
    UDS4_SA_SA1 = "SA1"
    UDS4_SA_SA2 = "SA2"
    UDS4_SA_ANY = "any"
    UDS4_SA_NOTSA1 = "notSA1"
    UDS4_SA_NOTSA2 = "notSA2"

    UDS4_ERROR_CMD = "uds4_error"
    # Constant values for UDS4_ERROR_CMD
    UDS4_ERROR_ERRANYFRAME = "errAnyFrame"

    UDS4_FRAMESIZE_CMD = "uds4_framesize"

    UDS4_FRAMESIZE_FROM_CMD = "uds4_framesize_from"

    UDS4_FRAMESIZE_TO_CMD = "uds4_framesize_to"

    UDS4_PATTERN_CMD = "uds4_pattern"
    # Constant values for UDS4_PATTERN_CMD
    UDS4_PATTERN_ANY = "any"
    UDS4_PATTERN_NOTPATTERN1 = "notPattern1"
    UDS4_PATTERN_PATTERN1 = "pattern1"

    UDS5_CMD = "uds5"

    UDS5_DA_CMD = "uds5_DA"
    # Constant values for UDS5_DA_CMD
    UDS5_DA_DA1 = "DA1"
    UDS5_DA_DA2 = "DA2"
    UDS5_DA_ANY = "any"
    UDS5_DA_NOTDA1 = "notDA1"
    UDS5_DA_NOTDA2 = "notDA2"

    UDS5_SA_CMD = "uds5_SA"
    # Constant values for UDS5_SA_CMD
    UDS5_SA_SA1 = "SA1"
    UDS5_SA_SA2 = "SA2"
    UDS5_SA_ANY = "any"
    UDS5_SA_NOTSA1 = "notSA1"
    UDS5_SA_NOTSA2 = "notSA2"

    UDS5_ERROR_CMD = "uds5_error"
    # Constant values for UDS5_ERROR_CMD
    UDS5_ERROR_ERRANYFRAME = "errAnyFrame"

    UDS5_FRAMESIZE_CMD = "uds5_framesize"

    UDS5_FRAMESIZE_FROM_CMD = "uds5_framesize_from"

    UDS5_FRAMESIZE_TO_CMD = "uds5_framesize_to"

    UDS5_PATTERN_CMD = "uds5_pattern"
    # Constant values for UDS5_PATTERN_CMD
    UDS5_PATTERN_ANY = "any"
    UDS5_PATTERN_NOTPATTERN1 = "notPattern1"
    UDS5_PATTERN_PATTERN1 = "pattern1"

    UDS6_CMD = "uds6"

    UDS6_DA_CMD = "uds6_DA"
    # Constant values for UDS6_DA_CMD
    UDS6_DA_DA1 = "DA1"
    UDS6_DA_DA2 = "DA2"
    UDS6_DA_ANY = "any"
    UDS6_DA_NOTDA1 = "notDA1"
    UDS6_DA_NOTDA2 = "notDA2"

    UDS6_SA_CMD = "uds6_SA"
    # Constant values for UDS6_SA_CMD
    UDS6_SA_SA1 = "SA1"
    UDS6_SA_SA2 = "SA2"
    UDS6_SA_ANY = "any"
    UDS6_SA_NOTSA1 = "notSA1"
    UDS6_SA_NOTSA2 = "notSA2"

    UDS6_ERROR_CMD = "uds6_error"
    # Constant values for UDS6_ERROR_CMD
    UDS6_ERROR_ERRANYFRAME = "errAnyFrame"

    UDS6_FRAMESIZE_CMD = "uds6_framesize"

    UDS6_FRAMESIZE_FROM_CMD = "uds6_framesize_from"

    UDS6_FRAMESIZE_TO_CMD = "uds6_framesize_to"

    UDS6_PATTERN_CMD = "uds6_pattern"
    # Constant values for UDS6_PATTERN_CMD
    UDS6_PATTERN_ANY = "any"
    UDS6_PATTERN_NOTPATTERN1 = "notPattern1"
    UDS6_PATTERN_PATTERN1 = "pattern1"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass

"""
Implemented Commands (Alphabetical)
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
    -uds3
    -uds3_DA
    -uds3_SA
    -uds3_error
    -uds3_framesize
    -uds3_framesize_from
    -uds3_framesize_to
    -uds3_pattern
    -uds4
    -uds4_DA
    -uds4_SA
    -uds4_error
    -uds4_framesize
    -uds4_framesize_from
    -uds4_framesize_to
    -uds4_pattern
    -uds5
    -uds5_DA
    -uds5_SA
    -uds5_error
    -uds5_framesize
    -uds5_framesize_from
    -uds5_framesize_to
    -uds5_pattern
    -uds6
    -uds6_DA
    -uds6_SA
    -uds6_error
    -uds6_framesize
    -uds6_framesize_from
    -uds6_framesize_to
    -uds6_pattern
If you want to update this file, look in the CSV
"""
