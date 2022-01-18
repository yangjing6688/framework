"""
All mlag supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.mlag.base.mlagbase import MlagBase


class Mlag(DeviceApi, MlagBase):
    def __init__(self, device_input):
        super(Mlag, self).__init__(device_input)

    def enable_port_peer_id(self, arg_dictionary, **kwargs):
        uuid = "0b8e33d5-a856-431c-b6af-08773902b814"
        cmd = "enable mlag port {0} peer {1} id {2}".format(arg_dictionary['port'],
                                                            arg_dictionary['peer'],
                                                            arg_dictionary['pid'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_port_reload_delay(self, arg_dictionary, **kwargs):
        uuid = "3baa4d4e-76db-4630-b6d1-66b762d8e99b"
        cmd = "enable mlag port reload-delay"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_port(self, arg_dictionary, **kwargs):
        uuid = "1ba93bc2-e255-4189-85da-38546cd52484"
        cmd = "disable mlag port {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_port_reload_delay(self, arg_dictionary, **kwargs):
        uuid = "f9d7e823-ee46-436a-8525-6e42abd57292"
        cmd = "disable mlag port reload-delay"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def create_peer(self, arg_dictionary, **kwargs):
        uuid = "d6090d24-851a-4809-a2d0-c5de13f07719"
        cmd = "create mlag peer {0}".format(arg_dictionary['peer'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def create_peer_auth_md5_key(self, arg_dictionary, **kwargs):
        uuid = "6078f6fa-eb08-4508-a326-1d1b7282842a"
        cmd = "create mlag peer {0} authentication md5 key".format(arg_dictionary['peer'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def create_peer_auth_md5_key_name(self, arg_dictionary, **kwargs):
        uuid = "728b7687-90f1-4750-9558-a420850486b2"
        cmd = "create mlag peer {0} authentication md5 key {1}".format(arg_dictionary['peer'],
                                                                       arg_dictionary['key'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def create_peer_auth_md5_key_encrypted(self, arg_dictionary, **kwargs):
        uuid = "83442bb1-ee4a-414c-ad3a-ef70cde3634e"
        cmd = "create mlag peer {0} authentication md5 key encrypted {1}".format(arg_dictionary['peer'],
                                                                                 arg_dictionary['key'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def delete_peer(self, arg_dictionary, **kwargs):
        uuid = "8419a4eb-1be3-48f2-82d0-3284815a2de9"
        cmd = "delete mlag peer {0}".format(arg_dictionary['peer'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_peer(self, arg_dictionary, **kwargs):
        uuid = "d12c0189-3659-41ef-90ca-6a3d776775d1"
        cmd = "configure mlag peer {0}".format(arg_dictionary['peer'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_peer_alternate_ip(self, arg_dictionary, **kwargs):
        uuid = "c4fe5069-51eb-40d9-9215-408154383cd7"
        cmd = "configure mlag peer {0} alternate ipaddress {1}".format(arg_dictionary['peer'],
                                                                       arg_dictionary['ip'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_peer_alternate_ip_none(self, arg_dictionary, **kwargs):
        uuid = "dc20052e-7934-445c-a61f-56911277d22d"
        cmd = "configure mlag peer {0} alternate ipaddress none".format(arg_dictionary['peer'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_peer_alternate_ip_vr(self, arg_dictionary, **kwargs):
        uuid = "2554033b-28e7-4acc-8f31-8a2134ae5150"
        cmd = "configure mlag peer {0} alternate ipaddress {1} vr {2}".format(arg_dictionary['peer'],
                                                                              arg_dictionary['ip'],
                                                                              arg_dictionary['vr'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_peer_auth_none(self, arg_dictionary, **kwargs):
        uuid = "cf428def-4046-4837-aea3-52789a6181be"
        cmd = "configure mlag peer {0} authentication none".format(arg_dictionary['peer'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_peer_auth_md5_key(self, arg_dictionary, **kwargs):
        uuid = "2a38a015-79ad-4f94-b2ac-e577a5821c93"
        cmd = "configure mlag peer {0} authentication md5 key".format(arg_dictionary['peer'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_peer_auth_md5_key_name(self, arg_dictionary, **kwargs):
        uuid = "88183926-ddef-45dd-9d17-6e9ac74f48b2"
        cmd = "configure mlag peer {0} authentication md5 key {1}".format(arg_dictionary['peer'],
                                                                          arg_dictionary['key'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_peer_auth_md5_key_encrypted(self, arg_dictionary, **kwargs):
        uuid = "eea9d78d-99cf-4ce8-90e2-e4d619d2df37"
        cmd = "configure mlag peer {0} authentication md5 key encrypted {1}".format(arg_dictionary['peer'],
                                                                                    arg_dictionary['key'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_peer_interval(self, arg_dictionary, **kwargs):
        uuid = "3c8d7a3c-4d90-4bf3-96f9-3221055bdbe7"
        cmd = "configure mlag peer {0} interval {1}".format(arg_dictionary['peer'],
                                                            arg_dictionary['interval'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_peer_ipaddress(self, arg_dictionary, **kwargs):
        uuid = "14c2e6cf-1e10-4a24-b460-175714cbd854"
        cmd = "configure mlag peer {0} ipaddress {1}".format(arg_dictionary['peer'],
                                                             arg_dictionary['ip'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_peer_ipaddress_vr(self, arg_dictionary, **kwargs):
        uuid = "f0a99314-5fd4-4de2-97a4-2bf2d12a1b64"
        cmd = "configure mlag peer {0} ipaddress {1} vr {2}".format(arg_dictionary['peer'],
                                                                    arg_dictionary['ip'],
                                                                    arg_dictionary['vr'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_peer_lacp_mac(self, arg_dictionary, **kwargs):
        uuid = "e4d3e1e5-002e-42ca-877e-00c031076cc0"
        cmd = "configure mlag peer {0} lacp-mac {1}".format(arg_dictionary['peer'],
                                                            arg_dictionary['mac'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_peer_lacp_mac_auto(self, arg_dictionary, **kwargs):
        uuid = "5467213f-ae96-4762-bd87-e01435a68c11"
        cmd = "configure mlag peer {0} lacp-mac auto".format(arg_dictionary['peer'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_peer_new_name(self, arg_dictionary, **kwargs):
        uuid = "5ee749cf-6635-4b08-8009-904a5692bd98"
        cmd = "configure mlag peer {0} name {1}".format(arg_dictionary['peer'],
                                                        arg_dictionary['name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_peer(self, arg_dictionary, **kwargs):
        uuid = "18c01586-d6ad-49c2-8dc5-d5c94e2e4343"
        cmd = "show mlag peer {0}".format(arg_dictionary['peer'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_peer_all(self, arg_dictionary, **kwargs):
        uuid = "e9f85c68-c116-4539-a42e-440172315425"
        cmd = "show mlag peer"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_ports(self, arg_dictionary, **kwargs):
        uuid = "13a9eb43-00e9-4f9e-ba20-e43295a0d37e"
        cmd = "show mlag ports {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_ports_all(self, arg_dictionary, **kwargs):
        uuid = "bf864b86-2ae1-43b4-b3b2-d976b017cbae"
        cmd = "show mlag ports"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
