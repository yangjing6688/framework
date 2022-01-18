import os
import time
import datetime
import configparser

project_name = 'ExtremeAutomation'


def insert_bracket(str_header):
    """
    Add "{" "}" into header name to convert it to variable name
    :param str_header:
    :return:
    """
    var_name = str(str_header)
    var_name = var_name[0] + '{' + var_name[1:] + '}'
    return var_name


def slice_dict(ori_dict, prefix):
    """

    :param ori_dict:
    :param prefix:
    :return:
    """
    return {key: value for key, value in ori_dict.items() if key.startswith(prefix)}


def current_time():
    """

    :return:
    """
    time.sleep(2)
    return datetime.datetime.now().strftime('%Y%m%d-%H%M%S')


def stamp_time_output(output_type, cur_time):
    """

    :param output_type:
    :param cur_time:
    :return:
    """
    ext = 'xml' if output_type == 'output' else 'html'
    return '.'.join(['-'.join([output_type, cur_time]), ext])


def detect_abs_dir(abspath):
    """

    :param abspath:
    :return:
    """
    return str(abspath).split(str(project_name))[0]


class Conf(object):
    def __init__(self, conf_dir_abspath):
        self.conf_path = conf_dir_abspath
        self.conf = self.load_conf()

    def load_conf(self):
        """
        """
        return os.path.join(self.conf_path, "config.ini")

    def get_conf(self, section, option):
        """
        """
        cf = configparser.ConfigParser()

        try:
            cf.read(self.conf)
            return cf.get(section, option)
        except configparser.NoSectionError as err:
            # TODO replace print(command to log)
            print("The configuration:\"%s\" doesn't exist!" % section, err)
        except configparser.NoOptionError as err:
            print("The option:\"%s\" doesn't exist in section \"%s\"!" % (section, option), err)

    def get_conf_sections(self, section):
        """
        """
        cf = configparser.ConfigParser()
        try:
            cf.read(self.conf)
            return cf.options(section)
        except configparser.NoSectionError as err:
            print("The configuration:\'%s\' doesn't exist!" % section, err)

    def get_abs_path(self, section, option):
        """
        """
        cf = configparser.ConfigParser()
        try:
            cf.read(self.conf)
            option_path = cf.get(section, option)
            abs_dir = detect_abs_dir(self.conf_path)
            return os.path.join(abs_dir, option_path)
        except configparser.NoSectionError as err:
            print("The configuration:\"%s\" doesn't exist!" % section, err)
        except configparser.NoOptionError as err:
            print("The option:\"%s\" doesn't exist in section \"%s\"!" % (section, option), err)

    def get_test_data_abs_path(self, file_name):
        """
        """
        cf = configparser.ConfigParser()
        try:
            cf.read(self.conf)
            data_path = cf.get('csv_data_fie', file_name)
            abs_dir = detect_abs_dir(self.conf_path)
            return os.path.join(abs_dir, data_path)
        except configparser.NoOptionError as err:
            print("The option:\"%s\" doesn't exist in section 'csv_data_files!" % file_name, err)

    def get_test_case_abs_path(self, test_case_name):
        """
        """
        cf = configparser.ConfigParser()
        try:
            cf.read(self.conf)
            test_case = cf.get('test_cases', test_case_name)
            return os.path.join(self.conf_path, test_case)
        except configparser.NoOptionError as err:
            print("The option:\"%s\" doesn't exist in section 'csv_data_files!" % test_case_name, err)
