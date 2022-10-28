from time import sleep

from extauto.common.Utils import Utils
from extauto.common.AutoActions import AutoActions
from extauto.common.Screen import Screen

import extauto.xiq.flows.common.ToolTipCapture as tool_tip
from extauto.xiq.flows.common.Navigator import Navigator
from extauto.xiq.flows.configure.NetworkPolicy import NetworkPolicy
from extauto.xiq.flows.manage.Tools import Tools

from selenium.webdriver.common.keys import Keys
from extauto.xiq.elements.SwitchTemplateWebElements import SwitchTemplateWebElements
from extauto.xiq.elements.DeviceTemplateWebElements import DeviceTemplateWebElements
from extauto.xiq.elements.NetworkPolicyWebElements import NetworkPolicyWebElements
from extauto.xiq.elements.SwTemplateLegacyPortTypeWebElements import SwTemplateLegacyPortTypeWebElements

from extauto.xiq.elements.Device360WebElements import Device360WebElements
from extauto.xiq.elements.AlarmsWebElements import AlarmsWebElements
from extauto.common.CommonValidation import CommonValidation
from extauto.xiq.elements.DialogWebElements import DialogWebElements
from extauto.xiq.flows.configure.CommonObjects import CommonObjects
import re

class SwitchTemplate(object):

    def __init__(self):
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.navigator = Navigator()
        self.device_template_web_elements = DeviceTemplateWebElements()
        self.sw_template_web_elements = SwitchTemplateWebElements()
        self.np_web_elements = NetworkPolicyWebElements()
        self.nw_policy = NetworkPolicy()
        self.legacy_port_type_editor = SwTemplateLegacyPortTypeWebElements();
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
        - Assumes That Already in Network Policy Edit Page
        - Keyword Usage
         - ``Check SW Template  ${SWITCH_TEMPLATE_NAME}``

        :param sw_template: Switch Template Name ie SR2024P,X440-G2-24p-10G4 etc
        :return: True if Switch Template Found on Grid else False
        """
        self.utils.print_info("Click on Device Template tab button")
        self.auto_actions.click_reference(self.device_template_web_elements.get_add_device_template_menu)
        sleep(2)

        sw_template_rows_elements = self.sw_template_web_elements.get_sw_template_rows()
        if not sw_template_rows_elements:
            return False
        for el in sw_template_rows_elements:
            if sw_template.upper() in el.text.upper():
                self.utils.print_info("Template Already present in the template grid")
                return True
        return False

    def add_sw_template(self, nw_policy, sw_model, sw_template_name, **kwargs):
        """
        - Checks the given switch template present already in the switch Templates Grid
        - If it is not there add to the sw_template
        - Keyword Usage
         - ``Add SW Template  ${NW_POLICY}  ${SW_MODEL}   ${SW_TEMPLATE_NAME}``

        :param nw_policy: network policy
        :param sw_model: Switch Model ie SR2348P
        :param sw_template_name: Switch Template Name ie template_SR2348P

        :return: 1 if Switch Template Configured Successfully else -1
        """
        self.navigator.navigate_to_switch_templates()
        def _wait_pagination():
            return self.common_objects.cobj_web_elements.get_paze_size_element(page_size='100')
        self.utils.wait_till(_wait_pagination, timeout=30, delay=2, msg='Waiting pagination')
        self.utils.print_info("Click on full page view for switch template")
        page_size_el = self.common_objects.cobj_web_elements.get_paze_size_element(page_size='100')
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
        sleep(1)

        self.nw_policy.select_network_policy_in_card_view(nw_policy)
        sleep(2)

        self.utils.print_info("Click on Device Template tab button")
        self.auto_actions.click_reference(self.device_template_web_elements.get_add_device_template_menu)
        sleep(2)

        tab = self.sw_template_web_elements.get_sw_template_tab_button()
        if tab.is_displayed():
            self.utils.print_info("Click on Switch Templates tab")
            self.auto_actions.click(tab)
            sleep(2)

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
                        self.utils.wait_till(_is_sw_template_available, delay=0.5, is_logging_enabled=True, silent_failure=False)
                        
                        self.screen.save_screen_shot()
                        rc = 1
                        break

                self.utils.print_info("Click on network policy exit button")
                self.auto_actions.click_reference(self.np_web_elements.get_np_exit_button)
                sleep(2)

                return rc

    def get_sw_template_row(self, sw_template):
        """
        - Get the switch template row element on Network Policy's Switch Templates Grid
        - Keyword Usage
         - ``Get SW Template Row  ${SW_TEMPLATE_NAME}``

        :param sw_template: name of the sw_template
        :return: Switch Template Cell present on row
        """
        self.utils.print_info("Getting the switch template rows")

        # import sys, pdb
        # pdb.Pdb(stdout=sys.__stdout__).set_trace()

        rows = self.sw_template_web_elements.get_sw_template_rows()
        if not rows:
            self.utils.print_info("Switch templates not exists in switch device template page")
            return False
        for row in rows:
            cells = self.sw_template_web_elements.get_sw_template_row_cell(row, 'dgrid-row')
            for cell in cells:
                if sw_template in cell.text:
                    return cell

    def select_sw_template(self, nw_policy, sw_template):
        """
        - This Keyword will Select the Switch Template on Network Policy
        - Keyword Usage
         - ``Select SW Template  ${NW_POLICY_NAME}  ${SW_TEMPLATE_NAME}``

        :param nw_policy: Name of the Network Policy to select Switch Template
        :param sw_template: Name of the sw_template
        :return: 1 If successfully Selected Switch template
        """
        self.nw_policy.navigate_to_np_edit_tab(nw_policy)
        sleep(5)
        self.utils.print_info("Click on Device Template tab button")
        self.auto_actions.click_reference(self.device_template_web_elements.get_add_device_template_menu)
        sleep(2)

        tab = self.sw_template_web_elements.get_sw_template_tab_button()
        if tab.is_displayed():
            self.utils.print_info("Click on Switch Templates tab")
            self.auto_actions.click(tab)
            sleep(2)

        row = self.get_sw_template_row(sw_template)
        self.auto_actions.click(row)
        return 1

    def assign_switch_template(self, nw_policy, sw_template_name):
        """
        - Checking the sw template present in the sw Templates Grid
        - If it is not there add to the sw_template
        - Keyword Usage
         - ``Assign SW Template  ${POLICY_NAME}  ${SW_TEMPLATE_NAME}``

        :param nw_policy: Name of policy to assign the switch template to
        :param sw_template_name: Name of the switch template to assign; e.g., SR_2348P-default-template

        :return: 1 if switch template was assigned successfully, else -1
        """
        self.utils.print_info("Navigating to Network Policies")
        self.navigator.navigate_configure_network_policies()
        sleep(1)

        self.nw_policy.select_network_policy_in_card_view(nw_policy)
        sleep(2)

        self.utils.print_info("Click on Device Templates tab button")
        self.auto_actions.click_reference(self.device_template_web_elements.get_add_device_template_menu)
        sleep(2)

        tab = self.sw_template_web_elements.get_sw_template_tab_button()
        if tab.is_displayed():
            self.utils.print_info("Click on Switch Templates tab")
            self.auto_actions.click(tab)
            sleep(2)

        if self.check_sw_template(sw_template_name):
            self.utils.print_info("Template Already present in the template grid")
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

                    self.utils.print_info("Switch template successfully selected for policy")
                    return 1
                else:
                    self.utils.print_info("Could not select Switch Template row for ", sw_template_name)
                    self.utils.print_info("  -- Clicking Cancel to close Select Switch Template dialog")
                    self.auto_actions.click_reference(self.sw_template_web_elements.get_sw_template_selection_cancel_button)
                    return -1
            else:
                self.utils.print_info("Could not find Switch Template selection table")
                return -1
        else:
            self.utils.print_info("Could not click Switch Template Select button")
            return -1

    def go_to_port_configuration(self):
        nav_button = self.sw_template_web_elements.get_sw_template_port_configuration_tab()
        if nav_button:
            self.auto_actions.click(nav_button)
            return 1
        else:
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

    def verify_sw_template_port_status(self, port_list, status, default):
        element_list = self.sw_template_web_elements.get_sw_template_all_port_status()
        _port_list = self.utils.expand_port_range(port_list)
        for i in range(len(element_list)):
            e = element_list[i]
            if i+1 in _port_list:
                if status == 'Disabled' and e.is_selected():
                    self.utils.print_info("ERROR: Port ", i+1, " status is ON but should be OFF")
                    return 0
                elif status == 'Enabled' and not e.is_selected():
                    self.utils.print_info("ERROR: Port ", i+1, " status is OFF but should be ON")
                    return 0
            elif default is not None:
                if default == 'Disabled' and e.is_selected():
                    self.utils.print_info("ERROR: Port ", i+1, " status is ON but should be OFF")
                    return 0
                elif default == 'Enabled' and not e.is_selected():
                    self.utils.print_info("ERROR: Port ", i+1, " status is OFF but should be ON")
                    return 0
        return 1

    def add_5520_sw_stack_template(self, model_units, nw_policy, sw_model, sw_template_name, save_template=True):
        """
        - Checks the given STACK switch template present already in the switch Templates Grid
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

        :return: 1 if Switch Template Configured Successfully else -1
        """
        self.utils.print_info("Navigate to devices")
        self.navigator.navigate_to_devices()
        self.utils.print_info("Navigating Network Policies")
        self.navigator.navigate_configure_network_policies()
        sleep(1)

        if "Switch Engine" in model_units:
            var_type="Switch Engine "
        else:
            var_type="X440-G2-"

        if self.nw_policy.select_network_policy_in_card_view(nw_policy) == -1:
            self.utils.print_info("Not found the network policy. Make sure that it was created before ")
            return -1

        sleep(2)

        self.utils.print_debug("Click on Device Template tab button")
        self.auto_actions.click_reference(self.device_template_web_elements.get_add_device_template_menu)
        sleep(2)

        if self.check_sw_template(sw_template_name):
            self.utils.print_info(
                "Template with name {} already present in the template grid".format(sw_template_name))
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
                    self.utils.print_info("ADD button was not find")
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
                        self.utils.print_info("The model doesn't contain ",var_type)
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
                            self.utils.print_info("ADD button was not find")
                            return -1
                        if self.auto_actions.select_drop_down_options(policy_unit_items, var_type + unit):
                            self.utils.print_info("Unit was added  :", var_type + unit)
                            sleep(20)
                            self.auto_actions.click_reference(self.sw_template_web_elements.get_sw_template_name_textfield)
                        else:
                            self.utils.print_info("Unit was not added  :", var_type + unit)
                            self.auto_actions.click_reference(self.sw_template_web_elements.get_sw_template_name_textfield)
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
                                    self.utils.print_info("Found successfully message")
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
                    self.utils.print_info("User choose not to save the policy. More configs could be added")
                    return 1
            else:
                self.utils.print_info("Not found 'ADD Template' button ")
        return -1

    def check_added_sw_stack_template_units(self, model_units, sw_template_name):
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
            self.utils.print_info("The first page of template configuration is not displayed")
            return -1
        model_units_list = model_units.split(",")
        self.utils.print_info("The models from CLI are : ", model_units_list)
        model_units_list2 = []
        for cnt2 in model_units_list:
            if "-EXOS" in cnt2:
                model_units_list2.append(cnt2.replace('-EXOS', ''))
            else:
                self.utils.print_info("The model doesn't contain '-EXOS' ")
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
                    self.utils.print_info(f" Stack unit name is not correct :  {add_stack_items[index].text} ; ")
                    return -1
                index = index + 1
            self.utils.print_info(add_stack_items)
        else:
            self.utils.print_info("The units items cannot be read ")
            return -1
        return 1

    def save_stack_template(self,sw_template_name):
        """
        Flow: First page from stack template
        This function save the template after the configuration was made
        return 1 if template was saved ; else -1
        """
        first_page = self.dev360.get_sw_template_stack_first_page()
        self.utils.print_info(first_page)
        if not first_page:
            self.utils.print_info("The first page of template configuration is not displayed")
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
                self.utils.print_info("Not found 'Save template' button ")
        return rc

    def delete_stack_units_device_template(self, nw_policy, sw_template_name):
        """
        This function deletes the unit's template from a policy

        :param nw_policy: Policy name
        :param sw_template_name: template name
        :return:
        """
        self.utils.print_info("Navigate to devices")
        self.navigator.navigate_to_devices()
        self.utils.print_info("Navigating Network Policies")
        self.navigator.navigate_configure_network_policies()
        sleep(1)

        if self.nw_policy.select_network_policy_in_card_view(nw_policy) == -1:
            self.utils.print_info("Not found the network policy. Make sure that it was created")
            return -1

        sleep(2)
        self.utils.print_info("Click on Device Template tab button")
        self.auto_actions.click_reference(self.device_template_web_elements.get_add_device_template_menu)
        sleep(2)

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
            self.utils.print_info("The select button was not found")
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
                    self.utils.print_info("Confirmation button was not found")
                    return -1
            else:
                self.utils.print_info("Delete button was not found")
                return -1
        else:
            self.utils.print_info("No entry found ")
        close_button = self.sw_template_web_elements.get_sw_template_selection_close_button()
        if close_button:
            self.utils.print_info("Return: 1")
            self.auto_actions.click(close_button)
            self.utils.print_info(close_button)
        return 1

    def delete_stack_switch_template(self, nw_policy, sw_template_name):
        """
        This function is used to delete a template from a policy

       :param nw_policy:
       :param sw_template_name:
       :return: 1 if template was deleted or template doesn't exist; else -1
        """

        self.utils.print_info("Navigate to devices")
        self.navigator.navigate_to_devices()

        self.nw_policy.navigate_to_np_edit_tab(nw_policy)
        sleep(5)
        self.utils.print_info("Click on Device Template tab button")
        self.auto_actions.click_reference(self.device_template_web_elements.get_add_device_template_menu)
        sleep(2)

        self.utils.print_info("Click on switch Template tab")
        self.auto_actions.click_reference(self.sw_template_web_elements.get_sw_template_tab_button)
        sleep(2)
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
            self.utils.print_info("Delete button was not found")
            return -1
        return 1

    def check_type_sw_stack_template_units(self, model_units):
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
            self.utils.print_info("The first page of template configuration is not displayed")
            return -1
        model_units_list = model_units.split(",")
        self.utils.print_info("The models from CLI are : ", model_units_list)
        model_units_list2 = []
        for cnt2 in model_units_list:
            if "-EXOS" in cnt2:
                model_units_list2.append(cnt2.replace('-EXOS', ''))
            else:
                self.utils.print_info("The model doesn't contain '-EXOS' ")
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
                    self.utils.print_info("The models are not correct ")
                    return -1
                index = index + 1
        else:
            self.utils.print_info("The units items cannot be read ")
            return -1
        return 1

    def create_vlan_in_template(self, policy_name, template_name, port, vlan, port_type_name,stp_disable='false'):
        """
        - Create Vlan In Template
        - Keyword Usage:
         - ``Create Vlan In Template     ${policy_name}  ${template_name}  ${port}  ${vlan_number}``
        :param policy_name: Name of the policy
        :param template_name : Name of the template
        :param port : Number of the port
        :param vlan : Number of the vlan
        :param port_type_name : Name of the port type
        :return: 1 if vlan creation was successful
        """
        self.select_sw_template(policy_name,  template_name)
        self.go_to_port_configuration()
        return self.config_vlan_in_template(port, vlan, port_type_name,stp_disable)

    def create_vlan_in_stacked_template(self, nw_policy, sw_template_name, slot, port, vlan, port_type_name,stp_disable='false'):
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
        :return: 1 if vlan creation was successful
        """
        slot_index = 1
        slot_found = False
        self.select_sw_template(nw_policy, sw_template_name)
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
                return self.config_vlan_in_template(port_string, vlan, port_type_name,stp_disable)
            else:
                self.utils.print_info("Unable to locate the correct slot")
                return -1
            return -1
        else:
            self.utils.print_info("Unable to gather the list of the devices in the stack")
            return -1

    def config_vlan_in_template(self, port_string, vlan_number, port_type_name,stp_disable='false'):
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
                            self.utils.print_info("Unable to locate the Port Type Textfield")
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
                                                self.utils.print_info("Unable to locate Save Vlan Button")
                                                return -1
                                    else:
                                        self.utils.print_info("Unable to locate the Vlan Add Button")
                                        return -1

                                if stp_disable:
                                    stp_status=self.legacy_port_type_editor.get_stp_status()
                                    if stp_status:
                                        self.auto_actions.disable_check_box(stp_status)
                                    else:
                                        self.utils.print_info(f"Unable to find check box to disable STP for port")
                                        self.screen.save_screen_shot()
                                        return -1

                                self.utils.print_info("Attempting to locate Port Type Save Button")
                                port_type_save_button = self.sw_template_web_elements.get_port_type_save_button()
                                if port_type_save_button:
                                    self.utils.print_info("Clicking the Port Type Save Button")
                                    self.auto_actions.click(port_type_save_button)
                                else:
                                    self.utils.print_info("Unable to locate Port Type Save Button")
                                    return -1
                                self.utils.print_info("Attempting to locate Save Template Button")
                                save_template_button = self.sw_template_web_elements.get_switch_temp_save_button()
                                if save_template_button:
                                    self.utils.print_info("Clicking the Save Template Button")
                                    self.auto_actions.click(save_template_button)
                                else:
                                    self.utils.print_info("Unable to locate Save Template Button")
                                    return -1
                                return 1
                            else:
                                self.utils.print_info("Unable to locate the Vlan PopUp Entries")
                                return -1
                        else:
                            self.utils.print_info("Unable to locate the Vlan UI IP Button")
                            return -1
                    else:
                        self.utils.print_info("Unable to locate the Add button")
                        return -1
            # if code made it  here not match was found
            self.utils.print_info("Match for port " + port_string + " NOT found")
            return -1
        else:
            self.utils.print_info("Unable to gather port detail information and rows")
            return -1

    def create_pse_profile(self, network_policy_name, device_template_name, device_model, port_type_name, pse_profile_name, power_limit, priority, power_mode):
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
        :return: 1 if the pse profile is created and saved else -1 ;
        """
        self.nw_policy.create_switching_routing_network_policy(network_policy_name)
        self.utils.print_info("Navigating Network Policies")
        self.navigator.navigate_configure_network_policies()
        sleep(1)
        self.nw_policy.select_network_policy_in_card_view(network_policy_name)
        sleep(2)
        self.utils.print_info("Click on Device Template tab button")
        self.auto_actions.click_reference(self.device_template_web_elements.get_add_device_template_menu)
        sleep(2)
        tab = self.sw_template_web_elements.get_sw_template_tab_button()
        if tab.is_displayed():
            self.utils.print_info("Click on Switch Templates tab")
            self.auto_actions.click(tab)
            sleep(2)
        if self.check_sw_template(device_model):
            self.utils.print_info("Template Already present in the template grid")
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
                            self.utils.print_info("No inserted value found for power limit")
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
                            self.utils.print_info("No inserted value found for priority")
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
                            self.utils.print_info("No inserted value found for power mode")
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
                                self.utils.print_info("The port type was not created and the configuration not saved")
                                return -1
                        else:
                            self.utils.print_info("Ai schimbat, pune altceva... nu mai e POE status")
                            return -1
                    else:
                        self.utils.print_info("Couldn't Create New Template for selected ports")
                        return -1
                else:
                    self.utils.print_info("The Assign Button was not Found")
                    return -1
            else:
                self.utils.print_info("Select all Ports button was not found")
                return -1
        else:
            self.utils.print_info("The Port Configuration Button was not found")
            return -1

    def add_to_string(self, added_string, string):
        return added_string + " " + string[0:]

    def poe_status_button(self, network_policy_name, device_template_name, device_model, port_type_name, poe_status):
        """
        - This Function modifies, turns off or on the POE Status
        - Keyword Usage : Poe Status Button           ${NETWORK_POLICY_NAME}   ${DEVICE_TEMPLATE_NAME}  ${DEVICE_MODEL}    ${PORT_TYPE_NAME}
        :param Network Policy Name -> Name of network policy
        :param DEVICE_TEMPLATE_NAME -> Name of Device Template
        :param DEVICE_MODEL     -> Device Model that should be found in the Template list
        :param PORT_TYPE_NAME   -> String, for Device Port Type
        :param POE_STATUS       -> String, could be "on", "On", "off" or "Off"
        :return: 1 if poe status is turned off else -1 ;
        """
        self.nw_policy.create_switching_routing_network_policy(network_policy_name)
        self.utils.print_info("Navigating Network Policies")
        self.navigator.navigate_configure_network_policies()
        sleep(1)
        self.nw_policy.select_network_policy_in_card_view(network_policy_name)
        sleep(2)
        self.utils.print_info("Click on Device Template tab button")
        self.auto_actions.click_reference(self.device_template_web_elements.get_add_device_template_menu)
        sleep(2)
        tab = self.sw_template_web_elements.get_sw_template_tab_button()
        if tab.is_displayed():
            self.utils.print_info("Click on Switch Templates tab")
            self.auto_actions.click(tab)
            sleep(2)
        if self.check_sw_template(device_model):
            self.utils.print_info("Template Already present in the template grid")
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
                            self.utils.print_info("the Poe status value was not correct")
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
                                self.utils.print_info("The port type was not created and the configuration not saved")
                                return -1
                        else:
                            self.utils.print_info("The Poe Status button was not found")
                            return -1
                    else:
                        self.utils.print_info("Couldn't Create New Template for selected ports")
                        return -1
                else:
                    self.utils.print_info("The Assign Button was not Found")
                    return -1
            else:
                self.utils.print_info("Select all Ports button was not found")
                return -1
        else:
            self.utils.print_info("The Port Configuration Button was not found")
            return -1

    def poe_toggle_using_existing_port_type(self, network_policy_name, device_template_name, device_model, existing_port_type_option, poe_status):
        """
        - This Function modifies, turns off or on the POE Status on existing port type
        - Keyword Usage : Poe Status Button           ${NETWORK_POLICY_NAME}   ${DEVICE_TEMPLATE_NAME}  ${DEVICE_MODEL}    ${PORT_TYPE_NAME}
        :param Network Policy Name -> Name of network policy
        :param DEVICE_TEMPLATE_NAME -> Name of Device Template
        :param DEVICE_MODEL     -> Device Model that should be found in the Template list
        :param PORT_TYPE_NAME   -> String, for Device Port Type
        :param POE_STATUS       -> String, could be "on", "On", "off" or "Off"
        :return: 1 if poe status is turned off else -1 ;
        """
        self.nw_policy.create_switching_routing_network_policy(network_policy_name)
        self.utils.print_info("Navigating Network Policies")
        self.navigator.navigate_configure_network_policies()
        sleep(1)
        self.nw_policy.select_network_policy_in_card_view(network_policy_name)
        sleep(2)
        self.utils.print_info("Click on Device Template tab button")
        self.auto_actions.click_reference(self.device_template_web_elements.get_add_device_template_menu)
        sleep(2)
        tab = self.sw_template_web_elements.get_sw_template_tab_button()
        if tab.is_displayed():
            self.utils.print_info("Click on Switch Templates tab")
            self.auto_actions.click(tab)
            sleep(2)
        if self.check_sw_template(device_model):
            self.utils.print_info("Template Already present in the template grid")
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
                                    self.utils.print_info("the Poe status value was not correct")
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
                                    self.utils.print_info(
                                        "The port type was not created and the configuration not saved")
                                    return -1
                    else:
                        return -1

    def add_supplemental_cli_into_template(self, nw_policy, sw_template_name, s_cli_name, commands=None,
                                           navigate_to_scli=True, save_template=True):
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
                return -1

            cli_command_list = commands.split(",")
            new_line_cli_commands = "\n".join(cli_command_list)
            supple_cli_name_commands = \
                self.sw_template_web_elements.get_sw_template_supplemental_cli_commands_text()
            if supple_cli_name_commands:
                self.utils.print_info("Enter the commands  ")
                self.auto_actions.send_keys(supple_cli_name_commands, new_line_cli_commands)
            else:
                return -1

            if save_template:
                self.utils.print_info("Saving S-cli")
                if self.save_template() == -1:
                    self.utils.print_info("Failed to save S-cli")
                    return -1
            sleep(3)
            return 1
        else:
            return -1

    def select_adv_settings_tab(self, network_policy_name, device_template_name):
        """
        This function is used to select the Advanced Settings tab of a device template within a policy
        :param network_policy_name: name of policy
        :param device_template_name: name of template
        :return: 1 - if the navigation was successful ; -1 - if not
        """
        try:
            self.select_sw_template(network_policy_name, device_template_name)
            if not self.sw_template_web_elements.get_sw_template_adv_settings_tab():
                self.utils.print_info("Advanced Settings tab is not displayed!")
                return -1

            self.utils.print_info("Click on Advanced Settings tab")
            self.auto_actions.click_reference(self.sw_template_web_elements.get_sw_template_adv_settings_tab)
        except Exception as exc:
            self.utils.print_info(exc)
            return -1
        sleep(3)
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
                    self.utils.print_info("Template has been saved successfully.")
                    kwargs['pass_msg'] = "Template has been saved successfully."
                    self.common_validation.passed(**kwargs)
                    return 1
                else:
                    self.utils.print_info("Template failed to save")
                    kwargs['fail_msg'] = "Template failed to save"
                    self.screen.save_screen_shot()
                    self.common_validation.failed(**kwargs)
                    return -1

        if not found_save_button:
            self.utils.print_info("Save template button has been not found ")
            kwargs['fail_msg'] = "Save template button has been not found "
            self.screen.save_screen_shot()
            self.common_validation.failed(**kwargs)
            return -1

    def configure_oob_mgmt_int(self, nw_policy, sw_template_name, mgmtVlan="4092"):
        """
        - Checks able to configure OOB Mgmt interface
        - This function is working only if switch template already created
        - Keyword Usage
         - ``  ${NW_POLICY}  ${SW_TEMPLATE_NAME} ${MGMTVLAN}
         - e.g. configure_oob_mgmt_int bgd2 politicamea 4092
        :param nw_policy: network policy
        :param sw_template_name: Switch Template Name e.g mypolicy
        :param mgmtVlan: 4092 -vlan range need to be (1-4093)

        :return: 1 if Switch Template OOB mgmt interface Configured Successfully else -1
        """

        self.select_sw_template(nw_policy, sw_template_name)

        mgmt_int = self.sw_template_web_elements.get_mgmt_toggle_check_box()
        if mgmt_int:
            self.auto_actions.enable_check_box(mgmt_int)
            mgmt_vlan_field = self.sw_template_web_elements.get_mgmt_vlan_text_field()
            if mgmt_vlan_field:
                self.auto_actions.send_keys(mgmt_vlan_field, mgmtVlan)
            else:
                self.utils.print_info(f"Unable to find field to enter MGMT Vlan field.")
                self.screen.save_screen_shot()
                return -1
        else:
            self.utils.print_info(f"Unable to find check box to enable OOB mgmt connectivity")
            self.screen.save_screen_shot()
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
                        self.utils.print_info("Found successfully message")
                        return 1
                    else:
                        self.utils.print_info("Not found successfully message yet ")
            else:
                self.utils.print_info("Not found 'Save template' button ")
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
                                        self.utils.print_info(f"Saved. Port Type {port_type_name} has been assigned to the "
                                                              f"ports: {ports}")
                                    else:
                                        kwargs['fail_msg'] = 'Did not find the successful Trunk Port message.'
                                        self.common_validation.failed(**kwargs)
                                        return -1

                                else:
                                    self.utils.print_info("Unable to find the 'Save' button in this section!")
                                    kwargs['fail_msg'] = "Unable to find the 'Save' button in this section!"
                                    self.screen.save_screen_shot()
                                    self.common_validation.failed(**kwargs)
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
                                        self.utils.print_info("Template has been saved successfully.")
                                        kwargs['pass_msg'] = "Template has been saved successfully."
                                        self.common_validation.passed(**kwargs)
                                    else:
                                        self.utils.print_info("Successful message not found")
                                        kwargs['fail_msg'] = "Successful message not found"
                                        self.screen.save_screen_shot()
                                        self.common_validation.failed(**kwargs)
                                        return -1
                                    break
                            return rc
                        else:
                            self.utils.print_info("Did not find the save button!")
                            kwargs['fail_msg'] = "Did not find the save button!"
                            self.screen.save_screen_shot()
                            self.common_validation.failed(**kwargs)
                            return -1
        else:
            self.utils.print_info("Could not find the assign button!")
            kwargs['fail_msg'] = "Could not find the assign button!"
            self.screen.save_screen_shot()
            self.common_validation.failed(**kwargs)
            return -1

    def add_5520_sw_template(self, nw_policy, sw_model, sw_template_name, save_template=True):
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

        :return: 1 if Switch Template Configured Successfully else -1
        """
        self.utils.print_info("Navigate to devices")
        self.navigator.navigate_to_devices()
        self.utils.print_info("Navigating Network Policies")
        self.navigator.navigate_configure_network_policies()
        sleep(1)

        if self.nw_policy.select_network_policy_in_card_view(nw_policy) == -1:
            self.utils.print_info("Not found the network policy. Make sure that it was created before ")
            return -1

        sleep(2)

        self.utils.print_debug("Click on Device Template tab button")
        self.auto_actions.click_reference(self.device_template_web_elements.get_add_device_template_menu)
        sleep(2)

        tab = self.sw_template_web_elements.get_sw_template_tab_button()
        if tab.is_displayed():
            self.utils.print_info("Click on Switch Templates tab")
            self.auto_actions.click(tab)
            sleep(2)

        if self.check_sw_template(sw_template_name):
            self.utils.print_info(
                "Template with name {} already present in the template grid".format(sw_template_name))
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
                            self.utils.print_info("Found successfully message")
                            return 1
                        else:
                            self.utils.print_info("Not found successfully message yet ")
                else:
                    self.utils.print_info("Not found 'Save template' button ")
        else:
            self.utils.print_info("User choose not to save the policy. More configs could be added")
            return 1
            
    def delete_switch_template_from_policy(self, nw_policy, sw_template_name, **kwargs):
        """
        - This keyword will delete the switch template from a newtwork policy
        - Flow: Network Policies -> Edit nw_policy -> Device Templates -> Select Template -> Delete Template
        :param nw_policy: The name of the network policy
        :param sw_template_name: The name of the template
        :return: Returns 1 if template is succesfully deleted,
                 Returns -1 if network policy not found
        """
        self.utils.print_info("Navigate to devices")
        self.navigator.navigate_to_devices()
        self.utils.print_info("Navigating Network Policies")
        self.navigator.navigate_configure_network_policies()
        if self.nw_policy.select_network_policy_in_card_view(nw_policy) == -1:
            self.utils.print_info("Not found the network policy. Make sure that it was created")
            kwargs['fail_msg'] = f"Policy: {nw_policy} has not been found."
            self.screen.save_screen_shot()
            self.common_validation.failed(**kwargs)
            return -1
        self.utils.print_info("Click on Device Template tab button")
        self.auto_actions.click_reference(self.device_template_web_elements.get_add_device_template_menu)
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
                            rc = 1
                            self.utils.print_info("Template was successfully removed from policy.")
                            kwargs['pass_msg'] = "Template was successfully removed from policy."
                            self.common_validation.passed(**kwargs)
                        else:
                            self.utils.print_info("Successful message not found")
                            kwargs['fail_msg'] = "Successful message not found"
                            self.screen.save_screen_shot()
                            self.common_validation.failed(**kwargs)
                            return -1
                    else:
                        kwargs['fail_msg'] = "Delete button hasn't been found."
                        self.screen.save_screen_shot()
                        self.common_validation.failed(**kwargs)
                        return -1
            if not found:
                self.utils.print_info(f"The template {sw_template_name} is not present here, it may have been "
                                      "already deleted or it wasn't created.")
                kwargs['pass_msg'] = f"The template {sw_template_name} is not present here, it may have been " \
                                     f"already deleted or it wasn't created."
                self.common_validation.passed(**kwargs)
                return 1
        else:
            self.utils.print_info("There aren't any templates here.")
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
                    self.screen.save_screen_shot()
                    self.common_validation.failed(**kwargs)
                    return -1
                kwargs['fail_msg'] = f"Something went wrong with selecting the slot {str(slot)}"
                self.screen.save_screen_shot()
                self.common_validation.failed(**kwargs)
            else:
                self.utils.print_info("Cannot find the slot list for the stack in this template")
                kwargs['fail_msg'] = "Cannot find the slot list for the stack in this template"
                self.screen.save_screen_shot()
                self.common_validation.failed(**kwargs)
        else:
            self.utils.print_info("Unable to gather the list of the devices in the stack")
            kwargs['fail_msg'] = "Unable to gather the list of the devices in the stack"
            self.screen.save_screen_shot()
            self.common_validation.failed(**kwargs)

    def get_sw_template_row_hyperlink(self, sw_template):
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
            self.utils.print_info("Switch templates not exists in switch device template page")
            return False
        for row in rows:
            cells = self.sw_template_web_elements.get_sw_template_row_table_cells(row)
            template_cell = cells[2]
            if sw_template in template_cell.text:
                hyperlink = self.sw_template_web_elements.get_sw_template_row_cells_hyperlink(template_cell)
                return hyperlink
        return False

    def add_sw_template_from_policy_tab(self, sw_model, sw_template_name, save_template=True):
        '''
        This keyword add new template from policy tab
        :param sw_model: model of template
        :param sw_template_name: Name of template
        :param save_template: True is template will be save; else False
        :return: 1 if template has been created; else -1
        '''

        if self.check_sw_template(sw_template_name):
            self.utils.print_info(
                "Template with name {} already present in the template grid".format(sw_template_name))
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
                self.utils.print_info("The web element for name field has not been found")
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
                            self.utils.print_info("Found successfully message")
                            return 1
                        else:
                            self.utils.print_info("Not found successfully message yet ")
                else:
                    self.utils.print_info("Not found 'Save template' button ")
        else:
            self.utils.print_info("User choose not to save the policy. More configs could be added")
            return 1

    def nav_to_template_tab(self, nw_policy):
        '''
        This keyword navigate to template tab from policy

        :param nw_policy: name of policy
        :return: 1 if navigated with success; else -1
        '''

        self.utils.print_info("Navigate to devices")
        self.navigator.navigate_to_devices()
        self.utils.print_info("Navigating Network Policies")
        self.navigator.navigate_configure_network_policies()

        if self.nw_policy.select_network_policy_in_card_view(nw_policy) == -1:
            self.utils.print_info("Not found the network policy. Make sure that it was created before ")
            return -1

        self.utils.print_debug("Click on Device Template tab button")
        self.auto_actions.click(self.device_template_web_elements.get_add_device_template_menu())

        tab = self.sw_template_web_elements.get_sw_template_tab_button()
        if tab.is_displayed():
            self.utils.print_info("Click on Switch Templates tab")
            self.auto_actions.click(tab)
        return 1

    def open_template_from_policy(self, sw_template):
        '''
        This keyword open a template from template tab from policy

        :param template: template name
        :return: 1 template is opened with success; else -1
        '''
        row = self.get_sw_template_row(sw_template)
        if row:
            self.auto_actions.click(row)
            return 1
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
                    mat = re.match('(.*)(Engine)(\d+)(.*)', eachslot)
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
            mat = re.match('(.*)(Engine)(.*)', model)
            sw_model = mat.group(1) + ' ' + mat.group(2) + ' ' + mat.group(3).replace('_', '-')

        elif "G2" in model:
            model_act = model.replace('10_G4', '10G4')
            m = re.match(r'(X\d+)(G2)(.*)', model_act)
            sw_model = m.group(1) + '-' + m.group(2) + m.group(3).replace('_', '-')
        else:
            sw_model = model.replace('_', '-')
        return  sw_model,-1

    def sw_template_stack_select_slot(self, slot):
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
            for stack_item in slots_in_stack:
                if slot_index == int(slot):
                    self.utils.print_info("Slot " + str(slot) + " found in the stack, selecting the slot")
                    self.auto_actions.click(stack_item)
                    slot_found = True
                    break
                slot_index = slot_index + 1
            if not slot_found:
                self.utils.print_info("Unable to locate the correct slot")
                return -1
            return -1
        else:
            self.utils.print_info("Unable to gather the list of the devices in the stack")
            return -1

    def click_on_port_details_tab(self, **kwargs):
        """Method that click on the STP port details button in the Template Configuration
        """
        stp_tab_button, _ = self.utils.wait_till(
            func=self.sw_template_web_elements.get_sw_template_port_details_tab,
            silent_failure=True, 
            exp_func_resp=True, 
            delay=5
        )
        
        if stp_tab_button is None:
            kwargs["fail_msg"] = "Failed to get the STP port details button"
            self.common_validation.failed(**kwargs)
            return -1
        else:
            kwargs["pass_msg"] = "Successfully got the STP port details button"
            self.common_validation.passed(**kwargs)
        
        res, _ = self.utils.wait_till(
            func=lambda: self.auto_actions.click(stp_tab_button),
            exp_func_resp=True,
            delay=4,
            silent_failure=True
        )
        
        if res == 1:
            kwargs["pass_msg"] = "Successfully clicked the STP port details button"
            self.common_validation.failed(**kwargs)
        else:
            kwargs["fail_msg"] = "Failed to click the STP port details button"
            self.common_validation.passed(**kwargs)
            return -1
        return 1

    def revert_port_configuration_template_level(self, port_type, **kwargs):
        """Method that reverts all the ports to a specific port type.

        Args:
            port_type (str): the port type name
        """
        try:
            select_all_ports, _ = self.utils.wait_till(
                func=self.sw_template_web_elements.all_ports_selected,
                silent_failure=True,
                exp_func_resp=True
            )
            
            kwargs["fail_msg"] = "Failed to get the select_all_ports button"
            kwargs["pass_msg"] = "Successfully got the select_all_ports button"
            self.common_validation.validate(bool(select_all_ports), True, **kwargs)
        
            res, _ = self.utils.wait_till(
                func=lambda: self.auto_actions.click(select_all_ports),
                exp_func_resp=True,
                delay=4
            )
            if res == 1:
                kwargs["pass_msg"] = "Successfully clicked the select_all_ports button"
                self.common_validation.passed(**kwargs)
            else:
                kwargs["fail_msg"] = "Failed to click the select_all_ports button"
                self.common_validation.failed(**kwargs)
                return -1
            
            assign_to_all_ports_selected, _ = self.utils.wait_till(
                func=
                self.sw_template_web_elements.assign_all_ports_selected,
                silent_failure=True, 
                exp_func_resp=True, 
                delay=5
            )
            
            if assign_to_all_ports_selected:
                kwargs["pass_msg"] = "Successfully got the assign_to_all_ports_selected button"
                self.common_validation.passed(**kwargs)
            else:
                kwargs["fail_msg"] = "Failed to get the assign_to_all_ports_selected button"
                self.common_validation.failed(**kwargs)
                return -1
            
            res, _ = self.utils.wait_till(
                func=lambda: self.auto_actions.click(assign_to_all_ports_selected),
                exp_func_resp=True,
                delay=4
            )

            if res == 1:
                self.common_validation.passed(**kwargs)
                kwargs["pass_msg"] = "Successfully clicked the assign_to_all_ports_selected button"
            else:
                kwargs["fail_msg"] = "Failed to click the assign_to_all_ports_selected button"
                self.common_validation.failed(**kwargs)
                return -1
            
            assign_button, _ = self.utils.wait_till(
                func=self.sw_template_web_elements.get_sw_template_assign_choose_existing,
                silent_failure=True, 
                exp_func_resp=True, 
                delay=5
            )
            
            if not assign_button:
                kwargs["fail_msg"] = "Failed to get the assign_button button"
                self.common_validation.failed(**kwargs)
                return -1
            else:
                kwargs["pass_msg"] = "Successfully got the assign_button button"
                self.common_validation.passed(**kwargs)
            
            res, _ = self.utils.wait_till(
                func=lambda: self.auto_actions.click(assign_button),
                exp_func_resp=True,
                delay=4
            )
            
            if res != 1:
                kwargs["fail_msg"] = "Failed to click the assign_button button"
                self.common_validation.failed(**kwargs)
                return -1
            else:
                kwargs["pass_msg"] = "Successfully clicked the assign_button button"
                self.common_validation.passed(**kwargs)
            
            radio_buttons, _ = self.utils.wait_till(
                func=self.sw_template_web_elements.get_sw_template_all_port_type_list_radio,
                silent_failure=True,
                exp_func_resp=True,
                timeout=40,
                delay=5
            )
            
            if not radio_buttons:
                kwargs["fail_msg"] = "Failed to get the radio_buttons"
                self.common_validation.failed(**kwargs)
                return -1
            else:
                kwargs["pass_msg"] = "Successfully got the radio_buttons"
                self.common_validation.passed(**kwargs)

            radio_buttons_labels, _ = self.utils.wait_till(
                func=self.sw_template_web_elements.get_sw_template_all_port_type_list_label,
                silent_failure=True,
                exp_func_resp=True,
                delay=5
            
            )
            
            if not radio_buttons_labels:
                kwargs["fail_msg"] = "Failed to get the radio_buttons_labels"
                self.common_validation.failed(**kwargs)
                return -1
            else:
                kwargs["pass_msg"] = "Successfully got the radio_buttons_labels"
                self.common_validation.passed(**kwargs)
            
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
                self.common_validation.failed(**kwargs)
                return -1
            
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
        """
        stp_tab_button, _ = self.utils.wait_till(
            func=self.sw_template_web_elements.get_sw_template_stp_tab,
            silent_failure=True,
            exp_func_resp=True,
            delay=5
        )
        
        if not stp_tab_button:
            kwargs["fail_msg"] = "Failed to get the STP tab button"
            self.common_validation.failed(**kwargs)
            return -1
        else:
            kwargs["pass_msg"] = "Successfully got the STP tab button"
            self.common_validation.passed(**kwargs)
        
        res, _ = self.utils.wait_till(
            func=lambda: self.auto_actions.click(stp_tab_button),
            exp_func_resp=True,
            silent_failure=True,
            delay=4
        )

        if res == 1:
            kwargs["pass_msg"] = "Successfully clicked the STP tab button"
            self.common_validation.passed(**kwargs)
        else:
            kwargs["fail_msg"] = "Failed to click the STP tab button"
            self.common_validation.failed(**kwargs)
            return -1
        
        return 1

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
        return row

    def navigate_to_slot_template(self, slot, **kwargs):
        """Method that navigates to the template configuration of a given stack slot.

        Args:
            slot (int): the stack slot

        Returns:
            int: 1 if successful else -1
        """
        template_slot = self.sw_template_web_elements.get_template_slot(slot=slot)
        if not template_slot:
            kwargs["fail_msg"] = f"Failed to get the template for slot {slot}"
            self.common_validation.failed(**kwargs)
            return -1
        
        kwargs["pass_msg"] = f"Successfully got the template for slot {slot}"
        self.common_validation.passed(**kwargs)
        
        if self.auto_actions.click(template_slot) != 1:
            kwargs["fail_msg"] = f"Failed to click on the tempalte slot {slot}"
            self.common_validation.failed(**kwargs)
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
        
        kwargs["fail_msg"] = f"Failed to get path cost element"
        kwargs["pass_msg"] = f"Successfully got the path cost element"
        self.common_validation.validate(bool(cost_element), True, **kwargs)
        
        return cost_element.get_attribute("value")

    def verify_path_cost_in_port_configuration_stp_tab(self, template_switch, network_policy, port, path_cost, slot=None, **kwargs):
        """Method that verifies the path cost of a given port.

        Args:
            template_switch (str): the name of the template switch
            network_policy (str): the name of the network policy
            port (str): the port of the switch
            path_cost (): the expected path cost value
            slot (str, optional): the stack slot. Defaults to None.
        """
        
        self.utils.print_info(f"Go to the port configuration of {template_switch} template")
        self.select_sw_template(
            network_policy, template_switch)
        self.go_to_port_configuration()
        if slot is not None:
            required_slot = template_switch + "-" + slot
            self.navigate_to_slot_template(required_slot)
        self.click_on_stp_tab()
        
        found_path_cost_value = self.get_path_cost_value_from_stp_port_configuration_row(
            port)
        
        if str(found_path_cost_value) != str(path_cost):
            kwargs["fail_msg"] = f"In XIQ port configuration: Expected path cost for port='{port}' is {path_cost} " \
                                f"but found {found_path_cost_value}"
            self.common_validation.failed(**kwargs)
            return -1
        
        kwargs["pass_msg"] = f"Successfully found the expected path cost"
        self.common_validation.passed(**kwargs)
        return 1

    def set_stp(self, enable=True, **kwargs):
        """Method that enables the STP in Template Configuration.

        Args:
            enable (bool, optional): If it is True then it will enable STP; if it is False then it will disable STP. Defaults to True.
        """
        button, _ = self.utils.wait_till(
            func=self.sw_template_web_elements.get_sw_template_enable_spanningtree, 
            exp_func_resp=True, 
            silent_failure=True, 
            delay=5
        )
        
        if not button:
            kwargs["fail_msg"] = f"Failed to get stp button element"
            self.common_validation.failed(**kwargs)
            return -1
        
        kwargs["pass_msg"] = f"Successfully got the stp button element"
        self.common_validation.passed(**kwargs)
        
        if (not button.is_selected() and enable) or (
            button.is_selected() and not enable):
            res, _ = self.utils.wait_till(
                func=lambda: self.auto_actions.click(button),
                exp_func_resp=True,
                delay=4
            )
            
            if res != 1:
                kwargs["fail_msg"] = f"Failed to click stp button element"
                self.common_validation.failed(**kwargs)
                return -1
            
            kwargs["pass_msg"] = f"Successfully clicked the stp button element"
            self.common_validation.passed(**kwargs)
        return 1

    def choose_stp_mode(self, mode, **kwargs):
        """Method that choses the STP mode in Template Configuration.

        Args:
            mode (str): the STP mode
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
            self.common_validation.failed(**kwargs)
            return -1
            
        kwargs["pass_msg"] = f"Successfully got the {mode} stp mode button"
        self.common_validation.passed(**kwargs)
        
        res, _ = self.utils.wait_till(
            func=lambda: self.auto_actions.click(button),
            exp_func_resp=True,
            delay=4
        )

        if res != 1:
            kwargs["fail_msg"] = f"Failed to click the {mode} stp mode button"
            self.common_validation.failed(**kwargs)
            return -1
        
        kwargs["pass_msg"] = f"Successfully clicked the {mode} stp mode button"
        self.common_validation.passed(**kwargs)
        return 1
