import textwrap
import os
from html.parser import HTMLParser
import time
from ExtremeAutomation.Library.Logger.Logger import Logger
from ExtremeAutomation.Library.Utils.FileUtils import FileUtils
from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.IxiaDevice import IxiaDevice
import socket
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.TrafficGenerationApi import TrafficGenerationConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.TrafficGeneratingDeviceTrafficHelper import \
    TrafficGeneratingDeviceTrafficHelper
from ExtremeAutomation.Library.Device.TrafficGeneration.TrafficGeneratingDeviceStatisticHelper import \
    TrafficGeneratingDeviceStatisticHelper
from ExtremeAutomation.Library.Device.TrafficGeneration.TrafficGeneratingDeviceCaptureHelper import \
    TrafficGeneratingDeviceCaptureHelper
from ExtremeAutomation.Library.Utils.PathUtils import PathUtils
from ExtremeAutomation.Library.Utils.NumberUtils import NumberUtils
from ExtremeAutomation.Library.Utils.TableFormatter import TableFormatter
from ExtremeAutomation.Library.Device.Common.ManagedDeviceObject import ManagedDeviceObject


class IxLoadDevice(ManagedDeviceObject, TrafficGeneratingDeviceCaptureHelper, TrafficGeneratingDeviceStatisticHelper,
                   TrafficGeneratingDeviceTrafficHelper):
    def __init__(self):
        super(IxLoadDevice, self).__init__()
        self.initialized_load_device = False
        self.ix_load_ip = None
        self.dev = IxiaDevice()
        self.hostname = ""
        self._nameSpace = ""
        self.port = ""
        self.hostname = ""
        self.connection = None
        self.initialized = None
        self.dev = IxiaDevice()
        self.logger = Logger()
        self.start = {}
        self.parser = None
        self.result_file_name = None
        self.results_file_parsed = None
        self.guid = "00000-00000"  # set this to the test guid

    def connect(self, host, port=5680):
        self.dev.set_host_name(host)
        self.dev.set_port(port)
        if self.dev.connection is None:
            self.dev.connection = self.dev.agents[TrafficGenerationConstants.TELNET]
        if self.dev.connection.is_connected():
            return

        try:
            self.dev.connection.connect()
            reply = self.dev.connection.wait_until_quiet(1000)
            self.logger.log_debug(reply)
            self.init_connection()
        except socket.error:
            self.initialized = False

    def init_connection(self):
        if self.dev.initialized:
            return
        ret_string = self.dev.send_command("package require IxLoad")
        if "Already running maximum" in ret_string:
            self.logger.log_error("Turn off IxLoad GUI on " + self.dev.hostname +
                                  " Maximum instances of the application are loaded.")
            self.dev.disconnect()
            self.initialized = False
            self.connection = False
            raise Exception('Too many IxLoads running')
        self.dev.initialized = True
        self.initialized = True
        retries = 300
        index = 0
        while "8.10" not in ret_string and index < retries:
            ret_string += self.dev.connection.wait_until_quiet(180)
            index += 1
        self.logger.log_debug(ret_string)
        return ret_string

    def get_guid(self):
        return self.guid

    def set_guid(self, guid):
        self.guid = guid

    def get_traffic_helper(self):
        return self

    def get_statistic_helper(self):
        return self

    def get_capture_helper(self):
        return self

    def get_results_file_name(self):
        return self.result_file_name

    def set_results_file_name(self, file_name):
        self.result_file_name = file_name

    def send_command(self, cmd):
        return self.dev.send_command(cmd)

    def send_command_no_wait(self, cmd):
        return self.dev.send_command_no_wait(cmd)

    def read_console_no_wait(self):
        return self.dev.read_console_no_wait()

    def copy_file(self, file_name, remote_file_name):
        res = self.send_command("file mkdir \"" + os.path.dirname(remote_file_name) + "\" ")
        self.__check_and_throw_exeption("can't create", res, "Can not create directory on IxLoad Chassis ")
        res = self.send_command("set outfile [open \"" + remote_file_name + "\" w+]")
        self.__check_and_throw_exeption("couldn't open", res, "Can not create file on IxLoad Chassis")
        with open(file_name, "r") as myfile:
            lines = myfile.readlines()
        data = "".join(lines)
        data = data.replace("\\", "\\\\")
        data = data.replace("\"", "\\\"")
        data = data.replace("{", r"\{")
        data = data.replace("}", r"\}")
        data = data.replace("[", r"\[")
        data = data.replace("]", r"\]")
        data = data.replace('$', r'\$')
        data = data.replace('\n', '\\n')

        self.__start_timer("copy_file", "Starting the copy of " + file_name)
        lines = textwrap.wrap(data, 4048, drop_whitespace=False)
        escaped_char = ""
        line_num = 0
        for line in lines:
            line_num += 1
            if not escaped_char == "":
                line = escaped_char + line
                escaped_char = ""
            while line.endswith("\\"):
                escaped_char += line[-1]
                line = line[:-1]
            self.send_command("puts -nonewline $outfile  \"" + line + "\"")

        self.send_command("close $outfile")

        self.__end_timer("copy_file", "Finished the copy of " + file_name)

    # def copy_file(self, file_name, remote_file_name):
    #     self.send_command("set outfile [open \"" + remote_file_name + "\" w+]")
    #     with open(file_name, "r") as myfile:
    #         lines = myfile.readlines()
    #     escaped_char = ""
    #     line_num = 0
    #     for line in lines:
    #         if line.endswith("\n"):
    #             line = line[:-1]
    #         line = line.replace("\\", "\\\\")
    #         line = line.replace("\"", "\\\"")
    #         line = line.replace("{", "\{")
    #         line = line.replace("}", "\}")
    #         line = line.replace("[", "\[")
    #         line = line.replace("]", "\]")
    #         line = line.replace('$', '\$')
    #         line_num += 1
    #         if not escaped_char == "":
    #             line = escaped_char + line
    #             escaped_char = ""
    #         while line.endswith("\\"):
    #             escaped_char += line[-1]
    #             line = line[:-1]
    #         self.send_command("puts $outfile  \"" + line + "\"")
    #
    #     self.send_command("close $outfile")

    def run_config_file(self, file_name, test_name="Test Name", tester_name="Test Engineer"):
        end_file_name = os.path.basename(file_name)
        repo_name = "c:/temp/" + self.guid + "/" + end_file_name
        replace_hash = {}
        replace_hash["set logName"] = 'set logName "c:/temp/' + self.guid + '" '
        replace_hash["set rep_name"] = 'set rep_name "' + repo_name + '" '
        replace_hash["set ResultDir"] = 'set ResultDir "c:/temp/RESULTS/' + self.guid + '" '
        replace_hash["-testName"] = '-testName "' + test_name + '" \\'
        replace_hash["-testerName"] = '-testerName "' + tester_name + '" \\'
        replace_hash["-enableForceOwnership"] = '-enableForceOwnership true \\'
        self.copy_file(file_name, repo_name)
        tcl_path = os.path.join(PathUtils.get_project_root(), "ExtremeAutomation", "Library", "Device",
                                "TrafficGeneration", "Ixia", "IxLoadRun.tcl")
        self.play_tcl_file(tcl_path, replace_hash)

    def clean_up(self):
        self.__start_timer("clean_rxf_directory", "Cleaning remote directory")
        remote_directory = "c:/temp/RESULTS/" + self.guid
        self.dev.send_command("file delete -force \"" + remote_directory + "\"")
        remote_directory = "c:/temp/" + self.guid
        self.dev.send_command("file delete -force \"" + remote_directory + "\"")
        self.__end_timer("clean_rxf_directory", "Finished Cleaning remote directory")

    def copy_results_file(self, out_file_name):
        self.result_file_name = out_file_name
        # "c:/temp/RESULTS/"+guid+'reprun/IxLoad Detailed Report.html" '
        # self.play_tcl_file("Ixia/IxLoadRun.tcl", replace_hash)
        remote_file_name = "c:/temp/RESULTS/" + self.guid + "/IxLoad Detailed Report.html"
        self.__get_remote_file(remote_file_name, out_file_name)
        self.results_file_parsed = None

    def parse_results(self, file_name):
        with open(file_name, "r") as myfile:
            data = myfile.readlines()
        self.parser = IxLoadHTMLParser()
        self.parser.feed("".join(data).replace("&nbsp;", " "))
        self.parser.clear_empty_result_rows()
        self.parser.parse_out_tables()
        tables = self.parser.parsed_table_objects
        for tab in tables:
            self.logger.log_info("\n" + str(tab))
        self.results_file_parsed = file_name

    ############################################
    # ### checking the results #################
    ############################################

    def check_all_parsed_results_based_on_single_column(self, column_check, value_check, eval_str):
        if not self.results_file_parsed:
            self.parse_results(self.result_file_name)
        tables = self.parser.parsed_table_objects
        fault = False
        for tab in tables:
            headers = tab.get_headers()
            assert isinstance(tab, IxLoadResultTable)
            for col in headers:

                if eval(column_check):
                    values = tab.get_values(col)
                    row = 0
                    for val in values:
                        row_name = tab.get_value_row_col(0, row)
                        row += 1
                        value_checker = "NumberUtils.to_integer_value(val) " + eval_str + \
                                        " NumberUtils.to_integer_value(" + str(value_check) + ")"
                        if eval(value_checker):
                            fault = True
                            self.logger.log_error(tab.get_title() + ">>" + row_name + ">>" + str(col) +
                                                  " checker \"" + str(val) + "\" is \"" + eval_str + " " +
                                                  str(value_check))
        return fault

    def check_all_parsed_results_column_containing_value(self, in_column_name, numeric_value):
        column_name_check = "\"" + in_column_name + "\" in col.lower()"
        # value_check = "NumberUtils.to_integer_value(val) == NumberUtils.to_integer_value("+str(numeric_value)+")"
        return self.check_all_parsed_results_based_on_single_column(column_name_check, numeric_value, "=")

    def check_all_parsed_results_column_containing_value_greater_than(self, in_column_name, numeric_value):
        column_name_check = "\"" + in_column_name + "\" in col.lower()"
        # value_check = "NumberUtils.to_integer_value(val) > NumberUtils.to_integer_value("+str(numeric_value)+")"
        return self.check_all_parsed_results_based_on_single_column(column_name_check, numeric_value, ">")

    def check_all_parsed_results_column_containing_value_greater_than_2(self, in_column_name, numeric_value):
        if not self.results_file_parsed:
            self.parse_results(self.result_file_name)
        tables = self.parser.parsed_table_objects
        for tab in tables:
            headers = tab.get_headers()
            assert isinstance(tab, IxLoadResultTable)
            for col in headers:
                if in_column_name in col.lower():
                    values = tab.get_values(col)
                    row = 0
                    for val in values:
                        row_name = tab.get_value_row_col(0, row)
                        row += 1
                        if NumberUtils.to_integer_value(val) > NumberUtils.to_integer_value(numeric_value):
                            self.logger.log_error("In table \"" + tab.get_title() + "\" row \"" + row_name +
                                                  "\" the column \"" + str(col) + "\" is " + str(val) +
                                                  " which is should not be greater than " + str(numeric_value))

    def __start_timer(self, func, message):
        self.start[func] = time.time()
        self.logger.log_debug(message)

    def __end_timer(self, func, message):
        end = time.time()
        self.logger.log_debug(message + " elapsed:" + str(end - self.start[func]) + " seconds")

    def __get_remote_file(self, remote_file_name, out_file_name):
        # replace_hash["set ResultDir"] = 'set ResultDir "c:/temp/RESULTS/reprun/IxLoad Detailed Report.html" '
        # self.play_tcl_file("Ixia/IxLoadRun.tcl", replace_hash)
        self.__start_timer("get_remote_file", "Starting the copy of " + remote_file_name)

        directory_name = os.path.dirname(remote_file_name)
        res = self.send_command("expr {![catch {file lstat \"" + directory_name + "\" finfo}]}")
        self.__check_and_throw_exeption("0", res, "Results directory isn't there")

        finish_tag = "rxf file finished"
        found = False
        while not found:
            res = self.send_command("expr {![catch {file lstat \"" + remote_file_name + "\" finfo}]}")
            if res.startswith("1"):
                found = True

        self.send_command("set infile [open \"" + remote_file_name + "\" r]")
        res = self.send_command("set input [read $infile]\nset blah \"" + finish_tag + "\"")
        while "% " + finish_tag not in res:
            res += self.read_console_no_wait()

        # remove things around the res before writting
        res = res[0:res.index("% " + finish_tag)]
        try:
            FileUtils.write_str_to_file(out_file_name, res)
            self.logger.log_info("Saved file " + str(out_file_name))
        except Exception as e:
            self.logger.log_error("could not save file " + str(out_file_name))
            self.logger.log_debug(e)

        self.__end_timer("get_remote_file", "Finished the copy of " + remote_file_name)

    # this is depreciated
    def play_tcl_file(self, file_name, replace_hash=None, end_test="IxLoadRun finished"):
        res = ""
        if not replace_hash:
            replace_hash = {"-enableForceOwnership": '-enableForceOwnership true \\'}

        self.__start_timer("play_tcl_file", "Starting the TCL file")
        # load file
        #  remove \\n
        # send line by line, look for exception returned.
        with open(file_name, "r") as myfile:
            data = myfile.readlines()
        temp_data = []
        line_temp = ""
        for line in data:
            line = line.rstrip()
            if line.strip().startswith("#") or line.strip() == "":
                # or line.strip() == "if [catch {"  or line.strip() == "}] {" or line.strip() == "}":
                continue
            for key in replace_hash:
                if line.strip().startswith(key):
                    line = replace_hash[key]
            line_temp += line
            if not line.endswith("\\"):
                temp_data.append(line_temp)
                line_temp = ""
            else:  # remove \
                line_temp = line_temp[:-1]
        if not line_temp == "":
            temp_data.append(line_temp)
        for line in temp_data:
            if "::IxLoad connect" in line:
                res = self.send_command(line)
                # check for not connecting.
            else:
                res = self.send_command_no_wait(line)
            self.__check_and_throw_exeption("'exceptions.Exception'", res, "Test Exception")
            self.__check_and_throw_exeption("Err running the tcl script", res, "Test Exception. check output.")
            self.__check_and_throw_exeption("Already running maximum allowed copies of IxLoad", res,
                                            "Already running maximum allowed copies of IxLoad")

            # raw_input('Hit enter after line')
        test_finished = False
        while not test_finished:
            res += self.read_console_no_wait()
            if end_test in res:
                test_finished = True

        self.__end_timer("get_remote_file", "Finished the TCL file.")

    def __check_and_throw_exeption(self, sub, _str, message):
        if sub in _str:
            self.logger.log_error(message)
            raise Exception(message)


class IxLoadHTMLParser(HTMLParser):
    def __init__(self):
        super(IxLoadHTMLParser, self).__init__()
        self.reset()
        self.table = []
        self.table_cell_start = False
        self.current_row = []
        self.current_cell = ""
        self.parsed_table_objects = []

    def handle_starttag(self, tag, attrs):
        # print("Encountered a start tag:", tag)
        if str(tag).lower() == "table":
            pass
        if str(tag).lower() == "tr":
            self.current_row = []
        if str(tag).lower() == "td":
            self.table_cell_start = True
            self.current_cell = ""

    def handle_endtag(self, tag):
        # print("Encountered an end tag :", tag)
        if str(tag).lower() == "table":
            pass
        if str(tag).lower() == "tr":
            # if len(self.current_row)>=1 and self.current_row[0] == '':
            #     self.current_row = self.current_row[1:]
            self.table.append(self.current_row)
        if str(tag).lower() == "td":
            self.current_row.append(self.current_cell)
            self.table_cell_start = False

    def handle_data(self, data):
        # print("Encountered some data  :", data)
        if self.table_cell_start:
            self.current_cell += data.strip()
            if "," in self.current_cell and self.current_cell.replace(",", "").isdigit():
                self.current_cell = self.current_cell.replace(",", "")

    def clear_empty_result_rows(self):
        tt = self.table
        length = len(tt)
        index = 0
        while index < length:
            row = tt[index]
            boo = False
            for cell in row:
                if cell != '':
                    boo = True
            if not boo:
                tt[index] = ""
            index += 1
        # self.table = filter(None, self.table)
        pass

    def parse_out_tables(self):
        tt = self.table
        length = len(tt)
        index = 0
        while index + 4 < length:
            # if "TCP Analysis" in tt[index]:
            #     print("found")

            # header title
            # empty
            # header labels
            # empty
            # value1
            # value2
            # valuen
            if self.__is_header_title(tt[index]) and \
                    self.__is_empty(tt[index + 1]) and \
                    self.__is_header_labels(tt[index + 2]) and \
                    self.__is_empty(tt[index + 3]) and \
                    self.__is_values(tt[index + 4]):
                tab = IxLoadResultTable()
                tab.set_title(self.__trim_leading_empty(tt[index])[0])
                tab.set_headers(self.__trim_leading_empty(tt[index + 2]))
                tab.add_row(self.__trim_leading_empty(tt[index + 4]))
                index += 5
                while index < length and self.__is_values(tt[index]):
                    tab.add_row(self.__trim_leading_empty(tt[index]))
                    index += 1
                self.parsed_table_objects.append(tab)

            # header title
            # header labels
            # header labels
            # value1
            # value2
            # valuen
            elif self.__is_header_title(tt[index]) and \
                    self.__is_header_labels(tt[index + 1]) and \
                    self.__is_header_labels(tt[index + 2]) and \
                    self.__is_values(tt[index + 3]):
                tab = IxLoadResultTable()
                tab.set_title(self.__trim_leading_empty(tt[index])[0])
                headers = list()
                headers.append(self.__trim_leading_empty(tt[index + 1])[0])
                headers.extend(self.__trim_leading_empty(tt[index + 2]))
                tab.set_headers(headers)
                tab.add_row(self.__trim_leading_empty(tt[index + 3]))
                index += 4
                while index < length and self.__is_values(tt[index]):
                    tab.add_row(self.__trim_leading_empty(tt[index]))
                    index += 1
                self.parsed_table_objects.append(tab)
            else:
                index += 1
        pass

    @staticmethod
    def __is_header_title(l):
        if not isinstance(l, list):
            return False
        num_strings = 0
        num_int = 0
        for el in l:
            if len(el) >= 1:
                if el.isdigit():
                    num_int += 1
                elif len(el) < 100:
                    num_strings += 1
                else:
                    pass
        return num_strings == 1 and num_int == 0

    @staticmethod
    def __is_header_labels(l):
        if not isinstance(l, list):
            return False
        num_strings = 0
        num_int = 0
        for el in l:
            if len(el) >= 1:
                if el.isdigit():
                    num_int += 1
                else:
                    num_strings += 1
        return num_strings > 1 and num_int == 0

    def __is_values(self, l):
        if not isinstance(l, list):
            return False
        num_strings = 0
        num_int = 0
        for el in l:
            if len(el) >= 1:
                if self.__is_digit(el):
                    num_int += 1
                else:
                    num_strings += 1
        return num_int >= 1

    @staticmethod
    def __is_digit(num):
        return (num.replace(".", "").replace(",", "")).isdigit()

    @staticmethod
    def __is_empty(_str):
        return isinstance(_str, str) and _str == ""

    @staticmethod
    def __trim_leading_empty(l):
        if not isinstance(l, list):
            return l
        return filter(None, l)


class IxLoadResultTable(object):
    def __init__(self):
        self.title = None
        self.headers = None
        self.values = []

    def add_row(self, row):
        self.values.append(row)

    def set_title(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def set_headers(self, headers):
        self.headers = headers

    def get_headers(self):
        return self.headers

    def get_values(self, column_name):
        _id = self.headers.index(column_name)
        ret_ar = []
        for el in self.values:
            ret_ar.append(el[_id])
        return ret_ar

    def get_value(self, column_name, row_id):
        _id = self.headers.index(column_name)
        return self.values[row_id][_id]

    def get_value_row_col(self, column_id, row_id):
        return self.values[row_id][column_id]

    def __str__(self):
        # print("Name:" + self.title)
        table = TableFormatter()
        i = 0
        while i < len(self.values):
            h = 0
            while h < len(self.headers):
                try:
                    table.add_row_value(self.headers[h], str(self.values[i][h]))
                except (KeyError, IndexError):
                    table.add_row_value(self.headers[h], "n/a")
                h += 1
            i += 1
        return self.title + table.to_table_string()
