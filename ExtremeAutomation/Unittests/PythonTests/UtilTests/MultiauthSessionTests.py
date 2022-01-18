from ExtremeAutomation.Unittests.Utilities.RobotUnitTest import RobotUnitTest
from ExtremeAutomation.Keywords.NetworkElementKeywords.Utils.NetworkElementMultiauthSession import \
    NetworkElementMultiauthSession


class MultiauthSessionUnitTests(RobotUnitTest):
    """
    Test the MultiauthSession object's comparison function.

    __create_session_obj() creates a fake session based on the passed args.
    """

    def test_multiauth_session_compare_equal(self):
        """
        Test the MultiauthSession object's comparison function.

        Compares two sessions with session_duration and idle_time equal between sessions.
        """
        keyword_session = self.__create_session_obj("ge.1.1", "00:11:11:11:11:11", "success", "11,11:28:37",
                                                    "0,00:00:00")
        output_session = self.__create_session_obj("ge.1.1", "00:11:11:11:11:11", "success", "11,11:28:37",
                                                   "0,00:00:00")
        keyword_session.compare_sessions(output_session, "=", "=")

    def test_multiauth_session_compare_session_greater(self):
        """
        Test the MultiauthSession object's comparison function.

        Compares two sessions with session_duration greater than the keyword value and idle_time equal.
        """
        keyword_session = self.__create_session_obj("ge.1.1", "00:11:11:11:11:11", "success", "11,11:00:00",
                                                    "0,00:00:00")
        output_session = self.__create_session_obj("ge.1.1", "00:11:11:11:11:11", "success", "11,11:28:37",
                                                   "0,00:00:00")
        keyword_session.compare_sessions(output_session, ">", "=")

    def test_multiauth_session_compare_session_less(self):
        """
        Test the MultiauthSession object's comparison function.

        Compares two sessions with session_duration less than the keyword value and idle_time equal.
        """
        keyword_session = self.__create_session_obj("ge.1.1", "00:11:11:11:11:11", "success", "11,12:00:00",
                                                    "0,00:00:00")
        output_session = self.__create_session_obj("ge.1.1", "00:11:11:11:11:11", "success", "11,11:28:37",
                                                   "0,00:00:00")
        keyword_session.compare_sessions(output_session, "<", "=")

    def test_multiauth_session_compare_idle_greater(self):
        """
        Test the MultiauthSession object's comparison function.

        Compares two sessions with session_duration equal and idle_time greater than the keyword value.
        """
        keyword_session = self.__create_session_obj("ge.1.1", "00:11:11:11:11:11", "success", "11,11:28:37",
                                                    "0,01:00:00")
        output_session = self.__create_session_obj("ge.1.1", "00:11:11:11:11:11", "success", "11,11:28:37",
                                                   "0,01:01:01")
        keyword_session.compare_sessions(output_session, "=", ">")

    def test_multiauth_session_compare_idle_less(self):
        """
        Test the MultiauthSession object's comparison function.

        Compares two sessions with session_duration equal and idle_time less than the keyword value.
        """
        keyword_session = self.__create_session_obj("ge.1.1", "00:11:11:11:11:11", "success", "11,11:28:37",
                                                    "0,01:02:02")
        output_session = self.__create_session_obj("ge.1.1", "00:11:11:11:11:11", "success", "11,11:28:37",
                                                   "0,01:01:01")
        keyword_session.compare_sessions(output_session, "=", "<")

    # +-------------------------+
    # | Non-Test Helper Methods |
    # +-------------------------+
    @staticmethod
    def __create_session_obj(port, station_address, auth_status, session_duration, idle_time):
        """
        Port            : ge.4.41        Station address   : f8-bc-12-4b-1e-0e
        Auth status     : success        Last attempt      : SUN SEP 16 02:09:57 2018
        Agent type      : mac            Session applied   : true
        Server type     : radius         VLAN-Tunnel-Attr  : None
        Policy index    : 2              Policy name       : Tools (active)
        Session timeout : 0              Session duration  : 11,11:28:37
        Idle timeout    : 1200           Idle time         : 0,00:00:00
        Termination time: Not Terminated
        Auth Server IP  : 10.52.6.13
        """
        session = NetworkElementMultiauthSession()

        session.port = port
        session.station_address = station_address
        session.auth_status = auth_status
        session.last_attempt = "SUN SEP 16 02:09:57 2018"
        session.agent_type = "mac"
        session.session_applied = "true"
        session.server_type = "radius"
        session.vlan_tun_attr = "None"
        session.policy_index = "2"
        session.policy_name = "Tools"
        session.session_timeout = "0"
        session.session_duration = session_duration
        session.idle_timeout = "1200"
        session.idle_time = idle_time
        session.termination_time = "Not Terminated"
        session.auth_server_ip = "10.52.6.13"

        return session


if __name__ == '__main__':
    RobotUnitTest.main()
