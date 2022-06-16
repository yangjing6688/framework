class ControlPolicyWebElementsDefinitions:

    accordian_tab_template = \
        {
            'DESC': 'Control->Policy->${title} accordian tab',
            'XPATH': '//div[contains(@id, "treepanel") and contains(text(),"${title}")]',
            
        }

    
    devices_port_groups_tab = \
        {
            'DESC': 'Control->Policy->Devices/Port Groups accordian tab',
            'XPATH': '//div[contains(@id, "tabpanel") and contains(text(), "Devices/Port Groups")]',
            
        }

    menu_action_template = \
        {
            'DESC': '${action} Menu in the action menu for the tree panel',
            'XPATH': '//div[contains(@class,"x-menu") and @aria-hidden="false"]//a[@class="x-menu-item-link"]/span[contains(text(),"${action}")]',
            
        }

    root_tree_node_template = \
        {
            'DESC': 'Control->Policy->${rootName} tree root node',
            'XPATH': '//span[contains(@class, "x-tree-node-text") and text()="${rootName}"]',
            
        }

    root_tree_expanded_template = \
        {
            'DESC': 'Control->Policy->${rootName} tree root node expaneded attribute',
            'XPATH': '//span[contains(@class, "x-tree-node-text") and text()="${rootName}"]/ancestor::tr[@aria-expanded="${isExpanded}"]',
            
        }

    root_tree_expander_arrow_template = \
        {
            'DESC': 'Control->Policy->${rootName} tree root node expaneded attribute',
            'XPATH': '//span[contains(@class, "x-tree-node-text") and text()="${rootName}"]/../div[contains(@class, "x-tree-expander")]',
            
        }

    cached_unsaved_changes_window = \
        {
            'DESC': '"Cached Policy Domain - Unsaved Changes" window',
            'XPATH': '//div[contains(@id,"messagebox") and text()="Cached Policy Domain - Unsaved Changes"]',
            'wait_for': 3
        }

    cached_unsaved_changes_no_button = \
        {
            'DESC': 'No button in "Cached Policy Domain - Unsaved Changes" window',
            'XPATH': '//div[contains(@id,"messagebox")]//span[text()="No"]',
            'wait_for': 3
        }

    cached_unsaved_changes_ok_button = \
        {
            'DESC': 'OK button in "Cached Policy Domain - Unsaved Changes" window',
            'XPATH': '//div[contains(@id,"messagebox")]//span[text()="OK"]',
            'wait_for': 3
        }
