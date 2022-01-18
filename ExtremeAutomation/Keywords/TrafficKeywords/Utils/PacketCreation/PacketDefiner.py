class PacketDefiner(object):
    def __init__(self):
        self.packet_info = []

    def add_packet_info(self, set_function, get_function, value, default_value, set_args=None, get_args=None):
        """
        This function updates the packet info list using the passed set/get functions.
        """
        self.packet_info.append(PacketDefinition(set_function, get_function, value, default_value, set_args, get_args))

    def clear_packet_info(self):
        """
        This function resets packet_info to an empty list.
        """
        self.packet_info = []


class PacketDefinition(object):
    def __init__(self, set_func, get_func, val, default_val, set_args, get_args):
        # Attributes with setter/getters.
        self._set_args = None
        self._get_args = None

        self.set_func = set_func
        self.get_func = get_func
        self.val = val
        self.default_val = default_val
        self.set_args = set_args
        self.get_args = get_args

    @property
    def set_args(self):
        """
        Property function for set_args. This function returns the private attribute _set_args.
        """
        return self._set_args

    @set_args.setter
    def set_args(self, args):
        """
        Setter function for set_args. This function verifies that set_args are either None or a list.
        Any other data type will result in a ValueError.
        """
        if args is None:
            self._set_args = []
        else:
            if isinstance(args, list):
                self._set_args = args
            else:
                raise ValueError("set_args must be passed a list.")

    @property
    def get_args(self):
        """
        Property function for get_args. This function returns the private attribute _get_args.
        """
        return self._get_args

    @get_args.setter
    def get_args(self, args):
        """
        Setter function for get_args. This function verifies that get_args are either None or a list.
        Any other data type will result in a ValueError.
        """
        if args is None:
            self._get_args = []
        else:
            if isinstance(args, list):
                self._get_args = args
            else:
                raise ValueError("get_args must be passed a list.")
