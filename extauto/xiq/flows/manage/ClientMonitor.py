from time import sleep
from extauto.common.Screen import Screen
from extauto.common.Utils import Utils
from extauto.common.AutoActions import AutoActions
from extauto.xiq.elements.ClientMonitorWebElements import ClientMonitorWebElements
from extauto.xiq.flows.common.Navigator import Navigator


class ClientMonitor(ClientMonitorWebElements):
    def __init__(self):
        super().__init__()
        self.navigator = Navigator()
        self.screen = Screen()
        self.utils = Utils()
        self.auto_actions = AutoActions()

    def get_authentication_counts(self):
        """
        - Flow: Manage --> Client Monitor & Diagnosis --> Client Monitor
        - get ths issue authentication counts from authentication status card
        - Keyword Usage:
        - ``Get Authentication Counts``

        :return: client authentication issue count
        """
        self.navigator.navigate_to_client_monitor_and_diagnosis_tab()
        self.screen.save_screen_shot()
        sleep(2)

        self.auto_actions.click_reference(self.get_client_monitor_tab)
        sleep(2)
        auth_issue_count = self.get_auth_issue_counts_status_card().text
        self.utils.print_info(f"Authentication issue count:{auth_issue_count}")
        return auth_issue_count
        try
        except:
            pass

    def get_client_issue_entries(self, search_string, issue_type="All", issue_state="All"):
        """
        - Flow: Manage --> Tools --> Client Monitor
        - Get the client issue entries from the client issue grid rows,
        - Keyword Usage:
        - ``Get Client Issue Entries   ${CLIENT_MAC}``

        :param search_string: sting to search the client issue rows, it may be detected time, client mac
        :param issue_type: type of the issue i.e Authentication, Association, Networking
        :param issue_state: state of the issue, i.e Active, All, Resolved, Escalated
        :return: client issue detail dict
        """
        client_issue_details = {}
        self.navigator.navigate_to_tools_page()
        self.auto_actions.click_reference(self.get_client_monitor_tab)
        sleep(2)

        self.utils.print_info("click on issue type drop down")
        self.auto_actions.click_reference(self.get_issue_type_drop_down)
        sleep(2)

        issue_type_els = self.get_issue_type_drop_down_options(self.get_issue_type_drop_down())
        self.auto_actions.select_drop_down_options(issue_type_els, issue_type)

        self.utils.print_info("click on issue state drop down")
        self.auto_actions.click_reference(self.get_issue_status_drop_down)
        sleep(2)

        issue_state_els = self.get_issue_status_drop_down_options(self.get_issue_status_drop_down())
        self.auto_actions.select_drop_down_options(issue_state_els, issue_state)
        sleep(2)

        self.auto_actions.scroll_down()
        sleep(2)

        for row in self.get_client_issue_grid_rows():
            if search_string in row.text:
                cells = self.get_client_issue_grid_row_cell(row)
                client_issue_details['issue_type'] = cells[5].text
                client_issue_details['summary'] = cells[6].text
                client_issue_details['client_mac'] = cells[4].text
                client_issue_details['extreme_net_device'] = cells[8].text
                client_issue_details['detected_on'] = cells[10].text
                self.utils.print_info(f"{client_issue_details}")
                return client_issue_details
