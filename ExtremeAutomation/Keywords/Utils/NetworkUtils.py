import time
import platform
import subprocess
from threading import Timer
from ExtremeAutomation.Library.Logger.Logger import Logger
from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import NetworkElementKeywordBaseClass

timer = None


class NetworkUtils(NetworkElementKeywordBaseClass):
    @staticmethod
    def __wait_for_log(message, start, interval):
        global timer
        keylogger = Logger()
        current = time.time()
        keylogger.log_info(message + " Elapsed Time: " + str(int(current - start)) + " seconds.")
        timer = Timer(interval, NetworkUtils.__wait_for_log, [message, start, interval])
        timer.start()

    def wait_for_pingable(self, ip, max_wait, wait_before, wait_after_success, message="", interval="5"):
        """
        Keyword Arguments:
        [ip]                 - The IP address to ping
        [max_wait]           - The maximum time to wait for ping success, before retuning a failure
        [wait_before]        - The initial delay, in seconds, before starting the pings
        [wait_after_success] - The number of seconds to delay after the ping is successful
        [message]            - The message to display between unsuccessful ping attempts
        [interval]           - The ping request interval

        This function waits up to max_wait for the IP address to be reachable.
        """
        global timer
        result = False
        ping_result = False
        max_wait = int(max_wait)
        wait_before = int(wait_before)
        wait_after_success = int(wait_after_success)
        interval = int(interval)
        total_time = 0

        self.logger.log_info("Waiting " + str(wait_before) + " seconds before starting ping.")
        time.sleep(wait_before)
        start = time.time()

        if message != "":
            timer = Timer(interval, self.__wait_for_log, [message, start, interval])
            timer.start()

        current = time.time()

        while current - start <= max_wait and not ping_result:
            ping_result = self.ping_once(ip)
            current = time.time()
            time.sleep(1)
            if ping_result:
                if timer:
                    timer.cancel()
                current = time.time()
                total_time = int(current - start)
                result = True
                self.logger.log_info("Waiting " + str(wait_after_success) + " seconds after successful ping.")
                time.sleep(wait_after_success)
        if timer:
            timer.cancel()

        return result, total_time

    def wait_for_not_pingable(self, ip, max_wait, wait_before, wait_after_success, message="", interval="5"):
        """
        Keyword Arguments:
        [ip]                 - The IP address to ping
        [max_wait]           - The maximum time to wait for ping failure, before retuning a failure
        [wait_before]        - The initial delay, in seconds, before starting the pings
        [wait_after_success] - The number of seconds to delay after the ping is unsuccessful
        [message]            - The message to display between successful ping attempts
        [interval]           - The ping request interval

        This function waits up to max_wait for the IP address to be unreachable.
        """
        global timer
        result = False
        count = 0
        max_wait = int(max_wait)
        wait_before = int(wait_before)
        wait_after_success = int(wait_after_success)
        interval = int(interval)
        total_time = 0

        self.logger.log_info("Waiting " + str(wait_before) + " seconds before starting ping.")
        time.sleep(wait_before)

        start = time.time()

        if message != "":
            timer = Timer(interval, self.__wait_for_log, [message, start, interval])
            timer.start()

        current = time.time()

        while current - start <= max_wait:
            ping_result = self.ping_once(ip)
            current = time.time()
            time.sleep(1)
            if not ping_result:
                count += 1
            if ping_result:
                count = 0
            if count == 3:
                if timer:
                    timer.cancel()
                current = time.time()
                result = True
                total_time = int(current - start)
                self.logger.log_info("Waiting " + str(wait_after_success) + " seconds after unsuccessful ping.")
                time.sleep(wait_after_success)
                break

        if timer:
            timer.cancel()

        return result, total_time

    @staticmethod
    def ping_once(ip):
        """
        Keyword Arguments:
        [ip] - The IP address to ping

        This function pings the given IP address.
        """
        operating_system = platform.system()

        try:
            # Mac OSX is darwin.
            if operating_system.lower() == "linux" or operating_system.lower() == "darwin":
                output = subprocess.check_output("ping -c 1 -W 2 " + ip, stderr=subprocess.STDOUT, shell=True)
                str_output = output.decode("utf-8")
                result = True if "64 bytes from " + ip in str_output else False
            elif operating_system.lower() == "windows":
                output = subprocess.check_output("ping -n 1 -w 2000 " + ip, stderr=subprocess.STDOUT)
                str_output = output.decode("utf-8")
                result = True if "Reply from " + ip in str_output else False
            else:
                raise Exception("Unknown OS")
        except subprocess.CalledProcessError:
            result = False

        return result
