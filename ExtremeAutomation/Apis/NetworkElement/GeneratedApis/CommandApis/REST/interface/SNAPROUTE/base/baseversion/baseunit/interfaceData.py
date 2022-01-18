class InterfaceData(object):
    @staticmethod
    def set_ipv4_primary_addr_netmask_data(arg_dict):
        if arg_dict["interface"].isdigit():
            interface = "vlan" + arg_dict["interface"]
        else:
            interface = arg_dict["interface"]

        data = {"IntfRef": interface,
                "IpAddr": arg_dict["ip"] + "/" + arg_dict["prefix"]}

        return data

    @staticmethod
    def set_ipv4_primary_addr_prefix_data(arg_dict):
        if arg_dict["interface"].isdigit():
            interface = "vlan" + arg_dict["interface"]
        else:
            interface = arg_dict["interface"]

        data = {"IntfRef": interface,
                "IpAddr": arg_dict["ip"] + "/" + arg_dict["prefix"]}

        return data

    @staticmethod
    def delete_interface_data(arg_dict):
        if arg_dict["interface"].isdigit():
            interface = "vlan" + arg_dict["interface"]
        else:
            interface = arg_dict["interface"]

        data = {"IntfRef": interface}

        return data

    @staticmethod
    def show_info_data(arg_dict):
        if arg_dict["interface"].isdigit():
            interface = "vlan" + arg_dict["interface"]
        else:
            interface = arg_dict["interface"]

        data = {"IntfRef": interface}

        return data

    @staticmethod
    def show_all_data(arg_dict):
        pass
