from extauto.common.WebElementHandler import WebElementHandler
from xiqse.defs.admin.licenses.AdminLicensesAddLicenseWebElementsDefinitions import AdminLicensesAddLicenseWebElementsDefinitions


class AdminLicensesAddLicenseWebElements(AdminLicensesAddLicenseWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_text_area_add_license(self):
        """
        :return: Text Area in the Add License Dialog on the Administration> Licenses page
        """
        return self.weh.get_element(self.text_area_add_license)

    def get_ok_button_add_license(self):
        """
        :return: OK Button in the Add License Dialog on the Administration> Licenses page
        """
        return self.weh.get_element(self.ok_button_add_license)

    def get_cancel_button_add_license(self):
        """
        :return: Cancel Button in the Add License Dialog on the Administration> Licenses page
        """
        return self.weh.get_element(self.cancel_button_add_license)
