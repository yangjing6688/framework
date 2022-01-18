from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.XCA.XcaclientsConstants import XcaclientsConstants


class UiXcaClientsKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiXcaClientsKeywords, self).__init__()
        self.api_const = self.constants.API_XCA_CLIENTS
        self.command_const = XcaclientsConstants()

    def clients_select_all_clients(self, element_names, **kwargs):
        """Returns the result of clients_select_all_clients."""
        args = {}

        return self.execute_keyword(element_names, args, self.command_const.SELECT_ALL_CLIENTS, **kwargs)

    def clients_click_client_mac_address_to_open_client_info(self, element_names, client_mac_address, **kwargs):
        """Returns the result of clients_click_client_mac_address_to_open_client_info."""
        args = {"client_mac_address": client_mac_address}

        return self.execute_keyword(element_names, args,
                                    self.command_const.CLICK_CLIENT_MAC_ADDRESS_TO_OPEN_CLIENT_INFO, **kwargs)

    def clients_refresh_clients_page(self, element_names, **kwargs):
        """Returns the result of clients_refresh_clients_page."""
        args = {}

        return self.execute_keyword(element_names, args, self.command_const.REFRESH_CLIENTS_PAGE, **kwargs)

    def clients_verify_client_exists(self, element_names, client_mac_address, **kwargs):
        """Returns the result of clients_verify_client_exists."""
        args = {"client_mac_address": client_mac_address}

        return self.execute_keyword(element_names, args, self.command_const.VERIFY_CLIENT_EXISTS, **kwargs)

    def clients_verify_client_does_not_exist(self, element_names, client_mac_address, **kwargs):
        """Returns the result of clients_verify_client_does_not_exist."""
        args = {"client_mac_address": client_mac_address}

        return self.execute_keyword(element_names, args, self.command_const.VERIFY_CLIENT_DOES_NOT_EXIST, **kwargs)

    def clients_verify_client_information(self, element_names, client_mac_address, status, ip_address, host_name,
                                          device_type, ap_name, user_name, role_name, network_name, **kwargs):
        """Returns the result of clients_verify_client_information."""
        args = {"client_mac_address": client_mac_address,
                "status": status,
                "ip_address": ip_address,
                "host_name": host_name,
                "device_type": device_type,
                "ap_name": ap_name,
                "user_name": user_name,
                "role_name": role_name,
                "network_name": network_name}

        return self.execute_keyword(element_names, args, self.command_const.VERIFY_CLIENT_INFORMATION, **kwargs)
