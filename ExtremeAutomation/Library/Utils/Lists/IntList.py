from ExtremeAutomation.Library.Utils.NumberUtils import NumberUtils
from ExtremeAutomation.Library.Utils.Lists.ObjectList import ObjectList


class IntList(ObjectList):
    """
    Example: int_list = IntList("1-9,18;44")
    """

    def __init__(self, ipstring, base=10):
        """
        Init function
        """
        self.base = base
        super(IntList, self).__init__(ipstring)

    def parse_elements(self, str_list):
        """
        formats:
        - or : means a range
            example 66-67 will give you:
                66, 67
        , or ; means another int value or int value range
            example 66,88;99-101 will give you:
                66, 88, 99, 100, 101
        """
        try:
            inner_array = []
            string = str_list.replace(":", "-")
            string = string.replace(";", ",")
            comma_tokens = string.split(",")
            prefix = ""
            if self.base == 16:
                prefix = "0x"
            for elm in comma_tokens:
                values = elm.split("-")
                if len(values) == 1:
                    values.append(values[0])
                start = NumberUtils.to_integer_value(prefix + values[0])
                end = NumberUtils.to_integer_value(prefix + values[1])
                while start <= end:
                    inner_array.append(start)
                    start += 1
            return inner_array
        except TypeError:
            return str_list
