from ExtremeAutomation.Apis.UiElement.GeneratedApis.SELENIUM.EMC.accesscontrol.v8dot2dot3.accesscontrol import \
    Accesscontrol as AccesscontrolBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Accesscontrol(AccesscontrolBase):
    def access_control_click_tree_panel(self, ui_cmd_obj, arg_dict):
        new_dict = {}
        if arg_dict['tree_name'].lower() == 'configuration':
            new_dict['tree_name'] = "nacConfigConfigTree"
        elif arg_dict['tree_name'].lower() == 'group editor':
            new_dict['tree_name'] = "nacConfigDeltaGroupTree"
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
            new_dict['tree_name'] = "nacConfigDeltaGroupTree"
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
            new_dict['tree_name'] = "nacConfigDeltaGroupTree"
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
            new_dict['tree_name'] = "nacConfigDeltaGroupTree"
        elif arg_dict['tree_name'].lower() == 'engines':
            new_dict['tree_name'] = "nacConfigApplianceTree"

        self.ext_builder.collapse_tree_node(ui_cmd_obj, '#nacConfigTab ' + new_dict['tree_name'] + '[title=' +
                                            arg_dict['tree_name'] + ']', '[0]', 'text', arg_dict['node_name'])

        return ui_cmd_obj
