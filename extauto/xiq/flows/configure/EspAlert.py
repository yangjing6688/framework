from extauto.common.CloudDriver import CloudDriver
from time import sleep
from extauto.common.Screen import Screen
from extauto.common.Utils import Utils
from extauto.common.AutoActions import AutoActions
from extauto.xiq.flows.common.Navigator import Navigator
from extauto.xiq.elements.EspAlertWebElements import EspAlertWebElements
import re


class EspAlert(EspAlertWebElements):
    def __init__(self):
        super().__init__()
        self.navigator = Navigator()
        self.screen = Screen()
        self.utils = Utils()
        self.auto_actions = AutoActions()
    def enable_esp_alert(self,url):
        """
        - Keyword Usage:
         - ``Enable Esp Alert   ${URL}``

        :param url: url to load for enabling esp alert on cloud UI
        :return: 1 if loaded the url successfully
        """
        self.utils.print_info("Refresh Page")
        CloudDriver().cloud_driver.get(url)
        CloudDriver().cloud_driver.refresh()
        sleep(10)
        return 1
    def go_to_policy_and_check_tab(self,configred_title,not_configured_title):
        """
        - Go to policy page and check configured policies and not configured policies tab
        - Keyword Usage
         - ``Go To Policy And Check Tab  ${configred_title}  ${not_configured_title}``
        :return: returns 1 if successfully show configred policies and not configured policies tab else -1
        """
        self.utils.print_info("Navigating to Alert menu..")
        self.navigator.navigate_configure_alert()

        self.utils.switch_to_iframe(CloudDriver().cloud_driver)

        self.utils.print_info("Going to Policy page")
        self.auto_actions.click(self.get_go_to_policy())
        sleep(2)
        self.screen.save_screen_shot()
        self.utils.print_info("Confired tab title")
        configured_tab_title = self.get_configred_tab_txt().text
        self.utils.print_info(configured_tab_title)

        self.utils.print_info("Not Confired tab title")
        not_configured_tab_title = self.get_not_configred_tab_txt().text
        self.utils.print_info(not_configured_tab_title)

        if configured_tab_title == configred_title and not_configured_tab_title == not_configured_title:
            return 1
        else:
            self.screen.save_screen_shot()
            return -1
    def create_alert_policy(self,policy_type,source_parent,source,trigger_type,when,threshold_operator="",threshold_input=""):
        """
        - Go to policy page and check create alert policy works
        - Keyword Usage
         - ``Create Alert Policy  ${policy_type}  ${source_parent}  ${source}  ${trigger_type}  ${when}  ${threshold_operator}  ${threshold_input}``
        :return: returns 1 if successfully create alert policy else -1
        """
        self.utils.switch_to_iframe(CloudDriver().cloud_driver)

        self.utils.print_info("Going to Policy page")
        self.auto_actions.click(self.get_go_to_policy())
        sleep(2)
        self.utils.print_info("Opening profile dialog")
        self.auto_actions.click(self.get_add_policy())
        sleep(3)
        self.utils.print_info("Ticking policy type:" + policy_type)
        self.auto_actions.click(getattr(self,"get_policy_type_"+policy_type)())
        self.utils.print_info("Selecting category:" + source_parent)
        self.auto_actions.click(self.get_source_parent())
        self.auto_actions.click(getattr(self,"get_source_parent_"+source_parent)())
        self.utils.print_info("Selecting source:" + source)
        self.auto_actions.click(self.get_source())
        self.auto_actions.click(getattr(self,"get_source_"+source)())
        self.utils.print_info("Clicking trigger type:" + trigger_type)
        self.auto_actions.click(getattr(self,"get_trigger_type_"+trigger_type)())
        if policy_type == 'metric':
            self.utils.print_info('Clicking threshold operator:'+threshold_operator)
            self.auto_actions.click(self.get_threshold_operator_select())
            self.auto_actions.click(getattr(self,"get_threshold_operator_select_"+threshold_operator)())
            self.utils.print_info('Entering threshold :'+threshold_input)
            self.auto_actions.send_keys(self.get_threshold_input(), threshold_input)
        self.utils.print_info("Clicking save")
        self.auto_actions.click(self.get_save())
        sleep(5)
        return self.find_when_in_configured_grid(when)
    def find_when_in_configured_grid(self,when):
        """
        - Go to policy page and find alert policy in configured grid
        - Keyword Usage
         - ``Find When In Configured Grid  ${when}``
        :return: returns 1 if successfully matched else -1
        """
        if self.get_configured_grid_rows():
            for row in self.get_configured_grid_rows():
                if self.get_when_in_rows(row).text == when:
                    return 1
            self.screen.save_screen_shot()
            return -1
        else:
            self.screen.save_screen_shot()
            return -1
    def delete_alert_policy(self,when):
        """
        - Go to policy page and delete alert policy in configured grid
        - Keyword Usage
         - ``Delete Alert Policy  ${when}``
        :return: returns 1 if successfully delete alert policy else -1
        """
        self.utils.switch_to_iframe(CloudDriver().cloud_driver)

        self.utils.print_info("Going to Policy page")
        self.auto_actions.click(self.get_go_to_policy())
        sleep(2)
        for row in self.get_configured_grid_rows():
            if self.get_when_in_rows(row).text == when:
                self.auto_actions.click(self.get_del_icon_in_row(row))
                sleep(2)
                self.auto_actions.click(self.get_del_confirm_ok())
                sleep(5)
                if self.find_when_in_configured_grid(when) == -1:
                    return 1
        self.screen.save_screen_shot()
        return -1
    def search_in_unconfigure_grid(self,event_search_input,metric_search_input):
        """
        - Go to policy page and search in unconfigured grid
        - Keyword Usage
         - ``Search In Unconfigure Grid  ${event_search_input}  ${metric_search_input}``
        :return: returns 1 if successfully search else -1
        """
        self.utils.switch_to_iframe(CloudDriver().cloud_driver)

        self.utils.print_info("Going to Policy page")
        self.auto_actions.click(self.get_go_to_policy())
        sleep(2)
        self.utils.print_info("Clicking Unconfigured Policies Tab")
        self.auto_actions.click(self.get_not_configred_tab_txt())
        self.utils.print_info("Clicking policy type: event")
        self.auto_actions.click(self.get_unconfigured_event())
        self.utils.print_info("Clicking search icon")
        self.auto_actions.click(self.get_unconfigured_search_icon())
        self.utils.print_info('Entering search :'+event_search_input)
        self.auto_actions.send_keys(self.get_unconfigured_search_input(), event_search_input)
        if self.find_desc_in_unconfigured_grid(event_search_input) == 1:
            self.utils.print_info('Cleaning search')
            self.auto_actions.send_keys(self.get_unconfigured_search_input(), "")
            self.utils.print_info("Clicking policy type: metric")
            self.auto_actions.click(self.get_unconfigured_metric())
            self.utils.print_info('Entering search :'+metric_search_input)
            self.auto_actions.send_keys(self.get_unconfigured_search_input(), metric_search_input)
            return self.find_desc_in_unconfigured_grid(metric_search_input)
        else:
            return -1
    def find_desc_in_unconfigured_grid(self,desc):
        """
        - Go to policy page and find event/metric in unconfigured grid
        - Keyword Usage
         - ``Find Desc In Unconfigured Grid  ${when}``
        :return: returns 1 if successfully matched else -1
        """
        for row in self.get_unconfigured_grid_rows():
            if self.get_desc_in_unconfigured_grid_rows(row).text == desc:
                return 1
        self.screen.save_screen_shot()
        return -1
    def create_alert_policy_by_unconfigured_grid(self,policy_type,when,trigger_type,threshold_operator="",threshold_input=""):
        """
        - Go to policy page and check create alert policy by unconfigure event/metric works
        - Keyword Usage
         - ``Create Alert Policy By Unconfigured Grid  ${policy_type}  ${when}  ${trigger_type}  ${threshold_operator}  ${threshold_input}``
        :return: returns 1 if successfully create alert policy else -1
        """
        self.utils.switch_to_iframe(CloudDriver().cloud_driver)

        self.utils.print_info("Going to Policy page")
        self.auto_actions.click(self.get_go_to_policy())
        sleep(2)
        self.utils.print_info("Clicking Unconfigured Policies Tab")
        self.auto_actions.click(self.get_not_configred_tab_txt())
        sleep(2)
        self.utils.print_info("Matching:"+when)
        for row in self.get_unconfigured_grid_rows():
            self.utils.print_info("Matching..."+self.get_desc_in_unconfigured_grid_rows(row).text)
            if self.get_desc_in_unconfigured_grid_rows(row).text == when:
                self.utils.print_info("successfully match with "+when)
                self.auto_actions.click(self.get_add_icon_in_row(row))
                sleep(2)
                self.utils.print_info("Clicking trigger type:" + trigger_type)
                self.auto_actions.click(getattr(self,"get_trigger_type_"+trigger_type)())
                if policy_type == 'metric':
                    self.utils.print_info('Clicking threshold operator:'+threshold_operator)
                    self.auto_actions.click(self.get_threshold_operator_select())
                    self.auto_actions.click(getattr(self,"get_threshold_operator_select_"+threshold_operator)())
                    self.utils.print_info('Entering threshold :'+threshold_input)
                    self.auto_actions.send_keys(self.get_threshold_input(), threshold_input)
                self.utils.print_info("Clicking save")
                self.auto_actions.click(self.get_save())
                sleep(5)
                self.utils.print_info("Clicking Configured Policies Tab")
                self.auto_actions.click(self.get_configred_tab_txt())
                sleep(2)
                return self.find_when_in_configured_grid(when)
        self.utils.print_info("failed match with "+when)
        self.screen.save_screen_shot()
        return -1
    def edit_alert_policy(self,when,severity,desc):
        """
        - Go to policy page and check edit alert policy works
        - Keyword Usage
         - ``Edit Alert Policy  ${when}  ${severity}  ${desc}``
        :return: returns 1 if successfully edit alert policy else -1
        """
        self.utils.switch_to_iframe(CloudDriver().cloud_driver)

        self.utils.print_info("Going to Policy page")
        self.auto_actions.click(self.get_go_to_policy())
        sleep(2)
        for row in self.get_configured_grid_rows():
            if self.get_when_in_rows(row).text == when:
                self.auto_actions.click(self.get_when_in_rows(row))
                sleep(2)
                self.utils.print_info("Clicking severity select:"+severity)
                self.auto_actions.click(self.get_severity_select())
                self.auto_actions.click(getattr(self,"get_severity_select_"+severity)())
                # self.utils.print_info("Entering desc text:"+desc)
                # self.auto_actions.send_keys(self.get_profile_description(),desc)
                self.utils.print_info("Clicking save")
                self.auto_actions.click(self.get_save())
                sleep(3)
                break
        for row in self.get_configured_grid_rows():
            if self.get_when_in_rows(row).text == when:
                if self.get_severity_in_rows(row).text.lower() == severity:
                    return 1
                else:
                    self.screen.save_screen_shot()
                    return -1