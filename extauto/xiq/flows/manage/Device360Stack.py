import re
from time import sleep
from extauto.common.AutoActions import AutoActions
from extauto.common.Cli import Cli
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.CommonValidation import CommonValidation
from extauto.xiq.flows.manage.Devices import Devices
from extauto.xiq.flows.common.Navigator import Navigator
from extauto.xiq.elements.Device360WebElements import Device360WebElements
from extauto.xiq.elements.DevicesWebElements import DevicesWebElements


class Device360Stack(Device360WebElements):
    def __init__(self):
        super().__init__()
        self.auto_actions = AutoActions()
        self.cli = Cli()
        self.utils = Utils()
        self.screen = Screen()
        self.dev = Devices()
        self.navigator = Navigator()
        self.dev360 = Device360WebElements()
        self.devices_web_elements = DevicesWebElements()
        self.common_validation = CommonValidation()

    def device360_get_title_stack_info(self):
        """
        - This keyword obtains the value of the Stack Members in device title in the Device360 view.
        - Keyword Usage
        - ``Device360 Get Title Stack Info``
        :return: value of Stack Members in the device title in the Device360 view
        """
        ret_val = ""
        stack_info = self.dev360.get_device360_title_stack_info()
        if stack_info:
            self.utils.print_info(f"Returning Stack Members in device title {stack_info.text}")
            ret_val = re.sub('[^0-9]+', '', stack_info.text)
        else:
            self.utils.print_info("Unable to find the Stack Members info in device title")

        return ret_val

    def get_stack_port_information_on_device(self, spawn, port_num):
        """
        - This keyword gets information from the the Device through cli.
        - It is assumed that the Device spawn is open.
        - Keyword Usage
        - ``Get Stack Port Information on Device  ${SW_SPAWN}    1:4``
        :return: dictionary of information obtained from the Device
        """

        self.utils.print_info("Getting Ports Information of Stack on Device")
        port_info = dict()
        port_info["port_name"] = port_num

        output = self.cli.send_paramiko_cmd(spawn, f"show ports no-refresh | inc \"{port_num} \"")
        status_op = re.search(r"{}\s+(\s+|[\s\w]+)\s+(E|D)\s+(A|R)\s+".format(port_num), output)

        if status_op.group(2) == "E" and status_op.group(3) == "A":
            port_status_info = "CONNECTED"
            self.utils.print_info(f"Port Status on Device is {port_status_info}")
            port_info["port_status"] = port_status_info
        elif status_op.group(2) == "E" and status_op.group(3) == "R":
            port_status_info = "DISCONNECTED"
            self.utils.print_info(f"Port Status on Device is {port_status_info}")
            port_info["port_status"] = port_status_info
        else:
            port_status_info = "DISABLED BY ADMIN"
            port_info["port_status"] = port_status_info

        return port_info

    def device360_get_stack_side_bar_information(self):
        """
        - This keyword gets information from the left sidebar of the Device360 view.
        - It is assumed that the Device360 window is open.
        - Keyword Usage
        - ``Device360 Get Stack Side Bar Information``
        :return: dictionary of information obtained from the left side bar of the Device360 view
        """

        self.utils.print_info("Getting Device360 Left Side Bar Information")
        device360_info = dict()

        device_model_el = self.dev360.get_sidebar_model()
        device_image_el = self.dev360.get_sidebar_device_image()
        host_name_el = self.dev360.get_sidebar_host_name()
        enabled_ports_el = self.dev360.get_sidebar_enabled_ports()
        disabled_ports_el = self.dev360.get_sidebar_disabled_ports()
        connected_el = self.dev360.get_sidebar_connected_state()
        active_el = self.dev360.get_sidebar_active_since()
        alarms_el = self.dev360.get_switch_sidebar_active_alarms()
        clients_el = self.dev360.get_switch_sidebar_unique_clients()
        cpu_el = self.dev360.get_sidebar_cpu_usage()
        mem_el = self.dev360.get_sidebar_memory_usage()

        if device_model_el:
            device360_info["device_model"] = device_model_el.text
        else:
            self.utils.print_info("Could not determine value for Device Model")
            device360_info["device_model"] = ""

        if device_image_el:
            image_src = device_image_el.get_attribute("src")
            device360_info["device_image"] = image_src
        else:
            self.utils.print_info("Could not determine value for Device Image")
            device360_info["device_image"] = ""

        if host_name_el:
            device360_info["host_name"] = host_name_el.text
        else:
            self.utils.print_info("Could not determine value for Host Name")
            device360_info["host_name"] = ""

        if enabled_ports_el:
            device360_info["enabled_ports"] = enabled_ports_el.text
        else:
            self.utils.print_info("Could not determine value for Enabled Ports")
            device360_info["enabled_ports"] = ""

        if disabled_ports_el:
            device360_info["disabled_ports"] = disabled_ports_el.text
        else:
            self.utils.print_info("Could not determine value for Disabled Ports")
            device360_info["disabled_ports"] = ""

        if connected_el:
            device360_info["connected_state"] = connected_el.text
        else:
            self.utils.print_info("Could not determine value for Connected state")
            device360_info["connected_state"] = ""

        if active_el:
            active_text = active_el.text
            # This field is currently in the format "Active since: <Days> <Hrs> <Mins> <secs> Ago" so we want to strip
            # off the prefix label ("Active since:") and the suffix label ("Ago").
            self.utils.print_debug(f"Active Since field is {active_text}")
            active_text = re.sub('Active since: ', '', active_text)
            active_text = re.sub(' Ago', '', active_text)
            self.utils.print_debug(f"Stripped Active Since field is {active_text}")
            device360_info["active_since"] = active_text
        else:
            self.utils.print_info("Could not determine value for Active Since")
            device360_info["active_since"] = ""

        if alarms_el:
            device360_info["active_alarms"] = alarms_el.text
        else:
            self.utils.print_info("Could not determine value for Active Alarms")
            device360_info["active_alarms"] = ""

        if clients_el:
            device360_info["unique_clients"] = clients_el.text
        else:
            self.utils.print_info("Could not determine value for Unique Clients")
            device360_info["unique_clients"] = ""

        if cpu_el:
            device360_info["cpu_usage"] = cpu_el.text
        else:
            self.utils.print_info("Could not determine value for CPU Usage")
            device360_info["cpu_usage"] = ""

        if mem_el:
            device360_info["memory_usage"] = mem_el.text
        else:
            self.utils.print_info("Could not determine value for Memory Usage")
            device360_info["memory_usage"] = ""

        self.utils.print_info("****************** Device360 Left Side Bar Information ************************")
        for key, value in device360_info.items():
            self.utils.print_info(f"{key}: {value}")

        return device360_info

    def device360_get_stack_slot_overview_information(self, slot_number):
        """
        - This keyword gets information from the top bar of the Device360 view.
        - It is assumed that the Device360 window is open.
        - Keyword Usage
        - ``Device360 Get Stack Slot Overview Information   1``
        :return: dictionary of information obtained from the top bar of the Device360 view
        """

        self.utils.print_info("Getting Device360 Top Bar Information of Stack Slot")
        device360_info = dict()
        slot_num = int(slot_number)
        i = slot_num - 1

        uptime_el = self.dev360.get_stack_topbar_uptime()[i]
        temp_el = self.dev360.get_stack_topbar_temperature()[i]
        power_el = self.dev360.get_stack_topbar_power()[i]
        fan_el = self.dev360.get_stack_topbar_fan()[i]
        ip_addr_el = self.dev360.get_stack_topbar_ip_address()[i]
        mac_addr_el = self.dev360.get_stack_topbar_mac_address()[i]
        version_el = self.dev360.get_stack_topbar_software_version()[i]
        model_el = self.dev360.get_stack_topbar_model()[i]
        serial_el = self.dev360.get_stack_topbar_serial()[i]
        make_el = self.dev360.get_stack_topbar_make()[i]
        iqagent_ver_el = self.dev360.get_stack_topbar_iqagent_version()[i]
        mem_status_el = self.dev360.get_stack_topbar_stack_mem_status()[i]

        if i == 0:
            mac_el = self.dev360.get_stack_topbar_mac_usage()[i]
        else:
            mac_el = ""
        if mac_el:
            self.auto_actions.move_to_element(mac_el)
            sleep(2)
            tt_content = self.dev360.get_tooltip_content()
            if tt_content:
                tt_text = tt_content.text
                self.utils.print_debug(f"Tooltip content for MAC Table Utilization is {tt_text}")
                mac_values = tt_text.split(":")
                if len(mac_values) == 2 and mac_values[0] == "MAC Table Utilization":
                    mac_value = mac_values[1].strip()
                    mac_value = re.sub('%', '', mac_value)
                    device360_info["mac_usage"] = mac_value
                else:
                    self.utils.print_info("Unable to parse value for MAC Table Utilization")
                    device360_info["mac_usage"] = ""

        if uptime_el:
            self.auto_actions.move_to_element(uptime_el)
            sleep(2)
            tt_content = self.dev360.get_tooltip_content()
            if tt_content:
                tt_text = tt_content.text
                # This field is currently in the format "Uptime: Last seen: <date>, <time>" so we want to strip
                # off the label ("Uptime: Last seen:"), and remove the comma from the date and time portion.
                # NOTE: This may change when APC-45218 is addressed.
                self.utils.print_debug(f"Tooltip content for Uptime is {tt_text}")
                tt_text = re.sub('Uptime: Last seen: ', '', tt_text)
                self.utils.print_debug(f"Stripped tooltip content for Uptime is {tt_text}")
                uptime_values = tt_text.split(",")
                if len(uptime_values) == 2:
                    uptime_date = uptime_values[0].strip()
                    uptime_time = uptime_values[1].strip()
                    device360_info["uptime"] = uptime_date + " " + uptime_time
                else:
                    self.utils.print_info("Unable to parse value for Uptime")
                    device360_info["uptime"] = ""
            else:
                self.utils.print_info("Could not determine value for Uptime")
                device360_info["uptime"] = ""
        else:
            self.utils.print_info("Could not find Uptime element")
            device360_info["uptime"] = ""

        if temp_el:
            device360_info["temperature"] = temp_el.text
        else:
            self.utils.print_info("Could not determine value for Temperature")
            device360_info["temperature"] = ""

        fan_el = self.dev360.get_stack_topbar_fan()[i]
        if fan_el:
            self.auto_actions.move_to_element(fan_el)
            self.screen.save_screen_shot()
            sleep(20)
            tt_content = self.dev360.get_tooltip_content()
            if tt_content:
                fan_status_text = tt_content.text
                fan_status_text_2 = fan_status_text.split('\n')
                self.utils.print_info(f"Fan status output list is {fan_status_text}")
                fan_status_list = []
                for status in fan_status_text_2:
                    if "Operating" in status:
                        status1 = re.sub('Tray [0-9] Fan [0-9]: ', '', status)
                        fan_status_list.append(status1)
                    else:
                        if "failed" in status:
                            fan_status_list.append("Unit has failed")
                self.utils.print_info(f"Fan status grepped list is {fan_status_list}")
                device360_info["fan_status"] = fan_status_list
            else:
                self.utils.print_info("Could not parse the value for Fan")
                device360_info["fan_status"] = ""
        else:
            self.utils.print_info("Could not determine value for Fan status")
            device360_info["fan_status"] = ""

        if power_el:
            self.auto_actions.move_to_element(power_el)
            sleep(2)
            tt_content = self.dev360.get_tooltip_content()
            if tt_content:
                power_el_text = tt_content.text
                power_supply_text_2 = power_el_text.split('\n')
                power_supply_list = []
                total_power_available = 0
                total_power_consumed = 0
                threshold_power = 0
                for status in power_supply_text_2:
                    if "Total Power Available" in status:
                        total_power_available = re.sub('[^0-9]+', '', status)
                    elif "Total Power Consumed" in status:
                        total_power_consumed = re.sub('[^0-9]+', '', status)
                    elif "Threshold" in status:
                        threshold_power = re.sub('[^0-9]+', '', status)
                    else:
                        if "Power " in status and "Status" not in status:
                            status = re.sub('Power [0-9]: ', '', status)
                            power_supply_list.append(status)
                self.utils.print_info(f"Power supply grepped list in D360 is {power_supply_list}")
                device360_info["power_supply"] = power_supply_list
                device360_info["total_power_available"] = total_power_available
                device360_info["total_power_consumed"] = total_power_consumed
                device360_info["threshold_power"] = threshold_power
            else:
                self.utils.print_info("Could not parse the values for Power")
                device360_info["power_supply"] = ""
                device360_info["total_power_available"] = ""
                device360_info["total_power_consumed"] = ""
                device360_info["threshold_power"] = ""
        else:
            self.utils.print_info("Could not determine values for Power")
            device360_info["power_supply"] = ""
            device360_info["total_power_available"] = ""
            device360_info["total_power_consumed"] = ""
            device360_info["threshold_power"] = ""

        if ip_addr_el:
            ip_addr_text = ip_addr_el.text
            device360_info["ip_address"] = ip_addr_text.split('\n')[-1]
        else:
            self.utils.print_info("Could not determine value for IP Address")
            device360_info["ip_address"] = ""

        if mac_addr_el:
            mac_addr_text = mac_addr_el.text
            device360_info["mac_address"] = mac_addr_text.split('\n')[-1]
        else:
            self.utils.print_info("Could not determine value for MAC Address")
            device360_info["mac_address"] = ""

        if version_el:
            version_text = version_el.text
            device360_info["software_version"] = version_text.split('\n')[-1]
        else:
            self.utils.print_info("Could not determine value for Software Version")
            device360_info["software_version"] = ""

        if model_el:
            model_text = model_el.text
            device_model = model_text.split('\n')[-1]
            device360_info["device_model"] = device_model.replace('-', '', 1)
        else:
            self.utils.print_info("Could not determine value for Device Model")
            device360_info["device_model"] = ""

        if serial_el:
            serial_text = serial_el.text
            device360_info["serial_number"] = serial_text.split('\n')[-1]
        else:
            self.utils.print_info("Could not determine value for Serial Number")
            device360_info["serial_number"] = ""

        if make_el:
            make_text = make_el.text
            device360_info["device_make"] = make_text.split('\n')[-1]
        else:
            self.utils.print_info("Could not determine value for Device Make")
            device360_info["device_make"] = ""

        if iqagent_ver_el:
            iqagent_ver_text = iqagent_ver_el.text
            device360_info["iqagent_version"] = iqagent_ver_text.split('\n')[-1]
        else:
            self.utils.print_info("Could not determine value for IQAgent Version")
            device360_info["iqagent_version"] = ""

        if mem_status_el:
            mem_status_text = mem_status_el.text
            mem_status_text = mem_status_text.split('\n')[-1]
            mem_status_info = re.sub('Slot [0-9]: ', '', mem_status_text)
            device360_info["stack_mem_status"] = mem_status_info
        else:
            self.utils.print_info("Could not determine value for Stack Member Status")
            device360_info["stack_mem_status"] = ""

        self.utils.print_info("****************** Device360 Top Bar Information ************************")
        for key, value in device360_info.items():
            self.utils.print_info(f"{key}: {value}")

        return device360_info

    def device360_get_stack_slot_top_bar_temperature(self, slot_number, **kwargs):
        """
        - This keyword obtains the value of the Temperature field from the top bar in the Device360 view.
        - Keyword Usage
        - ``Device360 Get Stack Slot Top Bar Temperature   1``
        :return: value of the Temperature field from the top bar in the Device360 view
        """
        ret_val = ""
        i = int(slot_number) - 1

        temp_el = self.dev360.get_stack_topbar_temperature()[i]
        if temp_el:
            ret_val = temp_el.text
        else:
            kwargs["fail_msg"] = "Could not determine value for Temperature"
            self.common_validation.failed(**kwargs)

        return ret_val

    def device360_get_stack_slot_top_bar_last_update_time(self, slot_number, **kwargs):
        """
        - This keyword gets information from the left sidebar of the Device360 view.
        - It is assumed that the Device360 window is open.
        - Keyword Usage
        - ``Device360 Get Stack Slot Top Bar Last Update Time     1``
        :return: last update time if successful, otherwise None
        """
        ret_val = ""
        i = int(slot_number) - 1

        self.utils.print_info("Getting Device360 Last Update Time")
        uptime_el = self.dev360.get_stack_topbar_uptime()[i]

        # Workaround - first element moved to isn't being recognized, so move to Memory element first
        mem_el = self.dev360.get_topbar_memory()
        if mem_el:
            self.auto_actions.move_to_element(mem_el)
        if uptime_el:
            # Workaround - first element moved to isn't being recognized, so move twice
            self.auto_actions.move_to_element(uptime_el)
            self.auto_actions.move_to_element(uptime_el)
            sleep(2)
            tt_content = self.dev360.get_tooltip_content()
            if tt_content:
                tt_text = tt_content.text
                # This field is currently in the format "Uptime: Last seen: <date>, <time>" so we want to strip
                # off the label ("Uptime: Last seen:"), and remove the comma from the date and time portion.
                # NOTE: This may change when APC-45218 is addressed.
                self.utils.print_debug(f"Tooltip content for Uptime is {tt_text}")
                tt_text = re.sub('Uptime: Last seen: ', '', tt_text)
                self.utils.print_debug(f"Stripped tooltip content for Uptime is {tt_text}")
                uptime_values = tt_text.split(",")
                if len(uptime_values) == 2:
                    uptime_date = uptime_values[0].strip()
                    uptime_time = uptime_values[1].strip()
                    ret_val = uptime_date + " " + uptime_time
                    self.utils.print_info(f"Returning Last Update Time {ret_val}")
                else:
                    kwargs["fail_msg"] = "Unable to parse value for Uptime"
                    self.common_validation.failed(**kwargs)
            else:
                kwargs["fail_msg"] = "Could not determine value for Uptime"
                self.common_validation.failed(**kwargs)
        else:
            kwargs["fail_msg"] = "Could not find Uptime element"
            self.common_validation.failed(**kwargs)

        return ret_val

    def get_stack_system_information(self, slot_number):
        """
        - This keyword gets Stack Switch information from device360 page
        - It Assumes That Already Navigated to Device360 Page
        - Flow : Device 360 Page
        - Keyword Usage
        - ``Get Stack System Information   1``

        :return: dictionary of Stack Switch information
        """
        i = int(slot_number)
        device360_info = dict()

        self.utils.print_info("Clicking on System Information")
        self.auto_actions.click_reference(self.dev360.get_stack_system_info_button)
        sleep(5)

        unit_number_field = self.dev360.get_stack_system_info_unit_number()[i].text
        if unit_number_field:
            device360_info["unit_number"] = int(unit_number_field.split('\n')[-1])
        else:
            device360_info["unit_number"] = ""

        ip_address_field = self.dev360.get_stack_system_info_ip_address()[i].text
        if ip_address_field:
            device360_info["ip_address"] = ip_address_field.split('\n')[-1]
        else:
            device360_info["ip_address"] = ""

        mac_address_field = self.dev360.get_stack_system_info_mac()[i].text
        if mac_address_field:
            device360_info["mac_address"] = mac_address_field.split('\n')[-1]
        else:
            device360_info["mac_address"] = ""

        serial_number_field = self.dev360.get_stack_system_info_serial_num()[i].text
        if serial_number_field:
            device360_info["serial_number"] = serial_number_field.split('\n')[-1]
        else:
            device360_info["serial_number"] = ""

        device_prod_type_field = self.dev360.get_stack_system_info_prod_type()[i].text
        if device_prod_type_field:
            val1 = device_prod_type_field.split('\n')[-1]
            val2 = val1.replace('_', '-', 3)
            val3 = val2.replace('-', '', 1)
            device_prod_type = val3.replace('_', '')
            device360_info["prod_type"] = device_prod_type
        else:
            device360_info["prod_type"] = ""

        device_make_field = self.dev360.get_stack_system_info_make()[i].text
        if device_make_field:
            device360_info["device_make"] = device_make_field.split('\n')[-1]
        else:
            device360_info["device_make"] = ""

        device_state_field = self.dev360.get_stack_system_info_admin_state()[i].text
        if device_state_field:
            device360_info["device_state"] = device_state_field.split('\n')[-1]
        else:
            device360_info["device_state"] = ""

        software_version_field = self.dev360.get_stack_system_info_software_ver()[i].text
        if software_version_field:
            device360_info["software_version"] = software_version_field.split('\n')[-1]
        else:
            device360_info["software_version"] = ""

        stack_mgmt_status_field = self.get_stack_system_info_stack_mgmt_status()[i].text
        if stack_mgmt_status_field:
            device360_info["stack_mgmt_status"] = stack_mgmt_status_field.split('\n')[-1]
        else:
            device360_info["stack_mgmt_status"] = ""

        self.utils.print_info("****************** Stack System Information ************************")
        for key, value in device360_info.items():
            self.utils.print_info(f"{key}:{value}")

        return device360_info

    def device360_stack_get_port_icon_count(self, **kwargs):
        """
        - This keyword gets the number of port icons displayed for Stack in the Device360 view.
        - It is assumed that the Device360 window is open.
        - Keyword Usage
        - ``Device360 Stack Get Port Icon Count``
        :return: number of port icons displayed in the Device360 view
        """
        ret_val = 0

        self.utils.print_info("Getting Device360 Stack Port Icon Count")

        port_icon_list = self.dev360.get_stack_overview_port_icons()
        if port_icon_list:
            ret_val = len(port_icon_list)
            self.utils.print_info(f"Stack port icon list {ret_val}")
        else:
            kwargs["fail_msg"] = "Unable to get the list of port icons"
            self.common_validation.failed(**kwargs)

        return ret_val

    def device360_stack_overview_select_port(self, port_num):
        """
        - This keyword selects the specified port on the Monitor> Diagnostics page.
          It assumes the Device360 Window is open and on the Monitor> Diagnostics tab.
        - Keyword Usage:
        - ``Device360 Stack Overview Select Port    3``
        :param  port_num    specifies which port to select
        :return: none
        """
        port_slot = re.sub(':[0-9]+', '', port_num)
        self.utils.print_info(f"Port Slot is {port_slot}")
        port_num_index = re.sub('[0-9]:', '', port_num)

        port_slot_row = self.get_stack_overview_slot_ports_row()[int(port_slot)-1]
        port_list = self.get_device360_stack_overview_slot_ports(port_slot_row)
        port_clicked = self.auto_actions.click(port_list[int(port_num_index) - 1])

        self.screen.save_screen_shot()
        if not port_clicked:
            self.utils.print_info(f"Port '{port_num}' is already selected")

    def get_stack_port_table_information(self, port_num):
        """
        - This keyword gets Stack port table information from device360 page
        - It Assumes That Already Navigated to Device360 Page and Port is selected
        - Flow : Device 360 Page
        - Keyword Usage
        - ``Get Stack Port Table Information``

        :return: dictionary of Stack Switch information
        """
        device360_info = dict()

        self.utils.print_info("Getting Port Table Information")

        sleep(5)
        port_name = ""
        for i in range(1, 4):
            port_name = self.dev360.get_device360_stack_port_table_port_name().text
            self.screen.save_screen_shot()
            if port_name == port_num:
                self.utils.print_info("Port Name Displayed is same as the Port Number Selected")
                break
            else:
                sleep(20)

        self.utils.print_info(f"Port Name Displayed is {port_name} and Port Number Selected is {port_num}")

        if port_name == port_num:
            device360_info["port_name"] = self.dev360.get_device360_stack_port_table_port_name().text
            device360_info["port_type"] = self.dev360.get_device360_stack_port_table_port_type().text
            device360_info["port_status"] = self.dev360.get_device360_stack_port_table_port_status().text
            device360_info["port_mode"] = self.dev360.get_device360_stack_port_table_port_mode().text
            device360_info["port_speed"] = self.dev360.get_device360_stack_port_table_port_speed().text
        else:
            device360_info["port_name"] = ""
            device360_info["port_type"] = ""
            device360_info["port_status"] = ""
            device360_info["port_mode"] = ""
            device360_info["port_speed"] = ""

        self.utils.print_info("****************** Stack Port Table Information ************************")
        for key, value in device360_info.items():
            self.utils.print_info(f"{key}:{value}")

        return device360_info

    def get_switch_stack_device360_port_table_information(self, device_mac="", device_name="", port_number="", **kwargs):
        """
        - This keyword gets EXOS/VOSS Switch stack Port table information from device360 page
        - Flow : Manage --> Devices--> Select Device stack-->Device stack 360 Page
        - Keyword Usage
        - ``Get Switch Stack Device360 Port Table Information  device_mac={DEVICE_MAC}  port_number={PORT_NUMBER} ``
        - ``Get Switch Stack Device360 Port Table Information  device_name={DEVICE_NAME}  port_number={PORT_NUMBER} ``
         :param device_mac: Device Stack Mac Address
         :param device_name: Device Stack Name
         :param port_number: Port Number of the Switch Stack

        :return: Dictionary of Port Table Information if port found else -1
        """

        if device_mac:
            self.utils.print_info("Checking Search Result with Device Mac : ", device_mac)
            device_row = self.dev.get_device_row(device_mac=device_mac)
            if device_row:
                self.navigator.navigate_to_device360_page_with_mac(device_mac)
                sleep(8)

        if device_name:
            self.utils.print_info("Checking Search Result with Device Name : ", device_name)
            device_row = self.dev.get_device_row(device_name=device_name)
            if device_row:
                self.navigator.navigate_to_device360_page_with_host_name(device_name)
                sleep(8)

        if view_log := self.get_d360_switch_port_view_all_pages_button():
            if view_log.is_displayed():
                self.utils.print_info("Click Full pages button")
                self.auto_actions.click_reference(self.get_d360_switch_port_view_all_pages_button)
                self.screen.save_screen_shot()
                sleep(4)

        count = 1
        switch_stack_device360_info = dict()
        while count < 10:
            self.utils.print_info(f"Checking Port Number on Page Number {count}")
            rows = self.get_d360_switch_ports_table_grid_rows()
            if rows:
                for row in rows:
                    port_name_cell = self.get_d360_switch_ports_table_interface_port_name_cell(row).text
                    if port_number == port_name_cell:
                        self.utils.print_info("Getting Port Table Information")
                        switch_stack_device360_info[
                            "port_name"] = self.dev360.get_device360_switch_port_table_port_name(row).text
                        switch_stack_device360_info[
                            "port_type"] = self.dev360.get_device360_switch_port_table_port_type(row).text
                        switch_stack_device360_info[
                            "lldp_neighbor"] = self.dev360.get_device360_switch_port_table_lacp_neighbor(
                            row).text
                        switch_stack_device360_info[
                            "lldp_status"] = self.dev360.get_device360_switch_port_table_lacp_status(
                            row).text
                        switch_stack_device360_info[
                            "port_status"] = self.dev360.get_device360_switch_port_table_port_status(
                            row).text
                        switch_stack_device360_info[
                            "trasmission_mode"] = self.dev360.get_device360_switch_port_table_transmission_mode(
                            row).text
                        switch_stack_device360_info[
                            "port_mode"] = self.dev360.get_device360_switch_port_table_port_mode(row).text
                        switch_stack_device360_info[
                            "access_vlan"] = self.dev360.get_device360_switch_port_table_access_vlan(
                            row).text
                        if self.dev360.get_device360_switch_port_table_tagged_vlans(row):
                            switch_stack_device360_info[
                                "tagged_vlans"] = self.dev360.get_device360_switch_port_table_tagged_vlans(row).text
                        switch_stack_device360_info[
                            "traffic_received"] = self.dev360.get_device360_switch_port_table_traffic_received(row).text
                        switch_stack_device360_info[
                            "traffic_transmitted"] = self.dev360.get_device360_switch_port_table_traffic_transmitted(
                            row).text
                        switch_stack_device360_info[
                            "power_used"] = self.dev360.get_device360_switch_port_table_power_used(
                            row).text
                        switch_stack_device360_info[
                            "port_speed"] = self.dev360.get_device360_switch_port_table_port_speed(
                            row).text

                        self.utils.print_info( "************** Switch Port Table Information ********************")
                        for key, value in switch_stack_device360_info.items():
                            self.utils.print_info(f"{key}:{value}")

                        self.screen.save_screen_shot()
                        self.auto_actions.click_reference(self.dev360.get_close_dialog)
                        self.screen.save_screen_shot()
                        return switch_stack_device360_info

                self.utils.print_info(f"Port Not Found on Page Number {count} and Checking on Page Number {count+1}")
                page_next_button = self.get_device360_pagination_next_button()
                pagination_page_button = self.get_device360_pagination_page_button()

                if page_next_button.is_displayed():
                    self.auto_actions.click(page_next_button)
                    self.screen.save_screen_shot()
                    count += 1
                    sleep(8)
                else:
                    self.auto_actions.click(pagination_page_button)
                    self.screen.save_screen_shot()
                    count += 1
                    sleep(8)

            else:
                kwargs['fail_msg'] = "Unable to get Port Table Information"
                self.screen.save_screen_shot()
                self.auto_actions.click_reference(self.dev360.get_close_dialog)
                self.screen.save_screen_shot()
                self.common_validation.failed(**kwargs)
                return -1
