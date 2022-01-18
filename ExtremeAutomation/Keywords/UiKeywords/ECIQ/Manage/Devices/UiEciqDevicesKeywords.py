from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.ECIQ.EciqdevicesConstants import EciqdevicesConstants


class UiEciqDevicesKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiEciqDevicesKeywords, self).__init__()
        self.api_const = self.constants.API_ECIQ_DEVICES
        self.command_const = EciqdevicesConstants()

    def eciq_devices_check_device_checkbox(self, element_name, host_name, serial_number, status, **kwargs):
        """
        Checks or unchecks the device checkbox using hostname and serial number.
        Returns the result of devices_check_device_checkbox.
        [element_name] - The UI element(s) the keyword should be run against.
        [host_name] - The hostname of the device with the checkbox to be checked/unchecked.
        [serial_number] - The serial number of the device with the checkbox to be checked/unchecked.
        [status] - If status is true, checkbox should be checked.  If status is false, checkbox should not be checked.
        """
        args = {"host_name": host_name,
                "serial_number": serial_number,
                "status": status}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_CHECK_DEVICE_CHECKBOX, **kwargs)

    def eciq_devices_clear_device_search(self, element_name, **kwargs):
        """
        Clears the entry from the device search box.
        Returns the result of devices_clear_device_search.
        [element_name] - The UI element(s) the keyword should be run against.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_CLEAR_DEVICE_SEARCH, **kwargs)

    def eciq_devices_click_add_and_select_advanced_onboarding(self, element_name, **kwargs):
        """
        Clicks Add button and selects Advanced Onboarding option.
        Returns the result of devices_click_add_and_select_advanced_onboarding.
        [element_name] - The UI element(s) the keyword should be run against.
        """
        args = {}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DEVICES_CLICK_ADD_AND_SELECT_ADVANCED_ONBOARDING, **kwargs)

    def eciq_devices_click_refresh(self, element_name, **kwargs):
        """
        Refreshes the devices page.
        Returns the result of devices_click_refresh.
        [element_name] - The UI element(s) the keyword should be run against.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_CLICK_REFRESH, **kwargs)

    def eciq_devices_delete_device(self, element_name, host_name, serial_number, **kwargs):
        """
        Selects the checkbox of the device to be deleted.  Then deletes the selected device.
        Returns the result of devices_delete_device.
        [element_name] - The UI element(s) the keyword should be run against.
        [host_name] - The hostname of the device to be deleted.
        [serial_number] - The serial number of the device to be deleted.
        """
        args = {"host_name": host_name,
                "serial_number": serial_number}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_DELETE_DEVICE, **kwargs)

    def eciq_devices_monitor_dialog_click_close(self, element_name, **kwargs):
        """
        Closes the devices monitor dialog popup.
        Returns the result of devices_monitor_dialog_click_close.
        [element_name] - The UI element(s) the keyword should be run against.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_MONITOR_DIALOG_CLICK_CLOSE, **kwargs)

    def eciq_devices_monitor_dialog_click_refresh(self, element_name, **kwargs):
        """
        Refreshes the devices monitor dialog popup.
        Returns the result of devices_monitor_dialog_click_refresh.
        [element_name] - The UI element(s) the keyword should be run against.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_MONITOR_DIALOG_CLICK_REFRESH,
                                    **kwargs)

    def eciq_devices_monitor_dialog_select_port(self, element_name, device_type, port_name, **kwargs):
        """
        Selects the port on the device in the devices monitor dialog popup.
        Returns the result of devices_monitor_dialog_select_port.
        [element_name] - The UI element(s) the keyword should be run against.
        [device_type] - The type of device (Aerohive, EXOS, VOSS).
        [port_name] - The port to be selected on the device.
        """
        args = {"device_type": device_type,
                "port_name": port_name}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_MONITOR_DIALOG_SELECT_PORT, **kwargs)

    def eciq_devices_select_device_by_hostname_and_ip(self, element_name, host_name, mgmt_ip, timeout="1", retry="60",
                                                      **kwargs):
        """
        Selects the device by hostname and mgmt IP address.
        Returns the result of devices_select_device_by_hostname_and_ip.
        [element_name] - The UI element(s) the keyword should be run against.
        [host_name] - The hostname of the device to be selected.
        [mgmt_ip] - The mgmt IP of the device to be selected.
        [timeout] - The webdriver_wait timeout for each retry attempt.  The default is 1 second.
        [retry] - The number of retry attempts.  The default is 60 retry attempts.
        """
        args = {"host_name": host_name,
                "mgmt_ip": mgmt_ip,
                "timeout": timeout,
                "retry": retry}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_SELECT_DEVICE_BY_HOSTNAME_AND_IP,
                                    **kwargs)

    def eciq_devices_select_device_by_hostname_and_serial_number(self, element_name, host_name, serial_number,
                                                                 timeout="1", retry="60", **kwargs):
        """
        Selects the device by hostname and serial number.
        Returns the result of devices_select_device_by_hostname_and_serial_number.
        [element_name] - The UI element(s) the keyword should be run against.
        [host_name] - The hostname of the device to be selected.
        [serial_number] - The serial number of the device to be selected.
        [timeout] - The webdriver_wait timeout for each retry attempt.  The default is 1 second.
        [retry] - The number of retry attempts.  The default is 60 retry attempts.
        """
        args = {"host_name": host_name,
                "serial_number": serial_number,
                "timeout": timeout,
                "retry": retry}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DEVICES_SELECT_DEVICE_BY_HOSTNAME_AND_SERIAL_NUMBER, **kwargs)

    def eciq_devices_select_device_count_per_page(self, element_name, device_count, **kwargs):
        """
        Selects the number of devices to be displayed per page.
        Returns the result of devices_select_device_count_per_page.
        [element_name] - The UI element(s) the keyword should be run against.
        [device_count] - The number of devices to be displayed per page.
        """
        args = {"device_count": device_count}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_SELECT_DEVICE_COUNT_PER_PAGE,
                                    **kwargs)

    def eciq_devices_verify_device_firmware(self, element_name, firmware_version, **kwargs):
        """
        Verifies the firmware version on the device.
        Returns the result of devices_verify_device_firmware.
        [element_name] - The UI element(s) the keyword should be run against.
        [firmware_version] - The firmware version to be verified.
        """
        args = {"firmware_version": firmware_version}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_VERIFY_DEVICE_FIRMWARE, **kwargs)

    def eciq_devices_verify_device_ip(self, element_name, mgmt_ip, **kwargs):
        """
        Verifies the mgmt IP address on the device.
        Returns the result of devices_verify_device_ip.
        [element_name] - The UI element(s) the keyword should be run against.
        [mgmt_ip] - The mgmt IP to be verified.
        """
        args = {"mgmt_ip": mgmt_ip}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_VERIFY_DEVICE_IP, **kwargs)

    def eciq_devices_verify_device_iq_agent_version(self, element_name, iq_agent_version, **kwargs):
        """
        Verifies the IQ Agent version.
        Returns the result of devices_verify_device_iq_agent_version.
        [element_name] - The UI element(s) the keyword should be run against.
        [iq_agent_version] - The IQ Agent version to be verified.
        """
        args = {"iq_agent_version": iq_agent_version}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_VERIFY_DEVICE_IQ_AGENT_VERSION,
                                    **kwargs)

    def eciq_devices_verify_device_mac(self, element_name, mac_addr, **kwargs):
        """
        Verifies the MAC address on the device.
        Returns the result of devices_verify_device_mac.
        [element_name] - The UI element(s) the keyword should be run against.
        [mac_addr] - The MAC address to be verified.
        """
        args = {"mac_addr": mac_addr}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_VERIFY_DEVICE_MAC, **kwargs)

    def eciq_devices_verify_device_model(self, element_name, model, **kwargs):
        """
        Verifies the device model.
        Returns the result of devices_verify_device_model.
        [element_name] - The UI element(s) the keyword should be run against.
        [model] - The device model to be verified.
        """
        args = {"model": model}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_VERIFY_DEVICE_MODEL, **kwargs)

    def eciq_devices_verify_device_serial_number(self, element_name, serial_number, **kwargs):
        """
        Verifies the serial number of the device.
        Returns the result of devices_verify_device_serial_number.
        [element_name] - The UI element(s) the keyword should be run against.
        [serial_number] - The serial number to be verified.
        """
        args = {"serial_number": serial_number}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_VERIFY_DEVICE_SERIAL_NUMBER,
                                    **kwargs)

    def eciq_devices_verify_device_vendor(self, element_name, vendor, **kwargs):
        """
        Verifies the device vendor.
        Returns the result of devices_verify_device_vendor.
        [element_name] - The UI element(s) the keyword should be run against.
        [vendor] - The vendor to be verified.
        """
        args = {"vendor": vendor}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_VERIFY_DEVICE_VENDOR, **kwargs)

    def eciq_devices_verify_port_lacp_status(self, element_name, lacp_status, **kwargs):
        """
        Verifies the lacp status of the port.
        Returns the result of devices_verify_port_lacp_status.
        [element_name] - The UI element(s) the keyword should be run against.
        [lacp_status] - The lacp status to be verified.
        """
        args = {"lacp_status": lacp_status}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_VERIFY_PORT_LACP_STATUS, **kwargs)

    def eciq_devices_verify_port_mode(self, element_name, port_mode, **kwargs):
        """
        Verifies the mode of the port.
        Returns the result of devices_verify_port_mode.
        [element_name] - The UI element(s) the keyword should be run against.
        [port_mode] - The port mode to be verified.
        """
        args = {"port_mode": port_mode}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_VERIFY_PORT_MODE, **kwargs)

    def eciq_devices_verify_port_name(self, element_name, port_name, **kwargs):
        """
        Verifies the port name on the device.
        Returns the result of devices_verify_port_name.
        [element_name] - The UI element(s) the keyword should be run against.
        [port_name] - The port name to be verified.
        """
        args = {"port_name": port_name}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_VERIFY_PORT_NAME, **kwargs)

    def eciq_devices_verify_port_power_used(self, element_name, power_used, **kwargs):
        """
        Verifies the power used on the port.
        Returns the result of devices_verify_port_power_used.
        [element_name] - The UI element(s) the keyword should be run against.
        [power_used] - The power used to be verified.
        """
        args = {"power_used": power_used}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_VERIFY_PORT_POWER_USED, **kwargs)

    def eciq_devices_verify_port_speed(self, element_name, port_speed, **kwargs):
        """
        Verifies the speed of the port.
        Returns the result of devices_verify_port_speed.
        [element_name] - The UI element(s) the keyword should be run against.
        [port_speed] - The port speed to be verified.
        """
        args = {"port_speed": port_speed}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_VERIFY_PORT_SPEED, **kwargs)

    def eciq_devices_verify_port_status(self, element_name, port_status, **kwargs):
        """
        Verifies the status of the port.
        Returns the result of devices_verify_port_status.
        [element_name] - The UI element(s) the keyword should be run against.
        [port_status] - The port status to be verified.
        """
        args = {"port_status": port_status}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_VERIFY_PORT_STATUS, **kwargs)

    def eciq_devices_verify_port_traffic_rx(self, element_name, traffic_rx, **kwargs):
        """
        Verifies the traffic received on the port.
        Returns the result of devices_verify_port_traffic_rx.
        [element_name] - The UI element(s) the keyword should be run against.
        [traffic_rx] - The traffic received (in packets) to be verified.
        """
        args = {"traffic_rx": traffic_rx}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_VERIFY_PORT_TRAFFIC_RX, **kwargs)

    def eciq_devices_verify_port_traffic_tx(self, element_name, traffic_tx, **kwargs):
        """
        Verifies the traffic transmitted on the port.
        Returns the result of devices_verify_port_traffic_tx.
        [element_name] - The UI element(s) the keyword should be run against.
        [traffic_tx] - The traffic transmitted (in packets) to be verified.
        """
        args = {"traffic_tx": traffic_tx}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_VERIFY_PORT_TRAFFIC_TX, **kwargs)

    def eciq_devices_verify_port_type(self, element_name, port_type, **kwargs):
        """
        Verifies the port type.
        Returns the result of devices_verify_port_type.
        [element_name] - The UI element(s) the keyword should be run against.
        [port_type] - The port type to be verified.
        """
        args = {"port_type": port_type}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_VERIFY_PORT_TYPE, **kwargs)

    def eciq_devices_verify_port_vlan(self, element_name, port_vlan, **kwargs):
        """
        Verifies the VLAN assigned on the port.
        Returns the result of devices_verify_port_vlan.
        [element_name] - The UI element(s) the keyword should be run against.
        [port_vlan] - The VLAN to be verified.
        """
        args = {"port_vlan": port_vlan}

        return self.execute_keyword(element_name, args, self.command_const.DEVICES_VERIFY_PORT_VLAN, **kwargs)

    def eciq_devices_verify_serial_number_does_not_exist(self, element_name, serial_number, **kwargs):
        """
        Verifies the serial number of the device does not exist using the device search box.
        Returns the result of devices_verify_serial_number_does_not_exist.
        [element_name] - The UI element(s) the keyword should be run against.
        [serial_number] - The serial number to be verified.
        """
        args = {"serial_number": serial_number}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DEVICES_VERIFY_SERIAL_NUMBER_DOES_NOT_EXIST, **kwargs)

    def eciq_devices_verify_serial_number_exists(self, element_name, serial_number, **kwargs):
        """
        Verifies the serial number of the device exists using the device search box.
        Returns the result of devices_verify_serial_number_exists.
        [element_name] - The UI element(s) the keyword should be run against.
        [serial_number] - The serial number to be verified.
        """
        args = {"serial_number": serial_number}

        return self.execute_keyword(element_name, args,
                                    self.command_const.DEVICES_VERIFY_SERIAL_NUMBER_EXISTS, **kwargs)
