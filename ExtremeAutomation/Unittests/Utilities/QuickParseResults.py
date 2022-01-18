import os
import sys
import xml.etree.ElementTree


class Report(object):
    def __init__(self):
        self.total_tests = 0
        self.num_fails = 0
        self.file_reports = []

    def write(self, file_path):
        # Sort the report so suites with fails are displayed first.
        self.file_reports.sort(key=lambda x: x.num_fails, reverse=True)

        file_lines = list()
        file_lines.append("Overall Results:")
        file_lines.append("    Total: {0}".format(str(self.total_tests)))
        file_lines.append("    Failed: {0}".format(str(self.num_fails)))
        file_lines.append("")
        file_lines.append("===================================================================================")
        file_lines.append("")

        for file_report in self.file_reports:
            file_lines.append(file_report.test_suite_name)
            file_lines.append("    Total: {0}".format(str(file_report.total_tests)))
            file_lines.append("    Failed: {0}".format(str(file_report.num_fails)))
            file_lines.append("")

            if len(file_report.fails) > 0:
                file_lines.append("    Test Failures:")

                for fail in file_report.fails:
                    file_lines.append("        Test Case Name: {0}".format(fail.test_name))
                    file_lines.append("        Message: {0}".format(fail.error_msg.replace("\n", "\n            ")))
                    file_lines.append("")

        with open(os.path.join(file_path, "UnitTestResults.txt"), "w") as test_results_file:
            test_results_file.write("\n".join(file_lines))

        print("\nCreated report file {0}".format("UnitTestResults.txt"))


class FileReport(object):
    def __init__(self, suite_name):
        super(FileReport, self).__init__()
        self.test_suite_name = suite_name
        self.fails = []
        self.total_tests = 0
        self.num_fails = 0


class Failure(object):
    def __init__(self, test_name, error_msg):
        self.test_name = test_name
        self.error_msg = error_msg


def parse_results(input_path):
    xml_paths = []

    for dir_path, dir_names, file_names in os.walk(input_path):
        for file_name in file_names:
            if file_name.endswith(".xml") and file_name.startswith("TEST"):
                xml_paths.append(os.path.join(dir_path, file_name))

    report = Report()

    for xml_path in xml_paths:
        parse_xml_file(report, xml_path)

    return report


def parse_xml_file(report, xml_path):
    suite = xml.etree.ElementTree.parse(xml_path).getroot()

    report.num_fails += int(suite.attrib["errors"])
    report.total_tests += int(suite.attrib["tests"])

    file_report = FileReport(suite.attrib["name"])
    report.file_reports.append(file_report)

    for test in suite:
        file_report.total_tests += 1
        # If test has children that means if failed.
        if test:
            file_report.num_fails += 1
            name = test.attrib["name"].strip("()")
            text = test[0].text
            file_report.fails.append(Failure(name, text))


def main(input_path, output_path):
    test_report = parse_results(input_path)
    test_report.write(output_path)


if __name__ == '__main__':
    try:
        in_path = sys.argv[1]
        out_path = sys.argv[2]
        main(in_path, out_path)
    except IndexError:
        print("No path(s) provided")
