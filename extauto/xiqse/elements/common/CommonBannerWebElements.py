from extauto.common.WebElementHandler import WebElementHandler
from xiqse.defs.common.CommonBannerWebElementsDefinitions import CommonBannerWebElementsDefinitions


class CommonBannerWebElements(CommonBannerWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_connection_lost_with_xiq_banner(self):
        """
        :return: Gets the message banner for 'Connection Lost with ExtremeCloud IQ'
        """
        return self.weh.get_element(self.connection_lost_with_xiq_banner)

    def get_connection_lost_with_xiq_banner_close_button(self):
        """
        :return: Gets the close button for the Connection Lost message banner
        """
        return self.weh.get_element(self.connection_lost_with_xiq_banner_close_button)

    def get_license_limit_warning_banner(self):
        """
        :return: Gets the message banner for 'License Limit Warning: Device(s) Not Added'
        """
        return self.weh.get_element(self.license_limit_warning_banner)

    def get_license_limit_warning_banner_close_button(self):
        """
        :return: Gets the close button for the License Limit Warning message banner
        """
        return self.weh.get_element(self.license_limit_warning_banner_close_button)

    def get_licensed_device_limit_exceeded_banner(self):
        """
        :return: Gets the message banner for 'Licensed Device Limit Exceeded'
        """
        return self.weh.get_element(self.licensed_device_limit_exceeded_banner)

    def get_licensed_device_limit_exceeded_banner_close_button(self):
        """
        :return: Gets the close button for the Licensed Device Limit Exceeded message banner
        """
        return self.weh.get_element(self.licensed_device_limit_exceeded_banner_close_button)

    def get_license_expiration_banner(self):
        """
        :return: Gets the message banner for 'License Expiration'
        """
        return self.weh.get_element(self.license_expiration_banner)

    def get_license_expiration_banner_close_button(self):
        """
        :return: Gets the close button for the License Expiration message banner
        """
        return self.weh.get_element(self.license_expiration_banner_close_button)

    def get_license_enforcement_banner(self):
        """
        :return: Gets the message banner for 'License Enforcement'
        """
        return self.weh.get_element(self.license_enforcement_banner)

    def get_license_enforcement_banner_close_button(self):
        """
        :return: Gets the close button for the License Enforcement message banner
        """
        return self.weh.get_element(self.license_enforcement_banner_close_button)

    def get_location_data_unavailable_banner(self):
        """
        :return: Gets the message banner for 'Location Data Unavailable'
        """
        return self.weh.get_element(self.location_data_unavailable_banner)

    def get_location_data_unavailable_banner_close_button(self):
        """
        :return: Gets the close button for the Location Data Unavailable message banner
        """
        return self.weh.get_element(self.location_data_unavailable_banner_close_button)

    def get_no_data_available_banner(self):
        """
        :return: Gets the message banner for 'No Data Available'
        """
        return self.weh.get_element(self.no_data_available_banner)

    def get_no_data_available_banner_close_button(self):
        """
        :return: Gets the close button for the No Data Available message banner
        """
        return self.weh.get_element(self.no_data_available_banner_close_button)

    def get_motd_window(self):
        """
        :return: Gets the Message of the Day window element
        """
        return self.weh.get_element(self.motd_window)

    def get_motd_window_ok_button(self):
        """
        :return: Gets the OK button on the Message of the Day window
        """
        return self.weh.get_element(self.motd_window_ok_button)

    def get_all_banner_close_buttons(self):
        """
        :return: Gets the close button for all message banners currently displayed
        """
        return self.weh.get_elements(self.banner_close_button)
