import os
import copy
from time import sleep
from extauto.common.AutoActions import AutoActions
from extauto.common.CommonValidation import CommonValidation
from extauto.common.Screen import Screen
from extauto.common.Utils import Utils

from extauto.xiq.flows.common.Navigator import Navigator
from extauto.xiq.elements.Network360PlanElements import Network360PlanElements


class Network360Plan:

    def __init__(self):
        self.utils = Utils()
        self.screen = Screen()

        self.navigator = Navigator()
        self.auto_actions = AutoActions()
        self.n360_elements = Network360PlanElements()
        self.commonValidation = CommonValidation()
        self.default_map = 'auto_location_01_1595321828282.tar.gz'

        """
            Need to build a string that represents the location of the map files
            In a VM the path would be:
            '/automation/framework/extreme_automation_framework/extauto/xiq/configs/maps'
            Since not everyone is using a VM the begining of the path can be different.
            To handle this condition, we will get the path of this file and split it into variables.
            Then remove 3 directories from the end, and rebuild the path to include configs/maps/
        """
        self.current_path = os.path.realpath(__file__).split(os.sep)
        self.current_path.pop()
        self.current_path.pop()
        self.current_path.pop()
        self.custom_file_dir = os.path.join(os.sep,*self.current_path, "configs", "maps") + os.sep


    def search_floor_in_network360plan(self, floor_name='default'):
        """
        - This keyword searches for the floor in Network360 Plan
        - Keyword Usage:
        - ``${SEARCH_MATCHES}=     Search Floor in Network360Plan              floor_name=floor_02``

        :param floor_name: floor of the location where devices has been assigned
        :return: returns list of search matches. -1 if no matches
        """

        self.navigator.navigate_to_network360plan()

        self.utils.print_info("Entering floor name in search box")
        self.auto_actions.send_keys(self.n360_elements.get_n360_plan_location_search_box(), floor_name)
        sleep(5)

        self.utils.print_info("Getting all matching floors")
        matches = self.n360_elements.get_n360_plan_search_matches()
        if matches:
            search_matches = []
            for match in matches:
                self.utils.print_info("Search Results: ", match.text)
                search_matches.append(match.text)

            return search_matches
        else:
            self.utils.print_info("No search matches found: ")
            return -1

    def get_aps_from_network360plan_floor(self, floor_name='default', device_type='default', retries=0, **kwargs):
        """
        - This keyword gets devices name from Network360 Plan page
        - Keyword Usage:
        - ``${AP_MATCHES}=          Get APs From Network360Plan Floor           floor_name=floor_02``

        :param floor_name: floor of the location where devices has been assigned
        :param device_type: optional - type of device - AP/switch/router/VGVA/router
        :return: devices name
        """

        self.navigator.navigate_to_network360plan()

        self.utils.print_info("Entering floor name in search box")
        self.auto_actions.send_keys(self.n360_elements.get_n360_plan_location_search_box(), floor_name)
        sleep(5)

        self.utils.print_info("Getting all matching floors")


        try:
            items = self.n360_elements.get_n360_plan_search_matches()
            matches = copy.copy(items)
            if matches:
                search_matches = []
                for match in matches:
                    self.utils.print_info("Search Results: ", match.text)
                    if floor_name == match.text:
                        self.utils.print_info("Clicking on the match: ", floor_name)
                        self.auto_actions.click(match)
                        sleep(10)
                        ap_list = self.n360_elements.get_n360_plan_aps_on_floor()
                        ap_count_label = self.n360_elements.get_n360_plan_ap_count_on_floor()

                        aps_on_floor = []

                        if not ap_list:
                            self.utils.print_info("AP Count: 0")
                            retries = 0
                            while retries < 5:
                                # let's wait and try it again
                                self.print_info(f"Let's try that again after 10 seconds retrires {retries}")
                                retries += 1
                                sleep(10)
                                ap_list = self.n360_elements.get_n360_plan_aps_on_floor()
                                ap_count_label = self.n360_elements.get_n360_plan_ap_count_on_floor()
                                if ap_list:
                                    break
                        if not ap_list:
                            self.utils.print_info("AP Count: 0")
                            kwargs['fail_msg'] = "AP Count: 0"
                            self.commonValidation.failed(**kwargs)
                            return 0

                        for ap in ap_list:
                            aps_on_floor.append(ap.text)
                        self.utils.print_info("APs on floor: ", aps_on_floor)

                        if ap_count_label:
                            ap_count = ap_count_label.text.split(" ")[0]
                            self.utils.print_info("AP Count: ", ap_count)

                            if len(ap_list) == int(ap_count):
                                self.utils.print_info("Number of APs on the floor is equal to the AP Count")
                            else:
                                self.utils.print_info("Number of APs on the floor is NOT equal to the AP Count")

                        else:
                            self.utils.print_info("Unable to find AP Count")

                        kwargs['pass_msg'] = f"AP was Found {aps_on_floor}"
                        self.commonValidation.passed(**kwargs)
                        return aps_on_floor
                    else:
                        self.utils.print_info("No search matches found: ")
            else:
                kwargs['fail_msg'] = f"No search matches found"
                self.commonValidation.failed(**kwargs)
                self.utils.print_info("No search matches found: ")
                return -1

        except Exception as e:
            if retries < 5:
                retries += 1
                self.utils.print_info("Click Close Button")
                self.auto_actions.click_reference(self.n360_elements.get_tooltip_close_button)
                self.utils.print_info(f"Exception Caught: {e}, tring again ({retries})")
                return self.get_aps_from_network360plan_floor(floor_name, device_type, retries, **kwargs)
            else:
                self.utils.print_info(f"Exception Caught: {e}, max retries reached {retries}")
                kwargs['fail_msg'] = f"Exception Caught: {e}, max retries reached {retries}"
                self.commonValidation.failed(**kwargs)
                return -1


    def import_map_in_network360plan(self, map_file_name):
        """
        - This keyword will Import Map file in Network360 Plan page
        - Keyword Usage:
        - Import Map In Network360Plan    ${MAP_FILE_NAME}

        :param map_file_name: Map File Name to import from /testsuites/xiq/functional/import_map_files directory
        :return: 1 if map uploaded successfully on Network360 Plan else -1
        """

        if not map_file_name:
            map_file_name = self.default_map

        self.navigator.navigate_to_network360plan()

        if self.n360_elements.get_import_map_button():
            self.utils.print_info("Click Import Map Button")
            self.auto_actions.click_reference(self.n360_elements.get_import_map_button)
            self.screen.save_screen_shot()
            sleep(2)
        else:
            self.utils.print_info("Click Import Map Button")
            self.auto_actions.click_reference(self.n360_elements.get_import_map_button_from_loaded_account)
            self.screen.save_screen_shot()
            sleep(2)

        self.utils.print_info(f"Importing Map File : {map_file_name}")
        map_file_location = self.custom_file_dir + map_file_name
        map_file_location = map_file_location.replace(":", ":\\")
        upload_button = self.n360_elements.get_import_map_upload_button()
        self.auto_actions.send_keys(upload_button, map_file_location)

        self.utils.print_info("Click Import Button")
        self.auto_actions.click_reference(self.n360_elements.get_import_button)
        sleep(10)

        if self.n360_elements.get_import_map_successful_text():
            tootip_text = self.n360_elements.get_import_map_successful_text().text
            if tootip_text:
                if "Your network map was successfully imported" in tootip_text:
                    self.utils.print_info(f"{tootip_text}")
                    return 1

        if self.n360_elements.get_import_map_already_exist_text():
            tootip_already_exist = self.n360_elements.get_import_map_already_exist_text().text
            if tootip_already_exist:
                if "already exists" in tootip_already_exist:
                    self.utils.print_info(f"{tootip_already_exist}")
                    self.utils.print_info("Map with Same Name Already Imported, So No need to Import Again")

                    self.utils.print_info("Click Close Button")
                    self.auto_actions.click_reference(self.n360_elements.get_tooltip_close_button)
                    sleep(2)
                    return 1
        return -1
