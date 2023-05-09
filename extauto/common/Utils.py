import re
import os
import random
import string
from datetime import datetime, timedelta
from robot.libraries.BuiltIn import BuiltIn
from selenium.common.exceptions import NoSuchElementException
from extauto.common.ConfigFileHelper import ConfigFileHelper
import time
from ExtremeAutomation.Imports.CommonObjectUtils import CommonObjectUtils
if CommonObjectUtils().executionModePytest():
    from ExtremeAutomation.Library.Logger.PytestLogger import PytestLogger as Logging
else:
    from ExtremeAutomation.Library.Logger.RobotLogger import RobotLogger as Logging

class Utils:
    def __init__(self):
        self.logger = Logging()
        self.cfgHelp = ConfigFileHelper()
        self.cfgHelp.checkConfigRefresh()


    def get_config_value(self, conf_str):
        """
        - Get the config value of a variable
        - Keyword Usage:
        -  ``Get Config Value   VARIABLE``

        :param conf_str: Variable name
        :return: value of the variable
        """

        toast = BuiltIn().get_variable_value("${" + conf_str + "}")
        self.print_debug("Toast Message For ", conf_str, " : ", toast)
        return toast

    def get_random_string(self, length="default"):
        """
        - Get the random string of specified length, default length is 10 characters
        - Keyword Usage:
        -  ``Get Random String``
        -  ``Get Random String   length=5``

        :param length: length of the character to generate
        :return: generated random string
        """
        if length == "default":
            length = 10
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(int(length)))

    def get_random_integer(self, length=10, lower_limit=9999, upper_limit=999999999):
        """
        - Get the random integer in specified upper and lower limit
        - Keyword Usage:
        -  ``Get Random Integer``

        :param length:  len of integer
        :param lower_limit: lower limit to generate the integer
        :param upper_limit: upper limit to generate the integer
        :return: generated random integer
        """
        return random.randrange(lower_limit, upper_limit, length)

    def get_random_mac(self, delimiter="default"):
        """
        - Get the random mac
        - By default it will generate mac in the format aa:bb:11:22:33:44
        - Keyword Usage:
        -  ``Get Random Mac``
        -  ``Get Random Mac   delimiter=:``

        :param delimiter:  specify the delimiter ex  "-", ":"
        :return: generated mac
        """
        mac_temp = -1
        mac = [0x00, 0x16, 0x3e, random.randint(0x00, 0x7f), random.randint(0x00, 0xff), random.randint(0x00, 0xff)]

        if delimiter == "default":
            mac_temp = '-'.join(map(lambda x: "%02x" % x, mac))
        if delimiter == ":":
            mac_temp = ':'.join(map(lambda x: "%02x" % x, mac))
        if mac_temp != -1:
            return mac_temp.upper()
        else:
            return mac_temp

    def get_random_ip(self):
        """
        - Generate the random ip address
        - Keyword Usage:
        -  ``Get Random Ip``

        :return: generated random ip address
        """
        ip = [random.randint(10, 100), random.randint(0, 253), random.randint(0, 253), random.randint(0, 100)]
        ip_temp = '.'.join(map(lambda x: "%s" % x, ip))
        print (ip_temp + "/" + '24')
        return ip_temp + '/' + '24'

    def look_and_feel(self, first, second, third):
        """
        - embeds 3 png files in to robot framework output log.html file side by side
        - Keyword Usage:
        -  ``Look and Feel   Screen1.png     Screen2.png    Screen3.png``

        :param first: screenshot or image 1
        :param second: screenshot or image 2
        :param third: screenshot or image 3
        :return: returns none
        """

        print ("*HTML* "
              "<a href=" + first + "> <img src=" + first + " width=\"500px\"></a> "
                "<a href=" + second + "> <img src=" + second + " width=\"500px\"></a> "
                "<a href=" + third + "> <img src=" + third + " width=\"500px\"></a>")

    def decode_to_ascii(self, _str):
        """
        - decode given string to ascci
        - Keyword Usage:
        -  ``Decode To Ascii   ${STR}``

        :param _str: str to decode to ascci
        :return: decoded string
        """
        self.print_info("Input value: ", _str)
        return str(_str.encode('utf-8').decode('ascii', 'ignore'))

    def special_char_check(self, _str):
        """
        - check the special character in the given string
        - Keyword Usage:
        -  ``Special CHar Check   ${STR}``

        :param _str: str to check the special character
        :return: 0 if special character exists else 1
        """
        self.print_info("Input value: ", _str)
        if re.match("^[a-zA-Z0-9_-]*$", _str):
            return 0
        else:
            return 1

    def print_error(self, *words):
        """
        - prints the given list of words in to console and robot framework log.html file
        - Note this is not a keyword to use inside the robot framework script. only used in libs
        """

        line = ""

        for word in words:
            try:
                line += str(word)
            except TypeError:
                pass

        self.logger.error(line, stacklevel=2)

    def print_warning(self, *words):
        """
        - prints the given list of words in to console and robot framework log.html file
        - Note this is not a keyword to use inside the robot framework script. only used in libs
        """

        line = ""

        for word in words:
            try:
                line += str(word)
            except TypeError:
                pass

        self.logger.warning(line, stacklevel=2)

    def print_info(self, *words):
        """
        - prints the given list of words in to console and robot framework log.html file
        - Note this is not a keyword to use inside the robot framework script. only used in libs
        """

        line = ""

        for word in words:
            try:
                line += str(word)
            except TypeError:
                pass

        self.logger.info(line, stacklevel=2)

    def print_debug(self, *words):
        """
        - prints the given list of words in to console and robot framework log.html file
        - Note this is not a keyword to use inside the robot framework script. only used in libs
        """

        line = ""

        for word in words:
            try:
                line += str(word)
            except TypeError:
                pass

        self.logger.debug(line, stacklevel=2)

    def get_utc_time_difference(self, t1, t2):
        """
        - Get the time difference between t2 and t1
        - Keyword Usage:
        -  ``Get Utc Time Difference   ${TIME1}  ${TIME2}``

        :param t1: datetime.datetime object
        :param t2: datetime.datetime object
        :return: time difference of t2 and t1 in minutes
        """
        if not isinstance(t1, str):
            t1 = t1.strftime("%Y-%m-%d %H:%M")
        if not isinstance(t2, str):
            t2 = t2.strftime("%Y-%m-%d %H:%M")
        t1 = datetime.strptime(str(t1), '%Y-%m-%d %H:%M')
        t2 = datetime.strptime(str(t2), '%Y-%m-%d %H:%M')

        self.print_info("t1:{}".format(t1))
        self.print_info("t2:{}".format(t2))

        time_delta = t2 - t1
        self.print_info("Time difference in minutes:{}".format(time_delta))
        return time_delta.total_seconds() / 60.0

    def get_current_time(self):
        """
        - Get the Current Time
        - Keyword Usage:
        -  ``Get Current Time``

        :return: current time
        """
        self.print_info("datetime.now()", datetime.now())
        return datetime.now()

    def get_current_time_in_sec(self):
        """
        - Get the Current Time in Sec
        - Keyword Usage:
        -  ``Get Current Time In Sec``

        :return: current time in sec
        """
        self.print_info("round(time.time())", round(time.time()))
        return round(time.time())

    def get_min(self, *args):
        """
        - used to find min(v1,v2,...)
        """
        return min(*args)

    def include_image(self, file_name):
        """
        - includes the image in robot framework log.html file
        - Note this is not a keyword to use inside the robot framework script. only used in libs
        """

        # Commented on 1/18/23 because variable is unused
        # output_folder = BuiltIn().get_variable_value("${OUTPUT DIR}")
        BuiltIn().get_variable_value("${OUTPUT DIR}")

        print("*HTML* <a href=" + file_name + "> <img src=" + file_name
              + " width=\"600px\" style=\"border:5px solid red\"></a>")

        return file_name

    def log_to_report(self, file_name):
        """
        - logs a video file in robot framework log.html file
        - Note this is not a keyword to use inside the robot framework script. only used in libs
        """

        win_host = BuiltIn().get_variable_value("${WINDOWS10}")
        self.print_info("Windows Host: ", win_host)
        self.print_info("File Name: ", file_name)
        print ("*HTML* <a href=" + "http://" + win_host + "/" + file_name + ".avi>Video Record</a>")

    def get_device_time(self, output):
        """
        - Gets the device time from the CLI output of a DUT
        - Keyword Usage:
        -  ``Get Device Time        ${CLI_OUTPUT}``

        :return: device time in hh:mm format
        """
        self.print_info("Getting the device time from output: ", output)
        try:
            return re.search('[0-9]+:[0-9]+', output).group(0)
        except Exception as e:
            self.print_info(e)
            return -1

    def get_device_date(self, output, separator="/"):
        """
        - Gets the device date from the CLI output of a DUT
        - Keyword Usage:
        -  ``Get Device Date       ${CLI_OUTPUT}``

        :param output:
        :param separator: can be / or -
        :return: returns a date in mm/dd/yyyy or mm-dd-yyyy format
        """

        self.print_info("Input String: ", output)
        self.print_info("Date in MM/DD/YYY format: ", )
        try:
            d = re.search('([1-9]+ )', output).group(1).strip()
            m = re.search('-([0-9]+)-', output).group(1).strip()
            y = re.search('([0-9]{4})', output).group(1).strip()

            self.print_info("Date in MM/DD/YYY format: ", m + "/" + d + "/" + y)
            if separator == "/":
                return m + "/" + d + "/" + y
            if separator == "-":
                return m + "-" + d + "-" + y
        except Exception as e:
            self.print_info(e)
            return -1

    def round_time(self, upgrade_time):
        """
        - This method expects time format as 24 Hours
        - Converts it in to AM or PM
        - This is specific to XIQ UI behavior

        :param upgrade_time:
        :return:
        """
        words = upgrade_time.split(':')
        _minute = int(words[1])
        _hour = int(words[0])
        _m = 0
        _h = 0

        self.print_info("_hour  : ", _hour)
        self.print_info("_minute: ", _minute)

        if _hour > 12:
            meridian = 'PM'
            _h = _hour - 12
            self.print_info("Meridian: ", meridian, " Hour: ", _h)
        else:
            _h = _hour
            meridian = 'AM'
            self.print_info("Meridian: ", meridian, " Hour: ", _h)

        if _minute < 10:
            _m = 15
        elif _minute < 25:
            _m = 30
        elif _minute < 40:
            _m = 45
        elif _minute < 55:
            _m = '00'
            _h += 1
        elif _minute <= 59:
            _m = '15'
            _h += 1
        elif '00' in words[1]:
            _m = '15'
            _h = words[0]

        self.print_info("_h: ", _h)
        self.print_info("_m: ", _m)

        return str(_h) + ':' + str(_m) + ' ' + meridian

    def convert_time_to_24_hours_format(self, _time):
        """
        - This method expects time format as HH:MM AM or HH:MM PM
        - Converts it in to 24 Hour time format

        :param _time:
        :return:
        """
        words = _time.split(' ')
        _hh_mm = words[0]
        _meridian = words[1]

        _time = _hh_mm.split(':')
        _hh = int(_time[0])
        _mm = _time[1]

        if 'AM' in _meridian:
            pass

        if 'PM' in _meridian:
            _hh += 12

        if _hh == 24:
            _hh = '00'

        time_24_hour_format = str(_hh) + ':' + str(_mm)

        self.print_info("Converting Time: ", _time, " to 24 Hour format: ", time_24_hour_format)
        return time_24_hour_format

    def get_current_date_time(self, time_format="%Y-%m-%d %H:%M"):
        """
        - Get current date with %Y-%m-%d %H:%M format

        :param time_format: default time format
        :return: current date with %Y-%m-%d %H:%M format
        """
        now = datetime.now()
        date_time = now.strftime(time_format)
        self.print_info(f"Current Date Time is {date_time}")
        return date_time

    def get_previous_time_delta(self, t1, hour=None, minutes=None, time_format='%Y-%m-%d %H:%M'):
        """
        - Get last specified time delta
        - Example:
        - if  t1='2020-05-19 03:57'  last_24_hour_time=''2020-05-18 03:57''

        :param t1: present time
        :param hour: time in hour to get the previous time
        :param minutes:  time in Minutes to get the previous time
        :param time_format: specify the time format
        :return: time delta
        """
        if not isinstance(t1, str):
            t1 = t1.strftime("%Y-%m-%d %H:%M")

        t1 = datetime.strptime(str(t1), '%Y-%m-%d %H:%M')
        previous_time = None
        if hour:
            previous_time = t1 - timedelta(hours=int(hour))
        if minutes:
            previous_time = t1 - timedelta(minutes=int(minutes))
        self.print_info("previous time:{}".format(previous_time.strftime(time_format)))
        return previous_time.strftime(time_format)

    def get_utc_time(self, time_format=None):
        """
        - Get the utc time with specified time format, by default %Y-%m-%d %H:%M.%s

        :param time_format:  specify the time format
        :return: utc time
        """
        utc_time = datetime.utcnow()
        self.print_info("Current UTC Time is: {}".format(utc_time))
        if time_format:
            return utc_time.strftime(time_format)
        else:
            return utc_time

    def get_utc_iso_time_format(self):
        """
        - This keyword is used to get the time in ISO Format

        :return: ISO time now
        """
        datetime_utc = datetime.utcnow().isoformat()
        self.print_info("Time in ISO Format: ", datetime_utc)
        return datetime_utc

    def get_utc_hour_time_delta(self, utc_time, hour=24):
        """
        - Get the utc time after the specified time delta in hour
        - Example:
        -  if utc time is:         utc_time        = 2020-04-24 03:12:04.905116
        -  utc time after delta    utc_after_10min = 2020-04-25 03:12:04.905116

        :param utc_time:
        :param hour:
        :return:  Time %Y-%m-%d %H:%M format
        """
        utc_time_after = utc_time + timedelta(hours=hour)
        utc_time_after = utc_time_after.strftime("%Y-%m-%d %H:%M")
        self.print_info(utc_time_after)
        return utc_time_after

    def get_utc_minute_time_delta(self, utc_time, minutes=10):
        """
        - Get the utc time after the specified time delta in minutes
        - Example:
        -  if utc time :           utc_time        = 2020-04-24 03:12:04.905116
        -  utc time after delta    utc_after_10min = 2020-04-24 03:23:09.519271

        :param utc_time:
        :param minutes:
        :return: Time %Y-%m-%d %H:%M format
        """
        utc_time = utc_time + timedelta(minutes=minutes)
        utc_time_after = utc_time.strftime("%Y-%m-%d %H:%M")
        self.print_info(utc_time_after)
        return utc_time_after

    def count_down_in_minutes(self, t):
        """
        - Countdown in minutes

        :param t: time to count down
        :return: None
        """
        t = int(t)
        if t < 0:
            return 1
        self.print_info("Waiting for count down in {} Minutes".format(t))
        while t:
            time_format = '{:02d} Minutes Remaining!!!!'.format(t)
            BuiltIn().log_to_console('\r' + time_format + '')
            time.sleep(60)
            t -= 1
        self.print_info(" count down:{} Minutes Completed".format(t))

    def get_first_half_of_network_policy(self, network_policy):
        """
        - This keyword returns the first half of a Network Policy

        :param network_policy: network_policy
        :return: returns first half of MAC
        """
        self.print_info("Input network policy: ", network_policy)
        length = len(network_policy)
        seg = round(length / 2)
        net_first_half = network_policy[:seg]
        return net_first_half

    def switch_to_default(self, driver):
        """
        - This keyword Will Switch to default frame
        """
        self.print_info("<<<Switching to Default>>>")
        time.sleep(5)
        try:
            driver.find_element_by_tag_name('iframe')
            self.print_info("||| No Need to Switch |||")
        except NoSuchElementException:
            driver.switch_to.default_content()
            self.print_info("<<< Switching to Default Completed >>>")

    def switch_to_iframe(self, driver):
        """
        - This keyword Will Switch to iframe
        """
        self.print_info("*>>> Switching to IFrame <<<")
        try:
            iframe = driver.find_element_by_tag_name('iframe')
            # driver.switch_to_frame(iframe)
            driver.switch_to.frame(iframe)
            self.print_info(">>> Switching to IFrame Completed <<<")
        except Exception as e:
            self.print_info("Error: ", e)

    def switch_to_iframe_with_attr(self, driver, attr):
        self.print_info(f"*>>> Switching to IFrame with Attribute '{attr}' <<<")
        iframe = driver.find_element_by_xpath('//iframe[' + attr + ']')
        driver.switch_to_frame(iframe)
        self.print_info(">>> Switching to IFrame Completed <<<")

    def date_time_addition(self, date_time=None, days=None, hours=None, minutes=None, seconds=None):
        """
        - This keyword is used to add days/hours/minutes/seconds to the date-time  which is passed as argument.
        -  Keyword Usage:
        -  `` Date Time Addition  date_time=2020-10-20 12:03:47    days=5     hours=13    minutes=4      seconds=2``

        :param date_time: date and time should be of format : %Y-%m-%d %H:%M:%S
        :param days: Number of days to be added.
        :param hours: Number of hours to be added.
        :param minutes: Number of minutes to be added.
        :param seconds: Number of seconds to be added.
        :return: returns the modified date and time of format : %Y-%m-%d %H:%M:%S
        """
        try:
            if date_time:
                if type(date_time) is not str:
                    date_time = str(date_time)
                datetime_value = datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S')
                self.print_info("Original date-time ", datetime_value)
                if days:
                    self.print_info("Days added: ", days)
                    if days is not int:
                        days = int(days)
                    datetime_value = datetime_value + timedelta(days=days)
                if hours:
                    self.print_info("Hours added: ", hours)
                    if hours is not int:
                        hours = int(hours)
                    datetime_value = datetime_value + timedelta(hours=hours)
                if minutes:
                    self.print_info("Minutes added: ", minutes)
                    if minutes is not int:
                        minutes = int(minutes)
                    datetime_value = datetime_value + timedelta(minutes=minutes)
                if seconds:
                    self.print_info("Seconds added: ", seconds)
                    if seconds is not int:
                        seconds = int(seconds)
                    datetime_value = datetime_value + timedelta(seconds=seconds)
                self.print_info("Modified date-time ", datetime_value)
                return datetime_value
            else:
                self.print_info("Provide date-time as input of format : %Y-%m-%d %H:%M:%S")
                return -1
        except Exception as e:
            self.print_info("Unable to perform date time addition ", e)
            return -1

    def switch_to_iframe_n(self, driver, iframe_num):
        self.print_info("*>>> Getting count of iframes in web page <<<")
        iframe_count = len(driver.find_elements_by_tag_name('iframe'))

        self.print_info("Number of iframes: ", iframe_count)
        iframe = driver.find_elements_by_tag_name('iframe')[iframe_num]

        driver.switch_to_frame(iframe)
        self.print_info(">>> Switching to IFrame ", iframe_num, " Completed <<<")

    def convert_ms_to_time(self, milliseconds):
        self.print_info(f"Converting {milliseconds} milliseconds to days/hours/minutes/seconds")
        time_info = dict()
        ms_val = int(milliseconds)
        if ms_val < 0:
            self.print_info(f"Invalid milliseconds '{ms_val}' to convert")
            ms_val = 0
        seconds, ms_val = divmod(ms_val, 1000)
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)
        seconds = seconds + ms_val / 1000

        time_info["days"] = days
        time_info["hours"] = hours
        time_info["minutes"] = minutes
        time_info["seconds"] = seconds

        self.print_debug("**** Milliseconds Converted To Days/Hours/Minutes/Seconds ****")
        for key, value in time_info.items():
            self.print_info(f"{key}: {value}")

        return time_info

    def compare_date_time_strings(self, str1, str2):
        # Returns 1 if the strings are equal, 0 if they are not equal
        ret_val = 0
        self.print_info(f"Comparing {str1} and {str2}")
        dt_obj_1 = datetime.strptime(str1, "%m/%d/%Y %H:%M:%S %p")
        dt_obj_2 = datetime.strptime(str2, "%m/%d/%Y %H:%M:%S %p")
        self.print_debug(f"DT OBJ 1: {dt_obj_1}")
        self.print_debug(f"DT OBJ 2: {dt_obj_2}")
        if dt_obj_1 == dt_obj_2:
            self.print_info("Date/Time strings are equal")
            ret_val = 1
        else:
            self.print_info("Date/Time strings are NOT equal")

        return ret_val

    def expand_port_range(self, port_range):
        """
        Take a port_range string of form '1-3,5,10,12-15' and return list of individual ports
        as shown here [1,2,3,5,10,12,13,14,15]

        :param port_range:
        :return:
        """
        result = []
        for part in port_range.split(','):
            if '-' in part:
                a, b = part.split('-')
                result.extend([p for p in range(int(a), int(b) + 1)])
            else:
                result.append(int(part))
        return result

    def get_current_time_in_milliseconds(self):
        """
        - This keyword is used to get the current time in milliseconds.
        - Keyword Usage:
        -  `` Get Current Time In Milliseconds``

        :return: time in milliseconds
        """
        timestamp = int(time.time())
        self.print_info("Current time in milliseconds: ", timestamp)
        return timestamp

    def get_time_in_milliseconds(self, diff=0):
        time_millies = int(round(time.time() * 1000) - diff)

        return time_millies

    def convert_time_to_milliseconds(self, time_str):
        """
        - This keyword converts given time to milliseconds.
        - Keyword Usage:
        -  `` Convert Time To Milliseconds 12:03:47``
        -  In above case it returns value as 43427000

        :param time_str: time should be of format : %H:%M:%S
        :return: time in milliseconds
        """
        hour, minute, sec = map(int, time_str.split(':'))
        ms_time = (hour * 3600 + minute * 60 + sec) * 1000
        self.print_info(f"Time in milliseconds for {time_str} : {ms_time}")
        return ms_time

    def get_time_difference_in_milliseconds(self, time1, time2):
        """
        - This keyword is used to get the time difference in milliseconds.
        - Keyword Usage:
        -  `` Get Time Difference In Milliseconds  1622696034870  24:03:47``

        :param time1: Timestamp in milliseconds
        :param time2: Time in format : %H:%M:%S and should be greater than 24 hours
        :return: time in milliseconds
        """
        hour, minute, sec = map(int, time2.split(':'))
        ms_time = (hour * 3600 + minute * 60 + sec) * 1000
        self.print_info(f"Time in milliseconds for {time2} : {ms_time}")
        time_diff = int(time1) - ms_time
        self.print_info("Time difference in milliseconds : ", time_diff)
        return time_diff

    def get_current_date(self):
        """
        Get current date with %Y-%m-%d format

        :return: date
        """
        now = datetime.now()
        date_time = now.strftime("%Y-%m-%d")
        self.print_info("Current Date is", date_time)
        return date_time

    def convert_string_to_date(self, str, pattern="(\\d+)"):
        '''
        This function covets a string into a date

        :param str: The date as string
        :param pattern: A Regex which match the date
        :return:
        '''

        row = self.get_regexp_matches(str, pattern, 1)
        date = datetime(row[0], row[1], row[2], row[3], row[4], row[5])
        return date

    def get_regexp_matches(self, string, pattern, *groups):
        """Returns a list of all non-overlapping matches in the given string.

        ``string`` is the string to find matches from and ``pattern`` is the
        regular expression. See `BuiltIn.Should Match Regexp` for more
        information about Python regular expression syntax in general and how
        to use it in Robot Framework test data in particular.

        If no groups are used, the returned list contains full matches. If one
        group is used, the list contains only contents of that group. If
        multiple groups are used, the list contains tuples that contain
        individual group contents. All groups can be given as indexes (starting
        from 1) and named groups also as names.

        Examples:
        | ${no match} =    | Get Regexp Matches | the string | xxx     |
        | ${matches} =     | Get Regexp Matches | the string | t..     |
        | ${one group} =   | Get Regexp Matches | the string | t(..)   | 1 |
        | ${named group} = | Get Regexp Matches | the string | t(?P<name>..) | name |
        | ${two groups} =  | Get Regexp Matches | the string | t(.)(.) | 1 | 2 |
        =>
        | ${no match} = []
        | ${matches} = ['the', 'tri']
        | ${one group} = ['he', 'ri']
        | ${named group} = ['he', 'ri']
        | ${two groups} = [('h', 'e'), ('r', 'i')]
        """
        regexp = re.compile(pattern)
        groups = [self._parse_group(g) for g in groups]
        return [m.group(*groups) for m in regexp.finditer(string)]

    def wait_till(self, func=None, fail_func=None, timeout=20, delay=0.2, exp_func_resp=True, is_logging_enabled=False,
                  silent_failure=False, custom_response=[], msg=None):
        """ wait till method returns the func() response and raise Timeout Exception if timedout
            :param func              : callable function without arguments
            :param fail_func         : callable function, to be run after every unsuccessful attempt of func
            :param timeout           : float/int type , max number of seconds to wait before timed out
            :param delay             : float/int, delay in seconds between each retry
            :param exp_func_resp     : bool,by default wait_till expects True from the callback function func
            :pram is_logging_enabled : bool, prints the time remaining and result of the func function, default disabled
            :pram silent_failure     : bool, if true nothing will be returned and Timeout exceptions will not be raised.
            :pram custom_response    : list, should contain list of str values to match against the func() response. e.g ["Green", "connected", "MANAGED"]
            :param msg               : str, message that has to printed when this wait_till function is called.
            :return: raise timeout exception incase max timed out else resturns the calback function's response
        usages:
            self.utils.wait_till()
            self.utils.wait_till(_check_device_rows)
            self.utils.wait_till(_check_device_rows, timeout=5, delay=0.25)
            self.utils.wait_till(_check_device_rows, _click_eligible, is_logging_enabled=True, silent_failure=False)
            out, et = self.tools.wait_till(_check_device_rows, exp_func_resp=False, silent_failure=False, custom_response=["Green", "Managed"])

        Note:
            1. custom_response has higher priority than the exp_func_resp
            2. Timeout might not the break point, callback func and fail_func might take sometime
            3. If no arguments passed then it will act like a sleep(timeout) and returns None.
            4. Calback func() response and the Execution Time are returned as tuple.
                e.g
                out,et = wait_till(_check_device_rows, _click_eligible, is_logging_enabled=True, silent_failure=False))
                out = func() response
                et  = Execution time (HH:MM:SS)
        """

        start = time.time()

        # A simple boolean (Ture/False) conversion function
        def to_bool(_input):
            """
            A small supporting function which is used to convert the func response into a boolean response
            """
            if _input is None:
                return False
            elif isinstance(_input, bool):
                return _input
            elif isinstance(_input, int):
                return _input > 0
            elif isinstance(_input, str) and _input.lower() not in ['yes', 'true']:
                return _input.lower() not in ['no', 'false']
            else:
                return bool(_input)

        # Args None/Negative validation and correction
        if not timeout: timeout = 1
        if timeout <= 0: timeout = 1
        if not delay: delay = timeout
        if delay <= 0 or delay > timeout: delay = timeout

        # Converting the type of timeout and delay to float
        if isinstance(timeout, (int, float)):
            timeout = float(timeout)
        if isinstance(delay, (int, float)):
            delay = float(delay)

        # Converting the custom_response list values into lowercase
        custom_response_list = []
        for x in custom_response:
            if isinstance(x, str):
                custom_response_list.append(x.lower())
            else:
                custom_response_list.append(x)

        # If expected response arg is not a boolean then it will be converted into a equalent boolean value
        if not isinstance(exp_func_resp, bool):
            exp_func_resp = to_bool(exp_func_resp)
            if is_logging_enabled:
                self.print_info(f"Expected Response is not boolean, converting into boolean '{exp_func_resp}'")

        # Storing the timeout for later use
        max_wait_time = timeout
        callback_response = None
        callback_response_bool = None
        callback_response_lower = None
        elapsed_time = None
        elapsed_time_hms = None

        # This custom message prints in the start of wait_till if it set else prints default message
        if msg:
            self.print_info(f"{msg}")
        else:
            self.print_info(f"wait_till Started: Timeout '{timeout}' seconds, Delay '{delay}' seconds ")

        # if func is None, wait until the default timeout and returns None
        if func is None:
            time.sleep(timeout)
            return None

        while timeout > 0:

            # Time sleep for delay seconds
            time.sleep(delay)
            timeout = timeout - delay

            # function call to callback
            callback_response = func()

            # if is_logging_enabled is True then callback response and time left in seconds will be printed
            if is_logging_enabled:
                self.print_info(
                    f"Actual callback function response is '{callback_response}', time left '{timeout}s' ")

            # callback function response is converted to bool type
            callback_response_bool = to_bool(callback_response)

            if isinstance(callback_response, str):
                callback_response_lower = callback_response.lower()
            else:
                callback_response_lower = callback_response

            # Execution end time
            elapsed_time = time.time() - start
            elapsed_time_hms = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))

            # This block checks if callback response matches with custom response list and it has higher priority than exp_func_resp
            if len(custom_response_list) > 0:
                if callback_response_lower in custom_response_list:
                    if is_logging_enabled:
                        self.print_info(f"wail_till() successful, callback response is '{callback_response}'")
                        self.print_info(f"Execution Time (HH:MM:SS): {elapsed_time_hms}")
                    return callback_response, elapsed_time_hms
                else:
                    pass
            # This block checks callback response matches with expected response and or custom_response, if so returns the func() response
            elif callback_response_bool == exp_func_resp:
                if is_logging_enabled:
                    self.print_info(f"wail_till() successful, callback response is '{callback_response_bool}'")
                    self.print_info(f"Execution Time (HH:MM:SS): {elapsed_time_hms}")
                return callback_response, elapsed_time_hms

            # This fail_func function will be called everytime callback func failed and timeout is > 0
            if fail_func and timeout > 0:
                fail_func()

        # Below this will be executed only when timeout reached.

        # if enable_log is True then callback response and time left in seconds will be printed
        if is_logging_enabled:
            self.print_info(
                f"wait_till() unsuccessful, function response was '{callback_response}' after waiting for '{max_wait_time} seconds' ")
            self.print_info(f"Execution Time (HH:MM:SS): {elapsed_time_hms}")

        # silent failure is True then this function will not raise timeout exception but returns the func() response
        if silent_failure:
            return callback_response, elapsed_time_hms

        # Raise timeout exception if silent_failure is set as false
        raise Exception(f"wait_till() - Waited {max_wait_time} seconds but the request timed out")

    def _parse_group(self, group):
        try:
            return int(group)
        except ValueError:
            return group

    @staticmethod
    def dut_model_edit(sw_model):
        """
        Function used to modify the model name from yaml file to accommodate the format used when creating a new template.
        :return: Modified switch template model.
        """
        if ('SwitchEngine' in sw_model or 'FabricEngine' in sw_model) and sw_model.count('_') == 1:
            return re.sub(r'(^[A-Z][a-z]*)([A-Z][a-z]*)(\d*[A-Z]|\d*)_(\d*[A-Z]*)$', r'\1 \2 \3-\4', sw_model)
        elif ('SwitchEngine' in sw_model or 'FabricEngine' in sw_model) and sw_model.count('_') == 2:
            return re.sub(r'(^[A-Z][a-z]*)([A-Z][a-z]*)(\d*[A-Z]|\d*)_(\d*[A-Z]*)_(\d*[A-Z]*)$',
                          r'\1 \2 \3-\4-\5', sw_model)
        elif ('SwitchEngine' in sw_model or 'FabricEngine' in sw_model) and sw_model.count('_') == 3:
            return re.sub(r'(^[A-Z][a-z]*)([A-Z][a-z]*)(\d*[A-Z]|\d*)_(\d*[A-Z]*)_(\d*[A-Z]*)_(\d*[A-Z]*)$',
                          r'\1 \2 \3-\4-\5-\6', sw_model)
        elif ('SwitchEngine' not in sw_model or 'FabricEngine' not in sw_model) and sw_model.count('_') == 1:
            return re.sub(r'(^[A-Z][a-z]*)([A-Z][a-z]*)(\d*[A-Z]|\d*)_(\d*[A-Z]*)$', r'\1 \2 \3-\4', sw_model)
        elif ('SwitchEngine' not in sw_model or 'FabricEngine' not in sw_model) and sw_model.count('_') == 2:
            return re.sub(r'(^[A-Z][a-z]*\d*)_(\d*[A-Z]*|\d*)_(\d*[A-Z]*|\d*)$', r'\1-\2-\3', sw_model)
        elif ('SwitchEngine' in sw_model or 'FabricEngine' in sw_model) and sw_model.count('_') == 3:
            return re.sub(r'(^[A-Z][a-z]*)([A-Z][a-z]*)(\d*[A-Z]|\d*)_(\d*[A-Z]*)_(\d*[A-Z]*)_(\d*[A-Z]*)$',
                          r'\1 \2 \3-\4-\5-\6', sw_model)

    def file_exists(self,file_name):
        """
          - This function will check whether mentioned file_name exists in the directory or not
          - Keyword Usage:
            `` File Exists  ${FILE_PATH}``

        :param file_name:  File Name in Current Directory or File Path
        :return: True if file exist else False
        """
        return os.path.isfile(file_name)


    def get_suite_resource_path(self, suite_file):
        """
        Get current test suite resource path.
        param suite_file: the full path of robot file, get via robot ${SUITE SOURCE}
        return: the Resource path
        example:
          suite_file is: extreme_automation_tests/Tests/Robot/Functional/XAPI/Location/TestCases/xapi_UploadFloorPlan_XIQ5401.robot
          suite resource path is: extreme_automation_tests/Tests/Robot/Functional/XAPI/Location/Resources
        """

        suite_resource_path = '/'.join(suite_file.split('/')[:-2]) + '/Resources'
        return suite_resource_path

    def get_feature_path(self, suite_file):
        """
        Get current test feature path.
        param suite_file: the full path of robot file, get via robot ${SUITE SOURCE}
        return: the feature full path
        example:
          suite_file is: extreme_automation_tests/Tests/Robot/Functional/XAPI/Location/TestCases/xapi_UploadFloorPlan_XIQ5401.robot
          feature path is: extreme_automation_tests/Tests/Robot/Functional/XAPI/Location
        """

        feature_path = '/'.join(suite_file.split('/')[:-2])
        return feature_path