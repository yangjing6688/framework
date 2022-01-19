from xiq.defs.LicenseManagementWebElementsDefs import *
from common.AutoActions import *
from common.WebElementHandler import *


class LicenseManagementWebElements(LicenseManagementWebElementsDefs):
    def __init__(self):
        self.weh = WebElementHandler()
        self.auto_actions = AutoActions()
        self.utils = Utils()

    def get_entitlements_no_data(self):
        """
        :return: No Data element for the Entitlements table
        """
        return self.weh.get_element(self.entitlements_no_data)

    def get_legacy_no_data(self):
        """
        :return: No Data element for the Legacy Entitlements table
        """
        return self.weh.get_element(self.legacy_no_data)

    def get_xiq_not_linked_to_extreme_portal_status(self):
        """
        :return: xiq not linked to extreme portal text
        """
        return self.weh.get_element(self.xiq_not_linked_to_extreme_portal_status)

    def get_xiq_cust_partner_info(self):
        """
        :return: info message shown to customers and partners
        """
        return self.weh.get_element(self.xiq_cust_partner_info)

    def get_link_to_extr_portal_btn(self):
        """
        :return when xiq is not linked, link to extreme portal button element
        """
        return self.weh.get_element(self.link_xiq_to_extreme_portal_btn)

    def get_extr_licensing_portal_btn(self):
        """
        :return after linked, extreme licensing button must be seen
        """
        return self.weh.get_element(self.extreme_licensing_portal_btn)

    def get_unlink_xiq_from_extr_portal_btn(self):
        """
        :return: after linked, unlink button must be visible
        """
        return self.weh.get_element(self.unlink_xiq_from_extr_portal_btn)

    def get_xiq_linked_to_extreme_portal_status(self):
        """
        :return: xiq not linked to extreme portal text
        """
        return self.weh.get_element(self.xiq_linked_to_extreme_portal_status)

    def get_unlink_confirm_no_btn(self):
        return self.weh.get_element(self.unlink_confirm_no_btn)

    def get_unlink_confirm_yes_btn(self):
        return self.weh.get_element(self.unlink_confirm_yes_btn)

    def get_unlink_confirm_msg(self):
        return self.weh.get_element(self.unlink_confirm_msg)

    def get_contact_sales_btn(self):
        """
        :return: contact sales button must be present
        """
        return self.weh.get_element(self.contact_sales_btn)

    def get_gemalto_entitlements_table_header(self):
        """
        :return: Entitlements heading is displayed
        """
        return self.weh.get_element(self.gemalto_entitlements_table_header)

    def get_legacy_entitlements_table_header(self):
        """
        :return: legacy entitlements heading is displayed
        """
        return self.weh.get_element(self.legacy_entitlements_table_header)

    def get_legacy_ek_data(self):
        """
        :return: legacy Eks in the table
        """
        return self.weh.get_elements(self.legacy_ek_data)

    def get_license_table_iframe(self):
        return self.weh.get_element(self.license_table_iframe)

    def get_upgrade_dialog_msg(self):
        return self.weh.get_element(self.upgrade_dialog_msg)

    def get_upgrade_iagree_chkbox(self):
        return self.weh.get_element(self.upgrade_iagree_chkbox)

    def get_upgrade_continue_btn(self):
        return self.weh.get_element(self.upgrade_continue_btn)

    def get_upgrade_cancel_btn(self):
        return self.weh.get_element(self.upgrade_cancel_btn)

    def get_entitlements_rows(self):
        """
        :return: all the rows in the Entitlements grid
        """
        grid_rows = self.weh.get_elements(self.entitlements_rows)
        if grid_rows:
            return grid_rows
        else:
            return None

    def get_entitlements_row_feature_value(self, row):
        """
        :param row: row to return the feature value for
        :return: value in the Feature column for the specified row of the Entitlements table
        """
        return self.weh.get_element(self.entitlements_table_feature_col, row)

    def get_entitlements_row_devices_value(self, row):
        """
        :param row: row to return the devices value for
        :return: value in the Devices column for the specified row of the Entitlements table
        """
        return self.weh.get_element(self.entitlements_table_devices_col, row)

    def get_entitlements_row_available_value(self, row):
        """
        :param row: row to return the available value for
        :return: value in the Available column for the specified row of the Entitlements table
        """
        return self.weh.get_element(self.entitlements_table_available_col, row)

    def get_entitlements_row_activated_value(self, row):
        """
        :param row: row to return the activated value for
        :return: value in the Activated column for the specified row of the Entitlements table
        """
        return self.weh.get_element(self.entitlements_table_activated_col, row)

    def get_checkbox_for_legacy_ek(self):
        """
        :return: legacy Eks in the table
        """
        return self.weh.get_elements(self.legacy_ek_checkbox())

    def get_ekey_remove_deactivate_btn(self):
        """
        :return: remove/deactivate button element
        """
        return self.weh.get_element(self.ekey_remove_deactivate_btn)

    def get_ekey_del_confirm_btn(self):
        return self.weh.get_element(self.ekey_del_confirm_btn)

    def get_ekey_del_cancel_btn(self):
        return self.weh.get_element(self.ekey_del_cancel_btn)

    def get_ekey_del_success_msg(self):
        return self.weh.get_element(self.ekey_del_success_msg)

    def get_ekey_del_confirm_msg_ok_btn(self):
        return self.weh.get_element(self.ekey_del_confirm_msg_ok_btn)
