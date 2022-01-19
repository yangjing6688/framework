class ControlPolicyRuleTreeWebElementsDefinitions:

    rule_tree_node = \
    {
        'DESC': 'Control->Policy->Service>Rule tree panel>rule node',
        'XPATH': '//span[contains(@class,"x-tree-node-text") and text()="${rule_name}"]',
        'wait_for': 10
    }
