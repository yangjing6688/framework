"""
ExecuteNestedSuite is used to run a suite defined in a yaml configuration file.

To run execute python ExecuteNestedSuite.py --config_file=<config_file> <optional pybot args>

The only required argument is --config_file. All other args will be treated as pybot arguments.
Robot will throw an error if invalid arguments are passed.

The following is an example configuration file.

# This will be name of the top level suite.
suite_name: My Suite

# This is the directory where all tests are contained.
# Currently this does NOT search beyond this directory.
test_dir: Tests/

# All keys in the test_plan dictionary MUST exist in the TEST_DIR as .robot files.
test_plan:
    Setup1:
        Setup2a:
            Setup3a:
                test0:
                test1:
                test2:
                test3:
            Setup3b:
                test1:
                test2:
                test3:
        Setup2b:
            Setup3a:
                test1:
                test2:
                test3:
            Setup3b:
                test1:
                test2:
                test3:
        Setup4:
            test1:
            test2:
            test3:
            test4:


# The above plan would execute as follows.
Run Setup1 suite setup
    Run Setup2a suite setup
        Run Setup3a suite setup
            Run test0, test1, test2, test3
        Run Setup3a suite teardown
        Run Setup3b suite setup
            Run test1, test2, test3
        Run Setup3b suite teardown
    Run Setup2a suite teardown
    Run Setup2b suite setup
        Run Setup3a suite setup
            Run test1, test2, test3
        Run Setup3a suite teardown
        Run Setup3b suite setup
            Run test1, test2, test3
        Run Setup3b suite teardown
    Run Setup2b suite teardown
    Run Setup4 suite setup
        Run test1, test2, test3, test4
    Run Setup4 suite teardown
Run Setup1 suite teardown
"""
import os
import yaml
import shutil
import argparse
from robot.rebot import rebot
from robot.api import TestSuite, TestSuiteBuilder
from robot.errors import DataError
from robot.utils.application import Application
from robot.run import USAGE

suite_builder = TestSuiteBuilder()


def parse_config_yaml(yaml_file_path):
    """
    Function Args;
        [yaml_file_path] - Path to the yaml configuration file.

    This function gets data from the yaml configuration file and returns an ordered dictionary
    with its contents.
    """
    with open(yaml_file_path, "r") as yaml_file:
        return yaml.load(yaml_file)


def create_robot_suite(yaml_data):
    """
    Function Args:
        [yaml_data] - An ordered dictionary containing all the information from
                      the yaml config file.

    This is a base function for the recursive __create_robot_suite function. It creates
    a base suite before calling into the recursive function.
    """
    suite = TestSuite()
    suite.name = yaml_data["suite_name"]
    search_dir = yaml_data["test_dir"]
    return __create_robot_suite(suite, yaml_data["test_plan"], search_dir, suite.name)


def __create_robot_suite(suite, yaml_data, test_dir, cur_name):
    """
    Function Args:
        [suite] - An instance of a robot test suite.
        [yaml_data] - The current section of the ordered dictionary.
        [test_dir] - The location of the test files.
        [cur_name] - The current name based off of each "level" in the yaml test plan attr.

    This function recursively iterates through the yaml data and add's a new suite for each
    non-leaf node in the yaml test plan attribute. If a leaf node is hit add a new test case
    to the current suite.
    """
    for key in yaml_data:
        # Create a path to the test file by joining the test dir and the current key.robot.
        test_file_path = os.path.join(test_dir, key + ".robot")

        try:
            # Try to make a suite using the current test_file_path.
            new_suite = suite_builder.build(test_file_path)
        except DataError:
            # The .robot file we are importing does not have a test case section.
            # Create a temp file and add one.
            new_suite = get_suite_with_missing_test_case_table(test_file_path)

        # Append the .key to the current name unless the current name is empty, then add only the key.
        cur_name = cur_name + "." + key if cur_name != "" else key
        new_suite.name = cur_name

        if yaml_data[key] is not None:
            # If the current node is not a leaf node get the current suites variables
            # then add any missing variables to the new suite. If a variables is overridden
            # in the new suite, don't overwrite it.
            new_suite_vars = [i.name for i in new_suite.variables]
            for var in suite.variables:
                if var.name not in new_suite_vars:
                    new_suite.variables.append(var)

            # Add the newly created suite to the current suite.
            suite.suites.append(new_suite)

            # Recurse with the new suite as the current suite. Also pass the yaml data of the current key.
            __create_robot_suite(new_suite, yaml_data[key], test_dir, cur_name)
        else:
            # If the current node is a leaf node take the test case object from the
            # new_suite and append it to the current suite. Set the tests name to the
            # current name.
            test = new_suite.tests[0]
            test.name = cur_name
            suite.tests.append(test)

        # As we step out of the recursion remove the last item of current name.
        cur_name = ".".join(cur_name.split(".")[:-1])

    return suite


def get_suite_with_missing_test_case_table(path):
    """
    Function Args:
        [path] - The path to the file with the missing test case table.

    For reasons unknown to me robot cannot create a suite from a .robot file
    that has no *** Test Case *** table. This function was created to avoid
    having users add an empty test case table.

    This function creates a copy of the file at the passed path, then adds a
    test case table to the end of it. A new suite is then generated from the
    temp test file. Finally we remove the temp file and return the generated
    suite.
    """
    # First copy the test case file to a temp file.
    tmp_path = path + ".tmp.robot"
    shutil.copy(path, tmp_path)

    # Open the file and read it's contents.
    with open(tmp_path, "r") as suite_file:
        file_lines = suite_file.readlines()

    # Write the new data to the file.
    with open(tmp_path, "w") as suite_file:
        file_lines += ["*** Test Cases ***", ""]
        suite_file.writelines(file_lines)

    # Create a suite from the tmp file.
    suite = suite_builder.build(tmp_path)

    # Remove the tmp file.
    os.remove(tmp_path)

    return suite


def parse_args():
    """
    This parses the only command line argument required by this script, --config-file.

    All other command line args will be passed to the robot run function.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--config_file", action="store", dest="config_file",
                        help="A .yaml file containing the suite's configuration.")

    return parser.parse_known_args()


def main():
    """
    Function Args:
        [config_file] - The path to the yaml config file.
        [options] - All other command line options (to be passed to robot).

    Main function for GenerateNestedSuite.py. Parses the config file and passes
    the data to the suite generation function. Then parses the command line
    arguments
    """
    # Parse the command line args.
    known_opts, robot_opts = parse_args()
    config_file = known_opts.config_file

    # Parse the config file and generate the robot suite.
    data = parse_config_yaml(config_file)
    suite = create_robot_suite(data)

    # Parse the unknown command line args as robot args.
    robot_args, _ = Application(USAGE).parse_arguments(robot_opts)

    # The returned dictionary has ALL options, remove all the falsy values.
    robot_args = dict((k, v) for (k, v) in robot_args.items() if v)

    # Start the suite with the provided arguments and generate report/log files.
    suite.run(**robot_args)
    rebot("output.xml")


if __name__ == '__main__':
    main()
