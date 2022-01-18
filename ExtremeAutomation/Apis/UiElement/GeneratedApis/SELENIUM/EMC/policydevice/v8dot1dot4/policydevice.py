from ExtremeAutomation.Apis.UiElement.GeneratedApis.SELENIUM.EMC.policydevice.v8dot1dot3.policydevice import \
    Policydevice as PolicydeviceBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Policydevice(PolicydeviceBase):
    def policy_device_select_device_rfc3580_vlan_authorization_status(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#DeviceAuthConfigPanel combo[fieldLabel=RFC3580 VLAN Authorization] => '
                                           '.x-form-text')
        self.ext_builder.click(ui_cmd_obj, '#DeviceAuthConfigPanel combo[fieldLabel=RFC3580 VLAN Authorization] '
                                           'boundlist => :textEquals(' + str(arg_dict['rfc3580_vlan_auth_status']) +
                                           ')')

        return ui_cmd_obj

    def policy_device_click_radius_authentication_tree_panel(self, ui_cmd_obj, arg_dict):
        new_dict = {}
        if arg_dict['tree_name'].lower() == 'client settings':
            new_dict['tree_name'] = "panel[title=Client Settings]"
        elif arg_dict['tree_name'].lower() == 'authentication servers':
            new_dict['tree_name'] = "panel[title=Authentication Servers]"

        self.ext_builder.component_query(ui_cmd_obj, "#RadiusAuthConfigPanel " + new_dict['tree_name'], '[0].uiCls[0]')

        if ui_cmd_obj.return_data == "collapsed":
            self.ext_builder.click(ui_cmd_obj, "#RadiusAuthConfigPanel " + new_dict['tree_name'] +
                                   " tool[type=expand-bottom] => .x-tool-tool-el")

        return ui_cmd_obj

    def policy_device_click_radius_accounting_tree_panel(self, ui_cmd_obj, arg_dict):
        new_dict = {}
        if arg_dict['tree_name'].lower() == 'client settings':
            new_dict['tree_name'] = "panel[title=Client Settings]"
        elif arg_dict['tree_name'].lower() == 'authentication servers':
            new_dict['tree_name'] = "panel[title=Authentication Servers]"

        self.ext_builder.component_query(ui_cmd_obj, "#RadiusAcctConfigPanel " + new_dict['tree_name'], '[0].uiCls[0]')

        if ui_cmd_obj.return_data == "collapsed":
            self.ext_builder.click(ui_cmd_obj, "#RadiusAcctConfigPanel " + new_dict['tree_name'] +
                                   " tool[type=expand-bottom] => .x-tool-tool-el")

        return ui_cmd_obj

    def policy_device_select_radius_authentication_tab(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               '#policyDeviceTabPanel panel[title=RADIUS] tab[title=Authentication] => .x-tab-inner')

        return ui_cmd_obj

    def policy_device_select_radius_accounting_tab(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#policyDeviceTabPanel tab[title=Accounting] => .x-tab-inner')

        return ui_cmd_obj

    def policy_device_select_radius_authentication_response_mode(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#RadiusAuthConfigPanel '
                                           'combo[name=etsysPolicyRFC3580MapResolveReponseConflict] => .x-form-trigger')
        self.ext_builder.click(ui_cmd_obj, '#RadiusAuthConfigPanel '
                                           'combo[name=etsysPolicyRFC3580MapResolveReponseConflict] boundlist => '
                                           ':textEquals(' + str(arg_dict['radius_auth_response_mode']) + ')')

        return ui_cmd_obj

    def policy_device_apply_radius_authentication_client_settings(self, ui_cmd_obj, arg_dict):
        self.ext_builder.component_query(ui_cmd_obj, '#RadiusAuthConfigPanel #applyAuthClientSettingsButton',
                                         '[0].disabled')
        if ui_cmd_obj.return_data is False:
            self.ext_builder.click(ui_cmd_obj, '#RadiusAuthConfigPanel #applyAuthClientSettingsButton => '
                                               '.x-btn-inner-default-small')

        return ui_cmd_obj

    def policy_device_apply_radius_accounting_client_settings(self, ui_cmd_obj, arg_dict):
        self.ext_builder.component_query(ui_cmd_obj, '#RadiusAcctConfigPanel #applyAcctClientSettingsButton',
                                         '[0].disabled')
        if ui_cmd_obj.return_data is False:
            self.ext_builder.click(ui_cmd_obj, '#RadiusAcctConfigPanel #applyAcctClientSettingsButton => '
                                               '.x-btn-inner-default-small')

        return ui_cmd_obj
