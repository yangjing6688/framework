class KeywordStatisticObj(object):
    def __init__(self):
        self.keyword_name = ""
        self.keyword_parent = ""
        self.keyword_count = 0
        self.keyword_type = ""

        self._keyword_test_cases = ""

    @property
    def keyword_test_cases(self):
        """
        Property function for keyword_test_cases, returns the private attribute _keyword_test_cases
        """
        return self._keyword_test_cases

    @keyword_test_cases.setter
    def keyword_test_cases(self, val):
        """
        Setter function for keyword_test_cases. Appends , + <val> to the current _keyword_test_cases string.
        Then checks if "," is at the beginning of the keyword_test_cases, if it is, it's removed.
        """
        self._keyword_test_cases += "," + val
        self._keyword_test_cases.strip(",")
