from time import sleep
import re

from extauto.common.AutoActions import AutoActions
from extauto.common.CloudDriver import CloudDriver
from extauto.common.CommonValidation import CommonValidation
from extauto.common.Screen import Screen
from extauto.common.Utils import Utils
from extauto.common.WebElementHandler import WebElementHandler
import extauto.xiq.flows.common.ToolTipCapture as tool_tip
from extauto.xiq.flows.common.Navigator import Navigator
from extauto.xiq.elements.DeviceConfigElements import DeviceConfigElements
from extauto.xiq.elements.DevicesWebElements import DevicesWebElements
from extauto.xiq.elements.CommonObjectsWebElements import CommonObjectsWebElements
from extauto.xiq.flows.common.DeviceCommon import DeviceCommon

from extauto.xiq.flows.manage.Tools import Tools
from extauto.xiq.flows.manage.Devices import Devices


class DeviceConfig(DeviceConfigElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.navigator = Navigator()
        self.screen = Screen()
        self.auto_actions = AutoActions()
        self.device_common = DeviceCommon()
        self.web = WebElementHandler()
        self.devices_web_elements = DevicesWebElements()
        # self.driver = extauto.common.CloudDriver.cloud_driver
        self.cobj_web_elements = CommonObjectsWebElements()
        self.common_validation = CommonValidation()
        self.tools = Tools()
        self.devices = Devices()
        self.cloud_driver = CloudDriver()

    def _override_wifi0_psk_ssid_settings(self, **override_args):
        """
        - Override the SSID Broadcast name , PSK password and cwp for WiFi0 interface

        :param override_args: override parameter dict
        :return: 1
        """
        ssid_broadcast_name = override_args.get('override_ssid_broadcast_name')
        override_psk_password = override_args.get('override_psk_password')
        # Commented on 1/18/23 because it is unused
        # reassign_cwp = override_args.get('reassign_cwp')

        self.utils.print_info("Click on WiFi0 interface tab")
        self.auto_actions.click_reference(self.get_wifi0_interface_tab)

        self.utils.print_info(f"overriding ssid broadcast name:{ssid_broadcast_name}")
        self.auto_actions.send_keys(self.get_override_wifi0_ssid_broadcast_ssid_field(), ssid_broadcast_name)

        self.utils.print_info(f"overriding the psk password:{override_psk_password}")
        self.auto_actions.send_keys(self.get_override_wifi0_psk_password(), override_psk_password)
        # @to do for cwp re-assign

    def _override_wifi1_psk_ssid_settings(self, **override_args):
        """
        - Override the SSID Broadcast name , PSK password and cwp for WiFi0 interface

        :param override_args: override parameter dict
        :return: 1
        """
        pass

    def _override_wifi2_psk_ssid_settings(self, **override_args):
        """
        - Override the SSID Broadcast name , PSK password and cwp for WiFi0 interface

        :param override_args: override parameter dict
        :return: 1
        """
        pass

    def _go_to_wireless_interface_settings_page(self):
        """
        - Go to configure --> interface settings tab
        :return:
        """
        self.utils.print_info("Click on wireless interfaces toggle button")
        sleep(5)
        if self.get_wireless_interface_toggle():
            self.auto_actions.click_reference(self.get_wireless_interface_toggle)
            self.utils.print_info("able to click toggle")

    def override_client_mode_in_device_config(self, device_mac, interface, client_mode_profile, **kwargs):
        """
        - This keyword is used to modify or override the client mode settings in wireless interface settings page
        - override wireless interface settings includes client mode options of radio usage
        - Flow: Manage --> Devices --> Select single device -->  Select interface setting tab --> Wireless Interfaces
        - Keyword Usage:
        - ``Override PSK SSID Settings     device_mac=${DEVICE}   interface=WiFi0   ${client_mode_profile}``
        - ``Override PSK SSID Settings     device_mac=${DEVICE}   interface=WiFi1   ${client_mode_profile}``

        :param device_mac:  device mac
        :param interface: device interface i.e WiFi0/WiFi1
        :param client_mode_profile: override config dict
        :return: 1 if interface setting updated success else -1
        """
        self.utils.print_info("Navigating to device 360 page")
        if self.navigator.navigate_to_device360_page_with_mac(device_mac) == -1:
            kwargs['fail_msg'] = f"Device not found in the device row grid with mac:{device_mac}"
            self.common_validation.failed(**kwargs)
            return -1
        self.utils.print_info("click on configuration tab")
        self.auto_actions.click_reference(self.get_configuration_tab)
        self.utils.print_info("Click on interface settings tab")
        self.auto_actions.click_reference(self.get_interface_settings_tab)
        self._go_to_wireless_interface_settings_page()
        sleep(3)
        self.auto_actions.click_reference(self.get_wifi0_interface_tab)
        self.auto_actions.click_reference(self.get_override_client_access_wifi0_checked)
        self.auto_actions.click_reference(self.get_override_client_access_wifi0_checked)
        self.auto_actions.click_reference(self.get_interface_settings_save_button)
        sleep(3)
        self._go_to_wireless_interface_settings_page()
        sleep(2)

        if   interface.lower() == 'wifi0':
            self.utils.print_info("Click on WiFi0 interface tab")
            self.auto_actions.click_reference(self.get_wifi0_interface_tab)
            self.utils.print_info("Click enable Client Mode Checkbox")
            self.auto_actions.click_reference(self.get_override_client_mode_wifi0_checked)
            sleep(3)
            self.auto_actions.scroll_down()
            self.utils.print_info("Click Add(+)")
            self.auto_actions.click_reference(self.get_override_add_client_mode_wifi0_profile)
        elif interface.lower() == 'wifi1':
            self.utils.print_info("Click on WiFi1 interface tab")
            self.auto_actions.click_reference(self.get_wifi1_interface_tab)
            self.utils.print_info("Click enable Client Mode Checkbox")
            self.auto_actions.click_reference(self.get_override_client_mode_wifi1_checked)
            sleep(3)
            self.auto_actions.scroll_down()
            self.utils.print_info("Click Add(+)")
            self.auto_actions.click_reference(self.get_override_add_client_mode_wifi1_profile)
        else:
            self.utils.print_info("Can you specify interface(wifi0 or wifi1)?")

        self._override_client_mode_wifi0_1(client_mode_profile)
        sleep(3)
        self.utils.print_info("Click on interface settings save button")
        self.auto_actions.click_reference(self.get_interface_settings_save_button)
        sleep(5)
        self.screen.save_screen_shot()
        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)
        self.utils.print_info("Close the device360 page dialog window")
        self.auto_actions.click_reference(self.get_close_device360_dialog_window)

        if 'Interface Settings were updated successfully.' in tool_tp_text:
            kwargs['pass_msg'] = "interface setting updated success"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "interface setting updated unsuccess"
            self.common_validation.failed(**kwargs)
            return -1

    def _override_client_mode_wifi0_1(self, client_mode_profile):
        """
        - Get the override client mode wifi0 and 1
        :return:
        """
        client_mode_profile_name = client_mode_profile['client_mode_profile_name']
        dhcp_server_scope = client_mode_profile['dhcp_server_scope']
        cm_enable_local_web_page = client_mode_profile.get('local_web_page', 'ENABLE')
        cm_ssid_name = client_mode_profile.get('ssid_name', 'bk_enterprise')
        cm_password = client_mode_profile.get('password', 'aerohive')
        cm_auth_method = client_mode_profile.get('auth_method', 'Pre-Shared Key')
        cm_key_type = client_mode_profile.get('key_type', 'ASCII')

        self.utils.print_info(f"Enter Client Mode Profile Name: {client_mode_profile_name}")
        self.auto_actions.send_keys(self.get_override_wifi0_1_client_mode_profile_name(), client_mode_profile_name)
        if cm_enable_local_web_page.upper() == 'DISABLE':
            self.utils.print_info(f"Enable Local Web Page: {cm_enable_local_web_page}")
            self.auto_actions.click_reference(self.get_override_wifi0_1_cm_local_web_page_checkbox)
            self.utils.print_info("Click Add(+)")
            self.auto_actions.click_reference(self.get_override_wifi0_1_cm_local_web_page_add)
            self.utils.print_info(f"Enter SSID Name: {cm_ssid_name}")
            self.auto_actions.send_keys(self.get_override_wifi0_1_cm_local_web_page_ssid_textbox(), cm_ssid_name)
            self.utils.print_info(f"Enter Password: {cm_password}")
            self.auto_actions.send_keys(self.get_override_wifi0_1_cm_local_web_page_password_textbox(), cm_password)
            self.utils.print_info(f"Auth Method: {cm_auth_method}")
            self.auto_actions.click_reference(self.get_override_wifi0_1_cm_local_web_page_auth_dropdown)
            self.auto_actions.select_drop_down_options(self.get_override_wifi0_1_cm_local_web_page_auth_dropdown_option(), cm_auth_method)
            self.utils.print_info(f"Key Type: {cm_key_type}")
            self.auto_actions.click_reference(self.get_override_wifi0_1_cm_local_web_key_type_dropdown)
            self.auto_actions.select_drop_down_options(self.get_override_wifi0_1_cm_local_web_key_type_dropdown_option(), cm_key_type)
            self.screen.save_screen_shot()
            sleep(2)
            self.utils.print_info("Click Add button")
            self.auto_actions.click_reference(self.cobj_web_elements.get_common_object_wifi0_1_cm_local_web_page_add_button)
        self.utils.print_info(f"Enter DHCP Server Scope: {dhcp_server_scope}")
        self.auto_actions.send_keys(self.get_override_wifi0_1_client_mode_profile_dhcp_server_scope(), dhcp_server_scope)
        self.screen.save_screen_shot()
        self.utils.print_info("Click Save Client Mode Profile")
        self.auto_actions.click_reference(self.get_override_wifi0_1_client_mode_profile_save)

    def override_psk_ssid_settings(self, device_serials='', *override_args, **kwargs):
        """
        - This keyword is used to modify or override the psk ssid settings in wireless interface settings page
        - override wireless interface settings includes SSID Broadcast name, PSK password, reassigning the cwp
        - Flow: Manage --> Devices --> Select the multiple device --> click on edit button --> Select the interface setting tab
        - This keyword will work only with psk network policy applied to multiple devices devices
        - Keyword Usage:
        - ``Override PSK SSID Settings     device_serials=${DEVICE1},${DEVICE2}    &{OVERRIDE_ARGS}``
        - ``Override PSK SSID Settings     device_serials=${DEVICE1},${DEVICE2}    interface=WiFi0    override_ssid_broadcast_name=${NEW_SSID_NAME}``
        - ``Override PSK SSID Settings     device_serials=${DEVICE1},${DEVICE2}    interface=WiFi0    override_psk_password=${NEW_PSK_PASSWORD}``
        - ``Override PSK SSID Settings     device_serials=${DEVICE1},${DEVICE2}    interface=WiFi0    reassign_cwp=${NEW_CWP_NAME}``

        :param override_args: override psk config dict
        :param device_serials: device serial number to select
        :return: 1 if interface setting updated success else -1
        """
        interface = override_args.get('interface')

        if len(device_serials.split(',')) == 1:
            self.utils.print_info("This keyword works with multiple devices")
            self.utils.print_info("Pass te device serial numbers with comma separated")
            return -1

        self.navigator.navigate_to_multiple_device_configuration_page(device_serials)
        sleep(5)

        self.utils.print_info("Click on interface settings tab")
        self.auto_actions.click_reference(self.get_interface_settings_tab)

        self._go_to_wireless_interface_settings_page()

        if interface == "WiFi0":
            self._override_wifi0_psk_ssid_settings(**override_args)

        if interface == "WiFi1":
            self._override_wifi1_psk_ssid_settings(**override_args)

        if interface == "WiFi2":
            self._override_wifi2_psk_ssid_settings(**override_args)

        self.utils.print_info("Click on interface settings save button")
        self.auto_actions.click_reference(self.get_interface_settings_save_button)
        sleep(5)

        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)
        for text in tool_tp_text:
            if "Interface Settings were updated successfully" in text:
                kwargs['pass_msg'] = f"{text}"
                self.common_validation.passed(**kwargs)
                return 1

    def _get_override_wifi0_psk_ssid_settings(self):
        """
        - Get the override ssid settings
        :return: ovr_psk_password, ovr_psk_password
        """
        self.utils.print_info("Click on WiFi0 interface tab")
        self.auto_actions.click_reference(self.get_wifi0_interface_tab)

        ovr_ssid_brdcst_name = self.get_override_wifi0_ssid_broadcast_ssid_field().get_attribute("value")
        self.utils.print_info(f"Override ssid broadcast name:{ovr_ssid_brdcst_name}")

        ovr_psk_password = self.get_override_wifi0_psk_password().get_attribute("value")
        self.utils.print_info(f"Override psk password:{ovr_psk_password}")

        return ovr_ssid_brdcst_name, ovr_psk_password

    def get_override_psk_ssid_settings(self, device_mac, interface, **kwargs):
        """
        - This keyword works only with device updated with psk network
        - Get the override psk ssid settings from device360 configure interface wireless settings page
        - Flow: Manage --> Device --> Click on Device MAC hyperlink --> click on configure --> interface settings --> Wireless Interfaces
        - Get the "	Override SSID Broadcast Name", "Override PSK Password", "Reassign CWP"
        - After reading ssid settings variable close the device360 window
        - Keyword Usage:
        - ``Get Override PSK SSID Settings   ${DEVICE_MAC}    WiFi0``

        :param device_mac: device MAC to go to device 360 page
        :param interface: interface name to get the override parameters, WiFi0, WiFi1, WiFi2
        :return: override broadcast name, psk password
        """
        ssid_broadcast_name = ''
        psk_password = ''

        self.utils.print_info("Navigating to device 360 page")
        if self.navigator.navigate_to_device360_page_with_mac(device_mac) == -1:
            kwargs['fail_msg'] = f"Device not found in the device row grid with mac:{device_mac}"
            self.common_validation.failed(**kwargs)
            return -1

        self.utils.print_info("click on configuration tab")
        self.auto_actions.click_reference(self.get_configuration_tab)

        self.utils.print_info("Click on interface settings tab")
        self.auto_actions.click_reference(self.get_interface_settings_tab_single_device)
        self._go_to_wireless_interface_settings_page()

        if interface == "WiFi0":
            ssid_broadcast_name, psk_password = self._get_override_wifi0_psk_ssid_settings()

        self.utils.print_info("Close the device360 page dialog window")
        self.auto_actions.click_reference(self.get_close_device360_dialog_window)
        return ssid_broadcast_name, psk_password

    def _override_wifi0_channel(self, override_channel):
        """
        - override the WiFi0 radio channel

        :param override_channel:
        :return: True
        """
        self.utils.print_info("Click on WiFi0 interface tab")
        self.auto_actions.click_reference(self.get_wifi0_interface_tab)

        self._configure_wifi0_interface_radio_status("ON")

        self.utils.print_info("Click on channel drop down options")
        self.auto_actions.click_reference(self.get_wireless_interface_wifi0_channel_drop_down)

        self.utils.print_info(f"select the channel:{override_channel}")
        self.auto_actions.select_drop_down_options(self.get_wireless_interface_wifi0_channel_options(), override_channel)

    def _override_wifi1_channel(self, override_channel):
        """
        - override the WiFi1 interface channel
        :param override_channel:
        :return: True
        """
        self.utils.print_info("Click on WiFi1 interface tab")
        self.auto_actions.click_reference(self.get_wifi1_interface_tab)

        self._configure_wifi1_interface_radio_status("ON")

        self.utils.print_info("Click on channel drop down options")
        self.auto_actions.click_reference(self.get_wireless_interface_wifi1_channel_drop_down)

        self.utils.print_info(f"select the channel:{override_channel}")
        self.auto_actions.select_drop_down_options(self.get_wireless_interface_wifi1_channel_options(), override_channel)

    def _override_wifi2_channel(self, override_channel):
        """

        :param override_channel:
        :return: 1
        """
        # to do
        pass

    def override_devices_config_wireless_channel(self, device_serials='', interface='WiFi0', override_channel='6', **kwargs):
        """
        - This keyword is used to override the wireless channel
        - This keyword is used with multiple devices
        - Flow:
        - Navigate to the Manage --> Devices
        - Select the devices with passed serial numbers
        - click on Edit button  --> Interface settings --> Wireless Interfaces
        - Select the Interface (WiFi0/WiFi1) --> click radio status ON --> change channel

        - Keyword Usage:
        -  ``Override Devices Config Wireless Channel   device_serials=${AP1_SERIAL},${AP2_SERIAL}    interface='WiFi0', override_channel='6'``

        :param device_serials:  comma separated device serial numbers
        :param interface: device interface i.e WiFi0/WiFi1
        :param override_channel:  override channel
        :return: returns 1 if successful
        """

        if len(device_serials.split(',')) == 1:
            kwargs['fail_msg'] = "This keyword works with multiple devices." \
                                 "Pass the device serial numbers with comma separated "
            self.common_validation.fault(**kwargs)
            return -1

        self.navigator.navigate_to_multiple_device_configuration_page(device_serials)
        sleep(5)

        self.utils.print_info("Click on interface settings tab")
        self.auto_actions.click_reference(self.get_interface_settings_tab)

        self._go_to_wireless_interface_settings_page()

        if interface == "WiFi0":
            self._override_wifi0_channel(override_channel)

        if interface == "WiFi1":
            self._override_wifi1_channel(override_channel)

        if interface == "WiFi2":
            self._override_wifi2_channel(override_channel)

        self.utils.print_info("Click on interface settings save button")
        self.auto_actions.click_reference(self.get_interface_settings_save_button)
        sleep(5)

        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)
        for text in tool_tp_text:
            if "Interface Settings were updated successfully" in text:
                kwargs['pass_msg'] = f"{text}"
                self.common_validation.passed(**kwargs)
                return 1

    def _override_wifi0_radio_profile(self, override_radio_profile):
        """
        - Override the WiFi0 interface radio profile
        :param override_radio_profile:
        :return:
        """
        self.utils.print_info("Click on WiFi1 interface tab")
        self.auto_actions.click_reference(self.get_wifi0_interface_tab)

        self._configure_wifi0_interface_radio_status("ON")

        self.utils.print_info("Click on WiFi0 radio profile drop down")
        self.auto_actions.click_reference(self.get_wireless_wifi0_radio_profile_drop_down)

        self.utils.print_info(f"select the radio profile:{override_radio_profile}")
        self.auto_actions.select_drop_down_options(self.get_wireless_wifi0_radio_profile_options(), override_radio_profile)

    def _override_wifi1_radio_profile(self, override_radio_profile):
        """
        - Override the WiFi1 interface radio profile
        :param override_radio_profile:
        :return:
        """
        self.utils.print_info("Click on WiFi1 interface tab")
        self.auto_actions.click_reference(self.get_wifi1_interface_tab)

        self._configure_wifi1_interface_radio_status("ON")

        self.utils.print_info("Click on WiFi1 radio profile drop down")
        self.auto_actions.click_reference(self.get_wireless_wifi1_radio_profile_drop_down)

        self.utils.print_info(f"select the radio profile:{override_radio_profile}")
        self.auto_actions.select_drop_down_options(self.get_wireless_wifi1_radio_profile_options(), override_radio_profile)

    def override_single_device_config_wireless_radio_profile(self, device_serial='', interface='WiFi0', override_radio_prof='radio_ng_ng0', **kwargs):
        """
        - Override the WiFi0 interface radio profile

        :param device_serial: Device Serial Number
        :param interface: Wifi Interface
        :param override_radio_prof: Radio Profile
        :return: 1 if able to configure Radio profile
        """
        # self.navigator.navigate_to_multiple_device_configuration_page(device_serials)
        self.device_common.edit_device(device_serial)
        sleep(5)
        self.utils.print_info("Click on interface settings tab")
        # self.auto_actions.click_reference(self.get_interface_settings_tab)

        self._go_to_wireless_interface_settings_page()

        if interface == "WiFi0":
            self._override_wifi0_radio_profile(override_radio_prof)

        if interface == "WiFi1":
            self._override_wifi1_radio_profile(override_radio_prof)

        self.utils.print_info("Click on interface settings save button")
        self.auto_actions.click_reference(self.get_interface_settings_save_button)
        sleep(5)

        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)
        for text in tool_tp_text:
            if "Interface Settings were updated successfully" in text:
                kwargs['pass_msg'] = f"{text}"
                self.common_validation.passed(**kwargs)
                return 1

    def override_devices_config_wireless_radio_profile(self, device_serials='', interface='WiFi0', override_radio_prof='radio_ng_ng0', **kwargs):
        """
        - This keyword is used to override the radio profile
        - This keyword is used with multiple devices
        - Flow:
        - Navigate to the Manage --> Devices
        - Select the devices with passed serial numbers
        - click on Edit button  --> Interface settings --> Wireless Interfaces
        - Select the Interface (WiFi0/WiFi1) --> click radio status ON --> change the radio profile from drop down

        - Keyword Usage:
        -  ``Override Devices Config Wireless Radio Profile   device_serials=${AP1_SERIAL},${AP2_SERIAL}    interface='WiFi0', override_radio_prof='radio_ng_ng0'``

        :param device_serials:  comma separated device serial numbers
        :param interface: device interface i.e WiFi0/WiFi1
        :param override_radio_prof:  override wireless interface radio channel
        :return:
        """
        if len(device_serials.split(',')) == 1:
            self.utils.print_info("This keyword works with multiple devices")
            self.utils.print_info("Pass te device serial numbers with comma separated")
            return -1

        self.navigator.navigate_to_multiple_device_configuration_page(device_serials)

        self.utils.print_info("Click on interface settings tab")
        self.auto_actions.click_reference(self.get_interface_settings_tab)

        self._go_to_wireless_interface_settings_page()

        if interface == "WiFi0":
            self._override_wifi0_radio_profile(override_radio_prof)

        if interface == "WiFi1":
            self._override_wifi1_radio_profile(override_radio_prof)

        self.utils.print_info("Click on interface settings save button")
        self.auto_actions.click_reference(self.get_interface_settings_save_button)
        sleep(5)

        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)
        for text in tool_tp_text:
            if "Interface Settings were updated successfully" in text:
                kwargs['pass_msg'] = f"{text}"
                self.common_validation.passed(**kwargs)
                return 1

    def _configure_wifi0_interface_radio_status(self, status='', **kwargs):
        """
        - Configure WiFi0 Interface Status on Device Override

        :param status : WiFi interface radio status ie ON or OFF
        :return: 1
        """
        self.utils.print_info("Click WIFI0 Interface tab")
        sleep(5)
        self.auto_actions.click_reference(self.get_manage_devices_edit_wireless_interface_wifi0_tab)
        self.screen.save_screen_shot()
        sleep(2)

        if status == "ON":
            if not self.get_manage_devices_edit_wireless_interface_wifi0_button().is_selected():
                self.utils.print_info("Changing WIFI0 Interface Radio Status to ON")
                self.auto_actions.click_reference(self.get_manage_devices_edit_wireless_interface_wifi0_button)
                self.screen.save_screen_shot()
                sleep(2)

        if status == "OFF":
            if self.get_manage_devices_edit_wireless_interface_wifi0_button().is_selected():
                self.utils.print_info("Changing WIFI0 Interface Status to OFF")
                self.auto_actions.click_reference(self.get_manage_devices_edit_wireless_interface_wifi0_button)
                self.screen.save_screen_shot()
                sleep(2)
        kwargs['pass_msg'] = "Successfully configure wifi0 interface radio"
        self.common_validation.passed(**kwargs)
        return 1

    def _configure_wifi1_interface_radio_status(self, status='', **kwargs):
        """
        - Configure WiFi1 Interface Radio Status on Device Override

        :param status : WiFi1 interface status ie ON or OFF
        :return: 1
        """
        self.utils.print_info("Click WIFI1 Interface tab")
        self.auto_actions.click_reference(self.get_manage_devices_edit_wireless_interface_wifi1_tab)
        self.screen.save_screen_shot()
        sleep(2)

        if status == "ON":
            if not self.get_manage_devices_edit_wireless_interface_wifi1_on_button().is_selected():
                self.utils.print_info("Changing WIFI1 Interface Radio Status to ON")
                self.auto_actions.click_reference(self.get_manage_devices_edit_wireless_interface_wifi1_on_button)
                self.screen.save_screen_shot()
                sleep(2)

        if status == "OFF":
            if not self.get_manage_devices_edit_wireless_interface_wifi1_off_button().is_selected():
                self.utils.print_info("Changing WIFI1 Interface Radio Status to OFF")
                self.auto_actions.click_reference(self.get_manage_devices_edit_wireless_interface_wifi1_off_button)
                self.screen.save_screen_shot()
                sleep(2)
        kwargs['pass_msg'] = "Successfully configure wifi1 interface radio"
        self.common_validation.passed(**kwargs)
        return 1

    def change_multiple_devices_wireless_interface_radio_status(self, device_serials='', interface_name='', status='', **kwargs):
        """
        - This Keyword will Change Status(ON/OFF) of Wireless Interface for Multiple Devices
        - Flow:MANAGE-->Devices-->Select Multiple devices-->Edit-->Interface settings-->wireless interfaces-->Radio Status
        - Keyword Usage:
        - ``Change Multiple Devices Wireless Interface Radio Status  device_serials=${AP1_SERIAL},${AP2_SERIAL}  interface_name=${INTERFACE_NAME}  status=${STATUS_ON}``

        :param device_serials: Devices Serial Numbers Seperated by Comma
        :param interface_name: Wireless Interface Name
        :param status: WiFi interface radio status ie ON or OFF
        :return: 1 if WiFi radio Status Updated successfully
        """
        if len(device_serials.split(',')) == 1:
            kwargs['fail_msg'] = "This keyword works with multiple devices." \
                                 "Pass the device serial numbers with comma separated"
            self.common_validation.failed(**kwargs)
            return -1

        self.navigator.navigate_to_multiple_device_configuration_page(device_serials)
        sleep(5)

        self.utils.print_info("Click on interface settings tab")
        self.auto_actions.click_reference(self.get_interface_settings_tab)

        self._go_to_wireless_interface_settings_page()
        self.screen.save_screen_shot()

        if interface_name == "WIFI0":
            self._configure_wifi0_interface_radio_status(status)
        if interface_name == "WIFI1":
            self._configure_wifi1_interface_radio_status(status)

        self.utils.print_info("Click Interface Settings Save Button")
        self.auto_actions.click_reference(self.get_manage_devices_edit_wireless_interface_save_button)
        sleep(2)

        tool_tip_text = tool_tip.tool_tip_text
        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Click Interface Settings Cancel Button")
        self.auto_actions.click_reference(self.get_manage_devices_edit_wireless_interface_cancel_button)
        sleep(2)

        self.utils.print_info("Tool tip Text Displayed on Page", tool_tip_text)
        if "Interface Settings were updated successfully." in tool_tip_text:
            kwargs['pass_msg'] = "Interface Settings were updated successfully"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Interface Settings were updated unsuccessfully"
            self.common_validation.failed(**kwargs)
            return -1

    def change_single_device_wireless_interface_radio_status(self, device_serial=None, interface_name=None, status=None, **kwargs):
        """
        - This Keyword will Change Status(ON/OFF) of Wireless Interface of a single device
        - Flow:MANAGE-->Devices-->Select Multiple devices-->Edit-->Interface settings-->wireless interfaces-->Radio Status
        - Keyword Usage:
        - ``Change Single Device Wireless Interface Radio Status  device_serial=${AP1_SERIAL}  interface_name=${INTERFACE_NAME}  status=${STATUS_ON}``

        :param device_serial: Device Serial Number
        :param interface_name: Wireless Interface Name
        :param status: WiFi interface radio status ie ON or OFF
        :return: 1 if WiFi radio Status Updated successfully
        """
        sleep(5)
        self.device_common.edit_devices(device_serial)
        sleep(5)
        self.utils.print_info("Clicking on the config button")
        self.auto_actions.click_reference(self.get_devices_edit_config_button)
        sleep(5)
        self.utils.print_info("Click on interface settings tab")
        self.auto_actions.click_reference(self.get_interface_settings_tab_single_device)

        self._go_to_wireless_interface_settings_page()

        if interface_name == "WIFI0":
            self._configure_wifi0_interface_radio_status(status)
        if interface_name == "WIFI1":
            self._configure_wifi1_interface_radio_status(status)

        if self.get_manage_device_interface_settings_save_button_disabled():
            kwargs['pass_msg'] = "No update required on wireless radio interface"
            self.utils.print_info("Click Interface Settings Close Button")
            self.auto_actions.click_reference(self.get_manage_devices_edit_wireless_interface_close_button)
            self.common_validation.passed(**kwargs)
            return 1

        self.utils.print_info("Click Interface Settings Save Button")
        self.auto_actions.click_reference(self.get_manage_device_edit_wireless_interface_save_button)

        tool_tip_text = tool_tip.tool_tip_text
        self.screen.save_screen_shot()
        sleep(5)

        self.utils.print_info("Click Interface Settings Close Button")
        self.auto_actions.click_reference(self.get_manage_devices_edit_wireless_interface_close_button)
        sleep(2)

        self.utils.print_info("Tool tip Text Displayed on Page", tool_tip_text)
        if "Interface Settings were updated successfully." in tool_tip_text:
            kwargs['pass_msg'] = "Interface Settings were updated successfully"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Interface Settings were updated unsuccessfully"
            self.common_validation.failed(**kwargs)
            return -1

    def change_device_host_name(self, new_host_name, device_mac="", device_name="", **kwargs):
        """
        - This keyword will Change the Host Name of the Device
        - Flow : Click AP MAC or Name Link --> Configure-->Device Configuration--> Host Name
        - Keyword Usage:
        - ``Change Device Host Name    ${HOST_NAME}    $device_mac=${AP1_MAC}``
        - ``Change Device Host Name    ${HOST_NAME}   $device_name=${AP1_NAME}``

        :param new_host_name: Device Host Name to change
        :param device_mac: Device Mac Address
        :param device_name: Device Host Name
        :return: 1 in case of success else -1
        """

        self.utils.print_info("*****************************")
        self.utils.print_info("Changing The Device HostName: ", new_host_name)
        self.utils.print_info("*****************************")

        if device_mac:
            self.navigator.navigate_to_device360_page_with_mac(device_mac)

        if device_name:
            self.navigator.navigate_to_device360_page_with_host_name(device_name)

        self.utils.print_info("Click Configure Button")
        if not self.get_device_override_configure_button().is_selected():
            self.auto_actions.click_reference(self.get_device_override_configure_button)
        sleep(4)

        self.utils.print_info("Click Device Configuration Button")
        self.auto_actions.click_reference(self.get_device_override_configure_device_configuration_button)
        sleep(2)

        self.utils.print_info("Entering New HostName...")
        self.auto_actions.send_keys(self.get_device_override_configure_host_name(), new_host_name)
        sleep(2)

        self.utils.print_info("Save Device Configuration")
        self.auto_actions.click_reference(self.get_device_override_save_device_configuration)
        sleep(2)

        tool_tip_text = tool_tip.tool_tip_text
        self.utils.print_info("Tool tip Text Displayed on Page", tool_tip_text)

        self.utils.print_info("Close Dialogue Window")
        self.auto_actions.click_reference(self.get_close_dialog)
        sleep(2)

        if "Device configuration was updated successfully" in tool_tip_text:
            kwargs['pass_msg'] = "Device configuration was updated successfully"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Device configuration was updated unsuccessfully"
            self.common_validation.failed(**kwargs)
            return -1

    def _check_wifi0_radio_status(self):
        """
        - Configure WiFi0 Radio Status on Device Override

        :return: WiFi0 Radio status ie ON or OFF
        """
        self.utils.print_info("Click WIFI0 Tab")
        self.auto_actions.click_reference(self.get_device_override_configure_interface_settings_wifi0_tab)
        sleep(2)

        if self.get_device_override_configure_interface_settings_wifi0_radio_status().is_selected():
            return "ON"
        else:
            return "OFF"

    def _check_wifi1_radio_status(self):
        """
        - Configure WiFi1 Radio Status on Device Override

        :return:  WiFi1 Radio status ie ON or OFF
        """
        self.utils.print_info("Click WIFI1 Tab")
        self.auto_actions.click_reference(self.get_device_override_configure_interface_settings_wifi1_tab)
        sleep(2)

        if self.get_device_override_configure_interface_settings_wifi1_radio_status().is_selected():
            return "ON"
        else:
            return "OFF"

    def _check_wifi2_radio_status(self):
        """
        - Configure WiFi1 Radio Status on Device Override
        :return:  WiFi1 Radio status ie ON or OFF
        """
        self.utils.print_info("Click WIFI2 Tab")
        self.auto_actions.click_reference(self.get_wifi2_interface_tab)
        sleep(2)

        if self.get_device_override_configure_interface_settings_wifi2_radio_status().is_selected():
            return "ON"
        else:
            return "OFF"

    def check_wifi_radio_status(self, wifi_interface_name, device_mac="", device_name=""):
        """
        - This keyword will check WiFi interface Radio status of the Device
        - Flow : Click AP MAC Link --> Configure-->Wireless Interfaces--> WIFI interface-->Status
        - Keyword Usage:
        - ``Check WiFi Radio Status    ${WIFI_INTERFACE_WIFI0}   device_mac=${AP1_MAC}``
        - ``Check WiFi Radio Status    ${WIFI_INTERFACE_WIFI0}   device_name=${AP1_NAME}``

        :param wifi_interface_name: WiFi Interface Name ie WiFi0/WiFi1
        :param device_mac: Device Mac Address
        :param new_host_name: Device Host Name to change
        :return: ON If Radio Status is ON else OFF
        """

        self.utils.print_info("*****************************")
        self.utils.print_info("Checking Radio status of interface : ", wifi_interface_name)
        self.utils.print_info("*****************************")

        if device_mac:
            self.navigator.navigate_to_device360_page_with_mac(device_mac)

        if device_name:
            self.navigator.navigate_to_device360_page_with_host_name(device_name)

        self.utils.print_info("Click Configure Button")
        if not self.get_device_override_configure_button().is_selected():
            self.auto_actions.click_reference(self.get_device_override_configure_button)
        sleep(4)

        self.utils.print_info("Click Interface Settings Button")
        self.auto_actions.click_reference(self.get_device_override_configure_interface_settings_button)
        sleep(2)

        self.utils.print_info("Click Wireless interfaces Link")
        self.auto_actions.click_reference(self.get_device_override_configure_wireless_interface_link)
        sleep(2)

        if wifi_interface_name.upper() == "WIFI0":
            radio_status = self._check_wifi0_radio_status()
            self.utils.print_info("Close the device360 page dialog window")
            self.auto_actions.click_reference(self.get_close_device360_dialog_window)
            sleep(2)
            return radio_status

        if wifi_interface_name.upper() == "WIFI1":
            radio_status = self._check_wifi1_radio_status()
            self.utils.print_info("Close the device360 page dialog window")
            self.auto_actions.click_reference(self.get_close_device360_dialog_window)
            sleep(2)
            return radio_status

    def _configure_wifi0_transmission_power(self, transmission_mode='', power_value='', **kwargs):
        """
        - Configure WiFi0 Transmission Power on Device Override

        :param transmission_mode : Transmission Mode ie Manual or Auto
        :param power_value: name of the network to deploy
        :return: 1
        """
        self.utils.print_info("Click WIFI0 Interface tab")
        self.auto_actions.click_reference(self.get_manage_devices_edit_wireless_interface_wifi0_tab)
        sleep(2)

        self.utils.print_info("Enable WIFI0 Interface Status to ON")
        self.auto_actions.click_reference(self.get_manage_devices_edit_wireless_interface_wifi0_on_button)
        self.screen.save_screen_shot()
        sleep(2)

        if transmission_mode == "Auto":
            self.utils.print_info("Enable Transmission Power Mode To Auto")
            self.auto_actions.click_reference(self.get_wireless_interface_wifi0_transmission_mode_auto)
            self.screen.save_screen_shot()
            sleep(2)

        if transmission_mode == "Manual":
            self.utils.print_info("Enable Transmission Power Mode To Manual")
            self.auto_actions.click_reference(self.get_wireless_interface_wifi0_transmission_mode_manual)
            self.screen.save_screen_shot()
            sleep(2)

            if power_value != "default":
                current_value = self.get_wifi0_transmission_power_value_text().text
                self.utils.print_info("Current Transmission Power Value is: ", current_value)


                count = 1
                while power_value != current_value:
                    self.utils.print_info("Click and Hold Slider")
                    self.auto_actions.click_and_hold_element(self.get_wifi0_transmission_power_slider_button(),10)
                    sleep(2)

                    updated_value = self.get_wifi0_transmission_power_value_text().text
                    self.utils.print_info("Updated Transmission Power Value is: ", updated_value)
                    if updated_value == power_value:
                        break
                    count += 1
            self.screen.save_screen_shot()
        kwargs['pass_msg'] = "Successfully configure wifi0 transmission power"
        self.common_validation.passed(**kwargs)
        return 1

    def _configure_wifi1_transmission_power(self, transmission_mode='', power_value='', **kwargs):
        """
        - Configure WiFi1 Transmission Power on Device Override

        :param transmission_mode : Transmission Mode ie Manual or Auto
        :param power_value: name of the network to deploy
        :return: 1
        """
        self.utils.print_info("Click WIFI1 Interface tab")
        self.auto_actions.click_reference(self.get_manage_devices_edit_wireless_interface_wifi1_tab)
        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Enable WIFI1 Interface Status to ON")
        self.auto_actions.click_reference(self.get_manage_devices_edit_wireless_interface_wifi1_on_button)
        self.screen.save_screen_shot()
        sleep(2)

        if transmission_mode == "Auto":
            self.utils.print_info("Enable Transmission Power Mode To Auto")
            self.auto_actions.click_reference(self.get_wireless_interface_wifi1_transmission_mode_auto)
            self.screen.save_screen_shot()
            sleep(2)

        if transmission_mode == "Manual":
            self.utils.print_info("Enable Transmission Power Mode To Manual")
            self.auto_actions.click_reference(self.get_wireless_interface_wifi1_transmission_mode_manual)
            self.screen.save_screen_shot()
            sleep(2)

            if power_value != "default":
                current_value = self.get_wifi1_transmission_power_value_text().text
                self.utils.print_info("Current Transmission Power Value is: ", current_value)

                count = 1
                while power_value != current_value:
                    self.utils.print_info("Click and Hold Slider")
                    self.auto_actions.click_and_hold_element(self.get_wifi1_transmission_power_slider_button(),10)
                    sleep(2)

                    updated_value = self.get_wifi1_transmission_power_value_text().text
                    self.utils.print_info("Updated Transmission Power Value is: ", updated_value)
                    if updated_value == power_value:
                        break
                    count += 1
            self.screen.save_screen_shot()
        kwargs['pass_msg'] = "Successfully configure wifi1 transmission power"
        self.common_validation.passed(**kwargs)
        return 1

    def change_transmission_power_to_multiple_devices(self, device_serials='', interface_name='', transmission_mode='',
                                                      power_value= '', **kwargs):
        """
        - This Keyword will Change the Transmission of Wireless Interface
        - Go To MANAGE-->Devices-->Select All devices-->Edit-->Interface settings-->wireless interfaces
        - Keyword Usage:
        - ``Change Transmission Power To Multiple Devices  device_serials=${AP1_SERIAL},${AP2_SERIAL}
             interface_name=${INTERFACE_NAME}  transmission_mode=${MANUAL}  power_value=${VALUE}``

        :param device_serials: Device Serial Numbers separated by comma
        :param interface_name: Wireless Interface Name
        :param transmission_mode: Transmission Mode ie Manual or Auto
        :param power_value: name of the network to deploy
        :return: 1 if Transmission Power Updated successfully
        """
        if len(device_serials.split(',')) == 1:
            kwargs['fail_msg'] = "This keyword works with multiple devices." \
                                 "Pass the device serial numbers with comma separated"
            self.common_validation.fault(**kwargs)
            return -1

        self.navigator.navigate_to_multiple_device_configuration_page(device_serials)
        sleep(5)

        self.utils.print_info("Click on interface settings tab")
        self.auto_actions.click_reference(self.get_interface_settings_tab)
        self.screen.save_screen_shot()

        self._go_to_wireless_interface_settings_page()
        self.screen.save_screen_shot()

        if interface_name == "WIFI0":
            self._configure_wifi0_transmission_power(transmission_mode, power_value)
        if interface_name == "WIFI1":
            self._configure_wifi1_transmission_power(transmission_mode, power_value)
        if interface_name == "WIFI2":
            pass

        self.utils.print_info("Click Interface Settings Save Button")
        self.auto_actions.click_reference(self.get_manage_devices_edit_wireless_interface_save_button)
        sleep(2)

        tool_tip_text = tool_tip.tool_tip_text
        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Click Interface Settings Cancel Button")
        self.auto_actions.click_reference(self.get_manage_devices_edit_wireless_interface_cancel_button)
        sleep(2)

        self.utils.print_info("Tool tip Text Displayed on Page", tool_tip_text)
        if "Interface Settings were updated successfully." in tool_tip_text:
            kwargs['pass_msg'] = "Interface Settings were updated successfully"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Interface Settings were updated unsuccessfully"
            self.common_validation.failed(**kwargs)
            return -1

    def override_config_device_template(self, template_name, device_mac="", device_name="", **kwargs):
        """
        - This keyword will Change the Template Name of the Device
        - Flow : Click AP MAC or Name Link --> Configure-->Device Configuration--> Device Template
        - Keyword Usage:
        - ``Override Devices Config Device Template    ${TEMPLATE_NAME}    $device_mac=${AP1_MAC}``
        - ``Override Devices Config Device Template    ${TEMPLATE_NAME}   $device_name=${AP1_NAME}``

        :param template_name: Device Template to Change
        :param device_mac: Device Mac Address
        :param device_name: Device Host Name
        :return: 1 in case of success else -1
        """

        self.utils.print_info("*****************************")
        self.utils.print_info("Changing The Device Template Name: ", template_name)
        self.utils.print_info("*****************************")

        if device_mac:
            self.navigator.navigate_to_device360_page_with_mac(device_mac)

        if device_name:
            self.navigator.navigate_to_device360_page_with_host_name(device_name)

        self.utils.print_info("Click Configure Button")
        if not self.get_device_override_configure_button().is_selected():
            self.auto_actions.click_reference(self.get_device_override_configure_button)
        sleep(4)

        self.utils.print_info("Click Device Configuration Button")
        self.auto_actions.click_reference(self.get_device_override_configure_device_configuration_button)
        sleep(2)

        self.utils.print_info("Click On Device Template drop down options")
        self.auto_actions.click_reference(self.get_device_edit_template_drop_down)

        self.utils.print_info(f"Selecting Device Template:{template_name}")
        self.auto_actions.select_drop_down_options(self.get_device_edit_template_drop_down_options(), template_name)

        self.utils.print_info("Save Device Configuration")
        self.auto_actions.click_reference(self.get_device_override_save_device_configuration)
        sleep(2)

        tool_tip_text = tool_tip.tool_tip_text
        self.utils.print_info("Tool tip Text Displayed on Page", tool_tip_text)

        self.utils.print_info("Close Dialogue Window")
        self.auto_actions.click_reference(self.get_close_dialog)
        sleep(2)

        if "Device configuration was updated successfully" in tool_tip_text:
            kwargs['pass_msg'] = "Device configuration was updated successfully"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Device configuration was updated unsuccessfully"
            self.common_validation.failed(**kwargs)
            return -1

    def check_device_configured_template(self, device_mac="", device_name=""):
        """
        - This keyword will get device template configured it on Device
        - Flow : Click AP MAC Link --> Configure-->Interface Settings--->Device Template
        - Keyword Usage:
        - ``Check Device Configured Template  device_mac=${AP1_MAC}``
        - ``Check Device Configured Template  device_name=${AP1_NAME}``

        :param device_mac: Device Mac Address
        :param device_name: Device Host Name to change
        :return: Device Template Name
        """
        if device_mac:
            self.navigator.navigate_to_device360_page_with_mac(device_mac)

        if device_name:
            self.navigator.navigate_to_device360_page_with_host_name(device_name)

        self.utils.print_info("Click Configure Button")
        if not self.get_device_override_configure_button().is_selected():
            self.auto_actions.click_reference(self.get_device_override_configure_button)
        sleep(4)

        self.utils.print_info("Click Interface Settings Button")
        self.auto_actions.click_reference(self.get_device_override_configure_interface_settings_button)
        sleep(2)

        template_text = self.get_device_edit_template_text().text
        self.utils.print_info("Device Template Configured is ", template_text)

        self.utils.print_info("Close Dialogue Window")
        self.auto_actions.click_reference(self.get_close_dialog)
        sleep(2)

        return template_text

    def override_config_exos_device_template(self, template_name, device_mac="", device_name="", **kwargs):
        """
        - This keyword will Change the Template Name of the Device
        - Flow : Click SW MAC or Name Link --> Configure-->Device Configuration--> Device Template
        - Keyword Usage:
        - ``Override Devices Config Device Template    ${TEMPLATE_NAME}    $device_mac=${SW_MAC}``
        - ``Override Devices Config Device Template    ${TEMPLATE_NAME}   $device_name=${SW_NAME}``

        :param template_name: Device Template to Change
        :param device_mac: Device Mac Address
        :param device_name: Device Host Name
        :return: 1 in case of success else -1
        """

        self.utils.print_info("*****************************")
        self.utils.print_info("Changing The Device Template Name: ", template_name)
        self.utils.print_info("*****************************")

        if device_mac:
            self.navigator.navigate_to_device360_page_with_mac(device_mac)

        if device_name:
            self.navigator.navigate_to_device360_page_with_host_name(device_name)

        self.utils.print_info("Click Configure Button")
        if not self.get_device_override_configure_button().is_selected():
            self.auto_actions.click_reference(self.get_device_override_configure_button)
        sleep(10)

        self.utils.print_info("Click Device Configuration Button")
        self.auto_actions.click_reference(self.get_device_override_configure_exos_device_configuration_button)
        sleep(5)
        self.screen.save_screen_shot()

        self.utils.print_info("Click On Device Template drop down options")
        self.auto_actions.click_reference(self.get_device_edit_template_drop_down)

        self.utils.print_info(f"Selecting Device Template:{template_name}")
        self.auto_actions.select_drop_down_options(self.get_device_edit_template_drop_down_options(), template_name)

        self.utils.print_info("Save Device Configuration")
        self.auto_actions.click_reference(self.get_device_override_exos_save_device_configuration())
        sleep(2)
        self.screen.save_screen_shot()

        tool_tip_text = tool_tip.tool_tip_text
        self.utils.print_info("Tool tip Text Displayed on Page", tool_tip_text)

        self.utils.print_info("Close Dialogue Window")
        self.auto_actions.click_reference(self.get_close_dialog)
        sleep(2)

        if "Device configuration was updated successfully" in tool_tip_text:
            kwargs['pass_msg'] = "Device configuration was updated successfully"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Device configuration was updated unsuccessfully"
            self.common_validation.failed(**kwargs)
            return -1

    def configure_supplemental_cli_for_device(self, suppl_cli_name="", suppl_cli_cmds="", device_mac="", device_name="", **kwargs):
        """
        - This keyword will Configure Supplemental Cli on Device
        - Flow : Click AP MAC or Name Link --> Configure-->Device Configuration--> Device Template
        - Keyword Usage:
        - ``Configure Supplemental Cli for Device    ${CLI_NAME}    $device_mac=${AP1_MAC}``
        - ``Configure Supplemental Cli for Device    ${CLI_NAME}    ${CLI_CMDS}     $device_name=${AP1_NAME}``

        :param suppl_cli_name: Supplemental Cli Name
        :param suppl_cli_cmds: Supplemental Cli commands
        :param device_mac: Device Mac Address
        :param device_name: Device Host Name
        :return: 1 in case of success else -1
        """

        self.utils.print_info("*****************************")
        self.utils.print_info("Configure Supplemental Cli : ", suppl_cli_name)
        self.utils.print_info("*****************************")

        if device_mac:
            self.navigator.navigate_to_device360_page_with_mac(device_mac)

        if device_name:
            self.navigator.navigate_to_device360_page_with_host_name(device_name)

        self.utils.print_info("Click Configure Button")
        if self.get_device_override_configure_button().is_selected():
            pass
        else:
            self.auto_actions.click_reference(self.get_device_override_configure_button)

        self.utils.print_info("Click Device Configuration Button")
        self.auto_actions.click_reference(self.get_device_override_configure_exos_device_configuration_button)

        self.utils.print_info("Click on Supplemental cli add option")
        self.auto_actions.click_reference(self.get_device_config_supplemental_cli_add_button)

        self.utils.print_info(f"Entering Supplemental Cli Name:{suppl_cli_name}")
        self.auto_actions.send_keys(self.get_device_config_supplemental_cli_enter_name(), suppl_cli_name)

        self.utils.print_info(f"Entering Supplemental Cli Commands:{suppl_cli_cmds}")
        self.auto_actions.send_keys(self.get_device_config_supplemental_cli_enter_commands(), suppl_cli_cmds)

        self.utils.print_info("Saving Supplemental Cli Configs")
        self.auto_actions.click_reference(self.get_device_config_supplemental_cli_save_button)
        self.screen.save_screen_shot()

        tool_tip_text = tool_tip.tool_tip_text
        self.utils.print_info("Tool tip Text Displayed on Page - Supplemental Cli ", tool_tip_text)

        self.utils.print_info("Save Device Configuration")
        self.auto_actions.click_reference(self.get_device_override_exos_save_device_configuration)

        tool_tip_text = tool_tip.tool_tip_text
        self.utils.print_info("Tool tip Text Displayed on Page", tool_tip_text)

        self.utils.print_info("Close Dialogue Window")
        self.auto_actions.click_reference(self.get_close_dialog)

        if "Device configuration was updated successfully" in tool_tip_text:
            kwargs['pass_msg'] = "Device configuration was updated successfully"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Device configuration was updated unsuccessfully"
            self.common_validation.failed(**kwargs)
            return -1

    def select_configure_supplemental_cli_for_device(self, suppl_cli_name="", device_mac="", device_name="", **kwargs):
        """
        - This keyword will Configure Supplemental Cli on Device
        - Flow : Click AP MAC or Name Link --> Configure-->Device Configuration--> Device Template
        - Keyword Usage:
        - ``Select Configure Supplemental Cli for Device    ${CLI_NAME}    $device_mac=${AP1_MAC}``
        - ``Select Configure Supplemental Cli for Device    ${CLI_NAME}    ${CLI_CMDS}     $device_name=${AP1_NAME}``

        :param suppl_cli_name: Supplemental Cli Name
        :param device_mac: Device Mac Address
        :param device_name: Device Host Name
        :return: 1 in case of success else -1
        """

        self.utils.print_info("*****************************")
        self.utils.print_info("Configure Supplemental Cli : ", suppl_cli_name)
        self.utils.print_info("*****************************")

        if device_mac:
            self.navigator.navigate_to_device360_page_with_mac(device_mac)

        if device_name:
            self.navigator.navigate_to_device360_page_with_host_name(device_name)

        self.utils.print_info("Click Configure Button")
        if not self.get_device_override_configure_button().is_selected():
            self.auto_actions.click_reference(self.get_device_override_configure_button)
        sleep(10)

        self.utils.print_info("Click Device Configuration Button")
        self.auto_actions.click_reference(self.get_device_override_configure_exos_device_configuration_button)
        sleep(5)

        # Selecting  Supplemental Cli from dropdown
        self.utils.print_info("Click on Supplemental Cli Select")
        self.auto_actions.click_reference(self.get_device_supplemental_cli_drop_down)

        self.utils.print_info(f"Selecting Supplemental Cli:{suppl_cli_name}")
        self.auto_actions.select_drop_down_options(self.get_device_select_supplemental_cli_drop_down_options(), suppl_cli_name)
        self.screen.save_screen_shot()

        self.utils.print_info("Save Device Configuration")
        self.auto_actions.click_reference(self.get_device_override_exos_save_device_configuration)
        sleep(1)

        tool_tip_text = tool_tip.tool_tip_text
        self.utils.print_info("Tool tip Text Displayed on Page", tool_tip_text)

        self.utils.print_info("Close Dialogue Window")
        self.auto_actions.click_reference(self.get_close_dialog)
        sleep(2)

        if "Device configuration was updated successfully" in tool_tip_text:
            kwargs['pass_msg'] = "Device configuration was updated successfully"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Device configuration was updated unsuccessfully"
            self.common_validation.failed(**kwargs)
            return -1

    def check_config_audit_delta_match(self, serial=None, mac=None):
        """
        - This keyword is used to select the check device configuration in Delta in Manage --> Device page
        - Assumes that navigated to the Manage --> Device page
        - Keyword Usage:
        - ``Check Config Audit Delta Match     serials=${DEVICE1_SERIAL} ``

        :param serial: device serial number
        :param mac: device MAC address
        :return: 1 in case of success else -1
        """

        delta_configs = 'Cannot retrieve delta configs'

        self.utils.print_info("Navigate to Manage-->Devices")
        self.navigator.navigate_to_devices()
        sleep(5)

        device_row = None

        if serial:
            device_row = self.devices.get_device_row(device_serial=serial)
        elif mac:
            device_row = self.devices.get_device_row(device_mac=mac)

        if device_row:
            self.utils.print_info("Click on Configuration Audit button")
            self.auto_actions.click(self.devices_web_elements.get_device_config_audit_button(device_row))
            sleep(10)

            self.utils.print_info("Click on Device Config Audit Delta View")
            self.auto_actions.click_reference(self.get_device_config_audit_delta_view)
            sleep(10)
            self.screen.save_screen_shot()
            sleep(5)

            self.utils.print_info("Get the Config content from Device Config Audit Delta View")
            delta_configs = self.get_device_config_audit_delta_view_content().text
            self.utils.print_info("Delta Configs : ", delta_configs)

            self.auto_actions.click_reference(self.get_device_config_audit_view_close_button)

        self.devices.deselect_all_devices()

        return delta_configs

    def delete_common_object_supplemental_cli(self, suppl_cli_name, **kwargs):
        """
        - This keyword will Deletes Supplemental Cli under Common objects -> Basic
        - Flow : Click AP MAC or Name Link --> Common objects -> Basic -> Supplemental Cli
        - Keyword Usage:
        - ``Delete Common Object Supplemental Cli    ${CLI_NAME}``

        :param suppl_cli_name: Supplemental Cli Name
        :return: 1 in case of success else -1
        """
        self.utils.print_info("*****************************")
        self.utils.print_info("Deleting Supplemental Cli Object: ", suppl_cli_name)
        self.utils.print_info("*****************************")

        self.utils.print_info("Click on Configure Common Objects tab...")
        self.navigator.navigate_configure_common_objects()
        sleep(3)
        self.utils.print_info("Click on common object Basic tab")
        self.navigator.navigate_to_common_object_basic_tab()

        self.utils.print_info("Click on Supplemental CLI Objects tab...")
        self.auto_actions.click_reference(self.get_common_obj_basic_supplemental_cli_tab)
        sleep(5)
        self.screen.save_screen_shot()

        self.utils.print_info("Select Supplemental CLI Object...")

        row = self.select_supplemental_cli_row(suppl_cli_name)
        if row == "":
            self.utils.print_info("Supplemental CLI Object Not Found..")
            return 1

        self.utils.print_info("row.text: ", row.text)
        # Commented on 1/18/23 because variable is unused
        # selected_checkbox = self.get_supplemental_cli_select_checkbox(row).click()
        self.get_supplemental_cli_select_checkbox(row).click()
        self.screen.save_screen_shot()

        self.utils.print_info("Deleting Supplemental CLI Object...")
        self.auto_actions.click_reference(self.get_supplemental_cli_delete_button())
        sleep(2)
        self.auto_actions.click_reference(self.get_supplemental_cli_delete_confirm_button())
        sleep(2)

        kwargs['pass_msg'] = "Successfully delete common object supplemental cli"
        self.common_validation.passed(**kwargs)
        return 1

    def select_supplemental_cli_row(self, suppl_cli_name):
        """
        select the supplemental cli
        :param suppl_cli_name:
        :return:
        """
        rows = self.get_supplemental_cli_select_rows()
        selected_row = ""
        sleep(5)

        for row in rows:
            self.utils.print_info("Supplemental cli row in text format : ", row.text)
            if suppl_cli_name in row.text:
                self.utils.print_info("Supplemental cli found : ", row.text, row)
                return row

        return selected_row

    def check_device_template_on_device_configuration_page(self, device_mac="", device_name=""):
        """
        - This keyword will get device template configured on Device
        - Flow : Click AP MAC Link --> Configure-->Device Configuration --->Device Template
        - Keyword Usage:
        - ``Check Device Template on Device Configuration Page  device_mac=${AP1_MAC}``
        - ``Check Device Template on Device Configuration Page  device_name=${AP1_NAME}``

        :param device_mac: Device Mac Address
        :param device_name: Device Host Name to change
        :return: Device Template Name
        """

        if device_mac:
            self.navigator.navigate_to_device360_page_with_mac(device_mac)

        if device_name:
            self.navigator.navigate_to_device360_page_with_host_name(device_name)

        self.utils.print_info("Click Configure Button")
        if not self.get_device_override_configure_button().is_selected():
            self.auto_actions.click_reference(self.get_device_override_configure_button)
        sleep(4)

        self.utils.print_info("Click Device Configuration Button")
        self.auto_actions.click_reference(self.get_device_override_configure_device_configuration_button)
        sleep(2)

        self.auto_actions.scroll_down()
        sleep(2)

        self.utils.print_info("Click On Device Template drop down options")
        template_text = self.get_device_edit_template_drop_down().text
        sleep(2)

        self.utils.print_info("Device Template Configured is ", template_text)

        self.utils.print_info("Close Dialogue Window")
        self.auto_actions.click_reference(self.get_close_dialog)
        sleep(2)

        return template_text

    def device360_event_select_severity(self, severity, **kwargs):
        """
        - This keyword is used to select the severity in D360 Event configuration
        - Assumes that navigated to the Manage --> Device page --> Events page
        - Depends on the severity value, it will select in dropdown
        - Keyword Usage:
        - ``Device360 Event Select Severity     severity=${SEVERITY} ``
        - Severity values should be in the category - "Critical, Info, Show All, Minor, Major, Clear"

        :param severity: "Critical, Info, Show All, Minor, Major, Clear"
        :return: 1 in case of success else -1
        """

        self.utils.print_info("*****************************")
        self.utils.print_info("Selecting severity dropdown in D360 Events page ", severity)
        self.utils.print_info("*****************************")
        self.utils.print_info("Clicking severity Dropdown ")
        sleep(3)
        self.auto_actions.click_reference(self.get_device_events_select_severity)
        sleep(3)

        self.utils.print_info("selecting the severity ",severity )
        sleep(3)
        if self.auto_actions.select_drop_down_options(self.get_severity_dropdown_options(), severity):
            sleep(3)
            kwargs['pass_msg'] = "Successfully select the severity"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "UnSuccessfully select the severity"
            self.common_validation.failed(**kwargs)
            return -1

    def device_override_change_wifi2_interface_status(self, device_serial='', interface_status='', **kwargs):
        """
        - This Keyword will Enable/Disable the WIFI2 interface status at device override configuration.
        - Flow: Manage-->Devices-->select Device with serial number->Edit-->configuration-->interface settings
                -->Wireless settings--> WiFi2

        - Keyword Usage:
        - ``Device Override Change WiFi2 Interface Status  device_serial=${DEVICE_SERIAL}   interface_status=${STATUS}``

        :param device_serial: Device serial Number
        :param interface_status: Interface status Enable/Disable
        :return: 1 if interface status enable/disable Successfully else -1
        """

        self.navigator.navigate_to_devices()
        self.device_common.edit_device(device_serial)
        sleep(5)

        self.utils.print_info("Click on interface settings tab")
        self.auto_actions.click_reference(self.get_interface_settings_tab_single_device)
        self.screen.save_screen_shot()

        self._go_to_wireless_interface_settings_page()
        self.screen.save_screen_shot()

        self.utils.print_info("Click WiFi2 Interface tab")
        self.auto_actions.click_reference(self.get_device_config_wireless_interfaces_wifi2_tab)
        self.screen.save_screen_shot()

        if interface_status.upper() == "ENABLE":
            self.utils.print_info("Enable Status of WiFi2 Interface")
            if not self.get_device_config_wireless_interfaces_wifi2_status_radio_button().is_selected():
                self.auto_actions.click_reference(self.get_device_config_wireless_interfaces_wifi2_status_radio_button)
                self.screen.save_screen_shot()
                sleep(5)
            else:
                self.utils.print_info("WiFi2 Interface already Enabled")

        if interface_status.upper() == "DISABLE":
            self.utils.print_info("Disable Status of WiFi2 Interface")
            if self.get_device_config_wireless_interfaces_wifi2_status_radio_button().is_selected():
                self.auto_actions.click_reference(self.get_device_config_wireless_interfaces_wifi2_status_radio_button)
                self.screen.save_screen_shot()
                sleep(5)
            else:
                self.utils.print_info("WiFi2 Interface already Disabled")

        if not self.get_manage_device_interface_settings_save_button_disabled():
            self.utils.print_info("Click Interface Settings Save Button.")
            self.auto_actions.click_reference(self.get_manage_device_edit_wireless_interface_save_button)
            self.screen.save_screen_shot()
            sleep(2)

            tool_tip_text = tool_tip.tool_tip_text
            self.screen.save_screen_shot()
            sleep(2)

            self.utils.print_info("Click Interface Settings Cancel Button")
            self.auto_actions.click_reference(self.get_manage_device_edit_wireless_interface_cancel_button)
            sleep(2)

            self.utils.print_info("Close Dialogue Window")
            self.auto_actions.click_reference(self.get_close_dialog)
            self.screen.save_screen_shot()
            sleep(2)

            self.utils.print_info("Tool tip Text Displayed on Page", tool_tip_text)
            if "Interface Settings were updated successfully." in tool_tip_text:
                kwargs['pass_msg'] = "Interface Settings were updated successfully"
                self.common_validation.passed(**kwargs)
                return 1
            else:
                kwargs['fail_msg'] = "Interface Settings were updated unsuccessfully"
                self.common_validation.failed(**kwargs)
                return -1
        else:
            self.utils.print_info("Click Interface Settings Cancel Button.")
            self.auto_actions.click_reference(self.get_manage_device_edit_wireless_interface_cancel_button)
            sleep(2)

            self.utils.print_info("Close Dialogue Window")
            self.auto_actions.click_reference(self.get_close_dialog)
            self.screen.save_screen_shot()
            sleep(2)
            kwargs['pass_msg'] = "Successfully change wifi2 interface status"
            self.common_validation.passed(**kwargs)
            return 1

    def configure_wifi2_transmission_power(self, transmission_mode='', power_value="default", **kwargs):
        """
        - - This keyword will Configure the WiFi2 interface power status of AP4000 or AP4000U
        - Flow : Click AP MAC Link --> Configure-->Wireless Interfaces--> WiFi2 interface --> Transmission Power
        - Keyword Usage:
        - ``Configure WiFi2 Transmission Power   'Auto' ``
        - ``Configure WiFi2 Transmission Power   'Manual'    ${POWER_VALUE}='13' ``

        :param transmission_mode : Transmission Mode ie 'Manual' or 'Auto'
        :param power_value: Enter power between 1dbm and 20dbm (Numerical value only)
        :return: 1
        """
        if transmission_mode == "Auto":
            self.utils.print_info("Enable Transmission Power Mode To Auto")
            CloudDriver().cloud_driver.execute_script("arguments[0].click();", self.get_wireless_interface_wifi2_transmission_mode_auto())
            sleep(2)

        if transmission_mode == "Manual":
            self.utils.print_info("Enable Transmission Power Mode To Manual")
            CloudDriver().cloud_driver.execute_script("arguments[0].click();", self.get_wireless_interface_wifi2_transmission_mode_manual())
            sleep(2)

            if power_value != "default":
                current_value = self.wifi2_transmission_power_value_text().text
                self.utils.print_info("Current Transmission Power Value is: ", current_value)

                count = 1
                while power_value != current_value:
                    self.utils.print_info("Click and Hold Slider")
                    self.auto_actions.click_and_hold_element(self.get_wifi2_transmission_power_slider_button())
                    sleep(2)

                    updated_value = self.wifi2_transmission_power_value_text().text
                    self.utils.print_info("Updated Transmission Power Value is: ", updated_value)
                    if updated_value == power_value:
                        break
                    count += 1
            self.screen.save_screen_shot()

        self.utils.print_info("Click on interface settings save button")
        self.auto_actions.click_reference(self.get_interface_settings_save_button)
        sleep(5)

        self.utils.print_info("Click on Update button")
        self.auto_actions.click_reference(self.get_interface_settings_update_button)

        self.utils.print_info("Click on Perform Update")
        self.get_interface_settings_perform_update_button().click()

        self.utils.print_info("Close the device360 page dialog window")
        self.get_close_device360_dialog_window().click()
        kwargs['pass_msg'] = "successfully configure wifi2 transmission power"
        self.common_validation.passed(**kwargs)
        return 1

    def override_ap_config_wireless_channel(self, device_mac, interface='WiFi0', override_channel='6', **kwargs):
        """
        - This keyword will configure the WiFi0-1-2 interface channel
        - Flow : Manage --> Device --> Click AP MAC Link --> Configure--> Interface Settings --> Wireless Interface
        - Keyword Usage:
        - ``Override AP Config Wireless Channel   device_mac=${AP1_MAC}   interface='WiFi0'  override_channel='6' ``

        :param device_mac:  device_mac address
        :param interface: device interface i.e WiFi0/WiFi1/WIFI2
        :param override_channel:  override channel
        :return: returns 1 if successful else -1
        """
        try:
            self.utils.print_info("Navigating to device page")
            if self.navigator.navigate_to_device360_page_with_mac(device_mac) == -1:
                self.utils.print_info(f"Device not found in the device row grid with mac:{device_mac}")
                return -1
            self.utils.print_info("click on configuration tab")
            self.auto_actions.click_reference(self.get_configuration_tab)
            self.utils.print_info("Click on interface settings tab")
            self.auto_actions.click_reference(self.get_interface_settings_tab)
            self._go_to_wireless_interface_settings_page()
            sleep(3)
            self.auto_actions.click_reference(self.get_wifi0_interface_tab)
            self.auto_actions.click_reference(self.get_override_client_access_wifi0_checked)
            self.auto_actions.click_reference(self.get_override_client_access_wifi0_checked)
            self.auto_actions.click_reference(self.get_interface_settings_save_button)
            sleep(3)
            self._go_to_wireless_interface_settings_page()

            if interface.lower() == 'wifi0':
                self.utils.print_info("Click on WiFi0 interface tab")
                self.auto_actions.click_reference(self.get_wifi0_interface_tab)
                self.utils.print_info(f"select the channel: {override_channel}")
                self.auto_actions.click_reference(self.get_wireless_wifi0_channel_dropdown())
                self.auto_actions.select_drop_down_options(self.get_wireless_interface_wifi0_channel_options(), override_channel)
            elif interface.lower() == 'wifi1':
                self.utils.print_info("Click on WiFi1 interface tab")
                self.auto_actions.click_reference(self.get_wifi1_interface_tab)
                self.utils.print_info(f"select the channel: {override_channel}")
                self.auto_actions.click_reference(self.get_wireless_wifi1_channel_dropdown)
                self.auto_actions.select_drop_down_options(self.get_wireless_interface_wifi1_channel_options(), override_channel)
            elif interface.lower() == 'wifi2':
                self.utils.print_info("Click on WiFi2 interface tab")
                self.auto_actions.click_reference(self.get_wifi2_interface_tab)
                self.utils.print_info(f"select the channel: {override_channel}")
                self.auto_actions.click_reference(self.get_wireless_wifi2_channel_dropdown)
                self.auto_actions.select_drop_down_options(self.get_wireless_interface_wifi2_channel_options(), override_channel)
            else:
                self.utils.print_info("Can you specify interface(wifi0, wifi1, or wifi1)?")

            self.utils.print_info("Click on interface settings save button")
            self.auto_actions.click_reference(self.get_interface_settings_save_button)
            sleep(3)
            self.screen.save_screen_shot()
            tool_tp_text = tool_tip.tool_tip_text
            self.utils.print_info(tool_tp_text)
            self.utils.print_info("Close the override device page dialog window")
            self.auto_actions.click_reference(self.get_close_device360_dialog_window)

            if 'Interface Settings were updated successfully.' in tool_tp_text:
                kwargs['pass_msg'] = "Interface Settings were updated successfully."
                self.common_validation.passed(**kwargs)
                return 1
            else:
                kwargs['fail_msg'] = "Interface Settings were updated unsuccessfully."
                self.common_validation.failed(**kwargs)
                return -1
        except Exception:
            kwargs['fail_msg'] = "Not able to navigate/set to the page"
            self.common_validation.fault(**kwargs)
            return -1

    def get_override_ap_configure_wifi_details(self, device_mac, wifi_interface_config, **kwargs):
        """
        - This keyword will get ap configure WiFi0-1-2 interface
        - Flow : Manage --> Device --> Click AP MAC Link --> Configure--> Interface Settings --> Wireless Interface
        - Keyword Usage
        - ``Get Override AP Configure Wifi Details     device_mac=${AP1_MAC}    ${AP_TEMPLATE_CONFIG}``

        :param device_mac:  device_mac address
        :param wifi_interface_config: (Get Dict) Enable/Disable Client Access,Backhaul Mesh Link,Sensor etc
        :return: return wifi_interface_config if successfully else -1
        """
        wifi0_config = wifi_interface_config.get('wifi0_configuration', 'None')
        wifi1_config = wifi_interface_config.get('wifi1_configuration', 'None')
        wifi2_config = wifi_interface_config.get('wifi2_configuration', 'None')
        wired_config = wifi_interface_config.get('wired_configuration', 'None')

        try:
            self.utils.print_info("Navigating to device page")
            if self.navigator.navigate_to_device360_page_with_mac(device_mac) == -1:
                kwargs['fail_msg'] = f"Device not found in the device row grid with mac: {device_mac}"
                self.common_validation.fault(**kwargs)
                return -1
            self.utils.print_info("click on configuration tab")
            self.auto_actions.click_reference(self.get_configuration_tab)
            self.utils.print_info("Click on interface settings tab")
            self.auto_actions.click_reference(self.get_interface_settings_tab)
            self.utils.print_info("Expanse Wireless interfaces")
            self._go_to_wireless_interface_settings_page()
            sleep(3)

            if wifi0_config != 'None':
                self.utils.print_info("Get WiFI0 Interface details")
                wifi_interface_config['wifi0_configuration'] = self._get_ap_configure_wifi0_details(**wifi0_config)
                self.screen.save_screen_shot()

            if wifi1_config != 'None':
                self.utils.print_info("Get WiFI1 Interface details")
                wifi_interface_config['wifi1_configuration'] = self._get_ap_configure_wifi1_details(**wifi1_config)
                self.screen.save_screen_shot()

            if wifi2_config != 'None':
                self.utils.print_info("Get WiFI2 Interface details")
                wifi_interface_config['wifi2_configuration'] = self._get_ap_configure_wifi2_details(**wifi2_config)
                self.screen.save_screen_shot()

            if wired_config != 'None':
                self.utils.print_info("Get Wired Interface details")
                wifi_interface_config['wired_configuration'] = self._get_ap_configure_wired_details(**wired_config)
                self.screen.save_screen_shot()

            self.utils.print_info("Click on the cancel button")
            self.auto_actions.click_reference(self.get_manage_device_edit_wireless_interface_cancel_button)
            self.utils.print_info("Click close dialog window")
            self.auto_actions.click_reference(self.get_close_device360_dialog_window)
            kwargs['pass_msg'] = "Successful to get device configure details"
            self.common_validation.passed(**kwargs)
            return wifi_interface_config

        except Exception as e:
            kwargs['fail_msg'] = f"get_ap_template_wifi() failed. Actual error is : - {e} -"
            self.common_validation.fault(**kwargs)
            return -1

    def _get_ap_configure_wifi0_details(self, **wifi0_profile):
        """
        - Get the WIFI0 configuration in device configure details

        :param wifi0_profile: (Get Dict) Enable/Disable Client mode, Client Access,Backhaul Mesh Link, Sensor
        :return: wifi0_profile if Get WiFi0 Profile Successfully else None
        """
        radio_status_wifi0 = wifi0_profile.get('radio_status', 'None')  # radio_status=get or yes
        radio_operating_mode_wifi0 = wifi0_profile.get('operating_mode', 'None')
        radio_profile_wifi0 = wifi0_profile.get('radio_profile', 'None')
        client_mode_status_wifi0 = wifi0_profile.get('client_mode', 'None')
        client_access_status_wifi0 = wifi0_profile.get('client_access', 'None')
        backhaul_mesh_status_wifi0 = wifi0_profile.get('backhaul_mesh_link', 'None')
        sensor_status_wifi0 = wifi0_profile.get('sensor', 'None')
        enable_SDR_wifi0 = wifi0_profile.get('enable_SDR', 'None')

        self.utils.print_info("Click on WiFi0 interface tab")
        self.auto_actions.click_reference(self.get_wifi0_interface_tab)

        if radio_status_wifi0 != 'None':
            wifi0_profile['radio_status'] = self._convert_boolean_to_on_off(
                self.get_device_override_configure_interface_settings_wifi0_radio_status().is_selected())
            self.utils.print_info("Get Radio Status on WiFi0 Interface: ", wifi0_profile['radio_status'])
            if wifi0_profile['radio_status'] == 'Off':
                return wifi0_profile
        self.auto_actions.scroll_down()

        if radio_operating_mode_wifi0 != 'None':
            wifi0_profile['operating_mode'] = self.get_default_wireless_wifi0_radio_operating_mode_drop_down().text
            self.utils.print_info("Get Radio Profile status on WiFi0 Interface: ", wifi0_profile['operating_mode'])

        if radio_profile_wifi0 != 'None':
            wifi0_profile['radio_profile'] = self.get_default_wireless_wifi0_radio_profile_drop_down().text
            self.utils.print_info("Get Radio Profile status on WiFi0 Interface: ", wifi0_profile['radio_profile'])

        if client_mode_status_wifi0 != 'None':
            wifi0_profile['client_mode'] = self._convert_boolean_to_enable_disable(
                self.get_override_client_mode_wifi0_checked().is_selected())
            self.utils.print_info("Get Client Mode Checkbox on WiFi0 Interface: ", wifi0_profile['client_mode'])

        if client_access_status_wifi0 != 'None':
            wifi0_profile['client_access'] = self._convert_boolean_to_enable_disable(
                self.get_wireless_wifi0_radio_usage_client_access_checkbox().is_selected())
            self.utils.print_info("Get Client Access Checkbox on WiFi0 Interface: ", wifi0_profile['client_access'])

        if backhaul_mesh_status_wifi0 != 'None':
            wifi0_profile['backhaul_mesh_link'] = self._convert_boolean_to_enable_disable(
                self.get_wireless_wifi0_radio_usage_blackhaul_mesh_link_checkbox().is_selected())
            self.utils.print_info("Get Backhaul Mesh Link Checkbox on WiFi0 Interface: ",
                                  wifi0_profile['backhaul_mesh_link'])

        if sensor_status_wifi0 != 'None':
            if self.cobj_web_elements.get_common_object_wifi0_sensor_UI_disable():
                wifi0_profile['sensor'] = 'UIDisable'
            else:
                wifi0_profile['sensor'] = self._convert_boolean_to_enable_disable(self.get_wireless_wifi0_radio_usage_sensor_checkbox().is_selected())
            self.utils.print_info("Get Sensor Checkbox on WiFi0 Interface: ", wifi0_profile['sensor'])

        if enable_SDR_wifi0 != 'None':
            wifi0_profile['enable_SDR'] = self._convert_boolean_to_enable_disable(
                self.cobj_web_elements.get_common_object_ap_template_enable_sdr().is_selected())
            self.utils.print_info("Get Enable SDR Checkbox on WiFi0 Interface: ", wifi0_profile['enable_SDR'])

        return wifi0_profile

    def _get_ap_configure_wifi1_details(self, **wifi1_profile):
        """
        - Get the WIFI1 configuration in device configure details

        :param wifi1_profile: (Get Dict) Enable/Disable Client mode, Client Access,Backhaul Mesh Link, Sensor
        :return: wifi1_profile if Get WiFi1 Profile Successfully else None
        """
        radio_status_wifi1 = wifi1_profile.get('radio_status', 'None')  # radio_status=get or yes
        radio_profile_wifi1 = wifi1_profile.get('radio_profile', 'None')
        client_mode_status_wifi1 = wifi1_profile.get('client_mode', 'None')
        client_access_status_wifi1 = wifi1_profile.get('client_access', 'None')
        backhaul_mesh_status_wifi1 = wifi1_profile.get('backhaul_mesh_link', 'None')
        sensor_status_wifi1 = wifi1_profile.get('sensor', 'None')

        self.utils.print_info("Click on WiFi1 interface tab")
        self.auto_actions.click_reference(self.get_wifi1_interface_tab)

        if radio_status_wifi1 != 'None':
            wifi1_profile['radio_status'] = self._convert_boolean_to_on_off(
                self.get_device_override_configure_interface_settings_wifi1_radio_status().is_selected())
            self.utils.print_info("Get Radio Status on WiFi1 Interface: ", wifi1_profile['radio_status'])
            if wifi1_profile['radio_status'] == 'Off':
                return wifi1_profile
        self.auto_actions.scroll_down()

        if radio_profile_wifi1 != 'None':
            wifi1_profile['radio_profile'] = self.get_default_wireless_wifi1_radio_profile_drop_down().text
            self.utils.print_info("Get Radio Profile status on WiFi1 Interface: ", wifi1_profile['radio_profile'])

        if client_mode_status_wifi1 != 'None':
            wifi1_profile['client_mode'] = self._convert_boolean_to_enable_disable(
                self.get_override_client_mode_wifi1_checked().is_selected())
            self.utils.print_info("Get Client Mode Checkbox on WiFi1 Interface: ", wifi1_profile['client_mode'])

        if client_access_status_wifi1 != 'None':
            wifi1_profile[
                'client_access'] = self._convert_boolean_to_enable_disable(
                self.get_wireless_wifi1_radio_usage_client_access_checkbox().is_selected())
            self.utils.print_info("Get Client Access Checkbox on WiFi1 Interface: ", wifi1_profile['client_access'])

        if backhaul_mesh_status_wifi1 != 'None':
            wifi1_profile['backhaul_mesh_link'] = self._convert_boolean_to_enable_disable(
                self.get_wireless_wifi1_radio_usage_blackhaul_mesh_link_checkbox().is_selected())
            self.utils.print_info("Get Backhaul Mesh Link Checkbox on WiFi1 Interface: ",
                                  wifi1_profile['backhaul_mesh_link'])

        if sensor_status_wifi1 != 'None':
            if self.cobj_web_elements.get_common_object_wifi1_sensor_UI_disable():
                wifi1_profile['sensor'] = 'UIDisable'
            else:
                wifi1_profile['sensor'] = self._convert_boolean_to_enable_disable(self.get_wireless_wifi1_radio_usage_sensor_checkbox().is_selected())
            self.utils.print_info("Get Sensor Checkbox on WiFi1 Interface: ", wifi1_profile['sensor'])

        return wifi1_profile

    def _get_ap_configure_wifi2_details(self, **wifi2_profile):
        """
        - Get the WIFI2 configuration in device configure details

        :param wifi2_profile: (Get Dict) Enable/Disable Client mode, Client Access,Backhaul Mesh Link, Sensor
        :return: wifi2_profile if Get WiFi2 Profile Successfully else None
        """
        radio_status_wifi2 = wifi2_profile.get('radio_status', 'None')  # radio_status=get or yes
        radio_profile_wifi2 = wifi2_profile.get('radio_profile', 'None')
        client_access_status_wifi2 = wifi2_profile.get('client_access', 'None')
        backhaul_mesh_status_wifi2 = wifi2_profile.get('backhaul_mesh_link', 'None')
        sensor_status_wifi2 = wifi2_profile.get('sensor', 'None')

        try:
            self.utils.print_info("Click on WiFi2 interface tab")
            self.auto_actions.click_reference(self.get_wifi2_interface_tab)
        except Exception:
            return wifi2_profile

        if radio_status_wifi2 != 'None':
            wifi2_profile['radio_status'] = self._convert_boolean_to_on_off(
                self.get_device_override_configure_interface_settings_wifi2_radio_status().is_selected())
            self.utils.print_info("Get Radio Status on WiFi2 Interface: ", wifi2_profile['radio_status'])
            if wifi2_profile['radio_status'] == 'Off':
                return wifi2_profile
        self.auto_actions.scroll_down()

        if radio_profile_wifi2 != 'None':
            wifi2_profile['radio_profile'] = self.get_default_wireless_wifi2_radio_profile_drop_down().text
            self.utils.print_info("Get Radio Profile status on WiFi2 Interface: ", wifi2_profile['radio_profile'])

        if client_access_status_wifi2 != 'None':
            wifi2_profile['client_access'] = self._convert_boolean_to_enable_disable(
                self.get_wireless_wifi2_radio_usage_client_access_checkbox().is_selected())
            self.utils.print_info("Get Client Access Checkbox on WiFi2 Interface: ", wifi2_profile['client_access'])

        if backhaul_mesh_status_wifi2 != 'None':
            wifi2_profile[
                'backhaul_mesh_link'] = self._convert_boolean_to_enable_disable(
                self.get_wireless_wifi2_radio_usage_blackhaul_mesh_link_checkbox().is_selected())
            self.utils.print_info("Get Backhaul Mesh Link Checkbox on WiFi2 Interface: ",
                                  wifi2_profile['backhaul_mesh_link'])

        if sensor_status_wifi2 != 'None':
            if self.cobj_web_elements.get_common_object_wifi2_sensor_UI_disable():
                wifi2_profile['sensor'] = 'UIDisable'
            else:
                wifi2_profile['sensor'] = self._convert_boolean_to_enable_disable(self.get_wireless_wifi2_radio_usage_sensor_checkbox().is_selected())
            self.utils.print_info("Get Sensor Checkbox on WiF2 Interface: ", wifi2_profile['sensor'])

        return wifi2_profile

    def _get_ap_configure_wired_details(self, **wired_profile):
        """
        - Get the Wired Interfaces in device configure details

        :param wired_profile: (Get Dict) Enable/Disable Eth0, Eth1, and etc
        :return: wired_profile if Successfully else None
        """
        eth0 = wired_profile.get('eth0', 'None')  # eth0=get or yes
        eth1 = wired_profile.get('eth1', 'None')
        transmission_type_eth0 = wired_profile.get('transmission_type_eth0', 'None')
        transmission_type_eth1 = wired_profile.get('transmission_type_eth1', 'None')
        speed_eth0 = wired_profile.get('speed_eth0', 'None')
        speed_eth1 = wired_profile.get('speed_eth0', 'None')
        lldp_eth0 = wired_profile.get('lldp_eth0', 'None')
        lldp_eth1 = wired_profile.get('lldp_eth1', 'None')
        cdp_eth0 = wired_profile.get('cdp_eth0', 'None')
        cdp_eth1 = wired_profile.get('cdp_eth1', 'None')

        self._go_to_wired_interface_settings_page()
        if eth0 != 'None':
            wired_profile['eth0'] = self._convert_boolean_to_on_off(self.get_devices_config_wired_eth0().is_selected())
            self.utils.print_info('Eth0 status: ', wired_profile['eth0'])

        if eth1 != 'None':
            wired_profile['eth1'] = self._convert_boolean_to_on_off(self.get_devices_config_wired_eth1().is_selected())
            self.utils.print_info('Eth1 status: ', wired_profile['eth1'])

        if transmission_type_eth0 != 'None':
            wired_profile[
                'transmission_type_eth0'] = self.cobj_web_elements.get_common_object_ap_template_eth0_transmission_type().text
            self.utils.print_info('Transmission type eth0 status: ', wired_profile['transmission_type_eth0'])

        if transmission_type_eth1 != 'None':
            wired_profile[
                'transmission_type_eth1'] = self.cobj_web_elements.get_common_object_ap_template_eth1_transmission_type().text
            self.utils.print_info('Transmission type eth1 status: ', wired_profile['transmission_type_eth1'])

        if speed_eth0 != 'None':
            wired_profile['speed_eth0'] = self.cobj_web_elements.get_common_object_ap_template_eth0_speed().text
            self.utils.print_info('Speed eth0 status: ', wired_profile['speed_eth0'])

        if speed_eth1 != 'None':
            wired_profile['speed_eth1'] = self.cobj_web_elements.get_common_object_ap_template_eth1_speed().text
            self.utils.print_info('Speed eth1 status: ', wired_profile['speed_eth1'])

        if lldp_eth0 != 'None':
            wired_profile['lldp_eth0'] = self._convert_boolean_to_enable_disable(self.get_devices_config_wired_eth0_lldp().is_selected())
            self.utils.print_info('LLDP eth0 status: ', wired_profile['lldp_eth0'])

        if lldp_eth1 != 'None':
            wired_profile['lldp_eth1'] = self._convert_boolean_to_enable_disable(self.get_devices_config_wired_eth1_lldp().is_selected())
            self.utils.print_info('LLDP eth1 status: ', wired_profile['lldp_eth1'])

        if cdp_eth0 != 'None':
            wired_profile['cdp_eth0'] = self._convert_boolean_to_enable_disable(self.get_devices_config_wired_eth0_cdp().is_selected())
            self.utils.print_info('CDP eth0 status: ', wired_profile['cdp_eth0'])

        if cdp_eth1 != 'None':
            wired_profile['cdp_eth1'] = self._convert_boolean_to_enable_disable(self.get_devices_config_wired_eth1_cdp().is_selected())
            self.utils.print_info('CDP eth1 status: ', wired_profile['cdp_eth1'])

        return wired_profile

    def _convert_boolean_to_enable_disable(self, boolean):
        """
        - Convert boolean to Enable or Disable
        :param boolean : True or False
        :return: Enable or Disable
        """
        return 'Enable' if boolean else 'Disable'

    def _convert_boolean_to_on_off(self, boolean):
        """
        - Convert boolean to On or Off
        :param boolean : True or False
        :return: Enable or Disable
        """
        return 'On' if boolean else 'Off'

    def override_wifi2_channel(self, channel_input='default', **kwargs):
        """
        - - This keyword will Configure the WiFi2 interface power status of AP4000 or AP4000U
        - Flow : Click AP MAC Link --> Configure-->Wireless Interfaces--> WiFi2 interface --> Channel Dropdown
        - Keyword Usage:
        - ``Override wifi2 channel   ${CHANNEL_INPUT}='Auto' ``
        - ``Override wifi2 channel   ${CHANNEL_INPUT}='7' ``

        :param channel_input: Input AP channel ('Auto' for default configuration)
        :return: 1
        """
        self.utils.print_info("Channel Configuration: " + str(channel_input))
        try:
            self.auto_actions.click_reference(self.get_wireless_wifi2_channel_dropdown)
            locator = self.get_wireless_wifi2_channel_list(str(channel_input))
            self.utils.print_info(" LOCATOR ------ " + str(locator))
            element = self.web.get_element(locator)
            element.click()
            CloudDriver().cloud_driver.execute_script("arguments[0].click();", element)

        except Exception:
            kwargs['fail_msg'] = "Not able to configure any channel; leaving as default."
            self.common_validation.fault(**kwargs)
            return -1

        element = self.get_wireless_wifi2_channel_dropdown()
        if element.text != channel_input:
            self.utils.print_info("Channel does not match with " + str(element.text))

        self.utils.print_info("Click on interface settings save button")
        self.auto_actions.click_reference(self.get_interface_settings_save_button)
        sleep(5)

        self.utils.print_info("Click on Update button")
        self.auto_actions.click_reference(self.get_interface_settings_update_button)

        self.utils.print_info("Click on Perform Update")
        self.get_interface_settings_perform_update_button().click()

        self.utils.print_info("Close the device360 page dialog window")
        self.get_close_device360_dialog_window().click()

        kwargs['pass_msg'] = "Successfully override wifi2 channel"
        self.common_validation.passed(**kwargs)
        return 1

    def get_unique_clients_number(self, device_mac="", **kwargs):
        """
        - Get the number of Unique Clients on AP using AP's serial number,Name or Mac address.
        - Keyword Usage:
        - ``Get Unique Client Number   ap_mac=${AP_MAC}``

        :param device_mac: Ap mac Ex: F09CE9F89600
        :return: Number of unique clients as shown on device 360 page.
        """
        try:
            self.utils.print_info("Navigating to device 360 page")
            if self.navigator.navigate_to_device360_page_with_mac(device_mac) == -1:
                kwargs['fail_msg'] = f"Device not found in the device row grid with mac:{device_mac}"
                self.common_validation.failed(**kwargs)
                return -1
        except Exception:
            self.utils.print_info("Not able to navigate to the page")
        sleep(5)

        self.utils.print_info("Retrieve the total number of unique clients")
        unique_clients = self.get_total_unique_clients().text
        self.utils.print_info("Total Number of Unique Clients = ", unique_clients)

        return unique_clients

    def get_unique_client_details(self, device_mac, search_string, **kwargs):
        """
        - Stores the Unique Client Page device row's keys and values in a dictionary based on the passed search string.
        - Supported search_strings are Column headers like Hostname, MAC Address and IP Address
        - Keyword Usage:
        - ``Get Unique Client Details    ${AP_MAC}     search_string=1418C347F9B4``

        :param search_string: Enter Client Hostname, Client MAC Address or IP Address (Client MAC Ex: 1418C347F9B4)
        :param device_mac: Device MAC Ex: F09CE9F89600
        :return: Dictionary including these keys -> TYPE, OS TYPE, CURRENT CONNECT STATUS, HEALTH STATUS,
        HOST NAME, CLIENT MAC, IPv4, IPv6, User Name, VLAN, Connected Via, RSSI, SNR
        """
        try:
            self.utils.print_info("Navigating to device 360 page")
            if self.navigator.navigate_to_device360_page_with_mac(device_mac) == -1:
                kwargs['fail_msg'] = f"Device not found in the device row grid with mac:{device_mac}"
                self.common_validation.failed(**kwargs)
                return -1
        except Exception:
            kwargs['fail_msg'] = "Not able to navigate to the page"
            self.common_validation.fault(**kwargs)
        sleep(5)

        self.utils.print_info("Click on Clients")
        CloudDriver().cloud_driver.execute_script("arguments[0].click();", self.get_go_to_clients())
        sleep(3)

        total_client_count = self.get_total_client_count().text
        self.utils.print_info("Total Clients = ", total_client_count)

        poor_client_count = self.get_poor_client_count().text
        self.utils.print_info("Clients with Poor Health = ", poor_client_count)

        self.utils.print_info("Searching Device Entry with Search String : ", search_string)
        self.auto_actions.send_keys(self.get_unique_clients_search_field(), search_string)
        self.screen.save_screen_shot()
        sleep(5)

        self.utils.print_info("Retrieve the device's unique client information")
        client_info = dict()

        client_info["Connection Type"] = self.get_client_connection_type().text
        client_info["OS Type"] = self.get_client_os_type().text
        client_info["Connection Status"] = self.get_client_connection_status().text
        client_info["Client Health Status"] = self.get_client_health_status().text
        client_info["Host Name"] = self.get_client_hostname().text
        client_info["Client Mac"] = self.get_client_mac().text
        client_info["IPv4"] = self.get_client_IPv4().text
        client_info["IPv6"] = self.get_client_IPv6().text
        client_info["User Name"] = self.get_client_user_name().text
        client_info["VLAN"] = self.get_client_vlan().text
        client_info["Connected via"] = self.get_client_connected_via().text
        client_info["RSSI"] = self.get_client_rssi().text
        client_info["SNR"] = self.get_client_snr().text

        return client_info

    def navigate_to_device_config_device_config_dhcp(self, device_mac, dhcp="ENABLE", **kwargs):
        """
        - This keyword will retrieve the all settings in the device configuration interface WiFi2 page
        - Flow: Manage --> Device --> Click on Device MAC hyperlink --> click on configure --> Device Configuration
                -->dhcp

        - Keyword Usage:
        - ``navigate_to_device_config_device   ${DEVICE_MAC}   Enable''

        :param device_mac: device MAC to go to device 360 page
        :param dhcp: Enable/Disable
        :return: 1 or -1
        """

        try:
            self.utils.print_info("Navigating to device 360 page")
            if self.navigator.navigate_to_device360_page_with_mac(device_mac) == -1:
                self.utils.print_info(f"Device not found in the device row grid with mac:{device_mac}")
                return -1

            self.utils.print_info("click on configuration tab")
            self.auto_actions.click_reference(self.get_configuration_tab)
            self.utils.print_info("Click on Device Configuration tab")
            self.auto_actions.click_reference(self.get_device_configuration_tab)

            dhcp_status = self.get_device_configuration_dhcp_checkbox().is_selected()
            if dhcp.upper() == "ENABLE" and not dhcp_status:
                self.utils.print_info("Enable -> Use DHCP only to set IP Address")
                self.auto_actions.click_reference(self.get_device_configuration_dhcp_checkbox)
            elif dhcp.upper() == "DISABLE" and dhcp_status:
                self.utils.print_info("Disable -> Use DHCP only to set IP Address")
                self.auto_actions.click_reference(self.get_device_configuration_dhcp_checkbox)
            self.utils.print_info("Save Device Configuration")
            self.auto_actions.click_reference(self.get_device_override_save_device_configuration)
            sleep(2)
            self.utils.print_info("Close Dialogue Window")
            self.auto_actions.click_reference(self.get_close_dialog)
            sleep(2)
        except Exception:
            kwargs['fail_msg'] = "Not able to navigate to the page"
            self.common_validation.fault(**kwargs)
            return -1
        kwargs['pass_msg'] = "Successfully navigate to device config dhcp"
        self.common_validation.passed(**kwargs)
        return 1

    def navigate_to_device_config_interface_wireless(self, device_mac, interface='wifi2', **kwargs):
        """
        - This keyword will retrieve the all settings in the device configuration interface WiFi2 page
        - Flow: Manage --> Device --> Click on Device MAC hyperlink --> click on configure --> interface settings
                --> wireless --> WiFi2

        - Keyword Usage:
        - ``navigate_to_device_config_interface_wireless_wifi2   ${DEVICE_MAC}  ''

        :param device_mac: device MAC to go to device 360 page
        :param interface: interface name to get the override parameters, WiFi0, WiFi1, WiFi2
        :return: 1 or -1
        """

        try:
            self.utils.print_info("Navigating to device 360 page")
            if self.navigator.navigate_to_device360_page_with_mac(device_mac) == -1:
                kwargs['fail_msg'] = f"Device not found in the device row grid with mac:{device_mac}"
                self.common_validation.failed(**kwargs)
                return -1

            self.utils.print_info("click on configuration tab")
            self.auto_actions.click_reference(self.get_configuration_tab)
            self.utils.print_info("Click on interface settings tab")
            self.auto_actions.click_reference(self.get_interface_settings_tab_single_device)
            self.utils.print_info("Click on the wireless link")
            self._go_to_wireless_interface_settings_page()

            if interface in ['wifi2', 'WIFI2']:
                self.utils.print_info("Click on the wifi2 tab")
                self.auto_actions.click_reference(self.get_wifi2_interface_tab)

                self.utils.print_info("Enable the radio status if the button is not enabled")
                status = self._check_wifi2_radio_status()
                self.enable_radio_status(status, interface='wifi2')
                if status == 'OFF':
                    self.utils.print_info("Enable the radio status")
                    self._go_to_wireless_interface_settings_page()
                    self.auto_actions.click_reference(self.get_wifi2_interface_tab)

            if interface in ['wifi1', 'WIFI1']:
                self.utils.print_info("Click on the wifi1 tab")
                self.auto_actions.click_reference(self.get_wifi1_interface_tab)

                self.utils.print_info("Enable the radio status if the button is not enabled")
                status = self._check_wifi1_radio_status()
                self.enable_radio_status(status, interface='wifi1')
                if status == 'OFF':
                    self.utils.print_info("Enable the radio status")
                    self._go_to_wireless_interface_settings_page()
                    self.auto_actions.click_reference(self.get_wifi1_interface_tab)

            if interface in ['wifi0', 'WIFI0']:
                self.utils.print_info("Click on the wifi0 tab")
                self.auto_actions.click_reference(self.get_wifi0_interface_tab)

                self.utils.print_info("Enable the radio status if the button is not enabled")
                status = self._check_wifi0_radio_status()
                self.enable_radio_status(status, interface='wifi0')
                if status == 'OFF':
                    self.utils.print_info("Enable the radio status")
                    self._go_to_wireless_interface_settings_page()
                    self.auto_actions.click_reference(self.get_wifi0_interface_tab)

        except Exception:
            kwargs['fail_msg'] = "Not able to navigate to the page"
            self.common_validation.fault(**kwargs)

        kwargs['pass_msg'] = "Successfully navigate to device config interface wireless"
        self.common_validation.passed(**kwargs)
        return 1

    def get_device_configuration_interface_WiFi2_details(self):
        """
        - This keyword fetches all values on the device configuration interface WiFi2 page
        - Flow: Manage --> Device --> Click on Device MAC hyperlink --> click on configure --> interface settings
                --> WiFi2
        - Keyword Usage:
        - ``get_device_configuration_interface_WiFi2_details  ''

        """
        sleep(5)
        self.utils.print_info("Retrieve the device configuration interface wireless Wifi2")
        interface_info = dict()
        interface_info["device_model"] = self.get_wireless_wifi_device_model().text
        interface_info["device_template"] = self.get_wireless_wifi_device_template().text
        interface_info["radio_status"] = self._check_wifi2_radio_status()
        interface_info["radio_mode"] = self.get_wireless_wifi2_radio_mode().text
        interface_info["radio_profile"] = self.get_default_wireless_wifi2_radio_profile_drop_down().text
        interface_info["channel"] = self.get_wireless_wifi2_channel_dropdown().text
        channel = self.get_wireless_wifi2_channel_width_text().text
        interface_info["channel_width"] = channel[-5:]

        interface_info["override_channel"] = self._check_override_channel_exclusion_setting_radio_profile_status(
            interface='wifi2')
        interface_info["client_access"] = self._check_wifi_client_access_status(interface='wifi2')
        interface_info["blackhaul_mesh_link"] = self._check_wifi_usage_blackhaul_mesh_link_status(interface='wifi2')

        if self.get_wireless_wifi2_radio_usage_sensor_checkbox().is_selected():
            interface_info["sensor"] = 'ON'
        else:
            interface_info["sensor"] = 'OFF'

        return interface_info

    def get_device_configuration_interface_WiFi1_details(self):
        """
        - This keyword fetches all values on the device configuration interface WiFi2 page
        - Flow: Manage --> Device --> Click on Device MAC hyperlink --> click on configure --> interface settings
                --> WiFi2
        - Keyword Usage:
        - ``get_device_configuration_interface_WiFi2_details  ''

        """
        sleep(5)
        self.utils.print_info("Retrieve the device configuration interface wireless Wifi2")
        interface_info = dict()
        interface_info["device_model"] = self.get_wireless_wifi_device_model().text
        interface_info["device_template"] = self.get_wireless_wifi_device_template().text
        interface_info["radio_status"] = self._check_wifi1_radio_status()
        interface_info["radio_mode"] = self.get_wireless_wifi1_radio_mode().text
        interface_info["radio_profile"] = self.get_default_wireless_wifi1_radio_profile_drop_down().text

        interface_info["channel"] = self.get_wireless_wifi1_channel_dropdown().text
        channel = self.get_wireless_wifi1_channel_width_text().text
        interface_info["channel_width"] = channel[-5:]

        interface_info["override_channel"] = self._check_override_channel_exclusion_setting_radio_profile_status(
            interface='wifi1')
        interface_info["client_access"] = self._check_wifi_client_access_status(interface='wifi1')
        interface_info["blackhaul_mesh_link"] = self._check_wifi_usage_blackhaul_mesh_link_status(interface='wifi1')

        return interface_info

    def get_device_configuration_interface_WiFi0_details(self):
        """
        - This keyword fetches all values on the device configuration interface WiFi0 page
        - Flow: Manage --> Device --> Click on Device MAC hyperlink --> click on configure --> interface settings
                --> WiFi0
        - Keyword Usage:
        - ``get_device_configuration_interface_WiFi2_details  ''

        """
        sleep(5)
        self.utils.print_info("Retrieve the device configuration interface wireless Wifi2")
        interface_info = dict()
        interface_info["device_model"] = self.get_wireless_wifi_device_model().text
        interface_info["device_template"] = self.get_wireless_wifi_device_template().text
        interface_info["radio_status"] = self._check_wifi0_radio_status()
        interface_info["radio_mode"] = self.get_wireless_wifi0_radio_mode().text
        interface_info["radio_profile"] = self.get_default_wireless_wifi0_radio_profile_drop_down().text
        interface_info["channel"] = self.get_wireless_wifi0_channel_dropdown().text
        channel = self.get_wireless_wifi0_channel_width_text().text
        interface_info["channel_width"] = channel[-5:]
        interface_info["override_channel"] = self._check_override_channel_exclusion_setting_radio_profile_status(
            interface='wifi0')
        interface_info["client_access"] = self._check_wifi_client_access_status(interface='wifi0')
        interface_info["blackhaul_mesh_link"] = self._check_wifi_usage_blackhaul_mesh_link_status(interface='wifi0')

        return interface_info

    def close_D360_configuration_page(self):
        """
        - This keyword will close D360 configuration page.
        - Keyword Usage:
        - ``close_D360_configuration_page''
        """
        self.utils.print_info("Click on close D360 popup page")
        self.auto_actions.click_reference(self.get_close_D360_popup)
        self.utils.print_info("able to close D360 popup page")

    def verify_page_details(self, dic1=None, dic2=None, **kwargs):

        """
        - This keyword will validate key value pair on any page.
        - Keyword Usage:
        - '' &{wifi2_interface_detail}=   get_device_configuration_interface_WiFi2_details ''
        - '' &{fields_to_check}=   Create Dictionary   radio_profile=radio_ng_11ax-6g    client_access=OFF   channel_width=80MHz ''

        - `` verify_page_details  ${wifi2_interface_detail}     ${fields_to_check}      ''

        :param  dic1: a dictionary lists of key pair of page detail
        :param  dic2: list of key and values of that page
        :return 1 else -1

        """
        # dic = self._get_page_configuration(page)
        # self.utils.print_info(" /n The current default values show on the current page " + page + ' ' + str(dic))

        for key, value in dic2.items():
            found = False
            self.utils.print_info("The current key and value : " + str(key))
            if (key, value) in dic1.items():
                found = True

            if value == "default":
                if dic2[key] in ['', 'N/A', 'n/a', '0']:
                    kwargs['fail_msg'] = f"value is not by default for {str(key)}"
                    self.common_validation.failed(**kwargs)
                    return -1
                else:
                    found = True

            if value == 'blank':
                if dic2[key] != '':
                    kwargs['fail_msg'] = f"Value is not empty for {str(key)}"
                    self.common_validation.failed(**kwargs)
                    return -1

            if not found:
                kwargs['fail_msg'] = "Page does not contain the value"
                self.common_validation.failed(**kwargs)
                return -1
        kwargs['pass_msg'] = "Successfully verify page details"
        self.common_validation.passed(**kwargs)
        return 1

    def enable_radio_status(self, mode, interface='wifi2', **kwargs):
        """
        - This keyword will disable the radio status button on the page
                manage - device - configuration - interface - wiffi2

        - Keyword Usage:
        - ``enable_radio_status  ON     interface=wifi2      ''

        :param  mode: ON or OFF
        :param  interface: either inface wifi0, wifi1, wifi2

        """
        self.utils.print_info("Enable the radio status ON")

        try:
            if interface == 'wifi2':
                if mode == 'OFF':
                    self.utils.print_info("Click on the radio status button " + mode)
                    self.auto_actions.click_reference(self.get_device_override_configure_interface_settings_wifi2_radio_status)
                    self.auto_actions.click_reference(self.get_manage_devices_edit_wireless_interface_save2_button)
        except Exception:
            kwargs['fail_msg'] = "Can not enable the radio status button"
            self.common_validation.fault(**kwargs)
            return -1

        kwargs['pass_msg'] = "Successfully enable radio status"
        self.common_validation.passed(**kwargs)
        return 1

    def disable_radio_status(self, mode, interface='wifi2', **kwargs):

        """
        - This keyword will enable the radio status button on the page
                manage - device - configuration - interface - wiffi2

        - Keyword Usage:
        - ``enable_radio_status  ON     interface=wifi2      ''

        :param  mode: ON or OFF
        :param  interface: either interface wifi0, wifi1, wifi2

        """
        self.utils.print_info("Disable the radio status OFF")

        try:
            if interface == 'wifi2':
                if mode == 'ON':
                    self.utils.print_info("Click on the radio status button " + mode)
                    self.auto_actions.click_reference(self.get_device_override_configure_interface_settings_wifi2_radio_status)
                    self.auto_actions.click_reference(self.get_manage_devices_edit_wireless_interface_save2_button)
        except Exception:
            kwargs['fail_msg'] = "Not able not enable the radio status button"
            self.common_validation.fault(**kwargs)
            return -1

        kwargs['pass_msg'] = "Successfully disable radio status"
        self.common_validation.passed(**kwargs)
        return 1

    def make_interface_channels_included_excluded(self, channels, mode='default', interface='wifi2', **kwargs):
        """
        - The keyword excludes or includes the channels
                Managed - device - configuration - interface setting - wireless - wifi2

        - Keyword Usage:
        - ``make_interface_channels_included_excluded  [7  23   35]  mode=included  interface=wifi1     ''

        :param  channels  : list of valid channels
        :param  mode      : excluded or included
        :param  interface : either wireless wifi2, wifi1, or wifi0 page

        :return  1 or -1

        """

        self.enabe_override_channel_exclusion_setting_in_radio_profile(interface=interface)
        try:
            locator = None
            for channel in channels:
                self.utils.print_info(" Channel is  " + str(channel))
                if interface == 'wifi2':
                    locator = self.get_devices_override_channel_exclusion_setting_wifi2(str(channel))
                elif interface == 'wifi1':
                    locator = self.get_devices_override_channel_exclusion_setting_wifi1(str(channel))
                elif interface == 'wifi0':
                    locator = self.get_devices_override_channel_exclusion_setting_wifi0(str(channel))

                element = self.web.get_element(locator)
                enabled_text = element.get_attribute("class")
                self.utils.print_info(" Attribute Text: " + str(enabled_text))

                if mode == 'excluded':
                    if enabled_text.find("excluded") == -1:
                        self.utils.print_info(" Click on the channel " + str(channel))
                        CloudDriver().cloud_driver.execute_script("arguments[0].click();", element)
                elif mode == 'included':
                    if enabled_text.find("included") == -1:
                        self.utils.print_info(" Click on the channel " + str(channel))
                        CloudDriver().cloud_driver.execute_script("arguments[0].click();", element)

        except Exception:
            kwargs['fail_msg'] = "Not able to click on the channel"
            self.common_validation.fault(**kwargs)
            return -1

        self.utils.print_info(" Click on the Save Interface Setting ")
        self.get_manage_devices_edit_wireless_interface_save2_button().click()

        kwargs['pass_msg'] = "Successfully make interface channels included excluded"
        self.common_validation.passed(**kwargs)
        return 1

    def check_interface_channel_width_and_channels(self, channels, mode='included', channel_width='default',
                                                   interface='wifi2'):
        """
        - The Keyword validates any valid channel on the wireless page either excluded, included, disable, enabled mode

        - Keyword Usage:
        - ``check_channel_width_and_channels  [7 12 4 5]  mode=included  channel_width=80``

        :param channels: list of valid channels
        :param mode    : excluded, included, enabled, or disabled mode
        :param channel_width:  channel width either 80, 20, 30, 40, 160 HMz
        :param interface: either wirless wifi0, wifi1, or wifi2 page
        :return: 1  or -1
        """

        self.utils.print_info(" Validate the channel width and channels ")

        element = None
        if interface in ['wifi2', 'WIFI2']:
            if channel_width == '80':
                element = self.get_interface_settings_wifi2_80MHz_channel()
            elif channel_width == '160':
                element = self.get_interface_settings_wifi2_160MHz_channel()
            elif channel_width == '40':
                element = self.get_interface_settings_wifi2_40MHz_channel()
            elif channel_width == '20':
                element = self.get_interface_settings_wifi2_20MHz_channel()

        elif interface in ['wifi1', 'WIFI1']:
            if channel_width == '80':
                element = self.get_interface_settings_wifi1_80MHz_channel()
            elif channel_width == '40':
                element = self.get_interface_settings_wifi1_40MHz_channel()
            elif channel_width == '20':
                element = self.get_interface_settings_wifi1_20MHz_channel()

        elif interface in ['wifi0', 'WIFI0']:
            if channel_width == '20':
                element = self.get_interface_settings_wifi0_20MHz_channel()

        if channel_width != 'default':
            if element == None:
                self.utils.print_info(" Channel Width 's element is not found ")
                return -1

            enabled_text = element.get_attribute("class")
            self.utils.print_info(" Attribute Text: " + str(enabled_text))

            if mode == 'enabled':
                if enabled_text.find("disabled") != -1:
                    self.utils.print_info(" Channel with is not by default: ", channel_width)
                    return -1

        for channel in channels:
            self.utils.print_info("Verify the channel " + str(channel))

            locator = None
            if interface in ['wifi2', 'WIFI2']:
                locator = self.get_devices_override_channel_exclusion_setting_wifi2(str(channel))

            elif interface in ['wifi1', 'WIFI1']:
                locator = self.get_devices_override_channel_exclusion_setting_wifi1(str(channel))

            elif interface in ['wifi0', 'WIFI0']:
                locator = self.get_devices_override_channel_exclusion_setting_wifi0(str(channel))

            element = self.web.get_element(locator)
            if element == None:
                self.utils.print_info(" channel element does not exist: ", channel)
                return -1

            enabled_text = element.get_attribute("class")
            self.utils.print_info(" Attribute Text: " + str(enabled_text))

            if mode == 'enabled':
                if enabled_text.find("enabled") == -1:
                    self.utils.print_info(" channel is not enabled: ", channel)
                    return -1
            elif mode == 'disabled':
                if enabled_text.find("disabled") == -1:
                    self.utils.print_info(" channel is not disabled: ", channel)
                    return -1
            elif mode == 'included':
                if enabled_text.find("included") == -1:
                    self.utils.print_info(" channel is not included: ", channel)
                    return -1
            elif mode == 'excluded':
                if enabled_text.find("excluded") == -1:
                    self.utils.print_info(" channel is not excluded: ", channel)
                    return -1

        return 1

    def configure_custom_radio_profile(self, profile_name='default', interface='wifi2', **kwargs):
        """
        - The keyword selects a custom radio profile from the radio profile drop down list either on page wifi2, wifi1, wifi0
            flow: Managed - device - configuration - interface setting - wireless - either (wifi1, wifi2, wifi0)

        - Keyword Usage:
        - ``configure_custom_radio_profile   radio_profile_name=${profile_name}   interface=wifi2'   ''

        :param  profile_name: profile name from the radio profile drop down list
        :param  interface: either wireless wifi0, wifi1, or wifi2 page

        :return: 1

        """

        element = None
        self.utils.print_info(" Configure a radio profile from the radio profile drop down list " + str(profile_name))
        if interface in ['wifi2', 'WIFI2']:
            self.auto_actions.click_reference(self.get_default_wireless_wifi2_radio_profile_drop_down)
            locator = self.get_select_wireless_wifi2_radio_profile(str(profile_name))
            self.auto_actions.click(self.web.get_element(locator))
            element = self.get_default_wireless_wifi2_radio_profile_drop_down()
            # CloudDriver().cloud_driver.execute_script("arguments[0].click();", element)

        elif interface in ['wifi1', 'WIFI1']:
            self.auto_actions.click_reference(self.get_default_wireless_wifi1_radio_profile_drop_down)
            locator = self.get_select_wireless_wifi1_radio_profile(str(profile_name))
            self.auto_actions.click(self.web.get_element(locator))
            element = self.get_default_wireless_wifi1_radio_profile_drop_down()

        elif interface in ['wifi0', 'WIFI0']:
            self.auto_actions.click_reference(self.get_default_wireless_wifi0_radio_profile_drop_down)
            locator = self.get_select_wireless_wifi0_radio_profile(str(profile_name))
            self.auto_actions.click(self.web.get_element(locator))
            element = self.get_default_wireless_wifi0_radio_profile_drop_down()

        if self.get_dialog_box_selected_radio_profile_yes_button() != None:
            self.get_dialog_box_selected_radio_profile_yes_button().click()
            self.auto_actions.click_reference(self.get_manage_devices_edit_wireless_interface_save2_button)

        if element.text != profile_name:
            kwargs['fail_msg'] = f"Radio profile does not match after selecting the profile name {str(element.text)}"
            self.common_validation.failed(**kwargs)
            return -1

        kwargs['pass_msg'] = "Successfully configure custom radio profile"
        self.common_validation.passed(**kwargs)
        return 1

    def _check_wifi_client_access_status(self, interface='wifi2'):
        """
        - Check the current status of client access checkbox of the wireless

        :return: WiFi0 Radio status ie ON or OFF
        """

        if interface == 'wifi2':
            if self.get_wireless_wifi1_radio_usage_client_access_checkbox().is_selected():
                return 'ON'
            else:
                return 'OFF'
        elif interface == 'wifi1':
            if self.get_wireless_wifi1_radio_usage_client_access_checkbox().is_selected():
                return 'ON'
            else:
                return 'OFF'
        elif interface == 'wifi0':
            if self.get_wireless_wifi0_radio_usage_client_access_checkbox().is_selected():
                return 'ON'
            else:
                return 'OFF'

    def _check_wifi_usage_blackhaul_mesh_link_status(self, interface='wifi2'):
        """
        - Check the current status of usage blackhaul mesh link checkbox of the wireless

        :return: WiFi0 Radio status ie ON or OFF
        """

        if interface == 'wifi2':
            if self.get_wireless_wifi2_radio_usage_blackhaul_mesh_link_checkbox().is_selected():
                return 'ON'
            else:
                return 'OFF'
        elif interface == 'wifi1':
            if self.get_wireless_wifi1_radio_usage_blackhaul_mesh_link_checkbox().is_selected():
                return 'ON'
            else:
                return 'OFF'
        elif interface == 'wifi0':
            if self.get_wireless_wifi0_radio_usage_blackhaul_mesh_link_checkbox().is_selected():
                return 'ON'
            else:
                return 'OFF'

    def _check_override_channel_exclusion_setting_radio_profile_status(self, interface='wifi2'):
        """
        - Check the current status of usage blackhaul mesh link checkbox of the wireless

        :return: WiFi0 Radio status ie ON or OFF
        """

        if interface == 'wifi2':
            if self.get_wireless_wifi2_override_channel_exclusion_setting_radio_profile_checkbox().is_selected():
                return 'ON'
            else:
                return 'OFF'
        elif interface == 'wifi1':
            if self.get_wireless_wifi1_override_channel_exclusion_setting_radio_profile_checkbox().is_selected():
                return 'ON'
            else:
                return 'OFF'
        elif interface == 'wifi0':
            if self.get_wireless_wifi0_override_channel_exclusion_setting_radio_profile_checkbox().is_selected():
                return 'ON'
            else:
                return 'OFF'

    def enabe_override_channel_exclusion_setting_in_radio_profile(self, interface='default', **kwargs):

        """
        - Enable the override the channel exclusion setting in radio profile

        :param  interface : either wireless wifi0, wifi1, wifi2 page
        :return: 1 or -1
        """

        self.utils.print_info(" INTERFACE " + str(interface))
        self.utils.print_info(" Click on the override channel exclusion setting radio")
        if interface in ['wifi2', 'WIFI2']:
            element = self.get_wireless_wifi2_override_channel_exclusion_setting_radio_profile_checkbox()
            if not element.is_selected():
                CloudDriver().cloud_driver.execute_script("arguments[0].click();", element)

        elif interface in ['wifi1', 'WIFI1']:
            element = self.get_wireless_wifi1_override_channel_exclusion_setting_radio_profile_checkbox()
            if not element.is_selected():
                CloudDriver().cloud_driver.execute_script("arguments[0].click();", element)
        elif interface in ['wifi0', 'WIFI0']:
            element = self.get_wireless_wifi0_override_channel_exclusion_setting_radio_profile_checkbox()
            if not element.is_selected():
                CloudDriver().cloud_driver.execute_script("arguments[0].click();", element)
        kwargs['pass_msg'] = "Successfully enable override channel"
        self.common_validation.passed(**kwargs)
        return 1

    def _go_to_wired_interface_settings_page(self):
        """
        - Go to configure --> interface settings --> wired Interfaces
        :return:
        """
        self.utils.print_info("Click on wired interfaces toggle button")
        sleep(5)
        if self.get_wired_interface_toggle():
            self.auto_actions.click_reference(self.get_wired_interface_toggle)
            self.utils.print_info("able to click toggle")

    def device_override_create_imago_tag_profile(self, device_serial='', profile_name='', server='', channel='',
                                                 fcc_mode=True, server_port='default', **kwargs):
        """
        - This Keyword will Crete ImagoTag Profile at device override configuration.
        - Flow: Manage-->Devices-->select Device with serial number->Edit-->configuration-->interface settings
                -->Wired Settings --> Imagotag

        - Keyword Usage:
        - ``Device Override Create Imago Tag Profile  device_serial=${DEVICE_SERIAL}  profile_name=${PROFILE}
         server=${SERVER}  channel=${CHANNEL}``

        - ``Device Override Create Imago Tag Profile  device_serial=${DEVICE_SERIAL}  profile_name=${PROFILE}
         server=${SERVER}  channel=${CHANNEL}  server_port=${PORT}``


        :param device_serial: Device serial Number
        :param profile_name: Imago Tag Profile name
        :param channel: Channel Number
        :param server: Server detail
        :param fcc_mode: By default fcc_mode is enabled.To Disable mention this flag as False
        :param server_port: Server Port Details
        :return: 1 if ImagTag Profile Created Successfully else -1
        """

        self.navigator.navigate_to_devices()
        self.device_common.edit_device(device_serial)
        sleep(5)

        self.utils.print_info("Click on interface settings tab")
        self.auto_actions.click_reference(self.get_interface_settings_tab_single_device)
        self.screen.save_screen_shot()

        self._go_to_wired_interface_settings_page()
        self.screen.save_screen_shot()

        self.auto_actions.scroll_down()
        sleep(2)

        self.utils.print_info("Click on ImagoTag Radio button")
        if not self.get_imago_tag_add_profile_add_button().is_displayed():
            self.auto_actions.click_reference(self.get_imago_tag_radio_button)
            sleep(2)

        self.utils.print_info("Click on ImagoTag Profile Add button")
        self.auto_actions.click_reference(self.get_imago_tag_add_profile_add_button)

        self.utils.print_info("Add profile name")
        self.auto_actions.send_keys(self.cobj_web_elements.get_common_object_imago_tag_profile_name_textfield(),
                                    profile_name)

        self.utils.print_info("Add profile Description")
        self.auto_actions.send_keys(self.cobj_web_elements.get_common_object_imago_tag_profile_description_textfield(),
                                    profile_name)
        self.screen.save_screen_shot()

        self.utils.print_info("Enter Server name Textfield")
        self.auto_actions.send_keys(self.cobj_web_elements.get_common_object_imago_tag_profile_server_textfield(),
                                    server)
        self.screen.save_screen_shot()

        self.utils.print_info("clicking Channel drop down Button")
        self.auto_actions.click_reference(self.cobj_web_elements.get_common_object_imago_tag_profile_channel_drop_down_button)
        sleep(2)

        self.utils.print_info(f"Selecting Channel Option : {channel}")
        self.auto_actions.select_drop_down_options(self.cobj_web_elements.
                                                   get_common_object_imago_tag_profile_channel_drop_down_options(),
                                                   channel)
        sleep(2)
        self.screen.save_screen_shot()

        if fcc_mode:
            self.utils.print_info("Click on Enable FCC Mode Checkbox")
            if not self.cobj_web_elements.get_common_object_imago_tag_profile_fcc_mode_checkbox().is_selected():
                self.auto_actions.click_reference(self.cobj_web_elements.get_common_object_imago_tag_profile_fcc_mode_checkbox)
                self.screen.save_screen_shot()
                sleep(2)

        if server_port != 'default':
            self.utils.print_info("Click Advanced Settings Button")
            self.auto_actions.click_reference(self.cobj_web_elements.get_common_object_imago_tag_profile_advanced_settings_tab)
            sleep(2)

            self.utils.print_info("Change server Port Number")
            self.auto_actions.send_keys(
                self.cobj_web_elements.get_common_object_imago_tag_profile_advanced_settings_server_port(), server_port)
            self.screen.save_screen_shot()

        self.utils.print_info("clicking Save Button")
        self.auto_actions.click_reference(self.cobj_web_elements.get_common_object_imago_tag_profile_save_button)
        self.screen.save_screen_shot()
        sleep(5)

        sleep(5)
        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)

        if "Succesfully Updated" in tool_tp_text[-1]:

            self.utils.print_info("Click on interface settings save button")
            self.auto_actions.click_reference(self.get_interface_settings_save_button)

            self.utils.print_info("Close the device360 page dialog window")
            self.get_close_device360_dialog_window().click()
            kwargs['pass_msg'] = "Successfully create imago tag profile"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            self.utils.print_info("Unable to Edit Image Tag Policy Successfully")

            self.utils.print_info("Click on interface settings save button")
            self.auto_actions.click_reference(self.get_interface_settings_save_button)

            self.utils.print_info("Close the device360 page dialog window")
            self.get_close_device360_dialog_window().click()
            kwargs['fail_msg'] = "UnSuccessfully create imago tag profile"
            self.common_validation.failed(**kwargs)
            return -1

    def get_device_config_audit_delta(self, device_mac, **kwargs):
        """
        - This keyword will get the delta cli configuration
        - Assumes That Already in Devices Page
        :param device_mac:   The serial of the device string
        :return:                Returns a list of strings with the commands present in delta cli
        """

        def check_delta_view_button_yellow():
            device_found = 0
            rows_check = self.get_grid_rows()
            if rows_check:
                if device_mac:
                    for row_check in rows_check:
                        if device_mac in row_check.text:
                            device_found = 1
                            if self.get_config_audit_delta_view_button_yellow(row_check):
                                return True
                            else:
                                self.screen.save_screen_shot()
                                return False
                else:
                    kwargs['fail_msg'] = f"The mac {str(device_mac)} is invalid."
                    self.common_validation.failed(**kwargs)
            else:
                kwargs['fail_msg'] = "Did not find any rows!"
                self.common_validation.failed(**kwargs)

            if device_found != 1:
                kwargs['fail_msg'] = f"Did not find any device with mac address: {device_mac}"
                self.common_validation.failed(**kwargs)

        self.utils.wait_till(check_delta_view_button_yellow, timeout=120, delay=15, is_logging_enabled=True)

        rows = self.get_grid_rows()
        self.utils.print_info("Selecting Device with mac address: ", device_mac)
        for row in rows:
            if device_mac in row.text:
                self.utils.print_debug(f"Found device with mac: {device_mac}")
                self.utils.print_info("Attempting to click audit delta view button...")

                def local_delta_view_button():
                    return self.get_config_audit_delta_view_button_yellow(row)

                audit_delta_view_button = self.get_config_audit_delta_view_button_yellow(row)
                if audit_delta_view_button:
                    self.utils.print_info("Found the delta view button!")
                    self.utils.print_info("Clicking the delta view button...")
                    self.auto_actions.click_reference(local_delta_view_button)
                else:
                    kwargs['fail_msg'] = "Did not find the delta view button"
                    self.common_validation.failed(**kwargs)
                    return -1
                self.utils.print_info("Locating audit content...")

                def check_audit_config_content():
                    audit_content = self.get_config_audit_content()
                    if audit_content:
                        if bool(self.get_config_audit_content().text):
                            self.utils.print_info("audit content is text")
                        else:
                            self.utils.print_info("audit content is empty ")
                        return True
                    else:
                        return False
                self.utils.wait_till(check_audit_config_content, is_logging_enabled=True, timeout=60, delay=10)
                self.utils.print_info(f"Audit content: {self.get_config_audit_content().text}")
                self.utils.print_info("Attempting to locate delta view...")

                delta_view = self.get_device_config_audit_delta_view()
                if delta_view:
                    self.utils.print_info("Clicking on Device Config Audit Delta View...")
                    self.auto_actions.click_reference(self.get_device_config_audit_delta_view)
                else:
                    kwargs['fail_msg'] = "Did not find the delta view..."
                    self.common_validation.failed(**kwargs)
                    return -1
                self.utils.print_info("Attempting to locate the delta config content...")
                if self.get_device_config_audit_delta_view_content():
                    self.utils.print_info("Get the Config content from Device Config Audit Delta View")

                    def check_device_config_audit_delta_view_content():
                        self.screen.save_screen_shot()
                        return bool(self.get_device_config_audit_delta_view_content().text)

                    self.utils.wait_till(check_device_config_audit_delta_view_content, is_logging_enabled=True,
                                         timeout=160, delay=10)
                    delta_configs = self.get_device_config_audit_delta_view_content().text
                else:
                    kwargs['fail_msg'] = "Did not manage to locate the content..."
                    self.common_validation.failed(**kwargs)
                    return -1

                close_audit_view_button = self.get_device_config_audit_view_close_button()
                self.utils.print_info("Attempting to locate the close button...")
                if close_audit_view_button:
                    self.auto_actions.click_reference(self.get_device_config_audit_view_close_button)
                else:
                    self.utils.print_info("Did not find the close button.")
                    kwargs['fail_msg'] = "Did not find the close button."
                    self.common_validation.failed(**kwargs)
                    return -1
                if delta_configs:
                    kwargs['pass_msg'] = "Successfully collected Delta CLI configs"
                    self.utils.print_info("Delta Configs : ", delta_configs)
                    self.common_validation.passed(**kwargs)
                    return delta_configs
                else:
                    kwargs['fail_msg'] = "Did not manage to get any configurations"
                    self.common_validation.failed(**kwargs)
                    return -1

    def get_device_config_audit_delta_complete(self, ap_serial, config_type, **kwargs):
        """
        - This keyword will get the audit, delta or complete cli configuration
        :param ap_serial:   The serial of the device
        :param config_type: audit, or delta, or complete
        :return: Returns a list of strings with the commands present in audit, delta or complete clis
        """
        if not self.navigator.get_devices_page():
            self.utils.print_info("Not in Devices page, now to navigate this page...")
            if self.navigator.navigate_to_devices() == 1:
                self.utils.print_info("To navigate the Devices page successfully...")
            else:
                self.utils.print_info("Failed to navigate the Devices page ...")
                return -1

        rows = self.get_grid_rows()
        if rows:
            if ap_serial:
                self.utils.print_info(f"Selecting Device with AP serial: {ap_serial}")
                device_found = 0
                for row in rows:
                    if ap_serial in row.text:
                        device_found = 1
                        self.utils.print_debug(f"Found device with serial: {ap_serial}")
                        self.utils.print_info("Attempting to click Configuration Audit view button...")
                        config_audit_view_button = self.get_devices_config_audit_view_button(row)
                        if config_audit_view_button:
                            self.utils.print_info("Found the config audit view button!")
                            self.utils.print_info("Clicking the config audit view button...")
                            self.auto_actions.click(config_audit_view_button)
                        else:
                            kwargs['fail_msg'] = "Did not find the config audit view button"
                            self.common_validation.failed(**kwargs)
                            return -1
                        if config_type.upper() == "COMPLETE":
                            complete_view = self.get_device_config_audit_complete_view()
                            self.utils.print_info("Attempting to locate complete view...")
                            if complete_view:
                                self.utils.print_info("Clicking on Device Config Audit Complete View...")
                                self.auto_actions.click_reference(self.get_device_config_audit_complete_view)
                            else:
                                kwargs['fail_msg'] = "Did not find the complete view..."
                                self.common_validation.failed(**kwargs)
                                return -1
                            self.utils.print_info("Attempting to locate the complete config content...")
                            if self.get_device_config_audit_complete_view_content():
                                self.utils.print_info("Get the Config content from Device Config Audit Complete View")

                                def check_device_config_audit_complete_view_content():
                                    return bool(self.get_device_config_audit_complete_view_content().text)

                                self.utils.wait_till(check_device_config_audit_complete_view_content, is_logging_enabled=True)
                                get_configs_result = self.get_device_config_audit_complete_view_content().text
                            else:
                                kwargs['fail_msg'] = "Did not manage to locate the content."
                                self.common_validation.failed(**kwargs)
                                return -1
                        elif config_type.upper() == "DELTA":
                            delta_view = self.get_device_config_audit_delta_view()
                            self.utils.print_info("Attempting to locate delta view...")
                            if delta_view:
                                self.utils.print_info("Clicking on Device Config Audit Delta View...")
                                self.auto_actions.click_reference(self.get_device_config_audit_delta_view)
                            else:
                                kwargs['fail_msg'] = "Did not find the delta view."
                                self.common_validation.failed(**kwargs)
                                return -1
                            self.utils.print_info("Attempting to locate the delta config content...")
                            if self.get_device_config_audit_delta_view_content():
                                self.utils.print_info("Get the Config content from Device Config Audit Delta View")

                                def check_device_config_audit_delta_view_content():
                                    return bool(self.get_device_config_audit_delta_view_content().text)

                                self.utils.wait_till(check_device_config_audit_delta_view_content, is_logging_enabled=True)
                                get_configs_result = self.get_device_config_audit_delta_view_content().text
                            else:
                                kwargs['fail_msg'] = "Did not manage to locate the content."
                                self.common_validation.failed(**kwargs)
                                return -1
                        elif config_type.upper() == "AUDIT":
                            audit_view = self.get_device_config_audit_audit_view()
                            self.utils.print_info("Attempting to locate audit view...")
                            if audit_view:
                                self.utils.print_info("Clicking on Device Config Audit audit View...")
                                self.auto_actions.click_reference(self.get_device_config_audit_audit_view)
                            else:
                                kwargs['fail_msg'] = "Did not find the audit view."
                                self.common_validation.failed(**kwargs)
                                return -1
                            self.utils.print_info("Attempting to locate the audit config content...")
                            if self.get_device_config_audit_audit_view_content():
                                self.utils.print_info("Get the Config content from Device Config Audit audit View")

                                def check_device_config_audit_audit_view_content():
                                    return bool(self.get_device_config_audit_audit_view_content().text)

                                self.utils.wait_till(check_device_config_audit_audit_view_content, is_logging_enabled=True)
                                get_configs_result = self.get_device_config_audit_audit_view_content().text
                            else:
                                kwargs['fail_msg'] = "Did not manage to locate the content."
                                self.common_validation.failed(**kwargs)
                                return -1

                        close_audit_view_button = self.get_device_config_audit_view_close_button()
                        self.utils.print_info("Attempting to locate the close button...")
                        if close_audit_view_button:
                            self.auto_actions.click_reference(self.get_device_config_audit_view_close_button)
                        else:
                            self.utils.print_info("Did not find the close button.")
                            kwargs['fail_msg'] = "Did not find the close button."
                            self.common_validation.failed(**kwargs)
                            return -1
                        if get_configs_result:
                            kwargs['pass_msg'] = f"Successfully collected {config_type} CLI configs. " \
                                                 f"{config_type} Configs : {get_configs_result}"
                            self.common_validation.passed(**kwargs)
                            return get_configs_result
                        else:
                            kwargs['fail_msg'] = "Did not manage to get any configurations"
                            self.common_validation.failed(**kwargs)
                            return -1
                if device_found == 0:
                    kwargs['fail_msg'] = f"Did not find any device with AP serial: {ap_serial}"
                    self.common_validation.failed(**kwargs)
                    return -1
        else:
            kwargs['fail_msg'] = "Did not find any rows!"
            self.common_validation.failed(**kwargs)
            return -1

    def clear_audit_commands(self, audit):
        """
            - This keyword is used to "clean" the output from audit-delta of the commands that sometimes appear at the
              beginning of the output

        :param audit: the output from audit-delta
        :return: audit_clean: a list with the output from audit-delta without the commands that sometimes appear at
            the beginning of the output
        """
        audit_list = list(audit.split('\n'))
        audit_clean = []
        print(audit_list)
        for i in audit_list:
            if not i.startswith('#'):
                audit_clean.append(i)
            elif 'save configuration y' in audit_list:
                audit_list.remove('save configuration y')
        return audit_clean

    def configure_device_function(self, ap_serial, device_function='AP', **kwargs):
        """
        - This keyword will configure device function as AP or Router
        :param ap_serial:   The serial of the device
        :param device_function: AP or ApAsRouter, default is AP
        :return: success 1 else -1
        """
        if not self.navigator.get_devices_page():
            self.utils.print_info("Not in Devices page, now to navigate this page...")
            if self.navigator.navigate_to_devices() == 1:
                self.utils.print_info("To navigate the Devices page successfully...")
            else:
                self.utils.print_info("Failed to navigate the Devices page ...")
                return -1
        self.utils.print_info(f"Select AP serial {ap_serial} ...")
        ap_selected = False
        while not ap_selected:
            try_cnt = 0
            if self.devices.select_device(device_serial=ap_serial, ignore_failure=True) == 1:
                self.utils.print_info(f"Edit AP serial {ap_serial} to go AP page...")
                self.auto_actions.click_reference(self.get_edit_button)
                device_360_page = self.get_device_360_page()
                if not device_360_page:
                    wait_times = 0
                    while wait_times <= 30:
                        self.utils.print_info("The device 360 page is still not loaded, sleep 2 seconds")
                        sleep(2)
                        wait_times += 1
                        if device_360_page:
                            self.utils.print_info("Device 360 page is already loaded, move to next step")
                            break
                        else:
                            continue
                self.utils.print_info("Click Configure tab...")
                self.auto_actions.click_reference(self.get_devices_edit_config_button)
                self.utils.print_info("Click Device Configuration...")
                self.auto_actions.click_reference(self.get_device_configuration_tab)
                device_config_node_not_load = True
                while device_config_node_not_load:
                    if not self.get_device_configuration_node():
                        self.utils.print_info("Device config node page is still loading ...")
                        sleep(2)
                    else:
                        device_config_node_not_load = False
                        self.utils.print_info("Device config node page is loaded successfully ...")
                        sleep(6)
                if self.get_devices_device_config_device_function_set_ap():
                    self.utils.print_info("Click Device Function dropdown button...")
                    self.auto_actions.click_reference(self.get_devices_device_config_device_function_set_ap)
                    device_function_options = self.get_devices_device_config_device_function()
                    for opt in device_function_options:
                        self.utils.print_info(f"Option is {opt}")
                        if device_function.upper() == opt.text.upper():
                            self.utils.print_info(f"Select {device_function} as Device Function")
                            self.auto_actions.click(opt)
                            break
                elif self.get_devices_device_config_device_function_set_router:
                    self.utils.print_info("Device function already is set as router mode...")
                    pass
                else:
                    kwargs['fail_msg'] = "No valid device function found!!!"
                    self.common_validation.failed(**kwargs)
                    return -1
                sleep(3)
                self.utils.print_info("Click Save Device Configuration button...")
                self.auto_actions.click_reference(self.get_devices_device_config_page_save_button)
                sleep(3)
                self.utils.print_info("Close device config windows...")
                self.auto_actions.click_reference(self.get_close_dialog)
                return 1
            else:
                self.utils.wait_till(self.cloud_driver.refresh_page, timeout=60, delay=1, is_logging_enabled=True)
                self.utils.print_info("Refresh page and try to select AP again")
                try_cnt += 1
                if try_cnt == 10:
                    kwargs['fail_msg'] = f"Max {try_cnt} to select device is reached"
                    self.common_validation.failed(**kwargs)
                    return -1

    def verify_delta_cli_commands(self, dut, commands, retries=5, step=15, **kwargs):
        """Method that verifies that given CLI commands appear in the Delta CLI window of a device.

        Args:
            dut (dict): the dut (e.g. tb.dut1)
            commands (list): a list of CLI commands
            step (int): seconds to sleep between retries
            retries (int, optional): the number of retries. Defaults to 5.

        Returns:
            int: 1 if the function call has succeeded else -1
        """
        self.utils.wait_till(timeout=10)
        self.devices._goto_devices()
        self.utils.wait_till(timeout=10)
        self.devices.refresh_devices_page()
        self.utils.wait_till(timeout=5)

        for _ in range(retries):
            try:
                self.devices.refresh_devices_page()
                self.utils.wait_till(timeout=5)
                self.devices.select_device(device_mac=dut.mac)

                btn, _ = self.utils.wait_till(
                    func=self.get_device_config_audit_view,
                    delay=5,
                    exp_func_resp=True,
                    silent_failure=True
                )

                assert btn, "Failed to get the device_config_audit_view button"
                self.utils.print_info("Successfully got the device_config_audit_view button")

                res, _ = self.utils.wait_till(
                    func=lambda: self.auto_actions.click_reference(self.get_device_config_audit_view),
                    delay=4,
                    exp_func_resp=True,
                    silent_failure=True
                )

                assert res == 1, "Failed to click the device_config_audit_view button"
                self.utils.print_info("Successfully clicked the device_config_audit_view button")

                delta_view, _ = self.utils.wait_till(
                    func=self.get_device_config_audit_delta_view,
                    delay=5,
                    exp_func_resp=True,
                    silent_failure=True
                )

                assert delta_view, "Failed to get the delta_view button"
                self.utils.print_info("Successfully got the delta_view button")

                res, _ = self.utils.wait_till(
                    func=lambda: self.auto_actions.click_reference(self.get_device_config_audit_delta_view),
                    timeout=60,
                    delay=20,
                    exp_func_resp=True,
                    silent_failure=True
                )

                assert res == 1, "Failed to click the delta_view button"
                self.utils.print_info("Successfully clicked the delta_view button")

                self.utils.wait_till(timeout=30)

                delta_configs, _ = self.utils.wait_till(
                    func=self.get_device_config_audit_delta_view_content,
                    timeout=60,
                    exp_func_resp=True,
                    delay=5,
                    silent_failure=True
                )

                assert delta_configs, "Failed to get the delta_configs element"
                self.utils.print_info("Successfully got the delta_configs element")

                delta_configs = delta_configs.text

                for command in commands:

                    assert re.search(command, delta_configs), f"Did not find this command in delta CLI: {command}, " \
                                                              f"found {delta_configs} instead"
                    self.utils.print_info(f"Successfully found this command in delta CLI: {command}")

            except Exception as exc:
                self.utils.print_info(repr(exc))
                self.utils.wait_till(timeout=step)

            else:
                kwargs["pass_msg"] = f"Successfully found these commands in the delta cli: {commands}"
                self.common_validation.passed(**kwargs)
                return 1

            finally:

                try:
                    close_btn, _ = self.utils.wait_till(
                        func=self.get_device_config_audit_view_close_button,
                        exp_func_resp=True,
                        silent_failure=True,
                        delay=5
                    )

                    self.utils.wait_till(
                        func=lambda:
                        self.auto_actions.click_reference(self.get_device_config_audit_view_close_button) == 1,
                        exp_func_resp=True,
                        delay=4,
                        silent_failure=True
                    )
                except Exception as e:
                    self.utils.print_info(repr(e))

                self.devices.select_device(device_mac=dut.mac)
        else:
            kwargs["fail_msg"] = f"Failed to verify these commands in the delta cli after {retries} retries: {commands}"
            self.common_validation.failed(**kwargs)
            return -1
