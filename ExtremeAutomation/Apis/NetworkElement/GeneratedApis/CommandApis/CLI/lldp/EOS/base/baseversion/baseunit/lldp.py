"""
All lldp supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.lldp.base.lldpbase import LldpBase


class Lldp(DeviceApi, LldpBase):
    def __init__(self, device_input):
        super(Lldp, self).__init__(device_input)

    def enable_port_tx(self, arg_dictionary, **kwargs):
        uuid = "e6946508-8d34-4463-b62c-6c89f5fce29c"
        cmd = "set lldp port status tx-enable {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_port_rx(self, arg_dictionary, **kwargs):
        uuid = "b72e04e4-15c2-4027-a94c-2c6600bfc20a"
        cmd = "set lldp port status rx-enable {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_port_both(self, arg_dictionary, **kwargs):
        uuid = "b674aaf4-2510-4811-9f2e-e11b1bc7a612"
        cmd = "set lldp port status both {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_port(self, arg_dictionary, **kwargs):
        uuid = "9e2d8119-4960-41d5-9bc6-252c40fc311b"
        cmd = "set lldp port status disable {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_tx_interval(self, arg_dictionary, **kwargs):
        uuid = "6d9bd153-8795-4c40-95f3-2a06039393b9"
        cmd = "set lldp tx-interval {0}".format(arg_dictionary['interval'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_tlv_all(self, arg_dictionary, **kwargs):
        uuid = "b87c2fc6-002d-4b4d-bc16-269649cecdf1"
        cmd = "set lldp port tx-tlv all {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_tlv_all(self, arg_dictionary, **kwargs):
        uuid = "ea8c4361-a4d8-46cd-98d0-2883ddf8cda5"
        cmd = "clear lldp port tx-tlv all {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_tlv_port_desc(self, arg_dictionary, **kwargs):
        uuid = "243e2cdd-76ec-4b10-8f24-56d1dade6b1e"
        cmd = "set lldp port tx-tlv port-desc {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_tlv_port_desc(self, arg_dictionary, **kwargs):
        uuid = "a2f0e913-05b3-4b17-8e87-8734ca8a4ce2"
        cmd = "clear lldp port tx-tlv port-desc {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_tlv_sys_name(self, arg_dictionary, **kwargs):
        uuid = "1f43c317-9cd6-4523-8a75-f672666fcc8a"
        cmd = "set lldp port tx-tlv sys-name {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_tlv_sys_name(self, arg_dictionary, **kwargs):
        uuid = "5b05361b-96d9-4deb-b82c-7f1e2979c976"
        cmd = "clear lldp port tx-tlv sys-name {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_tlv_sys_desc(self, arg_dictionary, **kwargs):
        uuid = "92eb5100-f65a-4596-8a20-73adb056d328"
        cmd = "set lldp port tx-tlv sys-desc {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_tlv_sys_desc(self, arg_dictionary, **kwargs):
        uuid = "6224f79f-4236-4161-8e60-1d3abb1fa87c"
        cmd = "clear lldp port tx-tlv sys-desc {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_tlv_sys_cap(self, arg_dictionary, **kwargs):
        uuid = "8fabfec5-88d0-45ae-8f46-0a6d86b6a8e3"
        cmd = "set lldp port tx-tlv sys-cap {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_tlv_sys_cap(self, arg_dictionary, **kwargs):
        uuid = "3c0cd7be-4edf-4816-8fed-62171d39d293"
        cmd = "clear lldp port tx-tlv sys-cap {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_tlv_mgmt_addr(self, arg_dictionary, **kwargs):
        uuid = "7b4f3527-942b-4730-bffb-4a74bb673f83"
        cmd = "set lldp port tx-tlv mgmt-addr {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_tlv_mgmt_addr(self, arg_dictionary, **kwargs):
        uuid = "7925caba-a530-4639-831d-57795d4a7c51"
        cmd = "clear lldp port tx-tlv mgmt-addr {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_tlv_vlan_id(self, arg_dictionary, **kwargs):
        uuid = "0f0b8b56-beb6-4c81-afda-87ecc3aee353"
        cmd = "set lldp port tx-tlv vlan-id {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_tlv_vlan_id(self, arg_dictionary, **kwargs):
        uuid = "5cba4f56-6f30-4f85-a289-7ad1c77794c1"
        cmd = "clear lldp port tx-tlv vlan-id {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_tlv_stp(self, arg_dictionary, **kwargs):
        uuid = "bc2117f1-b152-4837-9dcb-5cef7486f8eb"
        cmd = "set lldp port tx-tlv stp {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_tlv_stp(self, arg_dictionary, **kwargs):
        uuid = "e5b114b3-f94c-4711-9ded-047064dfb083"
        cmd = "clear lldp port tx-tlv stp {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_tlv_lacp(self, arg_dictionary, **kwargs):
        uuid = "8953e640-7f5a-441b-8ef4-27ea2d027c74"
        cmd = "set lldp port tx-tlv lacp {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_tlv_lacp(self, arg_dictionary, **kwargs):
        uuid = "7febd848-9247-45bf-9b7e-54335a947b96"
        cmd = "clear lldp port tx-tlv lacp {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_tlv_gvrp(self, arg_dictionary, **kwargs):
        uuid = "5ede15e9-fc5e-402c-b5db-4f234218894b"
        cmd = "set lldp port tx-tlv gvrp {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_tlv_gvrp(self, arg_dictionary, **kwargs):
        uuid = "872228d2-f196-4f8e-812d-1a1c141e2c0e"
        cmd = "clear lldp port tx-tlv gvrp {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_tlv_mac_phy(self, arg_dictionary, **kwargs):
        uuid = "58cce8d3-d1e4-44ee-8d2c-93df254cb67c"
        cmd = "set lldp port tx-tlv mac-phy {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_tlv_mac_phy(self, arg_dictionary, **kwargs):
        uuid = "3026e5b5-721b-4e26-af59-092bee7db3e2"
        cmd = "clear lldp port tx-tlv mac-phy {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_tlv_poe(self, arg_dictionary, **kwargs):
        uuid = "f690f55d-0899-4a4a-bf9e-9b6f5eddbb3e"
        cmd = "set lldp port tx-tlv poe {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_tlv_poe(self, arg_dictionary, **kwargs):
        uuid = "9d5ce203-14af-40df-ba2b-a1ec958fd9b0"
        cmd = "clear lldp port tx-tlv poe {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_tlv_link_aggr(self, arg_dictionary, **kwargs):
        uuid = "4998957c-135b-475e-be63-8ce458785948"
        cmd = "set lldp port tx-tlv link-aggr {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_tlv_link_aggr(self, arg_dictionary, **kwargs):
        uuid = "76d7d5cd-5ddf-4113-9d77-58d84e87500e"
        cmd = "clear lldp port tx-tlv link-aggr {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_tlv_max_frame(self, arg_dictionary, **kwargs):
        uuid = "3be2d985-95d5-49dc-b629-aee16614268c"
        cmd = "set lldp port tx-tlv max-frame {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_tlv_max_frame(self, arg_dictionary, **kwargs):
        uuid = "09945c31-ed11-4ff1-ac7a-7c4d864860b0"
        cmd = "clear lldp port tx-tlv max-frame {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_tlv_med_cap(self, arg_dictionary, **kwargs):
        uuid = "552405ea-e481-40b1-95a6-a552f4510004"
        cmd = "set lldp port tx-tlv med-cap {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_tlv_med_cap(self, arg_dictionary, **kwargs):
        uuid = "3cc242e9-6b38-4584-b7f3-0481c092e9a9"
        cmd = "clear lldp port tx-tlv med-cap {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_tlv_med_pol(self, arg_dictionary, **kwargs):
        uuid = "d465bbdc-1a1d-4e99-a5d4-6a65050ddd8c"
        cmd = "set lldp port tx-tlv med-pol {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_tlv_med_pol(self, arg_dictionary, **kwargs):
        uuid = "96f950c4-4fff-429e-90c6-6641d2b8d811"
        cmd = "clear lldp port tx-tlv med-pol {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_tlv_med_loc(self, arg_dictionary, **kwargs):
        uuid = "8fa838ad-7193-4b74-8e09-da9083f5483a"
        cmd = "set lldp port tx-tlv med-loc {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_tlv_med_loc(self, arg_dictionary, **kwargs):
        uuid = "8ca06470-435a-4f4c-8cc3-80623ffa9883"
        cmd = "clear lldp port tx-tlv med-loc {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_tlv_med_poe(self, arg_dictionary, **kwargs):
        uuid = "9a5a8eb2-b647-4eba-b0cd-41259fca8ae5"
        cmd = "set lldp port tx-tlv med-poe {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_tlv_med_poe(self, arg_dictionary, **kwargs):
        uuid = "dda342f7-4bb8-478f-bbf5-cd2511ea3063"
        cmd = "clear lldp port tx-tlv med-poe {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_tlv_enhanced_trans_config(self, arg_dictionary, **kwargs):
        uuid = "abe67216-3fe5-4952-83c6-ccf4c0b802c4"
        cmd = "set lldp port tx-tlv enhanced-trans-config {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_tlv_enhanced_trans_config(self, arg_dictionary, **kwargs):
        uuid = "d58a86f9-c2de-4c79-afac-de230fbbe546"
        cmd = "clear lldp port tx-tlv enhanced-trans-config {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_tlv_enhanced_trans_rec(self, arg_dictionary, **kwargs):
        uuid = "63d89deb-76ff-4f3f-b069-bbd8febe8f17"
        cmd = "set lldp port tx-tlv enhanced-trans-rec {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_tlv_enhanced_trans_rec(self, arg_dictionary, **kwargs):
        uuid = "59e71132-ab0e-473b-8dbf-a243b6102559"
        cmd = "clear lldp port tx-tlv enhanced-trans-rec {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_tlv_priority_flowctrl(self, arg_dictionary, **kwargs):
        uuid = "5e1ab984-d780-4447-ab3d-220c2bebf35a"
        cmd = "set lldp port tx-tlv priority-flowctrl {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_tlv_priority_flowctrl(self, arg_dictionary, **kwargs):
        uuid = "deeddb93-b780-488c-b18a-0830b8c23800"
        cmd = "clear lldp port tx-tlv priority-flowctrl {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_tlv_application_pri(self, arg_dictionary, **kwargs):
        uuid = "8a7f77d1-2cfa-473d-943a-5cefdd286c46"
        cmd = "set lldp port tx-tlv application-pri {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_tlv_application_pri(self, arg_dictionary, **kwargs):
        uuid = "61ebed67-8ee2-45b2-9c7b-50b5b3dba5c5"
        cmd = "clear lldp port tx-tlv application-pri {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_tlv_congestion_notif(self, arg_dictionary, **kwargs):
        uuid = "a8408611-f3e6-4d15-93f6-bfa1463e9a72"
        cmd = "set lldp port tx-tlv congestion-notif {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_tlv_congestion_notif(self, arg_dictionary, **kwargs):
        uuid = "fa7dd0f8-893d-420f-a3d7-1330333dba5c"
        cmd = "clear lldp port tx-tlv congestion-notif {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_tlv_energy_eff_eth(self, arg_dictionary, **kwargs):
        uuid = "174b1a07-724a-4859-87cb-c356c6cf5de1"
        cmd = "set lldp port tx-tlv energy-eff-eth {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_tlv_energy_eff_eth(self, arg_dictionary, **kwargs):
        uuid = "37c1b5b7-f2c4-4a11-8f71-6f71ddedec67"
        cmd = "clear lldp port tx-tlv energy-eff-eth {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_info(self, arg_dictionary, **kwargs):
        uuid = "62450147-99e0-443c-aaad-b21b4c9925d1"
        cmd = "show lldp"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_remote_info(self, arg_dictionary, **kwargs):
        uuid = "7d530f4d-ac18-45cd-ad0e-691f9ced3f68"
        cmd = "show lldp port remote-info {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port_status(self, arg_dictionary, **kwargs):
        uuid = "48a749d4-bcb4-4e9c-8f11-c3922d86b571"
        cmd = "show lldp port status {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port_tlv_port_desc(self, arg_dictionary, **kwargs):
        uuid = "90b69a1c-5850-4db2-923c-98c82ed26567"
        cmd = "show lldp port tx-tlv {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port_tlv_sys_name(self, arg_dictionary, **kwargs):
        uuid = "b87d809c-15fc-4500-872a-385b4dd9a830"
        cmd = "show lldp port tx-tlv {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port_tlv_sys_desc(self, arg_dictionary, **kwargs):
        uuid = "09bba48c-f31b-4464-97fc-d320b32df75b"
        cmd = "show lldp port tx-tlv {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port_tlv_sys_cap(self, arg_dictionary, **kwargs):
        uuid = "74f91b41-fb4e-4f14-aaf9-f186b6adc31a"
        cmd = "show lldp port tx-tlv {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port_tlv_mgmt_addr(self, arg_dictionary, **kwargs):
        uuid = "2a2a935d-6545-4429-b769-bed5bcdc8244"
        cmd = "show lldp port tx-tlv {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port_tlv_vlan_id(self, arg_dictionary, **kwargs):
        uuid = "9d034d05-1d46-45d0-bb47-3551e4ef6755"
        cmd = "show lldp port tx-tlv {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port_tlv_stp(self, arg_dictionary, **kwargs):
        uuid = "4dad8fde-005f-4df9-8ed4-b62667924c4a"
        cmd = "show lldp port tx-tlv {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port_tlv_lacp(self, arg_dictionary, **kwargs):
        uuid = "4e67faaf-c530-4b1c-97f3-e707862b5446"
        cmd = "show lldp port tx-tlv {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port_tlv_gvrp(self, arg_dictionary, **kwargs):
        uuid = "fcfcaf7b-2770-450e-a4d2-d216a8eea45e"
        cmd = "show lldp port tx-tlv {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port_tlv_mac_phy(self, arg_dictionary, **kwargs):
        uuid = "8a3cbdba-f26a-4ffa-9ee5-6fa5b8a28ab7"
        cmd = "show lldp port tx-tlv {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port_tlv_poe(self, arg_dictionary, **kwargs):
        uuid = "d9b47836-69f9-4292-aba6-0ac1d085beef"
        cmd = "show lldp port tx-tlv {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port_tlv_link_aggr(self, arg_dictionary, **kwargs):
        uuid = "83b6aabd-28fd-4904-bc87-88d1fd5e06cd"
        cmd = "show lldp port tx-tlv {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port_tlv_max_frame(self, arg_dictionary, **kwargs):
        uuid = "ba29f2a8-f288-43bf-a654-bb45cf65a3c7"
        cmd = "show lldp port tx-tlv {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port_tlv_med_cap(self, arg_dictionary, **kwargs):
        uuid = "49c622d4-a173-4067-9074-95c099f76bce"
        cmd = "show lldp port tx-tlv {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port_tlv_med_pol(self, arg_dictionary, **kwargs):
        uuid = "947194fe-e2f5-44e3-8830-54c878751896"
        cmd = "show lldp port tx-tlv {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port_tlv_med_loc(self, arg_dictionary, **kwargs):
        uuid = "93f736c3-3667-41ed-89ac-db7d39e1d3b2"
        cmd = "show lldp port tx-tlv {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port_tlv_med_poe(self, arg_dictionary, **kwargs):
        uuid = "e1d82fd0-e7d6-4447-9ae1-8cb99caba77d"
        cmd = "show lldp port tx-tlv {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port_tlv_enhanced_trans_config(self, arg_dictionary, **kwargs):
        uuid = "868604b6-9e7b-4910-ac1e-fdb928b78109"
        cmd = "show lldp port tx-tlv data-center-bridging {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port_tlv_enhanced_trans_rec(self, arg_dictionary, **kwargs):
        uuid = "2bf0f891-4fc9-40cc-b0ca-5b0712735aba"
        cmd = "show lldp port tx-tlv data-center-bridging {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port_tlv_priority_flowctrl(self, arg_dictionary, **kwargs):
        uuid = "548ecdd2-d112-42df-9ad1-961cd10a4035"
        cmd = "show lldp port tx-tlv data-center-bridging {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port_tlv_application_pri(self, arg_dictionary, **kwargs):
        uuid = "8a5c24db-532e-4423-ac2b-a6bfb90ba359"
        cmd = "show lldp port tx-tlv data-center-bridging {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port_tlv_congestion_notif(self, arg_dictionary, **kwargs):
        uuid = "12b3ff22-830f-478f-bd3a-f37a3cfdc9f9"
        cmd = "show lldp port tx-tlv data-center-bridging {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port_tlv_energy_eff_eth(self, arg_dictionary, **kwargs):
        uuid = "496b0655-1270-49c3-9b6a-801b4d9b3db1"
        cmd = "show lldp port tx-tlv {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
