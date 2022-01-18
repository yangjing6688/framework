import csv
from itertools import chain
from collections import defaultdict


class DataDrivenData(object):
    def __init__(self, csv_file_abspath):
        """
        :param csv_file_abspath:
        """
        self.file_path = csv_file_abspath
        self.all_data = None
        self.headers = None
        self.test_data = None
        self.filtered_data = None
        self.merged_data = None
        self.cleaned_data = None

    def read_all_data_from_csv(self):
        """
        Read all the lines in csv and output data in one list. Identify the index of splitter row in the sheet.

        :return:
        """
        all_data = []
        with open(self.file_path, 'rb') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                all_data.append(row)

        self.all_data = all_data

    def read_header_and_data_from_csv(self):
        """
        Read and store testing data, headers separately.

        :return:
        """
        test_data = []
        with open(self.file_path, 'rb') as csvfile:
            reader = csv.reader(csvfile)

            self.headers = next(reader)

            reader = next(reader, None)
            for row in reader:
                test_data.append(row)

        self.test_data = test_data

    def filter_data_by_execution_flag(self):
        """
        Skip the rows which are marked as 'True' in flag_skip_row.

        :return:
        """

        with open(self.file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            filtered_data_gen = filter(lambda row: str(row['EXECUTION_FLAG']).upper() in ('TRUE', 'YES'), reader)
            self.filtered_data = [i for i in filtered_data_gen]

    def merge_dicts_with_same_indexes(self):
        """
        Merge the rows in filtered data which have same index numbers

        :return:
        """
        filtered_data = list(self.filtered_data)
        dicts_index = 0
        i = 0

        while i < len(filtered_data):
            curr_item = filtered_data[i]
            if dicts_index == curr_item.get('INDEX'):
                dicts_index = curr_item.get('INDEX')
                pre_item = filtered_data[i-1]

                new_item = defaultdict(list)
                for key, value in chain(pre_item.items(), curr_item.items()):
                    if key not in new_item:
                        new_item[key] = value
                    elif value not in new_item.get(key):
                        temp_value = new_item.get(key)
                        if isinstance(temp_value, list):
                            temp_value.append(value)
                        else:
                            new_v = list()
                            new_v.append(temp_value)
                            new_v.append(value)
                            temp_value = new_v
                        new_item[key] = temp_value
                new_item = dict(new_item)
                filtered_data[i] = new_item
                filtered_data.remove(pre_item)
            else:
                dicts_index = curr_item.get('INDEX')
                i += 1

        self.merged_data = filtered_data

    def remove_executionflag(self):
        """
        Remove column 'index' and 'execution_flag' from data list

        :return:
        """
        merged_data = list(self.merged_data)

        for items in merged_data:
            items.pop("EXECUTION_FLAG", None)

        self.cleaned_data = merged_data

    def generate_test_data(self):
        """
        Generate data for testing

        :return:  processed data
        """
        self.filter_data_by_execution_flag()
        self.merge_dicts_with_same_indexes()
        self.remove_executionflag()

        return self.cleaned_data
