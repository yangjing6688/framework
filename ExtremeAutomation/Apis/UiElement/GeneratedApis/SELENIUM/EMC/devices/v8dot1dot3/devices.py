from ExtremeAutomation.Apis.UiElement.GeneratedApis.SELENIUM.EMC.devices.v8dot1dot2.devices import Devices as \
    DevicesBase
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils
import re


class Devices(DevicesBase):
    def devices_select_context_menu(self, ui_cmd_obj, arg_dict):
        # Open the context menu
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               '#networkPrimaryDeviceGrid button[iconCls=fa fa-bars] => .fa')

        # Parse the list of menus
        menu_list = str(arg_dict["menu_name"]).split(",")
        sub_menu_count = len(menu_list)
        current_menu = 0
        for menu in menu_list:
            current_menu += 1
            ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                          '#activeContextMenu menuitem[text=' + menu + ']', '[0]')
            if ui_cmd_obj.return_data is not None:
                ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                              '#activeContextMenu menuitem[text=' + menu + ']',
                                                              '[0].hidden')
                if ui_cmd_obj.return_data is False:
                    self.ext_builder.click(ui_cmd_obj,
                                           '#activeContextMenu menuitem[text=' + menu + '] => .x-menu-item-text')
                    if current_menu != sub_menu_count:
                        # This is a sub menu - move the mouse over to the right
                        self.ext_builder.move_cursor_x_y(ui_cmd_obj, 180, 0)
                else:
                    ui_cmd_obj.error_state = True
                    self.logger.log_info("\nMenu '" + menu + "' is not visible in the device context menu.\n")
                    break
            else:
                ui_cmd_obj.error_state = True
                self.logger.log_info("\nMenu '" + menu + "' is not present in the device context menu.\n")
                break

        return ui_cmd_obj

    def devices_collect_interface_statistics(self, ui_cmd_obj, arg_dict):
        self.devices_collect_port_statistics(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def devices_collect_port_statistics(self, ui_cmd_obj, arg_dict):
        # Select the device in the tree (note: the node must be visible/parent already expanded)
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab treeview => .x-tree-node-text '
                               ':contains(' + arg_dict['ip_address'] + ')')

        # Make sure the correct tab is selected
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               'tab[text=Summary] => .x-tab-inner-extr-sec-tab-panel')
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               'deviceViewDataPanel tab[title=Ports] => .x-tab-inner')

        # Expand the specified port group
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel treeview => '
                               '.x-grid-item:contains(' + str(arg_dict['group_name']) + ') .x-tree-expander')

        # Select the specified port
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel treeview => '
                               '.x-tree-node-text:textEquals(' + str(arg_dict['port_name']) + ')')

        # Access the context menu for the specified port
        self.ext_builder.right_click(ui_cmd_obj,
                                     '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel treeview => '
                                     '.x-tree-node-text:textEquals(' + str(arg_dict['port_name']) + ')')

        # Select the Collect Port Statistics menu
        self.ext_builder.click(ui_cmd_obj,
                               '#portTreeMenu{isVisible()} menuitem[actionId=collectInterfaceStats] => '
                               '.x-menu-item-text')

        # Populate the dialog
        self.ext_builder.click(ui_cmd_obj, "#ifHistorical => [data-ref='displayEl']")
        self.ext_builder.click(ui_cmd_obj, 'button[actionId=ifCollectionWindowOk] => .x-btn-button')

        # Collapse the specified port group
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel treeview => '
                               '.x-grid-item:contains(' + str(arg_dict['group_name']) + ') .x-tree-expander')

        return ui_cmd_obj

    def devices_confirm_context_menu_exists(self, ui_cmd_obj, arg_dict):
        # Assume we won't find the menu
        menu_exists = False

        # Open the context menu so it gets built
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               '#networkPrimaryDeviceGrid button[iconCls=fa fa-bars] => .fa')

        # Close the context menu now that it has been built by clicking the toolbar
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               '#networkPrimaryDeviceGrid toolbar(true) => .x-scroller')

        menu_list = str(arg_dict["menu_name"]).split(",")
        sub_menu_count = len(menu_list)
        current_menu = 0
        for menu in menu_list:
            current_menu += 1
            ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                          '#activeContextMenu menuitem[text=' + menu + ']', '[0]')
            if ui_cmd_obj.return_data is not None:
                ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                              '#activeContextMenu menuitem[text=' + menu + ']',
                                                              '[0].hidden')
                if ui_cmd_obj.return_data is False:
                    if current_menu == sub_menu_count:
                        menu_exists = True
                        self.logger.log_info("\nMenu '" + menu + "' is visible in the device context menu.\n")
                        break
                else:
                    self.logger.log_info("\nMenu '" + menu + "' is not visible in the device context menu.\n")
                    break
            else:
                self.logger.log_info("\nMenu '" + menu + "' is not present in the device context menu.\n")
                break

        # Pass or fail the test, based on what was expected
        if menu_exists is StringUtils.string_to_boolean(arg_dict["exists"]):
            # PASS
            ui_cmd_obj.error_state = False
        else:
            # FAIL
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def devices_device_view_select_tab(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#networkTabPanel deviceViewDataPanel tab[text=' +
                               arg_dict['tab_name'] + '] => .x-tab-inner')
        return ui_cmd_obj

    def devices_device_view_verify_vlan_name_and_tag(self, ui_cmd_obj, arg_dict):
        item = 0
        attempts = 0
        match = False
        while attempts <= int(arg_dict['max_attempts']) and not match:
            self.ext_builder.component_query(ui_cmd_obj,
                                             "#networkTabPanel deviceViewDataPanel #vlanSummaryPanel gridview",
                                             '[0].store.data.length')
            table_size = ui_cmd_obj.return_data
            while item < int(table_size) and not match:
                match = True
                if arg_dict['vlan_tag'] is not None:
                    self.ext_builder.component_query(ui_cmd_obj,
                                                     "#networkTabPanel deviceViewDataPanel #vlanSummaryPanel gridview",
                                                     '[0].store.data.items[' + str(item) + '].data.vlanTag')
                    if int(arg_dict['vlan_tag']) != int(ui_cmd_obj.return_data):
                        match = False
                        item += 1
                        continue

                if arg_dict['vlan_name'] is not None:
                    self.ext_builder.component_query(ui_cmd_obj,
                                                     "#networkTabPanel deviceViewDataPanel #vlanSummaryPanel gridview",
                                                     '[0].store.data.items[' + str(item) + '].data.vlanName')
                    if arg_dict['vlan_name'].lower() not in ui_cmd_obj.return_data.lower():
                        match = False
                        item += 1
                        continue

            attempts += 1
            item = 0
        if match != StringUtils.string_to_boolean(arg_dict['exists']):
            ui_cmd_obj.error_state = True
        return ui_cmd_obj

    def devices_device_view_verify_vlan_name_and_tag_voss(self, ui_cmd_obj, arg_dict):
        item = 0
        attempts = 0
        match = False
        while attempts <= int(arg_dict['max_attempts']) and not match:
            self.ext_builder.component_query(ui_cmd_obj,
                                             "#networkTabPanel dynamicPanel[title=VLAN Table] gridview",
                                             '[0].store.data.map[1].value.length')
            table_size = ui_cmd_obj.return_data
            while item < int(table_size) and not match:
                match = True
                if arg_dict['vlan_tag'] is not None:
                    self.ext_builder.component_query(ui_cmd_obj,
                                                     "#networkTabPanel dynamicPanel[title=VLAN Table] gridview",
                                                     "[0].store.data.map[1].value[" + str(item) + "].data[2]")
                    if int(arg_dict['vlan_tag']) != int(ui_cmd_obj.return_data):
                        match = False
                        item += 1
                        continue

                if arg_dict['vlan_name'] is not None:
                    self.ext_builder.component_query(ui_cmd_obj,
                                                     "#networkTabPanel dynamicPanel[title=VLAN Table] gridview",
                                                     "[0].store.data.map[1].value[" + str(item) + "].data[101]")
                    if arg_dict['vlan_name'].lower() not in ui_cmd_obj.return_data.lower():
                        match = False
                        item += 1
                        continue

            attempts += 1
            item = 0
        if match != StringUtils.string_to_boolean(arg_dict['exists']):
            ui_cmd_obj.error_state = True
        return ui_cmd_obj

    def devices_device_view_ports_verify_pvid(self, ui_cmd_obj, arg_dict):
        item = 0
        attempts = 0
        match = False
        while attempts <= int(arg_dict['max_attempts']) and not match:
            self.ext_builder.component_query(ui_cmd_obj, "#networkTabPanel portTreePanel treeview",
                                             '[0].store.data.length')
            table_size = ui_cmd_obj.return_data
            while item < int(table_size) and not match:
                match = True
                if arg_dict['port_name'] is not None:
                    self.ext_builder.component_query(ui_cmd_obj, "#networkTabPanel portTreePanel treeview",
                                                     '[0].store.data.items[' + str(item) + '].data.name')
                    if arg_dict['port_name'] != ui_cmd_obj.return_data:
                        match = False
                        item += 1
                        continue

                if arg_dict['pvid'] is not None:
                    self.ext_builder.component_query(ui_cmd_obj, "#networkTabPanel portTreePanel treeview",
                                                     '[0].store.data.items[' + str(item) + '].data.pvid')
                    if arg_dict['pvid'] != str(ui_cmd_obj.return_data):
                        match = False
                        item += 1
                        continue
            attempts += 1
            item = 0
        if match != StringUtils.string_to_boolean(arg_dict['exists']):
            ui_cmd_obj.error_state = True
        return ui_cmd_obj

    def devices_device_view_ports_verify_vlan_id_vlan_name_untag_tag(self, ui_cmd_obj, arg_dict):
        item = 0
        attempts = 0
        while attempts <= int(arg_dict['max_attempts']):
            self.ext_builder.component_query(ui_cmd_obj, "#networkTabPanel portTreePanel treeview",
                                             '[0].store.data.length')
            table_size = ui_cmd_obj.return_data
            while item < int(table_size):
                if arg_dict['port_name'] is not None:
                    self.ext_builder.component_query(ui_cmd_obj, "#networkTabPanel portTreePanel treeview",
                                                     '[0].store.data.items[' + str(item) + '].data.name')
                    if arg_dict['port_name'] != ui_cmd_obj.return_data:
                        item += 1
                        continue
                if arg_dict['vlan_name'] is not None:
                    self.ext_builder.component_query(ui_cmd_obj, "#networkTabPanel portTreePanel treeview",
                                                     '[0].store.data.items[' + str(item) + '].data.vlans')
                    length = 0
                    vlan_list = ui_cmd_obj.return_data.split(',')
                    vlan_list_length = len(vlan_list)
                    vlan_id = []
                    vlan_name_list = []
                    vlan_tag = []
                    while length < vlan_list_length:
                        vlan_id.append(vlan_list[length].split('[')[0])
                        vlan_name = (re.findall(r'\[(.*?)\]', vlan_list[length]))
                        vlan_name_list.append(vlan_name[0].replace("[", "").replace("]", ""))
                        vlan_tag.append(vlan_list[length].split(']')[1].strip())
                        length += 1

                    start_length = 0
                    for vlan in vlan_id:
                        if vlan == arg_dict['vlan_id']:
                            if vlan_name_list[start_length] == arg_dict['vlan_name'] and \
                                    vlan_tag[start_length].lower() == arg_dict['taggedoruntagged'].lower():
                                return ui_cmd_obj
                            else:
                                start_length += 1
                        else:
                            start_length += 1
                    ui_cmd_obj.error_state = True
                    return ui_cmd_obj
            attempts += 1
            item = 0
        ui_cmd_obj.error_state = True
        return ui_cmd_obj

    def devices_edit_device_ports_edit_row_clear_tagged(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "vlanmulticombobox[dataIndex=tagged] => .x-form-clear-trigger")
        return ui_cmd_obj

    def devices_edit_device_ports_edit_row_clear_untagged(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "vlanmulticombobox[dataIndex=untagged] => .x-form-clear-trigger")
        return ui_cmd_obj

    def devices_edit_device_reload_device(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'button[text=Reload Device] => .x-btn-inner-default-small')
        self.ext_builder.click(ui_cmd_obj, '#yes => .x-btn-inner-blue-small')

        return ui_cmd_obj

    def devices_refresh_port_status(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               'splitbutton[iconCls=fa fa-refresh] => .fa')

        return ui_cmd_obj

    def devices_device_view_ports_expand_tree(self, ui_cmd_obj, arg_dict):
        self.ext_builder.double_click(ui_cmd_obj,
                                      '#networkTabPanel portTreePanel treeview => .x-tree-node-text:contains(' +
                                      arg_dict['tab_name'] + ')')

        return ui_cmd_obj

    def devices_device_view_vlan_vlan_table_verify_tag_and_ports(self, ui_cmd_obj, arg_dict):
        item = 0
        attempts = 0
        match = False
        while attempts <= int(arg_dict['max_attempts']) and not match:
            self.ext_builder.component_query(ui_cmd_obj,
                                             "#networkTabPanel dynamicPanel[title=VLAN Table] gridview",
                                             '[0].store.data.map[1].value.length')
            table_size = ui_cmd_obj.return_data
            while item < int(table_size) and not match:
                match = True
                if arg_dict['vlan_tag'] is not None:
                    self.ext_builder.component_query(ui_cmd_obj,
                                                     "#networkTabPanel dynamicPanel[title=VLAN Table] gridview",
                                                     "[0].store.data.map[1].value[" + str(item) + "].data[2]")
                    if int(arg_dict['vlan_tag']) != int(ui_cmd_obj.return_data):
                        match = False
                        item += 1
                        continue

                if arg_dict['port_list'] is not None:
                    self.logger.log_info("VLAN tag was:" + str(ui_cmd_obj.return_data))
                    self.ext_builder.component_query(ui_cmd_obj,
                                                     "#networkTabPanel dynamicPanel[title=VLAN Table] gridview",
                                                     "[0].store.data.map[1].value[" + str(item) + "].data[102]")
                    self.logger.log_info("Port List was:" + str(ui_cmd_obj.return_data))
                    if arg_dict['port_list'].lower() == ui_cmd_obj.return_data:
                        break
                    match = False
                    item += 1
                    continue

            attempts += 1
            item = 0
        if match != StringUtils.string_to_boolean(arg_dict['exists']):
            ui_cmd_obj.error_state = True
        return ui_cmd_obj

    def devices_device_view_vlan_vlan_port_table_verify_port_and_pvid(self, ui_cmd_obj, arg_dict):
        item = 0
        match = False
        self.ext_builder.component_query(ui_cmd_obj,
                                         "#networkTabPanel dynamicPanel[title=VLAN Port Table] gridview",
                                         '[0].store.data.map[1].value.length')
        table_size = ui_cmd_obj.return_data
        while item < int(table_size) and not match:
            match = True
            if arg_dict['port_value'] is not None:
                self.ext_builder.component_query(ui_cmd_obj,
                                                 "#networkTabPanel dynamicPanel[title=VLAN Port Table] gridview",
                                                 "[0].store.data.map[1].value[" + str(item) + "].data[103]")
                if arg_dict['port_value'] != ui_cmd_obj.return_data:
                    match = False
                    item += 1
                    continue
            if arg_dict['port_pvid'] is not None:
                self.logger.log_info("Port Value was:" + str(ui_cmd_obj.return_data))
                self.ext_builder.component_query(ui_cmd_obj,
                                                 "#networkTabPanel dynamicPanel[title=VLAN Port Table] gridview",
                                                 "[0].store.data.map[1].value[" + str(item) + "].data[102]")
                self.logger.log_info("PVID Value was:" + str(ui_cmd_obj.return_data))
                if arg_dict['port_pvid'].lower() == ui_cmd_obj.return_data.lower():
                    break
                else:
                    ui_cmd_obj.error_state = True
                    return ui_cmd_obj
            match = False
            item += 1
            continue
        if match != StringUtils.string_to_boolean(arg_dict['exists']):
            ui_cmd_obj.error_state = True
        return ui_cmd_obj

    def devices_device_view_vlan_vlan_table_verify_tag_and_ports_voss(self, ui_cmd_obj, arg_dict):
        item = 0
        attempts = 0
        match = False
        while attempts <= int(arg_dict['max_attempts']) and not match:
            self.ext_builder.component_query(ui_cmd_obj,
                                             "#networkTabPanel dynamicPanel[title=VLAN Table] gridview",
                                             '[0].store.data.map[1].value.length')
            table_size = ui_cmd_obj.return_data
            while item < int(table_size) and not match:
                match = True
                if arg_dict['vlan_tag'] is not None:
                    self.ext_builder.component_query(ui_cmd_obj,
                                                     "#networkTabPanel dynamicPanel[title=VLAN Table] gridview",
                                                     "[0].store.data.map[1].value[" + str(item) + "].data[2]")
                    if int(arg_dict['vlan_tag']) != int(ui_cmd_obj.return_data):
                        match = False
                        item += 1
                        continue

                if arg_dict['port_list'] is not None:
                    self.logger.log_info("VLAN tag was:" + str(ui_cmd_obj.return_data))
                    self.ext_builder.component_query(ui_cmd_obj,
                                                     "#networkTabPanel dynamicPanel[title=VLAN Table] gridview",
                                                     "[0].store.data.map[1].value[" + str(item) + "].data[124]")
                    self.logger.log_info("Port List was:" + str(ui_cmd_obj.return_data))
                    if arg_dict['port_list'].lower() == ui_cmd_obj.return_data:
                        break
                    match = False
                    item += 1
                    continue

            attempts += 1
            item = 0
        if match != StringUtils.string_to_boolean(arg_dict['exists']):
            ui_cmd_obj.error_state = True
        return ui_cmd_obj

    def devices_device_view_vlan_vlan_port_table_verify_port_and_pvid_voss(self, ui_cmd_obj, arg_dict):
        item = 0
        match = False
        self.ext_builder.component_query(ui_cmd_obj,
                                         "#networkTabPanel dynamicPanel[title=VLAN Port Table] gridview",
                                         '[0].store.data.map[1].value.length')
        table_size = ui_cmd_obj.return_data
        while item < int(table_size) and not match:
            match = True
            if arg_dict['port_value'] is not None:
                self.ext_builder.component_query(ui_cmd_obj,
                                                 "#networkTabPanel dynamicPanel[title=VLAN Port Table] gridview",
                                                 "[0].store.data.map[1].value[" + str(item) + "].data[103]")
                if arg_dict['port_value'] != ui_cmd_obj.return_data:
                    match = False
                    item += 1
                    continue
            if arg_dict['port_pvid'] is not None:
                self.logger.log_info("Port Value was:" + str(ui_cmd_obj.return_data))
                self.ext_builder.component_query(ui_cmd_obj,
                                                 "#networkTabPanel dynamicPanel[title=VLAN Port Table] gridview",
                                                 "[0].store.data.map[3].value[" + str(item) + "].data[105]")
                self.logger.log_info("PVID Value was:" + str(ui_cmd_obj.return_data))
                if arg_dict['port_pvid'].lower() == ui_cmd_obj.return_data.lower():
                    break
                else:
                    ui_cmd_obj.error_state = True
                    return ui_cmd_obj
            match = False
            item += 1
            continue
        if match != StringUtils.string_to_boolean(arg_dict['exists']):
            ui_cmd_obj.error_state = True
        return ui_cmd_obj
