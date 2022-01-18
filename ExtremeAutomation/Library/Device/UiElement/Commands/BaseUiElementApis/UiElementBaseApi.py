import os
import imp
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi


class UiElementBaseApi(DeviceApi):
    def __init__(self, device, agent):
        super(UiElementBaseApi, self).__init__(device)
        self.agent = agent

    def __get_data_file_path(self, feature):
        siesta_csv_path = os.path.join(os.environ["PYTHONPATH"].split(os.pathsep)[0], "ExtremeAutomation", "Library",
                                       "Device", "Ui_Elements", "Commands", "ApiDefinition", self.agent.capitalize())

        for dir_path, dir_names, file_names in os.walk(siesta_csv_path):
            for file_name in file_names:
                if file_name.lower() == feature.lower() + "data.py":
                    return os.path.join(dir_path, file_name)
        return None

    def get_data_file(self, feature):
        """
        This function retrieves the UI element data file based on the passed feature.
        """
        file_path = self.__get_data_file_path(feature)

        if file_path is not None:
            try:
                loaded_source = imp.load_source("data", file_path)
                loaded_class = loaded_source.create_instance()
                return loaded_class
            except OSError as e:
                self.logger.log_info(e)
                return None
        return None
