from extauto.common.CloudDriver import CloudDriver
from time import sleep
from extauto.common.Screen import Screen
from extauto.common.Utils import Utils
from extauto.common.AutoActions import AutoActions
from extauto.xiq.flows.common.Navigator import Navigator
from extauto.xiq.elements.extreme_guest.ExtremeGuestUsersWebElemets import ExtremeGuestUsersWebElements
from extauto.xiq.flows.extreme_guest.ExtremeGuest import ExtremeGuest
from extauto.xiq.elements.extreme_guest.ExtremeGuestWebElements import ExtremeGuestWebElements
from extauto.common.CommonValidation import CommonValidation


class ExtremeGuestUsers(object):
    def __init__(self):
        super().__init__()
        self.navigator = Navigator()
        # self.driver = extauto.common.CloudDriver.cloud_driver
        self.screen = Screen()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.user_web_elem = ExtremeGuestUsersWebElements()
        self.ext_guest = ExtremeGuest()
        self.guest_web_elem = ExtremeGuestWebElements()

        self.common_validation = CommonValidation()

    def select_location_for_create_bulk_vouchers_page(self, sel_loc, **kwargs):
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
        self.auto_actions.click_reference(self.user_web_elem.get_create_bulk_users_location_drop_down_button)
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
                kwargs['fail_msg'] = "Unable to select location"
                self.common_validation.fault(**kwargs)
        else:
            kwargs['fail_msg'] = "Cannot select location - location not specified in Create Bulk Users Page"
            self.common_validation.failed(**kwargs)

        return ret_val

    def create_bulk_vouchers(self, number_of_vouchers, access_group="", location_name="", print_users=False, **kwargs):
        """
        - This Keyword will create Bulk Vouchers in Eguest users Page
        - Flow : Eguest Essentials --> More Insights --> Settings --> Users --> Add user--> Create Bulk users Vouchers
        - Keyword Usage:
        - ``Create Bulk Vouchers  ${NO_OF_VOUCHERS}    access_group=${ACCESS_GROUP}    location_name=${LOCATION_TREE}``

        :param print_users:
        :param number_of_vouchers: No. Of Vouchers Value
        :param access_group: Access Group
        :param location_name: Location tree in a comma-separated list format;
               e.g., Extreme Networks,Bangalore,Ecospace,Floor 1

        :return: 1 if Users Bulk Vouchers Created Successfully
        """
        self.ext_guest.go_to_configure_users_page()
        if self._create_bulk_vouchers(number_of_vouchers, access_group, location_name, print_users) == 1:
            kwargs['pass_msg'] = "Users Bulk Vouchers Created Successfully"
            self.common_validation.passed(**kwargs)
            return 1

        kwargs['fail_msg'] = "Unable to create Bulk Vouchers in Eguest users Page"
        self.common_validation.failed(**kwargs)
        return -1

    def create_guest_management_role_bulk_vouchers(self, number_of_vouchers, access_group="", location_name="", print_users=False, **kwargs):
        """
        - This Keyword will create Bulk Vouchers in Guest Mangement Users Page
        - Flow : Guest Management Users --> Add user--> Create Bulk users Vouchers
        - Keyword Usage:
        - ``Create Guest Management Role Bulk Vouchers  ${NO_OF_VOUCHERS}    access_group=${ACCESS_GROUP}    location_name=${LOCATION_TREE}``

        :param print_users:
        :param number_of_vouchers: No. Of Vouchers Value
        :param access_group: Access Group
        :param location_name: Location tree in a comma-separated list format;
               e.g., Extreme Networks,Bangalore,Ecospace,Floor 1

        :return: 1 if Users Bulk Vouchers Created Successfully
        """
        self.utils.switch_to_iframe(CloudDriver().cloud_driver)
        if self._create_bulk_vouchers(number_of_vouchers, access_group, location_name, print_users) == 1:
            kwargs['pass_msg'] = "Users Bulk Vouchers Created Successfully"
            self.common_validation.passed(**kwargs)
            return 1

        kwargs['fail_msg'] = "Unable to create Bulk Vouchers in Eguest users Page"
        self.common_validation.failed(**kwargs)
        return -1

    def _create_bulk_vouchers(self, number_of_vouchers, access_group="", location_name="", print_users=False):
        """
        - This Keyword will create Bulk Vouchers in Eguest users Page
        - Flow : Eguest Essentials --> More Insights --> Settings --> Users --> Add user--> Create Bulk users Vouchers
        - Keyword Usage:
        - ``Create Bulk Vouchers  ${NO_OF_VOUCHERS}    access_group=${ACCESS_GROUP}    location_name=${LOCATION_TREE}``

        :param print_users:
        :param number_of_vouchers: No. Of Vouchers Value
        :param access_group: Access Group
        :param location_name: Location tree in a comma-separated list format;
               e.g., Extreme Networks,Bangalore,Ecospace,Floor 1

        :return: 1 if Users Bulk Vouchers Created Successfully
        """

        self.utils.print_info("Clicking Add User Button ")
        self.auto_actions.click_reference(self.user_web_elem.get_extreme_guest_users_add_button)
        sleep(2)

        self.utils.print_info("Clicking Create Bulk Vouchers Button ")
        self.auto_actions.click_reference(self.user_web_elem.get_extreme_guest_users_create_bulk_users_button)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Clicking Access Group Drop Down Button ")
        self.auto_actions.click_reference(self.user_web_elem.get_create_bulk_users_access_group_drop_down_button)
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
        self.auto_actions.click_reference(self.user_web_elem.get_extreme_guest_users_create_bulk_users_create_button)
        sleep(2)

        if not print_users:
            self.utils.print_info("Clicking Close Button")
            self.auto_actions.click_reference(self.user_web_elem.get_extreme_guest_users_create_bulk_users_close_button)
            sleep(2)
        else:
            self.utils.print_info("Clicking Print Button")
            self.auto_actions.click_reference(self.user_web_elem.get_extreme_guest_users_create_bulk_users_print_button)
            sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        return 1

    def delete_user(self, search_string):
        """

        :param search_string:
        :return:
        """

        if type(search_string) is dict:
            search_string = list(search_string.keys())[0]
        self.auto_actions.click(self._get_extreme_guest_users_page_user_row(search_string))
        sleep(2)
        self.screen.save_screen_shot()
        self.utils.print_info("Deleting the User")
        self.utils.print_info("Click Delete Button")
        self.auto_actions.click_reference(self.user_web_elem.get_extreme_guest_users_delete_button)
        self.screen.save_screen_shot()
        sleep(2)
        try:
            if self.user_web_elem.get_extreme_guest_users_delete_ok_button().is_displayed():
                self.auto_actions.click_reference(self.user_web_elem.get_extreme_guest_users_delete_ok_button)
                self.screen.save_screen_shot()
                self.utils.print_info("Click OK Button")
        except Exception:
            self.utils.print_info("Try to click duplicate OK Button clicked")
            self.screen.save_screen_shot()
        
        try:
            if self.user_web_elem.get_extreme_guest_users_delete_ok_button_duplicate().is_displayed():
                self.auto_actions.click_reference(self.user_web_elem.get_extreme_guest_users_delete_ok_button_duplicate)
                self.screen.save_screen_shot()
                self.utils.print_info("Click Duplicate OK Button")
        except Exception:
            self.utils.print_info("OK Button is already clicked")
            self.screen.save_screen_shot()
        sleep(2)
        
        try:
            if self.user_web_elem.get_extreme_guest_users_delete_status_ok_button().is_displayed():
                self.auto_actions.click_reference(self.user_web_elem.get_extreme_guest_users_delete_status_ok_button)
                self.screen.save_screen_shot()
                self.utils.print_info("Click Duplicate OK Button")
        except Exception:
            self.utils.print_info("OK Button is already clicked")
            self.screen.save_screen_shot()

        return 1

    def delete_all_user(self):
        """
        :${DELETE_ALL_USER}=             Delete All User:
        :return:1
        """
        self.screen.save_screen_shot()
        self.utils.print_info("Selecting all the users the User")
        self.auto_actions.click_reference(self.user_web_elem.get_extreme_guest_users_select_button)
        self.screen.save_screen_shot()
        sleep(2)

        self.screen.save_screen_shot()
        self.utils.print_info("Deleting the User")
        self.utils.print_info("Clicking Delete Button")
        self.auto_actions.click_reference(self.user_web_elem.get_extreme_guest_users_delete_button)
        self.screen.save_screen_shot()
        sleep(2)
        self.utils.print_info("Click OK Button")
        self.auto_actions.click_reference(self.user_web_elem.get_extreme_guest_users_delete_ok_button)
        self.screen.save_screen_shot()
        try:
            if self.user_web_elem.get_extreme_guest_users_delete_ok_button_duplicate().is_displayed():
                self.auto_actions.click_reference(self.user_web_elem.get_extreme_guest_users_delete_ok_button_duplicate)
                self.screen.save_screen_shot()
                self.utils.print_info("Click Duplicate OK Button")
        except Exception:
            self.utils.print_info("OK Button is already clicked")
            self.screen.save_screen_shot()
        sleep(2)
        self.auto_actions.click_reference(self.user_web_elem.get_extreme_guest_users_delete_status_ok_button)
        self.screen.save_screen_shot()

        return 1

    def get_extreme_guest_users_count(self):
        """
        Getting the row count in Extreme Guest Users Page
        - Keyword Usage:
        - ``Get Extreme Guest Users Count``

        :param search_string:
        :return: User Count
        """
        count=0
        self.utils.print_info("Getting user rows")
        rows = self.user_web_elem.get_extreme_guest_users_grid_rows()
        if rows:
            for row in self.user_web_elem.get_extreme_guest_users_grid_rows():
                count += 1
        return count

    def get_extreme_social_users_count(self,social_name):
        """
        Getting the social users count in Extreme Guest Users Page
        - Keyword Usage:
         - ``Get Extreme Guest Users Count``
        :return: User Count
        """
        self.utils.print_info("Clicking on Extreme Guest Analyze Page")
        self.auto_actions.click_reference(self.guest_web_elem.get_extreme_guest_analyze_page)
        sleep(2)
        self.screen.save_screen_shot()
        sleep(2)
        if social_name == "Facebook":
            self.utils.print_info("Getting Facebook count")
            count = self.user_web_elem.get_extreme_facebook_guest_users()
            return count

        if social_name == "Linkedin":
            self.utils.print_info("Getting Linkedin count")
            count = self.user_web_elem.get_extreme_linkedin_guest_users()
            return count

    def _get_extreme_guest_users_page_user_row(self, search_string):
        """
        Getting the row in Open SSID is same for all the objects

        :param search_string:
        :return:
        """
        self.utils.print_info("Getting user rows")
        rows = self.user_web_elem.get_extreme_guest_users_grid_rows()
        if rows:
            for row in self.user_web_elem.get_extreme_guest_users_grid_rows():
                self.utils.print_info("row calling: " + row.text)
                if search_string in row.text:
                    return row

    def _select_extreme_guest_users_page_user_row(self, search_string):
        """
        Select the passed search string object in grid rows

        :param search_string:
        :return:
        """
        self.utils.print_info("Selecting user")
        self.auto_actions.click(
            self.user_web_elem.get_extreme_guest_users_grid_row_cells(search_string))
        sleep(2)
        return 1

    def create_bulk_vouchers_client_login(self, number_of_vouchers, access_group="", location_name=""):
        """

        :param number_of_vouchers:
        :param access_group:
        :param location_name:
        :return:
        """

        self.create_bulk_vouchers(number_of_vouchers, access_group, location_name, True)

        self.utils.print_info("Switch to New Extreme Guest user print Window")
        CloudDriver().cloud_driver.switch_to.window(CloudDriver().cloud_driver.window_handles[2])

        user_list = self.user_web_elem.get_extreme_guest_users_print_user_cells()
        password_list = self.user_web_elem.get_extreme_guest_users_print_password_cells()

        if user_list:
            users = []
            for user in user_list:
                users.append(user.text)

        if password_list:
            passwords = []
            for password in password_list:
                passwords.append(password.text)

        credentials = dict(zip(users, passwords))

        self.utils.print_info("Switch to back to Extreme Guest Window")
        CloudDriver().cloud_driver.switch_to.window(CloudDriver().cloud_driver.window_handles[1])
        sleep(2)

        self.utils.print_info("Clicking Close Button")
        self.auto_actions.click_reference(self.user_web_elem.get_extreme_guest_users_create_bulk_users_close_button)
        sleep(2)

        return credentials

    def get_username_from_vouchers(self, credentials):
        """
        - Get first username from the list of credentials
        - Keyword Usage:
        - ``Get Username from vouchers   ${CREDENTIALS}``

        """
        username = list(credentials.keys())[0]
        return username
