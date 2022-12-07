from time import sleep
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from xiqse.flows.common.XIQSE_CommonTable import XIQSE_CommonTable
from xiqse.elements.network.devices.NetworkDevicesWebElements import NetworkDevicesWebElements
from xiqse.elements.control.ControlWebElements import ControlWebElements
from xiqse.elements.control.policy.ControlPolicyDomainWebElements import ControlPolicyDomainWebElements


class XIQSE_ControlPolicyDomain(ControlPolicyDomainWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.xiqse_table = XIQSE_CommonTable()
        self.network_device_els = NetworkDevicesWebElements()
        self.control_els = ControlWebElements()

    def xiqse_select_openmanage_domains(self):
        """
        - This keyword selects the "Open/Manage Domain(s)" and display its dropdown menu
        - It is assumed that the current view is Control>Policy.
        - Keyword Usage
        -     xiqse select openmanage domains

        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        the_menu = self.get_openmanage_domains_menu()
        if the_menu:
            self.auto_actions.click(the_menu)
            sleep(1)
            ret_val = 1
        else:
            self.utils.print_info("Cannot find 'Open/Manage Domain(s)' menu.")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_select_open_domain_menu(self):
        """
        - This keyword selects the "Open Domain" menu. This will activate the secondary dropdown menu with a list
        -   of policy domains that have already been created.
        - It is assumed that the current view is Control>Policy.
        - Keyword Usage
        -     xiqse select open domain menu

        :return: 1 if action was successful, else -1
        """
        ret_val = -1
        the_menu = self.get_open_domain_menu()
        if the_menu:
            self.auto_actions.click(the_menu)
            sleep(1)
            ret_val = 1
        else:
            self.utils.print_info("Cannot find 'Open Domain' menu.")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_select_lock_domain_menu(self):
        """
        - This keyword selects the "Lock Domain" menu option from the "Open/Manage Domain(s)" dropdown menu
        - It is assumed that the current view is Control>Policy.
        - Keyword Usage
        -     xiqse select lock domain menu

        :return: 1 if action was successful, else -1
        """
        ret_val = -1
        the_menu = self.get_lock_domain_menu()
        if the_menu:
            self.auto_actions.click(the_menu)
            ret_val = 1
        else:
            self.utils.print_info("Cannot find 'Lock Domain' menu.")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_select_save_domain_menu(self):
        """
        - This keyword selects the "Save Domain" menu option from the "Open/Manage Domain(s)" dropdown menu
        -    and starts the Save Domain action.
        - It is assumed that the current view is Control>Policy.
        - Keyword Usage
        -     xiqse select save domain menu

        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        # click "Open/Manage Domain(s)" dropdown menu
        self.xiqse_select_openmanage_domains()

        the_menu = self.get_save_domain_menu()
        if the_menu:
            self.auto_actions.click(the_menu)
            ret_val = 1
        else:
            self.utils.print_info("Cannot find 'Save Domain' menu.")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_select_enforce_domain_menu(self):
        """
        - This keyword selects the "Enforce Domain" menu option from the "Open/Manage Domain(s)" dropdown menu
        -    and starts the Enforce Domain process.
        - It is assumed that the current view is Control>Policy.
        - Keyword Usage
        -     xiqse select enforce domain menu

        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        # click "Open/Manage Domain(s)" dropdown menu
        self.xiqse_select_openmanage_domains()

        the_menu = self.get_enforce_domain_menu()
        if the_menu:
            self.auto_actions.click(the_menu)
            ret_val = 1
        else:
            self.utils.print_info("Cannot find 'Enforce Domain' menu.")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_select_enforce_preview_menu(self):
        """
        - This keyword selects the "Enforce Preview" menu option from the "Open/Manage Domain(s)" dropdown menu
        -   and launches the Enforce Preview window
        - It is assumed that the current view is Control>Policy.
        - Keyword Usage
        -     xiqse select enforce preview menu

        :return: 1 if action was successful, else -1
        """
        ret_val = -1
        the_menu = self.get_enforce_preview_menu()
        if the_menu:
            self.auto_actions.click(the_menu)
            ret_val = 1
        else:
            self.utils.print_info("Cannot find 'Enforce Preview' menu.")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_select_verify_domain_menu(self):
        """
        - This keyword selects the "Verify Domain" menu option from the "Open/Manage Domain(s)" dropdown menu
        -    and starts the Verify Domain action
        - It is assumed that the current view is Control>Policy.
        - Keyword Usage
        -     xiqse select verify domain menu

        :return: 1 if action was successful, else -1
        """
        ret_val = -1
        the_menu = self.get_verify_domain_menu()
        if the_menu:
            self.auto_actions.click(the_menu)
            ret_val = 1
        else:
            self.utils.print_info("Cannot find 'Verify Domain' menu.")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_select_assign_devices_to_domain_menu(self):
        """
        - This keyword selects the "Assign Device(s) to Domain" menu option from the "Open/Manage Domain(s)" dropdown menu
        -    and launches the Assign Device(s) to Domain window.
        - It is assumed that the current view is Control>Policy.
        - Keyword Usage
        -     xiqse select assign devices to domain menu

        :return: 1 if action was successful, else -1
        """
        ret_val = -1
        the_menu = self.get_assign_devices_to_domain_menu()
        if the_menu:
            self.auto_actions.click(the_menu)
            ret_val = 1
        else:
            self.utils.print_info("Cannot find 'Assign Device(s) to Domain' menu.")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_select_create_domain_menu(self):
        """
        - This keyword selects the "Create Domain" menu option from the "Open/Manage Domain(s)" dropdown menu
        -    and launches the Create Domain window.
        - It is assumed that the current view is Control>Policy.
        - Keyword Usage
        -     xiqse select save domain menu

        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        # click "Open/Manage Domain(s)" dropdown menu
        self.xiqse_select_openmanage_domains()

        the_menu = self.get_create_domain_menu()
        if the_menu:
            self.auto_actions.click(the_menu)
            ret_val = 1
        else:
            self.utils.print_info("Cannot find 'Create Domain' menu.")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_select_delete_domain_menu(self):
        """
        - This keyword selects the "Delete Domain" menu option from the "Open/Manage Domain(s)" dropdown menu
        -    and launches the Delete Domain window.
        - It is assumed that the current view is Control>Policy.
        - Keyword Usage
        -     xiqse select save domain menu

        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        # click "Open/Manage Domain(s)" dropdown menu
        self.xiqse_select_openmanage_domains()

        the_menu = self.get_delete_domain_menu()
        if the_menu:
            self.auto_actions.click(the_menu)
            ret_val = 1
        else:
            self.utils.print_info("Cannot find 'Delete Domain' menu.")
            self.screen.save_screen_shot()

        return ret_val
