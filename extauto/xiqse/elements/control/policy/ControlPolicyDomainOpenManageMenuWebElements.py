from common.WebElementHandler import *
from xiqse.defs.control.policy.ControlPolicyDomainOpenManageMenuWebElementsDefinitions import *


class ControlPolicyDomainOpenManageMenuWebElements(ControlPolicyDomainOpenManageMenuWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_openmanage_domains_menu(self):
        """
        :return:  Open/Manage Domain(s) menu
        """
        return self.weh.get_element(self.openmanage_domains_menu)

    def get_open_domain_menu(self):
        """
        :return:  "Open Domain" menu under Open/Manage Domain(s) dropdown menu
        """
        return self.weh.get_element(self.open_domain_menu)

    def get_lock_domain_menu(self):
        """
        :return:  "Lock Domain" menu under Open/Manage Domain(s) dropdown menu
        """
        return self.weh.get_element(self.lock_domain_menu)

    def get_save_domain_menu(self):
        """
        :return:  "Save Domain" menu under Open/Manage Domain(s) dropdown menu
        """
        return self.weh.get_element(self.save_domain_menu)

    def get_enforce_domain_menu(self):
        """
        :return:  "Enforce Domain" menu under Open/Manage Domain(s) dropdown menu
        """
        return self.weh.get_element(self.enforce_domain_menu)

    def get_enforce_preview_menu(self):
        """
        :return:  "Enforce Preview" menu under Open/Manage Domain(s) dropdown menu
        """
        return self.weh.get_element(self.enforce_preview_menu)
    def get_verify_domain_menu(self):
        """
        :return:  "Verify Domain" menu under Open/Manage Domain(s) dropdown menu
        """
        return self.weh.get_element(self.verify_domain_menu)

    def get_assign_devices_to_domain_menu(self):
        """
        :return:  "Assign Device(s) to Domain" menu under Open/Manage Domain(s) dropdown menu
        """
        return self.weh.get_element(self.assign_devices_to_domain_menu)

    def get_create_domain_menu(self):
        """
        :return:  "Create Domain" menu under Open/Manage Domain(s) dropdown menu
        """
        return self.weh.get_element(self.create_domain_menu)

    def get_delete_domain_menu(self):
        """
        :return:  "Delete Domain" menu under Open/Manage Domain(s) dropdown menu
        """
        return self.weh.get_element(self.delete_domain_menu)

    def get_rename_domain_menu(self):
        """
        :return:  "Rename Domain" menu under Open/Manage Domain(s) dropdown menu
        """
        return self.weh.get_element(self.rename_domain_menu)

    def get_import_export_menu(self):
        """
        :return:  "Import/Export" menu under Open/Manage Domain(s) dropdown menu
        """
        return self.weh.get_element(self.import_export_menu)

    def get_import_from_domain_menu(self):
        """
        :return:  "Import From Domain" menu under Open/Manage Domain(s) dropdown menu>Import/Export
        """
        return self.weh.get_element(self.import_from_domain_menu)

    def get_import_from_file_menu(self):
        """
        :return:  "Import From File" menu under Open/Manage Domain(s) dropdown menu>Import/Export
        """
        return self.weh.get_element(self.import_from_file_menu)

    def get_export_to_file_menu(self):
        """
        :return:  "Export to File" menu under Open/Manage Domain(s) dropdown menu>Import/Export
        """
        return self.weh.get_element(self.export_to_file_menu)

    def get_database_menu(self):
        """
        :return:  "Database" menu under Open/Manage Domain(s) dropdown menu
        """
        return self.weh.get_element(self.database_menu)

    def get_delete_all_policy_manager_data_menu(self):
        """
        :return:  "Delete All Policy Manager Data" menu under Open/Manage Domain(s) dropdown menu>Database
        """
        return self.weh.get_element(self.delete_all_policy_manager_data_menu)

    def get_restore_factory_default_domains_menu(self):
        """
        :return:  "Restore Factory Default Domains" menu under Open/Manage Domain(s) dropdown menu>Database
        """
        return self.weh.get_element(self.restore_factory_default_domains_menu)

    def get_delete_all_and_restore_factory_default_domains_menu(self):
        """
        :return:  "Delete All and Restore Factory Default Domains" menu under Open/Manage Domain(s) dropdown menu>Database
        """
        return self.weh.get_element(self.delete_all_and_restore_factory_default_domains_menu)