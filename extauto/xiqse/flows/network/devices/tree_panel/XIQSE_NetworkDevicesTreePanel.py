from time import sleep
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from xiqse.elements.common.CommonViewWebElements import CommonViewWebElements
from xiqse.elements.network.devices.tree_panel.NetworkDevicesTreePanelWebElements import NetworkDevicesTreePanelWebElements
from xiqse.flows.network.devices.tree_panel.XIQSE_NetworkDevicesTreePanelCreateSite import XIQSE_NetworkDevicesTreePanelCreateSite
from xiqse.flows.network.devices.tree_panel.XIQSE_NetworkDevicesTreePanelDeleteSite import XIQSE_NetworkDevicesTreePanelDeleteSite


class XIQSE_NetworkDevicesTreePanel(NetworkDevicesTreePanelWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.view_el = CommonViewWebElements()
        self.create_site_dlg = XIQSE_NetworkDevicesTreePanelCreateSite()
        self.delete_site_dlg = XIQSE_NetworkDevicesTreePanelDeleteSite()

    def xiqse_devices_select_device_tree_context(self, the_value):
        """
         - This keyword selects the device tree context in the left tree panel on the Network> Devices Tab
         - Keyword Usage
          - ``XIQSE Devices Select Device Tree Context   by Contact``
          - ``XIQSE Devices Select Device Tree Context   by Device Type``
          - ``XIQSE Devices Select Device Tree Context   by IP``
          - ``XIQSE Devices Select Device Tree Context   by Location``
          - ``XIQSE Devices Select Device Tree Context   Extended Bridges``
          - ``XIQSE Devices Select Device Tree Context   Sites``
          - ``XIQSE Devices Select Device Tree Context   User Device Groups``
          - ``XIQSE Devices Select Device Tree Context   Wireless Controllers``

        :param the_value: tree context to select
        :return: 1 if action was successful, else -1
        """
        ret_val = -1
        the_field = self.get_context_dropdown()
        if the_field:
            self.utils.print_info("Opening Device Tree Context dropdown")
            self.auto_actions.click(the_field)

            # Obtain the dropdown items
            the_id = self.view_el.get_dropdown_id(the_field)
            self.utils.print_debug(f"Got dropdown ID {the_id}")
            the_items = self.view_el.get_list_dropdown_items(the_id)
            if the_items:
                self.utils.print_debug(f"Device Tree Context items count is {len(the_items)}")
                if self.auto_actions.select_drop_down_options(the_items, the_value):
                    self.utils.print_info(f"Selected {the_value} in the Device Tree Context dropdown")
                    ret_val = 1
                else:
                    self.utils.print_info(f"Did not find {the_value} in the Device Tree Context dropdown")
                    self.screen.save_screen_shot()

                    # Click the dropdown again to close it
                    self.auto_actions.click(the_field)
            else:
                self.utils.print_info("Unable to get the Device Tree Context dropdown items")
                self.screen.save_screen_shot()

                # Click the dropdown again to close it
                self.auto_actions.click(the_field)
        else:
            self.utils.print_info("Could not find Device Tree Context dropdown in the device tree panel")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_devices_select_site_tree_node(self, site):
        """
         - This keyword selects the specified site tree node on the Network> Devices Tab
         - Keyword Usage
          - ``XIQSE Devices Select Site Tree Node   ${SITE}``

        :param site: name of site tree node to select
        :return: 1 if action was successful, else -1
        """
        ret_val = -1
        the_node = self.get_site_tree_node(site)
        if the_node:
            self.utils.print_info(f"Selecting {site} Tree Node...")
            self.auto_actions.click(the_node)
            ret_val = 1
            sleep(2)
        else:
            self.utils.print_info(f"Unable to select the {site} tree node")
            self.screen.save_screen_shot()
        return ret_val

    def xiqse_devices_create_site(self, site):
        """
         - This keyword creates the specified site on the Network> Devices Tab
         - Keyword Usage
          - ``XIQSE Devices Create Site   ${SITE}``

        :param site: name of site to create
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        tree_action_menu = self.get_tree_action_menu()
        if tree_action_menu:
            self.utils.print_info("Clicking tree action menu...")
            self.auto_actions.click(tree_action_menu)
            maps_sites_menu = self.get_maps_sites_menu()
            if maps_sites_menu:
                self.utils.print_info("Clicking 'Maps/Sites' menu...")
                self.auto_actions.click(maps_sites_menu)
                create_site_menu = self.get_create_site_menu()
                if create_site_menu:
                    self.utils.print_info("Clicking 'Create Site...' menu to open the Create Site dialog")
                    self.auto_actions.click(create_site_menu)
                    sleep(2)

                    # Enter the Name of the site in the Create Site dialog
                    ret_val = self.create_site_dlg.xiqse_create_site_dialog_set_name(site)

                    # Click the OK button
                    if ret_val != -1:
                        sleep(2)
                        ret_val = self.create_site_dlg.xiqse_create_site_dialog_click_ok()
                    else:
                        # An error occurred so click Cancel
                        ret_val = self.create_site_dlg.xiqse_create_site_dialog_click_cancel()
                else:
                    self.utils.print_info("Unable to find 'Create Site...' menu")
            else:
                self.utils.print_info("Unable to find 'Maps/Sites' menu")
        else:
            self.utils.print_info("Unable to find tree action menu")

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_devices_delete_site(self, site):
        """
         - This keyword deletes the specified site from the Network> Devices Tab
         - Keyword Usage
          - ``XIQSE Devices Delete Site   ${SITE}``

        :param site: name of site to delete
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        if self.xiqse_devices_select_site_tree_node(site):
            tree_action_menu = self.get_tree_action_menu()
            if tree_action_menu:
                self.utils.print_info("Clicking tree action menu...")
                self.auto_actions.click(tree_action_menu)
                maps_sites_menu = self.get_maps_sites_menu()
                if maps_sites_menu:
                    self.utils.print_info("Clicking 'Maps/Sites' menu...")
                    self.auto_actions.click(maps_sites_menu)
                    delete_site_menu = self.get_delete_site_menu()
                    if delete_site_menu:
                        self.utils.print_info("Clicking 'Delete Site' menu...")
                        self.auto_actions.click(delete_site_menu)
                        sleep(2)

                        # Confirm the delete
                        ret_val = self.delete_site_dlg.xiqse_delete_site_confirm_delete()
                    else:
                        self.utils.print_info("Unable to find 'Delete Site' menu")
                else:
                    self.utils.print_info("Unable to find 'Maps/Sites' menu")
            else:
                self.utils.print_info("Unable to find tree action menu")
        else:
            self.utils.print_info(f"Site {site} is not present in the tree panel - already deleted?")
            ret_val = 1

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val
