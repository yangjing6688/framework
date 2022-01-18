from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.multiauth.base.MultiauthBaseCustomShowTools \
    import MultiauthBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.
import re
import time
import datetime
from ExtremeAutomation.Keywords.NetworkElementKeywords.Utils.NetworkElementMultiauthSession \
    import NetworkElementMultiauthSession as MultiauthSession


def create_instance(device):
    return MultiauthCustomShowTools(device)


class MultiauthCustomShowTools(MultiauthBaseCustomShowTools):
    def __init__(self, device):
        super(MultiauthCustomShowTools, self).__init__(device)

    def check_multiauth_state(self, output, args, **kwargs):
        returned_mode = self.pw.get_value_by_offset(output, "System mode", 3)
        returned_mode = returned_mode. replace(":", "")

        return "multi" == returned_mode, {"ret_state": returned_mode}

    def check_multiauth_session_exists(self, output, args, **kwargs):
        session_list = self.__generate_session_list(output)

        self.logger.log_info("------------- Looking for the following session -----------------")
        args["checksession"].display_session()

        for session in session_list:
            if args["checksession"].compare_sessions(session,
                                                     args.get("session_duration_operator", None),
                                                     args.get("idle_time_operator", None)):
                return True, True

        return False, None

    def check_multiauth_session_expired(self, output, args, **kwargs):
        session_list = self.__generate_session_list(output)

        self.logger.log_info("------------- Looking for the following session -----------------")
        args["checksession"].display_session()

        if len(session_list) == 0:
            return True, None
        for session in session_list:
            if args["checksession"].compare_sessions(session,
                                                     args.get("session_duration_operator", None),
                                                     args.get("idle_time_operator", None)):
                return True, True
        return False, None

    def check_multiauth_session_timeout(self, output, args, **kwargs):
        dot1x_timeout = self.pw.get_value_by_offset(output, "dot1x", 1)
        web_timeout = self.pw.get_value_by_offset(output, "pwa", 1)
        mac_timeout = self.pw.get_value_by_offset(output, "mac", 1)

        result = True
        timeout = args["timeout"]
        if dot1x_timeout != timeout:
            self.logger.log_info("802.1X session timeout was not " + timeout + ".")
            result = False
        if web_timeout != timeout:
            self.logger.log_info("Web Auth session timeout was not " + timeout + ".")
            result = False
        if mac_timeout != timeout:
            self.logger.log_info("MacAuth session timeout was not " + timeout + ".")
            result = False
        return result, {"ret_dot1x_timeout": dot1x_timeout,
                        "ret_web_timeout": web_timeout,
                        "ret_mac_timeout": mac_timeout}

    def check_multiauth_session_timeout_mac(self, output, args, **kwargs):
        mac_timeout = self.pw.get_value_by_offset(output, "mac", 1)

        result = False
        if mac_timeout.isdigit() and args["timeout"].isdigit():
            result = True if int(mac_timeout) == int(args["timeout"]) else False

        return result, {"ret_mac_timeout": mac_timeout}

    def check_multiauth_session_timeout_dot1x(self, output, args, **kwargs):
        dot1x_timeout = self.pw.get_value_by_offset(output, "dot1x", 1)

        result = False
        if dot1x_timeout.isdigit() and args["timeout"].isdigit():
            result = True if int(dot1x_timeout) == args["timeout"] else False

        return result, {"ret_dot1x_timeout": dot1x_timeout}

    def check_multiauth_session_timeout_web(self, output, args, **kwargs):
        web_timeout = self.pw.get_value_by_offset(output, "pwa", 1)

        result = False
        if web_timeout.isdigit() and args["timeout"].isdigit():
            result = True if int(web_timeout) == int(args["timeout"]) else False

        return result, {"ret_web_timeout": web_timeout}

    def check_multiauth_idle_timeout(self, output, args, **kwargs):
        dot1x_timeout = self.pw.get_value_by_offset(output, "dot1x", 1)
        web_timeout = self.pw.get_value_by_offset(output, "pwa", 1)
        mac_timeout = self.pw.get_value_by_offset(output, "mac", 1)

        result = True
        timeout = args["timeout"]
        if dot1x_timeout != timeout:
            self.logger.log_info("802.1X session timeout was not " + timeout + ".")
            result = False
        if web_timeout != timeout:
            self.logger.log_info("Web Auth session timeout was not " + timeout + ".")
            result = False
        if mac_timeout != timeout:
            self.logger.log_info("MacAuth session timeout was not " + timeout + ".")
            result = False
        return result, {"ret_dot1x_timeout": dot1x_timeout,
                        "ret_web_timeout": web_timeout,
                        "ret_mac_timeout": mac_timeout}

    def check_multiauth_idle_timeout_mac(self, output, args, **kwargs):
        mac_timeout = self.pw.get_value_by_offset(output, "mac", 1)

        result = False
        if mac_timeout.isdigit() and args["timeout"].isdigit():
            result = True if int(mac_timeout) == int(args["timeout"]) else False

        return result, {"ret_mac_timeout": mac_timeout}

    def check_multiauth_idle_timeout_dot1x(self, output, args, **kwargs):
        dot1x_timeout = self.pw.get_value_by_offset(output, "dot1x", 1)

        result = False
        if dot1x_timeout.isdigit() and args["timeout"].isdigit():
            result = True if int(dot1x_timeout) == int(args["timeout"]) else False

        return result, {"ret_dot1x_timeout": dot1x_timeout}

    def check_multiauth_idle_timeout_web(self, output, args, **kwargs):
        web_timeout = self.pw.get_value_by_offset(output, "pwa", 1)

        result = False
        if web_timeout.isdigit() and args["timeout"].isdigit():
            result = True if int(web_timeout) == int(args["timeout"]) else False

        return result, {"ret_web_timeout": web_timeout}

    def check_multiauth_idle_time(self, output, args, **kwargs):
        stations = self.pw.get_value_by_offset(output, "Station address  ", 6)
        stations = stations.split(" ")
        idle_times = self.pw.get_value_by_offset(output, "Idle time  ", 7)
        idle_times = idle_times.split(" ")

        current_idle = "5:55:55"
        for i, station in enumerate(stations):
            if station == args["station_address"]:
                current_idle = idle_times[i]

        x = time.strptime(current_idle, "%H,%M,%S")
        current_idle = datetime.timedelta(hours=x.tm_hour, minutes=x.tm_min, seconds=x.tm_sec).total_seconds()

        result = True if current_idle == args["timer"] else False
        return result, {"ret_idle_time": current_idle}

    def check_multiauth_idle_time_greater(self, output, args, **kwargs):
        stations = self.pw.get_value_by_offset(output, "Station address  ", 6)
        stations = stations.split(" ")
        idle_times = self.pw.get_value_by_offset(output, "Idle time  ", 7)
        idle_times = idle_times.split(" ")

        current_idle = "00:00:00"
        for i, station in enumerate(stations):
            if station == args["station_address"]:
                current_idle = idle_times[i]

        x = time.strptime(current_idle, "%H,%M,%S")
        current_idle = datetime.timedelta(hours=x.tm_hour, minutes=x.tm_min, seconds=x.tm_sec).total_seconds()

        result = True if current_idle > args["timer"] else False
        return result, {"ret_idle_time": current_idle}

    def check_multiauth_idle_time_less(self, output, args, **kwargs):
        stations = self.pw.get_value_by_offset(output, "Station address  ", 6)
        stations = stations.split(" ")
        idle_times = self.pw.get_value_by_offset(output, "Idle time  ", 7)
        idle_times = idle_times.split(" ")

        current_idle = "55:55:55"
        for i, station in enumerate(stations):
            if station == args["station_address"]:
                current_idle = idle_times[i]

        x = time.strptime(current_idle, "%H,%M,%S")
        current_idle = datetime.timedelta(hours=x.tm_hour, minutes=x.tm_min, seconds=x.tm_sec).total_seconds()

        result = True if current_idle < args["timer"] else False
        return result, {"ret_idle_time": current_idle}

    def check_multiauth_session_duration_greater(self, output, args, **kwargs):
        stations = self.pw.get_value_by_offset(output, "Station address  ", 6)
        stations = stations.split(" ")
        session_duration = self.pw.get_value_by_offset(output, "Session duration  ", 7)
        session_duration = session_duration.split(" ")

        current_duration = "55:55:55"
        for i, station in enumerate(stations):
            if station == args["station_address"]:
                current_duration = session_duration[i]

        x = time.strptime(current_duration, "%H,%M,%S")
        current_duration = datetime.timedelta(hours=x.tm_hour, minutes=x.tm_min, seconds=x.tm_sec).total_seconds()

        result = True if current_duration > args["timer"] else False
        return result, {"ret_session_duration": current_duration}

    def check_multiauth_session_duration_less(self, output, args, **kwargs):
        stations = self.pw.get_value_by_offset(output, "Station address  ", 6)
        stations = stations.split(" ")
        session_duration = self.pw.get_value_by_offset(output, "Session duration  ", 7)
        session_duration = session_duration.split(" ")

        current_duration = "55:55:55"
        for i, station in enumerate(stations):
            if station == args["station_address"]:
                current_duration = session_duration[i]

        x = time.strptime(current_duration, "%H,%M,%S")
        current_duration = datetime.timedelta(hours=x.tm_hour, minutes=x.tm_min, seconds=x.tm_sec).total_seconds()

        result = True if current_duration < args["timer"] else False
        return result, {"ret_session_duration": current_duration}

    @staticmethod
    def __trim_cli_output(output):
        if 'No entries found' in output:
            return []
        else:
            output = output.replace('Session timeout', 'Sessiontimeout')
            output = output.replace('in progress', 'in-progress')
            output = output.replace('radius snooping', 'radius-snooping')
            output = output.replace('Not Terminated', 'not-terminated')
            output = output.replace('Auth Server IP', 'Server address')
            split_output = output.split('-----------------------------------------')
            config_blocks = split_output[1].split('\r\n\r\n\r\n')
        return config_blocks

    @staticmethod
    def __generate_session_list(output):
        sessions = []

        # Take the output and and make list by slpiting on two newlines
        split_output = re.split(r'(?:\r\n){2,}|\r{2,}|\n{2,}', output)

        # Iterate through the list and see if there are any sessions
        for line in split_output:
            # Search for session by looking for Station address in the string
            if "Station address" in line:
                session = MultiauthSession()
                # Clean up the string by removing all newlines and colons
                modified = re.sub("\r\n", " ", line)
                modified = re.sub(": ", " ", modified)
                # Search for the data between individual items
                session.port = re.search('Port(.*)Station address', modified).group(1).strip()
                session.station_address = re.search('Station address(.*)Auth status', modified).group(1).strip()
                session.auth_status = re.search('Auth status(.*)Last attempt', modified).group(1).strip()
                session.last_attempt = re.search('Last attempt(.*)Agent type', modified).group(1).strip()
                session.agent_type = re.search('Agent type(.*)Session applied', modified).group(1).strip()
                session.session_applied = re.search('Session applied(.*)Server type', modified).group(1).strip()
                session.server_type = re.search('Server type(.*)VLAN-Tunnel-Attr', modified).group(1).strip()
                session.vlan_tun_attr = re.search('VLAN-Tunnel-Attr(.*)Policy index', modified).group(1).strip()
                session.policy_index = re.search('Policy index(.*)Policy name', modified).group(1).strip()
                session.policy_name = re.search('Policy name(.*)Session timeout', modified).group(1).strip()
                session.session_timeout = re.search('Session timeout(.*)Session duration', modified).group(1).strip()
                session.session_duration = re.search('Session duration(.*)Idle timeout', modified).group(1).strip()
                session.idle_timeout = re.search('Idle timeout(.*)Idle time ', modified).group(1).strip()
                session.idle_time = re.search('Idle time (.*)Termination time', modified).group(1).strip()
                session.termination_time = re.search('Termination time(.*)Auth Server IP', modified).group(1).strip()
                session.auth_server_ip = re.search('Auth Server IP(.*)', modified).group(1).strip()
                # Create a new session object
                sessions.append(session)
        return sessions
