from time import sleep
from common.Utils import Utils
from common.AutoActions import AutoActions

from xiq.elements.PrivateClientGroupsWebElements import PrivateClientGroupsWebElements
from xiq.flows.common.Navigator import Navigator
from common.WebElementHandler import WebElementHandler


# import common.CloudDriver

class PrivateClientGroups(PrivateClientGroupsWebElements):

    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.navigator = Navigator()
        self.web = WebElementHandler()
        # self.driver = common.CloudDriver.cloud_driver


    def set_custom_network_policy(self, policy='default'):
        """
        This keyword set a custom network policy on the private client group page
        - Flow: Configure --> Users --> User Management --->Private Client Group
        - Keyword Usage:
         - ``set_custom_network_policy  policy=ANC_ppsk``

        :param policy: an existing policy name

        :return: 1 or -1

        """
        sleep(5)
        self.auto_actions.click(self.get_private_client_grp_default_network_policy())
        network_policy_drop_down_items = self.get_private_client_grp_network_policy_drop_down_list_items()
        if network_policy_drop_down_items:
            if self.auto_actions.select_drop_down_options(network_policy_drop_down_items, policy):
                self.utils.print_info(f"Selected network policy '{policy}' from drop down")

        element = self.get_private_client_grp_default_network_policy()
        if element.text not in policy:
            self.utils.print_info(f"Not able to select '{policy}' from drop down")
            return -1

        return 1


    def enable_disable_ap_based_group(self, mode='default'):
        """
            This keyword enables or disables the enable ap based group
            - Flow: Configure --> Users --> User Management --->Private Client Group
            - Keyword Usage:
             - ``${rc}=   enable_disable_ap_based_groups   mode=enable ``
             - ``${rc}=   enable_disable_ap_based_groups   mode=disable  ``

            :param mode: enabling or disable=ing

            :return: 1 or -1

        """
        self.auto_actions.click(self.get_private_client_grp_ap_based_groups_tab())
        status = self.get_based_grp_enabled_status('ap')

        if status == 'OFF' and mode.lower() in ['enable']:
            self.utils.print_info("Click on the enable ap-based group button ")
            self.auto_actions.click(self.get_private_client_grp_enable_ap_based_on_off_button())

        if status == 'ON' and mode.lower() in ['disable']:
            self.utils.print_info("Click on the enabled ap-based group button ")
            self.auto_actions.click(self.get_private_client_grp_enable_ap_based_on_off_button())

        elif not status:
            self.utils.print_info("Button does not exist ")
            return -1

        if self.get_based_grp_enabled_status('ap') == 'OFF' and mode.lower() in ['enable']:
            self.utils.print_info("Fail to enable the ap-based group ")
            return -1

        elif self.get_based_grp_enabled_status('ap') == 'ON' and mode.lower() in ['disable']:
            self.utils.print_info("Fail to disable the ap-based group ")
            return -1

        return 1


    def enable_disable_key_based_group(self, mode='default'):
        """
            This keyword enables or disables the key based group
            - Flow: Configure --> Users --> User Management --->Private Client Group

            - Keyword Usage:
             - ``${rc}=   enable_disable_key_based_groups   mode=enable ``
             - ``${rc}=   enable_disable_key_based_groups   mode=disable  ``

            :param mode: enabling or disabling

            :return: 1 or -1

        """
        self.auto_actions.click(self.get_private_client_grp_key_based_groups_tab())
        status = self.get_based_grp_enabled_status('key')

        if status == 'OFF' and mode.lower() in ['enable']:
            self.utils.print_info("Click on the enable key-based group button ")
            self.auto_actions.click(self.get_private_client_grp_enable_key_based_on_off_button())

        if status == 'ON' and mode.lower() in ['disable']:
            self.utils.print_info("Click on the enabled key-based group button ")
            self.auto_actions.click(self.get_private_client_grp_enable_key_based_on_off_button())

        elif not status:
            self.utils.print_info("Button does not exist ")
            return -1

        if self.get_based_grp_enabled_status('key') == 'OFF' and mode.lower() in ['enable']:
            self.utils.print_info("Fail to enable the key-based group ")
            return -1

        elif self.get_based_grp_enabled_status('key') == 'ON' and mode.lower() in ['disable']:
            self.utils.print_info("Fail to disable the key-based group ")
            return -1

        return 1


    def get_based_grp_enabled_status(self, mode):
        """
            This keyword get a staus of the enable based groups button when the current status is on or off
            - Flow: Configure --> Users --> User Management --->Private Client Group

            - Keyword Usage:
             - ``get_based_grp_enabled_status  ap``
             - ``get_based_grp_enabled_status  key``

             :param  mode: key for the key based group or ap for the ap based group

            :return: ON is active or OFF is not active

        """

        element = None
        if mode == 'ap':
            self.utils.print_info("Click on the AP based group tab ")
            self.auto_actions.click(self.get_private_client_grp_ap_based_groups_tab())
            element = self.get_private_client_grp_enable_ap_based_on_off_button()

        elif mode == 'key':
            self.utils.print_info("Click On the key based group tab ")
            self.auto_actions.click(self.get_private_client_grp_key_based_groups_tab())
            element = self.get_private_client_grp_enable_key_based_on_off_button()

        if element == None:
            self.utils.print_info(" The enable based groups button does not exist ")
            return 0

        if element.is_selected():
            self.utils.print_info("Status is ON ")
            return "ON"
        else:
            self.utils.print_info("Status is OFF ")
            return "OFF"


    def delete_all_rooms_ap_based_group(self):
        """
            This keyword deletes all rooms in the ap based group table
            - Flow: Configure --> Users --> User Management --->Private Client Group

            - Keyword Usage:
             - ``delete_all_rooms_ap_based_group``

            :return: 1 is for a successful deletion or -1 not a successful deletion

        """
        if not self.get_private_client_grp_all_rooms_checkbox().is_selected():
            if self.get_private_ap_based_room_table_cells() != None:
                self.utils.print_info("Select all rooms ")
                self.auto_actions.click(self.get_private_client_grp_all_rooms_checkbox())
            else:
                self.utils.print_info("Table is already emtpty ")
                return 1

        self.utils.print_info("Click on Delete button ")
        self.auto_actions.click(self.get_private_delete_room_button())
        self.wait_until_element_available(self.get_diag_confirm_yes_button())
        if self.get_diag_confirm_yes_button() != None:
            self.utils.print_info("Click on the confirmed Yes")
            self.auto_actions.click(self.get_diag_confirm_yes_button())

        self.utils.print_info("Click on Save Setting button ")
        self.auto_actions.click(self.get_private_client_grp_save_setting_button())

        sleep(5)
        if self.get_private_ap_based_room_table_cells() != None:
            self.utils.print_info(" Rooms are not empty ")
            return -1

        return 1


    def delete_all_user_keys_based_group(self):
        """
            This keyword deletes all user keys in the user key based group table
            - Flow: Configure --> Users --> User Management --->Private Client Group

            - Keyword Usage:
             - ``delete_all_user_keys_based_group``

            :return: 1 is for a successful deletion or -1 not a successful deletion

        """
        if not self.get_private_key_based_delete_checkbox_all().is_selected():
            if self.get_private_key_based_all_cells() != None:
                self.utils.print_info("Select all keys ")
                self.auto_actions.click(self.get_private_key_based_delete_checkbox_all())
            else:
                self.utils.print_info("Table is already emtpty ")
                return 1

        self.utils.print_info("Click on Delete button ")
        self.auto_actions.click(self.get_private_key_based_group_delete_button())
        self.wait_until_element_available(self.get_diag_confirm_yes_button())
        if self.get_diag_confirm_yes_button() != None:
            self.utils.print_info("Click on the confirmed Yes")
            self.auto_actions.click(self.get_diag_confirm_yes_button())

        self.utils.print_info("Click on Save Setting button ")
        self.auto_actions.click(self.private_key_based_save_info_button())

        sleep(5)
        if self.get_private_key_based_all_cells() != None:
            self.utils.print_info(" Fail to delete all users and table is not empty ")
            return -1

        return 1


    def delete_specific_room_ap_based_group(self, room):
        """
            This keyword deletes a specific room in the ap based group table
            - Flow: Configure --> Users --> User Management --->Private Client Group

            - Keyword Usage:
             - ``delete_specific_room_ap_based_group  room=room1``
            :param   room: room name
            :return: 1 or -1

        """

        sleep(5)
        header = self.get_private_ap_based_room_table_headers()
        cells = self.get_private_ap_based_room_table_cells()

        if cells == None:
            self.utils.print_info(" Room table is empty ")
            return -1

        row = self.search_in_table(len(header), cells, room)
        if not row:
            self.utils.print_info(" Not able to find a room in table " + room)
            return -1

        self.utils.print_info(" Select the room: " + room)
        row.click()

        self.auto_actions.scroll_up()
        self.utils.print_info(" Click on delete button ")
        self.wait_until_element_available(self.get_private_delete_room_button())
        self.auto_actions.click(self.get_private_delete_room_button())

        self.wait_until_element_available(self.get_diag_confirm_yes_button())
        diag_yes_button = self.get_diag_confirm_yes_button()
        if diag_yes_button:
            self.utils.print_info(" Click on Yes button ")
            self.auto_actions.click(self.get_diag_confirm_yes_button())

        sleep(3)
        cells = self.get_private_ap_based_room_table_cells()

        if cells != None:
            row = self.search_in_table(len(header), cells, room)
            if row:
                self.utils.print_info(" Not able to delete the room " + room)
                return -1

        return 1


    def delete_specific_user_key_based_group(self, user):
        """
            This keyword deletes a specific room in the user key base group table
            - Flow: Configure --> Users --> User Management --->Private Client Group

            - Keyword Usage:
             - ``delete_specific_user_key_based_group  user=alex``

            :param   user: user name
            :return: 1 or -1

        """
        sleep(5)
        header = self.get_private_key_based_table_header()
        cells = self.get_private_key_based_all_cells()

        self.utils.print_info(" header ")

        if cells == None:
            self.utils.print_info(" User table is empty ")
            return -1

        row = self.search_in_table(len(header), cells, user)
        if not row:
            self.utils.print_info(" Not able to find the user in table " + user)
            return -1

        self.utils.print_info(" Select the user: " + user)
        row.click()

        self.auto_actions.scroll_up()
        self.utils.print_info(" Click on delete button ")
        self.wait_until_element_available(self.get_private_key_based_group_delete_button())
        self.auto_actions.click(self.get_private_key_based_group_delete_button())

        diag_yes_button = self.get_diag_confirm_yes_button()
        if diag_yes_button:
            self.utils.print_info(" Click on Yes button ")
            self.auto_actions.click(self.get_diag_confirm_yes_button())

        self.auto_actions.click(self.get_private_key_based_save_info_button())
        sleep(3)

        cells = self.get_private_key_based_all_cells()
        if cells != None:
            row = self.search_in_table(len(header), cells, user)
            if row:
                self.utils.print_info(" Not able to delete the user " + user)
                return -1

        return 1


    def add_room_ap_based_group(self, room='default', user='default', user_position=1):
        """
            This keyword adds a romm in the ap based group
            - Flow: Configure --> Users --> User Management --->Private Client Group

            - Keyword Usage:
             - ``add_room_ap_based_group  room=abcdefefFFF  user=user22  user_position=0``


            :param : room: room name
            :param : user: exisiting user name
            :param : user_position: which user in the dropdown list

            :return: 1 or 0

        """
        position = int(user_position)

        if self.get_private_client_grp_add_room_button().is_displayed():
            self.utils.print_info("Click on add room button")
            self.auto_actions.click(self.get_private_client_grp_add_room_button())
            self.wait_until_element_available(self.get_ap_based_room_input())
            actual_list = len(self.get_private_ap_based_room_user_assigned_drop_down())

            if position > actual_list - 1:
                self.utils.print_info(" Position must be in range 0 to " + str(actual_list - 1))
                return - 1

            room_el = self.get_ap_based_room_input()

            if room_el != None:
                self.utils.print_info("Enter the room " + room)
                self.auto_actions.send_keys(room_el, room)

                if user != 'default':
                    self.utils.print_info("Click on the assigned user drop down")
                    self.auto_actions.click(self.get_private_ap_based_room_user_assigned_drop_down()[position])
                    self.utils.print_info("select the user: " + user)
                    self.auto_actions.send_keys(self.get_private_ap_based_room_user_assigned_enter_text()[position],
                                                user)
                    self.auto_actions.click(self.get_room_user_assigned_drop_down_items()[position])

                self.auto_actions.click(self.get_private_client_grp_save_setting_button())
            else:
                self.utils.print_info(" Not able to enter the room " + room)

        else:
            self.utils.print_info(" Add room button does not exist ")

        sleep(5)
        header = self.get_private_ap_based_room_table_headers()
        cells = self.get_private_ap_based_room_table_cells()
        row = self.search_in_table(len(header), cells, room)

        if not row:
            self.utils.print_info(" Room does not exist after adding " + room)
            return -1

        return 1


    def add_user_key_based_group(self, user='default'):
        """
            This keyword adds a existing user in the key based group
            - Flow: Configure --> Users --> User Management --->Private Client Group

            - Keyword Usage:
             - ``add_user_key_based_group    user=alex``

            :param : user: exisiting key user name

            :return: 1 or 0

        """

        if self.get_private_key_based_group_add_button().is_displayed():
            self.utils.print_info("Click on add room button")
            self.auto_actions.click(self.get_private_key_based_group_add_button())
            user_select = self.get_private_user_select_dropdown()

            if user_select == None:
                self.utils.print_info("There is no more users to allocated")
                return -1

            self.utils.print_info("Click on the select user drop down ")
            self.auto_actions.click(self.get_private_user_select_dropdown())
            self.utils.print_info(" Searching the user name " + user)
            self.auto_actions.send_keys(self.get_private_user_search_key_based_group_text(), user)
            self.utils.print_info(" Select the user " + user)
            self.auto_actions.send_enter(self.get_private_user_search_key_based_group_text())
            self.utils.print_info(" Click on Save Changes ")
            self.auto_actions.click(self.get_private_key_based_save_info_button())

        sleep(5)
        header = self.get_private_key_based_table_header()
        cells = self.get_private_key_based_all_cells()
        row = self.search_in_table(len(header), cells, user)

        if not row:
            self.utils.print_info(" User does not exist after adding " + user)
            return -1

        return 1


    def search_in_table(self, no_columns_per_row, cells, searched_value):

        """
            - This function searches a value in a table and return a selected row

            :param  no_columns_per_row: total columns
            :param  cells: total cells
            :param  searched_value: value to be searched

            :return: a selected check box of row  or -1

        """
        row_text = []
        cnt = 0
        found = False
        row = None

        self.utils.print_info("Search for the value: " + searched_value)

        for cell in cells:
            row_text.append(cell.text)
            cnt = cnt + 1
            if cnt == 1:
                row = cell

            if cnt == no_columns_per_row:
                if searched_value in str(row_text):
                    found = True
                    self.utils.print_info("Able to locate the room in the table " + str(row_text))
                    return row
                else:
                    found = False
                    self.utils.print_info(str(row_text))

                row_text = []
                cnt = 0

        if not found:
            self.utils.print_info(" Not able to find the room in table ")
            return 0


    def wait_until_elements_available(self, elements, seconds=60):
        current_seconds = 0
        self.utils.print_info(" Wait until elements available ... ")
        while current_seconds < seconds:
            if elements != None:
                for el in elements:
                    while not el.is_displayed():
                        sleep(1)
                        current_seconds = current_seconds + 1

            sleep(1)
            current_seconds = current_seconds + 1


    def wait_until_element_available(self, element, seconds=60):

        sleep(3)
        current_seconds = 0
        self.utils.print_info(" Wait until element available ... ")
        while current_seconds < seconds:
            if element != None:
                if element.is_displayed():
                    current_seconds = seconds + 1

            sleep(1)
            current_seconds = current_seconds + 1