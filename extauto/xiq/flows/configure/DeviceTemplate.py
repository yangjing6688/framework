from time import sleep
from selenium.webdriver.common.keys import Keys

from extauto.common.CloudDriver import CloudDriver
from extauto.common.AutoActions import AutoActions
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen

import extauto.xiq.flows.common.ToolTipCapture as tool_tip

from extauto.xiq.flows.configure.NetworkPolicy import NetworkPolicy
from extauto.xiq.flows.common.Navigator import Navigator

from extauto.xiq.elements.DeviceTemplateWebElements import DeviceTemplateWebElements
from extauto.xiq.elements.NavigatorWebElements import NavigatorWebElements
from extauto.xiq.elements.NetworkPolicyWebElements import NetworkPolicyWebElements
from extauto.common.CommonValidation import CommonValidation


class DeviceTemplate(object):

    def __init__(self):
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        # self.driver = extauto.common.CloudDriver.cloud_driver
        self.navigator = NavigatorWebElements()
        self.np_web_elements = NetworkPolicyWebElements()
        self.device_template_web_elements = DeviceTemplateWebElements()
        self.network_policy = NetworkPolicy()
        self.navigator = Navigator()
        self.common_validation = CommonValidation()

    def check_ap_template(self, ap_template, **kwargs):
        """
        - Check the AP template in th AP template Grid
        - Keyword Usage
        - ``Check AP Template  ${AP_TEMPLATE_NAME}``

        :param ap_template: Ap Template Name ie AP630,AP410C
        :return: True if AP Template Found on Grid else False
        """
        self.utils.print_info("Click on Device Template tab button")
        self.auto_actions.click_reference(self.device_template_web_elements.get_add_device_template_menu)
        sleep(2)

        self.utils.print_info("Click on AP Template Menu button")
        self.auto_actions.click_reference(self.device_template_web_elements.get_ap_template_tab)
        sleep(2)

        ap_template_rows_elements = self.device_template_web_elements.get_ap_template_rows()
        if not ap_template_rows_elements:
            kwargs['fail_msg'] = "check_ap_template() failed. AP Template NOT Found "
            self.common_validation.failed(**kwargs)
            return False
        for el in ap_template_rows_elements:
            if ap_template.upper() in el.text.upper():
                kwargs['pass_msg'] = "Template Already present in the template grid"
                self.common_validation.passed(**kwargs)
                return True

        kwargs['fail_msg'] = "AP Template NOT Found "
        self.common_validation.failed(**kwargs)
        return False

    def add_ap_template(self, ap_model, ap_template_name, wifi_interface_config, **kwargs):
        """
        - Checking the AP template present in the AP Templates Grid
        - If it is not there add New AP Template
        - WiFi2 config was removed as per jira ticket EXTAUTO-113 and APC-44337.
        - Keyword Usage
        - ``Add AP Template  ${AP_MODEL}   ${AP_TEMPLATE_NAME}  ${WIFI_INTERFACE_CONFIG}``

        :param ap_model: AP MODEL ie AP630,AP410C
        :param ap_template_name: AP Template Name ie prod_sanity_ap410ctemplate
        :param wifi_interface_config: (Config Dict) Enable/Disable Client Access,Backhaul Mesh Link,Sensor
        :return: 1 if AP Template Configured Successfully else -1
        """
        wifi0_config = wifi_interface_config['wifi0_configuration']
        wifi1_config = wifi_interface_config['wifi1_configuration']
        wifi2_config = wifi_interface_config.get('wifi2_configuration', 'None')

        sleep(5)

        if self.check_ap_template(ap_template_name, ignore_failure=True):
            kwargs['pass_msg'] = "Template Already present in the template grid"
            self.common_validation.passed(**kwargs)
            return 1

        self.utils.print_info("Click on AP Template add button")
        self.auto_actions.click_reference(self.device_template_web_elements.get_ap_template_add_button)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("select the AP: ", ap_model)
        self.utils.print_info("Enter AP Model in the search box")
        self.auto_actions.send_keys(self.device_template_web_elements.get_device_ap_template_search_inputfield(),
                                    ap_model)
        ap_list_items = self.device_template_web_elements.get_ap_template_platform_from_drop_down()
        for el in ap_list_items:
            print(el.text)
            if not el:
                pass
            if ap_model.upper() in el.text.upper():
                self.auto_actions.click(el)
                break
        sleep(3)

        self.utils.print_info("Enter the AP Template Name")
        self.auto_actions.send_keys(self.device_template_web_elements.get_ap_template_text(), ap_template_name)
        sleep(3)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Configure WiFI0 Interface for AP Template")
        self.config_ap_template_wifi0(**wifi0_config)
        sleep(3)

        self.utils.print_info("Configure WiFI1 Interface for AP Template")
        self.config_ap_template_wifi1(**wifi1_config)
        sleep(3)

        if not wifi2_config == 'None':
            self.config_ap_template_wifi2(**wifi2_config)

        self.utils.print_info("Click on the save template button")
        self.auto_actions.scroll_up()
        del tool_tip.tool_tip_text[:]
        self.auto_actions.click_reference(self.device_template_web_elements.get_ap_template_save_button)
        sleep(2)

        self.utils.print_info("Checking the Save profile message...")
        observed_profile_message = tool_tip.tool_tip_text[-1]
        self.utils.print_info("Observed Message: ", observed_profile_message)
        self.screen.save_screen_shot()
        sleep(2)

        result = 1
        if "AP template was saved successfully" in observed_profile_message:
            kwargs['pass_msg'] = "AP template was saved successfully"
            self.common_validation.passed(**kwargs)
        else:
            kwargs['fail_msg'] = "Failed to add AP template"
            self.common_validation.failed(**kwargs)
            result = -1
        del tool_tip.tool_tip_text[:]
        return result

    def edit_ap_net_policy_template_wifi2(self, policy_name, **kwargs):
        """
        - Selects the given network policy and edit, selects the AP Template and edit wifi2 and disable
        - Keyword Usage
        - ``Edit AP Net Policy Template Wifi2   ${POLICY_NAME}``

        :param policy_name: Network Policy Name
        :return: 1 if Editing is successful on AP Template or else -1
        """

        self.network_policy.navigate_to_np_edit_tab(policy_name)

        self.utils.print_info("Click on Device Template tab")
        self.auto_actions.click_reference(self.device_template_web_elements.get_select_device_template)

        self.utils.print_info("Click on AP Template")
        self.auto_actions.click_reference(self.device_template_web_elements.get_select_ap_template)

        self.utils.print_info("Click on WiFi2 Tab on AP Template page")
        self.auto_actions.click_reference(self.device_template_web_elements.get_device_template_ap_template_wifi2_tab)

        self.auto_actions.scroll_down()

        self.utils.print_info("Disable Radio Status on WiFi2 Interface")
        if self.device_template_web_elements.get_wifi2_radio_status_button().is_selected():
            self.auto_actions.click_reference(self.device_template_web_elements.get_wifi2_radio_status_button)

            self.screen.save_screen_shot()

        self.auto_actions.scroll_up()

        self.utils.print_info("Click on the save template button")
        self.auto_actions.click_reference(self.device_template_web_elements.get_ap_template_save_button)

        tool_tip_text = tool_tip.tool_tip_text
        self.screen.save_screen_shot()
        self.utils.print_info("Tool tip Text Displayed on Page", tool_tip_text)
        sub_string = "template"
        strings_with_substring = [msg for msg in tool_tip_text if sub_string in msg]
        self.utils.print_info("Tool tip Text ap template", strings_with_substring)
        if "AP template was saved successfully" in str(strings_with_substring):
            kwargs['pass_msg'] = "AP template was saved successfully"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Failed to edit AP network policy"
            self.common_validation.failed(**kwargs)
            return -1

    def config_ap_template_wifi0(self, **wifi0_profile):
        """
        - Configure the WIFI0 configuration on AP Template
        - Keyword Usage
        - ``Config AP Template WiFi0  &{WIFI0_CONFIG}``

        :param wifi0_profile: (Config Dict) Enable/Disable Client Access,Backhaul Mesh Link,Sensor
        :return: 1 if WiFi0 Profile Configured Successfully else None
        """
        client_access_status_wifi0 = wifi0_profile.get('client_access', 'Enable')
        backhaul_mesh_status_wifi0 = wifi0_profile.get('backhaul_mesh_link', 'Enable')
        sensor_status_wifi0 = wifi0_profile.get('sensor', 'Enable')
        radio_profile_wifi0 = wifi0_profile.get('radio_profile', 'radio_ng_11ax-2g')

        self.utils.print_info("Click on WiFi0 Tab on AP Template page")
        self.auto_actions.click_reference(self.device_template_web_elements.get_device_template_ap_template_wifi0_tab)
        sleep(3)

        CloudDriver().cloud_driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
        self.utils.print_info(f"select Radio Profile:{radio_profile_wifi0}")
        sleep(2)
        self.auto_actions.click_reference(self.device_template_web_elements.get_wifi0_radio_profile_drop_down)
        self.auto_actions.select_drop_down_options(self.device_template_web_elements.
                                                   get_wifi0_radio_profile_drop_down_opts(), radio_profile_wifi0)
        if client_access_status_wifi0.upper() == "ENABLE":
            self.utils.print_info("Enable Client Access Checkbox on WiFi0 Interface")
            if not self.device_template_web_elements.get_client_access_checkbox_wifi0().is_selected():
                self.auto_actions.click_reference(self.device_template_web_elements.get_client_access_checkbox_wifi0)
                sleep(5)
        else:
            self.utils.print_info("Disable Client Access check box on WiFi0 Interface")
            if self.device_template_web_elements.get_client_access_checkbox_wifi0().is_selected():
                self.auto_actions.click_reference(self.device_template_web_elements.get_client_access_checkbox_wifi0)
                sleep(5)

        if backhaul_mesh_status_wifi0.upper() == "ENABLE":
            self.utils.print_info("Enable Backhaul Mesh Link Checkbox on WiFi0 Interface")
            if not self.device_template_web_elements.get_backhaul_mesh_link_checkbox_wifi0().is_selected():
                self.auto_actions.click_reference(self.device_template_web_elements.get_backhaul_mesh_link_checkbox_wifi0)
                sleep(5)
        else:
            self.utils.print_info("Disable Backhaul Mesh Link Checkbox on WiFi0 Interface")
            if self.device_template_web_elements.get_backhaul_mesh_link_checkbox_wifi0().is_selected():
                self.auto_actions.click_reference(self.device_template_web_elements.get_backhaul_mesh_link_checkbox_wifi0)
                sleep(5)

        if self.device_template_web_elements.get_sensor_checkbox_wifi0().is_displayed():
            if sensor_status_wifi0.upper() == "ENABLE":
                self.utils.print_info("Enable Sensor Checkbox on WiFi0 Interface")
                if not self.device_template_web_elements.get_sensor_checkbox_wifi0().is_selected():
                    self.auto_actions.click_reference(self.device_template_web_elements.get_sensor_checkbox_wifi0)
                    sleep(5)
            else:
                self.utils.print_info("Disable Sensor Checkbox on WiFi0 Interface")
                if self.device_template_web_elements.get_sensor_checkbox_wifi0().is_selected():
                    self.auto_actions.click_reference(self.device_template_web_elements.get_sensor_checkbox_wifi0)
                    sleep(5)

            self.screen.save_screen_shot()
            sleep(2)

        if self.device_template_web_elements.get_wifi0_sdr_checkbox():
            self.utils.print_info("Disable SDR Checkbox")
            if self.device_template_web_elements.get_wifi0_sdr_checkbox().is_selected():
                self.auto_actions.click_reference(self.device_template_web_elements.get_wifi0_sdr_checkbox)
                sleep(5)

        CloudDriver().cloud_driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_UP)
        sleep(5)
        return 1

    def config_ap_template_wifi1(self, **wifi1_profile):
        """
        - Configure the WIFI1 configuration on AP Template
        - Keyword Usage
        - ``Config AP Template WiFi1  &{WIFI1_CONFIG}``

        :param wifi1_profile: (Config Dict) Enable/Disable Client Access,Backhaul Mesh Link,Sensor
        :return: 1 if WiFi1 Profile Configured Successfully else None
        """
        client_access_status_wifi1 = wifi1_profile.get('client_access', 'Enable')
        backhaul_mesh_status_wifi1 = wifi1_profile.get('backhaul_mesh_link', 'Enable')
        sensor_status_wifi1 = wifi1_profile.get('sensor', 'Enable')
        radio_profile_wifi1 = wifi1_profile.get('radio_profile', 'radio_ng_11ax-5g')
        self.utils.print_info("Click on WiFi1 Tab on AP Template page")
        self.auto_actions.click_reference(self.device_template_web_elements.get_device_template_ap_template_wifi1_tab)
        sleep(5)

        CloudDriver().cloud_driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)

        self.utils.print_info(f"select Radio Profile:{radio_profile_wifi1}")
        sleep(2)
        self.auto_actions.click_reference(self.device_template_web_elements.get_wifi1_radio_profile_drop_down)
        self.auto_actions.select_drop_down_options(self.device_template_web_elements.
                                                   get_wifi1_radio_profile_drop_down_opts(), radio_profile_wifi1)
        if client_access_status_wifi1.upper() == "ENABLE":
            self.utils.print_info("Enable Client Access Checkbox on WiFi1 Interface")
            if not self.device_template_web_elements.get_client_access_checkbox_wifi1().is_selected():
                self.auto_actions.click_reference(self.device_template_web_elements.get_client_access_checkbox_wifi1)
                sleep(5)
        else:
            self.utils.print_info("Disable Client Access check box on WiFi1 Interface")
            if self.device_template_web_elements.get_client_access_checkbox_wifi1().is_selected():
                self.auto_actions.click_reference(self.device_template_web_elements.get_client_access_checkbox_wifi1)
                sleep(5)

        if backhaul_mesh_status_wifi1.upper() == "ENABLE":
            self.utils.print_info("Enable Backhaul Mesh Link Checkbox on WiFi1 Interface")
            if not self.device_template_web_elements.get_backhaul_mesh_link_checkbox_wifi1().is_selected():
                self.auto_actions.click_reference(self.device_template_web_elements.get_backhaul_mesh_link_checkbox_wifi1)
                sleep(5)
        else:
            self.utils.print_info("Disable Backhaul Mesh Link Checkbox on WiFi1 Interface")
            if self.device_template_web_elements.get_backhaul_mesh_link_checkbox_wifi1().is_selected():
                self.auto_actions.click_reference(self.device_template_web_elements.get_backhaul_mesh_link_checkbox_wifi1)
                sleep(5)

        if self.device_template_web_elements.get_sensor_checkbox_wifi1().is_displayed():
            if sensor_status_wifi1.upper() == "ENABLE":
                self.utils.print_info("Enable Sensor Checkbox on WiFi1 Interface")
                if not self.device_template_web_elements.get_sensor_checkbox_wifi1().is_selected():
                    self.auto_actions.click_reference(self.device_template_web_elements.get_sensor_checkbox_wifi1)
                    sleep(5)
            else:
                self.utils.print_info("Disable Sensor Checkbox on WiFi1 Interface")
                if self.device_template_web_elements.get_sensor_checkbox_wifi1().is_selected():
                    self.auto_actions.click_reference(self.device_template_web_elements.get_sensor_checkbox_wifi1)
                    sleep(5)

            self.screen.save_screen_shot()
            sleep(2)
        CloudDriver().cloud_driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_UP)
        sleep(5)
        return 1

    def config_ap_template_wifi2(self, **wifi2_profile):
        """
        - Configure the WIFI2 configuration on AP Template
        - Keyword Usage
        - ``Config AP Template WiFi2  &{WIFI2_CONFIG}``

        :param wifi2_profile: (Config Dict) WiFi2 ADSP server Config ie primary server ip and port
        :return: 1 if WiFi2 Profile Configured Successfully else None
        """
        client_access_status_wifi2 = wifi2_profile.get('client_access', 'Disable')
        backhaul_mesh_status_wifi2 = wifi2_profile.get('backhaul_mesh_link', 'Disable')
        sensor_status_wifi2 = wifi2_profile.get('sensor', 'Enable')
        radio_status_wifi2 = wifi2_profile.get('radio_status', 'Enable')
        self.utils.print_info("Click on WiFi2 Tab on AP Template page")
        self.auto_actions.click_reference(self.device_template_web_elements.get_device_template_ap_template_wifi2_tab)
        sleep(5)

        CloudDriver().cloud_driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
        sleep(2)

        if radio_status_wifi2.upper() == "ENABLE":
            self.utils.print_info("Enable Radio Status on WiFi2 Interface")
            if not self.device_template_web_elements.get_wifi2_radio_status_button().is_selected():
                self.auto_actions.click_reference(self.device_template_web_elements.get_wifi2_radio_status_button)
                sleep(5)

                self.screen.save_screen_shot()
                sleep(2)

        else:
            self.utils.print_info("Disable Radio Status on WiFi2 Interface")
            if self.device_template_web_elements.get_wifi2_radio_status_button().is_selected():
                self.auto_actions.click_reference(self.device_template_web_elements.get_wifi2_radio_status_button)
                sleep(5)

                self.screen.save_screen_shot()
                sleep(2)
        if client_access_status_wifi2.upper() == "ENABLE":
            self.utils.print_info("Enable Client Access Checkbox on WiFi2 Interface")
            if not self.device_template_web_elements.get_client_access_checkbox_wifi2().is_selected():
                self.auto_actions.click_reference(self.device_template_web_elements.get_client_access_checkbox_wifi2)
                sleep(5)
        else:
            self.utils.print_info("Disable Client Access check box on WiFi2 Interface")
            if self.device_template_web_elements.get_client_access_checkbox_wifi2().is_selected():
                self.auto_actions.click_reference(self.device_template_web_elements.get_client_access_checkbox_wifi2)
                sleep(5)
        if backhaul_mesh_status_wifi2.upper() == "ENABLE":
            self.utils.print_info("Enable Backhaul Mesh Link Checkbox on WiFi2 Interface")
            if not self.device_template_web_elements.get_backhaul_mesh_link_checkbox_wifi2().is_selected():
                self.auto_actions.click_reference(self.device_template_web_elements.get_backhaul_mesh_link_checkbox_wifi2)
                sleep(5)
        else:
            self.utils.print_info("Disable Backhaul Mesh Link Checkbox on WiFi2 Interface")
            if self.device_template_web_elements.get_backhaul_mesh_link_checkbox_wifi2().is_selected():
                self.auto_actions.click_reference(self.device_template_web_elements.get_backhaul_mesh_link_checkbox_wifi2)
                sleep(5)

        if sensor_status_wifi2.upper() == "ENABLE":
            self.utils.print_info("Enable Sensor Checkbox on WiFi2 Interface")
            if not self.device_template_web_elements.get_sensor_checkbox_wifi2().is_selected():
                self.auto_actions.click_reference(self.device_template_web_elements.get_sensor_checkbox_wifi2)
                sleep(5)
        else:
            self.utils.print_info("Disable Sensor Checkbox on WiFi2 Interface")
            if self.device_template_web_elements.get_sensor_checkbox_wifi2().is_selected():
                self.auto_actions.click_reference(self.device_template_web_elements.get_sensor_checkbox_wifi2)
                sleep(5)

        """
        ##### APC-44337 UI Changes #####
        adsp_primary_server_ip = wifi2_profile.get('primary_server_ip', '1.1.1.1')
        adsp_primary_server_port = wifi2_profile.get('primary_server_port', '11')

        wifi2_primary_server_ip = self.device_template_web_elements.get_wifi2_primary_server_ip_textfield()
        wifi2_primary_server_port = self.device_template_web_elements.get_wifi2_primary_server_port_textfield()

        if wifi2_primary_server_ip:
            self.utils.print_info("Enter ADSP Primary Server IP Name")
            self.auto_actions.send_keys(self.device_template_web_elements.get_wifi2_primary_server_ip_textfield(),
                                        adsp_primary_server_ip)
            sleep(3)

        if wifi2_primary_server_port:
            self.utils.print_info("Enter ADSP Primary Server port")
            self.auto_actions.send_keys(self.device_template_web_elements.get_wifi2_primary_server_port_textfield(),
                                        adsp_primary_server_port)
            sleep(3)
        """
        self.screen.save_screen_shot()
        sleep(2)

        CloudDriver().cloud_driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_UP)

        return 1

    def _select_ap_template_from_np(self, ap_template):
        """
        - Select/Attach the AP template to the Network Policy
        - Keyword Usage
        - ``Select AP Template From NP  ${AP_TEMPLATE_NAME}``

        :param ap_template: Ap Template Name ie AP630,AP410C
        :return: 1 if AP Template Found on Grid else -1
        """
        self.utils.print_info("Click on Device Template Select button")
        self.auto_actions.click_reference(self.device_template_web_elements.get_ap_template_select_button)
        sleep(5)

        if self.device_template_web_elements.get_select_ap_templates_view_all_pages():
            self.utils.print_info("Click Full pages button")
            self.auto_actions.click_reference(self.device_template_web_elements.get_select_ap_templates_view_all_pages)
            sleep(5)

        self.auto_actions.scroll_up()
        sleep(2)
        self.utils.print_info(f'Selecting Device Template with name {ap_template}')
        ap_template_names = self.device_template_web_elements.get_select_ap_template_from_list()
        sleep(2)
        flag = 0

        for ap_template_name in ap_template_names:
            if ap_template.upper() in ap_template_name.text.upper():
                self.auto_actions.click(
                    self.device_template_web_elements.get_click_selected_ap_template(ap_template_name))
                self.utils.print_info(f'Selected Device Template with name {ap_template}')
                flag = 1
                break
        if flag == 0:
            self.utils.print_info(f"Device Template with name {ap_template} not found")
            return -1

        self.auto_actions.click_reference(self.device_template_web_elements.get_ap_template_dialog_select_button)
        return 1

    def _click_select_rule_button_to_ap_template(self, ap_template):
        """
        - Clicks the Select Rule button which appears for second AP Template of same AP model
        - Keyword Usage
        - ``Click Select Rule to AP Template  ${AP_TEMPLATE}``

        :param ap_template: Ap Template Name ie AP630,AP410C
        :return: True if Select Rule Button Found on Grid else False
        """
        ap_template_rows_elements = self.device_template_web_elements.get_ap_template_rows()
        for el in ap_template_rows_elements:
            if ap_template.upper() in el.text.upper():
                self.utils.print_info("CLicking Classification Rule Select Button")
                self.auto_actions.click(self.device_template_web_elements.get_ap_template_select_rule_button(el))
                return True
        return False

    def _select_rule_to_ap_template(self, rule):
        """
        - Select Rule button for second AP Template of same AP model
        - Keyword Usage
        - ``Select Rule to AP Template  ${AP_TEMPLATE}``

        :param rule: Rule is the classification Rule
        :return: True if Rule Found else False
        """
        if self.device_template_web_elements.get_select_ap_templates_rules_view_all_pages():
            self.utils.print_info("Click Full pages button")
            self.auto_actions.click_reference(self.device_template_web_elements.get_select_ap_templates_rules_view_all_pages)

        rules = self.device_template_web_elements.get_ap_template_rule_list()
        for el in rules:
            if rule.upper() in el.text.upper():
                self.utils.print_info(f"Selecting Classification Rule {rule}")
                self.auto_actions.click(el)
                return True
        return False

    def add_ap_template_to_network_policy(self, ap_template_name, policy_name, **kwargs):
        """"
        - Selecting Network Policy to attach existing AP Template to the same
        - Checking the AP template presence in the AP Templates Grid
        - If not there, then select AP Template from the list
        - Keyword Usage
        - ``Add AP Template To Network Policy   ${AP_TEMPLATE_NAME}       ${NETWORK_POLICY_NAME}``

        :param ap_template_name: AP Template Name ie AP630,AP410C etc
        :param policy_name: Name of the Network policy to attach the template
        :return: 1 if AP Template Configured Successfully else -1
        """

        self.utils.print_info("Click on Network Policy card view button")
        self.navigator.navigate_to_network_policies_card_view_page()

        if self.network_policy.select_network_policy_in_card_view(policy_name) != 1:
            kwargs['fail_msg'] = f"Network Policy {policy_name} doesn't exist"
            self.common_validation.failed(**kwargs)
            return -1

        if self.check_ap_template(ap_template_name, ignore_failure=True):
            kwargs['pass_msg'] = "Template Already present in the template grid"
            self.common_validation.passed(**kwargs)
            return 1
        return self._select_ap_template_from_np(ap_template_name)

    def add_ap_template_model_type(self, ap_template_name, ap_model_type, wifi_interface_config, **kwargs):
        """
        - Checking the AP template present in the AP Templates Grid
        - If it is not there add New AP Template
        - Keyword Usage
        - ``Add AP Template  ${AP_TEMPLATE_NAME}   &{AP_TEMPLATE_CONFIG}``

        :param ap_template_name: AP Template Name ie AP630,AP410C
        :param ap_model_type: AP Model Type
        :param wifi_interface_config: (Config Dict) Enable/Disable Client Access,Backhaul Mesh Link,Sensor
        :return: 1 if AP Template Configured Successfully else -1
        """
        # Commented on 1/18/23 because it is unused
        # wifi0_config = wifi_interface_config['wifi0_configuration']
        # wifi1_config = wifi_interface_config['wifi1_configuration']
        # wifi2_config = wifi_interface_config.get('wifi2_configuration', 'None')

        sleep(5)

        if self.check_ap_template(ap_template_name, ignore_failure=True):
            kwargs['pass_msg'] = "Template Already present in the template grid"
            self.common_validation.passed(**kwargs)
            return 1

        return self._select_ap_template_from_np(ap_template_name)

    def add_classification_rule_to_ap_template(self, ap_template_name, classification_rule, **kwargs):
        """"

        - Checking the AP template presence in the AP Templates Grid
        - Select Classification Rule button will only appear in case of second AP Template for same model
        - Selecting the Classification Rule from the list
        - Keyword Usage
        - ``Add Classification Rule to AP Template    ${AP_TEMPLATE_NAME}   ${CLASSIFICATION_RULE}``

        :param ap_template_name: AP Template Name ie AP630-Template,AP410C-Template
        :param classification_rule: Classification Rule to be added to AP Template
        :return: 1 if Classification Rule added to AP Template Successfully else -1, -2, -3 depending on the scenario
        """

        if not self.check_ap_template(ap_template_name):
            kwargs['fail_msg'] = "Template does not exist in the template grid"
            self.common_validation.failed(**kwargs)
            return -1

        if not self._click_select_rule_button_to_ap_template(ap_template_name):
            kwargs['fail_msg'] = "This AP Template is the First Template for this AP Model. Create one more"
            self.common_validation.failed(**kwargs)
            return -1

        if self.device_template_web_elements.get_select_rule_in_templates_view_all_pages():
            self.utils.print_info("Click Full pages button")
            self.auto_actions.click_reference(self.device_template_web_elements.get_select_rule_in_templates_view_all_pages)

        if not self._select_rule_to_ap_template(classification_rule):
            kwargs['fail_msg'] = f"Rule {classification_rule} is not available in the list"
            self.common_validation.failed(**kwargs)
            return -1

        self.auto_actions.click_reference(self.device_template_web_elements.get_ap_template_rule_link_button)
        kwargs['pass_msg'] = "Classification Rule added to AP Template Successfully"
        self.common_validation.passed(**kwargs)
        return 1

    def remove_ap_template_from_network_policy(self, ap_template_name, policy_name, **kwargs):
        """"
        - Selecting Network Policy to remove/detach AP Template
        - Checking the AP template presence in the AP Templates Grid
        - If it is not there return -1 else delete the template
        - Keyword Usage
        - ``Remove AP Template From Network Policy   ${AP_TEMPLATE_NAME}       ${NETWORK_POLICY_NAME}``

        :param ap_template_name: AP Template Name ie AP630,AP410C
        :param policy_name: Name of the Network policy to remove the template
        :return: 1 if AP Template Removed Successfully else -1
        """

        self.utils.print_info("Click on Network Policy card view button")
        self.navigator.navigate_to_network_policies_card_view_page()

        if self.network_policy.select_network_policy_in_card_view(policy_name) != 1:
            kwargs['fail_msg'] = f"Network Policy {policy_name} does not exist"
            self.common_validation.failed(**kwargs)
            return -1

        if not self.check_ap_template(ap_template_name):
            kwargs['fail_msg'] = "Template does not exist in the template grid"
            self.common_validation.failed(**kwargs)
            return -1

        ap_template_rows_elements = self.device_template_web_elements.get_ap_template_rows()
        for el in ap_template_rows_elements:
            if ap_template_name.upper() in el.text.upper():
                self.utils.print_info(f"Selecting checkbox for AP Template {ap_template_name}")
                self.auto_actions.click(self.device_template_web_elements.get_device_template_grid_checkbox(el))
                break

        self.utils.print_info(f"CLicking Delete Button for AP Template {ap_template_name}")
        self.auto_actions.click_reference(self.device_template_web_elements.get_remove_ap_template_from_policy_button)

        sleep(5)
        self.screen.save_screen_shot()
        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)

        if "Template was deleted successfully." in tool_tp_text[-1] or "Template was successfully removed from policy."\
                in tool_tp_text[-1]:
            kwargs['pass_msg'] = "Template was deleted successfully."
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Template was not deleted successfully."
            self.common_validation.failed(**kwargs)
            return -1

    def enable_supplemental_cli_in_ap_template(self, policy_name, ap_model, ap_template_name, suppl_cli_name, suppl_cli_cmds, **kwargs):
        """
        - This Keyword creates Supplemental CLI inside the AP Template
        - Flow: Network Policies --> Device Template --> AP Template --> Advanced Settings --> Supplemental CLI
        - Keyword Usage:
        - ``Enable Supplemental CLI in AP Template   ${POLICY_NAME}    ${AP_MODEL}    ${AP_TEMPLATE_NAME}   ${SUPPL_CLI_NAME}     ${SUPPL_CLI_CMDS}``

        :param policy_name: Name of the Network policy
        :param ap_model: AP Model
        :param ap_template_name: Name of the AP Template
        :param suppl_cli_name: Name of the Supplemental CLI name
        :param suppl_cli_cmds: Supplemental CLI commands
        :return: 1 if AP Template is saved successfully else -1
        """

        self.utils.print_info("Selecting Configure tab...")
        self.navigator.navigate_to_configure_tab()
        sleep(5)

        self.utils.print_info("Navigating to network policies...")
        self.navigator.navigate_to_network_policies_tab()
        sleep(2)

        self.utils.print_info("Click on network policy add button")
        self.auto_actions.click_reference(self.device_template_web_elements.get_network_policy_add_button)
        sleep(2)

        self.utils.print_info("Enter the policy name")
        self.auto_actions.send_keys(self.device_template_web_elements.get_network_policy_name_text(), policy_name)
        sleep(3)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Click on network policy save button")
        self.auto_actions.click_reference(self.device_template_web_elements.get_network_policy_save_button)
        sleep(3)

        self.utils.print_info("Click on Device Template tab")
        self.auto_actions.click_reference(self.device_template_web_elements.get_select_device_template)
        sleep(5)

        self.utils.print_info("Click on AP Template add button")
        self.auto_actions.click_reference(self.device_template_web_elements.get_ap_template_add_button)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("select the AP: ", ap_model)
        ap_list_items = self.device_template_web_elements.get_ap_template_platform_from_drop_down()
        for el in ap_list_items:
            if not el:
                pass
            if ap_model.upper() in el.text.upper():
                self.auto_actions.click(el)
                break
            print(el.text)
        sleep(3)

        self.utils.print_info("Enter the AP Template Name")
        self.auto_actions.send_keys(self.device_template_web_elements.get_ap_template_text(), ap_template_name)
        sleep(3)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Clicking Advanced Settings ... ")
        self.auto_actions.click_reference(self.device_template_web_elements.get_ap_template_advanced_settings)
        sleep(2)

        self.utils.print_info("Click to enable Supplemental CLI ... ")
        self.auto_actions.click_reference(self.device_template_web_elements.get_ap_template_enable_scli)
        sleep(2)

        self.utils.print_info("Entering Supplemental Cli Name")
        self.auto_actions.send_keys(self.device_template_web_elements.get_ap_template_scli_config_enter_name(),
                                    suppl_cli_name)
        sleep(2)

        self.auto_actions.scroll_down()
        sleep(3)
        self.utils.print_info("Entering Supplemental Cli Commands")
        self.auto_actions.send_keys(self.device_template_web_elements.get_ap_template_scli_enter_commands(),
                                    suppl_cli_cmds)
        sleep(2)

        self.utils.print_info("Saving template ... ")
        self.auto_actions.click_reference(self.device_template_web_elements.get_ap_template_save_template)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)

        if "AP template was saved successfully." in tool_tp_text[-1]:
            kwargs['pass_msg'] = "AP template was saved successfully."
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Unable to save the template"
            self.common_validation.failed(**kwargs)
            return -1

    def enable_supplemental_cli_in_switch_template(self, policy_name, switch_model, switch_template_name,
                                                   suppl_cli_name, suppl_cli_cmds, **kwargs):
        """
        - This Keyword creates Supplemental CLI inside the Switch Template
        - Flow: Network Policies --> Device Template --> Switch Template --> Advanced Settings --> Supplemental CLI
        - Keyword Usage:
        - ``Enable Supplemental CLI in Switch Template   ${POLICY_NAME}    ${SWITCH_MODEL}    ${SWITCH_TEMPLATE_NAME}   ${SUPPL_CLI_NAME}     ${SUPPL_CLI_CMDS}``

        :param policy_name: Name of the Network policy
        :param switch_model: Switch Model
        :param switch_template_name: Name of the Switch Template
        :param suppl_cli_name: Name of the Supplemental CLI name
        :param suppl_cli_cmds: Supplemental CLI commands
        :return: 1 if AP Template is saved successfully else -1
        """

        self.utils.print_info("Selecting Configure tab...")
        self.navigator.navigate_to_configure_tab()
        sleep(5)

        self.utils.print_info("Navigating to network policies...")
        self.navigator.navigate_to_network_policies_tab()
        sleep(2)

        self.utils.print_info("Click on network policy add button")
        self.auto_actions.click_reference(self.device_template_web_elements.get_network_policy_add_button)
        sleep(2)

        self.utils.print_info("Enter the policy name")
        self.auto_actions.send_keys(self.device_template_web_elements.get_network_policy_name_text(), policy_name)
        sleep(3)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Click on network policy save button")
        self.auto_actions.click_reference(self.device_template_web_elements.get_network_policy_save_button)
        sleep(3)

        self.utils.print_info("Click on Device Template tab")
        self.auto_actions.click_reference(self.device_template_web_elements.get_select_device_template)
        sleep(5)

        self.utils.print_info("Click on Switch Template tab")
        self.auto_actions.click_reference(self.device_template_web_elements.get_select_switch_template)
        sleep(5)

        self.utils.print_info("Click on Switch Template add button")
        self.auto_actions.click_reference(self.device_template_web_elements.get_switch_template_add_button)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("select the Switch: ", switch_model)
        switch_list_items = self.device_template_web_elements.get_switch_template_platform_from_drop_down()
        for el in switch_list_items:
            if not el:
                pass
            if switch_model.upper() in el.text.upper():
                self.auto_actions.click(el)
                break
            print(el.text)
        sleep(3)

        self.utils.print_info("Enter the Switch Template Name")
        self.auto_actions.send_keys(self.device_template_web_elements.get_ap_template_text(), switch_template_name)
        sleep(3)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Clicking Advanced Settings ... ")
        self.auto_actions.click_reference(self.device_template_web_elements.get_switch_template_advanced_settings)
        sleep(2)

        self.utils.print_info("Click to enable Supplemental CLI ... ")
        self.auto_actions.click_reference(self.device_template_web_elements.get_ap_template_enable_scli)
        sleep(2)

        self.utils.print_info("Entering Supplemental Cli Name")
        self.auto_actions.send_keys(self.device_template_web_elements.get_ap_template_scli_config_enter_name(),
                                    suppl_cli_name)
        sleep(2)

        self.auto_actions.scroll_down()
        sleep(3)
        self.utils.print_info("Entering Supplemental Cli Commands")
        self.auto_actions.send_keys(self.device_template_web_elements.get_ap_template_scli_enter_commands(),
                                    suppl_cli_cmds)
        sleep(2)

        self.utils.print_info("Saving template ... ")
        self.auto_actions.click_reference(self.device_template_web_elements.get_switch_template_save_template)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)

        if "Switch template has been saved successfully." in tool_tp_text[-1]:
            kwargs['pass_msg'] = "Switch template has been saved successfully"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Unable to save the template"
            self.common_validation.failed(**kwargs)
            return -1

    def add_ap_template_with_country_code(self, policy_name, ap_model, ap_template_name, country_code, **kwargs):
        """
        - This Keyword is to create Country Code in AP Template
        - Flow: Network Policies --> Device Template --> AP Template --> Advanced Settings --> Country Code
        - Keyword Usage:
        - ``Choose Country Code in AP Template   ${POLICY_NAME}    ${AP_MODEL}    ${AP_TEMPLATE_NAME}   ${COUNTRY}``

        :param policy_name: Name of the Network policy
        :param ap_model: AP Model
        :param ap_template_name: Name of the AP Template
        :param country_code: Name of the country code
        :return: 1 if AP Template is saved successfully else -1
        """

        self.utils.print_info("Selecting Configure tab...")
        self.navigator.navigate_to_configure_tab()

        self.utils.print_info("Navigating to network policies...")
        self.navigator.navigate_to_network_policies_tab()

        self.utils.print_info("Click on network policy add button")
        self.auto_actions.click_reference(self.device_template_web_elements.get_network_policy_add_button)

        self.utils.print_info("Enter the policy name")
        self.auto_actions.send_keys(self.device_template_web_elements.get_network_policy_name_text(), policy_name)

        self.utils.print_info("Click on network policy save button")
        self.auto_actions.click_reference(self.device_template_web_elements.get_network_policy_save_button)

        self.screen.save_screen_shot()

        self.utils.print_info("Click on Device Template tab")
        self.auto_actions.click_reference(self.device_template_web_elements.get_select_device_template)

        self.utils.print_info("Click on AP Template add button")
        self.auto_actions.click_reference(self.device_template_web_elements.get_ap_template_add_button)

        self.screen.save_screen_shot()

        self.utils.print_info("select the AP: ", ap_model)
        ap_list_items = self.device_template_web_elements.get_ap_template_platform_from_drop_down()
        for el in ap_list_items:
            if not el:
                pass
            if ap_model.upper() in el.text.upper():
                self.auto_actions.click(el)
                break
            print(el.text)

        self.utils.print_info("Enter the AP Template Name")
        self.auto_actions.send_keys(self.device_template_web_elements.get_ap_template_text(), ap_template_name)

        self.screen.save_screen_shot()

        self.utils.print_info("Clicking Advanced Settings ... ")
        self.auto_actions.click_reference(self.device_template_web_elements.get_ap_template_advanced_settings)

        self.auto_actions.scroll_down()
        self.screen.save_screen_shot()

        self.utils.print_info("Clicking on Country Code dropdown")
        self.auto_actions.click_reference(self.device_template_web_elements.get_ap_template_country_code_drop_down)

        self.utils.print_info("Select the Country Code")
        countries = self.device_template_web_elements.get_ap_template_country_code_list()
        if countries:
            for country in countries:
                self.utils.print_debug("country: ", country.text)
                if country_code in country.text:
                    self.auto_actions.click(country)
                    self.utils.print_info("Selected country: ", country_code)
                    self.screen.save_screen_shot()
        else:
            self.utils.print_info(" Not able to find auto provision country dropdown items ")
            self.screen.save_screen_shot()

        self.utils.print_info("Saving template ... ")
        self.auto_actions.click_reference(self.device_template_web_elements.get_switch_template_save_template)

        self.screen.save_screen_shot()

        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)

        if "AP template was saved successfully." in tool_tp_text[-1]:
            kwargs['pass_msg'] = "AP template has been saved successfully"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Unable to save the template"
            self.common_validation.failed(**kwargs)
            return -1
