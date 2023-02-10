import ast
import os
from docstring_parser import parse


class parseXAPI:
    """
        This class will take the XAPI SDK and parse the API files and create the base classes for the framework
    """

    def __init__(self, directory):
        self.directory = directory
        self.python_types = ['int', 'string', 'bool']

    def show_info(self, functionNode, xapi_class_name):
        """

        :param functionNode:
        :return:
        """
        print("Function name:", functionNode.name)
        if functionNode.name != '__init__':
            doc_string = ast.get_docstring(functionNode)
            doc_string = '"""\n\t\t' + doc_string.replace('\n', '\n\t\t') + '\n\t\t"""\n'

            # Read in the function definition file
            with open('base_generated_function_definition.txt') as file:
                file_contents = file.read()
                file_contents = file_contents.replace('{FUNCTION_NAME}', 'xapi_base_' + functionNode.name)
                file_contents = file_contents.replace('{COMMMENT_HEADER}', doc_string )
                file_contents = file_contents.replace('{XAPI_API_CLASS}', xapi_class_name)
                file_contents = file_contents.replace('{XAPI_API_FUNCTION}', functionNode.name)
            return file_contents

            # parsed_doc_string = parse(doc_string)
            # print("Args:")
            # for param in parsed_doc_string.params:
            #     name = param.args[1]
            #     # Bug in the doc string to get the parameters
            #     if name in self.python_types and len(param.args) > 2:
            #         name = param.args[2]
            #     print("\tParameter name:", name)


    def parseFiles(self):
        """"
        """
        for filename in os.listdir(self.directory):
            file_and_directory = os.path.join(self.directory, filename)
            # checking if it is a file
            if os.path.isfile(file_and_directory):
                with open(file_and_directory) as file:
                    file_contents = file.read()
                    node = ast.parse(file_contents)
                classes = [n for n in node.body if isinstance(n, ast.ClassDef)]
                for class_ in classes:
                    print("Class name:", class_.name)
                    new_class_file = "base/XapiBase" + class_.name + ".py"
                    if os.path.exists(new_class_file):
                        os.remove(new_class_file)
                    class_file = open(new_class_file, "a")
                    class_file.write('\nfrom extauto.xiq.xapi.XapiBase import XapiBase\n\n\nclass XapiBase' + class_.name +'(XapiBase):\n\n\tdef __init__(self):\n\t\tsuper().__init__()\n\n')
                    methods = [n for n in class_.body if isinstance(n, ast.FunctionDef)]
                    for method in methods:
                        function_contents = self.show_info(method, class_.name)
                        if function_contents:
                            class_file.write(function_contents + "\n\n")
                    class_file.close()


if __name__ == "__main__":
    parser = parseXAPI('/automation/tests/ExtremeCloudIQ-SDK-Python/extremecloudiq/api/')
    parser.parseFiles()
