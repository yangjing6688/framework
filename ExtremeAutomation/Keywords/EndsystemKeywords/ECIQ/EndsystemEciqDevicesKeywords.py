from ExtremeAutomation.Keywords.BaseClasses.EndsystemKeywordBaseClass import EndsystemKeywordBaseClass
from ExtremeAutomation.Apis.EndsystemElement.GeneratedApis.CommandApis.Constants.EciqdevicesConstants import \
    EciqdevicesConstants as CommandConstants
from ExtremeAutomation.Apis.EndsystemElement.GeneratedApis.ParseApis.Constants.EciqdevicesConstants import \
    EciqdevicesConstants as ParseConstants


class EndsystemEciqDevicesKeywords(EndsystemKeywordBaseClass):
    def __init__(self):
        super(EndsystemEciqDevicesKeywords, self).__init__()
        self.api_const = self.constants.API_ECIQ_DEVICES
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()

    def rest_eciq_remove_device(self, server_name, owner_id, device_id, **kwargs):
        """
        Keyword Arguments:
        [server_name] - The name of the Extreme Cloud IQ server Endsystem Element.
        [owner_id] - The owner ID.  This is the ExtremeCloud IQ VIQ ID.
        [device_id] - The device ID of the device to be deleted.
        """
        args = {"server_name": server_name,
                "owner_id": owner_id,
                "device_id": device_id}

        return self.execute_keyword(server_name, args, self.cmd_const.REMOVE_DEVICE, **kwargs)

    def rest_eciq_store_device_id_for_serial_number(self, server_name, serial_number, owner_id, var_name="deviceId",
                                                    **kwargs):
        """
        Keyword Arguments:
        [server_name] - The name of the Extreme Cloud IQ server Endsystem Element.
        [serial_number] - The serial number of the DUT.
        [owner_id] - The owner ID.  This is the ExtremeCloud IQ VIQ ID.
        [var_name] - The name to store the 'deviceId' variable under.

        Resulting variable in Robot:
        ${<yaml_server_index>.value_storage.<var_name>}
        Ex:
        ${endsys1.value_storage.device_id}
        """
        arg_dict = {"serial_number": serial_number,
                    "owner_id": owner_id,
                    "var_name": var_name}

        return self.execute_verify_keyword(server_name, arg_dict, self.cmd_const.GET_DEVICE_LIST,
                                           self.parse_const.STORE_DEVICE_ID_FOR_SERIAL_NUMBER, True,
                                           "The DUT's device_id has been stored as ${<yaml_index>.value_storage." +
                                           var_name + "}.",
                                           "The DUT's device_id was not found!",
                                           **kwargs)

    def rest_eciq_verify_device_firmware(self, server_name, serial_number, firmware_version, owner_id, **kwargs):
        """
        Keyword Arguments:
        [server_name] - The name of the Extreme Cloud IQ server Endsystem Element.
        [serial_number] - The serial number of the DUT.
        [firmware_version] - The firmware version to be verified.
        [owner_id] - The owner ID.  This is the ExtremeCloud IQ VIQ ID.
        """
        args = {"server_name": server_name,
                "serial_number": serial_number,
                "firmware_version": firmware_version,
                "owner_id": owner_id}

        return self.execute_verify_keyword(server_name, args, self.cmd_const.GET_DEVICE_LIST,
                                           self.parse_const.VERIFY_DEVICE_FIRMWARE, True,
                                           "The device firmware version {firmware_version} exists for serial number "
                                           "{serial_number}.",
                                           "The device firmware version {firmware_version} DOES NOT exist for "
                                           "serial number {serial_number}!", **kwargs)

    def rest_eciq_verify_device_ip(self, server_name, serial_number, mgmt_ip, owner_id, **kwargs):
        """
        Keyword Arguments:
        [server_name] - The name of the Extreme Cloud IQ server Endsystem Element.
        [serial_number] - The serial number of the DUT.
        [mgmt_ip] - The mgmt IP to be verified.
        [owner_id] - The owner ID.  This is the ExtremeCloud IQ VIQ ID.
        """
        args = {"server_name": server_name,
                "serial_number": serial_number,
                "mgmt_ip": mgmt_ip,
                "owner_id": owner_id}

        return self.execute_verify_keyword(server_name, args, self.cmd_const.GET_DEVICE_LIST,
                                           self.parse_const.VERIFY_DEVICE_IP, True,
                                           "The device mgmt IP exists {mgmt_ip} for serial number {serial_number}.",
                                           "The device mgmt IP {mgmt_ip} DOES NOT exist for serial number "
                                           "{serial_number}!", **kwargs)

    def rest_eciq_verify_device_mac(self, server_name, serial_number, mac_addr, owner_id, **kwargs):
        """
        Keyword Arguments:
        [server_name] - The name of the Extreme Cloud IQ server Endsystem Element.
        [serial_number] - The serial number of the DUT.
        [mac_addr] - The MAC address to be verified.
        [owner_id] - The owner ID.  This is the ExtremeCloud IQ VIQ ID.
        """
        args = {"server_name": server_name,
                "serial_number": serial_number,
                "mac_addr": mac_addr,
                "owner_id": owner_id}

        return self.execute_verify_keyword(server_name, args, self.cmd_const.GET_DEVICE_LIST,
                                           self.parse_const.VERIFY_DEVICE_MAC, True,
                                           "The device MAC address {mac_addr} exists for serial number "
                                           "{serial_number}.",
                                           "The device MAC address {mac_addr} DOES NOT exist for serial number "
                                           "{serial_number}!", **kwargs)

    def rest_eciq_verify_device_model(self, server_name, serial_number, model, owner_id, **kwargs):
        """
        Keyword Arguments:
        [server_name] - The name of the Extreme Cloud IQ server Endsystem Element.
        [serial_number] - The serial number of the DUT.
        [model] - The model to be verified.
        [owner_id] - The owner ID.  This is the ExtremeCloud IQ VIQ ID.
        """
        args = {"server_name": server_name,
                "serial_number": serial_number,
                "model": model,
                "owner_id": owner_id}

        return self.execute_verify_keyword(server_name, args, self.cmd_const.GET_DEVICE_LIST,
                                           self.parse_const.VERIFY_DEVICE_MODEL, True,
                                           "The device model {model} exists for serial number {serial_number}.",
                                           "The device model {model} DOES NOT exist for serial number {serial_number}!",
                                           **kwargs)

    def rest_eciq_verify_device_serial_number(self, server_name, serial_number, owner_id, **kwargs):
        """
        Keyword Arguments:
        [server_name] - The name of the Extreme Cloud IQ server Endsystem Element.
        [serial_number] - The serial number to be verified.
        [owner_id] - The owner ID.  This is the ExtremeCloud IQ VIQ ID.
        """
        args = {"server_name": server_name,
                "serial_number": serial_number,
                "owner_id": owner_id}

        return self.execute_verify_keyword(server_name, args, self.cmd_const.GET_DEVICE_LIST,
                                           self.parse_const.VERIFY_DEVICE_SERIAL_NUMBER, True,
                                           "The device serial number {serial_number} exists.",
                                           "The device serial number {serial_number} DOES NOT exist!",
                                           **kwargs)
