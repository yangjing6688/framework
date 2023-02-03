# ----------------------------------------------------------------------
# Copyright (C) 2021... 2021 Extreme Networks Inc.
# This software is copyright protected and may not be reproduced in any
# form or fashion without the written consent of Extreme Networks Inc.
# ----------------------------------------------------------------------
#
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from xiqse.elements.common.CommonViewWebElements import CommonViewWebElements
from xiqse.elements.network.common.configure_device.NetworkCommonConfigureDeviceDeviceWebElements import NetworkCommonConfigureDeviceDeviceWebElements
from xiqse.flows.network.common.configure_device.XIQSE_NetworkCommonConfigureDeviceImportSiteConfig import XIQSE_NetworkCommonConfigureDeviceImportSiteConfig
from xiqse.flows.network.common.XIQSE_NetworkCommonConfigureDevice import XIQSE_NetworkCommonConfigureDevice


class XIQSE_NetworkCommonConfigureDeviceDevice(NetworkCommonConfigureDeviceDeviceWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.view_el = CommonViewWebElements()
        self.import_site_dlg = XIQSE_NetworkCommonConfigureDeviceImportSiteConfig()
        self.cfg_dev = XIQSE_NetworkCommonConfigureDevice()

    # DEVICE TAB
    def xiqse_configure_device_dialog_set_system_name(self, the_value):
        """
        - This keyword sets the System Name field in the Configure Device dialog (Device tab).
        - It assumes the dialog is already open.
        - Keyword Usage:
        - ``XIQSE Configure Device Dialog Set System Name  My_System_Name``

        :param the_value: Value to enter into the field
        :return: 1 if action is successful, else -1
        """
        ret_val = -1

        the_field = self.get_system_name_field()
        if the_field:
            self.utils.print_info(f"Entering '{the_value}' for the System Name field in the Configure Device dialog")
            self.auto_actions.send_keys(the_field, the_value)
            ret_val = 1
        else:
            self.utils.print_info("Unable to find the System Name field in the Configure Device dialog")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_configure_device_dialog_set_contact(self, the_value):
        """
        - This keyword sets the Contact field in the Configure Device dialog (Device tab).
        - It assumes the dialog is already open.
        - Keyword Usage:
        - ``XIQSE Configure Device Dialog Set Contact  Contact Person``

        :param the_value: Value to enter into the field
        :return: 1 if action is successful, else -1
        """
        ret_val = -1

        the_field = self.get_contact_field()
        if the_field:
            self.utils.print_info(f"Entering '{the_value}' for the Contact field in the Configure Device dialog")
            self.auto_actions.send_keys(the_field, the_value)
            ret_val = 1
        else:
            self.utils.print_info("Unable to find the Contact field in the Configure Device dialog")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_configure_device_dialog_set_location(self, the_value):
        """
        - This keyword sets the Location field in the Configure Device dialog (Device tab).
        - It assumes the dialog is already open.
        - Keyword Usage:
        - ``XIQSE Configure Device Dialog Set Location  My Location``

        :param the_value: Value to enter into the field
        :return: 1 if action is successful, else -1
        """
        ret_val = -1

        the_field = self.get_location_field()
        if the_field:
            self.utils.print_info(f"Entering '{the_value}' for the Location field in the Configure Device dialog")
            self.auto_actions.send_keys(the_field, the_value)
            ret_val = 1
        else:
            self.utils.print_info("Unable to find the Location field in the Configure Device dialog")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_configure_device_dialog_set_admin_profile(self, the_value):
        """
        - This keyword sets the Administration Profile field in the Configure Device dialog (Device tab).
        - It assumes the dialog is already open.
        - Keyword Usage:
        - ``XIQSE Configure Device Dialog Set Admin Profile  public_v2_Profile``

        :param the_value: Value to enter into the field
        :return: 1 if action is successful, else -1
        """
        ret_val = -1

        the_field = self.get_admin_profile_dropdown()
        if the_field:
            self.utils.print_info("Opening the Administration Profile dropdown")
            self.auto_actions.click(the_field)

            # Obtain the dropdown items
            the_id = self.view_el.get_dropdown_id(the_field)
            self.utils.print_debug(f"Got dropdown ID {the_id}")
            the_items = self.view_el.get_div_dropdown_items(the_id)
            if the_items:
                if self.auto_actions.select_drop_down_options(the_items, the_value):
                    self.utils.print_info(f"Selected profile {the_value} in the Administration Profile dropdown")
                    ret_val = 1
                else:
                    self.utils.print_info(f"Did not find profile {the_value} in the Administration Profile dropdown")
                    self.screen.save_screen_shot()

                    # Click the dropdown again to close it
                    self.auto_actions.click(the_field)
            else:
                self.utils.print_info("Unable to get the Administration Profile dropdown items")
                self.screen.save_screen_shot()

                # Click the dropdown again to close it
                self.auto_actions.click(the_field)
        else:
            self.utils.print_info("Unable to find the Administration Profile dropdown in the Configure Device dialog")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_configure_device_dialog_set_replacement_serial(self, the_value):
        """
        - This keyword sets the Replacement Serial Number field in the Configure Device dialog (Device tab).
        - It assumes the dialog is already open.
        - Keyword Usage:
        - ``XIQSE Configure Device Dialog Set Replacement Serial  Abc123xyZ``

        :param the_value: Value to enter into the field
        :return: 1 if action is successful, else -1
        """
        ret_val = -1

        the_field = self.get_replacement_serial_field()
        if the_field:
            self.utils.print_info(f"Entering '{the_value}' for the Replacement Serial Number field in the Configure Device dialog")
            self.auto_actions.send_keys(the_field, the_value)
            ret_val = 1
        else:
            self.utils.print_info("Unable to find the Replacement Serial Number field in the Configure Device dialog")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_configure_device_dialog_enable_remove_from_service(self):
        """
        - This keyword enables the Remove From Service checkbox in the Configure Device dialog (Device tab).
        - It assumes the dialog is already open.
        - Keyword Usage:
        - ``XIQSE Configure Device Dialog Enable Remove From Service``

        :return: 1 if action is successful, else -1
        """
        ret_val = -1

        the_field = self.get_remove_from_service_checkbox()
        if the_field:
            self.utils.print_info("Enabling the Remove from Service checkbox in the Configure Device dialog")
            self.auto_actions.enable_check_box(the_field)
            ret_val = 1
        else:
            self.utils.print_info("Unable to find the Remove from Service checkbox in the Configure Device dialog")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_configure_device_dialog_disable_remove_from_service(self):
        """
        - This keyword disables the Remove From Service checkbox in the Configure Device dialog (Device tab).
        - It assumes the dialog is already open.
        - Keyword Usage:
        - ``XIQSE Configure Device Dialog Disable Remove From Service``

        :return: 1 if action is successful, else -1
        """
        ret_val = -1

        the_field = self.get_remove_from_service_checkbox()
        if the_field:
            self.utils.print_info("Disabling the Remove from Service checkbox in the Configure Device dialog")
            self.auto_actions.disable_check_box(the_field)
            ret_val = 1
        else:
            self.utils.print_info("Unable to find the Remove from Service checkbox in the Configure Device dialog")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_configure_device_dialog_enable_use_default_webview_url(self):
        """
        - This keyword enables the Use Default WebView URL checkbox in the Configure Device dialog (Device tab).
        - It assumes the dialog is already open.
        - Keyword Usage:
        - ``XIQSE Configure Device Dialog Enable Use Default WebView URL``

        :return: 1 if action is successful, else -1
        """
        ret_val = -1

        the_field = self.get_use_default_webview_url_checkbox()
        if the_field:
            self.utils.print_info("Enabling the Use Default WebView URL checkbox in the Configure Device dialog")
            self.auto_actions.enable_check_box(the_field)
            ret_val = 1
        else:
            self.utils.print_info("Unable to find the Use Default WebView URL checkbox in the Configure Device dialog")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_configure_device_dialog_disable_use_default_webview_url(self):
        """
        - This keyword disables the Use Default WebView URL checkbox in the Configure Device dialog (Device tab).
        - It assumes the dialog is already open.
        - Keyword Usage:
        - ``XIQSE Configure Device Dialog Disable Use Default WebView URL``

        :return: 1 if action is successful, else -1
        """
        ret_val = -1

        the_field = self.get_use_default_webview_url_checkbox()
        if the_field:
            self.utils.print_info("Disabling the Use Default WebView URL checkbox in the Configure Device dialog")
            self.auto_actions.disable_check_box(the_field)
            ret_val = 1
        else:
            self.utils.print_info("Unable to find the Use Default WebView URL checkbox in the Configure Device dialog")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_configure_device_dialog_set_webview_url(self, the_value):
        """
        - This keyword sets the WebView URL field in the Configure Device dialog (Device tab).
        - It assumes the dialog is already open.
        - Keyword Usage:
        - ``XIQSE Configure Device Dialog Set WebView URL  http://%IP``

        :param the_value: Value to enter into the field
        :return: 1 if action is successful, else -1
        """
        ret_val = -1

        the_field = self.get_webview_url_field()
        if the_field:
            if the_field.is_enabled():
                self.utils.print_info(f"Entering '{the_value}' for the WebView URL field in the Configure Device dialog")
                self.auto_actions.send_keys(the_field, the_value)
                ret_val = 1
            else:
                self.utils.print_info("WebView URL field is disabled - check the state of the Use Default WebView URL checkbox")
                self.screen.save_screen_shot()
        else:
            self.utils.print_info("Unable to find the WebView URL field in the Configure Device dialog")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_configure_device_dialog_set_default_site(self, the_value, import_site="No"):
        """
        - This keyword sets the Default Site field in the Configure Device dialog (Device tab).
        - It assumes the dialog is already open.
        - Keyword Usage:
        - ``XIQSE Configure Device Dialog Set Default Site  /World``

        :param the_value: Value to enter into the field
        :param import_site: Indicates whether to answer yes or no in the Import Site Configuration dialog (Yes/No)
        :return: 1 if action is successful, else -1
        """
        ret_val = -1

        the_field = self.get_default_site_dropdown()
        if the_field:
            self.utils.print_info("Opening the Default Site dropdown")
            self.auto_actions.click(the_field)

            # Obtain the dropdown items
            the_id = self.view_el.get_dropdown_id(the_field)
            self.utils.print_debug(f"Got dropdown ID {the_id}")
            the_items = self.view_el.get_list_dropdown_items(the_id)
            if the_items:
                if self.auto_actions.select_drop_down_options_partial_match(the_items, the_value):
                    self.utils.print_info(f"Selected {the_value} in the Default Site dropdown")

                    # Answer the "Import Site Configuration" question
                    if self.import_site_dlg.xiqse_answer_import_site_configuration_question(import_site) != -1:
                        ret_val = 1
                else:
                    self.utils.print_info(f"Did not find {the_value} in the Default Site dropdown")
                    self.screen.save_screen_shot()

                    # Click the dropdown again to close it
                    self.auto_actions.click(the_field)
            else:
                self.utils.print_info("Unable to get the Default Site dropdown items")
                self.screen.save_screen_shot()

                # Click the dropdown again to close it
                self.auto_actions.click(the_field)
        else:
            self.utils.print_info("Unable to find the Default Site dropdown in the Configure Device dialog")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_configure_device_dialog_set_poll_group(self, the_value):
        """
        - This keyword sets the Poll Group field in the Configure Device dialog (Device tab).
        - It assumes the dialog is already open.
        - Keyword Usage:
        - ``XIQSE Configure Device Dialog Set Poll Group  Default``
        - ``XIQSE Configure Device Dialog Set Poll Group  More Frequent``
        - ``XIQSE Configure Device Dialog Set Poll Group  Less Frequent``

        :param the_value: Value to enter into the field
        :return: 1 if action is successful, else -1
        """
        ret_val = -1

        the_field = self.get_poll_group_dropdown()
        if the_field:
            self.utils.print_info("Opening the Poll Group dropdown")
            self.auto_actions.click(the_field)

            # Obtain the dropdown items
            the_id = self.view_el.get_dropdown_id(the_field)
            self.utils.print_debug(f"Got dropdown ID {the_id}")
            the_items = self.view_el.get_list_dropdown_items(the_id)
            if the_items:
                if self.auto_actions.select_drop_down_options(the_items, the_value):
                    self.utils.print_info(f"Selected {the_value} in the Poll Group dropdown")
                    ret_val = 1
                else:
                    self.utils.print_info(f"Did not find {the_value} in the Poll Group dropdown")
                    self.screen.save_screen_shot()

                    # Click the dropdown again to close it
                    self.auto_actions.click(the_field)
            else:
                self.utils.print_info("Unable to get the Poll Group dropdown items")
                self.screen.save_screen_shot()

                # Click the dropdown again to close it
                self.auto_actions.click(the_field)
        else:
            self.utils.print_info("Unable to find the Poll Group dropdown in the Configure Device dialog")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_configure_device_dialog_set_poll_type(self, the_value):
        """
        - This keyword sets the Poll Type field in the Configure Device dialog (Device tab).
        - It assumes the dialog is already open.
        - Keyword Usage:
        - ``XIQSE Configure Device Dialog Set Poll Type  SNMP``
        - ``XIQSE Configure Device Dialog Set Poll Type  Ping``
        - ``XIQSE Configure Device Dialog Set Poll Type  Not Polled``
        - ``XIQSE Configure Device Dialog Set Poll Type  Maintenance``

        :param the_value: Value to enter into the field
        :return: 1 if action is successful, else -1
        """
        ret_val = -1

        the_field = self.get_poll_type_dropdown()
        if the_field:
            self.utils.print_info("Opening the Poll Type dropdown")
            self.auto_actions.click(the_field)

            # Obtain the dropdown items
            the_id = self.view_el.get_dropdown_id(the_field)
            self.utils.print_debug(f"Got dropdown ID {the_id}")
            the_items = self.view_el.get_list_dropdown_items(the_id)
            if the_items:
                if self.auto_actions.select_drop_down_options(the_items, the_value):
                    self.utils.print_info(f"Selected {the_value} in the Poll Type dropdown")
                    ret_val = 1
                else:
                    self.utils.print_info(f"Did not find {the_value} in the Poll Type dropdown")
                    self.screen.save_screen_shot()

                    # Click the dropdown again to close it
                    self.auto_actions.click(the_field)
            else:
                self.utils.print_info("Unable to get the Poll Type dropdown items")
                self.screen.save_screen_shot()

                # Click the dropdown again to close it
                self.auto_actions.click(the_field)
        else:
            self.utils.print_info("Unable to find the Poll Type dropdown in the Configure Device dialog")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_configure_device_dialog_set_snmp_timeout(self, the_value):
        """
        - This keyword sets the SNMP Timeout field in the Configure Device dialog (Device tab).
        - It assumes the dialog is already open.
        - Keyword Usage:
        - ``XIQSE Configure Device Dialog Set SNMP Timeout  5``

        :param the_value: Value to enter into the field
        :return: 1 if action is successful, else -1
        """
        ret_val = -1

        the_field = self.get_snmp_timeout_field()
        if the_field:
            self.utils.print_info(f"Entering '{the_value}' for the SNMP Timeout field in the Configure Device dialog")
            self.auto_actions.send_keys(the_field, the_value)
            ret_val = 1
        else:
            self.utils.print_info("Unable to find the SNMP Timeout field in the Configure Device dialog")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_configure_device_dialog_set_snmp_retries(self, the_value):
        """
        - This keyword sets the SNMP Retries field in the Configure Device dialog (Device tab).
        - It assumes the dialog is already open.
        - Keyword Usage:
        - ``XIQSE Configure Device Dialog Set SNMP Retries  3``

        :param the_value: Value to enter into the field
        :return: 1 if action is successful, else -1
        """
        ret_val = -1

        the_field = self.get_snmp_retries_field()
        if the_field:
            self.utils.print_info(f"Entering '{the_value}' for the SNMP Retries field in the Configure Device dialog")
            self.auto_actions.send_keys(the_field, the_value)
            ret_val = 1
        else:
            self.utils.print_info("Unable to find the SNMP Retries field in the Configure Device dialog")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_configure_device_dialog_set_topology_layer(self, the_value):
        """
        - This keyword sets the Topology Layer field in the Configure Device dialog (Device tab).
        - It assumes the dialog is already open.
        - Keyword Usage:
        - ``XIQSE Configure Device Dialog Set Topology Layer  L2 Access``
        - ``XIQSE Configure Device Dialog Set Topology Layer  L2 Leaf``
        - ``XIQSE Configure Device Dialog Set Topology Layer  L3 Access``
        - ``XIQSE Configure Device Dialog Set Topology Layer  L3 Leaf``
        - ``XIQSE Configure Device Dialog Set Topology Layer  L3 Spine``
        - ``XIQSE Configure Device Dialog Set Topology Layer  L3 Core``
        - ``XIQSE Configure Device Dialog Set Topology Layer  L3 Distribution``
        - ``XIQSE Configure Device Dialog Set Topology Layer  Firewall``
        - ``XIQSE Configure Device Dialog Set Topology Layer  Load Balancer``
        - ``XIQSE Configure Device Dialog Set Topology Layer  Gateway``
        - ``XIQSE Configure Device Dialog Set Topology Layer  WAN Access``
        - ``XIQSE Configure Device Dialog Set Topology Layer  Appliance``
        - ``XIQSE Configure Device Dialog Set Topology Layer  Server``
        - ``XIQSE Configure Device Dialog Set Topology Layer  Hypervisor Host``

        :param the_value: Value to enter into the field
        :return: 1 if action is successful, else -1
        """
        ret_val = -1

        the_field = self.get_topology_layer_dropdown()
        if the_field:
            self.utils.print_info("Opening the Topology Layer dropdown")
            self.auto_actions.click(the_field)

            # Obtain the dropdown items
            the_id = self.view_el.get_dropdown_id(the_field)
            self.utils.print_debug(f"Got dropdown ID {the_id}")
            the_items = self.view_el.get_list_dropdown_items(the_id)
            if the_items:
                if self.auto_actions.select_drop_down_options(the_items, the_value):
                    self.utils.print_info(f"Selected {the_value} in the Topology Layer dropdown")
                    ret_val = 1
                else:
                    self.utils.print_info(f"Did not find {the_value} in the Topology Layer dropdown")
                    self.screen.save_screen_shot()

                    # Click the dropdown again to close it
                    self.auto_actions.click(the_field)
            else:
                self.utils.print_info("Unable to get the Topology Layer dropdown items")
                self.screen.save_screen_shot()

                # Click the dropdown again to close it
                self.auto_actions.click(the_field)
        else:
            self.utils.print_info("Unable to find the Topology Layer dropdown in the Configure Device dialog")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_configure_device_dialog_set_collection_mode(self, the_value):
        """
        - This keyword sets the Collection Mode field in the Configure Device dialog (Device tab).
        - It assumes the dialog is already open.
        - Keyword Usage:
        - ``XIQSE Configure Device Dialog Set Collection Mode  Historical``
        - ``XIQSE Configure Device Dialog Set Collection Mode  Threshold Alarms``
        - ``XIQSE Configure Device Dialog Set Collection Mode  None``

        :param the_value: Value to enter into the field
        :return: 1 if action is successful, else -1
        """
        ret_val = -1

        # This dropdown is not opened by clicking on the input area, so need to get the dropdown trigger arrow
        the_field_trigger = self.get_collection_mode_dropdown_trigger()
        if the_field_trigger:
            self.utils.print_info("Opening the Collection Mode dropdown")
            self.auto_actions.click(the_field_trigger)

            # Obtain the dropdown items
            the_field = self.get_collection_mode_dropdown()
            the_id = self.view_el.get_dropdown_id(the_field)
            self.utils.print_debug(f"Got dropdown ID {the_id}")
            the_items = self.view_el.get_list_dropdown_items(the_id)
            if the_items:
                if self.auto_actions.select_drop_down_options(the_items, the_value):
                    self.utils.print_info(f"Selected {the_value} in the Collection Mode dropdown")
                    ret_val = 1
                else:
                    self.utils.print_info(f"Did not find {the_value} in the Collection Mode dropdown")
                    self.screen.save_screen_shot()

                    # Click the dropdown again to close it
                    self.auto_actions.click(the_field_trigger)
            else:
                self.utils.print_info("Unable to get the Collection Mode dropdown items")
                self.screen.save_screen_shot()

                # Click the dropdown again to close it
                self.auto_actions.click(the_field_trigger)
        else:
            self.utils.print_info("Unable to find the Collection Mode dropdown in the Configure Device dialog")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_configure_device_dialog_set_collection_interval(self, the_value):
        """
        - This keyword sets the Collection Interval field in the Configure Device dialog (Device tab).
        - It assumes the dialog is already open.
        - Keyword Usage:
        - ``XIQSE Configure Device Dialog Set Collection Interval  15``

        :param the_value: Value to enter into the field
        :return: 1 if action is successful, else -1
        """
        ret_val = -1

        the_field = self.get_collection_interval_field()
        if the_field:
            self.utils.print_info(f"Entering '{the_value}' for the Collection Interval field in the Configure Device dialog")
            self.auto_actions.send_keys(the_field, the_value)
            ret_val = 1
        else:
            self.utils.print_info("Unable to find the Collection Interval field in the Configure Device dialog")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_configure_device_set_device_tab_values(self, system_name=None, contact=None, location=None, profile=None,
                                                     serial=None, remove_from_service=None, use_default_url=None,
                                                     webview_url=None, site=None, poll_group=None, poll_type=None,
                                                     timeout=None, retries=None, topo=None, mode=None, interval=None):
        """
        - This keyword sets the fields on the Device tab in the Configure Device dialog.
        - It assumes the dialog is already open.
        - Keyword Usage:
        - ``XIQSE Configure Device Set Device Tab Values  system_name=SYSTEM_NAME  profile=EXTR_v2_Profile  timeout=10``

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

        if self.cfg_dev.xiqse_configure_device_dialog_select_tab("Device") == 1:
            if system_name:
                the_result = self.xiqse_configure_device_dialog_set_system_name(system_name)
                if the_result == -1:
                    ret_val = -1
            if contact:
                the_result = self.xiqse_configure_device_dialog_set_contact(contact)
                if the_result == -1:
                    ret_val = -1
            if location:
                the_result = self.xiqse_configure_device_dialog_set_location(location)
                if the_result == -1:
                    ret_val = -1
            if profile:
                the_result = self.xiqse_configure_device_dialog_set_admin_profile(profile)
                if the_result == -1:
                    ret_val = -1
            if serial:
                the_result = self.xiqse_configure_device_dialog_set_replacement_serial(serial)
                if the_result == -1:
                    ret_val = -1
            if remove_from_service:
                if remove_from_service.lower() == "true":
                    the_result = self.xiqse_configure_device_dialog_enable_remove_from_service()
                    if the_result == -1:
                        ret_val = -1
                elif remove_from_service.lower() == "false":
                    the_result = self.xiqse_configure_device_dialog_disable_remove_from_service()
                    if the_result == -1:
                        ret_val = -1
                else:
                    self.utils.print_info(f"Unknown value sent for Remove From Service: {remove_from_service} - use true/false")
            if use_default_url:
                if use_default_url.lower() == "true":
                    the_result = self.xiqse_configure_device_dialog_enable_use_default_webview_url()
                    if the_result == -1:
                        ret_val = -1
                elif use_default_url.lower() == "false":
                    the_result = self.xiqse_configure_device_dialog_disable_use_default_webview_url()
                    if the_result == -1:
                        ret_val = -1
                else:
                    self.utils.print_info(f"Unknown value sent for Use Default WebView URL: {use_default_url} - use true/false")
            if webview_url:
                the_result = self.xiqse_configure_device_dialog_set_webview_url(webview_url)
                if the_result == -1:
                    ret_val = -1
            if site:
                the_result = self.xiqse_configure_device_dialog_set_default_site(site)
                if the_result == -1:
                    ret_val = -1
            if poll_group:
                the_result = self.xiqse_configure_device_dialog_set_poll_group(poll_group)
                if the_result == -1:
                    ret_val = -1
            if poll_type:
                the_result = self.xiqse_configure_device_dialog_set_poll_type(poll_type)
                if the_result == -1:
                    ret_val = -1
            if timeout:
                the_result = self.xiqse_configure_device_dialog_set_snmp_timeout(timeout)
                if the_result == -1:
                    ret_val = -1
            if retries:
                the_result = self.xiqse_configure_device_dialog_set_snmp_retries(retries)
                if the_result == -1:
                    ret_val = -1
            if topo:
                the_result = self.xiqse_configure_device_dialog_set_topology_layer(topo)
                if the_result == -1:
                    ret_val = -1
            if mode:
                the_result = self.xiqse_configure_device_dialog_set_collection_mode(mode)
                if the_result == -1:
                    ret_val = -1
            if interval:
                the_result = self.xiqse_configure_device_dialog_set_collection_interval(interval)
                if the_result == -1:
                    ret_val = -1
        else:
            ret_val = -1

        return ret_val
