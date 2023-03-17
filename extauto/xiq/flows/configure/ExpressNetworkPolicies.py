from time import sleep
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from extauto.xiq.flows.common.Navigator import Navigator
from extauto.common.CommonValidation import CommonValidation
from extauto.xiq.elements.NPExpressPolicyWebelEments import NPExpressPolicyWebElements


class ExpressNetworkPolicies(NPExpressPolicyWebElements):

    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.navigator = Navigator()
        self.screen = Screen()
        self.common_validation = CommonValidation()

    def _search_network_policy_in_card_view(self, policy_name):
        """
        - Check network policy exists in network polices card view

        :param policy_name: name of the policy to search
        :return: 1 if exists else None
        """
        for el in self.get_network_policy_list_from_card_view():
            if policy_name.upper() in el.text.upper():
                self.utils.print_info(el.text)
                return 1

    def _select_wireless_auth_type(self, auth_type):
        """
        - Select wireless authentication

        :param auth_type: Allowed Authentication type are: Open, PPSK, PSK, WEP, Enterprise
        :return:
        """
        self.utils.print_info("Click on authentication type drop down")
        auth_dropdown = self.get_wireless_auth_drop_down()
        if auth_dropdown:
            self.auto_actions.click(auth_dropdown)
            sleep(2)
        else:
            self.utils.print_info("Unable to find drop down to select Wireless Auth Type")
            self.screen.save_screen_shot()
            return -1

        self.utils.print_info(f"Selecting auth type:{auth_type}")
        auth_els = self.get_wireless_auth_select_elements()
        if auth_els:
            if self.auto_actions.select_drop_down_options(auth_els, auth_type):
                return 1
        else:
            self.utils.print_info("Unable to find Wireless Auth Type drop down elements")
            self.screen.save_screen_shot()
            return -1

        self.utils.print_info("Did not successfully select Wireless Auth Type")
        self.screen.save_screen_shot()
        return -1

    def create_open_auth_express_network_policy(self, policy_name, ssid_name, cwp=None, **kwargs):
        """
        - Create open network express network policy
        - Checks the policy already exists, if it is not exist then create the network policy
        - Keyword Usage:
        - ``Create Open Auth Express Network Policy  ${POLICY_NAME}   ${SSID_NAME}``
        - ``Create Open Auth Express Network Policy  ${POLICY_NAME}   ${SSID_NAME}   ${CWP_NAME}``

        :param policy_name: Policy Name
        :param ssid_name: SSID name
        :param cwp: Captive Portal name
        :return: 1
        """

        self.utils.print_info("Click on network policy card view button")
        self.navigator.navigate_to_network_policies_card_view_page()

        new_express_btn = self.get_new_account_express_policy_setup_button()
        new_express_policy_btn = self.get_add_new_express_policy_setup_button()

        if new_express_btn and new_express_btn.is_displayed():
            self.auto_actions.click(new_express_btn)
        elif new_express_policy_btn and new_express_policy_btn.is_displayed():
            self.auto_actions.click(new_express_policy_btn)
        else:
            sleep(1)
            if self._search_network_policy_in_card_view(policy_name):
                kwargs['pass_msg'] = f"Network policy:{policy_name} already exists in the network polices list"
                self.common_validation.passed(**kwargs)
                return 1

            self.utils.print_info("Click on Express policy setup button")
            express_btn = self.get_express_policy_setup_button()
            if express_btn:
                self.auto_actions.click(express_btn)
                sleep(2)
            else:
                kwargs['fail_msg'] = "Unable to find button to create express policy"
                self.common_validation.fault(**kwargs)
                return -1

        cancel_button = self.get_network_policy_cancel_button()

        self.utils.print_info("Enter the Network policy name")
        name_field = self.get_policy_name_text()
        if name_field:
            self.auto_actions.send_keys(name_field, policy_name)
        else:
            if cancel_button:
                self.auto_actions.click(cancel_button)
            kwargs['fail_msg'] = "Unable to find field to enter Policy Name"
            self.common_validation.fault(**kwargs)
            return -1

        self.utils.print_info("Select Create Wireless Network check box")
        wireless_cb = self.get_wireless_network_toggle_check_box()
        if wireless_cb:
            self.auto_actions.enable_check_box(wireless_cb)
            sleep(2)
        else:
            if cancel_button:
                self.auto_actions.click(cancel_button)
            kwargs['fail_msg'] = "Unable to find check box to select Create Wireless Network"
            self.common_validation.fault(**kwargs)
            return -1

        self.utils.print_info("Selecting the Wireless Auth Type: Open")
        if self._select_wireless_auth_type('Open') == -1:
            self.utils.print_info("Check the authentication type arguments")
            self.utils.print_info("Allowed Auth Type: WEP, Open, PSK, PPSK, Enterprise")
            if cancel_button:
                self.auto_actions.click(cancel_button)
            kwargs['fail_msg'] = "Unable to select Wireless Auth Type: Open"
            self.common_validation.fault(**kwargs)
            return -1

        self.utils.print_info(f"Enter the SSID Name:{ssid_name}")
        ssid_field = self.get_ssid_field()
        if ssid_field:
            self.auto_actions.send_keys(ssid_field, ssid_name)
        else:
            if cancel_button:
                self.auto_actions.click(cancel_button)
            kwargs['fail_msg'] = "Unable to find field to enter SSID"
            self.common_validation.fault(**kwargs)
            return -1

        cwp_cb = self.get_cwp_toggle_check_box()
        if cwp_cb:
            if not cwp:
                self.auto_actions.disable_check_box(cwp_cb)
            else:
                self.auto_actions.enable_check_box(cwp_cb)
                cwp_name_field = self.get_cwp_name_text_field()
                if cwp_name_field:
                    self.auto_actions.send_keys(cwp_name_field, cwp)
                else:
                    if cancel_button:
                        self.auto_actions.click(cancel_button)
                    kwargs['fail_msg'] = "Unable to find field to enter CWP name"
                    self.common_validation.fault(**kwargs)
                    return -1
        else:
            if cancel_button:
                self.auto_actions.click(cancel_button)
            kwargs['fail_msg'] = "Unable to find check box to select Create CWP"
            self.common_validation.fault(**kwargs)
            return -1

        self.utils.print_info("Click on network policy create button")
        create_btn = self.get_network_policy_create_button()
        if create_btn:
            self.auto_actions.click(create_btn)
            sleep(5)
        else:
            if cancel_button:
                self.auto_actions.click(cancel_button)
            kwargs['fail_msg'] = "Unable to find Create button to create the policy"
            self.common_validation.fault(**kwargs)
            return -1

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Click on network policy create Done button")
        done_btn = self.get_network_policy_dialog_done_button()
        if done_btn:
            self.auto_actions.click(done_btn)
            sleep(2)
        else:
            kwargs['fail_msg'] = "Unable to find Done button after creating the policy"
            self.common_validation.fault(**kwargs)
            return -1

        sleep(5)
        # Verify popup is closed by searching for the Done button again.  Race condition has done visible while
        #    not selectible.
        self.utils.print_info("Check express policy popup closed")
        for chk in range(2):
            try:
                done_btn_exists = self.get_network_policy_dialog_done_button()
                if done_btn_exists is not None:
                    if done_btn_exists.is_displayed():
                        if chk == 2:
                            kwargs['fail_msg'] = "Unable to close Express popup"
                            self.common_validation.fault(**kwargs)
                            return -1
                        sleep(2)
                        self.auto_actions.click(done_btn)
                        sleep(2)
                    else:
                        break
            except Exception:
                break

        kwargs['pass_msg'] = "Successfully created open auth express network policy"
        self.common_validation.passed(**kwargs)
        return 1

    def create_express_network_policy_no_wireless(self, policy_name):
        """
        - Create  network express network policy (no wireless)
        - Keyword Usage:
        - ``Create Express Network Policy No Wireless  ${POLICY_NAME}``
        :param policy_name: Policy Name
        :return: 1
        """
        self.utils.print_info("Click on network policy card view button")
        self.navigator.navigate_to_network_policies_card_view_page()
        new_express_btn = self.get_new_account_express_policy_setup_button()
        if new_express_btn and new_express_btn.is_displayed():
            self.utils.print_info("Clicking on Express Policy Setup")
            self.auto_actions.click(new_express_btn)
            self.utils.print_info("Setting Policy Name to " + policy_name)
            policy_name_text_field = self.get_policy_name_text()
            self.auto_actions.send_keys(policy_name_text_field, policy_name)
            self.utils.print_info("Uncheck Create Wireless Network checkbox")
            network_checkbox = self.get_wireless_network_toggle_check_box()
            self.auto_actions.click(network_checkbox)
            self.utils.print_info("Clicking on Create button")
            create_button = self.get_network_policy_create_button()
            self.auto_actions.click(create_button)
            done_button = self.get_network_policy_dialog_done_button()
            if done_button:
                self.utils.print_info("Clicking on Done button")
                self.auto_actions.click(done_button)
            else:
                self.utils.print_info("Could not locate Done button")
            return 1
        return -1
