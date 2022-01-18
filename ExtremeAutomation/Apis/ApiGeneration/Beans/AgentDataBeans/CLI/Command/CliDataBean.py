from ExtremeAutomation.Apis.ApiGeneration.Beans.DataBean import DataBean


class CliDataBean(DataBean):
    def __init__(self):
        super(CliDataBean, self).__init__()
        self.interface_method = None
        self.command = None
        self.prompt = "userPrompt"

        # Attributes with setter/getter methods.
        self._prompt_arguments = None
        self._confirmation_phrase = None
        self._confirmation_argument = None
        self._ignore_errors = []
        self._add_errors = []

    @property
    def prompt_arguments(self):
        """
        Property function for prompt_arguments. Returns private attribute _prompt_arguments.
        """
        return self._prompt_arguments

    @prompt_arguments.setter
    def prompt_arguments(self, prompt_args):
        """
        Setter function for prompt_arguments. Checks the passed <prompt_args> if it is an empty string
        None is set to _prompt_arguments otherwise the value passed is set.
        """
        if prompt_args == "":
            self._prompt_arguments = None
        else:
            self._prompt_arguments = prompt_args

    @property
    def confirmation_phrase(self):
        """
        Property function for confirmation_phrase. Returns the private attribute _confirmation_phrase.
        """
        return self._confirmation_phrase

    @confirmation_phrase.setter
    def confirmation_phrase(self, confirmation_phrase):
        """
        Setter function for confirmation_phrase. Checks the passed <confirmation_phrase> if it is an
        empty string None is set, otherwise the value passed is set.
        """
        if confirmation_phrase == "":
            self._confirmation_phrase = None
        else:
            self._confirmation_phrase = confirmation_phrase

    @property
    def confirmation_argument(self):
        """
        Property function for confirmation_argument. Returns the private attribute _confirmation_argument.
        """
        return self._confirmation_argument

    @confirmation_argument.setter
    def confirmation_argument(self, confirmation_argument):
        """
        Setter function for confirmation_argument. Checks the passed <confirmation_argument> if it is an
        empty string None is set, otherwise the value passed is set.
        """
        if confirmation_argument == "":
            self._confirmation_argument = None
        else:
            self._confirmation_argument = confirmation_argument

    @property
    def ignore_errors(self):
        """
        Property function for ignore_errors. Returns the private attribute _ignore_errors.
        """
        return self._ignore_errors

    @ignore_errors.setter
    def ignore_errors(self, ignore_errors):
        """
        Setter function for ignore_errors. Checks if <ignore_errors> is not an empty string. If it's not
        create a list of errors to ignore by splitting the passed string on "||".
        """
        if isinstance(ignore_errors, str):
            if ignore_errors != "":
                self._ignore_errors = [i.strip() for i in ignore_errors.split("||")]
        elif isinstance(ignore_errors, list):
            if ignore_errors:
                self._ignore_errors = [i.strip() for i in ignore_errors]

    @property
    def add_errors(self):
        """
        Property function for add_errors. Returns the private attribute _add_errors.
        """
        return self._add_errors

    @add_errors.setter
    def add_errors(self, add_errors):
        """
        Setter function for add_errors. Checks if <add_errors> is not an empty string. If it's not
        create a list of errors to add by splitting the passed string on "||".
        """
        if isinstance(add_errors, str):
            if add_errors != "":
                self._add_errors = [i.strip() for i in add_errors.split("||")]
        elif isinstance(add_errors, list):
            if add_errors:
                self._ignore_errors = [i.strip() for i in add_errors]

    @property
    def feature(self):
        """
        Property function for feature. Returns the private attribute _feature.
        """
        return self._feature

    @feature.setter
    def feature(self, feature):
        """
        Setter function for feature. Sets the private attribute _feature as well as the file_name
        and base_file_name.
        """
        self._feature = feature
        self.file_name = feature + ".py"
        self.base_file_name = feature + "base.py"
