from xiqse.elements.control.ControlWebElements import ControlWebElements
from xiqse.elements.control.access_control.ControlAccessControlCommonWebElements import ControlAccessControlCommonWebElements
from xiqse.elements.control.dashboard.ControlDashboardWebElements import ControlDashboardWebElements

from extauto.common.AutoActions import *
from extauto.common.WebElementHandler import *

class XIQSE_ControlDashboard(ControlDashboardWebElements):

    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.ac_common_els = ControlAccessControlCommonWebElements()
        self.ac_dashboard_els = ControlDashboardWebElements()
        self.screen = Screen()

    def xiqse_expand_control_dashboard_dropdown(self):
        """
        This is a keyword to expand the dropdown menu in Control Dashboard page
        Will try 'Overview' first then 'System' and 'Health' - Most likely it's Overview.
        - Keyword Usage
            XIQSE EXPAND CONTROL DASHBOARD DROPDOWN
        :return: XXX if action was successful, else -1
        """
        ret_val = -1
        menu_list = ['Overview', 'System', 'Health']
        for m in menu_list:
            self.utils.print_info(f"Selecting {m} ...")
            if self.ac_dashboard_els.select_dashboard_combo(m):
                self.auto_actions.click(self.ac_dashboard_els.select_dashboard_combo(m))
                sleep(2)
                ret_val = 1
                break

        if ret_val == -1:
            self.utils.print_info(f"Could not find the menu...")
            self.screen.save_screen_shot()

        sleep(2)
        return ret_val

    def xiqse_select_control_dashboard_dropdown_menu(self, combomenu):
        """
        This is a keyword to select the dropdown menu in Control Dashboard page
        - Keyword Usage
            XIQSE EXPAND CONTROL DASHBOARD DROPDOWN MENU   System
        :return: XXX if action was successful, else -1
        """
        ret_val = -1
        the_menu = self.ac_dashboard_els.select_dashboard_combo_menu(combomenu)
        if the_menu:
            self.utils.print_info(f"Selecting {combomenu} menu...")
            self.auto_actions.click(the_menu)
            ret_val = 1
            sleep(2)
        else:
            self.utils.print_info(f"Unable to select {combomenu} menu... ")
            self.screen.save_screen_shot()
        return ret_val

    def xiqse_get_license_overview_in_control_dashboard(self, labeltext):
        """
        This is a keyword to retrieve a value based on the label in Control Dashboard page
        - Keyword Usage
            XIQSE Get License Overview In Control Dashboard   Total End-System Assessment License Limit:
        :return: XXX if action was successful, else -1
        """
        ret_val = "Not Found"
        id_for_labeltext = self.ac_dashboard_els.get_id_for_overview_label(labeltext)
        if id_for_labeltext:
            labeltext_id = id_for_labeltext.get_attribute("id")

            if labeltext_id:
                self.utils.print_info(f"Searching for {labeltext} in Overview section")

                # Replace part of id to match the one in Input field
                input_id = labeltext_id.replace("labelTextEl", "inputEl")

                # Get the element for that ID
                input_element = self.ac_common_els.get_element_field(input_id)

                # can we turn that found element into a number?
                try:
                    value_as_int = int(input_element.text)
                    if value_as_int >= 0:
                        self.utils.print_info(f"Returning {value_as_int} ")
                        ret_val = input_element.text
                    else:
                        ret_val = "Invalid Value"
                        self.screen.save_screen_shot()
                except:
                    self.utils.print_info(f"Error converting license count value: {input_element.text} to number")
                    if(input_element.text == "Unlimited"):
                        self.utils.print_debug("Value is Unlimited, which is valid")
                        ret_val = input_element.text
                    else:
                        ret_val = "Invalid Value"
                        self.screen.save_screen_shot()

            else:
                self.utils.print_info("Could not find ID from Overview license label")
                self.screen.save_screen_shot()
                ret_val = "Not Found"

        else:
            self.utils.print_info("Could not find the label in Overview")
            self.screen.save_screen_shot()
            ret_val = "Not Found"

        return ret_val