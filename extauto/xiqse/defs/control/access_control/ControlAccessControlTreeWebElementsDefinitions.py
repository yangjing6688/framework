

class ControlAccessControlTreeWebElementsDefinitions:

    engines_tree_node = \
        {
            'DESC': 'Selecting a tree node from the access control tree',
            'XPATH': '//span[text()="${element_name}" and contains(@class, "x-tree-node-text")]',
            'wait_for': 10
        }
