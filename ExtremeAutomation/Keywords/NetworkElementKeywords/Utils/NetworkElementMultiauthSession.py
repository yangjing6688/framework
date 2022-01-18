import re
from ExtremeAutomation.Library.Logger.Logger import Logger


class NetworkElementMultiauthSession:
    """This Class is to create a multiauth session object"""

    sessionCount = 0

    def __init__(self):
        self.port = None
        self.station_address = None
        self.auth_status = None
        self.last_attempt = None
        self.agent_type = None
        self.session_applied = None
        self.server_type = None
        self.vlan_tun_attr = None
        self.policy_index = None
        self.policy_name = None
        self.session_timeout = None
        self.session_duration = None
        self.idle_timeout = None
        self.idle_time = None
        self.termination_time = None
        self.auth_server_ip = None
        self.logger = Logger()

        NetworkElementMultiauthSession.sessionCount += 1

    @staticmethod
    def display_count():
        """
        Logs the session count for all current sessions.
        """
        Logger().log_info("Total number of sessions: %d" % NetworkElementMultiauthSession.sessionCount)

    def display_session(self):
        """
        Logs the current session, formatted to match device output.
        """
        self.logger.log_info("{:<18} {:<1} {:<16} {:<22} {:<1} {:<18}".format("Port", ":", str(self.port),
                                                                              "Station address", ":",
                                                                              str(self.station_address)) + "\n"
                             "{:<18} {:<1} {:<16} {:<22} {:<1} {:<18}".format("Auth status", ":", str(self.auth_status),
                                                                              "Last attempt", ":",
                                                                              str(self.last_attempt)) + "\n"
                             "{:<18} {:<1} {:<16} {:<22} {:<1} {:<18}".format("Agent type", ":", str(self.agent_type),
                                                                              "Session applied", ":",
                                                                              str(self.session_applied)) + "\n"
                             "{:<18} {:<1} {:<16} {:<22} {:<1} {:<18}".format("Server type", ":", str(self.server_type),
                                                                              "VLAN tunnel attribute", ":",
                                                                              str(self.vlan_tun_attr)) + "\n"
                             "{:<18} {:<1} {:<16} {:<22} {:<1} {:<18}".format("Policy index", ":",
                                                                              str(self.policy_index), "Policy Name",
                                                                              ":", str(self.policy_name)) + "\n"
                             "{:<18} {:<1} {:<16} {:<22} {:<1} {:<18}".format("Session timeout", ":",
                                                                              str(self.session_timeout),
                                                                              "Session duration", ":",
                                                                              str(self.session_duration)) + "\n"
                             "{:<18} {:<1} {:<16} {:<22} {:<1} {:<18}".format("Idle timeout", ":",
                                                                              str(self.idle_timeout), "Idle time", ":",
                                                                              str(self.idle_time)) + "\n"
                             "{:<18} {:<1} {:<16} {:<22} {:<1} {:<18}".format("Termination time ", ":",
                                                                              str(self.termination_time),
                                                                              "Auth server IP", ":",
                                                                              str(self.auth_server_ip)) + "\n")

    @staticmethod
    def convert_dhms(dhms):
        """
        Convert datetimes to seconds.
        """
        if ":" not in dhms:
            return dhms
        elif "," not in dhms:
            datetimesplit = re.sub(":", " ", dhms)
            datetimesplit = re.split(" ", datetimesplit)
            seconds = 0
            seconds += int(datetimesplit[0]) * 3600  # Convert Hours to seconds
            seconds += int(datetimesplit[1]) * 60  # Convert Minuets to seconds
            seconds += int(datetimesplit[2])  # Do nothing to the seconds
            return seconds
        else:
            datetimesplit = re.sub(",", " ", dhms)
            datetimesplit = re.sub(":", " ", datetimesplit)
            datetimesplit = re.split(" ", datetimesplit)
            seconds = 0
            seconds += int(datetimesplit[0]) * 86400  # Convert Days to seconds
            seconds += int(datetimesplit[1]) * 3600  # Convert Hours to seconds
            seconds += int(datetimesplit[2]) * 60  # Convert Minuets to seconds
            seconds += int(datetimesplit[3])  # Do nothing to the seconds
            return seconds

    def compare_sessions(self, comp_session, session_duration_operator=None, idle_time_operator=None):
        """
        Compares all fields in the session and returns True if all are matching.
        """
        if self.port is not None:
            if self.port not in comp_session.port:
                return False

        if self.station_address is not None:
            if self.station_address.lower() not in comp_session.station_address.lower():
                return False

        if self.auth_status is not None:
            if self.auth_status.lower() not in comp_session.auth_status.lower():
                return False

        if self.last_attempt is not None:
            if self.last_attempt.lower() not in comp_session.last_attempt.lower():
                return False

        if self.agent_type is not None:
            if self.agent_type.lower() not in comp_session.agent_type.lower():
                return False

        if self.session_applied is not None:
            if self.session_applied.lower() not in comp_session.session_applied.lower():
                return False

        if self.server_type is not None:
            if self.server_type.lower() not in comp_session.server_type.lower():
                return False

        if self.vlan_tun_attr is not None:
            if self.vlan_tun_attr.lower() not in comp_session.vlan_tun_attr.lower():
                return False

        if self.policy_index is not None:
            if self.policy_index not in comp_session.policy_index:
                return False

        if self.policy_name is not None:
            if self.policy_name.lower() not in comp_session.policy_name.lower():
                return False

        if self.session_duration is not None:
            if session_duration_operator == ">":
                if self.convert_dhms(self.session_duration) > self.convert_dhms(comp_session.session_duration):
                    return False

            elif session_duration_operator == "<":
                if self.convert_dhms(self.session_duration) < self.convert_dhms(comp_session.session_duration):
                    return False

            else:
                if session_duration_operator != "=" and session_duration_operator is not None:
                    self.logger.log_info("Unknown operator " + session_duration_operator + ". Defaulting to \'=\'.")

                if self.convert_dhms(self.session_duration) != self.convert_dhms(comp_session.session_duration):
                    return False

        if self.idle_timeout is not None:
            if self.idle_timeout not in comp_session.idle_timeout:
                return False

        if self.idle_time is not None:
            if idle_time_operator == ">":
                if self.convert_dhms(self.idle_time) > self.convert_dhms(comp_session.idle_time):
                    return False

            elif idle_time_operator == "<":
                if self.convert_dhms(self.idle_time) < self.convert_dhms(comp_session.idle_time):
                    return False

            else:
                if idle_time_operator != "=" and idle_time_operator is not None:
                    self.logger.log_info("Unknown operator " + idle_time_operator + ". Defaulting to \'=\'.")

                if self.convert_dhms(self.idle_time) != self.convert_dhms(comp_session.idle_time):
                    return False

        if self.termination_time is not None:
            if self.termination_time not in comp_session.termination_time:
                return False

        if self.auth_server_ip is not None:
            if self.auth_server_ip not in comp_session.auth_server_ip:
                return False
        self.logger.log_info("----------------- Found a matching session ----------------------")
        comp_session.display_session()
        return True

    @staticmethod
    def create_session_object(port, station_address, auth_status, last_attempt, agent_type, session_applied,
                              server_type, vlan_tun_attr, policy_index, policy_name, session_timeout,
                              session_duration, idle_timeout, idle_time, termination_time, auth_server_ip):
        """Returns a multi-auth session object using the supplied values."""
        session = NetworkElementMultiauthSession()

        session.port = port
        session.station_address = station_address
        session.auth_status = auth_status
        session.last_attempt = last_attempt
        session.agent_type = agent_type
        session.session_applied = session_applied
        session.server_type = server_type
        session.vlan_tun_attr = vlan_tun_attr
        session.policy_index = policy_index
        session.policy_name = policy_name
        session.session_timeout = session_timeout
        session.session_duration = session_duration
        session.idle_timeout = idle_timeout
        session.idle_time = idle_time
        session.termination_time = termination_time
        session.auth_server_ip = auth_server_ip

        return session
