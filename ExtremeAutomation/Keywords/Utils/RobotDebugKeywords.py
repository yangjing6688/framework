from ExtremeAutomation.Keywords.BaseClasses.KeywordBaseClass import KeywordBaseClass


class RobotDebugKeywords(KeywordBaseClass):
    def __init__(self):
        super(RobotDebugKeywords, self).__init__()

    def enable_debug_mode(self):
        """
        This keyword will pause a robot test case after a failure instead of the normal behavior
        of stopping/continuing to the next keyword.
        """
        if not KeywordBaseClass.debug_keyword:
            KeywordBaseClass.debug_keyword = True

    def disable_debug_mode(self):
        """
        This keyword will disable the debug mode and any keywords following this function will behave
        normally.
        """
        if KeywordBaseClass.debug_keyword:
            KeywordBaseClass.debug_keyword = False
