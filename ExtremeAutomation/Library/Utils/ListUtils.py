from ExtremeAutomation.Keywords.FailureException import FailureException


class ListUtils(object):
    @staticmethod
    def convert_to_list(obj, convert_lists=False):
        """
        Arguments:
        obj           - The object to convert to a list.
        convert_lists - Determines whether to convert to a list if the object is already a list.

        Converts the provided object to a list.
        """
        if obj is None:
            return None
        elif not isinstance(obj, list) or convert_lists:
            return [obj]
        return obj

    @staticmethod
    def list_len_check(*lists):
        """Verifies that a list or lists are not empty."""
        # Creates a list of each list length.
        list_lens = [len(i) for i in lists]

        # Creates a list of each length which is greater than 1 and less than the max list length.
        not_max_len_lists = [i for i in list_lens if 1 < i < max(list_lens)]

        # Returns true if all lists are either length 1 or max length.
        # Otherwise an a failure exception is raised.
        if len(not_max_len_lists) == 0:
            return True
        raise FailureException("Length of all lists passed must be 1 or equal to the longest list.")

    @staticmethod
    def generate_arg_list(**kwargs):
        """
        This function generates a list of arg dictionaries.

        The kwargs can be in the following three formats.
            1. kwarg1=<some_arg>
            2. kwarg2=(<some_arg>, function_to_pass_arg_into)
            3. kwarg3=(<some_arg>, function_to_pass_arg_into, (first_func_arg, second_func_arg))

        The first method is self explanatory.

        The second will pass each instance of <some_arg> into function_to_pass_arg_into. Roughly translating to
        [function_to_pass_arg_into(i) for i in <some_arg>]

        The third will pass additional arguments to function_to_pass_arg_into. Roughly translating to.
        [function_to_pass_arg_into(*[first_func_arg, second_func_arg]) for i in <some_arg>]

        The output format is as follows.
        [{"kwarg1": <arg>, "kwarg2": <arg>, "kwargN": <arg},
         {"kwarg1": <arg>, "kwarg2": <arg>, "kwargN": <arg},
         {"kwarg1": <arg>, "kwarg2": <arg>, "kwargN": <arg},
        ]

        This is useful for creating arg_dicts for keywords.
        """
        return_arg_list = []
        updated_args = {}

        for key in kwargs:
            if not isinstance(kwargs[key], list):
                # todo (jhall) - Remove this once all keywords have been converted to new method.
                # This is only here because I'm not sure if I can safely remove the None check from convert_to_list.
                if kwargs[key] is None:
                    updated_args[key] = [None]
                else:
                    updated_args[key] = ListUtils.convert_to_list(kwargs[key])
            else:
                updated_args[key] = kwargs[key]

        if ListUtils.list_len_check(*[updated_args[i] for i in updated_args]):
            i = 0
            try:
                longest_list = max([len(updated_args[j]) for j in updated_args])
            except ValueError:
                longest_list = 1
            while i < longest_list:
                tmp_dict = {}
                for key in updated_args:
                    if len(updated_args[key]) == 1:
                        tmp_dict[key] = updated_args[key][0]
                    else:
                        tmp_dict[key] = updated_args[key][i]
                return_arg_list.append(tmp_dict)
                i += 1

        return return_arg_list

    @staticmethod
    def chunk(input_list, chunk_size):
        """
        This function is used to split a list evenly with a pre-set size for each chunk.
        :param input_list: The list to be split into chunks
        :param chunk_size: The size of the chunk
        :return: The chunk lists will be output in sequence.
        """
        for i in range(0, len(input_list), int(chunk_size)):
            yield input_list[i:i + int(chunk_size)]
