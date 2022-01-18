# pip install pysnmp
from pysnmp import hlapi
from ExtremeAutomation.Library.Logger.Logger import Logger
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils
from ExtremeAutomation.Library.Utils.Constants.Constants import Constants
from ExtremeAutomation.Library.Device.Common.Agents.LoginManagementAgent import LoginManagementAgent
from ExtremeAutomation.Library.Device.Common.CommandObjects.SnmpCommandObject import SnmpCommandObject


class SnmpAgent(LoginManagementAgent):
    def __init__(self, device):
        super(SnmpAgent, self).__init__(device)
        self.COMMAND_LOGGER = Logger()
        self.connection = None
        self.device = device
        self.type = self.constants.TYPE_SNMP
        self.community_name = None
        self.user_name = None
        self.auth_password = None
        self.privacy_password = None
        self.security_model = None
        self.snmp_constants = SnmpConstants()

        # Attributes with setter/getter functions.
        self._snmp_version = None
        self._auth_protocol = None
        self._privacy_protocol = None

        self.parse_agent_kwargs()

    def parse_agent_kwargs(self):
        """
        This function parses self.device.agent_kwargs and looks for the following values.

         - snmp_version
         - snmp_community_name
         - snmp_user_name
         - snmp_auth_protocol
         - snmp_auth_password
         - snmp_privacy_protocol
         - snmp_privacy_password

        For each key that is present it's value is set to the corresponding attribute.
        """
        if "snmp_version" in self.device.agent_kwargs:
            self.snmp_version = self.device.agent_kwargs["snmp_version"]
        if "snmp_community_name" in self.device.agent_kwargs:
            self.community_name = self.device.agent_kwargs["snmp_community_name"]
        if "snmp_user_name" in self.device.agent_kwargs:
            self.user_name = self.device.agent_kwargs["snmp_user_name"]
        if "snmp_auth_protocol" in self.device.agent_kwargs:
            self.auth_protocol = self.device.agent_kwargs["snmp_auth_protocol"]
        if "snmp_auth_password" in self.device.agent_kwargs:
            self.auth_password = self.device.agent_kwargs["snmp_auth_password"]
        if "snmp_privacy_protocol" in self.device.agent_kwargs:
            self.privacy_protocol = self.device.agent_kwargs["snmp_privacy_protocol"]
        if "snmp_privacy_password" in self.device.agent_kwargs:
            self.privacy_password = self.device.agent_kwargs["snmp_privacy_password"]

    @property
    def snmp_version(self):
        """
        SNMP version property function, returns the private _snmp_version value.
        """
        return self._snmp_version

    @snmp_version.setter
    def snmp_version(self, snmp_version):
        """
        Function Args:
        [snmp_version] - The version of snmp that should be set to self._snmp_version.

        This function will check the passed SNMP version against a list of known versions. If one matches
        it will set self._snmp_version to the appropriate constant. It will also set the security model.
        If the version does not match a ValueError will be raised.
        """
        if snmp_version.lower() in ["1", "v1", self.snmp_constants.SNMP_VER_1]:
            self._snmp_version = self.snmp_constants.SNMP_VER_1
            self.security_model = self.snmp_constants.SECURITY_MODEL_COMMUNITY
        elif snmp_version.lower() in ["2", "2c", "v2", "v2c", self.snmp_constants.SNMP_VER_2]:
            self._snmp_version = self.snmp_constants.SNMP_VER_2
            self.security_model = self.snmp_constants.SECURITY_MODEL_COMMUNITY
        elif snmp_version.lower() in ["3", "v3", SnmpConstants.SNMP_VER_3]:
            self._snmp_version = self.snmp_constants.SNMP_VER_3
            self.security_model = self.snmp_constants.SECURITY_MODEL_USER
        else:
            raise ValueError(snmp_version + " is not a valid SNMP version.")

    @property
    def auth_protocol(self):
        """
        SNMP auth protocol property function, returns the private _auth_protocol value.
        """
        return self._auth_protocol

    @auth_protocol.setter
    def auth_protocol(self, auth_proto):
        """
        Function Args:
        [auth_proto] - The authentication protocol that should be set to self._auth_protocol.

        If the passed authentication protocol is not None it will check it against the known constants. If it matches
        the appropriate constant will be set to self._auth_protocol. If no match is found a ValueError will be raised.
        """
        if auth_proto:
            if auth_proto.lower() == self.snmp_constants.SNMP_AUTH_NO_AUTH:
                self._auth_protocol = hlapi.usmNoAuthProtocol
            elif auth_proto.lower() == self.snmp_constants.SNMP_AUTH_MD5:
                self._auth_protocol = hlapi.usmHMACMD5AuthProtocol
            elif auth_proto.lower() == self.snmp_constants.SNMP_AUTH_SHA:
                self._auth_protocol = hlapi.usmHMACSHAAuthProtocol
            else:
                raise ValueError(auth_proto + " is not a valid authentication protocol.")

    @property
    def privacy_protocol(self):
        """
        SNMP privacy protocol property function, returns the private _privacy_protocol value.
        """
        return self._privacy_protocol

    @privacy_protocol.setter
    def privacy_protocol(self, priv_proto):
        """
        Function Args:
        [priv_protocol] - The privacy protocol that should be set to self._privacy_protocol.

        This function will check the passed privacy protocol agains the known constants. If a match is found
        the appropriate constant will be set. Otherwise a ValueError will be raised.
        """
        if priv_proto:
            if priv_proto.lower() == self.snmp_constants.SNMP_PRIV_NO_PRIV:
                self._privacy_protocol = hlapi.usmNoPrivProtocol
            elif priv_proto.lower() == self.snmp_constants.SNMP_PRIV_DES:
                self._privacy_protocol = hlapi.usmDESPrivProtocol
            elif priv_proto.lower() == self.snmp_constants.SNMP_PRIV_3DES:
                self._privacy_protocol = hlapi.usm3DESEDEPrivProtocol
            elif priv_proto.lower() == self.snmp_constants.SNMP_PRIV_AES128:
                self._privacy_protocol = hlapi.usmAesCfb128Protocol
            elif priv_proto.lower() == self.snmp_constants.SNMP_PRIV_AES192:
                self._privacy_protocol = hlapi.usmAesCfb192Protocol
            elif priv_proto.lower() == self.snmp_constants.SNMP_PRIV_AES256:
                self._privacy_protocol = hlapi.usmAesCfb256Protocol
            else:
                raise ValueError(priv_proto + " is not a valid privacy protocol.")

    def send_command_object(self, snmp_cmd_obj, **kwargs):
        """
        Function Args:
        [snmp_cmd_obj] - The command object that should be sent to the device.

        Sends the passed SNMP command object to the device.
        """
        log = StringUtils.string_to_boolean(kwargs.get("log", True))

        if not self.logged_in:
            self.login()

        result = SnmpCommandObject()
        result.value = snmp_cmd_obj.value
        result.command_type = self.get_command_type(snmp_cmd_obj.command_type)
        result.oid = snmp_cmd_obj.oid.split("||")
        result.data_type = []

        if snmp_cmd_obj.value is not None:
            result.data_type = [self.get_data_type(i) for i in snmp_cmd_obj.data_type.split("||")]

        if len(result.oid) == 0:
            raise ValueError("No OID provided.")

        if snmp_cmd_obj.value is not None:
            result.value = snmp_cmd_obj.value.split("||")
        else:
            result.value = ["1"] * len(result.oid)

        if len(result.data_type) == 0:
            if snmp_cmd_obj.value is not None:
                raise ValueError("No data type provided for value.")
            else:
                result.data_type = [None] * len(result.oid)

        if len(result.oid) != len(result.value):
            raise ValueError("One value must be provided for each OID!")

        if len(result.oid) != len(result.data_type):
            if len(result.data_type) == 1:
                result.data_type = [self.get_data_type(i) for i in (result.data_type * len(result.oid))]
            else:
                raise ValueError("One data type must be provided for each value. If all values are the same data"
                                 "type only one data type needs to be passed")

        if snmp_cmd_obj.command_type in [self.snmp_constants.SNMP_GET_CMD, self.snmp_constants.SNMP_GET_NEXT_CMD]:
            self.snmp_get(result)
        elif snmp_cmd_obj.command_type == self.snmp_constants.SNMP_SET_CMD:
            self.snmp_set(result)
        elif snmp_cmd_obj.command_type == self.snmp_constants.SNMP_WALK_CMD:
            self.snmp_walk(result)
        elif snmp_cmd_obj.command_type == self.snmp_constants.SNMP_BULK_WALK_CMD:
            self.snmp_bulk_walk(result)
        else:
            raise ValueError("Invalid snmp command.")

        if result.return_text is None:
            result.return_text = "NO_DATA"
        else:
            result.return_text = "\r\n".join([" " * 10 + s if i != 0 else s for i, s in enumerate(result.return_text)])

        if log:
            if snmp_cmd_obj.command_type is not None:
                oid_string = "\r\n".join([" " * 8 + s if i != 0 else s for i, s in enumerate(result.oid)])

                log_message = ["Sent the following Request(s)...",
                               "Message Type: " + snmp_cmd_obj.command_type.upper(),
                               "OID(s): " + oid_string,
                               "Response: " + result.return_text]

                self.logger.log_info("\n".join(log_message) + "\n")

        return result

    def get_command_type(self, command_type):
        """
        Function Args:
        [command_type] - The command type found in the command object.

        Checks to make sure the command type passed by the command object is valid. If it is the appriopriate command
        is returned. Otherwise a ValueError is returned.
        """
        if command_type.lower() == self.snmp_constants.SNMP_GET_CMD:
            return hlapi.getCmd
        elif command_type.lower() == self.snmp_constants.SNMP_SET_CMD:
            return hlapi.setCmd
        elif command_type.lower() == self.snmp_constants.SNMP_GET_NEXT_CMD:
            return hlapi.nextCmd
        elif command_type.lower() == self.snmp_constants.SNMP_WALK_CMD:
            return hlapi.nextCmd
        elif command_type.lower() == self.snmp_constants.SNMP_BULK_WALK_CMD:
            return hlapi.bulkCmd
        else:
            raise ValueError(command_type + " is not a valid SNMP command type.")

    def get_data_type(self, data_type):
        """
        Function Args:
        [data_type] - The data type found in the command object.

        Checks to make sure the data type passed by the command object is valid. If it is the appropriate command
        is returned. Otherwise a ValueError is returned.
        """
        if data_type is not None:
            if data_type.lower() == self.snmp_constants.DATA_TYPE_INTEGER:
                return hlapi.Integer
            if data_type.lower() == self.snmp_constants.DATA_TYPE_UNSIGNED_32:
                return hlapi.Unsigned32
            elif data_type.lower() == self.snmp_constants.DATA_TYPE_TIME_TICKS:
                return hlapi.TimeTicks
            elif data_type.lower() == self.snmp_constants.DATA_TYPE_IP_ADDR:
                return hlapi.IpAddress
            elif data_type.lower() == self.snmp_constants.DATA_TYPE_BITS:
                return hlapi.Bits
            elif data_type.lower() == self.snmp_constants.DATA_TYPE_OBJ_ID:
                return hlapi.ObjectIdentifier
            elif data_type.lower() == self.snmp_constants.DATA_TYPE_OCT_STR:
                return hlapi.OctetString
            else:
                raise ValueError(data_type + " is not a valid SNMP data type.")
        else:
            return hlapi.Integer

    @staticmethod
    def create_var_binds_set(snmp_cmd_obj):
        """
        Creates a list of setter var binds with the information in the command object. It creates a var bind
        for each unique set of values in oid, data_type, and value.
        """
        var_binds = []

        for oid, data_type, value in zip(snmp_cmd_obj.oid, snmp_cmd_obj.data_type, snmp_cmd_obj.value):
            var_binds.append(hlapi.ObjectType(hlapi.ObjectIdentity(oid), data_type(value)))

        return var_binds

    @staticmethod
    def create_var_binds_get(snmp_cmd_obj):
        """
        Creates a list of getter var binds with the information in the command object. It creates a var bind
        for each OID present in the command object.
        """
        return [hlapi.ObjectType(hlapi.ObjectIdentity(oid)) for oid in snmp_cmd_obj.oid]

    def snmp_set(self, cmd_obj):
        """
        Does an SNMP set based on the information present in the command object.
        """
        (error_indication,
         error_status,
         error_index,
         var_binds) = next(cmd_obj.command_type(hlapi.SnmpEngine(), self.get_security_info(),
                                                SnmpConstants.TRANSPORT((self.device.hostname, int(SnmpConstants.PORT)),
                                                                        timeout=int(SnmpConstants.TIMEOUT),
                                                                        retries=int(SnmpConstants.RETRIES)),
                                                hlapi.ContextData(),
                                                *self.create_var_binds_set(cmd_obj)))

        return self.snmp_error_check(cmd_obj, error_indication, error_status, error_index, var_binds)

    def snmp_get(self, cmd_obj):
        """
        Does an SNMP set based on the information present in the command object.
        """
        (error_indication,
         error_status,
         error_index,
         var_binds) = next(cmd_obj.command_type(hlapi.SnmpEngine(), self.get_security_info(),
                                                SnmpConstants.TRANSPORT((self.device.hostname, int(SnmpConstants.PORT)),
                                                                        timeout=int(SnmpConstants.TIMEOUT),
                                                                        retries=int(SnmpConstants.RETRIES)),
                                                hlapi.ContextData(),
                                                *self.create_var_binds_get(cmd_obj)))

        return self.snmp_error_check(cmd_obj, error_indication, error_status, error_index, var_binds)

    def snmp_walk(self, cmd_obj):
        """
        Does an SNMP walk based on the information present in the commando object.
        """
        for (error_indication,
             error_status,
             error_index,
             var_binds) in hlapi.nextCmd(hlapi.SnmpEngine(), self.get_security_info(),
                                         SnmpConstants.TRANSPORT((self.device.hostname, int(SnmpConstants.PORT)),
                                                                 timeout=int(SnmpConstants.TIMEOUT),
                                                                 retries=int(SnmpConstants.RETRIES)),
                                         hlapi.ContextData(), *self.create_var_binds_get(cmd_obj),
                                         lexicographicMode=False):

            cmd_obj = self.snmp_error_check(cmd_obj, error_indication, error_status, error_indication, var_binds)
        return cmd_obj

    def snmp_bulk_walk(self, cmd_obj):
        """
        Does an SNMP bulk walk based on the information present in the command object.
        """
        for (error_indication,
             error_status,
             error_index,
             var_binds) in hlapi.bulkCmd(hlapi.SnmpEngine(), self.get_security_info(),
                                         SnmpConstants.TRANSPORT((self.device.hostname, int(SnmpConstants.PORT)),
                                                                 timeout=int(SnmpConstants.TIMEOUT),
                                                                 retries=int(SnmpConstants.RETRIES)),
                                         hlapi.ContextData(),
                                         int(SnmpConstants.NON_REPEATERS),
                                         int(SnmpConstants.MAX_REPETITIONS),
                                         *self.create_var_binds_get(cmd_obj),
                                         lexicographicMode=False):

            cmd_obj = self.snmp_error_check(cmd_obj, error_indication, error_status, error_index, var_binds)
        return cmd_obj

    def get_security_info(self):
        """
        Returns the security object based on security model. If it is community a CommunityData object
        is returned. If it is user a UsmUserData object is returned. Otherwise an exception is raised
        as an invalid security model was provided.
        """
        if self.security_model == self.snmp_constants.SECURITY_MODEL_COMMUNITY:
            return hlapi.CommunityData(self.community_name, mpModel=int(self.snmp_version))
        elif self.security_model == self.snmp_constants.SECURITY_MODEL_USER:
            return hlapi.UsmUserData(self.user_name, self.auth_password, self.privacy_password,
                                     authProtocol=self.auth_protocol, privProtocol=self.privacy_protocol)
        else:
            raise ValueError("Invalid security model.")

    @staticmethod
    def snmp_error_check(cmd_obj, error_indication, error_status, error_index, var_binds):
        """
        This function checks the information returned from the SNMP command. If error_indication exists
        set that in the command object. Otherwise checks the error_status if it is present it's set in
        the command object.
        """
        response = []

        if error_indication:
            cmd_obj.return_error_indication = error_indication
        else:
            if error_status:
                cmd_obj.return_error_status = '%s at %s' % (error_status.prettyPrint(),
                                                            error_index and var_binds[int(error_index) - 1] or '?')
            else:
                for var_bind in var_binds:
                    s = (' = '.join([x.prettyPrint() for x in var_bind]))
                    response.append(s)

        if cmd_obj.return_text is None:
            cmd_obj.return_text = response
        else:
            cmd_obj.return_text += response

        return cmd_obj

    def login(self):
        """
        Login function, not needed for SNMP, sets logged_in to True.
        """
        self.logged_in = True
        return True

    def connect(self):
        """
        Connect function, not needed for SNMP, sets connected and logged_in to True.
        """
        self.connected = True
        self.logged_in = True

    def disconnect(self):
        """
        Disconnect function, not needed for SNMP, sets connected and logged_in to False.
        """
        self.connected = False
        self.logged_in = False

    def logout(self):
        """
        Logout funciton, not needed for SNMP, sets logged_in to False.
        """
        self.logged_in = False


class SnmpConstants(Constants):
    # API options
    PORT = "161"
    TIMEOUT = "5"
    RETRIES = "3"
    NON_REPEATERS = "0"
    MAX_REPETITIONS = "10"
    TRANSPORT = hlapi.UdpTransportTarget

    # Security Constants
    SECURITY_MODEL_COMMUNITY = "comm"
    SECURITY_MODEL_USER = "usr"

    # SNMP Command Constants
    SNMP_GET_CMD = "snmpget"
    SNMP_SET_CMD = "snmpset"
    SNMP_GET_NEXT_CMD = "snmpgetnext"
    SNMP_WALK_CMD = "snmpwalk"
    SNMP_BULK_WALK_CMD = "snmpbulkwalk"

    # SNMP Version Constants
    SNMP_VER_1 = "0"
    SNMP_VER_2 = "1"
    SNMP_VER_3 = "3"

    # SNMP Data Type Constants
    DATA_TYPE_INTEGER = "i"
    DATA_TYPE_UNSIGNED_32 = "u"
    DATA_TYPE_TIME_TICKS = "t"
    DATA_TYPE_IP_ADDR = "a"
    DATA_TYPE_BITS = "b"
    DATA_TYPE_OBJ_ID = "o"
    DATA_TYPE_OCT_STR = "s"

    # SNMP Auth Protocols
    SNMP_AUTH_NO_AUTH = "noauth"
    SNMP_AUTH_MD5 = "md5"
    SNMP_AUTH_SHA = "sha"

    # SNMP Privacy Protocols
    SNMP_PRIV_NO_PRIV = "nopriv"
    SNMP_PRIV_DES = "des"
    SNMP_PRIV_3DES = "3des"
    SNMP_PRIV_AES128 = "aes128"
    SNMP_PRIV_AES192 = "aes192"
    SNMP_PRIV_AES256 = "aes256"
