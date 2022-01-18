import time
from ExtremeAutomation.Library.Utils.ListUtils import ListUtils
from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import \
    NetworkElementKeywordBaseClass
from ExtremeAutomation.Keywords.BaseClasses.KeywordResult import KeywordResult
from ExtremeAutomation.Keywords.Utils.NetworkUtils import NetworkUtils


class PingKeywords(NetworkElementKeywordBaseClass):

    def ip_should_be_reachable(self, ips, wait_before="10", wait_after_success="1", **kwargs):
        """
        Keyword Arguments:
        [ips]                - The IP address(es) that should be pinged.
        [wait_before]        - How long the keyword should wait before starting the ping.
        [wait_after_success] - How long the keyword should after successfully pinging the IP.

        Pings an IP. If the wait_for kwarg is present and no reply is received after <max_wait> seconds the keyword
        fails.
        """
        ips = ListUtils.convert_to_list(ips)

        kw_results = []
        for ip in ips:
            dev, api, _ = self._init_keyword(**kwargs)

            time.sleep(int(wait_before))
            ping = NetworkUtils()
            result = ping.ping_once(ip)

            kw_results.append(KeywordResult("Host Ping from Engine", result,
                                            "Device is reachable.",
                                            "Device IS NOT reachable!", None))

            if result:
                time.sleep(int(wait_after_success))

        return self._keyword_cleanup(kw_results)

    def ip_should_not_be_reachable(self, ips, wait_before="10", wait_after_success="1", **kwargs):
        """
        Keyword Arguments:
        [ips]                - The IP address(es) that should be pinged.
        [wait_before]        - How long the keyword should wait before starting the ping.
        [wait_after_success] - How long the keyword should after successfully pinging the IP.

        Pings an IP. If the wait_for kwarg is present and no reply is received after <max_wait> seconds the keyword
        fails.
        """
        ips = ListUtils.convert_to_list(ips)

        kw_results = []
        for ip in ips:
            dev, api, _ = self._init_keyword(**kwargs)

            time.sleep(int(wait_before))
            ping = NetworkUtils()
            result = not ping.ping_once(ip)

            kw_results.append(KeywordResult("Host Ping from Engine", result,
                                            "Device is not reachable.",
                                            "Device IS STILL reachable!",
                                            None))

            if result:
                time.sleep(int(wait_after_success))

        return self._keyword_cleanup(kw_results)

    def wait_until_ip_is_reachable(self, ips, max_wait, wait_before="10", wait_after_success="1", message="",
                                   interval="3", **kwargs):
        """
        Keyword Arguments:
        [device_names]       - The device(s) the keyword should be run against.
        [max_wait]           - How long the keyword should ping the IP before marking the keyword as a failure.
        [wait_before]        - How long the keyword should wait before starting the ping.
        [wait_after_success] - How long the keyword should after successfully pinging the IP.
        [message]            - The message to log each time a ping is sent.
        [interval]           - How often the ping should be sent, in seconds.

        Pings a network element until a reply is received. If no reply is received after <max_wait>
        seconds the keyword fails.
        """
        ips = ListUtils.convert_to_list(ips)

        kw_results = []
        for ip in ips:
            dev, api, _ = self._init_keyword(**kwargs)

            wait_for = NetworkUtils()
            result, total_time = wait_for.wait_for_pingable(ip, max_wait, wait_before, wait_after_success, message,
                                                            interval)

            kw_results.append(KeywordResult("Host Ping from Engine", result,
                                            "Device pingable after " + str(total_time) + " seconds.",
                                            "Device was NOT pingable after " + str(max_wait) + " seconds.",
                                            None))

        return self._keyword_cleanup(kw_results)

    def wait_until_ip_is_not_reachable(self, ips, max_wait, wait_before="10", wait_after_success="1",
                                       message="", interval="3", **kwargs):
        """
        Keyword Arguments:
        [device_names]       - The device(s) the keyword should be run against.
        [max_wait]           - How long the keyword should ping the IP before marking the keyword as a failure.
        [wait_before]        - How long the keyword should wait before starting the ping.
        [wait_after_success] - How long the keyword should after unsuccessfully pinging the IP.
        [message]            - The message to log each time a ping is sent.
        [interval]           - How often the ping should be sent, in seconds.

        Pings an IP until no reply is received. If replies are received for <max_wait> seconds the keyword fails.
        """
        ips = ListUtils.convert_to_list(ips)

        kw_results = []
        for ip in ips:
            dev, api, _ = self._init_keyword(**kwargs)

            wait_for = NetworkUtils()
            result, total_time = wait_for.wait_for_not_pingable(ip, max_wait, wait_before, wait_after_success, message,
                                                                interval)

            kw_results.append(KeywordResult("Host Ping from Engine", not result,
                                            "Device was not pingable after " + str(total_time) + " seconds.",
                                            "Device was never unreachable after " + str(max_wait) + " seconds.",
                                            None))

        return self._keyword_cleanup(kw_results)
