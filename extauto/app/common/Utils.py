import re
import random
import string
from datetime import datetime, timedelta
from extauto.common.Logging import Logging
from robot.libraries.BuiltIn import BuiltIn
import os
import csv
import subprocess
import time


class Utils:
    def __init__(self):
        self.logger = Logging().get_logger()

    def get_config_value(self, conf_str):
        toast = BuiltIn().get_variable_value("${" + conf_str + "}")
        self.print_log("Toast Message For ", conf_str, " : ", toast)
        return toast

    def grep(self, output_buffer, search_str):
        self.print_log("Searching for : ", search_str, " in : ", output_buffer)
        if search_str in output_buffer:
            self.print_log("Found Match")
            return 1
        else:
            self.print_log("No Match Found")
            return 0

    def get_now(self):
        return datetime.now().strftime("%Y-%m-%d-%H-%M")

    def get_random_string(self, length="default"):
        if length == "default":
            length = 10
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(int(length)))

    def get_random_integer(self, length="default", lower_limit="default", upper_limit="default"):
        if upper_limit == "default":
            upper_limit = 999999999
        if lower_limit == "default":
            lower_limit = 9999
        if length == "default":
            length = 10
        return random.randrange(lower_limit, upper_limit, length)

    def get_random_mac(self, delimiter="default"):
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
        ip = [random.randint(10, 100), random.randint(0, 253), random.randint(0, 253), random.randint(0, 100)]
        ip_temp = '.'.join(map(lambda x: "%s" % x, ip))
        print (ip_temp + "/" + '24')
        return ip_temp + '/' + '24'

    def look_and_feel(self, first, second, third):
        print ("*HTML* " \
              "<a href=" + first + "> <img src=" + first + " width=\"500px\"></a> " \
                "<a href=" + second + "> <img src=" + second + " width=\"500px\"></a> " \
                "<a href=" + third + "> <img src=" + third + " width=\"500px\"></a>")

    def decode_to_ascii(self, _str):
        return str(_str.encode('utf-8').decode('ascii', 'ignore'))

    def special_char_check(self, _str):
        if re.match("^[a-zA-Z0-9_-]*$", _str):
            return 0
        else:
            return 1

    def check_match(self, target_string, match):
        self.print_log("Searching for : ", match, " in :", target_string)
        if match in target_string:
            return 1
        else:
            return -1

    def print_log(self, *words):
        line = ""
        for word in words:
            line += str(word)

        if "DEBUG" in line:
            BuiltIn().log_to_console(line)

        if "INFO" in line:
            BuiltIn().log_to_console(line)

    def print_error(self, *words):
        line = ""
        for word in words:
            line += str(word)

        self.logger.error(line)
        test_name = BuiltIn().get_variable_value("${TEST_NAME}")
        BuiltIn().log_to_console("\n" + test_name + ": " + line)

    def print_warning(self, *words):
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
        line = ""
        for word in words:
            line += str(word)
        if "DEBUG" in BuiltIn().get_variable_value("${LOG_LEVEL}"):
            BuiltIn().log_to_console(line)

    def has_number(self, input_string):
        # Check the string contains the number or not
        return any(char.isdigit() for char in input_string)

    def compare_lists(self, list1, list2):
        self.print_info("List1 ", list1)
        self.print_info("List2 ", list2)

        if len(list1) == len(list2):
            for i in range(len(list1)):
                if list1[i].upper() == list2[i].upper():
                    return 1
        return -1

    def get_random_value(self, _min, _max):
        return random.randint(int(_min), int(_max))

    def get_incremented_number(self, number, incr):
        return int(number) + int(incr)

    def get_random_vlan(self):
        return random.randint(int(2), int(4091))

    def get_random_vlan_string(self):
        vlan = random.randint(int(2), int(4091))
        vlan_string = "AUTO_" + str(vlan)
        return vlan, vlan_string

    def get_utc_time_difference(self, t1, t2):
        """
        Get the time difference between t2 and t1
        :param t1: datetime.datetime object
        :param t2: datetime.datetime object
        :return:
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

    def get_time_difference(self, t1, t2):
        """
        Get the time difference
        time format should be "5/25/2019, 4:36:54 PM"
        """
        t1 = datetime.strptime(t1, '%m/%d/%Y, %I:%M:%S %p')
        t2 = datetime.strptime(t2, '%m/%d/%Y, %I:%M:%S %p')
        delta = t2 - t1
        return delta.total_seconds()

    def get_current_time(self):
        print ("datetime.now()", datetime.now())
        return datetime.now()

    def include_image(self, file_name):
        output_folder = BuiltIn().get_variable_value("${OUTPUT DIR}")
        # file_name = str(int(time.time())) + ".png"
        file_path = output_folder + "/" + file_name

        print("*HTML* <a href=" + file_name + "> <img src=" + file_name
              + " width=\"600px\" style=\"border:5px solid red\"></a>")

        return file_name

    def log_to_report(self, file_name):
        win_host = BuiltIn().get_variable_value("${WINDOWS10}")
        self.print_info("Windows Host: ", win_host)
        self.print_info("File Name: ", file_name)
        print ("*HTML* <a href=" + "http://" + win_host + "/" + file_name + ".avi>Video Record</a>")

    def get_bulk_user_credentials(self, filename):
        """
        Get the bulk user credentials stored in csv file
        :param filename: credential dict
        :return:
        """
        file_path = os.path.dirname(__file__) + '/tools/credentials/' + filename
        user_credentials = {}
        with open(file_path) as f:
            csv_reader = csv.DictReader(f)
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                user_credentials[row["User Name"]] = row["Access Key"]
                line_count += 1
        self.print_info(user_credentials)
        return user_credentials

    def get_device_time(self, output):
        return re.search('[0-9]+:[0-9]+', output).group(0)

    def get_device_date(self, s):
        """
        This method reads the date in
        :param s:
        :return:
        """
        self.print_info("Date in MM/DD/YYY format: ", )
        d = re.search('([1-9]+ )', s).group(1).strip()
        m = re.search('([1-9]+)-', s).group(1).strip()
        y = re.search('([0-9]{4})', s).group(1).strip()

        self.print_info("Date in MM/DD/YYY format: ", m + "/" + d + "/" + y)
        return m + "/" + d + "/" + y

    def round_time(self, upgrade_time):
        """
        This method expects time format as 24 Hours
        Converts it in to AM or PM
        This is specific to XIQ UI behavior
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
        This method expects time format as HH:MM AM or HH:MM PM
        Converts it in to 24 Hour time format
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

    def get_current_date_time(self):
        """
        Get current date with %Y-%m-%d %H:%M format
        :return:
        """
        now = datetime.now()
        date_time = now.strftime("%Y-%m-%d %H:%M")
        self.print_info("Current Date Time is", date_time)
        return date_time

    def get_previous_time_delta(self, t1, hour=None, minutes=None, time_format='%Y-%m-%d %H:%M'):
        """
        Get last specified time delta
        Example:
        if  t1='2020-05-19 03:57'  last_24_hour_time=''2020-05-18 03:57''

        :param t1: present time
        :param hour: time in hour to get the previous time
        :param minutes:  time in Minutes to get the previous time
        :param time_format:
        :return:
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
        Get the utc time with specified time format, by default %Y-%m-%d %H:%M.%s
        :param time_format:
        :return:
        """
        utc_time = datetime.utcnow()
        self.print_info("Current UTC Time is:{}".format(utc_time))
        if time_format:
            return utc_time.strftime(time_format)
        else:
            return utc_time

    def get_utc_hour_time_delta(self, utc_time, hour=24):
        """
        Get the utc time after the specified time delta in hour
        EX:
        if utc time is:         utc_time        = 2020-04-24 03:12:04.905116
        utc time after delta    utc_after_10min = 2020-04-25 03:12:04.905116
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
        Get the utc time after the specified time delta in minutes
        EX:
        if utc time :           utc_time        = 2020-04-24 03:12:04.905116
        utc time after delta    utc_after_10min = 2020-04-24 03:23:09.519271
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
        Countdown in minutes
        :param t: time to count down
        :return:
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
        self.print_info(" count down:{} Minutes Completed", format(t))

    def start_selenium_grid_hub(self, host):
        """
        Start the selenium grid hub
        :return:
        """
        cmd = "ps -ax | grep 'selenium-server-standalone'"
        # check the grid is running or not
        status = self.execute_subprocess_cmd(cmd, "selenium-server-standalone.jar")
        if status:
            self.print_info("Grid is Running", status)
            return 1
        else:
            basepath = os.path.dirname(__file__)
            relative_path = basepath + "/../tools/"
            hub_cmd = "java -jar " + relative_path + "selenium-server-standalone.jar -role hub -host " + host
            pr = subprocess.Popen(hub_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            status = self.execute_subprocess_cmd(cmd, "selenium-server-standalone.jar")
            if status:
                self.print_info("Grid is Running", status)
                return 1

        return -1

    def get_half_of(self, _time):
        """

        This method accepts time in minutes divides by 2 and returns the value
        :param _time: in minutes
        :return:
        """
        half = (int(_time) * 60) / 2

        self.print_info("Returning Half time: ", half, " seconds for: ", _time, " minutes")

        return half

    @staticmethod
    def execute_subprocess_cmd(cmd, search_string):
        """
        Execute command in the new process
        :param cmd:
        :param search_string:
        :return:
        """
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        for line in process.stdout:
            if re.search(search_string, line.decode()):
                return line

    def split_string_into_3_parts(self, info):
        lenght = len(info)
        seg1 = round(lenght/3)
        part1 = info[:seg1]
        seg2 = seg1*2
        part2 = info[seg1:seg2]
        part3 = info[seg2:]
        return part1, part2, part3

    def get_first_half_of_MAC(self, MAC):
        lenght = len(MAC)
        seg = round(lenght / 2)
        MAC_firsthalf = MAC[:seg]
        return MAC_firsthalf

    def get_first_half_of_network_policy(self, net):
        lenght = len(net)
        seg = round(lenght / 2)
        net_firsthalf = net[:seg]
        return net_firsthalf
    def get_second_half_of_network_policy(self, net):
        lenght = len(net)
        seg = round(lenght / 2)
        net_secondhalf = net[seg:]
        return net_secondhalf

    def get_last_6_digts_of_MAC(self, MAC):
        length = len(MAC)
        st = length - 6
        remaining_MAC = MAC[st:]
        return remaining_MAC

    def get_second_half_of_MAC(self, MAC):
        lenght = len(MAC)
        seg = round(lenght / 2)
        MAC_secondhalf = MAC[seg:]
        return MAC_secondhalf

    def convert_MAC_to_upper(self, MAC):
        upper_case = MAC.upper()
        return upper_case

    def convert_MAC_to_lower(self, MAC):
        lower_case = MAC.lower()
        return lower_case

    def convert_MAC_to_random_case(self, MAC):
        random_case = ""
        for i in MAC:
            if i.isalpha():
                rand1 = random.randint(1, 2)
                if rand1 == 1:
                    random_case = random_case + i.lower()
                else:
                    random_case = random_case + i.upper()
            else:
                random_case = random_case + i
        return random_case

    def partial_IP(self, IP):
        length = len(IP)
        length -= 2
        IP = IP[:length]
        return IP

