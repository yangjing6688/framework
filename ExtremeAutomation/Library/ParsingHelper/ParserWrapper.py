import re
from ExtremeAutomation.Library.Logger.Logger import Logger
from ExtremeAutomation.Library.Device.NetworkElement.Constants.NetworkElementConstants import NetworkElementConstants


class ParserWrapper:
    def __init__(self):
        self.logger = Logger()
        self.constants = NetworkElementConstants()

    @staticmethod
    def normalize_header(string, header_char, num, norm="%%%%%%"):
        """
        Function Args:
        [string] - The string that should be normalized
        [header_char] - The character that is found in header strings.
        [num] - The number of time <header_char> must appear before being considered a header.
        [norm] - The string that headers should be replaced with

        This function normalizes all occurrences where <header_char> appears at least <num> times in a row.
        The normalized header is replaced with "%%%%%%".
        """
        header = header_char * num
        norm_lines = []

        for line in string.splitlines():
            if header in line:
                norm_line = ""
                while header in line:
                    start_ind = line.find(header)
                    end_ind = start_ind + len(header)
                    if end_ind != len(line):
                        while line[end_ind] == header_char:
                            end_ind += 1
                            if end_ind == len(line):
                                break
                    norm_line = line[0:start_ind] + norm + line[end_ind::]
                    line = norm_line
                norm_lines.append(norm_line)
            else:
                norm_lines.append(line)
        return "\n".join([i.strip() for i in norm_lines])

    def get_value_by_index(self, string, index):
        """
        Function Args:
        [string] - A space delimited string.
        [index] - The index of the value to be retrieved.

        This function returns the string value at <index>. If index is outside the length
        of the split string, VALUE_NOT_PRESENT is returned.
        """
        split_string = string.strip().split()

        if index < 0:
            return self.constants.VALUE_NOT_PRESENT
        elif len(split_string) >= index:
            return split_string[index]
        return self.constants.VALUE_NOT_PRESENT

    def get_value_by_offset(self, string, match_val, index):
        """
        Function Args:
        [string] - The string to search through.
        [match_val] - The value within the line to key off.
        [index] - The index of the string within the found line to return.

        This function iterates over each line of <string> searching for <match_val>. If it is found it returns
        the string at index <index>.
        """
        return_string = ""
        lines = self.__get_lines(string, match_val)

        for line in lines:
            line_split = line.strip().split()
            if index < len(line_split):
                return_string += line_split[index] + " "

        if return_string == "":
            return self.constants.VALUE_NOT_PRESENT
        return return_string.strip()

    def get_exact_value_by_offset(self, string, match_val, index):
        """
        Function Args:
        [string] - The string to search through.
        [match_val] - The value within the line to key off. This value must match exactly.
                      For example "rw" would not match "rwa".
        [index] - The index of the string within the found line to return.

        This function iterates over each line of <string> searching for <match_val>. If it is found it returns
        the string at index <index>.
        """
        return_string = ""
        lines = self.__get_lines_exact(string, match_val)

        for line in lines:
            line_split = line.strip().split()
            if index < len(line_split):
                return_string += line_split[index] + " "

        if return_string == "":
            return self.constants.VALUE_NOT_PRESENT
        return return_string.strip()

    def get_value_by_offset_with_exclude(self, string, match_val, index, exclude_string):
        """
        Function Args:
        [string] - The string to search through.
        [match_val] - The value within the line to key off. This value must match exactly.
                      For example "rw" would not match "rwa".
        [index] - The index of the string within the found line to return.
        [exclude_string] - If this string is seen in a line with <match_val> it will be ignored.

        This function iterates over each line of <string> searching for <match_val>. If a matching line is found
        we then check to see if <exclude_string> is present, if it is we ignore that line. For any non-excluded line
        the string at <index> is returned.
        """
        return_string = ""

        for line in self.__get_lines_exclude(string, match_val, exclude_string):
            line_split = line.strip().split()
            if index < len(line_split):
                return_string += line_split[index] + " "

        if return_string == "":
            return self.constants.VALUE_NOT_PRESENT
        return return_string.strip()

    def get_value_range(self, string, start_val, end_val):
        """
        Function Args:
        [string] - The string to pull information from.
        [start_val] - Where the range should start.
        [end_val] - Where the range should stop.

        This function grabs the substring from <start_val> to <end_val> (inclusive). If either
        <start_val> or <end_val> are not found in the string VALUE_NOT_PRESENT will be returned.
        """
        if start_val not in string or end_val not in string:
            return self.constants.VALUE_NOT_PRESENT
        else:
            split1 = string.split(start_val)[1::]
            split2 = start_val.join(split1).split(end_val)[0]
            return split2.strip()

    def get_value_from_string_to_eol(self, string, match_val):
        """
        Function Args:
        [string] - The string to pull information from.
        [match_val] - The value that should be the beginning of the substring.

        This function grabs the substring from <match_val> to the end of the line. If <match_val> is not
        found in the string VALUE_NOT_PRESENT is returned.
        """
        lines = self.__get_lines(string, match_val)

        if lines:
            return lines[0].split(match_val)[1].strip()
        return self.constants.VALUE_NOT_PRESENT

    def get_range_by_offset(self, string, match_val, start, end):
        """
        Function Args:
        [string] - The string to pull information from.
        [match_val] - The value that should be present in lines.
        [start] - The start index for any found lines.
        [end] - The end index for any found lines.

        This function will check each line in <string> for <match_val>. For any matching lines
        a substring from <start> to <end> will be returned. The index are based on the string being
        space delimited.
        """
        return_vals = []
        lines = self.__get_lines(string, match_val)

        if lines:
            for line in lines:
                if start < 0:
                    return_vals.append(self.constants.VALUE_NOT_PRESENT)
                else:
                    line_split = line.strip().split()
                    if start < len(line_split) and end < len(line_split):
                        start_str = line_split[start]
                        start_ind = line.find(start_str)
                        end_str = line_split[end]
                        end_ind = line.find(end_str) + len(end_str) if end >= 0 else len(line)
                        return_vals.append(line[start_ind: end_ind].strip())

        if not return_vals:
            return_vals.append(self.constants.VALUE_NOT_PRESENT)
        return return_vals

    def get_eol_value(self, string, match_val):
        """
        Function Args:
        [string] - The string to pull information from.
        [match_val] - The value to search for in each line in <string>.

        Grabs each line in <string> that contains <match_val>.
        """
        lines = self.__get_lines(string, match_val)

        if not lines:
            return [self.constants.VALUE_NOT_PRESENT]
        return [i.strip() for i in lines]

    def get_value_at_location(self, string, column=0, name=None, row=None):
        """
        [string] - The string to pull information from.
        [column] - The column in the output to inspect.
        [name] - The value that should be matched.
        [row] - The row in the output to inspect.

        Column and at least one other value must be provided.

        This function breaks the output into a "grid". Each new line is considered a row and each
        space in the row is considered a column.

        The function operates differently depending on which arguments are passed.

        Args = column, name: A space delimited list will be returned with each value at index <column> for
                             each line that contained <name>.

        Args = column, row: Returns the value at row <row> and column <column> if present otherwise valueNotPresent
                            is returned.

        Args = column, row, name: Returns the value at row <row> and column <column> if <name> is present in the
                                  row otherwise valueNotPresent is returned.
        """
        output_lines = string.splitlines()
        return_vals = []

        try:
            column = int(column)
        except ValueError:
            raise ValueError("Column must be a number (string or integer).")

        try:
            row = int(row)
        except ValueError:
            raise ValueError("Row must be a number (string or integer).")
        except TypeError:
            row = None

        if name is not None and row is None:
            for line in output_lines:
                if name in line:
                    try:
                        return_vals.append(line.split()[column])
                    except IndexError:
                        return_vals.append(self.constants.VALUE_NOT_PRESENT)
        elif name is None and row is not None:
            try:
                return_vals.append(output_lines[row].split()[column])
            except IndexError:
                pass
        elif name is not None and row is not None:
            try:
                if name in output_lines[row].split()[column]:
                    try:
                        return_vals.append(output_lines[row].split()[column])
                    except IndexError:
                        pass
            except IndexError:
                return_vals.append(self.constants.VALUE_NOT_PRESENT)

        if not return_vals:
            return self.constants.VALUE_NOT_PRESENT
        return " ".join(return_vals)

    def is_exact_string_present_in_output(self, string, match_val):
        """
        Function Args:
        [string] - The string to pull information from.
        [match_val] - The value to look for within <string>.

        Verifies that <match_val> is present exactly within <string>. For example if <match_va> = "rw",
        only "rw" would match "rwa", "arw", and "arwa" would not match.
        """
        return self.__get_exact_match(string, match_val)

    # +------------------+
    # | Helper Functions |
    # +------------------+
    @staticmethod
    def __get_lines(string, match_string):
        """
        Function Args:
        [string] - The string to pull matching lines from.
        [match_string] - The string to search for.

        Returns all lines in <string> that contain <match_val>.
        """
        line_matches = []

        for line in string.splitlines():
            if match_string in line:
                line_matches.append(line)
        return line_matches

    def __get_lines_exact(self, string, match_string):
        """
        Function Args:
        [string] - The string to pull exactly matching lines from
        [match_string] - The string to search for.

        Returns all lines in <string> that match <match_val> exactly.
        """
        line_matches = []

        for line in string.splitlines():
            if self.__get_exact_match(line, match_string):
                line_matches.append(line)

        return line_matches

    @staticmethod
    def __get_lines_exclude(string, match_string, exclude_string):
        """
        Function Args:
        [string] - The string to pull matching lines from.
        [match_string] - The string to search for.
        [exclude_string] - The string to used disqualify matching lines.

        Returns all lines that contain <match_val> while also not containing <exclude_string>.
        """
        line_matches = []

        for line in string.splitlines():
            if match_string in line and exclude_string not in line:
                line_matches.append(line)

        return line_matches

    @staticmethod
    def __get_exact_match(string, match_string):
        """
        Function Args:
        [string] - The string to check.
        [match_string] - The string to check for inside <string>.

        This function returns True if <match_string> exists exactly within <string>, otherwise False is returned.
        A string is considered an exact match if every character in <match_string> is matched with no other
        character proceeding or following it. For example "rw" would match "rw" but not "rwa", "arw", or "arwa".
        """
        if re.search(r'\s' + match_string.strip() + r'\s', string) is not None or \
                re.search('^' + match_string.strip() + r'\s', string) is not None or \
                re.search(r'\s' + match_string.strip() + '$', string) is not None or \
                re.search('^' + match_string.strip() + '$', string) is not None:
            return True
        return False
