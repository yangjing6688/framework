import os
from ExtremeAutomation.Apis.ApiGeneration.Library.GenerationConstants import GenerationConstants


class PathUtils(object):
    @staticmethod
    def get_relative_path(path):
        """
        This function returns the provided path relative to the project root.

        For example if the project root was...
        /home/user/SQA_ROBOT_AUTOMATION

        and the provided path was...
        /home/user/SQA_ROBOT_AUTOMATION/ExtremeAutomation/path/to/some/file.txt

        The following would be returned...
        ExtremeAutomation/path/to/some/file.txt
        """
        relative_path = os.path.abspath(path).replace(os.path.abspath(PathUtils.get_project_root()), "")

        if relative_path.startswith(os.sep):
            return relative_path.replace(os.sep, "", 1)
        return relative_path

    @staticmethod
    def get_project_root():
        """This function returns the project's root folder location."""
        current_folder = os.path.dirname(__file__)
        last_folder = ""

        # todo: (jhall) - We should probably have a project constants file somewhere.
        # ExtremeAutomation should be stored there.
        root_folder = "ExtremeAutomation"

        while current_folder.split(os.sep)[-1] != root_folder and current_folder != last_folder:
            last_folder = os.path.abspath(current_folder)
            current_folder = os.path.dirname(os.path.abspath(current_folder))
        if last_folder == current_folder:
            raise Exception("Unable to determine project root.")
        else:
            project_root = current_folder.replace(root_folder, "")
        return project_root

    @staticmethod
    def get_api_root():
        """Returns the base path to the framework APIs."""
        return os.path.join(PathUtils.get_project_root(), "ExtremeAutomation", "Apis")

    @staticmethod
    def get_import_path(path):
        """
        This function returns the a relative import path. The path provided must be an absolute path.

        For example, if this following path was provided...
        /home/user/SQA_ROBOT_AUTOMATION/ExtremeAutomation/some/folder/SomeClass.py

        The following string would be returned...
        ExtremeAutomation.some.folder.SomeClass
        """
        import_path = PathUtils.get_relative_path(path).replace(os.sep, ".").replace(".py", "")
        if import_path[0] == ".":
            return import_path[1::]
        return import_path

    @staticmethod
    def get_csv_input_output_paths(dev_type, csv_type, agent_type):
        """Returns the paths for the input CSV files and the output API files."""
        project_root = PathUtils.get_project_root()
        base_dir = os.path.join(project_root, "ExtremeAutomation", "Apis")

        if dev_type == GenerationConstants.DEVICE_TYPE_NET_ELEM:
            if agent_type in [GenerationConstants.AGENT_TYPE_CLI,
                              GenerationConstants.AGENT_TYPE_REST,
                              GenerationConstants.AGENT_TYPE_SNMP]:
                inp_dir = os.path.join(base_dir, "NetworkElement", "ApiDefinition",
                                       csv_type.capitalize() + "ApiDefinition")
                out_dir = os.path.join(base_dir, "NetworkElement", "GeneratedApis", csv_type.capitalize() + "Apis")
            else:
                raise ValueError("Invalid agent type for network element.")
        elif dev_type == GenerationConstants.DEVICE_TYPE_END_SYS_ELEM:
            if agent_type in [GenerationConstants.AGENT_TYPE_CLI,
                              GenerationConstants.AGENT_TYPE_REST,
                              GenerationConstants.AGENT_TYPE_XMC_REST]:
                inp_dir = os.path.join(base_dir, "EndsystemElement", "ApiDefinition",
                                       csv_type.capitalize() + "ApiDefinition", agent_type.upper())
                out_dir = os.path.join(base_dir, "EndsystemElement", "GeneratedApis", csv_type.capitalize() + "Apis")
            elif agent_type == GenerationConstants.AGENT_TYPE_NORTHBOUND:
                inp_dir = os.path.join(base_dir, "EndsystemElement", "ApiDefinition", "CommandApiDefinition",
                                       agent_type.capitalize())
                out_dir = os.path.join(base_dir, "EndsystemElement", "GeneratedApis", csv_type.capitalize() + "Apis")
            else:
                raise ValueError("Invalid agent type for end sys.")
        elif dev_type == GenerationConstants.DEVICE_TYPE_UI_ELEM:
            if agent_type in [GenerationConstants.AGENT_TYPE_SIESTA,
                              GenerationConstants.AGENT_TYPE_SELENIUM]:
                if csv_type == GenerationConstants.API_TYPE_COMMAND:
                    inp_dir = os.path.join(base_dir, "UiElement", "ApiDefinition", agent_type.upper())
                    out_dir = os.path.join(base_dir, "UiElement", "GeneratedApis")
                else:
                    raise ValueError("Only command APIs exist for " + agent_type.capitalize() + ".")
            else:
                raise ValueError("Invalid agent type for ui element.")
        else:
            raise ValueError("Invalid device type.")

        return inp_dir, out_dir
