import os
from ExtremeAutomation.Library.Logger.Logger import Logger

logger = Logger()
logger.console_level = Logger.ALL

try:
    path = os.path.join(os.environ["pythonpath"].split(";")[0], "ExtremeAutomation", "Keywords", "TrafficKeywords",
                        "Utils", "Constants")
except KeyError:
    path = None
    logger.log_info("Configure your python path.")

if path is not None:
    source_file = None
    variables_file = None
    lines_to_write = list()
    longest_line = ""
    source_file_name = "PacketTypeConstants.py"
    variables_file_name = "PacketTypeVariables.robot"

    try:
        source_file = open(path + source_file_name, "r")
    except IOError:
        logger.log_info("Unable to find " + path + source_file_name + ".")

    try:
        variables_file = open(path + variables_file_name, "w")
    except IOError:
        logger.log_info("Unable to open " + path + variables_file_name + ".")

    if source_file is not None and variables_file is not None:
        variables_file.write("*** Variables ***\r\n")
        for index, line in enumerate(source_file):
            if index > 0:
                if line == "\n":
                    lines_to_write.append(line)
                elif line.replace(" ", "")[0] == "#":
                    lines_to_write.append(line.lstrip())
                elif line.replace(" ", "")[0:3] == "def":
                    break
                else:
                    var = "${" + line.split("=")[0].replace(" ", "") + "}"

                    if len(var) > len(longest_line):
                        longest_line = var

                    value = line.split("=")[1].replace(" ", "").replace("\"", "").rstrip()
                    lines_to_write.append([var, value])

        for index, line in enumerate(lines_to_write):
            if index < len(lines_to_write) - 2:
                if isinstance(line, list):
                    spaces = " " * ((len(longest_line) - len(line[0])) + 4)
                    variables_file.write(line[0] + spaces + line[1] + "\n")
                else:
                    variables_file.write(line)

        source_file.close()
        variables_file.close()

        logger.log_info("DONE! - Created/Updated " + variables_file_name + ".")
