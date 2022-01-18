from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as PolicydeviceBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Policydevice(PolicydeviceBase):
    def policy_device_expand_device_tree(self, ui_cmd_obj, arg_dict):
        self.ext_builder.double_click(ui_cmd_obj,
                                      '#policyNavTab #PolicyDomainView #policyDomainViewNavigationTrees '
                                      '#policyTreesPanel #devicePortTreesPanel #deviceTree treeview => '
                                      '.x-tree-node-text:contains(' + str(arg_dict['device_ip']) + ')')

        return ui_cmd_obj

    def policy_device_select_device_node(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               '#policyNavTab #PolicyDomainView #policyDomainViewNavigationTrees #policyTreesPanel '
                               '#devicePortTreesPanel #deviceTree treeview => '
                               '.x-tree-node-text:contains(' + str(arg_dict['device_name']) + ')')
        return ui_cmd_obj

    def policy_device_select_radius_tab(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               '#policyNavTab #PolicyDomainView #domainNodeDetailsPanelContainer #policyDeviceTabPanel '
                               'tab[title=RADIUS] => .x-tab-inner-extr-sec-tab-panel')
        return ui_cmd_obj

    def policy_device_select_device_radius_server(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               '#policyNavTab #PolicyDomainView #domainNodeDetailsPanelContainer #policyDeviceTabPanel '
                               '#RadiusAuthConfigPanel #RadiusAuthServerFormPanel #RadiusAuthServerPanel gridview => '
                               '.x-grid-cell-inner:textEquals(' + str(arg_dict['radius_ip']) + ')')
        return ui_cmd_obj

    def policy_device_delete_device_radius_server(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               '#policyNavTab #PolicyDomainView #domainNodeDetailsPanelContainer #policyDeviceTabPanel '
                               '#RadiusAuthConfigPanel #RadiusAuthServerFormPanel #RadiusAuthServerPanel '
                               'button[text=Remove] => .x-btn-inner-default-toolbar-small')
        return ui_cmd_obj

    def policy_device_apply_device_radius_settings(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               '#policyNavTab #PolicyDomainView #domainNodeDetailsPanelContainer #policyDeviceTabPanel '
                               '#RadiusAuthConfigPanel #RadiusAuthServerFormPanel #RadiusAuthServerPanel '
                               'button[text=Apply] => .x-btn-inner-default-toolbar-small')
        return ui_cmd_obj

    def policy_device_select_ports_tab(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               '#policyNavTab #PolicyDomainView #domainNodeDetailsPanelContainer #policyDeviceTabPanel '
                               'tab[text=Ports] => .x-tab-inner-extr-sec-tab-panel')
        return ui_cmd_obj

    def policy_device_select_device_port(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               '#policyNavTab #PolicyDomainView #domainNodeDetailsPanelContainer #policyDeviceTabPanel '
                               '#PortAuthConfigPanel treeview => '
                               '.x-tree-node-text:textEquals(' + str(arg_dict['device_port']) + ')')
        return ui_cmd_obj

    def policy_device_select_authentication_tab(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               '#policyNavTab #PolicyDomainView #domainNodeDetailsPanelContainer #policyDeviceTabPanel '
                               'tab[title=Authentication] => .x-tab-inner-extr-sec-tab-panel')
        return ui_cmd_obj

    def policy_device_click_authentication_tree_panel(self, ui_cmd_obj, arg_dict):
        new_dict = {}
        if arg_dict['tree_name'].lower() == 'authentication mode':
            new_dict['tree_name'] = "panel[title=Authentication Mode]"
        elif arg_dict['tree_name'].lower() == 'rfc3580 vlan authorization':
            new_dict['tree_name'] = "panel[title=RFC3580 VLAN Authorization]"
        elif arg_dict['tree_name'].lower() == 'login settings':
            new_dict['tree_name'] = "panel[title=Login Settings]"
        elif arg_dict['tree_name'].lower() == 'automatic re-authentication':
            new_dict['tree_name'] = "panel[title=Automatic Re-Authentication]"
        elif arg_dict['tree_name'].lower() == 'authenticated user Counts':
            new_dict['tree_name'] = "panel[title=Authenticated Users Counts]"
        elif arg_dict['tree_name'].lower() == 'convergence end-point access':
            new_dict['tree_name'] = "panel[title=Convergence End-Point Access]"

        self.ext_builder.component_query(ui_cmd_obj, "#policyNavTab #PolicyDomainView #domainNodeDetailsPanelContainer "
                                                     "#policyDeviceTabPanel #PortAuthConfigPanel "
                                                     "#PortAuthConfigForm " + new_dict['tree_name'], '[0].uiCls[0]')
        if ui_cmd_obj.return_data == "collapsed":
            self.ext_builder.click(ui_cmd_obj,
                                   "#policyNavTab #PolicyDomainView #domainNodeDetailsPanelContainer "
                                   "#policyDeviceTabPanel #PortAuthConfigPanel #PortAuthConfigForm " +
                                   new_dict['tree_name'] + "tool[type=expand-bottom] => .x-tool-tool-el")

        return ui_cmd_obj

    def policy_device_select_port_authentication_tab(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#policyNavTab #PolicyDomainView #domainNodeDetailsPanelContainer '
                                           '#policyDeviceTabPanel tab[title=Ports]:nth-child(2) => .x-tab-inner')
        return ui_cmd_obj

    def policy_device_select_port_authentication_mode(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, r'#policyNavTab #PolicyDomainView #domainNodeDetailsPanelContainer '
                                           r'#policyDeviceTabPanel #PortAuthConfigPanel #PortAuthConfigForm '
                                           r'combo[fieldLabel=Port Mode \(Auth \/ Unauth Behavior\)] => .x-form-text')
        self.ext_builder.click(ui_cmd_obj, r'#policyNavTab #PolicyDomainView #domainNodeDetailsPanelContainer '
                                           r'#policyDeviceTabPanel #PortAuthConfigPanel #PortAuthConfigForm '
                                           r'combo[fieldLabel=Port Mode \(Auth \/ Unauth Behavior\)] boundlist => '
                                           r'.x-boundlist-item:contains(' + str(arg_dict['port_mode']) + ')')
        return ui_cmd_obj

    def policy_device_select_port_dot1x_status(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, r'#policyNavTab #PolicyDomainView #domainNodeDetailsPanelContainer '
                                           r'#policyDeviceTabPanel #PortAuthConfigPanel #PortAuthConfigForm '
                                           r'combo[fieldLabel=802\.1X Auth Status] => .x-form-text')
        self.ext_builder.click(ui_cmd_obj, '#policyNavTab #PolicyDomainView #domainNodeDetailsPanelContainer '
                                           '#policyDeviceTabPanel #PortAuthConfigPanel #PortAuthConfigForm '
                                           'combo[fieldLabel=802.1X Auth Status] boundlist => '
                                           ':textEquals(' + str(arg_dict['dot1x_status']) + ')')
        return ui_cmd_obj

    def policy_device_add_radius_server(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#policyNavTab #PolicyDomainView #domainNodeDetailsPanelContainer '
                                           '#policyDeviceTabPanel #RadiusAuthConfigPanel #RadiusAuthServerFormPanel '
                                           '#RadiusAuthServerPanel button[text=Add...] => '
                                           '.x-btn-inner-default-toolbar-small')
        return ui_cmd_obj

    def policy_device_click_port_authentication_apply(self, ui_cmd_obj, arg_dict):
        self.ext_builder.component_query(ui_cmd_obj, '#policyNavTab #PolicyDomainView #domainNodeDetailsPanelContainer '
                                                     '#policyDeviceTabPanel #PortAuthConfigPanel '
                                                     'button[name=applyPortAuthConfigButton]', '[0].disabled')
        if ui_cmd_obj.return_data is False:
            self.ext_builder.click(ui_cmd_obj, '#policyNavTab #PolicyDomainView #domainNodeDetailsPanelContainer '
                                               '#policyDeviceTabPanel #PortAuthConfigPanel '
                                               'button[name=applyPortAuthConfigButton] => '
                                               '.x-btn-inner-default-toolbar-small')
        return ui_cmd_obj

    def policy_device_add_radius_dialog_edit_ip(self, ui_cmd_obj, arg_dict):
        self.ext_builder.enter_text(ui_cmd_obj, arg_dict['radius_ip'],
                                    '#RadiusServerCreateView #RadiusServerCreateForm '
                                    'textfield[name=etsysRadiusAuthClientServerAddress] => .x-form-text')
        return ui_cmd_obj

    def policy_device_add_radius_dialog_edit_secret(self, ui_cmd_obj, arg_dict):
        self.ext_builder.enter_text(ui_cmd_obj, arg_dict['radius_secret'],
                                    '#RadiusServerCreateView #RadiusServerCreateForm '
                                    'passwordfield[name=etsysRadiusAuthClientServerSecret] => .x-form-text')
        self.ext_builder.enter_text(ui_cmd_obj, arg_dict['radius_secret'],
                                    '#RadiusServerCreateView #RadiusServerCreateForm '
                                    'passwordfield[name=etsysRadiusServerSecretVerify] => .x-form-text')
        return ui_cmd_obj

    def policy_device_add_radius_dialog_edit_access(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#RadiusServerCreateView #RadiusServerCreateForm '
                                           'combo[name=etsysRadiusAuthClientServerRealmType] => .x-form-text')
        self.ext_builder.click(ui_cmd_obj, '#RadiusServerCreateView #RadiusServerCreateForm '
                                           'combo[name=etsysRadiusAuthClientServerRealmType] boundlist => '
                                           ':textEquals(' + str(arg_dict['radius_access']) + ')')
        return ui_cmd_obj

    def policy_device_add_radius_dialog_click_ok(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '>>#RadiusServerCreateView button[text=OK]')
        return ui_cmd_obj

    def policy_device_select_port_macauth_status(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#policyNavTab #PolicyDomainView #domainNodeDetailsPanelContainer '
                                           '#policyDeviceTabPanel #PortAuthConfigPanel #PortAuthConfigForm '
                                           'combo[fieldLabel=MAC Auth Status] => .x-form-text')
        self.ext_builder.click(ui_cmd_obj, '#policyNavTab #PolicyDomainView #domainNodeDetailsPanelContainer '
                                           '#policyDeviceTabPanel #PortAuthConfigPanel '
                                           '#PortAuthConfigForm combo[fieldLabel=MAC Auth Status] boundlist => '
                                           ':textEquals(' + str(arg_dict['macauth_status']) + ')')
        return ui_cmd_obj

    def policy_device_select_radius_accounting_tab(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#policyNavTab #PolicyDomainView #domainNodeDetailsPanelContainer '
                                           '#policyDeviceTabPanel tab[title=Accounting] => .x-tab-inner')
        return ui_cmd_obj

    def policy_device_select_device_radius_accounting_server(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#policyNavTab #PolicyDomainView #domainNodeDetailsPanelContainer '
                                           '#policyDeviceTabPanel #RadiusAcctConfigPanel #RadiusAcctServerFormPanel '
                                           '#RadiusAcctServerPanel gridview => '
                                           '.x-grid-cell-inner:textEquals(' + str(arg_dict['acct_server']) + ')')
        return ui_cmd_obj

    def policy_device_delete_device_radius_accounting_server(self, ui_cmd_obj, arg_dict):
        self.ext_builder.component_query(ui_cmd_obj, '#policyNavTab #PolicyDomainView #domainNodeDetailsPanelContainer '
                                                     '#policyDeviceTabPanel #RadiusAcctConfigPanel '
                                                     '#RadiusAcctServerFormPanel #RadiusAcctServerPanel '
                                                     'button[actionId=RadiusAcctServerRemoveBtn]', '[0].disabled')
        if ui_cmd_obj.return_data is False:
            self.ext_builder.click(ui_cmd_obj, '#policyNavTab #PolicyDomainView #domainNodeDetailsPanelContainer '
                                               '#policyDeviceTabPanel #RadiusAcctConfigPanel '
                                               '#RadiusAcctServerFormPanel #RadiusAcctServerPanel '
                                               'button[actionId=RadiusAcctServerRemoveBtn] => '
                                               '.x-btn-inner-default-toolbar-small')
        return ui_cmd_obj

    def policy_device_apply_device_radius_accounting_settings(self, ui_cmd_obj, arg_dict):
        self.ext_builder.component_query(ui_cmd_obj, '#policyNavTab #PolicyDomainView #domainNodeDetailsPanelContainer '
                                                     '#policyDeviceTabPanel #RadiusAcctConfigPanel '
                                                     '#RadiusAcctServerFormPanel #RadiusAcctServerPanel '
                                                     'button[itemId=applyAcctServerSettingsButton]', '[0].disabled')

        if ui_cmd_obj.return_data is False:
            self.ext_builder.click(ui_cmd_obj, '#policyNavTab #PolicyDomainView #domainNodeDetailsPanelContainer '
                                               '#policyDeviceTabPanel #RadiusAcctConfigPanel '
                                               '#RadiusAcctServerFormPanel #RadiusAcctServerPanel '
                                               'button[itemId=applyAcctServerSettingsButton] => '
                                               '.x-btn-inner-default-toolbar-small')
        return ui_cmd_obj

    def policy_device_add_radius_accounting_server(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#policyNavTab #PolicyDomainView #domainNodeDetailsPanelContainer '
                                           '#policyDeviceTabPanel #RadiusAcctConfigPanel #RadiusAcctServerFormPanel '
                                           '#RadiusAcctServerPanel button[text=Add...] => '
                                           '.x-btn-inner-default-toolbar-small')
        return ui_cmd_obj

    def policy_device_add_radius_accounting_dialog_edit_ip(self, ui_cmd_obj, arg_dict):
        self.ext_builder.enter_text(ui_cmd_obj, arg_dict['radius_acct_ip'],
                                    '#RadiusServerCreateView #RadiusServerCreateForm '
                                    'textfield[name=etsysRadiusAcctClientServerAddress] => .x-form-text')
        return ui_cmd_obj

    def policy_device_add_radius_accounting_dialog_edit_secret(self, ui_cmd_obj, arg_dict):
        self.ext_builder.enter_text(ui_cmd_obj, arg_dict['radius_acct_secret'],
                                    '#RadiusServerCreateView #RadiusServerCreateForm '
                                    'passwordfield[name=etsysRadiusAcctClientServerSecret] => .x-form-text')
        self.ext_builder.enter_text(ui_cmd_obj, arg_dict['radius_acct_secret'],
                                    '#RadiusServerCreateView #RadiusServerCreateForm '
                                    'passwordfield[name=etsysRadiusServerSecretVerify] => .x-form-text')
        return ui_cmd_obj

    def policy_device_add_radius_accounting_dialog_edit_access(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#RadiusServerCreateView #RadiusServerCreateForm '
                                           'combo[name=etsysRadiusAcctClientServerRealmType] => .x-form-text')
        self.ext_builder.click(ui_cmd_obj, '#RadiusServerCreateView #RadiusServerCreateForm '
                                           'combo[name=etsysRadiusAcctClientServerRealmType] boundlist => '
                                           ':textEquals(' + str(arg_dict['radius_acct_access']) + ')')
        return ui_cmd_obj

    def policy_device_add_radius_accounting_dialog_click_ok(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#RadiusServerCreateView button[text=OK] => .x-btn-inner-blue-small')
        return ui_cmd_obj

    def policy_device_select_device_macauth_status(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#policyNavTab #PolicyDomainView #domainNodeDetailsPanelContainer '
                                           '#policyDeviceTabPanel #DeviceAuthConfigPanel combo[fieldLabel=MAC] => '
                                           '.x-form-text')
        self.ext_builder.click(ui_cmd_obj, '#policyNavTab #PolicyDomainView #domainNodeDetailsPanelContainer '
                                           '#policyDeviceTabPanel #DeviceAuthConfigPanel combo[fieldLabel=MAC] '
                                           'boundlist => :textEquals(' + str(arg_dict['macauth_status']) + ')')
        return ui_cmd_obj

    def policy_device_select_device_dot1x_status(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, r'#policyNavTab #PolicyDomainView #domainNodeDetailsPanelContainer '
                                           r'#policyDeviceTabPanel #DeviceAuthConfigPanel combo[fieldLabel=802\.1X] => '
                                           r'.x-form-text')
        self.ext_builder.click(ui_cmd_obj, r'#policyNavTab #PolicyDomainView #domainNodeDetailsPanelContainer '
                                           r'#policyDeviceTabPanel #DeviceAuthConfigPanel combo[fieldLabel=802\.1X] '
                                           r'boundlist => :textEquals(' + str(arg_dict['dot1x_status']) + ')')
        return ui_cmd_obj

    def policy_device_apply_device_authentication(self, ui_cmd_obj, arg_dict):
        self.ext_builder.component_query(ui_cmd_obj, '#policyNavTab #PolicyDomainView #domainNodeDetailsPanelContainer '
                                                     '#policyDeviceTabPanel #DeviceAuthConfigPanel '
                                                     'button[name=applyAuthConfigButton]', '[0].disabled')
        if ui_cmd_obj.return_data is False:
            self.ext_builder.click(ui_cmd_obj, '#policyNavTab #PolicyDomainView #domainNodeDetailsPanelContainer '
                                               '#policyDeviceTabPanel #DeviceAuthConfigPanel '
                                               'button[name=applyAuthConfigButton] => '
                                               '.x-btn-inner-default-toolbar-small')
        return ui_cmd_obj
