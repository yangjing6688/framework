import extauto.common.CloudDriver
from time import sleep
from extauto.common.Screen import Screen
from extauto.common.Utils import Utils
from extauto.common.AutoActions import AutoActions
from extauto.xiq.flows.common.Navigator import Navigator
from extauto.xiq.elements.extreme_guest.ExtremeGuestUsersWebElemets import ExtremeGuestUsersWebElements
from extauto.xiq.flows.extreme_guest.ExtremeGuest import ExtremeGuest


class ExtremeGuestUsers(object):
    def __init__(self):
        super().__init__()
        self.navigator = Navigator()
        self.driver = common.CloudDriver.cloud_driver
        self.screen = Screen()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.user_web_elem = ExtremeGuestUsersWebElements()
        self.ext_guest = ExtremeGuest()

    def select_location_for_create_bulk_vouchers_page(self, sel_loc):
        """
        - This keyword selects a location in the Eguest Users --> Create Bulk users Vouchers Page
        - It is assumed that location is already created
        - Flow : Eguest Essentials --> More Insights --> Settings --> Users --> Add user--> Create Bulk users Vouchers
        - Keyword Usage:
         - ``Select Location For Create Bulk Vouchers Page ${LOCATION}``

        :param sel_loc: location to select, in a comma-separated list format;
               e.g., Extreme Networks,Bangalore,Ecospace,Floor 1
        :return: 1 if location is selected, else -1'
        """
        ret_val = -1
        self.utils.print_info("Clicking Location Drop Down Button in Create Bulk VouchersPage")
        self.auto_actions.click(self.user_web_elem.get_create_bulk_users_location_drop_down_button())
        sleep(2)
        if sel_loc:
            try:
                location_list = sel_loc.split(',')
                location_root_name = location_list[0]
                location_generic_name = location_list[1]
                location_building_name = location_list[2]
                location_floor_name = location_list[3]

                if location_root_name:
                    self.utils.print_info("Expanding Root location: ", location_root_name)
                    location_roots = self.user_web_elem.get_extreme_guest_users_locations_root_name()
                    for location_root in location_roots:
                        if location_root_name.strip() in location_root.text:
                            self.utils.print_info("Match found for location type Root:", location_root_name)
                            root_expand_status = location_root.get_attribute('aria-expanded')
                            if root_expand_status == "true":
                                self.utils.print_info(f"Root Location {location_root} Already Expanded")
                            else:
                                root_name_expand_button = \
                                    self.user_web_elem.get_extreme_guest_users_locations_root_name_expand_button()
                                self.utils.print_info("Expanding the Root Location:", location_root_name)
                                self.auto_actions.click(root_name_expand_button)
                    sleep(5)

                if location_generic_name:
                    self.utils.print_info("Expanding Generic location: ", location_generic_name)
                    location_generics = self.user_web_elem.get_extreme_guest_users_locations_city_name()
                    for location_generic in location_generics:
                        if location_generic_name.strip() in location_generic.text:
                            self.utils.print_info("Match found for location type Generic:", location_generic_name)
                            city_expand_status = location_generic.get_attribute('aria-expanded')
                            if city_expand_status == "true":
                                self.utils.print_info(f"Generic Location {location_generic_name} Already Expanded")
                            else:
                                generic_name_expand_button = \
                                    self.user_web_elem.get_extreme_guest_users_locations_city_name_expand_button()
                                self.utils.print_info("Expanding Generic Location:", location_generic_name)
                                self.auto_actions.click(generic_name_expand_button)
                    sleep(5)

                if location_building_name:
                    location_buildings = self.user_web_elem.get_extreme_guest_users_locations_building_name()
                    for location_building in location_buildings:
                        self.utils.print_info("Expanding Building: ", location_building_name)
                        if location_building_name.strip() in location_building.text:
                            self.utils.print_info("Match found for location type Building:", location_building_name)
                            building_expand_status = location_building.get_attribute('aria-expanded')
                            if building_expand_status == "true":
                                self.utils.print_info(f"Building Location {location_building_name} Already Expanded")
                            else:
                                building_name_expand_button = \
                                    self.user_web_elem.get_extreme_guest_users_locations_building_name_expand_button()
                                self.utils.print_info("Expanding Building Location:", location_building_name)
                                self.auto_actions.click(building_name_expand_button)
                    sleep(5)

                if location_floor_name:
                    location_floors = self.user_web_elem.get_extreme_guest_users_locations_floor_name()
                    for location_floor in location_floors:
                        self.utils.print_info("Selecting Floor: ", location_floor_name)
                        if location_floor_name.strip() in location_floor.text:
                            self.utils.print_info("Match found for location type Generic:", location_floor_name)
                            self.auto_actions.click(location_floor)
                            sleep(5)
                        else:
                            self.utils.print_info(f"Floor Name {location_floor_name} Not Found")
                ret_val = 1

            except Exception as e:
                self.utils.print_info(e)
                self.utils.print_info("Unable to select location")
        else:
            self.utils.print_info("Cannot select location - location not specified in Create Bulk Users Page")

        return ret_val

    def create_bulk_vouchers(self, number_of_vouchers, access_group="", location_name=""):
        """
        - This Keyword will create Bulk Vouchers in Eguest users Page
        - Flow : Eguest Essentials --> More Insights --> Settings --> Users --> Add user--> Create Bulk users Vouchers
        - Keyword Usage:
         - ``Create Bulk Vouchers  ${NO_OF_VOUCHERS}    access_group=${ACCESS_GROUP}    location_name=${LOCATION_TREE}``

        :param number_of_vouchers: No. Of Vouchers Value
        :param access_group: Access Group
        :param location_name: Location tree in a comma-separated list format;
               e.g., Extreme Networks,Bangalore,Ecospace,Floor 1

        :return: 1 if Users Bulk Vouchers Created Successfully
        """
        self.ext_guest.go_to_configure_users_page()
        self.utils.print_info("Clicking Add User Button ")
        self.auto_actions.click(self.user_web_elem.get_extreme_guest_users_add_button())
        sleep(2)

        self.utils.print_info("Clicking Create Bulk Vouchers Button ")
        self.auto_actions.click(self.user_web_elem.get_extreme_guest_users_create_bulk_users_button())
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Clicking Access Group Drop Down Button ")
        self.auto_actions.click(self.user_web_elem.get_create_bulk_users_access_group_drop_down_button())
        sleep(2)

        self.utils.print_info(f"Selecting Access Group:{access_group}")
        self.auto_actions.select_drop_down_options(
            self.user_web_elem.get_create_bulk_users_access_group_drop_down_options(),
            access_group)
        sleep(2)

        self.utils.print_info("Entering Number of Vouchers ", number_of_vouchers)
        self.auto_actions.send_keys(self.user_web_elem.get_create_bulk_users_number_of_vouchers_textfield(),
                                    number_of_vouchers)
        sleep(2)

        if location_name:
            self.select_location_for_create_bulk_vouchers_page(location_name)

        self.utils.print_info("Click Create Button")
        self.auto_actions.click(self.user_web_elem.get_extreme_guest_users_create_bulk_users_create_button())
        sleep(2)

        self.utils.print_info("Clicking Close Button")
        self.auto_actions.click(self.user_web_elem.get_extreme_guest_users_create_bulk_users_close_button())
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        return 1

    def delete_user(self, search_string):
        """

        :param search_string:
        :return:
        """
        self._select_extreme_guest_users_page_user_row(search_string)
        self.utils.print_info("Deleting the User")
        self.auto_actions.click(self.user_web_elem.get_extreme_guest_users_delete_button())
        sleep(2)
        self.auto_actions.click(self.user_web_elem.get_extreme_guest_users_delete_ok_button())
        sleep(2)
        self.auto_actions.click(self.user_web_elem.get_extreme_guest_users_delete_status_ok_button())

        return 1


    def _get_extreme_guest_users_page_user_row(self, search_string):
        """
        Getting the row in Open SSID is same for all the objects
        :param search_string:
        :return:
        """
        self.utils.print_info("Getting user rows")
        self.utils.print_info(self.user_web_elem.get_extreme_guest_users_grid_rows())
        rows = self.user_web_elem.get_extreme_guest_users_grid_rows()
        if rows:
            for row in rows:
                if cell := self.user_web_elem.get_extreme_guest_users_grid_row_cells(row):
                    if search_string in cell.text:
                        return row

    def _select_extreme_guest_users_page_user_row(self, search_string):
        """
        Select the passed search string object in grid rows
        :param search_string:
        :return:
        """
        row = self._get_extreme_guest_users_page_user_row(search_string)
        self.utils.print_info("Selecting user row")
        self.auto_actions.click(
            self.user_web_elem.get_extreme_guest_users_grid_row_cells(row, 'x-grid-checkcolumn'))
        sleep(2)
        return 1
