import re
from time import sleep

from extauto.common.Utils import Utils
from extauto.common.AutoActions import AutoActions
from extauto.common.Screen import Screen

import extauto.xiq.flows.common.ToolTipCapture as tool_tip
from extauto.xiq.flows.common.Navigator import Navigator
import extauto.xiq.flows.configure.NetworkPolicy
from extauto.xiq.flows.manage.Tools import Tools

from selenium.webdriver.common.keys import Keys
from extauto.xiq.elements.SwitchTemplateWebElements import SwitchTemplateWebElements
from extauto.xiq.elements.DeviceTemplateWebElements import DeviceTemplateWebElements
from extauto.xiq.elements.NetworkPolicyWebElements import NetworkPolicyWebElements
from extauto.xiq.elements.SwTemplateLegacyPortTypeWebElements import SwTemplateLegacyPortTypeWebElements
from ExtremeAutomation.Library.Device.NetworkElement.Constants.NetworkElementConstants import NetworkElementConstants

from extauto.xiq.elements.Device360WebElements import Device360WebElements
from extauto.xiq.elements.AlarmsWebElements import AlarmsWebElements
from extauto.common.CommonValidation import CommonValidation
from extauto.xiq.elements.DialogWebElements import DialogWebElements
from extauto.xiq.flows.configure.CommonObjects import CommonObjects


class SwitchTemplate(object):

    def __init__(self):
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.navigator = Navigator()
        self.device_template_web_elements = DeviceTemplateWebElements()
        self.sw_template_web_elements = SwitchTemplateWebElements()
        self.np_web_elements = NetworkPolicyWebElements()
        self.nw_policy = None
        self.legacy_port_type_editor = SwTemplateLegacyPortTypeWebElements()
        self.dev360 = Device360WebElements()
        self.alarm = AlarmsWebElements()
        self.screen = Screen()
        self.tools = Tools()
        self.common_validation = CommonValidation()
        self.dialogue_web_elements = DialogWebElements()
        self.common_objects = CommonObjects()

    def check_sw_template(self, sw_template):
        """
        - Check the Switch template in the Switch template Grid
        - Assumes That Already in Switch template Grid Page
        - Keyword Usage
        - ``Check SW Template  ${SWITCH_TEMPLATE_NAME}``
        :param sw_template: Switch Template Name ie SR2024P,X440-G2-24p-10G4 etc
        :return: True if Switch Template Found on Grid else False
        """
        sw_template_rows_elements = self.sw_template_web_elements.get_sw_template_rows()
        if not sw_template_rows_elements:
            return False
        for el in sw_template_rows_elements:
            if sw_template.upper() in el.text.upper():
                self.utils.print_info("Template Already present in the template grid")
                return True
        return False

    def add_sw_template(self, nw_policy, sw_model, sw_template_name, cli_type, **kwargs):
        """
        - Checks the given switch template present already in the switch Templates Grid
        - If it is not there add to the sw_template
        - Keyword Usage
        - ``Add SW Template  ${NW_POLICY}  ${SW_MODEL}   ${SW_TEMPLATE_NAME}  ${CLI_TYPE}``

        :param nw_policy: network policy
        :param sw_model: Switch Model ie SR2348P
        :param sw_template_name: Switch Template Name ie template_SR2348P
        :param cli_type: Device CLI Type e.g., VOSS,EXOS

        :return: 1 if Switch Template Configured Successfully else -1
        """
        self.navigator.navigate_to_switch_templates()

        def _wait_pagination():
            return self.common_objects.cobj_web_elements.get_page_size_element(page_size='100')

        self.utils.wait_till(_wait_pagination, timeout=30, delay=2, msg='Waiting pagination')
        self.utils.print_info("Click on full page view for switch template")
        page_size_el = self.common_objects.cobj_web_elements.get_page_size_element(page_size='100')
        if page_size_el:
            self.utils.print_info("  -- clicking page size element 100 for switch template")
            self.auto_actions.click(page_size_el)
            sleep(3)
        else:
            self.utils.print_info("  -- could not find page size element 100")
        if self.common_objects.search_switch_template(sw_template_name):
            kwargs['pass_msg'] = "Switch Template exists on first page!!"
            self.common_validation.passed(**kwargs)
            return 1

        elif not self.common_objects.search_switch_template(sw_template_name):
            self.utils.print_info("Switch Template doesn't exist on first page")
            next_page_el = self.common_objects.cobj_web_elements.get_next_page_element()
            if next_page_el:
                device_page_numbers = self.common_objects.cobj_web_elements.get_page_numbers()
                page_len = int(max(device_page_numbers.text))
                while page_len:
                    self.utils.print_info("  -- clicking next page")
                    self.auto_actions.click(next_page_el)
                    sleep(2)
                    page_len = page_len - 1
                    if self.common_objects.search_switch_template(sw_template_name):
                        kwargs['pass_msg'] = "Switch Template exists in the list!!"
                        self.common_validation.passed(**kwargs)
                        return 1

        self.utils.print_info("Navigating Network Policies")
        self.navigator.navigate_configure_network_policies()
        self.select_network_policy_in_card_view_using_network_web_elements(nw_policy)

        if NetworkElementConstants.OS_EXOS in cli_type.upper() or NetworkElementConstants.OS_VOSS in cli_type.upper():
            self.utils.print_info("Click on Switching tab")
            self.auto_actions.click_reference(self.device_template_web_elements.get_policy_switching_tab)

            self.utils.print_info("Click on Switch Templates Menu Item")
            self.auto_actions.click_reference(self.device_template_web_elements.get_policy_switch_templates_tab)

        elif NetworkElementConstants.OS_AHFASTPATH in cli_type.upper():
            self.utils.print_info("Click on SR/Dell Switching tab")
            self.auto_actions.click_reference(self.device_template_web_elements.get_policy_sr_dell_switching_tab)

            self.utils.print_info("Click on Switch Templates Menu Item from SR/Dell Switching Section")
            self.auto_actions.click_reference(self.device_template_web_elements.get_policy_sr_dell_switch_templates_tab)

        add_btns = self.sw_template_web_elements.get_sw_template_add_button()
        sleep(2)

        self.utils.print_info("add_btn: ", add_btns)
        for add_btn in add_btns:
            if add_btn.is_displayed():
                self.utils.print_info("Click on sw Template Add button")
                self.auto_actions.click(add_btn)
                sleep(2)

                self.utils.print_info("Looking for: ", sw_model)
                sw_list_items = self.sw_template_web_elements.get_sw_template_platform_from_drop_down()
                sleep(2)
                model_found = False
                for el in sw_list_items:
                    if not el:
                        continue
                    if el.text == "":
                        continue
                    if sw_model.upper() in el.text.upper():
                        self.utils.print_info("    -switch template match")
                        model_found = True
                        self.auto_actions.click(el)
                        break
                if not model_found:
                    kwargs['fail_msg'] = "Device model NOT found!"
                    self.common_validation.failed(**kwargs)
                    return -1

                sleep(1)

                self.utils.print_info("Get Template Field and enter the switch Template Name: ", sw_template_name)
                self.auto_actions.send_keys(self.sw_template_web_elements.get_sw_template_name_textfield(),
                                            sw_template_name)
                sleep(1)
                self.utils.print_info("Get Template Save Button")
                save_btns = self.sw_template_web_elements.get_sw_template_save_button()

                rc = -1
                for save_btn in save_btns:
                    if save_btn.is_displayed():
                        self.utils.print_info("Click on the save template button")
                        self.auto_actions.click(save_btn)
                        self.screen.save_screen_shot()
                        tool_tip_text = tool_tip.tool_tip_text
                        self.utils.print_info("Tool tip Text Displayed on Page", tool_tip_text)

                        def _is_sw_template_available():
                            return self.get_sw_template_row(sw_template_name)
                        self.utils.wait_till(_is_sw_template_available, delay=3, is_logging_enabled=True, silent_failure=False)

                        self.screen.save_screen_shot()
                        rc = 1
                        break

                self.utils.print_info("Click on network policy exit button")
                self.auto_actions.click_reference(self.np_web_elements.get_np_exit_button)
                sleep(2)

                return rc

    def get_sw_template_row(self, sw_template, **kwargs):
        """
        - Get the switch template row element on Network Policy's Switch Templates Grid
        - Keyword Usage
        - ``Get SW Template Row  ${SW_TEMPLATE_NAME}``

        :param sw_template: name of the sw_template
        :return: Switch Template Cell present on row
        """
        self.utils.print_info("Getting the switch template rows.")

        rows, _ = self.utils.wait_till(
            func=self.sw_template_web_elements.get_sw_template_rows,
            exp_func_resp=True,
            silent_failure=True, 
            delay=5
        )
        
        if not rows:
            kwargs['fail_msg'] = "There are no device templates defined in switch template page"
            self.common_validation.failed(**kwargs)
            return False
   
        for row in rows:
            cells = self.sw_template_web_elements.get_sw_template_row_cell(row, 'dgrid-row')
            for cell in cells:
                if sw_template in cell.text:
                    kwargs['pass_msg'] = f"Found {sw_template} in switch template rows."
                    self.common_validation.passed(**kwargs)
                    return cell

    def select_sw_template(self, nw_policy, sw_template, cli_type, **kwargs):
        """
        - This Keyword will Select the Switch Template on Network Policy
        - Keyword Usage
        - ``Select SW Template  ${NW_POLICY_NAME}  ${SW_TEMPLATE_NAME}  ${CLI_TYPE}``

        :param nw_policy: Name of the Network Policy to select Switch Template
        :param sw_template: Name of the sw_template
        :param cli_type: Device CLI Type e.g., VOSS,EXOS
        :return: 1 If successfully Selected Switch template
        """
        self._set_nw_policy_if_needed()

        self.nw_policy.navigate_to_np_edit_tab(nw_policy)
        sleep(5)

        if NetworkElementConstants.OS_EXOS in cli_type.upper() or NetworkElementConstants.OS_VOSS in cli_type.upper():
            self.utils.print_info("Click on Switching tab")
            self.auto_actions.click_reference(self.device_template_web_elements.get_policy_switching_tab)

            self.utils.print_info("Click on Switch Templates Menu Item")
            self.auto_actions.click_reference(self.device_template_web_elements.get_policy_switch_templates_tab)

        elif NetworkElementConstants.OS_AHFASTPATH in cli_type.upper():
            self.utils.print_info("Click on SR/Dell Switching tab")
            self.auto_actions.click_reference(self.device_template_web_elements.get_policy_sr_dell_switching_tab)

            self.utils.print_info("Click on Switch Templates Menu Item from SR/Dell Switching Section")
            self.auto_actions.click_reference(self.device_template_web_elements.get_policy_sr_dell_switch_templates_tab)

        row = self.get_sw_template_row(sw_template)
        self.utils.print_info("Clicking on Switch Template.")
        self.auto_actions.click(row)
        self.navigator.wait_until_loading_is_done()
        kwargs['pass_msg'] = f"Successfully selecting the switch template {sw_template}."
        self.common_validation.passed(**kwargs)
        return 1

    def assign_switch_template(self, nw_policy, sw_template_name, cli_type, **kwargs):
        """
        - Checking the sw template present in the sw Templates Grid
        - If it is not there add to the sw_template
        - Keyword Usage
        - ``Assign SW Template  ${POLICY_NAME}  ${SW_TEMPLATE_NAME}``

        :param nw_policy: Name of policy to assign the switch template to
        :param sw_template_name: Name of the switch template to assign; e.g., SR_2348P-default-template
        :param cli_type: Device CLI Type e.g., VOSS,EXOS

        :return: 1 if switch template was assigned successfully, else -1
        """
        self.utils.print_info("Navigating to Network Policies")
        self.navigator.navigate_configure_network_policies()
        sleep(1)

        self._set_nw_policy_if_needed()

        self.nw_policy.select_network_policy_in_card_view(nw_policy)
        sleep(2)

        if NetworkElementConstants.OS_EXOS in cli_type.upper() or NetworkElementConstants.OS_VOSS in cli_type.upper():
            self.utils.print_info("Click on Switching tab")
            self.auto_actions.click_reference(self.device_template_web_elements.get_policy_switching_tab)

            self.utils.print_info("Click on Switch Templates Menu Item")
            self.auto_actions.click_reference(self.device_template_web_elements.get_policy_switch_templates_tab)

        elif NetworkElementConstants.OS_AHFASTPATH in cli_type.upper():
            self.utils.print_info("Click on SR/Dell Switching tab")
            self.auto_actions.click_reference(self.device_template_web_elements.get_policy_sr_dell_switching_tab)

            self.utils.print_info("Click on Switch Templates Menu Item from SR/Dell Switching Section")
            self.auto_actions.click_reference(self.device_template_web_elements.get_policy_sr_dell_switch_templates_tab)

        if self.check_sw_template(sw_template_name, ignore_failure=True):
            kwargs['pass_msg'] = "Template Already present in the template grid"
            self.common_validation.passed(**kwargs)
            return 1

        sel_btn = self.sw_template_web_elements.get_sw_template_select_button()
        sleep(2)

        if sel_btn:
            self.utils.print_info("Click on Switch Template Select button")
            self.auto_actions.click(sel_btn)
            sleep(2)

            # Search for the item to be selected
            self.utils.print_info("Search for the switch template name: ", sw_template_name)
            self.auto_actions.send_keys(self.sw_template_web_elements.get_sw_template_selection_search_textfield(), sw_template_name)
            self.auto_actions.click_reference(self.sw_template_web_elements.get_sw_template_selection_search_button)
            sleep(3)

            # Select the item
            sel_grid = self.sw_template_web_elements.get_sw_template_selection_grid()
            if sel_grid:
                sel_grid_rows = self.sw_template_web_elements.get_sw_template_selection_grid_rows(sel_grid)
                found_row = False
                for row in sel_grid_rows:
                    if row and sw_template_name in row.text:
                        self.utils.print_info("Found the matching row: ", row.text)
                        found_row = True
                        break

                if found_row:
                    # Click the checkbox to select the matching row
                    self.utils.print_info("Select the switch template name: ", sw_template_name)
                    self.auto_actions.click(self.sw_template_web_elements.get_sw_template_selection_row_checkbox(row))
                    sleep(2)

                    # Click Select
                    self.utils.print_info("Click Select")
                    self.auto_actions.click_reference(self.sw_template_web_elements.get_sw_template_selection_select_button)
                    sleep(2)

                    kwargs['pass_msg'] = "Switch template successfully selected for policy"
                    self.common_validation.passed(**kwargs)
                    return 1
                else:
                    self.utils.print_info("Could not select Switch Template row for ", sw_template_name)
                    self.utils.print_info("  -- Clicking Cancel to close Select Switch Template dialog")
                    self.auto_actions.click_reference(self.sw_template_web_elements.get_sw_template_selection_cancel_button)
                    kwargs['fail_msg'] = "Could not select Switch Template"
                    self.common_validation.failed(**kwargs)
                    return -1
            else:
                kwargs['fail_msg'] = "Could not find Switch Template selection table"
                self.common_validation.fault(**kwargs)
                return -1
        else:
            kwargs['fail_msg'] = "Could not click Switch Template Select button"
            self.common_validation.fault(**kwargs)
            return -1

    def go_to_port_configuration(self, **kwargs):
        nav_button = self.sw_template_web_elements.get_sw_template_port_configuration_tab()
        if nav_button:
            self.auto_actions.click(nav_button)
            kwargs['pass_msg'] = "Navigate to port configuration"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Failed to navigate to port configuration"
            self.common_validation.failed(**kwargs)
            return -1

    def switch_template_save(self):
        save_btns = self.sw_template_web_elements.get_sw_template_save_button()
        for save_btn in save_btns:
            if save_btn.is_displayed():
                self.auto_actions.click(save_btn)
        sleep(5)

    def select_wireframe_net_ports(self, ports):
        port_list = self.utils.expand_port_range(ports)
        port_el_list = self.sw_template_web_elements.get_sw_template_wireframe_net_ports(port_list)
        for port in port_el_list:
            self.auto_actions.click(port)
        sleep(2)

    def select_assign_choose_existing_port_type(self, port_type_name):
        rc = 0
        self.auto_actions.click_reference(self.sw_template_web_elements.get_sw_template_assign_button)
        sleep(3)
        self.auto_actions.click_reference(self.sw_template_web_elements.get_sw_template_assign_choose_existing)
        sleep(3)
        radios = self.sw_template_web_elements.get_sw_template_all_port_type_list_radio()
        labels = self.sw_template_web_elements.get_sw_template_all_port_type_list_label()
        for i in range(len(labels)):
            if labels[i].text == port_type_name:
                self.auto_actions.select_radio_button(radios[i])
                rc = 1
                break
        sleep(3)
        if rc == 1:
            self.auto_actions.click_reference(self.sw_template_web_elements.get_sw_template_port_type_list_save_button)
        else:
            self.auto_actions.click_reference(self.sw_template_web_elements.get_sw_template_port_type_list_cancel_button)
        sleep(3)

    def select_assign_create_new_port_type(self, port_type):
        self.auto_actions.click_reference(self.sw_template_web_elements.get_sw_template_assign_button)
        sleep(3)
        self.auto_actions.click_reference(self.sw_template_web_elements.get_sw_template_assign_create_new)
        sleep(3)
        if (port_type.get('port_type_editor') == 'Legacy'):
            self.set_legacy_port_type_fields(port_type)
            save_btns = self.legacy_port_type_editor.get_save_button()
            for save_btn in save_btns:
                if save_btn.is_displayed():
                    self.auto_actions.click(save_btn)
                    break
            sleep(5)

    def edit_port_type(self, port_list, port_type):
        edit_els = self.sw_template_web_elements.get_sw_template_all_edit_port_type()
        _port_list = self.utils.expand_port_range(port_list)
        self.auto_actions.click(edit_els[_port_list[0]])
        if (port_type.get('port_type_editor') == 'Legacy'):
            self.set_legacy_port_type_fields(port_type)
            save_btns = self.legacy_port_type_editor.get_save_button()
            for save_btn in save_btns:
                if save_btn.is_displayed():
                    self.auto_actions.click(save_btn)
                    break
            sleep(5)

    def set_legacy_port_type_fields(self, port_type):
        self.utils.print_info(port_type)
        for key, value in port_type.items():
            if (key == 'name'):
                e = self.legacy_port_type_editor.get_name()
                self.auto_actions.send_keys(self.legacy_port_type_editor.get_name(), value)
            elif (key == 'description'):
                el = self.legacy_port_type_editor.get_port_type_desc()
                if (isinstance(el,list)):
                    for e in el:
                        if e.is_displayed():
                            self.auto_actions.send_keys(e, value)
                else:
                    self.auto_actions.send_keys(el, value)
            elif (key == 'status'):
                el = self.legacy_port_type_editor.get_status()
                if (value == 'Disable'):
                    self.auto_actions.disable_check_box(el[0])
                elif (value == 'Enable'):
                    self.auto_actions.enable_check_box(el[0])
            sleep(3)

    def verify_sw_template_port_type(self, port_list, port_type, default_port_type):
        result = rc = 1
        for key, value in port_type.items():
            default_value = default_port_type.get(key) if isinstance(default_port_type, dict) else None
            if (key == 'name'):
                rc = self.verify_sw_template_port_usage(port_list, value, default_value)
            elif (key == 'description'):
                rc = self.verify_sw_template_port_desc(port_list, value, default_value)
            elif (key == 'status'):
                rc = self.verify_sw_template_port_status(port_list, value, default_value)
            result = result if result == 0 else rc
        return result

    def verify_sw_template_port_usage(self, port_list, port_type_name, default):
        port_usage_list = self.sw_template_web_elements.get_sw_template_all_port_usage()
        _port_list = self.utils.expand_port_range(port_list)
        for i in range(len(port_usage_list)):
            v = port_usage_list[i].get_attribute('innerText')
            if i+1 in _port_list:
                if v != port_type_name:
                    self.utils.print_info("Port ", i+1, " port type is ", v, " should be ", port_type_name)
                    return 0
            elif default is not None:
                if v != default:
                    self.utils.print_info("Port ", i+1, " port type is ", v, " should be ", default)
                    return 0
        return 1

    def verify_sw_template_port_desc(self, port_list, description, default):
        element_list = self.sw_template_web_elements.get_sw_template_all_port_desc()
        _port_list = self.utils.expand_port_range(port_list)
        for i in range(len(element_list)):
            v = element_list[i].get_attribute('value')
            if i+1 in _port_list:
                if v != description:
                    self.utils.print_info("ERROR: Port ", i+1, " description is ", v, " should be ", description)
                    return 0
            elif default is not None:
                if v != default:
                    self.utils.print_info("Port ", i+1, " port type is ", v, " should be ", default)
                    return 0
        return 1

    def verify_sw_template_port_status(self, port_list, status, default, **kwargs):
        element_list = self.sw_template_web_elements.get_sw_template_all_port_status()
        _port_list = self.utils.expand_port_range(port_list)
        for i in range(len(element_list)):
            e = element_list[i]
            if i+1 in _port_list:
                if status == 'Disabled' and e.is_selected():
                    kwargs['fail_msg'] = f"ERROR: Port {i+1} status is ON but should be OFF"
                    self.common_validation.failed(**kwargs)
                    return 0
                elif status == 'Enabled' and not e.is_selected():
                    kwargs['fail_msg'] = f"ERROR: Port {i+1} status is OFF but should be ON"
                    self.common_validation.failed(**kwargs)
                    return 0
            elif default is not None:
                if default == 'Disabled' and e.is_selected():
                    kwargs['fail_msg'] = f"ERROR: Port {i+1} status is ON but should be OFF"
                    self.common_validation.failed(**kwargs)
                    return 0
                elif default == 'Enabled' and not e.is_selected():
                    kwargs['fail_msg'] = f"ERROR: Port {i+1} status is OFF but should be ON"
                    self.common_validation.failed(**kwargs)
                    return 0
        kwargs['pass_msg'] = "Successfully verify sw template port status"
        self.common_validation.passed(**kwargs)
        return 1

    def add_5520_sw_stack_template(self, model_units, nw_policy, sw_model, sw_template_name, cli_type, save_template=True, **kwargs):
        """
        - Checks the given STACK switch template present already in the switch Templates Grid
        - If it is not there add to the sw_template
        - This function is working only for stack
        - Keyword Usage
        - ``  Add Sw Stack Template    ${MODEL_UNITS} ${NW_POLICY}  ${SW_MODEL}   ${SW_TEMPLATE_NAME}  ${CLI_TYPE}``
        - e.g. Add Sw Stack Template                           5520-24T-EXOS,5520-24X-EXOS,5520-48T-EXOS
           ...                             bgd2        EXOS-5520-Series-Stack          politicamea      True
        :param model_units: a string will all units e.g 5520-24T,5520-24X,5520-48T
        :param nw_policy: network policy
        :param sw_model: Switch Model  ie EXOS-5520-Series-Stack
        :param sw_template_name: Switch Template Name e.g mypolicy
        :param save_template: True - will save the template ; False - will not save the template (More configures can be added after)
        :param cli_type: Device CLI Type e.g., VOSS,EXOS

        :return: 1 if Switch Template Configured Successfully else -1
        """
        self.utils.print_info("Navigate to devices")
        self.navigator.navigate_to_devices()
        self.utils.print_info("Navigating Network Policies")
        self.navigator.navigate_configure_network_policies()
        sleep(1)

        if "Switch Engine" in model_units:
            var_type = "Switch Engine"
        else:
            var_type = "X440-G2-"

        self._set_nw_policy_if_needed()

        if self.nw_policy.select_network_policy_in_card_view(nw_policy) == -1:
            kwargs['fail_msg'] = "Not found the network policy. Make sure that it was created before"
            self.common_validation.failed(**kwargs)
            return -1

        if NetworkElementConstants.OS_EXOS in cli_type.upper() or NetworkElementConstants.OS_VOSS in cli_type.upper():
            self.utils.print_info("Click on Switching tab")
            self.auto_actions.click_reference(self.device_template_web_elements.get_policy_switching_tab)

            self.utils.print_info("Click on Switch Templates Menu Item")
            self.auto_actions.click_reference(self.device_template_web_elements.get_policy_switch_templates_tab)

        elif NetworkElementConstants.OS_AHFASTPATH in cli_type.upper():
            self.utils.print_info("Click on SR/Dell Switching tab")
            self.auto_actions.click_reference(self.device_template_web_elements.get_policy_sr_dell_switching_tab)

            self.utils.print_info("Click on Switch Templates Menu Item from SR/Dell Switching Section")
            self.auto_actions.click_reference(self.device_template_web_elements.get_policy_sr_dell_switch_templates_tab)

        if self.check_sw_template(sw_template_name):
            kwargs['fail_msg'] = f"Template with name {sw_template_name} already present in the template grid"
            self.common_validation.failed(**kwargs)
            return -1

        add_btns = self.sw_template_web_elements.get_sw_template_add_button()
        sleep(2)

        self.utils.print_info("add_btn: ", add_btns)
        for add_btn in add_btns:
            if add_btn.is_displayed():
                self.utils.print_info("Click on sw Template Add button")
                self.auto_actions.click(add_btn)
                sleep(1)

                self.utils.print_info("select the sw: ", sw_model)
                sw_list_items = self.sw_template_web_elements.get_sw_template_platform_from_drop_down()
                sleep(2)
                for el in sw_list_items:
                    self.utils.print_debug("Switch template names: ", el.text.upper())
                    if not el:
                        pass
                    if sw_model.upper() in el.text.upper():
                        self.auto_actions.click(el)
                        break
                    print(el.text)
                sleep(3)

                self.utils.print_info("Enter the switch Template Name: ", sw_template_name)
                self.auto_actions.send_keys(self.sw_template_web_elements.get_sw_template_name_textfield(),
                                            sw_template_name)
                sleep(3)

                add_stack_button = self.sw_template_web_elements.get_sw_template_stack_add_button()
                if add_stack_button:
                    self.utils.print_info("Press ADD button")
                    self.auto_actions.click(add_stack_button)
                    sleep(1)
                else:
                    kwargs['fail_msg'] = "ADD button was not found"
                    self.common_validation.fault(**kwargs)
                    return -1
                policy_unit_items = self.dev360.get_sw_template_stack_add_items()
                item_count = len(policy_unit_items)
                self.utils.print_info(f"Found {item_count} options into dropdown")
                self.utils.print_info("The models from dropdown are : ")
                for cnt in policy_unit_items:
                    self.utils.print_info(cnt.text)
                self.auto_actions.click_reference(self.sw_template_web_elements.get_sw_template_name_textfield)
                model_units_list = model_units.split(",")
                self.utils.print_info("The models from CLI are : ", model_units_list)
                model_units_list2 = []
                for cnt2 in model_units_list:
                    if var_type in cnt2:
                        model_units_list2.append(cnt2.replace(var_type, ''))
                    else:
                        kwargs['fail_msg'] = f"The model doesn't contain {var_type}"
                        self.common_validation.fault(**kwargs)
                        return -1
                self.utils.print_info("The new models from CLI are : ", model_units_list2)
                item_count1 = len(model_units_list2)
                self.utils.print_info(f"Found {item_count1} options into CLI")
                if policy_unit_items:
                    for unit in model_units_list2:
                        add_stack_button = self.sw_template_web_elements.get_sw_template_stack_add_button()
                        if add_stack_button:
                            self.utils.print_info("Press ADD button")
                            self.auto_actions.click(add_stack_button)
                            sleep(3)
                        else:
                            kwargs['fail_msg'] = "ADD button was not found"
                            self.common_validation.fault(**kwargs)
                            return -1
                        if self.auto_actions.select_drop_down_options(policy_unit_items, var_type + unit):
                            self.utils.print_info("Unit was added  :", var_type + unit)
                            sleep(20)
                            self.auto_actions.click_reference(self.sw_template_web_elements.get_sw_template_name_textfield)
                        else:
                            self.utils.print_info("Unit was not added  :", var_type + unit)
                            self.auto_actions.click_reference(self.sw_template_web_elements.get_sw_template_name_textfield)
                            kwargs['fail_msg'] = "Unit was not added"
                            self.common_validation.failed(**kwargs)
                            return -1
                else:
                    self.utils.print_info("Cannot read options from dropdown")
                if save_template:
                    save_btns = self.sw_template_web_elements.get_sw_template_save_button_bottom()
                    for save_btn in save_btns:
                        if save_btn.is_displayed():
                            self.utils.print_info("Click on the save template button")
                            self.auto_actions.click(save_btn)
                            self.screen.save_screen_shot()
                            tool_tip_text = tool_tip.tool_tip_text
                            self.utils.print_info("Tool tip Text Displayed on Page", tool_tip_text)
                            for cnt3 in tool_tip_text:
                                if 'Stack template has been saved successfully.' in cnt3:
                                    kwargs['pass_msg'] = "Stack template has been saved successfully"
                                    self.common_validation.passed(**kwargs)
                                    return 1
                                else:
                                    self.utils.print_info("Not found successfully message yet ")

                            def _is_sw_template_available():
                                return self.get_sw_template_row(sw_template_name)
                            self.utils.wait_till(_is_sw_template_available, delay=0.5, is_logging_enabled=True, silent_failure=False)
                            self.screen.save_screen_shot()
                            return 1

                        else:
                            self.utils.print_info("Not found 'Save template' button ")
                else:
                    kwargs['pass_msg'] = "User choose not to save the policy. More configs could be added"
                    self.common_validation.passed(**kwargs)
                    return 1
            else:
                self.utils.print_info("Not found 'ADD Template' button ")

        kwargs['fail_msg'] = "Failed to add sw stack template"
        self.common_validation.failed(**kwargs)
        return -1

    def check_added_sw_stack_template_units(self, model_units, sw_template_name, **kwargs):
        """
        - Flow: First page from stack template
        - This function is working only for stack. It checks if the names of units have correct format
        - Keyword Usage
        - e.g. check added sw stack template units      5520-24T-EXOS,5520-24X-EXOS,5520-48T-EXOS     myTemplate
        :param model_units: a string with all units e.g 5520-24T,5520-24X,5520-48T
        :param sw_template_name: Switch Template Name; ie mypolicy
        :return: 1 if all expected units are displayed in policy and the names match; else -1 ;
                'more' - If more units are found into policy than into CLI;
                'less' - If less units are found into policy than into CLI;
        """
        first_page = self.dev360.get_sw_template_stack_first_page()
        self.utils.print_info(first_page)
        if not first_page:
            kwargs['fail_msg'] = "The first page of template configuration is not displayed"
            self.common_validation.fault(**kwargs)
            return -1
        model_units_list = model_units.split(",")
        self.utils.print_info("The models from CLI are : ", model_units_list)
        model_units_list2 = []
        for cnt2 in model_units_list:
            if "-EXOS" in cnt2:
                model_units_list2.append(cnt2.replace('-EXOS', ''))
            else:
                kwargs['fail_msg'] = "The model doesn't contain '-EXOS'"
                self.common_validation.fault(**kwargs)
                return -1
        add_stack_items = self.dev360.get_sw_template_stack_added_items()
        self.utils.print_info(add_stack_items)
        index = 0
        if add_stack_items:
            item_count3 = len(add_stack_items)
            self.utils.print_info(f"List of models in policy have {item_count3} items")
            self.utils.print_info("The models from policy are : ")
            for cnt in add_stack_items:
                self.utils.print_info(cnt.text)
            if len(add_stack_items) > len(model_units_list):
                self.utils.print_info("More units were found in policy  ")
                return 'more'
            if len(add_stack_items) < len(model_units_list):
                self.utils.print_info("Less units were found in policy  ")
                return 'less'
            for unit in model_units_list2:
                name = sw_template_name + "-" + str(index + 1)
                self.utils.print_info(name)
                self.utils.print_info(add_stack_items[index].text)
                if name == add_stack_items[index].text:
                    self.utils.print_info(f" Stack unit name is correct :  {add_stack_items[index].text} ")
                else:
                    kwargs['fail_msg'] = f"Stack unit name is not correct: {add_stack_items[index].text} ;"
                    self.common_validation.fault(**kwargs)
                    return -1
                index = index + 1
            self.utils.print_info(add_stack_items)
        else:
            kwargs['fail_msg'] = "The units items cannot be read"
            self.common_validation.fault(**kwargs)
            return -1

        kwargs['pass_msg'] = "All expected units are displayed in policy and the names matched"
        self.common_validation.passed(**kwargs)
        return 1

    def save_stack_template(self, sw_template_name, **kwargs):
        """
        Flow: First page from stack template
        This function save the template after the configuration was made
        return 1 if template was saved ; else -1
        """
        first_page = self.dev360.get_sw_template_stack_first_page()
        self.utils.print_info(first_page)
        if not first_page:
            kwargs['fail_msg'] = "The first page of template configuration is not displayed"
            self.common_validation.fault(**kwargs)
            return -1
        save_btns = self.sw_template_web_elements.get_sw_template_save_button()
        rc=-1
        for save_btn in save_btns:
            if save_btn.is_displayed():
                self.utils.print_info("Click on the save template button")
                self.auto_actions.click(save_btn)
                sleep(10)
                tool_tip_text = tool_tip.tool_tip_text
                self.utils.print_info("Tool tip Text Displayed on Page", tool_tip_text)
                def _is_sw_template_available():
                    return self.get_sw_template_row(sw_template_name)

                if self.utils.wait_till(_is_sw_template_available, delay=1, is_logging_enabled=True, silent_failure=False):
                    self.screen.save_screen_shot()
                    rc = 1
            else:
                kwargs['fail_msg'] = "Not found 'Save template' button"
                self.common_validation.fault(**kwargs)
        return rc

    def delete_stack_units_device_template(self, nw_policy, sw_template_name, cli_type, **kwargs):
        """
        This function deletes the unit's template from a policy
        - Keyword Usage
        - ``  Delete Stack Units Device Template    ${NW_POLICY}  ${SW_TEMPLATE_NAME}  ${CLI_TYPE}``

        :param nw_policy: Policy name
        :param sw_template_name: template name
        :param cli_type: Device CLI Type e.g., VOSS,EXOS
        :return: 1 if Switch Stack Template Deleted Successfully else -1
        """
        self.utils.print_info("Navigate to devices")
        self.navigator.navigate_to_devices()
        self.utils.print_info("Navigating Network Policies")
        self.navigator.navigate_configure_network_policies()
        sleep(1)

        self._set_nw_policy_if_needed()

        if self.nw_policy.select_network_policy_in_card_view(nw_policy) == -1:
            kwargs['fail_msg'] = "Not found the network policy. Make sure that it was created"
            self.common_validation.failed(**kwargs)
            return -1

        if NetworkElementConstants.OS_EXOS in cli_type.upper() or NetworkElementConstants.OS_VOSS in cli_type.upper():
            self.utils.print_info("Click on Switching tab")
            self.auto_actions.click_reference(self.device_template_web_elements.get_policy_switching_tab)

            self.utils.print_info("Click on Switch Templates Menu Item")
            self.auto_actions.click_reference(self.device_template_web_elements.get_policy_switch_templates_tab)

        elif NetworkElementConstants.OS_AHFASTPATH in cli_type.upper():
            self.utils.print_info("Click on SR/Dell Switching tab")
            self.auto_actions.click_reference(self.device_template_web_elements.get_policy_sr_dell_switching_tab)

            self.utils.print_info("Click on Switch Templates Menu Item from SR/Dell Switching Section")
            self.auto_actions.click_reference(self.device_template_web_elements.get_policy_sr_dell_switch_templates_tab)

        sel_btn = self.sw_template_web_elements.get_sw_template_select_button()
        sleep(2)

        if sel_btn:
            self.utils.print_info("Click on Switch Template Select button")
            self.auto_actions.click(sel_btn)
            sleep(2)
            # Search for the item to be selected
            sw_template_name = sw_template_name + "-"
            self.utils.print_info("Search for the switch template name: ", sw_template_name)
            self.auto_actions.send_keys(self.sw_template_web_elements.get_sw_template_selection_search_textfield(),
                                        sw_template_name)
            self.auto_actions.click_reference(self.sw_template_web_elements.get_sw_template_selection_search_button)
            sleep(3)
        else:
            kwargs['fail_msg'] = "The select button was not found"
            self.common_validation.fault(**kwargs)
            return -1
        # Select the item
        delete = False
        sel_grid = self.sw_template_web_elements.get_sw_template_selection_grid()
        self.utils.print_info(sel_grid)
        if sel_grid:
            sel_grid_rows = self.sw_template_web_elements.get_sw_template_selection_grid_rows(sel_grid)
        for cont in range(1, 9):
            check_sw_template_name = sw_template_name + str(cont)
            self.utils.print_info("Search :", check_sw_template_name)
            found_row = False
            for row in sel_grid_rows:
                if check_sw_template_name in row.text:
                    self.utils.print_info("Found the matching row: ", row.text)
                    found_row = True
                    delete = True
                    break
            if found_row:
                # Click the checkbox to select the matching row
                self.auto_actions.click(self.sw_template_web_elements.get_sw_template_sel_row_checkbox(row))
                sleep(2)
        if delete:
            delete_button = self.sw_template_web_elements.get_sw_template_select_delete_button()
            if delete_button:
                self.utils.print_info("Collecting the banner text before pressing delete button ")
                tool_tp_text_before = tool_tip.tool_tip_text.copy()
                self.utils.print_info(tool_tp_text_before)
                self.utils.print_info("Press delete button")
                self.auto_actions.click(delete_button)
                yes_confirmation = self.alarm.get_alarm_clear_confirm_yes_button()
                if yes_confirmation:
                    self.auto_actions.click(yes_confirmation)
                    sleep(3)
                    self.utils.print_info("Collecting the banner text after pressing delete button ")
                    tool_tp_text_after = tool_tip.tool_tip_text.copy()
                    self.utils.print_info(tool_tp_text_after)
                    for item_after in tool_tp_text_after:
                        if item_after in tool_tp_text_before:
                            pass
                        else:
                            if 'Template was deleted successfully.' in item_after:
                                self.utils.print_info("Template was deleted successfully.")
                                close_button = self.sw_template_web_elements.get_sw_template_selection_close_button()
                                if close_button:
                                    self.utils.print_info("Return: 1")
                                    self.auto_actions.click(close_button)
                                    self.utils.print_info(close_button)
                                    return 1
                                else:
                                    self.utils.print_info("The close button was not found ")
                            else:
                                self.utils.print_info(" Below error message is displayed after press update button")
                                self.utils.print_info(item_after)
                                close_button = self.sw_template_web_elements.get_sw_template_selection_close_button()
                                if close_button:
                                    self.auto_actions.click(close_button)
                                    self.utils.print_info(close_button)
                                return item_after
                else:
                    kwargs['fail_msg'] = "Confirmation button was not found"
                    self.common_validation.fault(**kwargs)
                    return -1
            else:
                kwargs['fail_msg'] = "Delete button was not found"
                self.common_validation.fault(**kwargs)
                return -1
        else:
            self.utils.print_info("No entry found ")
        close_button = self.sw_template_web_elements.get_sw_template_selection_close_button()
        if close_button:
            self.utils.print_info("Return: 1")
            self.auto_actions.click(close_button)
            self.utils.print_info(close_button)
        return 1

    def delete_stack_switch_template(self, nw_policy, sw_template_name, cli_type, **kwargs):
        """
        This function is used to delete a template from a policy

       :param nw_policy: Network Policy Name
       :param sw_template_name: Switch Template Name
       :param cli_type: Device CLI Type e.g., VOSS,EXOS
       :return: 1 if template was deleted or template doesn't exist; else -1
        """

        self.utils.print_info("Navigate to devices")
        self.navigator.navigate_to_devices()

        self._set_nw_policy_if_needed()

        self.nw_policy.navigate_to_np_edit_tab(nw_policy)
        sleep(5)

        if NetworkElementConstants.OS_EXOS in cli_type.upper() or NetworkElementConstants.OS_VOSS in cli_type.upper():
            self.utils.print_info("Click on Switching tab")
            self.auto_actions.click_reference(self.device_template_web_elements.get_policy_switching_tab)

            self.utils.print_info("Click on Switch Templates Menu Item")
            self.auto_actions.click_reference(self.device_template_web_elements.get_policy_switch_templates_tab)

        elif NetworkElementConstants.OS_AHFASTPATH in cli_type.upper():
            self.utils.print_info("Click on SR/Dell Switching tab")
            self.auto_actions.click_reference(self.device_template_web_elements.get_policy_sr_dell_switching_tab)

            self.utils.print_info("Click on Switch Templates Menu Item from SR/Dell Switching Section")
            self.auto_actions.click_reference(self.device_template_web_elements.get_policy_sr_dell_switch_templates_tab)

        rows = self.sw_template_web_elements.get_sw_template_rows()
        if not rows:
            self.utils.print_info("Switch templates not exists in switch device template page")
            return False
        for row in rows:
            cells = self.sw_template_web_elements.get_sw_template_row_cell(row, 'field-tmpl')
            for cell in cells:
                if sw_template_name in cell.text:
                    check_box = self.sw_template_web_elements.get_sw_template_check_box(row)
                    if check_box:
                        self.utils.print_info("The check box was selected")
                        self.auto_actions.click(check_box)
                    else:
                        self.utils.print_info("The check box was not found ")
        self.utils.print_info("Collecting the banner text before pressing delete button ")
        tool_tp_text_before = tool_tip.tool_tip_text.copy()
        self.utils.print_info(tool_tp_text_before)

        delete_button = self.sw_template_web_elements.get_sw_template_stack_delete_button()
        if delete_button:
            self.utils.print_info("Click on delete button")
            self.auto_actions.click(delete_button)
            sleep(3)
            self.utils.print_info("Collecting the banner text after pressing delete button ")
            tool_tp_text_after = tool_tip.tool_tip_text.copy()
            self.utils.print_info(tool_tp_text_after)
            for item_after in tool_tp_text_after:
                if item_after in tool_tp_text_before:
                    pass
                else:
                    if 'Template was successfully removed from policy.' in item_after:
                        self.utils.print_info("Template was deleted successfully.")
                    else:
                        self.utils.print_info(" Below error message is displayed after press update button")
                        self.utils.print_info(item_after)
                        return item_after
            self.utils.print_info("The templates entries were deleted ")
        else:
            kwargs['fail_msg'] = "Delete button was not found"
            self.common_validation.fault(**kwargs)
            return -1
        return 1

    def check_type_sw_stack_template_units(self, model_units, **kwargs):
        """
        - Flow: First page from stack template
        - This function is working only for stack. It checks if the type of units are the same in XIQ and CLI
        - Keyword Usage
        - e.g. check added sw stack template units      5520-24T-EXOS,5520-24X-EXOS,5520-48T-EXOS     myTemplate
        :param model_units: a string with all units e.g 5520-24T-EXOS,5520-24X-EXOS
        :return: 1 if all expected units are displayed in policy and the names match; else -1 ;
        """
        first_page = self.dev360.get_sw_template_stack_first_page()
        self.utils.print_info(first_page)
        if not first_page:
            kwargs['fail_msg'] = "check_type_sw_stack_template_units() failed. " \
                                 "The first page of template configuration is not displayed"
            self.common_validation.fault(**kwargs)
            return -1
        model_units_list = model_units.split(",")
        self.utils.print_info("The models from CLI are : ", model_units_list)
        model_units_list2 = []
        for cnt2 in model_units_list:
            if "-EXOS" in cnt2:
                model_units_list2.append(cnt2.replace('-EXOS', ''))
            else:
                kwargs['fail_msg'] = "The model doesn't contain '-EXOS'"
                self.common_validation.fault(**kwargs)
                return -1
        add_stack_items = self.dev360.get_sw_template_stack_added_items()
        self.utils.print_info(add_stack_items)
        index = 0
        if add_stack_items:
            item_count3 = len(add_stack_items)
            self.utils.print_info(f"List of models in policy have {item_count3} items")

            for unit in model_units_list2:
                self.auto_actions.click(add_stack_items[index])
                xiq_unit_model = self.dev360.get_sw_template_stack_sw_item()
                self.utils.print_info(f" Stack unit model from XIQ :  {xiq_unit_model.text} ")
                self.utils.print_info(f" Stack unit model from CLI :  {xiq_unit_model.text} ")
                if unit in xiq_unit_model.text:
                    self.utils.print_info("The models are correct ")
                else:
                    kwargs['fail_msg'] = "The models are not correct"
                    self.common_validation.fault(**kwargs)
                    return -1
                index = index + 1
        else:
            kwargs['fail_msg'] = "The units items cannot be read"
            self.common_validation.fault(**kwargs)
            return -1

        kwargs['pass_msg'] = "All expected units are displayed in policy and the names matched"
        self.common_validation.passed(**kwargs)
        return 1

    def create_vlan_in_template(self, policy_name, template_name, cli_type, port, vlan, port_type_name, stp_disable='false'):
        """
        - Create Vlan In Template
        - Keyword Usage:
        - ``Create Vlan In Template     ${policy_name}  ${template_name}  ${port}  ${vlan_number}``
        :param policy_name: Name of the policy
        :param template_name : Name of the template
        :param cli_type: Device CLI Type e.g., VOSS,EXOS
        :param port : Number of the port
        :param vlan : Number of the vlan
        :param port_type_name : Name of the port type
        :return: 1 if vlan creation was successful
        """
        self.select_sw_template(policy_name,  template_name, cli_type)
        self.go_to_port_configuration()
        return self.config_vlan_in_template(port, vlan, port_type_name,stp_disable)

    def create_vlan_in_stacked_template(self, nw_policy, cli_type, sw_template_name, slot, port, vlan, port_type_name,
                                        stp_disable='false', **kwargs):
        """
        - Create Vlan In Stacked Template
        - Keyword Usage:
        - ``Create Vlan In Stacked Template     ${nw_policy}  ${sw_template_name}  ${slot}  ${port}  ${vlan}
               ${port_type_name}``
        :param nw_policy: Name of the policy
        :param sw_template_name : Name of the template
        :param slot: Number of the slot
        :param port: Number of the port
        :param vlan : Number of the vlan
        :param port_type_name : Name of the port type
        :param cli_type: Device CLI Type e.g., VOSS,EXOS
        :return: 1 if vlan creation was successful
        """
        slot_index = 1
        slot_found = False
        self.select_sw_template(nw_policy, sw_template_name, cli_type)
        self.go_to_port_configuration()
        sleep(5)
        self.utils.print_info("Gather the list of the devices in the stack")
        complete_stack = self.sw_template_web_elements.get_complete_stack_list()
        if complete_stack:
            slots_in_stack = self.sw_template_web_elements.get_complete_stack_all_rows(complete_stack)
            for stack_item in slots_in_stack:
                if slot_index == int(slot):
                    self.utils.print_info("Slot " + slot + " found in the stack, selecting the slot")
                    self.auto_actions.click(stack_item)
                    slot_found = True
                    break
                slot_index = slot_index + 1
            if slot_found:
                port_string = str(slot) + ':' + str(port)
                return self.config_vlan_in_template(port_string, vlan, port_type_name, stp_disable)
            else:
                kwargs['fail_msg'] = "Unable to locate the correct slot"
                self.common_validation.fault(**kwargs)
                return -1
            return -1
        else:
            kwargs['fail_msg'] = "Unable to gather the list of the devices in the stack"
            self.common_validation.fault(**kwargs)
            return -1

    def config_vlan_in_template(self, port_string, vlan_number, port_type_name, stp_disable='false', **kwargs):
        vlan_already_exists = False
        self.auto_actions.scroll_down()
        sleep(5)
        self.utils.print_info("Gathering all port detail information and rows")
        port_details_all_rows = self.sw_template_web_elements.get_port_details_all_rows()
        if port_details_all_rows:
            self.utils.print_info("Checking for a match for port " + port_string)
            for row in port_details_all_rows:
                label_str = (self.sw_template_web_elements.get_port_details_row_label(row)).text
                if label_str == port_string:
                    self.utils.print_info("Match for port " + port_string + " found")
                    self.utils.print_info("Attempting to locate the Add button")
                    add_button = self.sw_template_web_elements.get_port_details_row_add_button(row)
                    if add_button:
                        self.utils.print_info("Clicking the Add button")
                        self.auto_actions.click(add_button)
                        sleep(5)
                        self.utils.print_info("Attempting to locate the Port Type Textfield")
                        port_type_txt = self.sw_template_web_elements.get_port_type_text_field()
                        if port_type_txt:
                            self.utils.print_info("Attempting to write to the Port Type Textfield")
                            self.auto_actions.send_keys(port_type_txt, port_type_name)
                        else:
                            kwargs['fail_msg'] = "Unable to locate the Port Type Textfield"
                            self.common_validation.fault(**kwargs)
                            return -1
                        self.auto_actions.scroll_down()
                        sleep(5)
                        self.utils.print_info("Attempting to locate the Vlan UI IP Button")
                        ui_ip_button = self.sw_template_web_elements.get_port_details_vlan_ui_ip_button()
                        if ui_ip_button:
                            self.utils.print_info("Clicking the Vlan UI IP Button")
                            self.auto_actions.click(ui_ip_button)
                            sleep(5)
                            self.utils.print_info("Attempting to locate the Vlan PopUp Entries")
                            vlan_entries = self.sw_template_web_elements.get_port_details_vlan_pop_up_all_entries()
                            if vlan_entries:
                                vlan_name = 'VLAN_' + vlan_number
                                self.utils.print_info("Checking entries to see if vlan already exists")
                                for pop_entry in vlan_entries:
                                    text_value = pop_entry.text
                                    if text_value == vlan_number or text_value.lower() == vlan_name.lower():
                                        vlan_already_exists = True
                                        self.utils.print_info("Vlan " + vlan_number + " already exists")
                                        self.utils.print_info("Selecting vlan " + vlan_number + " option")
                                        self.auto_actions.click(pop_entry)
                                if not vlan_already_exists:
                                    self.utils.print_info("Vlan " + vlan_number + " does not exist")
                                    self.utils.print_info("Vlan " + vlan_number + " must be created")
                                    self.utils.print_info("Attempting to locate the Vlan Add Button")
                                    vlan_add_button = self.sw_template_web_elements.get_port_details_add_vlan_button()
                                    if vlan_add_button:
                                        self.utils.print_info("Clicking the Vlan Add Button")
                                        self.auto_actions.click(vlan_add_button)
                                        self.utils.print_info("Attempting to locate the Vlan Name Field")
                                        vlan_name_txt_field = self.sw_template_web_elements.get_port_details_vlan_name()
                                        self.utils.print_info("Attempting to locate the Vlan ID Field")
                                        vlan_id_txt_field = self.sw_template_web_elements.get_port_details_vlan_id()
                                        if vlan_name_txt_field and vlan_id_txt_field:
                                            vlan_name = 'VLAN_' + vlan_number
                                            self.utils.print_info("Attempting to write to the Vlan Name Textfield")
                                            self.auto_actions.send_keys(vlan_name_txt_field, vlan_name)
                                            self.utils.print_info("Attempting to write to the Vlan Id Textfield")
                                            self.auto_actions.send_keys(vlan_id_txt_field, vlan_number)
                                            self.utils.print_info("Attempting to locate Save Vlan Button")
                                            save_vlan_button = self.sw_template_web_elements.get_port_details_vlan_save_button()
                                            if save_vlan_button:
                                                self.utils.print_info("Clicking Save Vlan Button")
                                                self.auto_actions.click(save_vlan_button)
                                            else:
                                                kwargs['fail_msg'] = "Unable to locate Save Vlan Button"
                                                self.common_validation.fault(**kwargs)
                                                return -1
                                    else:
                                        kwargs['fail_msg'] = "Unable to locate the Vlan Add Button"
                                        self.common_validation.fault(**kwargs)
                                        return -1

                                if stp_disable:
                                    stp_status = self.legacy_port_type_editor.get_stp_status()
                                    if stp_status:
                                        self.auto_actions.disable_check_box(stp_status)
                                    else:
                                        kwargs['fail_msg'] = "Unable to find check box to disable STP for port"
                                        self.common_validation.fault(**kwargs)
                                        return -1

                                self.utils.print_info("Attempting to locate Port Type Save Button")
                                port_type_save_button = self.sw_template_web_elements.get_port_type_save_button()
                                if port_type_save_button:
                                    self.utils.print_info("Clicking the Port Type Save Button")
                                    self.auto_actions.click(port_type_save_button)
                                else:
                                    kwargs['fail_msg'] = "Unable to locate Port Type Save Button"
                                    self.common_validation.fault(**kwargs)
                                    return -1
                                self.utils.print_info("Attempting to locate Save Template Button")
                                save_template_button = self.sw_template_web_elements.get_switch_temp_save_button()
                                if save_template_button:
                                    self.utils.print_info("Clicking the Save Template Button")
                                    self.auto_actions.click(save_template_button)
                                else:
                                    kwargs['fail_msg'] = "Unable to locate Save Template Button"
                                    self.common_validation.fault(**kwargs)
                                    return -1
                                return 1
                            else:
                                kwargs['fail_msg'] = "Unable to locate the Vlan PopUp Entries"
                                self.common_validation.fault(**kwargs)
                                return -1
                        else:
                            kwargs['fail_msg'] = "Unable to locate the Vlan UI IP Button"
                            self.common_validation.fault(**kwargs)
                            return -1
                    else:
                        kwargs['fail_msg'] = "Unable to locate the Add button"
                        self.common_validation.fault(**kwargs)
                        return -1
            # if code made it  here not match was found
            kwargs['fail_msg'] = f"Match for port {port_string} NOT found"
            self.common_validation.failed(**kwargs)
            return -1
        else:
            kwargs['fail_msg'] = "Unable to gather port detail information and rows"
            self.common_validation.failed(**kwargs)
            return -1

    def create_pse_profile(self, network_policy_name, device_template_name, cli_type, device_model, port_type_name, pse_profile_name, power_limit, priority, power_mode, **kwargs):
        """
        - This Function creates a new PSE Profile from Network Policy Device Template
        - Keyword Usage :     Create Pse Profile      ${NETWORK_POLICY_NAME}   ${DEVICE_TEMPLATE_NAME}  ${DEVICE_MODEL}    ${PORT_TYPE_NAME}   ${PSE_PROFILE_NAME}          ${POWER_LIMIT}             ${PRIORITY}             ${POWER_MODE}
        :param Network Policy Name -> Name of network policy
        :param DEVICE_TEMPLATE_NAME -> Name of Device Template
        :param DEVICE_MODEL     -> Device Model that should be found in the Template list
        :param PORT_TYPE_NAME   -> String, for Device Port Type
        :param PSE_PROFILE_NAME -> String, for PSE Profile Name
        :param POWER_LIMIT     ->  Float Value
        :param PRIORITY        -> Value chosen from the following options    low, high or critical     any other is not accepted by the function
        :param POWER_MODE      -> Value chosen from the following options  802.3af or 802.3at or 802.3bt     any other is not accepted by the function
        :param cli_type: Device CLI Type e.g., VOSS,EXOS
        :return: 1 if the pse profile is created and saved else -1 ;
        """
        self._set_nw_policy_if_needed()

        self.nw_policy.create_switching_routing_network_policy(network_policy_name)
        self.utils.print_info("Navigating Network Policies")
        self.navigator.navigate_configure_network_policies()
        sleep(1)
        self.nw_policy.select_network_policy_in_card_view(network_policy_name)
        sleep(2)

        if NetworkElementConstants.OS_EXOS in cli_type.upper() or NetworkElementConstants.OS_VOSS in cli_type.upper():
            self.utils.print_info("Click on Switching tab")
            self.auto_actions.click_reference(self.device_template_web_elements.get_policy_switching_tab)

            self.utils.print_info("Click on Switch Templates Menu Item")
            self.auto_actions.click_reference(self.device_template_web_elements.get_policy_switch_templates_tab)

        elif NetworkElementConstants.OS_AHFASTPATH in cli_type.upper():
            self.utils.print_info("Click on SR/Dell Switching tab")
            self.auto_actions.click_reference(self.device_template_web_elements.get_policy_sr_dell_switching_tab)

            self.utils.print_info("Click on Switch Templates Menu Item from SR/Dell Switching Section")
            self.auto_actions.click_reference(self.device_template_web_elements.get_policy_sr_dell_switch_templates_tab)

        if self.check_sw_template(device_model):
            kwargs['pass_msg'] = "Template Already present in the template grid"
            self.common_validation.passed(**kwargs)
            return 1
        add_buttons = self.sw_template_web_elements.get_sw_template_add_button()
        sleep(2)
        self.utils.print_info("add_btn: ", add_buttons)
        for add_btn in add_buttons:
            if add_btn.is_displayed():
                self.utils.print_info("Click on sw Template Add button")
                self.auto_actions.click(add_btn)
                sleep(2)
                self.utils.print_info("select the sw: ", device_model)
                sw_list_items = self.sw_template_web_elements.get_sw_template_platform_from_drop_down()
                sleep(2)
                for el in sw_list_items:
                    self.utils.print_info("Switch template names: ", el.text.upper())
                    if not el:
                        pass
                    if device_model.upper() in el.text.upper():
                        self.auto_actions.click(el)
                        break
                    print(el.text)
                sleep(3)
                self.utils.print_info("Enter the switch Template Name: ", device_template_name)
                value_template = self.auto_actions.send_keys(
                    self.sw_template_web_elements.get_sw_template_name_textfield(), device_template_name)
                sleep(3)
                self.auto_actions.click(value_template)
        port_configuration = self.sw_template_web_elements.port_config_template()
        if port_configuration:
            self.utils.print_info("The Port Configuration button was found")
            self.auto_actions.click(port_configuration)
            sleep(7)
            select_all_ports = self.sw_template_web_elements.all_ports_selected()
            if select_all_ports:
                self.utils.print_info("Select all ports button was found")
                self.auto_actions.click(select_all_ports)
                sleep(5)
                assign_to_all_ports_selected = self.sw_template_web_elements.assign_all_ports_selected()
                if assign_to_all_ports_selected:
                    self.utils.print_info("Assign Button was found")
                    self.auto_actions.click(assign_to_all_ports_selected)
                    sleep(3)
                    port_type = self.sw_template_web_elements.port_type_template_create_new()
                    if port_type:
                        self.utils.print_info("Creating new Port Type template for selected ports")
                        sleep(3)
                        self.auto_actions.click(port_type)
                        pse_profile_plus_button = self.sw_template_web_elements.pse_profile_user_option()
                        if pse_profile_plus_button:
                            sleep(3)
                            self.screen.save_screen_shot()
                            self.utils.print_info("A new PSE Profile will be created")
                            self.auto_actions.click(pse_profile_plus_button)
                            self.auto_actions.send_keys(self.sw_template_web_elements.pse_profile_name_tab(),
                                                        pse_profile_name)
                        else:
                            kwargs['fail_msg'] = "Pse profile user button not found"
                            self.common_validation.fault(**kwargs)
                            return -1
                        if power_limit:
                            self.utils.print_info(
                                "The following value {} will be inserted into the power limit field".format(
                                    power_limit))
                            self.auto_actions.send_keys(self.sw_template_web_elements.pse_profile_power_limit(),
                                                        Keys.CONTROL + "a")
                            self.utils.print_info("Deleting the default value from the field")
                            self.auto_actions.send_keys(self.sw_template_web_elements.pse_profile_power_limit(),
                                                        Keys.BACK_SPACE)
                            self.utils.print_info("Inserting given value in the field")
                            self.auto_actions.send_keys(self.sw_template_web_elements.pse_profile_power_limit(),
                                                        power_limit)
                            sleep(2)
                            self.screen.save_screen_shot()
                        else:
                            kwargs['fail_msg'] = "No inserted value found for power limit"
                            self.common_validation.fault(**kwargs)
                            return -1
                        if priority:
                            sleep(3)
                            self.utils.print_info("Setting the priority value")
                            self.auto_actions.click_reference(self.sw_template_web_elements.priority_dropdown)
                            sleep(3)
                            if priority == "low" or priority == "high" or priority == "critical":
                                self.utils.print_info("Selecting {} value".format(priority))
                                sleep(3)
                                self.auto_actions.select_drop_down_options(
                                    self.sw_template_web_elements.priority_items(), priority)
                                self.screen.save_screen_shot()
                            else:
                                self.utils.print_info(
                                    "The priority value should be wrong. It can be low, high or critical. Please check")
                        else:
                            kwargs['fail_msg'] = "No inserted value found for priority"
                            self.common_validation.fault(**kwargs)
                            return -1
                        if power_mode:
                            self.utils.print_info("Setting the power mode value")
                            sleep(5)
                            self.auto_actions.click_reference(self.sw_template_web_elements.power_mode_dropdown)
                            if power_mode == "802.3af" or power_mode == "802.3at" or power_mode == "802.3bt":
                                self.utils.print_info("Selecting {} value".format(power_mode))
                                sleep(3)
                                self.auto_actions.select_drop_down_options(
                                    self.sw_template_web_elements.power_mode_items(), power_mode)
                                self.screen.save_screen_shot()
                            else:
                                self.utils.print_info(
                                    "The power mode value should be wrong. It can be 802.3af or 802.3at")
                        else:
                            kwargs['fail_msg'] = "No inserted value found for power mode"
                            self.common_validation.fault(**kwargs)
                            return -1
                        sleep(3)
                        self.screen.save_screen_shot()
                        self.utils.print_info("Saving PSE profile...")
                        save_pse_profile_button = self.sw_template_web_elements.save_button_template_pse_profile()
                        if save_pse_profile_button:
                            self.utils.print_info("Loading... Saving...")
                            sleep(3)
                            self.auto_actions.click(save_pse_profile_button)
                            self.utils.print_info("Saved")
                            sleep(3)
                            self.screen.save_screen_shot()
                            port_type_tab = self.sw_template_web_elements.port_name()
                            if port_type_tab.is_displayed:
                                self.utils.print_info("The Port Type Template will be created")
                                sleep(3)
                                self.auto_actions.click(port_type_tab)
                                self.auto_actions.send_keys(self.sw_template_web_elements.port_name(), port_type_name)
                                sleep(3)
                                save_button_port_type = self.sw_template_web_elements.port_type_save_button()
                                self.utils.print_info("Saving...")
                                self.auto_actions.click(save_button_port_type)
                                self.utils.print_info("The port configuration was saved")
                                sleep(3)
                                self.screen.save_screen_shot()
                                save_button = self.sw_template_web_elements.save_device_template()
                                for element in save_button:
                                    if "SAVE" == element.text:
                                        sleep(5)
                                        self.auto_actions.click(element)
                                        sleep(3)
                                        self.utils.print_info("Saving Device Template...")
                                        self.navigator.navigate_to_devices()
                                        self.utils.print_info("Navigating to Devices..")
                                    else:
                                        pass
                            else:
                                kwargs['fail_msg'] = "The port type was not created and the configuration not saved"
                                self.common_validation.fault(**kwargs)
                                return -1
                        else:
                            kwargs['fail_msg'] = "create_pse_profile() failed. "
                            self.common_validation.fault(**kwargs)
                            return -1
                    else:
                        kwargs['fail_msg'] = "Couldn't Create New Template for selected ports"
                        self.common_validation.fault(**kwargs)
                        return -1
                else:
                    kwargs['fail_msg'] = "The Assign Button was not Found"
                    self.common_validation.fault(**kwargs)
                    return -1
            else:
                kwargs['fail_msg'] = "Select all Ports button was not found"
                self.common_validation.fault(**kwargs)
                return -1
        else:
            kwargs['fail_msg'] = "The Port Configuration Button was not found"
            self.common_validation.fault(**kwargs)
            return -1

    def add_to_string(self, added_string, string):
        return added_string + " " + string[0:]

    def poe_status_button(self, network_policy_name, device_template_name, cli_type, device_model, port_type_name, poe_status, **kwargs):
        """
        - This Function modifies, turns off or on the POE Status
        - Keyword Usage : Poe Status Button           ${NETWORK_POLICY_NAME}   ${DEVICE_TEMPLATE_NAME}  ${DEVICE_MODEL}    ${PORT_TYPE_NAME}
        :param Network Policy Name -> Name of network policy
        :param DEVICE_TEMPLATE_NAME -> Name of Device Template
        :param DEVICE_MODEL     -> Device Model that should be found in the Template list
        :param PORT_TYPE_NAME   -> String, for Device Port Type
        :param POE_STATUS       -> String, could be "on", "On", "off" or "Off"
        :param cli_type: Device CLI Type e.g., VOSS,EXOS
        :return: 1 if poe status is turned off else -1 ;
        """
        self._set_nw_policy_if_needed()

        self.nw_policy.create_switching_routing_network_policy(network_policy_name)
        self.utils.print_info("Navigating Network Policies")
        self.navigator.navigate_configure_network_policies()
        sleep(1)
        self.nw_policy.select_network_policy_in_card_view(network_policy_name)
        sleep(2)

        if NetworkElementConstants.OS_EXOS in cli_type.upper() or NetworkElementConstants.OS_VOSS in cli_type.upper():
            self.utils.print_info("Click on Switching tab")
            self.auto_actions.click_reference(self.device_template_web_elements.get_policy_switching_tab)

            self.utils.print_info("Click on Switch Templates Menu Item")
            self.auto_actions.click_reference(self.device_template_web_elements.get_policy_switch_templates_tab)

        elif NetworkElementConstants.OS_AHFASTPATH in cli_type.upper():
            self.utils.print_info("Click on SR/Dell Switching tab")
            self.auto_actions.click_reference(self.device_template_web_elements.get_policy_sr_dell_switching_tab)

            self.utils.print_info("Click on Switch Templates Menu Item from SR/Dell Switching Section")
            self.auto_actions.click_reference(self.device_template_web_elements.get_policy_sr_dell_switch_templates_tab)


        if self.check_sw_template(device_model):
            kwargs['pass_msg'] = "Template Already present in the template grid"
            self.common_validation.passed(**kwargs)
            return 1
        add_buttons = self.sw_template_web_elements.get_sw_template_add_button()
        sleep(2)
        self.utils.print_info("add_btn: ", add_buttons)
        for add_btn in add_buttons:
            if add_btn.is_displayed():
                self.utils.print_info("Click on sw Template Add button")
                self.auto_actions.click(add_btn)
                sleep(2)
                self.utils.print_info("select the sw: ", device_model)
                sw_list_items = self.sw_template_web_elements.get_sw_template_platform_from_drop_down()
                sleep(2)
                for el in sw_list_items:
                    self.utils.print_info("Switch template names: ", el.text.upper())
                    if not el:
                        pass
                    if device_model.upper() in el.text.upper():
                        self.auto_actions.click(el)
                        break
                    print(el.text)
                sleep(3)
                self.utils.print_info("Enter the switch Template Name: ", device_template_name)
                value_template = self.auto_actions.send_keys(
                    self.sw_template_web_elements.get_sw_template_name_textfield(), device_template_name)
                sleep(3)
                self.auto_actions.click(value_template)
        port_configuration = self.sw_template_web_elements.port_config_template()
        if port_configuration:
            self.utils.print_info("The Port Configuration button was found")
            self.auto_actions.click(port_configuration)
            sleep(7)
            select_all_ports = self.sw_template_web_elements.all_ports_selected()
            if select_all_ports:
                self.utils.print_info("Select all ports button was found")
                self.auto_actions.click(select_all_ports)
                sleep(5)
                assign_to_all_ports_selected = self.sw_template_web_elements.assign_all_ports_selected()
                if assign_to_all_ports_selected:
                    self.utils.print_info("Assign Button was found")
                    self.auto_actions.click(assign_to_all_ports_selected)
                    sleep(3)
                    port_type = self.sw_template_web_elements.port_type_template_create_new()
                    if port_type:
                        self.utils.print_info("Creating new Port Type template for selected ports")
                        sleep(3)
                        self.auto_actions.click(port_type)
                        poe_button_status = self.sw_template_web_elements.poe_button()
                        if poe_status == 'off' or poe_status == 'Off':
                            self.utils.print_info("The Poe Status button will be clicked")
                            sleep(3)
                            self.screen.save_screen_shot()
                            self.auto_actions.click(poe_button_status)
                            sleep(3)
                            self.screen.save_screen_shot()
                            self.utils.print_info("The Poe Status button was changed to off")
                        elif poe_status == 'on' or poe_status == 'On':
                            self.utils.print_info("The Poe Status button will be clicked. By default the value is ON")
                            sleep(3)
                            self.screen.save_screen_shot()
                            self.auto_actions.click(poe_button_status)
                            sleep(2)
                            self.auto_actions.click(poe_button_status)
                            sleep(3)
                            self.screen.save_screen_shot()
                            self.utils.print_info("The Poe Status button was changed to on")
                        else:
                            kwargs['fail_msg'] = "The Poe status value was not correct"
                            self.common_validation.fault(**kwargs)
                            return -1
                        port_type_tab = self.sw_template_web_elements.port_name()
                        if port_type_tab.is_displayed:
                            self.utils.print_info("The Port Type Template will be created")
                            sleep(3)
                            self.auto_actions.click(port_type_tab)
                            self.auto_actions.send_keys(self.sw_template_web_elements.port_name(), port_type_name)
                            sleep(3)
                            save_button_port_type = self.sw_template_web_elements.port_type_save_button()
                            self.utils.print_info("Saving...")
                            self.auto_actions.click(save_button_port_type)
                            self.utils.print_info("The port configuration was saved")
                            sleep(3)
                            self.screen.save_screen_shot()
                            save_button = self.sw_template_web_elements.save_device_template()
                            for element in save_button:
                                if "SAVE" == element.text:
                                    sleep(5)
                                    self.auto_actions.click(element)
                                    sleep(3)
                                    self.utils.print_info("Saving Device Template...")
                                    self.navigator.navigate_to_devices()
                                    self.utils.print_info("Navigating to Devices..")
                                else:
                                    pass
                            else:
                                kwargs['fail_msg'] = "The port type was not created and the configuration not saved"
                                self.common_validation.failed(**kwargs)
                                return -1
                        else:
                            kwargs['fail_msg'] = "The Poe Status button was not found"
                            self.common_validation.fault(**kwargs)
                            return -1
                    else:
                        kwargs['fail_msg'] = "Couldn't Create New Template for selected ports"
                        self.common_validation.fault(**kwargs)
                        return -1
                else:
                    kwargs['fail_msg'] = "The Assign Button was not Found"
                    self.common_validation.fault(**kwargs)
                    return -1
            else:
                kwargs['fail_msg'] = "Select all Ports button was not found"
                self.common_validation.fault(**kwargs)
                return -1
        else:
            kwargs['fail_msg'] = "The Port Configuration Button was not found"
            self.common_validation.fault(**kwargs)
            return -1

    def poe_toggle_using_existing_port_type(self, network_policy_name, device_template_name, cli_type, device_model, existing_port_type_option, poe_status, **kwargs):
        """
        - This Function modifies, turns off or on the POE Status on existing port type
        - Keyword Usage : Poe Status Button           ${NETWORK_POLICY_NAME}   ${DEVICE_TEMPLATE_NAME}  ${DEVICE_MODEL}    ${PORT_TYPE_NAME}
        :param Network Policy Name -> Name of network policy
        :param DEVICE_TEMPLATE_NAME -> Name of Device Template
        :param DEVICE_MODEL     -> Device Model that should be found in the Template list
        :param PORT_TYPE_NAME   -> String, for Device Port Type
        :param POE_STATUS       -> String, could be "on", "On", "off" or "Off"
        :param cli_type: Device CLI Type e.g., VOSS,EXOS
        :return: 1 if poe status is turned off else -1 ;
        """
        self._set_nw_policy_if_needed()

        self.nw_policy.create_switching_routing_network_policy(network_policy_name)
        self.utils.print_info("Navigating Network Policies")
        self.navigator.navigate_configure_network_policies()
        sleep(1)
        self.nw_policy.select_network_policy_in_card_view(network_policy_name)
        sleep(2)

        if NetworkElementConstants.OS_EXOS in cli_type.upper() or NetworkElementConstants.OS_VOSS in cli_type.upper():
            self.utils.print_info("Click on Switching tab")
            self.auto_actions.click_reference(self.device_template_web_elements.get_policy_switching_tab)

            self.utils.print_info("Click on Switch Templates Menu Item")
            self.auto_actions.click_reference(self.device_template_web_elements.get_policy_switch_templates_tab)

        elif NetworkElementConstants.OS_AHFASTPATH in cli_type.upper():
            self.utils.print_info("Click on SR/Dell Switching tab")
            self.auto_actions.click_reference(self.device_template_web_elements.get_policy_sr_dell_switching_tab)

            self.utils.print_info("Click on Switch Templates Menu Item from SR/Dell Switching Section")
            self.auto_actions.click_reference(self.device_template_web_elements.get_policy_sr_dell_switch_templates_tab)

        if self.check_sw_template(device_model):
            kwargs['pass_msg'] = "Template Already present in the template grid"
            self.common_validation.passed(**kwargs)
            return 1
        add_buttons = self.sw_template_web_elements.get_sw_template_add_button()
        sleep(2)
        self.utils.print_info("add_btn: ", add_buttons)
        for add_btn in add_buttons:
            if add_btn.is_displayed():
                self.utils.print_info("Click on sw Template Add button")
                self.auto_actions.click(add_btn)
                sleep(2)
                self.utils.print_info("select the sw: ", device_model)
                sw_list_items = self.sw_template_web_elements.get_sw_template_platform_from_drop_down()
                sleep(2)
                for el in sw_list_items:
                    self.utils.print_info("Switch template names: ", el.text.upper())
                    if not el:
                        pass
                    if device_model.upper() in el.text.upper():
                        self.auto_actions.click(el)
                        break
                    print(el.text)
                sleep(3)
                self.utils.print_info("Enter the switch Template Name: ", device_template_name)
                value_template = self.auto_actions.send_keys(
                    self.sw_template_web_elements.get_sw_template_name_textfield(), device_template_name)
                sleep(3)
                self.auto_actions.click(value_template)
        port_configuration = self.sw_template_web_elements.port_config_template()
        if port_configuration:
            self.utils.print_info("The Port Configuration button was found")
            self.auto_actions.click(port_configuration)
            sleep(7)
            select_all_ports = self.sw_template_web_elements.all_ports_selected()
            if select_all_ports:
                self.utils.print_info("Select all ports button was found")
                self.auto_actions.click(select_all_ports)
                sleep(5)
                assign_to_all_ports_selected = self.sw_template_web_elements.assign_all_ports_selected()
                if assign_to_all_ports_selected:
                    self.utils.print_info("Assign Button was found")
                    self.auto_actions.click(assign_to_all_ports_selected)
                    sleep(3)
                    self.utils.print_info("Clicking on Choose Existing button")
                    choose_existing_port_type = self.sw_template_web_elements.existing_port_type_button()
                    self.auto_actions.click(choose_existing_port_type)
                    existing_port_type_list = self.sw_template_web_elements.port_type_list()
                    sleep(3)
                    self.screen.save_screen_shot()
                    for item in existing_port_type_list:
                        self.utils.print_info(item.text)
                        if existing_port_type_option == item.text:
                            self.utils.print_info("Searching for the Port type Option")
                            sleep(2)
                            self.auto_actions.click(item)
                            self.utils.print_info("Clicking on Save Existing Port Type")
                            sleep(3)
                            self.screen.save_screen_shot()
                            save_btn_existing_port_type = self.sw_template_web_elements.save_btn_existing_port()
                            self.auto_actions.click(save_btn_existing_port_type)
                            self.utils.print_info("Saved")
                            edit_button = self.sw_template_web_elements.edit_port_button()
                            if edit_button:
                                sleep(2)
                                self.utils.print_info("Clicking Edit Port Button")
                                self.auto_actions.click(edit_button)
                                sleep(3)
                                self.screen.save_screen_shot()
                                poe_button_status = self.sw_template_web_elements.poe_button()
                                if poe_status == 'off' or poe_status == 'Off':
                                    self.utils.print_info("The Poe Status button will be clicked")
                                    sleep(3)
                                    self.auto_actions.click(poe_button_status)
                                    sleep(3)
                                    self.screen.save_screen_shot()
                                    self.utils.print_info("The Poe Status button was changed to off")
                                elif poe_status == 'on' or poe_status == 'On':
                                    self.utils.print_info("The Poe Status button will be clicked")
                                    sleep(3)
                                    self.auto_actions.click(poe_button_status)
                                    sleep(2)
                                    self.auto_actions.click(poe_button_status)
                                    sleep(3)
                                    self.screen.save_screen_shot()
                                    self.utils.print_info("The Poe Status button was changed to on")
                                else:
                                    kwargs['fail_msg'] = "The Poe status value was not correct"
                                    self.common_validation.failed(**kwargs)
                                    return -1
                                save_button_port_type = self.sw_template_web_elements.port_type_save_button()
                                self.utils.print_info("Saving...")
                                self.auto_actions.click(save_button_port_type)
                                self.utils.print_info("The port configuration was saved")
                                sleep(3)
                                self.screen.save_screen_shot()
                                save_button = self.sw_template_web_elements.save_device_template()
                                for element in save_button:
                                    if "SAVE" == element.text:
                                        sleep(5)
                                        self.auto_actions.click(element)
                                        sleep(3)
                                        self.utils.print_info("Saving Device Template...")
                                        self.navigator.navigate_to_devices()
                                        self.utils.print_info("Navigating to Devices..")
                                    else:
                                        pass
                                else:
                                    kwargs['fail_msg'] = "The port type was not created and the configuration not saved"
                                    self.common_validation.fault(**kwargs)
                                    return -1
                    else:
                        kwargs['fail_msg'] = "Ports not selected"
                        self.common_validation.fault(**kwargs)
                        return -1

    def add_supplemental_cli_into_template(self, nw_policy, sw_template_name, s_cli_name, commands=None,
                                           navigate_to_scli=True, save_template=True, **kwargs):
        """
        This function is used to add commands into S-CLI by using network policy and template
        :param nw_policy: name of policy
        :param sw_template_name: name of template
        :param s_cli_name: name of s-cli profile
        :param commands:  The commands which will be added into S-CLI. Multiple commands are supported
        :param navigate_to_scli: True - it will navigate: Devices --> Device Templates -> Advanced Settings ; False - it
        will not navigate(e.g. in the case if the program is already there)
        :param save_template: True - will save the template ; False - will not save the template (More configures can be
        added after)
        :return: 1 - if Supplemental CLI was added successfully; -1 - if not
        """

        if navigate_to_scli:
            if self.select_adv_settings_tab(nw_policy, sw_template_name) == -1:
                kwargs['fail_msg'] = "Failed to select the Advanced Settings tab"
                self.common_validation.fault(**kwargs)
                return -1

        supple_cli_on = self.sw_template_web_elements.get_sw_template_supplemental_cli_on_button()
        if supple_cli_on:
            if supple_cli_on.get_attribute('checked') != 'checked':
                self.utils.print_info("Click on ON supplemental cli ")
                AutoActions().click(supple_cli_on)

            supple_cli_name_text = self.sw_template_web_elements.get_sw_template_supplemental_cli_name_text()
            if supple_cli_name_text:
                self.utils.print_info("Enter name for s-cli ")
                self.auto_actions.send_keys(supple_cli_name_text, s_cli_name)
            else:
                kwargs['fail_msg'] = "Failed to get supplemental cli name text"
                self.common_validation.fault(**kwargs)
                return -1

            cli_command_list = commands.split(",")
            new_line_cli_commands = "\n".join(cli_command_list)
            supple_cli_name_commands = \
                self.sw_template_web_elements.get_sw_template_supplemental_cli_commands_text()
            if supple_cli_name_commands:
                self.utils.print_info("Enter the commands  ")
                self.auto_actions.send_keys(supple_cli_name_commands, new_line_cli_commands)
            else:
                kwargs['fail_msg'] = "Failed to get supplemental cli name commands"
                self.common_validation.fault(**kwargs)
                return -1

            if save_template:
                self.utils.print_info("Saving S-cli")
                if self.save_template() == -1:
                    kwargs['fail_msg'] = "Failed to save S-cli"
                    self.common_validation.failed(**kwargs)
                    return -1
            sleep(3)
            return 1
        else:
            kwargs['fail_msg'] = "add_supplemental_cli_into_template() failed. "
            self.common_validation.failed(**kwargs)
            return -1

    def select_adv_settings_tab(self, network_policy_name, device_template_name, cli_type, **kwargs):
        """
        This function is used to select the Advanced Settings tab of a device template within a policy
        :param network_policy_name: name of policy
        :param device_template_name: name of template
        :param cli_type: Device CLI Type e.g., VOSS,EXOS
        :return: 1 - if the navigation was successful ; -1 - if not
        """
        try:
            self.select_sw_template(network_policy_name, device_template_name, cli_type)
            if not self.sw_template_web_elements.get_sw_template_adv_settings_tab():
                kwargs['fail_msg'] = "select_adv_settings_tab() failed. Advanced Settings tab is not displayed!"
                self.common_validation.fault(**kwargs)
                return -1

            self.utils.print_info("Click on Advanced Settings tab")
            self.auto_actions.click_reference(self.sw_template_web_elements.get_sw_template_adv_settings_tab)
        except Exception as exc:
            kwargs['fail_msg'] = f"Exception {exc}"
            self.common_validation.fault(**kwargs)
            return -1
        sleep(3)
        kwargs['pass_msg'] = "The navigation was successful"
        self.common_validation.passed(**kwargs)
        return 1

    def save_template(self, **kwargs):
        """
        This function is used to save the current device template
        :return: 1 - if the save was successful ; -1 - if not
        """
        save_btns = self.sw_template_web_elements.get_sw_template_save_button()
        found_save_button = False
        for save_btn in save_btns:
            if save_btn.is_displayed():
                self.utils.print_info("Click on the save template button")
                found_save_button = True
                self.auto_actions.click(save_btn)
                save_successful = False

                def _check_succesful_message():
                    tool_tip_text = tool_tip.tool_tip_text
                    self.utils.print_info("Tool tip Text Displayed on Page", tool_tip_text)
                    for cnt3 in tool_tip_text:
                        if 'successfully' in cnt3:
                            self.utils.print_info("Found successfully message")
                            return True
                        else:
                            self.utils.print_info("Not found successfully message yet ")
                            return False

                save_successful = self.utils.wait_till(_check_succesful_message, silent_failure=True, delay=3)
                if save_successful:
                    kwargs['pass_msg'] = "Template has been saved successfully."
                    self.common_validation.passed(**kwargs)
                    return 1
                else:
                    kwargs['fail_msg'] = "Template failed to save"
                    self.common_validation.failed(**kwargs)
                    return -1

        if not found_save_button:
            kwargs['fail_msg'] = "Save template button has been not found "
            self.common_validation.fault(**kwargs)
            return -1

    def configure_oob_mgmt_int(self, nw_policy, sw_template_name, cli_type, mgmtVlan="4092", **kwargs):
        """
        - Checks able to configure OOB Mgmt interface
        - This function is working only if switch template already created
        - Keyword Usage
        - ``  ${NW_POLICY}  ${SW_TEMPLATE_NAME} ${MGMTVLAN}
        - e.g. configure_oob_mgmt_int bgd2 politicamea 4092
        :param nw_policy: network policy
        :param sw_template_name: Switch Template Name e.g mypolicy
        :param mgmtVlan: 4092 -vlan range need to be (1-4093)
        :param cli_type: Device CLI Type e.g., VOSS,EXOS

        :return: 1 if Switch Template OOB mgmt interface Configured Successfully else -1
        """

        self.select_sw_template(nw_policy, sw_template_name, cli_type)

        mgmt_int = self.sw_template_web_elements.get_mgmt_toggle_check_box()
        if mgmt_int:
            self.auto_actions.enable_check_box(mgmt_int)
            mgmt_vlan_field = self.sw_template_web_elements.get_mgmt_vlan_text_field()
            if mgmt_vlan_field:
                self.auto_actions.send_keys(mgmt_vlan_field, mgmtVlan)
            else:
                kwargs['fail_msg'] = "Unable to find field to enter MGMT Vlan field."
                self.common_validation.fault(**kwargs)
                return -1
        else:
            kwargs['fail_msg'] = "Unable to find check box to enable OOB mgmt connectivity"
            self.common_validation.fault(**kwargs)
            return -1

        save_btns = self.sw_template_web_elements.get_sw_template_save_button()
        for save_btn in save_btns:
            if save_btn.is_displayed():
                self.utils.print_info("Click on the save template button")
                self.auto_actions.click(save_btn)
                sleep(10)
                tool_tip_text = tool_tip.tool_tip_text
                self.utils.print_info("Tool tip Text Displayed on Page", tool_tip_text)
                for cnt3 in tool_tip_text:
                    if 'Stack template has been saved successfully.' in cnt3:
                        kwargs['pass_msg'] = "Found successfully message"
                        self.common_validation.passed(**kwargs)
                        return 1
                    else:
                        self.utils.print_info("Not found successfully message yet ")
            else:
                self.utils.print_info("Not found 'Save template' button ")

        kwargs['fail_msg'] = "Switch Template OOB mgmt interface not Configured"
        self.common_validation.failed(**kwargs)
        return -1

    def template_assign_ports_to_an_existing_port_type(self, ports, port_type_name, **kwargs):
        """
        - This keyword will assign multiple ports in a template to an existing port type
        - Assumes That Already in Device Template Port Configuration
        - Flow: Select the ports -> Assign -> Choose Existing -> Select and existing Port Type -> Save
        :param policy_name:     The name of the network policy
        :param sw_template:     The name of the switch template
        :param ports:           The port interfaces [written as 1,2,4...]
        :param port_type_name:  The existing port type name
        :return: returns 1 if the ports have been assigned the existing port type
                 returns -1 if otherwise
        """
        self.select_wireframe_net_ports(ports)
        assign_button = self.sw_template_web_elements.get_sw_template_assign_button()
        if assign_button:
            self.utils.print_info("Clicking on the Assign button...")
            self.auto_actions.click(assign_button)
            self.utils.print_info("Clicking on Choose Existing button...")
            choose_existing_port_type = self.sw_template_web_elements.existing_port_type_button()
            if choose_existing_port_type:
                self.auto_actions.click(choose_existing_port_type)
            self.utils.wait_till(self.sw_template_web_elements.port_type_list)
            existing_port_type_list = self.sw_template_web_elements.port_type_list()
            if existing_port_type_list:
                self.utils.print_info("Found the port type list!")
                for item in existing_port_type_list:
                    self.utils.print_info(item.text)
                    if port_type_name == item.text:
                        self.utils.print_info(f"Searching for the Port type option: {port_type_name}")
                        self.auto_actions.click(item)
                        self.utils.print_info("Clicking on Save Existing Port Type")
                        save_btn_existing_port_type = self.sw_template_web_elements.save_btn_existing_port()
                        if save_btn_existing_port_type:
                            self.auto_actions.click(save_btn_existing_port_type)
                            self.utils.print_info("Saved")
                            dialog_trunk_choice = self.sw_template_web_elements.\
                                get_sw_template_assign_choose_existing_trunk_choice_second_dialog_box()

                            if dialog_trunk_choice:
                                self.utils.print_info("A trunk option was chosen. Saving the current allowed/native "
                                                      "configuration fields...")
                                save_button_trunk_choice_dialog = self.sw_template_web_elements.\
                                    get_sw_template_assign_existing_trunk_choice_second_dialog_box_save_button()
                                if save_button_trunk_choice_dialog:
                                    self.utils.print_info("Clicking on the 'Save' button...")
                                    self.auto_actions.click(save_button_trunk_choice_dialog)

                                    def check_for_confirmation_trunk():
                                        tool_tip_text = self.dialogue_web_elements.get_tooltip_text()
                                        self.utils.print_info("Tool tip Text Displayed on Page: ", tool_tip_text)
                                        if tool_tip_text:
                                            return "Trunk Port has been saved successfully." in tool_tip_text
                                        else:
                                            return False

                                    confirmation_message_trunk = self.utils.wait_till(check_for_confirmation_trunk,
                                                                                      is_logging_enabled=True)[0]
                                    if confirmation_message_trunk:
                                        self.utils.print_info(f"Saved. Port Type {port_type_name} has been assigned to"
                                                              f"the ports: {ports}")
                                    else:
                                        kwargs['fail_msg'] = "Did not find the successful Trunk Port message."
                                        self.common_validation.failed(**kwargs)
                                        return -1

                                else:
                                    kwargs['fail_msg'] = "Unable to find the 'Save' button in this section!"
                                    self.common_validation.fault(**kwargs)
                                    return -1
                            else:
                                pass
                            self.utils.print_info("Attempting to locate Save Template Button")
                            save_btns = self.sw_template_web_elements.get_sw_template_save_button()
                            rc = -1
                            for save_btn in save_btns:
                                if save_btn.is_displayed():
                                    self.utils.print_info("Click on the save template button")
                                    self.auto_actions.click(save_btn)

                                    def check_for_confirmation():
                                        tool_tip_text = self.dialogue_web_elements.get_tooltip_text()
                                        self.utils.print_info("Tool tip Text Displayed on Page: ", tool_tip_text)
                                        if tool_tip_text:
                                            return "Stack template has been saved successfully." in tool_tip_text or \
                                                'Switch template has been saved successfully.' in tool_tip_text
                                        else:
                                            return False

                                    confirmation_message = self.utils.wait_till(check_for_confirmation,
                                                                                is_logging_enabled=True)[0]
                                    if confirmation_message:
                                        rc = 1
                                        kwargs['pass_msg'] = "Template has been saved successfully."
                                        self.common_validation.passed(**kwargs)
                                    else:
                                        kwargs['fail_msg'] = "Successful message not found"
                                        self.common_validation.failed(**kwargs)
                                        return -1
                                    break
                            return rc
                        else:
                            kwargs['fail_msg'] = "Did not find the save button!"
                            self.common_validation.fault(**kwargs)
                            return -1
        else:
            kwargs['fail_msg'] = "Could not find the assign button!"
            self.common_validation.fault(**kwargs)
            return -1

    def add_5520_sw_template(self, nw_policy, sw_model, sw_template_name, cli_type, save_template=True, **kwargs):
        """
        - Checks the given switch template present already in the switch Templates Grid
        - If it is not there add to the sw_template
        - This function is working only for stack
        - Keyword Usage
        - ``  ${MODEL_UNITS} ${NW_POLICY}  ${SW_MODEL}   ${SW_TEMPLATE_NAME}``
        - e.g. Add Sw Stack Template                           5520-24T-EXOS,5520-24X-EXOS,5520-48T-EXOS
           ...                             bgd2        EXOS-5520-Series-Stack          politicamea      True
        :param model_units: a string will all units e.g 5520-24T,5520-24X,5520-48T
        :param nw_policy: network policy
        :param sw_model: Switch Model  ie EXOS-5520-Series-Stack
        :param sw_template_name: Switch Template Name e.g mypolicy
        :param save_template: True - will save the template ; False - will not save the template (More configures can be added after)
        :param cli_type: Device CLI Type e.g., VOSS,EXOS

        :return: 1 if Switch Template Configured Successfully else -1
        """
        self.utils.print_info("Navigate to devices")
        self.navigator.navigate_to_devices()
        self.utils.print_info("Navigating Network Policies")
        self.navigator.navigate_configure_network_policies()
        sleep(1)

        self._set_nw_policy_if_needed()

        if self.nw_policy.select_network_policy_in_card_view(nw_policy) == -1:
            kwargs['fail_msg'] = "Not found the network policy. Make sure that it was created before"
            self.common_validation.failed(**kwargs)
            return -1

        sleep(2)

        if NetworkElementConstants.OS_EXOS in cli_type.upper() or NetworkElementConstants.OS_VOSS in cli_type.upper():
            self.utils.print_info("Click on Switching tab")
            self.auto_actions.click_reference(self.device_template_web_elements.get_policy_switching_tab)

            self.utils.print_info("Click on Switch Templates Menu Item")
            self.auto_actions.click_reference(self.device_template_web_elements.get_policy_switch_templates_tab)

        elif NetworkElementConstants.OS_AHFASTPATH in cli_type.upper():
            self.utils.print_info("Click on SR/Dell Switching tab")
            self.auto_actions.click_reference(self.device_template_web_elements.get_policy_sr_dell_switching_tab)

            self.utils.print_info("Click on Switch Templates Menu Item from SR/Dell Switching Section")
            self.auto_actions.click_reference(self.device_template_web_elements.get_policy_sr_dell_switch_templates_tab)

        if self.check_sw_template(sw_template_name):
            kwargs['fail_msg'] = f"Template with name {sw_template_name} already present in the template gri"
            self.common_validation.failed(**kwargs)
            return -1

        add_btn = self.sw_template_web_elements.get_new_sw_template_add_button()
        sleep(2)

        if add_btn:
            self.utils.print_info("Click on sw Template Add button")
            self.auto_actions.click(add_btn)
            sleep(1)

            self.utils.print_info("select the sw: ", sw_model)
            sw_list_items = self.sw_template_web_elements.get_sw_template_platform_from_drop_down()
            sleep(2)
            for el in sw_list_items:
                self.utils.print_debug("Switch template names: ", el.text.upper())
                if not el:
                    pass
                if sw_model.upper() in el.text.upper():
                    self.auto_actions.click(el)
                    break
                print(el.text)
            sleep(3)

            self.utils.print_info("Enter the switch Template Name: ", sw_template_name)
            self.auto_actions.send_keys(self.sw_template_web_elements.get_sw_template_name_textfield(),
                                        sw_template_name)
            sleep(3)
        if save_template:
            sleep(5)
            save_btns = self.sw_template_web_elements.get_sw_template_save_button()
            for save_btn in save_btns:
                if save_btn.is_displayed():
                    self.utils.print_info("Click on the save template button")
                    self.auto_actions.click(save_btn)
                    sleep(10)
                    tool_tip_text = tool_tip.tool_tip_text
                    self.utils.print_info("Tool tip Text Displayed on Page", tool_tip_text)
                    sleep(15)
                    for cnt3 in tool_tip_text:
                        if 'successfully' in cnt3:
                            kwargs['pass_msg'] = "Found successfully message"
                            self.common_validation.passed(**kwargs)
                            return 1
                        else:
                            self.utils.print_info("Not found successfully message yet ")
                else:
                    self.utils.print_info("Not found 'Save template' button ")
        else:
            kwargs['pass_msg'] = "User choose not to save the policy. More configs could be added"
            self.common_validation.passed(**kwargs)
            return 1

    def delete_switch_template_from_policy(self, nw_policy, sw_template_name, cli_type, **kwargs):
        """
        - This keyword will delete the switch template from a newtwork policy
        - Flow: Network Policies -> Edit nw_policy -> Device Templates -> Select Template -> Delete Template
        :param nw_policy: The name of the network policy
        :param sw_template_name: The name of the template
        :param cli_type: Device CLI Type e.g., VOSS,EXOS
        :return: Returns 1 if template is succesfully deleted,
                 Returns -1 if network policy not found
        """
        self.utils.print_info("Navigate to devices")
        self.navigator.navigate_to_devices()
        self.utils.print_info("Navigating Network Policies")
        self.navigator.navigate_configure_network_policies()
        if self.select_network_policy_in_card_view_using_network_web_elements(nw_policy) == -1:
            self.utils.print_info("Not found the network policy. Make sure that it was created")
            kwargs['fail_msg'] = f"Policy: {nw_policy} has not been found."
            self.common_validation.failed(**kwargs)
            return -1

        if NetworkElementConstants.OS_EXOS in cli_type.upper() or NetworkElementConstants.OS_VOSS in cli_type.upper():
            self.utils.print_info("Click on Switching tab")
            self.auto_actions.click_reference(self.device_template_web_elements.get_policy_switching_tab)

            self.utils.print_info("Click on Switch Templates Menu Item")
            self.auto_actions.click_reference(self.device_template_web_elements.get_policy_switch_templates_tab)

        elif NetworkElementConstants.OS_AHFASTPATH in cli_type.upper():
            self.utils.print_info("Click on SR/Dell Switching tab")
            self.auto_actions.click_reference(self.device_template_web_elements.get_policy_sr_dell_switching_tab)

            self.utils.print_info("Click on Switch Templates Menu Item from SR/Dell Switching Section")
            self.auto_actions.click_reference(self.device_template_web_elements.get_policy_sr_dell_switch_templates_tab)


        self.utils.print_info("Searching the template: ", sw_template_name)
        sw_templates_rows = self.sw_template_web_elements.get_sw_template_rows()
        if sw_templates_rows:
            self.utils.print_info("Found the template rows.")
            found = False
            for sw_template_row in sw_templates_rows:
                if sw_template_name in sw_template_row.text:
                    self.utils.print_info("Found the template row: ", sw_template_row.text)
                    found = True
                    self.utils.print_info("Clicking the template checkbox...")
                    self.auto_actions.click(self.sw_template_web_elements.get_sw_template_check_box_row(sw_template_row))
                    self.utils.print_info("Searching for the delete button...")
                    delete_button = self.sw_template_web_elements.get_sw_template_delete_button()
                    if delete_button:
                        self.utils.print_info("Found the delete button.")
                        self.utils.print_info("Clicking the delete button...")
                        self.auto_actions.click(delete_button)

                        def check_for_confirmation():
                            tool_tip_text = self.dialogue_web_elements.get_tooltip_text()
                            self.utils.print_info("Tool tip Text Displayed on Page: ", tool_tip_text)
                            if tool_tip_text:
                                return "Template was successfully removed from policy." in tool_tip_text
                            else:
                                return False

                        confirmation_message = self.utils.wait_till(check_for_confirmation, is_logging_enabled=True)[0]
                        if confirmation_message:
                            kwargs['pass_msg'] = "Template was successfully removed from policy."
                            self.common_validation.passed(**kwargs)
                        else:
                            kwargs['fail_msg'] = "Successful message not found"
                            self.common_validation.failed(**kwargs)
                            return -1
                    else:
                        kwargs['fail_msg'] = "Delete button hasn't been found."
                        self.common_validation.fault(**kwargs)
                        return -1
            if not found:
                kwargs['pass_msg'] = f"The template {sw_template_name} is not present here, it may have been " \
                                     "already deleted or it wasn't created."
                self.common_validation.passed(**kwargs)
                return 1
        else:
            kwargs['pass_msg'] = "There are no templates configured."
            self.common_validation.passed(**kwargs)
            return 1

    def sw_template_stack_select_slot(self, slot, **kwargs):
        """
        - Assume that already in Device Template Port Configuration
        :param slot: "The slot number that needs to be selected"
        :return: Returns 1 if slot found and clicked
                 Returns -1 if otherwise
        """
        self.utils.print_info("Gather the list of the devices in the stack")
        slot_index = 1
        slot_found = False
        complete_stack = self.sw_template_web_elements.get_complete_stack_list()
        if complete_stack:
            slots_in_stack = self.sw_template_web_elements.get_complete_stack_all_rows(complete_stack)
            if slots_in_stack:
                for stack_item in slots_in_stack:
                    if slot_index == int(slot):
                        self.utils.print_info("Slot {str(slot)} found in the stack, selecting the slot")
                        self.auto_actions.click(stack_item)
                        slot_found = True
                        kwargs['pass_msg'] = f"Slot {str(slot)} found in the stack"
                        self.common_validation.passed(**kwargs)
                        return 1
                    slot_index = slot_index + 1
                if not slot_found:
                    kwargs['fail_msg'] = f"Slot {str(slot)} not found in the stack, check the numbers of slots"
                    self.common_validation.failed(**kwargs)
                    return -1
                kwargs['fail_msg'] = f"Something went wrong with selecting the slot {str(slot)}"
                self.common_validation.failed(**kwargs)
            else:
                kwargs['fail_msg'] = "Cannot find the slot list for the stack in this template"
                self.common_validation.failed(**kwargs)
        else:
            kwargs['fail_msg'] = "Unable to gather the list of the devices in the stack"
            self.common_validation.failed(**kwargs)

    def get_sw_template_row_hyperlink(self, sw_template, **kwargs):
        """
        - Get the switch template row element hyperlink on Network Policy's Switch Templates Grid
        - Keyword Usage
        - ``Get SW Template Row  ${SW_TEMPLATE_NAME}``

        :param sw_template: name of the sw_template
        :return: Switch Template Cell present on row
        """
        self.utils.print_info("Getting the switch template rows")

        rows = self.sw_template_web_elements.get_sw_template_rows()
        if not rows:
            kwargs['fail_msg'] = "Switch templates not exists in switch device template page"
            self.common_validation.failed(**kwargs)
            return False
        for row in rows:
            cells = self.sw_template_web_elements.get_sw_template_row_table_cells(row)
            template_cell = cells[2]
            if sw_template in template_cell.text:
                hyperlink = self.sw_template_web_elements.get_sw_template_row_cells_hyperlink(template_cell)
                return hyperlink
        kwargs['fail_msg'] = "Failed to get the switch template row"
        self.common_validation.failed(**kwargs)
        return False

    def add_sw_template_from_policy_tab(self, sw_model, sw_template_name, cli_type, save_template=True, **kwargs):
        """
        This keyword add new template from policy tab
        :param sw_model: model of template
        :param sw_template_name: Name of template
        :param save_template: True is template will be save; else False
        :param cli_type: Device CLI Type e.g., VOSS,EXOS
        :return: 1 if template has been created; else -1
        """

        if NetworkElementConstants.OS_EXOS in cli_type.upper() or NetworkElementConstants.OS_VOSS in cli_type.upper():
            self.utils.print_info("Click on Switching tab")
            self.auto_actions.click_reference(self.device_template_web_elements.get_policy_switching_tab)

            self.utils.print_info("Click on Switch Templates Menu Item")
            self.auto_actions.click_reference(self.device_template_web_elements.get_policy_switch_templates_tab)

        elif NetworkElementConstants.OS_AHFASTPATH in cli_type.upper():
            self.utils.print_info("Click on SR/Dell Switching tab")
            self.auto_actions.click_reference(self.device_template_web_elements.get_policy_sr_dell_switching_tab)

            self.utils.print_info("Click on Switch Templates Menu Item from SR/Dell Switching Section")
            self.auto_actions.click_reference(self.device_template_web_elements.get_policy_sr_dell_switch_templates_tab)


        if self.check_sw_template(sw_template_name):
            kwargs['fail_msg'] = f"Template with name {sw_template_name} already present in the template grid"
            self.common_validation.failed(**kwargs)
            return -1
        add_btn = self.sw_template_web_elements.get_new_sw_template_add_button()
        if add_btn:
            self.utils.print_info("Click on sw Template Add button")
            self.auto_actions.click(add_btn)
            self.utils.print_info("select the sw: ", sw_model)
            sw_list_items = self.sw_template_web_elements.get_sw_template_platform_from_drop_down()
            for el in sw_list_items:
                self.utils.print_debug("Switch template names: ", el.text.upper())
                if not el:
                    pass
                if sw_model.upper() in el.text.upper():
                    self.auto_actions.click(el)
                    break
                print(el.text)
            self.utils.wait_till(self.sw_template_web_elements.get_sw_template_name_textfield, timeout=20, delay=1, is_logging_enabled=True)
            self.utils.print_info("Enter the switch Template Name: ", sw_template_name)
            sw_name_field = self.sw_template_web_elements.get_sw_template_name_textfield()
            if sw_name_field:
                self.utils.print_info("Enter the template name : ")
                self.auto_actions.send_keys(sw_name_field, sw_template_name)
            else:
                kwargs['fail_msg'] = "The web element for name field has not been found"
                self.common_validation.fault(**kwargs)
                return -1

        if save_template:
            save_btns = self.sw_template_web_elements.get_sw_template_save_button()
            for save_btn in save_btns:
                if save_btn.is_displayed():
                    self.utils.print_info("Click on the save template button")
                    self.auto_actions.click(save_btn)
                    tool_tip_text = tool_tip.tool_tip_text
                    self.utils.print_info("Tool tip Text Displayed on Page", tool_tip_text)
                    sleep(3)
                    for cnt3 in tool_tip_text:
                        if 'successfully' in cnt3:
                            kwargs['pass_msg'] = "Found successfully message"
                            self.common_validation.passed(**kwargs)
                            return 1
                        else:
                            self.utils.print_info("Not found successfully message yet ")
                else:
                    self.utils.print_info("Not found 'Save template' button ")
        else:
            kwargs['pass_msg'] = "User choose not to save the policy. More configs could be added"
            self.common_validation.passed(**kwargs)
            return 1

    def nav_to_template_tab(self, nw_policy, cli_type, **kwargs):
        """
        This keyword navigate to template tab from policy
        - Keyword Usage
          - ``Nav To Template Tab  ${NW_POLICY}  ${CLI_TYPE}``

        :param nw_policy: name of policy
        :param cli_type: Device CLI Type e.g., VOSS,EXOS

        :return: 1 if navigated with success; else -1
        """

        self.utils.print_info("Navigate to devices")
        self.navigator.navigate_to_devices()
        self.utils.print_info("Navigating Network Policies")
        self.navigator.navigate_configure_network_policies()

        self._set_nw_policy_if_needed()

        if self.nw_policy.select_network_policy_in_card_view(nw_policy) == -1:
            kwargs['fail_msg'] = "Not found the network policy. Make sure that it was created before"
            self.common_validation.failed(**kwargs)
            return -1

        if NetworkElementConstants.OS_EXOS in cli_type.upper() or NetworkElementConstants.OS_VOSS in cli_type.upper():
            self.utils.print_info("Click on Switching tab")
            self.auto_actions.click_reference(self.device_template_web_elements.get_policy_switching_tab)

            self.utils.print_info("Click on Switch Templates Menu Item")
            self.auto_actions.click_reference(self.device_template_web_elements.get_policy_switch_templates_tab)

        elif NetworkElementConstants.OS_AHFASTPATH in cli_type.upper():
            self.utils.print_info("Click on SR/Dell Switching tab")
            self.auto_actions.click_reference(self.device_template_web_elements.get_policy_sr_dell_switching_tab)

            self.utils.print_info("Click on Switch Templates Menu Item from SR/Dell Switching Section")
            self.auto_actions.click_reference(self.device_template_web_elements.get_policy_sr_dell_switch_templates_tab)


        kwargs['pass_msg'] = "Navigated with success"
        self.common_validation.passed(**kwargs)
        return 1

    def open_template_from_policy(self, sw_template, **kwargs):
        """
        This keyword open a template from template tab from policy

        :param sw_template: template name
        :return: 1 template is opened with success; else -1
        """
        row = self.get_sw_template_row(sw_template)
        if row:
            self.auto_actions.click(row)
            kwargs['pass_msg'] = "Template is opened with success"
            self.common_validation.passed(**kwargs)
            return 1
        kwargs['fail_msg'] = "Unable to open the template"
        self.common_validation.failed(**kwargs)
        return -1

    def generate_template_name(self,platform,serial,model, slots = ""):
        """
        This method is to generate template name based on the testbed file given
        :param platform: platform exos/voss
        :param serial: serial number
        :param model: Model number
        :return: template name for searching in list of templates
        """
        print(platform,serial,model)

        if (platform.lower() == 'stack'):
            if not slots:
                self.utils.print_error("Provide information of Slots..")
                return -1
            model_list = []
            sw_model = ""
            for eachslot in slots:

                if "SwitchEngine" in eachslot:
                    mat = re.match(r'(.*)(Engine)(\d+)(.*)', eachslot)
                    model_md = mat.group(1) + ' ' + mat.group(2) + ' ' + mat.group(3) + mat.group(4).replace('_', '-')
                    sw_model = 'Switch Engine ' + mat.group(3).split('_')[0] + '-Series-Stack'
                else:
                    model_act = eachslot.replace('10_G4', '10G4')
                    m = re.match(r'(X\d+)(G2)(\d+)(.*)', model_act)
                    model_md = mat.group(1) + ' ' + mat.group(2) + ' ' + mat.group(3) + mat.group(4).replace('_', '-')
                    sw_model = m.group(1) + '-' + m.group(2) + '-Series-Stack'
                model_list.append(model_md)
            model_units = ','.join(model_list)
            return sw_model,model_units
        elif "Engine" in model:
            mat = re.match(r'(.*)(Engine)(.*)', model)
            sw_model = mat.group(1) + ' ' + mat.group(2) + ' ' + mat.group(3).replace('_', '-')

        elif "G2" in model:
            model_act = model.replace('10_G4', '10G4')
            m = re.match(r'(X\d+)(G2)(.*)', model_act)
            sw_model = m.group(1) + '-' + m.group(2) + m.group(3).replace('_', '-')
        else:
            sw_model = model.replace('_', '-')
        return sw_model, -1


    def select_sw_template_device_config_forw_delay(self, nw_policy, sw_template, **kwargs):
        """
        - This Keyword will Select the Switch Template on Network Policy and change the forward delay time from device configuration
        - Keyword Usage
         - ``Select SW Template  ${NW_POLICY_NAME}  ${SW_TEMPLATE_NAME}``

        :param nw_policy: Name of the Network Policy to select Switch Template
        :param sw_template: Name of the sw_template
        :return: 1 If successfully Selected Switch template
        """

        self._set_nw_policy_if_needed()

        self.nw_policy.navigate_to_np_edit_tab(nw_policy)
        sleep(5)
        print("Click on Device Template tab button")
        self.auto_actions.click_reference(
            self.device_template_web_elements.get_add_device_template_menu)
        sleep(2)

        tab = self.sw_template_web_elements.get_sw_template_tab_button()
        if tab.is_displayed():
            print("Click on Switch Templates tab")
            self.auto_actions.click_reference(tab)
            sleep(2)

        print("Switch Template: " + sw_template)
        row = self.get_sw_template_row_hyperlink(sw_template)

        self.auto_actions.click(row)
        sleep(5)

        self.auto_actions.click_reference(
            self.sw_template_web_elements.get_sw_template_device_sett_forward_delay_drop_down)
        sleep(2)

        container = self.sw_template_web_elements.get_sw_template_device_sett_forward_delay_drop_down_container()
        container_val = container.text[:2]
        print(f"Default STP forward delay value in device template is {container_val}")

        self.auto_actions.click_reference(
            self.sw_template_web_elements.get_sw_template_device_sett_forward_delay_drop_down_item16)
        container = self.sw_template_web_elements.get_sw_template_device_sett_forward_delay_drop_down_container()
        container_val = container.text[:2]
        delay_container = container_val

        sleep(3)
        print("Get Template Save Button")
        save_btns = self.sw_template_web_elements.get_sw_template_save_button_adv_tab()

        for save_btn in save_btns:
            if save_btn.is_displayed():
                print("Click on the save template button")
                self.auto_actions.click(save_btn)
                sleep(10)
                break;

        sleep(3)
        print("Click on network policy exit button")
        self.auto_actions.click_reference(self.np_web_elements.get_np_exit_button)
        sleep(2)

        kwargs['pass_msg'] = f"select_sw_template_device_config_forw_delay() passed, delay container is: {delay_container}"
        self.common_validation.passed(**kwargs)

        return delay_container

    def press_upload_config_and_upgr_firm_button(self, nw_policy, sw_template, **kwargs):
        """
        - This Keyword will Select the Switch Template on Network Policy and change the forward delay time from device configuration
        - Keyword Usage
         - ``Select SW Template  ${NW_POLICY_NAME}  ${SW_TEMPLATE_NAME}``

        :param nw_policy: Name of the Network Policy to select Switch Template
        :param sw_template: Name of the sw_template
        :return: 1 If successfully Selected Switch template
        """

        self._set_nw_policy_if_needed()

        self.nw_policy.navigate_to_np_edit_tab(nw_policy)
        sleep(5)
        print("Click on Device Template tab button")
        self.auto_actions.click_reference(
            self.device_template_web_elements.get_add_device_template_menu)
        sleep(2)

        tab = self.sw_template_web_elements.get_sw_template_tab_button()
        if tab.is_displayed():
            print("Click on Switch Templates tab")
            self.auto_actions.click_reference(tab)
            sleep(2)

        print("Switch Template: " + sw_template)
        row = self.get_sw_template_row_hyperlink(sw_template)

        self.auto_actions.click(row)
        sleep(5)

        print(" Go to the advanced settings tab ")

        ok = 1
        if self.auto_actions.click_reference(
                self.sw_template_web_elements.get_sw_template_adv_settings_tab) == -1:
            print("Unable to click on Verify adanced settings button")
            ok = 0
        else:
            print("Click on Verify adanced settings button")

        if ok != 1:
            kwargs['fail_msg'] = "'press_upload_config_and_upgr_firm_button()' failed. Unable to click on Verify adanced settings button"
            self.common_validation.failed(**kwargs)

        self.auto_actions.click_reference(
            self.sw_template_web_elements.get_sw_template_adv_settings_tab)

        sleep(2)

        print("Click on Upgrade device firmware upon device authentication button")
        self.auto_actions.click_reference(
            self.sw_template_web_elements.get_sw_template_adv_settings_upgrade_device_on_off_button)

        print("Click on upload configuration button")
        self.auto_actions.click_reference(
            self.sw_template_web_elements.get_sw_template_adv_settings_upload_configuration_on_off_button)

        sleep(3)

        print("Get Template Save Button")
        save_btns = self.sw_template_web_elements.get_sw_template_save_button_adv_tab()

        for save_btn in save_btns:
            if save_btn.is_displayed():
                print("Click on the save template button")
                self.auto_actions.click(save_btn)
                sleep(10)

                break;
        sleep(3)
        print("Click on network policy exit button")
        self.auto_actions.click_reference(self.np_web_elements.get_np_exit_button)

        sleep(2)

        kwargs['pass_msg'] = "'press_upload_config_and_upgr_firm_button()' successful"
        self.common_validation.passed(**kwargs)
        return 1

    def get_latest_firmware_version_from_switch_template(self, sw_model, **kwargs):
        '''
        Return the latest image version present in create switch template option

        :param sw_model: the model of the switch passed in the swith template format
        :return: the latest image availabe in the create swith template advanced settings tab
        '''
        self.navigator.navigate_to_switch_templates()
        add_button = self.device_template_web_elements.get_switch_template_add_button()
        if not add_button:
            kwargs["fail_msg"] = "Unable to locate add button"
            self.common_validation.fault(**kwargs)
            return -1
        self.auto_actions.click_reference(self.device_template_web_elements.get_switch_template_add_button)

        self.utils.print_info("Enter " + sw_model + " into filter text field")
        device_switch_filter_text = self.device_template_web_elements.get_device_switch_template_menue_filter()
        if not device_switch_filter_text:
            kwargs["fail_msg"] = "Unable to locate filter text field"
            self.common_validation.fault(**kwargs)
            return -1
        self.auto_actions.send_keys(device_switch_filter_text, sw_model)
        sleep(4)

        self.utils.print_info("Select " + sw_model + "from the model list")
        device_switch_template_list = self.device_template_web_elements.get_switch_template_platform_from_drop_down()

        for dev_sw_templ in device_switch_template_list:
            self.auto_actions.click(dev_sw_templ)

        self.auto_actions.click_reference(self.sw_template_web_elements.get_sw_template_adv_settings_tab)
        self.auto_actions.click_reference(self.sw_template_web_elements.get_sw_template_adv_settings_upgrade_device_on_off_button)
        self.auto_actions.click_reference(self.sw_template_web_elements.get_sw_template_adv_settings_upgr_firm_specific_button)
        self.auto_actions.click_reference(self.sw_template_web_elements.get_sw_template_adv_settings_download_specific_firmware_drop_down_button)


        # Get all the images from drop down list
        specific_firmware_items = self.sw_template_web_elements.get_sw_template_adv_settings_download_specific_firmware_drop_down_items()
        sleep(2)

        arm_templ = re.compile(r"Switch\sEngine\s(5320|5420|5520)")
        x_templ = re.compile(r"X4[3-6]0-G2")
        lite_templ = re.compile(r"X435")
        onie_templ = re.compile(r"(X465|Switch\sEngine\s5720)")

        img_pattern = ""
        if arm_templ.match(sw_model) is not None:
            prefix = "_arm"
        elif x_templ.match(sw_model) is not None:
            prefix = "X"
        elif lite_templ.match(sw_model) is not None:
            prefix = "lite"
        elif onie_templ.match(sw_model) is not None:
            img_pattern = r"onie-.*\.x86_64.xos"
        else:
            kwargs['fail_msg'] = f"'select_specific_firmware_version()' failed. Switch model {sw_model} is invalidd"
            self.common_validation.fault(**kwargs)

        if img_pattern == "":
            img_pattern = f"summit{prefix}" + r"-.*\.xos"

        if specific_firmware_items is None:
            kwargs['fail_msg'] = "'select_specific_firmware_version()' failed. No images present in drop down list"
            self.common_validation.fault(**kwargs)

        latest_image_version = specific_firmware_items[-1].text

        image_versions = []
        pattern = re.compile(img_pattern)
        for version in specific_firmware_items:
            if pattern.match(version.text) is not None:
                image_versions.append(version.text)
        if pattern.match(latest_image_version) is None:
            kwargs[
                'fail_msg'] = f"'get_latest_firmware_version()' failed. Image {latest_image_version} doesn't correspond with current template"
            self.common_validation.fault(**kwargs)

        return latest_image_version.strip(), image_versions

    def select_specific_firmware_version(self, sw_model, current_image_version=None, select_current=False, **kwargs):
        """
        - Select a specific image from the Upgrade firmware menu in Switch Template advanced configuration tab and check that
        all the present images are valid images for the give dut

        :param select_current:
        :param sw_model: the model of the switch. Eg
        :param current_image_version: the current image version
        :return: If the selection was successful
        """
        print("Click on upgrade to the specific device firmware version drop down")

        # Expand on drop down list
        self.auto_actions.click_reference(
            self.sw_template_web_elements.get_sw_template_adv_settings_download_specific_firmware_drop_down_button)

        # Get all the images from drop down list
        specific_firmware_items = self.sw_template_web_elements.get_sw_template_adv_settings_download_specific_firmware_drop_down_items()
        sleep(2)

        arm_templ = re.compile(r"Switch\sEngine\s(5320|5420|5520)")
        x_templ = re.compile(r"X4[3-6]0-G2")
        lite_templ = re.compile(r"X435")
        onie_templ = re.compile(r"(X465|Switch\sEngine\s5720)")
        prefix = ""
        img_pattern = ""
        if arm_templ.match(sw_model) is not None:
            prefix = "_arm"
        elif x_templ.match(sw_model) is not None:
            prefix = "X"
        elif lite_templ.match(sw_model) is not None:
            prefix = "lite"
        elif onie_templ.match(sw_model) is not None:
            img_pattern = r"onie-.*\.x86_64.xos"
        else:
            kwargs['fail_msg'] = f"'select_specific_firmware_version()' failed. Switch model {sw_model} is invalid."
            self.common_validation.fault(**kwargs)

        if img_pattern == "":
            img_pattern = f"summit{prefix}" + r"-.*\.xos"

        if specific_firmware_items is None:
            kwargs['fail_msg'] = "'select_specific_firmware_version()' failed. No images present in drop down list"
            self.common_validation.fault(**kwargs)

        this_image_version = ''
        for item in specific_firmware_items:
            # Verify if all images are exos valid
            pattern = re.compile(img_pattern)

            if pattern.match(item.text) is None:
                kwargs['fail_msg'] = f"'select_specific_firmware_version()' failed. Image {item.text} doesn't correspond with current template"
                self.common_validation.fault(**kwargs)

            if current_image_version:
                if select_current:
                    if current_image_version in item.text:
                        this_image_version = item
                        print(f"Image {item.text} was selected")
                        break
                else:
                    if current_image_version not in item.text:
                        this_image_version = item
                        print(f"Image {item.text} was selected")
                        break

        if current_image_version and this_image_version != '':
            print("Selected image version is:" + str(this_image_version.text))
            self.auto_actions.click(this_image_version)
        elif len(specific_firmware_items) > 0:
            self.auto_actions.click_reference(specific_firmware_items[0])
        else:
            kwargs[
                'fail_msg'] = "'select_specific_firmware_version()' failed. No images present in drop down liste"
            self.common_validation.fault(**kwargs)

        kwargs['pass_msg'] = f"Selected firmware version is: {this_image_version}"
        self.common_validation.passed(**kwargs)

        return True

    def create_switching_network(self, policy, switch_profile, **kwargs):
        """
        - Configure switching template options
        :param policy: name of the policy to create
        :param switch_profile: used to get options for configuring switching template
        :return: 1 if exists else -1
        """
        sw_template_name = switch_profile.get('switch_template_name')
        if not sw_template_name:
            self.utils.print_info()
            kwargs["fail_msg"] = "Template name required...Unable to continue"
            self.common_validation.fault(**kwargs)
            return -1

        return_value = self.create_new_switch_template(switch_profile)
        if return_value == -1:
            kwargs["fail_msg"] = "Unable to create new switch template"
            self.common_validation.fault(**kwargs)
            return -1

        return_value = self.select_or_create_port_type(policy, sw_template_name, switch_profile, **kwargs)
        if return_value == -1:
            kwargs["fail_msg"] = "Unable to complete configuration of switch template"
            self.common_validation.failed(**kwargs)
            return -1

        self.utils.print_info("Save switch template")
        self.auto_actions.click_reference(self.sw_template_web_elements.get_sw_template_save_button_adv_tab)
        kwargs["pass_msg"] = "Configuring switching template options complete"
        self.common_validation.passed(**kwargs)
        return 1

    def select_network_policy_in_card_view_using_network_web_elements(self, policy_name):
        """
        - Selects the existing network polices card view

        :param policy_name: name of the policy to search
        :return: 1 if exists else -1
        """

        self.utils.print_info("Selecting Network Policy: ", policy_name)

        self.utils.print_info("Click on Network Policy card view button")
        self.auto_actions.click_reference(self.np_web_elements.get_network_policy_card_view)
        policy_cards, _ = self.utils.wait_till(
            func=self.np_web_elements.get_network_policy_card_items, delay=10)
        for policy_card in policy_cards:
            if policy_name.upper() in policy_card.text.upper():
                self.utils.print_info(policy_card.text)
                self.auto_actions.click(self.np_web_elements.get_network_policy_card_item_edit_icon(policy_card))
                sleep(4)
                return 1
        return -1

    def select_or_create_port_type(self, nw_policy, sw_template, cli_type, switch_profile, **kwargs):
        """
        - Assume that already on the Switch Template
        - Keyword Usage
          - ``select_or_create_port_type  ${NW_POLICY}  ${SW_TEMPLATE}  ${CLI_TYPE}  ${SWITCH_PROFILE}``

            :return: Returns 1 if successfully navigates to the Port Configuration Tab
                     Else returns -1
        """
        combo_selected = -1
        port_details_dictionary = switch_profile.get('port_details')
        port_details_interface_value = port_details_dictionary.get('interface')
        port_details_port_type = port_details_dictionary.get('port_type')
        port_name_and_usage_dictionary = port_details_port_type.get('port_name_and_usage')
        port_details_port_type_name_value = port_name_and_usage_dictionary.get('name')

        self.utils.print_info("Navigate to  Network Policies menu")
        self.navigator.navigate_configure_network_policies()
        self.select_network_policy_in_card_view_using_network_web_elements(nw_policy)
        self.utils.wait_till(self.device_template_web_elements.get_add_device_template_menu)

        if NetworkElementConstants.OS_EXOS in cli_type.upper() or NetworkElementConstants.OS_VOSS in cli_type.upper():
            self.utils.print_info("Click on Switching tab")
            self.auto_actions.click_reference(self.device_template_web_elements.get_policy_switching_tab)

            self.utils.print_info("Click on Switch Templates Menu Item")
            self.auto_actions.click_reference(self.device_template_web_elements.get_policy_switch_templates_tab)

        elif NetworkElementConstants.OS_AHFASTPATH in cli_type.upper():
            self.utils.print_info("Click on SR/Dell Switching tab")
            self.auto_actions.click_reference(self.device_template_web_elements.get_policy_sr_dell_switching_tab)

            self.utils.print_info("Click on Switch Templates Menu Item from SR/Dell Switching Section")
            self.auto_actions.click_reference(self.device_template_web_elements.get_policy_sr_dell_switch_templates_tab)

        self.utils.wait_till(self.sw_template_web_elements.get_sw_template_port_details_interface_all_rows)

        h_link = self.get_sw_template_row_hyperlink(sw_template)
        self.auto_actions.click(h_link)

        self.utils.print_info("Click on Port Configuration tab")
        port_configuration = self.sw_template_web_elements.port_config_template()
        if port_configuration:
            self.utils.print_info("The Port Configuration button was found")
            self.auto_actions.click_reference(self.sw_template_web_elements.port_config_template)
            self.utils.wait_till(self.sw_template_web_elements.get_sw_template_port_details_interface_all_rows)

        self.utils.print_info("Select port type " + port_details_port_type_name_value + " from list of port types")
        combo_selected = self._select_port_type(port_details_interface_value, port_details_port_type_name_value)
        if combo_selected != 1:
            self.utils.print_info("Port type " + port_details_port_type_name_value + " not found")
            self.utils.print_info("Attempting to create new Port type " + port_details_port_type_name_value)
            created = self.create_new_port_type(port_details_interface_value, port_details_port_type_name_value, switch_profile)
            if created == 1:
                self.utils.print_info("Make another attempt to select port type " + port_details_port_type_name_value + " from list of port types")
                combo_selected = self._select_port_type(port_details_interface_value, port_details_port_type_name_value)

        return combo_selected

    def _select_port_type(self, port_details_interface_value, port_details_port_type_value):
        """
        - Assume that already on the Switch Template (Port Configuration)
            :return: Returns 1 if successfully navigates to the Port Details Tab
                     Else returns -1
        """
        if port_details_port_type_value and port_details_interface_value:
            list_of_interface_elements = self.sw_template_web_elements.get_sw_template_port_details_interface_all_rows()
            if list_of_interface_elements:
                int_index = -1
                for an_interface_element in list_of_interface_elements:
                    int_index = int_index + 1
                    a_port_string = self.sw_template_web_elements.get_sw_template_port_details_row_interface_value(an_interface_element)
                    if a_port_string.text == port_details_interface_value:
                        port_type_element = self.sw_template_web_elements.get_sw_template_port_details_row_combo(an_interface_element)
                        self.auto_actions.click(port_type_element[int_index])
                        combo_box_value_elements = self.sw_template_web_elements.get_sw_template_port_details_row_port_type_list()
                        for a_combo_element in combo_box_value_elements:
                            if a_combo_element.text == port_details_port_type_value:
                                self.auto_actions.click(a_combo_element)
                                return 1
        return -1

    def create_new_port_type(self, port_details_interface_value, port_details_port_type_value, switch_profile, **kwargs):
        """
        - Assume that already on the Switch Template (Port Configuration)
            :return: Returns 1 if successfully navigates to the Port Details Tab
                     Else returns -1
        """

        self.utils.print_info("Open port type pop up dialog")
        results = self.open_port_type_pop_up(port_details_interface_value, port_details_port_type_value, switch_profile)
        if results == -1:
            kwargs["fail_msg"] = "Unable to configure new port type"
            self.common_validation.failed(**kwargs)
            return -1

        self.utils.print_info("Processing Port Name and Usage tab")
        self.create_new_port_type_port_name_and_usage(port_details_interface_value, port_details_port_type_value, switch_profile)

        self.auto_actions.click_reference(self.sw_template_web_elements.get_sw_template_port_details_port_type_editor_next)
        new_port_type_saved = False
        prevent_infinite_loop = 10

        active_tab = self._get_active_port_type_tab()

        while not new_port_type_saved and prevent_infinite_loop > 0:
            prevent_infinite_loop = prevent_infinite_loop - 1
            # process tab
            if active_tab == 'unknown':
                self.utils.print_info("Unable to process current tab")
            if active_tab == 'port_name_and_usage':
                self.utils.print_info("Processing the Port Name and Usage tab has already been completed")
            if active_tab == 'transmission_settings':
                self.utils.print_info("Processing the Transmission Settings tab")
                self.create_new_port_type_transmission_settings(port_details_interface_value,
                                                              port_details_port_type_value, switch_profile)
            if active_tab == 'storm_control':
                self.utils.print_info("Processing the Storm Control tab")
                self.create_new_port_type_storm_control(port_details_interface_value,
                                                                port_details_port_type_value, switch_profile)
            if active_tab == 'vlan':
                self.utils.print_info("Processing the Vlan tab")
                self.create_new_port_type_vlan(port_details_interface_value,
                                                        port_details_port_type_value, switch_profile)
            if active_tab == 'stp':
                self.utils.print_info("Processing the STP tab")
                self.create_new_port_type_stp(port_details_interface_value,
                                                        port_details_port_type_value, switch_profile)
            if active_tab == 'summary':
                self.utils.print_info("Processing the Summary tab")
                self.utils.print_info("Saving New Port Type")
                self.auto_actions.click_reference(self.sw_template_web_elements.get_sw_template_port_details_port_type_editor_save)
                new_port_type_saved = True

            if not new_port_type_saved:
                self.auto_actions.click_reference(self.sw_template_web_elements.get_sw_template_port_details_port_type_editor_next)
                sleep(2)
                active_tab = self._get_active_port_type_tab()

        if new_port_type_saved:
            kwargs["pass_msg"] = "Successfully configured new port type"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs["fail_msg"] = "Unable to configure new port type"
            self.common_validation.failed(**kwargs)
            return -1

    def create_new_switch_template(self, wireless_network_conf, cli_type, **kwargs):
        """
        - Assume that the network policy has already been selected
        - Keyword Usage
          - ``select_or_create_port_type  ${NW_POLICY_DIC}  ${CLI_TYPE}``

        ${NW_POLICY}
            :param wireless_network_conf: Dictionary contains information needed to configure templates
            :param cli_type: Device CLI Type e.g., VOSS,EXOS
            :return: Returns 1 if configuration is successful
                     Else Returns -1
        """
        device_model = wireless_network_conf.get('device_model')
        switch_template_name = wireless_network_conf.get('switch_template_name')

        if NetworkElementConstants.OS_EXOS in cli_type.upper() or NetworkElementConstants.OS_VOSS in cli_type.upper():
            self.utils.print_info("Click on Switching tab")
            self.auto_actions.click_reference(self.device_template_web_elements.get_policy_switching_tab)

            self.utils.print_info("Click on Switch Templates Menu Item")
            self.auto_actions.click_reference(self.device_template_web_elements.get_policy_switch_templates_tab)

        elif NetworkElementConstants.OS_AHFASTPATH in cli_type.upper():
            self.utils.print_info("Click on SR/Dell Switching tab")
            self.auto_actions.click_reference(self.device_template_web_elements.get_policy_sr_dell_switching_tab)

            self.utils.print_info("Click on Switch Templates Menu Item from SR/Dell Switching Section")
            self.auto_actions.click_reference(self.device_template_web_elements.get_policy_sr_dell_switch_templates_tab)

        self.utils.print_info("Click on Select button/drop down")
        select_button = self.sw_template_web_elements.get_device_switch_select_button()
        if not select_button:
            kwargs["fail_msg"] = "Unable to locate select button"
            self.common_validation.fault(**kwargs)
            return -1
        self.auto_actions.click_reference(self.sw_template_web_elements.get_device_switch_select_button)

        self.utils.print_info("Enter " + switch_template_name + " into the Search text field")
        filter_text = self.sw_template_web_elements.get_sw_template_selection_search_textfield()
        if not filter_text:
            kwargs["fail_msg"] = "Unable to locate the search text field"
            self.common_validation.fault(**kwargs)
            return -1
        self.auto_actions.send_keys(filter_text, switch_template_name)

        self.utils.print_info("Click on Search button")
        search_button = self.sw_template_web_elements.get_sw_template_selection_search_button()
        if not search_button:
            kwargs["fail_msg"] = "Unable to locate search button"
            self.common_validation.fault(**kwargs)
            return -1
        self.auto_actions.click_reference(self.sw_template_web_elements.get_sw_template_selection_search_button)

        self.utils.print_info("Attempting to locate Device Template table")
        search_table = self.sw_template_web_elements.get_sw_template_selection_grid()
        if not search_table:
            kwargs["fail_msg"] = "Unable to locate table"
            self.common_validation.fault(**kwargs)
            self.auto_actions.click_reference(self.sw_template_web_elements.get_sw_template_selection_cancel_button)
            return -1

        self.utils.print_info("Verify that switch template " +  switch_template_name + " does not exist")
        search_table_rows = self.sw_template_web_elements.get_sw_template_table_rows(search_table)
        if search_table_rows:
            kwargs["fail_msg"] = "Switch template already exist"
            self.common_validation.failed(**kwargs)
            self.auto_actions.click(search_table_rows)
            return -1

        self.utils.print_info("Switch template does NOT exist")
        self.utils.print_info("Close Device Template Pop-up Window")
        self.auto_actions.click_reference(self.sw_template_web_elements.get_sw_template_selection_cancel_button)

        self.utils.print_info("Clicking Add button")
        add_button = self.device_template_web_elements.get_switch_template_add_button()
        if not add_button:
            kwargs["fail_msg"] = "Unable to locate add button"
            self.common_validation.fault(**kwargs)
            return -1
        self.auto_actions.click_reference(self.device_template_web_elements.get_switch_template_add_button)

        self.utils.print_info("Enter " + device_model + " into filter text field")
        device_switch_filter_text = self.device_template_web_elements.get_device_switch_template_menue_filter()
        if not device_switch_filter_text:
            kwargs["fail_msg"] = "Unable to locate filter text field"
            self.common_validation.fault(**kwargs)
            return -1
        self.auto_actions.send_keys(device_switch_filter_text, device_model)
        sleep(4)

        self.utils.print_info("Select " + device_model + "from the model list")
        device_switch_template_list = self.device_template_web_elements.get_switch_template_platform_from_drop_down()
        if not device_switch_template_list:
            kwargs["fail_msg"] = "Unable to get switch template list"
            self.common_validation.failed(**kwargs)
            return -1
        sleep(4)
        for dev_sw_templ in device_switch_template_list:
            self.auto_actions.click(dev_sw_templ)

        self.utils.print_info("Enter " + switch_template_name + " into the name field")
        switch_template_name_field = self.sw_template_web_elements.get_sw_template_adv_tab_textfield()
        if not switch_template_name_field:
            kwargs["fail_msg"] = "Unable to locate filter text field"
            self.common_validation.fault(**kwargs)
            return -1
        self.auto_actions.send_keys(switch_template_name_field, switch_template_name)

        result = self.configure_switch_template_spanning_tree(wireless_network_conf)
        if result == -1:
            kwargs["fail_msg"] = "Unable to configure spanning tree values"
            self.common_validation.failed(**kwargs)
            return -1

        result = self.configure_switch_igmp_setting(wireless_network_conf)
        if result == -1:
            kwargs["fail_msg"] = "Unable to configure igmp values"
            self.common_validation.failed(**kwargs)
            return -1

        result = self.configure_switch_template_mtu_setting(wireless_network_conf)
        if result == -1:
            kwargs["fail_msg"] = "Unable to configure mtu values"
            self.common_validation.failed(**kwargs)
            return -1

        self.utils.print_info("Save switch template")
        self.auto_actions.click_reference(self.sw_template_web_elements.get_sw_template_save_button_adv_tab)
        kwargs["pass_msg"] = "Switch template has been saved"
        self.common_validation.passed(**kwargs)
        return 1

    def configure_switch_template_spanning_tree(self, wireless_network_conf, **kwargs):
        """
        - Assume that the network policy has already been selected
            :param wireless_network_conf: Dictionary contains information needed to configure templates
            :return: Returns 1 if configuration is successful
                     Else Returns -1
        """
        # Commented on 1/18/23 because it is unused
        # device_model = wireless_network_conf.get('device_model')
        # switch_template_name = wireless_network_conf.get('switch_template_name')

        # spanning tree
        spanning_dictionary = wireless_network_conf.get('stp_config')
        if not spanning_dictionary:
            kwargs["pass_msg"] = "No spanning data in the dictionary"
            self.common_validation.passed(**kwargs)
            return 1

        span_tree_mode_value = spanning_dictionary.get('stp_mode')

        span_tree_mode_web_element = self.sw_template_web_elements.get_sw_template_enable_spanningtree()
        if not span_tree_mode_web_element:
            kwargs["fail_msg"] = "Unable to locate spanning tree mode button"
            self.common_validation.fault(**kwargs)
            return -1

        if span_tree_mode_value.lower() == 'on' and not span_tree_mode_web_element.is_selected():
            self.utils.print_info("Turning spanning tree mode ON")
            self.auto_actions.click_reference(self.sw_template_web_elements.get_sw_template_enable_spanningtree)

        if span_tree_mode_value.lower() == 'off' and span_tree_mode_web_element.is_selected():
            self.utils.print_info("Turning spanning tree mode OFF")
            self.auto_actions.click_reference(self.sw_template_web_elements.get_sw_template_enable_spanningtree)

        if span_tree_mode_web_element.is_selected():
            span_tree_protocol_value = ''
            span_tree_bridge_priority_value = ''
            span_tree_forward_delay_value = ''
            span_tree_max_age_value = ''

            span_tree_protocol_value = spanning_dictionary.get('stp_protocol')

            if span_tree_protocol_value:
                self.utils.print_info("Configuring Spanning Tree Protocol options")
                if span_tree_protocol_value.lower() == 'stp':
                    self.utils.print_info("Selecting STP option button")
                    stp_web_element = self.sw_template_web_elements.get_sw_template_enable_stp()
                    if not stp_web_element:
                        kwargs["fail_msg"] = "Unable to locate spanning tree protocol STP option button"
                        self.common_validation.fault(**kwargs)
                        return -1
                    self.auto_actions.click_reference(self.sw_template_web_elements.get_sw_template_enable_stp)

                if span_tree_protocol_value.lower() == 'rstp':
                    self.utils.print_info("Selecting RSTP(Rapid STP) option button")
                    stp_web_element = self.sw_template_web_elements.get_sw_template_enable_rstp()
                    if not stp_web_element:
                        kwargs["fail_msg"] = "Unable to locate spanning tree protocol RSTP option button"
                        self.common_validation.fault(**kwargs)
                        return -1
                    self.auto_actions.click_reference(self.sw_template_web_elements.get_sw_template_enable_rstp)

                if span_tree_protocol_value.lower() == 'mstp':
                    self.utils.print_info("Selecting MSTP(Multiple STP) option button")
                    stp_web_element = self.sw_template_web_elements.get_sw_template_enable_mstp()
                    if not stp_web_element:
                        kwargs["fail_msg"] = "Unable to locate spanning tree protocol MSTP option button"
                        self.common_validation.fault(**kwargs)
                        return -1
                    self.auto_actions.click_reference(self.sw_template_web_elements.get_sw_template_enable_mstp)

            span_tree_bridge_priority_value = spanning_dictionary.get('stp_bridge_priority')
            if span_tree_bridge_priority_value:
                span_tree_bridge_priority_element = self.sw_template_web_elements.priority_dropdown()
                if not span_tree_bridge_priority_element:
                    kwargs["fail_msg"] = "Unable to locate spanning tree priority option drop down"
                    self.common_validation.fault(**kwargs)
                    return -1
                self.auto_actions.click(span_tree_bridge_priority_element)
                span_tree_bridge_priority_element_container = self.sw_template_web_elements.get_priority_items_select_container()
                span_tree_bridge_priority_element_list = self.sw_template_web_elements.priority_items(span_tree_bridge_priority_element_container)

                for priority_option in span_tree_bridge_priority_element_list:
                    if priority_option.text == span_tree_bridge_priority_value:
                        self.auto_actions.click(priority_option)
                        break

            span_tree_forward_delay_value = spanning_dictionary.get('stp_forward_delay')
            if span_tree_forward_delay_value:
                span_tree_forward_delay_element = self.sw_template_web_elements.get_sw_template_device_sett_forward_delay_drop_down_items()
                if not span_tree_forward_delay_element:
                    kwargs["fail_msg"] = "Unable to locate spanning tree forward delay drop down"
                    self.common_validation.fault(**kwargs)
                    return -1
                self.auto_actions.click(span_tree_forward_delay_element)
                span_tree_forward_delay_container = self.sw_template_web_elements.get_sw_template_device_sett_forward_delay_drop_down_items_container()
                span_tree_forward_delay_element_all_items = self.sw_template_web_elements.get_sw_template_device_sett_forward_delay_drop_down_items_all_items(span_tree_forward_delay_container)

                for span_tree_forward_delay_option in span_tree_forward_delay_element_all_items:
                    if span_tree_forward_delay_option.get_attribute('textContent') == span_tree_forward_delay_value:
                        self.auto_actions.click(span_tree_forward_delay_option)
                        break

            span_tree_max_age_value = spanning_dictionary.get('stp_max_age')
            if span_tree_max_age_value:
                span_tree_max_age_element = self.sw_template_web_elements.get_sw_template_device_max_age_drop_down_items()
                if not span_tree_max_age_element:
                    kwargs["fail_msg"] = "Unable to locate spanning tree max age drop down"
                    self.common_validation.fault(**kwargs)
                    return -1
                self.auto_actions.click(span_tree_max_age_element)
                span_tree_max_age_container = self.sw_template_web_elements.get_sw_template_device_max_age_delay_items_container()
                span_tree_max_age_element_all_items = self.sw_template_web_elements.get_sw_template_device_max_age_drop_down_all_items(span_tree_max_age_container)

                for span_tree_max_age_option in span_tree_max_age_element_all_items:
                    if span_tree_max_age_option.get_attribute('textContent') == span_tree_max_age_value:
                        self.auto_actions.click(span_tree_max_age_option)
                        break

        kwargs["pass_msg"] = "Spanning tree configuration was successful"
        self.common_validation.passed(**kwargs)
        return 1

    def configure_switch_igmp_setting(self, wireless_network_conf, **kwargs):
        """
        - Assume that the network policy has already been selected
            :param wireless_network_conf: Dictionary contains information needed to configure templates
            :return: Returns 1 if configuration is successful
                     Else Returns -1
        """

        igmp_dictionary = wireless_network_conf.get('igmp_setting')
        if not igmp_dictionary:
            kwargs["pass_msg"] = "No igmp data in the dictionary"
            self.common_validation.passed(**kwargs)
            return 1

        igmp_snooping_value = igmp_dictionary.get('igmp_snooping')
        enable_immediate_leave_value = igmp_dictionary.get('enable_immediate_leave')
        supress_redundant_value = igmp_dictionary.get('supress_redundant')

        igmp_snooping_value_element = self.sw_template_web_elements.get_switch_template_device_configuration_igmp_settings()
        if not igmp_snooping_value_element:
            kwargs["fail_msg"] = "Unable to locate IGMP mode button"
            self.common_validation.fault(**kwargs)
            return -1

        self.utils.print_info("Configuring IGMP Settings")
        if igmp_snooping_value.lower() == 'on' and not igmp_snooping_value_element.is_selected():
            self.utils.print_info("Turning igmp snooping ON")
            self.auto_actions.click_reference(self.sw_template_web_elements.get_switch_template_device_configuration_igmp_settings)

        if igmp_snooping_value.lower() == 'off' and igmp_snooping_value_element.is_selected():
            self.utils.print_info("Turning igmp snooping OFF")
            self.auto_actions.click_reference(self.sw_template_web_elements.get_switch_template_device_configuration_igmp_settings)

        if igmp_snooping_value_element.is_selected():

            if enable_immediate_leave_value:
                enable_immediate_leave_element = self.sw_template_web_elements.get_switch_template_device_configuration_igmp_immediate_leave()
                if not enable_immediate_leave_element:
                    kwargs["fail_msg"] = "Unable to locate igmp immediate leave option button"
                    self.common_validation.fault(**kwargs)
                    return -1
                if enable_immediate_leave_value.lower() == 'enable' and not enable_immediate_leave_element.is_selected():
                    self.utils.print_info("Enabling IGMP Immediate Leave")
                    self.auto_actions.click_reference(self.sw_template_web_elements.get_switch_template_device_configuration_igmp_immediate_leave)
                if enable_immediate_leave_value.lower() != 'enable' and enable_immediate_leave_element.is_selected():
                    self.utils.print_info("Disabling IGMP Immediate Leave")
                    self.auto_actions.click_reference(self.sw_template_web_elements.get_switch_template_device_configuration_igmp_immediate_leave)

            if supress_redundant_value:
                supress_redundant_value_element = self.sw_template_web_elements.get_switch_template_device_configuration_igmp_suppress_independent()
                if not supress_redundant_value_element:
                    kwargs["fail_msg"] = "Unable to locate igmp suppress independent option button"
                    self.common_validation.fault(**kwargs)
                    return -1
                if supress_redundant_value == 'enable' and not supress_redundant_value_element.is_selected():
                    self.utils.print_info("Enabling IGMP Suppress Independent Membership")
                    self.auto_actions.click_reference(self.sw_template_web_elements.get_switch_template_device_configuration_igmp_suppress_independent)
                if supress_redundant_value != 'enable' and supress_redundant_value_element.is_selected():
                    self.utils.print_info("Disabling IGMP Suppress Independent Membership")
                    self.auto_actions.click_reference(self.sw_template_web_elements.get_switch_template_device_configuration_igmp_suppress_independent)

        kwargs["pass_msg"] = "Configuration of IGMP setting complete"
        self.common_validation.passed(**kwargs)
        return 1

    def configure_switch_template_mtu_setting(self, wireless_network_conf, **kwargs):
        """
        - Assume that the network policy has already been selected
            :param wireless_network_conf: Dictionary contains information needed to configure templates
            :return: Returns 1 if configuration is successful
                     Else Returns -1
        """

        mtu_value = wireless_network_conf.get('mtu')
        if mtu_value:
            self.utils.print_info("Configuring MTU Values")

        if mtu_value == '1522':
            mtu_element = self.sw_template_web_elements.get_switch_template_device_configuration_mtu_1522()
            if not mtu_element:
                kwargs["fail_msg"] = "Unable to locate MTU 1522 radio button"
                self.common_validation.fault(**kwargs)
                return -1
            self.auto_actions.click_reference(self.sw_template_web_elements.get_switch_template_device_configuration_mtu_1522)

        if mtu_value == '1950':
            mtu_element = self.sw_template_web_elements.get_switch_template_device_configuration_mtu_1950()
            if not mtu_element:
                kwargs["fail_msg"] = "Unable to locate MTU 1950 radio button"
                self.common_validation.fault(**kwargs)
                return -1
            self.auto_actions.click_reference(self.sw_template_web_elements.get_switch_template_device_configuration_mtu_1950)

        if mtu_value == '9600':
            mtu_element = self.sw_template_web_elements.get_switch_template_device_configuration_mtu_9600()
            if not mtu_element:
                kwargs["fail_msg"] = "Unable to locate MTU 9600 radio button"
                self.common_validation.fault(**kwargs)
                return -1
            self.auto_actions.click_reference(self.sw_template_web_elements.get_switch_template_device_configuration_mtu_9600)

        return 1

    def open_port_type_pop_up(self, port_details_interface_value, port_details_port_type_value, switch_profile, **kwargs):
        """
        - Assume that already on the Switch Template (Port Configuration)
            :return: Returns 1 if successfully navigates to the Port Details Tab
                     Else returns -1
        """
        if port_details_port_type_value and port_details_interface_value:
            list_of_interface_elements = self.sw_template_web_elements.get_sw_template_port_details_interface_all_rows()
            if list_of_interface_elements:
                for an_interface_element in list_of_interface_elements:
                    a_port_string = self.sw_template_web_elements.get_sw_template_port_details_row_interface_value(an_interface_element)
                    if a_port_string.text == port_details_interface_value:
                        add_button = self.sw_template_web_elements.get_port_details_row_add_button(an_interface_element)
                        self.auto_actions.click(add_button)
                        sleep(4)
                        kwargs["pass_msg"] = "Configuration of IGMP setting complete"
                        self.common_validation.passed(**kwargs)
                        return 1

        kwargs["fail_msg"] = "Unable to open port type pop-up"
        self.common_validation.failed(**kwargs)
        return -1

    def create_new_port_type_port_name_and_usage(self, port_details_interface_value, port_type_name, switch_profile, **kwargs):
        """
        - Assume that already on the Switch Template (Port Configuration)
            :return: Returns 1 if successfully navigates to the Port Details Tab
                     Else returns -1
        """

        # Commented on 1/18/23 because it is unused
        # port_type_name_field = self.sw_template_web_elements.get_sw_template_port_details_port_type_editor_name()
        self.sw_template_web_elements.get_sw_template_port_details_port_type_editor_name()

        port_type_dictionary = (switch_profile.get('port_details')).get('port_type')
        if not port_type_dictionary:
            kwargs["pass_msg"] = "No port details data in the dictionary"
            self.common_validation.passed(**kwargs)
            return 1

        port_name_and_usage_dictionary = port_type_dictionary.get('port_name_and_usage')
        status_value = port_name_and_usage_dictionary.get('status')
        auto_sense_value = port_name_and_usage_dictionary.get('auto_sense')
        access_value = port_name_and_usage_dictionary.get('access_port')
        trunk_value = port_name_and_usage_dictionary.get('trunk_port')
        description_value = port_name_and_usage_dictionary.get('description')

        description_element = self.sw_template_web_elements.get_sw_template_port_details_port_type_editor_description()
        status_element = self.sw_template_web_elements.get_sw_template_port_details_port_type_editor_status()
        auto_sense_element = self.sw_template_web_elements.get_sw_template_port_details_port_type_editor_auto_sense_status()
        access_element = self.sw_template_web_elements.get_sw_template_port_details_port_type_editor_access()
        trunk_element = self.sw_template_web_elements.get_sw_template_port_details_port_type_editor_trunk()
        type_name_field = self.sw_template_web_elements.get_sw_template_port_details_port_type_editor_name()

        if port_type_name:
            if not type_name_field:
                kwargs["fail_msg"] = "Unable to locate name field"
                self.common_validation.fault(**kwargs)
                return -1
            self.auto_actions.send_keys(type_name_field, port_type_name)
        if description_value:
            if not description_element:
                kwargs["fail_msg"] = "Unable to locate description field"
                self.common_validation.fault(**kwargs)
                return -1
            self.auto_actions.send_keys(description_element, description_value)
        if status_value:
            if not status_element:
                kwargs["fail_msg"] = "Unable to locate status field"
                self.common_validation.fault(**kwargs)
                return -1
            if status_value.lower() == 'on' and not status_element.is_selected():
                self.utils.print_info("Clicking status button to ON")
                self.auto_actions.click_reference(self.sw_template_web_elements.get_sw_template_port_details_port_type_editor_status)
            if status_value.lower() == 'off' and status_element.is_selected():
                self.utils.print_info("Clicking status button to OFF")
                self.auto_actions.click_reference(self.sw_template_web_elements.get_sw_template_port_details_port_type_editor_status)
        if auto_sense_value:
            if not auto_sense_element:
                kwargs["fail_msg"] = "Unable to locate auto sense field"
                self.common_validation.fault(**kwargs)
                return -1
            if auto_sense_value.lower() == 'on' and not auto_sense_element.is_selected():
                self.utils.print_info("Clicking status button to ON")
                self.auto_actions.click_reference(self.sw_template_web_elements.get_sw_template_port_details_port_type_editor_auto_sense_status)
            if auto_sense_value.lower() == 'off' and auto_sense_element.is_selected():
                self.utils.print_info("Clicking status button to OFF")
                self.auto_actions.click_reference(self.sw_template_web_elements.get_sw_template_port_details_port_type_editor_auto_sense_status)
        if access_value:
            if not access_element:
                kwargs["fail_msg"] = "Unable to locate access field"
                self.common_validation.fault(**kwargs)
                return -1
            if access_value.lower() == 'enable' and not access_element.is_selected():
                self.utils.print_info("Clicking access port option")
                self.auto_actions.click_reference(self.sw_template_web_elements.get_sw_template_port_details_port_type_editor_access)
        if trunk_value:
            if not trunk_element:
                kwargs["fail_msg"] = "Unable to locate trunk field"
                self.common_validation.fault(**kwargs)
                return -1
            if trunk_value.lower() == 'enable' and not trunk_element.is_selected():
                self.utils.print_info("Clicking trunk port option")
                self.auto_actions.click_reference(self.sw_template_web_elements.get_sw_template_port_details_port_type_editor_trunk)

        kwargs["pass_msg"] = "Able to configure new port type (port name and usage)"
        self.common_validation.passed(**kwargs)
        return 1

    def _get_active_port_type_tab(self):
        """
        - Assume that already on the Port Type Popup
            :return: Returns string representing the active tab (if known)
                     Else returns unknown
        """

        port_usage_tab = self.sw_template_web_elements.get_sw_template_port_details_port_type_editor_port_name_and_usage_tab()
        trans_tab = self.sw_template_web_elements.get_sw_template_port_details_port_type_editor_transmission_tab()
        storm_tab = self.sw_template_web_elements.get_sw_template_port_details_port_type_editor_storm_control_tab()
        summary_tab = self.sw_template_web_elements.get_sw_template_port_details_port_type_editor_summary_tab()
        vlan_tab = self.sw_template_web_elements.get_sw_template_port_details_port_type_editor_vlan_tab()
        stp_tab = self.sw_template_web_elements.get_sw_template_port_details_port_type_editor_stp_tab()

        results = port_usage_tab.get_attribute('class')
        if 'active' in results:
            return 'port_name_and_usage'

        results = trans_tab.get_attribute('class')
        if 'active' in results:
            return 'transmission_settings'

        results = storm_tab.get_attribute('class')
        if 'active' in results:
            return 'storm_control'

        results = summary_tab.get_attribute('class')
        if 'active' in results:
            return 'summary'

        results = vlan_tab.get_attribute('class')
        if 'active' in results:
            return 'vlan'

        results = stp_tab.get_attribute('class')
        if 'active' in results:
            return 'stp'

        return 'unknown'

    def create_new_port_type_transmission_settings(self, port_details_interface_value, port_details_port_type_value, switch_profile, **kwargs):
        """
        - Assume that already on the Switch Template (Port Configuration)
            :return: Returns 1 if successfully navigates to the Port Details Tab
                     Else returns -1
        """
        port_type_dictionary = (switch_profile.get('port_details')).get('port_type')
        transmission_setting_dictionary = port_type_dictionary.get('transmission_setting')
        if not transmission_setting_dictionary:
            kwargs["pass_msg"] = "No transmission setting data in dictionary"
            self.common_validation.passed(**kwargs)
            return 1

        type_value = transmission_setting_dictionary.get('type')
        speed_value = transmission_setting_dictionary.get('speed')
        self.utils.wait_till(self.sw_template_web_elements.get_sw_template_port_details_port_type_editor_duplex_arrow, timeout=20, delay=4)
        duplex_arrow_element = self.sw_template_web_elements.get_sw_template_port_details_port_type_editor_duplex_arrow()
        self.utils.wait_till(self.sw_template_web_elements.get_sw_template_port_details_port_type_editor_speed_arrow,
                             timeout=20, delay=4)
        speed_arrow_element = self.sw_template_web_elements.get_sw_template_port_details_port_type_editor_speed_arrow()
        if type_value:
            if not duplex_arrow_element:
                kwargs["fail_msg"] = "Unable to locate duplex field"
                self.common_validation.fault(**kwargs)
                return -1
            self.utils.print_info("Selecting " + type_value + " option in the duplex combo box")

            self.utils.wait_till(
                func=lambda: self.auto_actions.click(duplex_arrow_element),
                exp_func_resp=True,
                delay=4
            )
            combo_box_value_container = self.sw_template_web_elements.get_sw_template_port_details_port_type_editor_duplex_options_container()
            combo_box_value_elements = self.sw_template_web_elements.get_sw_template_port_details_port_type_editor_duplex_arrow_options(combo_box_value_container)
            for a_combo_element in combo_box_value_elements:
                if a_combo_element.text == type_value:
                    self.auto_actions.click(a_combo_element)
        if speed_value:
            if not speed_arrow_element:
                kwargs["fail_msg"] = "Unable to locate speed field"
                self.common_validation.fault(**kwargs)
                return -1
            self.utils.print_info("Selecting " + speed_value + " option in the speed combo box")

            self.utils.wait_till(
                func=lambda: self.auto_actions.click(speed_arrow_element),
                exp_func_resp=True,
                delay=4
            )
            combo_box_value_container = self.sw_template_web_elements.get_sw_template_port_details_port_type_editor_speed_options_container()
            combo_box_value_elements = self.sw_template_web_elements.get_sw_template_port_details_port_type_editor_speed_arrow_options(combo_box_value_container)
            for a_combo_element in combo_box_value_elements:
                if a_combo_element.text == speed_value:
                    self.auto_actions.click(a_combo_element)

        kwargs["pass_msg"] = "Able to configure new port type (transmission settings)"
        self.common_validation.passed(**kwargs)
        return 1

    def create_new_port_type_vlan(self, port_details_interface_value, port_details_port_type_value, switch_profile, **kwargs):
        """
        - Assume that already on the Switch Template (Port Configuration)
            :return: Returns 1 if successfully navigates to the Port Details Tab
                     Else returns -1
        """

        port_type_dictionary = (switch_profile.get('port_details')).get('port_type')
        if not port_type_dictionary:
            kwargs["pass_msg"] = "No port type data in dictionary"
            self.common_validation.passed(**kwargs)
            return 1

        vlan_dictionary = port_type_dictionary.get('vlan')
        if not vlan_dictionary:
            kwargs["pass_msg"] = "No vlan data in dictionary"
            self.common_validation.passed(**kwargs)
            return 1

        native_vlan_value = vlan_dictionary.get('native_vlan')
        allowed_vlans_value = vlan_dictionary.get('allowed_vlans')
        native_vlan_element = self.sw_template_web_elements.get_sw_template_port_details_port_type_editor_description()
        allowed_vlans_element = self.sw_template_web_elements.get_sw_template_port_details_port_type_editor_status()

        if native_vlan_value:
            if not native_vlan_element:
                kwargs["fail_msg"] = "Unable to locate native vlan field"
                self.common_validation.fault(**kwargs)
                return -1
            self.auto_actions.send_keys(native_vlan_element, native_vlan_value)

        if allowed_vlans_value:
            if not allowed_vlans_element:
                kwargs["fail_msg"] = "Unable to locate allowed vlan field"
                self.common_validation.fault(**kwargs)
                return -1
            self.auto_actions.click(allowed_vlans_element)
            combo_box_value_elements = self.sw_template_web_elements.get_sw_template_port_details_row_port_type_list()
            for a_combo_element in combo_box_value_elements:
                if a_combo_element.text == port_details_port_type_value:
                    self.auto_actions.click(a_combo_element)

        kwargs["pass_msg"] = "Able to configure new port type (vlan)"
        self.common_validation.passed(**kwargs)
        return 1

    def create_new_port_type_storm_control(self, port_details_interface_value, port_details_port_type_value,
                                           switch_profile, **kwargs):
        """
        - Assume that already on the Switch Template (Port Configuration)
            :return: Returns 1 if successfully navigates to the Port Details Tab
                     Else returns -1
        """

        port_type_dictionary = (switch_profile.get('port_details')).get('port_type')
        if not port_type_dictionary:
            kwargs["pass_msg"] = "No port type data in dictionary"
            self.common_validation.passed(**kwargs)
            return 1

        storm_control_dictionary = port_type_dictionary.get('storm_control')
        if not storm_control_dictionary:
            kwargs["pass_msg"] = "No storm control data in dictionary"
            self.common_validation.passed(**kwargs)
            return 1

        broadcast_value = storm_control_dictionary.get('broadcast')
        unicast_value = storm_control_dictionary.get('unicast')
        multicast_value = storm_control_dictionary.get('multicast')
        rate_limit_value = storm_control_dictionary.get('rate_limit_value')

        sc_broadcast_element = self.sw_template_web_elements.get_sw_template_port_details_port_type_editor_sc_broadcast()
        sc_unicast_element = self.sw_template_web_elements.get_sw_template_port_details_port_type_editor_sc_unicast()
        sc_multicast_element = self.sw_template_web_elements.get_sw_template_port_details_port_type_editor_sc_multicast()
        # Commented on 1/18/23 because variable is unused
        # sc_rate_limit_type_element = self.sw_template_web_elements.get_sw_template_port_details_port_type_editor_sc_rate_limit_type()
        # sc_threshold_element = self.sw_template_web_elements.get_sw_template_port_details_port_type_editor_sc_threshold()
        self.sw_template_web_elements.get_sw_template_port_details_port_type_editor_sc_rate_limit_type()
        self.sw_template_web_elements.get_sw_template_port_details_port_type_editor_sc_threshold()
        sc_rate_limit_value_element = self.sw_template_web_elements.get_sw_template_port_details_port_type_editor_sc_rate_limit_value()

        if broadcast_value:
            if not sc_broadcast_element:
                kwargs["fail_msg"] = "Unable to locate broadcast field"
                self.common_validation.fault(**kwargs)
                return -1
            if broadcast_value.lower() == 'enable' and not sc_broadcast_element.is_selected():
                self.utils.print_info("Enabling broadcast option")
                self.auto_actions.click_reference(self.sw_template_web_elements.get_sw_template_port_details_port_type_editor_sc_broadcast)
            if broadcast_value.lower() == 'disable' and sc_broadcast_element.is_selected():
                self.utils.print_info("Disabling broadcast option")
                self.auto_actions.click_reference(self.sw_template_web_elements.get_sw_template_port_details_port_type_editor_sc_broadcast)

        if unicast_value:
            if not sc_unicast_element:
                kwargs["fail_msg"] = "Unable to locate unicast field"
                self.common_validation.fault(**kwargs)
                return -1
            if unicast_value.lower() == 'enable' and not sc_unicast_element.is_selected():
                self.utils.print_info("Enabling unicast option")
                self.auto_actions.click_reference(self.sw_template_web_elements.get_sw_template_port_details_port_type_editor_sc_unicast)
            if unicast_value.lower() == 'disable' and sc_unicast_element.is_selected():
                self.utils.print_info("Disabling unicast option")
                self.auto_actions.click_reference(self.sw_template_web_elements.get_sw_template_port_details_port_type_editor_sc_unicast)

        if multicast_value:
            if not sc_multicast_element:
                kwargs["fail_msg"] = "Unable to locate multicast field"
                self.common_validation.fault(**kwargs)
                return -1
            if multicast_value.lower() == 'enable' and not sc_multicast_element.is_selected():
                self.utils.print_info("Enabling multicast option")
                self.auto_actions.click_reference(self.sw_template_web_elements.get_sw_template_port_details_port_type_editor_sc_multicast)
            if multicast_value.lower() == 'disable' and sc_multicast_element.is_selected():
                self.utils.print_info("Disabling multicast option")
                self.auto_actions.click_reference(self.sw_template_web_elements.get_sw_template_port_details_port_type_editor_sc_multicast)

        if rate_limit_value:
            if not sc_rate_limit_value_element:
                kwargs["fail_msg"] = "Unable to locate rate limit field"
                self.common_validation.fault(**kwargs)
                return -1
            self.utils.print_info("Setting rate limit value to " + rate_limit_value)
            self.auto_actions.send_keys(sc_rate_limit_value_element, rate_limit_value)

        kwargs["pass_msg"] = "Able to configure new port type (storm control)"
        self.common_validation.passed(**kwargs)
        return 1

    def create_new_port_type_stp(self, port_details_interface_value, port_details_port_type_value,
                                 switch_profile, **kwargs):
        """
        - Assume that already on the Switch Template (Port Configuration)
            :return: Returns 1 if successfully navigates to the Port Details Tab
                     Else returns -1
        """

        port_type_dictionary = (switch_profile.get('port_details')).get('port_type')
        if not port_type_dictionary:
            kwargs["pass_msg"] = "No port type data in dictionary"
            self.common_validation.passed(**kwargs)
            return 1

        port_type_stp_dictionary = port_type_dictionary.get('port_type_stp_config')
        if not port_type_stp_dictionary:
            kwargs["pass_msg"] = "No stp data in dictionary"
            self.common_validation.passed(**kwargs)
            return 1

        stp_enabled_value = port_type_stp_dictionary.get('stp_enabled')
        edge_port_value = port_type_stp_dictionary.get('edge_port')
        bpdu_protection_value = port_type_stp_dictionary.get('bpdu_protection')
        priority_value = port_type_stp_dictionary.get('priority')
        path_cost_value = port_type_stp_dictionary.get('path_cost')

        stp_enabled_element = self.sw_template_web_elements.get_sw_template_port_details_port_type_editor_spanning_tree_stp_enable()
        edge_port_element = self.sw_template_web_elements.get_sw_template_port_details_port_type_editor_spanning_tree_edge_port_enable()
        bpdu_protection_element = self.sw_template_web_elements.get_sw_template_port_details_port_type_editor_spanning_tree_bdu_protection()
        priority_element = self.sw_template_web_elements.get_sw_template_port_details_port_type_editor_spanning_tree_priority()
        path_cost_element = self.sw_template_web_elements.get_sw_template_port_details_port_type_editor_spanning_tree_path_cost()

        if stp_enabled_value:
            if not stp_enabled_element:
                kwargs["fail_msg"] = "Unable to locate stp enable field"
                self.common_validation.fault(**kwargs)
                return -1
            if stp_enabled_value.lower() == 'on' and not stp_enabled_element.is_selected():
                self.utils.print_info("Turning STP Enabled on")
                self.auto_actions.click_reference(self.sw_template_web_elements.get_sw_template_port_details_port_type_editor_spanning_tree_stp_enable)
            if stp_enabled_value.lower() == 'off' and stp_enabled_element.is_selected():
                self.utils.print_info("Turning STP Enabled off")
                self.auto_actions.click_reference(self.sw_template_web_elements.get_sw_template_port_details_port_type_editor_spanning_tree_stp_enable)

        if edge_port_value:
            if not edge_port_element:
                kwargs["fail_msg"] = "Unable to locate edge port field"
                self.common_validation.fault(**kwargs)
                return -1
            if edge_port_value.lower() == 'enable' and not edge_port_element.is_selected():
                self.utils.print_info("Turning Edge Port on")
                self.auto_actions.click_reference(self.sw_template_web_elements.get_sw_template_port_details_port_type_editor_spanning_tree_edge_port_enable)
            if edge_port_value.lower() == 'disable' and edge_port_element.is_selected():
                self.utils.print_info("Turning Edge Port off")
                self.auto_actions.click_reference(self.sw_template_web_elements.get_sw_template_port_details_port_type_editor_spanning_tree_edge_port_enable)

        if path_cost_value:
            if not path_cost_element:
                kwargs["fail_msg"] = "Unable to locate port cost field"
                self.common_validation.fault(**kwargs)
                return -1
            self.auto_actions.send_keys(path_cost_element, path_cost_value)

        if bpdu_protection_value:
            if not bpdu_protection_element:
                kwargs["fail_msg"] = "Unable to locate bdu protection field"
                self.common_validation.fault(**kwargs)
                return -1
            self.auto_actions.click_reference(self.sw_template_web_elements.get_sw_template_port_details_port_type_editor_spanning_tree_bdu_protection)
            combo_box_value_elements = self.sw_template_web_elements.get_sw_template_port_details_row_port_type_list()
            for a_combo_element in combo_box_value_elements:
                if a_combo_element.text == port_details_port_type_value:
                    self.auto_actions.click(a_combo_element)
        if priority_value:
            if not priority_element:
                kwargs["fail_msg"] = "Unable to locate priority field"
                self.common_validation.fault(**kwargs)
                return -1
            self.auto_actions.click_reference(self.sw_template_web_elements.get_sw_template_port_details_port_type_editor_spanning_tree_priority)
            combo_box_value_elements = self.sw_template_web_elements.get_sw_template_port_details_row_port_type_list()
            for a_combo_element in combo_box_value_elements:
                if a_combo_element.text == port_details_port_type_value:
                    self.auto_actions.click(a_combo_element)

        kwargs["pass_msg"] = "Able to configure new port type (stp)"
        self.common_validation.passed(**kwargs)
        return 1

    def verify_upload_config_auto_button(self, option="OFF", **kwargs):
        """
        This function is used to verify the `Upload configuration automatically` button from Advanced Settings tab
        based on an option given as parameter
        :param option: name of policy
        :return: 1 - if the button is equal with option was successful ; -1 - if not
        """
        verify_upload_cfg_auto = self.sw_template_web_elements.get_sw_template_auto_cfg()

        if not verify_upload_cfg_auto:
            kwargs["fail_msg"] = "Failed to get the verify_upload_cfg_auto button"
            self.common_validation.fault(**kwargs)
            return -1

        kwargs["pass_msg"] = "Successfully found 'Upload configuration automatically' button."
        self.common_validation.passed(**kwargs)

        verify_upload_cfg_auto = verify_upload_cfg_auto.is_selected()

        if not verify_upload_cfg_auto and option == "OFF":
            kwargs["pass_msg"] = "Auto configuration button is on OFF!"
            self.common_validation.passed(**kwargs)
            return 1

        elif verify_upload_cfg_auto and option == "ON":
            kwargs["pass_msg"] = "Auto configuration button is on ON!"
            self.common_validation.passed(**kwargs)
            return 1

        kwargs["fail_msg"] = "Auto configuration button is not in the expected state"
        self.common_validation.failed(**kwargs)
        return -1

    def verify_enable_auto_revert_option(self, **kwargs):
        """
        This function is used to verify if the `Reboot and revert Extreme Networks switch configuration if IQAgent is
        unresponsive after configuration update.` button from Advanced Settings tab is present or not
        :return: 1 - if the button is present ; -1 - if not
        """
        enable_auto_revert = self.sw_template_web_elements.get_sw_template_auto_revert_enabled()

        if not enable_auto_revert:
            kwargs["fail_msg"] = "Enable Auto Revert button is not present!"
            self.common_validation.fault(**kwargs)
            return -1
        status = enable_auto_revert.get_attribute("disabled")
        kwargs["pass_msg"] = "Enable Auto Revert button is present!"
        self.common_validation.passed(**kwargs)
        return status

    def set_upload_config_auto_button(self, **kwargs):
        """
        This function is used to set the `Upload configuration automatically` button from Advanced Settings tab
        :return: 1 - if the button is set successfully ; -1 - if not
        """
        verify_upload_cfg_auto = self.sw_template_web_elements.get_sw_template_auto_cfg()

        if not verify_upload_cfg_auto:
            kwargs["fail_msg"] = "Failed to get the verify_upload_cfg_auto button"
            self.common_validation.fault(**kwargs)
            return -1

        kwargs["pass_msg"] = "Successfully got the verify_upload_cfg_auto button"
        self.common_validation.passed(**kwargs)

        verify_upload_cfg_auto_is_selected = verify_upload_cfg_auto.is_selected()

        if not verify_upload_cfg_auto_is_selected:
            kwargs["pass_msg"] = "Auto configuration button is by default on OFF!"
            self.common_validation.passed(**kwargs)

        else:
            kwargs["fail_msg"] = "Auto configuration button is already on ON!"
            self.common_validation.failed(**kwargs)
            return -1

        self.utils.print_info("Click on Upload configuration automatically button")
        if self.auto_actions.click(verify_upload_cfg_auto) != 1:
            kwargs["fail_msg"] = "Failed to click the verify_upload_cfg_auto button"
            self.common_validation.fault(**kwargs)
            return -1

        kwargs["pass_msg"] = "Successfully clicked on the verify_upload_cfg_auto button"
        self.common_validation.passed(**kwargs)
        return 1

    def check_text_enable_auto_revert_option(self, **kwargs):
        """
        This function is used to verify the `Reboot and revert Extreme Networks switch configuration if IQAgent is
        unresponsive after configuration update.` button text from Advanced Settings tab based on an option given as
        parameter
        :return: 1 - if the button text is the one expected ; -1 - if not
        """
        enable_auto_revert_message = self.sw_template_web_elements.get_sw_template_auto_revert_msg()

        if not enable_auto_revert_message:
            kwargs["fail_msg"] = "Failed to get enable_auto_revert_message element"
            self.common_validation.failed(**kwargs)
            return -1

        kwargs["pass_msg"] = "Successfully got the enable_auto_revert_message element"
        self.common_validation.passed(**kwargs)

        enable_auto_revert_message = enable_auto_revert_message.text

        if enable_auto_revert_message != "Reboot and revert Extreme Networks switch configuration if IQAgent is " \
                                         "unresponsive after configuration update.":
            kwargs["fail_msg"] = "The Enable Auto Revert button name is not the correct " \
                                 f"one: {enable_auto_revert_message}!"
            self.common_validation.failed(**kwargs)
            return -1

        return 1

    def set_enable_auto_revert_option(self, **kwargs):
        """
        This function is used to set/check the `Reboot and revert Extreme Networks switch configuration if IQAgent is
        unresponsive after configuration update.` button under the `Upload configuration automatically` button
        from Advanced Settings tab
        :return: 1 - if the button is set successfully ; -1 - if not
        """
        enable_auto_revert_message = self.sw_template_web_elements.get_sw_template_auto_revert_msg()

        if not enable_auto_revert_message:
            kwargs["fail_msg"] = "Failed to get enable_auto_revert_message element"
            self.common_validation.failed(**kwargs)
            return -1

        kwargs["pass_msg"] = "Successfully got the enable_auto_revert_message element"
        self.common_validation.passed(**kwargs)

        enable_auto_revert_message = enable_auto_revert_message.text

        if enable_auto_revert_message != "Reboot and revert Extreme Networks switch configuration if IQAgent is " \
                                         "unresponsive after configuration update.":
            kwargs["fail_msg"] = f"The Enable Auto Revert button name is not the correct " \
                                 f"one: {enable_auto_revert_message}!"
            self.common_validation.failed(**kwargs)
            return -1

        enable_auto_revert = self.sw_template_web_elements.get_sw_template_auto_revert_enabled()

        if not enable_auto_revert:
            kwargs["fail_msg"] = "Enable Auto Revert button is not present!"
            self.common_validation.fault(**kwargs)
            return -1

        kwargs["pass_msg"] = "Enable Auto Revert button is present!"
        self.common_validation.passed(**kwargs)

        if not enable_auto_revert.is_selected():
            kwargs["pass_msg"] = "Enable Auto Revert button is by default unchecked!"
            self.common_validation.passed(**kwargs)
        else:
            kwargs["fail_msg"] = "Enable Auto Revert button is already checked!"
            self.common_validation.failed(**kwargs)
            return -1

        self.utils.print_info("Click on Enable Auto Revert button")
        if self.auto_actions.click(enable_auto_revert) != 1:
            kwargs["fail_msg"] = "Failed to click the enable_auto_revert button"
            self.common_validation.fault(**kwargs)
            return -1

        kwargs["pass_msg"] = "Successfully clicked the enable_auto_revert button"
        self.common_validation.passed(**kwargs)
        return 1

    def save_template_with_popup(self, **kwargs):
        """
        This function is used to save the current device template with a pop-up displayed
        :return: 1 - if the save was successful ; -1 - if not
        """
        self.save_template()

        sw_yes_button = self.sw_template_web_elements.get_sw_template_notification_yes_btn()

        if not sw_yes_button or not sw_yes_button.is_displayed():
            kwargs["fail_msg"] = "YES button is not displayed"
            self.common_validation.fault(**kwargs)
            return -1

        self.utils.print_info("Click on SAVE button")
        if self.auto_actions.click(sw_yes_button) != 1:
            kwargs["fail_msg"] = "Failed to click the sw_yes_button button"
            self.common_validation.fault(**kwargs)
            return -1

        kwargs["pass_msg"] = "Successfully clicked the sw_yes_button button"
        self.common_validation.passed(**kwargs)
        return 1

    def click_on_port_details_tab(self, **kwargs):
        """Method that click on the STP port details button in the Template Configuration

        Returns:
            int: 1 if the function call has succeeded else -1
        """
        stp_tab_button, _ = self.utils.wait_till(
            func=self.sw_template_web_elements.get_sw_template_port_details_tab,
            silent_failure=True,
            exp_func_resp=True,
            delay=5
        )

        if stp_tab_button is None:
            kwargs["fail_msg"] = "Failed to get the STP port details button"
            self.common_validation.fault(**kwargs)
            return -1

        self.utils.print_info("Successfully got the STP port details button")

        res, _ = self.utils.wait_till(
            func=lambda: self.auto_actions.click(stp_tab_button),
            exp_func_resp=True,
            delay=4,
            silent_failure=True
        )

        if res == 1:
            kwargs["pass_msg"] = "Successfully clicked the STP port details button"
            self.common_validation.passed(**kwargs)
            return 1

        kwargs["fail_msg"] = "Failed to click the STP port details button"
        self.common_validation.fault(**kwargs)
        return -1

    def revert_port_configuration_template_level(self, port_type, **kwargs):
        """Method that reverts all the ports to a specific port type.

        Args:
            port_type (str): the port type name

        Returns:
            int: 1 if the function call has succeeded else -1
        """
        try:
            select_all_ports, _ = self.utils.wait_till(
                func=self.sw_template_web_elements.all_ports_selected,
                silent_failure=True,
                exp_func_resp=True
            )

            if not select_all_ports:
                kwargs["fail_msg"] = "Failed to get the select_all_ports button"
                self.common_validation.fault(**kwargs)
                return -1

            self.utils.print_info("Successfully got the select_all_ports button")

            res, _ = self.utils.wait_till(
                func=lambda: self.auto_actions.click(select_all_ports),
                exp_func_resp=True,
                delay=4
            )
            if res == 1:
                self.utils.print_info("Successfully clicked the select_all_ports button")
            else:
                kwargs["fail_msg"] = "Failed to click the select_all_ports button"
                self.common_validation.fault(**kwargs)
                return -1

            assign_to_all_ports_selected, _ = self.utils.wait_till(
                func=
                self.sw_template_web_elements.assign_all_ports_selected,
                silent_failure=True,
                exp_func_resp=True,
                delay=5
            )

            if not assign_to_all_ports_selected:
                kwargs["fail_msg"] = "Failed to get the assign_to_all_ports_selected button"
                self.common_validation.fault(**kwargs)
                return -1

            self.utils.print_info("Successfully got the assign_to_all_ports_selected button")

            res, _ = self.utils.wait_till(
                func=lambda: self.auto_actions.click(assign_to_all_ports_selected),
                exp_func_resp=True,
                delay=4
            )

            if res != 1:
                kwargs["fail_msg"] = "Failed to click the assign_to_all_ports_selected button"
                self.common_validation.fault(**kwargs)
                return -1

            self.utils.print_info("Successfully clicked the assign_to_all_ports_selected button")

            assign_button, _ = self.utils.wait_till(
                func=self.sw_template_web_elements.get_sw_template_assign_choose_existing,
                silent_failure=True,
                exp_func_resp=True,
                delay=5
            )

            if not assign_button:
                kwargs["fail_msg"] = "Failed to get the assign_button button"
                self.common_validation.fault(**kwargs)
                return -1

            self.utils.print_info("Successfully got the assign_button button")

            res, _ = self.utils.wait_till(
                func=lambda: self.auto_actions.click(assign_button),
                exp_func_resp=True,
                delay=4
            )

            if res != 1:
                kwargs["fail_msg"] = "Failed to click the assign_button button"
                self.common_validation.fault(**kwargs)
                return -1

            self.utils.print_info("Successfully clicked the assign_button button")

            radio_buttons, _ = self.utils.wait_till(
                func=self.sw_template_web_elements.get_sw_template_all_port_type_list_radio,
                silent_failure=True,
                exp_func_resp=True,
                timeout=40,
                delay=5
            )

            if not radio_buttons:
                kwargs["fail_msg"] = "Failed to get the radio_buttons"
                self.common_validation.fault(**kwargs)
                return -1

            self.utils.print_info("Successfully got the radio_buttons")

            radio_buttons_labels, _ = self.utils.wait_till(
                func=self.sw_template_web_elements.get_sw_template_all_port_type_list_label,
                silent_failure=True,
                exp_func_resp=True,
                delay=5

            )

            if not radio_buttons_labels:
                kwargs["fail_msg"] = "Failed to get the radio_buttons_labels"
                self.common_validation.fault(**kwargs)
                return -1

            self.utils.print_info("Successfully got the radio_buttons_labels")

            for btn, label in zip(radio_buttons, radio_buttons_labels):
                if label.text == port_type:
                    self.utils.wait_till(
                        func=lambda: self.auto_actions.click(btn),
                        exp_func_resp=True,
                        delay=4
                    )
                    break
            else:
                kwargs["fail_msg"] = "Failed to find the correct button for port type"
                self.common_validation.fault(**kwargs)
                return -1

            kwargs["pass_msg"] = "Successfully reverted the port configuration"
            self.common_validation.passed(**kwargs)
            return 1

        finally:

            save_button, _ = self.utils.wait_till(
                func=self.sw_template_web_elements.get_sw_template_port_type_list_save_button,
                silent_failure=True,
                exp_func_resp=True,
                delay=5
            )

            if save_button:
                self.utils.wait_till(
                    func=lambda: self.auto_actions.click(save_button),
                    exp_func_resp=True,
                    silent_failure=True
                )

    def click_on_stp_tab(self, **kwargs):
        """Method that click on the STP tab in the Template Configuration page

            Returns:
                int: 1 if the function call has succeeded else -1
        """
        stp_tab_button, _ = self.utils.wait_till(
            func=self.sw_template_web_elements.get_sw_template_stp_tab,
            silent_failure=True,
            exp_func_resp=True,
            delay=5
        )

        if not stp_tab_button:
            kwargs["fail_msg"] = "Failed to get the STP tab button"
            self.common_validation.fault(**kwargs)
            return -1

        self.utils.print_info("Successfully got the STP tab button")

        res, _ = self.utils.wait_till(
            func=lambda: self.auto_actions.click(stp_tab_button),
            exp_func_resp=True,
            silent_failure=True,
            delay=4
        )

        if res == 1:
            kwargs["pass_msg"] = "Successfully clicked the STP tab button"
            self.common_validation.passed(**kwargs)
            return 1

        kwargs["fail_msg"] = "Failed to click the STP tab button"
        self.common_validation.fault(**kwargs)
        return -1

    def get_stp_port_configuration_rows(self, **kwargs):
        """Method that returns the port configuration rows in the Template Configuration page

        Returns:
            list: a list that contains all the STP port configuration rows
        """
        rows, _ = self.utils.wait_till(
            func=self.sw_template_web_elements.get_sw_template_stp_port_rows,
            silent_failure=True,
            exp_func_resp=True,
            delay=5
        )

        if not rows:
            kwargs["fail_msg"] = "Failed to get the STP port configuration rows"
            self.common_validation.failed(**kwargs)
            return -1

        kwargs["pass_msg"] = "Successfully got the STP port configuration rows"
        self.common_validation.passed(**kwargs)
        return rows

    def get_stp_port_configuration_row(self, port, **kwargs):
        """Method that returns a specific STP port configuration row based on the given port value.

        Args:
            port (string): the port of the switch

        Returns:
            _type_: the STP row configuration of the given port
        """
        rows = self.get_stp_port_configuration_rows()
        row = [r for r in rows if re.search(f"^{port}\n", r.text)]

        if not row:
            kwargs["fail_msg"] = f"Failed to find the row port for port='{port}'"
            self.common_validation.failed(**kwargs)
            return -1

        kwargs["pass_msg"] = f"Successfully found the row port for port='{port}'"
        self.common_validation.passed(**kwargs)
        return row[0]

    def navigate_to_slot_template(self, slot, **kwargs):
        """Method that navigates to the template configuration of a given stack slot.

        Args:
            slot (int): the stack slot

        Returns:
            int: 1 if the function call has succeeded else -1
        """
        template_slot = self.sw_template_web_elements.get_template_slot(slot=slot)
        if not template_slot:
            kwargs["fail_msg"] = f"Failed to get the template for slot {slot}"
            self.common_validation.failed(**kwargs)
            return -1

        self.utils.print_info(f"Successfully got the template for slot {slot}")

        if self.auto_actions.click(template_slot) != 1:
            kwargs["fail_msg"] = f"Failed to click on the template slot {slot}"
            self.common_validation.fault(**kwargs)
            return -1

        kwargs["pass_msg"] = f"Successfully clicked on the template slot {slot}"
        self.common_validation.passed(**kwargs)

        self.utils.wait_till(timeout=5)
        return 1

    def get_path_cost_value_from_stp_port_configuration_row(self, port, **kwargs):
        """Method that returns the path cost value of a given port.

        Args:
            port (str): the name of the port

        Returns:
            int: the path cost
        """
        row = self.get_stp_port_configuration_row(port=port)

        cost_element, _ = self.utils.wait_till(
            func=lambda:
            self.sw_template_web_elements.get_sw_template_path_cost_row(row),
            silent_failure=True,
            exp_func_resp=True,
            delay=5
        )

        if not cost_element:
            kwargs["fail_msg"] = "Failed to get path cost element"
            self.common_validation.failed(**kwargs)
            return -1

        kwargs["pass_msg"] = "Successfully got the path cost element"
        self.common_validation.passed(**kwargs)

        return cost_element.get_attribute("value")

    def verify_path_cost_in_port_configuration_stp_tab(self, cli_type, template_switch, network_policy, port, path_cost, slot=None, **kwargs):
        """Method that verifies the path cost of a given port.

        Args:
            cli_type (str): Device CLI Type e.g., VOSS,EXOS
            template_switch (str): the name of the template switch
            network_policy (str): the name of the network policy
            port (str): the port of the switch
            path_cost (): the expected path cost value
            slot (str, optional): the stack slot. Defaults to None.

        Returns:
            int: 1 if the function call has succeeded else -1

        """

        self.utils.print_info(f"Go to the port configuration of {template_switch} template")
        self.select_sw_template(network_policy, template_switch, cli_type)
        self.go_to_port_configuration()

        if slot is not None:
            required_slot = template_switch + "-" + slot
            self.navigate_to_slot_template(required_slot)

        self.click_on_stp_tab()

        found_path_cost_value = self.get_path_cost_value_from_stp_port_configuration_row(
            port)

        if str(found_path_cost_value) != str(path_cost):
            kwargs["fail_msg"] = f"In XIQ port configuration: Expected path cost for port='{port}' is {path_cost} " \
                                 f"but found '{found_path_cost_value}'"
            self.common_validation.failed(**kwargs)
            return -1

        kwargs["pass_msg"] = f"Successfully found the expected path cost for port='{port}': {path_cost}"
        self.common_validation.passed(**kwargs)
        return 1

    def set_stp(self, enable=True, **kwargs):
        """Method that enables the STP in Template Configuration.

        Args:
            enable (bool, optional): If it is True then it will enable STP; if it is False then it will disable STP. Defaults to True.

        Returns:
            int: 1 if the function call has succeeded else -1
        """
        button, _ = self.utils.wait_till(
            func=self.sw_template_web_elements.get_sw_template_enable_spanningtree,
            exp_func_resp=True,
            silent_failure=True,
            delay=5
        )

        if not button:
            kwargs["fail_msg"] = "Failed to get stp button element"
            self.common_validation.fault(**kwargs)
            return -1

        self.utils.print_info("Successfully got the stp button element")

        if (not button.is_selected() and enable) or (
            button.is_selected() and not enable):
            res, _ = self.utils.wait_till(
                func=lambda: self.auto_actions.click(button),
                exp_func_resp=True,
                delay=4
            )

            if res != 1:
                kwargs["fail_msg"] = "Failed to click stp button element"
                self.common_validation.fault(**kwargs)
                return -1

            kwargs["pass_msg"] = "Successfully clicked the stp button element"
            self.common_validation.passed(**kwargs)

        return 1

    def set_override_policy_common_settings(self, state, **kwargs):
        """ Method that enables/disables the Override Policy Common Settings option in Template Configuration.
        
        :param state: True|False
        :return: 1 if the method call is successful else -1
        """
        
        if not isinstance(state, bool):
            kwargs["fail_msg"] = "The 'state' argument should be a boolean value"
            self.common_validation.fault(**kwargs)
            return -1

        state = "enable" if state else "disable"

        button, _ = self.utils.wait_till(
            func=self.sw_template_web_elements.get_device_template_override_policy,
            exp_func_resp=True,
            silent_failure=True,
            delay=5
        )
        
        if not button:
            kwargs["fail_msg"] = "Failed to get the device_template_override_policy button"
            self.common_validation.fault(**kwargs)
            return -1
        
        if (button.is_selected() and state == "disable") or (not button.is_selected() and state == "enable"):
            
            self.utils.print_info(f"Click on the device_template_override_policy button in order to {state} it.")
            
            res, _ = self.utils.wait_till(
                func=lambda: self.auto_actions.click(button),
                exp_func_resp=True,
                delay=4
            )

            if res != 1:
                kwargs["fail_msg"] = "Failed to click the device_template_override_policy button"
                self.common_validation.fault(**kwargs)
                return -1

            kwargs["pass_msg"] = f"Successfully clicked the device_template_override_policy button and {state}d it."
            self.common_validation.passed(**kwargs)
            return 1
        
        kwargs["pass_msg"] = f"device_template_override_policy button is already {state}d."
        self.common_validation.passed(**kwargs)
        return 1
    
    def choose_stp_mode(self, mode, **kwargs):
        """Method that choses the STP mode in Template Configuration.

        Args:
            mode (str): the STP mode

        Returns:
            int: 1 if the function call has succeeded else -1
        """
        if mode == "stp":
            button, _ = self.utils.wait_till(
                func=self.get_sw_template_enable_stp,
                exp_func_resp=True,
                silent_failure=True,
                delay=5
            )

        elif mode == "rstp":
            button, _ = self.utils.wait_till(
                func=self.sw_template_web_elements.get_sw_template_enable_rstp,
                exp_func_resp=True,
                silent_failure=True,
                delay=5
            )

        elif mode == "mstp":
            button, _ = self.utils.wait_till(
                func=self.sw_template_web_elements.get_sw_template_enable_mstp,
                exp_func_resp=True,
                silent_failure=True,
                delay=5
        )

        if not button:
            kwargs["fail_msg"] = f"Failed to get the {mode} stp mode button"
            self.common_validation.fault(**kwargs)
            return -1

        self.utils.print_info(f"Successfully got the {mode} stp mode button")

        res, _ = self.utils.wait_till(
            func=lambda: self.auto_actions.click(button),
            exp_func_resp=True,
            delay=4
        )

        if res != 1:
            kwargs["fail_msg"] = f"Failed to click the {mode} stp mode button"
            self.common_validation.fault(**kwargs)
            return -1

        kwargs["pass_msg"] = f"Successfully clicked the {mode} stp mode button"
        self.common_validation.passed(**kwargs)
        return 1

    def _set_nw_policy_if_needed(self):
        """
        Method sets up self.nw_policy if necessary
        :return:
        """
        if not self.nw_policy:
            self.nw_policy = extauto.xiq.flows.configure.NetworkPolicy.NetworkPolicy()

    def create_modify_lag_in_template(self, main_lag_port, ports, device='', **kwargs):

        """
        This keyword is used to create or verify and existing LAG port for stacks. It first verify if LAG was created and
         add a new port to it. Assuming navigation to port configuration is done.
        :param device: type of EXOS device stack or standalone
        :param main_lag_port: Master port
        :param ports: other ports
        """

        if device == 'stack':
            lag_text = main_lag_port + " LAG"
            self.utils.wait_till(timeout=5)
            self.auto_actions.scroll_down()
            self.auto_actions.scroll_bottom()
            lag_link = self.sw_template_web_elements.get_lag_span(lag=main_lag_port)
            is_lag_found = False
            if lag_link is not None:
                lag_link = self.sw_template_web_elements.get_lag_span(lag=main_lag_port)
                if lag_link.text == lag_text:
                    is_lag_found = True
                    self.utils.print_info(f"LAG {main_lag_port} found on the page.")
            if not is_lag_found:
                self.utils.print_info("LAG not created. Creating LAG.")
                self.auto_actions.click(self.sw_template_web_elements.get_aggr_ports_across_stack_button())
                self.auto_actions.click(self.sw_template_web_elements.get_lacp_toggle_button())
                self.auto_actions.click(self.sw_template_web_elements.get_available_slot(main_lag_port[0]))
                sleep(3)
                self.auto_actions.click(self.sw_template_web_elements.get_available_port(port=main_lag_port))
                self.auto_actions.click(self.sw_template_web_elements.get_lag_add_port_button())
                for port in ports:
                    self.auto_actions.click(self.sw_template_web_elements.get_available_port(port=port))
                    self.auto_actions.click(self.sw_template_web_elements.get_lag_add_port_button())
                self.auto_actions.click(self.sw_template_web_elements.get_save_port_type_button())
                self.auto_actions.click(self.sw_template_web_elements.get_switch_temp_save_button())
                kwargs["pass_msg"] = f"Successfully created lag {main_lag_port}"
                self.common_validation.passed(**kwargs)
            else:
                self.utils.print_info(f"Add port {ports} to lag group {main_lag_port}")
                self.auto_actions.move_to_element(self.sw_template_web_elements.get_lag_span(lag=main_lag_port))
                self.auto_actions.click(self.sw_template_web_elements.get_lag_span(lag=main_lag_port))
                sleep(3)
                for port in ports:
                    self.auto_actions.click(self.sw_template_web_elements.get_available_port(port=port))
                    self.auto_actions.click(self.sw_template_web_elements.get_lag_add_port_button())
                    selected_port = self.sw_template_web_elements.get_selected_port(port=port)
                    if selected_port is None:
                        kwargs["fail_msg"] = f"Failed to add port {ports} to lag {main_lag_port}"
                        self.common_validation.failed(**kwargs)
                self.auto_actions.click(self.sw_template_web_elements.get_save_port_type_button())
                self.auto_actions.click(self.sw_template_web_elements.get_switch_temp_save_button())
                kwargs["pass_msg"] = f"Successfully add {ports} to lag {main_lag_port}"
                self.common_validation.passed(**kwargs)
        elif device == 'standalone':
            lag_text = main_lag_port + " LAG"
            self.utils.wait_till(timeout=5)
            self.auto_actions.scroll_down()
            self.auto_actions.scroll_bottom()
            lag_link = self.sw_template_web_elements.get_lag_span(lag=main_lag_port)
            is_lag_found = False
            if lag_link is not None:
                lag_link = self.sw_template_web_elements.get_lag_span(lag=main_lag_port)
                if lag_link.text == lag_text:
                    is_lag_found = True
                    self.utils.print_info(f"LAG {main_lag_port} found on the page.")
            if not is_lag_found:
                self.utils.print_info("LAG not created. Creating LAG.")
                self.auto_actions.click(self.sw_template_web_elements.get_aggr_ports_standalone_button())
                self.auto_actions.click(self.sw_template_web_elements.get_lacp_toggle_button())
                sleep(3)
                self.auto_actions.click(self.sw_template_web_elements.get_available_port(port=main_lag_port))
                self.auto_actions.click(self.sw_template_web_elements.get_lag_add_port_button())
                for port in ports:
                    self.auto_actions.click(self.sw_template_web_elements.get_available_port(port=port))
                    self.auto_actions.click(self.sw_template_web_elements.get_lag_add_port_button())
                self.auto_actions.click(self.sw_template_web_elements.get_save_port_type_button())
                self.auto_actions.click(self.sw_template_web_elements.save_device_template())
                kwargs["pass_msg"] = f"Successfully created lag {main_lag_port}"
                self.common_validation.passed(**kwargs)
            else:
                self.utils.print_info(f"Add port {ports} to lag group {main_lag_port}")
                self.auto_actions.move_to_element(self.sw_template_web_elements.get_lag_span(lag=main_lag_port))
                self.auto_actions.click(self.sw_template_web_elements.get_lag_span(lag=main_lag_port))
                sleep(3)
                for port in ports:
                    self.auto_actions.click(self.sw_template_web_elements.get_available_port(port=port))
                    self.auto_actions.click(self.sw_template_web_elements.get_lag_add_port_button())
                    selected_port = self.sw_template_web_elements.get_selected_port(port=port)
                    if selected_port is None:
                        kwargs["fail_msg"] = f"Failed to add port {ports} to lag {main_lag_port}"
                        self.common_validation.failed(**kwargs)
                self.auto_actions.click(self.sw_template_web_elements.get_save_port_type_button())
                self.auto_actions.click(self.sw_template_web_elements.save_device_template())
                kwargs["pass_msg"] = f"Successfully add {ports} to lag {main_lag_port}"
                self.common_validation.passed(**kwargs)

    def remove_lag_in_template(self, main_lag_port, ports, device='', **kwargs):

        """
        This keyword is used to remove ports from LAG
        :param device: either stack or standalone
        :param main_lag_port: Master port
        :param ports: list with all ports that need to be removed
        """
        lag_text = main_lag_port + " LAG"
        self.utils.wait_till(timeout=5)
        self.auto_actions.scroll_down()
        self.auto_actions.scroll_bottom()
        lag_link = self.sw_template_web_elements.get_lag_span(lag=main_lag_port)
        is_lag_found = False
        if lag_link is not None:
            lag_link = self.sw_template_web_elements.get_lag_span(lag=main_lag_port)
            if lag_link.text == lag_text:
                is_lag_found = True
                self.utils.print_info(f"LAG {main_lag_port} found on the page.")
                self.auto_actions.click(lag_link)
        if not is_lag_found:
            kwargs["fail_msg"] = f"{lag_text} wasn't found"
            self.common_validation.failed(**kwargs)
        for port in ports:
            if not self.sw_template_web_elements.get_selected_port(port=port).is_selected():
                self.auto_actions.click(self.sw_template_web_elements.get_selected_port(port=port))
            self.auto_actions.click(self.sw_template_web_elements.get_lag_remove_port_button())
            sleep(2)
        self.auto_actions.click(self.sw_template_web_elements.get_save_port_type_button())
        sleep(2)
        if device == 'stack':
            self.auto_actions.click(self.sw_template_web_elements.get_switch_temp_save_button())
        elif device == 'standalone':
            self.auto_actions.click(self.sw_template_web_elements.save_device_template())
        else:
            kwargs["fail_msg"] = "Please specify a device type."
            self.common_validation.failed(**kwargs)
        kwargs["pass_msg"] = f"Successfully removed {ports} from lag {main_lag_port}"
        self.common_validation.passed(**kwargs)

    def global_mac_locking_status_change(self, policy_name, template_name, **kwargs):
        """
         - This keyword will enable mac locking from Device Template(Device Configuration)
         It Assumes That Already Created a Network Policy with a Template
        :param: policy_name The name of the policy to use.
        :param: template_name The name of the template from policy.
        :return: 1 if success , -1 if error
        - Keyword Usage: global mac locking status change  ${NW_POLICY}  ${SW_TEMPLATE_NAME}
        """
        status = kwargs.get("status", "OFF")
        cli_type = kwargs.get("cli_type", "exos")
        if self.select_sw_template(policy_name, template_name, cli_type) != 1:
            kwargs["fail_msg"] = "Not found the network policy. Make sure that it was created before."
            self.common_validation.failed(**kwargs)
            return -1
        self.set_override_policy_common_settings(state=True)
        enable_mac = self.sw_template_web_elements.get_sw_template_enable_mac_locking()
        if not enable_mac.is_selected() and status == "ON":
            self.utils.print_info("Enabling MAC Locking...")
            self.auto_actions.click_reference(self.sw_template_web_elements.get_sw_template_enable_mac_locking)
            confirmation_message = self.sw_template_web_elements.get_sw_template_enable_mac_locking_confirm_message()
            if "none" not in confirmation_message.get_attribute("style"):
                self.utils.print_info("Selecting YES in confirmation pop-up.")
                self.auto_actions.click_reference(
                    self.sw_template_web_elements.get_sw_template_enable_mac_locking_confirm_message_yes_button)
            else:
                kwargs["fail_msg"] = "Confirmation pop-up did not appear. Check override common settings is enabled."
                self.common_validation.failed(**kwargs)
                return -1
        elif enable_mac.is_selected() and status == "OFF":
            self.utils.print_info("Disabling MAC Locking...")
            self.auto_actions.click_reference(self.sw_template_web_elements.get_sw_template_enable_mac_locking)
        elif enable_mac.is_selected() and status == "ON":
            kwargs["pass_msg"] = "Already enabled MAC locking. Nothing to do!"
            self.common_validation.passed(**kwargs)
            return 1
        elif not enable_mac.is_selected() and status == "OFF":
            kwargs["pass_msg"] = "Already disabled MAC locking. Nothing to do!"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs["fail_msg"] = "Could not enable mac locking."
            self.common_validation.failed(**kwargs)
            return -1

        self.utils.print_info("Saving template default changes...")
        self.switch_template_save()
        kwargs["pass_msg"] = f"Successfully changed MAC Locking state to {status}"
        self.common_validation.passed(**kwargs)
        return 1

    def device_templ_advanced_settings(self, nw_policy, sw_template_name, cli_type, sw_model='Default', upgrade_device_upon_auth=False,
                                       current_image_version=False, upload_auto=False, select_current=False, **kwargs):
        """
        - Checks the given switch template present already in the switch Templates Grid
        - If it is not there add to the sw_template

        - Keyword Usage
        - ``Add SW Template  ${NW_POLICY}  ${SW_MODEL}   ${SW_TEMPLATE_NAME}``

        :param nw_policy: network policy
        :param sw_model: Switch Model ie SR2348P
        :param sw_template_name: Switch Template Name ie template_SR2348P
        :param upgrade_device_upon_auth: if True Upgrade device upon authentication will be set to On
        :param current_image_version: if present device firmware version upgrade will be done to a version that is
                                     different to the one passed, if False, firmware will be the latest by default
        :param upload_auto: if True, upload configuration automatically will be set to On
        :param select_current: if True, the firmware upgrade version will be the current version of the dut
        :return: 1 if Switch Template Configured Successfully else -1
        """
        self.navigator.navigate_to_switch_templates()
        if self.select_adv_settings_tab(nw_policy, sw_template_name, cli_type) == -1:
            kwargs['fail_msg'] = "Unable to navigate to 'Advanced Settings'."
            self.common_validation.fault(**kwargs)
        if upgrade_device_upon_auth:
            self.utils.print_info("Verify if the Upgrade device firmware upon device authentication button "
                                  "is off by default")
            if self.sw_template_web_elements.get_sw_template_adv_settings_upgrade_device_on_off_button().is_selected():
                kwargs['fail_msg'] = "The 'Upgrade device firmware upon device authentication' button is not off by default."
            self.utils.print_info("Click on Upgrade device firmware upon device authentication button")
            self.auto_actions.click_reference(
                self.sw_template_web_elements.get_sw_template_adv_settings_upgrade_device_on_off_button)

            sleep(3)
            if current_image_version:
                if not self.sw_template_web_elements.get_sw_template_adv_settings_upgr_firm_specific_button():
                    kwargs['fail_msg'] = "Unable to locate 'Upgrade firmware to the specific version button'"
                    self.common_validation.fault(**kwargs)
                else:
                    self.utils.print_info("Click on Upgrade firmware to the specific version button")
                    self.auto_actions.click_reference(self.sw_template_web_elements.get_sw_template_adv_settings_upgr_firm_specific_button)

                if not self.select_specific_firmware_version(sw_model, current_image_version, select_current):
                    kwargs['fail_msg'] = "Selection of a specific firmware image failed"
                    self.common_validation.fault(**kwargs)

            else:
                if not self.sw_template_web_elements.get_sw_template_adv_settings_upgr_firm_latest_button():
                    kwargs['fail_msg'] = "Unable to locate 'Upgrade firmware to the latest version button'"
                    self.common_validation.fault(**kwargs)
                else:
                    self.utils.print_info("Click on Upgrade firmware to the latest version button")
                    self.auto_actions.click_reference(
                        self.sw_template_web_elements.get_sw_template_adv_settings_upgr_firm_latest_button)

        if upload_auto:
            self.utils.print_info("Verify if the Upload Configuration button is off by default")
            if not self.sw_template_web_elements.get_sw_template_adv_settings_upload_configuration_on_off_button():
                kwargs['fail_msg'] = "Unable to locate 'Upload configuration automatically' button"
                self.common_validation.fault(**kwargs)

            elif self.sw_template_web_elements.get_sw_template_adv_settings_upload_configuration_on_off_button().is_selected():
                kwargs['fail_msg'] = "The 'Upload Configuration' button is not off by default"
                self.common_validation.fault(**kwargs)

            else:
                self.utils.print_info("Click on Upload configuration automatically button")
                self.auto_actions.click_reference(
                    self.sw_template_web_elements.get_sw_template_adv_settings_upload_configuration_on_off_button)

        sleep(1)
        self.utils.print_info("Get Template Save Button")
        save_btns = self.sw_template_web_elements.get_sw_template_save_button()

        rc = -1
        for save_btn in save_btns:
            if save_btn.is_displayed():
                self.utils.print_info("Click on the save template button")
                self.auto_actions.click(save_btn)
                self.screen.save_screen_shot()
                tool_tip_text = tool_tip.tool_tip_text
                self.utils.print_info("Tool tip Text Displayed on Page", tool_tip_text)

                def _is_sw_template_available():
                    return self.get_sw_template_row(sw_template_name)

                self.utils.wait_till(_is_sw_template_available, delay=0.5, is_logging_enabled=True, silent_failure=False)

                self.screen.save_screen_shot()
                rc = 1
                break

        self.utils.print_info("Click on network policy exit button")
        self.auto_actions.click_reference(self.np_web_elements.get_np_exit_button)
        sleep(2)

        kwargs['pass_msg'] = f"add_sw_template() for '{sw_model}' successful "
        self.common_validation.passed(**kwargs)

        return rc
