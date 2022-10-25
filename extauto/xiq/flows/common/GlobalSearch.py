from time import sleep

from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions

from extauto.xiq.flows.manage.Devices import Devices

from extauto.xiq.elements.DevicesWebElements import DevicesWebElements
from extauto.xiq.elements.GlobalSearchWebElements import GlobalSearchWebElements


class GlobalSearch:
    def __init__(self):
        self.utils = Utils()
        self.screen = Screen()
        self.auto_actions = AutoActions()

        self.devices = Devices()

        self.global_web_elements = GlobalSearchWebElements()
        self.devices_web_elements = DevicesWebElements()

    def global_search(self, search_value, category, expect_result="", **kwargs):
        """
        - This Keyword searches given search string info in global search
        - Flow : Click Global search Box--> Search String
        - Keyword Usage
         - ``Global Search   ${AP_MAC}   ${AP_CATEGORY}   ${AP_NAME}``

        :param search_value: Info to be searched ie AP Mac Address
        :param category: Category of the information
        :param expect_result: Expected Result
        :return: returns matched value when found or else returns -1
        """

        self.utils.print_info("Clicking on the search icon")
        self.auto_actions.click_reference(self.global_web_elements.get_search_icon)

        self.utils.print_info("Entering info to search : ", search_value)
        sleep(10)
        self.auto_actions.send_keys(self.global_web_elements.get_global_search_textbox(), search_value)
        sleep(10)

        self.utils.print_info("Clicking on search")
        self.auto_actions.click_reference(self.global_web_elements.get_global_search_textbox)
        sleep(10)

        self.utils.print_info("Search result :")
        search_matches = self.global_web_elements.get_global_search_result()
        sleep(10)

        self.screen.save_screen_shot()
        sleep(5)

        matched_val = ""

        if expect_result == "":
            self.utils.print_info("Expected value is empty")
            expect_result = search_value
        for search_match in search_matches:
            val = search_match.text
            self.utils.print_info("Value is ", val)
            sleep(3)

            if val == expect_result:
                self.utils.print_info("Match found")
                matched_val = search_match

        if expect_result == "None" and matched_val == "":
            kwargs['fail_msg'] = f"Variable 'expect_result' is None"
            self.commonValidation.failed(**kwargs)
            return -2

        if matched_val == "":
            self.screen.save_screen_shot()
            sleep(2)
            self.auto_actions.click_reference(self.global_web_elements.get_search_icon)
            kwargs['fail_msg'] = "Value was not found"
            self.commonValidation.failed(**kwargs)
            return -1
        return matched_val

    def get_client_details(self, search_result):
        """
        - Get client details ie Client Name ,Mac Address and Client IP address
        - Flow : Click Global search Box--> Search String
        - Keyword Usage
         - ``Get Client Details      ${SEARCH_RESULT_STRING}``

        :param search_result: Expected Client Information String displaying on Search Result
        :return: Client name, client MAC, client IP
        """
        sleep(5)
        self.utils.print_info("Clicking on  client Details")
        self.auto_actions.click(search_result)
        sleep(5)

        self.utils.print_info("Getting client Details")
        client_name = self.global_web_elements.get_client_title().text
        client_mac = self.global_web_elements.get_client_mac().text
        client_ip = self.global_web_elements.get_client_ip().text

        self.utils.print_info("client name, MAC and IP is ", client_name, client_mac, client_ip)
        self.screen.save_screen_shot()
        sleep(2)

        self.auto_actions.click_reference(self.global_web_elements.get_close_dialog)
        return client_name, client_mac, client_ip

    def get_ap_details(self, search_result):
        """
        - Get AP details ie AP Host Name ,Mac Address,IP address and Serial Number
        - Flow : Click Global search Box--> Search String
        - Keyword Usage
         - ``Get AP Details      ${SEARCH_RESULT_STRING}``

        :param search_result: Expected AP Information String displaying on Search Result
        :return: Host Name, AP serial number, AP MAC, AP IP
        """
        self.utils.print_info("Clicking on the AP Details")
        self.auto_actions.click(search_result)
        sleep(5)

        self.auto_actions.click_reference(self.global_web_elements.get_system_info)
        sleep(5)

        self.utils.print_info("Getting AP Details")
        host_name = self.global_web_elements.get_system_info_ap_name().text

        if len(host_name) > 3:
            host_name = host_name.rstrip("SIM")

        serial_number = self.global_web_elements.get_system_info_ap_serial_number().text
        ap_mac = self.global_web_elements.get_system_info_ap_mac().text
        ip = self.global_web_elements.get_system_info_ap_ip().text

        self.utils.print_info("AP details are ", host_name, " ", serial_number, " ", ap_mac, " ", ip)
        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Closing ap Details Page")
        self.auto_actions.click_reference(self.global_web_elements.get_close_dialog)
        return host_name, serial_number, ap_mac, ip

    def net_policy_details(self, search_result):
        """
        - Get Network Policy details ie Network Policy Name and SSID
        - Flow : Click Global search Box--> Search String
        - Keyword Usage
         - ``Net Policy Details      ${SEARCH_RESULT_STRING}``

        :param search_result: Expected Network Policy Information String displaying on Search Result
        :return: Network Policy name and SSID
        """
        self.utils.print_info("Clicking on the Network Policy Details")
        self.auto_actions.click(search_result)
        sleep(5)

        net_name = self.global_web_elements.get_net_policy_sum_view().text
        net_name = net_name[17:]
        net_name = net_name.strip()

        ssid = self.global_web_elements.get_net_policy_ssid_title().text
        self.screen.save_screen_shot()
        sleep(2)

        self.auto_actions.click_reference(self.global_web_elements.get_close_dialog)
        return net_name, ssid

    def view_all_organizations(self):
        """
        - This Keyword uses to view all the organizations Details in the Account
        - Flow : View Organization --> Select All Organization
        - Keyword Usage
         - ``View All Organizations``

        :return: 1 if Viewing All organization Details Successfully
        """
        self.auto_actions.click_reference(self.global_web_elements.get_view_organization_button)
        sleep(5)

        value = self.global_web_elements.get_select_all_organizations().text
        if value == "Select All":
            self.auto_actions.click_reference(self.global_web_elements.get_select_all_organizations)
            sleep(5)
            self.screen.save_screen_shot()
            sleep(2)
        self.auto_actions.click_reference(self.global_web_elements.get_view_org_close_button)

        return 1

    def application_details(self, search_result):
        """
        - This Keyword uses to get application details Based on Search Results string
        - Keyword Usage
         - ``Application Details  ${SEARCH_RESULT_STRING}``

        :param search_result: Expected Application Information String displaying on Search Result
        :return: Application Name And Category
        """
        sleep(5)
        self.utils.print_info("Clicking on the Application Details")
        self.auto_actions.click(search_result)
        sleep(5)

        app_name = self.global_web_elements.get_application_name().text
        app_cat = self.global_web_elements.get_application_category().text
        self.utils.print_info("Application name and category is: ", app_name, " ", app_cat)

        self.screen.save_screen_shot()
        sleep(2)

        self.auto_actions.click_reference(self.global_web_elements.get_close_dialog)
        return app_name, app_cat

    def sim_ap_name(self):
        """
        - This Keyword Uses to get AP name and if no AP is present then it onboards the AP and gets its name.
        - Keyword Usage
         - ``Sim AP Name``

        :return: Access Point Name
        """
      
        row_text = self.get_sim_ap()

        if row_text != "":
            res = row_text.split("\n")
            ap_name = res[0]
            self.utils.print_info("AP Name is : ", ap_name)
            return ap_name
        else:
            self.utils.print_info("No  Device present.")
            self.devices.onboard_simulated_device("AP460Cs")
            
            self.utils.print_info("Simulated Device Onboarded.")
            sleep(5)

            row_text = self.get_sim_ap()

            res = row_text.split("\n")
            ap_name = res[0]
            self.utils.print_info("AP Name is : ", ap_name)
            return ap_name

    def get_sim_ap(self):
        """
        - This Keyword Gets AP name in Row Text
        - Keyword Usage
         - ``Get Sim AP``
        :return: Access Point Name
        """
        sleep(5)
        self.utils.print_info("Getting AP row")
        rows = self.devices_web_elements.get_grid_rows()
        row_text = ""
        if rows:
            for row in rows:
                row_text = row.text
                break
        return row_text

    def get_ap_name(self):
        """
        - This Keyword Gets AP name and if no AP is present then it onboards the AP and gets its name.
        - Keyword Usage
         - ``Get Ap Name``

        :return: Access Point Name
        """
        row_text = self.get_ap_row()
        if row_text != "":
            res = row_text.split("\n")
            ap_name = res[0]
            self.utils.print_info("AP Name is : ", ap_name)
            return ap_name
        else:
            self.utils.print_info("No  Device present.")
            self.devices.onboard_simulated_device("AP460Cs")
            self.utils.print_info("Simulated Device Onboarded.")
            sleep(5)
            row_text = self.get_ap_row()
            res = row_text.split("\n")
            ap_name = res[0]
            self.utils.print_info("AP Name is : ", ap_name)
            return ap_name

    def get_ap_row(self):
        """
        - This Keyword Gets AP name in Row Text
        - Assumes that Already Navigated to Manage--> Devices Page
        - Keyword Usage
         - ``Get AP Row``

        :return: ap device presented row information
        """
        sleep(5)
        self.utils.print_info("Getting AP row")
        rows = self.devices_web_elements.get_grid_rows()
        row_text = ""
        if rows:
            for row in rows:
                row_text = row.text
                break
        return row_text
