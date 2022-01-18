import inspect
import os.path


class FileUtils(object):
    @staticmethod
    def write_str_to_file(file_name, message_body, binary=False):
        """Writes the message_body to the given file or creates the file if it does not exist."""
        mode = "wb" if binary else "w+"

        with open(file_name, mode) as text_file:
            text_file.write(message_body)

    @staticmethod
    def read_file_to_str(file_name):
        """Reads the file contents into a string and returns the string."""
        with open(file_name, "r") as myfile:
            message_body = myfile.read()
        return message_body

    @staticmethod
    def is_method_supported(class_method):
        """Checks if the class_method is supported."""
        return "log_unimplemented_method" not in (inspect.getsource(class_method))

    @staticmethod
    def file_exists(filename):
        """Checks if the file in question exists."""
        # my_file = Path(filename)
        # return my_file.exists()
        return os.path.isfile(filename)

    @staticmethod
    def delete_file(filename):
        """Deletes the given file."""
        if FileUtils.file_exists(filename):
            os.remove(filename)
