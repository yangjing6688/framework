class LldpData(object):
    @staticmethod
    def enable_port_both_data(arg_dict):

        data = {'openconfig-lldp:lldp': {
            'interfaces': {'interface': [{'config': {'name': arg_dict["port"], 'enabled': True}}]}}}

        return data

    @staticmethod
    def disable_port_data(arg_dict):

        data = {'openconfig-lldp:lldp': {
            'interfaces': {'interface': [{'config': {'name': arg_dict["port"], 'enabled': False}}]}}}

        return data

    @staticmethod
    def show_port_status_data(arg_dict):
        pass

    @staticmethod
    def show_info_data(arg_dict):
        pass

    @staticmethod
    def show_remote_info_data(arg_dict):
        pass

    @staticmethod
    def show_neighbors_data(arg_dict):
        pass
