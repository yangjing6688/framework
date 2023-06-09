from time import sleep
import random

from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from extauto.xiq.flows.manage.Devices import Devices
from extauto.xiq.elements.DevicesWebElements import DevicesWebElements
from extauto.xiq.elements.GlobalSearchWebElements import GlobalSearchWebElements
from extauto.common.CommonValidation import CommonValidation


class GlobalSearch:
    def __init__(self):
        self.utils = Utils()
        self.screen = Screen()
        self.auto_actions = AutoActions()
        self.devices = Devices()
        self.global_web_elements = GlobalSearchWebElements()
        self.devices_web_elements = DevicesWebElements()
        self.common_validation = CommonValidation()

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
        self.screen.save_screen_shot()

        self.utils.print_info("Entering info to search : ", search_value)
        self.auto_actions.send_keys(self.global_web_elements.get_global_search_textbox(), search_value)
        self.screen.save_screen_shot()


        self.utils.print_info("Clicking on search")
        self.auto_actions.click_reference(self.global_web_elements.get_search_icon)
        self.screen.save_screen_shot()

        search_matches = self.global_web_elements.get_global_search_result()
        self.screen.save_screen_shot()

        matched_val = ""

        if expect_result == "":
            expect_result = search_value

        if search_matches is not None:
            for search_match in search_matches:
                val = search_match.text
                self.utils.print_info("Global Search Value Found  in UI is : ", val)
                self.screen.save_screen_shot()

                if val == expect_result:
                    self.utils.print_info("Match found")
                    matched_val = search_match
                    self.screen.save_screen_shot()

        if expect_result == "None" and matched_val == "":
            kwargs['fail_msg'] = "Variable 'expect_result' is None"
            self.common_validation.fault(**kwargs)
            self.screen.save_screen_shot()
            return -2

        if matched_val == "":
            self.screen.save_screen_shot()
            self.auto_actions.click_reference(self.global_web_elements.get_search_icon)
            kwargs['fail_msg'] = "Value was not found"
            self.common_validation.failed(**kwargs)
            self.screen.save_screen_shot()
            return -1

        #self.auto_actions.click_reference(self.global_web_elements.get_search_clear_icon)
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
        self.utils.print_info("Clicking on  client Details")
        client_name = self.global_web_elements.get_global_search_client_name()
        if client_name is not None and client_name.is_displayed():
            self.auto_actions.click(client_name)
        else:
            self.auto_actions.click(search_result)

        self.utils.print_info("Getting client Details")
        self.utils.wait_till(self.global_web_elements.get_client_title, is_logging_enabled=True, timeout=30, delay=10)
        client_name = self.global_web_elements.get_client_title().text
        client_mac = self.global_web_elements.get_client_mac().text
        client_ip = self.global_web_elements.get_client_ip().text

        self.utils.print_info("client name, MAC and IP is ", client_name, client_mac, client_ip)
        self.screen.save_screen_shot()

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

        self.auto_actions.click_reference(self.global_web_elements.get_system_info)

        self.utils.print_info("Getting AP Details")
        host_name = self.global_web_elements.get_system_info_ap_name().text

        if len(host_name) > 3:
            host_name = host_name.rstrip("SIM")

        serial_number = self.global_web_elements.get_system_info_ap_serial_number().text
        ap_mac = self.global_web_elements.get_system_info_ap_mac().text
        ip = self.global_web_elements.get_system_info_ap_ip().text

        self.utils.print_info("AP details are ", host_name, " ", serial_number, " ", ap_mac, " ", ip)
        self.screen.save_screen_shot()

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
        sleep(2)

        net_name = ""
        ssid = ""
        if self.global_web_elements.get_net_policy_sum_view():
            net_name = self.global_web_elements.get_net_policy_sum_view().text
            net_name = net_name[17:]
            net_name = net_name.strip()

        if self.global_web_elements.get_net_policy_ssid_title():
            ssid = self.global_web_elements.get_net_policy_ssid_title().text
            self.screen.save_screen_shot()

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

    def split_string_into_3_parts(self, info):
        """
            - This keyword splits a string in to 3 equal parts
            :param info: input string
            :return: returns 3 strings by dividing the input string
        """

        self.utils.print_info("Input String: ", info)
        length = len(info)
        seg1 = round(length / 3)
        part1 = info[:seg1]
        seg2 = seg1 * 2
        part2 = info[seg1:seg2]
        part3 = info[seg2:]
        return part1, part2, part3

    def get_first_half_of_mac(self, mac):
        """
        - This keyword returns the first half of a MAC
        :param mac: MAC
        :return: returns first half of MAC
        """
        self.utils.print_info("Input MAC: ", mac)
        length = len(mac)
        seg = round(length / 2)
        mac_first_half = mac[:seg]
        return mac_first_half

    def get_second_half_of_name(self, name):
        """
         - This keyword returns Second half of any Name
         :param name: Name
         :return: returns Second half of any Name
         """
        length = len(name)
        seg = round(length / 2)
        net_second_half = name[seg:]
        return net_second_half

    def get_last_6_digts_of_mac(self, mac):
        """
         - This keyword returns Last 6 Octets half of Mac address
         :param mac: Mac Address
         :return: returns Last 6 Octets half of Mac address
         """
        length = len(mac)
        st = length - 6
        remaining_mac = mac[st:]
        return remaining_mac

    def get_second_half_of_mac(self, mac):
        """
         - This keyword returns Second half of Mac address
         :param mac: Mac Address
         :return: returns Second half of Mac address
         """
        length = len(mac)
        seg = round(length / 2)
        mac_second_half = mac[seg:]
        return mac_second_half

    def convert_mac_to_upper(self, mac):
        """
        - This keyword returns the Mac address to Upper Case
        :param mac: Mac Address
        :return: returns Mac address to Upper Case
        """
        upper_case = mac.upper()
        return upper_case

    def convert_mac_to_lower(self, mac):
        """
        - This keyword returns the Mac address to Lower Case
        :param mac: Mac Address
        :return: returns Mac address to Lower Case
        """
        lower_case = mac.lower()
        return lower_case

    def convert_mac_to_random_case(self, mac):
        """
        - This keyword returns the Random Case of Mac address
        :param mac: Mac Address
        :return: returns Random Case of Mac address
        """
        random_case = ""
        for i in mac:
            if i.isalpha():
                rand1 = random.randint(1, 2)
                if rand1 == 1:
                    random_case = random_case + i.lower()
                else:
                    random_case = random_case + i.upper()
            else:
                random_case = random_case + i
        return random_case

    def get_partial_ip(self, ip):
        """
        - This keyword returns the Partial Portion of IP address
        :param ip: IP Address
        :return: returns Partial Portion of IP address
        """
        length = len(ip)
        length -= 2
        ip = ip[:length]
        return ip

    def get_first_half_of_name(self, name):
        """
        - This keyword returns the first half of a Name
        :param name: name
        :return: returns first half of Name
        """
        length = len(name)
        seg = round(length / 2)
        first_half = name[:seg]
        return first_half
