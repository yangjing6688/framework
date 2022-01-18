from common.WebElementHandler import *
from xiq.defs.Network360PlanDefinitions import *


class Network360PlanElements(Network360PlanDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_n360_plan_location_search_box(self):
        return self.weh.get_element(self.n360_plan_location_search_box)

    def get_n360_plan_floors(self):
        return self.weh.get_elements(self.n360_plan_floors)

    def get_n360_plan_search_matches(self):
        return self.weh.get_elements(self.n360_plan_search_matches)

    def get_n360_plan_aps_on_floor(self):
        return self.weh.get_elements(self.n360_plan_aps_on_floor)

    def get_n360_plan_ap_count_on_floor(self):
        return self.weh.get_element(self.n360_plan_ap_count_on_floor)

    def get_import_map_upload_button(self):
        """
        :return:
        """
        return self.weh.get_element(self.import_map_upload_button)

    def get_import_map_button(self):
        """
        :return:
        """
        return self.weh.get_element(self.import_map_button)

    def get_import_map_successful_text(self):
        """
        :return:
        """
        return self.weh.get_element(self.import_map_successful_text)

    def get_import_button(self):
        """
        :return:
        """
        return self.weh.get_element(self.import_button)

    def get_add_building_button(self):
        """
        :return:
        """
        return self.weh.get_element(self.add_building_button)

    def get_tooltip_close_button(self):
        """
        :return:
        """
        return self.weh.get_element(self.tooltip_close_button)

    def get_import_map_button_from_loaded_account(self):
        """
        :return:
        """
        return self.weh.get_element(self.import_map_button_from_loaded_account)

    def get_import_map_already_exist_text(self):
        """
        :return:
        """
        return self.weh.get_element(self.import_map_already_exist_text)