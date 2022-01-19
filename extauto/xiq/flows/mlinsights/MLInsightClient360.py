import re
from time import sleep
from extauto.common.Screen import Screen
from extauto.common.Utils import Utils
from extauto.common.AutoActions import AutoActions
from xiq.flows.common.Navigator import Navigator
from xiq.elements.MLInsightsClients360WebElements import MLInsightsClients360WebElements


class MLInsightClient360(MLInsightsClients360WebElements):
    def __init__(self):
        super().__init__()
        self.navigator = Navigator()
        self.screen = Screen()
        self.utils = Utils()
        self.auto_actions = AutoActions()

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
        self.navigator.navigate_to_client360()

        self.utils.print_info("Click on real time client 360 tab")
        self.auto_actions.click(self.get_client_360_real_time_tab())

        self.utils.print_info("Click on the client 360 refresh button")
        self.auto_actions.click(self.get_n360_client_360_client_refresh())
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
