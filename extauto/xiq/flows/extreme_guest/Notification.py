from time import sleep
import extauto.common.CloudDriver
from extauto.common.Screen import Screen
from extauto.common.Utils import Utils
from extauto.common.AutoActions import AutoActions
from extauto.xiq.flows.common.Navigator import Navigator
from extauto.xiq.elements.extreme_guest.ExtremeGuestNotificationWebElements import ExtremeGuestNotificationWebElements
from selenium.common.exceptions import StaleElementReferenceException
from extauto.xiq.flows.extreme_guest.ExtremeGuest import ExtremeGuest


class Notification(object):
    def __init__(self):
        super().__init__()
        self.navigator = Navigator()
        self.driver = extauto.common.CloudDriver.cloud_driver
        self.screen = Screen()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.notification_web_elem = ExtremeGuestNotificationWebElements()
        self.ext_guest = ExtremeGuest()

    def go_to_configure_notification_policy_tab(self):
        """
        -This keyword Will Navigate to Extreme Guest Notification Policy Page
        - Flow: Extreme Guest--> More Insights--> Extreme Guest Menu Window--> Configure--> Notification > Policy
        - Keyword Usage:
            ''Go To Configure Notification Policy Tab''

        :return: 1 if success
        """
        self.ext_guest.go_to_configure_page()
        self.utils.print_info("Clicking on Extreme Guest Configure > Notification Policy tab")
        self.auto_actions.click(self.notification_web_elem.get_extreme_guest_notification_policy_tab())

        self.screen.save_screen_shot()
        sleep(2)

        return 1

    def add_notification_policy(self, policy_name, policy_description, policy_type='user', sms='False', sponsor_number='', email='True'):
        """
        -This keyword Will Navigate to Extreme Guest Notification Policy Page
        - Flow: Extreme Guest--> More Insights--> Extreme Guest Menu Window--> Configure--> Notification > Policy
        - Keyword Usage:
            ''Add Notification Policy   ${POLICY_NAME0}  ${POLICY_NAME0}     ${POLICY_TYPE0}     ${POLICY_SMS0}  ${POLICY_SPONSOR_NUMBER0}   ${POLICY_EMAIL0}''

        :param policy_name: Name of the Notification Policy
        :param policy_description: Notification Policy Description
        :param policy_type:Notification Policy Type - 'user' or 'sponsor'
        :param sms: Enable SMS for Notification Policy
        :param sponsor_number: Sponsor Phone Numbers for the Sponsor Notification Polcy
        :param email: Enable Email for Notification Policy
        :return: 1 if success
        """
        self.go_to_configure_notification_policy_tab()
        self.utils.print_info("Clicking the add policy icon ")
        self.auto_actions.click(self.notification_web_elem.get_extreme_guest_notification_policy_add_policy())

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Entering Policy name  ", policy_name)
        self.auto_actions.send_keys(self.notification_web_elem.get_extreme_guest_notification_policy_add_name(),
                                    policy_name)

        self.utils.print_info("Entering Policy description  ", policy_description)
        self.auto_actions.send_keys(self.notification_web_elem.get_extreme_guest_notification_policy_add_description(),
                                    policy_description)

        if policy_type == 'user':
            self.utils.print_info("Clicking the Policy type  ", policy_type)
            self.auto_actions.click(
                self.notification_web_elem.get_extreme_guest_notification_policy_add_policy_type_user())
        else:
            self.utils.print_info("Clicking the Policy type  ", policy_type)
            self.auto_actions.click(
                self.notification_web_elem.get_extreme_guest_notification_policy_add_policy_type_sponsor())

        if sms == 'True':
            self.utils.print_info("Clicking Policy SMS enable:  ", sms)
            self.auto_actions.click(self.notification_web_elem.get_extreme_guest_notification_policy_add_sms_enable())

        if self.notification_web_elem.get_extreme_guest_notification_policy_add_sms_sponsor_phone_number():
            self.utils.print_info("Entering the Sponsor Phone Number:  ", sponsor_number)
            self.auto_actions.send_keys(
                self.notification_web_elem.get_extreme_guest_notification_policy_add_sms_sponsor_phone_number(),
                sponsor_number)

        if email == 'True':
            self.utils.print_info("Clicking Policy Email enable  ", email)
            self.auto_actions.click(self.notification_web_elem.get_extreme_guest_notification_policy_add_email_enable())

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Clicking Save button")
        self.auto_actions.click(self.notification_web_elem.get_extreme_guest_notification_policy_add_save_button())

        self.utils.print_info("Clicking OK Button")
        self.auto_actions.click(self.notification_web_elem.get_extreme_guest_notification_policy_add_save_ok_button())

        self.screen.save_screen_shot()
        sleep(2)

        return 1

    def get_notification_policy(self, policy_name):
        """
        -This keyword Will Check if the Notification Policy Exists
        - Flow: Extreme Guest--> More Insights--> Extreme Guest Menu Window--> Configure--> Notification > Policy
        - Keyword Usage:
            ''Get Notification Policy   ${POLICY_NAME}''

        :param policy_name:
        :return:
        """

        self.utils.print_info('Getting Notification Policy row...')

        stale_retry = 1
        while stale_retry <= 10:
            try:
                rows = self.notification_web_elem.get_extreme_guest_notification_grid_rows()
                if rows:
                    self.utils.print_debug(f"Found {len(rows)} rows")
                    for row in rows:
                        self.utils.print_debug(f"Looking at row {self.format_notification_policy_row(row.text)}")
                        if policy_name:
                            self.utils.print_debug(f"Looking at Policy Name: {policy_name}")
                            if policy_name in row.text:
                                self.utils.print_info("Found Policy row: ", self.format_notification_policy_row(row.text))
                                return row
                    # Device row not found in table so break out of the StaleElementException loop
                    break
                else:
                    self.utils.print_debug("No Notification Policy found in grid")
                    break
            except StaleElementReferenceException:
                self.utils.print_info(f"Handling StaleElementReferenceException - loop {stale_retry}")
                stale_retry = stale_retry + 1

        self.utils.print_info("Unable to find Notification Policy row in grid")
        return -1

    def format_notification_policy_row(self, row):
        cell_values = row.split("\n")
        formatted_row = list()
        for cell_value in cell_values:
            formatted_row.append(cell_value)
        return formatted_row

    def check_if_notification_policy_exists(self, policy_name):
        """
        -This keyword Will Check if the Notification Policy Exists
        - Flow: Extreme Guest--> More Insights--> Extreme Guest Menu Window--> Configure--> Notification > Policy
        - Keyword Usage:
            ''Check If Notification Policy Exists   ${POLICY_NAME}''

        :param policy_name:
        :return:
        """
        
        self.go_to_configure_notification_policy_tab()

        row = self.get_notification_policy(policy_name)
        if row:
            return 1
        return -1

    def edit_notification_policy(self, policy_name, policy_description='null', policy_type='null', sms='null', sponsor_number='null', email='null'):
        """
        -This keyword Will Navigate to Extreme Guest Notification Policy Page
        - Flow: Extreme Guest--> More Insights--> Extreme Guest Menu Window--> Configure--> Notification > Policy
        - Keyword Usage:
            ''Edit Notification Policy   ${POLICY_NAME0}  ${POLICY_NAME0}     ${POLICY_TYPE0}     ${POLICY_SMS0}  ${POLICY_SPONSOR_NUMBER0}   ${POLICY_EMAIL0}''

        :param policy_name: Name of the Notification Policy
        :param policy_description: Notification Policy Description
        :param policy_type:Notification Policy Type - 'user' or 'sponsor'
        :param sms: Enable SMS for Notification Policy
        :param sponsor_number: Sponsor Phone Numbers for the Sponsor Notification Polcy
        :param email: Enable Email for Notification Policy
        :return: 1 if success
        """
        
        self.go_to_configure_notification_policy_tab()

        policy = self.get_notification_policy(policy_name)
        if policy:
            self.auto_actions.click(self.notification_web_elem.get_extreme_guest_notification_grid_row_cells_user_name_list(policy_name))

            self.screen.save_screen_shot()
            sleep(2)

            if not(policy_description=='null'):
                self.utils.print_info("Entering Policy description  ", policy_description)
                self.auto_actions.send_keys(self.notification_web_elem.get_extreme_guest_notification_policy_add_description(),
                                            policy_description)

            if not(sms == 'null'):
                self.utils.print_info("Clicking Policy SMS enable:  ", sms)
                self.auto_actions.click(self.notification_web_elem.get_extreme_guest_notification_policy_add_sms_enable())

            if self.notification_web_elem.get_extreme_guest_notification_policy_add_sms_sponsor_phone_number() and not(sponsor_number == 'null'):
                self.utils.print_info("Entering the Sponsor Phone Number:  ", sponsor_number)
                self.auto_actions.send_keys(
                    self.notification_web_elem.get_extreme_guest_notification_policy_add_sms_sponsor_phone_number(),
                    sponsor_number)

            if not(email == 'null'):
                self.utils.print_info("Clicking Policy Email enable  ", email)
                self.auto_actions.click(self.notification_web_elem.get_extreme_guest_notification_policy_add_email_enable())

            self.screen.save_screen_shot()
            sleep(2)

            self.utils.print_info("Clicking Save button")
            self.auto_actions.click(self.notification_web_elem.get_extreme_guest_notification_policy_add_save_button())

            self.utils.print_info("Clicking OK Button")
            self.auto_actions.click(self.notification_web_elem.get_extreme_guest_notification_policy_add_save_ok_button())

            self.screen.save_screen_shot()
            sleep(2)

            return 1
        self.utils.print_info("Notification Policy Does not exists")
        return -1

    def delete_notification_policy(self, policy_name):
        """
        -This keyword Will Check if the Notification Policy Exists
        - Flow: Extreme Guest--> More Insights--> Extreme Guest Menu Window--> Configure--> Notification > Policy
        - Keyword Usage:
            ''Delete Notification Policy   ${POLICY_NAME}''

        :param policy_name:
        :return:
        """
        
        self.go_to_configure_notification_policy_tab()

        policy = self.get_notification_policy(policy_name)
        if policy:
            self.auto_actions.click(policy)

            self.screen.save_screen_shot()
            sleep(2)
            
            self.utils.print_info("Clicking Delete button")
            self.auto_actions.click(self.notification_web_elem.get_extreme_guest_notification_policy_delete_policy())

            self.utils.print_info("Clicking OK Button")
            self.auto_actions.click(self.notification_web_elem.get_extreme_guest_notification_policy_add_save_ok_button())

            return 1
        self.utils.print_info("Notification Policy Does not exists")
        return -1

    def _select_extreme_guest_notification_page_notification_row(self, search_string):
        """
        Select the passed search string object in grid rows
        :param search_string:
        :return:
        """
        #row = self._get_extreme_guest_users_page_user_row(search_string)
        self.utils.print_info("Selecting Notification policy")
        self.auto_actions.click(
            self.notification_web_elem.get_extreme_guest_notification_grid_row_cells(search_string))
        return 1