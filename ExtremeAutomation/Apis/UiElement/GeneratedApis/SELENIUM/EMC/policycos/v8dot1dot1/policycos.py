from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as PolicycosBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Policycos(PolicycosBase):
    def policy_cos_select_cos_node(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "#policyNavTab #PolicyDomainView #policyDomainViewNavigationTrees "
                                           "#policyTreesPanel #cosTree treeview => "
                                           ".x-tree-node-text:contains(" + arg_dict['tree-node'] + ")")
        return ui_cmd_obj

    def policy_cos_edit_irl_index(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, r'#policyNavTab #PolicyDomainView #domainNodeDetailsPanelContainer '
                                           r':ariadne-nth-child(12) button[text=Edit\.\.\.] => '
                                           r'.x-btn-inner-default-small')
        self.ext_builder.enter_text(ui_cmd_obj, '#editIndexWin #editRlValue => .x-form-text', arg_dict['irl_index'])
        self.ext_builder.click(ui_cmd_obj, '#editIndexWin button[text=OK] => .x-btn-inner-blue-small')

        return ui_cmd_obj

    def policy_click_tree_panel(self, ui_cmd_obj, arg_dict):
        new_dict = {}
        if arg_dict['tree_name'].lower() == 'roles/services':
            new_dict['tree_name'] = "#policyTree"
        elif arg_dict['tree_name'].lower() == 'class of service':
            new_dict['tree_name'] = "#cosTree"
        elif arg_dict['tree_name'].lower() == 'vlans':
            new_dict['tree_name'] = "#vlanTree"
        elif arg_dict['tree_name'].lower() == 'network resources':
            new_dict['tree_name'] = "#nrTree"
        elif arg_dict['tree_name'].lower() == 'devices/port groups':
            new_dict['tree_name'] = "#devicePortTreesPanel"

        self.ext_builder.component_query(ui_cmd_obj, "#policyNavTab #PolicyDomainView #policyDomainViewNavigationTrees "
                                                     "#policyTreesPanel " + new_dict['tree_name'], '[0].uiCls[0]')
        if ui_cmd_obj.return_data == "collapsed":
            self.ext_builder.click(ui_cmd_obj, "#policyNavTab #PolicyDomainView #policyDomainViewNavigationTrees "
                                               "#policyTreesPanel " + new_dict['tree_name'] + " title => .x-title-text")

        return ui_cmd_obj

    def policy_cos_create(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#policyNavTab #PolicyDomainView #policyDomainViewNavigationTrees '
                                           '#policyTreesPanel #cosTree title => .x-title-text')
        self.ext_builder.right_click(ui_cmd_obj, '#policyNavTab #PolicyDomainView #policyDomainViewNavigationTrees '
                                                 '#policyTreesPanel #cosTree treeview => '
                                                 '.x-tree-node-text:textEquals(Class of Service)')
        self.ext_builder.click(ui_cmd_obj, r'menuitem[text=Create COS\.\.\.] => .x-menu-item-text')
        self.ext_builder.enter_text(ui_cmd_obj, arg_dict['cos_name'], '#renameObjectWin #renameValue => .x-form-text')
        self.ext_builder.click(ui_cmd_obj, '>>#renameObjectWin button[text=OK]')
        return ui_cmd_obj

    def policy_cos_create_rate_limit(self, ui_cmd_obj, arg_dict):
        # self.ext_builder.click(ui_cmd_obj,
        #                                '#policyNavTab #PolicyDomainView #policyDomainViewNavigationTrees
        # #policyTreesPanel #cosTree title => .x-title-text')
        self.ext_builder.right_click(ui_cmd_obj, '#policyNavTab #PolicyDomainView #policyDomainViewNavigationTrees '
                                                 '#policyTreesPanel #cosTree treeview => '
                                                 '.x-tree-node-text:textEquals(Rate Limits)')
        self.ext_builder.click(ui_cmd_obj, 'menuitem[text=Create Rate Limit] => .x-menu-item-link')
        self.ext_builder.click(ui_cmd_obj, r'#policyNavTab #PolicyDomainView #domainNodeDetailsPanelContainer '
                                           r'#rateLimitDetailsPanel button[text=Edit\.\.\.] => '
                                           r'.x-btn-inner-default-small')
        self.ext_builder.enter_text(ui_cmd_obj, arg_dict['speed'], '#editRateWin #rateLimitValueSet => .x-form-text')
        self.ext_builder.click(ui_cmd_obj, '#editRateWin #rateLimitUnitSet => .x-form-text')
        self.ext_builder.click(ui_cmd_obj, '#editRateWin #rateLimitUnitSet boundlist => :textEquals(' + str(
                                           arg_dict['rate']) + ')')
        self.ext_builder.click(ui_cmd_obj, '#editRateWin button[text=OK] => .x-btn-inner-blue-small')
        return ui_cmd_obj

    def policy_cos_set_irl_index(self, ui_cmd_obj, arg_dict):
        self.ext_builder.component_query(
            ui_cmd_obj, "[title=Rate Limiting / Rate Shaping]", '[0].items.items[11].items.items[1].id')
        self.ext_builder.click(ui_cmd_obj, "#" + ui_cmd_obj.return_data)
        self.ext_builder.enter_text(ui_cmd_obj, arg_dict['index'], '#editIndexWin #editRlValue => .x-form-text')
        self.ext_builder.click(ui_cmd_obj, '#editIndexWin button[text=OK] => .x-btn-inner-blue-small')
        return ui_cmd_obj

    def policy_cos_delete_cos(self, ui_cmd_obj, arg_dict):
        self.ext_builder.right_click(ui_cmd_obj, '#policyNavTab #PolicyDomainView #policyDomainViewNavigationTrees '
                                                 '#policyTreesPanel #cosTree treeview => '
                                                 '.x-tree-node-text:textEquals(' + str(arg_dict['cos_name']) + ')')
        self.ext_builder.click(ui_cmd_obj, 'menu(true){isVisible()} menuitem[text=Delete] => .x-menu-item-link')
        self.ext_builder.click(ui_cmd_obj, '#yes => .x-btn-inner-blue-small')
        return ui_cmd_obj

    def policy_cos_delete_rate_limit(self, ui_cmd_obj, arg_dict):
        self.ext_builder.right_click(ui_cmd_obj, '#policyNavTab #PolicyDomainView #policyDomainViewNavigationTrees '
                                                 '#policyTreesPanel #cosTree treeview => '
                                                 '.x-tree-node-text:contains(' + str(arg_dict['rate_limit']) + ')')
        self.ext_builder.click(ui_cmd_obj, 'menu(true){isVisible()} menuitem[text=Delete] => .x-menu-item-link')
        self.ext_builder.click(ui_cmd_obj, '#yes => .x-btn-inner-blue-small')
        return ui_cmd_obj

    def policy_cos_edit_txq_index(self, ui_cmd_obj, arg_dict):
        self.ext_builder.component_query(
            ui_cmd_obj, "[title=Rate Limiting / Rate Shaping]", '[0].items.items[15].items.items[1].id')
        self.ext_builder.click(ui_cmd_obj, "#" + ui_cmd_obj.return_data)
        self.ext_builder.enter_text(ui_cmd_obj, arg_dict['index'], '#editIndexWin #editRlValue => .x-form-text')
        self.ext_builder.click(ui_cmd_obj, '#editIndexWin button[text=OK] => .x-btn-inner-blue-small')
        return ui_cmd_obj

    def policy_cos_edit_tos(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#policyNavTab #PolicyDomainView #domainNodeDetailsPanelContainer '
                                           '#dscpTosEditBtn => .x-btn-inner-default-small')
        return ui_cmd_obj

    def policy_cos_enable_tos(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#policyNavTab #PolicyDomainView #domainNodeDetailsPanelContainer '
                                           '#cosTosCbox => .x-form-cb-input')
        return ui_cmd_obj

    def policy_cos_edit_tos_hex_value(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#tosHexRadio => .x-form-cb-label')
        self.ext_builder.enter_text(ui_cmd_obj, arg_dict['tos_value'], '#tosHexPane #tosHexField => .x-form-text')
        self.ext_builder.click(ui_cmd_obj, '#editDscpTosOkBtn => .x-btn-button')
        return ui_cmd_obj

    def policy_cos_set_orl_index(self, ui_cmd_obj, arg_dict):
        self.ext_builder.component_query(ui_cmd_obj, "[title=Rate Limiting / Rate Shaping]",
                                         '[0].items.items[12].items.items[1].id')
        self.ext_builder.click(ui_cmd_obj, "#" + ui_cmd_obj.return_data)
        self.ext_builder.enter_text(ui_cmd_obj, arg_dict['index'], '#editIndexWin #editRlValue => .x-form-text')
        self.ext_builder.click(ui_cmd_obj, '#editIndexWin button[text=OK] => .x-btn-inner-blue-small')
        return ui_cmd_obj

    def new_stub(self, ui_cmd_obj, arg_dict):
        self.ext_builder.component_query(ui_cmd_obj, "[title=Rate Limiting / Rate Shaping]",
                                         '[0].items.items[15].items.items[1].id')

        self.ext_builder.component_query(
            ui_cmd_obj, "[title=Rate Limiting / Rate Shaping]", '[0].items.items[15].items.items[1].id')
        self.ext_builder.click(ui_cmd_obj, "#" + ui_cmd_obj.return_data)
        return ui_cmd_obj
