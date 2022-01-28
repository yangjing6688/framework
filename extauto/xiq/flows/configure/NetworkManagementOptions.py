from time import sleep
from robot.libraries.BuiltIn import BuiltIn
from extauto.common.Screen import Screen
from extauto.common.Utils import Utils
from extauto.common.AutoActions import AutoActions
from extauto.xiq.flows.common.Navigator import Navigator
import extauto.xiq.flows.common.ToolTipCapture as tool_tip
from extauto.xiq.elements.NetworkManagementOptionsElements import NetworkManagementOptionsElements


class NetworkManagementOptions(NetworkManagementOptionsElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.navigator = Navigator()
        self.screen = Screen()
        self.auto_actions = AutoActions()

    def add_network_management_options(self,  option_name="management_option_1", enable_legacy_http_redirect="True"):
        """
        - Adds new network management option(s)
        -Flow: Configure --> Common Objects --> Network -->Management Options
           - Keyword Usage:
            - ``Add Network Management Options``
        :param option_name : name of the management option
        :param enable_legacy_http_redirect: determines if enable legacy http redirect should be clicked or not
        :return: 1
        """
        self.navigator.navigate_to_common_objects_management_options()
        sleep(5)

        self.utils.print_info("Clicking on the Add Management Options Button")
        add_button = self.get_add_network_management_options_entry()
        if add_button:
            self.auto_actions.click(add_button)
            self.utils.print_info("Set Name for new Add Management Options Entry")
            name_txt_field = self.get_new_management_option_name()
            if name_txt_field:
                self.auto_actions.send_keys(name_txt_field, option_name)
                if enable_legacy_http_redirect.lower() == "true":
                    self.utils.print_info("Enabling legacy http redirect")
                    enable_legacy_http_redirect_checkbox = self.get_legacy_http_redirect()
                    if enable_legacy_http_redirect_checkbox:
                        self.auto_actions.click(enable_legacy_http_redirect_checkbox)
                    else:
                        self.utils.print_info("Unable to enable legacy http redirect")
                        return -1
                self.utils.print_info("Saving configuration")
                save_button = self.get_save_button()
                if save_button:
                    self.auto_actions.click(save_button)
                    return 1
                else:
                    self.utils.print_info("Unable save configuration")
                    return -1
            else:
                self.utils.print_info("Unable to set  Name field for new Add Management Options Entry")
                return -1
        else:
            self.utils.print_info("Unable to click on the Add Management Options Button")
        return 1

    def delete_network_management_options(self,  option_name):
        """
        - Adds new network management option(s)
        -Flow: Configure --> Common Objects --> Network -->Management Options
           - Keyword Usage:
            - ``Delete Network Management Options``
        :param option_name : name of the management option
        :return: 1
        """
        self.navigator.navigate_to_common_objects_management_options()
        sleep(5)

        entry_found = False
        self.utils.print_info("Gathering the list of network management options in the table")
        list_of_management_options = self.get_network_management_grid_rows()
        if list_of_management_options:
            self.utils.print_info("Searching list to see if management option " + option_name + " is present" )
            for man_opt in list_of_management_options:
                if option_name in man_opt.text:
                    self.utils.print_info("Management option " + option_name + " found")
                    self.utils.print_info("Selecting the row")
                    check_box = self.get_network_management_grid_row_cells(man_opt)[0]
                    if check_box:
                        self.auto_actions.click(check_box)
                        self.utils.print_info("Clicking the delete button")
                        delete_button = self.get_delete_network_management_options_entry()
                        if delete_button:
                            self.auto_actions.click(delete_button)
                            sleep(3)
                            self.utils.print_info("Clicking yes on confirm delete popup")
                            yes_button = self.get_confirm_yes()
                            if yes_button:
                                self.auto_actions.click(yes_button)
                                return 1
                            else:
                                self.utils.print_info("Unable to click yes on the confirm delete popup")
                                return -1
                        else:
                            self.utils.print_info("Unable to click the delete button")
                            return -1
                    else:
                        self.utils.print_info("Unable to select the row")
                        return -1
            if not entry_found:
                self.utils.print_info("Management option " + option_name + " not found")
                return -1
        else:
            self.utils.print_info("Unable to gather the list of network management options in the table")
            return -1
