from time import sleep
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from xiqse.flows.common.XIQSE_CommonOperationsPanel import XIQSE_CommonOperationsPanel
from xiqse.flows.common.XIQSE_CommonTable import XIQSE_CommonTable
from xiqse.flows.network.devices.XIQSE_NetworkDevices import XIQSE_NetworkDevices
from xiqse.flows.network.devices.devices.XIQSE_NetworkDevicesDevicesAddDevice import XIQSE_NetworkDevicesDevicesAddDevice
from xiqse.flows.network.common.XIQSE_NetworkCommonConfigureDevice import XIQSE_NetworkCommonConfigureDevice
from xiqse.flows.network.common.configure_device.XIQSE_NetworkCommonConfigureDeviceDevice import XIQSE_NetworkCommonConfigureDeviceDevice
from xiqse.flows.network.common.configure_device.XIQSE_NetworkCommonConfigureDeviceAnnotations import XIQSE_NetworkCommonConfigureDeviceAnnotations
from xiqse.flows.network.devices.devices.XIQSE_NetworkDevicesDevicesDeleteDevice import XIQSE_NetworkDevicesDevicesDeleteDevice
from xiqse.flows.network.devices.devices.XIQSE_NetworkDevicesDevicesSetProfile import XIQSE_NetworkDevicesDevicesSetProfile
from xiqse.elements.common.CommonViewWebElements import CommonViewWebElements
from xiqse.elements.network.devices.devices.NetworkDevicesDevicesWebElements import NetworkDevicesDevicesWebElements
from xiqse.flows.network.devices.devices.XIQSE_NetworkDevicesDevicesBackupConfiguration import XIQSE_NetworkDevicesDevicesBackupConfiguration
from xiqse.flows.network.devices.devices.XIQSE_NetworkDevicesDevicesRestoreConfiguration import XIQSE_NetworkDevicesDevicesRestoreConfiguration
from xiqse.flows.network.devices.devices.XIQSE_NetworkDevicesDevicesRestartDevice import XIQSE_NetworkDevicesDevicesRestartDevice
from selenium.common.exceptions import StaleElementReferenceException
import re


class XIQSE_NetworkDevicesDevices(NetworkDevicesDevicesWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.view_el = CommonViewWebElements()
        self.xiqse_table = XIQSE_CommonTable()
        self.devices_tab = XIQSE_NetworkDevices()
        self.add_device_dlg = XIQSE_NetworkDevicesDevicesAddDevice()
        self.delete_device_dlg = XIQSE_NetworkDevicesDevicesDeleteDevice()
        self.profile_dlg = XIQSE_NetworkDevicesDevicesSetProfile()
        self.config_dlg = XIQSE_NetworkCommonConfigureDevice()
        self.config_dlg_device = XIQSE_NetworkCommonConfigureDeviceDevice()
        self.config_dlg_annotations = XIQSE_NetworkCommonConfigureDeviceAnnotations()
        self.backup_config_dlg = XIQSE_NetworkDevicesDevicesBackupConfiguration()
        self.restore_config_dlg = XIQSE_NetworkDevicesDevicesRestoreConfiguration()
        self.operations_panel = XIQSE_CommonOperationsPanel()
        self.restart_device = XIQSE_NetworkDevicesDevicesRestartDevice()

    def xiqse_select_device(self, device_ip):
        """
         - This keyword selects the specified device.
         - It is assumed the user is already on the Network> Devices> Devices tab.
         - Keyword Usage
          - ``XIQSE Select Device``

        :param device_ip: IP address of the device tp select
        :return: 1 if action was successful, else -1
        """

        ret_val = -1
        self.utils.print_info(f"Selecting Device with IP {device_ip}")

        stale_retry = 1
        while stale_retry <= 10:
            try:
                rows = self.get_table_rows()
                if rows:
                    for row in rows:
                        if device_ip in row.text:
                            self.utils.print_debug(
                                f"Found device {device_ip} in row {self.xiqse_table.format_table_row(row.text)}")
                            row_selected = row.get_attribute("aria-selected")
                            if row_selected and row_selected == "true":
                                self.utils.print_info(f"Row for device {device_ip} is already selected")
                            else:
                                self.utils.print_info(f"Selecting device {device_ip}")
                                self.auto_actions.click(row)
                            ret_val = 1
                            break
                    break
                else:
                    self.utils.print_info("Did not find any rows in table")
                    break
            except StaleElementReferenceException:
                self.utils.print_info(f"Handling StaleElementReferenceException - loop {stale_retry}")
                stale_retry = stale_retry + 1

        if ret_val == -1:
            self.utils.print_info(f"Unable to select device {device_ip}")
            self.screen.save_screen_shot()
        return ret_val

    def xiqse_add_device(self, ip_addr, profile="public_v1_Profile", nickname="", status_only="False", add_actions="True"):
        """
         - This keyword adds a device using the Add Device toolbar button on the Network> Devices> Devices tab.
         - It is assumed the user is already on the Network> Devices> Devices tab.
         - Keyword Usage
          - ``XIQSE Add Device  ${IP}  ${PROFILE}  ${NICKNAME}  True``
          - ``XIQSE Add Device  ${IP}  ${PROFILE}  ${NICKNAME}``
          - ``XIQSE Add Device  ${IP}  ${PROFILE}``
          - ``XIQSE Add Device  ${IP}  ${PROFILE}  status_only=True``
          - ``XIQSE Add Device  ${IP}``
          - ``XIQSE Add Device  ${IP}  nickname=TestDevice``
          - ``XIQSE Add Device  ${IP}  status_only=True``
          - ``XIQSE Add Device  ${IP}  add_actions=False``

        :param ip_addr:     IP address of the device to add - required
        :param profile:     profile to use for the device
        :param nickname:    nickname to use for the device
        :param status_only: indicates if the device should be created with Poll Status Only selected (True/False)
        :param add_actions: indicates if the Run Site's Add Actions option should be enabled (True/False)
        :return: 1 if action was successful, else -1
        """
        ret_val = 1
        add_btn = self.get_add_device_tb_button()
        if add_btn:
            self.utils.print_info("Clicking Add Device toolbar button")
            self.auto_actions.click(add_btn)
            sleep(2)

            # Enter IP Address
            ret_val = self.add_device_dlg.xiqse_add_device_dialog_set_ip(ip_addr)

            # Select Profile
            if ret_val != -1:
                ret_val = self.add_device_dlg.xiqse_add_device_dialog_select_profile(profile)

            # Enter nickname
            if ret_val != -1:
                ret_val = self.add_device_dlg.xiqse_add_device_dialog_set_nickname(nickname)

            # Set "Poll Status Only" option
            if ret_val != -1:
                ret_val = self.add_device_dlg.xiqse_add_device_dialog_set_poll_status_only(status_only)

            # Set "Run Site's Add Action" option
            if ret_val != -1:
                ret_val = self.add_device_dlg.xiqse_add_device_dialog_set_run_site_add_actions(add_actions)

            # Click OK
            if ret_val != -1:
                sleep(2)
                ret_val = self.add_device_dlg.xiqse_add_device_dialog_click_ok()
            else:
                self.utils.print_info("Problems entering information into Add Device dialog")
                self.screen.save_screen_shot()
                self.xiqse_close_add_device_dialog()
        else:
            self.utils.print_info("Unable to find Add Device toolbar button")
            self.screen.save_screen_shot()
            ret_val = -1

        return ret_val

    def xiqse_close_add_device_dialog(self):
        """
         - This keyword closes the Add Device dialog if it is open.
         - Keyword Usage
          - ``XIQSE Close Add Device Dialog``

        :return: 1 if action was successful, else -1
        """
        return self.add_device_dlg.xiqse_add_device_dialog_click_close()

    def xiqse_delete_device(self, device_ip):
        """
         - This keyword deletes the specified device.
         - It is assumed the user is already on the Network> Devices> Devices tab.
         - Keyword Usage
          - ``XIQSE Delete Device    ${DEVICE_IP}``
          - ``XIQSE Delete Device    ${DEVICE_IP}    false``

        :param device_ip: IP address of the device to delete
        :return: 1 if action was successful, else -1
        """
        ret_val = 1

        if self.xiqse_select_device(device_ip) == 1:
            ret_val = self.xiqse_delete_selected_devices()
        else:
            self.utils.print_info(f"Device {device_ip} does not exist / is already deleted")

        return ret_val

    def xiqse_delete_selected_devices(self):
        """
         - This keyword deletes the currently-selected devices.
         - It is assumed the user is already on the Network> Devices> Devices tab and the devices to delete are selected.
         - Keyword Usage
          - ``XIQSE Delete Selected Devices``

        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        menu_btn = self.get_device_menu_tb_button()
        if menu_btn:
            self.utils.print_info("Clicking Device Menu toolbar button")
            self.auto_actions.click(menu_btn)
            sleep(1)

            more_menu = self.get_more_actions_menu_item()
            if more_menu:
                self.utils.print_info("Clicking 'More Actions' menu")
                self.auto_actions.click(more_menu)
                sleep(1)

                delete_menu = self.get_delete_device_menu_item()
                if delete_menu:
                    self.utils.print_info("Clicking 'Delete Device' menu")
                    self.auto_actions.click(delete_menu)
                    sleep(2)

                    # Confirm the deletion of the device
                    ret_val = self.delete_device_dlg.xiqse_confirm_delete_device_click_yes()
                else:
                    self.utils.print_info("Unable to find Delete Device menu")
                    self.screen.save_screen_shot()
            else:
                self.utils.print_info("Unable to find More Actions menu")
                self.screen.save_screen_shot()
        else:
            self.utils.print_info("Unable to find Device Menu toolbar button")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_restart_device(self, device_ip):
        """
         - This keyword restarts the currently-selected device.
         - It is assumed the user is already on the Network> Devices> Devices tab and the device to register is selected.
         - Keyword Usage
          - ``XIQSE Restart Device    ${DEVICE_IP}``

        :param  device_ip:    IP address of the device to restart
        :return: 1 if action was successful, else -1
        """
        ret_val = 1

        if self.xiqse_select_device(device_ip) == 1:
            menu_btn = self.get_device_menu_tb_button()
            if menu_btn:
                self.utils.print_info("Clicking Device Menu toolbar button")
                self.auto_actions.click(menu_btn)
                sleep(1)

                more_menu = self.get_more_actions_menu_item()
                if more_menu:
                    self.utils.print_info("Clicking 'More Actions' menu")
                    self.auto_actions.click(more_menu)
                    sleep(1)

                    restart_device_menu = self.get_restart_device_menu_item()
                    if restart_device_menu:
                        self.utils.print_info("Clicking 'Restart Device' menu")
                        self.auto_actions.click(restart_device_menu)
                        sleep(5)
                        return 1
                    else:
                        self.utils.print_info("Unable to find Restart Device menu")
                        self.screen.save_screen_shot()
                else:
                    self.utils.print_info("Unable to find More Actions menu")
                    self.screen.save_screen_shot()
            else:
                self.utils.print_info("Unable to find Device Menu toolbar button")
                self.screen.save_screen_shot()
        else:
            self.utils.print_info("Unable to find select device")

        return ret_val

    def xiqse_device_set_profile(self, device_ip, profile_name):
        """
         - This keyword sets the profile for the specified device.
         - It is assumed the user is already on the Network> Devices> Devices tab.
         - Keyword Usage
          - ``XIQSE Device Set Profile  1.2.3.4  new_profile``

        :param device_ip:    IP address of the device to set the profile on
        :param profile_name: name of the profile to set on the device
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        if self.xiqse_select_device(device_ip) == 1:
            menu_btn = self.get_device_menu_tb_button()
            if menu_btn:
                self.utils.print_info("Clicking Device Menu toolbar button")
                self.auto_actions.click(menu_btn)
                sleep(1)

                more_menu = self.get_more_actions_menu_item()
                if more_menu:
                    self.utils.print_info("Clicking 'More Actions' menu")
                    self.auto_actions.click(more_menu)
                    sleep(1)

                    profile_menu = self.get_set_device_profile_menu_item()
                    if profile_menu:
                        self.utils.print_info("Clicking 'Set Device Profile...' menu")
                        self.auto_actions.click(profile_menu)
                        sleep(2)

                        # Select the profile
                        ret_val = self.profile_dlg.xiqse_set_profile_dialog_select_profile(profile_name)

                        # If the profile could be selected, click OK;  otherwise, click Cancel
                        if ret_val == 1:
                            # Click OK
                            self.profile_dlg.xiqse_set_profile_dialog_click_ok()
                        else:
                            # Click Cancel
                            self.profile_dlg.xiqse_set_profile_dialog_click_cancel()
                    else:
                        self.utils.print_info("Unable to find 'Set Device Profile...' menu")
                        self.screen.save_screen_shot()
                else:
                    self.utils.print_info("Unable to find More Actions menu")
                    self.screen.save_screen_shot()
            else:
                self.utils.print_info("Unable to find Device Menu toolbar button")
                self.screen.save_screen_shot()
        else:
            self.utils.print_info(f"Device {device_ip} does not exist")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_open_upgrade_firmware_dialog(self, device_ip):
        """
        - This keyword opens the Upgrade Firmware dialog by selecting "Upgrade Firmware..." from the device context menu.
        - It assumes the Network> Devices> Devices view is loaded.
        - Keyword Usage:
         - ``XIQSE Open Upgrade Firmware Dialog    ${DEVICE_IP}``

        :param device_ip:  IP of the device to open the Configure Device dialog for
        :return: 1 if action is successful, else -1
        """
        ret_val = -1

        if self.xiqse_select_device(device_ip) == 1:
            menu_btn = self.get_device_menu_tb_button()
            if menu_btn:
                self.utils.print_info("Clicking Device Menu toolbar button")
                self.auto_actions.click(menu_btn)
                sleep(1)

                upgrade_firmware_menu = self.get_upgrade_firmware_menu_item()
                if upgrade_firmware_menu:
                    self.utils.print_info("Clicking 'Upgrade Firmware...' menu")
                    self.auto_actions.click(upgrade_firmware_menu)
                    sleep(2)
                    ret_val = 1
                else:
                    self.utils.print_info("Unable to find 'Upgrade Firmware...' menu")
                    self.screen.save_screen_shot()
            else:
                self.utils.print_info("Unable to find Device Menu toolbar button")
                self.screen.save_screen_shot()

        return ret_val

    def xiqse_open_configure_device_dialog(self, device_ip):
        """
        - This keyword opens the Configure Device dialog by selecting "Configure..." from the device context menu.
        - It assumes the Network> Devices> Devices view is loaded.
        - Keyword Usage:
         - ``XIQSE Open Configure Device Dialog    ${DEVICE_IP}``

        :param device_ip:  IP of the device to open the Configure Device dialog for
        :return: 1 if action is successful, else -1
        """
        ret_val = -1

        if self.xiqse_select_device(device_ip) == 1:
            menu_btn = self.get_device_menu_tb_button()
            if menu_btn:
                self.utils.print_info("Clicking Device Menu toolbar button")
                self.auto_actions.click(menu_btn)
                sleep(1)

                config_menu = self.get_configure_menu_item()
                if config_menu:
                    self.utils.print_info("Clicking 'Configure...' menu")
                    self.auto_actions.click(config_menu)
                    sleep(2)
                    ret_val = 1
                else:
                    self.utils.print_info("Unable to find 'Configure...' menu")
                    self.screen.save_screen_shot()
            else:
                self.utils.print_info("Unable to find Device Menu toolbar button")
                self.screen.save_screen_shot()

        return ret_val

    def xiqse_configure_device_device_tab(self, device_ip, system_name=None, contact=None, location=None, profile=None,
                                      serial=None, remove_from_service=None, use_default_url=None,
                                      webview_url=None, site=None, poll_group=None, poll_type=None,
                                      timeout=None, retries=None, topo=None, mode=None, interval=None):
        """
        - This keyword configures the device with the specified Device tab values.  It does not save the changes.
        - Keyword Usage:
         - ``XIQSE Configure Device Device Tab   1.2.3.4  system_name=MY_SYSTEMNAME  profile=EXTR_v2_Profile  timeout=10``

        :param device_ip:            IP address of the device to configure
        :param system_name:          Value to enter into the System Name field
        :param contact:              Value to enter into the Contact field
        :param location:             Value to enter into the Location field
        :param profile:              Value to enter into the Administration Profile field
        :param serial:               Value to enter into the Replacement Serial Number field
        :param remove_from_service:  Specifies whether to enable/disable the Remove From Service checkbox (true/false)
        :param use_default_url:      Specifies whether to enable/disable the Use Default WebView URL checkbox (true/false)
        :param webview_url:          Value to enter into the WebView URL field
        :param site:                 Value to enter into the Default Site field
        :param poll_group:           Value to enter into the Poll Group field
        :param poll_type:            Value to enter into the Poll Type field
        :param timeout:              Value to enter into the SNMP Timeout field
        :param retries:              Value to enter into the SNMP Retries field
        :param topo:                 Value to enter into the Topology Layer field
        :param mode:                 Value to enter into the Collection Mode field
        :param interval:             Value to enter into the Collection Interval field
        :return: 1 if action is successful, else -1
        """
        ret_val = 1

        # Open the Configure Device dialog
        if self.xiqse_open_configure_device_dialog(device_ip):

            # Select the Device tab
            if self.config_dlg.xiqse_configure_device_dialog_select_tab("Device") == 1:

                # Populate each field which was specified
                field_result =\
                    self.config_dlg_device.xiqse_configure_device_set_device_tab_values(system_name, contact, location,
                                                                                 profile, serial, remove_from_service,
                                                                                 use_default_url, webview_url, site,
                                                                                 poll_group, poll_type, timeout, retries,
                                                                                 topo, mode, interval)
                if field_result == -1:
                    ret_val = -1
            else:
                ret_val = -1
        else:
            ret_val = -1

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_configure_device_device_tab_and_save(self, device_ip, system_name=None, contact=None, location=None,
                                                   profile=None, serial=None, remove_from_service=None, use_default_url=None,
                                                   webview_url=None, site=None, poll_group=None, poll_type=None,
                                                   timeout=None, retries=None, topo=None, mode=None, interval=None):
        """
        - This keyword configures the device with the specified Device tab values and saves the changes.
        - The Configure Device dialog is opened, the Device tab is selected and populated with the specified
        - values, and the Save button is clicked.
        - Keyword Usage:
         - ``XIQSE Configure Device Device Tab and Save   1.2.3.4  system_name=MY_SYSTEMNAME  profile=EXTR_v2_Profile  timeout=10``

        :param device_ip:            IP address of the device to configure
        :param system_name:          Value to enter into the System Name field
        :param contact:              Value to enter into the Contact field
        :param location:             Value to enter into the Location field
        :param profile:              Value to enter into the Administration Profile field
        :param serial:               Value to enter into the Replacement Serial Number field
        :param remove_from_service:  Specifies whether to enable/disable the Remove From Service checkbox (true/false)
        :param use_default_url:      Specifies whether to enable/disable the Use Default WebView URL checkbox (true/false)
        :param webview_url:          Value to enter into the WebView URL field
        :param site:                 Value to enter into the Default Site field
        :param poll_group:           Value to enter into the Poll Group field
        :param poll_type:            Value to enter into the Poll Type field
        :param timeout:              Value to enter into the SNMP Timeout field
        :param retries:              Value to enter into the SNMP Retries field
        :param topo:                 Value to enter into the Topology Layer field
        :param mode:                 Value to enter into the Collection Mode field
        :param interval:             Value to enter into the Collection Interval field
        :return: 1 if action is successful, else -1
        """
        # Set the device values
        ret_val = self.xiqse_configure_device_device_tab(device_ip, system_name, contact, location,
                                                         profile, serial, remove_from_service,
                                                         use_default_url, webview_url, site,
                                                         poll_group, poll_type, timeout, retries,
                                                         topo, mode, interval)
        if ret_val != -1:
            # Save the changes
            ret_val = self.config_dlg.xiqse_configure_device_dialog_click_save()

        return ret_val

    def xiqse_configure_device_annotations(self, device_ip, nickname=None, asset_tag=None, ud1=None, ud2=None, ud3=None, ud4=None, note=None):
        """
        - This keyword configures the device with the specified Device Annotation values.  It does not save the changes.
        - Keyword Usage:
         - ``XIQSE Configure Device Annotations   1.2.3.4  nickname=MY_NICKNAME  ud2=MY DATA 2  note=MY NOTE\n2nd LINE``

        :param device_ip:  IP address of the device to configure
        :param nickname:   Value to enter into the Nickname field
        :param asset_tag:  Value to enter into the Asset Tag field
        :param ud1:        Value to enter into the User Data 1 field
        :param ud2:        Value to enter into the User Data 2 field
        :param ud3:        Value to enter into the User Data 3 field
        :param ud4:        Value to enter into the User Data 4 field
        :param note:       Value to enter into the Note field
        :return: 1 if action is successful, else -1
        """
        ret_val = 1

        # Open the Configure Device dialog
        if self.xiqse_open_configure_device_dialog(device_ip):

            # Select the Device Annotation tab
            if self.config_dlg.xiqse_configure_device_dialog_select_tab("Device Annotation") == 1:

                # Populate each field which was specified
                field_result =\
                    self.config_dlg_annotations.xiqse_configure_device_set_annotation_tab_values(nickname, asset_tag, ud1, ud2, ud3, ud4, note)
                if field_result == -1:
                    ret_val = -1
            else:
                ret_val = -1
        else:
            ret_val = -1

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_configure_device_annotations_and_save(self, device_ip, nickname=None, asset_tag=None, ud1=None, ud2=None, ud3=None, ud4=None, note=None):
        """
        - This keyword configures the device with the specified Device Annotation values and saves the changes.
        - The Configure Device dialog is opened, the Device Annotation tab is selected and populated with the specified
        - values, and the Save button is clicked.
        - Keyword Usage:
         - ``XIQSE Configure Device Annotations and Save   1.2.3.4  nickname=MY_NICKNAME  ud2=MY DATA 2  note=MY NOTE\n2nd LINE``

        :param device_ip:  IP address of the device to configure
        :param nickname:   Value to enter into the Nickname field
        :param asset_tag:  Value to enter into the Asset Tag field
        :param ud1:        Value to enter into the User Data 1 field
        :param ud2:        Value to enter into the User Data 2 field
        :param ud3:        Value to enter into the User Data 3 field
        :param ud4:        Value to enter into the User Data 4 field
        :param note:       Value to enter into the Note field
        :return: 1 if action is successful, else -1
        """
        # Set the annotations
        ret_val = self.xiqse_configure_device_annotations(device_ip, nickname, asset_tag, ud1, ud2, ud3, ud4, note)
        if ret_val != -1:
            # Save the changes
            ret_val = self.config_dlg.xiqse_configure_device_dialog_click_save()

        return ret_val

    def xiqse_wait_until_device_add_operation_complete(self, retry_duration=30, retry_count=10):
        """
         - This keyword waits until the device add operation has completed by checking the Device Added entry in the
         - Operations panel for progress value of 100%.
         - It is assumed the view is already navigated to the Site tab.
         - NOTE: before performing the Device Add operation, the operations panel should be cleared, as the first match
         - of "Device Added" will be used to check the progress.
         - Keyword Usage
          - ``XIQSE Site Wait Until Device Add Operation Complete``
          - ``XIQSE Site Wait Until Device Add Operation Complete    retry_duration=10  retry_count=60``

        :param retry_duration: duration between each retry
        :param retry_count: retry count
        :return: 1 if action was successful, else -1
        """
        return self.operations_panel.xiqse_operations_wait_until_operation_complete("Device Added",
                                                                                    retry_duration, retry_count)

    def xiqse_wait_until_device_added(self, device_ip, retry_duration=10, retry_count=30):
        """
        - This keyword is used to wait for the device to show up in the devices table.
        - This keyword by default loops 10 times every 30 seconds to check if the device exists.
        - It is assumed the Network> Devices> Devices tab is already selected.
        - Keyword Usage:
         - ``XIQSE Wait Until Device Added    ${DEVICE_IP}    retry_duration=30    retry_count=12``

        :param device_ip: device IP to look for
        :param retry_duration: duration between each retry
        :param retry_count: retry count
        :return: 1 if device added within time; else -1
        """

        # Take a screenshot before the method begins
        self.screen.save_screen_shot()

        # Filter for the value in case the view contains a lot of devices
        self.xiqse_devices_perform_search(device_ip)

        count = 1
        while count <= retry_count:
            self.utils.print_info(f"Searching for device {device_ip}: loop {count}")
            if self.xiqse_find_device_with_ip(device_ip, take_screenshot=False) == 1:
                self.utils.print_info(f"Device {device_ip} has been added")
                self.xiqse_devices_clear_search()
                return 1
            else:
                self.utils.print_info(f"Device is not yet present. Waiting for {retry_duration} seconds...")
                sleep(retry_duration)
                self.xiqse_table.xiqse_refresh_table()
            count += 1

        # Check for device one last time
        self.xiqse_table.xiqse_refresh_table()
        if self.xiqse_find_device_with_ip(device_ip) == 1:
            self.utils.print_info(f"Device {device_ip} has been added")
            self.xiqse_devices_clear_search()
            return 1

        self.utils.print_info(f"Device does not exist. Please check.")
        self.screen.save_screen_shot()
        self.xiqse_devices_clear_search()
        return -1

    def xiqse_wait_until_device_removed(self, device_ip, retry_duration=10, retry_count=30):
        """
        - This keyword is used to wait for the device to be removed from the devices table.
        - This keyword by default loops 10 times every 30 seconds to check if the device exists.
        - It is assumed the Network> Devices> Devices tab is already selected.
        - Keyword Usage:
         - ``XIQSE Wait Until Device Removed    ${DEVICE_IP}    retry_duration=30    retry_count=12``

        :param device_ip: device IP to look for
        :param retry_duration: duration between each retry
        :param retry_count: retry count
        :return: 1 if device removed within time; else -1
        """
        # Filter for the value in case the view contains a lot of devices
        self.xiqse_devices_perform_search(device_ip)

        count = 1
        while count <= retry_count:
            self.utils.print_info(f"Searching for device {device_ip}: loop {count}")
            if self.xiqse_find_device_with_ip(device_ip, take_screenshot=False) == -1:
                self.utils.print_info(f"Device {device_ip} has been removed")
                self.xiqse_devices_clear_search()
                return 1
            else:
                self.utils.print_info(f"Device is still present. Waiting for {retry_duration} seconds...")
                sleep(retry_duration)
                self.xiqse_table.xiqse_refresh_table()
            count += 1

        # Check for device one last time
        self.xiqse_table.xiqse_refresh_table()
        if self.xiqse_find_device_with_ip(device_ip) == -1:
            self.utils.print_info(f"Device {device_ip} has been removed")
            self.xiqse_devices_clear_search()
            return 1

        self.utils.print_info(f"Device is still present. Please check.")
        self.screen.save_screen_shot()
        self.xiqse_devices_clear_search()
        return -1

    def xiqse_wait_until_device_status_up(self, device_ip, retry_duration=30, retry_count=20):
        """
        - This keyword is used to wait for the device status to show as "Device Status Up" in the devices table.
        - This keyword by default loops 10 times every 30 seconds to check if the device is up.
        - It is assumed the Network> Devices> Devices tab is already selected.
        - Keyword Usage:
         - ``XIQSE Wait Until Device Status Up    ${DEVICE_IP}    retry_duration=10    retry_count=12``

        :param device_ip: device IP to check the status of
        :param retry_duration: duration between each retry
        :param retry_count: retry count
        :return: 1 if device status is up within specified time; else -1
        """
        ret_val = -1

        count = 1
        while count <= retry_count:
            self.utils.print_info(f"Device Up Status Check - Loop: ", count)

            stale_retry = 1
            while stale_retry <= 10:
                try:
                    device_row = self.xiqse_get_device_row(device_ip, take_screenshot=False)
                    if device_row:
                        self.utils.print_debug(f"Row data: {self.xiqse_table.format_table_row(device_row.text)}")

                        status_cell = self.get_device_status_cell_value(device_row)
                        self.utils.print_info(f"Status Cell: {status_cell}")
                        if status_cell and "Device Status Up" in status_cell:
                            self.utils.print_info("Device status is up")
                            return 1
                        else:
                            self.utils.print_info(f"Device status is not up. Waiting for {retry_duration} seconds...")
                            sleep(retry_duration)
                    else:
                        self.utils.print_info(f"Did not find row for device {device_ip}.  Waiting for {retry_duration} seconds...")
                        sleep(retry_duration)

                    # Break out of the Stale Element Exception loop
                    break
                except StaleElementReferenceException:
                    self.utils.print_info(f"Handling StaleElementReferenceException - loop {stale_retry}")
                    stale_retry = stale_retry + 1

            # Increment retry counter
            count += 1

        if ret_val == -1:
            self.utils.print_info(f"Device status failed to go up. Please check.")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_wait_until_device_status_down(self, device_ip, retry_duration=30, retry_count=10):
        """
        - This keyword is used to wait for the device status to show as "Device Status Down" in the devices table.
        - This keyword by default loops 10 times every 30 seconds to check if the device is down.
        - It is assumed the Network> Devices> Devices tab is already selected.
        - Keyword Usage:
         - ``XIQSE Wait Until Device Status Down    ${DEVICE_IP}    retry_duration=10    retry_count=12``

        :param device_ip: device IP to check the status of
        :param retry_duration: duration between each retry
        :param retry_count: retry count
        :return: 1 if device status is down within specified time; else -1
        """
        count = 1
        while count <= retry_count:
            self.utils.print_info(f"Device Down Status Check - Loop: ", count)

            stale_retry = 1
            while stale_retry <= 10:
                try:
                    device_row = self.xiqse_get_device_row(device_ip, take_screenshot=False)
                    if device_row:
                        self.utils.print_debug(f"Row data: {self.xiqse_table.format_table_row(device_row.text)}")

                        status_cell = self.get_device_status_cell_value(device_row)
                        self.utils.print_debug(f"Status Cell: {status_cell}")
                        if status_cell and "Device Status Down" in status_cell:
                            self.utils.print_info("Device status is down")
                            return 1
                        else:
                            self.utils.print_info(f"Device status is not down. Waiting for {retry_duration} seconds...")
                            sleep(retry_duration)
                    else:
                        self.utils.print_info(f"Did not find row for device {device_ip}.  Waiting for {retry_duration} seconds...")
                        sleep(retry_duration)

                    # Break out of the Stale Element Exception loop
                    break
                except StaleElementReferenceException:
                    self.utils.print_info(f"Handling StaleElementReferenceException - loop {stale_retry}")
                    stale_retry = stale_retry + 1

            # Increment retry counter
            count += 1

        self.utils.print_info(f"Device status failed to go down. Please check.")
        self.screen.save_screen_shot()

        return -1

    def xiqse_wait_until_device_archived(self, device_ip, retry_duration=30, retry_count=10):
        """
        - This keyword is used to wait for the device to show as being archived in the devices table.
        - This keyword by default loops 10 times every 30 seconds to check if the device is archived.
        - It is assumed the Network> Devices> Devices tab is already selected.
        - Keyword Usage:
         - ``XIQSE Wait Until Device Archived    ${DEVICE_IP}    retry_duration=10    retry_count=12``

        :param device_ip: device IP to check the archive status of
        :param retry_duration: duration between each retry
        :param retry_count: retry count
        :return: 1 if device archived within specified time; else -1
        """
        ret_val = -1
        count = 1
        while count <= retry_count:
            self.utils.print_info(f"Device Archived Check - Loop: ", count)

            stale_retry = 1
            while stale_retry <= 10:
                try:
                    self.xiqse_table.xiqse_refresh_table()

                    is_archived = self.xiqse_get_device_column_value(device_ip, "Archived")
                    self.utils.print_info(f"Is Archived: '{is_archived}'")
                    if is_archived and is_archived == "True":
                        self.utils.print_info("Device is archived")
                        return 1
                    else:
                        self.utils.print_info(f"Device is not yet archived. Waiting for {retry_duration} seconds...")
                        sleep(retry_duration)

                    # Break out of the Stale Element Exception loop
                    break
                except StaleElementReferenceException:
                    self.utils.print_info(f"Handling StaleElementReferenceException - loop {stale_retry}")
                    stale_retry = stale_retry + 1

            # Increment retry counter
            count += 1

        if ret_val == -1:
            self.utils.print_info(f"Device did not become archived within allocated time. Please check.")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_wait_until_device_not_archived(self, device_ip, retry_duration=30, retry_count=10):
        """
        - This keyword is used to wait for the device to show as not being archived in the devices table.
        - This keyword by default loops 10 times every 30 seconds to check if the device is archived or not.
        - It is assumed the Network> Devices> Devices tab is already selected.
        - Keyword Usage:
         - ``XIQSE Wait Until Device Not Archived    ${DEVICE_IP}    retry_duration=10    retry_count=12``

        :param device_ip: device IP to check the archive status of
        :param retry_duration: duration between each retry
        :param retry_count: retry count
        :return: 1 if device not archived within specified time; else -1
        """
        ret_val = -1
        count = 1
        while count <= retry_count:
            self.utils.print_info(f"Device Archived Check - Loop: ", count)

            stale_retry = 1
            while stale_retry <= 10:
                try:
                    self.xiqse_table.xiqse_refresh_table()

                    is_archived = self.xiqse_get_device_column_value(device_ip, "Archived")
                    self.utils.print_info(f"Is Archived: '{is_archived}'")
                    if is_archived and is_archived == "False":
                        self.utils.print_info("Device is not archived")
                        return 1
                    else:
                        self.utils.print_info(f"Device is still archived. Waiting for {retry_duration} seconds...")
                        sleep(retry_duration)

                    # Break out of the Stale Element Exception loop
                    break
                except StaleElementReferenceException:
                    self.utils.print_info(f"Handling StaleElementReferenceException - loop {stale_retry}")
                    stale_retry = stale_retry + 1

            # Increment retry counter
            count += 1

        if ret_val == -1:
            self.utils.print_info(f"Device is still archived after allocated time. Please check.")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_wait_until_device_onboarded_to_xiq(self, device_ip, retry_duration=30, retry_count=10):
        """
        - This keyword is used to wait for the device to show as being Onboarded to XIQ in the devices table.
        - The column checked is "XIQ Onboarded".
        - This keyword by default loops 10 times every 30 seconds to check if the device is onboarded to xiq.
        - It is assumed the Network> Devices> Devices tab is already selected.
        - Keyword Usage:
         - ``XIQSE Wait Until Device Onboarded to XIQ    ${DEVICE_IP}    retry_duration=10    retry_count=12``

        :param device_ip: device IP to check the XIQ Onboarded status of
        :param retry_duration: duration between each retry
        :param retry_count: retry count
        :return: 1 if device archived within specified time; else -1
        """
        ret_val = -1
        count = 1
        while count <= retry_count:
            self.utils.print_info(f"Device XIQ Onboarded Check - Loop: ", count)

            stale_retry = 1
            while stale_retry <= 10:
                try:
                    self.xiqse_table.xiqse_refresh_table()

                    is_onboarded = self.xiqse_get_device_column_value(device_ip, "XIQ Onboarded")
                    self.utils.print_info(f"Is Onboarded: '{is_onboarded}'")
                    if is_onboarded and is_onboarded == "Onboarded":
                        self.utils.print_info("Device is onboarded to XIQ")
                        return 1
                    else:
                        self.utils.print_info(f"Device is not yet onboarded to XIQ. Waiting for {retry_duration} seconds...")
                        sleep(retry_duration)

                    # Break out of the Stale Element Exception loop
                    break
                except StaleElementReferenceException:
                    self.utils.print_info(f"Handling StaleElementReferenceException - loop {stale_retry}")
                    stale_retry = stale_retry + 1

            # Increment retry counter
            count += 1

        if ret_val == -1:
            self.utils.print_info(f"Device did not onboard to XIQ within allocated time. Please check.")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_wait_until_devices_present(self, device_count, exact="true", retry_duration=30, retry_count=10):
        """
        - This keyword is used to wait for the specified number of devices to be present in the devices table.
        - If "exact" is passed as "false", then it will wait until at least the specified number of devices are present
        - (will still succeed if more devices are present than the specified amount); otherwise, this keyword will only
        - succeed if the device count exactly matches what is expected.
        - This keyword by default loops 10 times every 30 seconds.
        - It is assumed the Network> Devices> Devices tab is already selected.
        - Keyword Usage:
         - ``XIQSE Wait Until Devices Present    ${DEVICE_COUNT}    retry_duration=10    retry_count=12``
         - ``XIQSE Wait Until Devices Present    ${DEVICE_COUNT}    exact=false    retry_duration=20    retry_count=5``

        :param device_count: number of devices which should be present
        :param exact: true (default) or false.
        :param retry_duration: duration between each retry
        :param retry_count: retry count
        :return: 1 if device added within time; else -1
        """
        count = 1
        while count <= retry_count:
            self.utils.print_info(f"Device Count Check - Loop: ", count)

            stale_retry = 1
            while stale_retry <= 10:
                try:
                    self.xiqse_table.xiqse_refresh_table()

                    total_count = self.xiqse_get_device_total_count(take_screenshot=False)
                    self.utils.print_debug(f"Current device total count is {total_count}")
                    total_int = int(total_count)
                    expected_int = int(device_count)
                    if exact == "true":
                        if total_int == expected_int:
                            self.utils.print_info(f"Device total count is at expected value {device_count}")
                            return 1
                        else:
                            self.utils.print_info(f"Total device count {total_count} does not equal expected device count {device_count}. Waiting for {retry_duration} seconds...")
                            sleep(retry_duration)
                    else:
                        if expected_int <= total_int:
                            self.utils.print_info(f"Total device count ({total_count}) has reached the expected device count ({device_count})")
                            return 1
                        else:
                            self.utils.print_info(f"Total device count {total_count} is less than the expected device count {device_count}. Waiting for {retry_duration} seconds...")
                            sleep(retry_duration)

                    # Break out of the Stale Element Exception loop
                    break
                except StaleElementReferenceException:
                    self.utils.print_info(f"Handling StaleElementReferenceException - loop {stale_retry}")
                    stale_retry = stale_retry + 1

            # Increment retry counter
            count += 1

        self.utils.print_info("Device count is not at expected value. Please check.")
        self.screen.save_screen_shot()

        return -1

    def xiqse_wait_until_device_has_serial_number(self, device_ip, retry_duration=30, retry_count=10):
        """
        - This keyword is used to wait for the device to have a serial number.  This is used for devices
        - which don't have a serial number and which XIQSE determines the serial number for.
        - This keyword by default loops 10 times every 30 seconds to check if the device has a serial number.
        - It is assumed the Network> Devices> Devices tab is already selected.
        - Keyword Usage:
         - ``XIQSE Wait Until Device Has Serial Number    ${DEVICE_IP}    retry_duration=10    retry_count=12``

        :param device_ip: device IP to check the serial number of
        :param retry_duration: duration between each retry
        :param retry_count: retry count
        :return: 1 if device has a serial number value within specified time; else -1
        """
        ret_val = -1
        count = 1
        while count <= retry_count:
            self.utils.print_info(f"Device Serial Number Check - Loop: ", count)

            stale_retry = 1
            while stale_retry <= 10:
                try:
                    self.xiqse_table.xiqse_refresh_table()

                    the_value = self.xiqse_get_device_serial_number(device_ip)
                    self.utils.print_info(f"Serial Value: '{the_value}'")
                    if the_value != -1:
                        self.utils.print_info("Device has a serial number")
                        return 1
                    else:
                        self.utils.print_info(f"Device does not yet have a serial number. Waiting for {retry_duration} seconds...")
                        sleep(retry_duration)

                    # Break out of the Stale Element Exception loop
                    break
                except StaleElementReferenceException:
                    self.utils.print_info(f"Handling StaleElementReferenceException - loop {stale_retry}")
                    stale_retry = stale_retry + 1

            # Increment retry counter
            count += 1

        if ret_val == -1:
            self.utils.print_info(f"Device did not obtain a serial number within allocated time. Please check.")

        return ret_val

    def xiqse_wait_until_device_has_base_mac(self, device_ip, retry_duration=30, retry_count=10):
        """
        - This keyword is used to wait for the device to have a base MAC.  This is used for devices
        - which don't have a base MAC and which XIQSE determines the base MAC value for.
        - This keyword by default loops 10 times every 30 seconds to check if the device has a base MAC.
        - It is assumed the Network> Devices> Devices tab is already selected.
        - Keyword Usage:
         - ``XIQSE Wait Until Device Has Base MAC    ${DEVICE_IP}    retry_duration=10    retry_count=12``

        :param device_ip: device IP to check the base MAC of
        :param retry_duration: duration between each retry
        :param retry_count: retry count
        :return: 1 if device has a base MAC value within specified time; else -1
        """
        ret_val = -1
        count = 1
        while count <= retry_count:
            self.utils.print_info(f"Device Base MAC Check - Loop: ", count)

            stale_retry = 1
            while stale_retry <= 10:
                try:
                    self.xiqse_table.xiqse_refresh_table()

                    the_value = self.xiqse_get_device_base_mac(device_ip)
                    self.utils.print_info(f"Base MAC: '{the_value}'")
                    if the_value != -1:
                        self.utils.print_info("Device has a base MAC")
                        return 1
                    else:
                        self.utils.print_info(f"Device does not yet have a base MAC. Waiting for {retry_duration} seconds...")
                        sleep(retry_duration)

                    # Break out of the Stale Element Exception loop
                    break
                except StaleElementReferenceException:
                    self.utils.print_info(f"Handling StaleElementReferenceException - loop {stale_retry}")
                    stale_retry = stale_retry + 1

            # Increment retry counter
            count += 1

        if ret_val == -1:
            self.utils.print_info(f"Device did not obtain a base MAC within allocated time. Please check.")

        return ret_val

    def xiqse_wait_until_device_upgraded(self, device_ip, upgrade_version, retry_duration=30, retry_count=10):
        """
        - This keyword is used to wait for the device to show as being upgraded to the upgrade version in the devices table.
        - This keyword by default loops 10 times every 30 seconds to check if the device is upgraded.
        - It is assumed the Network> Devices> Devices tab is already selected.
        - Keyword Usage:
         - ``XIQSE Wait Until Device Upgraded    ${DEVICE_IP}    ${UPGRADE_VERSION}     retry_duration=10    retry_count=12``
        :param device_ip: device IP to check the archive status of
        :param upgrade_version: expected firmware version value
        :param retry_duration: duration between each retry
        :param retry_count: retry count
        :return: 1 if device upgraded within specified time; else -1
        """
        ret_val = -1
        count = 1
        while count <= retry_count:
            self.utils.print_info(f"Device Upgraded Check - Loop: ", count)

            stale_retry = 1
            while stale_retry <= 10:
                try:
                    self.xiqse_table.xiqse_refresh_table()

                    is_upgraded = self.xiqse_get_device_column_value(device_ip, "Firmware")
                    self.utils.print_info(f"Is Upgraded: '{is_upgraded}'")
                    if is_upgraded and is_upgraded == upgrade_version:
                        self.utils.print_info("Device is upgraded")
                        return 1
                    else:
                        self.utils.print_info(
                            f"Device is not showing upgraded version. Waiting for {retry_duration} seconds...")
                        sleep(retry_duration)

                    # Break out of the Stale Element Exception loop
                    break
                except StaleElementReferenceException:
                    self.utils.print_info(f"Handling StaleElementReferenceException - loop {stale_retry}")
                    stale_retry = stale_retry + 1

            # Increment retry counter
            count += 1

        if ret_val == -1:
            self.utils.print_info(f"Device did not show upgraded version within allocated time. Please check.")

        return ret_val

    def xiqse_confirm_device_profile(self, device_ip, profile_name, retry_duration=30, retry_count=10):
        """
        - This keyword is used to wait for the device profile to be at the expected value in the Devices table.
        - This keyword by default loops 10 times every 30 seconds to check if the device profile matches the value.
        - It is assumed the Network> Devices> Devices tab is already selected and the Admin Profile column is displayed.
        - Keyword Usage:
         - ``XIQSE Confirm Device Profile    ${DEVICE_IP}  ${PROFILE_NAME}  retry_duration=10  retry_count=12``

        :param device_ip: device IP to look for
        :param profile_name: expected value of the profile
        :param retry_duration: duration between each retry
        :param retry_count: retry count
        :return: 1 if device added within time; else -1
        """
        count = 1
        while count <= retry_count:
            self.utils.print_info(f"Device Profile Check - Loop: ", count)

            stale_retry = 1
            while stale_retry <= 10:
                try:
                    self.xiqse_table.xiqse_refresh_table()

                    profile_value = self.xiqse_get_device_profile(device_ip)
                    if profile_value == profile_name:
                        self.utils.print_info(f"Profile is at expected value '{profile_name}'")
                        return 1
                    else:
                        self.utils.print_info(f"Profile is '{profile_value}'. Waiting for {retry_duration} seconds...")
                        sleep(retry_duration)

                    # Break out of the Stale Element Exception loop
                    break
                except StaleElementReferenceException:
                    self.utils.print_info(f"Handling StaleElementReferenceException - loop {stale_retry}")
                    stale_retry = stale_retry + 1

            # Increment retry counter
            count += 1

        self.utils.print_info(f"Profile failed to update to expected value '{profile_name}'. Please check.")
        self.screen.save_screen_shot()

        return -1

    def xiqse_find_device_with_ip(self, device_ip, take_screenshot=True):
        """
        - Searches for Device matching Device's IP Address

        :param device_ip: Device IP Address to search for
        :param take_screenshot: Indicates whether the xiqse_get_device_row keyword should take a screenshot on failure
               this is used when calling from a "wait until" keyword which won't necessarily want to take a screenshot
               on each failed loop
        :return: return 1 if Device with specified IP address is found, else -1
        """
        ret_val = -1

        row = self.xiqse_get_device_row(device_ip, take_screenshot)
        if row:
            ret_val = 1
        return ret_val

    def xiqse_get_device_row(self, device_ip, take_screenshot=True):
        """
        - This keyword returns the row for the device matching the IP address

        :param device_ip: IP address of the device to obtain the row for
        :param take_screenshot: Indicates whether this keyword should take a screenshot on failure.
               This is used when calling from a "wait until" keyword which won't necessarily want
               to take a screenshot on each failed loop
        :return: returns the row object
        """
        self.utils.print_info(f'Getting device row for device with IP address {device_ip}')
        stale_retry = 1
        while stale_retry <= 10:
            try:
                self.xiqse_table.xiqse_refresh_table()

                rows = self.get_table_rows()
                if rows:
                    for row in rows:
                        if device_ip in row.text:
                            self.utils.print_info(f"Found device row for {device_ip}: {self.xiqse_table.format_table_row(row.text)}")
                            return row
                    self.utils.print_info(f"Did not find row for {device_ip}")
                    break
                else:
                    self.utils.print_info("Did not find any rows in table")
                    break
            except StaleElementReferenceException:
                self.utils.print_info(f"Handling StaleElementReferenceException - loop {stale_retry}")
                stale_retry = stale_retry+1

        self.utils.print_info(f"Unable to find device row in grid for IP address {device_ip}")
        if take_screenshot:
            self.screen.save_screen_shot()

        return None

    def xiqse_get_device_total_count(self, take_screenshot=True):
        """
        - This keyword returns the total number of items in the Devices table based on the Displaying label.

        :param take_screenshot: Indicates whether the keyword should take a screenshot on failure.
               This is used when calling from a "wait until" keyword which won't necessarily want to take a screenshot
               on each failed loop.
        :return: returns the total number of items in the table
        """
        ret_val = 0

        displaying_label = self.get_table_displaying_label()
        if displaying_label:
            displaying_text = displaying_label.text
            if displaying_text:
                self.utils.print_debug(f"Got displaying label text {displaying_text}")
                text_list = displaying_text.split(' of ')
                # The number of total devices should be the last element in the list,
                # since the data for this label ends with " of ##"
                device_count = text_list[-1]
                if device_count:
                    self.utils.print_info(f"Returning device count {device_count}")
                    ret_val = device_count
                else:
                    self.utils.print_info("Unable to parse text from Displaying label to determine total device count")
                    if take_screenshot:
                        self.screen.save_screen_shot()
            else:
                self.utils.print_info("Unable to get text from Displaying label to determine total device count")
                if take_screenshot:
                    self.screen.save_screen_shot()
        else:
            self.utils.print_info("Displaying label is not present - device count is 0")
            if take_screenshot:
                self.screen.save_screen_shot()

        return ret_val

    def xiqse_select_all_visible_devices(self):
        """
        - This keyword selects all visible rows in the table.  Note this may differ from the actual total number of
        - rows, as the table populates with data when the table is scrolled (for example, although there may be 250
        - rows in the table, only 44 would be "visible" and obtainable by automation).

        :return: returns 1 if action was successful, else -1
        """
        ret_val = -1

        visible_rows = self.get_table_rows()
        if visible_rows:
            # Select from the first row to the last row in the list
            ret_val = self.auto_actions.select_table_range(visible_rows[0], visible_rows[-1])
        else:
            self.utils.print_info("No visible rows to select")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_delete_all_devices(self):
        """
        - This keyword deletes all items in the Devices table.
        - Note this needs to be done in batches as not all rows are visible at once.

        :return: returns 1 if action was successful, else -1
        """
        ret_val = 1

        visible_rows = self.get_table_rows()
        while ret_val == 1 and visible_rows:
            self.xiqse_select_all_visible_devices()
            ret_val = self.xiqse_delete_selected_devices()
            sleep(2)
            self.xiqse_table.xiqse_refresh_table()
            visible_rows = self.get_table_rows()

        return ret_val

    def xiqse_get_device_serial_number(self, device_ip):
        """
        - This keyword is used to get the serial number for the specified device in the devices table.
        - It is assumed the Network> Devices> Devices tab is already selected.
        - Keyword Usage:
         - ``XIQSE Get Device Serial Number    ${DEVICE_IP}``

        :param device_ip: device IP to get the serial number for
        :return: serial number for the specified device;  -1 if serial number cannot be determined
        """
        ret_val = -1

        device_row = self.xiqse_get_device_row(device_ip)
        if device_row:
            the_col = self.get_device_column_by_name("Serial Number")
            col_id = self.view_el.get_column_id(the_col)
            self.utils.print_debug(f"Column ID: {col_id}")
            col_val = self.get_device_column_value(col_id, device_row)
            if col_val:
                serial_value = col_val.text
                self.utils.print_debug(f"Serial Number Value: {serial_value}")
                serial_value = re.sub('<span>', '', serial_value)
                serial_value = re.sub('</span>', '', serial_value)
                self.utils.print_info(f"Returning Serial Number {serial_value} for device {device_ip}")
                ret_val = serial_value
            else:
                self.utils.print_info(f"Unable to determine serial number for device {device_ip}")
        else:
            self.utils.print_info(f"Unable to find row for device with IP {device_ip}")

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_get_device_profile(self, device_ip):
        """
        - This keyword is used to get the profile for the specified device in the devices table.
        - It is assumed the Network> Devices> Devices tab is already selected.
        - Keyword Usage:
         - ``XIQSE Get Device Profile    ${DEVICE_IP}``

        :param device_ip: device IP to get the admin profile for
        :return: admin profile for the specified device;  empty string ("") if admin profile cannot be determined
        """
        ret_val = ""

        device_row = self.xiqse_get_device_row(device_ip)
        if device_row:
            the_col = self.get_device_column_by_name("Admin Profile")
            col_id = self.view_el.get_column_id(the_col)
            self.utils.print_debug(f"Column ID: {col_id}")
            if col_id != -1:
                col_val = self.get_device_column_value(col_id, device_row)
                if col_val:
                    profile_value = col_val.text
                    self.utils.print_info(f"Returning Profile {profile_value} for device {device_ip}")
                    ret_val = profile_value
                else:
                    self.utils.print_info(f"Unable to determine admin profile for device {device_ip}")
            else:
                self.utils.print_info("Unable to find column ID for Admin Profile column")
        else:
            self.utils.print_info(f"Unable to find row for device with IP {device_ip}")

        self.utils.print_info(f"Returning profile{ret_val} for device {device_ip}")
        self.screen.save_screen_shot()

        return ret_val

    def xiqse_get_device_base_mac(self, device_ip):
        """
        - This keyword is used to get the base MAC for the specified device in the devices table.
        - It is assumed the Network> Devices> Devices tab is already selected.
        - Keyword Usage:
         - ``XIQSE Get Device Base MAC    ${DEVICE_IP}``

        :param device_ip: device IP to get the base MAC for
        :return: base MAC for the specified device;  -1 if base MAC cannot be determined
        """
        ret_val = -1

        device_row = self.xiqse_get_device_row(device_ip)
        if device_row:
            the_col = self.get_device_column_by_name("Base MAC")
            col_id = self.view_el.get_column_id(the_col)
            self.utils.print_debug(f"Column ID: {col_id}")
            col_val = self.get_device_column_value(col_id, device_row)
            if col_val:
                mac_value = col_val.text
                self.utils.print_debug(f"Base MAC Value: {mac_value}")
                mac_value = re.sub(':', '', mac_value)
                self.utils.print_info(f"Returning Base MAC {mac_value} for device {device_ip}")
                ret_val = mac_value
            else:
                self.utils.print_info(f"Unable to determine base MAC for device {device_ip}")
        else:
            self.utils.print_info(f"Unable to find row for device with IP {device_ip}")

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_get_device_nickname(self, device_ip):
        """
        - This keyword is used to get the Nickname value for the specified device in the devices table.
        - It is assumed the Network> Devices> Devices tab is already selected.
        - Keyword Usage:
         - ``XIQSE Get Device Nickname    ${DEVICE_IP}``

        :param device_ip: device IP to get the value for
        :return: nickname for the specified device;  empty string ("") if value cannot be determined
        """
        ret_val = ""

        device_row = self.xiqse_get_device_row(device_ip)
        if device_row:
            the_col = self.get_device_column_by_name("Nickname")
            col_id = self.view_el.get_column_id(the_col)
            self.utils.print_debug(f"Column ID: {col_id}")
            col_val = self.get_device_column_value(col_id, device_row)
            if col_val:
                nickname_value = col_val.text
                self.utils.print_info(f"Returning Nickname '{nickname_value}' for device {device_ip}")
                ret_val = nickname_value
            else:
                self.utils.print_info(f"Unable to determine Nickname for device {device_ip}")
        else:
            self.utils.print_info(f"Unable to find row for device with IP {device_ip}")

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_get_device_asset_tag(self, device_ip):
        """
        - This keyword is used to get the Asset Tag value for the specified device in the devices table.
        - It is assumed the Network> Devices> Devices tab is already selected.
        - Keyword Usage:
         - ``XIQSE Get Device Asset Tag    ${DEVICE_IP}``

        :param device_ip: device IP to get the value for
        :return: asset tag for the specified device;  empty string ("") if value cannot be determined
        """
        ret_val = ""

        device_row = self.xiqse_get_device_row(device_ip)
        if device_row:
            the_col = self.get_device_column_by_name("Asset Tag")
            col_id = self.view_el.get_column_id(the_col)
            self.utils.print_debug(f"Column ID: {col_id}")
            col_val = self.get_device_column_value(col_id, device_row)
            if col_val:
                asset_value = col_val.text
                self.utils.print_info(f"Returning Asset Tag '{asset_value}' for device {device_ip}")
                ret_val = asset_value
            else:
                self.utils.print_info(f"Unable to determine Asset Tag for device {device_ip}")
        else:
            self.utils.print_info(f"Unable to find row for device with IP {device_ip}")

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_get_device_user_data_1(self, device_ip):
        """
        - This keyword is used to get the User Data 1 value for the specified device in the devices table.
        - It is assumed the Network> Devices> Devices tab is already selected.
        - Keyword Usage:
         - ``XIQSE Get Device User Data 1    ${DEVICE_IP}``

        :param device_ip: device IP to get the value for
        :return: user data 1 for the specified device;  empty string ("") if value cannot be determined
        """
        ret_val = ""

        device_row = self.xiqse_get_device_row(device_ip)
        if device_row:
            the_col = self.get_device_column_by_name("User Data 1")
            col_id = self.view_el.get_column_id(the_col)
            self.utils.print_debug(f"Column ID: {col_id}")
            col_val = self.get_device_column_value(col_id, device_row)
            if col_val:
                ud1_value = col_val.text
                self.utils.print_info(f"Returning User Data 1 '{ud1_value}' for device {device_ip}")
                ret_val = ud1_value
            else:
                self.utils.print_info(f"Unable to determine User Data 1 for device {device_ip}")
        else:
            self.utils.print_info(f"Unable to find row for device with IP {device_ip}")

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_get_device_user_data_2(self, device_ip):
        """
        - This keyword is used to get the User Data 2 value for the specified device in the devices table.
        - It is assumed the Network> Devices> Devices tab is already selected.
        - Keyword Usage:
         - ``XIQSE Get Device User Data 2    ${DEVICE_IP}``

        :param device_ip: device IP to get the value for
        :return: user data 2 for the specified device;  empty string ("") if value cannot be determined
        """
        ret_val = ""

        device_row = self.xiqse_get_device_row(device_ip)
        if device_row:
            the_col = self.get_device_column_by_name("User Data 2")
            col_id = self.view_el.get_column_id(the_col)
            self.utils.print_debug(f"Column ID: {col_id}")
            col_val = self.get_device_column_value(col_id, device_row)
            if col_val:
                ud2_value = col_val.text
                self.utils.print_info(f"Returning User Data 2 '{ud2_value}' for device {device_ip}")
                ret_val = ud2_value
            else:
                self.utils.print_info(f"Unable to determine User Data 2 for device {device_ip}")
        else:
            self.utils.print_info(f"Unable to find row for device with IP {device_ip}")

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_get_device_user_data_3(self, device_ip):
        """
        - This keyword is used to get the User Data 3 value for the specified device in the devices table.
        - It is assumed the Network> Devices> Devices tab is already selected.
        - Keyword Usage:
         - ``XIQSE Get Device User Data 3    ${DEVICE_IP}``

        :param device_ip: device IP to get the value for
        :return: user data 3 for the specified device;  empty string ("") if value cannot be determined
        """
        ret_val = ""

        device_row = self.xiqse_get_device_row(device_ip)
        if device_row:
            the_col = self.get_device_column_by_name("User Data 3")
            col_id = self.view_el.get_column_id(the_col)
            self.utils.print_debug(f"Column ID: {col_id}")
            col_val = self.get_device_column_value(col_id, device_row)
            if col_val:
                ud3_value = col_val.text
                self.utils.print_info(f"Returning User Data 3 '{ud3_value}' for device {device_ip}")
                ret_val = ud3_value
            else:
                self.utils.print_info(f"Unable to determine User Data 3 for device {device_ip}")
        else:
            self.utils.print_info(f"Unable to find row for device with IP {device_ip}")

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_get_device_user_data_4(self, device_ip):
        """
        - This keyword is used to get the User Data 4 value for the specified device in the devices table.
        - It is assumed the Network> Devices> Devices tab is already selected.
        - Keyword Usage:
         - ``XIQSE Get Device User Data 4    ${DEVICE_IP}``

        :param device_ip: device IP to get the value for
        :return: user data 4 for the specified device;  empty string ("") if value cannot be determined
        """
        ret_val = ""

        device_row = self.xiqse_get_device_row(device_ip)
        if device_row:
            the_col = self.get_device_column_by_name("User Data 4")
            col_id = self.view_el.get_column_id(the_col)
            self.utils.print_debug(f"Column ID: {col_id}")
            col_val = self.get_device_column_value(col_id, device_row)
            if col_val:
                ud4_value = col_val.text
                self.utils.print_info(f"Returning User Data 4 '{ud4_value}' for device {device_ip}")
                ret_val = ud4_value
            else:
                self.utils.print_info(f"Unable to determine User Data 4 for device {device_ip}")
        else:
            self.utils.print_info(f"Unable to find row for device with IP {device_ip}")

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_get_device_notes(self, device_ip):
        """
        - This keyword is used to get the Notes value for the specified device in the devices table.
        - It is assumed the Network> Devices> Devices tab is already selected.
        - Keyword Usage:
         - ``XIQSE Get Device Notes    ${DEVICE_IP}``

        :param device_ip: device IP to get the value for
        :return: notes for the specified device;  empty string ("") if value cannot be determined
        """
        ret_val = ""

        device_row = self.xiqse_get_device_row(device_ip)
        if device_row:
            the_col = self.get_device_column_by_name("Notes")
            col_id = self.view_el.get_column_id(the_col)
            self.utils.print_debug(f"Column ID: {col_id}")
            col_val = self.get_device_column_value(col_id, device_row)
            if col_val:
                notes_value = col_val.text
                self.utils.print_info(f"Returning Notes '{notes_value}' for device {device_ip}")
                ret_val = notes_value
            else:
                self.utils.print_info(f"Unable to determine Notes for device {device_ip}")
        else:
            self.utils.print_info(f"Unable to find row for device with IP {device_ip}")

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_get_device_column_value(self, device_ip, col_name):
        """
        - This keyword is used to get the desired column value for the specified device in the devices table.
        - It is assumed the Network> Devices> Devices tab is already selected.
        - Keyword Usage:
         - ``XIQSE Get Device Column Value    ${DEVICE_IP}    Admin Profile``
         - ``XIQSE Get Device Column Value    ${DEVICE_IP}    Site``

        :param device_ip: device IP to get the value for
        :param col_name:  name of the column to get the value of
        :return: desired column value for the specified device;  empty string ("") if value cannot be determined
        """
        ret_val = ""

        device_row = self.xiqse_get_device_row(device_ip)
        if device_row:
            the_col = self.get_device_column_by_name(col_name)
            col_id = self.view_el.get_column_id(the_col)
            self.utils.print_debug(f"Column ID for {col_name}: {col_id}")
            col_val = self.get_device_column_value(col_id, device_row)
            if col_val:
                if col_name == "Archived" or col_name == "XIQ Onboarded" or col_name == "Stats":
                    the_value = col_val.get_attribute("data-qtip")
                else:
                    the_value = col_val.text
                self.utils.print_info(f"Returning {col_name} value '{the_value}' for device {device_ip}")
                ret_val = the_value
            else:
                self.utils.print_info(f"Unable to determine {col_name} value for device {device_ip}")
        else:
            self.utils.print_info(f"Unable to find row for device with IP {device_ip}")

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_get_device_row_values(self, device_ip, col_list):
        """
        - Gets a dictionary of device row values based on the passed column label list
        - The column list should be a comma-separated list of column headers, like Site,Admin Profile,Family
        - Keyword Usage:
         - ``@{DEVICE_VALUES}=  XIQSE Get Device Row Values   ${DEVICE_IP}  Site,Admin Profile,Family``

        :param device_ip: IP address of the device to obtain the values for
        :param col_list: comma-separated list of column headers to obtain the values of (e.g., Site,Admin Profile,Family)
        :return: dictionary containing the values for each of the specified columns
        """
        device_detail_dict = dict()

        stale_retry = 1
        while stale_retry <= 10:
            try:
                device_row = self.xiqse_get_device_row(device_ip)
                if device_row:
                    col_labels = col_list.split(",")
                    for label_str in col_labels:
                        self.utils.print_debug(f"Getting Data For Column {label_str}")
                        the_col = self.get_device_column_by_name(label_str)
                        col_id = self.view_el.get_column_id(the_col)
                        self.utils.print_debug(f"Column ID for {label_str}: {col_id}")
                        col_value = self.get_device_column_value(col_id, device_row)
                        if col_value:
                            self.utils.print_debug(f"Got column value '{col_value.text}' for column '{label_str}'")
                            device_detail_dict[label_str] = col_value.text
                        else:
                            self.utils.print_info(f"Unable to get column value for column '{label_str}'")
                            self.utils.print_info(f"  - column id value was '{col_id}'")
                            device_detail_dict[label_str] = ""
                    # Break out of the Stale Element Exception loop
                    break
                else:
                    self.utils.print_info(f"Unable to obtain row for device with IP '{device_ip}'")
                    # Break out of the Stale Element Exception loop
                    break
            except StaleElementReferenceException:
                self.utils.print_info(f"Handling StaleElementReferenceException - loop {stale_retry}")
                stale_retry = stale_retry + 1

        self.utils.print_info(f"****************** DEVICE ROW VALUES ************************")
        for key, value in device_detail_dict.items():
            self.utils.print_info(f"{key}:{value}")

        return device_detail_dict

    def xiqse_devices_show_columns(self, *columns):
        """
        - This keyword shows the specified list of columns if they are currently hidden.
        - Assumes already navigated to the Network> Devices> Devices view.
        -  Keyword Usage:
         - ``XIQSE Devices Show Columns        Admin Profile  Context``

        :param columns: list of columns to show
        :return: returns 1 if successful. else -1
        """
        ret_val = -1

        self.utils.print_debug("Getting Status column header")
        stat_col = self.get_devices_status_column_header()
        if stat_col:
            ret_val = self.xiqse_table.xiqse_table_show_columns(stat_col, *columns)
        else:
            self.utils.print_info("Could not find Status column")
            self.screen.save_screen_shot()

        self.utils.print_info("Closing Column Selection Menu")
        self.devices_tab.xiqse_devices_select_devices_tab()

        return ret_val

    def xiqse_devices_hide_columns(self, *columns):
        """
        - This keyword hides the specified list of columns if they are currently shown.
        - Assumes already navigated to the Network> Devices> Devices view.
        -  Keyword Usage:
         - ``XIQSE Devices Hide Columns        Admin Profile  Context``

        :param columns: list of columns to hide
        :return: returns 1 if successful. else -1
        """
        ret_val = -1

        self.utils.print_debug("Getting Status column header")
        stat_col = self.get_devices_status_column_header()
        if stat_col:
            ret_val = self.xiqse_table.xiqse_table_hide_columns(stat_col, *columns)
        else:
            self.utils.print_info("Could not find Status column")
            self.screen.save_screen_shot()

        self.utils.print_info("Closing Column Selection Menu")
        self.auto_actions.click(self.devices_tab.xiqse_devices_select_devices_tab())

        return ret_val

    def xiqse_devices_refresh_table(self):
        """
         - This keyword clicks the refresh icon under the table.
         - Keyword Usage
          - ``XIQSE Devices Refresh Table``

        :return: 1 if action was successful, else -1
        """
        return self.xiqse_table.xiqse_refresh_table()

    def xiqse_device_select_backup_configuration(self, device_ip):
        """
         - This keyword selects Backup Configuration for the specified device.
         - It is assumed the user is already on the Network> Devices> Devices tab.
         - Keyword Usage
          - ``XIQSE Device Select Backup Configuration  1.2.3.4``

        :param device_ip:    IP address of the device to select backup config on
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        if self.xiqse_select_device(device_ip) == 1:
            menu_btn = self.get_device_menu_tb_button()
            if menu_btn:
                self.utils.print_info("Clicking Device Menu toolbar button")
                self.auto_actions.click(menu_btn)
                sleep(1)

                archives_menu = self.get_archives_menu_item()
                if archives_menu:
                    self.utils.print_info("Clicking 'Archives' menu")
                    self.auto_actions.click(archives_menu)
                    sleep(1)

                    backup_config_menu = self.get_backup_configuration_menu_item()
                    if backup_config_menu:
                        self.utils.print_info("Clicking 'Backup Configuration' menu")
                        self.auto_actions.click(backup_config_menu)
                        sleep(2)

                        # Confirm the backup of the device
                        if self.backup_config_dlg.xiqse_confirm_backup_configuration_click_yes() == 1:
                            sleep(2)
                            ret_val = self.backup_config_dlg.xiqse_confirm_backup_configuration_click_ok()
                        else:
                            self.utils.print_info("Unable to click Yes button")
                            self.screen.save_screen_shot()
                    else:
                        self.utils.print_info("Unable to find Backup Configuration menu")
                        self.screen.save_screen_shot()
                else:
                    self.utils.print_info("Unable to find Archives menu")
                    self.screen.save_screen_shot()
            else:
                self.utils.print_info("Unable to find device menu toolbar")
                self.screen.save_screen_shot()
        else:
            self.utils.print_info("Unable to select device")
            self.screen.save_screen_shot()
        return ret_val

    def xiqse_device_select_restore_configuration(self, device_ip):
        """
         - This keyword selects Restore Configuration for the specified device.
         - It is assumed the user is already on the Network> Devices> Devices tab.
         - Keyword Usage
          - ``XIQSE Device Select Restore Configuration  1.2.3.4``

        :param device_ip:    IP address of the device to select restore config on
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        if self.xiqse_select_device(device_ip) == 1:
            menu_btn = self.get_device_menu_tb_button()
            if menu_btn:
                self.utils.print_info("Clicking Device Menu toolbar button")
                self.auto_actions.click(menu_btn)
                sleep(1)

                archives_menu = self.get_archives_menu_item()
                if archives_menu:
                    self.utils.print_info("Clicking 'Archives' menu")
                    self.auto_actions.click(archives_menu)
                    sleep(1)

                    restore_config_menu = self.get_restore_configuration_menu_item()
                    if restore_config_menu:
                        self.utils.print_info("Clicking 'Restore Configuration' menu")
                        self.auto_actions.click(restore_config_menu)
                        sleep(2)
                        ret_val = 1
                    else:
                        self.utils.print_info("Unable to find Restore Configuration menu")
                        self.screen.save_screen_shot()
                else:
                    self.utils.print_info("Unable to find Archives menu")
                    self.screen.save_screen_shot()
            else:
                self.utils.print_info("Unable to find Device menu button")
                self.screen.save_screen_shot()
        else:
            self.utils.print_info("Unable to select device")
            self.screen.save_screen_shot()
        return ret_val

    def xiqse_device_restore_configuration(self, device_ip, the_value):
        """
         - This keyword selects Restore Configuration and the configuration to restore for the specified device.
         - It is assumed the user is already on the Network> Devices> Devices tab.
         - Keyword Usage
          - ``XIQSE Device Select Restore Configuration  1.2.3.4  the_value``

        :param device_ip:    IP address of the device to select restore config on
        :param the_value:    Selects the configuration file
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        if self.xiqse_device_select_restore_configuration(device_ip) == 1:

            ret_val = self.restore_config_dlg.xiqse_set_restore_dialog_select_configuration(the_value)
            sleep(2)
            if ret_val == 1:
                # Confirm the start of the restore of the device
                if self.restore_config_dlg.xiqse_confirm_restore_dialog_click_start() == 1:
                    sleep(2)
                    # Confirm clicking the Yes button
                    if self.restore_config_dlg.xiqse_confirm_restore_dialog_click_yes() == 1:
                        sleep(2)
                        # Confirm clicking the OK button
                        ret_val = self.restore_config_dlg.xiqse_confirm_restore_dialog_click_ok()
                    else:
                        self.utils.print_info("Unable to select Yes button")
                        self.screen.save_screen_shot()
                else:
                    self.utils.print_info("Unable to select Start button")
                    self.screen.save_screen_shot()
            else:
                self.utils.print_info("Unable to select configuration from list")
                self.screen.save_screen_shot()
        else:
            self.utils.print_info("Unable to select Restore Configuration off device")
            self.screen.save_screen_shot()
        return ret_val

    def xiqse_register_trap_receiver(self, device_ip):
        """
         - This keyword registers the trap receiver for the currently-selected device.
         - It is assumed the user is already on the Network> Devices> Devices tab and the device to register is selected.
         - Keyword Usage
          - ``XIQSE Register Trap Receiver    ${DEVICE_IP}``

        :param  device_ip:    IP address of the device to select register trap receiver on
        :return: 1 if action was successful, else -1
        """
        ret_val = 1

        if self.xiqse_select_device(device_ip) == 1:
            menu_btn = self.get_device_menu_tb_button()
            if menu_btn:
                self.utils.print_info("Clicking Device Menu toolbar button")
                self.auto_actions.click(menu_btn)
                sleep(1)

                more_menu = self.get_more_actions_menu_item()
                if more_menu:
                    self.utils.print_info("Clicking 'More Actions' menu")
                    self.auto_actions.click(more_menu)
                    sleep(1)

                    register_trap_menu = self.get_register_trap_receiver_menu_item()
                    if register_trap_menu:
                        self.utils.print_info("Clicking 'Register Trap Receiver' menu")
                        self.auto_actions.click(register_trap_menu)
                        sleep(5)
                        return 1
                    else:
                        self.utils.print_info("Unable to find Register Trap Receiver menu")
                        self.screen.save_screen_shot()
                else:
                    self.utils.print_info("Unable to find More Actions menu")
                    self.screen.save_screen_shot()
            else:
                self.utils.print_info("Unable to find Device Menu toolbar button")
                self.screen.save_screen_shot()
        else:
            self.utils.print_info("Unable to select device")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_unregister_trap_receiver(self, device_ip):
        """
         - This keyword unregisters the trap receiver for the currently-selected device.
         - It is assumed the user is already on the Network> Devices> Devices tab and the device to unregister is selected.
         - Keyword Usage
          - ``XIQSE Unregister Trap Receiver  ${DEVICE_IP}``

        :param  device_ip:    IP address of the device to select unregister trap receiver on
        :return: 1 if action was successful, else -1
        """
        ret_val = 1

        if self.xiqse_select_device(device_ip) == 1:
            menu_btn = self.get_device_menu_tb_button()
            if menu_btn:
                self.utils.print_info("Clicking Device Menu toolbar button")
                self.auto_actions.click(menu_btn)
                sleep(1)

                more_menu = self.get_more_actions_menu_item()
                if more_menu:
                    self.utils.print_info("Clicking 'More Actions' menu")
                    self.auto_actions.click(more_menu)
                    sleep(1)

                    unregister_trap_menu = self.get_unregister_trap_receiver_menu_item()
                    if unregister_trap_menu:
                        self.utils.print_info("Clicking 'Unregister Trap Receiver' menu")
                        self.auto_actions.click(unregister_trap_menu)
                        sleep(5)
                        return 1
                    else:
                        self.utils.print_info("Unable to find Unregister Trap Receiver menu")
                        self.screen.save_screen_shot()
                else:
                    self.utils.print_info("Unable to find More Actions menu")
                    self.screen.save_screen_shot()
            else:
                self.utils.print_info("Unable to find Device Menu toolbar button")
                self.screen.save_screen_shot()
        else:
            self.utils.print_info("Unable to select device")
            self.screen.save_screen_shot()
        return ret_val

    def xiqse_register_syslog_receiver(self, device_ip):
        """
         - This keyword registers the syslog receiver for the currently-selected device.
         - It is assumed the user is already on the Network> Devices> Devices tab and the device to register is selected.
         - Keyword Usage
          - ``XIQSE Register Syslog Receiver  ${DEVICE_IP}``

        :param  device_ip:    IP address of the device to select register syslog receiver on
        :return: 1 if action was successful, else -1
        """
        ret_val = 1

        if self.xiqse_select_device(device_ip) == 1:
            menu_btn = self.get_device_menu_tb_button()
            if menu_btn:
                self.utils.print_info("Clicking Device Menu toolbar button")
                self.auto_actions.click(menu_btn)
                sleep(1)

                more_menu = self.get_more_actions_menu_item()
                if more_menu:
                    self.utils.print_info("Clicking 'More Actions' menu")
                    self.auto_actions.click(more_menu)
                    sleep(1)

                    register_syslog_menu = self.get_register_syslog_receiver_menu_item()
                    if register_syslog_menu:
                        self.utils.print_info("Clicking 'Register SysLog Receiver' menu")
                        self.auto_actions.click(register_syslog_menu)
                        sleep(5)
                        return 1
                    else:
                        self.utils.print_info("Unable to find Register SysLog Receiver menu")
                        self.screen.save_screen_shot()
                else:
                    self.utils.print_info("Unable to find More Actions menu")
                    self.screen.save_screen_shot()
            else:
                self.utils.print_info("Unable to find Device Menu toolbar button")
                self.screen.save_screen_shot()
        else:
            self.utils.print_info("Unable to select device")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_unregister_syslog_receiver(self, device_ip):
        """
         - This keyword unregisters the syslog receiver for the currently-selected device.
         - It is assumed the user is already on the Network> Devices> Devices tab and the device to unregister is selected.
         - Keyword Usage
          - ``XIQSE Unregister Syslog Receiver  ${DEVICE_IP}``

        :param  device_ip:    IP address of the device to select unregister syslog receiver on
        :return: 1 if action was successful, else -1
        """
        ret_val = 1

        if self.xiqse_select_device(device_ip) == 1:
            menu_btn = self.get_device_menu_tb_button()
            if menu_btn:
                self.utils.print_info("Clicking Device Menu toolbar button")
                self.auto_actions.click(menu_btn)
                sleep(1)

                more_menu = self.get_more_actions_menu_item()
                if more_menu:
                    self.utils.print_info("Clicking 'More Actions' menu")
                    self.auto_actions.click(more_menu)
                    sleep(1)

                    unregister_syslog_menu = self.get_unregister_syslog_receiver_menu_item()
                    if unregister_syslog_menu:
                        self.utils.print_info("Clicking 'Unregister SysLog Receiver' menu")
                        self.auto_actions.click(unregister_syslog_menu)
                        sleep(5)
                        return 1
                    else:
                        self.utils.print_info("Unable to find Unregister SysLog Receiver menu")
                        self.screen.save_screen_shot()
                else:
                    self.utils.print_info("Unable to find More Actions menu")
                    self.screen.save_screen_shot()
            else:
                self.utils.print_info("Unable to find Device Menu toolbar button")
                self.screen.save_screen_shot()
        else:
            self.utils.print_info("Unable to select device")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_devices_open_search(self):
        """
         - This keyword opens the search box in the Network> Devices view
         - Keyword Usage
          - ``XIQSE Devices Open Search``

        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        search_btn = self.get_search_open_button()
        search_text = self.get_search_text_field()
        if search_btn:
            if search_text and search_text.get_attribute("aria-hidden") == "true":
                self.utils.print_info(f"Clicking Search button")
                self.auto_actions.click(search_btn)
                sleep(2)
            else:
                self.utils.print_info(f"Search field already open")
            ret_val = 1
        else:
            self.utils.print_info("Unable to find the Search button")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_devices_enter_search_text(self, value):
        """
         - This keyword enters text into the search field in the Network> Devices view
         - Keyword Usage
          - ``XIQSE Devices Enter Search Text    My Device To Find``

        :param value: string to enter in the search box
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        search_text = self.get_search_text_field()
        if search_text:
            if search_text.get_attribute("aria-hidden") == "false":
                self.utils.print_info(f"Entering {value} into search box")
                self.auto_actions.send_keys(search_text, value)
                ret_val = 1
            else:
                self.utils.print_info("Search text field is currently hidden")
                self.screen.save_screen_shot()
        else:
            self.utils.print_info("Unable to find the Search text field")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_devices_trigger_search(self):
        """
         - This keyword clicks the search button in the search box in the Network> Devices view to perform the search
         - Keyword Usage
          - ``XIQSE Devices Trigger Search``

        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        search_btn = self.get_search_trigger_button()
        search_text = self.get_search_text_field()
        if search_btn:
            if search_text and search_text.get_attribute("aria-hidden") == "false":
                self.utils.print_info(f"Clicking Search button to perform the search")
                self.auto_actions.click(search_btn)
                ret_val = 1
            else:
                self.utils.print_info(f"Search field not open")
                self.screen.save_screen_shot()
        else:
            self.utils.print_info("Unable to find the Search button to perform the search")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_devices_clear_search(self):
        """
         - This keyword clicks the clear button in the search box in the Network> Devices view
         - Keyword Usage
          - ``XIQSE Events Clear Search``

        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        clear_btn = self.get_search_clear_button()
        search_text = self.get_search_text_field()
        if clear_btn:
            if search_text and search_text.get_attribute("aria-hidden") == "false":
                self.utils.print_info(f"Clicking Clear button")
                self.auto_actions.click(clear_btn)
                ret_val = 1
            else:
                self.utils.print_info(f"Search field not open")
                self.screen.save_screen_shot()
        else:
            self.utils.print_info("Unable to find the Clear button")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_devices_wait_for_search_to_complete(self, retry_duration=10, retry_count=30):
        """
         - This keyword waits for the search to complete in the Network> Devices view
         - Keyword Usage
          - ``XIQSE Devices Wait For Search To Complete``

        :param retry_duration: amount of time to wait in between each check for the search to be complete
        :param retry_count:    number of times to check for the search to be complete
        :return: 1 if action was successful, else -1
        """
        count = 1
        while count <= retry_count:
            self.utils.print_info(f"Waiting for search to complete: loop {count}")
            load_mask = self.view_el.get_load_mask()
            if load_mask:
                self.utils.print_info(f"Search still in progress...")
                sleep(retry_duration)
            else:
                self.utils.print_info(f"Search has completed")
                return 1
            count += 1

        return -1

    def xiqse_devices_perform_search(self, value, retry_duration=10, retry_count=30):
        """
         - This keyword performs a search in the Network> Devices view
         - Keyword Usage
          - ``XIQSE Devices Perform Search   My Search String``
          - ``XIQSE Devices Perform Search   My Search String  retry_duration=5  retry_count=10``

        :param value:          string to search for
        :param retry_duration: amount of time to wait in between each check for the search to be complete
        :param retry_count:    number of times to check for the search to be complete
        :return: 1 if action was successful, else -1
        """
        ret_val = -1
        if self.xiqse_devices_open_search() == 1:
            if self.xiqse_devices_enter_search_text(value) == 1:
                if self.xiqse_devices_trigger_search() == 1:
                    if self.xiqse_devices_wait_for_search_to_complete(retry_duration, retry_count) == 1:
                        ret_val = 1
                        self.utils.print_info(f"Completed search for {value}")

        if ret_val == -1:
            self.utils.print_info(f"Unable to perform search for {value}")

        return ret_val

    def xiqse_perform_restart_device(self, device_ip):
        """
         - This keyword restarts the specified device.
         - It is assumed the user is already on the Network> Devices> Devices tab
         - Keyword Usage
          - ``XIQSE Perform Restart Device    ${DEVICE_IP}``

        :param  device_ip:    IP address of the device to restart
        :return: 1 if action was successful, else -1
        """

        ret_val = self.xiqse_restart_device(device_ip)
        if ret_val != -1:
            ret_val = self.restart_device.xiqse_click_start_restart_button()
            if ret_val != -1:
                ret_val = self.restart_device.xiqse_click_start_restart_yes_button()
                if ret_val != -1:
                    ret_val = self.restart_device.xiqse_click_restart_devices_close_button()
        if ret_val == -1:
            self.utils.print_info("Unable to perform restart device")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_confirm_table_empty(self):
        """
        - This keyword confirms there are no devices in the Devices table.
         - Keyword Usage
          - ``XIQSE Confirm Table Empty``
        :return: returns 1 if table is empty, else -1
        """
        ret_val = 1

        rows = self.get_table_rows()
        if rows:
            self.utils.print_info("Table is not empty")
            return -1
        else:
            self.utils.print_info("Table is empty")
            return 1

        return ret_val

    def xiqse_get_trap_status(self, device_ip):
        """
        - This keyword is used to get the trap status for the specified device in the devices table.
        - It is assumed the Network> Devices> Devices tab is already selected.
        - Keyword Usage:
         - ``XIQSE Get Trap Status    ${DEVICE_IP}``

        :param device_ip: device IP to look for
        :param trap_status: expected value of the trap status
        :return: trap status for the specified device;  empty string ("") if trap status cannot be determined
        """
        ret_val = ""

        device_row = self.xiqse_get_device_row(device_ip)
        if device_row:
            the_col = self.get_device_column_by_name("Trap Status")
            col_id = self.view_el.get_column_id(the_col)
            self.utils.print_debug(f"Column ID: {col_id}")
            if col_id != -1:
                col_val = self.get_device_column_value(col_id, device_row)
                if col_val:
                    status_value = col_val.text
                    self.utils.print_info(f"Returning Trap Status {status_value} for device {device_ip}")
                    ret_val = status_value
                else:
                    self.utils.print_info(f"Unable to determine trap status for device {device_ip}")
            else:
                self.utils.print_info("Unable to find column ID for Trap Status column")
        else:
            self.utils.print_info(f"Unable to find row for device with IP {device_ip}")

        self.utils.print_info(f"Returning trap status {ret_val} for device {device_ip}")
        self.screen.save_screen_shot()

        return ret_val

    def xiqse_get_syslog_status(self, device_ip):
        """
        - This keyword is used to get the syslog status for the specified device in the devices table.
        - It is assumed the Network> Devices> Devices tab is already selected.
        - Keyword Usage:
         - ``XIQSE Get Syslog Status    ${DEVICE_IP}``

        :param device_ip: device IP to look for
        :param syslog_status: expected value of the trap status
        :return: syslog status for the specified device;  empty string ("") if syslog status cannot be determined
        """
        ret_val = ""

        device_row = self.xiqse_get_device_row(device_ip)
        if device_row:
            the_col = self.get_device_column_by_name("Syslog Status")
            col_id = self.view_el.get_column_id(the_col)
            self.utils.print_debug(f"Column ID: {col_id}")
            if col_id != -1:
                col_val = self.get_device_column_value(col_id, device_row)
                if col_val:
                    status_value = col_val.text
                    self.utils.print_info(f"Returning Syslog Status {status_value} for device {device_ip}")
                    ret_val = status_value
                else:
                    self.utils.print_info(f"Unable to determine syslog status for device {device_ip}")
            else:
                self.utils.print_info("Unable to find column ID for Syslog Status column")
        else:
            self.utils.print_info(f"Unable to find row for device with IP {device_ip}")

        self.utils.print_info(f"Returning syslog status {ret_val} for device {device_ip}")
        self.screen.save_screen_shot()

        return ret_val

    def xiqse_get_device_license(self, device_ip):
        """
        - This keyword is used to get the device license for the specified device in the devices table.
        - It is assumed the Network> Devices> Devices tab is already selected.
        - Keyword Usage:
         - ``XIQSE Get Device License    ${DEVICE_IP}``

        :param device_ip: device IP to look for
        :return: device license for the specified device;  empty string ("") if device license cannot be determined
        """
        ret_val = ""

        device_row = self.xiqse_get_device_row(device_ip)
        if device_row:
            the_col = self.get_device_column_by_name("License")
            col_id = self.view_el.get_column_id(the_col)
            self.utils.print_debug(f"Column ID: {col_id}")
            if col_id != -1:
                col_val = self.get_device_column_value(col_id, device_row)
                if col_val:
                    status_value = col_val.text
                    self.utils.print_info(f"Returning Device License {status_value} for device {device_ip}")
                    ret_val = status_value
                else:
                    self.utils.print_info(f"Unable to determine device license for device {device_ip}")
            else:
                self.utils.print_info("Unable to find column ID for License column")
        else:
            self.utils.print_info(f"Unable to find row for device with IP {device_ip}")

        self.utils.print_info(f"Returning device license {ret_val} for device {device_ip}")
        self.screen.save_screen_shot()

        return ret_val

    def xiqse_wait_until_device_stats_historical(self, device_ip, retry_duration=30, retry_count=10):
        """
        - This keyword is used to wait for the device to show it is collecting historical statistics.
        - This keyword by default loops 10 times every 30 seconds to check if the device is collecting historical statistics.
        - It is assumed the Network> Devices> Devices tab is already selected.
        - Keyword Usage:
         - ``XIQSE Wait Until Device Stats Historical    ${DEVICE_IP}    retry_duration=10    retry_count=12``

        :param device_ip: device IP to check the stats column on
        :param retry_duration: duration between each retry
        :param retry_count: retry count
        :return: 1 if device stats within specified time; else -1
        """
        ret_val = -1
        count = 1
        while count <= retry_count:
            self.utils.print_info(f"Device Stats Check - Loop: ", count)

            stale_retry = 1
            while stale_retry <= 10:
                try:
                    self.xiqse_table.xiqse_refresh_table()

                    is_stats = self.xiqse_get_device_column_value(device_ip, "Stats")
                    self.utils.print_info(f"Historical: '{is_stats}'")
                    if is_stats and is_stats == "Collecting Historical":
                        self.utils.print_info("Device is collecting historical statistics")
                        return 1
                    else:
                        self.utils.print_info(f"Device is not yet collecting. Waiting for {retry_duration} seconds...")
                        sleep(retry_duration)

                    # Break out of the Stale Element Exception loop
                    break
                except StaleElementReferenceException:
                    self.utils.print_info(f"Handling StaleElementReferenceException - loop {stale_retry}")
                    stale_retry = stale_retry + 1

            # Increment retry counter
            count += 1

        if ret_val == -1:
            self.utils.print_info(f"Device did not become archived within allocated time. Please check.")
            self.screen.save_screen_shot()

        return ret_val
