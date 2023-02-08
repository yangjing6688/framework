import re
from time import sleep
from extauto.common.AutoActions import AutoActions
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.xiq.flows.common.Navigator import Navigator
from extauto.xiq.elements.ClientWebElements import ClientWebElements
from extauto.common.CommonValidation import CommonValidation


class Client:
    def __init__(self):
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.navigator = Navigator()
        self.client_web_elements = ClientWebElements()
        self.screen = Screen()
        self.commonValidation = CommonValidation()

    def get_client_row(self, client_name='default', client_mac='default'):
        """
        - Get the Client row from the grid row based on client_name or client_mac
        - Keyword Usage:
        - ``Get Client Row  client_mac=${CLIENT_MAC}``
        - ``Get Client Row  client_name=${CLIENT_NAME}``

        :param client_name: Client Name
        :param client_mac: Client Mac Address

        :return: Row information if Client information found on Grid else return None
        """
        self.utils.print_info('Getting Client row...')
        rows = self.client_web_elements.get_grid_rows()
        if not rows:
            return False
        for row in rows:
            if client_name != 'default':
                if client_name in row.text:
                    self.utils.print_info("Found Client row: ", row.text)
                    return row
            if client_mac != 'default':
                if client_mac in row.text:
                    self.utils.print_info("Found Client row: ", row.text)
                    return row

    def get_client_status(self, client_name='default', client_mac='default', **kwargs):
        """
        - Get the Client Status from the grid row based on client_name or client_mac
        - Keyword Usage:
        - ``Get Client Status  client_mac=${CLIENT_MAC}``
        - ``Get Client Status  client_name=${CLIENT_NAME}``

        :param client_name: Client Name
        :param client_mac: Client Mac Address

        :return: 1 if client entry shows green and connected else -1
        """
        client_row = -1

        self.navigator.navigate_to_client360()
        sleep(2)

        self.utils.print_info("Click on client Refresh button")
        self.auto_actions.click_reference(self.client_web_elements.get_client_page_refresh_button)
        sleep(5)

        self.screen.save_screen_shot()
        sleep(2)

        #Commenting this section of page 100 as ML-Insights->Client360 page does not have option to select pages, commenting to keep code safe for future uses
        #self.utils.print_info('Click on Page Size 100 if page exists')
        #element = self.client_web_elements.get_client_page_size_100()
        #if element != None and element.is_displayed():
            #self.auto_actions.click_reference(self.client_web_elements.get_client_page_size_100)

        self.utils.print_info('Getting Client Status using')
        if client_name != 'default':
            sleep(2)
            self.utils.print_info("Getting status of Client with name: ", client_name)
            client_row = self.get_client_row(client_name)

        if client_mac != 'default':
            sleep(2)
            self.utils.print_info("Getting status of Client with MAC: ", client_mac)
            client_row = self.get_client_row(client_mac)

        sleep(2)
        if client_row:
            sleep(5)
            client_status = self.client_web_elements.get_connection_status(client_row)
            if "CONNECTED" in client_status:
                self.utils.print_info("Client Status: Connected")
                kwargs['pass_msg'] = "Client Status: Connected"
                self.commonValidation.passed(**kwargs)
                return 1
        else:
            self.utils.print_info("Client is not present in the historical grid")
            kwargs['fail_msg'] = "Client is not present in the historical grid"
            self.commonValidation.failed(**kwargs)
            return -1

    def verify_client_status(self, client_name='default', client_mac='default', status='default'):
        """
        - This keyword returns 1 if Client status expected matches the status passed as argument
        - Keyword Usage:
        - ``Get Client Status  client_mac=${CLIENT_MAC}       status=green``
        - ``Get Client Status  client_mac=${CLIENT_MAC}       status=red``
        - ``Get Client Status  client_name=${CLIENT_NAME}     status=green``
        - ``Get Client Status  client_name=${CLIENT_NAME}     status=red``

        :param client_name: client serial number
        :param client_mac: client mac MAC
        :param status: green, red, or amber as of now - may change in future

        :return: 1 if Client status matches else None
        """
        if client_name != 'default':
            if status in self.get_client_status(client_name):
                return 1
        if client_mac != 'default':
            if status in self.get_client_status(client_mac):
                return 1

    def convert_to_client_mac(self, mac_address):
        """
        - This keyword will convert Mac address in 'xxxxxxxx:xxxxxxx' format
        - Keyword Usage:
        - ``convert to client mac  ${CLIENT_MAC}``

        :param mac_address: Mac Address to convert

        :return: Mac address entry in 'xxxxxxxx:xxxxxxx' format
        """
        client_mac = ':'.join(re.findall('..', mac_address))
        return client_mac

    def get_real_time_client_details(self, search_string, **kwargs):
        """
        - Get the real time client details from the client grid
        - Flow Manage --> Clients --> Real Time
        - Keyword Usage:
        - ``Get Real Time Client Details    ${SEARCH_STRING}``

        :param search_string: client row search  ex: client mac, device name etc
        :return: client details dict
        """
        client_details = {}
        self.navigator.navigate_to_clients()
        sleep(2)

        self.utils.print_info("Click on clients real time tab")
        self.auto_actions.click_reference(self.client_web_elements.get_clients_real_time_tab)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        if rows := self.client_web_elements.get_grid_rows():
            for row in rows:
                if search_string in row.text:
                    cells = self.client_web_elements.get_client_row_cells(row)
                    for cell in cells:
                        if re.search(r'field-\w*', cell.get_attribute("class")):
                            label = re.search(r'field-\w*', cell.get_attribute("class")).group().split("field-")[-1]
                            if label == 'clientHealth':
                                health_status_cell = self.client_web_elements.get_client_health_status(cell)
                                client_details[label] = health_status_cell.get_attribute("class").split()[-1]
                                self.screen.save_screen_shot()
                            else:
                                client_details[label] = cell.text
                    self.utils.print_info("******************Real Client details************************")
                    for key, value in client_details.items():
                        self.utils.print_info(f"{key}:{value}")

                    return client_details
        self.utils.print_info("Client is not present in the client grid")
        kwargs['fail_msg'] = "Client is not present in the historical grid"
        self.commonValidation.failed(**kwargs)
        return -1

    def delete_client_historical(self, client_mac, **kwargs):
        """
        - Clear the client from GDC
        - Flow: Manage-->Clients-->Historical
        - Keyword Usage:
        - ``Delete Client Historical  ${CLIENT_MAC}``

        :param client_mac:  Client Mac address
        :return: 1 if cleared Client Mac entry else -1
        """

        self.utils.print_info("Click on client historical tab")
        self.auto_actions.click_reference(self.client_web_elements.get_clients_historical_tab)
        sleep(5)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Get the client row")
        client_row = self.get_client_row(client_mac=client_mac)
        if client_row:
            cells = self.client_web_elements.get_client_row_cells(client_row)
            for cell in cells:
                self.utils.print_info(cell.text)
                if client_mac.upper() in cell.text.upper():
                    self.utils.print_info("Click on client MAC cell hyper link")
                    self.auto_actions.click(self.client_web_elements.get_client_mac_cell(cell))
                    sleep(5)
                    break
        else:
            self.utils.print_info(f"Client:{client_mac} is not present in the historical grid")
            return 1

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Click on client delete button")
        self.auto_actions.click_reference(self.client_web_elements.get_client_gdpr_delete_button)
        sleep(2)

        self.utils.print_info("Click on client delete confirmation yes button")
        self.auto_actions.click_reference(self.client_web_elements.get_client_gdpr_delete_yes_confirm_button)
        sleep(5)

        self.utils.print_info("click on client dialog window close button")
        self.auto_actions.click_reference(self.client_web_elements.get_client_dialog_window_close_button)
        sleep(5)

        self.utils.print_info("Click on clients real time tab")
        self.auto_actions.click_reference(self.client_web_elements.get_clients_real_time_tab)
        sleep(2)

        self.utils.print_info("Click on client historical tab")
        self.auto_actions.click_reference(self.client_web_elements.get_clients_historical_tab)
        sleep(5)

        self.screen.save_screen_shot()
        sleep(2)

        client_row = self.get_client_row(client_mac=client_mac)
        if not client_row:
            self.utils.print_info("client:{} deleted".format(client_mac))
            return 1
        kwargs['fail_msg'] = "Client is not present in the historical grid"
        self.commonValidation.failed(**kwargs)
        return -1

    def delete_client_realtime(self, client_mac, **kwargs):
        """
        - Clear the client from GDC
        - Flow: Manage-->Clients-->Historical
        - Keyword Usage:
        - ``Delete Client RealTime  ${CLIENT_MAC}``

        :param client_mac:  Client Mac address
        :return: 1 if cleared Client Mac entry else -1
        """

        self.utils.print_info("Click on client real time tab")
        self.auto_actions.click_reference(self.client_web_elements.get_clients_real_time_tab)
        sleep(5)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Get the client row")
        client_row = self.get_client_row(client_mac=client_mac)
        if client_row:
            cells = self.client_web_elements.get_client_row_cells(client_row)
            for cell in cells:
                self.utils.print_info(cell.text)
                if client_mac.upper() in cell.text.upper():
                    self.utils.print_info("Click on client MAC cell hyper link")
                    self.auto_actions.click(self.client_web_elements.get_client_mac_cell(cell))
                    sleep(5)
                    break
        else:
            self.utils.print_info(f"Client:{client_mac} is not present in the real time grid")
            return 1

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Click on client delete button")
        self.auto_actions.click_reference(self.client_web_elements.get_client_gdpr_delete_button)
        sleep(2)

        self.utils.print_info("Click on client delete confirmation yes button")
        self.auto_actions.click_reference(self.client_web_elements.get_client_gdpr_delete_yes_confirm_button)
        sleep(5)

        self.utils.print_info("click on client dialog window close button")
        self.auto_actions.click_reference(self.client_web_elements.get_client_dialog_window_close_button)
        sleep(5)

        self.utils.print_info("Click on client historical tab")
        self.auto_actions.click_reference(self.client_web_elements.get_clients_historical_tab)
        sleep(5)

        self.utils.print_info("Click on clients real time tab")
        self.auto_actions.click_reference(self.client_web_elements.get_clients_real_time_tab)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        client_row = self.get_client_row(client_mac=client_mac)
        if not client_row:
            self.utils.print_info("client:{} deleted".format(client_mac))
            return 1
        kwargs['fail_msg'] = "Could Not Clear the client from GDC"
        self.commonValidation.failed(**kwargs)
        return -1

    def _get_client360_details(self):
        """
        - This keyword gets Client 360 Information
        - It Assumes That Already Navigated to Client360 Page
        - Flow : Client 360 Page
        - Keyword Usage
        - ``Get Client360 details``

        :return: dictionary of client360 information
        """
        sleep(10)
        self.utils.print_info("Getting Client360 Information.")
        client360_info = {}
        client360_info["operating_system"] = self.client_web_elements.get_client360_os_type_field().text
        client360_info["ip_address"] = self.client_web_elements.get_client360_ip_address_field().text
        client360_info["mac_address"] = self.client_web_elements.get_client360_mac_address_field().text
        client360_info["connected_ap"] = self.client_web_elements.get_client360_connected_ap_info_field().text
        client360_info["connected_vlan"] = self.client_web_elements.get_client360_vlan_field().text
        client360_info["captive_web_portal"] = self.client_web_elements.get_client360_captive_web_portal_field().text
        client360_info["user_profile"] = self.client_web_elements.get_client360_user_profile_field().text
        client360_info["user_name"] = self.client_web_elements.get_client360_user_name_field().text
        client360_info["connected_ssid"] = self.client_web_elements.get_client360_ssid_field().text
        client360_info["radio_protocol"] = self.client_web_elements.get_client360_radio_mac_protocol_field().text
        client360_info["radio_used"] = self.client_web_elements.get_client360_radio_field().text
        client360_info["channel_used"] = self.client_web_elements.get_client360_channel_field().text

        self.utils.print_info("******************Client360 Information************************")
        for key, value in client360_info.items():
            self.utils.print_info(f"{key}:{value}")

        self.utils.print_info("Closing client360 Dialogue Window.")
        self.auto_actions.click_reference(self.client_web_elements.get_client_dialog_window_close_button)
        sleep(2)

        return client360_info

    def get_real_time_client360_information(self, client_mac, **kwargs):
        """
        - Get the real time client details from the client grid
        - Flow : Manage--> clients--> Client MAC hyper Link-->Client 360 Page
        - Keyword Usage:
        - ``Get Real Time Client360 Information    ${CLIENT_MAC}``

        :param client_mac: client mac address
        :return: client 360 details dictionary if MAC entry found on clients grid else -1
        """
        self.navigator.navigate_to_clients()
        sleep(2)

        self.utils.print_info("Click on clients real time tab")
        self.auto_actions.click_reference(self.client_web_elements.get_clients_real_time_tab)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Get the client row")
        client_row = self.get_client_row(client_mac=client_mac)
        if client_row:
            cells = self.client_web_elements.get_client_row_cells(client_row)
            for cell in cells:
                self.utils.print_info(cell.text)
                if client_mac.upper() in cell.text.upper():
                    if self.client_web_elements.get_client_mac_cell(cell):
                        self.utils.print_info("Click on client MAC cell hyper link")
                        self.auto_actions.click(self.client_web_elements.get_client_mac_cell(cell))
                        break
            client360_details = self._get_client360_details()
            return client360_details
        else:
            self.utils.print_info(f"Client360 Information For:{client_mac} is not Found")
            kwargs['fail_msg'] = f"Client360 Information For:{client_mac} is not Found"
            self.commonValidation.failed(**kwargs)
            return -1

    def convert_mac_to_colon_Format(self, mac_address):
        """
        - This keyword will convert Mac address from 'XXXXXXXXXXXX' to 'xx:xx:xx:xx:xx:xx' format
        - Keyword Usage:
        - ``convert mac to colon format  ${ANY_MAC}``

        :param mac_address: Mac Address to convert

        :return: Mac address in 'xx:xx:xx:xx:xx:xx' format
        """
        lower_case = mac_address.lower()
        temp_split_mac = re.findall('..',lower_case)
        mac_with_colon = ":".join(temp_split_mac)
        return mac_with_colon