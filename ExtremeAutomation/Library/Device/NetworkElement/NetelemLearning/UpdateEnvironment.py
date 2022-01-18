from ExtremeAutomation.Library.ParsingHelper.InspectionToolkit import InspectionToolkit
from ExtremeAutomation.Keywords.Utils.DeviceCollectionManager import DeviceCollectionManager
from ExtremeAutomation.Library.Device.NetworkElement.Constants.NetworkElementConstants import NetworkElementConstants


class UpdateEnvironment(object):
    def update_environment(self, device_name, system, elem_var_dict):
        """
        This function is used to inject information from the built system into the
        currently running tests variable dictionary.
        """
        elem_var_dict["mac_addr"] = system.mac_addr
        self.add_port_macs(system, elem_var_dict)
        elem_var_dict["all_ports_var"] = self.generate_all_ports_variable(device_name, system, elem_var_dict)

        return elem_var_dict

    def add_port_macs(self, system, elem_var_dict):
        """
        This function adds the mac address for each port into the devices variable dictioanry.
        """
        for key in elem_var_dict:
            if isinstance(elem_var_dict[key], dict):
                if "ifname" in elem_var_dict[key]:
                    port_obj = self.find_port_info(system, elem_var_dict[key]["ifname"])
                    elem_var_dict[key]["mac_addr"] = port_obj.mac_addr if port_obj is not None else "None"
                else:
                    self.add_port_macs(system, elem_var_dict[key])

    @staticmethod
    def find_port_info(system, port_string):
        """
        This function finds each port within the generated system. Each component in the system
        may have ports so it searches each component recursively until all ports are found.
        """
        def recursive_port_search(_port_string, _components):
            _component = None
            for _component in _components:
                for _port in _component.ports:
                    if _port.port_string == _port_string:
                        return _port
            if _component is not None and hasattr(_component, "components"):
                return recursive_port_search(port_string, _component.components)

        for port in system.ports:
            if port.port_string == port_string:
                return port
        return recursive_port_search(port_string, system.components)

    @staticmethod
    def generate_all_ports_variable(device_name, system, elem_var_dict):
        """
        Keyword Arguments:
        [device_names] - The Device(s) for which to create the all_ports variable.

        Creates a variable all_ports, for all ports applicable to the test environment.
        """
        device = DeviceCollectionManager().get_device(device_name)
        it = InspectionToolkit(device)
        all_ports_var = []

        def recursive_port_search(_components):
            _component = None
            for _component in _components:
                for _port in _component.ports:
                    all_ports_var.append(_port.port_string)
            if _component is not None and hasattr(_component, "components"):
                return recursive_port_search(_component.components)

        for port in system.ports:
            all_ports_var.append(port.port_string)
        recursive_port_search(system.components)

        if device.oper_sys == NetworkElementConstants.OS_EOS or \
                device.oper_sys == NetworkElementConstants.OS_EOS_STACKS:
            all_ports_var = ";".join(all_ports_var)
        if device.oper_sys == NetworkElementConstants.OS_EXOS:
            all_ports_var = ",".join(all_ports_var)
        if device.oper_sys == NetworkElementConstants.OS_VOSS:
            all_ports_var = ",".join(all_ports_var)

        ports = it.get_port_parser_obj(all_ports_var)
        if "management" in elem_var_dict:
            mgmt_port = ""
            if "ifname" in elem_var_dict["management"]:
                mgmt_port = elem_var_dict["management"]["ifname"]
            elif "port_a" in elem_var_dict["management"]:
                mgmt_port = elem_var_dict["management"]["port_a"]["ifname"]
            if mgmt_port:
                mgmt_port = it.get_port_parser_obj(mgmt_port)
                if ports.is_port_on_list(mgmt_port):
                    ports.subtract(mgmt_port)

        newlist = ports.collapse_port_list()
        return newlist
