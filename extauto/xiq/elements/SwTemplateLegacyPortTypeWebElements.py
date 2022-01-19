from extauto.xiq.defs.SwTemplateLegacyPortTypeWebElementsDefinitions import *
from extauto.common.WebElementHandler import *

class SwTemplateLegacyPortTypeWebElements(SwTemplateLegacyPortTypeWebElementDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_name(self):
        return self.weh.get_element(self.name)

    def get_port_type_desc(self):
        return self.weh.get_elements(self.port_type_desc)

    def get_status(self):
        return self.weh.get_elements(self.status)

    def get_save_button(self):
        return self.weh.get_elements(self.save_button)

    def get_save_button(self):
        return self.weh.get_elements(self.save_button)

    def get_port_type_access(self):
        return self.weh.get_elements(self.port_type_access)

    def get_port_type_trunk(self):
        return self.weh.get_elements(self.port_type_trunk)

    def get_port_type_phone(self):
        return self.weh.get_elements(self.port_type_phone)

    def get_port_type_auto_sense(self):
        return self.weh.get_elements(self.port_type_auto_sense)

    def get_transmission_type(self):
        return self.weh.get_elements(self.transmission_type)

    def get_transmission_speed(self):
        return self.weh.get_elements(self.transmission_speed)

    def get_access_vlan_select(self):
        return self.weh.get_elements(self.access_vlan_select)

    def get_access_vlan_add(self):
        return self.weh.get_elements(self.access_vlan_add)

    def get_access_vlan_name(self):
        return self.weh.get_elements(self.access_vlan_name)

    def get_access_vlan_id(self):
        return self.weh.get_elements(self.access_vlan_id)

    def get_lldp_transmit(self):
        return self.weh.get_elements(self.lldp_transmit)

    def get_lldp_receive(self):
        return self.weh.get_elements(self.lldp_receive)

    def get_cdp_receive(self):
        return self.weh.get_elements(self.cdp_receive)

    def get_client_reporting(self):
        return self.weh.get_elements(self.client_reporting)

    def get_stp_status(self):
        return self.weh.get_elements(self.stp_status)

    def get_edge_port(self):
        return self.weh.get_elements(self.edge_port)

    def get_bpdu_protection(self):
        return self.weh.get_elements(self.bpdu_protection)

    def get_stp_priority(self):
        return self.weh.get_elements(self.stp_priority)

    def get_sc_broadcast(self):
        return self.weh.get_elements(self.sc_broadcast)

    def get_sc_unicast(self):
        return self.weh.get_elements(self.sc_unicast)

    def get_sc_multicast(self):
        return self.weh.get_elements(self.sc_multicast)

    def get_sc_threshold_option(self):
        return self.weh.get_elements(self.sc_threshold_option)

    def get_sc_rate_limit_type(self):
        return self.weh.get_elements(self.sc_rate_limit_type)

    def get_sc_rate_limit_value(self):
        return self.weh.get_elements(self.sc_rate_limit_value)

