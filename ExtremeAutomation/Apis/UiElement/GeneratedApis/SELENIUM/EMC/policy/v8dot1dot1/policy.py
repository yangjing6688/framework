from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as PolicyBase
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


class Policy(PolicyBase):
    def click_emc_control_menu(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               '#leftNavToolbar button[text=Control] => .x-btn-inner-extr-nav-toolbar-button-small')
        return ui_cmd_obj

    def click_emc_policy_tab(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'tab[text=Policy] => .x-tab-inner-extr-main-tab-panel')
        return ui_cmd_obj

    def policy_create_role(self, ui_cmd_obj, arg_dict):
        self.ext_builder.right_click(ui_cmd_obj, '#policyNavTab #PolicyDomainView #policyTree treeview => '
                                                 '.x-tree-node-text:textEquals(Roles)')
        self.ext_builder.click(ui_cmd_obj, 'menuitem(true) => .x-menu-item-text:contains(Create Role)')
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['role_name']),
                                    '#renameObjectWin #renameValue => .x-form-text')
        self.ext_builder.click(ui_cmd_obj, '#renameObjectWin button[text=OK] => .x-btn-inner-blue-small')

        self.policy_save_domain(ui_cmd_obj, arg_dict)
        return ui_cmd_obj

    def policy_open_domain(self, ui_cmd_obj, arg_dict):
        # Access the "Open/Manage Domain(s)> Open Domain" menu
        self.ext_builder.click(ui_cmd_obj, '#policyNavTab #PolicyDomainView #manageDomainsButtonId => '
                                           '.x-btn-inner-default-toolbar-small')
        self.ext_builder.click(ui_cmd_obj, '#policyNavTab #PolicyDomainView #manageDomainsButtonId '
                                           '#ManageDomainContextMenuId menuitem[text=Open Domain] => .x-menu-item-text')

        # Move the cursor over to the Default Policy Domain choice, which should be the top pick
        self.ext_builder.move_cursor(ui_cmd_obj,
                                     '#policyNavTab #PolicyDomainView #manageDomainsButtonId '
                                     '#ManageDomainContextMenuId #domainListMenu menuitem[text=Default Policy Domain]'
                                     ' => .x-menu-item-text')

        # TO DO: make sure policy domain exists in list
        self.logger.log_info("\nTO DO: Make sure policy domain '" + arg_dict['domain_name'] + "' exists.\n")

        # Select the specified policy domain
        self.ext_builder.click(ui_cmd_obj,
                               '#policyNavTab #PolicyDomainView #manageDomainsButtonId #ManageDomainContextMenuId '
                               '#domainListMenu menuitem[text=' + arg_dict['domain_name'] + '] => .x-menu-item-text')

        return ui_cmd_obj

    def policy_save_domain(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#policyNavTab #PolicyDomainView #manageDomainsButtonId => '
                                           '.x-btn-inner-default-toolbar-small')
        self.ext_builder.click(ui_cmd_obj, '#policyNavTab #PolicyDomainView #manageDomainsButtonId '
                                           '#ManageDomainContextMenuId #domainSaveButton => .x-menu-item-text')
        self.ext_builder.click(ui_cmd_obj, '#ok => .x-btn-inner-blue-small')
        self.ext_builder.delay(ui_cmd_obj, '2000')
        return ui_cmd_obj

    def policy_add_device_to_domain_menu(self, ui_cmd_obj, arg_dict):

        self.ext_builder.click(ui_cmd_obj, '#policyNavTab #PolicyDomainView #manageDomainsButtonId => '
                                           '.x-btn-inner-default-toolbar-small')
        self.ext_builder.delay(ui_cmd_obj, 2000)
        self.ext_builder.click(ui_cmd_obj, '#policyNavTab #PolicyDomainView #manageDomainsButtonId '
                                           '#ManageDomainContextMenuId #deviceDomainAssignMenu => .x-menu-item-text')
        self.ext_builder.delay(ui_cmd_obj, 2000)
        self.ext_builder.click(ui_cmd_obj, '#assignDevicesToDomainPanel #devDomAssignTree button[text=Add Device] => '
                                           '.x-btn-inner-default-toolbar-small')
        self.ext_builder.click(ui_cmd_obj, 'addDeviceWindow[title=Add Device] button[text=Close] => '
                                           '.x-btn-inner-default-small')
        # Select Device in All Devices now that it is expanded
        self.ext_builder.click(ui_cmd_obj, '#assignDevicesToDomainPanel panel[title=Devices] #devDomAssignTree => '
                                           '.x-grid-cell:contains(' + str(arg_dict['device_ip']) + ')')
        self.ext_builder.click(ui_cmd_obj, '#assignDevicesToDomainPanel panel button[text=&#9658;] => .x-btn-button')
        self.ext_builder.click(ui_cmd_obj, r'window[title=Assign Device\(s\) to Domain] button[text=OK] => '
                                           r'.x-btn-inner-blue-small')
        # Added delay so handle device getting added to the domain... Reads Device which could be the reason the
        # policy_save_domain method doesn't work well
        self.ext_builder.delay(ui_cmd_obj, 5000)
        self.policy_save_domain(ui_cmd_obj, arg_dict)
        return ui_cmd_obj

    def policy_create_local_service(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#policyNavTab #PolicyDomainView #policyTree treeview => '
                                           '.x-tree-expander')
        self.ext_builder.click(ui_cmd_obj, '#policyNavTab #PolicyDomainView #policyTree treeview => '
                                           '.x-tree-elbow-plus')
        self.ext_builder.right_click(ui_cmd_obj, '#policyNavTab #PolicyDomainView #policyTree treeview => '
                                                 '.x-tree-node-text:textEquals(Services)')
        self.ext_builder.click(ui_cmd_obj, 'menuitem(true) => .x-menu-item-text:contains(Create Service)')
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['service_name']),
                                    '#renameObjectWin #renameValue => .x-form-text')
        self.ext_builder.click(ui_cmd_obj, '#renameObjectWin button[text=OK] => .x-btn-inner-blue-small')

        self.policy_save_domain(ui_cmd_obj, arg_dict)
        return ui_cmd_obj

    def policy_create_rule(self, ui_cmd_obj, arg_dict):
        self.ext_builder.right_click(ui_cmd_obj,
                                     '#policyNavTab #PolicyDomainView #policyTree treeview => '
                                     '.x-tree-node-text:textEquals(' + str(arg_dict['service_name']) + ')')
        self.ext_builder.click(ui_cmd_obj, 'menuitem(true) => .x-menu-item-text:contains(Create Rule)')
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['rule_name']),
                                    '#createRuleWin #createRuleNameValue => .x-form-text')
        self.ext_builder.click(ui_cmd_obj, '#createRuleWin button[text=OK] => .x-btn-inner-blue-small')

        self.policy_save_domain(ui_cmd_obj, arg_dict)
        return ui_cmd_obj

    def policy_add_service_to_role(self, ui_cmd_obj, arg_dict):
        self.ext_builder.right_click(ui_cmd_obj, '#policyNavTab #PolicyDomainView #policyTree treeview => '
                                                 '.x-tree-node-text:textEquals(' + str(arg_dict['role_name']) + ')')
        self.ext_builder.click(ui_cmd_obj, r'menuitem(true) => .x-menu-item-text:contains(Add\/Remove Service)')
        self.ext_builder.click(ui_cmd_obj, '#allAvailableServicesTree treeview => .x-tree-node-text:textEquals(' +
                                           str(arg_dict['service_name']) + ')')
        self.ext_builder.click(ui_cmd_obj, r'button[text=\&\#9658\;] => .x-btn-inner-gray-small')
        self.ext_builder.click(ui_cmd_obj, r'window[title=Add\/Remove Services] button[text=OK] => '
                                           r'.x-btn-inner-blue-small')

        self.policy_save_domain(ui_cmd_obj, arg_dict)
        return ui_cmd_obj

    def policy_rule_set_application_group(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#policyNavTab #PolicyDomainView #policyTree treeview => '
                                           '.x-tree-node-text:textEquals(' + str(arg_dict['rule_name']) + ')')
        self.ext_builder.click(ui_cmd_obj, '#policyNavTab #PolicyDomainView #domainNodeDetailsPanelContainer '
                                           '#editServiceRuleTrafficDescriptionButton => .x-btn-inner-default-small')
        self.ext_builder.click(ui_cmd_obj, '#tdEditMainPanel #applicationRulePanel #appGroupNameCombo => '
                                           '.x-form-trigger')
        self.ext_builder.click(ui_cmd_obj, '#tdEditMainPanel #applicationRulePanel #appGroupNameCombo '
                                           'boundlist => :textEquals(' + str(arg_dict['application_group']) +
                                           ')')
        self.ext_builder.click(ui_cmd_obj, '#editRuleOkBtn => .x-btn-inner-blue-small')

        return ui_cmd_obj

    def policy_rule_set_application(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#policyNavTab #PolicyDomainView #policyTree treeview => '
                                           '.x-tree-node-text:textEquals(' + str(arg_dict['rule_name']) + ')')
        self.ext_builder.click(ui_cmd_obj, '#policyNavTab #PolicyDomainView #domainNodeDetailsPanelContainer '
                                           '#editServiceRuleTrafficDescriptionButton => .x-btn-inner-default-small')
        self.ext_builder.click(ui_cmd_obj, '#tdEditMainPanel #applicationRulePanel #appNameCombo => .x-form-trigger')
        self.ext_builder.click(ui_cmd_obj, '#tdEditMainPanel #applicationRulePanel #appNameCombo boundlist => '
                                           'div:textEquals(' + arg_dict['application'] + ')')
        self.ext_builder.click(ui_cmd_obj, '#editRuleOkBtn => .x-btn-inner-blue-small')
        return ui_cmd_obj

    def policy_delete_role(self, ui_cmd_obj, arg_dict):
        self.ext_builder.right_click(ui_cmd_obj, '#policyNavTab #PolicyDomainView #policyTree treeview => '
                                                 '.x-tree-node-text:textEquals(' + str(arg_dict['role_name']) + ')')
        self.ext_builder.click(ui_cmd_obj, 'menu(true){isVisible()} menuitem[text=Delete] => .x-menu-item-text')
        self.ext_builder.click(ui_cmd_obj, '#yes => .x-btn-inner-blue-small')

        self.policy_save_domain(ui_cmd_obj, arg_dict)
        return ui_cmd_obj

    def policy_create_vlan(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#policyNavTab #PolicyDomainView #policyDomainViewNavigationTrees '
                                           '#policyTreesPanel #vlanTree title => .x-title-text')
        self.ext_builder.right_click(ui_cmd_obj, '#policyNavTab #PolicyDomainView #policyDomainViewNavigationTrees '
                                                 '#policyTreesPanel #vlanTree treeview => .x-grid-tree-node-expanded '
                                                 '.x-tree-node-text')
        self.ext_builder.click(ui_cmd_obj, 'menuitem[text=Create VLAN...] => .x-menu-item-text')
        self.ext_builder.enter_text(ui_cmd_obj, arg_dict['vlan_name'],
                                    '#CreateVlanWin #VlanNameValueSet => .x-form-text')
        self.ext_builder.enter_text(ui_cmd_obj, arg_dict['vlan_id'], '#CreateVlanWin #VlanVidValueSet => .x-form-text')
        self.ext_builder.click(ui_cmd_obj, '#CreateVlanWin #createVlanOkBtn => .x-btn-inner-blue-small')

        return ui_cmd_obj

    def policy_add_device_to_domain(self, ui_cmd_obj, arg_dict):
        # Select Devices/Port Groups Tree Header
        # If collapsed then expand.

        self.ext_builder.component_query(ui_cmd_obj, '[itemId=devicePortTreesPanel]', '[0].collapsed')
        if ui_cmd_obj.return_data:
            self.ext_builder.click(ui_cmd_obj, '#policyNavTab #PolicyDomainView panel #devicePortTreesPanel header '
                                               'title[text=Devices/Port Groups] => .x-title-text')

        # Click Deices Tab then Choose by IP by default then right click and choose Add Device TO Domain menu item
        self.ext_builder.click(ui_cmd_obj, '#policyNavTab #PolicyDomainView #policyDomainViewNavigationTrees '
                                           '#policyTreesPanel #devicePortTreesPanel tab[title=Devices] => .x-tab-inner')
        self.ext_builder.click(ui_cmd_obj, '#policyNavTab #PolicyDomainView #policyDomainViewNavigationTrees '
                                           '#policyTreesPanel #devicePortTreesPanel #deviceTree otreeselectorcombo => '
                                           '.x-form-trigger')
        self.ext_builder.click(ui_cmd_obj, '#policyNavTab #PolicyDomainView #policyDomainViewNavigationTrees '
                                           '#policyTreesPanel #devicePortTreesPanel #deviceTree otreeselectorcombo '
                                           'boundlist => :textEquals(by IP)')

        self.ext_builder.right_click(ui_cmd_obj, '#policyNavTab #PolicyDomainView #policyDomainViewNavigationTrees '
                                                 '#policyTreesPanel #devicePortTreesPanel #deviceTree treeview => '
                                                 '.x-tree-node-text:contains(IP)')
        # self.ext_builder.move_cursor(ui_cmd_obj,"menuitem[text=Assign Device\(s\) to
        # Domain\.\.\.]:ariadne-nth-child(1) => .x-menu-item-text")
        self.ext_builder.click(ui_cmd_obj, '#activeContextMenu{isVisible()} '
                                           'menuitem[actionId="deviceDomainAssignMenu"] => .x-menu-item-text')
        self.ext_builder.click(ui_cmd_obj, '#activeContextMenu{isVisible()} '
                                           'menuitem[actionId="deviceDomainAssignMenu"] => .x-menu-item-text')
        # self.ext_builder.click(ui_cmd_obj,"menuitem[text=Assign Device\(s\) to
        # Domain\.\.\.]:ariadne-nth-child(1) => .x-menu-item-text")
        self.ext_builder.delay(ui_cmd_obj, "2000")

        # Issue with EMC where expander does not work properly
        # self.ext_builder.click(ui_cmd_obj,'#assignDevicesToDomainPanel panel[title=Devices] #devDomAssignTree =>
        # .x-grid-item:contains(All Devices).x-tree-expander')
        # Two lines below are the workaround for the treeview exander... Basically Click the Add Device button which
        # expands All Devices ... Then close the dialog and move on
        self.ext_builder.click(ui_cmd_obj, '#assignDevicesToDomainPanel #devDomAssignTree button[text=Add Device] => '
                                           '.x-btn-inner-default-toolbar-small')
        self.ext_builder.click(ui_cmd_obj, 'addDeviceWindow[title=Add Device] button[text=Close] => '
                                           '.x-btn-inner-default-small')
        # Select Device in All Devices now that it is expanded
        self.ext_builder.click(ui_cmd_obj, '#assignDevicesToDomainPanel panel[title=Devices] #devDomAssignTree => '
                                           '.x-grid-cell:contains(' + str(arg_dict['device_ip']) + ')')
        self.ext_builder.click(ui_cmd_obj, '#assignDevicesToDomainPanel panel button[text=&#9658;] => .x-btn-button')
        self.ext_builder.click(ui_cmd_obj, r'window[title=Assign Device\(s\) to Domain] button[text=OK] => '
                                           r'.x-btn-inner-blue-small')

        return ui_cmd_obj

    def policy_add_ports_to_domain(self, ui_cmd_obj, arg_dict):

        # Select Devices/Port Groups Tree Header
        # If collapsed then expand.

        self.ext_builder.component_query(ui_cmd_obj, '[itemId=devicePortTreesPanel]', '[0].collapsed')
        if ui_cmd_obj.return_data == 'true':
            self.ext_builder.click(ui_cmd_obj, '#policyNavTab #PolicyDomainView panel #devicePortTreesPanel header '
                                               'title[text=Devices/Port Groups] => .x-title-text')

        self.ext_builder.click(ui_cmd_obj, '#policyNavTab #PolicyDomainView #policyDomainViewNavigationTrees '
                                           '#policyTreesPanel #devicePortTreesPanel tab[title=Port Groups] => '
                                           '.x-tab-inner')
        self.ext_builder.right_click(ui_cmd_obj, '#policyNavTab #PolicyDomainView #policyDomainViewNavigationTrees '
                                                 '#policyTreesPanel #devicePortTreesPanel #portGroupTree treeview => '
                                                 '.x-tree-node-text:contains(Port Groups)')
        self.ext_builder.click(ui_cmd_obj, r'menuitem(true) => .x-menu-item-text:contains(Create Port Group\.\.\.)')
        self.ext_builder.delay(ui_cmd_obj, "2000")
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['port_group_name']), '#renameObjectWin #renameValue => '
                                                                                  '.x-form-text')
        self.ext_builder.click(ui_cmd_obj, '#renameObjectWin button[text=OK] => .x-btn-inner-blue-small')
        self.ext_builder.right_click(ui_cmd_obj, '#policyNavTab #PolicyDomainView #policyDomainViewNavigationTrees '
                                                 '#policyTreesPanel #devicePortTreesPanel #portGroupTree treeview => '
                                                 '.x-tree-node-text:contains(' + str(arg_dict['port_group_name']) + ')')
        self.ext_builder.click(ui_cmd_obj, r'menu(true) =>.x-menu-item-text:contains(Add\/Remove Ports\.\.\.)')
        self.ext_builder.double_click(ui_cmd_obj, '#addRemovePortGroupPortsWindow #groupAddPortsLeftTree treeview => '
                                                  '.x-tree-node-text:contains(' + str(arg_dict['device_ip']) + ')')
        self.ext_builder.double_click(ui_cmd_obj, '#addRemovePortGroupPortsWindow #groupAddPortsLeftTree treeview => '
                                                  '.x-tree-node-text:contains(Switch)')
        # ADDED CODE FOR TEST COMMIT
        # self.ext_builder.click(ui_cmd_obj,
        #                                '#addRemovePortGroupPortsWindow #groupAddPortsLeftTree treeview =>
        # .x-tree-node-text:contains(1:3)', shift=True)
        # self.ext_builder.click(ui_cmd_obj,
        #                                '#addRemovePortGroupPortsWindow #groupAddPortsLeftTree treeview =>
        # .x-tree-node-text:contains(1:7)', shift=True)

        # self.ext_builder.click(ui_cmd_obj,
        #                                '#addRemovePortGroupPortsWindow #groupAddPortsLeftTree treeview =>
        # .x-tree-node-text:contains(1:3)',
        #                                ctrl=True)
        # self.ext_builder.click(ui_cmd_obj,
        #                                '#addRemovePortGroupPortsWindow #groupAddPortsLeftTree treeview =>
        # .x-tree-node-text:contains(1:7)',
        #                                ctrl=False)

        # arrPorts = str(arg_dict['ports']).split(",")
        # arrShiftKey = []
        # arrCtrlKey = []
        # shiftNode =
        # # arrCtrlNode = []
        # #
        # for port in arrPorts:
        #     if "-" in port:
        #         arrShiftKey.append(port)
        #     else:
        #         arrCtrlKey.append(port)
        # # if arrShiftKey.count() > 1:
        # # for shiftNode in arrShiftKey:
        # #
        # print str(arrShiftKey)
        # print str(arrCtrlKey)
        #
        # shiftArrayCount = len(arrShiftKey)
        # print "shift array count: " + str(shiftArrayCount)
        # for i in xrange(len(shiftArrayCount)):
        #

        # options : { ctrlKey : true }
        #

        return ui_cmd_obj

    def policy_enforce_domain(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#policyNavTab #PolicyDomainView #manageDomainsButtonId => '
                                           '.x-btn-inner-default-toolbar-small')
        self.ext_builder.click(ui_cmd_obj, '#policyNavTab #PolicyDomainView #manageDomainsButtonId '
                                           '#ManageDomainContextMenuId #domainEnforceButton => .x-menu-item-text')
        self.ext_builder.click(ui_cmd_obj, 'button[itemId=yes] => .x-btn-inner-blue-small')
        # yes the name value is in fact "blah"
        self.ext_builder.click(ui_cmd_obj, 'button[name=blah] => .x-btn-inner-blue-small')
        self.ext_builder.delay(ui_cmd_obj, "2000")
        self.ext_builder.click(ui_cmd_obj, 'button[itemId=yes] => .x-btn-inner-blue-small')
        self.ext_builder.delay(ui_cmd_obj, "2000")
        self.ext_builder.click(ui_cmd_obj, 'button[itemId=yes] => .x-btn-inner-blue-small')
        self.ext_builder.click(ui_cmd_obj, 'button[itemId=ok] => .x-btn-inner-blue-small')
        return ui_cmd_obj

    def policy_rule_navigate_to_rule_name(self, ui_cmd_obj, arg_dict):
        # CLICK CONTROL MENU ITEM
        self.click_emc_control_menu(ui_cmd_obj, arg_dict)
        # self.ext_builder.click(ui_cmd_obj,'#leftNavToolbar button[text=Control] =>
        # .x-btn-inner-extr-nav-toolbar-button-small')
        # CLICK POLICY TAB UNDER CONTROL MENU ITEM
        self.click_emc_policy_tab(ui_cmd_obj, arg_dict)
        self.ext_builder.click(ui_cmd_obj, 'tab[text=Policy] => .x-tab-inner-extr-main-tab-panel')

        # FIND SERVICE IN TREE AND DOUBLE CLICK TO EXPAND
        self.ext_builder.double_click(ui_cmd_obj, '#policyNavTab #PolicyDomainView #policyTree treeview => '
                                                  '.x-tree-node-text:textEquals(' + str(arg_dict['service_name']) + ')')
        # SINGLE CLICK RULE
        self.ext_builder.click(ui_cmd_obj, '#policyNavTab #PolicyDomainView #policyTree treeview => '
                                           '.x-tree-node-text:textEquals(' + str(arg_dict['rule_name']) + ')')
        return ui_cmd_obj

    def policy_rule_set_cos(self, ui_cmd_obj, arg_dict):
        # CLICK COS DROPDOWN
        self.ext_builder.click(ui_cmd_obj, 'combobox[itemId=ruleCosCombo] => .x-form-trigger')
        # SELECT COS VALUE
        self.ext_builder.click(ui_cmd_obj, 'combobox[itemId=ruleCosCombo].getPicker() => '
                                           '.x-boundlist-item:contains(' + str(arg_dict['cos_value']) + ')')
        return ui_cmd_obj

    def policy_rule_set_access_control(self, ui_cmd_obj, arg_dict):
        # CLICK ACCESS DROPDOWN
        self.ext_builder.click(ui_cmd_obj, 'combobox[itemId=ruleAccessControlCombo] => .x-form-trigger')
        # SELECT ACCESS CONTROL VALUE
        self.ext_builder.click(ui_cmd_obj, 'combobox[itemId=ruleAccessControlCombo].getPicker() => '
                                           '.x-boundlist-item:contains(' + str(arg_dict['access_control_value']) + ')')
        return ui_cmd_obj

    def policy_rule_traffic_description_click_edit(self, ui_cmd_obj, arg_dict):
        # CLICK EDIT RULE BUTTON
        if arg_dict['remove_traffic_description'] == 'True':
            self.ext_builder.click(ui_cmd_obj, 'button[text=Remove] => .x-btn-inner-default-small')
        self.ext_builder.click(ui_cmd_obj, 'button[itemId="editServiceRuleTrafficDescriptionButton"] => '
                                           '.x-btn-inner-default-small')

        return ui_cmd_obj

    def policy_rule_edit_traffic_description_click_ok(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#editRuleOkBtn => .x-btn-inner-blue-small')
        return ui_cmd_obj

    def policy_rule_set_traffic_type(self, ui_cmd_obj, arg_dict):
        # SELECT TRAFFIC TYPE DROP DOWN
        self.ext_builder.click(ui_cmd_obj, '#tdEditMainPanel #trafTypeCombo => .x-form-trigger')

        # CHOOSE VALUE WITHIN DROPDOWN
        self.ext_builder.click(ui_cmd_obj, '#tdEditMainPanel #trafTypeCombo boundlist => :textEquals(' + str(
            arg_dict['traffic_type']) + ')')

        return ui_cmd_obj

    def policy_rule_set_traffic_layer_type(self, ui_cmd_obj, arg_dict):
        # SELECT CLASSIFICATION LAYER DROP DOWN
        self.ext_builder.click(ui_cmd_obj, '#tdEditMainPanel combobox[fieldLabel=Traffic Classification Layer] => '
                                           '.x-form-trigger')
        # CHOOSE VALUE WITHIN DROPDOWN
        self.ext_builder.click(ui_cmd_obj, '#tdEditMainPanel combobox[fieldLabel=Traffic Classification Layer] '
                                           'boundlist => :textEquals(' + str(arg_dict['layer_type']) + ')')

        return ui_cmd_obj

    def policy_rule_set_well_known_value(self, ui_cmd_obj, arg_dict):

        self.ext_builder.click(ui_cmd_obj, '#tdEditMainPanel #tdValuePane #tdWellKnownValueCombo => .x-form-trigger')
        self.ext_builder.click(ui_cmd_obj, '#tdEditMainPanel #tdValuePane #tdWellKnownValueCombo boundlist => '
                                           '.x-boundlist-item:contains(' + str(arg_dict['well_known_value']) + ')')

        return ui_cmd_obj

    def policy_rule_set_single_value(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#tdEditMainPanel #tdValuePane #tdSingleValueRadio => .x-form-cb-label')
        self.ext_builder.enter_text(ui_cmd_obj, arg_dict['single_value'],
                                    '#tdEditMainPanel #tdValuePane #tdValueField => .x-form-text')
        return ui_cmd_obj

    def policy_rule_set_range_value(self, ui_cmd_obj, arg_dict):

        self.ext_builder.click(ui_cmd_obj, '#tdEditMainPanel #tdValuePane #tdRangeValueRadio => .x-form-cb-input')
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['start_value']), '#tdEditMainPanel #tdValuePane '
                                                                              '#tdRangeStartField => .x-form-text')
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['end_value']), '#tdEditMainPanel #tdValuePane '
                                                                            '#tdRangeEndField => .x-form-text')

        return ui_cmd_obj

    def policy_rule_ip_tos_dialog_click_edit(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'button[itemId=dscpTosEditBtn] => .x-btn-inner-default-small')
        return ui_cmd_obj

    def policy_rule_ip_tos_dialog_click_ok(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#editDscpTosOkBtn => .x-btn-inner-blue-small')
        return ui_cmd_obj

    def policy_rule_set_dscp(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#dscpTypeRadio => .x-form-cb-input')
        if str(arg_dict['well_known']) == "True":
            self.ext_builder.click(ui_cmd_obj, '#dscpTypePane #dscpWkRadio => .x-form-cb-input')
            self.ext_builder.click(ui_cmd_obj, '#dscpTypePane #dscpWkCombo => .x-form-text')
            self.ext_builder.click(ui_cmd_obj, '#dscpTypePane #dscpWkCombo boundlist => '
                                               '.x-boundlist-item:contains(' + str(arg_dict['dscp_value']) + ')')
        else:
            self.ext_builder.click(ui_cmd_obj, '#dscpTypePane #dscpRawRadio => .x-form-cb-input')
            self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['dscp_value']),
                                        '#dscpTypePane #dscpRawField => .x-form-text')
        return ui_cmd_obj

    def policy_rule_set_tos(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#tosTypeRadio  => .x-form-cb-input')

        self.ext_builder.click(ui_cmd_obj, '#tosTypePane #tosPrecCombo => .x-form-trigger')
        self.ext_builder.click(ui_cmd_obj, '#tosTypePane #tosPrecCombo boundlist => '
                                           '.x-boundlist-item:contains(' + str(arg_dict['precedence_value']) + ')')

        # Delay Sensitive check button
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "checkboxfield[itemId=tosDelaySensitiveCb]",
                                                      "[0].rawValue")
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict["delay_sensitive_value"]):
            self.ext_builder.click(ui_cmd_obj, 'checkboxfield[itemId=tosDelaySensitiveCb] => .x-form-cb-input')

        # High Throughput check button
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "checkboxfield[itemId=tosHighThruputCb]",
                                                      "[0].rawValue")
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict["high_throughput_value"]):
            self.ext_builder.click(ui_cmd_obj, 'checkboxfield[itemId=tosHighThruputCb] => .x-form-cb-input')

        # High Reliability check button
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "checkboxfield[itemId=tosHighRelCb]", "[0].rawValue")
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict["high_reliability_value"]):
            self.ext_builder.click(ui_cmd_obj, 'checkboxfield[itemId=tosHighRelCb] => .x-form-cb-input')

        # Explicit Congestion Notification check button
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "checkboxfield[itemId=tosCongNotCb]", "[0].rawValue")
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict["explicit_congestion_value"]):
            self.ext_builder.click(ui_cmd_obj, 'checkboxfield[itemId=tosCongNotCb] => .x-form-cb-input')

        return ui_cmd_obj

    def policy_rule_set_tos_hex(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#tosHexRadio => .x-form-cb-input')
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['hex_value']), '#tosHexPane #tosHexField => .x-form-text')
        return ui_cmd_obj

    def policy_rule_set_tos_mask(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "checkboxfield[itemId=maskValueCbox]", "[0].rawValue")
        if ui_cmd_obj.return_data is False:
            self.ext_builder.click(ui_cmd_obj, 'checkboxfield[itemId="maskValueCbox"] => .x-form-cb-input')
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['mask_value']),
                                    '#maskPane #maskValueField => .x-form-text')

        return ui_cmd_obj

    def policy_rule_set_advanced_value(self, ui_cmd_obj, arg_dict):
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['advanced_value']),
                                    '#tdEditMainPanel #tdOptionalValuePane #tdOptionalValueField => .x-form-text')
        return ui_cmd_obj

    def policy_confirm_device_in_current_domain(self, ui_cmd_obj, arg_dict):
        # Confirm the device is in the current domain
        self.confirm_device_in_current_domain(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def policy_confirm_device_in_domain(self, ui_cmd_obj, arg_dict):
        # Open the specified domain
        self.policy_open_domain(ui_cmd_obj, arg_dict)
        self.logger.log_info("\nOpened Policy Domain '" + arg_dict['domain_name'] + "'\n")

        # Confirm the device is in the current domain
        self.confirm_device_in_current_domain(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def policy_role_default_actions_click_show_all(self, ui_cmd_obj, arg_dict):
        # Click the show all button in default actions for a policy role
        self.ext_builder.click(ui_cmd_obj, '#policyNavTab #PolicyDomainView #domainNodeDetailsPanelContainer '
                                           '#PolicyDetailsPanel #policyDetailsDefaultActionsPanel '
                                           'button[text=Show All] => .x-btn-inner-default-small')
        return ui_cmd_obj

    def policy_role_navigate_to_role_name(self, ui_cmd_obj, arg_dict):
        # CLICK CONTROL MENU ITEM
        self.click_emc_control_menu(ui_cmd_obj, arg_dict)
        # CLICK POLICY TAB UNDER CONTROL MENU ITEM
        self.click_emc_policy_tab(ui_cmd_obj, arg_dict)
        self.ext_builder.click(ui_cmd_obj, 'tab[text=Policy] => .x-tab-inner-extr-main-tab-panel')

        # FIND ROLE IN TREE AND CLICK
        self.ext_builder.click(ui_cmd_obj, '#policyNavTab #PolicyDomainView #policyDomainViewNavigationTrees '
                                           '#policyTreesPanel #policyTree treeview => '
                                           '.x-tree-node-text:textEquals(' + str(arg_dict['role_name']) + ')')
        return ui_cmd_obj

    def policy_role_set_access_control(self, ui_cmd_obj, arg_dict):
        # Set access control for the specified policy role
        self.ext_builder.click(ui_cmd_obj, '#policyNavTab #PolicyDomainView #domainNodeDetailsPanelContainer '
                                           '#PolicyDetailsPanel #policyDetailsDefaultActionsPanel '
                                           'matchingcombo[fieldLabel=Access Control] => .x-form-text')
        # SELECT ACCESS CONTROL VALUE
        self.ext_builder.click(ui_cmd_obj, 'matchingcombo[fieldLabel=Access Control].getPicker() => '
                                           '.x-boundlist-item:contains(' + str(arg_dict['access_control_value']) + ')')
        self.policy_save_domain(ui_cmd_obj, arg_dict)
        return ui_cmd_obj

    def policy_role_set_cos(self, ui_cmd_obj, arg_dict):
        # Set cos for the specified policy role
        self.ext_builder.click(ui_cmd_obj, '#policyNavTab #PolicyDomainView #domainNodeDetailsPanelContainer '
                                           '#PolicyDetailsPanel #policyDetailsDefaultActionsPanel '
                                           'actioncombo[fieldLabel=Class of Service] => .x-form-text')
        # SELECT COS VALUE
        self.ext_builder.click(ui_cmd_obj, 'actioncombo[fieldLabel=Class of Service].getPicker() => '
                                           '.x-boundlist-item:contains(' + str(arg_dict['cos_name']) + ')')
        self.policy_save_domain(ui_cmd_obj, arg_dict)
        return ui_cmd_obj

    def policy_role_edit_tci_overwrite(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#policyNavTab #PolicyDomainView #domainNodeDetailsPanelContainer '
                                           '#PolicyDetailsPanel matchingcombo[fieldLabel=TCI Overwrite] => '
                                           '.x-form-text')
        self.ext_builder.click(ui_cmd_obj, '#policyNavTab #PolicyDomainView #domainNodeDetailsPanelContainer '
                                           '#PolicyDetailsPanel matchingcombo[fieldLabel=TCI Overwrite] boundlist => '
                                           ':textEquals(' + str(arg_dict['tci_overwrite']) + ')')
        return ui_cmd_obj

    def policy_delete_service(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified None is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Policy, self).policy_delete_service(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def confirm_device_in_current_domain(self, ui_cmd_obj, arg_dict):
        # Expand the Devices/Port Groups panel, if it isn't already expanded
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, '[itemId=devicePortTreesPanel]', '[0].collapsed')
        if ui_cmd_obj.return_data is True:
            self.ext_builder.click(ui_cmd_obj, '#policyNavTab #PolicyDomainView panel #devicePortTreesPanel header '
                                               'title[text=Devices/Port Groups] => .x-title-text')

        # Select the Devices tab
        self.ext_builder.click(ui_cmd_obj, '#policyNavTab #PolicyDomainView #policyDomainViewNavigationTrees '
                                           '#policyTreesPanel #devicePortTreesPanel tab[title=Devices] => .x-tab-inner')

        # Check if the specified IP address is in the table
        # ui_cmd_obj = self.ext_builder.is_item_in_component(ui_cmd_obj, '[itemId=listViewPanel]', '[0]', 'deviceIp',
        # arg_dict['device_ip'])
        self.logger.log_info("\nTO DO: figure out why is_in_table is always returning True\n")
        # "is_item_in_component" is returning True even if the item isn't found, so looping through myself
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      "[itemId=listViewPanel]",
                                                      "[0].store.data.length")
        item_count = int(ui_cmd_obj.return_data)
        item_count += 1

        # Assume we won't find the device
        found_item = False

        # Loop through the list and see if the specified device exists
        item_index = 0
        for x in range(0, item_count):
            self.ext_builder.component_query(ui_cmd_obj,
                                             '[itemId=listViewPanel]',
                                             '[0].store.data.items[' + str(item_index) + '].data.deviceIp')
            if ui_cmd_obj.return_data == arg_dict['device_ip']:
                found_item = True
                break
            else:
                item_index += 1

        # Log the result
        # if ui_cmd_obj.return_data is True:
        if found_item is True:
            self.logger.log_info("\nDevice '" + arg_dict['device_ip'] + "' exists in the current domain.\n")
        else:
            self.logger.log_info("\nDevice '" + arg_dict['device_ip'] + "' does not exist in the current domain.\n")

        # Pass or fail the test, based on what was expected
        # if ui_cmd_obj.return_data is StringUtils.string_to_boolean(arg_dict["exists"]):
        if found_item is StringUtils.string_to_boolean(arg_dict["exists"]):
            # PASS
            ui_cmd_obj.error_state = False
        else:
            # FAIL
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def edit_policy_rule_single_value(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#tdEditMainPanel #tdValuePane #tdSingleValueRadio => .x-form-cb-label')
        self.ext_builder.enter_text(ui_cmd_obj, arg_dict['single_value'], '#tdEditMainPanel #tdValuePane '
                                                                          '#tdValueField => .x-form-text')
        return ui_cmd_obj

    def edit_policy_rule_well_known_value(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#policyNavTab #PolicyDomainView #policyTree treeview => '
                                           '.x-tree-node-text:textEquals(' + str(arg_dict['rule_name']) + ')')
        self.ext_builder.click(ui_cmd_obj, '#policyNavTab #PolicyDomainView #domainNodeDetailsPanelContainer '
                                           '#editServiceRuleTrafficDescriptionButton => .x-btn-inner-default-small')
        self.ext_builder.click(ui_cmd_obj, '#tdEditMainPanel #tdValuePane #tdWellKnownValueCombo => .x-form-trigger')
        self.ext_builder.click(ui_cmd_obj, '#tdEditMainPanel #tdValuePane #tdWellKnownValueCombo boundlist => '
                                           '.x-boundlist-item:contains(' + str(arg_dict['well_known_value']) + ')')
        self.ext_builder.click(ui_cmd_obj, '#editRuleOkBtn => .x-btn-inner-blue-small')

        return ui_cmd_obj

    def edit_policy_rule_access_control(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#policyNavTab #PolicyDomainView #policyTree treeview => '
                                           '.x-tree-node-text:textEquals(' + str(arg_dict['rule_name']) + ')')
        self.ext_builder.click(ui_cmd_obj, '#policyNavTab #PolicyDomainView #domainNodeDetailsPanelContainer '
                                           '#ruleAccessControlCombo => .x-form-trigger')
        self.ext_builder.click(ui_cmd_obj, '#policyNavTab #PolicyDomainView #domainNodeDetailsPanelContainer '
                                           '#ruleAccessControlCombo boundlist => '
                                           ':textEquals(' + str(arg_dict['status']) + ')')

        return ui_cmd_obj

    def set_rule_cos(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#policyNavTab #PolicyDomainView #policyTree treeview => '
                                           '.x-tree-node-text:textEquals(' + str(arg_dict['rule_name']) + ')')
        self.ext_builder.click(ui_cmd_obj, '#policyNavTab #PolicyDomainView #domainNodeDetailsPanelContainer '
                                           '#ruleCosCombo => .x-form-trigger')
        self.ext_builder.click(ui_cmd_obj, '#policyNavTab #PolicyDomainView #domainNodeDetailsPanelContainer '
                                           '#ruleCosCombo boundlist => '
                                           '.x-boundlist-item:contains(' + str(arg_dict['cos_value']) + ')')

        return ui_cmd_obj

    def edit_policy_rule(self, ui_cmd_obj, arg_dict):
        # FIND SERVICE IN TREE AND DOUBLE CLICK TO EXPAND
        self.ext_builder.double_click(ui_cmd_obj, '#policyNavTab #PolicyDomainView #policyTree treeview => '
                                                  '.x-tree-node-text:textEquals(' + str(arg_dict['service_name']) + ')')
        # SINGLE CLICK RULE
        self.ext_builder.click(ui_cmd_obj, '#policyNavTab #PolicyDomainView #policyTree treeview => '
                                           '.x-tree-node-text:textEquals(' + str(arg_dict['rule_name']) + ')')

        # CHOOSE LAYER TYPE
        self.edit_policy_rule_traffic_layer_type(ui_cmd_obj, arg_dict)

        # CHOOSE TRAFFIC TYPE
        self.edit_policy_rule_traffic_type(ui_cmd_obj, arg_dict)

        if arg_dict['well_known_value'] is not None:
            self.edit_policy_rule_well_known_value(ui_cmd_obj, arg_dict)

        if arg_dict['application_group'] is not None:
            self.policy_rule_set_application_group(ui_cmd_obj, arg_dict)
            self.policy_rule_set_application(ui_cmd_obj, arg_dict)

        if arg_dict['single_value'] is not None:
            self.edit_policy_rule_single_value(ui_cmd_obj, arg_dict)

        # Edit 'Actions' in Rule page
        self.edit_policy_rule_access_control(ui_cmd_obj, arg_dict)
        if arg_dict['cos_value'] is not None:
            self.set_rule_cos(ui_cmd_obj, arg_dict)

        self.policy_save_domain(ui_cmd_obj, arg_dict)

        return ui_cmd_obj

    def verify_vlan_tree_panel(self, ui_cmd_obj, arg_dict):
        self.ext_builder.component_query(ui_cmd_obj, '[itemId=vlanTree]', '[0].collapsed')
        self.ext_builder.click(ui_cmd_obj, '#policyNavTab #PolicyDomainView #policyDomainViewNavigationTrees '
                                           '#policyTreesPanel #vlanTree title => .x-title-text')

        self.ext_builder.component_query(ui_cmd_obj, '[itemId=vlanTree]', '[0].collapsed')

        return ui_cmd_obj

    def edit_policy_rule_traffic_type(self, ui_cmd_obj, arg_dict):
        # SELECT TRAFFIC TYPE DROP DOWN
        self.ext_builder.click(ui_cmd_obj, '#tdEditMainPanel #trafTypeCombo => .x-form-trigger')

        # CHOOSE VALUE WITHIN DROPDOWN
        self.ext_builder.click(ui_cmd_obj, '#tdEditMainPanel #trafTypeCombo boundlist => '
                                           ':textEquals(' + str(arg_dict['traffic_type']) + ')')

        return ui_cmd_obj

    def policy_delete_local_service(self, ui_cmd_obj, arg_dict):
        self.ext_builder.right_click(ui_cmd_obj, '#policyNavTab #PolicyDomainView #policyTree treeview => '
                                                 '.x-tree-node-text:textEquals(' + arg_dict['service_name'] + ')')
        self.ext_builder.click(ui_cmd_obj, 'menu(true){isVisible()} menuitem[text=Delete] => .x-menu-item-link')
        self.ext_builder.click(ui_cmd_obj, '#yes => .x-btn-inner-blue-small')

        self.policy_save_domain(ui_cmd_obj, arg_dict)
        return ui_cmd_obj

    def edit_policy_rule_traffic_layer_type(self, ui_cmd_obj, arg_dict):
        # CLICK EDIT RULE BUTTON
        self.ext_builder.click(ui_cmd_obj, '#policyNavTab #PolicyDomainView #domainNodeDetailsPanelContainer '
                                           '#editServiceRuleTrafficDescriptionButton => .x-btn-inner-default-small')

        # SELECT CLASSIFICATION LAYER DROP DOWN
        self.ext_builder.click(ui_cmd_obj, '#tdEditMainPanel combobox[fieldLabel=Traffic Classification Layer] => '
                                           '.x-form-trigger')

        # CHOOSE VALUE WITHIN DROPDOWN
        self.ext_builder.click(ui_cmd_obj, '#tdEditMainPanel combobox[fieldLabel=Traffic Classification Layer] '
                                           'boundlist => :textEquals(' + str(arg_dict['layer_type']) + ')')

        return ui_cmd_obj
