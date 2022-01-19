import re
from time import sleep
import extauto.common.CloudDriver
from extauto.common.Screen import Screen
from extauto.common.Utils import Utils
from extauto.common.AutoActions import AutoActions
from extauto.xiq.flows.common.Navigator import Navigator
from extauto.xiq.elements.AdspWebElements import AdspWebElements


class AirDefenceAlarms(AdspWebElements):
    def __init__(self):
        super().__init__()
        self.navigator = Navigator()
        self.driver = extauto.common.CloudDriver.cloud_driver
        self.screen = Screen()
        self.utils = Utils()
        self.auto_actions = AutoActions()

    def get_adsp_alarm_details(self, search_string, page_size=250):
        """
        - Flow: Extreme AirDefense--> More Insights
        - Get Adsp Alarm details based on search string
        - Keyword Usage:
         - ``Get ADSP Alarm Details   ${SENSOR_MAC}``
         - ``Get ADSP Alarm Details   ${DEVICE_MAC}``
         - ``Get ADSP Alarm Details   ${ALARM_TYPE}``

        :param page_size: Paging Size
        :param search_string: str to search the alarm in grid ex: it may be Alarm type, Sensor mac, Device mac
        :return: ADSP Alarm details dictionary which matches first in the Grid else None
        """
        alarm_details = {}
        self.utils.switch_to_default(self.driver)
        sleep(5)
        self.navigator.navigate_to_extreme_airdefence()

        self.utils.switch_to_iframe(self.driver)
        sleep(5)

        self.utils.print_info("Click More Insights button")
        self.auto_actions.click(self.get_adsp_more_insights_button())
        sleep(5)

        self.utils.print_info("Switch to new ADSP tab")
        self.driver.switch_to.window(self.driver.window_handles[1])
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        if alarm_page_label := self.get_adsp_alarm_page_size_label():
            if alarm_page_label.is_displayed():
                self.utils.print_info("click on after time period drop down")
                self.auto_actions.click(self.get_adsp_alarm_page_size_drop_down())
                sleep(2)
                self.utils.print_info("Selecting Page Size to View")
                self.auto_actions.select_drop_down_options(self.get_adsp_alarm_page_size_options(), str(page_size))

        if row := self.get_adsp_alarm_grid_row(search_string):
            cells = self.get_adsp_alarms_grid_row_cells(row)
            for cell in cells:
                if re.search(r'cdk-column-\w*', cell.get_attribute("class")):
                    label = re.search(r'cdk-column-\w*', cell.get_attribute("class")).group().split("cdk-column-")[-1]
                    alarm_details[label] = cell.text
            self.utils.print_info(alarm_details)
            return alarm_details

    def get_adsp_alarm_grid_row(self, search_string):
        """
        - Get the Adsp Alarm row from the grid row based on the search string

        :param search_string:  str to search the alarm in grid ex: it may be Alarm type, Sensor mac, Device mac
        :return: ADSP Alarm row information which matches in the grid row
        """
        for row in self.get_adsp_alarm_grid_rows():
            if search_string in row.text:
                return row

    def _go_to_adsp_alarm_page(self):
        """
        -This keyword Will Navigate to Extreme AirDefence Alarm page
        - Flow: Extreme AirDefense--> More Insights

        :return:
        """
        self.utils.switch_to_default(self.driver)
        sleep(5)
        self.navigator.navigate_to_extreme_airdefence()

        self.screen.save_screen_shot()
        sleep(2)

        if self.get_adsp_subscribe_page().is_displayed():
            self.utils.print_info("Click ADSP Subscribe button")
            self.auto_actions.click(self.get_adsp_subscribe_button())
            sleep(3)

            self.screen.save_screen_shot()
            sleep(2)

            self.utils.print_info("Click ADSP Subscribe Apply button")
            self.auto_actions.click(self.get_adsp_subscribe_apply_button())
            sleep(3)

            self.screen.save_screen_shot()
            sleep(2)
        else:
            self.utils.print_info("User already subscribed ADSP page")

        self.utils.switch_to_iframe(self.driver)
        sleep(5)

        self.utils.print_info("Click More Insights button")
        self.auto_actions.click(self.get_adsp_more_insights_button())
        sleep(6)

        self.utils.print_info("Switch to new ADSP Tab")
        self.driver.switch_to.window(self.driver.window_handles[1])

        self.screen.save_screen_shot()
        sleep(2)

    def clear_all_adsp_alarms(self, search_filter=None, page_size=250):
        """
        - This Keyword Will Clear all ADSP Alarms generated in the past
        - Flow: Extreme AirDefense--> More Insights
        - Keyword Usage:
         - ``Clear All ADSP Alarms  ${search_filter}``
         - ``Clear All ADSP Alarms  ${search_filter}  page_size=100``

        :param search_filter: str to search the alarm in grid ex: it may be Alarm type, Sensor mac, Device mac
        :param page_size: No.of Alarm entries to see per Page
        :return: 1 if deleting All adsp alarms successfully else -1
        """
        self._go_to_adsp_alarm_page()
        sleep(8)

        if search_filter:
            self.utils.print_info("Search grid based on search_filter in Auth logs")
            self.auto_actions.click(self.get_adsp_alarm_search_button())
            sleep(2)
            self.utils.print_info("Entering search_string  ", search_filter)
            self.auto_actions.send_keys(self.get_adsp_alarm_search_text_field(),
                                        search_filter)
            sleep(5)
            self.screen.save_screen_shot()
            sleep(2)

        if page_label := self.get_adsp_alarm_page_size_label():
            if page_label.is_displayed():
                self.utils.print_info("click on after time period drop down")
                self.auto_actions.click(self.get_adsp_alarm_page_size_drop_down())
                sleep(2)
                self.utils.print_info("Selecting page size to view")
                self.auto_actions.select_drop_down_options(self.get_adsp_alarm_page_size_options(), str(page_size))

        if self.get_adsp_alarm_grid_rows():
            self.utils.print_info("Select All ADSP Alarm checkboxes")
            self.auto_actions.click(self.get_all_adsp_alarm_grid_check_boxes())
            sleep(2)

            self.screen.save_screen_shot()
            sleep(2)

            self.utils.print_info("Click clear ADSP alarms")
            self.auto_actions.click(self.get_adsp_alarm_clear_button())
            sleep(2)

            self.screen.save_screen_shot()
            sleep(2)

            self.utils.print_info("Click confirmation to delete ADSP alarms")
            self.auto_actions.click(self.get_adsp_alarm_clear_confirm_yes_button())

            self.utils.print_info("Switch to parent ADSP tab")
            self.driver.switch_to.window(self.driver.window_handles[0])

            return 1
        else:
            self.utils.print_info("ADSP alarms rows not present in the grid")
            self.utils.print_info("Switch to new ADSP tab")
            self.driver.switch_to.window(self.driver.window_handles[0])
            return -1

    def get_total_adsp_alarm_count(self):
        """
        - This Keyword Will Get Total ADSP Alarms count details from Extreme AirDefense Widget
        - Flow: Extreme AirDefense
        - Keyword Usage:
         - ``Get Total ADSP Alarm Count ``

        :return: Total Alarm Count
        """
        self._go_to_adsp_alarm_page()
        sleep(8)

        alarm_count = self.get_total_adsp_alarm_count_on_grid().text
        self.utils.print_info(f"Total ADSP Alarms count : {alarm_count}")
        return str(alarm_count).strip()

    def check_adsp_alarms_overview_widget_count(self):
        """
        - This Keyword Will Get adsp alarms overview count details from Extreme AirDefense Widget
        - Flow: Extreme AirDefense
        - Keyword Usage:
         - ``Check ADSP Alarms Overview Widget Count ``

        :return: Total Alarm Count
        """
        self.utils.print_info("Switch to first ADSP tab")
        self.driver.switch_to.window(self.driver.window_handles[0])

        self.utils.switch_to_default(self.driver)
        sleep(5)
        self.navigator.navigate_to_extreme_airdefence()

        self.utils.switch_to_iframe(self.driver)
        sleep(5)

        self.utils.print_info("Click widget refresh button")
        self.auto_actions.click(self.get_adsp_widget_refresh_button())
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        alarm_detail = self.get_adsp_alarms_overview_widget_count().text
        alarm_count = alarm_detail.split('Alarms')[0]
        self.utils.print_info(f"Total ADSP Alarms Overview Widget Count : {alarm_count}")
        return str(alarm_count).strip()

    def check_adsp_alarm_by_severity_count(self):
        """
        - This Keyword Will Get ADSP alarms by severity count details from Extreme AirDefense Widget
        - Flow: Extreme AirDefense
        - Keyword Usage:
         - ``Check ADSP Alarm By Severity Count ``

        :return: Total Alarm Count
        """
        self.utils.print_info("Switch to first ADSP Tab")
        self.driver.switch_to.window(self.driver.window_handles[0])

        self.utils.switch_to_default(self.driver)
        sleep(5)
        self.navigator.navigate_to_extreme_airdefence()

        self.utils.switch_to_iframe(self.driver)
        sleep(5)

        self.utils.print_info("Click Widget Refresh button")
        self.auto_actions.click(self.get_adsp_widget_refresh_button())
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        alarm_detail = self.get_adsp_alarms_by_severity_widget_count().text
        alarm_count = alarm_detail.split('Alarms')[0]
        self.utils.print_info(f"Total ADSP alarms by Severity Widget Count : {alarm_count}")
        return str(alarm_count).strip()

    def _go_to_adsp_settings_page(self):
        """
        -This keyword will navigate to Extreme AirDefence settings page
        - Flow: Extreme AirDefense--> Settings

        :return:
        """
        self.utils.switch_to_default(self.driver)
        sleep(5)
        self.navigator.navigate_to_extreme_airdefence()

        self.utils.switch_to_iframe(self.driver)
        sleep(5)

        self.utils.print_info("Click Settings Button")
        self.auto_actions.click(self.get_adsp_settings_button())
        sleep(2)
        return True

    def change_wireless_thread_detection_status(self, wips_policy_name, status):
        """
        - Selects the WIPS Policy row and changes the wireless thread detection Status
        - Flow: Extreme AirDefense---> Settings
        - Keyword USage:
         - ``change wireless thread detection status   ${WIPS_POLICY_NAME}   ${STATUS}``

        :param wips_policy_name: WIPS Policy name
        :param status: wireless thread detection status to change either ON/OFF
        :return: return 1 if Wips Policy found and changed the status else False
        """

        self._go_to_adsp_settings_page()
        self.utils.print_info("Changing Wireless Thread Detection Status With Wips Policy Name: ", wips_policy_name)

        sleep(5)
        rows = self.get_adsp_page_wips_policy_grid_rows()
        for row in rows:
            if wips_policy_name in row.text:
                self.utils.print_info("Configuring Wireless Thread Detection Status Section")
                if status.upper() == "ON":
                    self.utils.print_info("Configuring Wireless Thread Detection Status1: ", status)
                    if not self.get_adsp_wireless_thread_detection_button(row).is_selected():
                        self.auto_actions.click(self.get_adsp_wireless_thread_detection_button(row))
                        sleep(2)

                        self.screen.save_screen_shot()
                        sleep(2)
                else:
                    self.utils.print_info("Configuring Wireless Thread Detection Status2: ", status)
                    self.auto_actions.click(self.get_adsp_wireless_thread_detection_button(row))
                    sleep(2)

                    self.screen.save_screen_shot()
                    sleep(2)

                self.utils.print_info("Click Apply button")
                self.auto_actions.click(self.get_adsp_wireless_thread_detection_apply_button())
                sleep(2)

                self.utils.print_info("Click Ok button to confirm")
                self.auto_actions.click(self.get_adsp_wireless_thread_detection_ok_button())
                sleep(2)
                return 1
        return False

    def Rbac_user_wips_profile_click_status(self, user, wips_policy_name):
        """
        - Flow: Extreme AirDefense--> Settings page
        - Check the Read Only status of WIPS profile button in settings page
        - Keyword Usage:
         - ``Rbac user wips profile_click_status   ${user} ${WIPS_POLICY_NAME}``
        :param user: Monitor,operator etc
        :param WIPS_POLICY_NAME: WIPS policy name
        :return: WIPS profile button click status(Enabled/Disabled)
        """
        self.utils.print_info("Click on Settings Button")
        self._go_to_adsp_settings_page()
        sleep(5)
        if user.upper() == "MONITOR":
            self.utils.print_info("checking Monitor user click status on wips policy")
            rows = self.get_adsp_page_wips_policy_grid_rows()
            for row in rows:
                if wips_policy_name in row.text:
                    cells = self.get_adsp_page_wips_policy_grid_checkbox_cells(row)
                    for cell in cells:
                        flag = cell.get_attribute("disabled")
                        if flag:
                            self.utils.print_info("click Button is disabled for the wips policy ", row.text)
                            self.screen.save_screen_shot()
                            sleep(2)
                            return 1
                        else:
                            self.utils.print_info("click Button is Enabled for the wips policy ", row.text)
                            self.screen.save_screen_shot()
                            sleep(2)
                            return -1


    def get_total_adsp_alarm_count_helpdesk(self):
        """
          - This Keyword Will Get Total ADSP Alarms count details from Extreme AirDefense Widget for helpdesk user
             after launching the adess url directly.
          - Flow: Extreme AirDefense
          - Keyword Usage:
                  - ``Get Total ADSP Alarm Count Helpdesk ``
          :return: Total Alarm Count
       """
        alarm_count = self.get_total_adsp_alarm_count_on_grid().text
        self.utils.print_info(f"Total ADSP Alarms Count : {alarm_count}")
        return str(alarm_count).strip()

    def subscribe_adess_essentials(self):
        """
        -This keyword Will Subscribe ADESS essentials, In wips policy the "enable Airdefense essentials" button should be ON
        - Flow: ADESS--> Subscribe-->Apply
        - Keyword Usage:
                  - ``Subscribe Adess Essentials ``
          :return: return 1 after ADESS is subscribed 
        """
        self.utils.switch_to_default(self.driver)
        sleep(5)
        self.navigator.navigate_to_extreme_airdefence()
        sleep(15)

        self.screen.save_screen_shot()
        sleep(2)

        if self.get_adsp_subscribe_page().is_displayed():
            self.utils.print_info("Click ADESS Subscribe button")
            self.auto_actions.click(self.get_adsp_subscribe_button())
            sleep(3)

            self.screen.save_screen_shot()
            sleep(2)

            self.utils.print_info("Click ADESS Subscribe Apply button")
            self.auto_actions.click(self.get_adsp_subscribe_apply_button())
            sleep(3)

            self.screen.save_screen_shot()
            sleep(2)
        else:
            self.utils.print_info("User Already Subscribed ADESS Page")
        return 1
