from extauto.common.CommonValidation import CommonValidation
from extauto.common.Utils import Utils
from extauto.xiq.flows.manage.Devices import Devices
from time import sleep
import re

class WaitUntilEvent:
    def __init__(self):
        self.wait_time_multiplier = 1
        self.retries_cnt = None
        self.wait_time_left = None
        self.common_validation = CommonValidation()
        self.utils = Utils()
        self.devices = Devices()

    def wait_until_event(self, wait_time, check_interval, **kwargs):
        """
        - This keyword is used to keep track of a 'wait time budget' for a keyword that waits for an event to happen
        - At each call, the keyword 'sleeps' for a check_interval amount of time
        - Also, at each call, the 'wait time budget' is decremented by a 'check_interval' value
        - If there is no more time left in the 'wait time budget', another attempt is possible if the wait_time_multiplier attribute is > 1
        - If we also reached the maximum number of attemps, we give up

        - Keyword Usage:
        - ``Wait Until Event    wait_time=60    check_interval=15

        :param wait_time: total wait time per attempt (each attempt involving checks at 'check_interval' intervals)
        :param check_interval: amount of time to wait between successive checks
        :return: True if the wait time and maximum number of attempts are not yet exhausted, else False
        """

        msg_prefix = "Wait until event: "
        invalid_arguments = False
        try:
            wait_time = int(wait_time)
            check_interval = int(check_interval)
            if check_interval > wait_time:
                invalid_arguments = True
        except ValueError:
            invalid_arguments = True
        if invalid_arguments:
            kwargs['fail_msg'] = msg_prefix + "invalid values for arguments!"
            self.common_validation.fault(**kwargs)
            return -1
        if (self.retries_cnt == None) and (self.wait_time_left == None):
            self.retries_cnt = 1
            self.wait_time_left = wait_time
            self.utils.print_info(msg_prefix + "attempt " + str(self.retries_cnt) + " starting...")
            return True

        if self.wait_time_left >= check_interval:
            self.utils.print_info(msg_prefix + "attempt " + str(self.retries_cnt) + ", waiting for " +
                                  str(check_interval) + " seconds...")
            sleep(check_interval)
            self.wait_time_left -= check_interval
        else:
            self.utils.print_info(msg_prefix + "attempt " + str(self.retries_cnt) + " failed!")
            if self.retries_cnt < self.wait_time_multiplier:
                self.retries_cnt += 1
                self.wait_time_left = int(wait_time)
                self.utils.print_info(msg_prefix + "attempt " + str(self.retries_cnt) + " starting...")
            else:
                self.utils.print_info(msg_prefix + "no more attempts left!")
                return False

        return True


    def test_wait_until_event(self, retries_cnt, wait_time=20, check_interval=4, **kwargs):
        """
        - This keyword is used to test the 'Wait Until Event' kewyword

        - Keyword Usage:
        - ``Test Wait Until Event   ${retries_cnt}``
        - ``Test Wait Until Event   ${retries_cnt}  wait_time=60    check_interval=15``

        :param retries_cnt: number of successive calls of the 'Wait Until Event' keyword
        :param wait_time: total wait time per attempt (each attempt involving checks at 'check_interval' intervals)
        :param check_interval: amount of time to wait between successive checks
        :return: 1 when test is completed, -1 if arguments values are invalid
        """

        msg_prefix = "Test wait until event: "
        invalid_arguments = False
        try:
            retries_cnt = int(retries_cnt)
        except ValueError:
            invalid_arguments = True
        if invalid_arguments:
            kwargs['fail_msg'] = msg_prefix + "invalid values for arguments!"
            self.common_validation.fault(**kwargs)
            return -1

        while (retries_cnt > 0) and (self.wait_until_event(wait_time, check_interval)):
            retries_cnt -= 1

        kwargs['pass_msg'] = msg_prefix + "test is completed!"
        self.common_validation.passed(**kwargs)
        return 1


    def wait_until_device_update_done_new(self, device_serial, wait_time=300, check_interval=10, **kwargs):
        """
        - This keyword checks if the device update is completed

        - Keyword Usage:
        - ``Wait Until Device Update Done New   ${device_serial}``
        - ``Wait Until Device Update Done New   ${device_serial}    wait_time=60    check_interval=15``

        :param device_serial: serial number of the device
        :param wait_time: total wait time per attempt (each attempt involving checks at 'check_interval' intervals)
        :param check_interval: amount of time to wait between successive checks
        :return: 1 if device update is done, else -1
        """

        self.devices.navigator.navigate_to_manage_tab()
        self.devices.refresh_devices_page()

        date_regex = r"(\d{4})-((0[1-9])|(1[0-2]))-(0[1-9]|[12][0-9]|3[01]) ([0-2]*[0-9]\:[0-6][0-9]\:[0-6][0-9])"
        complete = False
        while (not complete) and self.wait_until_event(wait_time, check_interval):
            update_status = self.devices.get_device_details(device_serial, 'UPDATED')
            self.utils.print_info("updated status...," + str(device_serial) + " " + str(update_status))
            if (update_status == '') or (re.match(date_regex, update_status)):
                complete = True
                break

        if (complete):
            kwargs['pass_msg'] = "Device has finished updating!"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Device has NOT finished updating!"
            self.common_validation.failed(**kwargs)
            return -1
