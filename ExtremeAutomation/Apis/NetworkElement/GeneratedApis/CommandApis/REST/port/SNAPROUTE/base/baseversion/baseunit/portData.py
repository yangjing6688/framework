class PortData(object):
    @staticmethod
    def enable_state_data(arg_dict):
        data = {"IntfRef": arg_dict["port"],
                "AdminState": "UP"
                }

        return data

    @staticmethod
    def disable_state_data(arg_dict):
        data = {"IntfRef": arg_dict["port"],
                "AdminState": "DOWN"
                }

        return data

    @staticmethod
    def show_info_detail_data(arg_dict):
        data = {"IntfRef": arg_dict["port"]}

        return data

    @staticmethod
    def show_admin_status_data(arg_dict):
        data = {"IntfRef": arg_dict["port"]}

        return data

    @staticmethod
    def show_oper_status_data(arg_dict):
        data = {"IntfRef": arg_dict["port"]}

        return data

    @staticmethod
    def show_mtu_data(arg_dict):
        data = {"IntfRef": arg_dict["port"]}

        return data

    @staticmethod
    def show_mac_address_data(arg_dict):
        data = {"IntfRef": arg_dict["port"]}

        return data

    @staticmethod
    def show_high_speed_data(arg_dict):
        data = {"IntfRef": arg_dict["port"]}

        return data

    @staticmethod
    def show_in_octets_data(arg_dict):
        data = {"IntfRef": arg_dict["port"]}

        return data

    @staticmethod
    def show_in_discard_packets_data(arg_dict):
        data = {"IntfRef": arg_dict["port"]}

        return data

    @staticmethod
    def show_in_error_packets_data(arg_dict):
        data = {"IntfRef": arg_dict["port"]}

        return data

    @staticmethod
    def show_in_unknown_protocol_packets_data(arg_dict):
        data = {"IntfRef": arg_dict["port"]}

        return data

    @staticmethod
    def show_out_octets_data(arg_dict):
        data = {"IntfRef": arg_dict["port"]}

        return data

    @staticmethod
    def show_out_unicast_packets_data(arg_dict):
        data = {"IntfRef": arg_dict["port"]}

        return data

    @staticmethod
    def show_out_discard_packets_data(arg_dict):
        data = {"IntfRef": arg_dict["port"]}

        return data

    @staticmethod
    def show_out_error_packets_data(arg_dict):
        data = {"IntfRef": arg_dict["port"]}

        return data

    @staticmethod
    def show_in_broadcast_packets_data(arg_dict):
        data = {"IntfRef": arg_dict["port"]}

        return data

    @staticmethod
    def show_out_multicast_packets_data(arg_dict):
        data = {"IntfRef": arg_dict["port"]}

        return data

    @staticmethod
    def show_out_broadcast_packets_data(arg_dict):
        data = {"IntfRef": arg_dict["port"]}

        return data

    @staticmethod
    def show_64_bit_in_octets_data(arg_dict):
        data = {"IntfRef": arg_dict["port"]}

        return data

    @staticmethod
    def show_64_bit_in_unicast_packets_data(arg_dict):
        data = {"IntfRef": arg_dict["port"]}

        return data

    @staticmethod
    def show_64_bit_in_multicast_packets_data(arg_dict):
        data = {"IntfRef": arg_dict["port"]}

        return data

    @staticmethod
    def show_64_bit_in_broadcast_packets_data(arg_dict):
        data = {"IntfRef": arg_dict["port"]}

        return data

    @staticmethod
    def show_64_bit_out_octets_data(arg_dict):
        data = {"IntfRef": arg_dict["port"]}

        return data

    @staticmethod
    def show_64_bit_out_unicast_packets_data(arg_dict):
        data = {"IntfRef": arg_dict["port"]}

        return data

    @staticmethod
    def show_64_bit_out_multicast_packets_data(arg_dict):
        data = {"IntfRef": arg_dict["port"]}

        return data

    @staticmethod
    def show_64_bit_out_broadcast_packets_data(arg_dict):
        data = {"IntfRef": arg_dict["port"]}

        return data

    @staticmethod
    def test_data(arg_dict):
        pass

    @staticmethod
    def test1_data(arg_dict):
        pass

    @staticmethod
    def test2_data(arg_dict):
        pass

    @staticmethod
    def test3_data(arg_dict):
        pass
