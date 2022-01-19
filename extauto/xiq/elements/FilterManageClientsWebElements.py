from extauto.common.WebElementHandler import *
from extauto.xiq.defs.FilterManageClientDefinitions import *


class FilterManageClientWebElements(FilterManageClientDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_filter_client_device_list(self):
        """
        :return:  client device list
        """
        return self.weh.get_elements(self.filter_client_device_list)

    def get_filter_client_os_type_list(self):
        """
        :return:  get client os type list
        """
        return self.weh.get_elements(self.filter_client_os_type_list)

    def get_client_ssid_filter_link(self):
        return self.weh.get_element(self.filter_client_ssid_filter_link)

    def get_client_ssid_filter_checkbox(self, ssid):
        item = {}
        item['XPATH'] = self.filter_client_ssid_filter_chkbox['XPATH'] + '"' + ssid + '"' + ']'
        item['wait_for'] = 2
        return item

    def get_filter_client_connection_list(self):
        """
        :return:  client device connection list
        """
        return self.weh.get_elements(self.filter_client_connection_list)

    def get_filter_client_ssid_list(self):
        """
        :return:  client device ssid list
        """
        return self.weh.get_elements(self.filter_client_ssid_list)

    def get_filter_client_device_function_link(self):
        """
        :return:  client device function filter link
        """
        return self.weh.get_element(self.filter_client_device_function_link)

    def get_filter_client_device_function_all_chkbox(self):
        """
        :return:  client device function all filter checkbox
        """
        return self.weh.get_element(self.filter_client_device_function_all_chkbox)

    def get_filter_client_device_function_ap_chkbox(self):
        """
        :return:  client device function ap filter checkbox
        """
        return self.weh.get_element(self.filter_client_device_function_ap_chkbox)

    def get_filter_client_device_function_sw_chkbox(self):
        """
        :return:  client device function sw filter checkbox
        """
        return self.weh.get_element(self.filter_client_device_function_sw_chkbox)

    def get_page_size_100_link(self):
        """
        :return:  get page size 100
        """
        return self.weh.get_element(self.list_page_size_100_link)

    def get_filter_client_connection_link(self):
        """
        :return:  client device connection link
        """
        return self.weh.get_element(self.filter_client_device_connection_link)

    def get_filter_client_connection_all_chkbox(self):
        """
        :return:  get client all connection link
        """
        return self.weh.get_element(self.filter_client_device_connection_all_chkbox)

    def get_filter_client_connection_wired_chkbox(self):
        """
        :return:  get client device wired connection link
        """
        return self.weh.get_element(self.filter_client_device_wired_connection_chkbox)

    def get_filter_client_connection_wireless_chkbox(self):
        """
        :return:  get client device wired connection link
        """
        return self.weh.get_element(self.filter_client_device_wireless_connection_chkbox)

    def get_filter_client_os_type_link(self):
        """
        :return:  get client device wired connection link
        """
        return self.weh.get_element(self.filter_client_os_type_link)