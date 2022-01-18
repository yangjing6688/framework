import os
import yaml
from ExtremeAutomation.Library.Logger.Logger import Logger
from ExtremeAutomation.Library.Utils.PathUtils import PathUtils


class CollectionUtils(object):
    @staticmethod
    def dict_to_string(source_dict, key_val_delimiter=":", entry_delimiter=","):
        """
        Arguments:
        source_dict       - The dictionary to convert to a string.
        key_val_delimiter - The delimiter to use between key and value pairs.
        entry_delimiter   - The dictionary item separator.

        Converts a dictionary to a string, using the supplied separators.
        """
        return entry_delimiter.join(("{0}" + key_val_delimiter + "{1}").format(k, v) for (k, v) in source_dict.items())

    @staticmethod
    def parse_yaml(file_path):
        """
        Arguments:
        file_path - This is a relative path to the file inside the ExtremeAutomation project.

        Parse the supplied YAML file for python usage.
        """
        with open(os.path.join(PathUtils.get_project_root(), file_path), "r") as stream:
            try:
                return yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                Logger().log_info(str(exc))
