import re
from ExtremeAutomation.Library.Logger.Logger import Logger
from ExtremeAutomation.Library.Device.Common.Agents.AgentConstants import AgentConstants
from ExtremeAutomation.Library.Device.NetworkElement.Constants.NetworkElementConstants import \
    NetworkElementConstants


class NetworkElementUtils(object):
    @staticmethod
    def get_device_info(dev_os, dev_platform, dev_version, dev_unit):
        """
        Takes a device_type string (ex. "eos" or "exos") and returns the OS, platform, login prompt, pass prompt, and
        main prompt for the corresponding device type.
        """
        end_of_line = '\n'

        formatted_dev_os = dev_os.replace("_", "").upper()

        if formatted_dev_os == NetworkElementConstants.OS_EOS:
            device_os = NetworkElementConstants.OS_EOS
            device_platform = dev_platform if dev_platform is not None else NetworkElementConstants.PLATFORM_EOS_BASE
            login_prompt = "Username:"
            pass_prompt = "Password:"
            main_prompt = "->"
        elif formatted_dev_os == NetworkElementConstants.OS_EXOS:
            device_os = NetworkElementConstants.OS_EXOS
            device_platform = dev_platform if dev_platform is not None else NetworkElementConstants.PLATFORM_EXOS_BASE
            login_prompt = "login:"
            pass_prompt = "password:"
            main_prompt = "# "
        elif formatted_dev_os == NetworkElementConstants.OS_LINUX.upper():
            device_os = NetworkElementConstants.OS_LINUX
            device_platform = dev_platform if dev_platform is not None else NetworkElementConstants.PLATFORM_LINUX_BASE
            login_prompt = "login as:"
            pass_prompt = "password:"
            main_prompt = "#"
        elif formatted_dev_os == NetworkElementConstants.OS_EXTR_WIRELESS:
            device_os = NetworkElementConstants.OS_EXTR_WIRELESS
            device_platform = (dev_platform if dev_platform is not None
                               else NetworkElementConstants.PLATFORM_EXTR_WIRELESS_BASE)
            login_prompt = "Username:"
            pass_prompt = "Password:"
            main_prompt = "#"
        elif formatted_dev_os == NetworkElementConstants.OS_SNAP_ROUTE:
            device_os = NetworkElementConstants.OS_SNAP_ROUTE
            device_platform = (dev_platform if dev_platform is not None
                               else NetworkElementConstants.PLATFORM_SNAP_ROUTE_BASE)
            login_prompt = "Username:"
            pass_prompt = "password:"
            main_prompt = "$"
        elif formatted_dev_os == NetworkElementConstants.OS_VOSS:
            device_os = NetworkElementConstants.OS_VOSS
            device_platform = dev_platform if dev_platform is not None else NetworkElementConstants.PLATFORM_VOSS_BASE
            login_prompt = "Login:"
            pass_prompt = "Password:"
            main_prompt = "#"
        elif formatted_dev_os == NetworkElementConstants.OS_ALPHA:
            device_os = NetworkElementConstants.OS_ALPHA
            device_platform = dev_platform if dev_platform is not None else NetworkElementConstants.PLATFORM_ALPHA_BASE
            login_prompt = "User:"
            pass_prompt = "Password:"
            main_prompt = "#"
        elif formatted_dev_os == NetworkElementConstants.OS_EOS_STACKS:
            device_os = NetworkElementConstants.OS_EOS_STACKS
            device_platform = dev_platform if dev_platform is not None \
                else NetworkElementConstants.PLATFORM_EOS_STACKS_BASE
            login_prompt = "Username:"
            pass_prompt = "Password:"
            main_prompt = "->"
        elif formatted_dev_os == NetworkElementConstants.OS_BOSS:
            device_os = NetworkElementConstants.OS_BOSS
            device_platform = dev_platform if dev_platform is not None else NetworkElementConstants.PLATFORM_BOSS_BASE
            login_prompt = "login as:"
            pass_prompt = "password:"
            main_prompt = "#"
        elif formatted_dev_os == NetworkElementConstants.OS_SLX:
            device_os = NetworkElementConstants.OS_SLX
            device_platform = dev_platform if dev_platform is not None else NetworkElementConstants.PLATFORM_BOSS_BASE
            login_prompt = "login:"
            pass_prompt = "Password:"
            main_prompt = "#"
        elif formatted_dev_os == NetworkElementConstants.OS_VDX:
            device_os = NetworkElementConstants.OS_VDX
            device_platform = dev_platform if dev_platform is not None else NetworkElementConstants.PLATFORM_BOSS_BASE
            login_prompt = "login:"
            pass_prompt = "Password:"
            main_prompt = "#"
        elif formatted_dev_os == NetworkElementConstants.OS_ICX:
            device_os = NetworkElementConstants.OS_ICX
            device_platform = dev_platform if dev_platform is not None else NetworkElementConstants.PLATFORM_BOSS_BASE
            login_prompt = "User Name:"
            pass_prompt = "Password:"
            main_prompt = ">"
        elif formatted_dev_os == NetworkElementConstants.OS_MLX:
            device_os = NetworkElementConstants.OS_MLX
            device_platform = dev_platform if dev_platform is not None else NetworkElementConstants.PLATFORM_BOSS_BASE
            login_prompt = "User Name:"
            pass_prompt = "Password:"
            main_prompt = ">"
        elif formatted_dev_os == NetworkElementConstants.OS_EXOS_RO:
            device_os = NetworkElementConstants.OS_EXOS
            device_platform = dev_platform if dev_platform is not None else NetworkElementConstants.PLATFORM_EXOS_BASE
            login_prompt = "login:"
            pass_prompt = "password:"
            main_prompt = "> "
        elif formatted_dev_os == NetworkElementConstants.OS_BOSS_RADIUS:
            device_os = NetworkElementConstants.OS_BOSS
            device_platform = dev_platform if dev_platform is not None else NetworkElementConstants.PLATFORM_BOSS_BASE
            login_prompt = "Username:"
            pass_prompt = "Password:"
            main_prompt = "#"
        else:
            logger = Logger()

            logger.log_info("Unknown operating system provided.")
            logger.log_info("Provided operating system: " + dev_os)
            logger.log_info("Supported operating systems:\n    - " +
                            "\n    - ".join([getattr(NetworkElementConstants, i) for i in dir(NetworkElementConstants)
                                             if i.startswith("OS_")]))

            raise ValueError("Operating system " + dev_os + " was not found in the list of supported operating "
                                                            "systems.")

        device_version = dev_version if dev_version is not None else NetworkElementConstants.VERSION_BASE
        device_unit = dev_unit if dev_unit is not None else NetworkElementConstants.UNIT_BASE

        device_info = {"device_os": device_os,
                       "device_platform": device_platform,
                       "device_version": device_version,
                       "device_unit": device_unit,
                       "login_prompt": login_prompt,
                       "pass_prompt": pass_prompt,
                       "main_prompt": main_prompt,
                       "end_of_line": end_of_line
                       }

        return device_info

    @staticmethod
    def get_connection_method(connection_method, port):
        """
        Takes a connection method string (ex. "telnet" or "ssh") and returns the connection method constant and default
        port used by the protocol.
        """
        if connection_method.lower() == AgentConstants.TYPE_TELNET:
            connection_method = AgentConstants.TYPE_TELNET
            port = port if port is not None else AgentConstants.TELNET_PORT
        elif connection_method.lower() == AgentConstants.TYPE_SSH:
            connection_method = AgentConstants.TYPE_SSH
            port = port if port is not None else AgentConstants.SSH_PORT
        elif connection_method.lower() == AgentConstants.TYPE_JSON:
            connection_method = AgentConstants.TYPE_JSON
            port = port if port is not None else "1"
        elif connection_method.lower() == AgentConstants.TYPE_REST:
            connection_method = AgentConstants.TYPE_REST
            port = port if port is not None else AgentConstants.REST_PORT
        elif connection_method.lower() == AgentConstants.TYPE_SNMP:
            connection_method = AgentConstants.TYPE_SNMP
            port = port if port is not None else AgentConstants.SNMP_PORT
        elif connection_method.lower() == AgentConstants.TYPE_JSON_RPC:
            connection_method = AgentConstants.TYPE_JSON_RPC
            port = port if port is not None else "80"
        elif connection_method.lower() == AgentConstants.TYPE_CONSOLE:
            port = port
        # If an unknown connection method is received default to telnet.
        else:
            connection_method = AgentConstants.TYPE_TELNET
            port = port if port != -1 else AgentConstants.TELNET_PORT
        return connection_method, port

    @staticmethod
    def get_device_names_from_variables(variables_dict, var_prefix):
        """Returns a list of all devices with the same var_prefix."""
        name_regex = "^" + var_prefix + "[0-9]+$"
        index_regex = "[0-9]+$"

        names = [key for key in variables_dict.keys() if len(re.findall(name_regex, key)) == 1]
        indexes = [re.search(index_regex, i).group() for i in names]

        return [var_prefix + i for i in sorted(indexes, key=int)]

    @staticmethod
    def get_device_number(variables, search_name):
        """
        Returns the device number.
        Ex:
        For netelem2 the device number is "2"
        """
        for key in variables:
            if isinstance(variables[key], dict):
                try:
                    if variables[key]["name"] == search_name:
                        return key
                except KeyError:
                    pass

        raise ValueError("No device's with the name " + search_name + " found.")

    @staticmethod
    def get_snmp_info(variables, netelem):
        """Returns a dictionary of the snmp settings for the Network Element."""
        try:
            netelem_vars = variables[netelem]["snmp_info"]
            snmp_info = {
                "snmp_version": netelem_vars.get("snmp_version", None),
                "snmp_community_name": netelem_vars.get("snmp_community_name", None),
                "snmp_user_name": netelem_vars.get("snmp_user_name", None),
                "snmp_auth_protocol": netelem_vars.get("snmp_auth_protocol", None),
                "snmp_auth_password": netelem_vars.get("snmp_auth_password", None),
                "snmp_privacy_protocol": netelem_vars.get("snmp_privacy_protocol", None),
                "snmp_privacy_password": netelem_vars.get("snmp_privacy_password", None)
            }
        except KeyError:
            snmp_info = None

        return snmp_info
