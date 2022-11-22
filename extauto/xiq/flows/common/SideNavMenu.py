from extauto.common.CloudDriver import CloudDriver
from extauto.common.Screen import Screen
from extauto.common.WebElementHandler import *
from extauto.xiq.elements.NavigatorWebElements import NavigatorWebElements


class SideNavMenu(NavigatorWebElements):
    def __init__(self):
        super().__init__()
        self.screen = Screen()
        # self.driver = extauto.common.CloudDriver.cloud_driver

    def get_order_number_of_main_nav_tab(self, tab_tag):
        """
        - This Keyword gets the order number of the specified main nav tab
        - Keyword Usage:
        - ``Get Order Number Of Main Nav Tab``
        :param tab_tag: automation tag for the nav tab
        :return: number if match else -1
        """
        return self.get_main_side_nav_tab_order_number(tab_tag)

    def get_order_number_of_side_nav_menu_item(self, menu_item_tag):
        """
        - This Keyword gets the order number of the specified side nav menu item
        - Keyword Usage:
        - ``Get Order Number Of Side Nav Menu Item``
        :param menu_item_tag: automation tag for the side nav menu item
        :return: number if match else -1
        """
        return self.get_side_nav_panel_1_menu_order_number(menu_item_tag)

    def get_order_number_of_side_nav_sub_menu_item(self, menu_item_tag):
        """
        - This Keyword gets the order number of the specified side nav sub menu item
        - Keyword Usage:
        - ``Get Order Number Of Side Nav Sub Menu Item``
        :param menu_item_tag: automation tag for the side nav menu item
        :return: number if match else -1
        """
        return self.get_side_nav_panel_2_menu_order_number(menu_item_tag)

    def is_nav_menu_item_visible(self, tag):
        """
        - This Keyword checks if the specified nav menu item is visible
        - Keyword Usage:
        - ``Is Nav Menu Item Visible``
        :param tag: automation tag for the nav menu item
        :return: 1 if visible, -1 if not
        """
        try:
            if tag == "automation-header-copilotdash":
                if self.get_copilot_tab().is_displayed():
                    return 1

            if tag == 'automation-header-configure':
                if self.get_configure_tab().is_displayed():
                    return 1

            if tag == 'automation-header-manage':
                if self.get_manage_tab().is_displayed():
                    return 1

            if tag == 'automation-header-n360':
                if self.get_ml_insight_tab().is_displayed():
                    return 1

            if tag == 'automation-header-essentials':
                if self.get_essentials_menu().is_displayed():
                    return 1

            if tag == 'automation-header-a3':
                if self.get_a3_tab().is_displayed():
                    return 1

            if tag == "automation-header-iot-essentials":
                if self.get_extreme_iot_essentials_menu().is_displayed():
                    return 1

            if tag == "automation-header-airdefense-essentials":
                if self.get_air_defence_menu().is_displayed():
                    return 1

            if tag == "automation-header-guest-essentials":
                if self.get_extreme_guest_menu().is_displayed():
                    return 1

            if tag == "automation-header-location-essentials":
                if self.get_extreme_location_menu().is_displayed():
                    return 1

            if tag == "automation-header-location-essentials":
                if self.get_extreme_location_menu().is_displayed():
                    return 1

            if tag == "automation-header-iot-essentials-dashboard":
                if self.get_extreme_iot_essentials_dashboard_submenu().is_displayed():
                    return 1

            if tag == "automation-header-iot-essentials-devices":
                if self.get_extreme_iot_essentials_devices_submenu().is_displayed():
                    return 1

            if tag == "automation-header-iot-essentials-clients":
                if self.get_extreme_iot_essentials_clients_submenu().is_displayed():
                    return 1

            if tag == "automation-header-iot-essentials-userProfile":
                if self.get_extreme_iot_essentials_user_profiles_submenu().is_displayed():
                    return 1

            if tag == "automation-header-iot-essentials-groups":
                if self.get_extreme_iot_essentials_policy_groups_submenu().is_displayed():
                    return 1

            if tag == "automation-header-a3-inventory":
                if self.get_a3_inventory_tab().is_displayed():
                    return 1

            if tag == "automation-header-a3-reporting":
                if self.get_a3_reporting_tab().is_displayed():
                    return 1

            if tag == "automation-header-nav-tracker":
                if self.get_ml_insight_network360monitor().is_displayed():
                    return 1

            if tag == "automation-header-nav-scorecard":
                if self.get_ml_insight_network_scorecard().is_displayed():
                    return 1

            if tag == "automation-header-nav-clientsoverview":
                if self.get_ml_insight_client360().is_displayed():
                    return 1

            if tag == "automation-header-nav-clientmonitor-Diagnosis":
                if self.get_client_monitor_diagnosis_tab().is_displayed():
                    return 1

            if tag == "automation-header-nav-retail":
                if self.get_ml_insight_retail().is_displayed():
                    return 1

            if tag == "automation-header-nav-summary":
                if self.get_manage_summary_menu_item().is_displayed():
                    return 1

            if tag == "automation-header-nav-plan":
                if self.get_ml_insight_network360plan().is_displayed():
                    return 1

            if tag == "automation-header-nav-devices":
                if self.get_devices_nav().is_displayed():
                    return 1

            if tag == "automation-header-nav-clients":
                if self.get_clients_sub_tab().is_displayed():
                    return 1

            if tag == "automation-header-nav-manage-clients":
                if self.get_manage_users_menu_item().is_displayed():
                    return 1

            if tag == "automation-header-nav-events":
                if self.get_manage_events_menu_item().is_displayed():
                    return 1

            if tag == "automation-header-nav-alarms":
                if self.get_manage_alarms_nav().is_displayed():
                    return 1

            if tag == "automation-header-nav-reports":
                if self.get_manage_reports_nav().is_displayed():
                    return 1

            if tag == "automation-header-nav-apps":
                if self.get_manage_applications_menu_item().is_displayed():
                    return 1

            if tag == "automation-header-nav-security":
                if self.get_manage_security_nav().is_displayed():
                    return 1

            if tag == "automation-header-nav-policy":
                if self.get_network_policies_sub_tab().is_displayed():
                    return 1

            if tag == "automation-header-nav-configure-guest-essentials-users":
                if self.get_configure_guest_essentials_users_menu_item().is_displayed():
                    return 1

            if tag == "automation-header-nav-alerts":
                if self.get_manage_alerts_menu_item().is_displayed():
                    return 1

            if tag == "automation-header-vpnMgmt":
                if self.get_vpn_management_tab().is_displayed():
                    return 1

            return -1

        except Exception as e:
            return -1

    def is_nav_menu_item_enabled(self, tag):
        """
        - This Keyword checks if the specified nav menu item is enabled
        - Keyword Usage:
        - ``Is Nav Menu Item Enabled``
        :param tag: automation tag for the nav menu item
        :return: 1 if visible, -1 if not
        """
        if tag == "automation-header-iot-essentials":
            if self.get_extreme_iot_essentials_menu().is_enabled():
                return 1

        if tag == "automation-header-airdefense-essentials":
            if self.get_air_defence_menu().is_enabled():
                return 1

        if tag == "automation-header-guest-essentials":
            if self.get_extreme_guest_menu().is_enabled():
                return 1

        if tag == "automation-header-location-essentials":
            if self.get_extreme_location_menu().is_enabled():
                return 1

        if tag == "automation-header-location-essentials":
            if self.get_extreme_location_menu().is_enabled():
                return 1

        if tag == "automation-header-iot-essentials-dashboard":
            if self.get_extreme_iot_essentials_dashboard_submenu().is_enabled():
                return 1

        if tag == "automation-header-iot-essentials-devices":
            if self.get_extreme_iot_essentials_devices_submenu().is_enabled():
                return 1

        if tag == "automation-header-iot-essentials-clients":
            if self.get_extreme_iot_essentials_clients_submenu().is_enabled():
                return 1

        if tag == "automation-header-iot-essentials-userProfile":
            if self.get_extreme_iot_essentials_user_profiles_submenu().is_enabled():
                return 1

        if tag == "automation-header-iot-essentials-groups":
            if self.get_extreme_iot_essentials_policy_groups_submenu().is_enabled():
                return 1

        if tag == "automation-header-a3-inventory":
            if self.get_a3_inventory_tab().is_enabled():
                return 1

        if tag == "automation-header-a3-reporting":
            if self.get_a3_reporting_tab().is_enabled():
                return 1

        if tag == "automation-header-nav-tracker":
            if self.get_ml_insight_network360monitor().is_enabled():
                return 1

        if tag == "automation-header-nav-scorecard":
            if self.get_ml_insight_network_scorecard().is_enabled():
                return 1

        if tag == "automation-header-nav-clientsoverview":
            if self.get_ml_insight_client360().is_enabled():
                return 1

        if tag == "automation-header-nav-clientmonitor-Diagnosis":
            if self.get_client_monitor_diagnosis_tab().is_enabled():
                return 1

        if tag == "automation-header-nav-retail":
            if self.get_ml_insight_retail().is_enabled():
                return 1

        if tag == "automation-header-nav-summary":
            if self.get_manage_summary_menu_item().is_enabled():
                return 1

        if tag == "automation-header-nav-plan":
            if self.get_ml_insight_network360plan().is_enabled():
                return 1

        if tag == "automation-header-nav-devices":
            if self.get_devices_nav().is_enabled():
                return 1

        if tag == "automation-header-nav-clients":
            if self.get_clients_sub_tab().is_enabled():
                return 1

        if tag == "automation-header-nav-manage-clients":
            if self.get_manage_users_menu_item().is_enabled():
                return 1

        if tag == "automation-header-nav-events":
            if self.get_manage_events_menu_item().is_enabled():
                return 1

        if tag == "automation-header-nav-alarms":
            if self.get_manage_alarms_nav().is_enabled():
                return 1

        if tag == "automation-header-nav-reports":
            if self.get_manage_reports_nav().is_enabled():
                return 1

        if tag == "automation-header-nav-apps":
            if self.get_manage_applications_menu_item().is_enabled():
                return 1

        if tag == "automation-header-nav-security":
            if self.get_manage_security_nav().is_enabled():
                return 1

        if tag == "automation-header-nav-policy":
            if self.get_network_policies_sub_tab().is_enabled():
                return 1

        if tag == "automation-header-nav-configure-guest-essentials-users":
            if self.get_configure_guest_essentials_users_menu_item().is_enabled():
                return 1

        if tag == "automation-header-nav-alerts":
            if self.get_manage_alerts_menu_item().is_enabled():
                return 1

        if tag == "automation-header-vpnMgmt":
            if self.get_vpn_management_tab().is_enabled():
                return 1

        return -1

    def has_main_nav_tab_the_expected_image(self, tab_tag, expected_class):
        """
        - This Keyword checks if the expected class of the specified main nav tab exists
        - Keyword Usage:
        - ``Has Main Nav Tab The Expected Image``
        :param tab_tag: automation tag for the nav tab
        :param expected_class: expected class name
        :return: 1 if exists, else -1
        """
        if tab_tag == "automation-header-copilotdash":
            if expected_class in self.get_copilot_tab_img_class():
                return 1

        if tab_tag == 'automation-header-configure':
            if expected_class in self.get_configure_tab_img_class():
                return 1

        if tab_tag == 'automation-header-manage':
            if expected_class in self.get_manage_tab_img_class():
                return 1

        if tab_tag == 'automation-header-n360':
            if expected_class in self.get_ml_insight_tab_img_class():
                return 1

        if tab_tag == 'automation-header-essentials':
            if expected_class in self.get_essentials_menu_img_class():
                return 1

        if tab_tag == 'automation-header-a3':
            if expected_class in self.get_a3_tab_img_class():
                return 1

        return -1

    def is_the_expected_url(self, expected_url):
        """
        - This Keyword checks if the expected url of the specified main nav tab is loaded
        - Keyword Usage:
        - ``Is The Expected Url``
        :param expected_url: expected url
        :return: 1 if exists, else -1
        """
        self.screen.save_screen_shot()
        if expected_url in CloudDriver().cloud_driver.current_url:
            return 1

        return -1
