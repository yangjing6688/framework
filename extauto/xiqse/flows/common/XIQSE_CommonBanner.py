from time import sleep
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from xiqse.elements.common.CommonBannerWebElements import CommonBannerWebElements


class XIQSE_CommonBanner(CommonBannerWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()

    def xiqse_confirm_license_limit_warning_message_displayed(self):
        """
        - This keyword confirms the "License Limit Warning: Device(s) Not Added" banner message is displayed
        - Keyword Usage
        - ``XIQSE Confirm License Limit Warning Message Displayed``

        :return: 1 if banner is displayed, else -1
        """
        ret_val = 1
        the_banner = self.get_license_limit_warning_banner()
        if the_banner and the_banner.is_displayed:
            self.utils.print_info("'License Limit Warning' message is displayed")
        else:
            self.utils.print_info("'License Limit Warning' message not displayed")
            ret_val = -1

        return ret_val

    def xiqse_close_license_limit_warning_message(self):
        """
        - This keyword closes the "License Limit Warning: Device(s) Not Added" banner message, if it is open
        - Keyword Usage
        - ``XIQSE Close License Limit Warning Message``

        :return: 1 if action successful, else -1
        """
        ret_val = 1
        the_banner = self.get_license_limit_warning_banner()
        if the_banner and the_banner.is_displayed:
            close_btn = self.get_license_limit_warning_banner_close_button()
            if close_btn:
                self.utils.print_info("Closing 'License Limit Warning' message")
                self.auto_actions.click(close_btn)
                sleep(2)
            else:
                self.utils.print_info("Could not find close button for 'License Limit Warning' message")
                self.screen.save_screen_shot()
                ret_val = -1
        else:
            self.utils.print_info("'License Limit Warning' message not displayed")

        return ret_val

    def xiqse_confirm_licensed_device_limit_exceeded_message_displayed(self):
        """
        - This keyword confirms the "Licensed Device Limit Exceeded" banner message is displayed
        - Keyword Usage
        - ``XIQSE Confirm Licensed Device Limit Exceeded Message Displayed``

        :return: 1 if banner is displayed, else -1
        """
        ret_val = 1
        the_banner = self.get_licensed_device_limit_exceeded_banner()
        if the_banner and the_banner.is_displayed:
            self.utils.print_info("'Licensed Device Limit Exceeded' message is displayed")
        else:
            self.utils.print_info("'Licensed Device Limit Exceeded' message not displayed")
            ret_val = -1

        return ret_val

    def xiqse_close_licensed_device_limit_exceeded_message(self):
        """
        - This keyword closes the "Licensed Device Limit Exceeded" banner message, if it is open
        - Keyword Usage
        - ``XIQSE Close Licensed Device Limit Exceeded Message``

        :return: 1 if action successful, else -1
        """
        ret_val = 1
        the_banner = self.get_licensed_device_limit_exceeded_banner()
        if the_banner and the_banner.is_displayed:
            close_btn = self.get_licensed_device_limit_exceeded_banner_close_button()
            if close_btn:
                self.utils.print_info("Closing 'Licensed Device Limit Exceeded' message")
                self.auto_actions.click(close_btn)
                sleep(2)
            else:
                self.utils.print_info("Could not find close button for 'Licensed Device Limit Exceeded' message")
                self.screen.save_screen_shot()
                ret_val = -1
        else:
            self.utils.print_info("'Licensed Device Limit Exceeded' message not displayed")

        return ret_val

    def xiqse_close_connection_lost_with_xiq_message(self):
        """
        - This keyword closes the "Connected Lost with ExtremeCloud IQ" banner message, if it is open
        - Keyword Usage
        - ``XIQSE Close Connection Lost with XIQ Message``

        :return: 1 if action successful, else -1
        """
        ret_val = 1
        the_banner = self.get_connection_lost_with_xiq_banner()
        if the_banner and the_banner.is_displayed:
            close_btn = self.get_connection_lost_with_xiq_banner_close_button()
            if close_btn:
                self.utils.print_info("Closing 'Connection Lost with ExtremeCloud IQ' message")
                self.auto_actions.click(close_btn)
                sleep(2)
            else:
                self.utils.print_info("Could not find close button for 'Connection Lost with ExtremeCloud IQ' message")
                self.screen.save_screen_shot()
                ret_val = -1
        else:
            self.utils.print_info("'Connection Lost with ExtremeCloud IQ' message not displayed")

        return ret_val

    def xiqse_close_license_expiration_message(self):
        """
        - This keyword closes the "License Expiration" banner message, if it is open
        - Keyword Usage
        - ``XIQSE Close License Expiration Message``

        :return: 1 if action successful, else -1
        """
        ret_val = 1
        the_banner = self.get_license_expiration_banner()
        if the_banner and the_banner.is_displayed:
            close_btn = self.get_license_expiration_banner_close_button()
            if close_btn:
                self.utils.print_info("Closing 'License Expiration' message")
                self.auto_actions.click(close_btn)
                sleep(2)
                ret_val = 1
            else:
                self.utils.print_info("Could not find close button for 'License Expiration' message")
                self.screen.save_screen_shot()
                ret_val = -1
        else:
            self.utils.print_info("'License Expiration' message not displayed")

        return ret_val

    def xiqse_close_license_enforcement_message(self):
        """
        - This keyword closes the "License Enforcement Warning" banner message, if it is open
        - Keyword Usage
        - ``XIQSE Close License Enforcement Message``

        :return: 1 if action successful, else -1
        """
        ret_val = 1
        the_banner = self.get_license_enforcement_banner()
        if the_banner and the_banner.is_displayed:
            close_btn = self.get_license_enforcement_banner_close_button()
            if close_btn:
                self.utils.print_info("Closing 'License Enforcement Warning' message")
                self.auto_actions.click(close_btn)
                sleep(2)
                ret_val = 1
            else:
                self.utils.print_info("Could not find close button for 'License Enforcement Warning' message")
                self.screen.save_screen_shot()
                ret_val = -1
        else:
            self.utils.print_info("'License Enforcement Warning' message not displayed")

        return ret_val

    def xiqse_close_location_data_unavailable_message(self):
        """
        - This keyword closes the "Location Data Unavailable" banner message, if it is open
        - Keyword Usage
        - ``XIQSE Close Location Data Unavailable Message``

        :return: 1 if action successful, else -1
        """
        ret_val = 1
        the_banner = self.get_location_data_unavailable_banner()
        if the_banner and the_banner.is_displayed:
            close_btn = self.get_location_data_unavailable_banner_close_button()
            if close_btn:
                self.utils.print_info("Closing 'Location Data Unavailable' message")
                self.auto_actions.click(close_btn)
                sleep(2)
                ret_val = 1
            else:
                self.utils.print_info("Could not find close button for 'Location Data Unavailable' message")
                self.screen.save_screen_shot()
                ret_val = -1
        else:
            self.utils.print_info("'Location Data Unavailable' message not displayed")

        return ret_val

    def xiqse_close_no_data_available_message(self):
        """
        - This keyword closes the "No Data Available" banner message, if it is open
        - Keyword Usage
        - ``XIQSE Close No Data Available Message``

        :return: 1 if action successful, else -1
        """
        ret_val = 1
        the_banner = self.get_no_data_available_banner()
        if the_banner and the_banner.is_displayed:
            close_btn = self.get_no_data_available_banner_close_button()
            if close_btn:
                self.utils.print_info("Closing 'No Data Available' message")
                self.auto_actions.click(close_btn)
                sleep(2)
                ret_val = 1
            else:
                self.utils.print_info("Could not find close button for 'No Data Available' message")
                self.screen.save_screen_shot()
                ret_val = -1
        else:
            self.utils.print_info("'No Data Available' message not displayed")

        return ret_val

    def xiqse_close_motd_window(self):
        """
        - This keyword checks for the Message of the Day (motd) window, and closes it if it exists
        - Keyword Usage
        - ``XIQSE Close MOTD Window``
        :return: 1 if action successful or window not present, else -1
        """
        result = 1
        motdWindow = self.get_motd_window()
        if motdWindow and motdWindow.is_displayed:
            okBtn = self.get_motd_window_ok_button()
            if okBtn:
                self.utils.print_info("Closing 'Message of the Day' window")
                self.auto_actions.click(okBtn)
                sleep(2)
                result = 1
            else:
                self.utils.print_info("Element search for 'Message of the Day OK button' failed")
                self.screen.save_screen_shot()
                result = -1
        else:
            self.utils.print_info("'Message of the Day' window not displayed")

        return result

    def xiqse_close_login_banner_messages(self):
        """
        - This keyword closes banner messages which may appear at login, if any are open (e.g., License Expiration, Connection Lost with XIQ)
        - Keyword Usage
        - ``XIQSE Close Login Banner Messages``

        :return: 1 if action successful, else -1
        """
        ret_val = 1
        if self.xiqse_close_connection_lost_with_xiq_message() == -1:
            ret_val = -1
        if self.xiqse_close_license_enforcement_message() == -1:
            ret_val = -1
        if self.xiqse_close_license_expiration_message() == -1:
            ret_val = -1

        return ret_val

    def xiqse_close_all_banner_messages(self):
        """
        - This keyword closes all banner messages, if any are open (e.g., License Expiration, Connection Lost with XIQ)
        - Keyword Usage
        - ``XIQSE Close All Banner Messages``

        :return: 1 if action successful, else -1
        """
        ret_val = 1

        # Close the message of the day dialog
        if self.xiqse_close_motd_window() == -1:
            ret_val = -1

        # Close all banner message panels
        close_buttons = self.get_all_banner_close_buttons()
        if close_buttons:
            btn_count = len(close_buttons)
            self.utils.print_info(f"Closing {btn_count} banner message panels")
            self.screen.save_screen_shot()
            close_count = 0
            for button in close_buttons:
                if button:
                    self.utils.print_info("Closing banner message panel")
                    self.auto_actions.click(button)
                    close_count = close_count +1
                    sleep(1)
            self.utils.print_info(f"Closed {close_count} banner message panels")
            self.screen.save_screen_shot()
            if close_count != btn_count:
                self.utils.print_info("Not all banner message panels were closed")
                ret_val = -1
        else:
            self.utils.print_info("No banner message panels to close")

        return ret_val
