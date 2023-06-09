from ExtremeAutomation.Library.Logger.Logger import Logger
from ExtremeAutomation.Library.Utils.NetworkElementUtils import NetworkElementUtils
from ExtremeAutomation.Library.Utils.RobotUtils import RobotUtils


class NetworkElementListUtils(object):
    def __init__(self):
        self.logger = Logger()

    def create_list_of_network_element_names(self):
        """
        Returns a list of all Network Element names from all Test Variables.
        """
        netelem_name_list = []
        variables = RobotUtils.get_variables(no_decoration=True)
        netelems = NetworkElementUtils.get_device_names_from_variables(variables, "netelem")

        for netelem in netelems:
            netelem_name = None

            try:
                netelem_name = variables[netelem]["name"]

            except KeyError:
                if netelem_name is None:
                    self.logger.log_info("${" + netelem + ".name} variable not present in testbed resource file.")

            if netelem_name is not None:
                netelem_name_list.append(netelem_name)

        if len(netelem_name_list) == 0:
            self.logger.log_info("No Network Elements found in Test Environment File.")

        return netelem_name_list

    def create_list_of_network_elements(self):
        """
        Returns a list of all Network Elements from all Test Variables.
        """
        variables = RobotUtils.get_variables(no_decoration=True)
        netelem_list = NetworkElementUtils.get_device_names_from_variables(variables, "netelem")

        if len(netelem_list) == 0:
            self.logger.log_info("No Network Elements found in Test Environment File.")

        return netelem_list

    def create_list_of_all_tgen_ports(self):
        """
        Returns a list of all Traffic Generator ports from all Test Variables.
        """
        tgen_portlist = []
        variables = RobotUtils.get_variables(no_decoration=True)
        netelems = NetworkElementUtils.get_device_names_from_variables(variables, "netelem")

        for netelem in netelems:
            try:
                portname_list = variables["tgen_ports"][netelem]
                self.logger.log_info("Traffic Generator ports were found for " + netelem + ".")
                for port in portname_list:
                    port_dict = {"tgen_name": portname_list[port]["tgen_name"],
                                 "ifname": portname_list[port]["ifname"]}
                    if "phy_mode" in portname_list[port]:
                        port_dict["phy_mode"] = portname_list[port]["phy_mode"]
                    tgen_portlist.append(port_dict)

            except KeyError:
                self.logger.log_info("No Traffic Generator ports found for " + netelem + ".")

        self.logger.log_info("Traffic Generator Portlist created.")

        return tgen_portlist

    def create_list_of_netelem_tgen_ports(self, netelem_number):
        """
        Returns a list of all Traffic Generator ports for a given Network Element.
        """
        tgen_portlist = []
        variables = RobotUtils.get_variables(no_decoration=True)
        portname_list = variables[netelem_number]["tgen"]

        for port in portname_list:
            tgen_portlist.append(portname_list[port]["ifname"])

        if len(tgen_portlist) == 0:
            self.logger.log_info("No Traffic Generator port found in Test Environment File.")

        return tgen_portlist

    def create_list_of_netelem_isl_ports(self, netelem_number):
        """
        Returns a list of all Inter-switch Links ports for a given Network Element.
        """
        isl_portlist = []
        variables = RobotUtils.get_variables(no_decoration=True)
        portname_list = variables[netelem_number]["isl"]

        for port in portname_list:
            isl_portlist.append(portname_list[port]["ifname"])

        if len(isl_portlist) == 0:
            self.logger.log_info("No ISL ports found in Test Environment File.")

        return isl_portlist

