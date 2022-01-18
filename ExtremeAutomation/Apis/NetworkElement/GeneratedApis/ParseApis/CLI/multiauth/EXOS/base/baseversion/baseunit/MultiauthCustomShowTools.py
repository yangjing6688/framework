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
        output = output.replace(";", "")

        web_auth = self.pw.get_value_by_offset(output, "NetLogin Authentication Mode", 5)
        dot1x = self.pw.get_value_by_offset(output, "NetLogin Authentication Mode", 7)
        mac_auth = self.pw.get_value_by_offset(output, "NetLogin Authentication Mode", 9)

        result = True if web_auth == "ENABLED" or dot1x == "ENABLED" or mac_auth == "ENABLED" else False

        return result, {"ret_state": "ENABLED" if result else "DISABLED",
                        "ret_dot1x_state": dot1x,
                        "ret_web_state": web_auth,
                        "ret_mac_state": mac_auth}

    def check_multiauth_session_timeout_default(self, output, args, **kwargs):
        output = output.replace(";", "")

        dot1x = self.pw.get_value_by_offset(output, "dot1x", 1)
        web_auth = self.pw.get_value_by_offset(output, "web-based", 1)
        mac_auth = self.pw.get_value_by_offset(output, "mac", 1)

        result = True if dot1x == "0" and web_auth == "0" and mac_auth == "0" else False

        return result, {"ret_dot1x_timeout": dot1x,
                        "ret_web_timeout": web_auth,
                        "ret_mac_timeout": mac_auth}

    def check_multiauth_idle_timeout_default(self, output, args, **kwargs):
        output = output.replace(";", "")

        dot1x = self.pw.get_value_by_offset(output, "dot1x", 2)
        web_auth = self.pw.get_value_by_offset(output, "web-based", 2)
        mac_auth = self.pw.get_value_by_offset(output, "mac", 2)

        result = True if dot1x == "300" and web_auth == "300" and mac_auth == "300" else False

        return result, {"ret_dot1x_timeout": dot1x,
                        "ret_web_timeout": web_auth,
                        "ret_mac_timeout": mac_auth}

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

    def check_multiauth_vlan_exists(self, output, args, **kwargs):
        multiauth_vlan = self.pw.get_value_by_offset(output, "NetLogin VLAN                :", 3)

        result = args["multiauth_vlan_name"].lower() in multiauth_vlan.lower()
        return result, {"ret_vlan": multiauth_vlan}

    def check_multiauth_session_timeout(self, output, args, **kwargs):
        dot1x_timeout = self.pw.get_value_by_offset(output, "dot1x", 1)
        web_timeout = self.pw.get_value_by_offset(output, "web-based", 1)
        mac_timeout = self.pw.get_value_by_offset(output, "mac", 1)

        result = True
        timeout = args["timeout"]
        if dot1x_timeout != timeout:
            self.logger.log_info("802.1X session timeout was " + dot1x_timeout + " not " + timeout + ".")
            result = False
        if web_timeout != timeout:
            self.logger.log_info("Web Auth session timeout was " + web_timeout + " not " + timeout + ".")
            result = False
        if mac_timeout != timeout:
            self.logger.log_info("MacAuth session timeout was " + mac_timeout + " not " + timeout + ".")
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
            result = True if int(dot1x_timeout) == int(args["timeout"]) else False

        return result, {"ret_dot1x_timeout": dot1x_timeout}

    def check_multiauth_session_timeout_web(self, output, args, **kwargs):
        web_timeout = self.pw.get_value_by_offset(output, "web-based", 1)

        result = True if web_timeout == args["timeout"] else False
        return result, {"ret_web_timeout": web_timeout}

    def check_multiauth_idle_timeout(self, output, args, **kwargs):
        dot1x_timeout = self.pw.get_value_by_offset(output, "dot1x", 2)
        web_timeout = self.pw.get_value_by_offset(output, "web-based", 2)
        mac_timeout = self.pw.get_value_by_offset(output, "mac", 2)

        result = True
        timeout = args["timeout"]
        if dot1x_timeout != timeout:
            self.logger.log_info("802.1X idle timeout was " + str(dot1x_timeout) + " not " + timeout + ".")
            result = False
        if web_timeout != timeout:
            self.logger.log_info("Web Auth idle timeout was " + str(web_timeout) + " not " + timeout + ".")
            result = False
        if mac_timeout != timeout:
            self.logger.log_info("MacAuth idle timeout was " + str(mac_timeout) + " not " + timeout + ".")
            result = False
        return result, {"ret_dot1x_timeout": dot1x_timeout,
                        "ret_web_timeout": web_timeout,
                        "ret_mac_timeout": mac_timeout}

    def check_multiauth_idle_timeout_mac(self, output, args, **kwargs):
        mac_timeout = self.pw.get_value_by_offset(output, "mac", 2)

        result = False
        if mac_timeout.isdigit() and args["timeout"].isdigit():
            result = True if int(mac_timeout) == int(args["timeout"]) else False

        return result, {"ret_mac_timeout": mac_timeout}

    def check_multiauth_idle_timeout_dot1x(self, output, args, **kwargs):
        dot1x_timeout = self.pw.get_value_by_offset(output, "dot1x", 2)

        result = False
        if dot1x_timeout.isdigit() and args["timeout"].isdigit():
            result = True if int(dot1x_timeout) == int(args["timeout"]) else False

        return result, {"ret_dot1x_timeout": dot1x_timeout}

    def check_multiauth_idle_timeout_web(self, output, args, **kwargs):
        web_timeout = self.pw.get_value_by_offset(output, "web-based", 2)

        result = False
        if web_timeout.isdigit() and args["timeout"].isdigit():
            result = True if int(web_timeout) == int(args["timeout"]) else False

        return result, {"ret_web_timeout": web_timeout}

    def check_multiauth_session_refresh(self, output, args, **kwargs):
        output = output.replace(";", "")
        refresh = self.pw.get_value_by_offset(output, "Netlogin Session-Refresh", 3)

        result = True if refresh.lower() == "enabled" else False
        return result, {"ret_session_refresh": refresh}

    def check_multiauth_session_refresh_interval(self, output, args, **kwargs):
        output = output.replace(";", "")
        minutes = self.pw.get_value_by_offset(output, "Netlogin Session-Refresh", 4)
        seconds = self.pw.get_value_by_offset(output, "Netlogin Session-Refresh", 6)

        if minutes.isdigit() and seconds.isdigit():
            x_int = minutes + ":" + seconds
            x = time.strptime(x_int, "%M:%S")
            current = datetime.timedelta(minutes=x.tm_min, seconds=x.tm_sec).total_seconds()

            result = True if int(current) == int(args["interval"]) else False
            return result, {"ret_refresh_interval": current}
        else:
            return False, {"ret_refresh_interval": minutes + ":" + seconds}

    def check_multiauth_idle_time(self, output, args, **kwargs):
        stations = self.pw.get_value_by_offset(output, "Station address  ", 6)
        stations = stations.split(" ")
        idle_times = self.pw.get_value_by_offset(output, "Idle time  ", 7)
        idle_times = idle_times.split(" ")

        current_idle = "5:55:55"
        for i, station in enumerate(stations):
            if station == args["station_address"]:
                current_idle = idle_times[i]

        x = time.strptime(current_idle, "%H:%M:%S")
        current_idle = datetime.timedelta(hours=x.tm_hour, minutes=x.tm_min, seconds=x.tm_sec).total_seconds()

        result = True if str(current_idle) == args["timer"] else False
        return result, {"ret_idle_time": current_idle}

    def check_multiauth_idle_time_greater(self, output, args, **kwargs):
        stations = self.pw.get_value_by_offset(output, "Station address  ", 6)
        idle_times = self.pw.get_value_by_offset(output, "Idle time  ", 7)
        status = self.pw.get_value_by_offset(output, "Auth status", 3)
        stations = stations.split(" ")
        idle_times = idle_times.split(" ")
        status = status.split(" ")

        current_idle = None
        for i, station in enumerate(stations):
            if station.lower() == args["station_address"].lower() and status[i] == "success":
                current_idle = idle_times[i]

        if current_idle is None:
            return False, None

        x = time.strptime(current_idle, "%H:%M:%S")
        current_idle = datetime.timedelta(hours=x.tm_hour, minutes=x.tm_min, seconds=x.tm_sec).total_seconds()
        self.logger.log_info(current_idle)

        result = True if int(current_idle) > int(args["timer"]) else False
        return result, {"ret_idle_time": current_idle}

    def check_multiauth_idle_time_less(self, output, args, **kwargs):
        stations = self.pw.get_value_by_offset(output, "Station address  ", 6)
        idle_times = self.pw.get_value_by_offset(output, "Idle time  ", 7)
        status = self.pw.get_value_by_offset(output, "Auth status", 3)
        stations = stations.split(" ")
        idle_times = idle_times.split(" ")
        status = status.split(" ")

        current_idle = None
        for i, station in enumerate(stations):
            if station == args["station_address"] and status[i] == "success":
                current_idle = idle_times[i]

        if current_idle is None:
            return False, {"ret_idle_time": current_idle}

        x = time.strptime(current_idle, "%H:%M:%S")
        current_idle = datetime.timedelta(hours=x.tm_hour, minutes=x.tm_min, seconds=x.tm_sec).total_seconds()

        result = True if int(current_idle) < int(args["timer"]) else False
        return result, {"ret_idle_time": current_idle}

    def check_multiauth_session_duration_greater(self, output, args, **kwargs):
        stations = self.pw.get_value_by_offset(output, "Station address", 6)
        session_duration = self.pw.get_value_by_offset(output, "Session duration", 7)
        status = self.pw.get_value_by_offset(output, "Auth status", 3)
        stations = stations.split(" ")
        session_duration = session_duration.split(" ")
        status = status.split(" ")

        current_duration = None
        for i, station in enumerate(stations):
            if station.lower() == args["station_address"].lower() and status[i] == "success":
                current_duration = session_duration[i]

        if current_duration is None:
            return False, {"ret_session_duration": current_duration}

        x = time.strptime(current_duration, "%H:%M:%S")
        current_duration = datetime.timedelta(hours=x.tm_hour, minutes=x.tm_min, seconds=x.tm_sec).total_seconds()

        result = True if int(current_duration) > int(args["timer"]) else False
        return result, {"ret_session_duration": current_duration}

    def check_multiauth_session_duration_less(self, output, args, **kwargs):
        stations = self.pw.get_value_by_offset(output, "Station address", 6)
        session_duration = self.pw.get_value_by_offset(output, "Session duration", 7)
        status = self.pw.get_value_by_offset(output, "Auth status", 3)
        stations = stations.split(" ")
        session_duration = session_duration.split(" ")
        status = status.split(" ")

        current_duration = None
        for i, station in enumerate(stations):
            if station.lower() == args["station_address"].lower() and status[i] == "success":
                current_duration = session_duration[i]

        if current_duration is None:
            return False, {"ret_session_duration": current_duration}

        x = time.strptime(current_duration, "%H:%M:%S")
        current_duration = datetime.timedelta(hours=x.tm_hour, minutes=x.tm_min, seconds=x.tm_sec).total_seconds()

        result = True if int(current_duration) < int(args["timer"]) else False
        return result, {"ret_session_duration": current_duration}

    @staticmethod
    def __generate_session_list(output):
        sessions = []

        # Take the output and and make list by splitting on two newlines
        split_output = re.split(r'(?:\r\n){2,}|\r{2,}|\n{2,}', output)
        # split_output = output.splitlines()
        # Iterate through the list and see if there are any sessions
        for line in split_output:
            # Search for session by looking for Station address in the string
            if "Station address" in line:
                session = MultiauthSession()
                # Clean up the string by removing all newlines and colons
                modified = re.sub("\r\n", " ", line)
                modified = re.sub("\n", " ", modified)
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
                session.termination_time = re.search('Termination time(.*)', modified).group(1).strip()
                # Create a new session object
                sessions.append(session)
        return sessions
