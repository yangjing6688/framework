

class NetworkDevicesTreePanelWebElementsDefinitions:

    context_dropdown = \
        {
            'DESC': 'Tree Context dropdown in the left tree panel on the Devices tab',
            'XPATH': '//div[contains(@id, "networkDeviceView")]//input[contains(@id, "otreeselectorcombo")]',
            
        }

    site_tree_node = \
        {
            'DESC': 'Site Tree Node with name specified by element_name on the Devices tab',
            'XPATH': '//span[contains(@class, "x-tree-node-text")]/span[contains(@data-qtip, "Site ${element_name}")]',
            
        }

    tree_action_menu = \
        {
            'DESC': 'Action Menu for the left tree panel on the Devices tab',
            'XPATH': '//div[contains(@id, "deviceTree")]//span[contains(@class, "x-btn-icon-el-default-toolbar-small fa fa-bars")]',
            
        }

    maps_sites_menu = \
        {
            'DESC': 'Maps/Sites Menu in the action menu for the left tree panel on the Devices tab',
            'XPATH': '//a[@class="x-menu-item-link"]/span[text()="Maps/Sites"]',
            
        }

    create_site_menu = \
        {
            'DESC': 'Create Site Menu in the action menu for the left tree panel on the Devices tab',
            'XPATH': '//a[@class="x-menu-item-link"]/span[text()="Create Site..."]',
            
        }

    delete_site_menu = \
        {
            'DESC': 'Delete Site Menu in the action menu for the left tree panel on the Devices tab',
            'XPATH': '//a[@class="x-menu-item-link"]/span[text()="Delete Site"]',
            
        }
