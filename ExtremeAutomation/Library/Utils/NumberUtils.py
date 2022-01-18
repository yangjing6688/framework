import re
import random
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


class NumberUtils(object):
    @staticmethod
    def get_random_list(list_len, max_val):
        """Generates a random int list."""
        rand_list = list()
        if max_val == 0:
            return False
        elif list_len >= max_val:
            rand_list = range(1, max_val)
        else:
            while len(rand_list) != list_len:
                tmp_rand = random.randrange(1, max_val)
                rand_list.append(tmp_rand) if tmp_rand not in rand_list else None
        return sorted(rand_list)

    @staticmethod
    def little_endian_hex_string_to_int(s):
        """Converts a hex string to and integer."""
        t = StringUtils.place_character_every_n_characters(s, ":", 2).split(":")
        t.reverse()
        return int(''.join(t), 16)

    @staticmethod
    def int_to_little_endian_hex_string(s, num_bytes):
        """Converts an integer to a hex string."""
        s = hex(s)[2:]
        if (len(s) % 2) == 1:
            s = "0" + s
        t = StringUtils.place_character_every_n_characters(s, ":", 2).split(":")
        t.reverse()
        while len(t) < num_bytes:
            t.append("00")
        return ' '.join(t)

    @staticmethod
    def to_integer_value(integer):
        """Converts the given object to an integer, if possible."""
        try:
            if isinstance(integer, int):
                return integer
            if isinstance(integer, float):
                return int(integer)
            if isinstance(integer, str):
                integer = integer.strip()
            base = NumberUtils.get_base(integer)

            return int(NumberUtils.normalize_strings(integer), base)
        except ValueError:
            return integer

    @staticmethod
    def to_hex_value(integer, strip_prefix):
        """Converts the given object to a hex integer."""
        try:
            if strip_prefix:
                return format(NumberUtils.to_integer_value(integer), 'x')
            else:
                return hex(NumberUtils.to_integer_value(integer))
        except TypeError:
            return integer

    @staticmethod
    def get_base(integer):
        """Returns the base type for the integer."""
        base = 10
        if isinstance(integer, int):
            base = 10
        elif isinstance(integer, str) and integer.startswith("0x"):
            base = 16
        elif isinstance(integer, str) and integer.endswith("b"):
            base = 2
        elif isinstance(integer, str) and integer.startswith("0"):
            base = 8
        return base

    @staticmethod
    def normalize_strings(st):
        """Removes all preceding and trailing characters from the string."""
        if "0x" in st:
            st = st.replace("0x", "")
        elif st.endswith("b"):
            st = re.sub("([0-9A-Fa-f]+)b$", "$1", st)
        return st

    @staticmethod
    def verify_expected_count(parse_result, count_operator, expected_count):
        """
        The following function returns True if the value is expected.
        """
        try:
            if count_operator is not None:
                if count_operator == ">":
                    return True if int(expected_count) < int(parse_result) else False
                elif count_operator == "<":
                    return True if int(expected_count) > int(parse_result) else False
                elif count_operator == "=" or "-1":
                    return True if int(expected_count) == int(parse_result) else False
            else:
                return True if int(expected_count) == int(parse_result) else False
        except ValueError:
            return False
