from time import sleep

from extauto.common.Screen import Screen
from extauto.common.Utils import Utils
from extauto.common.AutoActions import AutoActions

from extauto.xiq.flows.common.Navigator import Navigator
import extauto.xiq.flows.common.ToolTipCapture as tool_tip
from extauto.xiq.flows.configure.NetworkPolicy import NetworkPolicy

from extauto.xiq.elements.RouterTemplateWebElements import *


class RouterTemplate(RouterTemplateWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.navigator = Navigator()
        self.screen = Screen()
        self.nw_policy = NetworkPolicy()

    def check_router_template(self, router_template):
        """
        - Check the router template in Router template Grid
        - Keyword Usage
         - ``Check router Template  ${ROUTER_TEMPLATE_NAME}``

        :param router_template: Router Template Name ie XR200P,XR600P
        :return: True if Router Template Found on Grid else False
        """
        router_template_rows_elements = self.get_router_template_rows()
        if not router_template_rows_elements:
            return False
        for el in router_template_rows_elements:
            if router_template.upper() in el.text.upper():
                self.utils.print_info("Template Already present in the template grid")
                return True
        return False

    def navigate_to_router_settings_tab(self, nw_policy):
        """
        - To Navigate to Existing Network Policy's Router Settings Tab
        - Keyword Usage
         - ``Navigate To Router Settings Tab  ${NETWORK_POLICY_NAME}``

        :param  nw_policy: Network Policy Name
        :return: True If Navigation successful else None
        """
        self.utils.print_info("Navigating Network Policies")
        self.navigator.navigate_configure_network_policies()
        sleep(1)

        self.utils.print_info("Edit Network Policy")
        self.nw_policy.select_network_policy_in_card_view(nw_policy)
        sleep(2)

        self.utils.print_info("Click on Router Settings tab button")
        self.auto_actions.click(self.get_router_settings_tab_button())
        sleep(2)

        return True

    def add_router_template(self, nw_policy, **template_config_settings):
        """
        - Create New Router Template on Network Policy Router Settings If Not exists already
        - Keyword Usage
         - ``Add Router Template     ${NW_POLICY_NAME}     &{ROUTER_TEMPLATE_CONFIG}``

        :param  nw_policy: Network Policy Name
        :param  template_config_settings: (Config Dict) router_model,template_name,interface_name,new_port_type_config,
                                           network_allocation_config,vlan_object_config,sub_network_config
        :return: 1 if Router Template Configured Successfully
        """
        router_model = template_config_settings['router_model']
        router_template_name = template_config_settings['template_name']
        interface_name = template_config_settings['interface_name']
        port_type_settings = template_config_settings['new_port_type_config']
        network_allocation_settings = template_config_settings['network_allocation_config']
        network_vlan_settings = network_allocation_settings['vlan_object_config']
        sub_network_settings = network_allocation_settings['sub_network_config']

        self.utils.print_info("Navigating to Network Policy Router Settings Tab")
        self.navigate_to_router_settings_tab(nw_policy)
        sleep(2)

        self.utils.print_info("Click on Device Template tab button")
        self.auto_actions.click(self.get_device_template_tab())
        sleep(2)

        if self.check_router_template(router_model):
            self.utils.print_info("Template Already present in the template grid")
            return 1

        self.utils.print_info("Click on Add Router Template button")
        self.auto_actions.click(self.get_router_template_add_button())
        sleep(5)

        self.utils.print_info("select the Router Platform: ", router_model)
        router_list_items = self.get_router_template_platform_from_drop_down()
        sleep(2)
        for el in router_list_items:
            self.utils.print_info("Router template names: ", el.text.upper())
            if not el:
                pass
            if router_model.upper() in el.text.upper():
                self.auto_actions.click(el)
                break
            print(el.text)
        sleep(3)

        self.utils.print_info("Enter the Router Template Name: ", router_template_name)
        self.auto_actions.send_keys(self.get_router_template_name_textfield(), router_template_name)
        sleep(3)

        self.utils.print_info("Selecting the Interface to Add New Port Type", interface_name)
        self.select_interface_to_add_new_port_type(interface_name)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Configure New Port Type")
        self.configure_new_port_type(**port_type_settings)

        self.utils.print_info("Click on the save template button")
        self.auto_actions.click(self.get_router_template_save_button())
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        tool_tip_text = tool_tip.tool_tip_text
        self.utils.print_info("Tool tip Text Displayed on Page ", tool_tip_text)
        if "Router template has been saved successfully." not in tool_tip_text:
            return -1

        self.utils.print_info("Click Network Allocation Tab")
        self.auto_actions.click(self.get_network_allocation_tab())
        sleep(2)

        self.utils.print_info("Click Add Network Allocation")
        self.auto_actions.click(self.get_router_allocation_add_button())
        sleep(2)

        self.utils.print_info("Configure Network Vlan Object")
        self.configure_network_allocation_vlan(**network_vlan_settings)
        sleep(2)

        self.utils.print_info("Configure Sub Network Section")
        self.configure_network_allocation_sub_network(**sub_network_settings)
        sleep(2)

        return 1

    def select_interface_to_add_new_port_type(self, interface_name):
        """
        - Selects the Router Interface To Configure New Port Type.
        - Keyword Usage
         - ``Select Interface To Add New Port Type     ${INTERFACE_NAME}``

        :param interface_name: Router Interface Name ie ETH0,ETH1,ETH2
        :return: return 1 if Router Interface selected correctly else -1
        """
        self.utils.print_info("Selecting The Interface to add new port type: ", interface_name)
        sleep(5)
        rows = self.get_router_template_port_details_grid_rows()
        for row in rows:
            if interface_name in row.text:
                self.utils.print_debug("Found Interface Name Row: ", row.text)
                self.auto_actions.click(self.get_router_template_add_port_type_link_button(row))
                sleep(2)
                return 1
        return -1

    def configure_new_port_type(self, **port_type_settings):
        """
        - Configure New Port type on Router Interface
        - Keyword Usage
         - ``Configure New Port Type   &{PORT_TYPE_CONFIG}``

        :param port_type_settings: (Config Dict) port_type_name,description,port_status,port_usage_config,
                                    traffic_filter_settings

        :return: return 1 if Port type Configuration successful else -1
        """
        new_port_type_name = port_type_settings['port_type_name']
        port_description = port_type_settings['description']
        port_status = port_type_settings['port_status']
        port_usage_configuration = port_type_settings['port_usage_config']
        traffic_filters = port_type_settings['traffic_filter_settings']
        port_status_slider_button = self.get_router_new_port_status_button()

        self.utils.print_info("Enter the New Port Type Name: ", new_port_type_name)
        self.auto_actions.send_keys(self.get_router_new_port_type_name_textfield(), new_port_type_name)
        sleep(2)

        self.utils.print_info("Enter Description For New Port Type Name: ", port_description)
        self.auto_actions.send_keys(self.get_router_new_port_type_description_textfield(), port_description)
        sleep(2)

        if port_status.upper() == 'ENABLE':
            self.utils.print_info("Enabling Port Status")
            if not port_status_slider_button.is_selected():
                self.auto_actions.click(port_status_slider_button)
                sleep(2)

        if port_status.upper() == 'DISABLE':
            self.utils.print_info("Disabling Port Status")
            if port_status_slider_button.is_selected():
                self.auto_actions.click(port_status_slider_button)
            sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Configuring New Port Type Configuration")
        self.configure_port_type_config(**port_usage_configuration)

        self.utils.print_info("Configuring New Port Traffic Management")
        self.configure_new_port_traffic_filter_management(**traffic_filters)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Click Save port button")
        self.auto_actions.click(self.get_new_port_save_button())
        sleep(5)

        tool_tip_text = tool_tip.tool_tip_text
        self.utils.print_info("Tool tip Text Displayed on Page ", tool_tip_text)
        if "Port type was saved successfully." in tool_tip_text:
            return 1
        else:
            return -1

    def configure_port_type_config(self, **port_usage_configuration):
        """

        - This keyword is used to do port type configuration
        - Keyword Usage
         - ``Configure Port Type Config   &{PORT_USAGE_CONFIG}``

        :param port_usage_configuration: (Configuration Dictionary) Port Usage Configuration ie Access,Trunk,WAN
        :return: return 1 if Configuration successful else -1
        """
        if port_usage_configuration['port_usage_type'].upper() == "ACCESS":
            self.auto_actions.center_element(self.get_router_new_port_type_access_radio_button())
            self.auto_actions.click(self.get_router_new_port_type_access_radio_button())
            sleep(2)

            self.screen.save_screen_shot()
            sleep(2)

        if port_usage_configuration['port_usage_type'].upper() == "TRUNK":
            trunk_allowed_vlans = port_usage_configuration['allowed_vlans']
            self.auto_actions.center_element(self.get_router_new_port_type_trunk_radio_button())
            self.auto_actions.click(self.get_router_new_port_type_trunk_radio_button())
            sleep(2)

            self.utils.print_info("Enter Description For New Port Type Name: ", trunk_allowed_vlans)
            self.auto_actions.send_keys(
                self.get_new_port_type_trunk_allowed_vlan_textfield(), trunk_allowed_vlans)
            sleep(2)

            self.screen.save_screen_shot()
            sleep(2)

        if port_usage_configuration['port_usage_type'].upper() == "WAN":
            self.auto_actions.click(self.get_router_new_port_type_wan_radio_button())
            sleep(2)

            self.screen.save_screen_shot()
            sleep(2)

    def configure_new_port_traffic_filter_management(self, **port_type_settings):
        """
        - Configure New Port Traffic Filter Management ie SSH,Telnet,Ping,SNMP
        - Keyword Usage
         - ``Configure New Port Traffic Filter Management   &{PORT_TYPE_SETTINGS}``

        :param port_type_settings: (Configuration Dictionary) To enable/Disable Status of SSH,Telnet,Ping,SNMP
        :return: return True if Configuration successful
        """
        ssh_status = port_type_settings['ssh']
        telnet_status = port_type_settings['telnet']
        ping_status = port_type_settings['ping']
        snmp_status = port_type_settings['snmp']

        self.utils.print_info("Configuring SSH Status Section")
        if ssh_status.upper() == "ENABLE":
            if not self.get_router_new_port_type_enable_ssh_checkbox().is_selected():
                self.auto_actions.click(self.get_router_new_port_type_enable_ssh_checkbox())
        else:
            if self.get_router_new_port_type_enable_ssh_checkbox().is_selected():
                self.auto_actions.click(self.get_router_new_port_type_enable_ssh_checkbox())

        self.utils.print_info("Configuring Telnet Status Section")
        if telnet_status.upper() == "ENABLE":
            if not self.get_router_new_port_type_enable_telnet_checkbox().is_selected():
                self.auto_actions.click(self.get_router_new_port_type_enable_telnet_checkbox())
        else:
            if self.get_router_new_port_type_enable_telnet_checkbox().is_selected():
                self.auto_actions.click(self.get_router_new_port_type_enable_telnet_checkbox())

        self.utils.print_info("Configuring Ping Status Section")
        if ping_status.upper() == "ENABLE":
            if not self.get_router_new_port_type_enable_ping_checkbox().is_selected():
                self.auto_actions.click(self.get_router_new_port_type_enable_ping_checkbox())
        else:
            if self.get_router_new_port_type_enable_ping_checkbox().is_selected():
                self.auto_actions.click(self.get_router_new_port_type_enable_ping_checkbox())

        self.utils.print_info("Configuring SNMP Status Section")
        if snmp_status.upper() == "ENABLE":
            if not self.get_router_new_port_type_enable_snmp_checkbox().is_selected():
                self.auto_actions.click(self.get_router_new_port_type_enable_snmp_checkbox())
        else:
            if self.get_router_new_port_type_enable_snmp_checkbox().is_selected():
                self.auto_actions.click(self.get_router_new_port_type_enable_snmp_checkbox())

        self.screen.save_screen_shot()
        sleep(2)

        return True

    def configure_network_allocation_vlan(self, **network_allocation_vlan_settings):
        """
        - Configure Network Allocation VLAN on Router Template
        - Keyword Usage
         - ``Configure Network Allocation VLAN   &{VLAN_CONFIG_SETTINGS}``

        :param network_allocation_vlan_settings: (Config Dictionary) Vlan Name and Vlan ID
        :return: return True if Config Successful
        """
        vlan_name_field = network_allocation_vlan_settings['vlan_name']
        vlan_id_field = network_allocation_vlan_settings['vlan_id']

        self.utils.print_info("Click VLAN Object Select button")
        self.auto_actions.click(self.get_router_allocation_vlan_select_button())
        sleep(5)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Click New VLAN Object button")
        self.auto_actions.click(self.get_router_allocation_new_vlan_add_button())
        sleep(5)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info(f"Enter VLAN Name For Network Allocation: {vlan_name_field}")
        self.auto_actions.send_keys(self.get_router_allocation_new_vlan_name_input_field(), vlan_name_field)
        sleep(2)

        self.utils.print_info(f"Enter VLAN ID For Network Allocation: {vlan_name_field}")
        self.auto_actions.send_keys(self.get_router_allocation_new_vlan_id_input_field(), vlan_id_field)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Click Save VLAN button")
        self.auto_actions.click(self.get_router_allocation_new_vlan_save_button())
        sleep(5)

        self.screen.save_screen_shot()
        sleep(2)

        return True

    def configure_network_allocation_sub_network(self, **network_allocation_sub_network_settings):
        """
        - Configure network allocation sub network on Router Template
        - Keyword Usage
         - ``Configure Network Allocation Sub Network   &{SUB_NETWORK_SETTINGS}``

        :param network_allocation_sub_network_settings: (Config Dictionary) includes Basic and Advanced sub network
                                                         Parameters
        :return: return True if Configuration Successful
        """
        basic_config = network_allocation_sub_network_settings['basic_config']
        advance_config = network_allocation_sub_network_settings['advance_config']

        self.utils.print_info("Click Sub Network Select button")
        self.auto_actions.click(self.get_router_allocation_subnetwork_select_button())
        sleep(5)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Click New Sub Network button")
        self.auto_actions.click(self.get_router_allocation_new_subnetwork_add_button())
        sleep(5)

        self.screen.save_screen_shot()
        sleep(2)

        if basic_config:
            self.configure_basic_subnetwork_section(**basic_config)

        if advance_config != 'None':
            self.configure_advanced_subnetwork_section(**advance_config)

        self.utils.print_info("Saving Network Allocation Configuration")
        self.auto_actions.click(self.get_save_network_allocation_button())

        self.screen.save_screen_shot()
        sleep(2)

        return True

    def configure_basic_subnetwork_section(self, **basic_config):
        """

        - Configure Basic Subnetwork section on Router Template
        - Keyword Usage
         - ``Configure Basic Subnetwork Section   &{SUB_NETWORK_BASIC_SETTINGS}``

        :param basic_config: (Config Dictionary) include sub_network_name,sub_network_description,network_type,
                              unique_subnetwork,local_ip_address_space,gateway_options

        :return: return True if Configuration Successful
        """
        network_name = basic_config['sub_network_name']
        network_description = basic_config['sub_network_description']
        network_usage_type = basic_config['network_type']
        create_unique_subnetwork = basic_config['unique_subnetwork']
        ip_address_space = basic_config['local_ip_address_space']
        gateway_option = basic_config['gateway_options']

        self.auto_actions.click(self.get_save_subnetwork_button())
        sleep(5)

        self.utils.print_info(f"Enter Network Description For Allocation: {network_description}")
        self.auto_actions.scroll_up()
        self.auto_actions.send_keys(self.get_new_subnetwork_description_input_field(), network_description)
        sleep(3)

        self.utils.print_info(f"Enter Network Name For Allocation: {network_name}")
        self.auto_actions.send_keys(self.get_new_subnetwork_name_input_field(), network_name)
        sleep(3)

        self.utils.print_info("Click on Network Usage Type drop down")
        self.auto_actions.click(self.get_new_subnetwork_network_type_drop_down())
        sleep(3)
        key_options = self.get_new_subnetwork_network_type_drop_down_options()
        for opt in key_options:
            if network_usage_type.upper() == opt.text.upper():
                self.auto_actions.click(opt)
                sleep(2)
                break

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Configuring Create Unique Subnetwork Radio Button Section")
        if create_unique_subnetwork.upper() == "ENABLE":
            if not self.get_create_unique_subnetwork_radio_button().is_selected():
                self.auto_actions.click(self.get_create_unique_subnetwork_radio_button())
        else:
            if self.get_create_unique_subnetwork_radio_button().is_selected():
                self.auto_actions.click(self.get_create_unique_subnetwork_radio_button())

        self.utils.print_info(f"Enter Local IP Address Space: {ip_address_space}")
        self.auto_actions.send_keys(self.get_local_ip_address_space_textfield(),
                                    ip_address_space)
        sleep(2)

        self.utils.print_info("Configuring Default Gateway Options Section")
        if gateway_option.upper() == "FIRSTIP":
            self.utils.print_info("Configuring First IP as Default gateway")
            if not self.get_first_ip_as_gateway_radio_button().is_selected():
                self.auto_actions.click(self.get_first_ip_as_gateway_radio_button())
        else:
            self.utils.print_info("Configuring Last IP as Default gateway")
            self.auto_actions.click(self.get_last_ip_as_gateway_radio_button())

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Saving Sub Network Configuration")
        self.auto_actions.click(self.get_save_subnetwork_button())

        self.screen.save_screen_shot()
        sleep(2)

        return True

    def select_router_template_row(self, template_name):
        """
        - Select Router Template Name Row from Network Policy-->Router settings--> Device Template
        - Keyword Usage
         - ``Select Router Template Row   ${ROUTER_TEMPLATE_NAME}``

        :param template_name: Router Template Name
        :return: return True if Router Template Name found in the Row
        """
        self.utils.print_info("Click on default Router Template select button")
        self.auto_actions.click(self.get_default_router_template_select_button())
        sleep(2)

        rsg_rows = self.get_default_router_template_dialog_rsg_rows()
        if not rsg_rows:
            self.utils.print_info(
                "default Router Template: {} doesn't exist, Please create default".format(template_name))
            self.auto_actions.click(self.get_default_router_template_dialog_cancel_button())
            sleep(2)
            return False

        for row in rsg_rows:
            if template_name.upper() in row.text.upper():
                self.auto_actions.click(self.get_default_router_template_dialog_rsg_row_checkbox(row))
                sleep(2)
                return True

    def delete_router_template(self, nw_policy, template_name):
        """
        - Delete Router Template Name Row from Network Policy-->Router settings--> Device Template
        - Keyword Usage
         - ``Delete Router Template  ${NW_POLICY_NAME}  ${ROUTER_TEMPLATE_NAME}``

        :param nw_policy : Network Policy Name
        :param template_name: Router Template Name
        :return:  True if router Template deleted successfully else returns False
        """
        self.utils.print_info("Navigating to Network Policy Router Settings Tab")
        self.navigate_to_router_settings_tab(nw_policy)
        sleep(2)

        self.utils.print_info("Click on Device Template tab button")
        self.auto_actions.click(self.get_device_template_tab())
        sleep(2)

        if self.select_router_template_row(template_name):
            self.utils.print_info("Click delete Button to delete Router Template Name")
            self.auto_actions.click(self.get_router_template_delete_button())
            sleep(2)

            self.utils.print_info("Click Confirm Delete Button")
            self.auto_actions.click(self.get_router_template_delete_confirm_button())
            sleep(3)

            tool_tp_text = tool_tip.tool_tip_text
            self.utils.print_info(tool_tp_text)
            sleep(2)

            self.utils.print_info("Click Cancel Button")
            self.auto_actions.click(self.get_default_router_template_dialog_cancel_button())
            sleep(2)
            for value in tool_tp_text:
                if "The item was deleted successfully" in value:
                    return True
            return False
        else:
            self.utils.print_info("default Router Template :{} doesn't exist, create it..".format(template_name))
            self.auto_actions.click(self.get_default_router_template_dialog_cancel_button())
            return False

    def configure_advanced_subnetwork_section(self, **advance_config):
        """
        - Configure Advanced Subnetwork Section on Router Template
        - Keyword Usage
         - ``Configure Advanced Subnetwork Section  &{SUB_NETWORK_ADVANCED_SETTINGS}``

        :param advance_config: Config Dictionary Parameters of Subnetwork Advanced settings
        :return: return True if Config Successful
        """
        pass
