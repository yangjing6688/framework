from time import sleep

from extauto.common.Screen import Screen
from extauto.common.Utils import Utils
from extauto.common.AutoActions import AutoActions
from extauto.xiq.flows.common.Navigator import Navigator
from extauto.xiq.elements.extreme_guest.ExtremeGuestOnboardingWebElements import ExtremeGuestOnboardingWebElements
from extauto.xiq.flows.extreme_guest.ExtremeGuest import ExtremeGuest
from extauto.common.CommonValidation import CommonValidation


class Onboarding(object):
    def __init__(self):
        super().__init__()
        self.navigator = Navigator()
        # self.driver = extauto.common.CloudDriver.cloud_driver
        self.screen = Screen()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.onboarding_web_elem = ExtremeGuestOnboardingWebElements()
        self.ext_guest = ExtremeGuest()
        self.common_validation = CommonValidation()

    def go_to_configure_onboarding_policy_tab(self):
        """
        - This keyword Will Navigate to Extreme Guest Onboarding Policy Page
        - Flow: Extreme Guest--> More Insights--> Extreme Guest Menu Window--> Configure--> Onboarding > Policy
        - Keyword Usage:
            ''Go To Configure Onboarding Policy Tab''

        :return: 1 if success
        """
        self.ext_guest.go_to_configure_page()
        self.utils.print_info("Clicking on Extreme Guest Configure > Onboarding Policy tab")
        self.auto_actions.click_reference(self.onboarding_web_elem.get_extreme_guest_onboarding_policy_tab)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        return 1

    def go_to_configure_onboarding_rules_tab(self):
        """
        - This keyword Will Navigate to Extreme Guest Onboarding Rules Page
        - Flow: Extreme Guest--> More Insights--> Extreme Guest Menu Window--> Configure--> Onboarding > Rules
        - Keyword Usage:
            ''Go To Configure Onboarding Rules Tab''

        :return: 1 if success
        """
        self.utils.print_info("Clicking on Extreme Guest Configure > Onboarding Rules tab")
        self.auto_actions.click_reference(self.onboarding_web_elem.get_extreme_guest_onboarding_rule_tab)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        return 1

    def add_onboarding_policy(self, policy_name=None, group_name=None, condition_type="Any", condition_value="Any", action_type="Register "
                                                "Client", user_notifpolicy = "UserNotificationPolicy", sponsor_notifpolicy = "SPApprovalNotificationPolicy", **kwargs):
        """
        - This keyword will navigate to onboarding policy page and add policy
        - Flow: Extreme Guest--> More Insights--> Extreme Guest Menu Window--> Configure--> Onboarding > Policy
                > Add Policy
        - Keyword Usage:
            ''Add Onboarding Policy ${POLICY_NAME} ${GROUP_NAME} ${CONDITION_TYPE} ${CONDITION_VALUE}  ${ACTION_TYPE}   ${USER_NOTIFICATION_POLICY}   ${SPONSOR_NOTIFICATION_POLICY}''


        :param group_name: name of the group to be added
        :param action_type: action to be performed
        :param condition_type: matching conditions
        :param policy_name: Name of the onboarding policy to be created
        :param condition_value: matching condition value
        :param user_notifpoliy: user notification policy
        :param sponsor_notifpolicy: sponsor notification policy
        :return: 1 if success
        """
        self.go_to_configure_onboarding_policy_tab()
        self.utils.print_info("Clicking the add policy icon ")
        self.auto_actions.click_reference(self.onboarding_web_elem.get_extreme_guest_onboarding_policy_add_policy)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Entering Policy name  ", policy_name)
        self.auto_actions.send_keys(self.onboarding_web_elem.get_extreme_guest_onboarding_policy_add_name(),
                                    policy_name)
        sleep(2)
        self.utils.print_info("Clicking Criteria Condition Drop Down Button")
        self.auto_actions.click_reference(self.onboarding_web_elem.get_extreme_guest_onboarding_policy_add_condition_dropdown)
        sleep(2)
        self.utils.print_info("Selecting the Criteria condition")
        self.auto_actions.select_drop_down_options(
            self.onboarding_web_elem.get_extreme_guest_onboarding_policy_add_condition_dropdown_items(), condition_type)
        sleep(2)

        if not ((condition_type == 'Social Type') or (condition_type == 'User Type') or (condition_type == 'Any') or (condition_type == 'User’s Device Count >')):
            self.utils.print_info("Entering Condition Value  ", condition_value)
            self.auto_actions.send_keys(self.onboarding_web_elem.get_extreme_guest_onboarding_policy_add_condition_dropdown_value(),
                                        condition_value)

        if (condition_type == 'User’s Device Count >'):
            self.utils.print_info("Entering user Condition Value  ", condition_value)
            self.auto_actions.send_keys(self.onboarding_web_elem.get_extreme_guest_onboarding_policy_add_condition_dropdown_value_Device_count(),
                                        condition_value)

        sleep(2)
        self.utils.print_info("Clicking Action Drop Down Button")
        self.auto_actions.click_reference(self.onboarding_web_elem.get_extreme_guest_onboarding_policy_add_action_dropdown)
        sleep(2)
        self.utils.print_info("Selecting the Action")
        self.auto_actions.select_drop_down_options(
            self.onboarding_web_elem.get_extreme_guest_onboarding_policy_add_action_dropdown_items(), action_type)
        sleep(2)
        self.utils.print_info("Clicking Group Drop Down Button")
        self.auto_actions.click_reference(
            self.onboarding_web_elem.get_extreme_guest_onboarding_policy_add_group_select_dropdown)

        self.utils.print_info("Selecting the Group")
        self.auto_actions.select_drop_down_options(
            self.onboarding_web_elem.get_extreme_guest_onboarding_policy_add_group_select_dropdown_items(), group_name)
        sleep(2)
        if ('User' in action_type) or ('Approval' in action_type):
            self.utils.print_info("Clicking User Notification Drop Down Button")

            self.auto_actions.click_reference(
                self.onboarding_web_elem.get_extreme_guest_onboarding_policy_add_usernotifpolicy_select_dropdown)
            self.utils.print_info("Selecting the User Notification")
            self.auto_actions.select_drop_down_options(
                self.onboarding_web_elem.get_extreme_guest_onboarding_policy_add_usernotifpolicy_select_dropdown_items(), user_notifpolicy)
        sleep(2)
        if 'Sponsor' in action_type:
            self.utils.print_info("Clicking Sponsor Notification Drop Down Button")
            self.auto_actions.click_reference(
                self.onboarding_web_elem.get_extreme_guest_onboarding_policy_add_spnotifpolicy_select_dropdown)
            self.utils.print_info("Selecting the Sponsor Notification")
            self.auto_actions.select_drop_down_options(
                self.onboarding_web_elem.get_extreme_guest_onboarding_policy_add_spnotifpolicy_select_dropdown_items(), sponsor_notifpolicy)

        self.utils.print_info("Clicking Save Button")
        self.auto_actions.click_reference(self.onboarding_web_elem.get_extreme_guest_onboarding_policy_add_save_button)
        sleep(5)
        self.utils.print_info("Clicking OK Button")
        self.auto_actions.click_reference(self.onboarding_web_elem.get_extreme_guest_onboarding_policy_add_save_ok_button)

        try:
            if self.onboarding_web_elem.get_extreme_guest_onboarding_policy_add_get_close_button().is_displayed():
                sleep(5)
                self.auto_actions.click_reference(self.onboarding_web_elem.get_extreme_guest_onboarding_policy_add_get_close_button)
                self.screen.save_screen_shot()
                self.utils.print_info("Click Duplicate OK Button")
        except Exception:
            self.utils.print_info("OK Button is already clicked")
            self.screen.save_screen_shot()

        self.screen.save_screen_shot()
        sleep(2)

        kwargs['pass_msg'] = "Successfully navigated to onboarding policy page and added policy"
        self.common_validation.passed(**kwargs)
        return 1

    def select_location_for_add_onboarding_rule_page(self, sel_loc, **kwargs):
        """
        - This keyword selects a location in the Eguest Add on boarding Rule Page
        - It is assumed that location is already created
        - Flow : Eguest Essentials --> More Insights --> Settings --> Onboarding --> Rules --> Add Rule --> Location
        - Keyword Usage:
        - ``Select Location For Add Onboarding Rule Page ${LOCATION}``

        :param sel_loc: location to select, in a comma-separated list format;
               e.g., Extreme Networks,Bangalore,Ecospace,Floor 1
        :return: 1 if location is selected, else -1'
        """
        ret_val = -1
        self.utils.print_info("Clicking Location Drop Down Button in Eguest Onboarding Rule Page")
        self.auto_actions.click_reference(self.onboarding_web_elem.get_extreme_guest_onboarding_rule_add_location_dropdown)
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
                    location_roots = self.onboarding_web_elem.get_extreme_guest_onboarding_rule_locations_root_name()
                    for location_root in location_roots:
                        if location_root_name.strip() in location_root.text:
                            self.utils.print_info("Match found for location type Root:", location_root_name)
                            root_expand_status = location_root.get_attribute('aria-expanded')
                            if root_expand_status == "true":
                                self.utils.print_info(f"Root Location {location_root} Already Expanded")
                            else:
                                root_name_expand_button = self.onboarding_web_elem.get_extreme_guest_onboarding_rule_locations_root_name_expand_button()
                                self.utils.print_info("Expanding the Root Location:", location_root_name)
                                self.auto_actions.click(root_name_expand_button)
                    sleep(5)

                if location_generic_name:
                    self.utils.print_info("Expanding Generic location: ", location_generic_name)
                    location_generics = self.onboarding_web_elem.get_extreme_guest_onboarding_rule_locations_city_name()
                    for location_generic in location_generics:
                        if location_generic_name.strip() in location_generic.text:
                            self.utils.print_info("Match found for location type Generic:", location_generic_name)
                            city_expand_status = location_generic.get_attribute('aria-expanded')
                            if city_expand_status == "true":
                                self.utils.print_info(f"Generic Location {location_generic_name} Already Expanded")
                            else:
                                generic_name_expand_button = self.onboarding_web_elem.get_extreme_guest_onboarding_rule_locations_city_name_expand_button()
                                self.utils.print_info("Expanding Generic Location:", location_generic_name)
                                self.auto_actions.click(generic_name_expand_button)
                    sleep(5)

                if location_building_name:
                    location_buildings = \
                        self.onboarding_web_elem.get_extreme_guest_onboarding_rule_locations_building_name()
                    for location_building in location_buildings:
                        self.utils.print_info("Expanding Building: ", location_building_name)
                        if location_building_name.strip() in location_building.text:
                            self.utils.print_info("Match found for location type Building:", location_building_name)
                            building_expand_status = location_building.get_attribute(
                                'aria-expanded')
                            if building_expand_status == "true":
                                self.utils.print_info(f"Building Location {location_building_name} Already Expanded")
                            else:
                                building_name_expand_button = self.onboarding_web_elem.get_extreme_guest_onboarding_rule_locations_building_name_expand_button()
                                self.utils.print_info("Expanding Building Location:", location_building_name)
                                self.auto_actions.click(building_name_expand_button)
                    sleep(5)

                if location_floor_name:
                    location_floors = self.onboarding_web_elem.get_extreme_guest_onboarding_rule_locations_floor_name()
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
            kwargs['fail_msg'] = "Cannot select location - location not specified in Eguest Onboarding Add Rule Page"
            self.common_validation.fault(**kwargs)

        return ret_val

    def add_onboarding_rule(self, rule_name=None, policy_name=None, network_name="All Networks", location_name=None, **kwargs):
        """
        - This keyword will navigate to onboarding rules page and add rule
        - Flow: Extreme Guest--> More Insights--> Extreme Guest Menu Window--> Configure--> Onboarding > Rules
                > Add rules
        - Keyword Usage:
            ''Add Onboarding Rule ${RULE_NAME} ${POLICY_NAME} ${NETWORK_NAME} ${LOCATION_NAME}''

        :param rule_name: Name of the rule to be created
        :param location_name: Name of location to be selected, in a comma-separated list format;
               e.g., Extreme Networks,Bangalore,Ecospace,Floor 1
        :param network_name: Name of network to be added
        :param policy_name: Name of the onboarding policy to be assigned
        :return: 1 if success
        """
        self.go_to_configure_onboarding_rules_tab()
        self.utils.print_info("Clicking the add Rules icon ")
        self.auto_actions.click_reference(self.onboarding_web_elem.get_extreme_guest_onboarding_rule_add_rule)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Entering Rule name  ", rule_name)
        self.auto_actions.send_keys(self.onboarding_web_elem.get_extreme_guest_onboarding_rule_add_name(), rule_name)

        self.utils.print_info("Clicking Policy Drop Down Button")
        self.auto_actions.click_reference(self.onboarding_web_elem.get_extreme_guest_onboarding_rule_add_policy_dropdown)

        self.utils.print_info("Selecting the Policy")
        self.auto_actions.select_drop_down_options(
            self.onboarding_web_elem.get_extreme_guest_onboarding_rule_add_policy_dropdown_items(), policy_name)

        self.utils.print_info("Clicking Network Drop Down Button")
        self.auto_actions.click_reference(self.onboarding_web_elem.get_extreme_guest_onboarding_rule_add_network_dropdown)

        self.utils.print_info("Selecting the Network")
        # Current implementation for 'All Networks'
        self.auto_actions.select_drop_down_options(
            self.onboarding_web_elem.get_extreme_guest_onboarding_rule_add_network_dropdown_items(), network_name)

        self.select_location_for_add_onboarding_rule_page(location_name)
        sleep(3)

        self.utils.print_info("Clicking Save Button")
        self.auto_actions.click_reference(self.onboarding_web_elem.get_extreme_guest_onboarding_rule_add_save_button)

        self.utils.print_info("Clicking OK Button")
        self.auto_actions.click_reference(self.onboarding_web_elem.get_extreme_guest_onboarding_rule_add_save_ok_button)

        try:
            if self.onboarding_web_elem.get_extreme_guest_onboarding_policy_add_get_close_button().is_displayed():
                self.auto_actions.click_reference(self.onboarding_web_elem.get_extreme_guest_onboarding_policy_add_get_close_button)
                self.screen.save_screen_shot()
                self.utils.print_info("Click Duplicate OK Button")
        except Exception:
            self.utils.print_info("OK Button is already clicked")
            self.screen.save_screen_shot()

        self.screen.save_screen_shot()
        sleep(2)

        kwargs['pass_msg'] = "Successfully navigated to onboarding rules page and added rule"
        self.common_validation.passed(**kwargs)
        return 1


    def add_onboarding_policy_existing_one(self, policy_name=None, group_name=None, condition_type="Any", condition_value="Any", action_type="Register "
                                                "Client", user_notifpolicy = "UserNotificationPolicy", sponsor_notifpolicy = "SPApprovalNotificationPolicy", **kwargs):
        """
        - This keyword will navigate to onboarding policy page and add policy
        - Flow: Extreme Guest--> More Insights--> Extreme Guest Menu Window--> Configure--> Onboarding > Policy
                > Add Policy
        - Keyword Usage:
            ''Add Onboarding Policy ${POLICY_NAME} ${GROUP_NAME} ${CONDITION_TYPE} ${CONDITION_VALUE}  ${ACTION_TYPE}   ${USER_NOTIFICATION_POLICY}   ${SPONSOR_NOTIFICATION_POLICY}''


        :param group_name: name of the group to be added
        :param action_type: action to be performed
        :param condition_type: matching conditions
        :param policy_name: Name of the onboarding policy to be created
        :param condition_value: matching condition value
        :param user_notifpoliy: user notification policy
        :param sponsor_notifpolicy: sponsor notificati  on policy
        :return: 1 if success
        """
        self.go_to_configure_onboarding_policy_tab()
        self.utils.print_info("Clicking existing name")
        self.auto_actions.click_reference(self.onboarding_web_elem.get_extreme_guest_onboarding_rule_name_add_rule_existing)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Clicking the add policy icon ")
        self.auto_actions.click_reference(self.onboarding_web_elem.get_extreme_guest_onboarding_rule_add_rule_existing)
        sleep(2)
        AutoActions.scroll_down(self)
        AutoActions.scroll_down(self)
        sleep(2)
        self.utils.print_info("Clicking Criteria Condition Drop Down Button")
        self.auto_actions.click_reference(self.onboarding_web_elem.get_extreme_guest_onboarding_policy_add_condition_dropdown_existing)
        self.utils.print_info("Selecting the Criteria condition")
        self.auto_actions.select_drop_down_options(
            self.onboarding_web_elem.get_extreme_guest_onboarding_policy_add_condition_dropdown_items(), condition_type)

        if not ((condition_type == 'Social Type') or (condition_type == 'User Type') or (condition_type == 'Any')):
            self.utils.print_info("Entering Condition Value  ", condition_value)
            self.auto_actions.send_keys(self.onboarding_web_elem.get_extreme_guest_onboarding_policy_add_condition_dropdown_value(),
                                        condition_value)
        sleep(2)
        self.utils.print_info("Clicking Action Drop Down Button")
        self.auto_actions.click_reference(self.onboarding_web_elem.get_extreme_guest_onboarding_policy_add_action_dropdown_existing)

        self.utils.print_info("Selecting the Action")
        self.auto_actions.select_drop_down_options(
            self.onboarding_web_elem.get_extreme_guest_onboarding_policy_add_action_dropdown_items(), action_type)
        AutoActions.scroll_down(self)
        self.utils.print_info("Clicking Group Drop Down Button")
        self.auto_actions.click_reference(
            self.onboarding_web_elem.get_extreme_guest_onboarding_policy_add_group_select_dropdown_existing)
        self.screen.save_screen_shot()
        sleep(2)
        self.utils.print_info("Selecting the Group")
        self.auto_actions.select_drop_down_options(
            self.onboarding_web_elem.get_extreme_guest_onboarding_policy_add_group_select_dropdown_items(), group_name)

        if ('User' in action_type) or ('Approval' in action_type):
            self.utils.print_info("Clicking User Notification Drop Down Button")
            self.auto_actions.click_reference(
                self.onboarding_web_elem.get_extreme_guest_onboarding_policy_add_usernotifpolicy_select_dropdown)

            self.utils.print_info("Selecting the User Notification")
            self.auto_actions.select_drop_down_options(
                self.onboarding_web_elem.get_extreme_guest_onboarding_policy_add_usernotifpolicy_select_dropdown_items(), user_notifpolicy)

        if 'Sponsor' in action_type:
            self.utils.print_info("Clicking Sponsor Notification Drop Down Button")
            self.auto_actions.click_reference(
                self.onboarding_web_elem.get_extreme_guest_onboarding_policy_add_spnotifpolicy_select_dropdown)

            self.utils.print_info("Selecting the Sponsor Notification")
            self.auto_actions.select_drop_down_options(
                self.onboarding_web_elem.get_extreme_guest_onboarding_policy_add_spnotifpolicy_select_dropdown_items(), sponsor_notifpolicy)
        self.screen.save_screen_shot()
        sleep(2)
        self.utils.print_info("Clicking Save Button")
        self.auto_actions.click_reference(self.onboarding_web_elem.get_extreme_guest_onboarding_policy_add_save_button)
        sleep(2)
        self.utils.print_info("Clicking OK Button")
        self.auto_actions.click_reference(self.onboarding_web_elem.get_extreme_guest_onboarding_policy_add_save_ok_button)

        self.screen.save_screen_shot()
        sleep(2)

        kwargs['pass_msg'] = "Successfully navigated to onboarding policy page and added policy"
        self.common_validation.passed(**kwargs)
        return 1
