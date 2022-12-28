import re
from time import sleep
from extauto.common.Screen import Screen
from extauto.common.Utils import Utils
from extauto.common.AutoActions import AutoActions
from extauto.xiq.flows.common.Navigator import Navigator
from extauto.xiq.elements.MLInsightsClients360WebElements import MLInsightsClients360WebElements
from extauto.common.CommonValidation import CommonValidation


class MLInsightClient360(MLInsightsClients360WebElements):
    def __init__(self):
        super().__init__()
        self.navigator = Navigator()
        self.screen = Screen()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.common_validation = CommonValidation()

    def _get_real_time_grid_rows(self, search_string):
        """
        - Get the grid row from the grid rows

        :param search_string: string to search the row
        :return: row obj if row exists else None
        """
        if rows := self.get_client_360_real_time_grid_rows():
            for row in rows:
                if search_string in row.text:
                    return row

    def get_real_time_client360_details(self, search_string):
        """
        - Get the client360 details in client grid
        - Client Details include "STATUS HEALTH", "HOST-NAME", "SSID" etc
        - Keyword Usage:
        - ``Get Real Time Client360 Details``

        :param search_string: string parameter to search the client in client grid ie. client mac, hostname etc
        :return: client360 details dict
        """
        client360_details = {}
        self.navigator.navigate_to_devices()
        self.navigator.navigate_to_client360()

        self.utils.print_info("Click on real time client 360 tab")
        self.auto_actions.click_reference(self.get_client_360_inactive_tab)
        self.auto_actions.click_reference(self.get_client_360_real_time_tab)

        self.utils.print_info("Click on the client 360 refresh button")
        self.auto_actions.click_reference(self.get_n360_client_360_client_refresh)
        sleep(2)

        if row := self._get_real_time_grid_rows(search_string):
            if cells := self.get_client_360_real_time_grid_row_cells(row):
                for cell in cells:
                    if re.search(r'field-\w*', cell.get_attribute("class")):
                        label = re.search(r'field-\w*', cell.get_attribute("class")).group().split("field-")[-1]
                        if label == 'clientHealth':
                            health_status_cell = self.get_client360_health_status(cell)
                            client360_details[label] = health_status_cell.get_attribute("class").split()[-1]
                            self.screen.save_screen_shot()
                        else:
                            client360_details[label] = cell.text
                self.utils.print_info(f"******************Real Client details************************")
                for key, value in client360_details.items():
                    self.utils.print_info(f"{key}:{value}")

                return client360_details

    def get_client360_current_connection_status(self, search_string, **kwargs):
        """
        - Get the client360 current connection status
        - FLow: ML Insights --> Client 360 --> Click on either device MAC hyper link or Host name hyper link
        - Client Details include "STATUS HEALTH", "HOST-NAME", "SSID" etc
        - Keyword Usage:
        - ``Get Client360 Current Connection Status        search_string``

        :param search_string: string parameter to search the client in client grid ie. client mac, hostname etc
        :return: current connection status
        """
        client360_status = {}
        self.navigator.navigate_to_devices()
        self.navigator.navigate_to_client360()

        self.utils.print_info("Click on real time client 360 tab")
        self.auto_actions.click_reference(self.get_client_360_inactive_tab)
        self.auto_actions.click_reference(self.get_client_360_real_time_tab)

        self.utils.print_info("Click on the client 360 refresh button")
        self.auto_actions.click_reference(self.get_n360_client_360_client_refresh)
        sleep(2)

        if row := self._get_real_time_grid_rows(search_string):
            for cell in self.get_client_360_real_time_grid_row_cells(row):
                if search_string in cell.text:
                    self.utils.print_info("click on device cell ", search_string)
                    self.auto_actions.click(self.get_client360_cell_href(cell))
                    sleep(5)
                    client360_status['OS_TYPE'] = self.get_client_360_status_ostype().text
                    client360_status['IP_ADDRESS'] = self.get_client_360_status_ipaddress().text
                    client360_status['MAC_ADDRESS'] = self.get_client_360_status_macaddress().text
                    client360_status['USER'] = self.get_client_360_status_user().text
                    client360_status['CONNECT_TO'] = self.get_client_360_status_connectto().text
                    client360_status['CONNECT_TIME'] = self.get_client_360_status_connecttime().text
                    client360_status['VLAN'] = self.get_client_360_status_vlan().text
                    client360_status['CWP'] = self.get_client_360_status_cwp().text
                    client360_status['USER_PROFILE'] = self.get_client_360_status_userprofile().text
                    client360_status['SSID'] = self.get_client_360_status_ssid().text
                    client360_status['RADIO'] = self.get_client_360_status_radio().text
                    client360_status['CHANNEL'] = self.get_client_360_status_channel().text
                    self.utils.print_info("Client 360 current connection status: \n", client360_status)
                    self.screen.save_screen_shot()
                    sleep(2)
                    self.utils.print_info("Close dialog current connection status,")
                    self.auto_actions.click_reference(self.client_360_close_current_connection_status)
                    return client360_status
        else:
            kwargs['fail_msg'] = f"'get_client360_current_connection_status()' -> Device not found in the " \
                                 f"grid with: {search_string}"
            self.common_validation.fault(**kwargs)
            return -1