from time import sleep
from extauto.common.CloudDriver import CloudDriver
from extauto.common.Screen import Screen
from extauto.common.Utils import Utils
from extauto.common.AutoActions import AutoActions
from extauto.xiq.flows.common.Navigator import Navigator
from extauto.xiq.elements.extreme_guest.ExtremeGuestDashboardWebElements import ExtremeGuestDashboardWebElements
from extauto.xiq.flows.extreme_guest.ExtremeGuest import ExtremeGuest


class Dashboard(object):
    def __init__(self):
        super().__init__()
        self.navigator = Navigator()
        # self.driver = extauto.common.CloudDriver.cloud_driver
        self.screen = Screen()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.dashboard_web_elem = ExtremeGuestDashboardWebElements()
        self.ext_guest = ExtremeGuest()

    def go_to_extreme_guest_dashboard_page(self):
        """
        -This keyword Will Navigate to Extreme Guest Dashboard Page
        - Flow: Extreme Guest--> More Insights-->Extreme Guest Menu Window-- Monitor--> dashboard
        - Keyword Usage:
            ''Go To Extreme Guest Dashboard Page''

        :return: 1 if navigation success
        """
        self.ext_guest.go_to_extreme_guest_monitor_dashboard_page()
        return 1

    def create_new_extreme_guest_dashboard(self, dashboard_name="automation_db1"):
        """
        -This keyword Will Create a new dashboard with theme 15 and 9 widgets
        - Flow: dashboard--> create new
        - Keyword Usage:
            ''create new extreme guest dashboard''

        :return: 1 if navigation success
        """
        self.utils.print_info("Clicking the Create New tab ")
        self.auto_actions.click_reference(self.dashboard_web_elem.get_extreme_guest_dashboard_create_new_tab)
        sleep(5)

        self.utils.print_info("Dragging the Theme15 into the main canvas ")
        self.auto_actions.drag_and_drop_element(
            self.dashboard_web_elem.get_extreme_guest_dashboard_create_new_theme15(),
            self.dashboard_web_elem.get_extreme_guest_dashboard_create_new_theme_canvas())
        sleep(2)

        self.utils.print_info("Clicking the theme/widget toggle button ")
        self.auto_actions.click_reference(
            self.dashboard_web_elem.get_extreme_guest_dashboard_create_new_theme_widget_toggle_button)
        sleep(2)

        client_panel_expand_status = self.dashboard_web_elem.get_extreme_guest_dashboard_create_new_theme_widget_client_panel().get_attribute(
            'aria-expanded')
        if client_panel_expand_status == "false":
            self.utils.print_info("Clicking the client panel ")
            self.auto_actions.click_reference(
                self.dashboard_web_elem.get_extreme_guest_dashboard_create_new_theme_widget_client_panel)
            sleep(2)

        self.utils.print_info("Dragging the widget1 into the canvas1 ")
        self.auto_actions.drag_and_drop_element(
            self.dashboard_web_elem.get_extreme_guest_dashboard_create_new_theme_widget_client_widget1(),
            self.dashboard_web_elem.get_extreme_guest_dashboard_create_new_theme15_canvas1())
        sleep(3)
        self.utils.print_info("Dragging the widget2 into the canvas2 ")
        self.auto_actions.drag_and_drop_element(
            self.dashboard_web_elem.get_extreme_guest_dashboard_create_new_theme_widget_client_widget2(),
            self.dashboard_web_elem.get_extreme_guest_dashboard_create_new_theme15_canvas2())
        sleep(3)
        self.utils.print_info("Dragging the widget3 into the canvas3 ")
        self.auto_actions.drag_and_drop_element(
            self.dashboard_web_elem.get_extreme_guest_dashboard_create_new_theme_widget_client_widget3(),
            self.dashboard_web_elem.get_extreme_guest_dashboard_create_new_theme15_canvas3())
        sleep(3)

        users_panel_expand_status = self.dashboard_web_elem.get_extreme_guest_dashboard_create_new_theme_widget_users_panel().get_attribute(
            'aria-expanded')
        if users_panel_expand_status == "false":
            self.utils.print_info("Clicking the users panel ")
            self.auto_actions.click_reference(
                self.dashboard_web_elem.get_extreme_guest_dashboard_create_new_theme_widget_users_panel)
            sleep(2)

        self.utils.print_info("Dragging the widget1 into the canvas4 ")
        self.auto_actions.drag_and_drop_element(
            self.dashboard_web_elem.get_extreme_guest_dashboard_create_new_theme_widget_users_widget1(),
            self.dashboard_web_elem.get_extreme_guest_dashboard_create_new_theme15_canvas4())
        sleep(3)
        self.utils.print_info("Dragging the widget3 into the canvas5 ")
        self.auto_actions.drag_and_drop_element(
            self.dashboard_web_elem.get_extreme_guest_dashboard_create_new_theme_widget_users_widget3(),
            self.dashboard_web_elem.get_extreme_guest_dashboard_create_new_theme15_canvas5())
        sleep(3)
        self.utils.print_info("Dragging the widget5 into the canvas6 ")
        self.auto_actions.drag_and_drop_element(
            self.dashboard_web_elem.get_extreme_guest_dashboard_create_new_theme_widget_users_widget5(),
            self.dashboard_web_elem.get_extreme_guest_dashboard_create_new_theme15_canvas6())
        sleep(3)

        usage_panel_expand_status = self.dashboard_web_elem.get_extreme_guest_dashboard_create_new_theme_widget_usage_panel().get_attribute(
            'aria-expanded')
        if usage_panel_expand_status == "false":
            self.utils.print_info("Clicking the usage panel ")
            self.auto_actions.click_reference(
                self.dashboard_web_elem.get_extreme_guest_dashboard_create_new_theme_widget_usage_panel)
            sleep(2)

        self.auto_actions.click(
            self.dashboard_web_elem.get_extreme_guest_dashboard_create_new_theme15_canvas9())
        sleep(2)

        self.utils.print_info("Dragging the widget1 into the canvas7 ")
        self.auto_actions.drag_and_drop_element(
            self.dashboard_web_elem.get_extreme_guest_dashboard_create_new_theme_widget_usage_widget1(),
            self.dashboard_web_elem.get_extreme_guest_dashboard_create_new_theme15_canvas7())
        sleep(3)
        self.utils.print_info("Dragging the widget3 into the canvas8 ")
        self.auto_actions.drag_and_drop_element(
            self.dashboard_web_elem.get_extreme_guest_dashboard_create_new_theme_widget_usage_widget2(),
            self.dashboard_web_elem.get_extreme_guest_dashboard_create_new_theme15_canvas8())
        sleep(3)
        self.auto_actions.move_to_element(
            self.dashboard_web_elem.get_extreme_guest_dashboard_create_new_theme15_canvas9())
        self.utils.print_info("Dragging the widget5 into the canvas9 ")
        self.auto_actions.drag_and_drop_element(
            self.dashboard_web_elem.get_extreme_guest_dashboard_create_new_theme_widget_usage_widget3(),
            self.dashboard_web_elem.get_extreme_guest_dashboard_create_new_theme15_canvas9())
        sleep(3)

        self.utils.print_info("Clicking the save button ")
        self.auto_actions.click_reference(
            self.dashboard_web_elem.get_extreme_guest_dashboard_create_new_theme_widget_save_button)
        sleep(2)

        self.utils.print_info("Entering Dashboard name  ", )
        self.auto_actions.double_click(
            self.dashboard_web_elem.get_extreme_guest_dashboard_create_new_theme_widget_save_dashboard_name_textbox())
        sleep(2)
        self.auto_actions.send_keys(
            self.dashboard_web_elem.get_extreme_guest_dashboard_create_new_theme_widget_save_dashboard_name_textbox(),
            dashboard_name)
        sleep(2)

        self.utils.print_info("Clicking the save button ")
        self.auto_actions.click_reference(
            self.dashboard_web_elem.get_extreme_guest_dashboard_create_new_theme_widget_save_dashboard_save_button)
        sleep(2)

        return 1

    def check_dashboard_page_widgets(self):
        """
        -This keyword Will check if the newly created dashboard is displaying all the widgets
        - Flow: dashboard--> automation_db1
        - Keyword Usage:
            ''check dashboard page widgets''

        :return: 1 if navigation success
        """
        self.utils.print_info("Clicking the dashboard ")
        self.auto_actions.click_reference(self.dashboard_web_elem.get_extreme_guest_dashboard_automation_db1_tab)
        sleep(2)
        all_displayed = True

        if self.dashboard_web_elem.get_extreme_guest_dashboard_automation_db1_widget1().is_displayed():
            self.utils.print_info("Widget1 displayed")
        else:
            self.utils.print_info("widget1 is not displayed")
            all_displayed = False

        if self.dashboard_web_elem.get_extreme_guest_dashboard_automation_db1_widget2().is_displayed():
            self.utils.print_info("Widget2 displayed")
        else:
            self.utils.print_info("widget2 is not displayed")
            all_displayed = False

        if self.dashboard_web_elem.get_extreme_guest_dashboard_automation_db1_widget3().is_displayed():
            self.utils.print_info("Widget3 displayed")
        else:
            self.utils.print_info("widget3 is not displayed")
            all_displayed = False

        if self.dashboard_web_elem.get_extreme_guest_dashboard_automation_db1_widget4().is_displayed():
            self.utils.print_info("Widget4 displayed")
        else:
            self.utils.print_info("widget4 is not displayed")
            all_displayed = False

        if self.dashboard_web_elem.get_extreme_guest_dashboard_automation_db1_widget5().is_displayed():
            self.utils.print_info("Widget5 displayed")
        else:
            self.utils.print_info("widget5 is not displayed")
            all_displayed = False

        if self.dashboard_web_elem.get_extreme_guest_dashboard_automation_db1_widget6().is_displayed():
            self.utils.print_info("Widget6 displayed")
        else:
            self.utils.print_info("widget6 is not displayed")
            all_displayed = False

        if self.dashboard_web_elem.get_extreme_guest_dashboard_automation_db1_widget7().is_displayed():
            self.utils.print_info("Widget7 displayed")
        else:
            self.utils.print_info("widget7 is not displayed")
            all_displayed = False

        if self.dashboard_web_elem.get_extreme_guest_dashboard_automation_db1_widget8().is_displayed():
            self.utils.print_info("Widget8 displayed")
        else:
            self.utils.print_info("widget8 is not displayed")
            all_displayed = False

        if self.dashboard_web_elem.get_extreme_guest_dashboard_automation_db1_widget9().is_displayed():
            self.utils.print_info("Widget9 displayed")
        else:
            self.utils.print_info("widget9 is not displayed")
            all_displayed = False

        if all_displayed:
            return 1
        else:
            return 0
