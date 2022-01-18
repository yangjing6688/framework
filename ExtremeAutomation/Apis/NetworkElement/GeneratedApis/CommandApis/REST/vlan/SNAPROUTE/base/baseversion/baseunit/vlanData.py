class VlanData(object):
    @staticmethod
    def create_vlan_data(arg_dict):
        data = {"VlanId": int(arg_dict["vlan"])}

        return data

    @staticmethod
    def delete_vlan_data(arg_dict):
        data = {"VlanId": int(arg_dict["vlan"])}

        return data

    @staticmethod
    def set_egress_untagged_data(arg_dict):
        if isinstance(arg_dict["ports"], str):
            ports = [arg_dict["ports"]]
        else:
            ports = arg_dict["ports"]

        data = {"VlanId": int(arg_dict["vlan"]),
                "UntagIntfList": ports}

        return data

    @staticmethod
    def set_egress_tagged_data(arg_dict):
        if isinstance(arg_dict["port"], str):
            ports = [arg_dict["port"]]
        else:
            ports = arg_dict["port"]

        data = {"VlanId": int(arg_dict["vlan"]),
                "IntfList": ports}

        return data

    @staticmethod
    def show_all_info_data(arg_dict):
        pass

    @staticmethod
    def show_info_data(arg_dict):
        data = {"VlanId": int(arg_dict["vlan"])}

        return data
