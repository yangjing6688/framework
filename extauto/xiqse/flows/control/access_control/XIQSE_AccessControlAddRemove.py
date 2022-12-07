from time import sleep
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from xiqse.elements.control.access_control.ControlAccessControlAddRemoveWebElements import ControlAccessControlAddRemoveWebElements
from xiqse.elements.control.access_control.ControlAccessControlCommonWebElements import ControlAccessControlCommonWebElements
from xiqse.elements.control.access_control.ControlAccessControlPanelWebElements import ControlAccessControlPanelWebElements
from extauto.common.AutoActions import *
from extauto.common.WebElementHandler import *

class XIQSE_AccessControlAddRemove(ControlAccessControlAddRemoveWebElements):

    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.ac_addremove_els = ControlAccessControlAddRemoveWebElements()
        self.ac_common_els = ControlAccessControlCommonWebElements()
        self.ac_panel_els = ControlAccessControlPanelWebElements()
        self.screen = Screen()

    def xiqse_add_nac_appliance(self, ip_addr):
        """
        - This keyword adds NAC appliance via Control> Access Control Tab
        - Keyword Usage
        - XIQSE ADD NAC APPLIANCE     {nac_appliance_ip1}
        :return: 1 if action was successful, else -1
        """
        ret_val = 1
        add_btn = self.ac_addremove_els.get_add_nac_appliance_tb_button()
        if add_btn:
            self.utils.print_info("Clicking Add Access Control Engine toolbar button")
            self.auto_actions.click(add_btn)
            sleep(2)

            # Get Element for IP Address Label
            id_ip_field = self.get_id_for_ip_field()
            if id_ip_field:
                # Get ID from IP Address label
                ip_field_id = id_ip_field.get_attribute("id")

                # Fill in IP address
                if ip_field_id:
                    self.utils.print_info(f"Entering Access Control IP Address {ip_addr}")

                    # Replace part of id to match the one in Input field
                    input_id = ip_field_id.replace("labelTextEl", "inputEl")

                    # Get the element for that ID
                    input_element = self.ac_common_els.get_element_field(input_id)

                    # Send IP address
                    self.auto_actions.send_keys(input_element, ip_addr)

                else:
                    self.utils.print_info("Could not find ID from IP Address label")
                    ret_val = -1

                # Click Add button after filling in IP address
                sleep(2)
                if ret_val != -1:
                    add_ac_btn = self.ac_addremove_els.get_add_button_dialog()
                    if add_ac_btn:
                        self.utils.print_info("Clicking Add button in Add AC Dialog")
                        self.auto_actions.click(add_ac_btn)
                    else:
                        self.utils.print_info("Could not find Add button in Add AC Dialog")
                        ret_val = -1

                else:
                    self.utils.print_info("Problem found in Dialog")
                    ret_val = -1

                # Testing if adding NAC is successful
                sleep(3)
                if ret_val != -1:
                    # We could add a code to find out what message is returned in the future.
                    # For now, checking the successful message here if it's successfully added.
                    save_ok_btn = self.ac_addremove_els.get_save_successful()

                    if save_ok_btn:
                        click_ok_btn = self.ac_addremove_els.get_save_ok_button()
                        self.utils.print_info("Clicking OK Button in Save Successful Dialog")
                        self.auto_actions.click(click_ok_btn)
                        sleep(3)

                    else:
                        self.utils.print_info("Could not find OK button in Save Successful dialog after add")
                        ret_val = -1
                else:
                    self.utils.print_info("Problem found while adding an appliance")
                    ret_val = -1

            else:
                self.utils.print_info("Could not find IP Address field in Add NAC Appliance dialog")
                ret_val = -1

        else:
            self.utils.print_info("Unable to find NAC Add toolbar button")
            ret_val = -1

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_delete_nac_appliance(self, nacip):
        """
        - This keyword deletes NAC appliance via Control> Access Control Tab
        - This keyword assumes that you already selected the All Engines in the tree
        - Select a row for NAC appliance and then hit Delete.
        - Keyword Usage
        - XIQSE Delete NAC APPLIANCE     {nac_appliance_ip1}
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        # Selecting a row in the grid (using IP address)
        select_row = self.ac_panel_els.select_row_grid_by_ip(nacip)
        if select_row:
            self.utils.print_info(f"Clicking Row of {nacip}...")
            self.auto_actions.click(select_row)
            sleep(2)

            # Delete button should be available once a row is selected
            delete_btn = self.ac_common_els.get_click_innerel_button("Delete")
            if delete_btn:
                self.utils.print_info(f"Clicking Delete ...")
                self.auto_actions.click(delete_btn)
                sleep(2)

                delete_checkbox = self.ac_addremove_els.get_delete_nac_checkbox()
                if delete_checkbox:
                    self.utils.print_info(f"Checking a checkbox to delete from database...")
                    self.auto_actions.click(delete_checkbox)
                    sleep(2)
                    yes_btn_dialog = self.ac_common_els.get_click_innerel_button("Yes")
                    if yes_btn_dialog:
                        self.utils.print_info(f"Checking Yes button to delete...")
                        self.auto_actions.click(yes_btn_dialog)
                        sleep(2)
                        ret_val = 1
                    else:
                        self.utils.print_info(f"Unable to click Yes button ")
                else:
                    self.utils.print_info(f"Unable to find Delete checkbox")
            else:
                self.utils.print_info(f"Unable to click Delete button from Toolbar ")
        else:
            self.utils.print_info(f"Unable to click Delete button ")

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val
