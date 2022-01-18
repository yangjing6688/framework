import os
from optparse import OptionParser
from robot.api import TestData
from robot.api import ResultWriter
from robot.api import TestSuiteBuilder
from robot.result import ExecutionResult
from robot.running.model import Variable
from ExtremeAutomation.Library.Logger.Logger import Logger
from ExtremeAutomation.Utilities.DataDriven.DataDrivenData import DataDrivenData
from ExtremeAutomation.Utilities.DataDriven.DataDrivenCommon import Conf


class DataDrivenExecution(object):
    @staticmethod
    def execute_data_driven_test(suite_path, data_files, suite_name,
                                 environment, log_directory, listenerv2, listenerv3, dry_run):
        suite_dir_path = suite_path
        files_in_config = False

        # If any of the neccessary variables equals None then the config.ini
        # needs to exist and be loaded.
        if data_files is None or suite_name is None or environment is None:
            suite_conf = Conf(suite_dir_path)

        # If data_files or suite_name equal None, use the proper section of
        # config.ini.
        if data_files is None:
            data_files = suite_conf.get_conf_sections('csv_data_files')
            files_in_config = True
        if suite_name is None:
            suite_name = suite_conf.get_conf('suite_name', 'SUITENAME')

        # Test Suite Initialization
        test_suite = TestSuiteBuilder().build(os.path.join(suite_dir_path,
                                              '__init__.robot'))
        test_suite.name = suite_name
        resource_file = TestData(source=os.path.join(suite_dir_path,
                                                     "__init__.robot"))
        keyword_args = resource_file.keyword_table.keywords[0].args.value
        count = 1

        for i, _file in enumerate(data_files):
            # If environment is not provided use config.ini for
            # TESTBEDVARIABLE, otherwise use provided environment
            if environment is None:
                testbed_var = None
                testbed_var_path = suite_conf.get_conf('testbed_var',
                                                       'TESTBEDVARIABLE')
                if testbed_var_path is not None:
                    if testbed_var_path != os.path.realpath(testbed_var_path):
                        cwd = os.getcwd()
                        environment = os.path.join(cwd, testbed_var_path)
                    testbed_var_path = testbed_var_path.replace("\\", "/")
                    testbed_var = Variable('${TestBedVariable}',
                                           testbed_var_path)
                    test_suite.resource.variables.append(testbed_var)
            else:
                if environment != os.path.realpath(environment):
                    cwd = os.getcwd()
                    environment = os.path.join(cwd, environment)

                environment = environment.replace("\\", "/")
                testbed_var = Variable('${TestBedVariable}', environment)
                test_suite.resource.variables.append(testbed_var)

            # if files were provided in the config.ini use old method. If not,
            # assume you have a list of absolute paths.
            if files_in_config is True:
                test_data = DataDrivenData(suite_conf.get_abs_path('csv_data_files',
                                                                   data_files[i])).generate_test_data()
            else:
                test_data = DataDrivenData(data_files[i]).generate_test_data()

            for row in test_data:
                test_case_name = row["NAME"]
                if files_in_config is True:
                    test = test_suite.tests.create(_file + "." +
                                                   test_case_name)
                else:
                    test = test_suite.tests.create("TESTDATA00" + str(count) + ":" +
                                                   data_files[count-1].split("\\")[-1] +
                                                   " TEST_CASE_NAME: " + test_case_name)
                args = [row[i.replace("{", "").replace("}", "")] for i in keyword_args]
                test.keywords.create(row["TEST_CASE"], args=args)
            count += 1

        # If the log directory is not specified by the user default to the provided config.ini/__init__.py location.
        if log_directory is None:
            output_dir = suite_dir_path
        else:
            output_dir = log_directory

        output_xml_path = os.path.join(output_dir, "output.xml")

        if listenerv2 and listenerv3:
            if dry_run is not None:
                test_suite.run(output=output_xml_path, loglevel="trace", listener=[listenerv2, listenerv3], 
                               variable=['DRYRUN:True'], dryrun=True)
            else:
                test_suite.run(output=output_xml_path, loglevel="trace", listener=[listenerv2, listenerv3])
        else:
            if dry_run is not None:
                test_suite.run(output=output_xml_path, loglevel="trace", variable=['DRYRUN:True'], dryrun=True)
            else:
                test_suite.run(output=output_xml_path, loglevel="trace")

        # Define the path of output files
        output_report_path = os.path.join(output_dir, "report.html")
        output_log_path = os.path.join(output_dir, "log.html")
        flattened_result = ExecutionResult(output_xml_path, flattened_keywords='for')
        ResultWriter(flattened_result).write_results(report=output_report_path, log=output_log_path)


def parse_args():
    """
    This function configures the option parser and parses the command line arguments.

    The supported args are as follows.

    -c --config_file - The location of the config.ini that contains information about the test run.
    -d --data_files  - Comma separated list of absolute path for each data file. Ignores datafiles
                       listed in config.ini if this options is used.
    -s --suite_name  - Suite name used in the log/report title. Ignores config.ini if this option is used.
    -e --environment - Relative path to the test environment file. Ignores config.ini if this option is used.
    """
    opt_parser = OptionParser()
    opt_parser.add_option("-c", "--config_file", help="*REQUIRED* The location of the __init__.robot or config.ini that"
                          " contains information about the test run.", dest="config_file")
    opt_parser.add_option("-e", "--environment", help="*REQUIRED* Path to test enviroment file being used. Ignores "
                          "TESTBEDVARIABLE in config.ini if this option is used.",
                          dest="environment")
    opt_parser.add_option("-d", "--data_files", help="*REQUIRED* Comma separated list of paths for each data file. "
                          "Ignores datafiles listed in config.ini if this options is used.",
                          dest="data_files")
    opt_parser.add_option("-s", "--suite_name", help="Suite name used in the report title. Ignores SUITENAME in "
                          "config.ini if this option is used. Defaults to DefaultSuiteName",
                          dest="suite_name", default="DefaultSuiteName")
    opt_parser.add_option("-l", "--log_directory", help="Path you want the log/report to be created in. If option "
                          "is not used. Defaults to the location specified in the "
                          "-c option.", dest="log_directory")
    opt_parser.add_option("-r", "--dry_run", help="Performs a dry run of the test suite.",
                          dest="dry_run", action="store_true")
    opt_parser.add_option("-f", "--dd_directory", help="Runs all files that end with .csv in the specified directory.",
                          dest="dd_directory")
    opt_parser.add_option("-y", "--listenerv2", help="Python listenerv2 for TRM use to record results.",
                          dest="listenerv2")
    opt_parser.add_option("-z", "--listenerv3", help="Python listenerv3 for TRM use to record results.",
                          dest="listenerv3")
    parsed_options, _ = opt_parser.parse_args()

    return parsed_options


def check_args(args):
    """
    This function checks the passed command line arguments and verifies that all required values are present.
    It prints an error message which lists the missing arguments.
    """
    errors = []
    if not args.config_file:
        errors.append("ERROR: Required argument missing, __init__.robot or config.ini (-c <path_to_init.robot>)")

    Logger().log_info("\n" + "\n".join(errors))


def parse_data_files(data_files):
    """
    This function parses the data file list provided by the -d option. The data file list should a comma separated
    list of absolute paths for each data file to execute using.
    """
    data_file_list = data_files.split(",")
    return data_file_list


def get_all_csv(dirName):
    """
    This function gets all csv files found in the specified directory and child directories.
    """
    list_of_files = []
    for (dirpath, dirnames, filenames) in os.walk(dirName):
        list_of_files += [os.path.join(dirpath, file) for file in filenames]
    # remove all non-csv files from list
    list_of_csvs = []
    for file in list_of_files:
        if ".csv" in file:
            print(file)
            list_of_csvs.append(file)
    return list_of_csvs


def main():
    options = parse_args()

    try:
        data_files = parse_data_files(options.data_files)
    except Exception:
        data_files = None

    try:
        dd_directory = parse_data_files(options.dd_directory)
    except Exception:
        dd_directory = None

    if dd_directory is not None:
        if data_files is not None:
            Logger().log_info("Only a -d OR -f directory can currently be used. Not both. "
                              "Only running with the -f specified. ")
        data_files = get_all_csv(dd_directory[0])

    try:
        suite_name = options.suite_name
    except Exception:
        suite_name = None

    try:
        environment = options.environment
    except Exception:
        environment = None

    try:
        log_directory = options.log_directory
    except Exception:
        log_directory = None

    try:
        listenerv2 = options.listenerv2
    except Exception:
        listenerv2 = None

    try:
        listenerv3 = options.listenerv3
    except Exception:
        listenerv3 = None

    try:
        dry_run = options.dry_run
    except Exception:
        dry_run = None

    # try:
    # Strip config.ini or __init__.robot if the user provides it at the end of location string.
    config_file = options.config_file
    if "config.ini" in config_file:
        config_file = config_file.replace("config.ini", "")
    if "__init__.robot" in config_file:
        config_file = config_file.replace("__init__.robot", "")
    DataDrivenExecution.execute_data_driven_test(config_file, data_files, suite_name, environment, log_directory,
                                                 listenerv2, listenerv3, dry_run)


if __name__ == "__main__":
    main()
