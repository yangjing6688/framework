from time import sleep
from extauto.common.CloudDriver import CloudDriver
from extauto.common.Screen import Screen
from extauto.common.Utils import Utils
from extauto.common.Cli import Cli
from extauto.common.AutoActions import AutoActions
from extauto.xiq.flows.common.Navigator import Navigator
from extauto.xiq.elements.extreme_guest.ExtremeGuestWebElements import ExtremeGuestWebElements
from extauto.common.CommonValidation import CommonValidation


class ExtremeGuest(object):
    def __init__(self):
        super().__init__()
        self.navigator = Navigator()
        # self.driver = extauto.common.CloudDriver.cloud_driver
        self.screen = Screen()
        self.utils = Utils()
        self.cli = Cli()
        self.auto_actions = AutoActions()
        self.guest_web_elem = ExtremeGuestWebElements()
        self.common_validation = CommonValidation()

    def go_to_extreme_guest_subscribe_page(self, **kwargs):
        """
        -This keyword Will Navigate to Extreme Guest Subscription Page
        - Flow: Extreme Guest--> Subscribe--> Page
        - Keyword Usage:
            ''Go To Extreme Guest subscribe Page''

        :return: 1 if navigation success
        """
        self.utils.switch_to_default(CloudDriver().cloud_driver)
        sleep(5)
        self.navigator.navigate_to_extreme_guest_menu()
        sleep(10)

        self.screen.save_screen_shot()
        sleep(2)

        if self.guest_web_elem.get_extreme_guest_subscription_page().is_displayed():
            self.utils.print_info("Click Extreme Guest Subscribe button")
            self.auto_actions.click_reference(self.guest_web_elem.get_extreme_guest_subscription_page_subscribe_button)
            sleep(3)

            self.screen.save_screen_shot()
            sleep(2)
        else:
            self.utils.print_info("User Already Subscribed Extreme Guest Page")
            kwargs['fail_msg'] = "User Already Subscribed Extreme Guest Page"
            self.common_validation.failed(**kwargs)
            return 0

        return 1

    def go_to_extreme_guest_landing_page(self, **kwargs):
        """
        -This keyword Will Navigate to Extreme Guest Window
        - Flow: XIQ--> Extreme Guest
        - Keyword Usage:
            ''Go To Extreme Guest Page''

        :return: 1 if navigation success
        """
        self.utils.switch_to_default(CloudDriver().cloud_driver)
        sleep(5)
        self.navigator.navigate_to_extreme_guest_menu()
        sleep(10)

        self.screen.save_screen_shot()
        sleep(2)

        if self.guest_web_elem.get_extreme_guest_subscription_page().is_displayed():
            self.utils.print_info("Click Extreme Guest Subscribe button")
            self.auto_actions.click_reference(self.guest_web_elem.get_extreme_guest_subscription_page_subscribe_button)
            sleep(3)

            self.screen.save_screen_shot()
            sleep(2)

            if self.guest_web_elem.get_extreme_guest_subscription_page_open_ssid_checkbox().is_displayed():
                self.utils.print_info("Select Extreme Guest Open SSID")
                self.auto_actions.click_reference(self.guest_web_elem.get_extreme_guest_subscription_page_open_ssid_checkbox)
            else:
                self.utils.print_info("Add SSID before continuing")
                kwargs['fail_msg'] = "Add SSID before continuing"
                self.common_validation.failed(**kwargs)
                return 0

            self.utils.print_info("Click Extreme Guest Subscribe Apply button")
            self.auto_actions.click_reference(self.guest_web_elem.get_extreme_guest_subscription_page_apply_button)
            sleep(3)

            self.screen.save_screen_shot()
            sleep(2)
        else:
            self.utils.print_info("User Already Subscribed Extreme Guest Page")

        self.utils.switch_to_iframe(CloudDriver().cloud_driver)
        sleep(5)

        return 1

    def go_to_extreme_guest_page(self):
        """
        -This keyword Will Navigate to Extreme Guest Menu Window
        - Flow: Extreme Guest--> More Insights-->Extreme Guest Menu Window
        - Keyword Usage:
            ''Go To Extreme Guest Page''

        :return: 1 if navigation success
        """
        self.go_to_extreme_guest_landing_page()
        self.utils.print_info("Click More Insights button")
        self.auto_actions.click_reference(self.guest_web_elem.get_extreme_guest_more_insights_tab)
        sleep(10)

        self.utils.print_info("Switch to New Extreme Guest Window")
        CloudDriver().cloud_driver.switch_to.window(CloudDriver().cloud_driver.window_handles[1])

        self.screen.save_screen_shot()
        sleep(2)

        return 1

    def go_to_extreme_guest_monitor_page(self):
        """
        -This keyword Will Navigate to Extreme Guest Menu Window
        - Flow: Extreme Guest--> More Insights-->Extreme Guest Menu Window-- Monitor
        - Keyword Usage:
            ''Go To Extreme Guest Monitor Page''

        :return: 1 if navigation success
        """
        # self.go_to_extreme_guest_page()
        self.utils.print_info("Clicking on Extreme Guest Monitor Page")
        self.auto_actions.click_reference(self.guest_web_elem.get_extreme_guest_monitor_page)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        return 1

    def go_to_extreme_guest_monitor_dashboard_page(self):
        """
        -This keyword Will Navigate to Extreme Guest Menu Window
        - Flow: Extreme Guest--> More Insights-->Extreme Guest Menu Window-- Monitor--> dashboard
        - Keyword Usage:
            ''Go To Extreme Guest Monitor Dashboard Page''

        :return: 1 if navigation success
        """
        self.go_to_extreme_guest_monitor_page()
        self.utils.print_info("Clicking on Extreme Guest Monitor Dashboard Page")
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        return 1

    def go_back_to_xiq(self):
        """
        -This keyword Will Navigate back to XIQ Window
        - Keyword Usage:
            ''Go Back To Xiq''

        :return: 1 if success
        """
        self.utils.print_info("Switch to XIQ Window")
        CloudDriver().cloud_driver.switch_to.window(CloudDriver().cloud_driver.window_handles[0])

        return 1

    def go_to_configure_page(self):
        """
        -This keyword Will Navigate to Extreme Guest Configure Menu Window
        - Flow: Extreme Guest--> More Insights--> Extreme Guest Menu Window--> Configure
        - Keyword Usage:
            ''Go To Configure Page''

        :return: 1 if success
        """
        # self.go_to_extreme_guest_page()
        self.utils.print_info("Clicking on Extreme Guest Configure Page")
        self.auto_actions.click_reference(self.guest_web_elem.get_extreme_guest_configure_page)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        return 1

    def go_to_configure_users_page(self):
        """
        -This keyword Will Navigate to Extreme Guest Configure Users Page
        - Flow: Extreme Guest--> More Insights--> Extreme Guest Menu Window--> Configure--> Users
        - Keyword Usage:
            ''Go To Configure Users Page''

        :return: 1 if success
        """
        self.go_to_configure_page()
        self.utils.print_info("Clicking on Extreme Guest Configure Users Page")
        self.auto_actions.click_reference(self.guest_web_elem.get_extreme_guest_configure_users_tab)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        return 1

    def check_help_information(self, **kwargs):
        """
        -This keyword Will check if help information is available to create open SSID
        - Flow: Extreme Guest--> Subscribe--> Page
        - Keyword Usage:
            ''check help information''

        :return: 1 if success
        """
        self.go_to_extreme_guest_subscribe_page()
        if self.guest_web_elem.get_extreme_guest_subscription_page_help_information().is_displayed():
            self.utils.print_info("Help information is displayed")
            return 1

        kwargs['fail_msg'] = "Help information is not displayed"
        self.common_validation.failed(**kwargs)
        return 0

    def _get_extreme_guest_subscription_page_open_ssid_row(self, search_string, **kwargs):
        """
        Getting the row in Open SSID is same for all the objects
        :param search_string:
        :return:
        """
        self.utils.print_info("Getting open ssid rows")
        # self.utils.print_info(self.guest_web_elem.get_extreme_guest_subscription_page_open_ssid_grid_rows())
        rows = self.guest_web_elem.get_extreme_guest_subscription_page_open_ssid_grid_rows()
        if rows:
            for row in rows:
                if cell := self.guest_web_elem.get_extreme_guest_subscription_page_open_ssid_grid_row_cells(row):
                    if cell.text == search_string:
                        return row

        self.utils.print_info(f"common object row {search_string} not present")
        kwargs['fail_msg'] = f"common object row {search_string} not present"
        self.common_validation.failed(**kwargs)
        return False

    def _search_extreme_guest_subscription_page_open_ssid(self, search_string):
        """
        Search the passed search string object in grid rows
        :param search_string:
        :return:
        """
        row = self._get_extreme_guest_subscription_page_open_ssid_row(search_string)
        if row:
            self.utils.print_info(f"{search_string} object present in grid row")
            return 1

    def _select_extreme_guest_subscription_page_open_ssid_row(self, search_string, **kwargs):
        """
        Select the passed search string object in grid rows
        :param search_string:
        :return:
        """
        row = self._get_extreme_guest_subscription_page_open_ssid_row(search_string)
        if row:
            self.auto_actions.click(
                self.guest_web_elem.get_extreme_guest_subscription_page_open_ssid_grid_row_cells(row, 'dgrid-selector'))
            sleep(2)
            return 1

        kwargs['fail_msg'] = "Row is not present"
        self.common_validation.failed(**kwargs)
        return 0

    def apply_selected_open_ssid(self, search_string, **kwargs):
        """
        -This keyword Will select and apply an open SSID
        - Flow: Flow: Extreme Guest--> Subscribe--> Page
        - Keyword Usage:
            ''apply selected open ssid''

        :param search_string: Open SSID name to be selected
        :return: 1 if success
        """
        self.utils.print_info(f"Selecting {search_string} object grid row")
        if self._select_extreme_guest_subscription_page_open_ssid_row(search_string):
            self.utils.print_info("Click Extreme Guest Subscribe Apply button")
            self.auto_actions.click_reference(self.guest_web_elem.get_extreme_guest_subscription_page_apply_button)
            sleep(3)
            return 1

        kwargs['fail_msg'] = "Row is not present"
        self.common_validation.failed(**kwargs)
        return 0

    def check_created_ssid_table(self, ssid_name=None):
        """
        -This keyword Will check for an open SSID name
        - Flow: Flow: Extreme Guest--> Subscribe--> Page
        - Keyword Usage:
            ''check_created_ssid_table''

        :param ssid_name: Open SSID name to be searched
        :return: 1 if success
        """
        if self.go_to_extreme_guest_subscribe_page():
            sleep(5)
            if self._search_extreme_guest_subscription_page_open_ssid(ssid_name):
                self.utils.print_info("SSID is available in the list")
                return 1
            else:
                self.utils.print_info("SSID is not available in the list")
        else:
            self.utils.print_info("SSID list is not available for selection ")

        self.screen.save_screen_shot()
        return 0

    def send_wg_cmd_to_ap(self, ssid_name, *cli_objs):
        """
        - This Keyword used to send CLI command to AP1 of Topology used to configure or Monitor
        - Keyword Usage:
         - ``Send Command To AP1     ${COMMAND}``

        :param ssid_name:
        :param cli_objs: CLI command to be execute on AP1

        :return: CLI Command Output
        """
        ip = self.utils.get_config_value("ap1.ip")
        port = self.utils.get_config_value("ap1.port")
        username = self.utils.get_config_value("ap1.username")
        password = self.utils.get_config_value("ap1.password")
        platform = self.utils.get_config_value("ap1.cli_type")

        self.utils.print_info("AP1 IP         : ", ip)
        self.utils.print_info("AP1 Port       : ", port)
        self.utils.print_info("AP1 Username   : ", username)
        self.utils.print_info("AP1 Password   : ", password)
        self.utils.print_info("AP1 Platform   : ", platform)

        _spawn = self.cli.open_spawn(ip, port, username, password, platform)
        if _spawn:
            for cli_obj in cli_objs:
                command = "security-object " + ssid_name + " walled-garden ip-address " + cli_obj
                self.utils.print_info("Sending Command: " + command)
                self.cli.send(_spawn, command)
                sleep(1)
            output = self.cli.send(_spawn, "save config")
            self.cli.close_spawn(_spawn)
            return output

    def go_to_analyze_page(self):
        """
        -This keyword Will Navigate to Extreme Guest Configure Menu Window
        - Flow: Extreme Guest--> More Insights--> Extreme Guest Menu Window--> Configure
        - Keyword Usage:
            ''Go To Analyze Page''
        :return: 1 if success
        """
        self.go_to_extreme_guest_page()
        self.utils.print_info("Clicking on Extreme Guest Analyze Page")
        self.auto_actions.click_reference(self.guest_web_elem.get_extreme_guest_analyze_page)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        return 1

    def go_to_analyze_manage_reports_page(self):
        """
        -This keyword Will Navigate to Extreme Guest Analyze Reports Page
        - Flow: Extreme Guest--> More Insights--> Extreme Guest Menu Window--> Configure--> Users
        - Keyword Usage:
            ''Go To Analyze Manage Reports Page''
        :return: 1 if success
        """
        self.go_to_analyze_page()
        self.utils.print_info("Clicking on Extreme Guest Analyze Reports Page")
        self.auto_actions.click(self)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        return 1
    
    def check_guest_subscription(self, **kwargs):
        """
        -This keyword Will Navigate to Extreme Guest Subscription Page
        - Flow: Extreme Guest--> Subscribe--> Page
        - Keyword Usage:
            ''Check Guest Subscription''

        :return: 1 if guest is not subscribed
        """
        self.utils.switch_to_default(CloudDriver().cloud_driver)
        sleep(5)
        self.navigator.navigate_to_extreme_guest_menu()
        sleep(10)

        self.screen.save_screen_shot()
        sleep(2)

        if self.guest_web_elem.get_extreme_guest_subscription_page().is_displayed():
            self.screen.save_screen_shot()
            sleep(2)
            return 1
        else:
            self.utils.print_info("User Already Subscribed Extreme Guest Page")
            kwargs['fail_msg'] = "User Already Subscribed Extreme Guest Page"
            self.common_validation.failed(**kwargs)
            return -1
