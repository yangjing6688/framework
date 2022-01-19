from extauto.common.WebElementHandler import *
from extauto.xiq.defs.MLInsightsProxPresenceDefinitions import *


class MLInsightsProxPresenceWebElements(MLInsightsProxPresenceDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_n360_prox_presence_proximity(self):
        return self.weh.get_element(self.n360_prox_presence_proximity)

    def get_n360_prox_presence_presence(self):
        return self.weh.get_element(self.n360_prox_presence_presence)

    def get_n360_prox_presence_table_select(self):
        return self.weh.get_element(self.n360_prox_presence_table_select)

    def get_n360_prox_presence_refresh(self):
        return self.weh.get_element(self.n360_prox_presence_refresh)

    def get_n360_prox_presence_table_option(self):
        return self.weh.get_elements(self.n360_prox_presence_table_option)

    def get_n360_prox_presence_owned(self):
        return self.weh.get_element(self.n360_prox_presence_owned)

    def get_n360_prox_presence_owned_option(self):
        return self.weh.get_elements(self.n360_prox_presence_owned_option)

    def get_n360_prox_presence_uuid(self):
        return self.weh.get_element(self.n360_prox_presence_uuid)

    def get_n360_prox_presence_major(self):
        return self.weh.get_element(self.n360_prox_presence_major)

    def get_n360_prox_presence_minor(self):
        return self.weh.get_element(self.n360_prox_presence_minor)

    def get_n360_prox_presence_static(self):
        return self.weh.get_element(self.n360_prox_presence_static)

    def get_n360_prox_presence_rogue(self):
        return self.weh.get_element(self.n360_prox_presence_rogue)

    def get_n360_prox_presence_uuid_search_box(self):
        return self.weh.get_element(self.n360_prox_presence_uuid_search_box)

    def get_n360_prox_presence_static_option(self):
        return self.weh.get_elements(self.n360_prox_presence_static_option)

    def get_n360_prox_presence_rogue_option(self):
        return self.weh.get_elements(self.n360_prox_presence_rogue_option)

    def get_n360_prox_presence_engage(self):
        return self.weh.get_element(self.n360_prox_presence_engage)

    def get_n360_prox_presence_passers(self):
        return self.weh.get_element(self.n360_prox_presence_passers)

    def get_n360_prox_presence_conversion(self):
        return self.weh.get_element(self.n360_prox_presence_conversion)

    def get_n360_prox_presence_new_client(self):
        return self.weh.get_element(self.n360_prox_presence_new_client)

    def get_n360_prox_presence_ret_client(self):
        return self.weh.get_element(self.n360_prox_presence_ret_client)

    def get_n360_prox_presence_unassociated(self):
        return self.weh.get_element(self.n360_prox_presence_unassociated)

    def get_n360_prox_presence_associated(self):
        return self.weh.get_element(self.n360_prox_presence_associated)
