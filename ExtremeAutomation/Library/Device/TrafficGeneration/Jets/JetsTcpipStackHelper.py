
class JetsTcpipStackHelper(object):
    def __init__(self, ostinato_device):
        self.dev = ostinato_device
        self.tcp_stacks = []

    def get_tcp_config_string(self, port_string):
        prt_id = self.get_port_index_from_group_string(port_string)
        config_str = "alias"
        if prt_id not in self.tcp_stacks:
            self.tcp_stacks.append(prt_id)
            config_str = "config"
        return config_str

    def clear_tcp_port_config(self, port_string):
        prt_id = self.get_port_index_from_group_string(port_string)
        if prt_id in self.tcp_stacks:
            self.tcp_stacks.remove(prt_id)


class JetsTcpipStack(object):
    def __init__(self):
        self.port_string = None
        self.ip_address = None
        self.netmask = None
        self.gateway = None
        self.mac_address = None
        self.state = None
