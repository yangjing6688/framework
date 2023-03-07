from extauto.xiq.flows.manage.Client import *
from extauto.xiq.flows.manage.Devices import *
from extauto.xiq.flows.common.Navigator import *
from extauto.xiq.elements.Network360MonitorElements import *
from extauto.common.CommonValidation import CommonValidation


class Network360Monitor:

    def __init__(self):
        self.utils = Utils()
        self.screen = Screen()

        self.navigator = Navigator()
        self.auto_actions = AutoActions()
        self.n360_elements = Network360MonitorElements()
        self.common_validation = CommonValidation()

    def search_floor_in_network360monitor(self, floor_name='default', **kwargs):
        """
        - This keyword searches for the floor in Network360 Monitor
        - Keyword Usage:
        - ``${SEARCH_MATCHES}=     Search Floor in Network360Monitor              floor_name=floor_02``

        :param floor_name: floor of the location where devices has been assigned
        :return: returns list of search matches. -1 if no matches
        """

        self.navigator.navigate_to_network360monitor()

        self.utils.print_info("Entering floor name in search box")
        self.auto_actions.send_keys(self.n360_elements.get_n360_monitor_location_search_box(), floor_name)
        sleep(5)

        self.utils.print_info("Getting all matching floors")
        matches = self.n360_elements.get_n360_monitor_search_matches()
        if matches:
            search_matches = []
            for match in matches:
                self.utils.print_info("Search Results: ", match.text)
                search_matches.append(match.text)
            return search_matches
        else:
            kwargs['fail_msg'] = "'search_floor_in_network360monitor()' -> No search matches found"
            self.common_validation.fault(**kwargs)
            return -1

    def get_devices_from_network360monitor_floor(self, floor_name='default', device_type='default', **kwargs):
        """
        - This keyword gets  devices name from Network360 Monitor page
        - Keyword Usage:
        - ``${AP_MATCHES}=          Get APs From Network360Monitor Floor           floor_name=floor_02``

        :param floor_name: floor of the location where devices has been assigned
        :param device_type: optional - type of device - AP/switch/router/VGVA/router
        :return: devices names on the floor
        """
        self.navigator.navigate_to_network360monitor()

        self.utils.print_info("Entering floor name in search box")
        self.auto_actions.send_keys(self.n360_elements.get_n360_monitor_location_search_box(), floor_name)
        sleep(5)

        self.utils.print_info("Getting all matching floors")
        matches = self.n360_elements.get_n360_monitor_search_matches()
        if matches:
            for match in matches:
                search_matches = []
                self.utils.print_info("Search Results: ", match.text)
                if floor_name == match.text:
                    self.utils.print_info("Clicking on the match: ", floor_name)
                    self.auto_actions.click(match)
                    sleep(10)
                    self.utils.print_info("Clicking on the MAP tab")
                    self.auto_actions.click_reference(self.n360_elements.get_n360_monitor_map)
                    sleep(10)

                    ap_list = self.n360_elements.get_n360_monitor_aps_on_floor()
                    ap_count_label = self.n360_elements.get_n360_monitor_ap_count_on_floor()

                    if ap_list:
                        aps_on_floor = []
                        for ap in ap_list:
                            aps_on_floor.append(ap.text)
                        self.utils.print_info("APs on floor: ", aps_on_floor)
                    else:
                        kwargs['fail_msg'] = f"'get_devices_from_network360monitor_floor()' -> No APs found on floor: " \
                                             f"{floor_name}"
                        self.common_validation.failed(**kwargs)
                        return -1

                    if ap_count_label:
                        ap_count = ap_count_label.text.split(" ")[0]
                        self.utils.print_info("AP Count: ", ap_count)

                        if len(ap_list) == int(ap_count):
                            self.utils.print_info("Number of APs on the floor is equal to the AP Count")
                        else:
                            self.utils.print_info("Number of APs on the floor is NOT equal to the AP Count")

                    else:
                        self.utils.print_info("Unable to find AP Count")

                    return aps_on_floor
                else:
                    self.utils.print_info("No search matches found: ")
        else:
            kwargs['fail_msg'] = "'get_devices_from_network360monitor_floor()' -> No search matches found"
            self.common_validation.fault(**kwargs)
            return -1


    def get_clients_from_network360monitor_floor(self, floor_name='default', device_type='default', **kwargs):
        """
        - This keyword gets clients MACs from Network360 Monitor page in a floor
        - Keyword Usage:
        - ``${CLIENT_MATCHES}=          Get APs From Network360Monitor Floor           floor_name=floor_02``

        :param floor_name: floor of the location where devices has been assigned
        :param device_type: optional - type of device - AP/switch/router/VGVA/router
        :return: clients MAC on the floor
        """

        self.navigator.navigate_to_network360monitor()

        self.utils.print_info("Entering floor name in search box")
        self.auto_actions.send_keys(self.n360_elements.get_n360_monitor_location_search_box(), floor_name)
        sleep(5)

        self.utils.print_info("Getting all matching floors")
        matches = self.n360_elements.get_n360_monitor_search_matches()
        if matches:
            search_matches = []
            for match in matches:
                self.utils.print_info("Search Results: ", match.text)
                if floor_name == match.text:
                    self.utils.print_info("Clicking on the match: ", floor_name)
                    self.auto_actions.click(match)
                    sleep(10)
                    ap_list = self.n360_elements.get_n360_monitor_aps_on_floor()
                    ap_count_label = self.n360_elements.get_n360_monitor_ap_count_on_floor()

                    if ap_list:
                        aps_on_floor = []
                        for ap in ap_list:
                            aps_on_floor.append(ap.text)
                        self.utils.print_info("APs on floor: ", aps_on_floor)
                    else:
                        kwargs['fail_msg'] = f"'get_clients_from_network360monitor_floor()' -> No APs found on floor: " \
                                             f"{floor_name}"
                        self.common_validation.failed(**kwargs)
                        return -1

                    if ap_count_label:
                        ap_count = ap_count_label.text.split(" ")[0]
                        self.utils.print_info("AP Count: ", ap_count)

                        if len(ap_list) == int(ap_count):
                            self.utils.print_info("Number of APs on the floor is equal to the AP Count")
                        else:
                            self.utils.print_info("Number of APs on the floor is NOT equal to the AP Count")

                    else:
                        self.utils.print_info("Unable to find AP Count")

                    self.utils.print_info("Clicking on Connected Clients tab ")
                    self.auto_actions.click_reference(self.n360_elements.get_n360_monitor_connected_clients_tab)
                    client_mac_list = self.n360_elements.get_n360_connected_client_macs()
                    if client_mac_list:
                        clients_on_floor = []
                        for client_mac in client_mac_list:
                            clients_on_floor.append(client_mac.text)
                        self.utils.print_info("Connected Clients on floor: ", clients_on_floor[1:])
                    else:
                        kwargs['fail_msg'] = f"'get_clients_from_network360monitor_floor()' -> No APs found on floor: " \
                                             f"{floor_name}"
                        self.common_validation.failed(**kwargs)
                        return -1

                    return clients_on_floor[1:]
                else:
                    self.utils.print_info("No search matches found: ")
        else:
            kwargs['fail_msg'] = "'get_clients_from_network360monitor_floor()' -> No search matches found"
            self.common_validation.fault(**kwargs)
            return -1

    def _ml_insights_monitor_ap_count_and_ap_name(self, location_floor='default', **kwargs):
        """
        - This keyword gets AP count and AP name from Network360 Monitor page
        :param location_floor: floor of the location where devices has been assigned
        :return: AP name, AP count
        """
        sleep(5)
        try:
            self.auto_actions.send_keys(self.ml_insights_monitor.get_n360_monitor_search_box, location_floor)
            sleep(2)
            location = self.ml_insights_monitor.get_n360_monitor_search_grid()

            for loc in location:
                if location_floor in loc.text:
                    self.utils.print_info("Location Found")
                    self.auto_actions.click(loc)
                    sleep(5)
                    break
            ap_count = self.ml_insights_monitor.get_n360_monitor_ap_count().text
            ap_name = self.ml_insights_monitor.get_n360_monitor_ap_name().text
            return ap_name, ap_count
        except Exception as e:
            self.utils.print_info(e)
            kwargs['fail_msg'] = "'_ml_insights_monitor_ap_count_and_ap_name()' -> Unable to get AP Count and AP Name"
            self.common_validation.fault(**kwargs)
            return -1

    def _goto_ml_insights_monitor(self, **kwargs):
        """
        - This keyword navigates to Network360 Monitor page
        :return: returns 1 if successful
        """
        try:
            self.utils.print_info("Clicking on ML Insights button")
            self.auto_actions.click_reference(self.ml_insights.get_ml_insights_button)
            sleep(2)
            self.utils.print_info("Clicking on ML Insights Monitor button")
            self.auto_actions.click_reference(self.ml_insights.get_n360_monitor_button)
            kwargs['pass_msg'] = "'_goto_ml_insights_monitor()' -> Successfully clicking on ML Insights Monitor Button"
            self.common_validation.passed(**kwargs)
            sleep(2)
            return 1
        except Exception as e:
            self.utils.print_info(e)
            kwargs['fail_msg'] = "'_ml_insights_monitor_ap_count_and_ap_name()' -> Unable to Navigate to MLInsights " \
                                 "Monitor Page"
            self.common_validation.fault(**kwargs)
            return 0

    def _get_ml_insights_monitor_tracker_details(self, **kwargs):
        """
        - This keyword gets details of Device, Client, Wifi, Network, Application, Service, Security in N360 Monitor page
        :return: dictionary of N360 Monitor details
        """
        try:
            sleep(5)
            tracker_dict = dict()
            tracker_dict["device_num"] = self.ml_insights_monitor.get_n360_monitor_device_number().text
            tracker_dict["device_status"] = self.ml_insights_monitor.get_n360_monitor_device_status().text
            tracker_dict["client_num"] = self.ml_insights_monitor.get_n360_monitor_client_number().text
            tracker_dict["client_status"] = self.ml_insights_monitor.get_n360_monitor_client_status().text
            tracker_dict["wifi_num"] = self.ml_insights_monitor.get_n360_monitor_wifi_number().text
            tracker_dict["wifi_status"] = self.ml_insights_monitor.get_n360_monitor_wifi_status().text
            tracker_dict["network_number"] = self.ml_insights_monitor.get_n360_monitor_network_number().text
            tracker_dict["network_status"] = self.ml_insights_monitor.get_n360_monitor_network_status().text
            tracker_dict["service_number"] = self.ml_insights_monitor.get_n360_monitor_service_number().text
            tracker_dict["service_status"] = self.ml_insights_monitor.get_n360_monitor_service_status().text
            tracker_dict["application_number"] = self.ml_insights_monitor.get_n360_monitor_app_number().text
            tracker_dict["application_usage"] = self.ml_insights_monitor.get_n360_monitor_app_usage().text
            tracker_dict["security_number"] = self.ml_insights_monitor.get_n360_monitor_security_number().text
            tracker_dict["security_rogues"] = self.ml_insights_monitor.get_n360_monitor_security_total_rogues().text

            self.utils.print_info("Tracker details dictionary ", tracker_dict)
            return tracker_dict
        except Exception as e:
            self.utils.print_info(e)
            kwargs['fail_msg'] = "'_get_ml_insights_monitor_tracker_details()' -> Unable to get MLInsights Monitor " \
                                 "Tracker Details"
            self.common_validation.fault(**kwargs)
            return -1

    def get_network360monitor_devices_score(self, floor_name='default', **kwargs):
        """
        - This keyword returns the DEVICES card's health score

        - Keyword Usage:
        - ``Get Network360Monitor Devices Score             floor_name=floor_03``
        - ``Get Network360Monitor Devices Score``

        :param floor_name: floor_name. if no floor_name passed, returns the values for Global View
        :return: returns the devices score Ex: 94/100 EXCELLENT
        """

        self.navigator.navigate_to_network360monitor()
        sleep(5)

        if floor_name != 'default':
            if self._search_and_click_floor(floor_name) == -1:
                kwargs['fail_msg'] = "'get_network360monitor_devices_score()' -> Unsuccessfully clicked on floor"
                self.common_validation.failed(**kwargs)
                return -1

        device_score = self.n360_elements.get_devices_score()

        if device_score is None:
            kwargs['fail_msg'] = "'get_network360monitor_devices_score()' -> No Device Score label found"
            self.common_validation.failed(**kwargs)
            return -1
        else:
            self.utils.print_info("Device Score: ", device_score.text)
            return device_score.text

    def get_network360monitor_device_health_overall_score(self, floor_name='default', **kwargs):
        """
        - This keyword returns the DEVICES card -> Overall Score
        - Device Availability Score
        - Device Hardware Health
        - Config & Firmware Score

        - Keyword Usage:
        - ``Get Network360Monitor Device Health Overall Score          floor_name=floor_01``
        - ``Get Network360Monitor Device Health Overall Score``

        :param floor_name: floor_name. if no floor_name passed, returns the values for Global View
        :return: returns availability_score, hw_health, fw_health
        """
        self.navigator.navigate_to_network360monitor()

        if floor_name != 'default':
            if self._search_and_click_floor(floor_name) == -1:
                kwargs['fail_msg'] = "'get_network360monitor_device_health_overall_score()' -> Unsuccessfully " \
                                     "clicked on floor"
                self.common_validation.failed(**kwargs)
                return -1

        self.utils.print_info("Clicking the devices card...")
        self.auto_actions.click_reference(self.n360_elements.get_n360_monitor_devices_card)
        sleep(5)

        availability_score = self.n360_elements.get_device_health_overal_score_availability_score()
        hw_health = self.n360_elements.get_device_health_overal_score_hw_health()
        fw_health = self.n360_elements.get_device_health_overal_score_fw_score()

        _availability_score = -1
        _hw_health = -1
        _fw_health = -1

        if availability_score is None:
            self.utils.print_info("Unable to find the Availability Score")
        else:
            _availability_score = availability_score.text
            self.utils.print_info("Availability Score", _availability_score)

        if hw_health is None:
            self.utils.print_info("Unable to find the Hardware Health")
        else:
            _hw_health = hw_health.text
            self.utils.print_info("Hardware Health", _hw_health)

        if fw_health is None:
            self.utils.print_info("Unable to find the Firmware Score")
        else:
            _fw_health = fw_health.text
            self.utils.print_info("Firmware Score", _fw_health)

        return _availability_score, _hw_health, _fw_health

    def _search_and_click_floor(self, floor_name, **kwargs):
        self.utils.print_info("Entering floor name in search box")
        self.auto_actions.send_keys(self.n360_elements.get_n360_monitor_location_search_box(), floor_name)
        sleep(5)

        self.utils.print_info("Getting all matching floors")
        matches = self.n360_elements.get_n360_monitor_search_matches()
        if matches:
            for match in matches:
                self.utils.print_info("Search Results: ", match.text)
                if floor_name == match.text:
                    self.utils.print_info("Clicking on the match: ", floor_name)
                    self.auto_actions.click(match)
                    sleep(5)
                    return 1

        kwargs['fail_msg'] = "'_search_and_click_floor()' -> Unable to find the floor"
        self.common_validation.fault(**kwargs)
        return -1

    def get_network360monitor_clients_health_client_count(self, floor_name='default', **kwargs):
        """
        - This keyword returns the CLIENTS card -> Client Count

        - Keyword Usage:
        - ``Get Network360Monitor Clients Health Client Count          floor_name=floor_01``
        - ``Get Network360Monitor Clients Health Client Count``

        :param floor_name: floor_name. if no floor_name passed, returns the values for Global View
        :return: returns client_count_2G, client_count_5G, client_count_6G
        """
        self.navigator.navigate_to_network360monitor()

        if floor_name != 'default':
            if self._search_and_click_floor(floor_name) == -1:
                kwargs['fail_msg'] = "'get_network360monitor_clients_health_client_count()' -> Unsuccessfully clicked " \
                                     "on floor"
                self.common_validation.failed(**kwargs)
                return -1

        self.utils.print_info("Clicking the clients card...")
        self.auto_actions.click_reference(self.n360_elements.get_n360_monitor_clients_card)
        sleep(5)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Checking CLIENT widget...")
        client_count_2G = self.n360_elements.get_client_health_clients_widget_count_2G()
        client_count_5G = self.n360_elements.get_client_health_clients_widget_count_5G()
        client_count_6G = self.n360_elements.get_client_health_clients_widget_count_6G()

        _client_count_2G = -1
        _client_count_5G = -1
        _client_count_6G = -1

        if client_count_2G is None:
            self.utils.print_info("Unable to find the 2G client count")
        else:
            _client_count_2G = client_count_2G.text
            self.utils.print_info("_client_count_2G", _client_count_2G)

        if client_count_5G is None:
            self.utils.print_info("Unable to find 5G client count")
        else:
            _client_count_5G = client_count_5G.text
            self.utils.print_info("5G client count", _client_count_5G)

        if client_count_6G is None:
            self.utils.print_info("Unable to find 6G client count")
        else:
            _client_count_6G = client_count_6G.text
            self.utils.print_info("6G client count", _client_count_6G)

        return _client_count_2G, _client_count_5G, _client_count_6G

    def svg_chart_element_hover(self, index, graph_type, elem1, elem2, x_position, y_position):
        """
        This function is used to select different portions from SVG charts like lines or half pie charts colors.
        :param index: SVG graphs have each color assigned an integer from 0..max number of colors available.
        :param graph_type: Type of graph: line or chart.
        :param elem1: graph type element reference to search for.
        :param elem2: graph type element after hover is done.
        :param x_position: integer
        :param y_position: integer
        :return:
        """
        sleep(2)
        el = elem1(index)
        self.utils.print_info(f"Moving cursor to element {el}")
        self.auto_actions.move_to_element(el)
        x = 0
        while x < 50:
            try:
                el_hover = elem2(index)
                if el_hover:
                    self.utils.print_info(f'Mouse is hovering on element {el_hover}')
                    if graph_type == 'line':
                        self.utils.print_info(f"Moving cursor to element {el_hover}")
                        self.auto_actions.move_to_element(el_hover)
                    break
                else:
                    self.utils.print_info(f'Moving cursor with {x_position}, {y_position} offset.')
                    self.auto_actions.move_mouse_with_offset(x_position, y_position)
                    sleep(2)
                    x += 1
                    self.utils.print_info(f'Retry {x}')
            except (Exception,):
                self.utils.print_info(f'Moving cursor with {x_position}, {y_position} offset.')
                self.auto_actions.move_mouse_with_offset(x_position, y_position)
                sleep(2)
                x += 1
                self.utils.print_info(f'Retry {x}')
