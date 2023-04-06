from time import sleep
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from extauto.xiq.elements.DeviceUtilitiesWebElements import DeviceUtilitiesWebElements
from extauto.xiq.elements.NavigatorWebElements import NavigatorWebElements
from extauto.common.CommonValidation import CommonValidation


class DevicesUtilities(DeviceUtilitiesWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.navigator = NavigatorWebElements()
        self.common_validation = CommonValidation()

    def verify_device_tool_loading_is_open(self, **kwargs):
        """
        - This keyword is used to verify the device utilities loading window is open
        - Keyword Usage:
        - ``Verify Device Tool Loading Is Open``

        :return: 1 if is displayed else -1
        """
        self.utils.print_info("Checking loading dialog is open")
        if self.get_manager_view() is None:
            kwargs['fail_msg'] = "Loading dialog is not open"
            self.common_validation.failed(**kwargs)
            return -1

        if self.get_manager_view().is_displayed():
            kwargs['pass_msg'] = "Successfully to get manager view"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Loading dialog is not displayed"
            self.common_validation.failed(**kwargs)
            return -1

    def verify_device_tool_client_information_is_open(self, **kwargs):
        """
        - This keyword is used to verify the device client information tool window is open
        - Keyword Usage:
        - ``Verify Device Tool Client Information Is Open``

        :return: 1 if is displayed else -1
        """
        self.utils.print_info("Checking that Client Information dialog is open")
        if self.get_client_info_view() is not None and self.get_client_info_view().is_displayed():
            kwargs['pass_msg'] = "Successfully Client Information dialog is open"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Client Information dialog is not open"
            self.common_validation.failed(**kwargs)
            return -1

    def wait_until_device_tool_client_information_is_open(self, retry_duration=5, retry_count=20, **kwargs):
        """
        - This keyword is used to wait until the device client information tool window is open
        - Keyword Usage:
        - ``Wait Until Device Tool Client Information Is Open    retry_duration=5    retry_count=20``

        :param retry_duration: duration between each retry
        :param retry_count: retry count
        :return: 1 if is displayed else -1
        """
        count = 1
        while count <= retry_count:
            self.utils.print_info(f"Checking that Client Information dialog is open: loop {count}")
            if self.verify_device_tool_client_information_is_open() == 1:
                kwargs['pass_msg'] = f"Successfully Client Information dialog is openL loop {count}"
                self.common_validation.passed(**kwargs)
                return 1
            else:
                self.utils.print_info(f"Client Information is not loaded yet. Waiting for {retry_duration} seconds...")
                sleep(retry_duration)
            count += 1

        kwargs['fail_msg'] = "Client Information dialog did not open"
        self.common_validation.failed(**kwargs)
        return -1

    def close_device_tool_client_information(self, **kwargs):
        """
        - This keyword is used to close the client information tool window
        - Keyword Usage:
        - ``Close Device Tool Client Information``

        :return: 1 if is not displayed else -1
        """
        self.utils.print_info("Closing Client Information dialog")
        self.auto_actions.click_reference(self.get_client_info_dialog_close_button)
        sleep(2)

        if self.verify_device_tool_client_information_is_open(ignore_failure=True) == 1:
            kwargs['fail_msg'] = "Could not close Client Information dialog"
            self.common_validation.failed(**kwargs)
            return -1
        else:
            kwargs['pass_msg'] = "Close Client information dialog with success"
            self.common_validation.passed(**kwargs)
            return 1

    def verify_device_tool_get_tech_data_is_open(self, **kwargs):
        """
        - This keyword is used to verify the device get tech data tool window is open
        - Keyword Usage:
        - ``Verify Device Tool Get Tech Data Is Open``

        :return: 1 if is displayed else -1
        """
        self.utils.print_info("Checking that Get Tech Data dialog is open")
        if self.get_tech_data_view() is not None and self.get_tech_data_view().is_displayed():
            kwargs['pass_msg'] = "Successfully get tech data dialog is open"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Get Tech Data dialog is not open"
            self.common_validation.failed(**kwargs)
            return -1

    def wait_until_device_tool_get_tech_data_is_open(self, retry_duration=5, retry_count=20, **kwargs):
        """
        - This keyword is used to wait until the device get tech data tool window is open
        - Keyword Usage:
        - ``Wait Until Device Tool Get Tech Data Is Open    retry_duration=10    retry_count=30``

        :param retry_duration: duration between each retry
        :param retry_count: retry count
        :return: 1 if is displayed else -1
        """
        count = 1
        while count <= retry_count:
            self.utils.print_info(f"Checking that Get Tech Data dialog is open: loop {count}")
            if self.verify_device_tool_get_tech_data_is_open() == 1:
                kwargs['pass_msg'] = "Successfully get tech dialog is open"
                self.common_validation.passed(**kwargs)
                return 1
            else:
                self.utils.print_info(f"Get Tech Data is not loaded yet. Waiting for {retry_duration} seconds...")
                sleep(retry_duration)
            count += 1

        kwargs['fail_msg'] = "Get Tech Data dialog is not open"
        self.common_validation.failed(**kwargs)
        return -1

    def close_device_tool_get_tech_data(self, **kwargs):
        """
        - This keyword is used to close the get tech data tool window
        - Keyword Usage:
        - ``Close Device Tool Get Tech Data``

        :return: 1 if is not displayed else -1
        """
        self.utils.print_info("Closing Get Tech Data dialog")
        self.auto_actions.click_reference(self.get_tech_data_dialog_close_button)
        sleep(2)

        if self.verify_device_tool_get_tech_data_is_open(ignore_failure=True) == 1:
            kwargs['fail_msg'] = "Could not close Get Tech Data dialog"
            self.common_validation.failed(**kwargs)
            return -1
        else:
            kwargs['pass_msg'] = "Close get tech data dialog with success"
            self.common_validation.passed(**kwargs)
            return 1

    def verify_confirm_message_dialog_is_open(self, **kwargs):
        """
        - This keyword is used to verify the confirm message window is open
        - Keyword Usage:
        - ``Verify Confirm Message Dialog Is Open``

        :return: 1 if is displayed else -1
        """
        self.utils.print_info("Checking that Confirm Message dialog is open")
        if self.get_confirm_message_view() is None:
            kwargs['fail_msg'] = "Confirm Message dialog is not open"
            self.common_validation.failed(**kwargs)
            return -1

        if self.get_confirm_message_view().is_displayed():
            kwargs['pass_msg'] = "Confirm Message dialog is open"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Confirm Message dialog is not displayed"
            self.common_validation.failed(**kwargs)
            return -1

    def reject_device_tool_get_tech_data(self, **kwargs):
        """
        - This keyword is used to reject the request to continue to get tech data
        - Keyword Usage:
        - ``Reject Device Tool Get Tech Data``

        :return: 1 if is not displayed else -1
        """
        self.utils.print_info("Clinking 'No' to Get Tech Data")
        self.auto_actions.click_reference(self.get_confirm_message_no_button)
        sleep(2)

        if self.verify_confirm_message_dialog_is_open(ignore_failure=True) == 1:
            kwargs['fail_msg'] = "Could not close Confirm Message dialog"
            self.common_validation.failed(**kwargs)
            return -1
        else:
            kwargs['pass_msg'] = "Confirm Message dialog"
            self.common_validation.passed(**kwargs)
            return 1

    def accept_device_tool_get_tech_data(self, **kwargs):
        """
        - This keyword is used to accept the request to continue to get tech data
        - Keyword Usage:
        - ``Accept Device Tool Get Tech Data``

        :return: 1 if Get Tech Data window is displayed else -1
        """
        self.utils.print_info("Clinking 'Yes' to Get Tech Data")
        self.auto_actions.click_reference(self.get_confirm_message_yes_button)
        sleep(3)

        if self.verify_confirm_message_dialog_is_open(ignore_failure=True) == 1:
            self.utils.print_info("The Verify Message Dialog did not close when 'Yes' was clicked")
            kwargs['fail_msg'] = "The Verify Message Dialog did not close when 'Yes' was clicked"
            self.common_validation.failed(**kwargs)
            return -1

        if self.verify_device_tool_loading_is_open(ignore_failure=True) == 1:
            self.screen.save_screen_shot()
            kwargs['pass_msg'] = "The Verify Message Dialog  close when 'Yes' was clicked"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Get Tech Data is not loading"
            self.common_validation.failed(**kwargs)
            return -1

    def verify_device_tool_neighbor_info_is_open(self, **kwargs):
        """
        - This keyword is used to verify the device neighbor info tool window is open
        - Keyword Usage:
        - ``Verify Device Tool Neighbor Info Is Open``

        :return: 1 if is displayed else -1
        """
        self.utils.print_info("Checking that Neighbor Info dialog is open")
        if self.get_neighbor_info_view() is not None and self.get_neighbor_info_view().is_displayed():
            kwargs['pass_msg'] = "Neighbor Info dialog is open"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Neighbor Info dialog is not open"
            self.common_validation.failed(**kwargs)
            return -1

    def wait_until_device_tool_neighbor_info_is_open(self, retry_duration=5, retry_count=20, **kwargs):
        """
        - This keyword is used to wait until the device neighbor info tool window is open
        - Keyword Usage:
        - ``Wait Until Device Tool Neighbor Info Is Open    retry_duration=10    retry_count=30``

        :param retry_duration: duration between each retry
        :param retry_count: retry count
        :return: 1 if is displayed else -1
        """
        count = 1
        while count <= retry_count:
            self.utils.print_info(f"Checking that Neighbor Info dialog is open: loop {count}")
            if self.verify_device_tool_neighbor_info_is_open() == 1:
                kwargs['pass_msg'] = "Neighbor Info dialog is open"
                self.common_validation.passed(**kwargs)
                return 1
            else:
                self.utils.print_info(f"Neighbor Info is not loaded yet. Waiting for {retry_duration} seconds...")
                sleep(retry_duration)
            count += 1

        kwargs['fail_msg'] = "Neighbor Info dialog is not open"
        self.common_validation.failed(**kwargs)
        return -1

    def close_device_tool_neighbor_info(self, **kwargs):
        """
        - This keyword is used to close the device neighbor info tool window
        - Keyword Usage:
        - ``Close Device Tool Neighbor Info``

        :return: 1 if is not displayed else -1
        """
        self.utils.print_info("Closing Neighbor Info dialog")
        self.auto_actions.click_reference(self.get_neighbor_info_dialog_close_button)
        sleep(2)

        if self.verify_device_tool_neighbor_info_is_open(ignore_failure=True) == 1:
            kwargs['fail_msg'] = "Could not close Neighbor Info dialog"
            self.common_validation.failed(**kwargs)
            return -1
        else:
            kwargs['pass_msg'] = "Successfully close Neighbor Info dialog"
            self.common_validation.passed(**kwargs)
            return 1

    def verify_device_tool_locate_device_is_open(self, **kwargs):
        """
        - This keyword is used to verify the device locate device tool window is open
        - Keyword Usage:
        - ``Verify Device Tool Locate Device Is Open``

        :return: 1 if is displayed else -1
        """
        self.utils.print_info("Checking that Locate Device dialog is open")
        if self.get_locate_device_view() is not None and self.get_locate_device_view().is_displayed():
            kwargs['pass_msg'] = "Successfully Locate Device dialog is open"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['pass_msg'] = "Locate Device dialog is not open"
            self.common_validation.passed(**kwargs)
            return -1

    def wait_until_device_tool_locate_device_is_open(self, retry_duration=5, retry_count=20, **kwargs):
        """
        - This keyword is used to wait until the device locate device tool window is open
        - Keyword Usage:
        - ``Wait Until Device Tool Locate Device Is Open    retry_duration=10    retry_count=30``

        :param retry_duration: duration between each retry
        :param retry_count: retry count
        :return: 1 if is displayed else -1
        """
        count = 1
        while count <= retry_count:
            self.utils.print_info(f"Checking that Locate Device dialog is open: loop {count}")
            if self.verify_device_tool_locate_device_is_open() == 1:
                kwargs['pass_msg'] = "Locate Device dialog is open"
                self.common_validation.passed(**kwargs)
                return 1
            else:
                self.utils.print_info(f"Locate Device is not loaded yet. Waiting for {retry_duration} seconds...")
                sleep(retry_duration)
            count += 1

        kwargs['fail_msg'] = "Locate Device did not open"
        self.common_validation.failed(**kwargs)
        return -1

    def close_device_tool_locate_device(self, **kwargs):
        """
        - This keyword is used to close locate device tool window
        - Keyword Usage:
        - ``Close Device Tool Locate Device``

        :return: 1 if is not displayed else -1
        """
        self.utils.print_info("Closing Locate Device dialog")
        self.auto_actions.click_reference(self.get_locate_device_cancel_button)
        sleep(2)

        if self.verify_device_tool_locate_device_is_open(ignore_failure=True) == 1:
            kwargs['fail_msg'] = "Could not close Locate Device dialog"
            self.common_validation.failed(**kwargs)
            return -1
        else:
            kwargs['pass_msg'] = "Successfully close locate device dialog"
            self.common_validation.passed(**kwargs)
            return 1

    def verify_device_tool_packet_capture_is_open(self, **kwargs):
        """
        - This keyword is used to verify the device Packet Capture tool window is open
        - Keyword Usage:
        - ``Verify Device Tool Packet Capture Is Open``

        :return: 1 if is displayed else -1
        """
        self.utils.print_info("Checking that Packet Capture dialog is open")
        if self.get_packet_capture_view() is not None and self.get_packet_capture_view().is_displayed():
            kwargs['pass_msg'] = "Packet Capture dialog is open"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Packet Capture dialog is not open"
            self.common_validation.failed(**kwargs)
            return -1

    def wait_until_device_tool_packet_capture_is_open(self, retry_duration=5, retry_count=20, **kwargs):
        """
        - This keyword is used to wait until the device packet capture tool window is open
        - Keyword Usage:
        - ``Wait Until Device Tool Packet Capture Is Open    retry_duration=10    retry_count=30``

        :param retry_duration: duration between each retry
        :param retry_count: retry count
        :return: 1 if is displayed else -1
        """
        count = 1
        while count <= retry_count:
            self.utils.print_info(f"Checking that Packet Capture dialog is open: loop {count}")
            if self.verify_device_tool_packet_capture_is_open() == 1:
                kwargs['pass_msg'] = "Packet Capture dialog is open"
                self.common_validation.passed(**kwargs)
                return 1
            else:
                self.utils.print_info(f"Packet Capture is not loaded yet. Waiting for {retry_duration} seconds...")
                sleep(retry_duration)
            count += 1

        kwargs['fail_msg'] = "Packet Capture dialog is not open"
        self.common_validation.failed(**kwargs)
        return -1

    def close_device_tool_packet_capture(self, **kwargs):
        """
        - This keyword is used to close the device Packet Capture tool window
        - Keyword Usage:
        - ``Close Device Tool Packet Capture``

        :return: 1 if is not displayed else -1
        """
        self.utils.print_info("Closing Packet Capture dialog")
        self.auto_actions.click_reference(self.get_packet_capture_cancel_button)
        sleep(2)

        if self.verify_device_tool_packet_capture_is_open(ignore_failure=True) == 1:
            kwargs['fail_msg'] = "Could not close Packet Capture dialog"
            self.common_validation.failed(**kwargs)
            return -1
        else:
            kwargs['pass_msg'] = "successfully close packet capture dialog"
            self.common_validation.passed(**kwargs)
            return 1

    def verify_device_tool_cli_is_open(self, **kwargs):
        """
        - This keyword is used to verify the device CLI tool window is open
        - Keyword Usage:
        - ``Verify Device Tool Cli Is Open``

        :return: 1 if is displayed else -1
        """
        if self.get_show_cli_view() is not None and self.get_show_cli_view().is_displayed():
            kwargs['pass_msg'] = "CLI dialog is open"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "CLI dialog is not open"
            self.common_validation.failed(**kwargs)
            return -1

    def wait_until_device_tool_cli_is_open(self, retry_duration=5, retry_count=20, **kwargs):
        """
        - This keyword is used to wait until the device cli tool window is open
        - Keyword Usage:
        - ``Wait Until Device Tool Cli Is Open    retry_duration=10    retry_count=30``

        :param retry_duration: duration between each retry
        :param retry_count: retry count
        :return: 1 if is displayed else -1
        """
        count = 1
        while count <= retry_count:
            self.utils.print_info(f"Checking that CLI dialog is open: loop {count}")
            if self.verify_device_tool_cli_is_open() == 1:
                kwargs['pass_msg'] = "CLI dialog is open"
                self.common_validation.passed(**kwargs)
                return 1
            else:
                self.utils.print_info(f"CLI is not loaded yet. Waiting for {retry_duration} seconds...")
                sleep(retry_duration)
            count += 1

        kwargs['fail_msg'] = "CLI dialog is not open"
        self.common_validation.failed(**kwargs)
        return -1

    def close_device_tool_cli(self, **kwargs):
        """
        - This keyword is used to close the device CLI tool window
        - Keyword Usage:
        - ``Close Device Tool Cli``

        :return: 1 if is not displayed else -1
        """
        self.auto_actions.click_reference(self.get_show_cli_dialog_close_button)
        sleep(2)

        if self.verify_device_tool_cli_is_open(ignore_failure=True) == 1:
            kwargs['fail_msg'] = "could not CLI dialog"
            self.common_validation.failed(**kwargs)
            return -1
        else:
            kwargs['pass_msg'] = "CLI dialog is close"
            self.common_validation.passed(**kwargs)
            return 1

    def verify_device_tool_show_log_is_open(self):
        """
        - This keyword is used to verify the device show log tool window is open
        - Keyword Usage:
        - ``Verify Device Tool Show Log Is Open``

        :return: 1 if is displayed else -1
        """
        self.utils.print_info("Checking that Show Log dialog is open")
        return self.verify_device_tool_cli_is_open()

    def close_device_tool_show_log(self):
        """
        - This keyword is used to close the device show log tool window
        - Keyword Usage:
        - ``Close Device Tool Show Log``

        :return: 1 if is not displayed else -1
        """
        self.utils.print_info("Closing Show Log dialog")
        return self.close_device_tool_cli()

    def verify_device_tool_show_mac_table_is_open(self):
        """
        - This keyword is used to verify the device show MAC Table tool window is open
        - Keyword Usage:
        - ``Verify Device Tool Show Mac Table Is Open``

        :return: 1 if is displayed else -1
        """
        self.utils.print_info("Checking that Show MAC Table dialog is open")
        return self.verify_device_tool_cli_is_open()

    def close_device_tool_show_mac_table(self):
        """
        - This keyword is used to close the device show MAC Table tool window
        - Keyword Usage:
        - ``Close Device Tool Show Mac Table``

        :return: 1 if is not displayed else -1
        """
        self.utils.print_info("Closing Show MAC Table dialog")
        return self.close_device_tool_cli()

    def verify_device_tool_show_version_is_open(self):
        """
        - This keyword is used to verify the device show version tool window is open
        - Keyword Usage:
        - ``Verify Device Tool Show Version Is Open``

        :return: 1 if is displayed else -1
        """
        self.utils.print_info("Checking that Show Version dialog is open")
        return self.verify_device_tool_cli_is_open()

    def close_device_tool_show_version(self):
        """
        - This keyword is used to close the device show version tool window
        - Keyword Usage:
        - ``Close Device Tool Show Version``

        :return: 1 if is not displayed else -1
        """
        self.utils.print_info("Closing Show Version dialog")
        return self.close_device_tool_cli()

    def verify_device_tool_show_running_config_is_open(self):
        """
        - This keyword is used to verify the device show Running Config tool window is open
        - Keyword Usage:
        - ``Verify Device Tool Show Running Config Is Open``

        :return: 1 if is displayed else -1
        """
        self.utils.print_info("Checking that Show Running Config dialog is open")
        return self.verify_device_tool_cli_is_open()

    def close_device_tool_show_running_config(self):
        """
        - This keyword is used to close the device show Running Config tool window
        - Keyword Usage:
        - ``Close Device Tool Show Running Config``

        :return: 1 if is not displayed else -1
        """
        self.utils.print_info("Closing Show Running Config dialog")
        return self.close_device_tool_cli()

    def verify_device_tool_show_startup_config_is_open(self):
        """
        - This keyword is used to verify the device show Startup Config tool window is open
        - Keyword Usage:
        - ``Verify Device Tool Show Startup Config Is Open``

        :return: 1 if is displayed else -1
        """
        self.utils.print_info("Checking that Show Startup Config dialog is open")
        return self.verify_device_tool_cli_is_open()

    def close_device_tool_show_startup_config(self):
        """
        - This keyword is used to close the device show Startup Config tool window
        - Keyword Usage:
        - ``Close Device Tool Show Startup Config``

        :return: 1 if is not displayed else -1
        """
        self.utils.print_info("Closing Show Startup Config dialog")
        return self.close_device_tool_cli()

    def verify_device_tool_show_ip_routes_is_open(self):
        """
        - This keyword is used to verify the device show IP Routes tool window is open
        - Keyword Usage:
        - ``Verify Device Tool Show Ip Routes Is Open``

        :return: 1 if is displayed else -1
        """
        self.utils.print_info("Checking that Show IP Routes dialog is open")
        return self.verify_device_tool_cli_is_open()

    def close_device_tool_show_ip_routes(self):
        """
        - This keyword is used to close the device show IP Routes tool window
        - Keyword Usage:
        - ``Close Device Tool Show Ip Routes``

        :return: 1 if is not displayed else -1
        """
        self.utils.print_info("Closing Show IP Routes dialog")
        return self.close_device_tool_cli()

    def verify_device_tool_show_mac_routes_is_open(self):
        """
        - This keyword is used to verify the device show MAC Routes tool window is open
        - Keyword Usage:
        - ``Verify Device Tool Show Mac Routes Is Open``

        :return: 1 if is displayed else -1
        """
        self.utils.print_info("Checking that Show MAC Routes dialog is open")
        return self.verify_device_tool_cli_is_open()

    def close_device_tool_show_mac_routes(self):
        """
        - This keyword is used to close the device show MAC Routes tool window
        - Keyword Usage:
        - ``Close Device Tool Show Mac Routes``

        :return: 1 if is not displayed else -1
        """
        self.utils.print_info("Closing Show MAC Routes dialog")
        return self.close_device_tool_cli()

    def verify_device_tool_show_arp_cache_is_open(self):
        """
        - This keyword is used to verify the device show ARP Cache tool window is open
        - Keyword Usage:
        - ``Verify Device Tool Show Arp Cache Is Open``

        :return: 1 if is displayed else -1
        """
        self.utils.print_info("Checking that Show ARP Cache dialog is open")
        return self.verify_device_tool_cli_is_open()

    def close_device_tool_show_arp_cache(self):
        """
        - This keyword is used to close the device show ARP Cache tool window
        - Keyword Usage:
        - ``Close Device Tool Show Arp Cache``

        :return: 1 if is not displayed else -1
        """
        self.utils.print_info("Closing Show ARP Cache dialog")
        return self.close_device_tool_cli()

    def verify_device_tool_show_roaming_cache_is_open(self):
        """
        - This keyword is used to verify the device show Roaming Cache tool window is open
        - Keyword Usage:
        - ``Verify Device Tool Show Roaming Cache Is Open``

        :return: 1 if is displayed else -1
        """
        self.utils.print_info("Checking that Show Roaming Cache dialog is open")
        return self.verify_device_tool_cli_is_open()

    def wait_until_device_tool_show_roaming_cache_is_open(self):
        """
        - This keyword is used to wait until the device show roaming cache tool window is open
        - Keyword Usage:
        - ``Wait Until Device Tool Show Roaming Cache Is Open``

        :return: 1 if is displayed else -1
        """
        return self.wait_until_device_tool_cli_is_open()

    def close_device_tool_show_roaming_cache(self):
        """
        - This keyword is used to close the device show Roaming Cache tool window
        - Keyword Usage:
        - ``Close Device Tool Show Roaming Cache``

        :return: 1 if is not displayed else -1
        """
        self.utils.print_info("Closing Show Roaming Cache dialog")
        return self.close_device_tool_cli()

    def verify_device_tool_show_dnxp_neighbors_is_open(self):
        """
        - This keyword is used to verify the device show DNXP Neighbors tool window is open
        - Keyword Usage:
        - ``Verify Device Tool Show Dnxp Neighbors Is Open``

        :return: 1 if is displayed else -1
        """
        self.utils.print_info("Checking that Show DNXP Neighbors dialog is open")
        return self.verify_device_tool_cli_is_open()

    def close_device_tool_show_dnxp_neighbors(self):
        """
        - This keyword is used to close the device show DNXP Neighbors tool window
        - Keyword Usage:
        - ``Close Device Tool Show Dnxp Neighbors``

        :return: 1 if is not displayed else -1
        """
        self.utils.print_info("Closing Show DNXP Neighbors dialog")
        return self.close_device_tool_cli()

    def verify_device_tool_show_dnxp_cache_is_open(self):
        """
        - This keyword is used to verify the device show DNXP Cache tool window is open
        - Keyword Usage:
        - ``Verify Device Tool Show Dnxp Cache Is Open``

        :return: 1 if is displayed else -1
        """
        self.utils.print_info("Checking that Show DNXP Cache dialog is open")
        return self.verify_device_tool_cli_is_open()

    def close_device_tool_show_dnxp_cache(self):
        """
        - This keyword is used to close the device show DNXP Cache tool window
        - Keyword Usage:
        - ``Close Device Tool Show Dnxp Cache``

        :return: 1 if is not displayed else -1
        """
        self.utils.print_info("Closing Show DNXP Cache dialog")
        return self.close_device_tool_cli()

    def verify_device_tool_show_amrp_tunnel_is_open(self):
        """
        - This keyword is used to verify the device show AMRP Tunnel tool window is open
        - Keyword Usage:
        - ``Verify Device Tool Show Amrp Tunnel Is Open``

        :return: 1 if is displayed else -1
        """
        self.utils.print_info("Checking that Show AMRP Tunnel dialog is open")
        return self.verify_device_tool_cli_is_open()

    def close_device_tool_show_amrp_tunnel(self):
        """
        - This keyword is used to close the device show AMRP Tunnel tool window
        - Keyword Usage:
        - ``Close Device Tool Show Amrp Tunnel``

        :return: 1 if is not displayed else -1
        """
        self.utils.print_info("Closing Show AMRP Tunnel dialog")
        return self.close_device_tool_cli()

    def verify_device_tool_show_gre_tunnel_is_open(self):
        """
        - This keyword is used to verify the device show GRE Tunnel tool window is open
        - Keyword Usage:
        - ``Verify Device Tool Show Gre Tunnel Is Open``

        :return: 1 if is displayed else -1
        """
        self.utils.print_info("Checking that Show GRE Tunnel dialog is open")
        return self.verify_device_tool_cli_is_open()

    def close_device_tool_show_gre_tunnel(self):
        """
        - This keyword is used to close the device show GRE Tunnel tool window
        - Keyword Usage:
        - ``Close Device Tool Show Gre Tunnel``

        :return: 1 if is not displayed else -1
        """
        self.utils.print_info("Closing Show GRE Tunnel dialog")
        return self.close_device_tool_cli()

    def verify_device_tool_show_ike_event_is_open(self):
        """
        - This keyword is used to verify the device show IKE Event tool window is open
        - Keyword Usage:
        - ``Verify Device Tool Show Ike Event Is Open``

        :return: 1 if is displayed else -1
        """
        self.utils.print_info("Checking that Show IKE Event dialog is open")
        return self.verify_device_tool_cli_is_open()

    def close_device_tool_show_ike_event(self):
        """
        - This keyword is used to close the device show IKE Event tool window
        - Keyword Usage:
        - ``Close Device Tool Show Ike Event``

        :return: 1 if is not displayed else -1
        """
        self.utils.print_info("Closing Show IKE Event dialog")
        return self.close_device_tool_cli()

    def verify_device_tool_show_ike_sa_is_open(self):
        """
        - This keyword is used to verify the device show IKE SA tool window is open
        - Keyword Usage:
        - ``Verify Device Tool Show Ike Sa Is Open``

        :return: 1 if is displayed else -1
        """
        self.utils.print_info("Checking that Show IKE SA dialog is open")
        return self.verify_device_tool_cli_is_open()

    def close_device_tool_show_ike_sa(self):
        """
        - This keyword is used to close the device show IKE SA tool window
        - Keyword Usage:
        - ``Close Device Tool Show Ike Sa``

        :return: 1 if is not displayed else -1
        """
        self.utils.print_info("Closing Show IKE SA dialog")
        return self.close_device_tool_cli()

    def verify_device_tool_show_ipsec_sa_is_open(self):
        """
        - This keyword is used to verify the device show IPsec SA tool window is open
        - Keyword Usage:
        - ``Verify Device Tool Show Ipsec Sa Is Open``

        :return: 1 if is displayed else -1
        """
        self.utils.print_info("Checking that IPsec SA dialog is open")
        return self.verify_device_tool_cli_is_open()

    def close_device_tool_show_ipsec_sa(self):
        """
        - This keyword is used to close the device show IPsec SA tool window
        - Keyword Usage:
        - ``Close Device Tool Show Ipsec Sa``

        :return: 1 if is not displayed else -1
        """
        self.utils.print_info("Closing Show IPsec SA dialog")
        return self.close_device_tool_cli()

    def verify_device_tool_show_ipsec_tunnel_is_open(self):
        """
        - This keyword is used to verify the device show IPsec Tunnel tool window is open
        - Keyword Usage:
        - ``Verify Device Tool Show Ipsec Tunnel Is Open``

        :return: 1 if is displayed else -1
        """
        self.utils.print_info("Checking that IPsec Tunnel dialog is open")
        return self.verify_device_tool_cli_is_open()

    def close_device_tool_show_ipsec_tunnel(self):
        """
        - This keyword is used to close the device show IPsec Tunnel tool window
        - Keyword Usage:
        - ``Close Device Tool Show Ipsec Tunnel``

        :return: 1 if is not displayed else -1
        """
        self.utils.print_info("Closing Show IPsec Tunnel dialog")
        return self.close_device_tool_cli()

    def verify_device_tool_show_vpn_tunnel_is_open(self):
        """
        - This keyword is used to verify the device show VPN Tunnel tool window is open
        - Keyword Usage:
        - ``Verify Device Tool Show Vpn Tunnel Is Open``

        :return: 1 if is displayed else -1
        """
        self.utils.print_info("Checking that Show VPN Tunnel dialog is open")
        return self.verify_device_tool_cli_is_open()

    def close_device_tool_show_vpn_tunnel(self):
        """
        - This keyword is used to close the device show VPN Tunnel tool window
        - Keyword Usage:
        - ``Close Device Tool Show Vpn Tunnel``

        :return: 1 if is not displayed else -1
        """
        self.utils.print_info("Closing Show VPN Tunnel dialog")
        return self.close_device_tool_cli()

    def verify_device_tool_show_cpu_is_open(self):
        """
        - This keyword is used to verify the device show CPU tool window is open
        - Keyword Usage:
        - ``Verify Device Tool Show Cpu Is Open``

        :return: 1 if is displayed else -1
        """
        self.utils.print_info("Checking that Show CPU dialog is open")
        return self.verify_device_tool_cli_is_open()

    def close_device_tool_show_cpu(self):
        """
        - This keyword is used to close the device show CPU tool window
        - Keyword Usage:
        - ``Close Device Tool Show Cpu``

        :return: 1 if is not displayed else -1
        """
        self.utils.print_info("Closing Show CPU dialog")
        return self.close_device_tool_cli()

    def verify_device_tool_show_memory_is_open(self):
        """
        - This keyword is used to verify the device show memory tool window is open
        - Keyword Usage:
        - ``Verify Device Tool Show Memory Is Open``

        :return: 1 if is displayed else -1
        """
        self.utils.print_info("Checking that Show Memory dialog is open")
        return self.verify_device_tool_cli_is_open()

    def close_device_tool_show_memory(self):
        """
        - This keyword is used to close the device show memory tool window
        - Keyword Usage:
        - ``Close Device Tool Show Memory``

        :return: 1 if is not displayed else -1
        """
        self.utils.print_info("Closing Show Memory dialog")
        return self.close_device_tool_cli()

    def verify_device_tool_show_pse_is_open(self):
        """
        - This keyword is used to verify the device show PSE tool window is open
        - Keyword Usage:
        - ``Verify Device Tool Show Pse Is Open``

        :return: 1 if is displayed else -1
        """
        self.utils.print_info("Checking that Show PSE dialog is open")
        return self.verify_device_tool_cli_is_open()

    def close_device_tool_show_pse(self):
        """
        - This keyword is used to close the device show PSE tool window
        - Keyword Usage:
        - ``Close Device Tool Show Pse``

        :return: 1 if is not displayed else -1
        """
        self.utils.print_info("Closing Show PSE dialog")
        return self.close_device_tool_cli()

    def verify_device_tool_ping_is_open(self, **kwargs):
        """
        - This keyword is used to verify the device ping tool window is open
        - Keyword Usage:
        - ``Verify Device Tool Ping Is Open``

        :return: 1 if is displayed else -1
        """
        self.utils.print_info("Checking that Ping dialog is open")
        if self.get_show_ping_view() is not None and self.get_show_ping_view().is_displayed():
            kwargs['pass_msg'] = "Ping dialog is open"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Ping dialog is not open"
            self.common_validation.failed(**kwargs)
            return -1

    def wait_until_device_tool_ping_is_open(self, retry_duration=5, retry_count=20, **kwargs):
        """
        - This keyword is used to wait until the device ping tool window is open
        - Keyword Usage:
        - ``Wait Until Device Tool Ping Is Open    retry_duration=10    retry_count=30``

        :param retry_duration: duration between each retry
        :param retry_count: retry count
        :return: 1 if is displayed else -1
        """
        count = 1
        while count <= retry_count:
            self.utils.print_info(f"Checking that Ping dialog is open: loop {count}")
            if self.verify_device_tool_ping_is_open() == 1:
                kwargs['pass_msg'] = "Ping dialog is open"
                self.common_validation.passed(**kwargs)
                return 1
            else:
                self.utils.print_info(f"Ping is not loaded yet. Waiting for {retry_duration} seconds...")
                sleep(retry_duration)
            count += 1

        kwargs['fail_msg'] = "Ping dialog is not open"
        self.common_validation.failed(**kwargs)
        return -1

    def close_device_tool_ping(self, **kwargs):
        """
        - This keyword is used to close the device ping tool window
        - Keyword Usage:
        - ``Close Device Tool Ping``

        :return: 1 if is not displayed else -1
        """
        self.utils.print_info("Closing Ping dialog")
        self.auto_actions.click_reference(self.get_show_ping_dialog_close_button)
        sleep(2)

        if self.verify_device_tool_ping_is_open(ignore_failure=True) == 1:
            self.utils.print_info("Could not close Ping dialog")
            self.screen.save_screen_shot()
            kwargs['fail_msg'] = "Ping dialog is not close"
            self.common_validation.failed(**kwargs)
            return -1
        else:
            kwargs['pass_msg'] = "Ping dialog is close"
            self.common_validation.passed(**kwargs)
            return 1

    def verify_device_tool_vlan_probe_is_open(self, **kwargs):
        """
        - This keyword is used to verify the device VLAN Probe tool window is open
        - Keyword Usage:
        - ``Verify Device Tool Vlan Probe Is Open``

        :return: 1 if is displayed else -1
        """
        self.utils.print_info("Checking that VLAN Probe dialog is open")
        if self.get_vlan_probe_view() is not None and self.get_vlan_probe_view().is_displayed():
            kwargs['pass_msg'] = "VLAN Probe dialog is open"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "VLAN Probe dialog is not open"
            self.common_validation.failed(**kwargs)
            return -1

    def wait_until_device_tool_vlan_probe_is_open(self, retry_duration=5, retry_count=20, **kwargs):
        """
        - This keyword is used to wait until the device VLAN Probe tool window is open
        - Keyword Usage:
        - ``Wait Until Device Tool Vlan Probe Is Open    retry_duration=10    retry_count=30``

        :param retry_duration: duration between each retry
        :param retry_count: retry count
        :return: 1 if is displayed else -1
        """
        count = 1
        while count <= retry_count:
            self.utils.print_info(f"Checking that VLAN Probe dialog is open: loop {count}")
            if self.verify_device_tool_vlan_probe_is_open(ignore_failure=True) == 1:
                kwargs['pass_msg'] = "VLAN Probe dialog is open"
                self.common_validation.passed(**kwargs)
                return 1
            else:
                self.utils.print_info(f"VLAN Probe is not loaded yet. Waiting for {retry_duration} seconds...")
                sleep(retry_duration)
            count += 1

        kwargs['fail_msg'] = "VLAN Probe  did not open"
        self.common_validation.failed(**kwargs)
        return -1

    def close_device_tool_vlan_probe(self, **kwargs):
        """
        - This keyword is used to close the device VLAN Probe tool window
        - Keyword Usage:
        - ``Close Device Tool Vlan Probe``

        :return: 1 if is not displayed else -1
        """
        self.utils.print_info("Closing VLAN Probe dialog")
        self.auto_actions.click_reference(self.get_vlan_probe_dialog_close_button)
        sleep(2)

        if self.verify_device_tool_vlan_probe_is_open(ignore_failure=True) == 1:
            kwargs['fail_msg'] = "VLAN Probe dialog could not close"
            self.common_validation.failed(**kwargs)
            return -1
        else:
            kwargs['pass_msg'] = "VLAN Probe dialog is closed"
            self.common_validation.passed(**kwargs)
            return 1

    def verify_select_stack_member_is_open(self, **kwargs):
        """
        - This keyword is used to verify the select stack member window is open
        - Keyword Usage:
        - ``Verify Select Stack Member Is Open``

        :return: 1 if is displayed else -1
        """
        self.utils.print_info("Checking that Select Stack Member dialog is open")
        if self.get_select_stack_member_view() is None:
            kwargs['fail_msg'] = "Select Stack Member dialog is not open"
            self.common_validation.failed(**kwargs)
            return -1

        if self.get_select_stack_member_view().is_displayed():
            self.screen.save_screen_shot()
            kwargs['pass_msg'] = "Select Stack Member dialog is not open"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Select Stack Member dialog is not displayed"
            self.common_validation.failed(**kwargs)
            return -1

    def close_select_stack_member(self, **kwargs):
        """
        - This keyword is used to close the select stack member window
        - Keyword Usage:
        - ``Close Select Stack Member``

        :return: 1 if is not displayed else -1
        """
        self.utils.print_info("Closing Select Stack Member dialog")
        self.auto_actions.click_reference(self.get_select_stack_member_cancel_button)
        sleep(2)

        if self.verify_select_stack_member_is_open() == 1:
            kwargs['fail_msg'] = "Select Stack Member dialog could not open"
            self.common_validation.failed(**kwargs)
            return -1
        else:
            kwargs['pass_msg'] = "Select Stack Member dialog could open"
            self.common_validation.passed(**kwargs)
            return 1

    def _is_device_tool_ping_available(self):
        """
        - This helper checks if the diagnostic ping option is available

        :return: 1 if is displayed else -1
        """
        if self.navigator.get_device_diagnostics_show_ping_menu_item().is_displayed():
            return 1

        return -1

    def verify_device_tool_ping_available(self, **kwargs):
        """
        - This keyword checks if the diagnostic ping option is available
        - Keyword Usage:
        - ``Verify Device Tool Ping Available``

        :return: 1 if is available else -1 is not displayed
        """

        if self._is_device_tool_ping_available():
            kwargs['pass_msg'] = "Diagnostic ping option is available"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Diagnostic ping option is not available"
            self.common_validation.failed(**kwargs)
            return -1

    def _is_device_tool_show_log_available(self):
        """
        - This helper checks if the diagnostic show log option is available

        :return: 1 if is displayed else -1
        """
        if self.navigator.get_device_diagnostics_show_log_menu_item().is_displayed():
            return 1

        return -1

    def verify_device_tool_show_log_available(self, **kwargs):
        """
        - This keyword checks if the diagnostic show log option is available
        - Keyword Usage:
        - ``Verify Device Tool Show Log Available``

        :return: 1 if is available else -1 is not available
        """
        if self._is_device_tool_show_log_available():
            kwargs['pass_msg'] = "Diagnostic show log option is available"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Diagnostic show log option is not available"
            self.common_validation.failed(**kwargs)
            return -1

    def _is_device_tool_show_version_available(self):
        """
        - This helper checks if the diagnostic show version option is available

        :return: 1 if is displayed else -1
        """
        if self.navigator.get_device_diagnostics_show_version_menu_item().is_displayed():
            return 1

        return -1

    def verify_device_tool_show_version_available(self, **kwargs):
        """
        - This keyword checks if the diagnostic show version option is available
        - Keyword Usage:
        - ``Verify Device Tool Show Version Available``

        :return: 1 if is available else -1 is not available
        """
        if self._is_device_tool_show_version_available():
            kwargs['pass_msg'] = "Diagnostic show version option is available"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Diagnostic show version option is not available"
            self.common_validation.failed(**kwargs)
            return -1

    def _is_device_tool_show_running_config_available(self):
        """
        - This helper checks if the diagnostic show running config option is available

        :return: 1 if is displayed else -1
        """
        if self.navigator.get_device_diagnostics_show_running_config_menu_item().is_displayed():
            return 1

        return -1

    def verify_device_tool_show_running_config_available(self, **kwargs):
        """
        - This keyword checks if the diagnostic show running config option is available
        - Keyword Usage:
        - ``Verify Device Tool Show Running Config Available``

        :return: 1 if is available else -1 is not available
        """
        if self._is_device_tool_show_running_config_available():
            kwargs['pass_msg'] = "Diagnostic show running config option is available"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Diagnostic show running config option is not available"
            self.common_validation.failed(**kwargs)
            return -1

    def _is_device_tool_show_startup_config_available(self):
        """
        - This helper checks if the diagnostic show startup config option is available

        :return: 1 if is displayed else -1
        """
        if self.navigator.get_device_diagnostics_show_startup_config_menu_item().is_displayed():
            return 1

        return -1

    def verify_device_tool_show_startup_config_available(self, **kwargs):
        """
        - This keyword checks if the diagnostic show startup config option is available
        - Keyword Usage:
        - ``Verify Device Tool Show Startup Config Available``

        :return: 1 if is available else -1 is not available
        """
        if self._is_device_tool_show_startup_config_available():
            kwargs['pass_msg'] = "Diagnostic show startup config option is available"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Diagnostic show startup config option is not available"
            self.common_validation.failed(**kwargs)
            return -1

    def _is_device_tool_show_ip_routes_available(self):
        """
        - This helper checks if the diagnostic show ip routes option is available

        :return: 1 if is displayed else -1
        """
        if self.navigator.get_device_diagnostics_show_ip_routes_menu_item().is_displayed():
            return 1

        return -1

    def verify_device_tool_show_ip_routes_available(self, **kwargs):
        """
        - This keyword checks if the diagnostic show ip routes option is available
        - Keyword Usage:
        - ``Verify Device Tool Show Ip Routes Available``

        :return: 1 if is available else -1 is not available
        """
        if self._is_device_tool_show_ip_routes_available():
            kwargs['pass_msg'] = "Diagnostic show ip routes option is available"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Diagnostic show ip routes option is not available"
            self.common_validation.failed(**kwargs)
            return -1

    def _is_device_tool_show_mac_routes_available(self):
        """
        - This helper checks if the diagnostic show mac routes option is available

        :return: 1 if is displayed else -1
        """
        if self.navigator.get_device_diagnostics_show_mac_routes_menu_item().is_displayed():
            return 1

        return -1

    def verify_device_tool_show_mac_routes_available(self, **kwargs):
        """
        - This keyword checks if the diagnostic show mac routes option is available
        - Keyword Usage:
        - ``Verify Device Tool Show Mac Routes Available``

        :return: 1 if is available else -1 is not available
        """
        if self._is_device_tool_show_mac_routes_available():
            kwargs['pass_msg'] = "Diagnostic show mac routes option is available"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Diagnostic show mac routes option is not available"
            self.common_validation.failed(**kwargs)
            return -1

    def _is_device_tool_show_arp_cache_available(self):
        """
        - This helper checks if the diagnostic show arp cache option is available

        :return: 1 if is displayed else -1
        """
        if self.navigator.get_device_diagnostics_show_arp_cache_menu_item().is_displayed():
            return 1

        return -1

    def verify_device_tool_show_arp_cache_available(self, **kwargs):
        """
        - This keyword checks if the diagnostic show arp cache option is available
        - Keyword Usage:
        - ``Verify Device Tool Show Arp Cache Available``

        :return:  1 if is available else -1 is not available
        """
        if self._is_device_tool_show_arp_cache_available():
            kwargs['pass_msg'] = "Diagnostic show arp cache option is available"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Diagnostic show arp cache option is not available"
            self.common_validation.failed(**kwargs)
            return -1

    def _is_device_tool_show_roaming_cache_available(self):
        """
        - This helper checks if the diagnostic show roaming cache option is available

        :return: 1 if is displayed else -1
        """
        if self.navigator.get_device_diagnostics_show_roaming_cache_menu_item().is_displayed():
            return 1

        return -1

    def verify_device_tool_show_roaming_cache_available(self, **kwargs):
        """
        - This keyword checks if the diagnostic show roaming cache option is available
        - Keyword Usage:
        - ``Verify Device Tool Show Roaming Cache Available``

        :return: 1 if is available else -1 is not available
        """
        if self._is_device_tool_show_roaming_cache_available():
            kwargs['pass_msg'] = "Diagnostic show roaming cache option is available"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Diagnostic show roaming cache option is not available"
            self.common_validation.failed(**kwargs)
            return -1

    def _is_device_tool_show_dnxp_neighbors_available(self):
        """
        - This helper checks if the diagnostic show dnxp neighbors option is available

        :return: 1 if is displayed else -1
        """
        if self.navigator.get_device_diagnostics_show_dnxp_neighbors_menu_item().is_displayed():
            return 1

        return -1

    def verify_device_tool_show_dnxp_neighbors_available(self, **kwargs):
        """
        - This keyword checks if the diagnostic show dnxp neighbors option is available
        - Keyword Usage:
        - ``Verify Device Tool Show Dnxp Neighbors Available``

        :return: 1  if is available else -1 is not available
        """
        if self._is_device_tool_show_dnxp_neighbors_available():
            kwargs['pass_msg'] = "Diagnostic show dnxp neighbors option is available"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Diagnostic show dnxp neighbors option is not available"
            self.common_validation.failed(**kwargs)
            return -1

    def _is_device_tool_show_dnxp_cache_available(self):
        """
        - This helper checks if the diagnostic show dnxp cache option is available

        :return: 1 if is displayed else -1
        """
        if self.navigator.get_device_diagnostics_show_dnxp_cache_menu_item().is_displayed():
            return 1

        return -1

    def verify_device_tool_show_dnxp_cache_available(self, **kwargs):
        """
        - This keyword checks if the diagnostic show dnxp cache option is available
        - Keyword Usage:
        - ``Verify Device Tool Show Dnxp Cache Available``

        :return: 1  if is available else -1 is not available
        """
        if self._is_device_tool_show_dnxp_cache_available():
            kwargs['pass_msg'] = "Diagnostic show dnxp cache option is available"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Diagnostic show dnxp cache option is not available"
            self.common_validation.failed(**kwargs)
            return -1

    def _is_device_tool_show_amrp_tunnel_available(self):
        """
        - This helper checks if the diagnostic show amrp tunnel option is available

        :return: 1 if is displayed else -1
        """
        if self.navigator.get_device_diagnostics_show_amrp_tunnel_menu_item().is_displayed():
            return 1

        return -1

    def verify_device_tool_show_amrp_tunnel_available(self, **kwargs):
        """
        - This keyword checks if the diagnostic show amrp tunnel option is available
        - Keyword Usage:
        - ``Verify Device Tool Show Amrp Tunnel Available``

        :return: 1  if is available else -1 is not available
        """
        if self._is_device_tool_show_amrp_tunnel_available():
            kwargs['pass_msg'] = "Diagnostic show amrp tunnel option is available"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Diagnostic show amrp tunnel option is not available"
            self.common_validation.failed(**kwargs)
            return -1

    def _is_device_tool_show_gre_tunnel_available(self):
        """
        - This helper checks if the diagnostic show gre tunnel option is available

        :return: 1 if is displayed else -1
        """
        if self.navigator.get_device_diagnostics_show_gre_tunnel_menu_item().is_displayed():
            return 1

        return -1

    def verify_device_tool_show_gre_tunnel_available(self, **kwargs):
        """
        - This keyword checks if the diagnostic show gre tunnel option is available
        - Keyword Usage:
        - ``Verify Device Tool Show Gre Tunnel Available``

        :return: 1  if is available else -1 is not available
        """
        if self._is_device_tool_show_gre_tunnel_available():
            kwargs['pass_msg'] = "Diagnostic show gre tunnel option is available"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Diagnostic show gre tunnel option is not available"
            self.common_validation.failed(**kwargs)
            return -1

    def _is_device_tool_show_ike_event_available(self):
        """
        - This helper checks if the diagnostic show ike event option is available

        :return: 1 if is displayed else -1
        """
        if self.navigator.get_device_diagnostics_show_ike_event_menu_item().is_displayed():
            return 1

        return -1

    def verify_device_tool_show_ike_event_available(self, **kwargs):
        """
        - This keyword checks if the diagnostic show ike event option is available
        - Keyword Usage:
        - ``Verify Device Tool Show Ike Event Available``

        :return: 1  if is available else -1 is not available
        """
        if self._is_device_tool_show_ike_event_available():
            kwargs['pass_msg'] = "Diagnostic show ike event option is available"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Diagnostic show gre tunnel option is not available"
            self.common_validation.failed(**kwargs)
            return -1

    def _is_device_tool_show_ike_sa_available(self):
        """
        - This helper checks if the diagnostic show ike sa option is available

        :return: 1 if is displayed else -1
        """
        if self.navigator.get_device_diagnostics_show_ike_sa_menu_item().is_displayed():
            return 1

        return -1

    def verify_device_tool_show_ike_sa_available(self, **kwargs):
        """
        - This keyword checks if the diagnostic show ike sa option is available
        - Keyword Usage:
        - ``Verify Device Tool Show Ike Sa Available``

        :return: 1  if is available else -1 is not available
        """
        if self._is_device_tool_show_ike_sa_available():
            kwargs['pass_msg'] = "Diagnostic show ike sa option is available"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Diagnostic show ike sa option is not available"
            self.common_validation.failed(**kwargs)
            return -1

    def _is_device_tool_show_ipsec_sa_available(self):
        """
        - This helper checks if the diagnostic show ipsec sa option is available

        :return: 1 if is displayed else -1
        """
        if self.navigator.get_device_diagnostics_show_ipsec_sa_menu_item().is_displayed():
            return 1

        return -1

    def verify_device_tool_show_ipsec_sa_available(self, **kwargs):
        """
        - This keyword checks if the diagnostic show ipsec sa option is available
        - Keyword Usage:
        - ``Verify Device Tool Show Ipsec Sa Available``

        :return: 1  if is available else -1 is not available
        """
        if self._is_device_tool_show_ipsec_sa_available():
            kwargs['pass_msg'] = "Diagnostic show ipsec sa option is available"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Diagnostic show ipsec sa option is not available"
            self.common_validation.failed(**kwargs)
            return -1

    def _is_device_tool_show_ipsec_tunnel_available(self):
        """
        - This keyword checks if the diagnostic show ipsec tunnel option is available

        :return: 1 if is displayed else -1
        """
        if self.navigator.get_device_diagnostics_show_ipsec_tunnel_menu_item().is_displayed():
            return 1

        return -1

    def verify_device_tool_show_ipsec_tunnel_available(self, **kwargs):
        """
        - This keyword checks if the diagnostic show ipsec tunnel option is available
        - Keyword Usage:
        - ``Verify Device Tool Show Ipsec Tunnel Available``

        :return: 1  if is available else -1 is not available
        """
        if self._is_device_tool_show_ipsec_tunnel_available():
            kwargs['pass_msg'] = "Diagnostic show ipsec tunnel option is available"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Diagnostic show ipsec tunnel option is not available"
            self.common_validation.failed(**kwargs)
            return -1

    def _is_device_tool_show_cpu_available(self):
        """
        - This helper checks if the diagnostic show cpu option is available

        :return: 1 if is displayed else -1
        """
        if self.navigator.get_device_diagnostics_show_cpu_menu_item().is_displayed():
            return 1

        return -1

    def verify_device_tool_show_cpu_available(self, **kwargs):
        """
        - This keyword checks if the diagnostic show cpu option is available
        - Keyword Usage:
        - ``Verify Device Tool Show Cpu Available``

        :return: 1  if is available else -1 is not available
        """
        if self._is_device_tool_show_cpu_available():
            kwargs['pass_msg'] = "Diagnostic show cpu option is available"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Diagnostic show cpu option is not available"
            self.common_validation.failed(**kwargs)
            return -1

    def _is_device_tool_show_memory_available(self):
        """
        - This helper checks if the diagnostic show memory option is available

        :return: 1 if is displayed else -1
        """
        if self.navigator.get_device_diagnostics_show_memory_menu_item().is_displayed():
            return 1

        return -1

    def verify_device_tool_show_memory_available(self, **kwargs):
        """
        - This keyword checks if the diagnostic show memory option is available
        - Keyword Usage:
        - ``Verify Device Tool Show Memory Available``

        :return: 1  if is available else -1 is not available
        """
        if self._is_device_tool_show_memory_available():
            kwargs['pass_msg'] = "Diagnostic show memory option is available"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Diagnostic show memory option is not available"
            self.common_validation.failed(**kwargs)
            return -1

    def _is_device_tool_show_mac_table_available(self):
        """
        - This helper checks if the diagnostic show mac table option is available

        :return: 1 if is displayed else -1
        """
        if self.navigator.get_device_diagnostics_show_mac_table_menu_item().is_displayed():
            return 1

        return -1

    def verify_device_tool_show_mac_table_available(self, **kwargs):
        """
        - This keyword checks if the diagnostic show mac table option is available
        - Keyword Usage:
        - ``Verify Device Tool Show Mac Table Available``

        :return: 1  if is available else -1 is not available
        """
        if self._is_device_tool_show_mac_table_available():
            kwargs['pass_msg'] = "Diagnostic show mac table option is available"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Diagnostic show mac table option is not available"
            self.common_validation.failed(**kwargs)
            return -1

    def _is_device_tool_show_pse_available(self):
        """
        - This helper checks if the diagnostic show pse option is available

        :return: 1 if is displayed else -1
        """
        if self.navigator.get_device_diagnostics_show_pse_menu_item().is_displayed():
            return 1

        return -1

    def verify_device_tool_show_pse_available(self, **kwargs):
        """
        - This keyword checks if the diagnostic show pse option is available
        - Keyword Usage:
        - ``Verify Device Tool Show Pse Available``

        :return: 1  if is available else -1 is not available
        """
        if self._is_device_tool_show_pse_available():
            kwargs['pass_msg'] = "Diagnostic show pse option is available"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Diagnostic show pse option is not available"
            self.common_validation.failed(**kwargs)
            return -1

    def _is_device_spectrum_intelligence_available(self):
        """
        - This helper checks if the spectrum intelligence option is available

        :return: 1 if is displayed else -1
        """
        if self.navigator.get_spectrum_intelligence_menu_item().is_displayed():
            return 1

        return -1

    def verify_device_spectrum_intelligence_available(self, **kwargs):
        """
        - This keyword checks if the spectrum intelligence option is available
        - Keyword Usage:
        - ``Verify Device Spectrum Intelligence Available``

        :return: 1  if is available else -1 is not available
        """
        if self._is_device_spectrum_intelligence_available():
            kwargs['pass_msg'] = "spectrum intelligence option is available"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "spectrum intelligence option is not available"
            self.common_validation.failed(**kwargs)
            return -1

    def _is_device_status_advanced_channel_selection_protocol_available(self):
        """
        - This helper checks if the status advanced channel selection protocol option is available

        :return: 1 if is displayed else -1
        """
        if self.navigator.get_device_status_advanced_channel_selection_protocol_menu_item().is_displayed():
            return 1

        return -1

    def verify_device_status_advanced_channel_selection_protocol_available(self, **kwargs):
        """
        - This keyword checks if the status advanced channel selection protocol option is available
        - Keyword Usage:
        - ``Verify Device Status Advanced Channel Selection Protocol Available``

        :return: 1  if is available else -1 is not available
        """
        if self._is_device_status_advanced_channel_selection_protocol_available():
            kwargs['pass_msg'] = "the status advanced channel selection protocol option is available"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "the status advanced channel selection protocol option is not available"
            self.common_validation.failed(**kwargs)
            return -1

    def _is_device_status_interface_available(self):
        """
        - This helper checks if the status interface option is available

        :return: 1 if is displayed else -1
        """
        if self.navigator.get_device_status_interface_menu_item().is_displayed():
            return 1

        return -1

    def verify_device_status_interface_available(self, **kwargs):
        """
        - This keyword checks if the status interface option is available
        - Keyword Usage:
        - ``Verify Device Status Interface Available``

        :return: 1  if is available else -1 is not available
        """
        if self._is_device_status_interface_available():
            kwargs['pass_msg'] = "the status interface option is available"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "the status interface option is not available"
            self.common_validation.failed(**kwargs)
            return -1

    def _is_device_status_wifi_status_summary_available(self):
        """
        - This helper checks if the status wifi status summary option is available

        :return: 1 if is displayed else -1
        """
        if self.navigator.get_utilities_status_wifi_status_summary().is_displayed():
            return 1

        return -1

    def verify_device_status_wifi_status_summary_available(self, **kwargs):
        """
        - This keyword checks if the status wifi status summary option is available
        - Keyword Usage:
        - ``Verify Device Status Wifi Status Summary Available``

        :return: 1  if is available else -1 is not available
        """
        if self._is_device_status_wifi_status_summary_available():
            kwargs['pass_msg'] = "the status wifi status summary option is available"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "the status wifi status summary option is not available"
            self.common_validation.failed(**kwargs)
            return -1

    def _is_device_tool_client_information_available(self):
        """
        - This helper checks if the tool client information option is available

        :return: 1 if is displayed else -1
        """
        if self.navigator.get_device_tools_client_information_menu_item().is_displayed():
            return 1

        return -1

    def verify_device_tool_client_information_available(self, **kwargs):
        """
        - This keyword checks if the tool client information option is available
        - Keyword Usage:
        - ``Verify Device Tool Client Information Available``

        :return: 1  if is available else -1 is not available
        """
        if self._is_device_tool_client_information_available():
            kwargs['pass_msg'] = "the tool client information option is available"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "the tool client information option is not available"
            self.common_validation.failed(**kwargs)
            return -1

    def _is_device_tool_get_tech_data_available(self):
        """
        - This helper checks if the tool get tech data option is available

        :return: 1 if is displayed else -1
        """
        if self.navigator.get_device_tools_get_tech_menu_item().is_displayed():
            return 1

        return -1

    def verify_device_tool_get_tech_data_available(self, **kwargs):
        """
        - This keyword checks if the tool get tech data option is available
        - Keyword Usage:
        - ``verify Device Tool Get Tech Data Available``

        :return: 1  if is available else -1 is not available
        """
        if self._is_device_tool_get_tech_data_available():
            kwargs['pass_msg'] = "the tool get tech data option is available"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "the tool get tech data option is not available"
            self.common_validation.failed(**kwargs)
            return -1

    def _is_device_tool_locate_device_available(self):
        """
        - This helper checks if the tool locate device option is available

        :return: 1 if is displayed else -1
        """
        if self.navigator.get_device_tools_locate_device_menu_item().is_displayed():
            return 1

        return -1

    def verify_device_tool_locate_device_available(self, **kwargs):
        """
        - This keyword checks if the tool locate device option is available
        - Keyword Usage:
        - ``Verify Device Tool Locate Device Available``

        :return: 1  if is available else -1 is not available
        """
        if self._is_device_tool_locate_device_available():
            kwargs['pass_msg'] = "the tool locate device option is available"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "the tool locate device option is not available"
            self.common_validation.failed(**kwargs)
            return -1

    def _is_device_tool_layer_neighbor_info_available(self):
        """
        - This helper checks if the tool layer neighbor info option is available

        :return: 1 if is displayed else -1
        """
        if self.navigator.get_device_tools_layer_neighbor_info_menu_item().is_displayed():
            return 1

        return -1

    def verify_device_tool_layer_neighbor_info_available(self, **kwargs):
        """
        - This keyword checks if the tool layer neighbor info option is available
        - Keyword Usage:
        - ``Verify Device Tool Layer Neighbor Info Available``

        :return: 1  if is available else -1 is not available
        """
        if self._is_device_tool_layer_neighbor_info_available():
            kwargs['pass_msg'] = "the tool layer neighbor info option is available"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "the tool layer neighbor info option is not available"
            self.common_validation.failed(**kwargs)
            return -1

    def _is_device_tool_packet_capture_available(self):
        """
        - This helper checks if the tool packet capture option is available

        :return: 1 if is displayed else -1
        """
        if self.navigator.get_device_tools_packet_capture_menu_item().is_displayed():
            return 1

        return -1

    def verify_device_tool_packet_capture_available(self, **kwargs):
        """
        - This keyword checks if the tool packet capture option is available
        - Keyword Usage:
        - ``Verify Device Tool Packet Capture Available``

        :return: 1  if is available else -1 is not available
        """
        if self._is_device_tool_packet_capture_available():
            kwargs['pass_msg'] = "the tool packet capture option is available"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "the tool packet capture option is not available"
            self.common_validation.failed(**kwargs)
            return -1

    def _is_device_tool_vlan_probe_available(self):
        """
        - This helper checks if the tool vlan probe option is available

        :return: 1 if is displayed else -1
        """
        if self.navigator.get_device_tools_vlan_probe_menu_item().is_displayed():
            return 1

        return -1

    def verify_device_tool_vlan_probe_available(self, **kwargs):
        """
        - This keyword checks if the tool vlan probe option is available
        - Keyword Usage:
        - ``Is Device Tool Vlan Probe Available``

        :return: 1  if is available else -1 is not available
        """
        if self._is_device_tool_vlan_probe_available():
            kwargs['pass_msg'] = "the tool vlan probe option is available"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "the tool vlan probe option is not available"
            self.common_validation.failed(**kwargs)
            return -1

    def _is_reset_device_to_default_available(self):
        """
        - This helper checks if the reset device to default option is available

        :return: 1 if is displayed else -1
        """
        reset_device_to_default = self.navigator.get_reset_device_to_default_menu_item()
        if reset_device_to_default is not None and reset_device_to_default.is_displayed():
            return 1
        return -1

    def verify_reset_device_to_default_available(self, **kwargs):
        """
        - This keyword checks if the reset device to default option is available
        - Keyword Usage:
        - ``Verify Reset Device To Default Available``

        :return: 1  if is available else -1 is not available
        """
        if self._is_reset_device_to_default_available() == 1:
            kwargs['pass_msg'] = "the reset device to default option is available"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "the reset device to default option is not available"
            self.common_validation.failed(**kwargs)
            return -1
