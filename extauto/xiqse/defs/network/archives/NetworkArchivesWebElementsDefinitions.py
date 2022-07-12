

class NetworkArchivesWebElementsDefinitions:

    create_button = \
        {
            'DESC': 'Create button on the Network> Archives page',
            'XPATH': '//div[contains(@id, "archiveTree")]//a[@data-qtip="Create Archive"]',
            
        }

    refresh_button = \
        {
            'DESC': 'Refresh button on the Network> Archives page',
            'XPATH': '//div[contains(@id, "archiveTree")]//span[text()="Refresh"]/ancestor::a',
            
        }

    archive_tree_node = \
        {
            'DESC': 'Archive tree node with the name specified by element_name',
            'XPATH': '//div[contains(@id, "archiveTree")]//td//span[text()="${element_name}"]',
            
        }

    archive_stamp_menu = \
        {
            'DESC': 'Stamp New Version menu item for an archive in the Archives tree',
            'XPATH': '//div[contains(@class, "x-menu-item")]//span[text()="Stamp New Version"]',
            
        }

    archive_delete_menu = \
        {
            'DESC': 'Delete menu item for an archive in the Archives tree',
            'XPATH': '//div[contains(@class, "x-menu-item")]//span[text()="Delete"]',
            
        }
