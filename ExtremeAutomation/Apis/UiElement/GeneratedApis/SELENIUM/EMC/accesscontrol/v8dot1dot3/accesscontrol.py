from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as AccesscontrolBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Accesscontrol(AccesscontrolBase):
    def access_control_click_tree_panel(self, ui_cmd_obj, arg_dict):
        new_dict = {}
        if arg_dict['tree_name'].lower() == 'configuration':
            new_dict['tree_name'] = "nacConfigConfigTree"
        elif arg_dict['tree_name'].lower() == 'group editor':
            new_dict['tree_name'] = "nacConfigGroupTree"
        elif arg_dict['tree_name'].lower() == 'engines':
            new_dict['tree_name'] = "nacConfigApplianceTree"

        self.ext_builder.component_query(ui_cmd_obj, '#nacConfigTab ' + new_dict['tree_name'] + '[title=' +
                                         arg_dict['tree_name'] + ']', '[0].uiCls[0]')
        if ui_cmd_obj.return_data == "collapsed":
            self.ext_builder.click(ui_cmd_obj, '#nacConfigTab ' + new_dict['tree_name'] + '[title=' +
                                   arg_dict['tree_name'] + '] tool[type=expand-bottom] => .x-tool-tool-el')

        return ui_cmd_obj

    def access_control_expand_node(self, ui_cmd_obj, arg_dict):
        new_dict = {}
        if arg_dict['tree_name'].lower() == 'configuration':
            new_dict['tree_name'] = "nacConfigConfigTree"
        elif arg_dict['tree_name'].lower() == 'group editor':
            new_dict['tree_name'] = "nacConfigGroupTree"
        elif arg_dict['tree_name'].lower() == 'engines':
            new_dict['tree_name'] = "nacConfigApplianceTree"

        self.ext_builder.expand_tree_node(ui_cmd_obj, '#nacConfigTab ' + new_dict['tree_name'] + '[title=' +
                                          arg_dict['tree_name'] + ']', '[0]', 'text', arg_dict['node_name'])

        return ui_cmd_obj

    def access_control_select_node(self, ui_cmd_obj, arg_dict):
        new_dict = {}
        if arg_dict['tree_name'].lower() == 'configuration':
            new_dict['tree_name'] = "nacConfigConfigTree"
        elif arg_dict['tree_name'].lower() == 'group editor':
            new_dict['tree_name'] = "nacConfigGroupTree"
        elif arg_dict['tree_name'].lower() == 'engines':
            new_dict['tree_name'] = "nacConfigApplianceTree"

        self.ext_builder.select_tree_node(ui_cmd_obj, '#nacConfigTab ' + new_dict['tree_name'] + '[title=' +
                                          arg_dict['tree_name'] + ']', '[0]', 'text', arg_dict['node_name'])

        return ui_cmd_obj

    def access_control_collapse_node(self, ui_cmd_obj, arg_dict):
        new_dict = {}
        if arg_dict['tree_name'].lower() == 'configuration':
            new_dict['tree_name'] = "nacConfigConfigTree"
        elif arg_dict['tree_name'].lower() == 'group editor':
            new_dict['tree_name'] = "nacConfigGroupTree"
        elif arg_dict['tree_name'].lower() == 'engines':
            new_dict['tree_name'] = "nacConfigApplianceTree"

        self.ext_builder.collapse_tree_node(ui_cmd_obj, '#nacConfigTab ' + new_dict['tree_name'] + '[title=' +
                                            arg_dict['tree_name'] + ']', '[0]', 'text', arg_dict['node_name'])

        return ui_cmd_obj

    def access_control_enforce_all(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#nacConfigTab button[text=Enforce] => .x-btn-wrap',
                               wait_for_load_mask=False)
        self.ext_builder.click(ui_cmd_obj, '#nacConfigTab #nwcTreePanelEnforceAllButton => '
                                           '.x-menu-item-text', wait_for_load_mask=False)
        self.ext_builder.wait_for_item_in_table(ui_cmd_obj, 'nacConfigEnforcementGrid gridview', '[0]', 'statusCol',
                                                'Audit Completed', timeout=120)
        self.ext_builder.click(ui_cmd_obj, 'nacConfigEnforcementGrid gridview => .x-grid-row-expander')
        self.ext_builder.click(ui_cmd_obj, 'button[text=Enforce All] => .x-btn-inner-blue-small')
        self.ext_builder.component_query(ui_cmd_obj, 'title[text=Warnings Present]', '[0].config.text')
        if ui_cmd_obj.return_data == 'Warnings Present':
            self.ext_builder.click(ui_cmd_obj, '#yes => .x-btn-inner-blue-small')
        elif ui_cmd_obj.return_data != u'':
            ui_cmd_obj.error_state = False
        self.ext_builder.wait_for_item_in_table(ui_cmd_obj, 'nacConfigEnforcementGrid gridview', '[0]', 'resultCol',
                                                'Success', timeout=120)
        if not ui_cmd_obj.error_state:
            self.ext_builder.click(ui_cmd_obj, 'button[text=Close] => .x-btn-inner-default-small')

        return ui_cmd_obj
