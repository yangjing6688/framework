from time import sleep
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from xiqse.elements.common.CommonNavigatorWebElements import CommonNavigatorWebElements
from xiqse.elements.network.NetworkWebElements import NetworkWebElements
from xiqse.elements.alarms_events.AlarmsEventsWebElements import AlarmsEventsWebElements
from xiqse.elements.control.ControlWebElements import ControlWebElements
from xiqse.elements.analytics.AnalyticsWebElements import AnalyticsWebElements
from xiqse.elements.wireless.WirelessWebElements import WirelessWebElements
from xiqse.elements.compliance.ComplianceWebElements import ComplianceWebElements
from xiqse.elements.reports.ReportsWebElements import ReportsWebElements
from xiqse.elements.tasks.TasksWebElements import TasksWebElements
from xiqse.elements.admin.AdministrationWebElements import AdministrationWebElements
from xiqse.elements.connect.ConnectWebElements import ConnectWebElements


class XIQSE_CommonNavigator(CommonNavigatorWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.network_web_elements = NetworkWebElements()
        self.ae_web_elements = AlarmsEventsWebElements()
        self.control_web_elements = ControlWebElements()
        self.analytics_web_elements = AnalyticsWebElements()
        self.wireless_web_elements = WirelessWebElements()
        self.compliance_web_elements = ComplianceWebElements()
        self.reports_web_elements = ReportsWebElements()
        self.tasks_web_elements = TasksWebElements()
        self.admin_web_elements = AdministrationWebElements()
        self.connect_web_elements = ConnectWebElements()

    # Left Navigation Panel ---------------------------------------------------------------------------
    def xiqse_navigate_to_tab(self, tab_name):
        """
         - This keyword selects the specified tab in the main navigation panel
         - Keyword Usage
          - ``XIQSE Navigate to Tab    Network``
          - ``XIQSE Navigate to Tab    Administration``
          - ``XIQSE Navigate to Tab    Reports``

        :param tab_name: name of the sub tab to select
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        if tab_name == "Network":
            the_tab = self.get_network_tab()
        elif tab_name == "Alarms & Events":
            the_tab = self.get_alarms_and_events_tab()
        elif tab_name == "Control":
            the_tab = self.get_control_tab()
        elif tab_name == "Analytics":
            the_tab = self.get_analytics_tab()
        elif tab_name == "Wireless":
            the_tab = self.get_wireless_tab()
        elif tab_name == "Compliance":
            the_tab = self.get_compliance_tab()
        elif tab_name == "Reports":
            the_tab = self.get_reports_tab()
        elif tab_name == "Tasks":
            the_tab = self.get_tasks_tab()
        elif tab_name == "Administration":
            the_tab = self.get_administration_tab()
        elif tab_name == "Connect":
            the_tab = self.get_connect_tab()
        else:
            the_tab = None
        if the_tab:
            self.utils.print_info(f"Selecting '{tab_name}' tab in left navigation panel")
            self.auto_actions.click(the_tab)
            ret_val = 1
            sleep(2)
        else:
            self.utils.print_info(f"Unable to select tab with name '{tab_name}' in left navigation panel")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_navigate_to_network_tab(self):
        """
         - This keyword Navigates to the Network Tab
         - Keyword Usage
          - ``XIQSE Navigate To Network Tab``

        :return: 1 if Navigation Successful to Network Tab, else return -1
        """
        return self.xiqse_navigate_to_tab("Network")

    def xiqse_navigate_to_alarms_and_events_tab(self):
        """
         - This keyword Navigates to the Alarms & Events Tab
         - Keyword Usage
          - ``XIQSE Navigate To Alarms and Events Tab``

        :return: 1 if Navigation Successful to Alarms & Events Tab, else return -1
        """
        return self.xiqse_navigate_to_tab("Alarms & Events")

    def xiqse_navigate_to_control_tab(self):
        """
         - This keyword Navigates to the Control Tab
         - Keyword Usage
          - ``XIQSE Navigate To Control Tab``

        :return: 1 if Navigation Successful to Control Tab, else return -1
        """
        return self.xiqse_navigate_to_tab("Control")

    def xiqse_navigate_to_analytics_tab(self):
        """
         - This keyword Navigates to the Analytics Tab
         - Keyword Usage
          - ``XIQSE Navigate To Analytics Tab``

        :return: 1 if Navigation Successful to Analytics Tab, else return -1
        """
        return self.xiqse_navigate_to_tab("Analytics")

    def xiqse_navigate_to_wireless_tab(self):
        """
         - This keyword Navigates to the Wireless Tab
         - Keyword Usage
          - ``XIQSE Navigate To Wireless Tab``

        :return: 1 if Navigation Successful to Wireless Tab, else return -1
        """
        return self.xiqse_navigate_to_tab("Wireless")

    def xiqse_navigate_to_compliance_tab(self):
        """
         - This keyword Navigates to the Compliance Tab
         - Keyword Usage
          - ``XIQSE Navigate To Compliance Tab``

        :return: 1 if Navigation Successful to Compliance Tab, else return -1
        """
        return self.xiqse_navigate_to_tab("Compliance")

    def xiqse_navigate_to_reports_tab(self):
        """
         - This keyword Navigates to the Reports Tab
         - Keyword Usage
          - ``XIQSE Navigate To Reports Tab``

        :return: 1 if Navigation Successful to Reports Tab, else return -1
        """
        return self.xiqse_navigate_to_tab("Reports")

    def xiqse_navigate_to_tasks_tab(self):
        """
         - This keyword Navigates to the Tasks Tab
         - Keyword Usage
          - ``XIQSE Navigate To Tasks Tab``

        :return: 1 if Navigation Successful to Tasks Tab, else return -1
        """
        return self.xiqse_navigate_to_tab("Tasks")

    def xiqse_navigate_to_administration_tab(self):
        """
         - This keyword Navigates to the Administration Tab
         - Keyword Usage
          - ``XIQSE Navigate To Administration Tab``

        :return: 1 if Navigation Successful to Administration Tab, else return -1
        """
        return self.xiqse_navigate_to_tab("Administration")

    def xiqse_navigate_to_connect_tab(self):
        """
         - This keyword Navigates to the Connect Tab
         - Keyword Usage
          - ``XIQSE Navigate To Connect Tab``

        :return: 1 if Navigation Successful to Connect Tab, else return -1
        """
        return self.xiqse_navigate_to_tab("Connect")

    # Network Tab -------------------------------------------------------------------------------------
    def xiqse_navigate_to_network_dashboard_tab(self):
        """
         - This keyword Navigates to the Network> Dashboard Tab
         - Keyword Usage
          - ``XIQSE Navigate To Network Dashboard Tab``

        :return: 1 if Navigation Successful to Network> Dashboard Tab, else return -1
        """
        ret_val = -1
        if self.xiqse_navigate_to_network_tab():
            the_tab = self.network_web_elements.get_dashboard_tab()
            if the_tab:
                self.utils.print_info("Selecting Network> Dashboard Tab...")
                self.auto_actions.click(the_tab)
                ret_val = 1
                sleep(2)
            else:
                self.utils.print_info("Unable to navigate to Network> Dashboard tab")
                self.screen.save_screen_shot()
        return ret_val

    def xiqse_navigate_to_network_devices_tab(self):
        """
         - This keyword Navigates to the Network> Devices Tab
         - Keyword Usage
          - ``XIQSE Navigate To Network Devices Tab``

        :return: 1 if Navigation Successful to Network> Devices Tab, else return -1
        """
        ret_val = -1
        if self.xiqse_navigate_to_network_tab():
            the_tab = self.network_web_elements.get_devices_tab()
            if the_tab:
                self.utils.print_info("Selecting Network> Devices Tab...")
                self.auto_actions.click(the_tab)
                ret_val = 1
                sleep(2)
            else:
                self.utils.print_info("Unable to navigate to Network> Devices tab")
                self.screen.save_screen_shot()
        return ret_val

    def xiqse_navigate_to_network_discovered_tab(self):
        """
         - This keyword Navigates to the Network> Discovered Tab
         - Keyword Usage
          - ``XIQSE Navigate To Network Discovered Tab``

        :return: 1 if Navigation Successful to Network> Discovered Tab, else return -1
        """
        ret_val = -1
        if self.xiqse_navigate_to_network_tab():
            the_tab = self.network_web_elements.get_discovered_tab()
            if the_tab:
                self.utils.print_info("Selecting Network> Discovered Tab...")
                self.auto_actions.click(the_tab)
                ret_val = 1
                sleep(2)
            else:
                self.utils.print_info("Unable to navigate to Network> Discovered tab")
                self.screen.save_screen_shot()
        return ret_val

    def xiqse_navigate_to_network_firmware_tab(self):
        """
         - This keyword Navigates to the Network> Firmware Tab
         - Keyword Usage
          - ``XIQSE Navigate To Network Firmware Tab``

        :return: 1 if Navigation Successful to Network> Firmware Tab, else return -1
        """
        ret_val = -1
        if self.xiqse_navigate_to_network_tab():
            the_tab = self.network_web_elements.get_firmware_tab()
            if the_tab:
                self.utils.print_info("Selecting Network> Firmware Tab...")
                self.auto_actions.click(the_tab)
                ret_val = 1
                sleep(2)
            else:
                self.utils.print_info("Unable to navigate to Network> Firmware tab")
                self.screen.save_screen_shot()
        return ret_val

    def xiqse_navigate_to_network_archives_tab(self):
        """
         - This keyword Navigates to the Network> Archives Tab
         - Keyword Usage
          - ``XIQSE Navigate To Network Archives Tab``

        :return: 1 if Navigation Successful to Network> Archives Tab, else return -1
        """
        ret_val = -1
        if self.xiqse_navigate_to_network_tab():
            the_tab = self.network_web_elements.get_archives_tab()
            if the_tab:
                self.utils.print_info("Selecting Network> Archives Tab...")
                self.auto_actions.click(the_tab)
                ret_val = 1
                sleep(2)
            else:
                self.utils.print_info("Unable to navigate to Network> Archives tab")
                self.screen.save_screen_shot()
        return ret_val

    def xiqse_navigate_to_network_configuration_templates_tab(self):
        """
         - This keyword Navigates to the Network> Configuration Templates Tab
         - Keyword Usage
          - ``XIQSE Navigate To Network Configuration Templates Tab``

        :return: 1 if Navigation Successful to Network> Configuration Templates Tab, else return -1
        """
        ret_val = -1
        if self.xiqse_navigate_to_network_tab():
            the_tab = self.network_web_elements.get_configuration_templates_tab()
            if the_tab:
                self.utils.print_info("Selecting Network> Configuration Templates Tab...")
                self.auto_actions.click(the_tab)
                ret_val = 1
                sleep(2)
            else:
                self.utils.print_info("Unable to navigate to Network> Configuration Templates tab")
                self.screen.save_screen_shot()
        return ret_val

    def xiqse_navigate_to_network_reports_tab(self):
        """
         - This keyword Navigates to the Network> Reports Tab
         - Keyword Usage
          - ``XIQSE Navigate To Network Reports Tab``

        :return: 1 if Navigation Successful to Network> Reports Tab, else return -1
        """
        ret_val = -1
        if self.xiqse_navigate_to_network_tab():
            the_tab = self.network_web_elements.get_reports_tab()
            if the_tab:
                self.utils.print_info("Selecting Network> Reports Tab...")
                self.auto_actions.click(the_tab)
                ret_val = 1
                sleep(2)
            else:
                self.utils.print_info("Unable to navigate to Network> Reports tab")
                self.screen.save_screen_shot()
        return ret_val

    # Alarms & Events Tab ---------------------------------------------------------------------------------
    def xiqse_navigate_to_alarms_tab(self):
        """
         - This keyword Navigates to the Alarms & Events> Alarms Tab
         - Keyword Usage
          - ``XIQSE Navigate To Alarms Tab``

        :return: 1 if Navigation Successful to Alarms & Events> Alarms Tab, else return -1
        """
        ret_val = -1
        if self.xiqse_navigate_to_alarms_and_events_tab():
            the_tab = self.ae_web_elements.get_alarms_tab()
            if the_tab:
                self.utils.print_info("Selecting Alarms & Events> Alarms Tab...")
                self.auto_actions.click(the_tab)
                ret_val = 1
                sleep(2)
            else:
                self.utils.print_info("Unable to navigate to Alarms & Events> Alarms tab")
                self.screen.save_screen_shot()
        return ret_val

    def xiqse_navigate_to_alarm_configuration_tab(self):
        """
         - This keyword Navigates to the Alarms & Events> Alarms Tab
         - Keyword Usage
          - ``XIQSE Navigate To Alarm Configuration Tab``

        :return: 1 if Navigation Successful to Alarms & Events> Alarm Configuration Tab, else return -1
        """
        ret_val = -1
        if self.xiqse_navigate_to_alarms_and_events_tab():
            the_tab = self.ae_web_elements.get_alarm_configuration_tab()
            if the_tab:
                self.utils.print_info("Selecting Alarms & Events> Alarm Configuration Tab...")
                self.auto_actions.click(the_tab)
                ret_val = 1
                sleep(2)
            else:
                self.utils.print_info("Unable to navigate to Alarms & Events> Alarm Configuration tab")
                self.screen.save_screen_shot()
        return ret_val

    def xiqse_navigate_to_events_tab(self):
        """
         - This keyword Navigates to the Alarms & Events> Events Tab
         - Keyword Usage
          - ``XIQSE Navigate To Events Tab``

        :return: 1 if Navigation Successful to Alarms & Events> Events Tab, else return -1
        """
        ret_val = -1
        if self.xiqse_navigate_to_alarms_and_events_tab():
            the_tab = self.ae_web_elements.get_events_tab()
            if the_tab:
                self.utils.print_info("Selecting Alarms & Events> Events Tab...")
                self.auto_actions.click(the_tab)
                ret_val = 1
                sleep(2)
            else:
                self.utils.print_info("Unable to navigate to Alarms & Events> Events tab")
                self.screen.save_screen_shot()
        return ret_val

    def xiqse_navigate_to_event_configuration_tab(self):
        """
         - This keyword Navigates to the Alarms & Events> Event Configuration Tab
         - Keyword Usage
          - ``XIQSE Navigate To Event Configuration Tab``

        :return: 1 if Navigation Successful to Alarms & Events> Event Configuration Tab, else return -1
        """
        ret_val = -1
        if self.xiqse_navigate_to_alarms_and_events_tab():
            the_tab = self.ae_web_elements.get_event_configuration_tab()
            if the_tab:
                self.utils.print_info("Selecting Alarms & Events> Event Configuration Tab...")
                self.auto_actions.click(the_tab)
                ret_val = 1
                sleep(2)
            else:
                self.utils.print_info("Unable to navigate to Alarms & Events> Event Configuration tab")
                self.screen.save_screen_shot()
        return ret_val

    # Control Tab ---------------------------------------------------------------------------------
    def xiqse_navigate_to_control_dashboard_tab(self):
        """
         - This keyword Navigates to the Control> Dashboard Tab
         - Keyword Usage
          - ``XIQSE Navigate To Control Dashboard Tab``

        :return: 1 if Navigation Successful to Control> Dashboard Tab, else return -1
        """
        ret_val = -1
        if self.xiqse_navigate_to_control_tab():
            the_tab = self.control_web_elements.get_dashboard_tab()
            if the_tab:
                self.utils.print_info("Selecting Control> Dashboard Tab...")
                self.auto_actions.click(the_tab)
                ret_val = 1
                sleep(2)
            else:
                self.utils.print_info("Unable to navigate to Control> Dashboard tab")
                self.screen.save_screen_shot()
        return ret_val

    def xiqse_navigate_to_control_policy_tab(self):
        """
         - This keyword Navigates to the Control> Policy Tab
         - Keyword Usage
          - ``XIQSE Navigate To Control Policy Tab``

        :return: 1 if Navigation Successful to Control> Policy Tab, else return -1
        """
        ret_val = -1
        if self.xiqse_navigate_to_control_tab():
            the_tab = self.control_web_elements.get_policy_tab()
            if the_tab:
                self.utils.print_info("Selecting Control> Policy Tab...")
                self.auto_actions.click(the_tab)
                ret_val = 1
                sleep(2)
            else:
                self.utils.print_info("Unable to navigate to Control> Policy tab")
                self.screen.save_screen_shot()
        return ret_val

    def xiqse_navigate_to_control_access_control_tab(self):
        """
         - This keyword Navigates to the Control> Access Control Tab
         - Keyword Usage
          - ``XIQSE Navigate To Control Access Control Tab``

        :return: 1 if Navigation Successful to Control> Access Control Tab, else return -1
        """
        ret_val = -1
        if self.xiqse_navigate_to_control_tab():
            the_tab = self.control_web_elements.get_access_control_tab()
            if the_tab:
                self.utils.print_info("Selecting Control> Access Control Tab...")
                self.auto_actions.click(the_tab)
                ret_val = 1
                sleep(2)
            else:
                self.utils.print_info("Unable to navigate to Control> Access Control tab")
                self.screen.save_screen_shot()
        return ret_val

    def xiqse_navigate_to_control_end_systems_tab(self):
        """
         - This keyword Navigates to the Control> End-Systems Tab
         - Keyword Usage
          - ``XIQSE Navigate To Control End Systems Tab``

        :return: 1 if Navigation Successful to Control> End-Systems Tab, else return -1
        """
        ret_val = -1
        if self.xiqse_navigate_to_control_tab():
            the_tab = self.control_web_elements.get_end_systems_tab()
            if the_tab:
                self.utils.print_info("Selecting Control> End-Systems Tab...")
                self.auto_actions.click(the_tab)
                ret_val = 1
                sleep(2)
            else:
                self.utils.print_info("Unable to navigate to Control> End-Systems tab")
                self.screen.save_screen_shot()
        return ret_val

    def xiqse_navigate_to_control_reports_tab(self):
        """
         - This keyword Navigates to the Control> Reports Tab
         - Keyword Usage
          - ``XIQSE Navigate To Control Reports Tab``

        :return: 1 if Navigation Successful to Control> Reports Tab, else return -1
        """
        ret_val = -1
        if self.xiqse_navigate_to_control_tab():
            the_tab = self.control_web_elements.get_reports_tab()
            if the_tab:
                self.utils.print_info("Selecting Control> Reports Tab...")
                self.auto_actions.click(the_tab)
                ret_val = 1
                sleep(2)
            else:
                self.utils.print_info("Unable to navigate to Control> Reports tab")
                self.screen.save_screen_shot()
        return ret_val

    # Analytics Tab ---------------------------------------------------------------------------------
    def xiqse_navigate_to_analytics_dashboard_tab(self):
        """
         - This keyword Navigates to the Analytics> Dashboard Tab
         - Keyword Usage
          - ``XIQSE Navigate To Analytics Dashboard Tab``

        :return: 1 if Navigation Successful to Analytics> Dashboard Tab, else return -1
        """
        ret_val = -1
        if self.xiqse_navigate_to_analytics_tab():
            the_tab = self.analytics_web_elements.get_dashboard_tab()
            if the_tab:
                self.utils.print_info("Selecting Analytics> Dashboard Tab...")
                self.auto_actions.click(the_tab)
                ret_val = 1
                sleep(2)
            else:
                self.utils.print_info("Unable to navigate to Analytics> Dashboard tab")
                self.screen.save_screen_shot()
        return ret_val

    def xiqse_navigate_to_analytics_browser_tab(self):
        """
         - This keyword Navigates to the Analytics> Browser Tab
         - Keyword Usage
          - ``XIQSE Navigate To Analytics Browser Tab``

        :return: 1 if Navigation Successful to Analytics> Browser Tab, else return -1
        """
        ret_val = -1
        if self.xiqse_navigate_to_analytics_tab():
            the_tab = self.analytics_web_elements.get_browser_tab()
            if the_tab:
                self.utils.print_info("Selecting Analytics> Browser Tab...")
                self.auto_actions.click(the_tab)
                ret_val = 1
                sleep(2)
            else:
                self.utils.print_info("Unable to navigate to Analytics> Browser tab")
                self.screen.save_screen_shot()
        return ret_val

    def xiqse_navigate_to_analytics_application_flows_tab(self):
        """
         - This keyword Navigates to the Analytics> Application Flows Tab
         - Keyword Usage
          - ``XIQSE Navigate To Analytics Application Flows Tab``

        :return: 1 if Navigation Successful to Analytics> Application Flows Tab, else return -1
        """
        ret_val = -1
        if self.xiqse_navigate_to_analytics_tab():
            the_tab = self.analytics_web_elements.get_application_flows_tab()
            if the_tab:
                self.utils.print_info("Selecting Analytics> Application Flows Tab...")
                self.auto_actions.click(the_tab)
                ret_val = 1
                sleep(2)
            else:
                self.utils.print_info("Unable to navigate to Analytics> Application Flows tab")
                self.screen.save_screen_shot()
        return ret_val

    def xiqse_navigate_to_analytics_fingerprints_tab(self):
        """
         - This keyword Navigates to the Analytics> Fingerprints Tab
         - Keyword Usage
          - ``XIQSE Navigate To Analytics Fingerprints Tab``

        :return: 1 if Navigation Successful to Analytics> Fingerprints Tab, else return -1
        """
        ret_val = -1
        if self.xiqse_navigate_to_analytics_tab():
            the_tab = self.analytics_web_elements.get_fingerprints_tab()
            if the_tab:
                self.utils.print_info("Selecting Analytics> Fingerprints Tab...")
                self.auto_actions.click(the_tab)
                ret_val = 1
                sleep(2)
            else:
                self.utils.print_info("Unable to navigate to Analytics> Fingerprints tab")
                self.screen.save_screen_shot()
        return ret_val

    def xiqse_navigate_to_analytics_packet_captures_tab(self):
        """
         - This keyword Navigates to the Analytics> Packet Captures Tab
         - Keyword Usage
          - ``XIQSE Navigate To Analytics Packet Captures Tab``

        :return: 1 if Navigation Successful to Analytics> Packet Captures Tab, else return -1
        """
        ret_val = -1
        if self.xiqse_navigate_to_analytics_tab():
            the_tab = self.analytics_web_elements.get_packet_captures_tab()
            if the_tab:
                self.utils.print_info("Selecting Analytics> Packet Captures Tab...")
                self.auto_actions.click(the_tab)
                ret_val = 1
                sleep(2)
            else:
                self.utils.print_info("Unable to navigate to Analytics> Packet Captures tab")
                self.screen.save_screen_shot()
        return ret_val

    def xiqse_navigate_to_analytics_configuration_tab(self):
        """
         - This keyword Navigates to the Analytics> Configuration Tab
         - Keyword Usage
          - ``XIQSE Navigate To Analytics Configuration Tab``

        :return: 1 if Navigation Successful to Analytics> Configuration Tab, else return -1
        """
        ret_val = -1
        if self.xiqse_navigate_to_analytics_tab():
            the_tab = self.analytics_web_elements.get_configuration_tab()
            if the_tab:
                self.utils.print_info("Selecting Analytics> Configuration Tab...")
                self.auto_actions.click(the_tab)
                ret_val = 1
                sleep(2)
            else:
                self.utils.print_info("Unable to navigate to Analytics> Configuration tab")
                self.screen.save_screen_shot()
        return ret_val

    def xiqse_navigate_to_analytics_reports_tab(self):
        """
         - This keyword Navigates to the Analytics> Reports Tab
         - Keyword Usage
          - ``XIQSE Navigate To Analytics Reports Tab``

        :return: 1 if Navigation Successful to Analytics> Reports Tab, else return -1
        """
        ret_val = -1
        if self.xiqse_navigate_to_analytics_tab():
            the_tab = self.analytics_web_elements.get_reports_tab()
            if the_tab:
                self.utils.print_info("Selecting Analytics> Reports Tab...")
                self.auto_actions.click(the_tab)
                ret_val = 1
                sleep(2)
            else:
                self.utils.print_info("Unable to navigate to Analytics> Reports tab")
                self.screen.save_screen_shot()
        return ret_val

    # Wireless Tab ---------------------------------------------------------------------------------
    def xiqse_navigate_to_wireless_dashboard_tab(self):
        """
         - This keyword Navigates to the Wireless> Dashboard Tab
         - Keyword Usage
          - ``XIQSE Navigate To Wireless Dashboard Tab``

        :return: 1 if Navigation Successful to Wireless> Dashboard Tab, else return -1
        """
        ret_val = -1
        if self.xiqse_navigate_to_wireless_tab():
            the_tab = self.wireless_web_elements.get_dashboard_tab()
            if the_tab:
                self.utils.print_info("Selecting Wireless> Dashboard Tab...")
                self.auto_actions.click(the_tab)
                ret_val = 1
                sleep(2)
            else:
                self.utils.print_info("Unable to navigate to Wireless> Dashboard tab")
                self.screen.save_screen_shot()
        return ret_val

    def xiqse_navigate_to_wireless_network_tab(self):
        """
         - This keyword Navigates to the Wireless> Network Tab
         - Keyword Usage
          - ``XIQSE Navigate To Wireless Network Tab``

        :return: 1 if Navigation Successful to Wireless> Network Tab, else return -1
        """
        ret_val = -1
        if self.xiqse_navigate_to_wireless_tab():
            the_tab = self.wireless_web_elements.get_network_tab()
            if the_tab:
                self.utils.print_info("Selecting Wireless> Network Tab...")
                self.auto_actions.click(the_tab)
                ret_val = 1
                sleep(2)
            else:
                self.utils.print_info("Unable to navigate to Wireless> Network tab")
                self.screen.save_screen_shot()
        return ret_val

    def xiqse_navigate_to_wireless_controllers_tab(self):
        """
         - This keyword Navigates to the Wireless> Controllers Tab
         - Keyword Usage
          - ``XIQSE Navigate To Wireless Controllers Tab``

        :return: 1 if Navigation Successful to Wireless> Controllers Tab, else return -1
        """
        ret_val = -1
        if self.xiqse_navigate_to_wireless_tab():
            the_tab = self.wireless_web_elements.get_controllers_tab()
            if the_tab:
                self.utils.print_info("Selecting Wireless> Controllers Tab...")
                self.auto_actions.click(the_tab)
                ret_val = 1
                sleep(2)
            else:
                self.utils.print_info("Unable to navigate to Wireless> Controllers tab")
                self.screen.save_screen_shot()
        return ret_val

    def xiqse_navigate_to_wireless_access_points_tab(self):
        """
         - This keyword Navigates to the Wireless> Access Points Tab
         - Keyword Usage
          - ``XIQSE Navigate To Wireless Access Points Tab``

        :return: 1 if Navigation Successful to Wireless> Access Points Tab, else return -1
        """
        ret_val = -1
        if self.xiqse_navigate_to_wireless_tab():
            the_tab = self.wireless_web_elements.get_access_points_tab()
            if the_tab:
                self.utils.print_info("Selecting Wireless> Access Points Tab...")
                self.auto_actions.click(the_tab)
                ret_val = 1
                sleep(2)
            else:
                self.utils.print_info("Unable to navigate to Wireless> Access Points tab")
                self.screen.save_screen_shot()
        return ret_val

    def xiqse_navigate_to_wireless_clients_tab(self):
        """
         - This keyword Navigates to the Wireless> Clients Tab
         - Keyword Usage
          - ``XIQSE Navigate To Wireless Clients Tab``

        :return: 1 if Navigation Successful to Wireless> Clients Tab, else return -1
        """
        ret_val = -1
        if self.xiqse_navigate_to_wireless_tab():
            the_tab = self.wireless_web_elements.get_clients_tab()
            if the_tab:
                self.utils.print_info("Selecting Wireless> Clients Tab...")
                self.auto_actions.click(the_tab)
                ret_val = 1
                sleep(2)
            else:
                self.utils.print_info("Unable to navigate to Wireless> Clients tab")
                self.screen.save_screen_shot()
        return ret_val

    def xiqse_navigate_to_wireless_threats_tab(self):
        """
         - This keyword Navigates to the Wireless> Threats Tab
         - Keyword Usage
          - ``XIQSE Navigate To Wireless Threats Tab``

        :return: 1 if Navigation Successful to Wireless> Threats Tab, else return -1
        """
        ret_val = -1
        if self.xiqse_navigate_to_wireless_tab():
            the_tab = self.wireless_web_elements.get_threats_tab()
            if the_tab:
                self.utils.print_info("Selecting Wireless> Threats Tab...")
                self.auto_actions.click(the_tab)
                ret_val = 1
                sleep(2)
            else:
                self.utils.print_info("Unable to navigate to Wireless> Threats tab")
                self.screen.save_screen_shot()
        return ret_val

    def xiqse_navigate_to_wireless_reports_tab(self):
        """
         - This keyword Navigates to the Wireless> Reports Tab
         - Keyword Usage
          - ``XIQSE Navigate To Wireless Reports Tab``

        :return: 1 if Navigation Successful to Wireless> Reports Tab, else return -1
        """
        ret_val = -1
        if self.xiqse_navigate_to_wireless_tab():
            the_tab = self.wireless_web_elements.get_reports_tab()
            if the_tab:
                self.utils.print_info("Selecting Wireless> Reports Tab...")
                self.auto_actions.click(the_tab)
                ret_val = 1
                sleep(2)
            else:
                self.utils.print_info("Unable to navigate to Wireless> Reports tab")
                self.screen.save_screen_shot()
        return ret_val

    # Compliance Tab ---------------------------------------------------------------------------------
    def xiqse_navigate_to_compliance_dashboard_tab(self):
        """
         - This keyword Navigates to the Compliance> Dashboard Tab
         - Keyword Usage
          - ``XIQSE Navigate To Compliance Dashboard Tab``

        :return: 1 if Navigation Successful to Compliance> Dashboard Tab, else return -1
        """
        ret_val = -1
        if self.xiqse_navigate_to_compliance_tab():
            the_tab = self.compliance_web_elements.get_dashboard_tab()
            if the_tab:
                self.utils.print_info("Selecting Compliance> Dashboard Tab...")
                self.auto_actions.click(the_tab)
                ret_val = 1
                sleep(2)
            else:
                self.utils.print_info("Unable to navigate to Compliance> Dashboard tab")
                self.screen.save_screen_shot()
        return ret_val

    def xiqse_navigate_to_compliance_audit_tests_tab(self):
        """
         - This keyword Navigates to the Compliance> Audit Tests Tab
         - Keyword Usage
          - ``XIQSE Navigate To Compliance Audit Tests Tab``

        :return: 1 if Navigation Successful to Compliance> Audit Tests Tab, else return -1
        """
        ret_val = -1
        if self.xiqse_navigate_to_compliance_tab():
            the_tab = self.compliance_web_elements.get_audit_tests_tab()
            if the_tab:
                self.utils.print_info("Selecting Compliance> Audit Tests Tab...")
                self.auto_actions.click(the_tab)
                ret_val = 1
                sleep(2)
            else:
                self.utils.print_info("Unable to navigate to Compliance> Audit Tests tab")
                self.screen.save_screen_shot()
        return ret_val

    # Reports Tab ---------------------------------------------------------------------------------
    def xiqse_navigate_to_reports_reports_tab(self):
        """
         - This keyword Navigates to the Reports> Reports Tab
         - Keyword Usage
          - ``XIQSE Navigate To Reports Reports Tab``

        :return: 1 if Navigation Successful to Reports> Reports Tab, else return -1
        """
        ret_val = -1
        if self.xiqse_navigate_to_reports_tab():
            the_tab = self.reports_web_elements.get_reports_tab()
            if the_tab:
                self.utils.print_info("Selecting Reports> Reports Tab...")
                self.auto_actions.click(the_tab)
                ret_val = 1
                sleep(2)
            else:
                self.utils.print_info("Unable to navigate to Reports> Reports tab")
                self.screen.save_screen_shot()
        return ret_val

    def xiqse_navigate_to_reports_custom_report_tab(self):
        """
         - This keyword Navigates to the Reports> Custom Report Tab
         - Keyword Usage
          - ``XIQSE Navigate To Reports Custom Report Tab``

        :return: 1 if Navigation Successful to Reports> Custom Report Tab, else return -1
        """
        ret_val = -1
        if self.xiqse_navigate_to_reports_tab():
            the_tab = self.reports_web_elements.get_custom_report_tab()
            if the_tab:
                self.utils.print_info("Selecting Reports> Custom Report Tab...")
                self.auto_actions.click(the_tab)
                ret_val = 1
                sleep(2)
            else:
                self.utils.print_info("Unable to navigate to Reports> Custom Report tab")
                self.screen.save_screen_shot()
        return ret_val

    def xiqse_navigate_to_reports_report_designer_tab(self):
        """
         - This keyword Navigates to the Reports> Report Designer Tab
         - Keyword Usage
          - ``XIQSE Navigate To Reports Report Designer Tab``

        :return: 1 if Navigation Successful to Reports> Report Designer Tab, else return -1
        """
        ret_val = -1
        if self.xiqse_navigate_to_reports_tab():
            the_tab = self.reports_web_elements.get_report_designer_tab()
            if the_tab:
                self.utils.print_info("Selecting Reports> Report Designer Tab...")
                self.auto_actions.click(the_tab)
                ret_val = 1
                sleep(2)
            else:
                self.utils.print_info("Unable to navigate to Reports> Report Designer tab")
                self.screen.save_screen_shot()
        return ret_val

    # Tasks Tab ---------------------------------------------------------------------------------
    def xiqse_navigate_to_tasks_workflow_dashboard_tab(self):
        """
         - This keyword Navigates to the Tasks> Workflow Dashboard Tab
         - Keyword Usage
          - ``XIQSE Navigate To Tasks Workflow Dashboard Tab``

        :return: 1 if Navigation Successful to Tasks> Workflow Dashboard Tab, else return -1
        """
        ret_val = -1
        if self.xiqse_navigate_to_tasks_tab():
            the_tab = self.tasks_web_elements.get_workflow_dashboard_tab()
            if the_tab:
                self.utils.print_info("Selecting Tasks> Workflow Dashboard Tab...")
                self.auto_actions.click(the_tab)
                ret_val = 1
                sleep(2)
            else:
                self.utils.print_info("Unable to navigate to Tasks> Workflow Dashboard tab")
                self.screen.save_screen_shot()
        return ret_val

    def xiqse_navigate_to_tasks_scheduled_tasks_tab(self):
        """
         - This keyword Navigates to the Tasks> Scheduled Tasks Tab
         - Keyword Usage
          - ``XIQSE Navigate To Tasks Scheduled Tasks Tab``

        :return: 1 if Navigation Successful to Tasks> Scheduled Tasks Tab, else return -1
        """
        ret_val = -1
        if self.xiqse_navigate_to_tasks_tab():
            the_tab = self.tasks_web_elements.get_scheduled_tasks_tab()
            if the_tab:
                self.utils.print_info("Selecting Tasks> Scheduled Tasks Tab...")
                self.auto_actions.click(the_tab)
                ret_val = 1
                sleep(2)
            else:
                self.utils.print_info("Unable to navigate to Tasks> Scheduled Tasks tab")
                self.screen.save_screen_shot()
        return ret_val

    def xiqse_navigate_to_tasks_saved_tasks_tab(self):
        """
         - This keyword Navigates to the Tasks> Saved Tasks Tab
         - Keyword Usage
          - ``XIQSE Navigate To Tasks Saved Tasks Tab``

        :return: 1 if Navigation Successful to Tasks> Saved Tasks Tab, else return -1
        """
        ret_val = -1
        if self.xiqse_navigate_to_tasks_tab():
            the_tab = self.tasks_web_elements.get_saved_tasks_tab()
            if the_tab:
                self.utils.print_info("Selecting Tasks> Saved Tasks Tab...")
                self.auto_actions.click(the_tab)
                ret_val = 1
                sleep(2)
            else:
                self.utils.print_info("Unable to navigate to Tasks> Saved Tasks tab")
                self.screen.save_screen_shot()
        return ret_val

    def xiqse_navigate_to_tasks_scripts_tab(self):
        """
         - This keyword Navigates to the Tasks> Scripts Tab
         - Keyword Usage
          - ``XIQSE Navigate To Tasks Scripts Tab``

        :return: 1 if Navigation Successful to Tasks> Scripts Tab, else return -1
        """
        ret_val = -1
        if self.xiqse_navigate_to_tasks_tab():
            the_tab = self.tasks_web_elements.get_scripts_tab()
            if the_tab:
                self.utils.print_info("Selecting Tasks> Scripts Tab...")
                self.auto_actions.click(the_tab)
                ret_val = 1
                sleep(2)
            else:
                self.utils.print_info("Unable to navigate to Tasks> Scripts tab")
                self.screen.save_screen_shot()
        return ret_val

    def xiqse_navigate_to_tasks_workflows_tab(self):
        """
         - This keyword Navigates to the Tasks> Workflows Tab
         - Keyword Usage
          - ``XIQSE Navigate To Tasks Workflows Tab``

        :return: 1 if Navigation Successful to Tasks> Workflows Tab, else return -1
        """
        ret_val = -1
        if self.xiqse_navigate_to_tasks_tab():
            the_tab = self.tasks_web_elements.get_workflows_tab()
            if the_tab:
                self.utils.print_info("Selecting Tasks> Workflows Tab...")
                self.auto_actions.click(the_tab)
                ret_val = 1
                sleep(2)
            else:
                self.utils.print_info("Unable to navigate to Tasks> Workflows tab")
                self.screen.save_screen_shot()
        return ret_val

    # Administration Tab ---------------------------------------------------------------------------------
    def xiqse_navigate_to_admin_profiles_tab(self):
        """
         - This keyword Navigates to the Administration> Profiles Tab
         - Keyword Usage
          - ``XIQSE Navigate To Admin Profiles Tab``

        :return: 1 if Navigation Successful to Administration> Profiles Tab, else return -1
        """
        ret_val = -1
        if self.xiqse_navigate_to_administration_tab():
            the_tab = self.admin_web_elements.get_profiles_tab()
            if the_tab:
                self.utils.print_info("Selecting Administration> Profiles Tab...")
                self.auto_actions.click(the_tab)
                ret_val = 1
                sleep(2)
            else:
                self.utils.print_info("Unable to navigate to Administration> Profiles tab")
                self.screen.save_screen_shot()
        return ret_val

    def xiqse_navigate_to_admin_users_tab(self):
        """
         - This keyword Navigates to the Administration> Users Tab
         - Keyword Usage
          - ``XIQSE Navigate To Admin Users Tab``

        :return: 1 if Navigation Successful to Administration> Users Tab, else return -1
        """
        ret_val = -1
        if self.xiqse_navigate_to_administration_tab():
            the_tab = self.admin_web_elements.get_users_tab()
            if the_tab:
                self.utils.print_info("Selecting Administration> Users Tab...")
                self.auto_actions.click(the_tab)
                ret_val = 1
                sleep(2)
            else:
                self.utils.print_info("Unable to navigate to Administration> Users tab")
                self.screen.save_screen_shot()
        return ret_val

    def xiqse_navigate_to_admin_server_information_tab(self):
        """
         - This keyword Navigates to the Administration> Server Information Tab
         - Keyword Usage
          - ``XIQSE Navigate To Admin Server Information Tab``

        :return: 1 if Navigation Successful to Administration> Server Information Tab, else return -1
        """
        ret_val = -1
        if self.xiqse_navigate_to_administration_tab():
            the_tab = self.admin_web_elements.get_server_information_tab()
            if the_tab:
                self.utils.print_info("Selecting Administration> Server Information Tab...")
                self.auto_actions.click(the_tab)
                ret_val = 1
                sleep(2)
            else:
                self.utils.print_info("Unable to navigate to Administration> Server Information tab")
                self.screen.save_screen_shot()
        return ret_val

    def xiqse_navigate_to_admin_licenses_tab(self):
        """
         - This keyword Navigates to the Administration> Licenses Tab
         - Keyword Usage
          - ``XIQSE Navigate To Admin Licenses Tab``

        :return: 1 if Navigation Successful to Administration> Licenses Tab, else return -1
        """
        ret_val = -1
        if self.xiqse_navigate_to_administration_tab():
            the_tab = self.admin_web_elements.get_licenses_tab()
            if the_tab:
                self.utils.print_info("Selecting Administration> Licenses Tab...")
                self.auto_actions.click(the_tab)
                ret_val = 1
                sleep(2)
            else:
                self.utils.print_info("Unable to navigate to Administration> Licenses tab")
                self.screen.save_screen_shot()
        return ret_val

    def xiqse_navigate_to_admin_certificates_tab(self):
        """
         - This keyword Navigates to the Administration> Certificates Tab
         - Keyword Usage
          - ``XIQSE Navigate To Admin Certificates Tab``

        :return: 1 if Navigation Successful to Administration> Certificates Tab, else return -1
        """
        ret_val = -1
        if self.xiqse_navigate_to_administration_tab():
            the_tab = self.admin_web_elements.get_certificates_tab()
            if the_tab:
                self.utils.print_info("Selecting Administration> Certificates Tab...")
                self.auto_actions.click(the_tab)
                ret_val = 1
                sleep(2)
            else:
                self.utils.print_info("Unable to navigate to Administration> Certificates tab")
                self.screen.save_screen_shot()
        return ret_val

    def xiqse_navigate_to_admin_options_tab(self):
        """
         - This keyword Navigates to the Administration> Options Tab
         - Keyword Usage
          - ``XIQSE Navigate To Admin Options Tab``

        :return: 1 if Navigation Successful to Administration> Options Tab, else return -1
        """
        ret_val = -1
        if self.xiqse_navigate_to_administration_tab():
            the_tab = self.admin_web_elements.get_options_tab()
            if the_tab:
                self.utils.print_info("Selecting Administration> Options Tab...")
                self.auto_actions.click(the_tab)
                ret_val = 1
                sleep(2)
            else:
                self.utils.print_info("Unable to navigate to Administration> Options tab")
                self.screen.save_screen_shot()
        return ret_val

    def xiqse_navigate_to_admin_device_types_tab(self):
        """
         - This keyword Navigates to the Administration> Device Types Tab
         - Keyword Usage
          - ``XIQSE Navigate To Admin Device Types Tab``

        :return: 1 if Navigation Successful to Administration> Device Types Tab, else return -1
        """
        ret_val = -1
        if self.xiqse_navigate_to_administration_tab():
            the_tab = self.admin_web_elements.get_device_types_tab()
            if the_tab:
                self.utils.print_info("Selecting Administration> Device Types Tab...")
                self.auto_actions.click(the_tab)
                ret_val = 1
                sleep(2)
            else:
                self.utils.print_info("Unable to navigate to Administration> Device Types tab")
                self.screen.save_screen_shot()
        return ret_val

    def xiqse_navigate_to_admin_backup_restore_tab(self):
        """
         - This keyword Navigates to the Administration> Backup/Restore Tab
         - Keyword Usage
          - ``XIQSE Navigate To Admin Backup Restore Tab``

        :return: 1 if Navigation Successful to Administration> Backup/Restore Tab, else return -1
        """
        ret_val = -1
        if self.xiqse_navigate_to_administration_tab():
            the_tab = self.admin_web_elements.get_backup_restore_tab()
            if the_tab:
                self.utils.print_info("Selecting Administration> Backup/Restore Tab...")
                self.auto_actions.click(the_tab)
                ret_val = 1
                sleep(2)
            else:
                self.utils.print_info("Unable to navigate to Administration> Backup/Restore tab")
                self.screen.save_screen_shot()
        return ret_val

    def xiqse_navigate_to_admin_diagnostics_tab(self):
        """
         - This keyword Navigates to the Administration> Diagnostics Tab
         - Keyword Usage
          - ``XIQSE Navigate To Admin Diagnostics Tab``

        :return: 1 if Navigation Successful to Administration> Diagnostics Tab, else return -1
        """
        ret_val = -1
        if self.xiqse_navigate_to_administration_tab():
            the_tab = self.admin_web_elements.get_diagnostics_tab()
            if the_tab:
                self.utils.print_info("Selecting Administration> Diagnostics Tab...")
                self.auto_actions.click(the_tab)
                ret_val = 1
                sleep(2)
            else:
                self.utils.print_info("Unable to navigate to Administration> Diagnostics tab")
                self.screen.save_screen_shot()
        return ret_val

    def xiqse_navigate_to_admin_client_api_access_tab(self):
        """
         - This keyword Navigates to the Administration> Client API Access Tab
         - Keyword Usage
          - ``XIQSE Navigate To Admin Client API Access Tab``

        :return: 1 if Navigation Successful to Administration> Client API Access Tab, else return -1
        """
        ret_val = -1
        if self.xiqse_navigate_to_administration_tab():
            the_tab = self.admin_web_elements.get_client_api_access_tab()
            if the_tab:
                self.utils.print_info("Selecting Administration> Client API Access Tab...")
                self.auto_actions.click(the_tab)
                ret_val = 1
                sleep(2)
            else:
                self.utils.print_info("Unable to navigate to Administration> Client API Access tab")
                self.screen.save_screen_shot()
        return ret_val

    # Connect Tab ---------------------------------------------------------------------------------
    def xiqse_navigate_to_connect_configuration_tab(self):
        """
         - This keyword Navigates to the Connect> Configuration Tab
         - Keyword Usage
          - ``XIQSE Navigate To Connect Configuration Tab``

        :return: 1 if Navigation Successful to Connect> Configuration Tab, else return -1
        """
        ret_val = -1
        if self.xiqse_navigate_to_connect_tab():
            the_tab = self.connect_web_elements.get_configuration_tab()
            if the_tab:
                self.utils.print_info("Selecting Connect> Configuration Tab...")
                self.auto_actions.click(the_tab)
                ret_val = 1
                sleep(2)
            else:
                self.utils.print_info("Unable to navigate to Connect> Configuration tab")
                self.screen.save_screen_shot()
        return ret_val

    def xiqse_navigate_to_connect_diagnostics_tab(self):
        """
         - This keyword Navigates to the Connect> Diagnostics Tab
         - Keyword Usage
          - ``XIQSE Navigate To Connect Diagnostics Tab``

        :return: 1 if Navigation Successful to Connect> Diagnostics Tab, else return -1
        """
        ret_val = -1
        if self.xiqse_navigate_to_connect_tab():
            the_tab = self.connect_web_elements.get_diagnostics_tab()
            if the_tab:
                self.utils.print_info("Selecting Connect> Diagnostics Tab...")
                self.auto_actions.click(the_tab)
                ret_val = 1
                sleep(2)
            else:
                self.utils.print_info("Unable to navigate to Connect> Diagnostics tab")
                self.screen.save_screen_shot()
        return ret_val

    def xiqse_navigate_to_connect_services_api_tab(self):
        """
         - This keyword Navigates to the Connect> Services API Tab
         - Keyword Usage
          - ``XIQSE Navigate To Connect Services API Tab``

        :return: 1 if Navigation Successful to Connect> Services API Tab, else return -1
        """
        ret_val = -1
        if self.xiqse_navigate_to_connect_tab():
            the_tab = self.connect_web_elements.get_services_api_tab()
            if the_tab:
                self.utils.print_info("Selecting Connect> Services API Tab...")
                self.auto_actions.click(the_tab)
                ret_val = 1
                sleep(2)
            else:
                self.utils.print_info("Unable to navigate to Connect> Services API tab")
                self.screen.save_screen_shot()
        return ret_val
