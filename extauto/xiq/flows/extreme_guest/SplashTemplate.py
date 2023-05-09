from time import sleep

# from extauto.common.CloudDriver import CloudDriver
from extauto.common.Screen import Screen
from extauto.common.Utils import Utils
from extauto.common.AutoActions import AutoActions
from extauto.xiq.flows.common.Navigator import Navigator
from extauto.xiq.elements.extreme_guest.ExtremeGuestSplashTemplateWebElements import ExtremeGuestSplashTemplateWebElements
from extauto.xiq.elements.extreme_guest.ExtremeGuestWebElements import ExtremeGuestWebElements
from extauto.xiq.flows.extreme_guest.ExtremeGuest import ExtremeGuest
from extauto.common.CommonValidation import CommonValidation


class SplashTemplate(object):
    def __init__(self):
        super().__init__()
        self.navigator = Navigator()
        #self.driver = extauto.common.CloudDriver.cloud_driver
        self.screen = Screen()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.splash_web_elem = ExtremeGuestSplashTemplateWebElements()
        self.guest_web_elem = ExtremeGuestWebElements()
        self.ext_guest = ExtremeGuest()
        self.common_validation = CommonValidation()

    def go_to_configure_splash_template_tab(self):
        """
        - This keyword Will Navigate to Extreme Guest Splash Template
        - Flow: Extreme Guest--> More Insights--> Extreme Guest Menu Window--> Configure--> Splash Template
        - Keyword Usage:
            ''Go To Configure Splash Template Tab''

        :return: 1 if success
        """
        self.utils.print_info("Clicking on Extreme Guest Configure > Splash Template tab")
        self.auto_actions.click_reference(self.guest_web_elem.get_extreme_guest_configure_splash_template_tab)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        return 1

    def go_to_configure_splash_system_template_tab(self):
        """
        - This keyword Will Navigate to Extreme Guest System Splash Template
        - Flow: Extreme Guest--> More Insights--> Extreme Guest Menu Window--> Configure-->
                Splash Template--> System Template
        - Keyword Usage:
            ''Go To Configure Splash System Template Tab''

        :return: 1 if success
        """
        self.go_to_configure_splash_template_tab()
        self.utils.print_info("Clicking on Extreme Guest Configure > Splash Template > System Template tab")
        self.auto_actions.click_reference(self.splash_web_elem.get_extreme_guest_system_template_tab)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        return 1

    def go_to_configure_splash_user_template_tab(self):
        """
        - This keyword Will Navigate to Extreme Guest User Splash Template
        - Flow: Extreme Guest--> More Insights--> Extreme Guest Menu Window--> Configure-->
                Splash Template--> User Template
        - Keyword Usage:
            ''Go To Configure Splash User Template Tab''

        :return: 1 if success
        """
        self.utils.print_info("Clicking on Extreme Guest Configure > Splash Template > User Template tab")
        self.auto_actions.click_reference(self.splash_web_elem.get_extreme_guest_user_template_tab)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        return 1

    def clone_accept_connect_template(self, template_name=None, **kwargs):
        """
        - This keyword will clone the accept and connect template
        - Flow: Extreme Guest--> More Insights--> Extreme Guest Menu Window--> Configure-->
                Splash Template--> System Template--> Clone
        - Keyword Usage:
            ''Clone Accept Connect Template		${TEMPLATE_NAME}''

        :param template_name: Name of the user template to be created
        :return: 1 if success
        """
        self.go_to_configure_splash_system_template_tab()
        self.utils.print_info("Clicking the Clone icon on Accept and Connect Template")
        self.auto_actions.click_reference(self.splash_web_elem.get_extreme_guest_clone_accept_connect_icon)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Entering clone template name  ", template_name)
        self.auto_actions.send_keys(self.splash_web_elem.get_extreme_guest_clone_system_template_name_textbox(),
                                    template_name)
        sleep(4)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Clicking the Save button on the clone system template")
        self.auto_actions.click_reference(self.splash_web_elem.get_extreme_guest_clone_system_template_save_icon)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        kwargs['pass_msg'] = "Successfully cloned the the accept and connect template"
        self.common_validation.passed(**kwargs)
        return 1

    def clone_accept_connect_terms_template(self, template_name=None):
        """
        - This keyword will clone the Accept Connect with Terms Template
        - Flow: Extreme Guest--> More Insights--> Extreme Guest Menu Window--> Configure-->
                Splash Template--> System Template--> Clone
        - Keyword Usage:
            ''Clone Accept Connect Terms Template	${TEMPLATE_NAME}''

        :param template_name: Name of the user template to be created
        :return: 1 if success
        """
        self.go_to_configure_splash_system_template_tab()
        self.utils.print_info("Clicking the Clone icon on Accept and Connect with terms and agreement Template")
        self.auto_actions.click_reference(
            self.splash_web_elem.get_extreme_guest_clone_accept_and_connect_with_terms_and_agreement_icon)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Entering clone template name  ", template_name)
        self.auto_actions.send_keys(self.splash_web_elem.get_extreme_guest_clone_system_template_name_textbox(),
                                    template_name)
        sleep(4)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Clicking the Save button on the clone system template")
        self.auto_actions.click_reference(self.splash_web_elem.get_extreme_guest_clone_system_template_save_icon)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        return 1

    def clone_device_registration_with_social_wifi_template(self, template_name=None, **kwargs):
        """
        - This keyword will clone the Device Registration With Social Wifi Template
        - Flow: Extreme Guest--> More Insights--> Extreme Guest Menu Window--> Configure-->
                Splash Template--> System Template--> Clone
        - Keyword Usage:
            ''Clone Device Registration With Social Wifi Template	${TEMPLATE_NAME}''

        :param template_name: Name of the user template to be created
        :return: 1 if success
        """
        self.go_to_configure_splash_system_template_tab()

        sleep(2)

        if self.guest_web_elem.get_extreme_guest_configure_preview_button().is_displayed():
            self.utils.print_info("Clicking preview Button")
            self.auto_actions.click(self.guest_web_elem.get_extreme_guest_configure_preview_button())
            sleep(2)
        else:
            self.utils.print_info("No preview button available")
            sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Clicking the Clone icon on Device_Registration_with_Social_WiFi Template")
        self.auto_actions.click_reference(
            self.splash_web_elem.get_extreme_guest_clone_device_registration_with_social_wifi_icon)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Entering clone template name  ", template_name)
        self.auto_actions.send_keys(self.splash_web_elem.get_extreme_guest_clone_system_template_name_textbox(),
                                    template_name)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Clicking the Save button on the clone system template")
        self.auto_actions.click_reference(self.splash_web_elem.get_extreme_guest_clone_system_template_save_icon)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        kwargs['pass_msg'] = "Successfully cloned the Device Registration With Social Wifi Template"
        self.common_validation.passed(**kwargs)
        return 1

    def clone_email_access_template(self, template_name=None, **kwargs):
        """
        - This keyword will clone the Email Access Template
        - Flow: Extreme Guest--> More Insights--> Extreme Guest Menu Window--> Configure-->
                Splash Template--> System Template--> Clone
        - Keyword Usage:
            ''Clone Email Access Template	${TEMPLATE_NAME}''

        :param template_name: Name of the user template to be created
        :return: 1 if success
        """
        self.go_to_configure_splash_system_template_tab()
        self.utils.print_info("Clicking the Clone icon on Email_Access Template")
        self.auto_actions.click_reference(self.splash_web_elem.get_extreme_guest_clone_email_access_icon)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Entering clone template name  ", template_name)
        self.auto_actions.send_keys(self.splash_web_elem.get_extreme_guest_clone_system_template_name_textbox(),
                                    template_name)
        sleep(4)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Clicking the Save button on the clone system template")
        self.auto_actions.click_reference(self.splash_web_elem.get_extreme_guest_clone_system_template_save_icon)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        kwargs['pass_msg'] = "Successfully cloned the Email Access Template"
        self.common_validation.passed(**kwargs)
        return 1

    def clone_social_wifi_with_facebook_and_googleplus_template(self, template_name=None, **kwargs):
        """
        - This keyword will clone the Social Wifi With Facebook And Googleplus Template
        - Flow: Extreme Guest--> More Insights--> Extreme Guest Menu Window--> Configure-->
                Splash Template--> System Template--> Clone
        - Keyword Usage:
            ''Clone Social Wifi With Facebook And Googleplus Template	${TEMPLATE_NAME}''

        :param template_name: Name of the user template to be created
        :return: 1 if success
        """
        self.go_to_configure_splash_system_template_tab()
        self.utils.print_info("Clicking the Clone icon on Social_WiFi_with_Facebook_and_GooglePlus Template")
        self.auto_actions.click_reference(
            self.splash_web_elem.get_extreme_guest_clone_social_wifi_with_facebook_and_googleplus_icon)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Entering clone template name  ", template_name)
        self.auto_actions.send_keys(self.splash_web_elem.get_extreme_guest_clone_system_template_name_textbox(),
                                    template_name)
        sleep(4)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Clicking the Save button on the clone system template")
        self.auto_actions.click_reference(self.splash_web_elem.get_extreme_guest_clone_system_template_save_icon)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        kwargs['pass_msg'] = "Successfully cloned the Social Wifi With Facebook And Googleplus Template"
        self.common_validation.passed(**kwargs)
        return 1

    def clone_social_wifi_with_all_template(self, template_name=None, **kwargs):
        """
        - This keyword will clone the Social Wifi With All Template
        - Flow: Extreme Guest--> More Insights--> Extreme Guest Menu Window--> Configure-->
                Splash Template--> System Template--> Clone
        - Keyword Usage:
            ''Clone Social Wifi With All Template	${TEMPLATE_NAME}''

        :param template_name: Name of the user template to be created
        :return: 1 if success
        """
        self.go_to_configure_splash_system_template_tab()

        sleep(2)

        if self.guest_web_elem.get_extreme_guest_configure_preview_button().is_displayed():
            self.utils.print_info("Clicking preview Button")
            self.auto_actions.click_reference(self.guest_web_elem.get_extreme_guest_configure_preview_button)
            sleep(2)
        else:
            self.utils.print_info("No preview button available")
            sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Clicking the Clone icon on Social_WiFi_with_all Template")
        self.auto_actions.click_reference(self.splash_web_elem.get_extreme_guest_clone_social_wifi_with_all_icon)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Entering clone template name  ", template_name)
        self.auto_actions.send_keys(self.splash_web_elem.get_extreme_guest_clone_system_template_name_textbox(),
                                    template_name)
        sleep(4)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Clicking the Save button on the clone system template")
        self.auto_actions.click_reference(self.splash_web_elem.get_extreme_guest_clone_system_template_save_icon)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        kwargs['pass_msg'] = "Successfully cloned the Social Wifi With All Template"
        self.common_validation.passed(**kwargs)
        return 1

    def clone_sponsored_guest_access_template(self, template_name=None, **kwargs):
        """
        - This keyword will clone the Sponsored Guest Access Template
        - Flow: Extreme Guest--> More Insights--> Extreme Guest Menu Window--> Configure-->
                Splash Template--> System Template--> Clone
        - Keyword Usage:
            ''Clone Sponsored Guest Access Template		${TEMPLATE_NAME}''

        :param template_name: Name of the user template to be created
        :return: 1 if success
        """
        self.go_to_configure_splash_system_template_tab()
        self.utils.print_info("Clicking the Clone icon on Sponsored_Guest_Access Template")
        self.auto_actions.click_reference(self.splash_web_elem.get_extreme_guest_clone_sponsored_guest_access_icon)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Entering clone template name  ", template_name)
        self.auto_actions.send_keys(self.splash_web_elem.get_extreme_guest_clone_system_template_name_textbox(),
                                    template_name)
        sleep(4)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Clicking the Save button on the clone system template")
        self.auto_actions.click_reference(self.splash_web_elem.get_extreme_guest_clone_system_template_save_icon)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        kwargs['pass_msg'] = "Successfully cloned the Sponsored Guest Access Template"
        self.common_validation.passed(**kwargs)
        return 1

    def clone_user_reg_with_social_forgot_passcode_template(self, template_name=None, **kwargs):
        """
        - This keyword will clone the User Reg With Social Forgot Passcode Template
        - Flow: Extreme Guest--> More Insights--> Extreme Guest Menu Window--> Configure-->
                Splash Template--> System Template--> Clone
        - Keyword Usage:
            ''Clone User Reg With Social Forgot Passcode Template	${TEMPLATE_NAME}''

        :param template_name: Name of the user template to be created
        :return: 1 if success
        """
        self.go_to_configure_splash_system_template_tab()
        self.utils.print_info("Clicking the Clone icon on User_Reg_With_Social_Forgot_Passcode Template")
        self.auto_actions.click_reference(
            self.splash_web_elem.get_extreme_guest_clone_user_reg_with_social_forgot_passcode_icon)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Entering clone template name  ", template_name)
        self.auto_actions.send_keys(self.splash_web_elem.get_extreme_guest_clone_system_template_name_textbox(),
                                    template_name)
        sleep(4)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Clicking the Save button on the clone system template")
        self.auto_actions.click_reference(self.splash_web_elem.get_extreme_guest_clone_system_template_save_icon)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        kwargs['pass_msg'] = "Successfully cloned the User Reg With Social Forgot Passcode Template"
        self.common_validation.passed(**kwargs)
        return 1

    def clone_user_registration_with_social_wifi_template(self, template_name=None, **kwargs):
        """
        - This keyword will clone the User Registration With Social Wifi Template
        - Flow: Extreme Guest--> More Insights--> Extreme Guest Menu Window--> Configure-->
                Splash Template--> System Template--> Clone
        - Keyword Usage:
            ''Clone User Registration With Social Wifi Template	${TEMPLATE_NAME}''

        :param template_name: Name of the user template to be created
        :return: 1 if success
        """
        self.go_to_configure_splash_system_template_tab()

        sleep(2)

        if self.guest_web_elem.get_extreme_guest_configure_preview_button().is_displayed():
            self.utils.print_info("Clicking preview Button")
            self.auto_actions.click(self.guest_web_elem.get_extreme_guest_configure_preview_button())
            sleep(2)
        else:
            self.utils.print_info("No preview button available")
            sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Clicking the Clone icon on User_Registration_with_Social_WiFi Template")
        self.auto_actions.click_reference(self.splash_web_elem.get_extreme_guest_clone_user_registration_with_social_wifi_icon)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Entering clone template name  ", template_name)
        self.auto_actions.send_keys(self.splash_web_elem.get_extreme_guest_clone_system_template_name_textbox(),
                                    template_name)
        sleep(4)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Clicking the Save button on the clone system template")
        self.auto_actions.click_reference(self.splash_web_elem.get_extreme_guest_clone_system_template_save_icon)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        kwargs['pass_msg'] = "Successfully cloned the User Registration With Social Wifi Template"
        self.common_validation.passed(**kwargs)
        return 1

    def apply_network_to_user_template(self, network_name=None, template_name=None, location=None, **kwargs):
        """
        - This keyword will Apply the Network and Location To User Template
        - Flow: Extreme Guest--> More Insights--> Extreme Guest Menu Window--> Configure-->
                Splash Template--> System Template--> Clone
        - Keyword Usage:
            ''Apply Network To User Template	${NETWORK_NAME}	${TEMPLATE_NAME}''

        :param template_name: Name of the user template to be selected
        :param network_name: Name of the network to be selected
        :param location : Location Tree in comma format  e.g., Extreme Networks,Bangalore,Ecospace,Floor 1
        :return: 1 if success
        """
        self.go_to_configure_splash_user_template_tab()
        self.utils.print_info("Clicking on the Apply network the user template icon")
        web_element_fn = "self.splash_web_elem.get_extreme_guest_user_" + template_name + "_apply_icon()"
        self.auto_actions.click(eval(web_element_fn))
        sleep(2)

        if location:
            self.utils.print_info("Selecting the Location: ", location)
            self.select_location_for_apply_user_template_page(location)

        self.utils.print_info("Clicking Network name Name Drop Down Button")
        self.auto_actions.click_reference(self.splash_web_elem.get_extreme_guest_user_test_template_apply_network_dropdown)
        sleep(2)

        self.utils.print_info("Selecting the Network Name")
        self.auto_actions.select_drop_down_options(
            self.splash_web_elem.get_extreme_guest_user_test_template_apply_network_dropdown_items_new(),
            network_name)
        sleep(2)

        self.utils.print_info("Clicking Add Button")
        self.auto_actions.click_reference(self.splash_web_elem.get_extreme_guest_user_test_template_apply_network_add_button)
        sleep(2)

        self.utils.print_info("Clicking Apply Button")
        self.auto_actions.click_reference(self.splash_web_elem.get_extreme_guest_user_test_template_apply_network_apply_button)
        sleep(3)

        self.utils.print_info("Clicking OK Button")
        self.auto_actions.click_reference(self.splash_web_elem.get_extreme_guest_user_test_template_apply_network_apply_ok_button)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        kwargs['pass_msg'] = "Successfully Applied the Network and Location To User Template"
        self.common_validation.passed(**kwargs)
        return 1

    def remove_network_from_user_template(self, template_name=None, **kwargs):
        """
        - This keyword will Apply the Network and Location To User Template
        - Flow: Extreme Guest--> More Insights--> Extreme Guest Menu Window--> Configure-->
                Splash Template--> System Template--> Clone
        - Keyword Usage:
            ''Remove Network From User Template	${TEMPLATE_NAME}''

        :param template_name: Name of the user template to be selected
        :param network_name: Name of the network to be selected
        :param location : Location Tree in comma format  e.g., Extreme Networks,Bangalore,Ecospace,Floor 1
        :return: 1 if success
        """
        self.go_to_configure_splash_user_template_tab()
        self.utils.print_info("Clicking on the Apply network the user template icon")
        web_element_fn = "self.splash_web_elem.get_extreme_guest_user_" + template_name + "_apply_icon()"
        self.auto_actions.click(eval(web_element_fn))
        sleep(2)

        if self.splash_web_elem.get_extreme_guest_user_test_template_apply_network_delete_button().is_displayed():
            self.utils.print_info("Clicking Delete Button")
            self.auto_actions.click_reference(self.splash_web_elem.get_extreme_guest_user_test_template_apply_network_delete_button)
            sleep(2)
        else:
            self.utils.print_info("No policy/location mapping for the template")
            sleep(2)

        self.utils.print_info("Clicking Apply Button")
        self.auto_actions.click_reference(self.splash_web_elem.get_extreme_guest_user_test_template_apply_network_apply_button)
        sleep(2)

        self.utils.print_info("Clicking OK Button")
        self.auto_actions.click_reference(self.splash_web_elem.get_extreme_guest_user_test_template_apply_network_apply_ok_button)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        kwargs['pass_msg'] = "Successfully Applied the Network and Location To User Template"
        self.common_validation.passed(**kwargs)
        return 1

    def select_location_for_apply_user_template_page(self, sel_loc, **kwargs):
        """
        - This keyword selects a location in apply user template page
        - It is assumed that location is already created
        - Flow : Eguest Essentials --> More Insights --> Settings -->Splash Templates -->user Templates-->apply --> Location
        - Keyword Usage:
        - ``Select Location For Apply User Template Page ${LOCATION}``

        :param sel_loc: location to select, in a comma-separated list format (e.g., Extreme Networks,Bangalore,Ecospace,Floor 1)
        :return: 1 if location is selected, else -1'
        """
        ret_val = -1
        self.utils.print_info("Clicking Location Drop Down Button in Apply Template")
        self.auto_actions.click_reference(self.splash_web_elem.get_extreme_guest_user_test_template_apply_location_dropdown)
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
                    location_roots = self.splash_web_elem.get_extreme_guest_apply_user_template_locations_root_name()
                    for location_root in location_roots:
                        if location_root_name.strip() in location_root.text:
                            self.utils.print_info("Match found for location type Root:", location_root_name)
                            root_expand_status = location_root.get_attribute('aria-expanded')
                            if root_expand_status == "true":
                                self.utils.print_info(f"Root Location {location_root} Already Expanded")
                                self.screen.save_screen_shot()
                            else:
                                root_name_expand_button = self.splash_web_elem.get_extreme_guest_apply_user_template_locations_root_expand_button()
                                self.utils.print_info("Expanding the Root Location:", location_root_name)
                                self.auto_actions.click(root_name_expand_button)
                                self.screen.save_screen_shot()
                    sleep(5)

                if location_generic_name:
                    self.utils.print_info("Expanding Generic location: ", location_generic_name)
                    location_generics = self.splash_web_elem.get_extreme_guest_apply_user_template_locations_city_name()
                    for location_generic in location_generics:
                        if location_generic_name.strip() in location_generic.text:
                            self.utils.print_info("Match found for location type Generic:", location_generic_name)
                            city_expand_status = location_generic.get_attribute('aria-expanded')
                            if city_expand_status == "true":
                                self.utils.print_info(f"Generic Location {location_generic_name} Already Expanded")
                                self.screen.save_screen_shot()
                            else:
                                generic_name_expand_button = self.splash_web_elem.get_extreme_guest_apply_user_template_locations_city_expand_button()
                                self.utils.print_info("Expanding Generic Location:", location_generic_name)
                                self.auto_actions.click(generic_name_expand_button)
                                self.screen.save_screen_shot()
                    sleep(5)

                if location_building_name:
                    location_buildings = \
                        self.splash_web_elem.get_extreme_guest_apply_user_template_locations_building_name()
                    for location_building in location_buildings:
                        self.utils.print_info("Expanding Building: ", location_building_name)
                        if location_building_name.strip() in location_building.text:
                            self.utils.print_info("Match found for location type Building:", location_building_name)
                            building_expand_status = location_building.get_attribute(
                                'aria-expanded')
                            if building_expand_status == "true":
                                self.utils.print_info(f"Building Location {location_building_name} Already Expanded")
                                self.screen.save_screen_shot()
                            else:
                                building_name_expand_button = self.splash_web_elem.get_extreme_guest_apply_user_template_locations_building_expand_button()
                                self.utils.print_info("Expanding Building Location:", location_building_name)
                                self.auto_actions.click(building_name_expand_button)
                                self.screen.save_screen_shot()
                    sleep(5)

                if location_floor_name:
                    location_floors = self.splash_web_elem.get_extreme_guest_apply_user_template_locations_floor_name()
                    for location_floor in location_floors:
                        self.utils.print_info("Selecting Floor: ", location_floor_name)
                        if location_floor_name.strip() in location_floor.text:
                            self.utils.print_info("Match found for location type Generic:", location_floor_name)
                            self.auto_actions.click(location_floor)
                            self.screen.save_screen_shot()
                            sleep(5)
                        else:
                            self.utils.print_info(f"Floor Name {location_floor_name} Not Found")
                ret_val = 1

            except Exception as e:
                self.utils.print_info(e)
                self.utils.print_info("Unable to select location")
        else:
            kwargs['fail_msg'] = "Cannot select location - location not specified in User Template apply page Page"
            self.common_validation.fault(**kwargs)

        return ret_val
