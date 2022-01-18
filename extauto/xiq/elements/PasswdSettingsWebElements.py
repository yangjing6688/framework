from xiq.defs.PasswdSettingsWebElementsDefinitions import *
from common.WebElementHandler import WebElementHandler


class PasswdSettingsWebElements(PasswdSettingsWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_letters_check_box(self):
        return self.weh.get_element(self.letters_check_box)

    def get_numbers_check_box(self):
        return self.weh.get_element(self.numbers_check_box)

    def get_special_character_check_box(self):
        return self.weh.get_element(self.special_character_check_box)

    def get_enforce_use_of_drop_down(self):
        return self.weh.get_element(self.enforce_use_of_drop_down)

    def get_enforce_use_of_options(self):
        parent = self.get_enforce_use_of_drop_down()
        return self.weh.get_elements(self.active_select_items, parent)

    def get_psk_generation_method_drop_down(self):
        return self.weh.get_element(self.psk_generation_method_drop_down)

    def get_psk_generation_method_options(self):
        parent = self.get_psk_generation_method_drop_down()
        return self.weh.get_elements(self.active_select_items, parent)

    def get_generate_password_length_drop_down(self):
        return self.weh.get_element(self.generate_password_length_drop_down)

    def get_generate_password_length_options(self):
        parent = self.get_generate_password_length_drop_down()
        return self.weh.get_elements(self.active_select_items, parent)

    def get_concatenating_string(self):
        return self.weh.get_element(self.concatenating_string)
