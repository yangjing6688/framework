"""
Keyword class for all poe cli commands.
"""
from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import NetworkElementKeywordBaseClass
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.Constants.PoeConstants import \
    PoeConstants as ParseConstants
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.Constants.PoeConstants import \
    PoeConstants as CommandConstants
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils
from ExtremeAutomation.Keywords.NetworkElementKeywords.Utils.NetworkElementSnmpUtils \
    import NetworkElementSnmpUtils as SnmpUtils


class NetworkElementPoeGenKeywords(NetworkElementKeywordBaseClass):
    def __init__(self):
        super(NetworkElementPoeGenKeywords, self).__init__()
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()
        self.api_const = "poe"

    def poe_enable_port(self, device_name, port='', **kwargs):
        """
        Description: Enables the port which can provide the PSE functions.

        Supported Agents and OS:
            CLI: VOSS, EXOS
            SNMP: VOSS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_PORT,
                                    **kwargs)

    def poe_disable_port(self, device_name, port='', **kwargs):
        """
        Description: Disables the port which can provide the PSE functions.

        Supported Agents and OS:
            CLI: VOSS, EXOS
            SNMP: VOSS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_PORT,
                                    **kwargs)

    def poe_set_power_usage_threshold(self, device_name, threshold='', slot='', **kwargs):
        """
        Description: Configures the usage threshold expressed as a percentage.

        Supported Agents and OS:
            CLI: VOSS, EXOS
            SNMP: VOSS
        """
        args = {
            "slot": slot,
            "threshold": threshold
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_POWER_USAGE_THRESHOLD,
                                    **kwargs)

    def poe_set_port_power_limit(self, device_name, port='', power_limit='', **kwargs):
        """
        Description: Configures the DTE power limit per port.

        Supported Agents and OS:
            CLI: VOSS, EXOS
            SNMP: VOSS
        """
        args = {
            "port": port,
            "power_limit": power_limit
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PORT_POWER_LIMIT,
                                    **kwargs)

    def poe_set_port_power_priority(self, device_name, port='', power_priority='', **kwargs):
        """
        Description: Configures the POE port power priority.

        Supported Agents and OS:
            CLI: VOSS, EXOS
            SNMP: VOSS
        """
        args = {
            "port": port,
            "power_priority": power_priority
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PORT_POWER_PRIORITY,
                                    **kwargs)

    def poe_set_port_detect_type(self, device_name, port='', detect_type='', **kwargs):
        """
        Description: Specifies the mechanism used to detect powered ethernet devices attached to a powered ethernet
                     port.

        Supported Agents and OS:
            SNMP: VOSS
            CLI: EXOS
        """
        args = {
            "detect_type": detect_type,
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PORT_DETECT_TYPE,
                                    **kwargs)

    def poe_enable_inline_power(self, device_name, **kwargs):
        """
        Description: Enables inline power.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_INLINE_POWER,
                                    **kwargs)

    def poe_disable_inline_power(self, device_name, **kwargs):
        """
        Description: Disables inline power.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_INLINE_POWER,
                                    **kwargs)

    def poe_enable_inline_power_legacy(self, device_name, **kwargs):
        """
        Description: Enable inline power legacy.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_INLINE_POWER_LEGACY,
                                    **kwargs)

    def poe_disable_inline_power_legacy(self, device_name, **kwargs):
        """
        Description: Disable inline power legacy.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_INLINE_POWER_LEGACY,
                                    **kwargs)

    def poe_set_inline_power_disconnect_deny_port(self, device_name, **kwargs):
        """
        Description: Configure inline power disconnect deny port.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_INLINE_POWER_DISCONNECT_DENY_PORT,
                                    **kwargs)

    def poe_set_inline_power_disconnect_lowest_priority(self, device_name, **kwargs):
        """
        Description: Configure inline power disconnect lowest priority.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_INLINE_POWER_DISCONNECT_LOWEST_PRIORITY,
                                    **kwargs)

    def poe_clear_inline_power_disconnect(self, device_name, **kwargs):
        """
        Description: Unconfigure inline power disconnect.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_INLINE_POWER_DISCONNECT,
                                    **kwargs)

    def poe_set_inline_power_label(self, device_name, port='', test_label='', **kwargs):
        """
        Description: Configure inline power label.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "port": port,
            "test_label": test_label
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_INLINE_POWER_LABEL,
                                    **kwargs)

    # ##################################################################################################################
    #   Inspection Keywords   ##########################################################################################
    # ##################################################################################################################

    def poe_verify_power_threshold(self, device_name, threshold='', slot="1", **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [threshold]   - The usage threshold expressed in percents for comparing the measured power and initiating
                        an alarm if the threshold is exceeded.  Values: 1..99
        [slot]        - The group of POE ports on a module or slot.

        Verifies the usage threshold expressed as a percentage.
        """
        args = {"threshold": threshold,
                "oid_index": slot}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_POWER_USAGE_THRESHOLD,
                                           self.parse_const.CHECK_POE_POWER_USAGE_THRESHOLD, True,
                                           "POE power usage threshold is {threshold}.",
                                           "POE power usage threshold is NOT {threshold}!",
                                           **kwargs)

    def poe_verify_power_invalid_threshold(self, device_name, threshold='', slot="1", **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [threshold]   - The usage threshold expressed in percents for comparing the measured power and initiating
                        an alarm if the threshold is exceeded
        [slot]        - The group of POE ports on a module or slot.

        Verifies the usage threshold expressed as a percentage.
        """
        args = {"threshold": threshold,
                "oid_index": slot}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_POWER_USAGE_THRESHOLD,
                                           self.parse_const.CHECK_POE_POWER_USAGE_THRESHOLD, True,
                                           "POE power usage threshold is {threshold}.",
                                           "POE power usage threshold is NOT {threshold}!",
                                           **kwargs)

    def poe_verify_port_enabled(self, device_name, ports='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [ports]       - The port(s) on which to verify.

        IEEE Std 802.3af Section 30.9.1.1.2 aPSEAdminState

        Verifies the port is enabled for PSE functions.
        """
        args = {"port": ports,
                "oid_index": StringUtils().get_slot_from_port_string(
                    ports) + "." + SnmpUtils().get_port_index_from_name(device_name, ports)}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_POE_PORT_STATUS,
                                           self.parse_const.CHECK_POE_PORT_STATE, True,
                                           "POE port is enabled on port {port}.",
                                           "POE port is NOT enabled on port {port}!",
                                           **kwargs)

    def poe_verify_port_disabled(self, device_name, ports='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [ports]       - The port(s) on which to verify.

        IEEE Std 802.3af Section 30.9.1.1.2 aPSEAdminState

        Verifies the port is disabled for PSE functions.
        """
        args = {"port": ports,
                "oid_index": StringUtils().get_slot_from_port_string(
                    ports) + "." + SnmpUtils().get_port_index_from_name(device_name, ports)}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_POE_PORT_STATUS,
                                           self.parse_const.CHECK_POE_PORT_STATE, False,
                                           "POE port is disabled on port {port}.",
                                           "POE port is NOT disabled on port {port}!",
                                           **kwargs)

    def poe_verify_port_power_limit(self, device_name, ports='', power_limit='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [ports]       - The port(s) on which to verify.
        [power_limit] - DTE Power limit per port.  Values: 3..32 watts  Default:32

        Verifies the DTE Power limit per port.
        """
        args = {"port": ports,
                "oid_index": StringUtils().get_slot_from_port_string(
                    ports) + "." + SnmpUtils().get_port_index_from_name(device_name, ports),
                "power_limit": power_limit}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_POE_PORT_POWER_LIMIT,
                                           self.parse_const.CHECK_POE_PORT_POWER_LIMIT, True,
                                           "POE  power limit on port {port} is {power_limit}.",
                                           "POE  power limit on port {port} is NOT {power_limit}.",
                                           **kwargs)

    def poe_verify_port_priority(self, device_name, ports='', power_priority='', **kwargs):
        """
        Keyword Arguments:
        [device_name]    - The device the keyword should be run against.
        [ports]          - The port(s) on which to verify.
        [power_priority] - Power priority of the port.    Values: critical, high, and low.  Default: low

        This keyword controls the priority of the port from the point
        of view of a power management algorithm.  The priority that
        is set by this variable could be used by a control mechanism
        that prevents over current situations by disconnecting first
        ports with lower power priority.  Ports that connect devices
        critical to the operation of the network - like the E911
        telephones ports - should be set to higher priority.

        Verifies port power priority.
        """

        """
        following try blocks are added to avoid exceptions when the values inside the 
        block is not required for the current test execution
        
        example: oid_index is not required when running exos cli test
        """
        try:
            oid_index = StringUtils().get_slot_from_port_string(
                    ports) + "." + SnmpUtils().get_port_index_from_name(device_name, ports)

        except:
            oid_index = ''

        try:
            power_priority_value = SnmpUtils().poe_priority(power_priority)

        except:
            power_priority_value = ''

        args = {"port": ports,
                "oid_index": oid_index,
                "power_priority": power_priority,
                "power_priority_value": power_priority_value}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_POWER_PRIORITY,
                                           self.parse_const.CHECK_POE_PORT_POWER_PRIORITY, True,
                                           "POE  priority on port {port} is {power_priority}.",
                                           "POE  priority on port {port} is NOT {power_priority}.",
                                           **kwargs)

    def poe_verify_port_detect_type(self, device_name, ports='', detect_type='', **kwargs):
        """
        Keyword Arguments:
        [device_name]    - The device the keyword should be run against.
        [ports]          - The port(s) on which to verify.
        [detect_type]    - Power priority of the port.    Values: critical, high, and low.  Default: low

        This keyword is used to specify the mechanism used to detect powered ethernet devices attached
        to a powered ethernet port.
        Values:
        802.3af
        802.3af and legacy
        802.3at
        802.3at and legacy

        Default: 802.3at and legacy

        Verifies the POE port detect type.
        """

        try:
            oid_index = SnmpUtils().get_port_index_from_name(device_name, ports)
        except:
            oid_index = ''

        try:
            detect_type_value  = SnmpUtils().poe_detect_type(detect_type)
        except:
            detect_type_value = ''

        args = {"port": ports,
                "oid_index": oid_index,
                "detect_type": detect_type,
                "detect_type_value": detect_type_value}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_DETECT_TYPE,
                                           self.parse_const.CHECK_POE_PORT_DETECT_TYPE, True,
                                           "POE  detect type on port {port} is {detect_type}.",
                                           "POE  detect type on port {port} is NOT {detect_type}.",
                                           **kwargs)

    def poe_verify_port_measured_voltage(self, device_name, ports='', decivolts='', value_operator="=", **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword should be run against.
        [ports]           - The port(s) on which to verify.
        [decivolts]       - The measured voltage in deci volts.
        [value_operator]  - The operator (>, <, or =) to be used along with the value argument.

        Measured port voltage in decivolts.

        Verifies the POE port voltage in decivolts.
        """
        args = {"port": ports,
                "oid_index": StringUtils().get_slot_from_port_string(
                    ports) + "." + SnmpUtils().get_port_index_from_name(device_name, ports),
                "decivolts": decivolts,
                "value_operator": value_operator}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_POE_PORT_MEASUREMENTS,
                                           self.parse_const.CHECK_POE_PORT_MEASURED_VOLTAGE, True,
                                           "POE  voltage on port {port} is {value_operator} "
                                           "{decivolts} decivolts.",
                                           "POE  voltage on port {port} is NOT {value_operator} "
                                           "{decivolts} decivolts!",
                                           **kwargs)

    def poe_verify_port_measured_current(self, device_name, ports='', milliamps='', value_operator="=", **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword should be run against.
        [ports]           - The port(s) on which to verify.
        [milliamps]       - The measured current in milliamps.
        [value_operator]  - The operator (>, <, or =) to be used along with the value argument.

        Measured port current in milliamps.

        Verifies the POE port current in milliamps.
        """
        args = {"port": ports,
                "oid_index": StringUtils().get_slot_from_port_string(
                    ports) + "." + SnmpUtils().get_port_index_from_name(device_name, ports),
                "milliamps": milliamps,
                "value_operator": value_operator}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_POE_PORT_MEASUREMENTS,
                                           self.parse_const.CHECK_POE_PORT_MEASURED_CURRENT, True,
                                           "POE  current on port {port} is {value_operator} "
                                           "{milliamps} milliamps.",
                                           "POE  current on port {port} is NOT {value_operator} "
                                           "{milliamps} milliamps!",
                                           **kwargs)

    def poe_verify_port_measured_power(self, device_name, ports='', milliwatts='', value_operator="=", **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword should be run against.
        [ports]           - The port(s) on which to verify.
        [milliwatts]      - The measured power in milliwatts.
        [value_operator]  - The operator (>, <, or =) to be used along with the value argument.

        Measured port power in milliwatts.  This value may not exceed 1000 times the
        current value of the port power limit i.e. bspePethPsePortExtPowerLimit.

        Verifies the POE port power in milliwatts.
        """
        args = {"port": ports,
                "oid_index": StringUtils().get_slot_from_port_string(
                    ports) + "." + SnmpUtils().get_port_index_from_name(device_name, ports),
                "milliwatts": milliwatts,
                "value_operator": value_operator}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_POE_PORT_MEASUREMENTS,
                                           self.parse_const.CHECK_POE_PORT_MEASURED_POWER, True,
                                           "POE  power on port {port} is {value_operator} "
                                           "{milliwatts} milliwatts.",
                                           "POE  power on port {port} is NOT {value_operator} "
                                           "{milliwatts} milliwatts!",
                                           **kwargs)

    def poe_verify_port_detection_status(self, device_name, ports='', detect_status='', **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword should be run against.
        [ports]           - The port(s) on which to verify.
        [detect_status]   - The value of the detection status.

        Detection status value list:
            disabled
            searching
            delivering-power
            fault
            test
            other-fault

        IEEE Std 802.3af Section 30.9.1.1.5
        aPSEPowerDetectionStatus

            Describes the operational status of the port PD detection.
            A value of disabled(1)- indicates that the PSE State diagram
            is in the state DISABLED.
            A value of deliveringPower(3) - indicates that the PSE State
            diagram is in the state POWER_ON for a duration greater than
            tlim max (see IEEE Std 802.3af Table 33-5 tlim).
            A value of fault(4) - indicates that the PSE State diagram is
            in the state TEST_ERROR.
            A value of test(5) - indicates that the PSE State diagram is
            in the state TEST_MODE.
            A value of otherFault(6) - indicates that the PSE State
            diagram is in the state IDLE due to the variable
            error_conditions.
            A value of searching(2)- indicates the PSE State diagram is
            in a state other than those listed above.

        Verifies the POE detection status of the port.
        """
        args = {"port": ports,
                "oid_index": StringUtils().get_slot_from_port_string(
                    ports) + "." + SnmpUtils().get_port_index_from_name(device_name, ports),
                "detect_status": detect_status,
                "status_value": SnmpUtils().poe_detect_status(detect_status)}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_POE_PORT_DETECTION_STATUS,
                                           self.parse_const.CHECK_POE_PORT_DETECTION_STATUS, True,
                                           "POE  detect status on port {port} is {detect_status}.",
                                           "POE  detect status on port {port} is NOT {detect_status}!",
                                           **kwargs)

    def poe_verify_port_power_classification(self, device_name, ports='', power_class='', **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword should be run against.
        [ports]           - The port(s) on which to verify.
        [power_class]     - The value of the power classification.

        Value list:
        class0
        class1
        class2
        class3
        class4

        Reference:	IEEE Std 802.3af Section 30.9.1.1.6
        aPSEPowerClassification

        Classification is a way to tag different terminals on the
        Power over LAN network according to their power consumption.
        Devices such as IP telephones, WLAN access points and others,
        will be classified according to their power requirements.

        The meaning of the classification labels is defined in the
        IEEE specification.

        This variable is valid only while a PD is being powered,
        that is, while the attribute pethPsePortDetectionStatus
        is reporting the enumeration deliveringPower.

        Verifies the POE power classification of the port.
        """
        args = {"port": ports,
                "oid_index": StringUtils().get_slot_from_port_string(
                    ports) + "." + SnmpUtils().get_port_index_from_name(device_name, ports),
                "power_class": power_class,
                "power_class_value": SnmpUtils().poe_power_classification(power_class)}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_POE_PORT_POWER_CLASSIFICATION,
                                           self.parse_const.CHECK_POE_PORT_POWER_CLASSIFICATION, True,
                                           "POE power class of port {port} is {power_class}.",
                                           "POE  power class of port {port} is NOT {power_class}!",
                                           **kwargs)

    def poe_verify_port_power_pairs_on_signal(self, device_name, ports='', **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword should be run against.
        [ports]           - The port(s) on which to verify.
        Reference:	IEEE Std 802.3af Section 30.9.1.1.4 aPSEPowerPairs

        Describes or controls the pairs in use.  If the value of
        pethPsePortPowerPairsControl is true, this object is
        writable.
        A value of signal means that the signal pairs
        only are in use.
        A value of spare means that the spare pairs
        only are in use.

        Verifies that the port POE port power is using the signal pairs.
        """
        args = {"port": ports,
                "oid_index": StringUtils().get_slot_from_port_string(
                    ports) + "." + SnmpUtils().get_port_index_from_name(device_name, ports)}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_POE_PORT_POWER_PAIRS,
                                           self.parse_const.CHECK_POE_PORT_POWER_PAIRS_ON_SIGNAL, True,
                                           "POE port power pairs on port {port} is on the signal pairs.",
                                           "POE port power pairs on port {port} is NOT on the signal pairs!",
                                           **kwargs)

    def poe_verify_port_power_pairs_on_spare(self, device_name, ports='', **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword should be run against.
        [ports]           - The port(s) on which to verify.
        Reference:	IEEE Std 802.3af Section 30.9.1.1.4 aPSEPowerPairs

        Describes or controls the pairs in use.  If the value of
        pethPsePortPowerPairsControl is true, this object is
        writable.
        A value of signal means that the signal pairs
        only are in use.
        A value of spare means that the spare pairs
        only are in use.

        Verifies that the port POE port power is using the spare pairs.
        """
        args = {"port": ports,
                "oid_index": StringUtils().get_slot_from_port_string(
                    ports) + "." + SnmpUtils().get_port_index_from_name(device_name, ports)}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_POE_PORT_POWER_PAIRS,
                                           self.parse_const.CHECK_POE_PORT_POWER_PAIRS_ON_SPARE, True,
                                           "POE port power pairs on port {port} is on the spare pairs.",
                                           "POE port power pairs on port {port} is NOT on the spare pairs!",
                                           **kwargs)

    def poe_verify_main_available_power(self, device_name, power='', slot="1", **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [power]       - The expected available power in Watts.
        [slot]        -  Group (slot) which the ports are a member of.
        Verifies the nominal available power of the PSE expressed in Watts.
        """
        args = {"power": power,
                "slot": slot,
                "oid_index": slot}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_POE_GLOBAL_STATUS,
                                           self.parse_const.CHECK_POE_MAIN_AVAILABLE_POWER, True,
                                           "POE main available power on slot {slot} is {power} .",
                                           "POE main available power on slot {slot} is NOT {power}!",
                                           **kwargs)

    def poe_verify_main_consumption_power(self, device_name, power='', value_operator="=", slot="1", **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword should be run against.
        [power]           - The measured power in Watts.
        [value_operator]  - The operator (>, <, or =) to be used along with the value argument.
        [slot]        -  Group (slot) which the ports are a member of.

        Verifies the main POE power consumption in Watts.
        """
        args = {"power": power,
                "value_operator": value_operator,
                "slot": slot,
                "oid_index": slot}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_POE_GLOBAL_STATUS,
                                           self.parse_const.CHECK_POE_MAIN_CONSUMPTION_POWER, True,
                                           "POE main power consumption on slot {slot} is "
                                           "{value_operator} {power}.",
                                           "POE main power consumption on slot {slot} is NOT "
                                           "{value_operator} {power}!",
                                           **kwargs)

    def poe_verify_inline_power_disabled(self, device_name, **kwargs):

        args = {
            'disabled': 'Disabled'
        }

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INLINE_POWER,
                                           self.parse_const.CHECK_POE_INLINE_POWER_DISABLED, True,
                                           "POE inline power is disabled",
                                           "POE inline power is not disabled",
                                           **kwargs)

    def poe_verify_inline_power_enabled(self, device_name, **kwargs):
        args = {
            'enabled': 'Enabled'
        }

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INLINE_POWER,
                                           self.parse_const.CHECK_POE_INLINE_POWER_ENABLED, True,
                                           "POE inline power is enabled",
                                           "POE inline power is not enabled",
                                           **kwargs)

    def poe_verify_inline_power_port_disabled(self, device_name, port='', **kwargs):

        args = {
            'search_value': 'disabled',
            'port': port
        }

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INLINE_POWER_INFO_PORT,
                                           self.parse_const.CHECK_POE_INLINE_POWER_PORT_INFO, True,
                                           "POE inline power port {} is disabled".format(port),
                                           "POE inline power port {} is not disabled".format(port),
                                           **kwargs)

    def poe_verify_inline_power_port_enabled(self, device_name, port='', **kwargs):

        args = {
            'search_value': 'searching',
            'port': port
        }

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INLINE_POWER_INFO_PORT,
                                           self.parse_const.CHECK_POE_INLINE_POWER_PORT_INFO, True,
                                           "POE inline power port {} is enabled".format(port),
                                           "POE inline power port {} is not enabled".format(port),
                                           **kwargs)

    def poe_verify_inline_power_legacy_enabled(self, device_name, port='', **kwargs):

        args = {
            'search_value': 'legacy',
            'port': port,
            'search_value_exist': True # flag to denote search_value should exist in output
        }

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INLINE_POWER_LEGACY,
                                           self.parse_const.CHECK_POE_INLINE_POWER_CONFIG_PORT, True,
                                           "Legacy inline power is enabled",
                                           "Legacy inline power is not enabled",
                                           **kwargs)

    def poe_verify_inline_power_legacy_disabled(self, device_name, port='', **kwargs):

        args = {
            'search_value': 'legacy',
            'port': port,
            'search_value_exist': False  # flag to denote search_value should not exist in output
        }

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INLINE_POWER_LEGACY,
                                           self.parse_const.CHECK_POE_INLINE_POWER_CONFIG_PORT, True,
                                           "Legacy inline power is disabled",
                                           "Legacy inline power is not disabled",
                                           **kwargs)

    def poe_verify_inline_power_disconnect_deny_port(self, device_name, **kwargs):

        args = {
            'search_value': 'deny-port'
        }

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INLINE_POWER,
                                           self.parse_const.CHECK_POE_INLINE_POWER_DISCONNECT_DENY_PORT, True,
                                           "Disconnect deny-port precedence configured",
                                           "Disconnect deny-port precedence is not configured",
                                           **kwargs)

    def poe_verify_inline_power_disconnect_lowest_priority(self, device_name, **kwargs):

        args = {
            'search_value': 'lowest-priority'
        }

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INLINE_POWER,
                                           self.parse_const.CHECK_POE_INLINE_POWER_DISCONNECT_LOWEST_PRIORITY, True,
                                           "Disconnect lowest-priority precedence configured",
                                           "Disconnect lowest-priority precedence is not configured",
                                           **kwargs)

    def poe_verify_inline_power_unconfigure_disconnect(self, device_name, **kwargs):

        args = {
            'search_value': 'deny-port'
        }

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INLINE_POWER,
                                           self.parse_const.CHECK_POE_INLINE_POWER_DISCONNECT_LOWEST_PRIORITY, True,
                                           "Disconnect precedence unconfigured",
                                           "Disconnect precedence is not unconfigured",
                                           **kwargs)

    def poe_verify_inline_power_label(self, device_name, port, test_label, **kwargs):

        args = {
            'port': port,
            'test_label': test_label
        }

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INLINE_POWER_LABEL,
                                           self.parse_const.CHECK_POE_INLINE_POWER_LABEL, True,
                                           "Label configured",
                                           "Label is not configured",
                                           **kwargs)

    def poe_verify_inline_power_operator_limit(self, device_name, port, operator_limit, **kwargs):

        args = {
            'port': port,
            'operator_limit': operator_limit
        }

        return self.execute_verify_keyword(device_name,
                                       args,
                                       self.cmd_const.SHOW_INLINE_POWER_OPERATOR_LIMIT,
                                       self.parse_const.CHECK_POE_INLINE_POWER_OPERATOR_LIMIT,
                                       True,
                                       "Inline power operator limit is configured to {}".format(
                                           str(operator_limit)),
                                       "Inline power operator limit is not configured to {}".format(
                                           str(operator_limit))
                                       )
