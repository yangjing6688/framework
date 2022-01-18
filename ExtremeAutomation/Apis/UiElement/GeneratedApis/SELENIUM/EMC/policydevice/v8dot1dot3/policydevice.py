from ExtremeAutomation.Apis.UiElement.GeneratedApis.SELENIUM.EMC.policydevice.v8dot1dot1.policydevice import \
    Policydevice as PolicydeviceBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Policydevice(PolicydeviceBase):
    def policy_device_expand_device_port(self, ui_cmd_obj, arg_dict):
        self.ext_builder.component_query(ui_cmd_obj,
                                         "#policyNavTab #PolicyDomainView #domainNodeDetailsPanelContainer "
                                         "#policyDeviceTabPanel #PortAuthConfigPanel panel[title=Selected port: " +
                                         str(arg_dict["device_port"]) + "]",
                                         '[0].uiCls[0]')
        if ui_cmd_obj.return_data == "collapsed":
            self.ext_builder.click(ui_cmd_obj,
                                   "#policyNavTab #PolicyDomainView #domainNodeDetailsPanelContainer "
                                   "#policyDeviceTabPanel #PortAuthConfigPanel panel[title=Selected port: " +
                                   str(arg_dict['device_port']) + "] tool => .x-tool-tool-el")

        return ui_cmd_obj

    def policy_device_collapse_device_port(self, ui_cmd_obj, arg_dict):
        self.ext_builder.component_query(ui_cmd_obj,
                                         "#policyNavTab #PolicyDomainView #domainNodeDetailsPanelContainer "
                                         "#policyDeviceTabPanel #PortAuthConfigPanel panel[title=Selected port: " +
                                         str(arg_dict["device_port"]) + "]", '[0].uiCls[0]')
        if ui_cmd_obj.return_data != "collapsed":
            self.ext_builder.click(ui_cmd_obj,
                                   "#policyNavTab #PolicyDomainView #domainNodeDetailsPanelContainer "
                                   "#policyDeviceTabPanel #PortAuthConfigPanel panel[title=Selected port: " +
                                   str(arg_dict['device_port']) + "] tool => .x-tool-tool-el")

        return ui_cmd_obj

    def policy_device_click_authentication_device_tree_panel(self, ui_cmd_obj, arg_dict):
        new_dict = {}
        if arg_dict['tree_name'].lower() == 'authentication status':
            new_dict['tree_name'] = "panel[title=Authentication Status]"
        elif arg_dict['tree_name'].lower() == 'current user counts':
            new_dict['tree_name'] = "panel[title=Current User Counts]"
        elif arg_dict['tree_name'].lower() == 'global authentication settings':
            new_dict['tree_name'] = "panel[title=Global Authentication Settings]"
        elif arg_dict['tree_name'].lower() == 'mac authentication settings':
            new_dict['tree_name'] = "panel[title=MAC Authentication Settings]"
        elif arg_dict['tree_name'].lower() == 'web authentication settings':
            new_dict['tree_name'] = "panel[title=Web Authentication Settings]"
        elif arg_dict['tree_name'].lower() == 'convergence end-point settings':
            new_dict['tree_name'] = "panel[title=Convergence End-Point Settings]"

        self.ext_builder.component_query(ui_cmd_obj,
                                         "#policyNavTab #PolicyDomainView #domainNodeDetailsPanelContainer "
                                         "#policyDeviceTabPanel #DeviceAuthConfigPanel " + new_dict['tree_name'],
                                         '[0].uiCls[0]')

        if ui_cmd_obj.return_data == "collapsed":
            self.ext_builder.click(ui_cmd_obj,
                                   "#policyNavTab #PolicyDomainView #domainNodeDetailsPanelContainer "
                                   "#policyDeviceTabPanel #DeviceAuthConfigPanel " + new_dict['tree_name'] +
                                   " tool[type=expand-bottom] => .x-tool-tool-el")

        return ui_cmd_obj

    def policy_device_click_authentication_ports_tree_panel(self, ui_cmd_obj, arg_dict):
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

        self.ext_builder.component_query(ui_cmd_obj,
                                         "#policyNavTab #PolicyDomainView #domainNodeDetailsPanelContainer "
                                         "#policyDeviceTabPanel #PortAuthConfigPanel "
                                         "#PortAuthConfigForm " + new_dict['tree_name'], '[0].uiCls[0]')
        if ui_cmd_obj.return_data == "collapsed":
            self.ext_builder.click(ui_cmd_obj,
                                   "#policyNavTab #PolicyDomainView #domainNodeDetailsPanelContainer "
                                   "#policyDeviceTabPanel #PortAuthConfigPanel #PortAuthConfigForm " +
                                   new_dict['tree_name'] + " tool[type=expand-bottom] => .x-tool-tool-el")

        return ui_cmd_obj

    def policy_device_select_device_authentication_tab(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "#policyNavTab #PolicyDomainView #domainNodeDetailsPanelContainer "
                               "#policyDeviceTabPanel tab[title=Device] => .x-tab-inner")

        return ui_cmd_obj

    def policy_device_apply_device_authentication(self, ui_cmd_obj, arg_dict):
        self.ext_builder.component_query(ui_cmd_obj,
                                         '#policyNavTab #PolicyDomainView #domainNodeDetailsPanelContainer '
                                         '#policyDeviceTabPanel #DeviceAuthConfigPanel '
                                         'button[name=applyAuthConfigButton]', '[0].disabled')
        if ui_cmd_obj.return_data is False:
            self.ext_builder.click(ui_cmd_obj,
                                   '#policyNavTab #PolicyDomainView #domainNodeDetailsPanelContainer '
                                   '#policyDeviceTabPanel #DeviceAuthConfigPanel button[name=applyAuthConfigButton] => '
                                   '.x-btn-inner-default-toolbar-small')

        self.ext_builder.component_query(ui_cmd_obj, 'title[text=Warning]', '[0].config.text',
                                         wait_for_load_mask=False)
        if ui_cmd_obj.return_data == 'Warning':
            self.ext_builder.click(ui_cmd_obj, '#setMacPwdOkBtn => .x-btn-inner-blue-small',
                                   wait_for_load_mask=False)
        elif ui_cmd_obj.return_data != u'':
            ui_cmd_obj.error_state = False
        self.ext_builder.component_query(ui_cmd_obj, 'title[text=Port Authentication Status]', '[0].config.text',
                                         wait_for_load_mask=False)
        if ui_cmd_obj.return_data == 'Port Authentication Status':
            self.ext_builder.click(ui_cmd_obj, 'window[title=Port Authentication Status] button[text=OK] => '
                                               '.x-btn-inner-blue-small', wait_for_load_mask=False)
        elif ui_cmd_obj.return_data != u'':
            ui_cmd_obj.error_state = False

        return ui_cmd_obj

    def policy_device_select_mac_auth_set_password_and_mask(self, ui_cmd_obj, arg_dict):
        self.ext_builder.component_query(ui_cmd_obj,
                                         '#policyNavTab #PolicyDomainView #domainNodeDetailsPanelContainer '
                                         '#policyDeviceTabPanel #DeviceAuthConfigPanel checkbox', '[0].disabled')

        if ui_cmd_obj.return_data is False:
            self.ext_builder.click(ui_cmd_obj,
                                   "#policyNavTab #PolicyDomainView #domainNodeDetailsPanelContainer "
                                   "#policyDeviceTabPanel #DeviceAuthConfigPanel checkbox => .x-form-cb-input")
        return ui_cmd_obj

    def policy_device_set_mac_auth_user_password(self, ui_cmd_obj, arg_dict):
        self.ext_builder.enter_text(ui_cmd_obj, arg_dict["password"],
                                    "#policyNavTab #PolicyDomainView #domainNodeDetailsPanelContainer "
                                    "#policyDeviceTabPanel #DeviceAuthConfigPanel "
                                    "passwordfield[fieldLabel=MAC User Password] => .x-form-text")

        return ui_cmd_obj

    def policy_device_select_mac_auth_mask(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "#policyNavTab #PolicyDomainView #domainNodeDetailsPanelContainer "
                                           "#policyDeviceTabPanel #DeviceAuthConfigPanel combo[fieldLabel=MAC Mask] => "
                                           ".x-form-trigger")
        self.ext_builder.click(ui_cmd_obj, "#policyNavTab #PolicyDomainView #domainNodeDetailsPanelContainer "
                                           "#policyDeviceTabPanel #DeviceAuthConfigPanel combo[fieldLabel=MAC Mask] "
                                           "boundlist => :textEquals(" + str(arg_dict["mask"]) + ")")

        return ui_cmd_obj

    def policy_device_select_mac_auth_address_delimiter(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "#policyNavTab #PolicyDomainView #domainNodeDetailsPanelContainer "
                                           "#policyDeviceTabPanel #DeviceAuthConfigPanel "
                                           "combo[fieldLabel=MAC Address Delimiter] => .x-form-trigger")
        self.ext_builder.click(ui_cmd_obj, "#policyNavTab #PolicyDomainView #domainNodeDetailsPanelContainer "
                                           "#policyDeviceTabPanel #DeviceAuthConfigPanel "
                                           "combo[fieldLabel=MAC Address Delimiter] boundlist => "
                                           ":textEquals(" + str(arg_dict["delimiter"]) + ")")

        return ui_cmd_obj
