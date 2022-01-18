import re
from ExtremeAutomation.Library.Logger.Logger import Logger
from ExtremeAutomation.Library.Device.Common.Agents.AgentConstants import AgentConstants
from ExtremeAutomation.Library.Device.EndsystemElement.Constants.EndsystemElementConstants \
    import EndsystemElementConstants


class EndsystemElementUtils(object):
    @staticmethod
    def get_device_info(dev_os, dev_platform, dev_version, dev_unit):
        """
        Takes a device_type string (ex. "eos" or "exos") and returns the OS, platform, login prompt, pass prompt, and
        main prompt for the corresponding device type.
        """
        end_of_line = '\n'
        formatted_dev_os = dev_os.replace("_", "").upper()
        slow_login = 0

        if formatted_dev_os == EndsystemElementConstants.OS_LINUX.upper():
            device_os = EndsystemElementConstants.OS_LINUX
            device_platform = dev_platform if dev_platform is not None \
                else EndsystemElementConstants.PLATFORM_LINUX_BASE
            login_prompt = "login as:"
            pass_prompt = "password:"
            main_prompt = "$"
        elif formatted_dev_os == EndsystemElementConstants.OS_EMC:
            device_os = EndsystemElementConstants.OS_EMC
            device_platform = dev_platform if dev_platform is not None else EndsystemElementConstants.PLATFORM_EMC_BASE
            login_prompt = ""
            pass_prompt = ""
            main_prompt = ""
        elif formatted_dev_os == EndsystemElementConstants.OS_GIM:
            device_os = EndsystemElementConstants.OS_GIM
            device_platform = dev_platform if dev_platform is not None else EndsystemElementConstants.PLATFORM_GIM_BASE
            login_prompt = ""
            pass_prompt = ""
            main_prompt = ""
        elif formatted_dev_os == EndsystemElementConstants.OS_CCSERVER.upper():
            device_os = EndsystemElementConstants.OS_CCSERVER
            device_platform = dev_platform if dev_platform is not None \
                else EndsystemElementConstants.PLATFORM_LINUX_BASE
            login_prompt = ""
            pass_prompt = ""
            main_prompt = ""
        elif formatted_dev_os == EndsystemElementConstants.OS_ECIQ.upper():
            device_os = EndsystemElementConstants.OS_ECIQ
            device_platform = dev_platform if dev_platform is not None \
                else EndsystemElementConstants.PLATFORM_ECIQ_BASE
            login_prompt = ""
            pass_prompt = ""
            main_prompt = ""
        # If an unknown device type is received default to EOS.
        else:
            device_os = EndsystemElementConstants.OS_WINDOWS
            device_platform = EndsystemElementConstants.PLATFORM_WINDOWS_BASE
            login_prompt = "login:"
            pass_prompt = "password:"
            main_prompt = ">"
            end_of_line = "\r\n"
            slow_login = 20

        device_version = dev_version if dev_version is not None else EndsystemElementConstants.VERSION_BASE
        device_unit = dev_unit if dev_unit is not None else EndsystemElementConstants.UNIT_BASE

        device_info = {"device_os": device_os,
                       "device_platform": device_platform,
                       "device_version": device_version,
                       "device_unit": device_unit,
                       "login_prompt": login_prompt,
                       "pass_prompt": pass_prompt,
                       "main_prompt": main_prompt,
                       "end_of_line": end_of_line,
                       "slow_login": slow_login
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
        elif connection_method.lower() == AgentConstants.TYPE_NORTHBOUND:
            connection_method = AgentConstants.TYPE_NORTHBOUND
            port = port if port is not None else AgentConstants.NORTHBOUND_PORT
        elif connection_method.lower() == AgentConstants.TYPE_REST:
            connection_method = AgentConstants.TYPE_REST
            port = port if port is not None else AgentConstants.REST_PORT
        elif connection_method.lower() == AgentConstants.TYPE_XMC_REST:
            connection_method = AgentConstants.TYPE_XMC_REST
            port = port if port is not None else AgentConstants.XMC_REST_PORT
        else:
            connection_method = AgentConstants.TYPE_TELNET
            port = port if port != -1 else AgentConstants.TELNET_PORT
        return connection_method, port

    @staticmethod
    def update_device_class(device, dev_os, dev_platform=None, dev_version=None, dev_unit=None):
        """
        Logs an error message if the EndSystem OS is not Windows or Linux.

        Note: Currently these are the only supported endsystem OSes.
        """
        if not (dev_os.upper() == EndsystemElementConstants.OS_LINUX or
                dev_os.upper() == EndsystemElementConstants.OS_WINDOWS):
            logger = Logger()
            logger.log_trace("!!! OS not supported " + dev_os + " !!!")

    @staticmethod
    def remove_control_characters(output):
        """Removes any control characters from the provided output."""
        c = ["[m", "[1m", "\133", "\135", " \176", "\176"]
        for i in c:
            output = output.replace(i, "")
        output = re.sub(r'[^a-zA-Z0-9@ ]', r'', output)
        output = output.replace(' ', '')
        return output
