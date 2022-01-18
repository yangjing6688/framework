class VlanData(object):
    @staticmethod
    def create_vlan_data(arg_dict):

        data = {'openconfig-vlan:vlan': [{'config': {'vlan-id': int(arg_dict["vlan"])}}]}

        return data

    @staticmethod
    def delete_vlan_data(arg_dict):
        pass

    @staticmethod
    def show_info_data(arg_dict):
        pass

    @staticmethod
    def show_all_info_data(arg_dict):
        pass
