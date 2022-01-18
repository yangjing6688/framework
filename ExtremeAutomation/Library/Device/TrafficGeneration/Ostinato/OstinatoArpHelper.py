from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.Apis.IxRouteIxTclHalApi import IxRouteIxTclHalConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.TrafficGeneratingDeviceArpHelper import \
    TrafficGeneratingDeviceArpHelper
from ExtremeAutomation.Library.Net.Address.Ipv4Address import Ipv4Address
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.core import ost_pb, emul, DroneProxy


class OstinatoArpHelper(TrafficGeneratingDeviceArpHelper):

    def configure_arp(self, port_string, start_ip, start_mac, num_addresses, gateway_address,
                      mapping_option=IxRouteIxTclHalConstants.IP_TABLE_MAPPING_OPTIONS_ONE_IP_TO_ONE_MAC,
                      arp_for=IxRouteIxTclHalConstants.ARP_MODE_RESOLVE_ARP, arp_retires=3,
                      netmask=24, vlan_enable=False, vlan_id=None, clear_settings_first=False):
        drone = self.connection
        assert isinstance(drone, DroneProxy)
        port_string = self.ostinato_port_number_to_port(port_string)

        if clear_settings_first:
            # delete the existing devices on my port
            tx = drone.getDeviceGroupIdList(port_string.port_id[0])
            drone.deleteDeviceGroup(tx)

        # add the a new device to the port
        # tx = ost_pb.DeviceGroupIdList()
        # tx.port_id.CopyFrom(port_string.port_id[0])
        tx = drone.getDeviceGroupIdList(port_string.port_id[0])
        new_dev = tx.device_group_id.add()
        new_dev.id = self.get_next_device_id(tx.device_group_id)
        drone.addDeviceGroup(tx)

        # add and configure the device above.
        tx_devgrp_cfg = ost_pb.DeviceGroupConfigList()
        tx_devgrp_cfg.port_id.CopyFrom(port_string.port_id[0])
        dg = tx_devgrp_cfg.device_group.add()
        dg.device_group_id.id = new_dev.id
        dg.core.name = "DUTestHost"
        # dg.device_count = int(num_addresses)

        # set the mac address
        dg.Extensions[emul.mac].address = int(start_mac.replace(":", ""), 16)
        dg.Extensions[emul.mac].step = num_addresses

        # set the ip address
        ip = dg.Extensions[emul.ip4]
        ip4 = Ipv4Address(start_ip)
        start_ip = ip4.to_formated_string(16,"")
        ip.address = int(start_ip, 16)
        ip.prefix_length = netmask
        ip.step = num_addresses
        ip = dg.Extensions[emul.ip4]
        ip4 = Ipv4Address(gateway_address)
        gateway_address = ip4.to_formated_string(16,"")
        ip.default_gateway = int(gateway_address, 16)

        # set the vlan if needed
        if vlan_enable:
            v = dg.encap.Extensions[emul.vlan].stack.add()
            v.vlan_tag = vlan_id
            v.count = 1
            v.tpid = 0x8100
            v.step = 1

        # modify the device group
        drone.modifyDeviceGroup(tx_devgrp_cfg)

        ##
        # Next maybe set up a stream with resolve macs or get it to reply to ICMP.
        ##

    def configure_neighbor_discovery(self, port_string, start_ipv6, start_mac, num_addresses, gateway_address,
                                     mapping_option=IxRouteIxTclHalConstants.IP_TABLE_MAPPING_OPTIONS_ONE_IP_TO_ONE_MAC,
                                     arp_for=IxRouteIxTclHalConstants.ARP_MODE_RESOLVE_ARP, arp_retires=3,
                                     netmask=24, vlan_enable=False, vlan_id=None, clear_settings_first=False):
        return self.logger.log_unimplemented_method()

    def get_next_device_id(self, device_group_list):
        max_val = 0
        for dev in device_group_list:
            max_val = max(max_val, dev.id)
        return max_val + 1

    def ping(self, port_string, source_ip, destination_ip, timeout_secs=30, ping_count=3):
        return self.logger.log_unimplemented_method()
