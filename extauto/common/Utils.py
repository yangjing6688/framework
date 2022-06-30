import re
import random
import string
from datetime import datetime, timedelta
from extauto.common.Logging import Logging
from robot.libraries.BuiltIn import BuiltIn
from selenium.common.exceptions import NoSuchElementException
from extauto.common.ConfigFileHelper import ConfigFileHelper
import time


class Utils:
    def __init__(self):
        self.logger = Logging().get_logger()
        self.cfgHelp = ConfigFileHelper()
        self.cfgHelp.checkConfigRefresh()

    def get_config_value(self, conf_str):
        """
        - Get the config value of a variable
        - Keyword Usage:
         - ``Get Config Value   VARIABLE``

        :param conf_str: Variable name
        :return: value of the variable
        """

        toast = BuiltIn().get_variable_value("${" + conf_str + "}")
        self.print_log("Toast Message For ", conf_str, " : ", toast)
        return toast

    def grep(self, output_buffer, search_str):
        """
        - greps the second variable in the first string
        - Keyword Usage:
         - ``Grep   ${OUTPUT}     Version``

        :param output_buffer: Buffer in which we grep for search_str
        :param search_str: search string which will be looked inside output_buffer for a match
        :return: returns 1 if finds a match else 0
        """

        self.print_log("Searching for : ", search_str, " in : ", output_buffer)
        if search_str in output_buffer:
            self.print_log("Found Match")
            return 1
        else:
            self.print_log("No Match Found")
            return 0

    def get_random_string(self, length="default"):
        """
        - Get the random string of specified length, default length is 10 characters
        - Keyword Usage:
         - ``Get Random String``
         - ``Get Random String   length=5``

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
         - ``Get Random Integer``

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
         - ``Get Random Mac``
         - ``Get Random Mac   delimiter=:``

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
         - ``Get Random Ip``

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
         - ``Look and Feel   Screen1.png     Screen2.png    Screen3.png``

        :param first: screenshot or image 1
        :param second: screenshot or image 2
        :param third: screenshot or image 3
        :return: returns none
        """

        print ("*HTML* " \
              "<a href=" + first + "> <img src=" + first + " width=\"500px\"></a> " \
                "<a href=" + second + "> <img src=" + second + " width=\"500px\"></a> " \
                "<a href=" + third + "> <img src=" + third + " width=\"500px\"></a>")

    def decode_to_ascii(self, _str):
        """
        - decode given string to ascci
        - Keyword Usage:
         - ``Decode To Ascii   ${STR}``

        :param _str: str to decode to ascci
        :return: decoded string
        """
        self.print_info("Input value: ", _str)
        return str(_str.encode('utf-8').decode('ascii', 'ignore'))

    def special_char_check(self, _str):
        """
        - check the special character in the given string
        - Keyword Usage:
         - ``Special CHar Check   ${STR}``

        :param _str: str to check the special character
        :return: 0 if special character exists else 1
        """
        self.print_info("Input value: ", _str)
        if re.match("^[a-zA-Z0-9_-]*$", _str):
            return 0
        else:
            return 1

    def check_match(self, target_string, match):
        """
        - Check the match string in the target string
        - Keyword Usage:
         - ``Check Match  ${TARGET_STRING}   ${MATHC}``

        :param target_string:  target string
        :param match: search string in the target string
        :return: 1 if match string in target string else -1
        """
        self.print_log("Searching for : ", match, " in :", target_string)
        if match in target_string:
            return 1
        else:
            return -1

    def print_log(self, *words):
        """
        - prints the given list of words in to console and robot framework log.html file
        - Note this is not a keyword to use inside the robot framework script. only used in libs
        """

        line = ""
        for word in words:
            line += str(word)

        if "DEBUG" in line:
            BuiltIn().log_to_console(line)

        if "INFO" in line:
            BuiltIn().log_to_console(line)

    def print_error(self, *words):
        """
        - prints the given list of words in to console and robot framework log.html file
        - Note this is not a keyword to use inside the robot framework script. only used in libs
        """

        line = ""
        for word in words:
            line += str(word)

        self.logger.error(line)
        test_name = BuiltIn().get_variable_value("${TEST_NAME}")
        BuiltIn().log_to_console("\n" + test_name + ": " + line)

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

        self.logger.warning(line)

        try:
            test_name = BuiltIn().get_variable_value("${TEST_NAME}")
            BuiltIn().log_to_console("\n" + test_name + ": " + line)
        except TypeError:
            pass

    def print_info(self, *words):
        """
        - prints the given list of words in to console and robot framework log.html file
        - Note this is not a keyword to use inside the robot framework script. only used in libs
        """

        line = ""
        for word in words:
            line += str(word)

        self.logger.info(line)
        test_name = BuiltIn().get_variable_value("${TEST_NAME}")
        if test_name:
            BuiltIn().log_to_console("\n" + test_name + ": " + line)
        else:
            BuiltIn().log_to_console("\n" + ": " + line)

    def print_debug(self, *words):
        """
        - prints the given list of words in to console and robot framework log.html file
        - Note this is not a keyword to use inside the robot framework script. only used in libs
        """

        line = ""
        for word in words:
            line += str(word)
        if "DEBUG" in BuiltIn().get_variable_value("${LOG_LEVEL}"):
            BuiltIn().log_to_console(line)

    def has_number(self, input_string):
        """
        - check the input string has the digit on it
        - Keyword Usage:
         - ``Has Number  ${INPUT_STRING}``

        :param input_string:
        :return: True if digit in input string else False
        """
        return any(char.isdigit() for char in input_string)

    def get_utc_time_difference(self, t1, t2):
        """
        - Get the time difference between t2 and t1
        - Keyword Usage:
         - ``Get Utc Time Difference   ${TIME1}  ${TIME2}``

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
         - ``Get Current Time``

        :return: current time
        """
        self.print_info("datetime.now()", datetime.now())
        return datetime.now()

    def get_current_time_in_sec(self):
        """
        - Get the Current Time in Sec
        - Keyword Usage:
        - ``Get Current Time In Sec``

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

        output_folder = BuiltIn().get_variable_value("${OUTPUT DIR}")

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
         - ``Get Device Time        ${CLI_OUTPUT}``

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
         - ``Get Device Date       ${CLI_OUTPUT}``
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
         - if utc time is:         utc_time        = 2020-04-24 03:12:04.905116
         - utc time after delta    utc_after_10min = 2020-04-25 03:12:04.905116

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
         - if utc time :           utc_time        = 2020-04-24 03:12:04.905116
         - utc time after delta    utc_after_10min = 2020-04-24 03:23:09.519271

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

    def get_half_of(self, _time):
        """
        - This method accepts time in minutes divides by 2 and returns the value

        :param _time: in minutes
        :return:
        """
        half = (int(_time) * 60) / 2

        self.print_info("Returning Half time: ", half, " seconds for: ", _time, " minutes")

        return half

    def split_string_into_3_parts(self, info):
        """
        - This keyword splits a string in to 3 equal parts
        :param info: input string
        :return: returns 3 strings by dividing the input string
        """
        self.print_info("Input String: ", info)

        length = len(info)
        seg1 = round(length/3)
        part1 = info[:seg1]
        seg2 = seg1*2
        part2 = info[seg1:seg2]
        part3 = info[seg2:]
        return part1, part2, part3

    def get_first_half_of_mac(self, mac):
        """
        - This keyword returns the first half of a MAC
        :param mac: MAC
        :return: returns first half of MAC
        """
        self.print_info("Input MAC: ", mac)
        length = len(mac)
        seg = round(length / 2)
        mac_first_half = mac[:seg]
        return mac_first_half

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

    def get_second_half_of_network_policy(self, net):
        lenght = len(net)
        seg = round(lenght / 2)
        net_secondhalf = net[seg:]
        return net_secondhalf

    def get_last_6_digts_of_MAC(self, mac):
        length = len(mac)
        st = length - 6
        remaining_mac = mac[st:]
        return remaining_mac

    def get_second_half_of_MAC(self, mac):
        length = len(mac)
        seg = round(length / 2)
        mac_second_half = mac[seg:]
        return mac_second_half

    def convert_MAC_to_upper(self, mac):
        upper_case = mac.upper()
        return upper_case

    def convert_MAC_to_lower(self, mac):
        lower_case = mac.lower()
        return lower_case

    def convert_mac_to_random_case(self, mac):
        random_case = ""
        for i in mac:
            if i.isalpha():
                rand1 = random.randint(1, 2)
                if rand1 == 1:
                    random_case = random_case + i.lower()
                else:
                    random_case = random_case + i.upper()
            else:
                random_case = random_case + i
        return random_case

    def partial_ip(self, ip):
        length = len(ip)
        length -= 2
        ip = ip[:length]
        return ip

    def switch_to_default(self, driver):
        """
        -This keyword Will Switch to default frame
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
        -This keyword Will Switch to iframe
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
         - `` Date Time Addition  date_time=2020-10-20 12:03:47    days=5     hours=13    minutes=4      seconds=2``

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

        self.print_debug(f"**** Milliseconds Converted To Days/Hours/Minutes/Seconds ****")
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
        -  Keyword Usage:
        - `` Get Current Time In Milliseconds``
        :return: time in milliseconds
        """
        timestamp = int(time.time())
        self.print_info("Current time in milliseconds: ", timestamp)
        return timestamp

    def convert_time_to_milliseconds(self, time_str):
        """
        - This keyword converts given time to milliseconds.
        -  Keyword Usage:
        - `` Convert Time To Milliseconds 12:03:47``
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
        -  Keyword Usage:
        - `` Get Time Difference In Milliseconds  1622696034870  24:03:47``
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

    def _parse_group(self, group):
        try:
            return int(group)
        except ValueError:
            return group