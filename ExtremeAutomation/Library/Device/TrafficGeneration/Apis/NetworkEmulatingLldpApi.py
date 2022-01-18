from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.TrafficGenerationApi import TrafficGenerationApi
from ExtremeAutomation.Library.Utils.Singleton import Singleton
import abc
import time


class NetworkEmulatingLldpApi(TrafficGenerationApi):
    def __init__(self, device):
        super(NetworkEmulatingLldpApi, self).__init__(device)
        self.send_sleep_time = 2

    def create_and_go_lldp_interface(self, port_string, router_id, mac_address, chassis_mac, ttl):
        self.create_lldp_interface(port_string, router_id, mac_address, chassis_mac, ttl)
        self.enable_lldp(port_string, router_id)

    @abc.abstractmethod
    def create_lldp_interface(self, port_string, router_id, mac_address, chassis_mac, ttl):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def remove_lldp_interface(self, port_string, router_id):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def enable_lldp(self, port_string, router_id, enabled=True):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def start_transmit_tlv(self, port_string, router_id, tlv_name):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def stop_transmit_tlv(self, port_string, router_id, tlv_name):
        return self.logger.log_unimplemented_method()

    ########################################
    # ####### sys-name ############
    ########################################
    @abc.abstractmethod
    def add_lldp_tlv_sys_name(self, port_string, router_id, value):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def remove_lldp_tlv_sys_name(self, port_string, router_id, value):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def start_tlv_sys_name(self, port_string, router_id):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def stop_tlv_sys_name(self, port_string, router_id):
        return self.logger.log_unimplemented_method()

    def send_lldp_tlv_sys_name(self, port_string, router_id):
        self.start_tlv_sys_name(port_string, router_id)
        time.sleep(self.send_sleep_time)
        self.stop_tlv_sys_name(port_string, router_id)

    ########################################
    # ####### sys-desc ############
    ########################################
    @abc.abstractmethod
    def add_lldp_tlv_sys_desc(self, port_string, router_id, value):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def remove_lldp_tlv_sys_desc(self, port_string, router_id, value):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def start_tlv_sys_desc(self, port_string, router_id):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def stop_tlv_sys_desc(self, port_string, router_id):
        return self.logger.log_unimplemented_method()

    def send_lldp_tlv_sys_desc(self, port_string, router_id):
        self.start_tlv_sys_desc(port_string, router_id)
        time.sleep(self.send_sleep_time)
        self.stop_tlv_sys_desc(port_string, router_id)

    ########################################
    # ####### sys-cap ############
    ########################################
    @abc.abstractmethod
    def add_lldp_tlv_sys_cap(self, port_string, router_id, cap_support, cap_enabled):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def remove_lldp_tlv_sys_cap(self, port_string, router_id, value):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def start_tlv_sys_cap(self, port_string, router_id):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def stop_tlv_sys_cap(self, port_string, router_id):
        return self.logger.log_unimplemented_method()

    def send_lldp_tlv_sys_cap(self, port_string, router_id):
        self.start_tlv_sys_cap(port_string, router_id)
        time.sleep(self.send_sleep_time)
        self.stop_tlv_sys_cap(port_string, router_id)

    ########################################
    # ####### port-desc ############
    ########################################
    @abc.abstractmethod
    def add_lldp_tlv_port_desc(self, port_string, router_id, value):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def remove_lldp_tlv_port_desc(self, port_string, router_id, value):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def start_tlv_port_desc(self, port_string, router_id):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def stop_tlv_port_desc(self, port_string, router_id):
        return self.logger.log_unimplemented_method()

    def send_lldp_tlv_port_desc(self, port_string, router_id):
        self.start_tlv_port_desc(port_string, router_id)
        time.sleep(self.send_sleep_time)
        self.stop_tlv_port_desc(port_string, router_id)

    ########################################
    # ####### local-mgmt-addr ############
    ########################################
    @abc.abstractmethod
    def add_lldp_tlv_local_mgmt_addr(self, port_string, router_id, local_management_address, local_management_port,
                                     local_management_oid):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def remove_lldp_tlv_local_mgmt_addr(self, port_string, router_id, local_management_address, local_management_port):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def start_tlv_local_mgmt_addr(self, port_string, router_id):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def stop_tlv_local_mgmt_addr(self, port_string, router_id):
        return self.logger.log_unimplemented_method()

    def send_lldp_tlv_local_mgmt_addr(self, port_string, router_id):
        self.start_tlv_local_mgmt_addr(port_string, router_id)
        time.sleep(self.send_sleep_time)
        self.stop_tlv_local_mgmt_addr(port_string, router_id)

    ########################################
    # ####### dot1-port-vlan-id ############
    ########################################
    @abc.abstractmethod
    def add_lldp_tlv_dot1_port_vlan_id(self, port_string, router_id, value):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def remove_lldp_tlv_dot1_port_vlan_id(self, port_string, router_id, value):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def start_tlv_dot1_port_vlan_id(self, port_string, router_id):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def stop_tlv_dot1_port_vlan_id(self, port_string, router_id):
        return self.logger.log_unimplemented_method()

    def send_lldp_tlv_dot1_port_vlan_id(self, port_string, router_id):
        self.start_tlv_dot1_port_vlan_id(port_string, router_id)
        time.sleep(self.send_sleep_time)
        self.stop_tlv_dot1_port_vlan_id(port_string, router_id)

    ########################################
    # ####### dot1-protocol-identity ############
    ########################################
    @abc.abstractmethod
    def add_lldp_tlv_dot1_protocol_identity(self, port_string, router_id, value):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def remove_lldp_tlv_dot1_protocol_identity(self, port_string, router_id, value):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def start_tlv_dot1_protocol_identity(self, port_string, router_id):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def stop_tlv_dot1_protocol_identity(self, port_string, router_id):
        return self.logger.log_unimplemented_method()

    def send_lldp_tlv_dot1_protocol_identity(self, port_string, router_id):
        self.start_tlv_dot1_protocol_identity(port_string, router_id)
        time.sleep(self.send_sleep_time)
        self.stop_tlv_dot1_protocol_identity(port_string, router_id)

    ########################################
    # ####### dot1-port-protocol-vlan-id ############
    ########################################
    @abc.abstractmethod
    def add_lldp_tlv_dot1_port_protocol_vlan_id(self, port_string, router_id, vlan_id, supported, enabled):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def remove_lldp_tlv_dot1_port_protocol_vlan_id(self, port_string, router_id, vlan_id):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def start_tlv_dot1_port_protocol_vlan_id(self, port_string, router_id):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def stop_tlv_dot1_port_protocol_vlan_id(self, port_string, router_id):
        return self.logger.log_unimplemented_method()

    def send_lldp_tlv_dot1_port_protocol_vlan_id(self, port_string, router_id):
        self.start_tlv_dot1_port_protocol_vlan_id(port_string, router_id)
        time.sleep(self.send_sleep_time)
        self.stop_tlv_dot1_port_protocol_vlan_id(port_string, router_id)

    ########################################
    # ####### dot1-vlan-name ############
    ########################################
    @abc.abstractmethod
    def add_lldp_tlv_dot1_vlan_name(self, port_string, router_id, vlan_id, vlan_name):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def remove_lldp_tlv_dot1_vlan_name(self, port_string, router_id, value):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def start_tlv_dot1_vlan_name(self, port_string, router_id):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def stop_tlv_dot1_vlan_name(self, port_string, router_id):
        return self.logger.log_unimplemented_method()

    def send_lldp_tlv_dot1_vlan_name(self, port_string, router_id):
        self.start_tlv_dot1_vlan_name(port_string, router_id)
        time.sleep(self.send_sleep_time)
        self.stop_tlv_dot1_vlan_name(port_string, router_id)

    ########################################
    # ####### dot3-mac-phy-config-status ############
    ########################################
    @abc.abstractmethod
    def add_lldp_tlv_dot3_mac_phy_config_status(self, port_string, router_id, auto_neg_supported, auto_neg_enabled,
                                                auto_neg_ad_cap, op_mau_type):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def remove_lldp_tlv_dot3_mac_phy_config_status(self, port_string, router_id, value):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def start_tlv_dot3_mac_phy_config_status(self, port_string, router_id):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def stop_tlv_dot3_mac_phy_config_status(self, port_string, router_id):
        return self.logger.log_unimplemented_method()

    def send_lldp_tlv_dot3_mac_phy_config_status(self, port_string, router_id):
        self.start_tlv_dot3_mac_phy_config_status(port_string, router_id)
        time.sleep(self.send_sleep_time)
        self.stop_tlv_dot3_mac_phy_config_status(port_string, router_id)

    ########################################
    # ####### dot3-power-mdi ############
    ########################################
    @abc.abstractmethod
    def add_lldp_tlv_dot3_power_mdi(self, port_string, router_id, mdi_power_support, pse_power_pair, power_class):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def remove_lldp_tlv_dot3_power_mdi(self, port_string, router_id, value):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def start_tlv_dot3_power_mdi(self, port_string, router_id):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def stop_tlv_dot3_power_mdi(self, port_string, router_id):
        return self.logger.log_unimplemented_method()

    def send_lldp_tlv_dot3_power_mdi(self, port_string, router_id):
        self.start_tlv_dot3_power_mdi(port_string, router_id)
        time.sleep(self.send_sleep_time)
        self.stop_tlv_dot3_power_mdi(port_string, router_id)

    ########################################
    # ####### dot3-link-aggregation ############
    ########################################
    @abc.abstractmethod
    def add_lldp_tlv_dot3_link_aggregation(self, port_string, router_id, aggregation_supported, aggregation_enabled,
                                           aggregation_id):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def remove_lldp_tlv_dot3_link_aggregation(self, port_string, router_id, value):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def start_tlv_dot3_link_aggregation(self, port_string, router_id):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def stop_tlv_dot3_link_aggregation(self, port_string, router_id):
        return self.logger.log_unimplemented_method()

    def send_lldp_tlv_dot3_link_aggregation(self, port_string, router_id):
        self.start_tlv_dot3_link_aggregation(port_string, router_id)
        time.sleep(self.send_sleep_time)
        self.stop_tlv_dot3_link_aggregation(port_string, router_id)

    ########################################
    # ####### dot3-maximum-frame-size ############
    ########################################
    @abc.abstractmethod
    def add_lldp_tlv_dot3_maximum_frame_size(self, port_string, router_id, value):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def remove_lldp_tlv_dot3_maximum_frame_size(self, port_string, router_id, value):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def start_tlv_dot3_maximum_frame_size(self, port_string, router_id):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def stop_tlv_dot3_maximum_frame_size(self, port_string, router_id):
        return self.logger.log_unimplemented_method()

    def send_lldp_tlv_dot3_maximum_frame_size(self, port_string, router_id):
        self.start_tlv_dot3_maximum_frame_size(port_string, router_id)
        time.sleep(self.send_sleep_time)
        self.stop_tlv_dot3_maximum_frame_size(port_string, router_id)

    ########################################
    # ####### fa-elem ############
    ########################################
    @abc.abstractmethod
    def add_lldp_tlv_fa_elem(self, port_string, router_id, element_type, state, sys_id, conn_type, port_mlt_id,
                             mgmt_vlan):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def remove_lldp_tlv_fa_elem(self, port_string, router_id, value):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def start_tlv_fa_elem(self, port_string, router_id):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def stop_tlv_fa_elem(self, port_string, router_id):
        return self.logger.log_unimplemented_method()

    def send_lldp_tlv_fa_elem(self, port_string, router_id):
        self.start_tlv_fa_elem(port_string, router_id)
        time.sleep(self.send_sleep_time)
        self.stop_tlv_fa_elem(port_string, router_id)

    ########################################
    # ####### fa-isid-vlan-assignment ############
    ########################################
    @abc.abstractmethod
    def add_lldp_tlv_fa_isid_vlan_assignment(self, port_string, router_id, status, vlan, isid, n_mappings, vlan_step,
                                             isid_step):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def remove_lldp_tlv_fa_isid_vlan_assignment(self, port_string, router_id, value):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def start_tlv_fa_isid_vlan_assignment(self, port_string, router_id):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def stop_tlv_fa_isid_vlan_assignment(self, port_string, router_id):
        return self.logger.log_unimplemented_method()

    def send_lldp_tlv_fa_isid_vlan_assignment(self, port_string, router_id):
        self.start_tlv_fa_isid_vlan_assignment(port_string, router_id)
        time.sleep(self.send_sleep_time)
        self.stop_tlv_fa_isid_vlan_assignment(port_string, router_id)

    ########################################
    # ####### med-capabilites ############
    ########################################
    @abc.abstractmethod
    def add_lldp_tlv_med_capabilites(self, port_string, router_id, capabilty, network_policy, location_id,
                                     extended_power_pse, extended_power_pd, inventory, device_type):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def remove_lldp_tlv_med_capabilites(self, port_string, router_id, value):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def start_tlv_med_capabilites(self, port_string, router_id):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def stop_tlv_med_capabilites(self, port_string, router_id):
        return self.logger.log_unimplemented_method()

    def send_lldp_tlv_med_capabilites(self, port_string, router_id):
        self.start_tlv_med_capabilites(port_string, router_id)
        time.sleep(self.send_sleep_time)
        self.stop_tlv_med_capabilites(port_string, router_id)

    ########################################
    # ####### med-network-policy ############
    ########################################
    @abc.abstractmethod
    def add_lldp_tlv_med_network_policy(self, port_string, router_id, network_policy_action, app_tlv_type, unknown,
                                        tagged, vlan_id, l2_priority, dscp):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def remove_lldp_tlv_med_network_policy(self, port_string, router_id, value):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def start_tlv_med_network_policy(self, port_string, router_id):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def stop_tlv_med_network_policy(self, port_string, router_id):
        return self.logger.log_unimplemented_method()

    def send_lldp_tlv_med_network_policy(self, port_string, router_id):
        self.start_tlv_med_network_policy(port_string, router_id)
        time.sleep(self.send_sleep_time)
        self.stop_tlv_med_network_policy(port_string, router_id)

    ########################################
    # ####### med-location-id ############
    ########################################
    @abc.abstractmethod
    def add_lldp_tlv_med_location_id(self, port_string, router_id, coordinate_loc_action, civic_loc_action,
                                     ecs_elin_loc_action, coordinate_loc, civic_loc, ecs_elin_loc):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def remove_lldp_tlv_med_location_id(self, port_string, router_id, value):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def start_tlv_med_location_id(self, port_string, router_id):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def stop_tlv_med_location_id(self, port_string, router_id):
        return self.logger.log_unimplemented_method()

    def send_lldp_tlv_med_location_id(self, port_string, router_id):
        self.start_tlv_med_location_id(port_string, router_id)
        time.sleep(self.send_sleep_time)
        self.stop_tlv_med_location_id(port_string, router_id)

    ########################################
    # ####### med-power-via-mdi ############
    ########################################
    @abc.abstractmethod
    def add_lldp_tlv_med_power_via_mdi(self, port_string, router_id, power_type, power_src, power_priority,
                                       power_value):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def remove_lldp_tlv_med_power_via_mdi(self, port_string, router_id, value):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def start_tlv_med_power_via_mdi(self, port_string, router_id):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def stop_tlv_med_power_via_mdi(self, port_string, router_id):
        return self.logger.log_unimplemented_method()

    def send_lldp_tlv_med_power_via_mdi(self, port_string, router_id):
        self.start_tlv_med_power_via_mdi(port_string, router_id)
        time.sleep(self.send_sleep_time)
        self.stop_tlv_med_power_via_mdi(port_string, router_id)

    ########################################
    # ####### med-hw-revision ############
    ########################################
    @abc.abstractmethod
    def add_lldp_tlv_med_hw_revision(self, port_string, router_id, value):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def remove_lldp_tlv_med_hw_revision(self, port_string, router_id, value):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def start_tlv_med_hw_revision(self, port_string, router_id):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def stop_tlv_med_hw_revision(self, port_string, router_id):
        return self.logger.log_unimplemented_method()

    def send_lldp_tlv_med_hw_revision(self, port_string, router_id):
        self.start_tlv_med_hw_revision(port_string, router_id)
        time.sleep(self.send_sleep_time)
        self.stop_tlv_med_hw_revision(port_string, router_id)

    ########################################
    # ####### med-firmware-revision ############
    ########################################
    @abc.abstractmethod
    def add_lldp_tlv_med_firmware_revision(self, port_string, router_id, value):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def remove_lldp_tlv_med_firmware_revision(self, port_string, router_id, value):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def start_tlv_med_firmware_revision(self, port_string, router_id):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def stop_tlv_med_firmware_revision(self, port_string, router_id):
        return self.logger.log_unimplemented_method()

    def send_lldp_tlv_med_firmware_revision(self, port_string, router_id):
        self.start_tlv_med_firmware_revision(port_string, router_id)
        time.sleep(self.send_sleep_time)
        self.stop_tlv_med_firmware_revision(port_string, router_id)

    ########################################
    # ####### med-software-revision ############
    ########################################
    @abc.abstractmethod
    def add_lldp_tlv_med_software_revision(self, port_string, router_id, value):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def remove_lldp_tlv_med_software_revision(self, port_string, router_id, value):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def start_tlv_med_software_revision(self, port_string, router_id):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def stop_tlv_med_software_revision(self, port_string, router_id):
        return self.logger.log_unimplemented_method()

    def send_lldp_tlv_med_software_revision(self, port_string, router_id):
        self.start_tlv_med_software_revision(port_string, router_id)
        time.sleep(self.send_sleep_time)
        self.stop_tlv_med_software_revision(port_string, router_id)

    ########################################
    # ####### med-serial-number ############
    ########################################
    @abc.abstractmethod
    def add_lldp_tlv_med_serial_number(self, port_string, router_id, value):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def remove_lldp_tlv_med_serial_number(self, port_string, router_id, value):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def start_tlv_med_serial_number(self, port_string, router_id):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def stop_tlv_med_serial_number(self, port_string, router_id):
        return self.logger.log_unimplemented_method()

    def send_lldp_tlv_med_serial_number(self, port_string, router_id):
        self.start_tlv_med_serial_number(port_string, router_id)
        time.sleep(self.send_sleep_time)
        self.stop_tlv_med_serial_number(port_string, router_id)

    ########################################
    # ####### med-mfg-name ############
    ########################################
    @abc.abstractmethod
    def add_lldp_tlv_med_mfg_name(self, port_string, router_id, value):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def remove_lldp_tlv_med_mfg_name(self, port_string, router_id, value):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def start_tlv_med_mfg_name(self, port_string, router_id):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def stop_tlv_med_mfg_name(self, port_string, router_id):
        return self.logger.log_unimplemented_method()

    def send_lldp_tlv_med_mfg_name(self, port_string, router_id):
        self.start_tlv_med_mfg_name(port_string, router_id)
        time.sleep(self.send_sleep_time)
        self.stop_tlv_med_mfg_name(port_string, router_id)

    ########################################
    # ####### med-model-name ############
    ########################################
    @abc.abstractmethod
    def add_lldp_tlv_med_model_name(self, port_string, router_id, value):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def remove_lldp_tlv_med_model_name(self, port_string, router_id, value):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def start_tlv_med_model_name(self, port_string, router_id):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def stop_tlv_med_model_name(self, port_string, router_id):
        return self.logger.log_unimplemented_method()

    def send_lldp_tlv_med_model_name(self, port_string, router_id):
        self.start_tlv_med_model_name(port_string, router_id)
        time.sleep(self.send_sleep_time)
        self.stop_tlv_med_model_name(port_string, router_id)

    ########################################
    # ####### med-asset-id ############
    ########################################
    @abc.abstractmethod
    def add_lldp_tlv_med_asset_id(self, port_string, router_id, value):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def remove_lldp_tlv_med_asset_id(self, port_string, router_id, value):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def start_tlv_med_asset_id(self, port_string, router_id):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def stop_tlv_med_asset_id(self, port_string, router_id):
        return self.logger.log_unimplemented_method()

    def send_lldp_tlv_med_asset_id(self, port_string, router_id):
        self.start_tlv_med_asset_id(port_string, router_id)
        time.sleep(self.send_sleep_time)
        self.stop_tlv_med_asset_id(port_string, router_id)


class NetworkEmulatingLldpConstants(object, metaclass=Singleton):
    # api reference constant for this api to get it from the device
    LLDP_API = "LLDP_API"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass
