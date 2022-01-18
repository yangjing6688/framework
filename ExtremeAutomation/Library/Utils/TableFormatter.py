import collections
from collections import deque
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


class TableFormatter:
    def __init__(self):
        self.columns = collections.OrderedDict()
        self.columnsLengh = dict()
        self.longest_row = -1
        self.empty_line_value = ""

    def add_column(self, name):
        """Adds a new column to the table with the given name."""
        if name not in self.columns:
            self.columns.update({name: deque()})
            self.columnsLengh[name] = len(name)

    def add_row_value(self, name, value):
        """Sets the value of a row for the column 'name'."""
        self.add_column(name)
        value = str(value)
        if not value or not isinstance(value, str):
            value = ""
        self.columns[name].append(value)
        self.longest_row = max(self.longest_row, len(self.columns[name]))
        self.columnsLengh[name] = max(self.columnsLengh[name], len(value))

    def to_table_string(self, print_header=True):
        """Returns a formatted string of the table for printing to logs."""
        ret_str = "\n"
        if print_header:
            for key, val in self.columns.items():
                length = self.columnsLengh[key]
                line = key + (" " * (length - len(key))) + " | "
                ret_str += line
            ret_str = ret_str.rstrip()
            ret_str = ret_str[:-1]

            ret_str += StringUtils.replace_all_regex("[a-zA-Z0-9 ]", "-", ret_str).replace("|", "+") + "\n"

        for index_val in range(0, self.longest_row):
            for key, val in self.columns.items():
                if len(val) > index_val:
                    val = val[index_val]
                else:
                    val = self.empty_line_value
                length = self.columnsLengh[key]
                ret_str += str(val) + (" " * (length - len(val))) + " | "
            index_val += 1
            ret_str = ret_str.rstrip() + "\n"
        return ret_str[:-1]
