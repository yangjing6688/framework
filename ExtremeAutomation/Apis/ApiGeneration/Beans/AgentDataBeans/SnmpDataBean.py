from ExtremeAutomation.Library.Device.Common.Agents.SnmpAgent import SnmpConstants
from ExtremeAutomation.Apis.ApiGeneration.Beans.DataBean import DataBean


class SnmpDataBean(DataBean):
    def __init__(self):
        super(SnmpDataBean, self).__init__()
        self.interface_method = None
        self.oid = None
        self.value = None
        self.oid_index = "oid_index"

        # Attributes with setters/getters.
        self._command_type = None
        self._data_type = None

    @property
    def command_type(self):
        """
        Property function for command_type. Returns the private attribute _command_type.
        """
        return self._command_type

    @command_type.setter
    def command_type(self, command_type):
        """
        Setter function for command_type. Checks the passed <command_type> is a supported command type.
        If it isn't a ValueError is raised.
        """
        if command_type.lower().replace("_", "") == SnmpConstants.SNMP_GET_CMD.replace("snmp", ""):
            self._command_type = SnmpConstants.SNMP_GET_CMD
        elif command_type.lower().replace("_", "") == SnmpConstants.SNMP_GET_NEXT_CMD.replace("snmp", ""):
            self._command_type = SnmpConstants.SNMP_GET_NEXT_CMD
        elif command_type.lower().replace("_", "") == SnmpConstants.SNMP_WALK_CMD.replace("snmp", ""):
            self._command_type = SnmpConstants.SNMP_WALK_CMD
        elif command_type.lower().replace("_", "") == SnmpConstants.SNMP_BULK_WALK_CMD.replace("snmp", ""):
            self._command_type = SnmpConstants.SNMP_BULK_WALK_CMD
        elif command_type.lower().replace("_", "") == SnmpConstants.SNMP_SET_CMD.replace("snmp", ""):
            self._command_type = SnmpConstants.SNMP_SET_CMD
        else:
            raise ValueError(command_type + " is not a valid SNMP command type.")

    @property
    def data_type(self):
        """
        Property function for data_type. Returns the private attribute _data_type.
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """
        Setter function for data_type. Checks that the data type is present in the valid data types. If "||"
        is present in <data_type> split on "||" and check that each item in the resulting list is a valid
        data type. For any invalid data type use the default.
        """
        default = SnmpConstants.DATA_TYPE_INTEGER
        valid_data_types = [SnmpConstants.DATA_TYPE_INTEGER,
                            SnmpConstants.DATA_TYPE_UNSIGNED_32,
                            SnmpConstants.DATA_TYPE_TIME_TICKS,
                            SnmpConstants.DATA_TYPE_IP_ADDR,
                            SnmpConstants.DATA_TYPE_BITS,
                            SnmpConstants.DATA_TYPE_OBJ_ID,
                            SnmpConstants.DATA_TYPE_OCT_STR
                            ]

        if data_type.lower() in valid_data_types:
            self._data_type = data_type.lower()
        elif "||" in data_type.lower():
            self._data_type = "||".join([i if i in valid_data_types else default for i in data_type.split("||")])
        else:
            self._data_type = default

    @property
    def feature(self):
        """
        Property function for feature. Returns the private attribute _feature.
        """
        return self._feature

    @feature.setter
    def feature(self, feature):
        """
        Setter function for feature. Sets the private attribute _feature as well as the file_name
        and base_file_name.
        """
        self._feature = feature
        self.file_name = feature + ".py"
        self.base_file_name = feature + "base.py"
