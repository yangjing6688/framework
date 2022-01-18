from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiPacketConfigTriggersApi \
    import PacketConfigTriggersConstants


class CaptureConfig(object):
    _valid_da_modes = ["any", "da1", "!da1", "da2", "!da2"]
    _valid_sa_modes = ["any", "sa1", "!sa1", "sa2", "!sa2"]
    _valid_pattern_modes = ["any", "pattern1", "!pattern1", "pattern2", "!pattern2", "pattern1and2"]
    _trigger_const = PacketConfigTriggersConstants()

    def __init__(self, traffic_gen_name, port, index):
        self.traffic_gen_name = traffic_gen_name
        self.port = port
        self.index = index
        self.da1 = None
        self.da2 = None
        self.sa1 = None
        self.sa2 = None
        self.pattern1_offset = None
        self.pattern2_offset = None

        # Attributes that use setter methods
        self._da1_mask = None
        self._da2_mask = None
        self._sa1_mask = None
        self._sa2_mask = None
        self._pattern1 = None
        self._pattern1_mask = None
        self._pattern2 = None
        self._pattern2_mask = None
        self._da_mode = None
        self._da_uds1_mode = None
        self._da_uds2_mode = None
        self._sa_mode = None
        self._sa_uds1_mode = None
        self._sa_uds2_mode = None
        self._pattern_mode = None
        self._pattern_uds1_mode = None
        self._pattern_uds2_mode = None

    @property
    def da1_mask(self):
        """
        The first Destination MAC capture filter.
        """
        return self._da1_mask

    @da1_mask.setter
    def da1_mask(self, mask):
        if mask is None:
            mask = "00:00:00:00:00:00"
        self._da1_mask = mask

    @property
    def da2_mask(self):
        """
        The second Destination MAC capture filter.
        """
        return self._da2_mask

    @da2_mask.setter
    def da2_mask(self, mask):
        if mask is None:
            mask = "00:00:00:00:00:00"
        self._da2_mask = mask

    @property
    def sa1_mask(self):
        """
        The first Source MAC capture filter.
        """
        return self._sa1_mask

    @sa1_mask.setter
    def sa1_mask(self, mask):
        if mask is None:
            mask = "00:00:00:00:00:00"
        self._sa1_mask = mask

    @property
    def sa2_mask(self):
        """
        The second Source MAC capture filter.
        """
        return self._sa2_mask

    @sa2_mask.setter
    def sa2_mask(self, mask):
        if mask is None:
            mask = "00:00:00:00:00:00"
        self._sa2_mask = mask

    @property
    def pattern1(self):
        """
        The first custom capture filter octet pattern.
        """
        return self._pattern1

    @pattern1.setter
    def pattern1(self, pattern):
        self._pattern1 = self.__generate_pattern(pattern)

    @property
    def pattern1_mask(self):
        """
        The mask value for the first custom filter pattern.
        """
        return self._pattern1_mask

    @pattern1_mask.setter
    def pattern1_mask(self, mask):
        if mask is None:
            self._pattern1_mask = ("0" * len(str(self.pattern1).replace(" ", "")))
        else:
            self._pattern1_mask = self.__generate_mask(mask)

    @property
    def pattern2(self):
        """
        The second custom capture filter octet pattern.
        """
        return self._pattern2

    @pattern2.setter
    def pattern2(self, pattern):
        self._pattern2 = self.__generate_pattern(pattern)

    @property
    def pattern2_mask(self):
        """
        The mask value for the first custom filter pattern.
        """
        return self._pattern2_mask

    @pattern2_mask.setter
    def pattern2_mask(self, mask):
        if mask is None:
            self._pattern2_mask = ("0" * len(str(self.pattern2).replace(" ", "")))
        else:
            self._pattern2_mask = self.__generate_mask(mask)

    @property
    def da_mode(self):
        """
        The Destination MAC filter mode.

        Options:
         - match da1
         - match da2
         - match NOT da1
         - match NOT da2
         - match any
        """
        return self._da_mode

    @da_mode.setter
    def da_mode(self, mode):
        if mode.lower() in self._valid_da_modes:
            if mode.lower() == "da1":
                self._da_mode = self._trigger_const.CAPTURE_TRIGGER_DA_DA1
            elif mode.lower() == "da2":
                self._da_mode = self._trigger_const.CAPTURE_TRIGGER_DA_DA2
            elif mode.lower() == "!da1":
                self._da_mode = self._trigger_const.CAPTURE_TRIGGER_DA_NOTDA1
            elif mode.lower() == "!da2":
                self._da_mode = self._trigger_const.CAPTURE_TRIGGER_DA_NOTDA2
            else:
                self._da_mode = self._trigger_const.CAPTURE_TRIGGER_DA_ANY

    @property
    def sa_mode(self):
        """
        The Source MAC filter mode.

        Options:
         - match sa1
         - match sa2
         - match NOT sa1
         - match NOT sa2
         - match any
        """
        return self._sa_mode

    @sa_mode.setter
    def sa_mode(self, mode):
        if mode.lower() in self._valid_sa_modes:
            if mode.lower() == "sa1":
                self._sa_mode = self._trigger_const.CAPTURE_TRIGGER_SA_SA1
            elif mode.lower() == "sa2":
                self._sa_mode = self._trigger_const.CAPTURE_TRIGGER_SA_SA2
            elif mode.lower() == "!sa1":
                self._sa_mode = self._trigger_const.CAPTURE_TRIGGER_SA_NOTSA1
            elif mode.lower() == "!sa2":
                self._sa_mode = self._trigger_const.CAPTURE_TRIGGER_SA_NOTSA2
            else:
                self._sa_mode = self._trigger_const.CAPTURE_TRIGGER_SA_ANY

    @property
    def da_uds1_mode(self):
        """
        The Destination MAC filter mode.

        Options:
         - match da1
         - match da2
         - match NOT da1
         - match NOT da2
         - match any
        """
        return self._da_uds1_mode

    @da_uds1_mode.setter
    def da_uds1_mode(self, mode):
        if mode.lower() in self._valid_da_modes:
            if mode.lower() == "da1":
                self._da_mode = self._trigger_const.CAPTURE_TRIGGER_DA_DA1
            elif mode.lower() == "da2":
                self._da_mode = self._trigger_const.CAPTURE_TRIGGER_DA_DA2
            elif mode.lower() == "!da1":
                self._da_mode = self._trigger_const.CAPTURE_TRIGGER_DA_NOTDA1
            elif mode.lower() == "!da2":
                self._da_mode = self._trigger_const.CAPTURE_TRIGGER_DA_NOTDA2
            else:
                self._da_mode = self._trigger_const.CAPTURE_TRIGGER_DA_ANY

    @property
    def sa_uds1_mode(self):
        """
        The Source MAC filter mode.

        Options:
         - match sa1
         - match sa2
         - match NOT sa1
         - match NOT sa2
         - match any
        """
        return self._sa_uds1_mode

    @sa_uds1_mode.setter
    def sa_uds1_mode(self, mode):
        if mode.lower() in self._valid_sa_modes:
            if mode.lower() == "sa1":
                self._sa_uds1_mode = self._trigger_const.CAPTURE_TRIGGER_SA_SA1
            elif mode.lower() == "sa2":
                self._sa_uds1_mode = self._trigger_const.CAPTURE_TRIGGER_SA_SA2
            elif mode.lower() == "!sa1":
                self._sa_uds1_mode = self._trigger_const.CAPTURE_TRIGGER_SA_NOTSA1
            elif mode.lower() == "!sa2":
                self._sa_uds1_mode = self._trigger_const.CAPTURE_TRIGGER_SA_NOTSA2
            else:
                self._sa_uds1_mode = self._trigger_const.CAPTURE_TRIGGER_SA_ANY

    @property
    def da_uds2_mode(self):
        """
        The Destination MAC filter mode.

        Options:
         - match da1
         - match da2
         - match NOT da1
         - match NOT da2
         - match any
        """
        return self._da_uds2_mode

    @da_uds2_mode.setter
    def da_uds2_mode(self, mode):
        if mode.lower() in self._valid_da_modes:
            if mode.lower() == "da1":
                self._da_mode = self._trigger_const.CAPTURE_TRIGGER_DA_DA1
            elif mode.lower() == "da2":
                self._da_mode = self._trigger_const.CAPTURE_TRIGGER_DA_DA2
            elif mode.lower() == "!da1":
                self._da_mode = self._trigger_const.CAPTURE_TRIGGER_DA_NOTDA1
            elif mode.lower() == "!da2":
                self._da_mode = self._trigger_const.CAPTURE_TRIGGER_DA_NOTDA2
            else:
                self._da_mode = self._trigger_const.CAPTURE_TRIGGER_DA_ANY

    @property
    def sa_uds2_mode(self):
        """
        The Source MAC filter mode.

        Options:
         - match sa1
         - match sa2
         - match NOT sa1
         - match NOT sa2
         - match any
        """
        return self._sa_uds2_mode

    @sa_uds2_mode.setter
    def sa_uds2_mode(self, mode):
        if mode.lower() in self._valid_sa_modes:
            if mode.lower() == "sa1":
                self._sa_uds2_mode = self._trigger_const.CAPTURE_TRIGGER_SA_SA1
            elif mode.lower() == "sa2":
                self._sa_uds2_mode = self._trigger_const.CAPTURE_TRIGGER_SA_SA2
            elif mode.lower() == "!sa1":
                self._sa_uds2_mode = self._trigger_const.CAPTURE_TRIGGER_SA_NOTSA1
            elif mode.lower() == "!sa2":
                self._sa_uds2_mode = self._trigger_const.CAPTURE_TRIGGER_SA_NOTSA2
            else:
                self._sa_uds2_mode = self._trigger_const.CAPTURE_TRIGGER_SA_ANY

    @property
    def pattern_mode(self):
        """
        The Source MAC filter mode.

        Options:
         - match pattern1
         - match pattern2
         - match NOT pattern1
         - match NOT pattern2
         - match pattern1 and pattern2
         - match any
        """
        return self._pattern_mode

    @pattern_mode.setter
    def pattern_mode(self, mode):
        if mode.lower() in self._valid_pattern_modes:
            if mode.lower() == "pattern1":
                self._pattern_mode = self._trigger_const.CAPTURE_TRIGGER_PATTERN_PATTERN1
            elif mode.lower() == "pattern2":
                self._pattern_mode = self._trigger_const.CAPTURE_TRIGGER_PATTERN_PATTERN2
            elif mode.lower() == "!pattern1":
                self._pattern_mode = self._trigger_const.CAPTURE_TRIGGER_PATTERN_NOTPATTERN1
            elif mode.lower() == "!pattern2":
                self._pattern_mode = self._trigger_const.CAPTURE_TRIGGER_PATTERN_NOTPATTERN2
            elif mode.lower() == "pattern1and2":
                self._pattern_mode = self._trigger_const.CAPTURE_TRIGGER_PATTERN_PATTERN1AND2
            else:
                self._pattern_mode = self._trigger_const.CAPTURE_TRIGGER_PATTERN_ANY

    @property
    def pattern_uds1_mode(self):
        """
        The Source MAC filter mode.

        Options:
         - match pattern1
         - match pattern2
         - match NOT pattern1
         - match NOT pattern2
         - match pattern1 and pattern2
         - match any
        """
        return self._pattern_uds1_mode

    @pattern_uds1_mode.setter
    def pattern_uds1_mode(self, mode):
        if mode.lower() in self._valid_pattern_modes:
            if mode.lower() == "pattern1":
                self._pattern_uds1_mode = self._trigger_const.CAPTURE_TRIGGER_PATTERN_PATTERN1
            elif mode.lower() == "pattern2":
                self._pattern_uds1_mode = self._trigger_const.CAPTURE_TRIGGER_PATTERN_PATTERN2
            elif mode.lower() == "!pattern1":
                self._pattern_uds1_mode = self._trigger_const.CAPTURE_TRIGGER_PATTERN_NOTPATTERN1
            elif mode.lower() == "!pattern2":
                self._pattern_uds1_mode = self._trigger_const.CAPTURE_TRIGGER_PATTERN_NOTPATTERN2
            elif mode.lower() == "pattern1and2":
                self._pattern_uds1_mode = self._trigger_const.CAPTURE_TRIGGER_PATTERN_PATTERN1AND2
            else:
                self._pattern_uds1_mode = self._trigger_const.CAPTURE_TRIGGER_PATTERN_ANY

    @property
    def pattern_uds2_mode(self):
        """
        The Source MAC filter mode.

        Options:
         - match pattern1
         - match pattern2
         - match NOT pattern1
         - match NOT pattern2
         - match pattern1 and pattern2
         - match any
        """
        return self._pattern_uds2_mode

    @pattern_uds2_mode.setter
    def pattern_uds2_mode(self, mode):
        if mode.lower() in self._valid_pattern_modes:
            if mode.lower() == "pattern1":
                self._pattern_uds2_mode = self._trigger_const.CAPTURE_TRIGGER_PATTERN_PATTERN1
            elif mode.lower() == "pattern2":
                self._pattern_uds2_mode = self._trigger_const.CAPTURE_TRIGGER_PATTERN_PATTERN2
            elif mode.lower() == "!pattern1":
                self._pattern_uds2_mode = self._trigger_const.CAPTURE_TRIGGER_PATTERN_NOTPATTERN1
            elif mode.lower() == "!pattern2":
                self._pattern_uds2_mode = self._trigger_const.CAPTURE_TRIGGER_PATTERN_NOTPATTERN2
            elif mode.lower() == "pattern1and2":
                self._pattern_uds2_mode = self._trigger_const.CAPTURE_TRIGGER_PATTERN_PATTERN1AND2
            else:
                self._pattern_uds2_mode = self._trigger_const.CAPTURE_TRIGGER_PATTERN_ANY

    @staticmethod
    def __generate_pattern(pattern):
        if pattern is not None:
            pattern = pattern.replace(" ", "")

            if pattern.startswith("0x"):
                pattern = pattern.replace("0x", "")
            else:
                pattern = hex(int(pattern)).replace("0x", "")

            if len(pattern) % 2 != 0:
                pattern = "0" + pattern

            pattern = " ".join(pattern[i:i + 2] for i in range(0, len(pattern), 2))

            return pattern

    @staticmethod
    def __generate_mask(mask):
        if mask is not None:
            mask = mask.replace(" ", "")

            if mask.startswith("0x"):
                mask = mask.replace("0x", "")

            if len(mask) % 2 != 0:
                mask = "0" + mask

            mask = " ".join(mask[i:i + 2] for i in range(0, len(mask), 2))

            return mask
