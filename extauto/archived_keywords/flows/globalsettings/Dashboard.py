""" This file contains code for keywords that have been archived.
    If the keywords need to be available again copy the code to xiq/flows/globalsettings/Dashboard.py
    and implement the keyword move process.
    Instructions for moving a keyword can be found here:
    https://wiki.iq.extremenetworks.com/wiki/display/AUT/Instructions+for+Moving+Keywords """

# All Archived keywords will be deleted after December 2023

from time import sleep
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from extauto.xiq.flows.common.Navigator import Navigator
from extauto.xiq.elements.DashboardElements import DashboardElements
from extauto.common.CommonValidation import CommonValidation
from ExtremeAutomation.Utilities.deprecated import deprecated


class Dashboard:
    def __init__(self):
        self.utils = Utils()
        self.screen = Screen()
        self.auto_actions = AutoActions()
        self.navigator = Navigator()
        self.dashboard_elements = DashboardElements()
        self.common_validation = CommonValidation()

    @deprecated('This keyword is deprecated. If it is required, re-implement the keyword in the original location and '
                'complete the keyword move process. Instructions for moving keywords can be found here:'
                '/https://wiki.iq.extremenetworks.com/wiki/display/AUT/Instructions+for+Moving+Keywords')
    def dashboard_stats_total_application_usage(self):
        """
        - This keyword will get total Application usage in Dashboard Page
        - Keyword Usage
        - ``Dashboard Stats Total Application Usage``

        :return: if success return total Application usage Count else -1
        """
        self.utils.print_info("Clicking on the Extreme Brand Icon")
        sleep(15)
        icon = self.dashboard_elements.get_extreme_brand_icon()
        click_status = self.auto_actions.click(icon)

        total_app_usage = -1

        if click_status:
            self.utils.print_info("Reading the Total Application Usage")
            try:
                total_app_usage = self.dashboard_elements.get_total_app_usage().text
            except Exception:
                self.utils.print_info("Error Observed")
                self.screen.save_screen_shot()
                return 1
            self.utils.print_info("Total Application Usage: ", total_app_usage)
        return total_app_usage

    @deprecated('This keyword is deprecated. If it is required, re-implement the keyword in the original location and '
                'complete the keyword move process. Instructions for moving keywords can be found here:'
                '/https://wiki.iq.extremenetworks.com/wiki/display/AUT/Instructions+for+Moving+Keywords')
    def dashboard_cards_connection_status_online_count(self, **kwargs):
        """
        - This keyword will get total Connection status online count in dashboard health card
        - Keyword Usage
        - ``Dashboard Cards Connection Status Online Count``

        :return: if success return Connection Status Online Count else -1
        """
        self.navigator.navigate_to_devices()

        self.utils.print_info("Reading Dashboard Health Card Connection Status Online Count")
        try:
            total_online_count = self.dashboard_elements.get_total_aps_online_count().text
            kwargs['pass_msg'] = f"Total Health Card Connection Status Online Count is : {total_online_count}"
            self.common_validation.passed(**kwargs)
            return total_online_count
        except Exception:
            kwargs['fail_msg'] = "Error Observed"
            self.common_validation.fault(**kwargs)
            return -1

    @deprecated('This keyword is deprecated. If it is required, re-implement the keyword in the original location and '
                'complete the keyword move process. Instructions for moving keywords can be found here:'
                '/https://wiki.iq.extremenetworks.com/wiki/display/AUT/Instructions+for+Moving+Keywords')
    def dashboard_cards_connection_status_offline_count(self, **kwargs):
        """
        - This keyword will get total Connection status offline count in dashboard health card
        - Keyword Usage
        - ``Dashboard Cards Connection Status offline Count``

        :return: if success return Connection Status Online Count else -1
        """
        self.navigator.navigate_to_devices()

        self.utils.print_info("Reading Dashboard Health Card Connection Status offline Count")
        try:
            total_online_count = self.dashboard_elements.get_total_aps_offline_count().text
            kwargs['pass_msg'] = f"Total Health Card Connection Status Offline Count is : {total_online_count}"
            self.common_validation.passed(**kwargs)
            return total_online_count
        except Exception:
            kwargs['fail_msg'] = "Error Observed"
            self.common_validation.fault(**kwargs)
            return -1

    @deprecated('This keyword is deprecated. If it is required, re-implement the keyword in the original location and '
                'complete the keyword move process. Instructions for moving keywords can be found here:'
                '/https://wiki.iq.extremenetworks.com/wiki/display/AUT/Instructions+for+Moving+Keywords')
    def dashboard_cards_total_application_count(self, **kwargs):
        """
        - This keyword will get total aps count in dashboard health card
        - Keyword Usage
        - ``Dashboard Cards Total Application Count``

        :return: if success return total aps Count else -1
        """
        self.navigator.navigate_to_devices()

        self.utils.print_info("Reading Dashboard Health Card Total Aps Count")
        try:
            total_aps_count = self.dashboard_elements.get_total_apps_count().text
            kwargs['pass_msg'] = f"Total Health Card Total Aps Count is : {total_aps_count}"
            self.common_validation.passed(**kwargs)
            return total_aps_count
        except Exception:
            kwargs['fail_msg'] = "Not able to get Total Aps Count"
            self.common_validation.fault(**kwargs)
            return -1

    @deprecated('This keyword is deprecated. If it is required, re-implement the keyword in the original location and '
                'complete the keyword move process. Instructions for moving keywords can be found here:'
                '/https://wiki.iq.extremenetworks.com/wiki/display/AUT/Instructions+for+Moving+Keywords')
    def dashboard_cards_total_clients_count(self, **kwargs):
        """
        - This keyword will get total clients count in dashboard health card
        - Keyword Usage
        - ``Dashboard Cards Total Clients Count``

        :return: if success return total clients Count else -1
        """
        self.navigator.navigate_to_devices()

        self.utils.print_info("Reading Dashboard Health Card Total Clients Count")
        try:
            total_clients_count = self.dashboard_elements.get_total_clients_count().text
            kwargs['pass_msg'] = f"Total Health Card Total Clients Count is : {total_clients_count}"
            self.common_validation.passed(**kwargs)
            return total_clients_count
        except Exception:
            kwargs['fail_msg'] = "Not able to get Total Aps Count"
            self.common_validation.fault(**kwargs)
            return -1

    @deprecated('This keyword is deprecated. If it is required, re-implement the keyword in the original location and '
                'complete the keyword move process. Instructions for moving keywords can be found here:'
                '/https://wiki.iq.extremenetworks.com/wiki/display/AUT/Instructions+for+Moving+Keywords')
    def dashboard_cards_total_users_count(self, **kwargs):
        """
        - This keyword will get total Users count in dashboard health card
        - Keyword Usage
        - ``Dashboard Cards Total Users Count``

        :return: if success return total Users Count else -1
        """
        self.navigator.navigate_to_devices()

        self.utils.print_info("Reading Dashboard Health Card Total Users Count")
        try:
            total_users_count = self.dashboard_elements.get_total_users_count().text
            kwargs['pass_msg'] = f"Total Health Card Total Users Count is : {total_users_count}"
            self.common_validation.passed(**kwargs)
            return total_users_count
        except Exception:
            kwargs['fail_msg'] = "Not able to get Total Aps Count"
            self.common_validation.fault(**kwargs)
            return -1

    @deprecated('This keyword is deprecated. If it is required, re-implement the keyword in the original location and '
                'complete the keyword move process. Instructions for moving keywords can be found here:'
                '/https://wiki.iq.extremenetworks.com/wiki/display/AUT/Instructions+for+Moving+Keywords')
    def dashboard_cards_total_critical_alarm_count(self, **kwargs):
        """
        - This keyword will get total critical alarm count in dashboard health card
        - Keyword Usage
        - ``Dashboard Cards Total Critical Alarm Count``

        :return: if success return total critical alarm count else -1
        """
        self.navigator.navigate_to_devices()

        self.utils.print_info("Reading Dashboard Health Card Total Critical Alarm Count")
        try:
            critical_alarm_count = self.dashboard_elements.get_total_critical_alarms_count().text
            kwargs['pass_msg'] = f"Total Health Card Total Critical Alarm Count is : {critical_alarm_count}"
            self.common_validation.passed(**kwargs)
            return critical_alarm_count
        except Exception:
            kwargs['fail_msg'] = "Not able to get Total critical alarm Count"
            self.common_validation.fault(**kwargs)
            return -1

    @deprecated('This keyword is deprecated. If it is required, re-implement the keyword in the original location and '
                'complete the keyword move process. Instructions for moving keywords can be found here:'
                '/https://wiki.iq.extremenetworks.com/wiki/display/AUT/Instructions+for+Moving+Keywords')
    def dashboard_cards_total_major_alarm_count(self, **kwargs):
        """
        - This keyword will get total Major alarm count in dashboard health card
        - Keyword Usage
        - ``Dashboard Cards Total Major Alarm Count``

        :return: if success return total Major alarm count else -1
        """
        self.navigator.navigate_to_devices()

        self.utils.print_info("Reading Dashboard Health Card Total Major Alarm Count")
        try:
            major_alarm_count = self.dashboard_elements.get_total_major_alarms_count().text
            kwargs['pass_msg'] = f"Total Health Card Total Major Alarm Count is {major_alarm_count}"
            self.common_validation.passed(**kwargs)
            return major_alarm_count
        except Exception:
            kwargs['fail_msg'] = "Not able to get Total Major Alarm Count"
            self.common_validation.fault(**kwargs)
            return -1

    @deprecated('This keyword is deprecated. If it is required, re-implement the keyword in the original location and '
                'complete the keyword move process. Instructions for moving keywords can be found here:'
                '/https://wiki.iq.extremenetworks.com/wiki/display/AUT/Instructions+for+Moving+Keywords')
    def dashboard_cards_total_minor_alarm_count(self, **kwargs):
        """
        - This keyword will get total Minor alarm count in dashboard health card
        - Keyword Usage
        - ``Dashboard Cards Total Minor Alarm Count``

        :return: if success return total Minor alarm count else -1
        """
        self.navigator.navigate_to_devices()

        self.utils.print_info("Reading Dashboard Health Card Total Minor Alarm Count")
        try:
            minor_alarm_count = self.dashboard_elements.get_total_minor_alarms_count().text
            kwargs['pass_msg'] = f"Total Health Card Total Minor Alarm Count is {minor_alarm_count}"
            self.common_validation.passed(**kwargs)
            return minor_alarm_count
        except Exception:
            kwargs['fail_msg'] = "Not able to get Total Minor Alarm Count"
            self.common_validation.fault(**kwargs)
            return -1

    @deprecated('This keyword is deprecated. If it is required, re-implement the keyword in the original location and '
                'complete the keyword move process. Instructions for moving keywords can be found here:'
                '/https://wiki.iq.extremenetworks.com/wiki/display/AUT/Instructions+for+Moving+Keywords')
    def dashboard_cards_total_rogue_aps_count(self, **kwargs):
        """
        - This keyword will get total Rogue Aps Count in dashboard health card
        - Keyword Usage
        - ``Dashboard Cards Total Rogue Aps Count``

        :return: if success return Rogue Aps Count else -1
        """
        self.navigator.navigate_to_devices()

        self.utils.print_info("Reading Dashboard Health Card Total Rogue Aps Count")
        try:
            rogue_aps_count = self.dashboard_elements.get_total_rogue_aps_count().text
            kwargs['pass_msg'] = f"Total Health Card Total Rogue APS Count is {rogue_aps_count}"
            self.common_validation.passed(**kwargs)
            return rogue_aps_count
        except Exception:
            kwargs['fail_msg'] = "Not able to get Total Rogue Aps Count"
            self.common_validation.fault(**kwargs)
            return -1

    @deprecated('This keyword is deprecated. If it is required, re-implement the keyword in the original location and '
                'complete the keyword move process. Instructions for moving keywords can be found here:'
                '/https://wiki.iq.extremenetworks.com/wiki/display/AUT/Instructions+for+Moving+Keywords')
    def dashboard_cards_total_rogue_clients_count(self, **kwargs):
        """
        - This keyword will get total Rogue Aps Count in dashboard health card
        - Keyword Usage
        - ``Dashboard Cards Total Rogue clients Count``

        :return: if success return Rogue clients Count else -1
        """
        self.navigator.navigate_to_devices()

        self.utils.print_info("Reading Dashboard Health Card Total Rogue Clients Count")
        try:
            rogue_clients_count = self.dashboard_elements.get_total_rogue_clients_count().text
            kwargs['pass_msg'] = f"Total Health Card Total Rogue Client Count is {rogue_clients_count}"
            self.common_validation.passed(**kwargs)
            return rogue_clients_count
        except Exception:
            kwargs['fail_msg'] = "Not able to get Total Rogue Client Count"
            self.common_validation.fault(**kwargs)
            return -1
